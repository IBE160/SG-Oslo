# Data Models

This document defines the data schema for the core entities in the StudyBuddy AI system.

## 1. User Model

Represents a user of the application.

-   **Table Name**: `users`

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Not Null | Unique identifier for the user. |
| `email` | `VARCHAR(255)` | Unique, Not Null | User's email address for login. |
| `password_hash`| `VARCHAR(255)`| Not Null | Hashed password for authentication. |
| `full_name` | `VARCHAR(255)`| | User's full name. |
| `created_at` | `TIMESTAMPZ` | Not Null, Default `NOW()`| Timestamp of when the user was created. |
| `updated_at` | `TIMESTAMPZ` | Not Null, Default `NOW()`| Timestamp of the last update. |

## 2. Document Model

Represents a document uploaded by a user.

-   **Table Name**: `documents`

| Column | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Not Null | Unique identifier for the document. |
| `user_id` | `UUID` | Foreign Key (users.id) | The user who uploaded the document. |
| `file_name` | `VARCHAR(255)`| Not Null | Original name of the uploaded file. |
| `storage_key` | `VARCHAR(1024)`| Not Null, Unique | The key/path to the file in object storage. |
| `status` | `VARCHAR(50)` | Not Null, Default `'PENDING'`| Processing status (e.g., PENDING, PROCESSED, FAILED). |
| `created_at` | `TIMESTAMPZ` | Not Null, Default `NOW()`| Timestamp of when the document was uploaded. |
| `updated_at` | `TIMESTAMPZ` | Not Null, Default `NOW()`| Timestamp of the last update. |
