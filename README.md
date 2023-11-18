# FastAPI Dropbox-like Service

A simple FastAPI application that implements a simplified Dropbox-like service where users can upload, retrieve, and manage files through a set of RESTful APIs. The service also supports the storage of metadata for each uploaded file.

## Features

- Upload File API: Allow users to upload files onto the platform.
- Read File API: Retrieve a specific file based on a unique identifier.
- Update File API: Update an existing file or its metadata.
- Delete File API: Delete a specific file based on a unique identifier.
- List Files API: List all available files and their metadata.

## Prerequisites

- Python 3.7 or higher
- FastAPI
- Uvicorn

## Installation

1. Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

3. Run the FastAPI application:

    ```
    python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
    ```

4. Access the API documentation:

    - **Swagger UI**: Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API using Swagger UI.


