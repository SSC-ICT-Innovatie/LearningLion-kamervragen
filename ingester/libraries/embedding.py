from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import torch

class Embedding:
  embeddings = None
  def __init__(self):
      self.setup_embeddings()
      print("Embedding class initialized")

  def get_embeddings(self):
    """
        haal het embeddings model op
    """
    if self.embeddings is None:
       return self.setup_embeddings()
    return self.embeddings
    
  def setup_embeddings(self,localModel=False, modelname="textgain/allnli-GroNLP-bert-base-dutch-cased"):
    """
        maak het embeddings model klaar
    """
    print("Setting up embeddings")
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    model_name = modelname
    if torch.backends.mps.is_available():
        model_kwargs = {'device': 'mps'}
    elif torch.cuda.is_available():
        model_kwargs = {'device': 'cuda'}
    else:
        model_kwargs = {'device': 'cpu'}
    model_kwargs["trust_remote_code"] = True
    encode_kwargs = {'normalize_embeddings': False,
                     'batch_size': 16}
    
    if(localModel):
        self.embeddings = SentenceTransformer(model_name)

    else:
        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
    print("Embeddings set up")
    return self.embeddings
