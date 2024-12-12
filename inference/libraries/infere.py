import json
import os
import requests
import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from huggingface_hub import snapshot_download

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class Infer:
    system_prompt = """Je bent een vriendelijke chatbot genaamd Learning Lion. Je wilt altijd graag vragen beantwoorden en blijft altijd vriendelijk. Alle informatie die jij vertelt komt uit de bestanden die zijn bijgevoegd, mochten de bestanden niet bestaan of onvoldoende informatie bevatten dan zeg je 'ik weet het niet' of 'ik kan je niet helpen'."""

    def __init__(self, model_name_or_path, filename="model.gguf", device_map="auto", no_quantized=False):
        self.model_name_or_path = model_name_or_path
        self.filename = filename
        self.device_map = device_map
        self.no_quantized = no_quantized
        self.is_quantized = False
        self.tokenizer = None
        self.model = None
        self.download_dest = "./temp_model"
        self.load_model()

    def load_model(self):
        """
        Load a quantized or non-quantized model and its tokenizer.
        """
        if "GGUF" in self.model_name_or_path:
            raise ValueError("GGUF models are not supported in this implementation.")
        
        # Ensure the model is downloaded or accessible locally
        local_path = self._ensure_model_downloaded()
        self.is_quantized = self._detect_quantization()

        if self.is_quantized and not self.no_quantized:
            # Configure BitsAndBytes for quantization
            bnb_config = BitsAndBytesConfig(
                load_in_8bit=True,
                llm_int8_threshold=6.0,
                llm_int8_enable_fp32_cpu_offload=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                local_path,
                quantization_config=bnb_config,
                device_map=self.device_map
            )
        else:
            self.model = AutoModelForCausalLM.from_pretrained(
                local_path,
                device_map=self.device_map
            )

        self.tokenizer = AutoTokenizer.from_pretrained(local_path)
        self.model.resize_token_embeddings(len(self.tokenizer))
        print("Model and tokenizer successfully loaded.")

    def _ensure_model_downloaded(self):
        """
        Ensure the model is downloaded or accessible locally.
        """
        if os.path.exists(self.model_name_or_path):
            return self.model_name_or_path

        safe_model_name = self.model_name_or_path.replace("/", "--")
        local_model_dir = f"./temp_model/models--{safe_model_name}"

        if os.path.exists(local_model_dir):
            print(f"Model already exists locally: {local_model_dir}")
            return local_model_dir

        print(f"Downloading model: {self.model_name_or_path}")
        return snapshot_download(self.model_name_or_path, cache_dir="./temp_model")

    def _detect_quantization(self):
        """
        Detect whether the model is quantized based on specific files or metadata.
        """
        quantized_file = os.path.join(self.model_name_or_path, "quantized_config.json")
        return os.path.exists(quantized_file)

    def parse_chatlog(self, chatlog):
        """
        Parse the chatlog string into a structured conversation format.
        """
        parsed_conversation = []
        entries = chatlog.split("map[")
        for entry in entries[1:]:
            from_user = "fromUser:true" in entry
            message_start = entry.find("message:") + len("message:")
            message_end = entry.find(" username:")
            message = entry[message_start:message_end].strip()
            role = "user" if from_user else "assistant"
            parsed_conversation.append({"role": role, "content": message})
        return parsed_conversation

    def _construct_conversation(self, prompt, chatlog=None, files=None, system_prompt=None):
        """
        Construct the conversation in the required format.
        """
        system_prompt = system_prompt or self.system_prompt
        conversation = [{"role": "system", "content": system_prompt}]

        if chatlog:
            conversation.extend(self.parse_chatlog(chatlog))

        conversation.append({"role": "user", "content": prompt})

        if files:
            conversation.append({"role": "system", "content": f"Relevante bestanden:\n{files}"})

        return "\n".join(f"{entry['role'].capitalize()}: {entry['content']}" for entry in conversation)

    def predict(self, prompt, chatlog=None, files=None, system_prompt=None, generation_kwargs=None):
        """
        Predict a response using the loaded model.
        """
        if not self.model or not self.tokenizer:
            raise ValueError("Model and tokenizer must be loaded first.")

        conversation_text = self._construct_conversation(prompt, chatlog, files, system_prompt)
        pipeline_instance = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

        # Default generation settings
        base_generate_kwargs = {
            "do_sample": True,
            "temperature": 1.0,
            "max_new_tokens": 1000
        }
        final_generate_kwargs = {**base_generate_kwargs, **(generation_kwargs or {})}

        response = pipeline_instance(conversation_text, **final_generate_kwargs)
        return response[0]["generated_text"]