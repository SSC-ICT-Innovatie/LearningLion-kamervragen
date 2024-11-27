import torch
from inference.libraries.infere import Infer

inference_Global = None

def infer_run_local(prompt,
                    chatlog=None,
                    files=None, 
                    LLM="BramVanroy/fietje-2-chat", 
                    systemPrompt=None, 
                    generation_kwargs=None):
  global inference_Global
  if inference_Global is None:
    inference_Global = Infer(LLM)
  # Models that dont require a GPU or are needed to exclude the device tag
  gpuBanlist = ["PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-4bit-smashed","PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-8bit-smashed"]
  
  device = "cpu"
  if not torch.cuda.is_available():
    device = "cpu"
  if torch.backends.mps.is_available():
    device = "mps"
  if torch.cuda.is_available():
    device = "cuda"
    
  if LLM not in gpuBanlist:
    generation_kwargs = generation_kwargs or {}
    generation_kwargs["device"] = device
  
  return inference_Global.predict(prompt, chatlog, files, systemPrompt, generation_kwargs)

def infer_factory(LLM="BramVanroy/fietje-2-chat"):
  return Infer(LLM)