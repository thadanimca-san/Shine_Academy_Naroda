# EduOS Master Architecture

EduOS is not just an app. It is a highly scalable Educational Operating System that consumes deeply structured knowledge graphs and dynamically renders them into interactive experiences.

## Core Engines

1. **Learning Engine (Renderer):** The presentation layer that maps JSON blocks to Flutter Widgets.
2. **Knowledge Graph (Brain):** The ontological map connecting terms, concepts, and relationships.
3. **Curriculum Engine:** Handles syllabus unlocking and progression routing.
4. **Pedagogy Engine (Director):** Ensures educational sequences flow logically (Theory -> Example -> Activity -> Assessment).
5. **Universal Reward Engine:** The global gamification system managing XP, streaks, and voice rewards.
6. **Assessment Engine:** Handles quizzes, flashcards, distractor rationales, and Bloom's Taxonomy tracking.
7. **Learning Analytics Engine (Future):** Tracks time-per-topic, retention, and weak areas.

## Scale Vision
EduOS is designed to support millions of students and decades of content by decoupling the **Content** (JSON/Cloud) from the **Engine** (Flutter Application). No code updates are required to add a new subject.
