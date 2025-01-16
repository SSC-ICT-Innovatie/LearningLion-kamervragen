# Inference Component

This component provides a flexible framework for performing inference using different AI models, either locally or via an API. It supports both the Ollama inference engine and a custom inference implementation for local and remote execution. The design is extensible, allowing users to adapt and enhance its functionality for various use cases.

## Features

- **Local Inference**: Run inference on a local machine using specified AI models.
- **API Inference**: Connect to an external inference API for model execution.
- **Threaded Execution**: Perform API and local inference in parallel, leveraging threading for efficiency.
- **Configurable Models**: Supports customizable AI models via environment variables and function parameters.
- **Race-Based Results**: Utilizes a race to handle multiple concurrent inference outputs and uses the one that is returned first.
- **Fallback Mechanisms**: Allows fallback to alternative inference methods in case of issues.

## Requirements

- `.env` file with the following keys:
  - `DOMAIN`: The domain of the API endpoint for inference.
  - `API_KEY`: API key for authentication.

## Usage

### Local Inference

Use the `infer_run_local` function to execute inference:

```python
from your_module import infer_run_local

result = infer_run_local(
    prompt="What is the capital of France?",
    LLM="your-model-name",
    systemPrompt="Provide an informative answer.",
    generation_kwargs={"max_length": 100},
    no_quantized=True
)
print(result)
```

### API Inference

If `DOMAIN` and `API_KEY` are set in the `.env` file, the component will attempt to use the API for inference:

```python
result = infer_run_local(
    prompt="Summarize this document.",
    files=["example.txt"],
    systemPrompt="Generate a concise summary."
)
print(result)
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.