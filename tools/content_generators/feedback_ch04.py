"""Per-option explanations for Ch 4 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch04_quadratic_equations"

F = {
 "ch04.s2.check": {
  "$x(x + 3) = 10$": "Correct! It becomes $x^{2} + 3x - 10 = 0$: the highest power is 2.",
  "$x^{2} + 2x = x^{2} - 5$": "The $x^{2}$ terms cancel, leaving $2x + 5 = 0$: linear.",
  "$x^{3} - x = 0$": "The highest power is 3, so it is not quadratic.",
  "$2x + 3 = 7$": "There is no $x^{2}$ term: this is linear.",
 },
 "ch04.s3.check": {
  "$5$ and $-2$": "Correct! $(x - 5)(x + 2) = 0$ gives $x = 5$ or $x = -2$.",
  "$-5$ and $2$": "The signs are reversed. Check: $(-5)^{2} - 3(-5) - 10 = 30 \\neq 0$.",
  "$10$ and $-1$": "Their product is $-10$, but their sum is $9$, not $3$.",
  "$2$ and $5$": "Check: $4 - 6 - 10 = -12 \\neq 0$. Mind the signs: the product of the roots is $-10$.",
 },
 "ch04.s4.check": {
  "$2 \\pm \\sqrt{3}$": "Correct! $x = \\dfrac{4 \\pm \\sqrt{12}}{2} = 2 \\pm \\sqrt{3}$.",
  "$4 \\pm \\sqrt{3}$": "Do not forget to divide $-b = 4$ by $2a = 2$ as well.",
  "$-2 \\pm \\sqrt{3}$": "Here $b = -4$, so $-b = +4$, and $\\dfrac{4}{2} = 2$.",
  "$2 \\pm \\sqrt{5}$": "The discriminant is $b^{2} - 4ac = 16 - 4 = 12$, not $16 + 4$.",
 },
 "ch04.s5.check1": {
  "real and equal": "Correct! $b^{2} - 4ac = 144 - 144 = 0$.",
  "real and distinct": "That needs $b^{2} - 4ac > 0$, but here it is $144 - 144 = 0$.",
  "not real": "That needs $b^{2} - 4ac < 0$, but here it is exactly $0$.",
  "more than two in number": "A quadratic equation never has more than two roots.",
 },
 "ch04.s5.check2": {
  "$\\pm 4$": "Correct! $k^{2} - 16 = 0$ gives $k = 4$ or $k = -4$.",
  "$\\pm 2$": "Then $k^{2} - 16 = 4 - 16 \\neq 0$. Remember $4ac = 4 \\times 2 \\times 2 = 16$.",
  "$4$ only": "$k = -4$ also works, because $(-4)^{2} = 16$ too.",
  "$\\pm 16$": "$k^{2} = 16$, so $k = \\pm 4$, not $\\pm 16$.",
 },
 "ch04.q.mcq01": {
  "$(x - 2)^{2} + 1 = 2x - 3$": "Correct! It simplifies to $x^{2} - 6x + 8 = 0$.",
  "$x(x + 1) + 8 = (x + 2)(x - 2)$": "The $x^{2}$ terms cancel, leaving $x + 12 = 0$: linear.",
  "$x^{2} + 3x + 1 = (x - 2)^{2}$": "The $x^{2}$ terms cancel, leaving $7x - 3 = 0$: linear.",
  "$(x + 2)^{3} = 2x(x^{2} - 1)$": "After simplifying, an $x^{3}$ term remains: degree 3.",
 },
 "ch04.q.mcq02": {
  "$2$ and $3$": "Correct! $(x - 2)(x - 3) = 0$.",
  "$-2$ and $-3$": "Check: $4 + 10 + 6 = 20 \\neq 0$. The signs are reversed.",
  "$6$ and $-1$": "Those are the roots of $x^{2} - 5x - 6 = 0$: the constant term is $+6$ here.",
  "$1$ and $6$": "Their product is 6 but their sum is 7, not 5.",
 },
 "ch04.q.mcq03": {
  "$-8$": "Correct! $(-4)^{2} - 4 \\times 2 \\times 3 = 16 - 24 = -8$.",
  "$8$": "$16 - 24$ is negative: $-8$.",
  "$40$": "It is $b^{2} - 4ac$, not $b^{2} + 4ac$.",
  "$4$": "Use $b^{2} - 4ac$ with $b = -4$: $16 - 24 = -8$.",
 },
 "ch04.q.mcq04": {
  "no real roots": "Correct! $b^{2} - 4ac = 16 - 20 = -4 < 0$.",
  "two distinct real roots": "That needs $b^{2} - 4ac > 0$, but it is $-4$.",
  "two equal real roots": "That needs $b^{2} - 4ac = 0$, but it is $-4$.",
  "more than two real roots": "A quadratic equation has at most two roots.",
 },
 "ch04.q.mcq05": {
  "$\\pm 6$": "Correct! $k^{2} - 36 = 0$, so $k = 6$ or $k = -6$.",
  "$6$ only": "$k = -6$ also works: $(-6)^{2} = 36$.",
  "$\\pm 3$": "Then $k^{2} = 9 \\neq 36$. The condition is $k^{2} = 4 \\times 1 \\times 9$.",
  "$\\pm 9$": "Then $k^{2} = 81 \\neq 36$.",
 },
 "ch04.q.mcq06": {
  "$1$": "Correct! $4 + 2k - 6 = 0$ gives $k = 1$.",
  "$-1$": "Then $4 - 2 - 6 = -4 \\neq 0$.",
  "$2$": "Then $4 + 4 - 6 = 2 \\neq 0$.",
  "$3$": "Then $4 + 6 - 6 = 4 \\neq 0$.",
 },
 "ch04.q.mcq07": {
  "$11$ and $12$": "Correct! $11 \\times 12 = 132$.",
  "$12$ and $13$": "$12 \\times 13 = 156$, not 132.",
  "$10$ and $11$": "$10 \\times 11 = 110$, not 132.",
  "$13$ and $14$": "$13 \\times 14 = 182$, not 132.",
 },
 "ch04.q.mcq08": {
  "$0$ and $9$": "Correct! $x(x - 9) = 0$ gives both roots.",
  "$9$ only": "Dividing by $x$ loses the root $x = 0$. Factorise instead: $x(x - 9) = 0$.",
  "$3$ and $-3$": "Those are the roots of $x^{2} = 9$, not $x^{2} = 9x$.",
  "$0$ only": "$x = 9$ also works: $81 = 81$.",
 },
 "ch04.q.mcq09": {
  "$2x^{2} - 3x + 1 = 0$": "Correct! $b^{2} - 4ac = 9 - 8 = 1 > 0$.",
  "$x^{2} + x + 1 = 0$": "$b^{2} - 4ac = 1 - 4 = -3 < 0$: no real roots.",
  "$4x^{2} - 4x + 1 = 0$": "$b^{2} - 4ac = 16 - 16 = 0$: equal roots, not distinct.",
  "$x^{2} + 2x + 3 = 0$": "$b^{2} - 4ac = 4 - 12 = -8 < 0$: no real roots.",
 },
 "ch04.q.mcq10": {
  "$\\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$": "Correct! This is Sridharacharya's formula.",
  "$\\dfrac{b \\pm \\sqrt{b^{2} - 4ac}}{2a}$": "The formula starts with $-b$, not $b$.",
  "$\\dfrac{-b \\pm \\sqrt{b^{2} + 4ac}}{2a}$": "Under the root it is $b^{2} - 4ac$.",
  "$-b \\pm \\dfrac{\\sqrt{b^{2} - 4ac}}{2a}$": "The whole numerator $-b \\pm \\sqrt{b^{2} - 4ac}$ is divided by $2a$.",
 },
 "ch04.q.mcq11": {
  "$2$": "Correct! Degree 2 means at most 2 roots.",
  "$1$": "Many quadratic equations have two roots, like $x^{2} - 4 = 0$.",
  "$3$": "Only a degree-3 equation can have 3 roots.",
  "infinitely many": "A quadratic equation has at most 2 roots.",
 },
 "ch04.q.mcq12": {
  "$4$ cm": "Correct! $4 \\times 6 = 24$.",
  "$6$ cm": "Then the length is 8 cm and the area $48 \\neq 24$. 6 cm is the length.",
  "$3$ cm": "Then the area is $3 \\times 5 = 15 \\neq 24$.",
  "$2$ cm": "Then the area is $2 \\times 4 = 8 \\neq 24$.",
 },
 "ch04.q.sqp6": {
  "$(x + 2)^{2} = 2(x + 3)$": "This becomes $x^{2} + 2x - 2 = 0$: quadratic.",
  "$x^{2} + 3x = (-1)(1 - 3x)^{2}$": "This becomes $10x^{2} - 3x + 1 = 0$: quadratic.",
  "$x^{3} - x^{2} + 2x + 1 = (x + 1)^{3}$": "The $x^{3}$ terms cancel, leaving $4x^{2} + x = 0$: quadratic.",
  "$(x + 2)(x + 1) = x^{2} + 2x + 3$": "Correct! $x^{2} + 3x + 2 = x^{2} + 2x + 3$ gives $x - 1 = 0$: linear.",
 },
}

AR = {  # id: (why A, why R)
 "ch04.q.ar1": ("$b^{2} - 4ac = 4 - 20 = -16 < 0$.", "a negative discriminant is exactly why there are no real roots."),
 "ch04.q.ar2": ("$4 - 6 + 2 = 0$.", "a quadratic equation never has more than two roots, but this does not show that 2 satisfies the equation."),
 "ch04.q.ar3": ("it simplifies to $-2x = 0$, which is linear.", "this is the definition of a quadratic equation."),
 "ch04.q.ar4": ("$b^{2} - 4ac = 36 - 36 = 0$.", "a zero discriminant is exactly why the roots are equal."),
 "ch04.q.ar5": ("$2^{2} - 4 = 0$ and $(-2)^{2} - 4 = 0$.", "for example, $x^{2} + 1 = 0$ has no real roots."),
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
