
from DataFetcher.libraries.data_classes.range_enum import Range
from querier.libraries import database, query
from querier.libraries.embedding import Embedding
from querier.libraries.fetchingType import FetchingType

def run_local_query_stores(prompt,subject=None,range=Range.Tiny):
  print("Querying stores")
  documents = []
  embed = Embedding()
  data = database.Database(embed)
  data.setup_database(range=range)
  querier = query.Query()
  querier.setup_querier(data)
  data.close_database_connection()
  answer_documents = querier.query(prompt, type=FetchingType.Answers, range=range)
  documents.extend(answer_documents)
  if subject is not None:
    subject_documents = querier.query(subject,type=FetchingType.Subjects, range=range)
    documents.extend(querier.combine_arrays_no_overlap(subject_documents, answer_documents))
  return documents
  
def getDocumentBlobFromDatabase(UUID: str, range=Range.Tiny):
    # Initialize the embedding and database objects
    embed = Embedding()
    data = database.Database(embed)
    
    # Get the database connection based on the specified range
    db_connection = data.get_database_connection(range=range)
    
    # Open a cursor without using 'with'
    cursor = db_connection.cursor()
    cursor.execute("SELECT document FROM documents WHERE UUID = ?", (UUID,))
    item = cursor.fetchone()
    # Close the cursor and database connection
    data.close_database_connection()
    
    # Return the document if found, or None if not
    return item[0] if item else None