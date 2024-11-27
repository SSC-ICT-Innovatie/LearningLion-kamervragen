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
  gpuBanlist = ["PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-4bit-smashed","PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-8bit-smashed"]
  
  if inference_Global is None or inference_Global.llm != LLM:
    if LLM in gpuBanlist:
      inference_Global = Infer(LLM, exclude_device=True)
    else:
      inference_Global = Infer(LLM)
  
  return inference_Global.predict(prompt, chatlog, files, systemPrompt, generation_kwargs)

def infer_factory(LLM="BramVanroy/fietje-2-chat"):
  return Infer(LLM)