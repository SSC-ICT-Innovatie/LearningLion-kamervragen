# Query Module

This module provides functionality for querying data from vector stores and retrieving specific documents from a database. The design emphasizes modularity and flexibility, allowing it to be adapted or extended for different use cases involving data retrieval and processing.

## Features

- **Query Vector Stores**: Retrieve relevant documents using a query prompt and optional subject.
- **Combine Query Results**: Merge and deduplicate results from different query types.
- **Retrieve Document Blobs**: Fetch specific documents, such as PDFs, from a database using unique identifiers.

## Usage

### Querying Stores

The `run_local_query_stores` function retrieves documents based on a query prompt and an optional subject. It supports combining results to ensure no overlap.

#### Parameters

- `prompt` (str): The main query to search for relevant documents.
- `subject` (str, optional): Additional context to narrow the search.
- `range` (Range): Specifies the data range to query (e.g., `Range.Tiny`).

#### Returns

- A list of retrieved documents.

### Retrieving Document Blobs

The `getDocumentBlobFromDatabase` function fetches a specific document (e.g., PDF) from the database using its UUID.

#### Parameters

- `UUID` (str): The unique identifier for the document.
- `range` (Range): Specifies the data range to query (e.g., `Range.Tiny`).

#### Returns

- The document blob (e.g., PDF content) if found, otherwise `None`.

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.
