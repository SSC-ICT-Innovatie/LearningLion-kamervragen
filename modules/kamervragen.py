from flask import jsonify
from DataFetcher.libraries.data_classes.range_enum import Range
from DataFetcher.run_local import run_local_datafetcher
from inference.run_local import infer_run_local
from ingester.libraries.database import Database
from ingester.libraries.embedding import Embedding
from ingester.run_local import run_local_ingest_stores
from querier.run_local import run_local_query_stores


class KamerVragen:
  def initialize(app, data):
    try:
      range = Range.Tiny
      if "range" in data:
          if data["range"] not in Range.__members__:
              return jsonify({"error": "Invalid range"})
          range = Range[data["range"]]
      run_local_datafetcher(range=range)
      run_local_ingest_stores()
      return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)})
      
  def inference(app, data, defaultRange=Range.Tiny, model="BramVanroy/fietje-2-chat", systemPrompt=None): 
    files = []
    _range = defaultRange
    fetchedFiles = []
    if "range" in data:
      if data["range"] not in Range.__members__:
          return jsonify({"error": "Invalid range"})
      _range = Range[data["range"]]
      app.logger.info(f"Using range: {_range.name}")
    if "files" in data:
      embeddings = Embedding()
      database = Database(embed=embeddings, range=_range)
      files = data['files']
      print(f"Files: {files}")
      for file in files:
          print(f"File: {file}")
          print(f"uuid {file.get('uuid')}")
          database.get_database_connection()
          # get answer from database
          fetchedData = database.getQuestion(file.get('uuid'), file.get('questionNumber'))
          print(f"for file: {file.get('uuid')} question number: {file.get('questionNumber')} fetched data: {fetchedData}")
          fetchedFiles.append(fetchedData)
          print(f"for file: {file.get('uuid')} question number: {file.get('questionNumber')} fetched data: {fetchedData}")
      print(f"Question and answer: {fetchedFiles}")
      app.logger.info(f"Question and answer: {fetchedFiles}")
    app.logger.info(f"Prompt: {data['prompt']}")
    AIresponse = infer_run_local(data["prompt"], files=fetchedFiles, LLM=model, systemPrompt=systemPrompt)
    app.logger.info(f"AI response: {AIresponse}")
    return jsonify({
      "prompt": data["prompt"],
      "output": AIresponse
    })
    
  def query(app, data, defaultRange=Range.Tiny):
    """
    Query the stores for the given prompt
    Query is promised
    """
    _range = defaultRange
    if("range" in data):
      if data["range"] not in Range.__members__:
          return jsonify({"error": "Invalid range"})
      _range = Range[data["range"]]
    app.logger.info("Using range: {range.name}")
    documents = run_local_query_stores(data["query"], range=_range)
    app.logger.info(f"Documents: {documents}")
    return jsonify({
        "query": data["query"],
        "documents": documents
    })
