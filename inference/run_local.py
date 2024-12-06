import json
import os

import requests
from inference.libraries.infere import Infer
from dotenv import load_dotenv
inference_Global = None

def infer_run_local(prompt,
                    chatlog=None,
                    files=None, 
                    LLM="BramVanroy/fietje-2-chat", 
                    systemPrompt=None, 
                    generation_kwargs=None,
                    filename=None,
                    no_quantized=False):
  
  loaded = load_dotenv()
  if(loaded):
    print("Loaded .env file")
    domain = os.getenv("DOMAIN")
    api_key = os.getenv("API_KEY")
    if(domain is not None):
      if(api_key is not None):
        # fetch inference response from API
        print("Place request to API")
      
        prompt = [
          {
            "role": "system",
            "content": systemPrompt
          },
          {
            "role": "user",
            "content": f"prompt: {prompt} \n\n\nrelevant files: {files}"
          },
        ]
        receive = requests.post(domain, 
        json = {'prompt': json.dumps(prompt)}, 
        headers={'Authorization':api_key})
        output = receive.json()['result']['output']
        print(f"API response: {output}")
        return output
  
  global inference_Global
  gpuBanlist = ["PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-4bit-smashed","PrunaAI/BramVanroy-GEITje-7B-ultra-bnb-8bit-smashed"]
  
  if inference_Global is None or inference_Global.llm != LLM:
    if LLM in gpuBanlist:
      inference_Global = Infer(LLM, exclude_device=True, no_quantized=no_quantized)
    else:
      inference_Global = Infer(LLM, filename=filename, no_quantized=no_quantized)
  
  return inference_Global.predict(prompt, chatlog, files, systemPrompt, generation_kwargs)

def infer_factory(LLM="BramVanroy/fietje-2-chat"):
  return Infer(LLM)