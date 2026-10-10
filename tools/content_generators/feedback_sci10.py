"""Per-option explanations for Science Ch 10 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch10_human_eye_and_colourful_world"

S31 = ["As sunlight passes through the atmosphere, shorter wavelengths, such as blue are scattered more than other colors.", "The sky appears blue because all colors are scattered equally, but blue light is stronger and more visible to the human eye.",
       "The blue color of the sky is due to longer wavelengths like red and orange scattering more than shorter wavelengths, making blue stand out more.", "The atmosphere contains blue-colored particles that give the sky its blue appearance."]
F = {
 "sci10ch10.s2.check": {"ciliary muscles": "Correct!", "pupil": "The pupil only lets light in.", "retina": "The retina is the screen.", "iris": "The iris controls the pupil size."},
 "sci10ch10.s3.check": {"myopia, concave lens": "Correct!", "hypermetropia, convex lens": "Hypermetropia makes near objects blurred.", "presbyopia, bifocal lens": "Presbyopia comes with age and affects near vision.", "cataract, convex lens": "Cataract is a cloudy lens, treated by surgery."},
 "sci10ch10.s4.check": {"Red": "Correct!", "Violet": "Violet bends the most.", "Green": "Green is in the middle.", "Blue": "Blue bends more than red."},
 "sci10ch10.s5.check": {"atmospheric refraction": "Correct!", "dispersion in a prism": "There is no prism in the sky.", "reflection from clouds": "Stars twinkle on clear nights too.", "scattering by dust only": "Scattering gives colour, not twinkling."},
 "sci10ch10.s6.check": {"There is no atmosphere to scatter sunlight": "Correct!", "The Sun gives no blue light there": "Sunlight still has all colours.", "The astronaut's eyes cannot see blue": "The eyes are normal.", "Space is full of black dust": "Space is nearly empty."},
 "sci10ch10.q.ex.q1": {"presbyopia.": "Presbyopia is a defect.", "accommodation.": "Correct!", "near-sightedness.": "That is a defect.", "far-sightedness.": "That is a defect."},
 "sci10ch10.q.ex.q2": {"cornea.": "Light enters through the cornea.", "iris.": "The iris controls the pupil.", "pupil.": "The pupil is an opening.", "retina.": "Correct!"},
 "sci10ch10.q.ex.q3": {"25 m.": "Far too large.", "2.5 cm.": "Far too small.", "25 cm.": "Correct!", "2.5 m.": "Too large."},
 "sci10ch10.q.ex.q4": {"pupil.": "The pupil only lets light in.", "retina.": "The retina is the screen.", "ciliary muscles.": "Correct!", "iris.": "The iris controls the pupil size."},
 "sci10ch10.q.sqp31": {S31[0]: "Correct!", S31[1]: "Colours are not scattered equally.", S31[2]: "Longer wavelengths are scattered less, not more.", S31[3]: "There are no blue particles."},
 "sci10ch10.q.gseb2025_5": {"cataract": "Correct!", "myopia": "Myopia blurs far objects.", "hypermetropia": "Hypermetropia blurs near objects.", "presbyopia": "Presbyopia is loss of accommodation."},
 "sci10ch10.q.gseb2025_19": {"Red": "Correct!", "Violet": "Violet bends the most.", "Green": "Green is in the middle."},
 "sci10ch10.q.mcq01": {"iris": "Correct!", "retina": "The retina is the screen.", "cornea": "The cornea is the clear front surface.", "optic nerve": "It carries signals to the brain."},
 "sci10ch10.q.mcq02": {"real and inverted": "Correct!", "virtual and erect": "A virtual image cannot form on a screen.", "real and erect": "A convex lens gives an inverted real image.", "virtual and inverted": "The image on the retina is real."},
 "sci10ch10.q.mcq03": {"convex lens": "Correct!", "concave lens": "That corrects myopia.", "plane glass": "Plane glass does not change focus.", "cylindrical mirror": "Mirrors are not used in spectacles."},
 "sci10ch10.q.mcq04": {"presbyopia with myopia": "Correct!", "cataract": "Cataract is treated by surgery.", "colour blindness": "Lenses cannot correct it.", "only myopia": "A simple concave lens corrects myopia alone."},
 "sci10ch10.q.mcq05": {"violet": "Correct!", "red": "Red deviates the least.", "yellow": "Yellow is in the middle.", "green": "Green is in the middle."},
 "sci10ch10.q.mcq06": {"in the direction opposite to the Sun": "Correct!", "towards the Sun": "The light comes back from the droplets.", "only at noon": "Rainbows are usually seen in the morning or evening.", "only at night": "A rainbow needs sunlight."},
 "sci10ch10.q.mcq07": {"atmospheric refraction": "Correct!", "scattering of light": "Scattering gives colour.", "dispersion": "Dispersion splits colours.", "reflection by clouds": "It happens on clear days too."},
 "sci10ch10.q.mcq08": {"is scattered the least by fog and smoke": "Correct!", "is scattered the most": "Then it could not be seen far.", "is the brightest colour": "Brightness is not the reason.", "travels slowest in air": "All colours travel almost equally fast in air."},
 "sci10ch10.q.mcq09": {"the Tyndall effect": "Correct!", "dispersion": "No colours are split.", "total internal reflection": "That needs a denser medium boundary.", "atmospheric refraction": "That causes twinkling."},
 "sci10ch10.q.mcq10": {"−0.5 D": "Correct!", "+0.5 D": "Myopia needs a concave (negative) lens.", "−2 D": "P = 1/f with f = −2 m gives −0.5 D.", "+2 D": "Sign and value are both wrong."},
}
AR = {
 "sci10ch10.q.ar1": ("myopia is corrected with a concave lens.", "diverging the rays moves the image back onto the retina."),
 "sci10ch10.q.ar2": ("planets shine steadily.", "the light from their many points averages out."),
 "sci10ch10.q.ar3": ("the sky looks blue.", "air molecules scatter blue light more than red."),
 "sci10ch10.q.ar4": ("a prism splits white light into colours.", "each colour bends by a different angle."),
 "sci10ch10.q.ar5": ("the near point of a normal eye is about 25 cm.", "the eye lens cannot become any thicker."),
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
