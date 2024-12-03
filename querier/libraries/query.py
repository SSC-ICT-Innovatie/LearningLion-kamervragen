from langchain.retrievers import EnsembleRetriever

from querier.libraries import database
from querier.libraries.embedding import Embedding
# import database
from enum import Enum

class Type(Enum):
    all:1
    answers:2
    subjects:3
class Query:
    ensemble_retriever = None

    def __init__(self):
        print("Query class initialized")

    def setup_querier(self, database: database.Database):
        print("Setting up ensemble retriever")

        # Retrieve the Chroma vector store
        chroma_vectorstore = database.get_vector_store()
        if chroma_vectorstore is None:
            raise ValueError("Chroma vector store is not set in the database")
        chroma_retriever = chroma_vectorstore.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 5,"score_threshold": 0.2})
        # Retrieve the BM25 retriever
        bm25_retriever = database.get_bm25B_retriever()
        if bm25_retriever is None:
            raise ValueError("BM25 retriever is not set in the database")

        # Create the ensemble retriever
        self.ensemble_retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, chroma_retriever],
            weights=[0.0, 1.0], # TODO: tune these weights,
        )

        print("Ensemble retriever set up")
            
    def query(self, query_text, type=Type.all):
        embed = Embedding()
        data = database.Database(embed)
        combined_results = []
        print(f"Querying: {query_text}")
        print(f"Type: {type.name}")
        if(type == Type.all or type == Type.subjects):
            bm25A = data.get_bm25A_retriever()
            results = bm25A.invoke(query_text)
            combined_results.extend(results)
        
        if(type == Type.all or type == Type.answers):
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
                cursor.execute("SELECT answer FROM questions WHERE UUID = ?", (result.metadata['UUID'],))
                item = cursor.fetchone()
                print(f"Item: {item}")
                # Close the cursor and database connection
                # Assuming fields like `text` and `metadata` exist in `Document`
                json_ready_results.append({
                    "text": getattr(result, "page_content", ""),  # Replace with the actual text attribute
                    "metadata": getattr(result, "metadata", {}),  # Replace with the actual metadata attribute
                    "answer": item[0] if item else None
                })
            data.close_database_connection()
            combined_results.extend(json_ready_results)
            print(f"Got {len(combined_results)} results")
            return combined_results 

    def get_ensemble_retriever(self):
        return self.ensemble_retriever