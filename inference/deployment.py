import os
from infere import Infer


class Deployment:
  inference = None
  def __init__ (self, base_directory=None, context=None):
    modelname = os.getenv("MODEL_NAME", "BramVanroy/fietje-2-chat")
    self.inference = Infer(modelname)
    print("Deployment class initialized")
    
  def request(self, data, context):
    if "prompt" not in data:
      print("No prompt provided")
      return {"error": "No prompt provided"}
    # chatlog = None
    # if "chatlog" in data:
    #   if "chatlog" in data is not None:
    #     chatlog = data["chatlog"]
    # files = None
    # if "files" in data:
    #   if "file" in data is not None:
    #     files = data["file"]
    return {"output":self.inference.predict(data["prompt"])}