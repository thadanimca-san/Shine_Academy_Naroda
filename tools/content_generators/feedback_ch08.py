"""Per-option explanations for Ch 8 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch08_introduction_to_trigonometry"

F = {
 "ch08.s2.check1": {"$\\dfrac{4}{5}$": "Correct! Sides 3, 4, 5: $\\cos A = \\dfrac{4}{5}$.", "$\\dfrac{3}{4}$": "That is $\\tan A$: opposite over adjacent.",
                    "$\\dfrac{5}{3}$": "That is $\\text{cosec } A$, the reciprocal of $\\sin A$.", "$\\dfrac{2}{5}$": "$\\cos A$ is not $1 - \\sin A$. Use $\\sin^{2} A + \\cos^{2} A = 1$."},
 "ch08.s2.check2": {"$\\sec A$": "Correct! $\\sec A = \\dfrac{1}{\\cos A}$.", "$\\text{cosec } A$": "$\\text{cosec } A$ is the reciprocal of $\\sin A$.",
                    "$\\cot A$": "$\\cot A$ is the reciprocal of $\\tan A$.", "$\\tan A$": "$\\tan A = \\dfrac{\\sin A}{\\cos A}$, not $\\dfrac{1}{\\cos A}$."},
 "ch08.s3.check": {"$1$": "Correct! $\\dfrac{1}{2} + \\dfrac{1}{2} = 1$.", "$\\dfrac{1}{2}$": "Both terms are $\\dfrac{1}{2}$; add them.",
                   "$\\sqrt{3}$": "$\\sin 30^\\circ = \\cos 60^\\circ = \\dfrac{1}{2}$.", "$0$": "They are equal, so the sum (not the difference) is 1."},
 "ch08.s4.check": {"$9$": "Correct! $9(\\sec^{2} A - \\tan^{2} A) = 9 \\times 1$.", "$1$": "Don't forget the factor 9.", "$8$": "$\\sec^{2} A - \\tan^{2} A = 1$, so the answer is $9 \\times 1$.", "$0$": "$\\sec^{2} A$ and $\\tan^{2} A$ differ by 1, not 0."},
 "ch08.q.ex8_2.q2.i": {"$\\sin 60^\\circ$": "Correct! The value is $\\dfrac{\\sqrt{3}}{2}$.", "$\\cos 60^\\circ$": "The value is $\\dfrac{\\sqrt{3}}{2}$, but $\\cos 60^\\circ = \\dfrac{1}{2}$.",
                       "$\\tan 60^\\circ$": "That is $\\dfrac{2\\tan 30^\\circ}{1 - \\tan^{2} 30^\\circ}$, with a minus sign.", "$\\sin 30^\\circ$": "$\\sin 30^\\circ = \\dfrac{1}{2}$, but the value is $\\dfrac{\\sqrt{3}}{2}$."},
 "ch08.q.ex8_2.q2.ii": {"$\\tan 90^\\circ$": "$\\tan 90^\\circ$ is not defined, but the value here is 0.", "$1$": "The numerator $1 - 1 = 0$.", "$\\sin 45^\\circ$": "The numerator is 0, so the value is 0.", "$0$": "Correct! $\\dfrac{1 - 1}{1 + 1} = 0$."},
 "ch08.q.ex8_2.q2.iii": {"$0^\\circ$": "Correct! Both sides are 0.", "$30^\\circ$": "$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ but $2\\sin 30^\\circ = 1$.",
                         "$45^\\circ$": "$\\sin 90^\\circ = 1$ but $2\\sin 45^\\circ = \\sqrt{2}$.", "$60^\\circ$": "$\\sin 120^\\circ \\neq 2\\sin 60^\\circ = \\sqrt{3}$, which is more than 1."},
 "ch08.q.ex8_2.q2.iv": {"$\\cos 60^\\circ$": "The value is $\\sqrt{3}$, but $\\cos 60^\\circ = \\dfrac{1}{2}$.", "$\\sin 60^\\circ$": "That is the answer with a plus sign in the denominator.",
                        "$\\tan 60^\\circ$": "Correct! The value is $\\sqrt{3}$.", "$\\sin 30^\\circ$": "The value is $\\sqrt{3}$, but $\\sin 30^\\circ = \\dfrac{1}{2}$."},
 "ch08.q.ex8_3.q3.i": {"$1$": "Don't forget the factor 9.", "$9$": "Correct! $9 \\times 1 = 9$.", "$8$": "$\\sec^{2} A - \\tan^{2} A = 1$, so it is $9 \\times 1$.", "$0$": "$\\sec^{2} A$ and $\\tan^{2} A$ differ by 1."},
 "ch08.q.ex8_3.q3.ii": {"$0$": "Check with $\\theta = 45^\\circ$: $(2 + \\sqrt{2})(2 - \\sqrt{2}) = 2$.", "$1$": "Check with $\\theta = 45^\\circ$: the product is 2.",
                        "$2$": "Correct! The product simplifies to $\\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$.", "$-1$": "Check with $\\theta = 45^\\circ$: the product is 2."},
 "ch08.q.ex8_3.q3.iii": {"$\\sec A$": "Multiply out: $\\dfrac{(1 + \\sin A)(1 - \\sin A)}{\\cos A} = \\cos A$.", "$\\sin A$": "$1 - \\sin^{2} A = \\cos^{2} A$, giving $\\cos A$.",
                         "$\\text{cosec } A$": "Write everything in $\\sin$ and $\\cos$: the answer is $\\cos A$.", "$\\cos A$": "Correct! $\\dfrac{1 - \\sin^{2} A}{\\cos A} = \\cos A$."},
 "ch08.q.ex8_3.q3.iv": {"$\\sec^{2} A$": "That is only the numerator, $1 + \\tan^{2} A$.", "$-1$": "Both numerator and denominator are positive.",
                        "$\\cot^{2} A$": "It is upside down: $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$.", "$\\tan^{2} A$": "Correct! $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$."},
 "ch08.q.mcq01": {"$1$": "Correct!", "$\\dfrac{1}{2}$": "Add both terms: $\\dfrac{1}{2} + \\dfrac{1}{2}$.", "$\\sqrt{3}$": "Both values are $\\dfrac{1}{2}$.", "$0$": "Add, don't subtract."},
 "ch08.q.mcq02": {"$\\dfrac{4}{5}$": "Correct!", "$\\dfrac{3}{4}$": "That is $\\tan A$.", "$\\dfrac{5}{3}$": "That is $\\text{cosec } A$.", "$\\dfrac{2}{5}$": "$\\cos A \\neq 1 - \\sin A$; use the 3-4-5 triangle."},
 "ch08.q.mcq03": {"$1$": "Correct!", "$0$": "$\\tan 0^\\circ = 0$, not $\\tan 45^\\circ$.", "$\\sqrt{3}$": "That is $\\tan 60^\\circ$.", "$\\dfrac{1}{\\sqrt{2}}$": "That is $\\sin 45^\\circ$ or $\\cos 45^\\circ$."},
 "ch08.q.mcq04": {"$1$": "Correct! The identity holds for every angle.", "$\\dfrac{1}{2}$": "$\\dfrac{3}{4} + \\dfrac{1}{4} = 1$.", "$\\dfrac{\\sqrt{3}}{2}$": "Square the values first: $\\dfrac{3}{4} + \\dfrac{1}{4}$.", "$2$": "$\\sin^{2} A + \\cos^{2} A = 1$."},
 "ch08.q.mcq05": {"$\\dfrac{12}{13}$": "Correct! Sides 5, 12, 13.", "$\\dfrac{5}{13}$": "That is $\\cos A$.", "$\\dfrac{12}{5}$": "That is $\\tan A$ itself.", "$\\dfrac{13}{12}$": "That is $\\text{cosec } A$."},
 "ch08.q.mcq06": {"$\\sec A$": "Correct!", "$\\text{cosec } A$": "That is the reciprocal of $\\sin A$.", "$\\cot A$": "That is the reciprocal of $\\tan A$.", "$\\tan A$": "$\\tan A = \\dfrac{\\sin A}{\\cos A}$."},
 "ch08.q.mcq07": {"$0$": "Correct!", "$1$": "That is $\\cos 0^\\circ$ or $\\sin 90^\\circ$.", "$\\dfrac{1}{2}$": "That is $\\cos 60^\\circ$.", "not defined": "$\\tan 90^\\circ$ is not defined, but $\\cos 90^\\circ = 0$."},
 "ch08.q.mcq08": {"$\\dfrac{\\sqrt{3} - 1}{2}$": "Correct!", "$\\sin 30^\\circ$": "$\\sin 60^\\circ - \\sin 30^\\circ \\neq \\sin(60^\\circ - 30^\\circ)$.",
                  "$\\dfrac{1}{2}$": "That treats it like $\\sin 30^\\circ$; subtract the values instead.", "$\\dfrac{\\sqrt{3} + 1}{2}$": "That is the sum, not the difference."},
 "ch08.q.mcq09": {"$1$": "Correct!", "$0$": "$\\sin^{2} A \\times \\text{cosec}^{2} A = 1$.", "$\\sin^{2} A$": "Multiply by $\\text{cosec}^{2} A$ too.", "$\\cos^{2} A$": "$1 - \\cos^{2} A = \\sin^{2} A$."},
 "ch08.q.mcq10": {"$30^\\circ$": "Correct!", "$60^\\circ$": "$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$.", "$45^\\circ$": "$\\sin 45^\\circ = \\dfrac{1}{\\sqrt{2}}$.", "$90^\\circ$": "$\\sin 90^\\circ = 1$."},
 "ch08.q.mcq11": {"$\\sin A = \\dfrac{5}{4}$": "Correct! $\\sin A$ can never be more than 1.", "$\\tan A = 5$": "$\\tan A$ can be any positive number.",
                  "$\\sec A = 2$": "$\\sec 60^\\circ = 2$.", "$\\cos A = 0.6$": "Possible: the 3-4-5 triangle gives $\\cos A = 0.6$."},
 "ch08.q.mcq12": {"$30^\\circ$": "Correct!", "$60^\\circ$": "$\\tan 60^\\circ = \\sqrt{3}$.", "$45^\\circ$": "$\\tan 45^\\circ = 1$.", "$0^\\circ$": "$\\tan 0^\\circ = 0$."},
}

AR = {
 "ch08.q.ar1": ("$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$.", "the hypotenuse being longest is exactly why $\\sin A < 1$."),
 "ch08.q.ar2": ("it is the identity with $A = 35^\\circ$.", "this identity gives A directly."),
 "ch08.q.ar3": ("$\\sin 90^\\circ = 1$ but $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$.", "$\\sin 90^\\circ = 1$ is a correct value."),
 "ch08.q.ar4": ("$2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$.", "$\\tan 45^\\circ = 1$, not 0."),
 "ch08.q.ar5": ("$\\sin 0^\\circ = 0$ makes $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ undefined.", "it is true, but it has nothing to do with $\\cot 0^\\circ$."),
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
    if item.get("type") == "true_false":
        right = item["options"][item["correct_index"]]
        item["option_feedback"] = [("Correct! " if o == right else "Not quite. ") + item["explanation"] for o in item["options"]]; return
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
    if q["type"] in ("mcq", "assertion_reason", "true_false"): apply(q); n += 1
for s in chapter["sections"]:
    for blk in s["blocks"]:
        if blk["type"] == "knowledge_check": apply(blk); n += 1
for p, d in ((qp, bank), (cp, chapter)):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, indent=2); f.write("\n")
print("items with feedback:", n)
