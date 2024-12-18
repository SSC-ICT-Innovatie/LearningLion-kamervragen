import os
import sys
import datetime as dt
from loguru import logger
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings, AzureOpenAIEmbeddings
import torch
import weaviate

# local imports
import settings

def create_vectordb_name(content_folder_name, chunk_size=None, chunk_overlap=None, embeddings_type=None, embeddings_model=None, vecdb_type=None, added_context=None, splitting_method=None):
    # FORMAT OF VECTORDB NAME: VECDB_TYPE_chunk_size_chunk_overlap_EMBEDDINGS_PROVIDER_EMBEDDINGS_MODEL_ADDED_CONTEXT_EMBEDDINGSTYPE_VECDB_TYPE_SPLITTING_METHOD
    templateVectorname = "VECDBTYPE_chunksize_chunkoverlap_EMBEDDINGS_PROVIDER_EMBEDDINGS_MODEL_ADDED_CONTEXT_EMBEDDINGSTYPE_VECDB_TYPE_SPLITTING_METHOD"
    content_folder_path = os.path.join(settings.DOC_DIR, content_folder_name)
    
    templateVectorname = templateVectorname.replace("VECDBTYPE", settings.VECDB_TYPE)
    if chunk_size:
        templateVectorname = templateVectorname.replace("chunksize", str(chunk_size))
    else:
        templateVectorname = templateVectorname.replace("chunksize", str(settings.CHUNK_SIZE))
    templateVectorname = templateVectorname.replace("chunkoverlap", str(chunk_overlap))
    templateVectorname = templateVectorname.replace("EMBEDDINGS_PROVIDER", settings.EMBEDDINGS_PROVIDER)
    if embeddings_model is None:
        embeddings_model = settings.EMBEDDINGS_MODEL
    embeddings_model = embeddings_model.replace("/", "-")
    templateVectorname = templateVectorname.replace("EMBEDDINGS_MODEL", str(embeddings_model))
    templateVectorname = templateVectorname.replace("ADDED_CONTEXT", str(added_context))
    templateVectorname = templateVectorname.replace("EMBEDDINGSTYPE", str(embeddings_type))
    if splitting_method is None:
        splitting_method = "None"
    else:
        splitting_method = str(splitting_method)
    splitting_method = splitting_method.replace(".", "-")
    templateVectorname = templateVectorname.replace("SPLITTING_METHOD", str(splitting_method))
    vectordb_folder_path = os.path.join(settings.VECDB_DIR, content_folder_name) + templateVectorname 
    
    return content_folder_path, vectordb_folder_path


def exit_program():
    print("Exiting the program...")
    sys.exit(0)


def getattr_or_default(obj, attr, default=None):
    """
    Get an attribute from an object, returning a default value if the attribute
    is not found or its value is None.
    """
    value = getattr(obj, attr, default)
    return value if value is not None else default


def get_chroma_vector_store(collection_name, embeddings, vectordb_folder) -> Chroma:
    
    if settings.VECDB_TYPE == "chromadb":
        vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory=vectordb_folder,
            collection_metadata={"hnsw:space": "cosine"}
        )
    # if settings.VECDB_TYPE == "weaviate":
        # vector_store = Weaviate(
        #     collection_name=collection_name,
        #     embedding_function=embeddings,
        #     persist_directory=vectordb_folder,
        #     collection_metadata={"hnsw:space": "cosine"}
    return vector_store


def get_settings_as_dictionary(file_name):
    # Initialize an empty dictionary to store the variables and their values
    variables_dict = {}
    # Open and read the file
    with open(file=file_name, mode='r', encoding="utf-8") as file:
        lines = file.readlines()
    start_reading = False
    # Process each line in the file
    for line in lines:
        # start reading below the line with # #########
        if line.startswith("# #########"):
            start_reading = True
        # ignore comment lines
        if start_reading and not line.startswith("#"):
            # Remove leading and trailing whitespace and split the line by '='
            parts = line.strip().split('=')
            # Check if the line can be split into two parts
            if len(parts) == 2:
                # Extract the variable name and value
                variable_name = parts[0].strip()
                variable_value = parts[1].strip()
                # Use exec() to assign the value to the variable name
                exec(f'{variable_name} = {variable_value}')
                # Add the variable and its value to the dictionary
                variables_dict[variable_name] = eval(variable_name)
    return variables_dict


def getEmbeddings(embeddings_provider, embeddings_model, local_api_url, azureopenai_api_version):
    # determine embeddings model
    if embeddings_provider == "openai":
        embeddings = OpenAIEmbeddings(model=embeddings_model, client=None)
        logger.info("Loaded openai embeddings")
    elif embeddings_provider == "huggingface":
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model)
    elif embeddings_provider == "local_embeddings":
        model_name = embeddings_model
        if torch.backends.mps.is_available():
            model_kwargs = {'device': 'mps'}
        elif torch.cuda.is_available():
            model_kwargs = {'device': 'cuda'}
        else:
            model_kwargs = {'device': 'cpu'}
        model_kwargs["trust_remote_code"] = True
        encode_kwargs = {'normalize_embeddings': False}
        embeddings = HuggingFaceEmbeddings(
            
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs )
        logger.info("Loaded local embeddings: " + embeddings_model)
    elif embeddings_provider == "azureopenai":
        logger.info("Retrieve " + embeddings_model)
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=embeddings_model,
            openai_api_version=azureopenai_api_version,
            azure_endpoint=local_api_url,
            )
        logger.info("Loaded Azure OpenAI embeddings")
    return embeddings


def get_timestamp():
    return str(dt.datetime.now())


def get_content_folder_name(docdiroveride = None) -> str:
    '''Select a folder from the DOC_DIR to work with.'''
    if docdiroveride is None:
        path = settings.DOC_DIR
    elif docdiroveride is not None:
        path = docdiroveride
    content_folder_names = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    print(f"Available folders in {path}:")
    for idx, folder in enumerate(content_folder_names, start=1):
        print(f"{idx}. {folder}")
    
    selection = int(input("Select a folder by number: ")) - 1
    return content_folder_names[selection]
