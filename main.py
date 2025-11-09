import os
import uuid
import shutil  # Import shutil for file operations
import google.generativeai as genai  # Import Google Gemini API
from io import BytesIO  # For handling file content in memory
import json  # Import json for parsing AI responses

# Document parsing libraries
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document as DocxDocument
import pypdf  # For PDF processing (if needed beyond text extraction)
import ftfy  # For fixing text encoding issues

from fastapi import FastAPI, Request, Form, Response, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import firebase_admin
from firebase_admin import credentials, firestore, auth

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Initialize Firebase
FIREBASE_SERVICE_ACCOUNT_PATH = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
if not FIREBASE_SERVICE_ACCOUNT_PATH:
    raise ValueError("FIREBASE_SERVICE_ACCOUNT_PATH environment variable not set.")
cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()  # Initialize Firestore

# Get Gemini API Key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=GEMINI_API_KEY)  # Configure Gemini API

# In-memory session storage (for PoC)
sessions = {}

# Create a directory for temporary file storage
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Helper to get current user from session
def get_current_user(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessions:
        return sessions[session_id]
    return None


# Placeholder function to save data to Firestore
def save_to_firestore(collection_name: str, data: dict):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id


# Function to extract text from PDF and DOCX files
async def extract_text_from_file(file_path: str, content_type: str) -> str:
    text = ""
    if content_type == "application/pdf":
        try:
            text = extract_pdf_text(file_path)
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            raise HTTPException(
                status_code=500, detail="Failed to extract text from PDF."
            )
    elif (
        content_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        try:
            doc = DocxDocument(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            print(f"Error extracting text from DOCX: {e}")
            raise HTTPException(
                status_code=500, detail="Failed to extract text from DOCX."
            )

    # Fix common encoding issues
    text = ftfy.fix_text(text)
    return text


# Function to generate content using Gemini
async def generate_content_with_gemini(text: str, content_type: str):
    model = genai.GenerativeModel("gemini-pro")

    if content_type == "summary":
        prompt = f"Please provide a concise summary of the following text:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    elif content_type == "flashcards":
        prompt = f"Generate a list of flashcards (question and answer pairs) from the following text. Provide the output as a JSON array of objects, where each object has 'question' and 'answer' keys:\n\n{text}"
        response = model.generate_content(prompt)
        # Assuming the model returns valid JSON, parse it
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            print(f"Error parsing flashcards JSON: {response.text}")
            return []
    elif content_type == "quiz":
        prompt = f"Generate a multiple-choice quiz from the following text. Provide the output as a JSON array of objects, where each object has 'question', 'options' (an array of strings), and 'correct_answer' (string) keys:\n\n{text}"
        response = model.generate_content(prompt)
        # Assuming the model returns valid JSON, parse it
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            print(f"Error parsing quiz JSON: {response.text}")
            return []
    return "Generated content placeholder"


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register")
async def post_register(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    try:
        user = auth.create_user(email=email, password=password)
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        return templates.TemplateResponse(
            "register.html", {"request": request, "error": f"Error creating user: {e}"}
        )


@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def post_login(
    response: Response, email: str = Form(...), password: str = Form(...)
):
    try:
        # In a real application, you would use Firebase client SDK to sign in
        # and then verify the ID token on the backend.
        # For this PoC, we'll check if the user exists in Firebase.
        # NOTE: This does NOT verify the password. It only checks if the email is registered.
        # This is a security flaw for a production app.
        try:
            user_record = auth.get_user_by_email(email)
            # If user_record is found, we consider them "logged in" for this PoC.
            # In a real app, you'd verify password via client SDK and token.
            session_id = str(uuid.uuid4())
            sessions[session_id] = {"email": email}
            
            response_obj = Response(status_code=303) # Create a Response object for redirect
            response_obj.headers["Location"] = "/dashboard" # Set the Location header for redirect
            response_obj.set_cookie(key="session_id", value=session_id, path="/", httponly=True, samesite="lax") # Set cookie with explicit attributes
            return response_obj
        except auth.UserNotFoundError:
            print(f"DEBUG: post_login - User not found for email: {email}")
            return RedirectResponse(
                url="/login?error=Invalid credentials", status_code=303
            )
        except Exception as e:
            # Catch other Firebase errors or general exceptions
            print(f"DEBUG: post_login - Firebase login error: {e}")
            return RedirectResponse(
                url=f"/login?error=Login error: {e}", status_code=303
            )
    except Exception as e:
        print(f"DEBUG: post_login - General exception: {e}")
        return RedirectResponse(url=f"/login?error=Login error: {e}", status_code=303)


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    # Get message from query params if available
    message = request.query_params.get("message")
    error = request.query_params.get("error")

    # Retrieve user's study sets from Firestore
    study_sets_ref = db.collection("study_sets").where("user_id", "==", user["email"])
    study_sets = []
    for doc in study_sets_ref.stream():
        study_set_data = doc.to_dict()
        study_set_data["id"] = doc.id  # Add the document ID
        study_sets.append(study_set_data)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "message": message,
            "error": error,
            "study_sets": study_sets,
        },
    )


@app.get("/study-sets/{study_set_id}", response_class=HTMLResponse)
async def get_study_set(request: Request, study_set_id: str):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()

    # Ensure the study set belongs to the current user
    if study_set_data["user_id"] != user["email"]:
        raise HTTPException(
            status_code=403, detail="Not authorized to view this study set"
        )

    return templates.TemplateResponse(
        "study_session.html",
        {"request": request, "user": user, "study_set": study_set_data},
    )


@app.post("/save-study-set")
async def save_study_set(request: Request, study_set_id: str = Form(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()

    # Ensure the study set belongs to the current user
    if study_set_data["user_id"] != user["email"]:
        raise HTTPException(
            status_code=403, detail="Not authorized to save this study set"
        )

    # Update the status to "saved"
    study_set_ref.update({"status": "saved"})

    return RedirectResponse(
        url=f"/study-sets/{study_set_id}?message=Study set saved successfully!",
        status_code=303,
    )


@app.post("/upload")
async def post_upload(request: Request, file: UploadFile = File(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # File type validation
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only PDF and DOCX are allowed."
        )

    # File size validation (e.g., max 5MB)
    max_file_size = 5 * 1024 * 1024  # 5 MB
    file_content = await file.read()
    if len(file_content) > max_file_size:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size is {max_file_size / (1024 * 1024)} MB.",
        )

    # Save file temporarily
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(file_content)

    print(
        f"Received file: {file.filename}, Content-Type: {file.content_type}, Size: {len(file_content)} bytes, saved to {file_location}"
    )

    # Extract text from the uploaded file
    extracted_text = await extract_text_from_file(file_location, file.content_type)

    # Generate content using Gemini
    summary = await generate_content_with_gemini(extracted_text, "summary")
    flashcards = await generate_content_with_gemini(extracted_text, "flashcards")
    quiz = await generate_content_with_gemini(extracted_text, "quiz")

    # Store generated content in Firestore
    study_set_data = {
        "user_id": user["email"],  # Using email as user_id for PoC
        "document_name": file.filename,
        "upload_timestamp": firestore.SERVER_TIMESTAMP,
        "status": "completed",
        "summary": summary,
        "flashcards": flashcards,
        "quiz": quiz,
    }
    study_set_id = save_to_firestore("study_sets", study_set_data)
    print(f"Study set saved to Firestore with ID: {study_set_id}")

    return RedirectResponse(
        url="/dashboard?message=File uploaded. AI is generating study materials...",
        status_code=303,
    )
