<story-context id="bmad/bmm/workflows/4-implementation/story-context/template" v="1.0">
  <metadata>
    <epicId>1</epicId>
    <storyId>1.4</storyId>
    <title>user-dashboard</title>
    <status>drafted</status>
    <generatedAt>2025-11-05</generatedAt>
    <generator>BMAD Story Context Workflow</generator>
    <sourceStoryPath>C:\DEV\SG-Oslo\docs\stories\1-4-user-dashboard.md</sourceStoryPath>
  </metadata>

  <story>
    <asA>logged-in user</asA>
    <iWant>to see a personal dashboard</iWant>
    <soThat>I can upload files and see my saved study sets</soThat>
    <tasks>
- [ ] Create dashboard UI (HTML template).
- [ ] Create a protected `/dashboard` endpoint that requires authentication.
- [ ] Display a welcome message with the user's email.
- [ ] Add an "Upload File" button.
- [ ] Add a section for saved study sets.
</tasks>
  </story>

  <acceptanceCriteria>
1. A dashboard page is created that is only accessible to logged-in users.
2. The dashboard displays a welcome message to the user.
3. The dashboard contains a prominent "Upload File" button.
4. The dashboard has a section to display a list of saved study sets (this will be empty initially).
</acceptanceCriteria>

  <artifacts>
        <docs>
      <artifact>
        <path>docs/PRD.md</path>
        <title>studyBuddy-AI Product Requirements Document (PRD)</title>
        <section>UI Design Goals</section>
        <snippet>Dashboard (Home View): Central hub to upload new files, see progress indicators, and view a list of previously saved study sets.</snippet>
      </artifact>
      <artifact>
        <path>docs/architecture.md</path>
        <title>Decision Architecture</title>
        <section>Epic to Architecture Mapping</section>
        <snippet>Epic 1: Core Application Setup and User Authentication -> This epic will be implemented in the `main.py` file and the `templates` folder, with user data being stored in Firestore.</snippet>
      </artifact>
      <artifact>
        <path>docs/epics.md</path>
        <title>studyBuddy-AI - Epic Breakdown</title>
        <section>Story 1.4: User Dashboard</section>
        <snippet>As a logged-in user, I want to see a personal dashboard, So that I can upload files and see my saved study sets.</snippet>
      </artifact>
    </docs>
        <code>
      <artifact>
        <path>main.py</path>
        <kind>Python application file</kind>
        <symbol>app</symbol>
        <reason>Core FastAPI application setup with Firebase initialization, registration, and login logic.</reason>
      </artifact>
      <artifact>
        <path>templates/register.html</path>
        <kind>HTML template</kind>
        <symbol>registration form</symbol>
        <reason>Existing registration UI.</reason>
      </artifact>
      <artifact>
        <path>templates/login.html</path>
        <kind>HTML template</kind>
        <symbol>login form</symbol>
        <reason>Existing login UI.</reason>
      </artifact>
      <artifact>
        <path>templates/index.html</path>
        <kind>HTML template</kind>
        <symbol>index page</symbol>
        <reason>Main index page.</reason>
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
