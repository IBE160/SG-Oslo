import os
import uuid
import shutil
import random
import google.generativeai as genai
from google.api_core.exceptions import NotFound, InvalidArgument
from io import BytesIO
import json
from dotenv import load_dotenv
import logging
from contextlib import asynccontextmanager

# Document parsing libraries
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document as DocxDocument
import pypdf
import ftfy

from fastapi import FastAPI, Request, Form, Response, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import firebase_admin
from firebase_admin import credentials, firestore, auth

# --- Globals ---
db = None
model = None
sessions = {}

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Application Lifespan (Startup and Shutdown) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    global db, model
    logger.info("Starting application initialization...")
    try:
        # 1. Load environment variables
        load_dotenv()
        logger.info("Environment variables loaded.")

        # 2. Initialize Firebase
        service_key_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
        if not service_key_path:
            raise ValueError("FIREBASE_SERVICE_ACCOUNT_PATH not set in .env")
        cred = credentials.Certificate(service_key_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        logger.info("✅ Firebase initialized")

        # 3. Configure and verify Gemini
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY not set in .env")
        genai.configure(api_key=google_api_key)
        logger.info("✅ Google API key loaded")
        
        # Proactively check if the model exists by making a lightweight call
        model = genai.GenerativeModel("gemini-flash-latest")
        model.count_tokens("test") # This will raise an error if the model/API key is invalid
        logger.info("✅ Gemini initialized and ready")

    except Exception as e:
        logger.critical(f"Application startup failed: {e}")
        # In a real production scenario, you might want to exit the process
        # For now, we'll log and the app will be in a non-functional state
        raise

    yield  # Application runs here

    logger.info("Application shutdown.")

# --- FastAPI App Initialization ---
app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

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
            logger.error(f"Error extracting text from PDF: {e}")
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF.")
    elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        try:
            doc = DocxDocument(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            logger.error(f"Error extracting text from DOCX: {e}")
            raise HTTPException(status_code=500, detail="Failed to extract text from DOCX.")
    text = ftfy.fix_text(text)
    return text

# Function to generate content using Gemini
async def generate_content_with_gemini(text: str, content_type: str):
    if not model:
        logger.error("Gemini model not initialized. Cannot generate content.")
        return "AI service is not configured."
        
    try:
        # Define prompts based on content type
        prompts = {
            "summary": f"Please provide a detailed, highly organized, easy-to-read, and scannable summary suitable for a technical overview of the following text. Use the following formatting rules:\n\n"
                       f"1. Use Markdown headings (## and ###) for the main concepts and sub-sections.\n"
                       f"2. If the text compares 'Procedural Programming' and 'Object-Oriented Programming', use a two-column Markdown table to clearly contrast them.\n"
                       f"3. For 'Key OO Concepts' like Objects, Classes, Encapsulation, Inheritance, Polymorphism, and Composition, use bolded, distinct headings and bullet points.\n"
                       f"4. Define and bold key terms like 'Attributes', 'Behaviors (Methods)', 'Superclass', 'Subclass', and the relationships ('Is-a', 'Has-a').\n"
                       f"5. The summary should be well-structured, using Markdown for formatting.\n"
                       f"6. Use bullet points to list key information.\n"
                       f"7. Ensure there are line breaks between paragraphs and bullet points for readability.\n"
                       f"8. Do not use double asterisks for bolding.\n"
                       f"9. Do not include any promotional text or artifacts from the document's table of contents or index.\n"
                       f"10. Ensure the output is clean and does not contain any special characters like '***'.\n\n"
                       f"{text}",
            "flashcards": f"Generate a list of flashcards (question and answer pairs) from the following text. The list must contain a minimum of 5 and a maximum of 10 flashcards. Provide the output as a JSON array of objects, where each object has 'question' and 'answer' keys:\n\n{text}",
            "quiz": f"Generate a multiple-choice quiz from the following text. Provide the output as a JSON array of objects, where each object has 'question', 'options' (an array of strings), and 'correct_answer' (string) keys:\n\n{text}"
        }
        prompt = prompts.get(content_type)
        if not prompt:
            return "Invalid content type."

        response = model.generate_content(prompt)

        # Handle JSON parsing for specific content types
        if content_type in ["flashcards", "quiz"]:
            try:
                # Clean the response to remove markdown fences
                text = response.text.strip()
                if text.startswith("```json"):
                    text = text[7:]
                if text.endswith("```"):
                    text = text[:-3]
                
                return json.loads(text)
            except json.JSONDecodeError:
                logger.error(f"Error parsing JSON from Gemini for {content_type}: {response.text}")
                return []
        
        # Clean the summary text
        summary_text = response.text.replace('***', '').replace('**', '').strip()
        return summary_text

    except Exception as e:
        logger.error(f"Gemini content generation failed: {e}")
        return "AI temporarily unavailable"

# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse("home.html", {"request": request, "user": user})

@app.get("/how-it-works", response_class=HTMLResponse)
async def get_how_it_works(request: Request):
    user = get_current_user(request)
    # The content of how-it-works is now fully in the HTML file.
    # If it were still markdown, the logic would be here.
    return templates.TemplateResponse("how-it-works.html", {"request": request, "user": user})

@app.get("/faq", response_class=HTMLResponse)
async def get_faq(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse("faq.html", {"request": request, "user": user})

@app.get("/register", response_class=HTMLResponse)
async def get_register(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse("register.html", {"request": request, "user": user})

@app.post("/register")
async def post_register(request: Request, email: str = Form(...), password: str = Form(...)):
    user = get_current_user(request)
    try:
        user = auth.create_user(email=email, password=password)
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": f"Error creating user: {e}", "user": user})

@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    user = get_current_user(request)
    return templates.TemplateResponse("login.html", {"request": request, "user": user})

@app.post("/login")
async def post_login(response: Response, email: str = Form(...), password: str = Form(...)):
    try:
        try:
            user_record = auth.get_user_by_email(email)
            session_id = str(uuid.uuid4())
            sessions[session_id] = {"email": email}
            
            response_obj = Response(status_code=303)
            response_obj.headers["Location"] = "/dashboard"
            response_obj.set_cookie(key="session_id", value=session_id, path="/", httponly=True, samesite="lax")
            return response_obj
        except auth.UserNotFoundError:
            logger.warning(f"Failed login attempt for non-existent user: {email}")
            return RedirectResponse(url="/login?error=Invalid credentials", status_code=303)
    except Exception as e:
        logger.error(f"Login error for user {email}: {e}")
        return RedirectResponse(url=f"/login?error=An unexpected login error occurred.", status_code=303)

@app.post("/logout")
async def post_logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessions:
        del sessions[session_id]
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie(key="session_id", path="/")
    return response


# --- Category Routes (New) ---
@app.get("/categories")
async def get_categories_api(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    categories = []
    if db:
        categories_ref = db.collection("categories").where("user_id", "==", user["email"]).order_by("createdAt")
        for doc in categories_ref.stream():
            cat_data = doc.to_dict()
            cat_data["id"] = doc.id
            categories.append(cat_data)
    return {"categories": categories}

@app.post("/categories")
async def post_category(request: Request, name: str = Form(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    if not name or len(name.strip()) == 0:
        return RedirectResponse(url="/dashboard?error=Category name cannot be empty.", status_code=303)

    if db:
        category_data = {
            "user_id": user["email"],
            "name": name.strip(),
            "createdAt": firestore.SERVER_TIMESTAMP
        }
        save_to_firestore("categories", category_data)
        return RedirectResponse(url="/dashboard?message=Category created.", status_code=303)
    
    return RedirectResponse(url="/dashboard?error=Database not available.", status_code=303)
# --- End of Category Routes ---


# --- Progression Tracking Routes (New) ---
@app.post("/quiz-results")
async def post_quiz_result(request: Request,
                           study_set_id: str = Form(...),
                           score: float = Form(...),
                           question_count: int = Form(...),
                           correct_count: int = Form(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    # Verify user owns the study set
    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()
    if not study_set.exists or study_set.to_dict().get("user_id") != user.get("email"):
        raise HTTPException(status_code=404, detail="Study set not found")

    result_data = {
        "user_id": user["email"],
        "studySetId": study_set_id,
        "score": score,
        "questionCount": question_count,
        "correctCount": correct_count,
        "completedAt": firestore.SERVER_TIMESTAMP
    }
    save_to_firestore("quiz_results", result_data)
    
    return {"message": "Quiz result saved successfully."}


@app.get("/study-sets/{study_set_id}/progress")
async def get_study_set_progress(request: Request, study_set_id: str):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    # Verify user owns the study set first
    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()
    if not study_set.exists or study_set.to_dict().get("user_id") != user.get("email"):
        raise HTTPException(status_code=404, detail="Study set not found")

    # Query for progress
    progress_data = []
    progress_query = db.collection("quiz_results") \
        .where("user_id", "==", user["email"]) \
        .where("studySetId", "==", study_set_id) \
        .order_by("completedAt")
    
    for doc in progress_query.stream():
        result = doc.to_dict()
        # Firestore timestamps are not directly JSON serializable in this setup
        if "completedAt" in result and hasattr(result["completedAt"], 'isoformat'):
             result["completedAt"] = result["completedAt"].isoformat()
        progress_data.append(result)
        
    return {"progress": progress_data}
# --- End of Progression Tracking Routes ---


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    message = request.query_params.get("message")
    error = request.query_params.get("error")
    category_filter = request.query_params.get("category_filter")

    study_sets = []
    categories = []
    if db:
        # Fetch categories first, as they are always needed
        categories_ref = db.collection("categories").where("user_id", "==", user["email"]).order_by("name")
        for doc in categories_ref.stream():
            cat_data = doc.to_dict()
            cat_data["id"] = doc.id
            categories.append(cat_data)

        # Fetch study sets based on the query
        study_sets_query = db.collection("study_sets").where("user_id", "==", user["email"])
        
        # Apply category filter if one is provided and is not 'all'
        if category_filter and category_filter != "all":
            study_sets_query = study_sets_query.where("categoryId", "==", category_filter)

        for doc in study_sets_query.stream():
            study_set_data = doc.to_dict()
            study_set_data["id"] = doc.id
            study_sets.append(study_set_data)
        
    return templates.TemplateResponse("dashboard.html", {
        "request": request, 
        "user": user, 
        "message": message, 
        "error": error, 
        "study_sets": study_sets,
        "categories": categories,
        "current_filter": category_filter
    })

@app.get("/study-sets/{study_set_id}", response_class=HTMLResponse)
async def get_study_set(request: Request, study_set_id: str):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")
        
    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()
    if study_set_data.get("user_id") != user.get("email"):
        raise HTTPException(status_code=403, detail="Not authorized to view this study set")

    study_set_data["id"] = study_set_id  # Add the ID to the dictionary

    return templates.TemplateResponse("study_session.html", {"request": request, "user": user, "study_set": study_set_data})

@app.get("/get-study-set-content/{study_set_id}/{content_type}")
async def get_study_set_content(request: Request, study_set_id: str, content_type: str):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    limit = request.query_params.get("limit")

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()
    if study_set_data.get("user_id") != user.get("email"):
        raise HTTPException(status_code=403, detail="Not authorized to view this study set")

    content = study_set_data.get(content_type)
    if content is None:
        raise HTTPException(status_code=404, detail="Content type not found")

    # If it's a quiz and a limit is set, shuffle and slice the quiz
    if content_type == 'quiz' and limit:
        try:
            limit = int(limit)
            if isinstance(content, list):
                random.shuffle(content)
                content = content[:limit]
        except (ValueError, TypeError):
            # Ignore invalid limit, return full quiz
            pass

    return {"content": content}


@app.post("/study-sets/{study_set_id}/assign-category")
async def post_assign_category(request: Request, study_set_id: str, category_id: str = Form(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    # Verify user owns the study set
    if not study_set.exists or study_set.to_dict().get("user_id") != user.get("email"):
        return RedirectResponse(url="/dashboard?error=Study set not found.", status_code=303)

    # Verify user owns the category (unless it's "none")
    if category_id != "none":
        category_ref = db.collection("categories").document(category_id)
        category = category_ref.get()
        if not category.exists or category.to_dict().get("user_id") != user.get("email"):
            return RedirectResponse(url="/dashboard?error=Category not found.", status_code=303)

    update_data = {"categoryId": category_id if category_id != "none" else firestore.DELETE_FIELD}
    study_set_ref.update(update_data)
    
    return RedirectResponse(url="/dashboard?message=Category updated.", status_code=303)


@app.post("/save-study-set")
async def save_study_set(request: Request, study_set_id: str = Form(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()
    if study_set_data.get("user_id") != user.get("email"):
        raise HTTPException(status_code=403, detail="Not authorized to save this study set")

    study_set_ref.update({"status": "saved"})
    return RedirectResponse(url=f"/study-sets/{study_set_id}?message=Study set saved successfully!", status_code=303)

@app.post("/delete-study-set/{study_set_id}")
async def post_delete_study_set(request: Request, study_set_id: str):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    if not db:
        raise HTTPException(status_code=503, detail="Database not available.")

    study_set_ref = db.collection("study_sets").document(study_set_id)
    study_set = study_set_ref.get()

    if not study_set.exists:
        raise HTTPException(status_code=404, detail="Study set not found")

    study_set_data = study_set.to_dict()
    if study_set_data.get("user_id") != user.get("email"):
        raise HTTPException(status_code=403, detail="Not authorized to delete this study set")

    # Delete the document from Firestore
    study_set_ref.delete()
    logger.info(f"Deleted study set {study_set_id} from Firestore.")

    # Delete the file from the filesystem
    try:
        document_name = study_set_data.get("document_name")
        if document_name:
            file_path = os.path.join(UPLOAD_DIR, document_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted file {file_path} from filesystem.")
            else:
                logger.warning(f"File not found for deletion: {file_path}")
    except Exception as e:
        logger.error(f"Error deleting file for study set {study_set_id}: {e}")

    return RedirectResponse(url="/dashboard?message=Study set deleted successfully.", status_code=303)

@app.post("/upload-document")
async def post_upload_document(request: Request, file: UploadFile = File(...)):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # File validation
    allowed_types = ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
    if file.content_type not in allowed_types:
        return RedirectResponse(url="/dashboard?error=Invalid file type. Only PDF and DOCX are allowed.", status_code=303)
    
    max_file_size = 5 * 1024 * 1024  # 5 MB
    file_content = await file.read()
    if len(file_content) > max_file_size:
        return RedirectResponse(url=f"/dashboard?error=File too large. Maximum size is {max_file_size / (1024 * 1024)} MB.", status_code=303)

    # Save file and process
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(file_content)

    try:
        extracted_text = await extract_text_from_file(file_location, file.content_type)
        
        # Generate all three content types
        summary = await generate_content_with_gemini(extracted_text, "summary")
        flashcards = await generate_content_with_gemini(extracted_text, "flashcards")
        quiz = await generate_content_with_gemini(extracted_text, "quiz")

        # Store all in Firestore
        study_set_data = {
            "user_id": user["email"],
            "document_name": file.filename,
            "upload_timestamp": firestore.SERVER_TIMESTAMP,
            "status": "completed",
            "summary": summary,
            "flashcards": flashcards,
            "quiz": quiz,
        }
        study_set_id = save_to_firestore("study_sets", study_set_data)
        logger.info(f"Study set {study_set_id} with summary, flashcards, and quiz saved for user {user['email']}")

        return RedirectResponse(url="/dashboard?message=File uploaded and study materials generated.", status_code=303)
    except HTTPException as e:
        return RedirectResponse(url=f"/dashboard?error={e.detail}", status_code=303)
    finally:
        # Clean up the uploaded file
        if os.path.exists(file_location):
            os.remove(file_location)