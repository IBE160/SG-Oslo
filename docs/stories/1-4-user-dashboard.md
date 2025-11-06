# Story 1.4: User Dashboard

Status: drafted

## Story

As a logged-in user,
I want to see a personal dashboard,
so that I can upload files and see my saved study sets.

## Acceptance Criteria

1. A dashboard page is created that is only accessible to logged-in users.
2. The dashboard displays a welcome message to the user.
3. The dashboard contains a prominent "Upload File" button.
4. The dashboard has a section to display a list of saved study sets (this will be empty initially).

## Tasks / Subtasks

- [x] Create dashboard UI (HTML template).

### Completion Notes List

- Created `templates/dashboard.html` with a basic dashboard layout.
- [x] Create a protected `/dashboard` endpoint that requires authentication.

### Completion Notes List

- Created `templates/dashboard.html` with a basic dashboard layout.
- Updated `main.py` to include a protected `/dashboard` endpoint with session management.
- [x] Display a welcome message with the user's email.
- [x] Add an "Upload File" button.
- [x] Add a section for saved study sets.

## Dev Notes

- The dashboard should be the main landing page after login.
- The list of saved study sets will be populated in a later story.

### Project Structure Notes

- Dashboard UI will be in the `templates` directory.
- The `/dashboard` endpoint will be in `main.py`.

### References

- [Source: docs/epics.md#Epic-1-Core-Application-Setup-and-User-Authentication]

## Dev Agent Record

Status: done

### Completion Notes
**Completed:** 2025-11-05
**Definition of Done:** All acceptance criteria met, code reviewed, tests passing

### File List
- main.py (modified)
- templates/dashboard.html (new)
