"""Marks a new-format chapter as approved by a teacher.

Usage:
  python3 scripts/approve_chapter.py <chapter folder> "<teacher name>"

Example:
  python3 scripts/approve_chapter.py app_core/content/cbse/class10/maths/ncert_rationalised/ch01_real_numbers "Mrs. Shah"

Sets the chapter and all its questions to "approved" and records who approved
it and when. Only approved content is shown in the app students install.
Run the content checker afterwards:
  flutter test test/content/content_check_test.dart
"""
import datetime
import json
import os
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    folder, teacher = sys.argv[1], sys.argv[2].strip()
    if not teacher:
        sys.exit("Please give the teacher's name.")

    today = datetime.date.today().isoformat()
    chapter_path = os.path.join(folder, "chapter.json")
    questions_path = os.path.join(folder, "questions.json")
    for path in (chapter_path, questions_path):
        if not os.path.exists(path):
            sys.exit(f"Not found: {path}")

    with open(chapter_path, encoding="utf-8") as f:
        chapter = json.load(f)
    chapter.update(status="approved", reviewed_by=teacher, reviewed_on=today)

    with open(questions_path, encoding="utf-8") as f:
        bank = json.load(f)
    for question in bank["questions"]:
        question["status"] = "approved"

    for path, data in ((chapter_path, chapter), (questions_path, bank)):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print(f"Approved '{chapter['title']}' and {len(bank['questions'])} questions, by {teacher} on {today}.")


if __name__ == "__main__":
    main()
