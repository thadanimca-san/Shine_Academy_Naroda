# Decisions Log

Decisions taken while the founder was away. Each one can be changed; this
records what was chosen and why.

---

## 2026-10-10: Night of building the new content format

### 1. Learn and Practice are separate files
**Decision:** Each chapter has `chapter.json` (Learn) and `questions.json` (Practice and the paper generator).
**Why:** Learn and Practice have equal importance but different needs. Questions need marks, type, source and a marking scheme; lessons need teaching flow. One question bank serves Practice, the question bank screen and the paper generator.

### 2. Old chapter ids keep working through "aliases"
**Decision:** `app_core/content/index.json` lists each new chapter with the old module ids it replaces (for example `ncert_class10_maths_ch1`).
**Why:** The curriculum files, routes and screens didn't need to change. When a chapter exists in the new format, the app uses it; otherwise it uses the old content exactly as before. Chapters move over one at a time with no risk to the rest.

### 3. Release builds show only teacher-approved content
**Decision:** Chapters and questions have a status: `draft`, `reviewed` or `approved`. Debug builds show everything. The version students install shows only `approved`, and falls back to the old chapter otherwise.
**Why:** "Accurate data" is the promise. Tonight's chapters are marked `reviewed` (checked by AI and by a script, not yet by a teacher), so **students will not see them until a teacher changes the status to `approved`**.

### 4. Class 10 Maths follows the current rationalised NCERT book
**Decision:** Chapter 1 doesn't include Euclid's division lemma or decimal expansions. Chapter 2 doesn't include the division algorithm or cubic relationships.
**Why:** These were removed from the CBSE board syllabus. The old "gold" Chapter 1 still taught them, and its exercise numbers didn't match the current book. Teaching removed topics wastes students' time before the boards.
**Please confirm:** the curriculum file calls Class 10 Maths "Ganita Prakash (New 2024 CBSE Edition)". As far as I know, Ganita Prakash is for Classes 6–8, and Class 10 students still use the rationalised NCERT Mathematics book. Please check with your teachers.

### 5. Board-style questions are labelled as our own, not as past board papers
**Decision:** Questions written by us have `source.kind = "shine"`. Only NCERT exercise questions and examples carry NCERT references.
**Why:** I can't verify which year's board paper a question came from. Labelling a question "CBSE 2024" without proof would be dishonest. Real previous-year questions can be added once we have the actual papers.

### 6. Every answer is checked by a script
**Decision:** The chapter generators recompute every HCF, LCM, factorisation, zero, sum and product with the `sympy` maths library, and stop if any stated answer is wrong. The content checker also confirms that every formula renders and every point marked as a zero on a graph really is a zero.
**Why:** AI makes arithmetic mistakes. The old Chapter 1 had two impossible board questions (for example, HCF 9 and LCM 2016 with one number 54 cannot exist, because 54 contains 3³ but 2016 contains only 3²).

### 7. MCQ answers are spread across options (a)–(d)
**Decision:** Options are rotated by a fixed rule, so the correct answer isn't always the first one.
**Why:** Students quickly learn patterns like "the answer is always (a)".

### 8. Animations as reusable blocks
**Decision:** Two new block types: `factor_tree` (animated prime factorisation) and `function_graph` (animated polynomial graph with zeroes marked). Both respect the phone's "reduce motion" setting and draw their finished picture in PDFs.
**Why:** One animation serves every chapter that needs it, instead of a custom screen per chapter. `function_graph` will also serve Quadratic Equations and Coordinate Geometry.

### 9. Graphs for NCERT Exercise 2.1 are drawn by us
**Decision:** The six graph-reading questions use graphs drawn to give the same answers as the textbook (0, 1, 3, 2, 4, 3 zeroes).
**Why:** We can't copy the textbook figures. Each question has a teacher note asking for a comparison with NCERT Fig. 2.10.

### 10. Paper generator reuses the existing "Advanced Paper Generator"
**Decision:** No new screen. When a subject has a board blueprint (CBSE Class 10 Maths now does), "preset" mode builds the paper in the exact board pattern: Sections A–E, 80 marks. Other subjects work as before. If the chosen chapters don't have enough questions yet, the teacher sees which sections are short.
**Why:** Reuse over parallel code. The blueprint is data, so adding another subject's pattern needs no programming.

### 11. Paper PDFs are drawn from the same widgets as the screen
**Decision:** Question paper and answer key PDFs now go through the "draw on screen, then capture" path with the shared watermark.
**Why:** LaTeX maths cannot print through the old text-only path. Text in these PDFs cannot be copied out. **Trade-off:** generating a PDF now takes a few seconds longer (progress is shown), and the file is larger. Please test it on a real phone and on the classroom panel.

### 12. Practice screen understands maths
**Decision:** The on-screen test, its review screen and the question selection list now draw formulas properly. A question can carry a figure (for example a graph).
**Why:** Without this, Chapter 1's practice questions would show raw codes like `$2^{3}$`.
