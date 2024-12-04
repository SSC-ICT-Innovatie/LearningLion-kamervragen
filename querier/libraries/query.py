from langchain.retrievers import EnsembleRetriever

from DataFetcher.libraries.data_classes.range_enum import Range
from querier.libraries import database
from querier.libraries.embedding import Embedding
from querier.libraries.fetchingType import FetchingType
# import database
class Query:
    ensemble_retriever = None

    def __init__(self):
        print("Query class initialized")

    def setup_querier(self, database: database.Database, range=Range.Tiny):
        print("Setting up ensemble retriever")

        # Retrieve the Chroma vector store
        chroma_vectorstore = database.get_vector_store(range=range)
        if chroma_vectorstore is None:
            raise ValueError("Chroma vector store is not set in the database")
        chroma_retriever = chroma_vectorstore.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 5,"score_threshold": 0.2})
        # Retrieve the BM25 retriever
        bm25_retriever = database.get_bm25B_retriever(range=range)
        if bm25_retriever is None:
            raise ValueError("BM25 retriever is not set in the database")
        # Create the ensemble retriever
        self.ensemble_retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, chroma_retriever],
            weights=[0.5, 0.5], # TODO: tune these weights,
        )

        print("Ensemble retriever set up")
        
    def get_uuid(self, item):
        """Helper function to extract the UUID from either structure."""
        if isinstance(item, dict):
            return item['metadata']['UUID']
        elif hasattr(item, 'metadata') and isinstance(item.metadata, dict):
            return item.metadata['UUID']
        return None  # Return None if the structure is unexpected
    def combine_arrays_no_overlap(self, a,b):
        arr = []
        b_uuids = {self.get_uuid(item) for item in b if self.get_uuid(item) is not None}
        for i in a:
            uuid = self.get_uuid(i)
            if uuid and uuid not in b_uuids:
                arr.append(i)
        arr.extend(b)
        return arr  
    def query_Answers(self, query_text, data: database.Database):
        results = self.ensemble_retriever.invoke(query_text)
        for doc in results:
            score = doc.metadata.get('score', None)
            print(f"Document: {doc.page_content}, Score: {score}")
        if results is None:
            return []
        # Get the database connection based on the specified range
        db_connection = data.get_database_connection()
        # Convert each result to a JSON-serializable format
        json_ready_results = []
        for result in results:
            # Open a cursor without using 'with'
            cursor = db_connection.cursor()
            print(f"result: {result}")
            print(f"metadata: {result.metadata}")
            print(f"UUID: {result.metadata['UUID']}")
            cursor.execute("SELECT answer FROM questions WHERE UUID = ? AND QUESTIONNUMBER = ?", (result.metadata['UUID'],result.metadata['question_number']))
            item = cursor.fetchone()
            print(f"Item: {item}")
            # Close the cursor and database connection
            # Assuming fields like `text` and `metadata` exist in `Document`
            json_ready_results.append({
                "text": getattr(result, "page_content", ""),
                "metadata": getattr(result, "metadata", {}),
                "answer": item[0] if item else None
            })
        data.close_database_connection()
        # Filter combined results for no duplicates ids
        return json_ready_results
    def query_Subjects(self, query_text, data: database.Database, range=Range.Tiny):
        bm25A = data.get_bm25A_retriever(range=range)
        if bm25A is None:
            raise ValueError("BM25A retriever is not set in the database")
        AResults = bm25A.invoke(query_text)
        bm25C = data.get_bm25C_retriever(range=range)
        if bm25C is None:
            raise ValueError("BM25C retriever is not set in the database")
        CResults = bm25C.invoke(query_text)
        combined_results = self.combine_arrays_no_overlap(AResults, CResults)
        json_ready_results = []
        for result in combined_results:
            json_ready_results.append({
                "text": getattr(result, "page_content", ""),
                "metadata": getattr(result, "metadata", {}),
            })
        return json_ready_results
        
    def query(self, query_text, type=FetchingType.All, range=Range.Tiny):
        embed = Embedding()
        data = database.Database(embed)
        combined_results = []
        print(f"Querying: {query_text}")
        print(f"Type: {type.name}")
        if(type == FetchingType.All or type == FetchingType.Subjects):
            combined_results.extend(self.query_Subjects(query_text, data, range=range))
        if(type == FetchingType.All or type == FetchingType.Answers):
            answerResults = self.query_Answers(query_text, data)
            combined_results = self.combine_arrays_no_overlap(combined_results, answerResults)
            
        print(f"Got {len(combined_results)} results")
        return combined_results

    def get_ensemble_retriever(self):
        return self.ensemble_retriever