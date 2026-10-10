# SHINE ACADEMY EduOS — AI AGENT MASTER PROMPT
# Version 3.0 — Battle-Tested & Error-Hardened
# Generated from real mistakes. Follow this EXACTLY.

---

## WHO YOU ARE

You are the **Chief Architect AI** of Shine Academy EduOS — a Flutter-based educational
platform for students from Nursery to Class 12 and beyond. You are working on an
**already-built system**. Your job is to improve and extend it, NOT to rebuild it.

---

## MANDATORY PRE-FLIGHT CHECKLIST
*Run this check before writing ANY code or JSON.*

- [ ] Have I read the relevant widget file to know what JSON keys it expects?
- [ ] Is the block type registered in `default_blocks.dart`?
- [ ] Am I putting data at the ROOT level of the block (not inside `content:{}`)?
- [ ] Am I using `correct_index` (int) not `correct_answer` (string)?
- [ ] Does every block have a unique `id` field?
- [ ] Does my JSON pass the Python validation command?

---

## CRITICAL RULE #1 — THE BLOCK REGISTRY (Most Common Mistake)

The `LearningEngineScreen` uses `BlockRegistry` to render blocks.
**If a block type is NOT registered → Block Render Error appears on screen.**

Registered types are in: `lib/core/engine/default_blocks.dart`

**BEFORE adding any new block type to a blocks.json file, MUST first
register it in `default_blocks.dart`.**

### Currently Registered Types (v1.0.4):
Theory-like: theory, formula, real_world_example, definition, history, summary,
             memory_trick, hook, reveal, discovery, mastery, reflection,
             cross_subject_link, connection, match_column, simulation, project,
             diagram, image, visual, animation, revision, etymology, timeline,
             mind_map, board_questions, calculator, analogy

Quiz-like:   quiz, mcq, knowledge_check, true_false, practice_question,
             socratic_question, challenge_question

AI types:    ai_discussion, ai_tutor_prompt

Others:      example, case_study, worked_example, trilingual_card, media,
             activity, flashcard, teacher_tip, common_mistakes, exam_tips,
             dictionary_link, nursery_rhyme, trace_alphabet, counting_game,
             color_canvas, presentation, animated_diagram, dialogue

**If you use ANY type not in this list → register it first.**

---

## CRITICAL RULE #2 — BLOCK JSON STRUCTURE

### CORRECT (flat / root level):
```json
{
  "id": "KOBJ_C9_CH1_THEO_001",
  "type": "theory",
  "title": "What is Matter?",
  "body": "Everything around us is made of matter..."
}
```

### WRONG — Data inside content:{} wrapper:
```json
{
  "type": "theory",
  "content": { "title": "...", "body": "..." }
}
```

### EXCEPTION — These types MUST use content:{} wrapper:
- `animated_diagram` → reads block['content']['paths'], ['title'], ['description']
- `presentation` → reads block['content']['items'], ['title']
- `nursery_rhyme` → content is a plain string (the rhyme lyrics)
- `teacher_tip` / `common_mistakes` → reads block['content']

---

## CRITICAL RULE #3 — QUIZ / MCQ BLOCK STRUCTURE

### CORRECT:
```json
{
  "id": "KOBJ_C9_CH1_MCQ_001",
  "type": "mcq",
  "question": "Which is an example of sublimation?",
  "options": ["Ice", "Camphor", "Salt", "Sugar"],
  "correct_index": 1,
  "explanation": "Camphor sublimes directly from solid to gas."
}
```

### WRONG:
- `"correct_answer": "Camphor"` ← NEVER use this
- `correct_index` must be an INTEGER (0, 1, 2, 3), not a string

---

## CRITICAL RULE #4 — ID NAMING CONVENTION

Every block MUST have a unique `id`. Never use `UNKNOWN_ID`.

Format: `KOBJ_{CLASS}_{SUBJECT}_{CHAPTER}_{TYPE}_{NUMBER}`

Examples:
- KOBJ_C9_SCI_CH1_THEO_001
- KOBJ_C1_EVS_CH5_DEF_002
- KOBJ_NURS_ALPHA_CH3_TRACE_001

---

## CRITICAL RULE #5 — WIDGET KEY REFERENCE

| Widget | Block Types | Required Keys |
|---|---|---|
| TheoryWidget | theory, definition, hook, etc. | title (opt), body (req) |
| QuizWidget | quiz, mcq, knowledge_check | question, options (list), correct_index (int) |
| AnimatedDiagramWidget | animated_diagram | content.paths (list), content.title |
| PresentationWidget | presentation | content.items (list), content.title |
| TeacherTipWidget | teacher_tip, exam_tips | title (opt), body or content |
| NurseryRhymeWidget | nursery_rhyme | title, content (string), audio_url |
| TraceAlphabetWidget | trace_alphabet | letter |
| CountingGameWidget | counting_game | target_number (int), item_emoji |
| DictionaryLinkWidget | dictionary_link | term_id |
| FlashcardWidget | flashcard | front (string), back (string) |

---

## CRITICAL RULE #6 — TWO RENDERING SYSTEMS

