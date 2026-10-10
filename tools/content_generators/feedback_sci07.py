"""Per-option explanations for Science Ch 7 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch07_how_do_organisms_reproduce"

F = {
 "sci10ch07.s2.check": {"Some variants may survive if the environment changes": "Correct!", "It makes every individual stronger": "A variation may not help the individual at all.", "It stops DNA copying": "Variation comes from DNA copying.", "It makes all offspring identical": "Variation makes them different."},
 "sci10ch07.s3.check": {"Plasmodium": "Correct!", "Amoeba": "Amoeba uses binary fission.", "Hydra": "Hydra uses budding and regeneration.", "Spirogyra": "Spirogyra uses fragmentation."},
 "sci10ch07.s4.check": {"fruit": "Correct!", "seed": "The ovule becomes the seed.", "embryo": "The zygote becomes the embryo.", "pollen tube": "The pollen tube grows from the pollen grain."},
 "sci10ch07.s5.check": {"Oviduct (fallopian tube)": "Correct!", "Uterus": "The zygote is implanted in the uterus after fertilisation.", "Ovary": "The ovary releases the egg.", "Vagina": "Fertilisation does not happen there."},
 "sci10ch07.s6.check": {"Condom": "Correct!", "Copper-T": "It only prevents pregnancy.", "Oral pills": "They only prevent pregnancy.", "Surgery": "It only prevents pregnancy."},
 "sci10ch07.q.ex.q1": {"Amoeba.": "Amoeba uses binary fission.", "Yeast.": "Correct!", "Plasmodium.": "Plasmodium uses multiple fission.", "Leishmania.": "Leishmania uses binary fission."},
 "sci10ch07.q.ex.q2": {"Ovary": "The ovary is a female part.", "Uterus": "The uterus is a female part.", "Vas deferens": "Correct!", "Fallopian tube": "The fallopian tube is a female part."},
 "sci10ch07.q.ex.q3": {"sepals.": "Sepals are separate outer parts.", "ovules.": "Ovules are in the ovary.", "pistil.": "The pistil is the female part.", "pollen grains.": "Correct!"},
 "sci10ch07.q.mcq01": {"binary fission in a definite plane": "Correct!", "multiple fission": "That is Plasmodium.", "budding": "That is Hydra and yeast.", "spore formation": "That is Rhizopus."},
 "sci10ch07.q.mcq02": {"fragmentation": "Correct!", "budding": "That is Hydra and yeast.", "multiple fission": "That is Plasmodium.", "regeneration only": "Spirogyra breaks up on its own: fragmentation."},
 "sci10ch07.q.mcq03": {"Bryophyllum": "Correct!", "Rose": "Rose is grown by cuttings or grafting.", "Mango": "Mango leaves do not form buds.", "Wheat": "Wheat grows from seeds."},
 "sci10ch07.q.mcq04": {"spore formation": "Correct!", "binary fission": "That is Amoeba.", "fragmentation": "That is Spirogyra.", "budding": "That is Hydra and yeast."},
 "sci10ch07.q.mcq05": {"Hibiscus": "Correct!", "Papaya": "Papaya flowers are unisexual.", "Watermelon": "Watermelon flowers are unisexual.", "None of these": "Hibiscus is bisexual."},
 "sci10ch07.q.mcq06": {"pollination": "Correct!", "fertilisation": "That is the fusion of gametes after pollination.", "germination": "That is the growth of a seed.", "regeneration": "That is regrowth from a body part."},
 "sci10ch07.q.mcq07": {"sperm formation needs a lower temperature": "Correct!", "they need more blood": "That is not the reason.", "they are too large": "Size is not the reason.", "they make urine": "The kidneys make urine."},
 "sci10ch07.q.mcq08": {"placenta": "Correct!", "ovary": "The ovary releases eggs.", "oviduct": "Fertilisation happens in the oviduct.", "cervix": "The cervix is the opening of the uterus."},
 "sci10ch07.q.mcq09": {"HIV-AIDS": "Correct!", "Gonorrhoea": "Gonorrhoea is bacterial.", "Syphilis": "Syphilis is bacterial.", "None of these": "HIV-AIDS is viral."},
 "sci10ch07.q.mcq10": {"half": "Correct!", "double": "Then the zygote would have four times the number.", "the same": "Then the zygote would have double the number.", "one-fourth": "Gametes have half."},
}
AR = {
 "sci10ch07.q.ar1": ("gametes carry half the chromosomes.", "halving keeps the number the same after fusion."),
 "sci10ch07.q.ar2": ("bananas are grown from suckers or stem cuttings.", "without seeds, another method is needed."),
 "sci10ch07.q.ar3": ("pollination moves pollen, while fertilisation is the fusion of gametes.", "fertilisation follows pollination."),
 "sci10ch07.q.ar4": ("a copper-T gives no protection against STDs.", "a copper-T is used to prevent pregnancy."),
 "sci10ch07.q.ar5": ("Planaria regenerates from pieces.", "its specialised cells can rebuild all the tissues."),
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
