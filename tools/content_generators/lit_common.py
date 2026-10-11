"""Shared helpers for CBSE Class 10 English literature (First Flight), English (184) paper pattern.

Section C of the board paper: extracts (5 marks: 5 one-mark parts), short answers in 40-50 words
(3 marks) and long answers in 100-120 words (6 marks). The content checker allows these marks for
subject "english_literature". Objective items follow ss_common: answer first, feedback for every option.
Extracts quote only a few lines of the text, as the board paper does."""
from ss_common import SS, SHINE, check

BOOK = "NCERT First Flight: Textbook in English for Class X"
SUBJECT = "english_literature"
MS3 = ["1 mark: content point 1", "1 mark: content point 2", "1 mark: expression and accuracy (40-50 words)"]
MS6 = ["3 marks: content (relevant points from the text)", "2 marks: organisation and coherence",
       "1 mark: accuracy of language (100-120 words)"]
EX5 = ["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark", "(iv) 1 mark", "(v) 1 mark"]


def ex(n, part="Thinking about the Text"):
    return {"kind": "ncert_exercise", "exercise": part, "question": n}


class Lit(SS):
    def sa(self, id_, concepts, question, points, source=SHINE, difficulty="medium"):
        """Short answer, 3 marks, 40-50 words."""
        check(len(points) >= 2, f"{id_}: give at least two content points")
        self.q(id_, "short_answer", 3, concepts, source, question, difficulty, answer_steps=points, marking_scheme=MS3)

    def la(self, id_, concepts, question, points, source=SHINE, difficulty="hard"):
        """Long answer, 6 marks, 100-120 words; points form a model answer."""
        check(len(points) >= 4, f"{id_}: a long answer needs at least four points")
        self.q(id_, "long_answer", 6, concepts, source, question, difficulty, answer_steps=points, marking_scheme=MS6)

    def vsa(self, id_, concepts, question, points, source=SHINE, difficulty="easy"):
        self.q(id_, "very_short_answer", 2, concepts, source, question, difficulty, answer_steps=points,
               marking_scheme=["1 mark: first point", "1 mark: second point"])

    def extract(self, id_, concepts, lines, parts, source=SHINE, difficulty="medium", intro="Read the extract and answer the questions."):
        """Board-style extract: `lines` is the quoted text, `parts` five (question, answer) pairs, 1 mark each."""
        check(len(parts) == 5, f"{id_}: an extract has five 1-mark parts")
        q = intro + "\n\n" + "\n".join(f"*{l}*" for l in lines.split("\n")) + "\n\n" + "\n\n".join(
            f"({n}) {p}" for n, (p, _) in zip(("i", "ii", "iii", "iv", "v"), parts))
        steps = [f"({n}) {a}" for n, (_, a) in zip(("i", "ii", "iii", "iv", "v"), parts)]
        self.q(id_, "case_based", 5, concepts, source, q, difficulty, answer_steps=steps, marking_scheme=EX5)


def make(prefix):
    c = Lit(prefix)
    c.AR = {}
    return c


def header(key, n, title, author, kind, concepts, note):
    """kind: 'prose', 'play' or 'poem'."""
    return {"schema_version": 1, "id": f"cbse.c10.english.first_flight.{key}", "title": title, "book": BOOK, "board": "CBSE",
            "class": 10, "subject": SUBJECT, "chapter_number": n, "author": author, "text_type": kind, "languages": ["en"],
            "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-12",
            "syllabus_note": note, "concepts": concepts}


def path(folder):
    return f"app_core/content/cbse/class10/english/first_flight/{folder}"
