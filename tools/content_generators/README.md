# Content generators

These scripts produce the chapters in `app_core/content/`. Every chapter has
four steps. All scripts take the project root (or a chapter folder) as their
first argument, and they need `tools/content_translation/` on the Python path.

| Step | Script | What it does |
|---|---|---|
| 1 | `gen_chNN.py` (maths) / `gen_sciNN.py` (science) | Writes the English `chapter.json` and `questions.json`. Answers are checked first: maths with exact fractions or sympy, chemistry equations atom by atom (`sci_common.ce`). |
| 2 | `feedback_chNN.py` / `feedback_sciNN.py` | Adds an explanation for every option of every objective item. |
| 3 | `tr_chNN_lesson.py`, `tr_chNN_questions.py` (and `tr_sci…`) | Hindi and Gujarati text. Templates use `{0}`, `{1}`… for the formulas of the English text, so formulas are copied exactly. |
| 4 | `tools/content_translation/apply_translations.py <folder> <lesson module> <questions module>` | Writes the `_hi` / `_gu` fields; stops with a list if anything is still in English. |

Then register the chapter in `app_core/content/index.json` and `pubspec.yaml`,
add it to `test/quiz_game_screen_test.dart`, and run
`flutter test test/content/ test/quiz_game_screen_test.dart`.

Run a chapter's scripts in this order (paths are examples):

```
cd tools/content_generators
PYTHONPATH=../content_translation python3 gen_sci01.py ../..
PYTHONPATH=../content_translation python3 feedback_sci01.py ../..
cp ../../app_core/content/cbse/class10/science/ncert_rationalised/ch01_*/ *.json /tmp/work/
PYTHONPATH=.:../content_translation python3 ../content_translation/apply_translations.py /tmp/work tr_sci01_lesson tr_sci01_questions
```

Terminology: Hindi follows the NCERT Hindi books; Gujarati follows the GSEB
textbooks. Chapters are `reviewed` until a teacher approves them with
`scripts/approve_chapter.py <folder> "<teacher>"`; release builds show only
approved chapters.
