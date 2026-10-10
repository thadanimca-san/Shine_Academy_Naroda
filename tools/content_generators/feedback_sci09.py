"""Per-option explanations for Science Ch 9 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch09_light_reflection_and_refraction"

L1 = "$\\dfrac{1}{v} - \\dfrac{1}{u} = \\dfrac{1}{f}$"; L2 = "$\\dfrac{1}{v} + \\dfrac{1}{u} = \\dfrac{1}{f}$"; L3 = "$\\dfrac{1}{u} - \\dfrac{1}{v} = \\dfrac{1}{f}$"
F = {
 "sci10ch09.s2.check": {"10 cm": "Correct!", "20 cm": "That is R, not f.", "40 cm": "f is half of R, not double.", "5 cm": "f = R/2 = 10 cm."},
 "sci10ch09.s3.check": {"between P and F": "Correct!", "at C": "That gives a real image of the same size.", "beyond C": "That gives a real, diminished image.", "at F": "That gives an image at infinity."},
 "sci10ch09.s4.check": {"real, inverted and enlarged": "Correct!", "virtual, erect and enlarged": "A negative m means real and inverted.", "real, erect and diminished": "|m| = 2 means enlarged, and real images are inverted.", "virtual, inverted and diminished": "A negative m means real; |m| = 2 means enlarged."},
 "sci10ch09.s5.check": {"Water (1.33)": "Correct!", "Kerosene (1.44)": "Its refractive index is higher than water's.", "Turpentine oil (1.47)": "Its refractive index is higher than water's.", "Crown glass (1.52)": "It has the highest refractive index here."},
 "sci10ch09.s6.check": {"concave lens of focal length 50 cm": "Correct!", "convex lens of focal length 50 cm": "Negative power means a concave lens.", "concave lens of focal length 2 m": "f = 1/P = 1/2 m = 0.5 m.", "convex lens of focal length 2 m": "Negative power means concave, and f = 0.5 m."},
 "sci10ch09.q.ex.q1": {"Water": "Water is transparent; a water drop acts as a lens.", "Glass": "Glass is the usual lens material.", "Plastic": "Transparent plastic is used for lenses.", "Clay": "Correct!"},
 "sci10ch09.q.ex.q2": {"Between the principal focus and the centre of curvature": "That gives a real, enlarged, inverted image.", "At the centre of curvature": "That gives a real image of the same size.",
                       "Beyond the centre of curvature": "That gives a real, diminished image.", "Between the pole of the mirror and its principal focus.": "Correct!"},
 "sci10ch09.q.ex.q3": {"At the principal focus of the lens": "The image would be at infinity.", "At twice the focal length": "Correct!", "At infinity": "The image would be a point at F₂.", "Between the optical centre of the lens and its principal focus.": "That gives a virtual image."},
 "sci10ch09.q.ex.q4": {"both concave.": "Correct!", "both convex.": "A convex mirror and a convex lens both have positive focal length.", "the mirror is concave and the lens is convex.": "A convex lens has positive f.", "the mirror is convex, but the lens is concave.": "A convex mirror has positive f."},
 "sci10ch09.q.ex.q5": {"only plane.": "A convex mirror also always gives an erect image.", "only concave.": "Far from a concave mirror, the image is inverted.", "only convex.": "A plane mirror also always gives an erect image.", "either plane or convex.": "Correct!"},
 "sci10ch09.q.ex.q6": {"A convex lens of focal length 50 cm.": "A longer focal length magnifies less.", "A concave lens of focal length 50 cm.": "A concave lens makes letters smaller.", "A convex lens of focal length 5 cm.": "Correct!", "A concave lens of focal length 5 cm.": "A concave lens makes letters smaller."},
 "sci10ch09.q.sqp30": {"I and II": "Statement II is wrong: convex mirrors give virtual images.", "I, II and III": "Statement II is wrong.", "II and III": "Statement II is wrong.", "I and III": "Correct!"},
 "sci10ch09.q.gseb2025_6": {"only plane": "A convex mirror also always gives an erect image.", "only concave": "Far from a concave mirror, the image is inverted.", "only convex": "A plane mirror also always gives an erect image.", "either plane or convex": "Correct!"},
 "sci10ch09.q.gseb2025_11": {L1: "Correct!", L2: "That is the mirror formula.", L3: "The signs are reversed."},
 "sci10ch09.q.mcq01": {"24 cm": "Correct!", "6 cm": "R is double f, not half.", "12 cm": "That is f.", "36 cm": "R = 2f = 24 cm."},
 "sci10ch09.q.mcq02": {"virtual, erect and diminished": "Correct!", "real, inverted and diminished": "A convex mirror never forms a real image.", "virtual, erect and enlarged": "The image is always smaller.", "real, erect and same size": "A convex mirror never forms a real image."},
 "sci10ch09.q.mcq03": {"Concave": "Correct!", "Convex": "A convex mirror makes the image smaller.", "Plane": "A plane mirror does not enlarge.", "None of these": "A concave mirror is used."},
 "sci10ch09.q.mcq04": {"speeds up and bends away from the normal": "Correct!", "slows down and bends towards the normal": "That happens from air into glass.", "goes straight without bending": "Only a ray along the normal goes straight.", "stops at the boundary": "Light passes into the air."},
 "sci10ch09.q.mcq05": {"it has no unit": "Correct!", "m/s": "That is the unit of speed.", "dioptre": "That is the unit of power.", "metre": "Refractive index is a ratio."},
 "sci10ch09.q.mcq06": {"between F₁ and O": "Correct!", "at 2F₁": "That gives a real image of the same size.", "beyond 2F₁": "That gives a real, diminished image.", "at F₁": "That gives an image at infinity."},
 "sci10ch09.q.mcq07": {"+4 D": "Correct!", "−4 D": "A convex lens has positive power.", "+0.25 D": "Convert 25 cm to 0.25 m, then take 1/f.", "+25 D": "Use f in metres: 0.25 m."},
 "sci10ch09.q.mcq08": {"+2 D": "Correct!", "+4 D": "Add with signs: 3 + (−1).", "−2 D": "3 + (−1) is positive.", "−3 D": "Add the powers: 3 − 1."},
 "sci10ch09.q.mcq09": {"negative": "Correct!", "positive": "The object is to the left of the pole.", "zero": "The object is not at the pole.", "equal to f": "u can be any distance."},
 "sci10ch09.q.mcq10": {"$2 \\times 10^{8}$ m/s": "Correct!", "$3 \\times 10^{8}$ m/s": "That is the speed in vacuum.", "$4.5 \\times 10^{8}$ m/s": "Divide by n, do not multiply.", "$1.5 \\times 10^{8}$ m/s": "3 ÷ 1.5 = 2."},
}
AR = {
 "sci10ch09.q.sqp32": ("a convex mirror forms a virtual image at v = +13 cm.", "the formula gives v = +13 cm, not infinity."),
 "sci10ch09.q.ar1": ("convex mirrors are used as rear-view mirrors.", "an erect image of a wide area is what a driver needs."),
 "sci10ch09.q.ar2": ("the dipped part looks displaced.", "refraction at the surface causes it."),
 "sci10ch09.q.ar3": ("a concave lens has negative power.", "a concave lens does diverge light."),
 "sci10ch09.q.ar4": ("kerosene (1.44) has a higher refractive index than water (1.33).", "kerosene is lighter than water."),
 "sci10ch09.q.ar5": ("the image is complete, only dimmer.", "the uncovered half still collects light from every point."),
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
