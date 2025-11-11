# Decision Architecture

## Executive Summary

This document outlines the architecture for the StudyBuddy AI project. The architecture is designed to be simple, scalable, and easy to build upon, with a focus on using modern, well-supported technologies. The core of the architecture is a FastAPI backend with a simple HTML/CSS frontend, using Firebase for data persistence, authentication, and file storage. The AI-powered features will be provided by Google Gemini, with OpenAI's GPT-4 as a backup.

## Decision Summary

| Category | Decision | Version | Affects Epics | Rationale |
| --- | --- | --- | --- | --- |
| Project Structure | Custom FastAPI structure | N/A | 1, 2 | Simple and easy to understand for a PoC. |
| Data Persistence | Firestore | N/A | 1, 2 | Easy to use, flexible, and integrates well with Firebase Authentication. |
| API Pattern | REST API | N/A | 1, 2 | Simple, standard, and well-supported by FastAPI. |
| Authentication | Firebase Authentication | N/A | 1 | Secure, easy to implement, and integrates with Firestore. |
| File Storage | Firebase Storage | N/A | 2 | Part of the Firebase ecosystem, scalable, and reliable. |
| AI Service | Google Gemini / OpenAI GPT-4 | N/A | 2 | Provides a primary and backup AI service for reliability. |

## Project Structure

```
/
├── main.py         # Main application file
├── requirements.txt  # Python libraries
├── static/           # CSS and JavaScript files
│   └── styles.css
└── templates/        # HTML files
    ├── index.html
    ├── login.html
    └── dashboard.html
```

## Epic to Architecture Mapping

*   **Epic 1: Core Application Setup and User Authentication** -> This epic will be implemented in the `main.py` file and the `templates` folder, with user data being stored in Firestore.
*   **Epic 2: AI-Powered Study Material Generation** -> This epic will involve the `main.py` file for the API endpoints, Firebase Storage for file uploads, and the integration with the Google Gemini and OpenAI APIs.

## Technology Stack Details

### Core Technologies

*   **Backend:** FastAPI
*   **Frontend:** HTML, CSS, JavaScript (served from FastAPI)
*   **Database:** Firestore
*   **Authentication:** Firebase Authentication
*   **File Storage:** Firebase Storage
*   **AI Service:** Google Gemini, OpenAI GPT-4

### Integration Points

*   The frontend will communicate with the backend via a REST API.
*   The backend will communicate with Firestore, Firebase Authentication, and Firebase Storage using the official Firebase Python libraries.
*   The backend will communicate with the Google Gemini and OpenAI APIs using their respective Python libraries.

## Implementation Patterns

*   **Naming Conventions:**
    *   Python variables and functions: `snake_case`
    *   HTML/CSS classes: `kebab-case`
    *   API endpoints: `/api/v1/...`
*   **Code Organization:**
    *   API routes will be organized into separate files in a `routers` directory as the application grows.
    *   Reusable functions will be placed in a `utils` directory.
*   **Error Handling:**
    *   The API will return standard HTTP status codes (e.g., 400 for bad requests, 500 for server errors).
    *   Error messages will be clear and concise.
*   **Logging:**
    *   The application will use the standard Python `logging` module.
    *   Logs will be written to the console.

## Data Architecture

*   **Users:** A `users` collection in Firestore will store user information (e.g., user ID, email).
*   **Files:** A `files` collection in Firestore will store metadata about the uploaded files (e.g., file name, user ID, storage path).
*   **Study Sets:** A `study_sets` collection in Firestore will store the generated content (summary, flashcards, quiz), linked to the user and the uploaded file.

## API Contracts

*   The API will use JSON for all request and response bodies.
*   A detailed API specification (e.g., using OpenAPI/Swagger) will be created as part of the implementation of Epic 2.

## Security Architecture

*   All API endpoints that require authentication will be protected using Firebase Authentication.
*   User passwords will not be stored in our database; they will be managed by Firebase Authentication.
*   All user data will be stored securely in Firestore and Firebase Storage, with access controls to ensure that only the owner of the data can access it.

### Credential Management

Sensitive API keys and service account paths (e.g., `GEMINI_API_KEY`, `FIREBASE_SERVICE_ACCOUNT_PATH`) are not hardcoded or committed to version control. Instead, they are loaded from environment variables at runtime. This ensures that credentials remain secure and are not exposed in the codebase, especially when working with public repositories.

## Performance Considerations

*   For the PoC, we will focus on a simple and clean implementation. Performance optimization will be a focus for future versions.
*   The AI content generation will be an asynchronous process to avoid blocking the main application thread.

## Deployment Architecture

*   For the PoC, the application can be deployed to a simple cloud service like Heroku or a small virtual private server (VPS).
*   A more robust deployment architecture (e.g., using Docker and a cloud provider like Google Cloud or AWS) will be considered for future versions.

## Development Environment

### Prerequisites

*   Python 3.9+
*   A Google Firebase project.
*   API keys for Google Gemini and OpenAI.

### Setup Commands

```bash
# 1. Clone the repository
git clone <repository_url>

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the application
uvicorn main:app --reload
```

## Architecture Decision Records (ADRs)

*   **ADR-001: Choice of Backend Framework:** We have chosen FastAPI as our backend framework due to its high performance, ease of use, and excellent support for asynchronous operations.
*   **ADR-002: Choice of Database and Authentication:** We have chosen to use Firebase Firestore and Firebase Authentication to leverage the Firebase ecosystem, which provides a secure and easy-to-use solution for data persistence and user management.
*   **ADR-003: Choice of File Storage:** We have chosen to use Firebase Storage for file uploads to keep our architecture consistent with the rest of the Firebase services.

---

_Generated by BMAD Decision Architecture Workflow v1.0_
_Date: 2025-11-01_
_For: BIP_
