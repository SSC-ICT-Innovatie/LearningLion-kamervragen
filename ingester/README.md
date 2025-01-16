# Ingestion Component

This component facilitates local data ingestion, embedding, and vector store setup using a specified range and model. It is designed to streamline the ingestion process for applications requiring vector-based retrieval and BM25 retriever functionality.

## Features

- **Data Ingestion**: Handles local data ingestion from the `tmp` directory.
- **Embeddings Setup**: Configures embeddings using a specified model.
- **Vector Store Integration**: Prepares and initializes the chroma vector store for storing processed data.
- **BM25 Retriever Support**: Creates and saves multiple BM25 retrievers for efficient data retrieval.

## Usage

### Run Local Ingestion

To perform local ingestion, use the `run_local_ingest_stores` function. This will ingest data, configure embeddings, and set up BM25 retrievers.

```python
from your_module import run_local_ingest_stores

run_local_ingest_stores(
    range=Range.Tiny,
    modelname="textgain/allnli-GroNLP-bert-base-dutch-cased"
)
```

### Parameters

- `range`: Specifies the data range for ingestion. Defaults to `Range.Tiny`.
- `modelname`: Defines the model used for embedding setup. Defaults to `"textgain/allnli-GroNLP-bert-base-dutch-cased"`.

### Output

1. **Embeddings**: Configures embeddings with the specified model.
2. **Vector Store**: Initializes and updates the vector store.
3. **BM25 Retrievers**: Generates and saves retrievers (`bm25A`, `bm25B`, `bm25C`) for future use.

## Process Overview

1. **Initialize Components**:
   - Embedding setup via the `Embedding` class.
   - Database setup using the `Database` class.
   - Data ingestion through the `Ingestion` class.
2. **Ingest Data**:
   - Source directory: `./tmp`.
   - Vector store: Prepared with embeddings and ingested data.
3. **Set and Save BM25 Retrievers**:
   - `bm25A`, `bm25B`, and `bm25C` retrievers are created and saved as `.pkl` files.

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.
