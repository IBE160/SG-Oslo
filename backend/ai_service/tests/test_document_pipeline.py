import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from docx import Document # Added import for Document

from backend.ai_service.main import app
from backend.ai_service.document_pipeline import extract_text_from_pdf, extract_text_from_docx, chunk_text

client = TestClient(app)

# --- Test document_pipeline functions ---

def test_extract_text_from_pdf_success(tmp_path):
    # Create a dummy PDF file (simplified for testing, real PDF creation is complex)
    # The actual content validity is less important than that the function can process it without error
    pdf_content = b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj 3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R>>endobj 4 0 obj<</Length 55>>stream\nBT /F1 12 Tf 72 712 Td (Hello from PDF!) Tj ET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000074 00000 n\n0000000157 00000 n\n0000000287 00000 n\ntrailer<</Size 5/Root 1 0 R>>startxref 378\n%%EOF"
    pdf_file = tmp_path / "test.pdf"
    pdf_file.write_bytes(pdf_content)

    extracted_text = extract_text_from_pdf(str(pdf_file))
    assert isinstance(extracted_text, str)
    assert len(extracted_text) > 0 # Assert that some text is extracted

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
    # Check that there is overlap by ensuring the start of the second chunk is contained in the first
    assert chunks[0][-10:] in chunks[1] # More robust check for overlap

# --- Test FastAPI endpoint ---

@patch('backend.ai_service.document_pipeline.process_document')
@patch('backend.ai_service.ai_client.generate_summary')
@patch('backend.ai_service.ai_client.generate_flashcards')
@patch('backend.ai_service.ai_client.generate_quiz')
def test_upload_document_pdf_success(mock_generate_quiz, mock_generate_flashcards, mock_generate_summary, mock_process_document, tmp_path): # Added tmp_path
    mock_process_document.return_value = ["chunk1", "chunk2"]
    mock_generate_summary.return_value = "This is a summary."
    mock_generate_flashcards.return_value = [{"front": "Q1", "back": "A1"}]
    mock_generate_quiz.return_value = [{"question": "Q?", "options": ["A","B"], "answer": "A"}]

    # Create a dummy PDF file for the upload test
    test_pdf_file = tmp_path / "sample.pdf"
    test_pdf_file.write_bytes(b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj 3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R>>endobj 4 0 obj<</Length 55>>stream\nBT /F1 12 Tf 72 712 Td (Hello from PDF!) Tj ET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000074 00000 n\n0000000157 00000 n\n0000000287 00000 n\ntrailer<</Size 5/Root 1 0 R>>startxref 378\n%%EOF")

    with open(test_pdf_file, "rb") as f: # Use tmp_path for the file
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
