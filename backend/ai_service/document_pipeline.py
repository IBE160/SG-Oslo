import os
from typing import List

from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF {file_path}: {e}")
        raise
    return text

def extract_text_from_docx(file_path: str) -> str:
    """
    Extracts text from a DOCX file.
    """
    text = ""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error extracting text from DOCX {file_path}: {e}")
        raise
    return text

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """
    Splits text into smaller chunks with optional overlap.
    """
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
        if start >= len(text) - overlap: # Ensure we don't create tiny chunks at the very end
            break
    return chunks

def process_document(file_path: str, file_type: str) -> List[str]:
    """
    Orchestrates document processing: extracts text and splits it into chunks.
    """
    extracted_text = ""
    if file_type == "application/pdf":
        extracted_text = extract_text_from_pdf(file_path)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        extracted_text = extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    chunks = chunk_text(extracted_text)
    return chunks
