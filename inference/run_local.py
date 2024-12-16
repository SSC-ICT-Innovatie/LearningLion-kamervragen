import json
import os
from dotenv import load_dotenv
import requests
from inference.libraries.infere import Infer
import ollama
import threading
import queue

inference_Global = None

def ollama_infer_run_local(messages, model='llama2'):
    """
    Het uitvoeren van een Ollama inferentie lokaal
    
    :param messages: de berichten die moeten worden gegeven aan Ollama
    :param model: het model dat moet worden gebruikt
    """
    try:
        print(f"Recived: {messages}")
        response = ollama.chat(model=model, messages=messages)
        print(f"Ollama Response: {response['message']['content']}")
        return response['message']['content']
    except Exception as e:
        print(f"Error during Ollama inference: {e}")
        return None

def infer_run_local(prompt,
                    chatlog=None,
                    files=None,
                    LLM="BramVanroy/fietje-2-chat",
                    systemPrompt=None,
                    generation_kwargs=None,
                    filename=None,
                    no_quantized=False,
                    noOllama=False):
    
    """
    het uitvoeren van een inferentie lokaal
    
    Als er een API in de .env is ingesteld, wordt deze ook gebruikt voor inferentie
    
    :param prompt: de prompt die moet worden gegeven aan het model
    :param chatlog: het chatlog dat moet worden gegeven aan het model
    :param files: de bestanden die moeten worden gegeven aan het model
    :param LLM: het model dat moet worden gebruikt
    :param systemPrompt: het systeem prompt dat moet worden gegeven aan het model
    :param generation_kwargs: de generatie argumenten die moeten worden gegeven aan het model
    :param filename: de naam van het bestand dat moet worden gegeven aan het model
    :param no_quantized: of het model niet moet worden gekwantiseerd
    :param noOllama: of Ollama niet moet worden gebruikt
    """
    # Load environment variables
    load_dotenv()
    domain = os.getenv("DOMAIN")
    api_key = os.getenv("API_KEY")
    
    result_queue = queue.Queue()

    # Function to perform API inference
    def api_infer():
        if domain and api_key:
            try:
                print("Starting API inference...")
                api_prompt = [
                    {"role": "system", "content": systemPrompt},
                    {"role": "user", "content": f"prompt: {prompt} \n\n\nrelevant files: {files}"}
                ]
                response = requests.post(
                    f"{domain}?timeout=3600",
                    json={'prompt': json.dumps(api_prompt)},
                    headers={'Authorization': api_key}
                )
                output = response.json().get('result', {}).get('output', None)
                print(f"API Response: {output}")
                print(f"Response: {response}")
                result_queue.put(output)
            except Exception as e:
                print(f"Error during API inference: {e}")

    # Function to perform Ollama inference
    def ollama_infer():
        try:
            print("Starting Ollama inference...")
            ollama_prompt = [
                {"role": "system", "content": systemPrompt},
                {"role": "user", "content": prompt}
            ]
            output = ollama_infer_run_local(ollama_prompt, model=LLM)
            result_queue.put(output)
        except Exception as e:
            print(f"Error during Ollama inference: {e}")

    # Start threads for API and Ollama
    if domain and api_key:
        threading.Thread(target=api_infer, daemon=True).start()
    if noOllama is False:
      threading.Thread(target=ollama_infer, daemon=True).start()

    # Wait for the first response
    try:
        result = result_queue.get()  # Adjust timeout as needed
        return result
    except queue.Empty:
        return "No response received in time."

def infer_factory(LLM="BramVanroy/fietje-2-chat"):
    return Infer(LLM)