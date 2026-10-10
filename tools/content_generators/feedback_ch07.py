"""Per-option explanations for Ch 7 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch07_coordinate_geometry"

F = {
 "ch07.s2.check1": {"$5$": "Correct! $\\sqrt{9 + 16} = 5$.", "$7$": "Don't add the coordinates: square them, add, then take the root.",
                    "$25$": "25 is $3^{2} + 4^{2}$; take the square root.", "$1$": "That is $4 - 3$. Use $\\sqrt{x^{2} + y^{2}}$."},
 "ch07.s2.check2": {"$2$": "Correct! The distance from the $y$-axis is the $x$-coordinate.", "$3$": "3 is the distance from the $x$-axis.",
                    "$\\sqrt{13}$": "$\\sqrt{13}$ is the distance from the origin.", "$5$": "Adding the coordinates does not give a distance."},
 "ch07.s3.check1": {"$(4, 2)$": "Correct! $\\left(\\dfrac{8}{2}, \\dfrac{4}{2}\\right)$.", "$(8, 4)$": "Remember to divide the sums by 2.",
                    "$(2, 3)$": "Add the coordinates, don't subtract them: $\\dfrac{2 + 6}{2} = 4$.", "$(4, 3)$": "$\\dfrac{5 + (-1)}{2} = 2$, not 3."},
 "ch07.s3.check2": {"$(2, 3)$": "Correct! One-third of the way from $(0, 0)$ to $(6, 9)$.", "$(4, 6)$": "That divides it in $2 : 1$, two-thirds of the way.",
                    "$(3, 4.5)$": "That is the mid-point (ratio $1 : 1$).", "$(1, 1.5)$": "That is one-sixth of the way. Divide by $1 + 2 = 3$."},
 "ch07.q.mcq01": {"$5$": "Correct! $\\sqrt{9 + 16} = 5$.", "$7$": "Don't add the coordinates.", "$25$": "Take the square root of 25.", "$1$": "Use $\\sqrt{x^{2} + y^{2}}$."},
 "ch07.q.mcq02": {"$5$": "Correct! $\\sqrt{3^{2} + 4^{2}} = 5$.", "$25$": "Take the square root of 25.", "$7$": "That is $3 + 4$; square, add, then take the root.", "$\\sqrt{7}$": "Square the differences: $9 + 16 = 25$."},
 "ch07.q.mcq03": {"$(4, 2)$": "Correct!", "$(8, 4)$": "Divide the sums by 2.", "$(2, 3)$": "Add the coordinates: $\\dfrac{2 + 6}{2} = 4$.", "$(4, 3)$": "$\\dfrac{5 - 1}{2} = 2$."},
 "ch07.q.mcq04": {"$(x, 0)$": "Correct! The $y$-coordinate is 0.", "$(0, y)$": "That is a point on the $y$-axis.", "$(x, x)$": "That is a point on the line $y = x$.", "$(0, 0)$": "That is only the origin."},
 "ch07.q.mcq05": {"$(2, 3)$": "Correct! One-third of the way.", "$(4, 6)$": "That is the ratio $2 : 1$.", "$(3, 4.5)$": "That is the mid-point.", "$(1, 1.5)$": "Divide by $1 + 2 = 3$, not 6."},
 "ch07.q.mcq06": {"$10$": "Correct! $\\sqrt{36 + 64} = 10$.", "$2$": "That is $8 - 6$. Square first.", "$14$": "Don't add the numbers: $\\sqrt{36 + 64}$.", "$6$": "6 is only the horizontal part."},
 "ch07.q.mcq07": {"$\\pm 4$": "Correct! $p^{2} = 16$, so $p = 4$ or $-4$.", "$4$ only": "$p = -4$ also gives $p^{2} = 16$.", "$-4$ only": "$p = 4$ also works.", "$0$": "Then the distance is 3, not 5."},
 "ch07.q.mcq08": {"$1 : 1$": "Correct! $5k - 5 = 0$ gives $k = 1$.", "$1 : 2$": "Then $y = \\dfrac{5 - 10}{3} \\neq 0$.", "$2 : 1$": "Then $y = \\dfrac{10 - 5}{3} \\neq 0$.", "$5 : 1$": "Then $y = \\dfrac{25 - 5}{6} \\neq 0$."},
 "ch07.q.mcq09": {"$12$": "Correct! $3 + 4 + 5 = 12$.", "$7$": "Include the third side, the hypotenuse 5.", "$10$": "The hypotenuse is 5, not 3.", "$5$": "5 is only the hypotenuse."},
 "ch07.q.mcq10": {"$(-3, 2)$": "Correct! The origin is halfway between $A$ and $B$.", "$(3, -2)$": "That is $A$ itself.", "$(6, -4)$": "That is $2A$, not the reflection.", "$(-6, 4)$": "Halve that: $B = (-3, 2)$."},
 "ch07.q.mcq11": {"$3$": "Correct! The distance from the $x$-axis is the $y$-coordinate.", "$2$": "2 is the distance from the $y$-axis.", "$\\sqrt{13}$": "That is the distance from the origin.", "$5$": "Adding coordinates does not give a distance."},
 "ch07.q.mcq12": {"$(1, 3)$": "Correct!", "$(2, 1)$": "Check: $\\dfrac{2 \\times 4 + 3 \\times (-1)}{5} = 1$, not 2.", "$(3, 1)$": "Multiply 2 with the far end $(4, -3)$ and 3 with $(-1, 7)$.", "$(1, 5)$": "$y = \\dfrac{-6 + 21}{5} = 3$."},
 "ch07.q.sqp2": {"$2$": "Correct! The shortest distance from the $y$-axis is the $x$-coordinate.", "$3$": "3 is the distance from the $x$-axis.", "$5$": "Adding coordinates does not give a distance.", "$1$": "That is $3 - 2$; use the $x$-coordinate."},
 "ch07.q.sqp16": {"Square": "A square needs equal adjacent sides; $AB = 6$ but $BC = \\sqrt{360}$.", "Rectangle": "$AB$ is vertical but $BC$ is not horizontal, so the angle at $B$ is not $90^\\circ$.",
                  "Parallelogram": "Correct! Opposite sides are equal and parallel.", "Trapezium": "Both pairs of opposite sides are parallel, so it is a parallelogram."},
 "ch07.q.ex7_1.q1.i": None,
}
F = {k: v for k, v in F.items() if v}

AR = {
 "ch07.q.ar1": ("its $x$-coordinate is 0.", "having $x$-coordinate 0 is exactly what puts a point on the $y$-axis."),
 "ch07.q.ar2": ("$\\sqrt{9 + 16} = 5$.", "the distance is $\\sqrt{x^{2} + y^{2}}$, not $x + y$."),
 "ch07.q.ar3": ("the mid-point is $(3, 5)$.", "this is the mid-point formula."),
 "ch07.q.ar4": ("both distances are $\\sqrt{106}$.", "it is true, but it does not show why the two distances are equal."),
 "ch07.q.ar5": ("$\\left(\\dfrac{6 - 8}{7}, \\dfrac{-12 - 8}{7}\\right) = \\left(-\\dfrac{2}{7}, -\\dfrac{20}{7}\\right)$.", "this is the section formula, which gives the point directly."),
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
