"""Per-option explanations for Science Ch 13 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch13_our_environment"

X3 = ["Carrying cloth-bags to put purchases in while shopping", "Switching off unnecessary lights and fans", "Walking to school instead of getting your mother to drop you on her scooter", "All of the above"]
F = {
 "sci10ch13.s2.check": {"Aquarium": "Correct!", "Forest": "A forest is natural.", "Lake": "A lake is natural.", "Pond": "A pond is natural."},
 "sci10ch13.s3.check": {"10 J": "Correct!", "100 J": "That reaches the secondary consumers.", "1000 J": "That reaches the herbivores.", "1 J": "Only three steps of 10%: 10 J."},
 "sci10ch13.s4.check": {"Eagle": "Correct!", "Grass": "The producer has the least.", "Grasshopper": "It is low in the chain.", "Frog": "Snakes and eagles above it collect more."},
 "sci10ch13.s5.check": {"absorbing harmful UV radiation from the Sun": "Correct!", "producing oxygen for breathing": "Plants produce our oxygen.", "keeping the earth warm at night": "That is not the role of ozone.", "blocking all sunlight": "Visible light passes through."},
 "sci10ch13.s6.check": {"Cake, wood and grass": "Correct!", "Grass, wood and plastic": "Plastic is not biodegradable.", "Glass, paper and leaves": "Glass is not biodegradable.", "Polythene, fruit peel and cotton": "Polythene is not biodegradable."},
 "sci10ch13.q.ex.q1": {"Grass, flowers and leather": "Leather takes very long to break down and is usually treated.", "Grass, wood and plastic": "Plastic is not biodegradable.",
                       "Fruit-peels, cake and lime-juice": "These are biodegradable too; the NCERT answer is (d), but (c) is also acceptable.", "Cake, wood and grass": "Correct!"},
 "sci10ch13.q.ex.q2": {"Grass, wheat and mango": "These are all producers.", "Grass, goat and human": "Correct!", "Goat, cow and elephant": "These are all herbivores; there is no producer.", "Grass, fish and goat": "A goat does not eat fish."},
 "sci10ch13.q.ex.q3": {X3[0]: "True, but the others are also eco-friendly.", X3[1]: "True, but the others are also eco-friendly.", X3[2]: "True, but the others are also eco-friendly.", X3[3]: "Correct!"},
 "sci10ch13.q.sqp6": {"(i), (ii), (iii)": "Statement (i) is wrong: ozone reduces UV.", "(ii), (iii), (iv)": "Correct!", "(iii), (iv), (v)": "Statement (v) is wrong: CFCs destroy ozone.", "(i), (iv), (v)": "Statements (i) and (v) are wrong."},
 "sci10ch13.q.sqp7": {"Organic farming": "It reduces chemicals.", "Increase in tree plantation": "Trees are not waste.", "Use of plastic as packaging material": "Correct!", "Composting of kitchen waste": "Composting reduces waste."},
 "sci10ch13.q.gseb2024_23": {"Primary consumer": "Correct!", "Secondary consumer": "That is the third level.", "Tertiary consumer": "That is the fourth level."},
 "sci10ch13.q.gseb2024_24": {"Primary consumer": "That is the second level.", "Secondary consumer": "Correct!", "Tertiary consumer": "That is the fourth level."},
 "sci10ch13.q.gseb2025_23": {"Herbivores": "Herbivores eat plants.", "Producers": "Correct!", "Carnivores": "Carnivores eat animals."},
 "sci10ch13.q.gseb2025_24": {"Herbivores": "Correct!", "Producers": "Producers make their own food.", "Carnivores": "Carnivores eat animals."},
 "sci10ch13.q.mcq01": {"Temperature": "Correct!", "Grass": "Grass is living.", "Bacteria": "Bacteria are living.", "Deer": "A deer is living."},
 "sci10ch13.q.mcq02": {"bacteria and fungi": "Correct!", "green plants": "Plants are producers.", "herbivores": "Herbivores are consumers.", "carnivores": "Carnivores are consumers."},
 "sci10ch13.q.mcq03": {"1%": "Correct!", "10%": "10% is what passes between trophic levels.", "50%": "Far less is captured.", "90%": "Far less is captured."},
 "sci10ch13.q.mcq04": {"10 J": "Correct!", "100 J": "That reaches the primary consumers.", "1 J": "Only two steps: 10 J.", "500 J": "Only 10% passes each step."},
 "sci10ch13.q.mcq05": {"unidirectional": "Correct!", "cyclic": "Nutrients cycle; energy does not.", "bidirectional": "It does not flow back.", "random": "It follows the food chain."},
 "sci10ch13.q.mcq06": {"primary consumer": "Correct!", "producer": "Grass is the producer.", "secondary consumer": "The lion is.", "decomposer": "Decomposers break down dead matter."},
 "sci10ch13.q.mcq07": {"chlorofluorocarbons (CFCs)": "Correct!", "carbon dioxide": "CO₂ causes global warming, not ozone depletion.", "oxygen": "Oxygen forms ozone.", "nitrogen": "Nitrogen is not the cause."},
 "sci10ch13.q.mcq08": {"Polythene bag": "Correct!", "Vegetable peel": "It rots easily.", "Paper": "Paper is biodegradable.", "Cotton cloth": "Cotton is biodegradable."},
 "sci10ch13.q.mcq09": {"energy decreases sharply at each step": "Correct!", "animals do not like long chains": "That is not a scientific reason.", "plants are few": "Plants are plentiful.", "decomposers stop them": "Decomposers do not limit chain length."},
 "sci10ch13.q.mcq10": {"freeze CFC production at 1986 levels": "Correct!", "ban all plastics": "It was about CFCs.", "plant more trees": "It was about CFCs.", "increase ozone at ground level": "Ground-level ozone is harmful."},
}
AR = {
 "sci10ch13.q.sqp9": ("the vulture, at the top, has the most pesticide.", "the vulture is at the last level and gets only 10% of the energy."),
 "sci10ch13.q.ar1": ("the top consumer has the most pesticide.", "the chemicals build up at every step."),
 "sci10ch13.q.ar2": ("food chains are short.", "too little energy is left after a few steps."),
 "sci10ch13.q.ar3": ("ozone at ground level is a deadly poison.", "the upper ozone layer does absorb UV."),
 "sci10ch13.q.ar4": ("decomposers are essential.", "they recycle nutrients back to the soil."),
 "sci10ch13.q.ar5": ("microbes cannot break plastics down.", "recycling does not explain why they do not break down."),
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
