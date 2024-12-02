import os
import requests
import torch
from transformers import pipeline
from transformers import BitsAndBytesConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from llama_cpp import Llama
from huggingface_hub import snapshot_download

os.environ["TOKENIZERS_PARALLELISM"] = "false"

class Infer:
	systemPrompt = """Je bent een vriendelijke chatbot genaamd Learning Lion. Je wilt altijd graag vragen beantwoorden en blijft altijd vriendelijk. Alle informatie die jij verteld komt uit de bestanden die zijn bijgevoegd, mochten de bestanden niet bestaan of onvoldoende informatie bevatten dan zeg je 'ik weet het niet' of 'ik kan je niet helpen'."""
	llm = None
	downloadDest="./temp_model"
	def __init__(self, model_name_or_path, filename="model.guff", exclude_device=False,device_map="auto", no_quantized=False, args=None):
		self.model_name_or_path = model_name_or_path
		self.device_map = device_map
		self.is_quantized = False
		self.tokenizer = None
		self.model = None
		self.filename = filename
		self.no_quantized = no_quantized
		self.load_model()
   
		# args = args or {}
		# if not exclude_device:
		# 	device = 0 if torch.cuda.is_available() else -1
		# 	self.generator = pipeline("text-generation", model=modelName, device=device, **args)
		# else:
		# 	self.generator = pipeline("text-generation", model=modelName, **args)
		# print("Model loaded")
		# self.llm = modelName
	def load_model_gguf(self):
		print("Model must be Guff")
		modeluri = self.download_model(self.get_gguf_file_url(self.model_name_or_path,filename=self.filename), self.downloadDest, self.filename)
		self.model = Llama(model_path=modeluri, n_ctx=16384, n_threads=10, n_gpu_layers=-1)

	def get_gguf_file_url(self, repo_id, filename="model.gguf"):
		"""
		Get the URL for a GGUF file in a Hugging Face repository.
		Args:
				repo_id (str): The repository ID (e.g., 'TheBloke/GEITje-7B-chat-GGUF').
				filename (str): The expected GGUF filename (default: 'model.gguf').
		Returns:
				str: The full URL to the GGUF file.
		"""
		api_url = f"https://huggingface.co/api/models/{repo_id}"
		response = requests.get(api_url)
		if response.status_code == 200:
				model_data = response.json()
				for file in model_data.get("siblings", []):
						if filename in file["rfilename"]:  # Check for GGUF file
								return f"https://huggingface.co/{repo_id}/resolve/main/{file['rfilename']}"
		raise ValueError(f"Failed to find GGUF file '{filename}' in repository '{repo_id}'.")
	def download_model(self, url, save_path,filename="model.gguf"):
		"""
		Download a GGUF model from a URL.
		Args:
				url (str): The URL to the GGUF model.
				save_path (str): The local path to save the model.
		"""
		print(f"Downloading model from {url}...")
		if(not os.path.exists(save_path)):
			os.makedirs(save_path)
		else:
			if os.path.exists(f"{save_path}/{filename}"):
				print(f"Model already exists at {save_path}/{filename}.")
				return f"{save_path}/{filename}"
		response = requests.get(url, stream=True)
		if response.status_code == 200:
				with open(f"{save_path}/{filename}", "wb") as f:
						for chunk in response.iter_content(chunk_size=1024):
								f.write(chunk)
				print(f"Model downloaded and saved to {save_path}/{filename}.")
				return f"{save_path}/{filename}"
		else:
				print(f"Failed to download model: {response.status_code}")

	def load_model(self):
			if "GGUF" in self.model_name_or_path:
					print("The string contains 'GGUF'.")
					self.load_model_gguf()
					return
			
			# Ensure the model is downloaded or accessible locally
			local_path = self._ensure_model_downloaded()
			print(f"Model path: {local_path}")
			
			# Detect quantization
			self.is_quantized = self._detect_quantization()
			
			if self.is_quantized and not self.no_quantized:
					# Configure BitsAndBytes for quantization
					bnb_config = BitsAndBytesConfig(
						load_in_8bit=True,
						llm_int8_threshold=6.0,
						llm_int8_enable_fp32_cpu_offload=True,
					)
					print("Model is quantized")
					print("Setting model")
					self.model = AutoModelForCausalLM.from_pretrained(
							self.model_name_or_path,
							quantization_config=bnb_config,
							device_map=self.device_map,
					)
			else:
					# Load a non-quantized model
					print("Setting model")
					self.model = AutoModelForCausalLM.from_pretrained(
							self.model_name_or_path,
							device_map=self.device_map,
					)

			# Load the tokenizer
			print("Setting tokenizer")
			self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)

			# Ensure the model's embedding layer matches the tokenizer's vocabulary size
			print("Resizing model embeddings to match tokenizer vocabulary size...")
			self.model.resize_token_embeddings(len(self.tokenizer))

			print("Model and tokenizer successfully loaded.")
	def _ensure_model_downloaded(self):
			"""
			Ensure the model is downloaded if it's not already local.
			Returns:
					str: The local path to the model.
			"""
			if(os.path.exists(self.model_name_or_path)):
				print(f"Model already exists at {self.model_name_or_path}.")
				return self.model_name_or_path
			if(os.path.exists(f"{self.downloadDest}/{self.model_name_or_path}")):
				print(f"Model already exists at {self.downloadDest}/{self.model_name_or_path}.")
				return f"{self.downloadDest}/{self.model_name_or_path}"
			if(os.path.exists(f"{self.downloadDest}/{self.filename}")):
				print(f"Model already exists at {self.downloadDest}/{self.filename}.")
				return f"{self.downloadDest}/{self.filename}"
   
			# Convert the model name to the filesystem-safe format
			safe_model_name = self.model_name_or_path.replace("/", "--")
			local_model_dir = f"./temp_model/models--{safe_model_name}"

			# Check if the model is already downloaded in the specified directory
			if os.path.exists(local_model_dir):
					print(f"Model already exists locally: {local_model_dir}")
					return local_model_dir

			print(f"Downloading model: {self.model_name_or_path}")
			return snapshot_download(self.model_name_or_path, cache_dir="./temp_model")

	def _detect_quantization(self):
				"""
				Detect whether the model is quantized based on available files or metadata.
				Returns:
						bool: True if the model is quantized, False otherwise.
				"""
				# Check for specific files that indicate quantization
				quantized_file = os.path.join(self.model_name_or_path, "quantized_config.json")
				if os.path.exists(quantized_file):
						print(f"Detected quantized model at: {self.model_name_or_path}")
						return True

				# Check for any other custom indicator of quantization if necessary
				# Add more logic here if you have other ways to detect quantization

				print(f"Detected non-quantized model at: {self.model_name_or_path}")
				return False
  
	def _getPipeline(self, task="text-generation", **pipeline_args):
		if type(self.model) is Llama:
			return self.model
		if not self.model or not self.tokenizer:
						raise ValueError("Model and tokenizer must be loaded first.")
		return pipeline(task, model=self.model, tokenizer=self.tokenizer, **pipeline_args)

	def parse_chatlog(self, chatlog):
			# Parse the chatlog string into a usable list format
			parsed_conversation = []
			# Split chatlog entries by 'map[' to isolate each message entry
			entries = chatlog.split("map[")
			for entry in entries[1:]:  # Skip the first split result, as it's empty
				# Extract whether it's from the user and the message text
				from_user = "fromUser:true" in entry
				message_start = entry.find("message:") + len("message:")
				message_end = entry.find(" username:")
				message = entry[message_start:message_end].strip()
				# Determine the role and append to parsed_conversation
				role = "user" if from_user else "assistant"
				parsed_conversation.append({"role": role, "content": message})
			return parsed_conversation

	def predict(self, prompt, chatlog=None, files=None, system_prompt=None, generation_kwargs=None):
			"""
			General function to handle prediction.
			Delegates to `predict_gguf` or `predict_default` based on the model type.
			"""
			pipeline = self._getPipeline()

			# Determine whether to use GGUF or default pipeline
			if isinstance(pipeline, Llama):  # GGUF-specific model
					return self.predict_gguf(
							prompt=prompt,
							chatlog=chatlog,
							files=files,
							system_prompt=system_prompt,
							generation_kwargs=generation_kwargs,
					)

			# Default behavior for Hugging Face-compatible pipelines
			return self.predict_default(
					prompt=prompt,
					chatlog=chatlog,
					files=files,
					system_prompt=system_prompt,
					generation_kwargs=generation_kwargs,
			)

	def _construct_conversation_text(self, prompt, chatlog, files, system_prompt, is_gguf):
		"""
		Constructs conversation text for GGUF models.
		"""
		# Initialize conversation with the system prompt
		conversation = [{"role": "system", "content": system_prompt}]

		# Add chatlog to the conversation if it exists and is not empty
		if chatlog:
				parsed_chatlog = self.parse_chatlog(chatlog)
				conversation.extend(parsed_chatlog)

		# Add the user prompt to the conversation
		conversation.append({"role": "user", "content": prompt})

		# Include files if they exist and are not empty
		if files:
				conversation.append({"role": "system", "content": f"Relevante bestanden:\n{files}"})

		# Return flat text format for GGUF
		return "\n".join(f"{entry['role'].capitalize()}: {entry['content']}" for entry in conversation)


	def predict_gguf(self, prompt, chatlog=None, files=None, system_prompt=None, generation_kwargs=None):
		"""
		Predict a response using a GGUF model.
		"""
		# Ensure the model is loaded
		if self.model is None:
				raise ValueError("No GGUF model is loaded.")

		# Set default system prompt if not provided
		if system_prompt is None:
				system_prompt = self.systemPrompt

		# Initialize the conversation
		conversation = []

		# Add system prompt as the initial entry
		if system_prompt:
				conversation.append(f"System: {system_prompt}")

		# Add parsed chatlog if it exists and is not empty
		if chatlog:
				for entry in self.parse_chatlog(chatlog):
						role = entry.get("role", "user").capitalize()
						content = entry.get("content", "")
						conversation.append(f"{role}: {content}")

		# Add the user's new prompt
		conversation.append(f"User: {prompt}")

		# Include files if provided
		if files:
			conversation.append(f"System: Relevant files: {', '.join(map(str, files))}")

		# Combine the conversation into a flat text format
		conversation_text = "\n".join(conversation)

		# Debug: Print the constructed prompt
		# print("Final Conversation Text for GGUF Model:\n", conversation_text)

		# Base generation settings
		base_generate_kwargs = {"max_tokens": 10000000, "temperature": 0.7}
		final_generate_kwargs = {**base_generate_kwargs, **(generation_kwargs or {})}
		# Generate response using the model
		print("Generating response...")
		response = self.model(conversation_text, **final_generate_kwargs,)
		print(f"Response: {response}")
		# Extract and clean the response text
		if "choices" in response and len(response["choices"]) > 0:
				return response["choices"][0]["text"].strip()

		# If no valid response, raise an error
		raise ValueError("The model did not return a valid response.")

	def predict_default(self, prompt, chatlog=None, files=None, system_prompt=None, generation_kwargs=None):
			"""
			Predict a response using a Hugging Face-compatible model.
			"""
			pipeline = self._getPipeline()

			# Set default system prompt if not provided
			if system_prompt is None:
					system_prompt = self.systemPrompt

			# Construct the conversation
			conversation_text = self._construct_conversation_text(
					prompt=prompt, chatlog=chatlog, files=files, system_prompt=system_prompt, is_gguf=False
			)

			# Add special tokens to the tokenizer
			pipeline.tokenizer.add_special_tokens({
					'additional_special_tokens': ['<|im_start|>', '<|im_end|>']
			})
			pipeline.model.resize_token_embeddings(len(pipeline.tokenizer))

			# Base generation settings
			base_generate_kwargs = {
					"do_sample": True,
					"temperature": 1.0,
					"max_new_tokens": 1000,
			}
			final_generate_kwargs = {**base_generate_kwargs, **(generation_kwargs or {})}

			# Generate response
			response = pipeline(conversation_text, **final_generate_kwargs)
			response = response[0]["generated_text"]

			return response


	def _construct_conversation_text(self, prompt, chatlog, files, system_prompt, is_gguf):
			"""
			Shared logic to construct the conversation text for both GGUF and default pipelines.
			"""
			# Initialize conversation with the system prompt
			conversation = [{"role": "system", "content": system_prompt}]

			# Add chatlog to the conversation
			if chatlog is not None:
					parsed_chatlog = self.parse_chatlog(chatlog)
					conversation.extend(parsed_chatlog)

			# Add the user prompt to the conversation
			conversation.append({"role": "user", "content": prompt})

			# Include files if provided
			if files is not None and len(files) > 0:
					conversation.append({"role": "system", "content": f"Relevante bestanden:\n{files}"})

			# Format conversation text
			if is_gguf:
					# Flat text format for GGUF
					return "\n".join(f"{entry['role'].capitalize()}: {entry['content']}" for entry in conversation)
			else:
					# Return structured conversation for Hugging Face-compatible pipelines
					return conversation