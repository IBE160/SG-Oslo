# ibe160 UX Design Specification

_Created on Wednesday, November 19, 2025 by BIP_
_Generated using BMad Method - Create UX Design Workflow v1.0_

---

## Executive Summary

StudyBuddy AI is an intelligent web application designed for university and college students. Its core purpose is to automate the creation of study materials (summaries, flashcards, quizzes) from uploaded text-based PDF and DOCX files. The application aims to save students significant time on manual study preparation, improve learning efficiency, and enhance understanding through active learning methods. Future visions include AI-driven topic maps, micro-learning, personalized tutoring, and integration with user-owned cloud storage.

The primary users are tech-savvy university and college students overwhelmed by large volumes of course material. They spend excessive time on manual tasks like summarizing and creating flashcards, which hinders deep learning. They seek an efficient, intuitive tool that provides high-quality, structured study aids to help them save time, improve academic results, and focus on active learning. They appreciate tools that feel like a personal tutor and offer engaging, productive experiences.

---

## 1. Design System Foundation

### 1.1 Design System Choice

**Chosen Design System:** Bootstrap (with Material Design Principles and Custom Theming)

**Rationale:** This approach offers an excellent balance of robust, accessible components and styling flexibility, which is crucial for achieving a "sleek, nice, and easy to click around" experience for all users. It integrates efficiently with a "simple web UI with FastAPI HTML templates" for an MVP, allowing us to apply the clean, intuitive visual language of Material Design for the desired aesthetic.

---

## 2. Core User Experience & Website Content Structure

### 2.1 Defining Experience

**Core Experience:** The core experience is centered on users uploading a document and instantly receiving a complete set of study materials (summary, flashcards, quiz) with minimal effort. It is designed to be intuitive for all users, regardless of their technical expertise. A key aspect of the experience is a sleek, visually appealing design with a user-friendly and easy-to-navigate interface.

**Platform:** The application will be a web application accessible through modern web browsers.

**Desired Emotional Response:** The application aims to evoke a range of positive emotions in the user. The primary goal is to make users feel **in control** of their study material, **efficient** with their time, and **productive** in their learning. The experience should also be **fun** and **encouraging**, leading to a tangible **sense of achievement**. A critical component of this is ensuring the AI-generated content provides **clarity**, capturing the essence of the source material in an easy-to-read format.

**Defining Experience Statement:** When described to a friend, the app's core essence is that **"it makes studying much easier and efficient."** This statement serves as the guiding principle for the entire user experience, emphasizing the core value proposition of simplifying the study process and saving users time.

### 2.1.3 Core Experience Principles

Based on the defining experience and desired emotional response, the following core experience principles will guide every UX decision:

**Speed:** Actions should feel instantaneous. The UI will be highly responsive, with immediate feedback (e.g., progress indicators for AI generation) and minimal friction, reinforcing the value of time-saving.

**Guidance:** A high degree of guidance will be provided, especially for non-tech-savvy users. This includes clear labels, sensible defaults, and a "less is more" approach to the initial UI, utilizing progressive disclosure to manage complexity.

**Flexibility:** For the MVP, simplicity will be prioritized over extensive flexibility. The focus is on a single, streamlined path from document upload to study material generation, without extensive customization options for AI outputs (e.g., summary length, quiz difficulty).

**Feedback:** Feedback will be clear, encouraging, and celebratory. Success messages for content generation will reinforce the feeling of achievement and efficiency. Error messages will be simple, jargon-free, and guide the user towards a solution, consistent with the sleek and intuitive design.

### 2.2 Website Page Content Breakdown

#### 2.2.1 Home Page
*   **Hero Section:**
    *   **Headline:** “Study Smarter, Not Longer.”
    *   **Subtext:** “Upload your notes. Get instant summaries, flashcards, and quizzes.”
    *   **Primary CTA button:** Upload Your Notes
    *   **Secondary CTA:** Try a Demo
    *   **Visuals:** Illustration, graphics, or photo.
*   **Key Value Proposition (Three Blocks):**
    *   ⏳ Save Time — automatic processing
    *   📚 Learn Efficiently — AI summaries + flashcards
    *   🎯 Personalized for You — tailored questions & quizzes
*   **Quick Demo Preview:**
    *   A small interactive slider or card showing:
        *   Before: Notes PDF
        *   After: Summary / Flashcard / Quiz
*   **Why It Works (Short Explanation):**
    *   Simple step-by-step visual:
        *   Upload notes
        *   AI analyzes content
        *   Output: Summary, Flashcards, Quiz
        *   Review & study
*   **CTA Section:**
    *   “Start improving your study workflow today”
    *   **Button:** Get Started Free

