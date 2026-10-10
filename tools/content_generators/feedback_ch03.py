"""Per-option explanations for Ch 3 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch03_pair_of_linear_equations"

F = {
 "ch03.s2.check": {
  "Yes, it satisfies both equations": "Correct! $3 + 2 = 5$ and $2 \\times 3 - 2 = 4$: both equations are true.",
  "No, it satisfies only the first equation": "Check the second too: $2 \\times 3 - 2 = 4$ ✓. It satisfies both.",
  "No, it satisfies only the second equation": "Check the first too: $3 + 2 = 5$ ✓. It satisfies both.",
  "No, it satisfies neither equation": "Substitute carefully: $3 + 2 = 5$ ✓ and $6 - 2 = 4$ ✓.",
 },
 "ch03.s3.check1": {
  "parallel lines": "Correct! $\\dfrac{6}{2} = \\dfrac{-3}{-1} = 3$ but $\\dfrac{10}{9} \\neq 3$: same slope, different lines.",
  "intersecting lines": "Intersecting needs $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$, but here both ratios are 3.",
  "coincident lines": "Coincident needs all three ratios equal, but $\\dfrac{c_1}{c_2} = \\dfrac{10}{9} \\neq 3$.",
  "perpendicular lines": "Perpendicular lines are not decided by these ratios; here $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$, so they are parallel.",
 },
 "ch03.s3.check2": {
  "$6$": "Correct! $\\dfrac{2}{4} = \\dfrac{3}{k} = \\dfrac{7}{14} = \\dfrac{1}{2}$ gives $k = 6$.",
  "$3$": "Then $\\dfrac{3}{3} = 1 \\neq \\dfrac{1}{2}$. All ratios must equal $\\dfrac{1}{2}$.",
  "$7$": "Then $\\dfrac{3}{7} \\neq \\dfrac{1}{2}$. Solve $\\dfrac{3}{k} = \\dfrac{1}{2}$.",
  "$14$": "Then $\\dfrac{3}{14} \\neq \\dfrac{1}{2}$. Solve $\\dfrac{3}{k} = \\dfrac{1}{2}$.",
 },
 "ch03.s4.check": {
  "$x = 9, y = 5$": "Correct! $y = 14 - x$, so $2x - 14 = 4$, $x = 9$, $y = 5$.",
  "$x = 5, y = 9$": "Check $x - y = 4$: $5 - 9 = -4 \\neq 4$. The values are swapped.",
  "$x = 10, y = 4$": "Check $x - y = 4$: $10 - 4 = 6 \\neq 4$.",
  "$x = 7, y = 7$": "Check $x - y = 4$: $7 - 7 = 0 \\neq 4$.",
 },
 "ch03.s5.check": {
  "multiply the first by 2 and the second by 3, then add": "Correct! The $y$-terms become $+6y$ and $-6y$, which cancel when added.",
  "add the equations as they are": "The $y$-terms $3y$ and $-2y$ do not cancel. First make them equal in size.",
  "multiply both by 3": "The $y$-terms become $9y$ and $-6y$: still not equal in size.",
  "subtract the equations as they are": "Subtracting leaves $5y$: nothing is eliminated.",
 },
 "ch03.q.mcq01": {
  "no solution": "Correct! $\\dfrac{1}{-3} = \\dfrac{2}{-6} \\neq \\dfrac{5}{1}$: the lines are parallel.",
  "a unique solution": "A unique solution needs $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$; here both equal $-\\dfrac{1}{3}$.",
  "exactly two solutions": "Two lines can never meet at exactly two points.",
  "infinitely many solutions": "That needs all three ratios equal, but $\\dfrac{c_1}{c_2} = 5 \\neq -\\dfrac{1}{3}$.",
 },
 "ch03.q.mcq02": {
  "$6$": "Correct! $\\dfrac{2}{4} = \\dfrac{3}{k} = \\dfrac{7}{14}$ gives $k = 6$.",
  "$3$": "Then $\\dfrac{3}{k} = 1 \\neq \\dfrac{1}{2}$.",
  "$-6$": "A negative $k$ makes $\\dfrac{3}{k}$ negative, but it must equal $\\dfrac{1}{2}$.",
  "$12$": "Then $\\dfrac{3}{12} = \\dfrac{1}{4} \\neq \\dfrac{1}{2}$.",
 },
 "ch03.q.mcq03": {
  "$10$": "Correct! $\\dfrac{1}{5} = \\dfrac{2}{k}$ gives $k = 10$, and $\\dfrac{-3}{7} \\neq \\dfrac{1}{5}$.",
  "$5$": "Then $\\dfrac{2}{5} \\neq \\dfrac{1}{5}$: the lines would intersect.",
  "$-10$": "Then $\\dfrac{2}{-10} = -\\dfrac{1}{5} \\neq \\dfrac{1}{5}$.",
  "$2$": "Then $\\dfrac{2}{2} = 1 \\neq \\dfrac{1}{5}$.",
 },
 "ch03.q.mcq04": {
  "$3$ and $1$": "Correct! Adding gives $2x = 6$, so $x = 3$ and $y = 1$.",
  "$1$ and $3$": "Check $x - y = 2$: $1 - 3 = -2$. The values are swapped.",
  "$2$ and $2$": "Check $x - y = 2$: $2 - 2 = 0$.",
  "$4$ and $0$": "Check $x - y = 2$: $4 - 0 = 4$.",
 },
 "ch03.q.mcq05": {
  "parallel": "Correct! $\\dfrac{6}{2} = \\dfrac{-3}{-1} \\neq \\dfrac{10}{9}$.",
  "intersecting at exactly one point": "That needs $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$; here both are 3.",
  "coincident": "That needs $\\dfrac{c_1}{c_2} = 3$ too, but it is $\\dfrac{10}{9}$.",
  "intersecting at exactly two points": "Two straight lines can never meet at exactly two points.",
 },
 "ch03.q.mcq06": {
  "$30$ and $10$": "Correct! $x = 3y$ and $x + 10 = 2(y + 10)$ give $y = 10$, $x = 30$.",
  "$45$ and $15$": "After 10 years: 55 and 25, and $55 \\neq 2 \\times 25$.",
  "$36$ and $12$": "After 10 years: 46 and 22, and $46 \\neq 2 \\times 22$.",
  "$24$ and $8$": "After 10 years: 34 and 18, and $34 \\neq 2 \\times 18$.",
 },
 "ch03.q.mcq07": {
  "$24$ and $11$": "Correct! $24 + 11 = 35$ and $24 - 11 = 13$.",
  "$23$ and $12$": "$23 - 12 = 11$, not 13.",
  "$25$ and $10$": "$25 - 10 = 15$, not 13.",
  "$22$ and $13$": "$22 - 13 = 9$, not 13.",
 },
 "ch03.q.mcq08": {
  "$5$": "Correct! Eliminating $y$ gives $x = 3$, then $y = 2$, so $x + y = 5$.",
  "$6$": "Solve first: $x = 3$, $y = 2$, so $x + y = 5$.",
  "$7$": "Check: $x = 3$, $y = 2$ satisfy both equations, and $3 + 2 = 5$.",
  "$4$": "Check: $x = 3$, $y = 2$, so $x + y = 5$.",
 },
 "ch03.q.mcq09": {
  "$2x + y - 6 = 0$ and $4x - 2y - 4 = 0$": "Correct! $\\dfrac{2}{4} \\neq \\dfrac{1}{-2}$, so the lines intersect (at $(2, 2)$).",
  "$x - y = 8$ and $3x - 3y = 16$": "$\\dfrac{1}{3} = \\dfrac{-1}{-3} \\neq \\dfrac{8}{16}$: parallel, so inconsistent.",
  "$x + y = 5$ and $2x + 2y = 12$": "$\\dfrac{1}{2} = \\dfrac{1}{2} \\neq \\dfrac{5}{12}$: parallel, so inconsistent.",
  "$2x - 2y - 2 = 0$ and $4x - 4y - 5 = 0$": "$\\dfrac{2}{4} = \\dfrac{-2}{-4} \\neq \\dfrac{2}{5}$: parallel, so inconsistent.",
 },
 "ch03.q.mcq10": {
  "infinitely many": "Correct! $\\dfrac{3}{9} = \\dfrac{-1}{-3} = \\dfrac{3}{9}$: the lines coincide.",
  "one": "One solution needs $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$; here they are equal.",
  "two": "Two straight lines can never have exactly two common points.",
  "zero": "No solution needs $\\dfrac{c_1}{c_2}$ to be different, but here all three ratios are $\\dfrac{1}{3}$.",
 },
 "ch03.q.mcq11": {
  "$15$": "Correct! $\\dfrac{2}{6} = \\dfrac{1}{3}$, so $\\dfrac{5}{c} = \\dfrac{1}{3}$ and $c = 15$.",
  "$5$": "Then $\\dfrac{5}{5} = 1 \\neq \\dfrac{1}{3}$: the lines would be parallel.",
  "$10$": "Then $\\dfrac{5}{10} = \\dfrac{1}{2} \\neq \\dfrac{1}{3}$: parallel, not coincident.",
  "$-15$": "Then $\\dfrac{5}{-15} = -\\dfrac{1}{3} \\neq \\dfrac{1}{3}$.",
 },
 "ch03.q.mcq12": {
  "intersect at exactly one point": "Correct! Different slopes mean the lines cross once.",
  "are parallel": "Parallel lines have $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2}$.",
  "coincide": "Coincident lines have all three ratios equal.",
  "do not exist": "Every linear equation in two variables has a straight-line graph.",
 },
 "ch03.q.sqp3": {
  "$\\dfrac{15}{4}$": "With $k = \\dfrac{15}{4}$, $\\dfrac{3}{2} = \\dfrac{2k}{5}$: the lines would be parallel.",
  "$\\neq \\dfrac{15}{4}$": "Correct! Not parallel means $\\dfrac{3}{2} \\neq \\dfrac{2k}{5}$, i.e. $k \\neq \\dfrac{15}{4}$.",
  "any rational number": "Not quite: $k = \\dfrac{15}{4}$ is rational but makes the lines parallel.",
  "any rational number having 4 as denominator": "$k = \\dfrac{15}{4}$ has denominator 4 and makes the lines parallel.",
 },
}

AR = {  # id: (why A, why R)
 "ch03.q.ar1": ("all three ratios equal $\\dfrac{1}{2}$.", "equal ratios mean the same line, which is exactly why there are infinitely many solutions."),
 "ch03.q.ar2": ("$\\dfrac{3}{6} = \\dfrac{-2}{-4} \\neq \\dfrac{5}{9}$.", "this is the condition for parallel lines, which is exactly why there is no solution."),
 "ch03.q.ar3": ("$3 - 2 = 1$ and $3 + 2 = 5$.", "parallel lines never meet."),
 "ch03.q.ar4": ("all three ratios equal $\\dfrac{1}{2}$, so the lines coincide and the pair is consistent.", "coincident lines share every point."),
 "ch03.q.ar5": ("$3 \\times 2 + k \\times 1 = 7$ gives $k = 1$.", "substituting the solution is exactly how $k$ is found."),
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
