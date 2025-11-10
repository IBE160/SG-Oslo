<story-context id="bmad/bmm/workflows/4-implementation/story-context/template" v="1.0">
  <metadata>
    <epicId>2</epicId>
    <storyId>2.5</storyId>
    <title>save-study-set</title>
    <status>drafted</status>
    <generatedAt>2025-11-08</generatedAt>
    <generator>BMAD Story Context Workflow</generator>
    <sourceStoryPath>C:\DEV\SG-Oslo\docs\stories\2-5-save-study-set.md</sourceStoryPath>
  </metadata>

  <story>
    <asA>user</asA>
    <iWant>to be able to explicitly save a generated study set</iWant>
    <soThat>I can access it later</soThat>
    <tasks>
- [ ] Add a "Save Study Set" button to `templates/study_session.html`.
- [ ] Implement a backend endpoint (`POST /save-study-set`) to handle saving the study set.
- [ ] The backend endpoint should update the status of the study set in Firestore from "completed" to "saved" (or similar).
- [ ] Display a confirmation message to the user after saving.
</tasks>
  </story>

  <acceptanceCriteria>
1. On the "Study Session" page, there is a "Save Study Set" button.
2. Clicking the "Save Study Set" button persists the current study set (summary, flashcards, quiz) to the user's saved study sets in Firestore.
3. The user receives confirmation that the study set has been saved.
</acceptanceCriteria>

  <artifacts>
        <docs>
      <artifact>
        <path>docs/PRD.md</path>
        <title>studyBuddy-AI Product Requirements Document (PRD)</title>
        <section>Functional Requirements</section>
        <snippet>FR004: The system shall store generated study materials in a structured format.</snippet>
      </artifact>
      <artifact>
        <path>docs/PRD.md</path>
        <title>studyBuddy-AI Product Requirements Document (PRD)</title>
        <section>Functional Requirements</section>
        <snippet>FR008: The system shall allow users to explicitly save generated study sets for later retrieval.</snippet>
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
        <section>Story 2.5: Save Study Set</section>
        <snippet>As a user, I want to be able to explicitly save a generated study set, So that I can access it later.</snippet>
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
        <section>APIs and Interfaces</section>
        <snippet>`POST /save-study-set`: Endpoint to mark a generated study set as saved by the user.</snippet>
      </artifact>
      <artifact>
        <path>docs/tech-spec-epic-2.md</path>
        <title>Epic Technical Specification: AI-Powered Study Material Generation</title>
        <section>Workflows and Sequencing</section>
        <snippet>Study Set Management: User can explicitly save a generated study set, which updates its status in Firestore.</snippet>
      </artifact>
    </docs>
        <code>
      <artifact>
        <path>main.py</path>
        <kind>Python application file</kind>
        <symbol>app</symbol>
        <reason>Core FastAPI application setup, Firebase initialization, Firestore client, `POST /upload` endpoint, `save_to_firestore` function, `generate_content_with_gemini` function, and `GET /study-sets/{study_set_id}` endpoint. A new endpoint for saving study sets will be added here.</reason>
      </artifact>
      <artifact>
        <path>templates/study_session.html</path>
        <kind>HTML template</kind>
        <symbol>study session UI</symbol>
        <reason>The "Study Session" page where the "Save Study Set" button will be added.</reason>
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
