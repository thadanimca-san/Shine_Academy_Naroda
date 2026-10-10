"""Per-option explanations for Ch 11 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch11_areas_related_to_circles"

F = {
 "ch11.s2.check": {"$154$ cm²": "Correct! A quadrant is $\\dfrac{1}{4}$ of $616$ cm².", "$616$ cm²": "That is the whole circle; a quadrant is a quarter of it.", "$22$ cm²": "That is the length of the quadrant's arc in cm, not an area.", "$308$ cm²": "That is a semicircle; a quadrant is half of that."},
 "ch11.s3.check1": {"$28.5$ cm²": "Correct! $78.5 - 50$.", "$78.5$ cm²": "That is the sector; subtract the triangle.", "$50$ cm²": "That is the triangle; the segment is sector minus triangle.", "$235.5$ cm²": "That is the major sector."},
 "ch11.s3.check2": {"the area of the circle": "Correct!", "the area of the major sector": "The major segment alone is bigger than the major sector.", "the area of the triangle": "The triangle is only part of the minor sector.", "the area of the minor sector": "The two segments cover the whole circle."},
 "ch11.q.ex11_1.q14": {"$\\dfrac{p}{180} \\times 2\\pi R$": "This is twice the arc length, not an area.", "$\\dfrac{p}{180} \\times \\pi R^{2}$": "This is twice the area: the fraction is $\\dfrac{p}{360}$.", "$\\dfrac{p}{360} \\times 2\\pi R$": "This is the arc length, not the area.", "$\\dfrac{p}{720} \\times 2\\pi R^{2}$": "Correct! It equals $\\dfrac{p}{360} \\times \\pi R^{2}$."},
 "ch11.q.sqp7": {"$4\\left[\\dfrac{\\pi}{12} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²": "The angle is $60^\\circ$, so the sector is $\\dfrac{\\pi}{6}$, and there are 8 segments.", "$\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²": "That is only one segment; there are 8.",
                "$4\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²": "Each common region has 2 segments, and there are 4 regions: 8 segments.", "$8\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²": "Correct!"},
 "ch11.q.sqp13": {"$441$": "That is $r^{2}$; use $\\dfrac{1}{2} l r$.", "$321$": "Use $\\dfrac{1}{2} \\times 22 \\times 21$.", "$231$": "Correct!", "$221$": "Use $\\dfrac{1}{2} \\times 22 \\times 21$."},
 "ch11.q.mcq01": {"$\\dfrac{\\theta}{360} \\times 2\\pi r$": "Correct!", "$\\dfrac{\\theta}{360} \\times \\pi r^{2}$": "That is the area of the sector.", "$\\dfrac{\\theta}{180} \\times \\pi r^{2}$": "That is twice the area of the sector.", "$\\dfrac{\\theta}{720} \\times \\pi r$": "That is a quarter of the arc length."},
 "ch11.q.mcq02": {"$154$ cm²": "Correct!", "$616$ cm²": "That is the whole circle.", "$44$ cm²": "That is half the circumference, a length.", "$308$ cm²": "That is a semicircle."},
 "ch11.q.mcq03": {"$90^\\circ$": "Correct!", "$15^\\circ$": "Each minute is $6^\\circ$, not $1^\\circ$.", "$60^\\circ$": "That is 10 minutes.", "$180^\\circ$": "That is 30 minutes."},
 "ch11.q.mcq04": {"$22$ cm": "Correct!", "$44$ cm": "That is the arc for $120^\\circ$.", "$231$ cm": "That is the sector's area in cm², not the arc.", "$11$ cm": "Use $2\\pi r$, not $\\pi r$."},
 "ch11.q.mcq05": {"$38.5$ cm²": "Correct!", "$154$ cm²": "That is the whole circle.", "$11$ cm²": "11 cm is the arc length, not the area.", "$77$ cm²": "That is a semicircle."},
 "ch11.q.mcq06": {"$60^\\circ$": "Correct!", "$30^\\circ$": "That is $\\dfrac{1}{12}$ of the circle.", "$6^\\circ$": "Multiply $\\dfrac{1}{6}$ by $360^\\circ$.", "$120^\\circ$": "That is $\\dfrac{1}{3}$ of the circle."},
 "ch11.q.mcq07": {"$28.5$ cm²": "Correct!", "$78.5$ cm²": "That is the sector; subtract the triangle.", "$50$ cm²": "That is the triangle.", "$235.5$ cm²": "That is the major sector."},
 "ch11.q.mcq08": {"$25$ cm": "Correct!", "$11$ cm": "That is only the arc; add the two radii.", "$18$ cm": "Add both radii: $11 + 7 + 7$.", "$38.5$ cm": "That is the area in cm², not the perimeter."},
 "ch11.q.mcq09": {"the area of the circle": "Correct!", "the area of the major sector": "The major segment alone is bigger than the major sector.", "the area of the triangle": "The triangle is only part of the minor sector.", "the area of the minor sector": "The two segments cover the whole circle."},
 "ch11.q.mcq10": {"$\\dfrac{1}{2} l r$": "Correct!", "$l r$": "That is twice the area.", "$2 l r$": "That is four times the area.", "$\\pi l r$": "There is no $\\pi$: it is already inside $l$."},
}
AR = {
 "ch11.q.ar1": ("$\\dfrac{90}{360} \\times \\dfrac{22}{7} \\times 196 = 154$ cm².", "this formula is exactly what gives the area in A."),
 "ch11.q.ar2": ("the area grows in the same ratio as the angle.", "this proportion is exactly why doubling the angle doubles the area."),
 "ch11.q.ar3": ("$\\dfrac{60}{360} \\times 2 \\times \\dfrac{22}{7} \\times 21 = 22$ cm.", "it is true, but the arc length comes from the circumference $2\\pi r$, not from the area."),
 "ch11.q.ar4": ("the segment is $78.5 - 50 = 28.5$ cm².", "a segment is the sector with the triangle taken away."),
 "ch11.q.ar5": ("one round of $360^\\circ$ takes 60 minutes.", "one round takes 60 minutes, not 30."),
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
