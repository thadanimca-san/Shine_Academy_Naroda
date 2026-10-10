"""Per-option explanations for Ch 9 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch09_some_applications_of_trigonometry"

F = {
 "ch09.s2.check": {"angle of depression": "Correct! The boat is below eye level.", "angle of elevation": "Elevation is for objects above eye level.",
                   "right angle": "The angle is with the horizontal, and it is less than $90^\\circ$.", "angle of the cliff": "The angle is between the line of sight and the horizontal."},
 "ch09.s3.check1": {"$10\\sqrt{3}$ m": "Correct! $30 \\times \\dfrac{1}{\\sqrt{3}} = 10\\sqrt{3}$.", "$30\\sqrt{3}$ m": "That uses $\\tan 60^\\circ$. Here the angle is $30^\\circ$.",
                    "$15$ m": "That uses $\\sin 30^\\circ$; with height and distance use $\\tan$.", "$10$ m": "$\\dfrac{30}{\\sqrt{3}} = 10\\sqrt{3}$, not 10."},
 "ch09.s3.check2": {"$50$ m": "Correct! $100\\sin 30^\\circ = 50$.", "$50\\sqrt{3}$ m": "That uses $\\cos 30^\\circ$, which gives the ground distance.",
                    "$100\\sqrt{3}$ m": "The height cannot be more than the string.", "$200$ m": "The height cannot be more than the 100 m string."},
 "ch09.q.mcq01": {"$10\\sqrt{3}$ m": "Correct!", "$30\\sqrt{3}$ m": "That uses $\\tan 60^\\circ$.", "$15$ m": "Use $\\tan$, not $\\sin$, with height and distance.", "$10$ m": "$\\dfrac{30}{\\sqrt{3}} = 10\\sqrt{3}$."},
 "ch09.q.mcq02": {"$5\\sqrt{3}$ m": "Correct! $10 \\times \\dfrac{\\sqrt{3}}{2}$.", "$5$ m": "That uses $\\sin 30^\\circ$; the angle is $60^\\circ$.", "$10\\sqrt{3}$ m": "The height cannot exceed the 10 m ladder.", "$20$ m": "The height cannot exceed the 10 m ladder."},
 "ch09.q.mcq03": {"$60^\\circ$": "Correct! $\\tan \\theta = \\sqrt{3}$.", "$30^\\circ$": "$\\tan 30^\\circ = \\dfrac{1}{\\sqrt{3}}$, but here $\\tan \\theta = \\sqrt{3}$.", "$45^\\circ$": "That needs the shadow to equal the height.", "$90^\\circ$": "Then there would be no shadow."},
 "ch09.q.mcq04": {"increases": "Correct!", "decreases": "It decreases when you walk away.", "stays the same": "The distance changes, so the angle changes.", "becomes zero": "It becomes larger, not zero."},
 "ch09.q.mcq05": {"$50$ m": "Correct! $\\tan 45^\\circ = 1$.", "$50\\sqrt{3}$ m": "That is for $30^\\circ$.", "$25$ m": "At $45^\\circ$ the distance equals the height.", "$100$ m": "At $45^\\circ$ the distance equals the height."},
 "ch09.q.mcq06": {"$50$ m": "Correct!", "$50\\sqrt{3}$ m": "That is the ground distance ($\\cos 30^\\circ$).", "$100\\sqrt{3}$ m": "The height cannot be more than the string.", "$200$ m": "The height cannot be more than the string."},
 "ch09.q.mcq07": {"$45^\\circ$": "Correct! $\\tan \\theta = 1$.", "$30^\\circ$": "Then the shadow would be longer than the pole.", "$60^\\circ$": "Then the shadow would be shorter than the pole.", "$90^\\circ$": "Then there would be no shadow."},
 "ch09.q.mcq08": {"$7$ m": "Correct! At $45^\\circ$ the distance equals the height.", "$7\\sqrt{3}$ m": "That is for $30^\\circ$.", "$\\dfrac{7}{\\sqrt{3}}$ m": "That is for $60^\\circ$.", "$14$ m": "At $45^\\circ$, distance $=$ height $= 7$ m."},
 "ch09.q.mcq09": {"$60^\\circ$": "Correct!", "$30^\\circ$": "$\\tan 30^\\circ = \\dfrac{1}{\\sqrt{3}}$; the ratio is upside down.", "$45^\\circ$": "That needs the ratio $1 : 1$.", "$90^\\circ$": "Then there would be no shadow."},
 "ch09.q.mcq10": {"alternate angles": "Correct! The horizontal lines are parallel.", "vertically opposite angles": "They are not formed by two crossing lines at one point.",
                  "complementary angles": "Their sum is not $90^\\circ$; they are equal.", "supplementary angles": "Their sum is not $180^\\circ$; they are equal."},
 "ch09.q.mcq11": {"$3$ m": "Correct! $\\dfrac{1.5}{\\sin 30^\\circ} = 3$.", "$1.5\\sqrt{3}$ m": "That is the ground distance.", "$0.75$ m": "The slide must be longer than its height.", "$\\sqrt{3}$ m": "Use $\\sin 30^\\circ = \\dfrac{1.5}{L}$."},
 "ch09.q.mcq12": {"$60^\\circ$": "Correct! $\\tan \\theta = \\sqrt{3}$.", "$30^\\circ$": "$\\tan 30^\\circ = \\dfrac{1}{\\sqrt{3}}$.", "$45^\\circ$": "That needs height $=$ distance.", "$90^\\circ$": "The angle of elevation is less than $90^\\circ$ here."},
}
AR = {
 "ch09.q.ar1": ("$\\tan \\theta = \\dfrac{\\text{height}}{\\text{shadow}} = 1$.", "$\\tan 45^\\circ = 1$ is exactly what gives the angle."),
 "ch09.q.ar2": ("the distance decreases while the height stays the same.", "the height of the tower does not change."),
 "ch09.q.ar3": ("$\\sin \\theta = \\dfrac{5}{10} = \\dfrac{1}{2}$ gives $30^\\circ$, not $60^\\circ$.", "$\\sin 30^\\circ = \\dfrac{1}{2}$ is a correct value."),
 "ch09.q.ar4": ("they are alternate angles between parallel lines.", "alternate angles between parallel lines are equal, which is exactly why A holds."),
 "ch09.q.ar5": ("$\\tan \\theta = \\dfrac{20}{20} = 1$.", "it is true, but it is about depression, not about A."),
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
