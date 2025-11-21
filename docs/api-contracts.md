# API Contracts

This document outlines the API contracts for the StudyBuddy AI system, detailing the endpoints, request/response formats, and authentication mechanisms.

## 1. Authentication & User Service

**Base URL**: `/api/auth` (or similar for API Gateway routing)

### 1.1 User Registration

-   **Endpoint**: `/register`
-   **Method**: `POST`
-   **Description**: Registers a new user.
-   **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "strongpassword123",
      "fullName": "John Doe"
    }
    ```
-   **Response (Success - 201 Created)**:
    ```json
    {
      "message": "User registered successfully",
      "userId": "uuid-of-new-user"
    }
    ```
-   **Response (Error - 400 Bad Request)**:
    ```json
    {
      "error": "Email already exists"
    }
    ```

### 1.2 User Login

-   **Endpoint**: `/login`
-   **Method**: `POST`
-   **Description**: Authenticates a user and returns an authentication token.
-   **Request Body**:
    ```json
    {
      "email": "user@example.com",
      "password": "strongpassword123"
    }
    ```
-   **Response (Success - 200 OK)**:
    ```json
    {
      "message": "Login successful",
      "token": "jwt-authentication-token",
      "userId": "uuid-of-user"
    }
    ```
-   **Response (Error - 401 Unauthorized)**:
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

### 1.3 Get User Profile (Protected)

-   **Endpoint**: `/profile`
-   **Method**: `GET`
-   **Description**: Retrieves the authenticated user's profile information.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Response (Success - 200 OK)**:
    ```json
    {
      "userId": "uuid-of-user",
      "email": "user@example.com",
      "fullName": "John Doe",
      "createdAt": "2025-11-20T10:00:00Z"
    }
    ```
-   **Response (Error - 401 Unauthorized)**:
    ```json
    {
      "error": "Authentication required"
    }
    ```

## 2. Document Service

**Base URL**: `/api/documents` (or similar for API Gateway routing)

### 2.1 Upload Document (Protected)

-   **Endpoint**: `/upload`
-   **Method**: `POST`
-   **Description**: Uploads a new document for processing.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Request Body**: `multipart/form-data` with a file field named `document`.
    ```
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
    ...
    ------WebKitFormBoundary7MA4YWxkTrZu0gW
    Content-Disposition: form-data; name="document"; filename="my_lecture_notes.pdf"
    Content-Type: application/pdf

    <binary content of PDF file>
    ------WebKitFormBoundary7MA4YWxkTrZu0gW--
    ```
-   **Response (Success - 202 Accepted)**:
    ```json
    {
      "message": "Document upload initiated",
      "documentId": "uuid-of-new-document",
      "status": "PENDING"
    }
    ```
-   **Response (Error - 400 Bad Request)**:
    ```json
    {
      "error": "Invalid file type or size"
    }
    ```

### 2.2 Get User Documents (Protected)

-   **Endpoint**: `/`
-   **Method**: `GET`
-   **Description**: Retrieves a list of documents uploaded by the authenticated user.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Response (Success - 200 OK)**:
    ```json
    [
      {
        "documentId": "doc-uuid-1",
        "fileName": "lecture-1.pdf",
        "status": "PROCESSED",
        "uploadedAt": "2025-11-20T11:00:00Z"
      },
      {
        "documentId": "doc-uuid-2",
        "fileName": "assignment-guide.txt",
        "status": "PENDING",
        "uploadedAt": "2025-11-21T09:30:00Z"
      }
    ]
    ```
-   **Response (Error - 401 Unauthorized)**:
    ```json
    {
      "error": "Authentication required"
    }
    ```

### 2.3 Get Document Status (Protected)

-   **Endpoint**: `/{documentId}/status`
-   **Method**: `GET`
-   **Description**: Retrieves the processing status of a specific document.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **URL Parameters**: `documentId` (UUID)
-   **Response (Success - 200 OK)**:
    ```json
    {
      "documentId": "doc-uuid-1",
      "status": "PROCESSED"
    }
    ```
-   **Response (Error - 404 Not Found)**:
    ```json
    {
      "error": "Document not found or not owned by user"
    }
    ```

## 3. AI Service

**Base URL**: `/api/ai` (or similar for API Gateway routing)

### 3.1 Ask Question (Protected)

-   **Endpoint**: `/question`
-   **Method**: `POST`
-   **Description**: Asks a question about a specific document.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Request Body**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "question": "What are the main topics discussed in this document?"
    }
    ```
-   **Response (Success - 200 OK)**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "question": "What are the main topics discussed in this document?",
      "answer": "The main topics discussed are X, Y, and Z."
    }
    ```
-   **Response (Error - 400 Bad Request)**:
    ```json
    {
      "error": "Document not processed or invalid question"
    }
    ```

### 3.2 Summarize Document (Protected)

-   **Endpoint**: `/summarize`
-   **Method**: `POST`
-   **Description**: Generates a summary of a specific document.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Request Body**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "summaryLength": "short" // Optional: "short", "medium", "long"
    }
    ```
-   **Response (Success - 200 OK)**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "summary": "This document provides a concise overview of..."
    }
    ```
-   **Response (Error - 400 Bad Request)**:
    ```json
    {
      "error": "Document not processed"
    }
    ```

### 3.3 Generate Quiz (Protected)

-   **Endpoint**: `/quiz`
-   **Method**: `POST`
-   **Description**: Generates a quiz based on the content of a specific document.
-   **Headers**: `Authorization: Bearer jwt-authentication-token`
-   **Request Body**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "numQuestions": 5, // Optional: number of questions
      "questionType": "multiple_choice" // Optional: "multiple_choice", "true_false", "short_answer"
    }
    ```
-   **Response (Success - 200 OK)**:
    ```json
    {
      "documentId": "uuid-of-processed-document",
      "quiz": [
        {
          "question": "What is the capital of France?",
          "type": "multiple_choice",
          "options": ["Berlin", "Madrid", "Paris", "Rome"],
          "correctAnswer": "Paris"
        },
        {
          "question": "The Earth is flat. (True/False)",
          "type": "true_false",
          "correctAnswer": "False"
        }
      ]
    }
    ```
-   **Response (Error - 400 Bad Request)**:
    ```json
    {
      "error": "Document not processed"
    }
    ```