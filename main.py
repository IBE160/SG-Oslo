import os
import uuid

from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import firebase_admin
from firebase_admin import credentials, firestore, auth

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase-service-account.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # Initialize Firestore

# Get Gemini API Key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# In-memory session storage (for PoC)
sessions = {}

# Placeholder function to save data to Firestore
def save_to_firestore(collection_name: str, data: dict):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def post_register(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": f"Error creating user: {e}"})

@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def post_login(response: Response, email: str = Form(...), password: str = Form(...)):
    try:
        # In a real application, you would verify credentials with Firebase client SDK
        if email == "test@example.com" and password == "password": # Placeholder for actual Firebase login
            session_id = str(uuid.uuid4())
            sessions[session_id] = {"email": email}
            response.set_cookie(key="session_id", value=session_id)
            return RedirectResponse(url="/dashboard", status_code=303)
        else:
            return RedirectResponse(url="/login?error=Invalid credentials", status_code=303)
    except Exception as e:
        return RedirectResponse(url=f"/login?error=Login error: {e}", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessions:
        user = sessions[session_id]
        return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})
    else:
        return RedirectResponse(url="/login", status_code=303)

