"""Shared helpers for CBSE Class 10 English Grammar chapters (same content format as maths and science).

Every objective item is written as a list of (option, feedback) pairs with the right answer FIRST;
write() then moves the answer to an id-dependent position and keeps feedback aligned with its option."""
import json, os
from collections import Counter

def check(cond, msg):
    if not cond: raise SystemExit(f"WRONG: {msg}")

SHINE = {"kind": "shine"}
AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
BOOK = "Shine Academy English Grammar, Class 10 (CBSE 184)"

def _options(pairs):
    check(len(pairs) >= 2, "need two options")
    texts = [o for o, _ in pairs]
    check(len(texts) == len(set(texts)), f"repeated option in {texts}")
    check(all(f.strip() for _, f in pairs[1:]), f"every wrong option needs feedback: {texts}")
    return texts, ["Correct!"] + [f for _, f in pairs[1:]]

class Grammar:
    def __init__(self, prefix):
        self.prefix, self.Q = prefix, []
    def blk(self, id_, type_, **kw): return {"id": f"{self.prefix}.{id_}", "type": type_, **kw}
    def check_block(self, id_, question, pairs, explanation, type_="knowledge_check"):
        options, fb = _options(pairs)
        return self.blk(id_, type_, question=question, options=options, correct_index=0, explanation=explanation, option_feedback=fb)
    def socratic(self, id_, question, options, correct, explanation):
        return self.blk(id_, "socratic_question", question=question, options=options, correct_index=correct, explanation=explanation)
    def q(self, id_, type_, marks, concepts, question, difficulty="medium", **kw):
        self.Q.append({"id": f"{self.prefix}.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
                       "source": SHINE, "question": question, "status": "reviewed", **kw})
    def mcq(self, id_, concepts, question, pairs, explanation, difficulty="easy"):
        options, fb = _options(pairs)
        self.q(id_, "mcq", 1, concepts, question, difficulty, options=options, correct_index=0, explanation=explanation, option_feedback=fb)
    def tf(self, id_, concepts, statement, true, explanation, difficulty="easy"):
        c = 0 if true else 1
        self.q(id_, "true_false", 1, concepts, f"State whether the following statement is true or false: {statement}", difficulty,
               options=["True", "False"], correct_index=c, explanation=explanation,
               option_feedback=[("Correct! " if i == c else "Not quite. ") + explanation for i in range(2)])
    def ar(self, id_, concepts, a_, r_, correct, explanation, why_a, why_r):
        """why_a / why_r: short reasons, used in the feedback for every option."""
        truth = [(True, True, True), (True, True, False), (True, False, None), (False, True, None)]
        a_true, r_true, _ = truth[correct]
        fb = []
        for i in range(4):
            head = "Correct!" if i == correct else "Not quite."
            fb.append(f"{head} A is {'true' if a_true else 'false'}: {why_a} R is {'true' if r_true else 'false'}: {why_r}")
        self.q(id_, "assertion_reason", 1, concepts, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium",
               options=AR_OPTIONS, correct_index=correct, explanation=explanation, option_feedback=fb)

    @staticmethod
    def _spread(item):
        if item.get("type") in ("assertion_reason", "true_false", "socratic_question") or "options" not in item: return
        n = len(item["options"])
        shift = sum(map(ord, item["id"])) % n
        rot = lambda xs: xs[shift:] + xs[:shift]
        right = item["options"][item["correct_index"]]
        item["options"] = rot(item["options"])
        if "option_feedback" in item: item["option_feedback"] = rot(item["option_feedback"])
        item["correct_index"] = item["options"].index(right)
        check(item.get("option_feedback", ["Correct!"] * n)[item["correct_index"]].startswith("Correct!"), f"feedback misaligned in {item['id']}")

    def write(self, root, path, chapter):
        for it in self.Q: self._spread(it)
        for s in chapter["sections"]:
            for b in s["blocks"]: self._spread(b)
        ids = [it["id"] for it in self.Q]
        check(len(ids) == len(set(ids)), "duplicate question ids")
        qs = [(it["question"], tuple(sorted(it.get("options", [])))) for it in self.Q]
        dup = [q for q, c in Counter(qs).items() if c > 1]
        check(not dup, f"duplicate questions: {dup[:3]}")
        os.makedirs(os.path.join(root, path), exist_ok=True)
        for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": chapter["id"], "questions": self.Q})]:
            with open(os.path.join(root, path, name), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
        print(f"blocks={sum(len(s['blocks']) for s in chapter['sections'])} questions={len(self.Q)} types={dict(Counter(it['type'] for it in self.Q))}",
              "answer positions:", dict(Counter(it["correct_index"] for it in self.Q if it["type"] == "mcq")))

def header(n, title, concepts, note):
    return {"schema_version": 1, "id": f"cbse.c10.english.grammar.ch{n:02d}", "title": title, "book": BOOK, "board": "CBSE", "class": 10,
            "subject": "english_grammar", "chapter_number": n, "languages": ["en"], "status": "reviewed",
            "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10", "syllabus_note": note, "concepts": concepts}
