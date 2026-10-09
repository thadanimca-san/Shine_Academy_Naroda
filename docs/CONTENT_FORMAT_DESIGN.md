# Content Format Design (DRAFT, for discussion)

Status: draft, written 2026-10-09. Nothing here is implemented yet.
Builds on `standards/*.yaml` and `docs/GOLD_STANDARD_CHAPTER_SCHEMA.md`, and keeps
the field conventions the app already reads (`body`, `body_hi`, `body_gu`,
`correct_index`, flat blocks).

---

## 1. Why we need this

Today the same chapter lives in several places, and they disagree.
Class 10 Maths Chapter 1 alone has four copies:

| Copy | Blocks | Who reads it |
|---|---|---|
| `app_core/chapters/ncert_class10_maths_ch1.json` | 25 | Learn tab (what students see today) |
| `app_core/learning_modules/ncert_class10_maths_ch1/blocks.json` | 69 | nobody directly |
| `app_core/learning_modules/master_curriculum.json` (23 MB) | 69 | Learn tab fallback |
| `app_core/content_database/cbse_class10_maths/cls10_math_realnumbers.json` | 69, different | Maths mini-app |

Fixing a mistake in one copy leaves the others wrong. On top of that, the
mini-apps keep their content inside Dart code, so only a programmer can change it.

**Goal:** every chapter, question and concept exists exactly once, in one
predictable place, in one format, and every screen (Learn, Practice, paper
generator, concept search, PDF) reads from there.

---

## 2. Where content lives

```
app_core/content/
  catalog/
    cbse_class10.json            what students can pick: subjects -> books -> chapters
    gseb_class10.json            may point to CBSE chapters instead of copying them
  cbse/class10/maths/ncert_2024/ch01_real_numbers/
    chapter.json                 the Learn part
    questions.json               the Practice part (also feeds the paper generator)
  concepts/
    hcf.json                     one file per core concept, with a level per class
    force.json
  paper_blueprints/
    cbse_class10_maths.json      the board's paper pattern, used by the paper generator
```

- **New and old textbook editions** are separate book folders under the same
  subject (`ncert_2024/`, `ncert_classic/`). The catalog shows the book name in bold.
- **Same syllabus on two boards** (Class 10 Maths and Science): the GSEB catalog
  points at the CBSE chapter folder. No copies.
- The 23 MB `master_curriculum.json` goes away. The app loads one chapter at a
  time, only when it's opened.

---

## 3. The chapter file (`chapter.json`): Learn

```json
{
  "schema_version": 1,
  "id": "cbse.c10.maths.ncert2024.ch01",
  "title": "Real Numbers",
  "book": "NCERT Mathematics (2024)",
  "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 1,
  "languages": ["en"],
  "status": "approved",
  "reviewed_by": "teacher name",
  "reviewed_on": "2026-11-02",
  "concepts": ["hcf", "lcm", "prime_factorisation", "irrational_numbers"],
  "sections": [
    {
      "id": "s1",
      "title": "Fundamental Theorem of Arithmetic",
      "blocks": [
        { "id": "s1.b1", "type": "hook", "body": "..." },
        { "id": "s1.b2", "type": "theory", "body": "Every composite number is a product of primes: $n = p_1^{a_1} \\times p_2^{a_2}$" },
        { "id": "s1.b3", "type": "animation", "animation": "factor_tree", "params": { "number": 140 } }
      ]
    }
  ]
}
```

Rules:

- **Text** is Markdown plus LaTeX: `**bold**`, `- bullet`, `$inline$`, `$$display$$`.
  One shared widget draws it on screen and in PDFs.
- **Languages** follow the existing convention: `body`, then `body_hi` and `body_gu`
  when translated. Missing translations are *not* filled in by Google Translate
  at runtime in the new format. They show English until a reviewed translation exists.
- **Status** is `draft`, `reviewed` or `approved`. Release builds only show `approved`.
- **Accounts formats** are structured data, never plain text. Example:
  ```json
  { "type": "journal", "rows": [
      { "date": "2026-04-01", "debit": "Cash A/c", "credit": "Capital A/c",
        "narration": "Being capital introduced", "lf": "", "amount": 50000 } ] }
  ```
  The same goes for `ledger`, `trial_balance`, `balance_sheet`, `cash_book`. These reuse
  the existing commerce widgets.