#### 2.2.2 How It Works Page
*   Break down the workflow with visuals.
*   **Step Sections:**
    *   **Upload Your Study Material:** Notes, PDFs, slides, textbook pages
    *   **Instant Processing:** AI converts your content
    *   **Receive Learning Tools:** Summary, Flashcards, Quiz
    *   **Study & Track Progress:** Track your learning journey

#### 2.2.3 Features Page
*   Use cards or tabs for clarity.
*   **Core Features:**
    *   AI Summaries
    *   Smart Flashcards
    *   Auto-Generated Quizzes
    *   Study Streak Counter & Analytics
    *   Multiple File Types Supported
    *   Sync & Save Across Devices or cloud
*   **Advanced Features:**
    *   Custom difficulty settings
    *   Smart recall scheduling
    *   Topic detection & organization

#### 2.2.4 Pricing Page
*   Clear and student-friendly.
*   **Plans:**
    *   **Free Plan:** Limited uploads
    *   **Premium / Pro Plan:** Unlimited uploads, Personalized quiz generator, Advanced analytics
*   **Student Discount Information:** Details on student discounts.
*   **Billing FAQ:**
    *   “Do I need a credit card?”
    *   “Can I cancel anytime?”

#### 2.2.5 Resources Page (Dropdown Menu)
*   **Content:** Study tips, productivity hacks, spaced repetition guides
*   **Study Templates:** Note-taking layouts, planner PDFs
*   **FAQ:** Technical + product questions

#### 2.2.6 Login / Sign Up Page
*   Simple, minimal, with soft pastel background.
*   **Fields:** Email, Password
*   **Integration:** Button to connect to cloud services to save material there.

### 2.3 Navigation and Key Components

**Top Menu:**
*   Home | How It Works | Features | Pricing | Resources ▼ | Login / Sign Up

**Hamburger Menu:**
*   A hamburger menu will be consistently present, providing access to the main sections of the application, regardless of the user's login status.
*   The menu will be a dropdown and contain the following items:
    *   **Login:** For users to sign in.
    *   **Upload File:** The primary action for creating new study sets.
    *   **Create Flashcards:** A direct link to the flashcard creation functionality.
    *   **Create Quiz:** A direct link to the quiz creation functionality.
    *   **About StudyBuddy:** Information about the application.
    *   **FAQ:** Frequently Asked Questions about StudyBuddy.
    *   **Resources:** Link to the Resources Page.

**User Dropdown (Logged-In State):**
*   Once logged in, a user-specific dropdown menu will be available.
*   This menu will display categories of the user's created content (e.g., "History 101," "Biology 205").
*   This allows for easy access and organization of study materials.

**Login Button:**
*   A "Login" button will be prominently displayed for users who are not signed in.

**Important Buttons & Components:**
*   **Primary CTA:** Upload your notes
*   **Secondary CTA:** Try a demo
*   **Action Buttons inside app:** “Generate Summary”, “Generate Flashcards”, “Generate Quiz”
*   **Dropdown Menus:** Resources, Account Settings, Profile Menu, Possibly “More” on mobile view
*   **Other UI Components:** Upload zone with drag-and-drop, Progress bar during AI processing, Tabs for switching between summary / flashcards / quiz, Card layout for content previews

**Quiz Generation Options:**
*   When creating a quiz, users will have the option to choose the desired length and difficulty:
    *   **15-Minute Quiz:** A quick quiz with a smaller set of questions.
    *   **1-Hour Deep Dive:** A comprehensive quiz covering the material in more depth.

**Flashcards with Visuals:**
*   Flashcards will be enhanced with symbols and photos to make them more engaging and effective.
*   The application will automatically suggest relevant images based on the flashcard's content, and users will have the option to upload their own.

**Footer:**
*   Contact
*   Privacy Policy
*   Terms
*   Support link
*   Social icons

---

## 3. Visual Foundation

### 3.1 Color System

The color palette aims for a **fresh, modern, academic** look with pops of energizing color, balancing professionalism with engaging aesthetics.

