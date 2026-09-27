# Shine Academy Master Educational Specification (v1)

**CRITICAL MANDATE FOR ALL AI AGENTS:**
Whenever a user requests the generation of a new chapter, subject, or learning module, you MUST strictly adhere to this specification. This guarantees that Shine Academy maintains a world-class, consistent standard of interactive education across all grades.

---

## 1. Chapter Metadata Requirements
Every chapter's `metadata.json` MUST contain the following rich relationships for the AI engine:
*   `learning_outcomes`: An array of measurable goals (e.g., ["Define an atom", "Calculate molecular mass"]).
*   `prerequisites`: Array of chapter IDs the student must have mastered.
*   `next_chapters`: Array of chapter IDs to unlock next.
*   `core_concepts`: Array of dictionary term IDs introduced.

## 2. Block Metadata Requirements (Adaptive Learning)
Inside `blocks.json`, EVERY single block (theory, flashcard, quiz, tip) MUST include:
*   `difficulty`: "Beginner", "Intermediate", or "Advanced"
*   `estimated_minutes`: Integer representing time to consume
*   `bloom`: Cognitive depth ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")

## 3. Required Content Sequence
Every generated chapter must follow this structural flow:

### Phase A: The Hook
*   **Real World Application / Story:** A block connecting the topic to everyday life to build curiosity.
*   **Learning Goals:** A block explaining exactly what the student will learn.

### Phase B: Concept Breakdown (Iterative)
For every major concept within the chapter, you must include:
*   **Theory Block:** Clear, concise explanation.
*   **Dictionary Link:** Inline link to the formal definition (`dictionary_link`).
*   **Teacher Tip or Analogy:** A creative way to remember it (`teacher_tip` or `memory_trick`).
*   **Interactive Check:** A flashcard or quick multiple-choice question to test immediate understanding.
*   **Common Mistake:** A warning about how students usually get this wrong (`common_mistakes`).

### Phase C: Synthesis & Assessment
*   **Summary / Revision Notes:** A condensed summary of the entire chapter.
*   **Higher-Order Thinking Question:** An advanced block challenging the student's understanding.
*   **Board/Exam Questions:** Inclusion of real exam-style questions in the `question_bank.json`.

---

## 4. Dictionary Generation Rules
When introducing new terms, you must generate their respective Knowledge Graph JSONs in the dictionary directory. They MUST include:
*   `related`: Array of IDs.
*   `prerequisites`: Array of IDs.
*   `used_in`: Array of Chapter IDs.
