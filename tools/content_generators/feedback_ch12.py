"""Per-option explanations for Ch 12 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/maths/ncert_rationalised/ch12_surface_areas_and_volumes"

F = {
 "ch12.s2.check": {"$250$ cm²": "Correct! The cuboid is $10 \\times 5 \\times 5$.", "$300$ cm²": "That counts both cubes fully; the two joined faces are hidden.", "$150$ cm²": "That is only one cube.", "$125$ cm²": "That is the volume of one cube in cm³."},
 "ch12.s3.check1": {"$\\dfrac{2}{3}\\pi r^{3}$": "Correct!", "$\\dfrac{4}{3}\\pi r^{3}$": "That is the whole sphere.", "$2\\pi r^{2}$": "That is the curved surface area, not the volume.", "$\\dfrac{1}{3}\\pi r^{3}$": "That is a quarter of the sphere."},
 "ch12.s3.check2": {"$\\dfrac{2}{3}$": "Correct!", "$\\dfrac{1}{3}$": "That is the cone that was removed.", "$\\dfrac{1}{2}$": "The cone is one-third of the cylinder, not half.", "$\\dfrac{3}{4}$": "The cone is one-third of the cylinder, not a quarter."},
 "ch12.q.sqp11": {"$\\dfrac{5}{6}$ cm": "Use $85 = \\dfrac{1}{3} \\times 51 \\times h$.", "$\\dfrac{5}{3}$ cm": "That is $85 \\div 51$; multiply by 3.", "$\\dfrac{5}{2}$ cm": "Use $85 = \\dfrac{1}{3} \\times 51 \\times h$.", "$5$ cm": "Correct!"},
 "ch12.q.mcq01": {"$250$ cm²": "Correct!", "$300$ cm²": "The two joined faces are hidden: subtract them.", "$150$ cm²": "That is one cube.", "$125$ cm²": "That is the volume of one cube in cm³."},
 "ch12.q.mcq02": {"$\\pi r l + 2\\pi r^{2}$": "Correct!", "$\\pi r l + 3\\pi r^{2}$": "That adds the hidden circle.", "$\\pi r(l + r) + 2\\pi r^{2}$": "That adds the cone's hidden base.", "$\\pi r l + \\pi r^{2}$": "The hemisphere's curved surface is $2\\pi r^{2}$."},
 "ch12.q.mcq03": {"$\\dfrac{2}{3}\\pi r^{3}$": "Correct!", "$\\dfrac{4}{3}\\pi r^{3}$": "That is the whole sphere.", "$2\\pi r^{3}$": "Halve $\\dfrac{4}{3}\\pi r^{3}$.", "$\\dfrac{1}{3}\\pi r^{3}$": "That is a quarter of the sphere."},
 "ch12.q.mcq04": {"$3 : 1$": "Correct!", "$1 : 3$": "That is cone : cylinder.", "$2 : 1$": "The cone is one-third of the cylinder.", "$1 : 1$": "The cone holds less."},
 "ch12.q.mcq05": {"$308$ cm²": "Correct!", "$462$ cm²": "That is the total surface $3\\pi r^{2}$.", "$154$ cm²": "That is the base circle $\\pi r^{2}$.", "$616$ cm²": "That is the whole sphere."},
 "ch12.q.mcq06": {"$10$ cm": "Correct!", "$14$ cm": "That is $6 + 8$; use Pythagoras.", "$2$ cm": "That is $8 - 6$.", "$\\sqrt{28}$ cm": "Add the squares: $36 + 64$."},
 "ch12.q.mcq07": {"$154$ cm²": "Correct!", "$38.5$ cm²": "That is one circle $\\pi r^{2}$; a sphere is four of them.", "$179.67$ cm²": "That is the volume in cm³.", "$77$ cm²": "That is a hemisphere's curved surface."},
 "ch12.q.mcq08": {"$7$ cm": "Correct!", "$3.5$ cm": "That is the radius.", "$14$ cm": "It would not fit on the face.", "$49$ cm": "That is the area of a face in cm²."},
 "ch12.q.mcq09": {"increases by $\\pi r^{2}$": "Correct!", "decreases by $\\pi r^{2}$": "The inner curved surface $2\\pi r^{2}$ is more than the circle removed.", "increases by $2\\pi r^{2}$": "Subtract the circle $\\pi r^{2}$ that is removed.", "does not change": "It loses $\\pi r^{2}$ and gains $2\\pi r^{2}$."},
 "ch12.q.mcq10": {"$\\dfrac{3080}{3}$ cm³": "Correct!", "$1540$ cm³": "That is the full cylinder.", "$\\dfrac{1540}{3}$ cm³": "That is the cone that was removed.", "$\\dfrac{4620}{3}$ cm³": "That is the full cylinder; subtract the cone."},
}
AR = {
 "ch12.q.ar1": ("only the two curved surfaces are on the outside.", "hiding the bases is exactly why they are not counted."),
 "ch12.q.ar2": ("the cylinder plus two hemispheres gives this sum.", "two hemispheres make $\\dfrac{4}{3}\\pi r^{3}$, which explains the second term."),
 "ch12.q.ar3": ("two faces are hidden, so it is $192 - 32 = 160$ cm².", "$6a^{2}$ is the surface of one cube."),
 "ch12.q.ar4": ("$\\sqrt{5^{2} + 12^{2}} = 13$ cm.", "it is true, but the slant height comes from Pythagoras, not from the volume."),
 "ch12.q.ar5": ("half of the sphere's $4\\pi r^{2}$ is $2\\pi r^{2}$.", "the flat circle adds $\\pi r^{2}$, so the total is $3\\pi r^{2}$."),
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
