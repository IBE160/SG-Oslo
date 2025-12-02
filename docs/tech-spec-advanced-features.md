# Tech Spec: Advanced Study Features (Epic 3)

**Version:** 1.0
**Status:** Draft
**Date:** 2025-12-02

## 1. Overview

This document outlines the technical implementation plan for adding advanced features to StudyBuddy AI, including content categorization, user progression tracking, and flexible session types. These features correspond to ideas documented in the `product-brief-studyBuddy-AI-2025-11-01.md` and `brainstorming-session-results-2025-11-15.md`.

## 2. Feature: Content Categorization

### 2.1. User Stories

*   **As a user,** I want to create custom categories (e.g., "Biology 101", "History Exam") to organize my study sets.
*   **As a user,** I want to assign a study set to a category upon creation or from my dashboard.
*   **As a user,** I want to filter my list of study sets by category on the dashboard.
*   **As a user,** I want to delete categories I no longer need.

### 2.2. Backend Changes

#### 2.2.1. Data Models (Firestore)

1.  **New Collection: `categories`**
    *   `id` (string, auto-generated)
    *   `userId` (string, reference to `users` collection)
    *   `name` (string, e.g., "Biology 101")
    *   `createdAt` (timestamp)

2.  **Modification to `study_sets` Collection**
    *   Add new field: `categoryId` (string, nullable, reference to `categories` collection).

#### 2.2.2. API Endpoints

*   `POST /categories`
    *   **Body:** `{ "name": "New Category Name" }`
    *   **Auth:** Required
    *   **Action:** Creates a new category for the authenticated user.
    *   **Returns:** The new category object.

*   `GET /categories`
    *   **Auth:** Required
    *   **Action:** Retrieves all categories for the authenticated user.
    *   **Returns:** An array of category objects.

*   `PUT /study-sets/{studySetId}/category`
    *   **Body:** `{ "categoryId": "cat_id_123" }`
    *   **Auth:** Required
    *   **Action:** Assigns or un-assigns (if `categoryId` is null) a study set to a category.
    *   **Returns:** Success/failure message.

*   `DELETE /categories/{categoryId}`
    *   **Auth:** Required
    *   **Action:** Deletes a category. This should also set `categoryId` to `null` for all associated study sets.
    *   **Returns:** Success/failure message.

### 2.3. Frontend Changes

*   **Dashboard (`templates/dashboard.html`)**
    *   Add a "Manage Categories" button that opens a modal.
    *   The modal will contain a form to create new categories and a list to delete existing ones.
    *   Add a dropdown filter at the top of the "Your Study Sets" list to filter by category.
    *   For each study set in the list, add a small dropdown to assign/change its category.

---

## 3. Feature: Progression Tracking

### 3.1. User Story

*   **As a user,** I want to see my quiz scores for a specific study set over time, so I can track my learning progress.

### 3.2. Backend Changes

#### 3.2.1. Data Models (Firestore)

1.  **New Collection: `quiz_results`**
    *   `id` (string, auto-generated)
    *   `userId` (string, reference to `users`)
    *   `studySetId` (string, reference to `study_sets`)
    *   `score` (number, e.g., 85.5 for 85.5%)
    *   `completedAt` (timestamp)
    *   `questionCount` (number)
    *   `correctCount` (number)

#### 3.2.2. API Endpoints

*   `POST /quiz-results`
    *   **Body:** `{ "studySetId": "set_id_123", "score": 85.5, "questionCount": 20, "correctCount": 17 }`
    *   **Auth:** Required
    *   **Action:** Saves the result of a completed quiz.
    *   **Returns:** The new quiz result object.

*   `GET /study-sets/{studySetId}/progress`
    *   **Auth:** Required
    *   **Action:** Retrieves all `quiz_results` for a specific study set, ordered by date.
    *   **Returns:** An array of quiz result objects.

### 3.3. Frontend Changes

*   **Study Session Page (`templates/study_session.html`)**
    *   When a quiz is completed, the frontend will calculate the score and `POST` it to `/quiz-results`.

*   **Dashboard (`templates/dashboard.html`)**
    *   When a user clicks on a study set, instead of immediately redirecting, the content area (`study-set-content-display`) could expand to show a "Progress Chart" tab alongside the "Study" button.
    *   The "Progress Chart" tab will fetch data from `/study-sets/{studySetId}/progress` and render a line chart showing score vs. time.
    *   A JavaScript charting library (e.g., Chart.js) will be needed.

---

## 4. Feature: Flexible Session Types

### 4.1. User Story

*   **As a user,** when starting a quiz, I want to choose between a short quiz (e.g., 5 questions) and the full quiz, so I can study based on how much time I have.

### 4.2. Backend Changes

#### 4.2.1. API Endpoints

*   **Modification to `GET /get-study-set-content/{studySetId}/quiz`**
    *   Add an optional query parameter: `?limit=<number>`.
    *   **Action:** If `limit` is provided, the backend returns a random subset of the specified number of questions from the full quiz. If not provided, it returns all questions.

### 4.3. Frontend Changes

*   **Dashboard or Study Session Page**
    *   When a user initiates a quiz for a study set, a small modal or a set of buttons will appear.
    *   **Options:** "Quick Quiz (5 Questions)", "Medium Quiz (10 Questions)", "Full Quiz".
    *   The frontend will then call the quiz API with the corresponding `limit` parameter.
    *   The quiz view will be updated to handle fetching and displaying the selected number of questions.

---

## 5. High-Level Task Breakdown

1.  **Backend - Models:** Implement the `categories` and `quiz_results` collections in Firestore. Update the `study_sets` model.
2.  **Backend - APIs:** Build and test all new endpoints for Categories and Progress Tracking.
3.  **Backend - Logic:** Update the quiz-serving logic to handle the `limit` parameter.
4.  **Frontend - Categories:** Implement the category management modal and filtering on the dashboard.
5.  **Frontend - Session Types:** Implement the quiz type selection modal.
6.  **Frontend - Progress Chart:** Integrate a charting library and build the progress visualization component on the dashboard.
7.  **End-to-End Testing:** Test the full user flow for all three features.
