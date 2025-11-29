# Component Inventory - StudyBuddy AI Frontend

This document lists the major UI components required for the StudyBuddy AI frontend application, grouped by functional areas. This inventory will serve as a guide for development and design.

## 1. Layout & Navigation Components

-   **Header**: Contains the application title/logo, user avatar/menu, and global navigation links.
-   **Sidebar/Navigation Menu**: Provides links to different sections of the application (e.g., Dashboard, My Documents, Settings).
-   **Footer**: Contains copyright information, links to privacy policy, terms of service, etc. (optional for initial MVP).
-   **Main Content Area**: The dynamic area where different views and components are rendered.

## 2. Authentication Components

-   **Login Form**: Allows users to log in with email and password.
-   **Registration Form**: Allows new users to create an account.
-   **Forgot Password/Reset Password Forms**: (Optional for initial MVP) Components for password recovery.

## 3. Document Management Components

-   **Document Upload Form/Button**: Interface for users to upload new documents (e.g., drag-and-drop area, file input).
-   **Document List/Table**: Displays a list of uploaded documents with their status, filename, and options (e.g., view, delete).
-   **Document Card/Item**: A reusable component for displaying individual document details within the list.
-   **Document Viewer**: (Basic) A component to display the content of a document (e.g., PDF viewer, text display).

## 4. AI Interaction Components

-   **Chat Interface/Question Input**: An input field and display area for users to ask questions about a document.
-   **Answer Display**: Displays the AI-generated answers or summaries.
-   **Quiz Generation Form**: Allows users to specify parameters for quiz generation (e.g., number of questions, type).
-   **Quiz Display/Player**: Renders the generated quiz and handles user interaction (e.g., selecting answers, submitting).
-   **Summary Display**: Displays the AI-generated summary of a document.

## 5. General UI Elements

-   **Button**: Reusable button component.
-   **Input Field (Text, Password, etc.)**: Reusable input components.
-   **Dropdown/Select**: Reusable dropdown component.
-   **Loading Spinner/Indicator**: Visual feedback for ongoing operations.
-   **Alert/Notification Message**: Displays success, error, or informational messages.
-   **Modal/Dialog**: Used for confirmations, additional forms, etc.
