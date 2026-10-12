"""Shared helpers for CBSE Class 10 Hindi Course B (085) chapters, same content format as English literature.

Board pattern 2025-26 (Section C, textbooks): extract-based MCQs (1 mark each), short answers in 25-30 words
(2 marks) from Sparsh, and answers in 50-60 words (3 marks) from Sanchayan. Lessons are written with English as
the base text plus Hindi and Gujarati (added by tools/content_translation/lit_translate.py); exam answers are
meant to be written in Hindi, so the Hindi field carries the model answer. Hindi quotations stay in Hindi."""
from lit_common import Lit, SHINE, check

SUBJECT = "hindi_b"
BOOKS = {"sparsh": "NCERT स्पर्श भाग 2 (Sparsh Part 2)", "sanchayan": "NCERT संचयन भाग 2 (Sanchayan Part 2)",
         "vyakaran": "Shine Academy हिंदी व्याकरण (Hindi Grammar), Class 10 Course B", "rachna": "Shine Academy रचनात्मक लेखन (Writing), Class 10 Course B"}
MS2 = ["1 mark: content (correct point from the text)", "1 mark: expression in Hindi (25-30 words)"]
MS3 = ["2 marks: content (relevant points from the text)", "1 mark: expression in Hindi (50-60 words)"]


def ex(n, part="प्रश्न-अभ्यास"):
    return {"kind": "ncert_exercise", "exercise": part, "question": n}


class Hindi(Lit):
    def two(self, id_, concepts, question, points, source=SHINE, difficulty="easy"):
        """Sparsh short answer, 2 marks, 25-30 words."""
        check(len(points) >= 2, f"{id_}: give two points")
        self.q(id_, "very_short_answer", 2, concepts, source, question, difficulty, answer_steps=points, marking_scheme=MS2)

    def three(self, id_, concepts, question, points, source=SHINE, difficulty="medium"):
        """Sanchayan answer, 3 marks, 50-60 words."""
        check(len(points) >= 2, f"{id_}: give at least two points")
        self.q(id_, "short_answer", 3, concepts, source, question, difficulty, answer_steps=points, marking_scheme=MS3)


def make(prefix):
    c = Hindi(prefix)
    c.AR = {}
    return c


def header(book, key, n, title, author, kind, concepts, note):
    """kind: 'poem', 'prose', 'play', 'grammar' or 'writing'."""
    return {"schema_version": 1, "id": f"cbse.c10.hindi_b.{book}.{key}", "title": title, "book": BOOKS[book], "board": "CBSE",
            "class": 10, "subject": SUBJECT, "chapter_number": n, "author": author, "text_type": kind, "languages": ["en"],
            "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-12",
            "syllabus_note": note, "concepts": concepts}


def path(book, folder):
    return f"app_core/content/cbse/class10/hindi_b/{book}/{folder}"
