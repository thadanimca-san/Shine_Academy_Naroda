# Gold Standard Learning Module Schema

This schema is designed as the educational DNA of the Shine Academy Naroda platform. It abstracts learning into fundamental, reusable components (blocks) rather than hardcoded screens. This ensures that the platform can teach a Jr. KG student the Alphabet, a Class 12 student Accountancy, or a professional preparing for UPSC, all using the exact same rendering engine.

## Core Philosophy

1.  **Data-Driven UI:** Flutter acts as a pure renderer. It reads the `"type"` of a block (e.g., `concept_block`, `interactive_activity`, `mcq`) and inflates the corresponding UI component.
2.  **Polymorphic Content:** The `content` array can hold any sequence of elements. A chapter could be a video followed by a quiz, or a text explanation followed by a 3D model.
3.  **Future-Ready:** The schema includes hooks for AI, offline syncing, analytics, and gamification, ensuring the architecture remains robust for the next 20 years.

---

## Schema Structure

### 1. `metadata`
Contains essential tracking, routing, and configuration data for the module.
*   **`module_id`**: Unique identifier (e.g., `com.shine.class12.accounts.ch1`).
*   **`subject_domain`**: The broader subject area.
*   **`target_audience`**: Tags used for filtering and search.
*   **`difficulty_level`**: Allows adaptive learning engines to recommend modules.
*   **`estimated_learning_time_minutes`**: Helps students plan their study sessions.
*   **`supported_languages`**: Array of language codes (e.g., `["en", "gu", "hi"]`) indicating available translations.
*   **`features_enabled`**: Boolean toggles for future features like `ai_tutor`, `voice_reading`, or `offline_learning`.

### 2. `pedagogy`
Defines the educational journey and prerequisites.
*   **`learning_objectives`**: What the student will learn.
*   **`prerequisite_knowledge`**: Array of concepts they should know, with deep links to previous modules.
*   **`learning_outcomes`**: Measurable skills acquired upon completion.
*   **`future_learning_path`**: Where the student should go next.

### 3. `content` (The Core Engine)
An array of polymorphic blocks. Flutter loops through this array and renders widgets sequentially.
*   **`type`**: The critical discriminator (e.g., `concept_block`, `worked_example`, `interactive_activity`, `case_study`).
*   **`multilingual_text`**: Instead of a single string, content is stored in a dictionary mapped to language codes, enabling instant language switching without changing the UI structure.
*   **`visuals` / `animations`**: Links to network or local assets (Lottie, PNG, MP4).
*   **`teaching_aids`**: Meta-information to assist learning. Includes `teacher_tips`, `common_mistakes`, `memory_tricks`, and `real_life_applications`. The UI can render these as expandable "Did You Know?" or "Warning" callouts.
*   **`vocabulary`**: Words with definitions and paths to pronunciation audio files, crucial for language learners and complex technical subjects.

### 4. `assessments`
A dedicated section for evaluating knowledge.
*   **`formative_assessments`**: Embedded questions (MCQs, True/False, Match the Following) meant for practice.
*   **`summative_assessments`**: Graded tests at the end of the module.
*   **`previous_year_questions`**: Crucial for board/competitive exams like GSEB, JEE, UPSC.

### 5. `resources`
Supplementary materials for offline or deeper study.
*   **`revision_notes` / `mind_maps`**: Links to downloadable PDFs or high-res images.
*   **`summary`**: A quick text recap.
*   **`faqs`**: Common doubts preemptively answered.

### 6. `analytics_and_gamification`
Data designed to feed the student dashboard and gamification engine.
*   **`points_awarded`**: Base XP for completing the module.
*   **`badges_unlockable`**: Identifiers for badges the student can earn.
*   **`milestone_triggers`**: Hooks that tell the cloud database to update the student's global progress or notify parents.

---

## Why this is the "Educational DNA"

By separating the **What** (JSON Data) from the **How** (Flutter UI), Shine Academy can scale infinitely. 

*   **To add a Jr. KG Alphabet module:** We use the exact same schema. We populate `content` with a block of `type: "canvas_tracing_activity"` and `audio: "assets/a_apple.mp3"`. Flutter sees `canvas_tracing_activity` and renders a drawing pad.
*   **To add a JEE Physics module:** We populate `content` with a block of `type: "physics_simulation"` passing parameters for gravity and friction.
*   **To add UPSC History:** We use heavy `concept_block` types, `case_study` types, and `mind_maps`.

The Flutter codebase remains untouched. The JSON schema becomes the universal language of the platform.
