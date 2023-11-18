from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from typing import List, Optional
from datetime import datetime
import os

app = FastAPI()

files = []
upload_folder = "uploaded_files"

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)


def get_file_by_id(file_id: str):
    for file in files:
        if file['file_id'] == file_id:
            return file
    return None


@app.post("/files/upload")
async def upload_file(file: UploadFile = File(...), metadata: Optional[dict] = None):
    file_id = str(len(files) + 1)
    
    # Save file data to local folder
    file_path = os.path.join(upload_folder, file.filename)
    with open(file_path, "wb") as local_file:
        local_file.write(file.file.read())

    # Store metadata
    file_metadata = {
        "file_id": file_id,
        "file_name": file.filename,
        "created_at": datetime.now(),
        "size": os.path.getsize(file_path),
        "file_type": file.content_type,
        "local_path": file_path,
    }
    if metadata:
        file_metadata.update(metadata)
    files.append(file_metadata)
    return {"file_id": file_id}


@app.get("/files/{file_id}")
async def read_file(file_id: str):
    file = get_file_by_id(file_id)
    if file:
        return StreamingResponse(content=open(file['local_path'], "rb"), media_type=file['file_type'])
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.put("/files/{file_id}")
async def update_file(file_id: str, file: UploadFile = File(...), metadata: Optional[dict] = None):
    existing_file = get_file_by_id(file_id)
    if existing_file:
        # Save updated file data to local folder
        file_path = os.path.join(upload_folder, file.filename)
        with open(file_path, "wb") as local_file:
            local_file.write(file.file.read())

        # Update metadata
        existing_file['file_name'] = file.filename
        existing_file['size'] = os.path.getsize(file_path)
        existing_file['file_type'] = file.content_type
        existing_file['created_at'] = datetime.now()
        existing_file['local_path'] = file_path
        if metadata:
            existing_file.update(metadata)

        return existing_file
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.delete("/files/{file_id}")
async def delete_file(file_id: str):
    global files
    file = get_file_by_id(file_id)
    if file:
        os.remove(file['local_path'])  # Delete the file from the local folder
        files = [f for f in files if f['file_id'] != file_id]
        return {"message": "File deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/files")
async def list_files():
    return files
