import os
import shutil
from typing import List

from fastapi import FastAPI, UploadFile, File, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .document_pipeline import process_document

app = FastAPI()

# Temporary directory for uploaded files
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "temp_uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "AI Service is running!"}

@app.post("/upload-document/")
async def upload_document(file: UploadFile = File(...)) -> List[str]:
    if not file.filename:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="No upload file found"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Determine file type (a more robust solution might use python-magic or similar)
        # For now, we'll rely on the client-provided content type or filename extension
        content_type = file.content_type
        if content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            # Fallback to extension if content_type is generic or missing
            if file.filename.lower().endswith(".pdf"):
                content_type = "application/pdf"
            elif file.filename.lower().endswith(".docx"):
                content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            else:
                os.remove(file_path) # Clean up unsupported file
                raise HTTPException(
                    status_code=HTTP_400_BAD_REQUEST,
                    detail=f"Unsupported file type: {file.content_type} or file extension. Only PDF and DOCX are supported."
                )

        chunks = process_document(file_path, content_type)
        return chunks
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {e}"
        )
    finally:
        if os.path.exists(file_path):
            os.remove(file_path) # Clean up the temporary file
