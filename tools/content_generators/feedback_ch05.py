"""Per-option explanations for Ch 5 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch05_arithmetic_progressions"

F = {
 "ch05.s2.check": {
  "$-2$": "Correct! $1 - 3 = -2$, and $-1 - 1 = -2$ too.",
  "$2$": "Subtract in the right order: $d = a_2 - a_1 = 1 - 3 = -2$.",
  "$3$": "3 is the first term, not the common difference.",
  "$-1$": "$-1$ is the third term. $d = 1 - 3 = -2$.",
 },
 "ch05.s3.check": {
  "$29$": "Correct! $a_8 = 1 + 7 \\times 4 = 29$.",
  "$33$": "That is $1 + 8 \\times 4$. Use $(n - 1) = 7$, not 8.",
  "$32$": "That is $8 \\times 4$. Start from the first term: $1 + 7 \\times 4$.",
  "$36$": "Use $a_n = a + (n - 1)d = 1 + 7 \\times 4$.",
 },
 "ch05.s4.check": {
  "$210$": "Correct! $5 \\times (6 + 36) = 210$.",
  "$195$": "Check $2a + (n - 1)d = 6 + 36 = 42$, then multiply by $\\dfrac{10}{2} = 5$.",
  "$420$": "Remember to multiply by $\\dfrac{n}{2} = 5$, not by $n = 10$.",
  "$39$": "39 is the 10th term. The question asks for the sum of 10 terms.",
 },
 "ch05.q.ex5_2.q2.i": {
  "$97$": "That uses $d = +3$. Here $d = 7 - 10 = -3$.",
  "$77$": "Mind the sign: $10 + 29 \\times (-3) = 10 - 87 = -77$.",
  "$-77$": "Correct! $a_{30} = 10 + 29 \\times (-3) = -77$.",
  "$-87$": "$-87$ is $29 \\times (-3)$; add the first term 10.",
 },
 "ch05.q.ex5_2.q2.ii": {
  "$28$": "That uses 11 steps of $\\dfrac{5}{2}$ plus 0.5. Use $a_{11} = -3 + 10 \\times \\dfrac{5}{2}$.",
  "$22$": "Correct! $d = \\dfrac{5}{2}$, so $a_{11} = -3 + 25 = 22$.",
  "$-38$": "$d = -\\dfrac{1}{2} - (-3) = +\\dfrac{5}{2}$: the terms increase.",
  "$-48\\dfrac{1}{2}$": "The AP is increasing ($d = \\dfrac{5}{2}$), so the 11th term cannot be negative.",
 },
 "ch05.q.mcq01": {
  "$4$": "Correct! $7 - 3 = 4$.",
  "$-4$": "$d = a_2 - a_1 = 7 - 3 = +4$.",
  "$3$": "3 is the first term.",
  "$\\dfrac{7}{3}$": "The difference, not the ratio: $7 - 3 = 4$.",
 },
 "ch05.q.mcq02": {
  "$41$": "Correct! $5 + 9 \\times 4 = 41$.",
  "$45$": "That is $5 + 10 \\times 4$. Use $(n - 1) = 9$.",
  "$37$": "That is the 9th term.",
  "$50$": "That is $10 \\times 5$; use $a + (n - 1)d$.",
 },
 "ch05.q.mcq03": {
  "$-3, -1, 1, 3, \\ldots$": "Correct! The difference is always 2.",
  "$1, 4, 9, 16, \\ldots$": "Differences $3, 5, 7$ are not equal.",
  "$2, 4, 8, 16, \\ldots$": "Differences $2, 4, 8$: each term is doubled, not increased by a fixed amount.",
  "$1, -1, 1, -1, \\ldots$": "Differences $-2, 2, -2$ are not equal.",
 },
 "ch05.q.mcq04": {
  "$400$": "Correct! $\\dfrac{20}{2}(1 + 39) = 400$.",
  "$200$": "The 20th odd number is 39: $\\dfrac{20}{2}(1 + 39) = 400$.",
  "$420$": "That is the sum of the first 20 even numbers.",
  "$441$": "That is $21^{2}$, the sum of the first 21 odd numbers.",
 },
 "ch05.q.mcq05": {
  "$6$": "Correct! $2(x + 10) = 2x + (3x + 2)$ gives $x = 6$: the terms are 12, 16, 20.",
  "$4$": "Then the terms are 8, 14, 14: not an AP.",
  "$5$": "Then the terms are 10, 15, 17: not an AP.",
  "$8$": "Then the terms are 16, 18, 26: not an AP.",
 },
 "ch05.q.mcq06": {
  "$10 - 3n$": "Correct! $7 + (n - 1)(-3) = 10 - 3n$.",
  "$7 - 3n$": "Check $n = 1$: $7 - 3 = 4$, not 7.",
  "$3n + 4$": "The terms decrease, so the coefficient of $n$ must be negative.",
  "$4 - 3n$": "Check $n = 1$: $4 - 3 = 1$, not 7.",
 },
 "ch05.q.mcq07": {
  "$9$": "Correct! $a_5 = S_5 - S_4 = 25 - 16 = 9$.",
  "$25$": "25 is $S_5$, the sum of five terms, not the 5th term.",
  "$16$": "16 is $S_4$.",
  "$10$": "Use $a_5 = S_5 - S_4 = 25 - 16$.",
 },
 "ch05.q.mcq08": {
  "$34$": "Correct! $\\dfrac{139 - 7}{4} + 1 = 34$.",
  "$33$": "That is the number of steps. Add 1 for the first term.",
  "$35$": "$\\dfrac{139 - 7}{4} = 33$, plus 1 gives 34.",
  "$32$": "$\\dfrac{139 - 7}{4} = 33$, plus 1 gives 34.",
 },
 "ch05.q.mcq09": {
  "$57$": "Correct! $99 - 14 \\times 3 = 57$.",
  "$45$": "That is the 15th term from the beginning.",
  "$54$": "That is $99 - 15 \\times 3$. Use $(n - 1) = 14$.",
  "$60$": "That is the 14th term from the end.",
 },
 "ch05.q.mcq10": {
  "$-5, -5, -5, \\ldots$": "Correct! Adding 0 keeps every term the same.",
  "$-5, 0, 5, \\ldots$": "Here $d = 5$, not 0.",
  "$0, -5, -10, \\ldots$": "The first term must be $-5$, and $d$ here is $-5$.",
  "$-5, -10, -15, \\ldots$": "Here $d = -5$, not 0.",
 },
 "ch05.q.mcq11": {
  "$2$": "Correct! $a_{n+1} - a_n = 2$.",
  "$3$": "3 is the constant term. The terms are 5, 7, 9, so $d = 2$.",
  "$5$": "5 is the first term.",
  "$2n$": "$d$ is a fixed number: $a_{n+1} - a_n = 2$.",
 },
 "ch05.q.mcq12": {
  "$5050$": "Correct! $\\dfrac{100 \\times 101}{2} = 5050$, as Gauss found.",
  "$5000$": "Use $\\dfrac{n(n + 1)}{2}$, not $\\dfrac{n^{2}}{2}$.",
  "$10100$": "Remember to divide by 2.",
  "$5100$": "$\\dfrac{100 \\times 101}{2} = 5050$.",
 },
}

AR = {  # id: (why A, why R)
 "ch05.q.ar1": ("every difference is $7 - 3 = 11 - 7 = 4$.", "a constant difference is exactly what makes a list an AP."),
 "ch05.q.ar2": ("$301 = 6 \\times 50 + 1$ leaves remainder 1, so it is not a term.", "every term is $5 + 6(n - 1)$, which leaves remainder 5, and this is exactly why 301 cannot be a term."),
 "ch05.q.ar3": ("$S_{10} = 10 \\times 11 = 110$, not 100.", "$S_n = \\dfrac{n}{2}\\left[4 + 2(n - 1)\\right] = n(n + 1)$."),
 "ch05.q.ar4": ("$5 + 9 \\times 3 = 32$.", "the common difference can also be negative or zero, as in $10, 7, 4, \\ldots$"),
 "ch05.q.ar5": ("$a_1 = S_1 = 1^{2} = 1$.", "it is true, but A follows from $a_1 = S_1$, not from this fact."),
}

_TRUTH = {0: (True, True, True), 1: (True, True, False), 2: (True, False, None), 3: (False, True, None)}
_CLAIMS = [(True, True, True), (True, True, False), (True, False, None), (False, True, None)]
def ar_fb(ci, wa, wr):
    a, r, e = _TRUTH[ci]; out = []
    for ca, cr, ce in _CLAIMS:
        if (ca, cr) == (a, r) and (ce is None or ce == e):
            out.append(f"Correct! A is {'true' if a else 'false'}: {wa} R is {'true' if r else 'false'}: {wr}")
        elif ca != a: out.append(f"Check the Assertion again: it is {'true' if a else 'false'}, because {wa}")
        elif cr != r: out.append(f"Check the Reason again: it is {'true' if r else 'false'}, because {wr}")
        else: out.append(("R does explain A: " if e else "Both are true, but R is not the reason A is true: ") + wr)
    return out

def apply(item):
    if item.get("type") == "assertion_reason":
        item["option_feedback"] = ar_fb(item["correct_index"], *AR[item["id"]]); return
    spec = F[item["id"]]
    missing = [o for o in item["options"] if o not in spec]
    assert not missing, (item["id"], missing)
    item["option_feedback"] = [spec[o] for o in item["options"]]
    assert item["option_feedback"][item["correct_index"]].startswith("Correct!"), item["id"]

qp, cp = f"{BASE}/questions.json", f"{BASE}/chapter.json"
bank, chapter = json.load(open(qp)), json.load(open(cp))
n = 0
for q in bank["questions"]:
    if q["type"] in ("mcq", "assertion_reason"): apply(q); n += 1
for s in chapter["sections"]:
    for blk in s["blocks"]:
        if blk["type"] == "knowledge_check": apply(blk); n += 1
for p, d in ((qp, bank), (cp, chapter)):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, indent=2); f.write("\n")
print("items with feedback:", n)