- **Animations** are a block type that names a built-in animation and gives it
  numbers (`factor_tree` with 140). One animation then serves every chapter that needs it.

---

## 4. The question file (`questions.json`): Practice and the paper generator

Learn and Practice get equal weight: every chapter has a full question bank,
not just a few quiz blocks.

```json
{
  "id": "cbse.c10.maths.ch01.q017",
  "type": "short_answer",
  "marks": 3,
  "difficulty": "medium",
  "concepts": ["irrational_numbers"],
  "source": { "kind": "pyq", "year": 2024, "paper": "CBSE 30/1/1" },
  "question": "Prove that $\\sqrt{5}$ is irrational.",
  "answer_steps": ["Assume $\\sqrt{5} = \\frac{a}{b}$ ...", "..."],
  "marking_scheme": ["1 mark: assumption", "1 mark: squaring step", "1 mark: contradiction"],
  "status": "approved"
}
```

- `type`: `mcq`, `assertion_reason`, `true_false`, `fill_blank`, `very_short_answer`,
  `short_answer`, `long_answer`, `case_based`, `numerical`, plus accounts types.
  MCQs keep `options` and `correct_index` (an integer), as today.
- `source.kind`: `ncert_exercise` (with exercise and question number), `ncert_example`,
  `pyq` (year and paper code), `sample_paper`, `shine` (our own).
  This answers "every NCERT exercise question is present?" with a simple count.
- `marking_scheme` lets the answer key show what a board examiner expects.

### Paper blueprint (`paper_blueprints/cbse_class10_maths.json`)

The paper generator reads the board pattern from data, so it works for any subject:

```json
{ "total_marks": 80, "duration_minutes": 180, "sections": [
  { "name": "A", "types": ["mcq", "assertion_reason"], "count": 20, "marks_each": 1 },
  { "name": "B", "types": ["very_short_answer"], "count": 5,  "marks_each": 2 },
  { "name": "C", "types": ["short_answer"],      "count": 6,  "marks_each": 3 },
  { "name": "D", "types": ["long_answer"],       "count": 4,  "marks_each": 5 },
  { "name": "E", "types": ["case_based"],        "count": 3,  "marks_each": 4 } ] }
```

Teachers then choose chapters, difficulty mix, and whether to include past board
questions. They get a paper plus an answer key, both as watermarked PDFs.

---

## 5. Core concepts (`concepts/force.json`)

```json
{
  "id": "force",
  "name": "Force",
  "aliases": ["push", "pull", "bal"],
  "levels": [
    { "class": 5, "summary": "A push or a pull ...", "blocks": [ ... ] },
    { "class": 8, "summary": "...", "blocks": [ ... ] },
    { "class": 9, "summary": "$F = ma$ ...", "blocks": [ ... ] }
  ],
  "related": ["mass", "acceleration", "friction"],
  "chapters": ["cbse.c9.science.ncert2024.ch08"]
}
```

A Class 9 student searching "force" sees the Class 9 level first, and can step
down to easier levels. Concepts don't change when the syllabus changes; chapters
just link to them.

---

## 6. Safety net: the content checker

One script runs before every release build and refuses to continue if:

- a block or question has no `id`, or two items share one;
- `correct_index` is missing or out of range;
- a LaTeX formula doesn't parse;
- a catalog points at a chapter that doesn't exist;
- a release build would include anything not `approved`.

---

## 7. Moving over without breaking anything

1. Build the new loader so it checks `app_core/content/` first and falls back to
   today's locations. Existing chapters keep working.
2. Move **CBSE Class 10 Maths Chapter 1** first. Start from the 69-block version,
   fix it, have a teacher approve it, and add its question bank.
3. Move the rest of CBSE Class 10, one subject at a time.
4. Delete an old copy only after its new version is approved.
5. Mini-apps move into JSON one at a time, after the board-exam release.

---

## 8. Open questions for the founder

1. Is splitting each chapter into **Learn** (`chapter.json`) and **Practice**
   (`questions.json`) right for how you teach?
2. For previous-year papers: which years do we have, and in what form (PDF scans,
   typed)?
3. Who reviews which subject? We record the reviewer's name on each chapter.
