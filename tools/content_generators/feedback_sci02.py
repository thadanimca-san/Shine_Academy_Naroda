"""Per-option explanations for Science Ch 2 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch02_acids_bases_and_salts"

F = {
 "sci10ch02.s2.check": {"basic": "Correct!", "acidic": "Phenolphthalein stays colourless in acids.", "neutral": "It stays colourless in neutral solutions.", "pure water": "Pure water is neutral; it stays colourless."},
 "sci10ch02.s3.check": {"sodium carbonate": "Correct!", "zinc": "Zinc gives hydrogen, which does not affect lime water.", "sodium hydroxide": "A base only neutralises the acid; no gas forms.", "copper oxide": "A metal oxide gives a salt and water, no gas."},
 "sci10ch02.s4.check": {"It contains ions": "Correct!", "It contains water molecules": "Pure water hardly conducts.", "It contains glucose": "Glucose gives no ions.", "It is a liquid": "Many liquids, like alcohol, do not conduct."},
 "sci10ch02.s5.check": {"A has more hydrogen ions; A is acidic and B is basic": "Correct!", "B has more hydrogen ions; B is acidic": "A higher pH means fewer hydrogen ions.", "Both are acidic": "pH 8 is above 7, so B is basic.", "Both are neutral": "Only pH 7 is neutral."},
 "sci10ch02.s6.check": {"Washing soda": "Correct!", "Baking soda": "Baking soda is used in cooking and as an antacid.", "Common salt": "Common salt does not remove hardness.", "Sodium hydroxide": "It is not used to soften water at home."},
 "sci10ch02.q.it5.q1": {"Bleaching powder": "Correct!", "Baking soda": "Baking soda is NaHCO₃.", "Washing soda": "Washing soda is Na₂CO₃·10H₂O.", "Plaster of Paris": "Plaster of Paris is CaSO₄·½H₂O."},
 "sci10ch02.q.it5.q2": {"Dry slaked lime": "Correct!", "Quicklime": "Quicklime is CaO; chlorine is passed over slaked lime, Ca(OH)₂.", "Limestone": "Limestone is calcium carbonate.", "Gypsum": "Gypsum gives plaster of Paris."},
 "sci10ch02.q.it5.q3": {"Washing soda": "Correct!", "Baking soda": "Baking soda is used in cooking.", "Sodium chloride": "Common salt does not soften water.", "Sodium hydroxide": "It is not used for softening water."},
 "sci10ch02.q.ex.q1": {"$1$": "pH 1 is strongly acidic; it would turn blue litmus red.", "$4$": "pH 4 is acidic.", "$5$": "pH 5 is acidic.", "$10$": "Correct!"},
 "sci10ch02.q.ex.q2": {"$\\mathrm{NaCl}$": "A salt does not release carbon dioxide from egg-shells.", "$\\mathrm{HCl}$": "Correct!", "$\\mathrm{LiCl}$": "A salt does not release carbon dioxide from egg-shells.", "$\\mathrm{KCl}$": "A salt does not release carbon dioxide from egg-shells."},
 "sci10ch02.q.ex.q3": {"$4$ mL": "Twice the base needs more acid, not less.", "$8$ mL": "That is for 10 mL of NaOH.", "$12$ mL": "Double 8 mL.", "$16$ mL": "Correct!"},
 "sci10ch02.q.ex.q4": {"Antibiotic": "Antibiotics fight bacterial infections.", "Analgesic": "Analgesics relieve pain.", "Antacid": "Correct!", "Antiseptic": "Antiseptics prevent infection of wounds."},
 "sci10ch02.q.sqp20": {"Orange in the acid, red in the base": "Methyl orange is red in acid.", "Red in the acid, yellow in the base": "Correct!", "Red in the acid, orange in the base": "In a base it turns yellow.", "Yellow in the acid, red in the base": "The colours are the other way round."},
 "sci10ch02.q.sqp21": {"Sulphuric acid": "An acid has a low pH.", "Acetic acid": "An acid has a low pH.", "Magnesium hydroxide": "It is a weak base and only slightly soluble.", "Sodium hydroxide": "Correct!"},
 "sci10ch02.q.sqp22": {"water soluble calcium carbonate converts to water soluble calcium bicarbonate.": "Calcium carbonate is insoluble: that is why lime water turns milky.",
                      "insoluble calcium carbonate converts to water soluble calcium bicarbonate.": "Correct!",
                      "water soluble calcium carbonate converts to insoluble calcium bicarbonate.": "It is the other way round.", "insoluble calcium carbonate converts to insoluble calcium bicarbonate.": "Calcium bicarbonate is soluble, so the milkiness goes."},
 "sci10ch02.q.gseb2024_1": {"Phenolphthalein": "Correct!", "Litmus": "Litmus comes from lichen: natural.", "Turmeric": "Turmeric is natural.", "Onion": "Onion is a natural olfactory indicator."},
 "sci10ch02.q.gseb2025_2": {"Methyl orange": "It changes colour, not smell.", "Phenolphthalein": "It changes colour, not smell.", "Vanilla": "Correct!", "Turmeric": "It changes colour, not smell."},
 "sci10ch02.q.mcq01": {"vinegar": "Correct!", "soap solution": "Soap is basic.", "lime water": "Lime water is basic.", "baking soda solution": "Baking soda is basic."},
 "sci10ch02.q.mcq02": {"Carbon dioxide": "Correct!", "Hydrogen": "Hydrogen comes from metals with acids.", "Oxygen": "No oxygen forms.", "Chlorine": "No chlorine forms."},
 "sci10ch02.q.mcq03": {"$1.2$": "Correct!", "$7.0$": "That is pure water.", "$7.4$": "That is blood.", "$10$": "That is milk of magnesia."},
 "sci10ch02.q.mcq04": {"$5.5$": "Correct!", "$7.5$": "That is slightly basic.", "$8.5$": "That is basic.", "$3.5$": "Decay starts earlier, below 5.5."},
 "sci10ch02.q.mcq05": {"$\\mathrm{NaHCO_{3}}$": "Correct!", "$\\mathrm{Na_{2}CO_{3}}$": "That is sodium carbonate (washing soda without water).", "$\\mathrm{NaOH}$": "That is caustic soda.", "$\\mathrm{NaCl}$": "That is common salt."},
 "sci10ch02.q.mcq06": {"Chlorine": "Correct!", "Hydrogen": "Hydrogen forms at the cathode.", "Oxygen": "Chloride ions are discharged, not oxygen.", "Carbon dioxide": "There is no carbon in brine."},
 "sci10ch02.q.mcq07": {"Sodium carbonate": "Correct!", "Sodium chloride": "Strong acid + strong base: neutral.", "Ammonium chloride": "Strong acid + weak base: acidic.", "Potassium sulphate": "Strong acid + strong base: neutral."},
 "sci10ch02.q.mcq08": {"baking soda": "Correct!", "vinegar": "Vinegar is an acid; it adds to the sting.", "lemon juice": "Lemon juice is acidic.", "common salt": "Salt is neutral and does not neutralise the acid."},
 "sci10ch02.q.mcq09": {"$2$": "Correct!", "$\\dfrac{1}{2}$": "That is plaster of Paris.", "$5$": "That is copper sulphate.", "$10$": "That is washing soda."},
 "sci10ch02.q.mcq10": {"Calcium oxide": "Correct!", "Carbon dioxide": "A non-metal oxide is acidic.", "Sulphur dioxide": "A non-metal oxide is acidic.", "Phosphorus pentoxide": "A non-metal oxide is acidic."},
}
AR = {
 "sci10ch02.q.ar1": ("glucose solution has no ions to carry current.", "having no ions is exactly why it cannot conduct."),
 "sci10ch02.q.ar2": ("pH 2 is further below 7.", "a lower pH means more hydrogen ions, not fewer."),
 "sci10ch02.q.ar3": ("moisture would make it set into hard gypsum.", "this setting reaction is exactly why it is kept dry."),
 "sci10ch02.q.ar4": ("acid must be added slowly to water.", "the heat given out is large."),
 "sci10ch02.q.ar5": ("sodium carbonate removes permanent hardness.", "it is true, but it is about baking soda, not washing soda."),
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
