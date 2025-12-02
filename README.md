# StudyBuddy AI

A smart learning assistant that transforms your study materials into interactive summaries, flashcards, and quizzes using the power of AI.

## 🚀 Key Features

- **AI-Powered Content Generation:** Automatically generate concise summaries, interactive flashcards, and multiple-choice quizzes from your documents.
- **Versatile File Uploads:** Supports both PDF and DOCX file formats for your lecture notes, articles, and readings.
- **Secure User Authentication:** Safe and secure user registration and login system.
- **Study Set Organization:** Organize your study materials with custom categories.
- **Progress Tracking:** Visualize your quiz scores over time with a personal progress chart for each study set.
- **Flexible Quizzing:** Choose your quiz length (short, medium, or full) to fit your study session.

## 🛠️ Technology Stack

- **Backend:** Python, **FastAPI**, Uvicorn
- **AI & Cloud Services:**
  - **Google Gemini:** For all AI content generation.
  - **Firebase Authentication:** For user management.
  - **Firestore:** NoSQL database for data storage.
- **Frontend:**
  - **Jinja2:** For server-side HTML templating.
  - **Tailwind CSS:** For styling and responsive design.
  - **Chart.js:** For data visualization (progress charts).
  - **Showdown.js:** For rendering Markdown content.
- **Document Parsing:** `pdfminer.six`, `python-docx`
- **Version Control:** Git, GitHub

## ⚙️ Setup and Installation

Follow these steps to get the application running locally.

### 1. Prerequisites

- Python 3.9+
- Access to Google Cloud with the Gemini API enabled.
- A Firebase project with Authentication and Firestore enabled.

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 3. Set Up Virtual Environment

It is highly recommended to use a virtual environment.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install all required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

You need to set up your credentials for Google services.

1.  Create a file named `.env` in the root of the project.
2.  Add the following variables, replacing the placeholders with your actual credentials:

    ```
    # Path to your Firebase service account JSON key file
    FIREBASE_SERVICE_ACCOUNT_PATH="path/to/your/firebase-service-account-key.json"

    # Your Google API key for the Gemini model
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

### 6. Set Up Firestore Indexes

This application requires two composite indexes in Firestore to function correctly. The application will fail on the first run and provide you with direct links to create these indexes.

1.  Run the application for the first time.
2.  Attempt to navigate to the dashboard. The server will log an error containing a `https://console.firebase.google.com/...` link for the `categories` collection.
3.  Open the link and create the required index.
4.  After the first index is enabled, restart the server, go to the dashboard, and click on a study set to view the progress chart. This will cause another server error with a second link.
5.  Open the second link and create the index for the `quiz_results` collection.
6.  Wait for both indexes to be **"Enabled"** in the Firebase console.

### 7. Run the Application

Once the setup is complete, run the application using Uvicorn.

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## 📖 Usage

1.  **Register/Login:** Create a new account or log in.
2.  **Upload Document:** On the dashboard, upload a PDF or DOCX file. The AI will process it and generate a new study set.
3.  **Organize:** Assign your new study set to a category.
4.  **View Progress:** Click on a study set to view your quiz progress over time.
5.  **Study:** Click "Go to Study Session" to view the summary, flip through flashcards, and take a quiz of your chosen length.
