"""Per-option explanations for Science Ch 1 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch01_chemical_reactions_and_equations"

F = {
 "sci10ch01.s1.check": {},
 "sci10ch01.s2.check": {"$2$": "Correct! 2 H and 2 Cl on each side.", "$1$": "One molecule of HCl has only one H and one Cl.", "$4$": "That would need two molecules of each gas.", "$3$": "Count the atoms: 2 H and 2 Cl."},
 "sci10ch01.s3.check1": {"decomposition reaction": "Correct!", "combination reaction": "Here one substance breaks up; it does not combine.", "displacement reaction": "No element takes another's place.", "double displacement reaction": "There is only one reactant."},
 "sci10ch01.s3.check2": {"$\\mathrm{CuO}$": "Correct! It loses oxygen.", "$\\mathrm{H_{2}}$": "Hydrogen gains oxygen: it is oxidised.", "$\\mathrm{Cu}$": "Copper is a product.", "$\\mathrm{H_{2}O}$": "Water is a product."},
 "sci10ch01.s4.check": {"To prevent the oil in them from getting oxidised": "Correct!", "To make the chips crisper by heating": "Nitrogen is not used for heating.", "To add flavour": "Nitrogen has no taste.", "To make the bag heavier": "The purpose is to keep oxygen out."},
 "sci10ch01.q.ex.q1": {"(a) and (b)": "Correct!", "(a) and (c)": "(c) is correct: carbon gains oxygen and is oxidised.", "(a), (b) and (c)": "(c) is a correct statement.", "all": "(c) and (d) are correct statements."},
 "sci10ch01.q.ex.q2": {"combination reaction.": "There are two products, not one.", "double displacement reaction.": "Aluminium is an element, not a compound.", "decomposition reaction.": "Two substances react; nothing breaks up on its own.", "displacement reaction.": "Correct!"},
 "sci10ch01.q.ex.q3": {"Hydrogen gas and iron chloride are produced.": "Correct!", "Chlorine gas and iron hydroxide are produced.": "Iron displaces hydrogen, not chlorine.", "No reaction takes place.": "Iron is more reactive than hydrogen.", "Iron salt and water are produced.": "Water forms when an acid reacts with a base, not a metal."},
 "sci10ch01.q.sqp17": {"Only equation 1 is a redox reaction, p = 1 and q = 3": "Count the atoms again: 2 Fe and 20 H.", "Both equations 1 and 2 are redox reactions, p = 2 and q = 4": "There are 20 hydrogen atoms in $\\mathrm{2C_{4}H_{10}}$.",
                       "Only equation 2 is a redox reaction, p = 2 and q = 10": "Equation 1 is also redox: Al is oxidised, Fe₂O₃ is reduced.", "Both equations 1 and 2 are redox reactions, p = 2 and q = 10": "Correct!"},
 "sci10ch01.q.sqp23": {"$\\mathrm{BaCl_{2}}$": "It is used up in the reaction.", "$\\mathrm{BaSO_{4}}$": "It is the insoluble precipitate.", "$\\mathrm{Na_{2}SO_{4}}$": "It is used up in the reaction.", "$\\mathrm{NaCl}$": "Correct!"},
 "sci10ch01.q.mcq01": {"(aq)": "Correct!", "(l)": "(l) means a liquid.", "(s)": "(s) means a solid.", "(g)": "(g) means a gas."},
 "sci10ch01.q.mcq02": {"combination and exothermic": "Correct!", "decomposition and endothermic": "Two substances combine, and heat is given out.", "displacement and exothermic": "Nothing is displaced.", "combination and endothermic": "The mixture gets hot: heat is given out."},
 "sci10ch01.q.mcq03": {"brown ferric oxide": "Correct!", "white ferrous oxide": "The residue is brown.", "black copper oxide": "There is no copper here.", "green ferrous sulphate": "It decomposes; it does not stay the same."},
 "sci10ch01.q.mcq04": {"$2 : 1$": "Correct!", "$1 : 2$": "Hydrogen is the larger volume.", "$1 : 1$": "Water has twice as many hydrogen atoms as oxygen atoms.", "$8 : 1$": "That is the ratio by mass, not by volume."},
 "sci10ch01.q.mcq05": {"decomposes in light": "Correct!", "combines with oxygen": "Light breaks it down; it does not combine.", "dissolves in water": "It is insoluble.", "is a good conductor": "Photography uses its reaction to light."},
 "sci10ch01.q.mcq06": {"potassium iodide solution": "Correct!", "sodium chloride solution": "Lead chloride is white, not yellow.", "copper sulphate solution": "No yellow precipitate forms.", "water": "Water only dilutes it."},
 "sci10ch01.q.mcq07": {"Copper turning into copper oxide on heating": "Correct!", "Copper oxide turning into copper with hydrogen": "That is reduction of copper oxide.", "Ice melting": "That is a physical change.", "Salt dissolving in water": "That is a physical change."},
 "sci10ch01.q.mcq08": {"Zinc": "Correct!", "Silver": "Silver is less reactive than copper.", "Gold": "Gold is less reactive than copper.", "Platinum": "Platinum is less reactive than copper."},
 "sci10ch01.q.mcq09": {"2, 2, 2, 1": "Correct!", "1, 1, 1, 1": "That leaves 2 H on the left and 3 H on the right.", "2, 1, 2, 1": "Check the oxygen and hydrogen atoms.", "1, 2, 1, 2": "Check the sodium atoms."},
 "sci10ch01.q.mcq10": {"corrosion": "Correct!", "rancidity": "Rancidity is about oils and fats in food.", "precipitation": "No precipitate forms from a solution.", "decomposition": "Silver combines with sulphur; it does not break up."},
}
F.pop("sci10ch01.s1.check")
AR = {
 "sci10ch01.q.ar1": ("atoms are neither created nor destroyed in a reaction.", "conservation of mass is exactly why balancing is needed."),
 "sci10ch01.q.ar2": ("zinc pushes copper out of copper sulphate.", "zinc is more reactive than copper, not the other way round."),
 "sci10ch01.q.ar3": ("heat is needed to break calcium carbonate down.", "it is true, but it does not explain the heat absorbed."),
 "sci10ch01.q.ar4": ("copper oxide loses oxygen, so it is reduced.", "losing oxygen is reduction."),
 "sci10ch01.q.ar5": ("nitrogen-filled packets keep food fresh.", "keeping oxygen away is exactly why nitrogen is used."),
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
