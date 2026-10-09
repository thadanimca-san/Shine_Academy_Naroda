# Night Report: 9–10 October 2026

## What was done

All five steps you asked for are finished. Each one is saved as a separate local commit (nothing was pushed).

1. **New content system.** The app now looks for chapters in one new place (`app_core/content/`) first. If a chapter isn't there yet, it uses the old content exactly as before, so nothing that worked yesterday is broken.
2. **Content checker.** One command checks every new chapter for:
   - missing or repeated IDs
   - wrong answers keys
   - wrong marks for a question type
   - formulas that don't display
   - graph points that aren't really zeroes
   - chapters missing from the app's file list

   Command: `flutter test test/content/content_check_test.dart`
3. **CBSE Class 10 Maths Chapter 1, Real Numbers (gold standard).**
   - 36 lesson blocks in 5 sections, following the 8-step teaching cycle. Includes an **animated factor tree**.
   - 59 practice questions:
     - all **21 NCERT exercise questions** (Ex 1.1 and 1.2, every part)
     - 6 NCERT examples
     - 15 MCQs and 5 assertion-reason questions
     - 10 short and long-answer questions, each with a model answer and marking scheme
     - 2 case-based questions
4. **Paper generator in the exact CBSE pattern.**
   - In **Assess → Advanced Paper Generator**, choose CBSE, Class 10, Maths and "preset" mode.
   - The paper follows the board pattern: Sections A–E, 80 marks.
   - Questions are spread across the chosen chapters. You can swap any question.
   - The question paper and the answer key (with marking scheme) export as **watermarked PDFs**, where maths prints exactly as on screen and text cannot be copied.
5. **Chapter 2, Polynomials**, done the same way.
   - 31 lesson blocks with **animated graphs** that show zeroes on the x-axis.
   - 47 questions, including all **18 NCERT exercise questions**. The 6 graph questions come with their own graphs.

Also fixed along the way:
- Maths now displays properly in **Practice** (the on-screen test and its review), in worked examples, flashcards and the question list.
- The step numbers in worked examples showed `${entry.key + 1}` instead of 1, 2, 3. Fixed.

## Important things I found

- **The old "gold" Chapter 1 followed the old syllabus.** It taught Euclid's lemma and decimal expansions, which CBSE removed, and its exercise numbers didn't match the current NCERT book.
- **Two "board" questions in the old Chapter 1 were impossible.** Example: "HCF 9, LCM 2016, one number 54" cannot exist. This shows why every chapter needs a teacher's check.
- **The curriculum calls Class 10 Maths "Ganita Prakash (New 2024)".** As far as I know, Ganita Prakash is for Classes 6–8, and Class 10 still uses the rationalised NCERT Mathematics book. **Please check with your teachers.**
- **Chapter 1 alone can't fill a full 80-mark paper.** Real Numbers has no 5-mark questions. The generator tells the teacher which sections are short. Papers fill up as more chapters are added.

## What you should test

> **Use a debug build (`flutter run`) for testing.** The version students install only shows chapters a teacher has **approved**. Tonight's chapters are marked "reviewed", so a release APK still shows the old chapters until you approve them.

1. Learn → CBSE → Class 10 → Mathematics → Chapter 1 → **Learn**. Check:
   - the formulas look right
   - the factor tree grows
   - the "think about it" questions and checks work
2. Same for Chapter 2: watch the graphs draw themselves.
3. Chapter 1 → **Practice**: the test should show 20 objective questions with proper maths.
4. Assess → Advanced Paper Generator → CBSE, Class 10, Maths, select chapters 1 and 2 → generate. Check:
   - the sections and marks
   - the message about short sections
   - **Export paper PDF** and **Export answer key PDF**: logo watermark, "do not copy" line, maths printed correctly
5. Try a PDF on the **classroom panel** too. PDFs now take a few seconds more to make.

## What needs a teacher's check

- **All content of Chapters 1 and 2.** Every number was checked by a computer script, but a teacher must check the teaching, the wording and the marking schemes.
- **The 6 graph questions in Exercise 2.1.** I drew my own graphs with the same answers as the book (0, 1, 3, 2, 4, 3 zeroes). Please compare them with NCERT Fig. 2.10.
- **Board-style questions** are marked as our own ("shine"), not as past board papers. I can't verify board-paper years without the actual papers.

**When a teacher approves a chapter**, run:

```
python3 scripts/approve_chapter.py app_core/content/cbse/class10/maths/ncert_rationalised/ch01_real_numbers "Teacher Name"
flutter test test/content/content_check_test.dart
```

## Things I could not finish or verify

- **Older experiment tests:** 5 old PDF test files (`pdf_test`, `test_capture`, `test_pdf_gen`, `test_pdf_ispdf_fix`, `test_pdf_maths`) hang in the test environment, because they try to capture real screens. Tonight's 31 new tests all pass. I believe the old ones failed before tonight too, but I didn't prove it. They should probably be deleted or rewritten. Your decision.
- **PDF quality on real devices** can only be checked on a phone or panel (step 5 above).
- I did not touch the old copies of chapters (as you asked). They can be removed once the new chapters are approved.

## Questions for you

1. Is Class 10 Maths really "Ganita Prakash" this year, or the rationalised NCERT book? (See above.)
2. Do you have **previous years' CBSE papers** (PDF or printed)? With them I can add real past-paper questions labelled by year.
3. Which teacher will check Maths? Once Chapters 1 and 2 are approved, I'll continue with Chapters 3–14 at the same quality.
4. Should I delete the 5 old PDF experiment tests?
5. Shall I push tonight's commits to GitHub, or keep them local for now?

## Where things are

- Design: `docs/CONTENT_FORMAT_DESIGN.md`
- Every decision taken tonight, with reasons: `docs/DECISIONS_LOG.md`
- Instructions for AI agents: `.agents/AI_AGENT_MASTER_PROMPT.md` (new section at the end)
