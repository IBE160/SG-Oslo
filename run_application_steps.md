Oppskrift for å kjøre applikasjonen

1.  **Install Python Dependencies (Corrected):**
    The `python-multipart` library was missing from the `requirements.txt`. I have now added it. Please run this command again to ensure all necessary libraries are installed.

    ```bash
    pip install -r requirements.txt
    ```

2.  **Firebase Service Account Key (Security Best Practice):**
    To address the security concern of not committing your Firebase key to a public repository, we will now read its path from an environment variable.

    **Steps to resolve:**
    a. **Download your Firebase Service Account Key:**
    _ Go to your Firebase project in the Firebase console.
    _ Click on "Project settings" (the gear icon).
    _ Go to the "Service accounts" tab.
    _ Click "Generate new private key" and then "Generate key". This will download a JSON file to your computer.
    b. **Place the JSON file:** Move the downloaded JSON file into your project's root directory (C:\DEV\SG-Oslo). You can rename it to something simple, like `serviceAccountKey.json`.
    c. **Set Environment Variable for Firebase Key Path (for Windows Command Prompt):**
    Instead of modifying `main.py` directly, you will set an environment variable that points to this file. **Replace `<PATH_TO_YOUR_FIREBASE_KEY_FILE>` with the actual absolute path to your `serviceAccountKey.json` file.**
    `bash
    set FIREBASE_SERVICE_ACCOUNT_PATH=C:\DEV\SG-Oslo\serviceAccountKey.json
    `
    _(Adjust the path if you placed the file elsewhere or named it differently.)_

3.  **Set Gemini API Key (for Windows Command Prompt):**
    **Replace `<YOUR_GEMINI_API_KEY>` with your actual key.** This needs to be done in the _same terminal session_ where you will run the application.

    ```bash
    set GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
    ```

    _(Note: Do NOT use quotes around the API key unless it contains spaces or special characters that need escaping. API keys typically do not.)_

4.  **Run the FastAPI Application:**
    This command starts the web server. You should see output indicating that Uvicorn is running.

    ```bash
    uvicorn main:app --reload
    ```

5.  **Access the Webpage:**
    Once Uvicorn is running (you'll see messages like 'Uvicorn running on http://127.0.0.1:8000'), open your web browser and go to:

    ```
    http://127.0.0.1:8000
    ```

    **Important:** Keep the terminal where Uvicorn is running open. If you close it, the application will stop. You can open a _new_ terminal if you need to run other commands, but the application's terminal must remain active.

Please try these updated steps, paying close attention to re-running `pip install -r requirements.txt` again, and let me know if you encounter any further issues.
