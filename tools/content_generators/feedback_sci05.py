"""Per-option explanations for Science Ch 5 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch05_life_processes"

F = {
 "sci10ch05.s2.check": {"Make starch by photosynthesis": "Correct!", "Take in water through its roots": "Roots absorb water even in the dark.", "Respire": "Plants respire day and night.", "Lose water from its leaves": "Some water is still lost from the leaves."},
 "sci10ch05.s3.check": {"Bile": "Correct!", "Saliva": "Saliva digests starch in the mouth.", "Gastric juice": "Gastric juice is acidic, not alkaline.", "Pancreatic juice": "It has lipase, which digests fats only after bile has emulsified them."},
 "sci10ch05.s4.check": {"Mitochondria": "Correct!", "Cytoplasm": "Glucose becomes pyruvate in the cytoplasm; the next step needs mitochondria.", "Nucleus": "The nucleus controls the cell; it does not respire.", "Chloroplast": "Chloroplasts make food by photosynthesis."},
 "sci10ch05.s5.check": {"Left ventricle": "Correct!", "Right ventricle": "It pumps deoxygenated blood to the lungs.", "Left atrium": "It receives oxygenated blood from the lungs.", "Right atrium": "It receives deoxygenated blood from the body."},
 "sci10ch05.s6.check": {"tubule": "Correct!", "Bowman's capsule": "Filtration happens here, not reabsorption.", "urinary bladder": "The bladder only stores urine.", "ureter": "The ureter only carries urine to the bladder."},
 "sci10ch05.q.ex.q1": {"nutrition.": "Nutrition is about taking in food.", "respiration.": "The lungs are for respiration.", "excretion.": "Correct!", "transportation.": "The heart and blood vessels transport materials."},
 "sci10ch05.q.ex.q2": {"transport of water.": "Correct!", "transport of food.": "Phloem carries food.", "transport of amino acids.": "Amino acids move in the phloem.", "transport of oxygen.": "Oxygen enters through stomata and diffuses."},
 "sci10ch05.q.ex.q3": {"carbon dioxide and water.": "These are needed, but so are chlorophyll and sunlight.", "chlorophyll.": "Chlorophyll is needed, but so are the others.", "sunlight.": "Sunlight is needed, but so are the others.", "all of the above.": "Correct!"},
 "sci10ch05.q.ex.q4": {"cytoplasm.": "Only the first step, glucose to pyruvate, happens here.", "mitochondria.": "Correct!", "chloroplast.": "Chloroplasts carry out photosynthesis.", "nucleus.": "The nucleus does not break down food."},
 "sci10ch05.q.sqp1": {"Cuscuta, yeast, legumes, leeches and tapeworm": "Yeast is a saprophyte and legumes make their own food.", "Cactus, ticks, lice, leeches and cow": "Cactus is an autotroph and the cow is not a parasite.",
                      "Cuscuta, ticks, lice, leeches and tapeworm": "Correct!", "Cactus, grass, lice, lion and tapeworm": "Cactus and grass are autotrophs; the lion is a predator."},
 "sci10ch05.q.sqp2": {"Ethanol + carbon dioxide + Energy": "That happens in yeast.", "Lactic acid + Energy": "Correct!", "Lactic acid + carbon monoxide + Energy": "No carbon monoxide is formed.", "Carbon dioxide + Water + Energy": "That needs enough oxygen."},
 "sci10ch05.q.gseb2025_4": {"nutrition": "Nutrition is about food.", "transportation": "The heart and blood vessels transport materials.", "excretion": "The kidneys are for excretion.", "respiration": "Correct!"},
 "sci10ch05.q.gseb2025_9": {"ethanol": "Yeast makes ethanol, not our muscles.", "acetic acid": "Acetic acid is not formed in respiration.", "lactic acid": "Correct!"},
 "sci10ch05.q.mcq01": {"Mouth": "Correct!", "Stomach": "The stomach starts the digestion of proteins.", "Small intestine": "Starch digestion is completed here, not started.", "Large intestine": "The large intestine absorbs water."},
 "sci10ch05.q.mcq02": {"guard cells": "Correct!", "root hairs": "Root hairs absorb water from the soil.", "xylem vessels": "Xylem carries water up the plant.", "chloroplasts alone": "Chloroplasts make food; guard cells open the pore."},
 "sci10ch05.q.mcq03": {"Trypsin": "Correct!", "Lipase": "Lipase digests fats.", "Salivary amylase": "It digests starch, in the mouth.", "Pepsin": "Pepsin digests proteins, but it comes from the stomach."},
 "sci10ch05.q.mcq04": {"ATP": "Correct!", "Glucose": "Glucose is the fuel, not the currency.", "Pyruvate": "Pyruvate is a step in the breakdown of glucose.", "ADP": "ADP is what is left after ATP releases energy."},
 "sci10ch05.q.mcq05": {"ethanol and carbon dioxide": "Correct!", "lactic acid": "Lactic acid forms in our muscle cells.", "carbon dioxide and water": "That needs oxygen.", "glucose": "Glucose is the starting material."},
 "sci10ch05.q.mcq06": {"Pulmonary artery": "Correct!", "Pulmonary vein": "It brings oxygenated blood from the lungs.", "Aorta": "The aorta carries oxygenated blood to the body.", "Vena cava": "It brings deoxygenated blood from the body to the heart."},
 "sci10ch05.q.mcq07": {"Two": "Correct!", "Three": "Amphibians and many reptiles have three chambers.", "Four": "Birds and mammals have four chambers.", "One": "No vertebrate heart has one chamber."},
 "sci10ch05.q.mcq08": {"transpiration pull": "Correct!", "root pressure": "Root pressure is the main force at night.", "gravity": "Gravity pulls water down, not up.", "translocation": "Translocation is the movement of food in phloem."},
 "sci10ch05.q.mcq09": {"nephron": "Correct!", "neuron": "A neuron is a nerve cell.", "alveolus": "Alveoli are in the lungs.", "villus": "Villi are in the small intestine."},
 "sci10ch05.q.mcq10": {"dialysis": "Correct!", "transfusion": "Transfusion replaces blood; it does not remove waste.", "vaccination": "Vaccination prevents diseases.", "photosynthesis": "Photosynthesis happens in plants."},
}
AR = {
 "sci10ch05.q.ar1": ("bile has no enzymes but still helps digestion.", "emulsifying fats and making the medium alkaline help lipase to act."),
 "sci10ch05.q.ar2": ("ventricles have thicker, more muscular walls.", "pumping blood to all the organs needs more force."),
 "sci10ch05.q.ar3": ("aquatic organisms breathe much faster.", "water holds much less oxygen than air."),
 "sci10ch05.q.ar4": ("the pulmonary artery carries deoxygenated blood to the lungs.", "arteries carry blood away from the heart."),
 "sci10ch05.q.ar5": ("most of the filtrate does not become urine.", "selective reabsorption returns most of the water to the blood."),
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
