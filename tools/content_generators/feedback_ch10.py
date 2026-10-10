"""Per-option explanations for Ch 10 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch10_circles"

F = {
 "ch10.s2.check": {"$\\sqrt{119}$ cm": "Correct! $144 - 25 = 119$.", "$12$ cm": "12 cm is $OQ$, the hypotenuse.", "$13$ cm": "That adds the squares; $OQ$ is the hypotenuse, so subtract.", "$8.5$ cm": "Use Pythagoras: $PQ^{2} = 12^{2} - 5^{2}$."},
 "ch10.s3.check1": {"$50^\\circ$": "Correct! Half of $100^\\circ$.", "$40^\\circ$": "That is $\\angle APO$, half of $80^\\circ$.", "$80^\\circ$": "$\\angle AOB = 100^\\circ$; $\\angle POA$ is half of it.", "$100^\\circ$": "That is the whole $\\angle AOB$; $OP$ bisects it."},
 "ch10.s3.check2": {"None": "Correct!", "One": "One tangent is possible only from a point on the circle.", "Two": "Two tangents come from a point outside.", "Infinitely many": "The circle has infinitely many tangents, but none passes through an inside point."},
 "ch10.q.ex10_1.q1": {"infinitely many": "Correct! One at every point.", "one": "There is one at each point, and a circle has infinitely many points.", "two": "Two is the most from one outside point.", "none": "Every point of a circle has a tangent."},
 "ch10.q.ex10_1.q2.i": {"one": "Correct!", "two": "A line meeting the circle twice is a secant.", "no": "A line with no common point does not touch the circle.", "infinitely many": "A line and a circle meet in at most two points."},
 "ch10.q.ex10_1.q2.ii": {"secant": "Correct!", "tangent": "A tangent meets the circle once.", "chord": "A chord is only the segment between the two points.", "radius": "A radius joins the centre to the circle."},
 "ch10.q.ex10_1.q2.iii": {"two": "Correct! At the ends of one diameter.", "one": "There is another one at the other end of the diameter.", "three": "Only two tangents can be parallel to each other.", "infinitely many": "Only two tangents can be parallel to each other."},
 "ch10.q.ex10_1.q2.iv": {"point of contact": "Correct!", "centre": "The centre is inside the circle, not on the tangent.", "end point": "A tangent line has no end point there.", "point of intersection of chords": "Chords are not involved."},
 "ch10.q.ex10_1.q3": {"$12$ cm": "12 cm is $OQ$.", "$13$ cm": "Subtract the squares; $OQ$ is the hypotenuse.", "$8.5$ cm": "Use Pythagoras.", "$\\sqrt{119}$ cm": "Correct! $144 - 25 = 119$."},
 "ch10.q.ex10_2.q1": {"$7$ cm": "Correct! $625 - 576 = 49$.", "$12$ cm": "Use $r^{2} = 25^{2} - 24^{2}$.", "$15$ cm": "Use $r^{2} = 25^{2} - 24^{2}$.", "$24.5$ cm": "Squares, not the average: $r = 7$ cm."},
 "ch10.q.ex10_2.q2": {"$60^\\circ$": "$\\angle PTQ = 180^\\circ - 110^\\circ$.", "$70^\\circ$": "Correct!", "$80^\\circ$": "$\\angle PTQ = 180^\\circ - 110^\\circ$.", "$90^\\circ$": "The two right angles are at $P$ and $Q$, not at $T$."},
 "ch10.q.ex10_2.q3": {"$50^\\circ$": "Correct!", "$60^\\circ$": "$\\angle AOB = 100^\\circ$, so $\\angle POA = 50^\\circ$.", "$70^\\circ$": "$\\angle AOB = 100^\\circ$, so $\\angle POA = 50^\\circ$.", "$80^\\circ$": "That is the angle between the tangents."},
 "ch10.q.sqp4": {"$3$ cm": "That is $AD$.", "$4$ cm": "That is $CD$.", "$6$ cm": "Correct! $AB + 4 = 3 + 7$.", "$7$ cm": "That is $BC$."},
 "ch10.q.sqp18": {"$40$ cm": "Correct!", "$9$ cm": "That is the radius.", "$41$ cm": "That is the distance to the centre, the hypotenuse.", "$50$ cm": "That adds 41 and 9; use Pythagoras."},
 "ch10.q.mcq01": {"$0$": "Correct!", "$1$": "One tangent needs a point on the circle.", "$2$": "Two tangents need a point outside.", "infinitely many": "None pass through an inside point."},
 "ch10.q.mcq02": {"$1$": "Correct!", "$0$": "Every point of the circle has a tangent.", "$2$": "Two come from an outside point.", "infinitely many": "Only one tangent at each point."},
 "ch10.q.mcq03": {"$90^\\circ$": "Correct!", "$60^\\circ$": "The tangent is perpendicular to the radius.", "$45^\\circ$": "The tangent is perpendicular to the radius.", "$180^\\circ$": "They meet at a right angle, not along a straight line."},
 "ch10.q.mcq04": {"$12$ cm": "Correct!", "$8$ cm": "That is $13 - 5$; use Pythagoras.", "$18$ cm": "That is $13 + 5$.", "$\\sqrt{194}$ cm": "Subtract the squares: $169 - 25$."},
 "ch10.q.mcq05": {"$120^\\circ$": "Correct!", "$60^\\circ$": "They add up to $180^\\circ$, they are not equal.", "$30^\\circ$": "$180^\\circ - 60^\\circ = 120^\\circ$.", "$90^\\circ$": "$180^\\circ - 60^\\circ = 120^\\circ$."},
 "ch10.q.mcq06": {"$10$ cm": "Correct!", "$5$ cm": "The tangents are equal, not halved.", "$20$ cm": "The tangents are equal.", "cannot be found": "Theorem 10.2 gives it: 10 cm."},
 "ch10.q.mcq07": {"$16$ cm": "Correct!", "$8$ cm": "That is half the chord.", "$12$ cm": "Half the chord is $\\sqrt{100 - 36} = 8$.", "$4$ cm": "That is $10 - 6$."},
 "ch10.q.mcq08": {"parallel": "Correct!", "perpendicular": "Both are perpendicular to the diameter, so they are parallel to each other.", "intersecting at the centre": "Tangents never pass through the centre.", "equal to the diameter": "Tangent lines have no fixed length."},
 "ch10.q.mcq09": {"$3$ cm": "Correct!", "$5$ cm": "$AD = AB + CD - BC = 3$ cm.", "$9$ cm": "Use $AB + CD = AD + BC$.", "$17$ cm": "That adds all three sides."},
 "ch10.q.mcq10": {"$2$": "Correct!", "$1$": "There is one at each end of a diameter.", "$3$": "Only two.", "infinitely many": "Only two tangents can be parallel to one line."},
}
AR = {
 "ch10.q.ar1": ("$\\sqrt{5^{2} - 3^{2}} = 4$ cm.", "the right angle is exactly what lets us use Pythagoras."),
 "ch10.q.ar2": ("every line through an inside point cuts the circle twice.", "this is exactly why no line through it can be a tangent."),
 "ch10.q.ar3": ("congruent right triangles give equal tangents.", "it is true, but it does not explain why two tangents are equal."),
 "ch10.q.ar4": ("the angle is $180^\\circ - 70^\\circ = 110^\\circ$.", "the angles in the quadrilateral with two right angles add up this way."),
 "ch10.q.ar5": ("only one perpendicular can be drawn at a point, and the radius is one.", "a circle has infinitely many tangents."),
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
