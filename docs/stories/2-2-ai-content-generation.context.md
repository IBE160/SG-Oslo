<story-context id="bmad/bmm/workflows/4-implementation/story-context/template" v="1.0">
  <metadata>
    <epicId>2</epicId>
    <storyId>2.2</storyId>
    <title>ai-content-generation</title>
    <status>drafted</status>
    <generatedAt>2025-11-08</generatedAt>
    <generator>BMAD Story Context Workflow</generator>
    <sourceStoryPath>C:\DEV\SG-Oslo\docs\stories\2-2-ai-content-generation.md</sourceStoryPath>
  </metadata>

  <story>
    <asA>user</asA>
    <iWant>the system to automatically generate a summary, flashcards, and a quiz after I upload a file</iWant>
    <soThat>I can quickly start studying</soThat>
    <tasks>
- [ ] Integrate Google Gemini API for text generation.
- [ ] Implement backend logic to trigger AI generation after file upload.
- [ ] Implement prompt engineering for summary generation.
- [ ] Implement prompt engineering for flashcard generation.
- [ ] Implement prompt engineering for quiz generation.
- [ ] Store generated content (summary, flashcards, quiz) in Firestore.
- [ ] Update UI to show AI processing status (progress indicator).
</tasks>
  </story>

  <acceptanceCriteria>
1. After a file is uploaded, the backend triggers the AI content generation process.
2. The system calls the AI service (Gemini/GPT-4) to generate the summary, flashcards, and quiz.
3. The generated content is stored in the Firestore database, associated with the user's account.
4. The user sees a progress indicator while the AI is working.
</acceptanceCriteria>

  <artifacts>
        <docs>
      <artifact>
        <path>docs/PRD.md</path>
        <title>studyBuddy-AI Product Requirements Document (PRD)</title>
        <section>Functional Requirements</section>
        <snippet>FR003: The system shall utilize AI (e.g., Google Gemini, OpenAI GPT-4) to generate summaries, flashcards, and quizzes from extracted text.</snippet>
      </artifact>
      <artifact>
        <path>docs/PRD.md</path>
        <title>studyBuddy-AI Product Requirements Document (PRD)</title>
        <section>Functional Requirements</section>
        <snippet>FR004: The system shall store generated study materials in a structured format.</snippet>
      </artifact>
      <artifact>
        <path>docs/architecture.md</path>
        <title>Decision Architecture</title>
        <section>Epic to Architecture Mapping</section>
        <snippet>Epic 2: AI-Powered Study Material Generation -> This epic will involve integrating with external AI services (Google Gemini/OpenAI GPT-4), implementing document parsing logic, and storing generated content in Firestore.</snippet>
      </artifact>
      <artifact>
        <path>docs/epics.md</path>
        <title>studyBuddy-AI - Epic Breakdown</title>
        <section>Story 2.2: AI Content Generation</section>
        <snippet>As a user, I want the system to automatically generate a summary, flashcards, and a quiz after I upload a file, So that I can quickly start studying.</snippet>
      </artifact>
      <artifact>
        <path>docs/tech-spec-epic-2.md</path>
        <title>Epic Technical Specification: AI-Powered Study Material Generation</title>
        <section>Services and Modules</section>
        <snippet>AI Generation Module: Orchestrates calls to Google Gemini (and potentially OpenAI GPT-4) APIs, sending extracted text and receiving AI-generated summaries, flashcards, and quizzes. Handles prompt engineering and response parsing.</snippet>
      </artifact>
      <artifact>
        <path>docs/tech-spec-epic-2.md</path>
        <title>Epic Technical Specification: AI-Powered Study Material Generation</title>
        <section>Services and Modules</section>
        <snippet>Firestore Integration Module: Manages all interactions with the Firestore database for Epic 2, including saving new study sets, retrieving existing ones, and updating document processing statuses.</snippet>
      </artifact>
      <artifact>
        <path>docs/tech-spec-epic-2.md</path>
        <title>Epic Technical Specification: AI-Powered Study Material Generation</title>
        <section>Data Models and Contracts</section>
        <snippet>StudySet (Firestore Collection): Defines the structure for storing generated content.</snippet>
      </artifact>
      <artifact>
        <path>docs/tech-spec-epic-2.md</path>
        <title>Epic Technical Specification: AI-Powered Study Material Generation</title>
        <section>Workflows and Sequencing</section>
        <snippet>AI Content Generation: The extracted text is sent to the AI Generation Module, which calls the Google Gemini API to produce the summary, flashcards, and quiz.</snippet>
      </artifact>
    </docs>
        <code>
      <artifact>
        <path>main.py</path>
        <kind>Python application file</kind>
        <symbol>app</symbol>
        <reason>Core FastAPI application setup, Firebase initialization, Firestore client, `POST /upload` endpoint, and `save_to_firestore` function. AI generation logic will be integrated here.</reason>
      </artifact>
      <artifact>
        <path>temp_uploads/</path>
        <kind>Directory</kind>
        <symbol>UPLOAD_DIR</symbol>
        <reason>Temporary storage for uploaded files, which will be the input for AI content generation.</reason>
      </artifact>
    </code>
        <dependencies>
      <dependency>
        <ecosystem>Python</ecosystem>
        <manifest>requirements.txt</manifest>
        <packages>
          <package>fastapi</package>
          <package>uvicorn</package>
          <package>firebase-admin</package>
          <package>pdfminer.six</package>
          <package>python-docx</package>
          <package>pypdf</package>
          <package>ftfy</package>
          <package>google-generativeai</package>
        </packages>
      </dependency>
    </dependencies>
  </artifacts>

  <constraints></constraints>
  <interfaces></interfaces>
  <tests>
    <standards></standards>
    <locations></locations>
    <ideas></ideas>
  </tests>
</story-context>
