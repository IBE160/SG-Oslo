# studyBuddy-AI - Epic Breakdown

**Author:** BIP
**Date:** 2025-11-01
**Project Level:** 2
**Target Scale:** MVP for a class project

---

## Overview

This document provides the detailed epic breakdown for studyBuddy-AI, expanding on the high-level epic list in the [PRD](./PRD.md).

Each epic includes:

- Expanded goal and value proposition
- Complete story breakdown with user stories
- Acceptance criteria for each story
- Story sequencing and dependencies

**Epic Sequencing Principles:**

- Epic 1 establishes foundational infrastructure and initial functionality
- Subsequent epics build progressively, each delivering significant end-to-end value
- Stories within epics are vertically sliced and sequentially ordered
- No forward dependencies - each story builds only on previous work

---

## Epic 1: Core Application Setup and User Authentication

**Goal:** Establish the foundational infrastructure of the application, including the backend server, database, and user authentication system. This epic will create the basic "shell" of the application, allowing users to register, log in, and view their personal dashboard.

### Stories

**Story 1.1: Project Setup**

As a developer,
I want to set up the initial project structure with a FastAPI backend and a simple UI,
So that we have a foundation to build upon.

**Acceptance Criteria:**
1. A new Git repository is created for the project.
2. A virtual environment for Python is set up.
3. FastAPI is installed and a basic "Hello World" endpoint is working.
4. A simple HTML template is created for the main page.

**Prerequisites:** None

---

**Story 1.2: User Registration**

As a new user,
I want to be able to register for an account using my email,
So that I can access the application.

**Acceptance Criteria:**
1. A registration page is created with fields for email and password.
2. User registration is handled by Firebase Authentication.
3. Upon successful registration, the user is redirected to the login page.

**Prerequisites:** Story 1.1

---

**Story 1.3: User Login**

As a registered user,
I want to be able to log in to the application,
So that I can access my dashboard.

**Acceptance Criteria:**
1. A login page is created with fields for email and password.
2. User login is handled by Firebase Authentication.
3. Upon successful login, the user is redirected to their dashboard.

**Prerequisites:** Story 1.2

---

**Story 1.4: User Dashboard**

As a logged-in user,
I want to see a personal dashboard,
So that I can upload files and see my saved study sets.

**Acceptance Criteria:**
1. A dashboard page is created that is only accessible to logged-in users.
2. The dashboard displays a welcome message to the user.
3. The dashboard contains a prominent "Upload File" button.
4. The dashboard has a section to display a list of saved study sets (this will be empty initially).

**Prerequisites:** Story 1.3

---

## Epic 2: AI-Powered Study Material Generation

**Goal:** Implement the core functionality of the application, allowing users to upload documents and receive AI-generated study materials (summaries, flashcards, and quizzes). This epic will deliver the main value proposition of the application.

### Stories

**Story 2.1: File Upload**

As a logged-in user,
I want to be able to upload a PDF or DOCX file,
So that I can generate study materials from it.

**Acceptance Criteria:**
1. The user can select a file from their computer.
2. The file is uploaded to the server.
3. The system validates the file type and size.
4. The user sees a progress indicator during the upload.
5. The user receives a confirmation message upon successful upload.

**Prerequisites:** Story 1.4

---

**Story 2.2: AI Content Generation**

As a user,
I want the system to automatically generate a summary, flashcards, and a quiz after I upload a file,
So that I can quickly start studying.

**Acceptance Criteria:**
1. After a file is uploaded, the backend triggers the AI content generation process.
2. The system calls the AI service (Gemini/GPT-4) to generate the summary, flashcards, and quiz.
3. The generated content is stored in the Firestore database, associated with the user's account.
4. The user sees a progress indicator while the AI is working.

**Prerequisites:** Story 2.1

---

**Story 2.3: Display Generated Content**

As a user,
I want to be able to view the generated summary, flashcards, and quiz,
So that I can start studying.

**Acceptance Criteria:**
1. The generated content is displayed to the user on the "Study Session" page.
2. The summary is displayed as a block of text.
3. The flashcards are displayed in an interactive format (e.g., clickable to reveal the answer).
4. The quiz is displayed as a series of multiple-choice questions.

**Prerequisites:** Story 2.2

---

**Story 2.4: Quiz Interaction**

As a user,
I want to be able to answer the quiz questions and get immediate feedback,
So that I can test my knowledge.

**Acceptance Criteria:**
1. The user can select an answer for each quiz question.
2. After selecting an answer, the user is immediately shown whether their answer was correct or not.
3. The user's score is tracked as they go through the quiz.

**Prerequisites:** Story 2.3

---

**Story 2.5: Save Study Set**

As a user,
I want to be able to save a generated study set,
So that I can access it later.

**Acceptance Criteria:**
1. There is a "Save" button on the "Study Session" page.
2. When the user clicks "Save", the generated content is permanently saved to their account.
3. The saved study set appears in the user's dashboard.

**Prerequisites:** Story 2.3

---

## Story Guidelines Reference

**Story Format:**

```
**Story [EPIC.N]: [Story Title]**

As a [user type],
I want [goal/desire],
So that [benefit/value].

**Acceptance Criteria:**
1. [Specific testable criterion]
2. [Another specific criterion]
3. [etc.]

**Prerequisites:** [Dependencies on previous stories, if any]
```

**Story Requirements:**

- **Vertical slices** - Complete, testable functionality delivery
- **Sequential ordering** - Logical progression within epic
- **No forward dependencies** - Only depend on previous work
- **AI-agent sized** - Completable in 2-4 hour focused session
- **Value-focused** - Integrate technical enablers into value-delivering stories

---

**For implementation:** Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown.
