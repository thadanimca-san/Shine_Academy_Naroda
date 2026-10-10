"""Shared helpers for CBSE Class 10 Science chapter generators.

ce() turns a plain equation such as "2H2(g) + O2(g) -> 2H2O(l)" into LaTeX and
refuses any equation whose atoms do not balance, so a wrong equation can never
reach students."""
import json, os, re
from collections import Counter

def check(cond, msg):
    if not cond: raise SystemExit("WRONG: " + msg)

# ---------------------------------------------------------------- chemistry
_STATE = re.compile(r"\((s|l|g|aq)\)$")
def _atoms(formula):
    """Atom counts of one formula unit, e.g. 'Al2(SO4)3' or 'CuSO4.5H2O'."""
    total = Counter()
    for part in formula.split("."):
        m = re.match(r"^(\d*)(.*)$", part); mult = int(m.group(1) or 1)
        stack = [Counter()]; i = 0; s = m.group(2)
        while i < len(s):
            ch = s[i]
            if ch == "(":
                stack.append(Counter()); i += 1
            elif ch == ")":
                j = i + 1
                while j < len(s) and s[j].isdigit(): j += 1
                n = int(s[i + 1:j] or 1); top = stack.pop()
                for k, v in top.items(): stack[-1][k] += v * n
                i = j
            else:
                m2 = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
                if not m2: raise SystemExit(f"cannot read formula {formula!r}")
                stack[-1][m2.group(1)] += int(m2.group(2) or 1); i += len(m2.group(0))
        for k, v in stack[0].items(): total[k] += v * mult
    return total

def _species(token):
    token = token.strip().rstrip("↑↓")
    m = re.match(r"^(\d*)(.+?)$", token)
    coef, rest = int(m.group(1) or 1), _STATE.sub("", m.group(2))
    return coef, rest

def balanced(eq):
    left, _, right = re.split(r"\s(->|-\[[^\]]*\]->)\s", eq)
    def side(s):
        c = Counter()
        for t in s.split(" + "):
            coef, f = _species(t)
            for k, v in _atoms(f).items(): c[k] += coef * v
        return c
    return side(left) == side(right)

def _tex_species(token):
    arrow = ""
    if token.endswith("↑"): arrow, token = " \\uparrow", token[:-1]
    if token.endswith("↓"): arrow, token = " \\downarrow", token[:-1]
    m = re.match(r"^(\d*)(.+?)$", token)
    coef, body = m.group(1), m.group(2)
    state = ""
    sm = _STATE.search(body)
    if sm: state, body = sm.group(0), body[:sm.start()]
    body = re.sub(r"(?<=[A-Za-z)])(\d+)", r"_{\1}", body).replace(".", " \\cdot ")
    return f"{coef}{body}{state}{arrow}"

def ce(eq, check_balance=True):
    """'2H2 + O2 -> 2H2O' as inline LaTeX. '-[D]->' puts Δ (heat) over the arrow."""
    if check_balance:
        check(balanced(eq), f"unbalanced equation: {eq}")
    left, arrow, right = re.split(r"\s(->|-\[[^\]]*\]->)\s", eq)
    over = re.match(r"-\[([^\]]*)\]->", arrow)
    arr = "\\xrightarrow{\\Delta}" if over and over.group(1) == "D" else "\\rightarrow"
    tex = " + ".join(_tex_species(t) for t in left.split(" + ")) + f" {arr} " + " + ".join(_tex_species(t) for t in right.split(" + "))
    return f"$\\mathrm{{{tex}}}$"

def chem(formula):
    """A single formula such as 'CuSO4' as inline LaTeX."""
    return f"$\\mathrm{{{_tex_species(formula)}}}$"

# ---------------------------------------------------------------- content builders
AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Science (086)", "question": n}
SHINE = {"kind": "shine"}
def pyq_gseb(year, n): return {"kind": "pyq", "year": year, "paper": f"GSEB SSC Science, March {year}", "question": n}

class Chapter:
    def __init__(self, prefix):
        self.prefix, self.Q = prefix, []
    def blk(self, id_, type_, **kw): return {"id": f"{self.prefix}.{id_}", "type": type_, **kw}
    def placed(self, id_, figure): return {"id": f"{self.prefix}.{id_}", **figure}
    def q(self, id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
        self.Q.append({"id": f"{self.prefix}.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
                       "source": source, "question": question, "status": "reviewed", **kw})
    def mcq(self, id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
        self.q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
    def ar(self, id_, concepts, a_, r_, correct, explanation, source=SHINE):
        self.q(id_, "assertion_reason", 1, concepts, source, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)

    def tf(self, id_, concepts, statement, true, explanation, source=SHINE, difficulty="easy"):
        """True/false item; feedback repeats the explanation after 'Correct!' or 'Not quite.'."""
        correct = 0 if true else 1
        self.q(id_, "true_false", 1, concepts, source, f"State whether the following statement is true or false: {statement}", difficulty,
               options=["True", "False"], correct_index=correct, explanation=explanation,
               option_feedback=[("Correct! " if i == correct else "Not quite. ") + explanation for i in range(2)])

    def spread(self, item, keep=lambda item: False):
        """Moves the right answer to a position that depends on the id, so it is not always first.
        Board-paper items and assertion-reason items keep their printed order."""
        opts = item.get("options")
        kind = item.get("source", {}).get("kind")
        if not opts or item.get("type") in ("assertion_reason", "true_false") or kind in ("sample_paper", "pyq") or keep(item):
            return
        shift = sum(map(ord, item["id"])) % len(opts)
        correct = opts[item["correct_index"]]
        item["options"] = opts[shift:] + opts[:shift]
        item["correct_index"] = item["options"].index(correct)

    def write(self, root, path, chapter, keep=lambda item: False):
        for it in self.Q: self.spread(it, keep)
        for s in chapter["sections"]:
            for b in s["blocks"]: self.spread(b, keep)
        ids = [it["id"] for it in self.Q]
        check(len(ids) == len(set(ids)), "duplicate question ids")
        os.makedirs(os.path.join(root, path), exist_ok=True)
        for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": chapter["id"], "questions": self.Q})]:
            with open(os.path.join(root, path, name), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
        kinds = Counter(it["source"]["kind"] for it in self.Q)
        print(f"blocks={sum(len(s['blocks']) for s in chapter['sections'])} questions={len(self.Q)} sources={dict(kinds)}",
              "answer positions:", Counter(it["correct_index"] for it in self.Q if it["type"] == "mcq"))

if __name__ == "__main__":
    for e in ["2H2 + O2 -> 2H2O", "Fe2O3 + 2Al -> Al2O3 + 2Fe", "3BaCl2 + Al2(SO4)3 -> 2AlCl3 + 3BaSO4", "CuSO4.5H2O -[D]-> CuSO4 + 5H2O",
              "2Pb(NO3)2(s) -[D]-> 2PbO(s) + 4NO2(g) + O2(g)"]:
        print(balanced(e), ce(e))
    print(balanced("Fe + H2O -> Fe3O4 + H2"))
