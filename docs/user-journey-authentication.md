# User Journey: Authentication (Sign Up & Login)

## 1. User Story/Scenario
**User:** A new user who has just discovered StudyBuddy AI and wants to save their generated study sets.
**Goal:** Create a new account or log into an existing one to access and save personalized content.

## 2. Entry Point
The user can initiate the "Authentication" journey from:
*   The "Login / Sign Up" button in the Top Menu.
*   The "Login" option in the Hamburger Menu.
*   A prompt to "Save Study Set" after generating content as a guest.
*   The "Get Started Free" button on the Home Page's CTA Section.

## 3. Steps

### 3.1 User Registration (Sign Up)
1.  **User Action:** Clicks "Sign Up" or "Get Started Free".
2.  **System Response:** Navigates to the "Login / Sign Up" page, with the "Sign Up" form active. The page is simple and minimal, with a soft pastel background.
3.  **User Action:** Fills in the registration form:
    *   Email
    *   Password
    *   Confirm Password
4.  **System Response:**
    *   Provides real-time validation feedback (e.g., "Password must be at least 8 characters").
5.  **User Action:** Clicks the "Sign Up" button.
6.  **System Response:**
    *   Displays a success message: "Welcome to StudyBuddy AI! Please check your email to verify your account."
    *   Logs the user in and redirects them to their dashboard or the page they were on previously.
    *   (Optional) Sends a verification email.

### 3.2 User Login
1.  **User Action:** Clicks "Login".
2.  **System Response:** Navigates to the "Login / Sign Up" page, with the "Login" form active.
3.  **User Action:** Fills in the login form:
    *   Email
    *   Password
4.  **System Response:**
    *   Provides real-time validation feedback (e.g., "Invalid email format").
5.  **User Action:** Clicks the "Login" button.
6.  **System Response (Successful Login):**
    *   Redirects the user to their dashboard or the last page they visited.
    *   The Top Menu updates to show a "User Dropdown" with their profile icon/initials.
7.  **System Response (Failed Login):**
    *   Displays an error message: "Invalid email or password."
    *   Provides a "Forgot Password?" link.

### 3.3 Cloud Service Integration
1.  **User Action:** On the "Sign Up" or "Login" page, clicks a button like "Connect with Google Drive" or "Connect with OneDrive".
2.  **System Response:**
    *   Initiates an OAuth flow with the selected cloud service.
    *   Upon successful authorization, the user is either registered or logged in and redirected to their dashboard.

## 4. Success Criteria
*   New user can successfully create an account and log in.
*   Existing user can successfully log in.
*   User receives clear feedback on success or failure.
*   User can connect their cloud service account for saving materials.

## 5. Potential Pain Points/Considerations
*   **Password Complexity:** Balancing security with user convenience.
*   **Verification Email:** Ensuring the email is delivered promptly and doesn't end up in spam.
*   **Social Login Errors:** Handling errors from OAuth providers gracefully.
*   **"Forgot Password" Flow:** A simple and secure process for password recovery.
*   **Session Management:** How long does a user stay logged in?
*   **Privacy:** Clear communication about data privacy and how cloud service integration works.
