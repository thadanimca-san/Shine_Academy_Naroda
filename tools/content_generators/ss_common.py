"""Shared helpers for CBSE Class 10 Social Science chapters (same content format as science).

Objective items are written as (option, feedback) pairs with the right answer FIRST; write() moves the
answer to an id-dependent position (board-paper items keep their printed order) and keeps the feedback
aligned. Assertion-reason feedback uses the science wording so the Hindi/Gujarati tooling applies unchanged."""
import json, os
from collections import Counter
from sci_common import Chapter, check, SHINE, AR_OPTIONS

SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Social Science (087)", "question": n}
MS2 = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]
MS5 = ["1 mark: first point", "1 mark: second point", "1 mark: third point", "1 mark: fourth point", "1 mark: fifth point"]
CB = ["(i) 1 mark", "(ii) 1 mark", "(iii) 2 marks"]
BOOKS = {"history": "NCERT India and the Contemporary World – II", "geography": "NCERT Contemporary India – II",
         "civics": "NCERT Democratic Politics – II", "economics": "NCERT Understanding Economic Development"}
FOLDER = {"history": "history", "geography": "geography", "civics": "political_science", "economics": "economics"}

_TRUTH = {0: (True, True, True), 1: (True, True, False), 2: (True, False, None), 3: (False, True, None)}
def ar_fb(ci, wa, wr):
    a, r, e = _TRUTH[ci]; out = []
    for ca, cr, ce in _TRUTH.values():
        if (ca, cr) == (a, r) and (ce is None or ce == e):
            out.append(f"Correct! A is {'true' if a else 'false'}: {wa} R is {'true' if r else 'false'}: {wr}")
        elif ca != a: out.append(f"Check the Assertion again: it is {'true' if a else 'false'}, because {wa}")
        elif cr != r: out.append(f"Check the Reason again: it is {'true' if r else 'false'}, because {wr}")
        else: out.append(("R does explain A: " if e else "Both are true, but R is not the reason A is true: ") + wr)
    return out

def _pairs(pairs):
    texts = [o for o, _ in pairs]
    check(len(texts) >= 2 and len(texts) == len(set(texts)), f"options: {texts}")
    check(all(f.strip() for _, f in pairs[1:]), f"every wrong option needs feedback: {texts}")
    return texts, ["Correct!"] + [f for _, f in pairs[1:]]

class SS(Chapter):
    def kc(self, id_, question, pairs, explanation):
        options, fb = _pairs(pairs)
        return self.blk(id_, "knowledge_check", question=question, options=options, correct_index=0, explanation=explanation, option_feedback=fb)
    def socratic(self, id_, question, options, correct, explanation):
        return self.blk(id_, "socratic_question", question=question, options=options, correct_index=correct, explanation=explanation)
    def m(self, id_, concepts, question, pairs, explanation, difficulty="easy", source=SHINE, correct=0):
        """correct: index of the right answer in `pairs` (only board items keep a printed order with the answer not first)."""
        options = [o for o, _ in pairs]
        check(len(options) == len(set(options)), f"options: {options}")
        fb = [("Correct!" if i == correct else f) for i, (_, f) in enumerate(pairs)]
        check(all(x.strip() for x in fb), f"feedback missing in {id_}")
        self.q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation, option_feedback=fb)
    def arq(self, id_, concepts, a_, r_, correct, explanation, why_a, why_r, source=SHINE):
        self.ar(id_, concepts, a_, r_, correct, explanation, source)
        self.Q[-1]["option_feedback"] = ar_fb(correct, why_a, why_r)
        self.AR[self.Q[-1]["id"]] = (why_a, why_r)
    def w(self, id_, type_, concepts, question, steps, scheme=None, source=SHINE, difficulty="medium"):
        marks = {"very_short_answer": 2, "short_answer": 3, "long_answer": 5, "case_based": 4}[type_]
        scheme = scheme or {2: MS2, 3: MS3, 5: MS5, 4: CB}[marks]
        if type_ != "case_based": check(len(steps) >= marks - (1 if marks == 5 else 0), f"{id_}: too few points for {marks} marks")
        self.q(id_, type_, marks, concepts, source, question, difficulty, answer_steps=steps, marking_scheme=scheme)

    def _rotate(self, item):
        opts = item.get("options")
        kind = item.get("source", {}).get("kind")
        if not opts or item.get("type") in ("assertion_reason", "true_false", "socratic_question") or kind in ("sample_paper", "pyq"): return
        shift = sum(map(ord, item["id"])) % len(opts)
        rot = lambda xs: xs[shift:] + xs[:shift]
        right = opts[item["correct_index"]]
        item["options"] = rot(opts)
        if "option_feedback" in item: item["option_feedback"] = rot(item["option_feedback"])
        item["correct_index"] = item["options"].index(right)
        check(item.get("option_feedback", ["Correct!"])[item["correct_index"]].startswith("Correct!"), f"feedback misaligned in {item['id']}")

    def write(self, root, path, chapter, keep=None):
        for it in self.Q: self._rotate(it)
        for s in chapter["sections"]:
            for b in s["blocks"]: self._rotate(b)
        ids = [it["id"] for it in self.Q]
        check(len(ids) == len(set(ids)), "duplicate question ids")
        os.makedirs(os.path.join(root, path), exist_ok=True)
        for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": chapter["id"], "questions": self.Q})]:
            with open(os.path.join(root, path, name), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
        print(f"blocks={sum(len(s['blocks']) for s in chapter['sections'])} questions={len(self.Q)}",
              dict(Counter(it['type'] for it in self.Q)), dict(Counter(it['source']['kind'] for it in self.Q)),
              "positions:", dict(Counter(it["correct_index"] for it in self.Q if it["type"] == "mcq")))

def make(subject, n, prefix):
    c = SS(prefix); c.AR = {}
    return c

def header(subject, n, title, concepts, note):
    return {"schema_version": 1, "id": f"cbse.c10.{subject}.ncert.ch{n:02d}", "title": title, "book": BOOKS[subject], "board": "CBSE", "class": 10,
            "subject": subject, "chapter_number": n, "languages": ["en"], "status": "reviewed",
            "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-11", "syllabus_note": note, "concepts": concepts}

def path(subject, folder):
    return f"app_core/content/cbse/class10/social_science/{FOLDER[subject]}/{folder}"