**Primary Pastels:**
*   **Pastel Blue (#AFCBFF):** A serene and calming blue, suitable for core UI elements, backgrounds, and primary information. Conveys trust and professionalism.
*   **Pastel Mint (#BFF6E7):** A fresh and uplifting mint green, ideal for highlights, interactive elements, and accents that require a gentle visual emphasis. Conveys clarity and growth.

**Secondary Pastels:**
*   **Pastel Coral (#FFB9B5):** A soft and inviting coral, to be used sparingly for motivational cues, friendly alerts, or elements requiring a warm, subtle call to action. Conveys warmth and approachability.
*   **Pastel Lavender (#EBDDFF):** A delicate and soothing lavender, perfect for secondary elements, subtle backgrounds, or to provide visual balance without overwhelming the user. Conveys calm and creativity.

**Neutrals:**
*   **Off White (#F7F7FA):** The primary background color, providing a clean, bright, and expansive canvas for content.
*   **Black (Text Color) (#000000):** Used for primary text to ensure maximum readability and contrast against lighter backgrounds.
*   **Warm Gray (Secondary Text) (#A7A7B0):** Employed for secondary text, metadata, and subtle UI elements to create hierarchy and reduce visual clutter without sacrificing readability.

**Semantic Colors (for system feedback):**
*   **Success:** A green tone, derived to complement the palette.
*   **Warning:** A yellow/orange tone, derived to complement the palette.
*   **Error:** A red tone, derived to complement the palette.

**Usage Guidelines:**
*   **Midnight Blue** or **Off White** are foundational for backgrounds.
*   Buttons and key actions will predominantly use **Vibrant Teal** to ensure they stand out.
*   **Warm Coral** will be reserved for special, motivational, or urgent UI moments.
*   **Soft Lilac** will provide balance for secondary elements or subtle visual differentiation.

**Interactive Visualizations:**

- Color Theme Explorer: [ux-color-themes.html](./ux-color-themes.html)

### 3.2 Typography

Typography should feel academic, modern, and easy to skim.

**Primary Font:**
*   **Inter** (or similar geometric sans-serif)

**Font Weights:**
*   **700** – headers
*   **500** – subheaders
*   **400** – body text

**Hierarchy Guidelines:**
*   **H1**: 32–40px, bold, used sparingly for page titles.
*   **H2**: 24–28px, medium, section headers.
*   **H3**: 18–20px, medium, card titles.
*   **Body**: 14–16px, regular, high readability.

**Tone Expression:**
*   Clean line spacing.
*   Short paragraphs.
*   Friendly but professional microcopy.

### 3.3 Layout & Spacing

**Grid:**
*   8pt spacing system.
*   Consistent padding inside cards and sections.

**Page Structure:**
*   Clear hierarchy: Title → Description → Primary Action → Content.
*   Ample whitespace around major content blocks.
*   Avoid more than two accent colors per screen.

**Responsive:**
*   Mobile-first layout.
*   Breakpoints: 480 / 768 / 1024 / 1440.

---


## 4. Design Direction

### 4.1 Chosen Design Approach

{{design_direction_decision}}

**Interactive Mockups:**

- Design Direction Showcase: [ux-design-directions.html](./ux-design-directions.html)

---

## 5. User Journey Flows

### 5.1 Critical User Paths

{{user_journey_flows}}

---

## 6. Component Library

### 6.1 Component Strategy

{{component_library_strategy}}

---

## 7. UX Pattern Decisions

### 7.1 Consistency Rules

{{ux_pattern_decisions}}

---

## 8. Responsive Design & Accessibility

### 8.1 Responsive Strategy

{{responsive_accessibility_strategy}}

---

## 9. Implementation Guidance

### 9.1 Completion Summary

{{completion_summary}}

---

## Appendix

### Related Documents

- Product Requirements: `{{prd_file}}`
- Product Brief: `{{brief_file}}`
- Brainstorming: `{{brainstorm_file}}`

### Core Interactive Deliverables

This UX Design Specification was created through visual collaboration:

- **Color Theme Visualizer**: C:\Users\birgi\SG-Oslo\docs/ux-color-themes.html
  - Interactive HTML showing all color theme options explored
  - Live UI component examples in each theme
  - Side-by-side comparison and semantic color usage

- **Design Direction Mockups**: C:\Users\birgi\SG-Oslo\docs/ux-design-directions.html
  - Interactive HTML with 6-8 complete design approaches
  - Full-screen mockups of key screens
  - Design philosophy and rationale for each direction

### Optional Enhancement Deliverables

_This section will be populated if additional UX artifacts are generated through follow-up workflows._

<!-- Additional deliverables added here by other workflows -->

### Next Steps & Follow-Up Workflows

This UX Design Specification can serve as input to:

- **Wireframe Generation Workflow** - Create detailed wireframes from user flows
- **Figma Design Workflow** - Generate Figma files via MCP integration
- **Interactive Prototype Workflow** - Build clickable HTML prototypes
- **Component Showcase Workflow** - Create interactive component library
- **AI Frontend Prompt Workflow** - Generate prompts for v0, Lovable, Bolt, etc.
- **Solution Architecture Workflow** - Define technical architecture with UX context

### Version History

| Date     | Version | Changes                         | Author        |
| -------- | ------- | ------------------------------- | ------------- |
| Wednesday, November 19, 2025 | 1.0     | Initial UX Design Specification | BIP |

---

_This UX Design Specification was created through collaborative design facilitation, not template generation. All decisions were made with user input and are documented with rationale._