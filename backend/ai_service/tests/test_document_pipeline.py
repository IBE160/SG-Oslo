import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from docx import Document
from pypdf import PdfReader # Import PdfReader

from backend.ai_service.main import app
from backend.ai_service.document_pipeline import extract_text_from_pdf, extract_text_from_docx, chunk_text

client = TestClient(app)

# --- Test document_pipeline functions ---

@patch('backend.ai_service.document_pipeline.PdfReader') # Patch PdfReader
def test_extract_text_from_pdf_success(mock_pdf_reader, tmp_path):
    mock_instance = MagicMock()
    mock_instance.pages = [MagicMock(), MagicMock()]
    mock_instance.pages[0].extract_text.return_value = "Page 1 text."
    mock_instance.pages[1].extract_text.return_value = "Page 2 text."
    mock_pdf_reader.return_value = mock_instance

    pdf_file = tmp_path / "test.pdf"
    pdf_file.write_bytes(b"dummy pdf content") # Content no longer matters as much

    extracted_text = extract_text_from_pdf(str(pdf_file))
    assert "Page 1 text." in extracted_text
    assert "Page 2 text." in extracted_text
    assert isinstance(extracted_text, str)
    assert len(extracted_text) > 0

def test_extract_text_from_docx_success(tmp_path):
    doc = Document()
    doc.add_paragraph("Hello from DOCX!")
    docx_file = tmp_path / "test.docx"
    doc.save(docx_file)

    extracted_text = extract_text_from_docx(str(docx_file))
    assert "Hello from DOCX!" in extracted_text

def test_chunk_text():
    long_text = "This is a long sentence that needs to be chunked. " * 10
    chunks = chunk_text(long_text, chunk_size=50, overlap=10)
    assert len(chunks) > 1
    assert len(chunks[0]) == 50
    assert chunks[0][-10:] in chunks[1]

# --- Test FastAPI endpoint ---

@patch('backend.ai_service.main.process_document') # Corrected patch path to mock in main.py
@patch('backend.ai_service.ai_client.generate_summary')
@patch('backend.ai_service.ai_client.generate_flashcards')
@patch('backend.ai_service.ai_client.generate_quiz')
def test_upload_document_pdf_success(mock_generate_quiz, mock_generate_flashcards, mock_generate_summary, mock_process_document, tmp_path):
    mock_process_document.return_value = ["chunk1", "chunk2"]
    mock_generate_summary.return_value = "This is a summary."
    mock_generate_flashcards.return_value = [{"front": "Q1", "back": "A1"}]
    mock_generate_quiz.return_value = [{"question": "Q?", "options": ["A","B"], "answer": "A"}]

    test_pdf_file = tmp_path / "sample.pdf"
    test_pdf_file.write_bytes(b"dummy pdf content for upload test")

    with open(test_pdf_file, "rb") as f:
        response = client.post(
            "/upload-document/",
            files={"file": ("sample.pdf", f, "application/pdf")}
        )

    assert response.status_code == 200
    assert response.json()["summary"] == "This is a summary."
    assert response.json()["flashcards"] == [{"front": "Q1", "back": "A1"}]
    assert response.json()["quiz"] == [{"question": "Q?", "options": ["A","B"], "answer": "A"}]
    assert response.json()["chunks"] == ["chunk1", "chunk2"]
    mock_process_document.assert_called_once()
    mock_generate_summary.assert_called_once_with(["chunk1", "chunk2"])
    mock_generate_flashcards.assert_called_once_with(["chunk1", "chunk2"])
    mock_generate_quiz.assert_called_once_with(["chunk1", "chunk2"])

def test_upload_document_unsupported_type():
    with patch('builtins.open', MagicMock()), \
         patch('shutil.copyfileobj', MagicMock()), \
         patch('os.remove', MagicMock()) as mock_os_remove:
        response = client.post(
            "/upload-document/",
            files={"file": ("sample.txt", b"some text", "text/plain")}
        )
        assert response.status_code == 400
        assert "Unsupported file type" in response.json()["detail"]
        mock_os_remove.assert_called_once()

# Add more tests for error handling, empty files, etc.
