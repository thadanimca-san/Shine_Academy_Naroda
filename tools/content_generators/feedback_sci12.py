"""Per-option explanations for Science Ch 12 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch12_magnetic_effects_of_current"

E1 = ["The field consists of straight lines perpendicular to the wire.", "The field consists of straight lines parallel to the wire.", "The field consists of radial lines originating from the wire.", "The field consists of concentric circles centred on the wire."]
F = {
 "sci10ch12.s2.check": {"A compass at the crossing would point in two directions at once": "Correct!", "Field lines repel each other": "That is not the reason.", "Field lines exist only inside the magnet": "They exist outside too.", "They do cross near the poles": "They never cross."},
 "sci10ch12.s3.check": {"the same at all points (uniform)": "Correct!", "zero": "There is a strong field inside.", "strongest near the wire only": "Inside, it is the same everywhere.", "made of concentric circles": "That is around a straight wire."},
 "sci10ch12.s4.check": {"When the current is perpendicular to the field": "Correct!", "When the current is parallel to the field": "Then the force is zero.", "When the current is zero": "No current, no force.", "It is the same in all directions": "It depends on the angle."},
 "sci10ch12.s5.check": {"increases heavily": "Correct!", "reduces substantially": "The resistance falls, so the current rises.", "does not change": "It rises sharply.", "becomes zero": "It becomes very large."},
 "sci10ch12.s6.check": {"It draws about 9 A, so the fuse blows or the circuit overloads": "Correct!", "It works normally": "9 A is more than the 5 A rating.", "It draws only 2 A": "I = P/V = 2000/220 ≈ 9 A.", "The voltage doubles": "The supply voltage stays 220 V."},
 "sci10ch12.q.it4.q1": {"velocity and momentum": "Correct!", "mass": "Mass does not change.", "speed": "The force is perpendicular, so the speed stays the same.", "mass and speed": "Neither changes."},
 "sci10ch12.q.it4.q3": {"towards south": "Use Fleming's left-hand rule with current west and force north.", "towards east": "That is along the motion, giving no force.", "downward": "That would push it south.", "upward": "Correct!"},
 "sci10ch12.q.ex.q1": {E1[0]: "The lines go round the wire.", E1[1]: "The lines go round the wire.", E1[2]: "The lines are circles, not radial.", E1[3]: "Correct!"},
 "sci10ch12.q.ex.q2": {"reduces substantially.": "The resistance falls, so the current rises.", "does not change.": "It rises sharply.", "increases heavily.": "Correct!", "vary continuously.": "It rises sharply."},
 "sci10ch12.q.mcq01": {"north pole to south pole": "Correct!", "south pole to north pole": "That is inside the magnet.", "the middle to the ends": "They run from pole to pole.", "nowhere; they are absent outside": "They exist all around the magnet."},
 "sci10ch12.q.mcq02": {"closest together": "Correct!", "farthest apart": "Spread-out lines mean a weak field.", "curved the most": "Curvature does not show strength.", "straight": "Straightness does not show strength."},
 "sci10ch12.q.mcq03": {"the current is increased": "Correct!", "the wire is made longer": "Length does not change the field near it.", "the current is reduced": "Less current, weaker field.", "you move away from the wire": "The field weakens with distance."},
 "sci10ch12.q.mcq04": {"a strong electromagnet": "Correct!", "a permanent magnet always": "Soft iron loses magnetism when the current stops.", "non-magnetic": "Iron strengthens the field.", "a resistor": "It is not used as a resistor."},
 "sci10ch12.q.mcq05": {"force (motion)": "Correct!", "current": "That is the middle finger.", "magnetic field": "That is the forefinger.", "voltage": "Voltage is not part of the rule."},
 "sci10ch12.q.mcq06": {"50 Hz": "Correct!", "60 Hz": "That is used in some other countries.", "220 Hz": "220 is the voltage.", "100 Hz": "It changes direction 100 times a second, but the frequency is 50 Hz."},
 "sci10ch12.q.mcq07": {"red": "Correct!", "green": "Green is earth.", "black": "Black is neutral.", "blue": "Not used for live in the NCERT convention."},
 "sci10ch12.q.mcq08": {"15 A": "Correct!", "5 A": "That is for bulbs and fans.", "1 A": "Far too low.", "50 A": "Domestic circuits use 15 A."},
 "sci10ch12.q.mcq09": {"can be transmitted over long distances without much energy loss": "Correct!", "flows in one direction only": "That is DC.", "can be stored in a cell": "Cells store DC.", "has no frequency": "AC has a frequency of 50 Hz."},
 "sci10ch12.q.mcq10": {"west": "Correct!", "east": "Current is opposite to electron motion.", "north": "The motion is along east-west.", "south": "The motion is along east-west."},
}
AR = {
 "sci10ch12.q.ar1": ("field lines never cross.", "two directions at one point are impossible."),
 "sci10ch12.q.ar2": ("the fuse is in series with the live wire.", "being in series, its melting cuts off the supply."),
 "sci10ch12.q.ar3": ("metal bodies are earthed for safety.", "the earth wire carries current only during a leakage."),
 "sci10ch12.q.ar4": ("the field inside a solenoid is uniform.", "parallel, equally spaced lines mean a uniform field."),
 "sci10ch12.q.ar5": ("there is no force when the conductor is along the field.", "the maximum at 90° does not explain the zero at 0°."),
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
