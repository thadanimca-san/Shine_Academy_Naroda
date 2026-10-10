"""Per-option explanations for Science Ch 3 objective items (keyed by option text)."""
import json, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
ROOT = sys.argv[1]
BASE = f"{ROOT}/app_core/content/cbse/class10/science/ncert_rationalised/ch03_metals_and_non_metals"

F = {
 "sci10ch03.s2.check": {"Mercury": "Correct!", "Sodium": "Sodium is a soft solid.", "Gallium": "Gallium melts only at about body temperature.", "Lead": "Lead is a solid."},
 "sci10ch03.s3.check1": {"Silver nitrate solution and copper": "Correct!", "Sodium chloride solution and copper": "Copper is less reactive than sodium.", "Iron sulphate solution and silver": "Silver is less reactive than iron.", "Magnesium chloride solution and aluminium": "Aluminium is less reactive than magnesium."},
 "sci10ch03.s3.check2": {"Copper": "Correct!", "Zinc": "Zinc is above hydrogen and gives hydrogen.", "Magnesium": "Magnesium reacts quickly with dilute acid.", "Iron": "Iron is above hydrogen."},
 "sci10ch03.s4.check": {"the ions can move only in the molten state": "Correct!", "the solid has no ions": "The solid is made of ions, but they are fixed.", "molten salt has free electrons": "Ions, not electrons, carry the current.", "heat makes it a metal": "It stays an ionic compound."},
 "sci10ch03.s5.check": {"roasting": "Correct!", "calcination": "Calcination is for carbonate ores in limited air.", "electrolysis": "Electrolysis uses electric current.", "refining": "Refining purifies a metal already extracted."},
 "sci10ch03.s6.check": {"lead and tin": "Correct!", "copper and zinc": "That is brass.", "copper and tin": "That is bronze.", "iron and nickel": "That is part of stainless steel."},
 "sci10ch03.q.it4.q2": {"Gold and platinum": "Correct!", "Sodium and potassium": "They are too reactive to occur free.", "Iron and zinc": "They are found as oxides, sulphides or carbonates.", "Aluminium and magnesium": "They are reactive and found in compounds."},
 "sci10ch03.q.it4.q3": {"Reduction": "Correct!", "Oxidation": "Removing oxygen is reduction.", "Calcination": "Calcination makes the oxide from a carbonate.", "Neutralisation": "That is an acid-base reaction."},
 "sci10ch03.q.it5.q2": {"Gold and platinum": "Correct!", "Iron and zinc": "Iron rusts; zinc slowly corrodes.", "Sodium and potassium": "They react at once with air.", "Copper and lead": "Copper turns green and lead tarnishes."},
 "sci10ch03.q.ex.q1": {"NaCl solution and copper metal": "Copper is less reactive than sodium.", "MgCl₂ solution and aluminium metal": "Aluminium is less reactive than magnesium.", "FeSO₄ solution and silver metal": "Silver is less reactive than iron.", "AgNO₃ solution and copper metal.": "Correct!"},
 "sci10ch03.q.ex.q2": {"Applying grease": "It works, but so do the others.", "Applying paint": "It works, but so do the others.", "Applying a coating of zinc": "It works, but so do the others.", "All of the above.": "Correct!"},
 "sci10ch03.q.ex.q3": {"calcium": "Correct!", "carbon": "Carbon forms gaseous oxides.", "silicon": "Silicon dioxide does not dissolve in water.", "iron.": "Iron oxide does not dissolve in water."},
 "sci10ch03.q.ex.q4": {"zinc is costlier than tin.": "The reason is reactivity, not cost.", "zinc has a higher melting point than tin.": "Melting point is not the reason.", "zinc is more reactive than tin.": "Correct!", "zinc is less reactive than tin.": "Zinc is more reactive than tin."},
 "sci10ch03.q.sqp18": {"I and II": "Calcium oxide is basic; it does not react with NaOH.", "I and III": "Correct!", "II and IV": "Calcium oxide does not react with NaOH, and SO₂ does react with NaOH.", "III and IV": "Sulphur dioxide, an acidic oxide, reacts with NaOH."},
 "sci10ch03.q.sqp19": {"In test tube P the iron nail gets a blue coating and in test tube Q there is no reaction.": "Copper is brown, not blue, and iron also displaces silver.", "The iron nail gets a brown coating in test tube P and a silver coating in test tube Q.": "Correct!",
                      "There is no reaction in either test tube P or Q.": "Iron is more reactive than copper and silver.", "There is no reaction in test tube P but a silver coating forms on the iron nail in test tube Q.": "Iron also displaces copper."},
 "sci10ch03.q.gseb2025_12": {"$\\mathrm{HgS}$": "Correct!", "$\\mathrm{ZnS}$": "That is zinc blende.", "$\\mathrm{Cu_{2}S}$": "That is copper glance."},
 "sci10ch03.q.mcq01": {"Iodine": "Correct!", "Sulphur": "Sulphur is dull yellow.", "Phosphorus": "Phosphorus is not lustrous.", "Carbon (coal)": "Coal is dull."},
 "sci10ch03.q.mcq02": {"Graphite": "Correct!", "Diamond": "Diamond does not conduct electricity.", "Coal": "Coal is a poor conductor.", "Charcoal powder": "Charcoal powder is a poor conductor."},
 "sci10ch03.q.mcq03": {"Potassium": "Correct!", "Magnesium": "Magnesium reacts only with hot water.", "Iron": "Iron reacts only with steam.", "Copper": "Copper does not react with water."},
 "sci10ch03.q.mcq04": {"bubbles of hydrogen stick to its surface": "Correct!", "it is lighter than water": "Calcium is denser than water.", "it melts": "It does not melt in water.", "it forms an oxide layer": "The bubbles, not an oxide layer, make it float."},
 "sci10ch03.q.mcq05": {"calcination": "Correct!", "roasting": "Roasting uses excess air, for sulphide ores.", "smelting": "Smelting is reduction at high temperature.", "refining": "Refining purifies the metal."},
 "sci10ch03.q.mcq06": {"aluminium": "Correct!", "iron oxide": "Iron oxide is reduced; it is the oxidising agent.", "carbon": "There is no carbon in the thermite reaction.", "hydrogen": "There is no hydrogen in the thermite reaction."},
 "sci10ch03.q.mcq07": {"electrolysis of their molten chlorides": "Correct!", "heating with carbon": "Carbon cannot reduce such reactive metals.", "heating alone": "That works only for metals like mercury.", "roasting": "Roasting only converts sulphides to oxides."},
 "sci10ch03.q.mcq08": {"22 parts gold and 2 parts silver or copper": "Correct!", "22 parts gold and 24 parts copper": "The total is 24 parts.", "pure gold": "Pure gold is 24 carat.", "2 parts gold and 22 parts copper": "It is the other way round."},
 "sci10ch03.q.mcq09": {"High melting point": "Correct!", "Conduction in the solid state": "Ions cannot move in the solid.", "Solubility in kerosene": "They dissolve in water, not kerosene.", "Low boiling point": "Their boiling points are high."},
 "sci10ch03.q.mcq10": {"zinc": "Correct!", "tin": "Tin plating is used for food cans.", "chromium": "That is chrome plating.", "copper": "Copper is not used for galvanising."},
}
AR = {
 "sci10ch03.q.ar1": ("kerosene keeps air and water away from sodium.", "its high reactivity is exactly why it is kept under kerosene."),
 "sci10ch03.q.ar2": ("copper does not give hydrogen with dilute HCl.", "copper lies below hydrogen in the series."),
 "sci10ch03.q.ar3": ("molten ionic compounds conduct.", "moving ions are exactly what carry the current."),
 "sci10ch03.q.ar4": ("aluminium oxide reacts with both acids and bases.", "it is true, but it does not explain the amphoteric nature of the oxide."),
 "sci10ch03.q.ar5": ("ornaments use 22 carat gold, not pure gold.", "pure gold is too soft to keep its shape."),
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
