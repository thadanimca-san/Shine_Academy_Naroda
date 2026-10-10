"""Per-option explanations for Science Ch 8 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch08_heredity"

F = {
 "sci10ch08.s2.check": {"Sexual reproduction": "Correct!", "Asexual reproduction": "Asexual reproduction gives only small copying variations.", "Both produce the same": "Sexual reproduction mixes DNA from two parents.", "Neither produces any variation": "DNA copying is never perfect."},
 "sci10ch08.s3.check": {"One quarter": "Correct!", "One half": "Only tt is short: one box in four.", "Three quarters": "Three quarters are tall.", "None": "The tt plants are short."},
 "sci10ch08.s4.check": {"RY, Ry, rY, ry": "Correct!", "Rr and Yy": "A gamete has one copy of each gene.", "RY and ry only": "The genes separate independently, giving Ry and rY too.", "RR, rr, YY, yy": "A gamete has one copy of each gene, not two of one."},
 "sci10ch08.s5.check": {"an enzyme that makes a growth hormone": "Correct!", "chlorophyll only": "Chlorophyll is for photosynthesis.", "the cell wall only": "The cell wall does not control height.", "water in the cells": "The gene controls an enzyme."},
 "sci10ch08.s6.check": {"boy": "Correct!", "girl": "A girl needs an X from the father.", "either, depending on the mother": "The mother always gives X.", "either, depending on the temperature": "That happens in some reptiles, not humans."},
 "sci10ch08.q.ex.q1": {"TTWW": "Then all offspring would be tall.", "TTww": "Then all would be tall and violet would not appear.", "TtWW": "Correct!", "TtWw": "Then about half the flowers would be white."},
 "sci10ch08.q.sqp5": {"BB X bb": "Correct!", "Bb X Bb": "One quarter would be white.", "Bb X bb": "Half would be white.", "bb X bb": "All would be white."},
 "sci10ch08.q.gseb2024_18": {"tt only": "Correct!", "TT only": "TT shows the dominant trait.", "Tt only": "Tt shows the dominant trait.", "TT and Tt": "These show the dominant trait."},
 "sci10ch08.q.gseb2025_10": {"Lizard": "Lizards do not change sex.", "Snail": "Correct!", "Frog": "Frogs do not change sex."},
 "sci10ch08.q.gseb2025_18": {"Trait A": "It is in fewer individuals, so it probably arose later.", "Trait B": "Correct!", "Both arose at the same time": "Their spread is very different.", "It cannot be said": "The spread gives a good clue."},
 "sci10ch08.q.mcq01": {"garden pea": "Correct!", "fruit fly": "Fruit flies were used later by other scientists.", "maize": "Mendel used peas.", "rose": "Mendel used peas."},
 "sci10ch08.q.mcq02": {"all tall": "Correct!", "all short": "Short is recessive.", "half tall, half short": "That is Tt × tt.", "medium height": "Mendel found no medium-height plants."},
 "sci10ch08.q.mcq03": {"1 : 2 : 1": "Correct!", "3 : 1": "That is the phenotype ratio.", "9 : 3 : 3 : 1": "That is for two traits.", "1 : 1": "That is Tt × tt."},
 "sci10ch08.q.mcq04": {"9 : 3 : 3 : 1": "Correct!", "3 : 1": "That is for one trait.", "1 : 2 : 1": "That is the genotype ratio for one trait.", "1 : 1 : 1 : 1": "That is a test cross with two traits."},
 "sci10ch08.q.mcq05": {"gene": "Correct!", "chromosome": "A chromosome carries many genes.", "nucleus": "The nucleus contains the chromosomes.", "gamete": "A gamete is a germ cell."},
 "sci10ch08.q.mcq06": {"XY": "Correct!", "XX": "That is a female.", "YY": "No human has YY.", "XO": "That is not the normal male set."},
 "sci10ch08.q.mcq07": {"the temperature at which the eggs are kept": "Correct!", "the X and Y chromosomes": "That is in humans.", "the food of the mother": "Food does not decide sex.", "the size of the egg": "Egg size does not decide sex."},
 "sci10ch08.q.mcq08": {"Two: T and t": "Correct!", "One: Tt": "A gamete has only one copy.", "Four": "There is only one gene pair, so two kinds.", "One: T": "Half the gametes carry t."},
 "sci10ch08.q.mcq09": {"1 tall : 1 short": "Correct!", "3 tall : 1 short": "That is Tt × Tt.", "all tall": "That is TT × tt.", "all short": "That is tt × tt."},
 "sci10ch08.q.mcq10": {"sexually": "Correct!", "asexually by fission": "Fission gives few variations.", "by budding": "Budding gives few variations.", "by fragmentation": "Fragmentation gives few variations."},
}
AR = {
 "sci10ch08.q.sqp8": ("the enzyme decides how much growth hormone is made.", "the gene makes the protein (enzyme) that helps the plant grow tall."),
 "sci10ch08.q.ar1": ("the father's sperm decides the sex.", "the X or Y in the sperm decides it, since every egg has X."),
 "sci10ch08.q.ar2": ("all F1 plants (Tt) are tall.", "tallness is dominant, not recessive."),
 "sci10ch08.q.ar3": ("a short plant must be tt.", "a recessive trait shows only in tt."),
 "sci10ch08.q.ar4": ("a variation may not help the individual at all.", "variations help a species survive changes."),
 "sci10ch08.q.ar5": ("each germ cell has one chromosome of each pair.", "fusion restores the full number every generation."),
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
