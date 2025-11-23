import os
import shutil
from typing import Dict, Any, List # Import List for chunks return type hint

from fastapi import FastAPI, UploadFile, File, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .document_pipeline import process_document
from .ai_client import generate_summary, generate_flashcards, generate_quiz # Import generate_quiz

app = FastAPI()

# Temporary directory for uploaded files
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "temp_uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "AI Service is running!"}

@app.post("/upload-document/", response_model=Dict[str, Any])
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="No upload file found"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Determine file type
        content_type = file.content_type
        if content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
            if file.filename.lower().endswith(".pdf"):
                content_type = "application/pdf"
            elif file.filename.lower().endswith(".docx"):
                content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            else:
                os.remove(file_path)
                raise HTTPException(
                    status_code=HTTP_400_BAD_REQUEST,
                    detail=f"Unsupported file type: {file.content_type} or file extension. Only PDF and DOCX are supported."
                )

        # Process the document to get text chunks
        chunks = process_document(file_path, content_type)
        
        # Generate summary from the text chunks
        summary = generate_summary(chunks)

        # Generate flashcards from the text chunks
        flashcards = generate_flashcards(chunks)

        # Generate quiz from the text chunks
        quiz = generate_quiz(chunks)
        
        return {"summary": summary, "flashcards": flashcards, "quiz": quiz, "chunks": chunks}

    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {e}"
        )
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
