# User Journey: Upload Document

## 1. User Story/Scenario
**User:** A university student, overwhelmed with course material, needs to quickly convert a lecture PDF into study tools.
**Goal:** Upload a PDF document and receive instant summaries, flashcards, and a quiz generated from its content.

## 2. Entry Point
The user can initiate the "Upload Document" journey from:
*   The "Upload Your Notes" button on the Home Page's Hero Section.
*   The "Upload File" option in the Hamburger Menu (accessible whether logged in or not).

## 3. Steps

### Step 3.1: Accessing the Upload Interface
1.  **User Action:** Clicks "Upload Your Notes" (Home Page) or "Upload File" (Hamburger Menu).
2.  **System Response:** The application navigates to an "Upload Zone" page/modal. This page features:
    *   A prominent drag-and-drop area.
    *   A "Browse Files" button for manual file selection.
    *   Supported file types listed (PDF, DOCX).
    *   Clear instructions.

### Step 3.2: Uploading the Document
1.  **User Action:**
    *   Option A: Drags and drops a supported file (e.g., `lecture_notes.pdf`) into the upload zone.
    *   Option B: Clicks "Browse Files", selects `lecture_notes.pdf` from their file system, and clicks "Open".
2.  **System Response:**
    *   A progress bar appears, indicating the file upload status.
    *   The file name is displayed next to the progress bar.
    *   Visual feedback (e.g., a checkmark or "Uploaded!") upon successful upload.
    *   If an unsupported file type is uploaded, an error message is displayed: "Unsupported file type. Please upload a PDF or DOCX file."
    *   If the file is too large (e.g., >50MB), a warning message is displayed: "File size exceeds limit (50MB). Please upload a smaller file."

### Step 3.3: Processing the Document
1.  **System Action:** Upon successful upload, the system automatically begins processing the document using AI.
2.  **System Response:**
    *   A "Processing..." message is displayed, possibly with a spinning loader or progress animation.
    *   Estimated time to completion may be shown if feasible.
    *   Message: "AI is analyzing your content and preparing your study tools."

### Step 3.4: Receiving Learning Tools
1.  **System Action:** AI completes processing.
2.  **System Response:**
    *   A success message is displayed: "Your study tools are ready!"
    *   The user is automatically redirected to a "Study Set View" page.
    *   This page features a tabbed interface or a "bento-style" grid to present:
        *   **Summary:** Condensed overview of the document.
        *   **Flashcards:** Interactive flashcards generated from key concepts.
        *   **Quiz:** An auto-generated quiz (defaulting to a 15-minute quick quiz).

### Step 3.5: Initial Review and Action
1.  **User Action:** The user reviews the generated Summary, Flashcards, and Quiz.
2.  **System Response:** Provides options to:
    *   Switch between tabs/sections (Summary, Flashcards, Quiz).
    *   Start Flashcard session.
    *   Start Quiz (with options to choose 15-min or 1-hour deep dive).
    *   Save Study Set.
    *   Download content.

## 4. Success Criteria
*   User successfully uploads a PDF or DOCX file.
*   AI processing completes without errors.
*   User is presented with a generated summary, flashcards, and a quiz.
*   User can easily navigate between the generated study tools.

## 5. Potential Pain Points/Considerations
*   **Long Processing Times:** User frustration if AI processing takes too long. Need clear progress indicators and potentially email notifications for very long processes.
*   **AI Quality:** Quality of generated content (summaries, flashcards, quiz questions) must be high to maintain user trust.
*   **File Upload Limits:** Clear communication of size and type limits.
*   **Error Handling:** User-friendly error messages and guidance for resolution.
*   **Empty State:** What happens if the uploaded document contains no extractable content?
*   **Pre-Login Upload:** If the user uploads a file before logging in, what is the flow to save/access it later? (Prompt to login/sign-up after processing).