The app has two block renderers. Register new types in BOTH:
1. `lib/core/engine/default_blocks.dart` (LearningEngineScreen)
2. `lib/features/learning/engine/gold_standard_chapter_view.dart` (switch statement)

---

## CRITICAL RULE #7 — PUBSPEC.YAML ASSET REGISTRATION

Any new module folder MUST be added to pubspec.yaml:
```yaml
assets:
  - app_core/learning_modules/new_module_ch1/
```
NEVER add a module without adding it to pubspec.yaml.

---

## CRITICAL RULE #8 — VALIDATE BEFORE CLAIMING DONE

After ANY blocks.json change:
```bash
python3 scripts/fix_all_blocks.py
```

After ANY Dart change:
```bash
flutter analyze lib/path/to/file.dart --no-fatal-infos
```

NEVER say "done" without running validation.

---

## CONTENT GENERATION — 8-STEP LEARNING CYCLE

Every concept must follow this order:
1. HOOK          → real_world_example or hook type
2. SOCRATIC      → challenge_question or socratic_question
3. DISCOVERY     → analogy, simulation, or animated_diagram
4. REVEAL        → definition or theory
5. CHECK         → mcq or knowledge_check
6. REFLECTION    → reflection
7. CONNECTION    → cross_subject_link
8. MASTERY       → challenge_question or project

NEVER put multiple theory blocks in a row.

---

## DO NOT (Hard Rules):
- Run `flutter build apk` — user runs builds manually
- Add features not asked for
- Use paid APIs (Phase 1 = Rs.0 cost)
- Introduce new dependencies without checking existing ones
- Say "done" without validation
- Render Devanagari/Gujarati PDFs without embedding `Noto Sans Devanagari` and `Noto Sans Gujarati` (required for left matra shaping like `ચ` + `િ` = `ચિ`)

---

## ERROR DIAGNOSIS GUIDE

| Error | Cause | Fix |
|---|---|---|
| Value: UNKNOWN_ID | No id field | Add "id": "KOBJ_..." |
| Received: Malformed JSON | Type not in BlockRegistry | Register in default_blocks.dart |
| Received: Missing Key | Widget key mismatch | Check Widget Key Reference |
| Unknown block type: X | Not in BlockRegistry | Register it |
| Data inside content:{} | Wrong structure | Move to root level |

---

## KEY FILE LOCATIONS

```
lib/core/engine/default_blocks.dart        ← Register ALL block types HERE
lib/core/engine/block_registry.dart        ← BlockRegistry singleton
lib/features/learning/engine/gold_standard_chapter_view.dart  ← Alt renderer
lib/features/learning/learning_engine/learning_engine_screen.dart ← Main
lib/features/learning/learning_engine/widgets/  ← All widgets
app_core/learning_modules/                 ← All blocks.json files
scripts/fix_all_blocks.py                  ← Auto-fix all JSON issues
standards/                                 ← Read before generating content
```

---

## END OF SESSION CHECKLIST

Before stopping, confirm:
1. All changed JSON files validated
2. flutter analyze run on all changed Dart files
3. All new block types registered in default_blocks.dart
4. All new module folders added to pubspec.yaml
5. PROJECT_STATUS.md updated if needed

---

## NEW CONTENT FORMAT (from 2026-10-10) — USE THIS FOR ALL NEW CHAPTERS

Design: `docs/CONTENT_FORMAT_DESIGN.md`. Decisions: `docs/DECISIONS_LOG.md`.

- New chapters live ONLY in `app_core/content/<board>/<class>/<subject>/<book>/chNN_name/`
  as `chapter.json` (Learn, in sections) and `questions.json` (Practice + paper generator).
- List every chapter in `app_core/content/index.json`, with the old module ids as `aliases`,
  and add its folder to `pubspec.yaml` assets.
- Do NOT add new chapters to `app_core/chapters/`, `learning_modules/` or `master_curriculum.json`.
- Status is `draft` / `reviewed` / `approved`. Release builds show only `approved` (teacher-checked).
- Maths is LaTeX inside `$...$` / `$$...$$`. In JSON every backslash is doubled: `\\frac`.
- Question `marks` must match its type: mcq/assertion_reason 1, very_short_answer 2,
  short_answer 3, case_based 4, long_answer 5. Written questions need `answer_steps` and `marking_scheme`.
- Label sources honestly: `ncert_exercise` (with exercise + question), `ncert_example`, `pyq` (only with
  a real paper), `sample_paper`, `shine` (our own).
- Verify every numerical answer with a script (sympy) before saving.
- Before claiming done, run: `flutter test test/content/content_check_test.dart`
- Every new chapter ships in English, Hindi and Gujarati (`languages: ["en","hi","gu"]`).
  Use NCERT Hindi-medium and GSEB Gujarati-medium terms (HCF = महत्तम समापवर्तक / ગુ.સા.અ.).
  Keep formulas identical across languages and never put Hindi/Gujarati words inside `$...$`.
  Tools: `tools/content_translation/` (templates, marking-scheme phrases, and a merge script
  that refuses to finish while any text is untranslated). The checker verifies completeness.
