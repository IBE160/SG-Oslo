# User Journey: Take a Quiz

## 1. User Story/Scenario
**User:** A student who has just generated a quiz from their notes, or is returning to study, wants to test their knowledge and track their progress.
**Goal:** Successfully complete a quiz and view their results and performance insights.

## 2. Entry Point
The user can initiate the "Take a Quiz" journey from:
*   The "Quiz" tab/section on the "Study Set View" page immediately after generating study tools.
*   A "Start Quiz" button on a saved study set's detail page (e.g., from their dashboard or a content category).
*   The "Create Quiz" option in the Hamburger Menu (which would lead to selecting/uploading content, then generating a quiz).

## 3. Steps

### Step 3.1: Selecting a Quiz
1.  **User Action (Scenario A: Freshly Generated Quiz):** User is on the "Study Set View" page, on the "Quiz" tab/section.
    *   **System Response:** Displays the generated quiz. Options to choose quiz length (15-Min Quiz / 1-Hour Deep Dive). Default is 15-Min Quiz.
2.  **User Action (Scenario B: Saved Quiz):** User navigates to a specific quiz from their dashboard or content categories.
    *   **System Response:** Displays the quiz details (e.g., source document, topic, previous attempts). Options to choose quiz length (15-Min Quiz / 1-Hour Deep Dive).

### Step 3.2: Starting the Quiz
1.  **User Action:** Selects desired quiz length (if applicable) and clicks "Start Quiz".
2.  **System Response:**
    *   The quiz interface loads.
    *   Displays the first question, timer (if applicable), and progress indicator (e.g., "1 of 10").
    *   Clear options to select an answer (e.g., multiple choice, true/false).

### Step 3.3: Answering Questions
1.  **User Action:** Reads the question, considers options, and selects an answer. Clicks "Next Question" or an equivalent navigation button.
2.  **System Response:**
    *   Records the answer.
    *   Moves to the next question.
    *   Updates the progress indicator.
    *   If applicable, provides immediate feedback (correct/incorrect) or saves feedback for end-of-quiz review.

### Step 3.4: Completing the Quiz
1.  **User Action:** Answers the last question and clicks "Submit Quiz" or "Finish".
2.  **System Response:**
    *   Confirms quiz completion.
    *   Calculates and displays the score.
    *   Navigates to a "Quiz Results" page.

### Step 3.5: Reviewing Results
1.  **System Response (Quiz Results Page):**
    *   Displays overall score and percentage.
    *   Shows a breakdown of correct/incorrect answers.
    *   Allows user to review each question with the correct answer and their chosen answer.
    *   Highlights areas of strength and weakness (if advanced analytics are implemented).
    *   Provides options to:
        *   "Retake Quiz"
        *   "Review Flashcards for this Topic"
        *   "Go back to Study Set"
        *   "Save Results" (if not automatically saved)
        *   "Share Results" (if applicable)

## 4. Success Criteria
*   User can easily select and start a quiz.
*   User can navigate through quiz questions and submit answers.
*   User receives a score and can review their performance.
*   User can choose different quiz types (15-min / 1-hour).

## 5. Potential Pain Points/Considerations
*   **Navigation during quiz:** Clear indication of current question, remaining questions, and time.
*   **Saving Progress:** What happens if the user leaves the quiz mid-way? Autosave feature?
*   **Question Quality:** AI-generated questions must be relevant and accurate.
*   **Feedback Mechanism:** How is feedback provided (immediate vs. end-of-quiz)?
*   **Accessibility:** Ensuring quiz interface is usable for all students (e.g., keyboard navigation).
*   **Integration with Flashcards/Summary:** Seamless linking between quiz results and other study tools for targeted review.
