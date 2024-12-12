import os
import json
from transformers import pipeline
from huggingface_hub import login


class Deployment:
    def __init__(self, base_directory=None, context=None):
        """
        Initialize the Deployment class with a pipeline for text generation.
        """
        print("Initializing deployment...")

        # Read model-related environment variables
        MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")
        self.MAX_RESPONSE_LENGTH = int(os.environ.get("MAX_RESPONSE_LENGTH", 256))

        # Log in to Hugging Face if token is provided
        HF_TOKEN = os.environ.get("HF_TOKEN")
        if HF_TOKEN:
            login(token=HF_TOKEN)

        print(f"Loading pipeline for model: {MODEL_NAME}")
        self.pipeline = pipeline(
            "text-generation",
            model=MODEL_NAME,
            tokenizer=MODEL_NAME,
            torch_dtype="auto",
            device_map="auto",
        )
        print("Pipeline loaded successfully.")

        # Default configuration for text generation
        self.default_config = {
            "do_sample": True,
            "temperature": 0.7,
            "max_new_tokens": self.MAX_RESPONSE_LENGTH,
        }

    def request(self, data, context=None):
        """
        Handles incoming requests for text generation based on JSON conversation input.
        """
        print("Processing request...")

        # Parse JSON prompt
        try:
            prompt_data = json.loads(data["prompt"])
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error parsing prompt: {e}")
            return {"error": "Invalid prompt format."}

        # Process the conversation
        try:
            messages = json.loads(prompt_data["prompt"])
            conversation = self._format_conversation(messages)
        except KeyError as e:
            print(f"Error extracting conversation: {e}")
            return {"error": "Invalid conversation structure."}

        # Generate response
        try:
            outputs = self.pipeline(conversation, **self.default_config)
            response = outputs[0]["generated_text"]
        except Exception as e:
            print(f"Error during generation: {e}")
            return {"error": str(e)}

        # Return the generated response
        return {"output": response}

    def _format_conversation(self, messages):
        """
        Formats the conversation into a single string prompt.
        """
        formatted_conversation = ""
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            formatted_conversation += f"{role.capitalize()}: {content}\n"

        formatted_conversation += "Assistant:"
        return formatted_conversation