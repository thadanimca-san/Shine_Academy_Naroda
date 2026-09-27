# Architectural Blueprint: Shine Academy EduOS (Flutter Client & Dynamic JSON Engine)

## 1. Architectural Vision
Shine Academy EduOS uses a **Server-Driven UI (SDUI) / JSON-Driven Architecture** to render rich, interactive educational chapters dynamically. Instead of hardcoding screens, the Flutter client acts as a high-performance rendering engine that parses structured JSON payloads into native interactive widgets via a centralized `BlockRegistry`.

---

## 2. Core System Components

### A. The Block Registry (`BlockRegistry`)
* **Definition:** A singleton registry mapping string identifiers (`type`) to factory constructors of Flutter widgets.
* **Contract:** Every registered block widget must implement a standard interface accepting a typed data model derived from JSON.
* **Supported Block Types:**
  * `hook` (Mystery/Real-world connection card)
  * `socratic_thinking` (Interactive prediction prompt)
  * `discovery` (Intuitive analogy / visual container)
  * `reveal` (Formal definition & core concept card)
  * `knowledge_check` (Low-pressure MCQ / interactive poll)
  * `reflection` (Deep-dive journaling or prompt card)
  * `connection` (Cross-subject link / knowledge graph node)
  * `mastery` (Application challenge / mini-task widget)
  * `animated_diagram` (Lottie / vector animation wrapper)

### B. The Rendering Pipeline
1. **Payload Ingestion:** The app fetches a chapter JSON containing metadata and an ordered array of `blocks`.
2. **Lazy List Rendering:** The root screen uses `ListView.builder` (or `CustomScrollView` with slivers) to render blocks lazily, optimizing memory and frame rates on low-end Android digital panels and budget smartphones.
3. **Dynamic Resolution:** For each element in the block array:
   - Read `type` (e.g., `"knowledge_check"`).
   - Lookup corresponding builder in `BlockRegistry`.
   - Pass JSON payload map to the widget constructor.
   - Fallback to a graceful error widget if `type` is unknown.

### C. State & Progress Persistence
* **Local Caching:** Chapter JSONs are stored locally (via Hive or Isar) for offline-first capability in classrooms with poor connectivity.
* **Block-Level State:** Interactive blocks (MCQs, predictions) manage their own local state (e.g., selected answer, correctness) and emit state change callbacks up to the parent lesson controller to track completion progress.

---

## 3. Standard JSON Schema Specification

Every chapter must adhere to the following top-level JSON structure:

```json
{
  "chapter_id": "sci_gr10_ch01_chemical_reactions",
  "board": "CBSE",
  "grade": 10,
  "subject": "Science",
  "curriculum_version": "2026-revised",
  "title": "Chemical Reactions and Equations",
  "subtopic_index": 1,
  "blocks": [
    {
      "block_id": "b1_hook",
      "type": "hook",
      "data": {
        "title": "Why does iron rust outdoors?",
        "content": "Have you ever noticed old iron gates turning reddish-brown over time...",
        "image_url": "assets/images/rust_gate.png"
      }
    },
    {
      "block_id": "b2_socratic",
      "type": "socratic_thinking",
      "data": {
        "prompt": "What do you think happens to the total weight of iron when it rusts? Does it increase, decrease, or stay the same?",
        "options": ["Increases", "Decreases", "Stays the same"],
        "correct_index": 0,
        "explanation_hint": "Think about what is combining with the iron from the air."
      }
    }
  ]
}
```
