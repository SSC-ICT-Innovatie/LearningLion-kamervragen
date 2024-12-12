from enum import Enum
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, make_response, request

from DataFetcher.libraries.data_classes.range_enum import Range
from modules.kamervragen import KamerVragenModule
from querier.libraries.fetchingType import FetchingType
from querier.run_local import getDocumentBlobFromDatabase, run_local_query_stores
from inference.run_local import infer_run_local
from flask_cors import CORS, cross_origin

class RequestFilter(logging.Filter):
    def filter(self, record):
        record.ip = request.remote_addr if request else "No-IP"
        return True



range = Range.Tiny
app = Flask(__name__)

# if not app.debug:  # Enable logging only in production mode
# Create a file handler
file_handler = RotatingFileHandler(
    'app.log', maxBytes=1024 * 1024 * 10, backupCount=5
)  # Log file size = 10MB, keep 5 backups

# Set logging level and format
file_handler.setLevel(logging.INFO)  # Change to logging.DEBUG for debug info
formatter = logging.Formatter(
    '%(asctime)s - %(ip)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
file_handler.addFilter(RequestFilter())
# Add handler to Flask app logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

# Log that logging has started
app.logger.info('Logging is set up.')


CORS(app, resources={r"/*": {"origins": "*"}}, 
     allow_headers=["Content-Type", "Authorization", "ngrok-skip-browser-warning"])
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization, ngrok-skip-browser-warning")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
    return response

defaultLLMModel = "llama3.2:3b"

@app.route('/')
def index():
    app.logger.info('Hello, World!')
    return {"Hello": "World"}

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/ping')
def ping():
    return {"pong"}

class Specialty(Enum):
    KamerVragen = 1
    
LLMModels = [
    "Open-Orca/Mistral-7B-OpenOrca",
    "BramVanroy/fietje-2-chat",
    "BramVanroy/GEITje-7B-ultra",
    "PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-4bit-smashed",
    "PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-8bit-smashed",
    "BramVanroy/GEITje-7B-ultra-GGUF,geitje-7b-ultra-q5_k_m.gguf",
    "BramVanroy/GEITje-7B-ultra-GGUF,geitje-7b-ultra-f16.gguf",
]

datascopes = [
    "Tiny",
    "Medium",
    "Large"

]
    
def doesSpecialtyExist(name: str) -> bool:
    return name in Specialty.__members__

@app.route('/specialties', methods=['GET'])

def specialties():
    return jsonify([specialty.name for specialty in Specialty])

def doesLLMModelExist(name: str) -> bool:
    return name in LLMModels

@app.route('/llmmodels', methods=['GET'])
def llmmodels():
    return jsonify(LLMModels)

@app.route('/datascopes', methods=['GET'])
def GetDatascopes():
    return jsonify(datascopes)

@app.route('/init', methods=['POST'])

def init():
    if request.is_json is False:
        return jsonify({"error": "Invalid JSON"})
    data = request.get_json()
    if "specialty" not in data:
        return jsonify({"error": "No specialty provided"})
    if doesSpecialtyExist(data["specialty"]) is False:
        return jsonify({"error": "Invalid specialty"})
    if data["specialty"] == "KamerVragen":
        return KamerVragenModule.initialize(app, data)
    return False

@app.route('/prompt', methods=['POST'])

def prompt():
    # Access the JSON data sent in the request body
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No data provided"})
    if "prompt" not in data:
        return jsonify({"error": "No prompt provided"})
    if "type" not in data:
        return jsonify({"error": "No type provided"})
    type = data["type"]
    if type in FetchingType.__members__:
        return jsonify({"error": "Invalid type"})
    

    documents = run_local_query_stores(data["prompt"], type=type)
    print(f"Got {len(documents)} documents")
    print(f"Documents: {documents[:5]}")
    AIresponse = infer_run_local(data["prompt"], files=documents)
    print(f"AI response: {AIresponse}")
    return jsonify({
        "prompt": data["prompt"],
        "documents": documents,
        "output": AIresponse
    })
@app.route('/document', methods=['GET'])

def document():
    getParams = request.args
    uuid = getParams.get('uuid')  # Fetch UUID safely
    if not uuid:
        return "UUID parameter is missing", 400  # Bad request if UUID is missing
    pdf_data = getDocumentBlobFromDatabase(uuid, range=Range.Large)
    if pdf_data is None:
        return "Document not found", 404  # Not found if UUID does not exist

    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename="document.pdf"'
    
    return response

@app.route('/query', methods=['POST'])

def query():
    data = request.get_json()
    # log ip address
    app.logger.info(f"IP address: {request.remote_addr}")
    app.logger.info(f"Data recived: {data}")
    _range = range
    if data is None:
        app.logger.error("No data provided")
        return jsonify({"error": "No data provided"})
    if "query" not in data:
        app.logger.error("No query provided")
        return jsonify({"error": "No query provided"})
    if "specialty" not in data:
        app.logger.error("No specialty provided")
        return jsonify({"error": "No specialty provided"})
    if doesSpecialtyExist(data["specialty"]) is False:
        return jsonify({"error": "Invalid specialty"})
    if("scope" in data):
        print(f"Range: {data['scope']}")
        if data["scope"] not in Range.__members__:
            return jsonify({"error": "Invalid range"})
        _range = Range[data["scope"]]
        app.logger.info(f"Using range: {_range.name}")
    if data["specialty"] == "KamerVragen":
        return KamerVragenModule.query(app, data, range=_range)
    
@app.route('/llm', methods=['POST'])

def infer():
    model = defaultLLMModel
    data = request.get_json()
    app.logger.info(f"IP address: {request.remote_addr}")
    app.logger.info(f"Data recived: {data}")
    if data is None:
        app.logger.error("No data provided")
        return jsonify({"error": "No data provided"})
    if "prompt" not in data:
        app.logger.error("No prompt provided")
        return jsonify({"error": "No prompt provided"})
    if "specialty" not in data:
        app.logger.error("No specialty provided")
        return jsonify({"error": "No specialty provided"})
    if doesSpecialtyExist(data["specialty"]) is False:
        return jsonify({"error": "Invalid specialty"})
    specialty = data["specialty"]
    # Always use the default model for now
    # if "model" in data:
    #     if doesLLMModelExist(data["model"]):
    #         model = data["model"]
    #     else:
    #         print(f"Invalid model: {data['model']}")
    #         return jsonify({"error": "Invalid model"})
    systemPrompt = None
    if "systemPrompt" in data:
        systemPrompt = data["systemPrompt"]
    if specialty == "KamerVragen":
        return KamerVragenModule.inference(app, data, model=model, systemPrompt=systemPrompt)
    else:
        return {
            "prompt": data["prompt"],
            "output": infer_run_local(data["prompt"], LLM=model)
        }
        