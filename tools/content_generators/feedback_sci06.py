"""Per-option explanations for Science Ch 6 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch06_control_and_coordination"

F = {
 "sci10ch06.s2.check": {"synapse": "Correct!", "axon": "The axon carries the impulse away from the cell body.", "dendrite": "Dendrites receive information.", "cell body": "The cell body has the nucleus."},
 "sci10ch06.s3.check": {"Cerebellum": "Correct!", "Medulla": "The medulla controls blood pressure, salivation and vomiting.", "Fore-brain": "The fore-brain is for thinking.", "Pons": "The pons is part of the hind-brain but does not control balance."},
 "sci10ch06.s4.check": {"abscisic acid": "Correct!", "auxin": "Auxin promotes cell growth.", "gibberellin": "Gibberellins help the stem grow.", "cytokinin": "Cytokinins promote cell division."},
 "sci10ch06.s5.check": {"Thyroxin": "Correct!", "Insulin": "Insulin is made by the pancreas without iodine.", "Adrenaline": "Adrenaline does not need iodine.", "Growth hormone": "Growth hormone does not need iodine."},
 "sci10ch06.s6.check": {"It reaches all cells of the body through the blood": "Correct!", "It is faster": "Nervous control is faster.", "It uses electrical impulses": "Nerves use electrical impulses; hormones are chemicals.", "It reaches only cells connected by nerves": "That is nervous control."},
 "sci10ch06.q.ex.q1": {"Insulin": "Insulin is an animal hormone.", "Thyroxin": "Thyroxin is an animal hormone.", "Oestrogen": "Oestrogen is an animal hormone.", "Cytokinin.": "Correct!"},
 "sci10ch06.q.ex.q2": {"dendrite.": "A dendrite is part of a neuron.", "synapse.": "Correct!", "axon.": "An axon is part of a neuron.", "impulse.": "The impulse is the message, not the gap."},
 "sci10ch06.q.ex.q3": {"thinking.": "Yes, but the brain does the others too.", "regulating the heart beat.": "Yes, but the brain does the others too.", "balancing the body.": "Yes, but the brain does the others too.", "all of the above.": "Correct!"},
 "sci10ch06.q.sqp3": {"Posture and balance: Cerebrum": "Balance is controlled by the cerebellum.", "Salivation: Medulla in midbrain": "The medulla is in the hind-brain.", "Hunger: Pons in hindbrain": "The hunger centre is in the fore-brain.", "Blood pressure: Medulla in hindbrain": "Correct!"},
 "sci10ch06.q.sqp4": {"growth hormone from pituitary gland": "Growth hormone controls growth, not blood sugar.", "oestrogen from ovary": "Oestrogen controls changes at puberty.", "insulin from pituitary gland": "Insulin is not made by the pituitary.", "insulin from pancreas": "Correct!"},
 "sci10ch06.q.gseb2025_17": {"Thyroxin": "Correct!", "Insulin": "Insulin does not need iodine.", "Adrenaline": "Adrenaline does not need iodine.", "Growth hormone": "Growth hormone does not need iodine."},
 "sci10ch06.q.gseb2025_21": {"Help in the growth of stem": "That is gibberellins.", "Wilting of leaves": "That is abscisic acid.", "Promote cell division": "Correct!"},
 "sci10ch06.q.gseb2025_22": {"Help in the growth of stem": "Correct!", "Wilting of leaves": "That is abscisic acid.", "Promote cell division": "That is cytokinin."},
 "sci10ch06.q.mcq01": {"dendrite → cell body → axon": "Correct!", "axon → cell body → dendrite": "That is backwards.", "cell body → dendrite → axon": "Information enters at the dendrite.", "axon → dendrite → cell body": "The axon is the exit, not the entry."},
 "sci10ch06.q.mcq02": {"spinal cord": "Correct!", "cerebrum": "The cerebrum is for thinking; reflexes skip it.", "cerebellum": "The cerebellum controls balance.", "heart": "The heart is not part of the nervous system."},
 "sci10ch06.q.mcq03": {"medulla": "Correct!", "cerebellum": "The cerebellum controls balance.", "fore-brain": "The fore-brain is for thinking.", "spinal cord": "The spinal cord handles reflexes."},
 "sci10ch06.q.mcq04": {"fore-brain": "Correct!", "cerebellum": "The cerebellum controls balance.", "medulla": "The medulla controls blood pressure and salivation.", "spinal cord": "The spinal cord handles reflexes."},
 "sci10ch06.q.mcq05": {"positive geotropism": "Correct!", "negative phototropism only": "Roots do grow away from light, but downward growth is a response to gravity.", "chemotropism": "That is growth towards chemicals.", "hydrotropism": "That is growth towards water."},
 "sci10ch06.q.mcq06": {"chemotropism": "Correct!", "hydrotropism": "That is growth towards water.", "phototropism": "That is growth towards light.", "geotropism": "That is growth in response to gravity."},
 "sci10ch06.q.mcq07": {"Auxin": "Correct!", "Abscisic acid": "It inhibits growth.", "Cytokinin": "It promotes cell division.", "Insulin": "Insulin is an animal hormone."},
 "sci10ch06.q.mcq08": {"Pituitary": "Correct!", "Thyroid": "The thyroid secretes thyroxin.", "Adrenal": "The adrenal secretes adrenaline.", "Pancreas": "The pancreas secretes insulin."},
 "sci10ch06.q.mcq09": {"the blood": "Correct!", "nerves": "Nerves carry electrical impulses, not hormones.", "the synapse": "The synapse is a gap between neurons.", "the lymph only": "Hormones are carried by the blood."},
 "sci10ch06.q.mcq10": {"dwarfism": "Correct!", "goitre": "Goitre is due to lack of iodine.", "diabetes": "Diabetes is due to lack of insulin.", "gigantism": "Gigantism is due to too much growth hormone."},
}
AR = {
 "sci10ch06.q.ar1": ("reflexes are quicker than actions we think about.", "skipping the thinking in the brain saves time."),
 "sci10ch06.q.ar2": ("touch makes the leaves fold up.", "the cells change shape by losing water; there is no growth."),
 "sci10ch06.q.ar3": ("iodine in salt is good for health.", "without iodine the thyroid cannot make thyroxin."),
 "sci10ch06.q.ar4": ("it prepares the body for an emergency.", "adrenaline is secreted by the adrenal glands."),
 "sci10ch06.q.ar5": ("shoots grow towards light.", "longer cells on the shady side bend the shoot towards the light."),
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
