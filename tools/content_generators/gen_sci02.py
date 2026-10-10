"""CBSE Class 10 Science Ch 2: Acids, Bases and Salts.
Equations go through ce(), which refuses unbalanced ones; ionic equations are
written by hand and checked separately below."""
import sys
from sci_common import Chapter, ce, chem, check, balanced, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch02"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch02_acids_bases_and_salts"
C = Chapter("sci10ch02")
blk = C.blk

E = {k: ce(v) for k, v in {
 "zn_h2so4": "Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g)", "naoh_zn": "2NaOH(aq) + Zn(s) -> Na2ZnO2(s) + H2(g)",
 "na2co3": "Na2CO3(s) + 2HCl(aq) -> 2NaCl(aq) + H2O(l) + CO2(g)", "nahco3": "NaHCO3(s) + HCl(aq) -> NaCl(aq) + H2O(l) + CO2(g)",
 "limewater": "Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l)", "bicarb": "CaCO3(s) + H2O(l) + CO2(g) -> Ca(HCO3)2(aq)",
 "neutral": "NaOH(aq) + HCl(aq) -> NaCl(aq) + H2O(l)", "cuo": "CuO + 2HCl -> CuCl2 + H2O", "caco3_hcl": "CaCO3 + 2HCl -> CaCl2 + H2O + CO2",
 "chloralkali": "2NaCl(aq) + 2H2O(l) -> 2NaOH(aq) + Cl2(g) + H2(g)", "bleach": "2Ca(OH)2 + 2Cl2 -> Ca(ClO)2 + CaCl2 + 2H2O",
 "solvay": "NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3", "soda_heat": "2NaHCO3 -[D]-> Na2CO3 + H2O + CO2",
 "washing": "Na2CO3 + 10H2O -> Na2CO3.10H2O", "cuso4": "CuSO4.5H2O -[D]-> CuSO4 + 5H2O", "mgoh2": "Mg(OH)2 + 2HCl -> MgCl2 + 2H2O",
 "mg_hcl": "Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)", "al_h2so4": "2Al(s) + 3H2SO4(aq) -> Al2(SO4)3(aq) + 3H2(g)", "fe_hcl": "Fe(s) + 2HCl(aq) -> FeCl2(aq) + H2(g)",
 "naoh_h2so4": "2NaOH(aq) + H2SO4(aq) -> Na2SO4(aq) + 2H2O(l)",
}.items()}
# Ionic and fractional equations, written by hand (balance checked on whole-number versions)
H3O = "$\\mathrm{H_{3}O^{+}}$"; HPLUS = "$\\mathrm{H^{+}(aq)}$"; OHM = "$\\mathrm{OH^{-}(aq)}$"
ION_HCL = "$\\mathrm{HCl + H_{2}O \\rightarrow H_{3}O^{+} + Cl^{-}}$"
ION_NAOH = "$\\mathrm{NaOH(s) \\xrightarrow{H_{2}O} Na^{+}(aq) + OH^{-}(aq)}$"
ION_NEUT = "$\\mathrm{H^{+}(aq) + OH^{-}(aq) \\rightarrow H_{2}O(l)}$"
POP_FORM = "$\\mathrm{CaSO_{4} \\cdot 2H_{2}O \\xrightarrow{373\\,K} CaSO_{4} \\cdot \\tfrac{1}{2}H_{2}O + 1\\tfrac{1}{2}H_{2}O}$"
POP_SET = "$\\mathrm{CaSO_{4} \\cdot \\tfrac{1}{2}H_{2}O + 1\\tfrac{1}{2}H_{2}O \\rightarrow CaSO_{4} \\cdot 2H_{2}O}$"
check(balanced("2CaSO4.2H2O -> (CaSO4)2.H2O + 3H2O") and balanced("(CaSO4)2.H2O + 3H2O -> 2CaSO4.2H2O"), "plaster of Paris (doubled: two units of CaSO4·½H2O share one H2O)")

INDICATORS = ("| Indicator | In acid | In base |\n|---|---|---|\n| Litmus | blue → red | red → blue |\n| Phenolphthalein | colourless | pink |\n| Methyl orange | red | yellow |\n"
              "| Turmeric | yellow | reddish-brown |\n| Onion (olfactory) | smell stays | smell goes |\n| Vanilla (olfactory) | smell stays | smell goes |")
PH_TABLE = ("| Substance | pH (about) |\n|---|---|\n| Gastric juice | $1.2$ |\n| Lemon juice | $2.2$ |\n| Pure water | $7.0$ |\n| Blood | $7.4$ |\n| Milk of magnesia | $10$ |\n| Sodium hydroxide solution | $14$ |")
SALTS = ("| Salt | Formula | Made from | Main uses |\n|---|---|---|---|\n"
         f"| Common salt | {chem('NaCl')} | sea water, rock salt | food; raw material for NaOH, baking soda, washing soda, bleaching powder |\n"
         f"| Bleaching powder | {chem('Ca(ClO)2')} | chlorine + dry slaked lime | bleaching cotton, linen and paper; disinfecting drinking water; oxidising agent |\n"
         f"| Baking soda | {chem('NaHCO3')} | NaCl + water + CO₂ + NH₃ | baking powder, antacid, soda-acid fire extinguishers |\n"
         f"| Washing soda | {chem('Na2CO3.10H2O')} | heating baking soda, then recrystallising | glass, soap and paper industries; removing permanent hardness of water; cleaning |\n"
         f"| Plaster of Paris | $\\mathrm{{CaSO_{{4}} \\cdot \\tfrac{{1}}{{2}}H_{{2}}O}}$ | heating gypsum at 373 K | plaster for broken bones, toys, decoration, smooth surfaces |")

sections = [
 {"id": "s1", "title": "Sour, bitter and salty", "blocks": [
  blk("s1.hook", "hook", title="Why does an ant bite sting?",
    body="Lemon and curd taste **sour**: they contain acids. Soap and baking soda feel soapy and taste **bitter**: they are bases. An ant or bee sting hurts because it injects an acid, and rubbing a little baking soda, a base, gives relief.\n\n"
         "In this chapter you will learn how to recognise acids and bases safely with indicators, how they react, what pH means, and how common salts like baking soda and plaster of Paris are made."),
  blk("s1.inspiration", "inspiration", title="Medicines from Indian plants", person="Asima Chatterjee", years="1917–2006",
    body="Asima Chatterjee studied the chemistry of Indian medicinal plants. From them she developed the anti-epileptic drug **Ayush-56** (from *Marsilea minuta*) and anti-malarial medicines.\n\n"
         "In 1944 she became the first woman to receive a Doctor of Science degree from an Indian university, and in 1975 she was the first woman General President of the Indian Science Congress.",
    quote="Careful work in the laboratory can turn traditional knowledge into medicine for everyone.",
    future="Chemists who understand acids, bases and salts work in medicines, food processing, water treatment, agriculture and cosmetics."),
  blk("s1.socratic", "socratic_question", question="Which of these would you use to find out, safely, whether a liquid is an acid?",
    options=["An indicator such as litmus", "Tasting it", "Touching it"], correct_index=0,
    explanation="Never taste or touch unknown chemicals. Indicators change colour (or smell) in acids and bases."),
 ]},
 {"id": "s2", "title": "Indicators", "blocks": [
  blk("s2.reveal", "theory", title="Acid-base indicators", revision=True,
    body="An **indicator** shows, by a change in colour or smell, whether a substance is acidic or basic.\n\n"
         "- **Natural:** litmus (from lichen), turmeric, red cabbage leaves, coloured flower petals.\n- **Synthetic:** phenolphthalein and methyl orange.\n"
         "- **Olfactory:** onion, vanilla and clove oil, whose smell disappears in a base.\n\nAcids turn blue litmus red; bases turn red litmus blue."),
  blk("s2.table", "markdown_table", title="Indicator colours", revision=True, body=INDICATORS),
  blk("s2.check", "knowledge_check", question="Phenolphthalein is added to a solution and it turns pink. The solution is:",
    options=["basic", "acidic", "neutral", "pure water"], correct_index=0, explanation="Phenolphthalein is colourless in acids and neutral water, and pink in bases."),
 ]},
 {"id": "s3", "title": "How acids and bases react", "blocks": [
  blk("s3.metals", "theory", title="With metals", revision=True,
    body=f"Acid + metal → salt + hydrogen gas: {E['zn_h2so4']}\n\nThe hydrogen burns with a **pop** sound near a burning candle.\n\n"
         f"Some metals react with strong bases too: {E['naoh_zn']} (sodium zincate). Not every metal does this."),
  blk("s3.carbonates", "theory", title="With carbonates and hydrogencarbonates", revision=True,
    body=f"Metal carbonate or hydrogencarbonate + acid → salt + carbon dioxide + water:\n\n- {E['na2co3']}\n- {E['nahco3']}\n\n"
         f"Carbon dioxide turns lime water milky: {E['limewater']} With excess carbon dioxide the milkiness disappears, because soluble calcium hydrogencarbonate forms: {E['bicarb']}\n\n"
         "Limestone, chalk and marble are all forms of calcium carbonate."),
  blk("s3.neutral", "theory", title="Acids with bases: neutralisation", revision=True,
    body=f"Acid + base → salt + water. This is **neutralisation**: {E['neutral']}\n\n"
         f"Metal oxides react with acids like bases do, so they are **basic oxides**: {E['cuo']} (the solution turns blue-green). "
         f"Non-metal oxides react with bases like acids do, so they are **acidic oxides**: {E['limewater']}"),
  blk("s3.discovery", "discovery", title="Activity 2.5: watch the pink disappear",
    body="Take a little dilute sodium hydroxide solution and add two drops of phenolphthalein: it turns pink. Add dilute hydrochloric acid drop by drop. "
         "At one drop the pink colour disappears: the base has been neutralised. Add one drop of NaOH again, and the pink returns."),
  blk("s3.check", "knowledge_check", question="A gas that turns lime water milky is given off when an acid reacts with:",
    options=["sodium carbonate", "zinc", "sodium hydroxide", "copper oxide"], correct_index=0, explanation="Carbonates give carbon dioxide, which turns lime water milky."),
 ]},
 {"id": "s4", "title": "What acids and bases have in common", "blocks": [
  blk("s4.thm", "theory", title="Ions in water", revision=True,
    body=f"Acids give **hydrogen ions** {HPLUS} in water; these join water molecules as hydronium ions {H3O}: {ION_HCL}\n\n"
         f"Bases give **hydroxide ions** {OHM}: {ION_NAOH} Bases that dissolve in water are called **alkalis**.\n\n"
         f"Neutralisation is really {ION_NEUT}\n\n"
         "Solutions of acids and bases conduct electricity because they contain ions. Glucose and alcohol contain hydrogen but do not give H⁺ ions, so they are not acids. "
         "Dry HCl gas does not change dry litmus: without water there are no H⁺ ions."),
  blk("s4.caution", "teacher_tip", title="Safety: acid into water",
    body="Mixing a concentrated acid or base with water is highly **exothermic**. Always add the acid **slowly to water** while stirring, never water to acid: the heat could make the mixture splash out and the glass could crack. "
         "Mixing an acid or base with water lowers the concentration of ions per unit volume: this is **dilution**."),
  blk("s4.check", "knowledge_check", question="Why does an aqueous solution of an acid conduct electricity?",
    options=["It contains ions", "It contains water molecules", "It contains glucose", "It is a liquid"], correct_index=0, explanation="Ions carry the electric current; pure water and glucose solution have almost none."),
 ]},
 {"id": "s5", "title": "How strong? The pH scale", "blocks": [
  blk("s5.thm", "theory", title="pH", revision=True,
    body="The **pH scale** runs from 0 to 14 and measures the hydrogen ion concentration. **p** stands for *potenz*, German for power.\n\n"
         "- pH 7: neutral.\n- pH less than 7: acidic. The **lower** the pH, the **more** H⁺ ions and the **stronger** the acid.\n- pH more than 7: basic. The higher the pH, the more OH⁻ ions and the stronger the base.\n\n"
         "A **universal indicator** shows different colours at different pH values. Acids that give many H⁺ ions (like HCl) are **strong**; those that give fewer (like acetic acid) are **weak**."),
  blk("s5.table", "markdown_table", title="pH of some common substances", revision=True, body=PH_TABLE),
  blk("s5.life", "theory", title="pH in everyday life", revision=True,
    body="- **Our body** works within a narrow pH range, about 7.0 to 7.8. Acid rain (pH below 5.6) harms fish in rivers.\n"
         "- **Digestion:** the stomach makes hydrochloric acid. Too much causes **indigestion**; an **antacid** such as milk of magnesia, a mild base, neutralises it: " + E["mgoh2"] + "\n"
         "- **Tooth decay** starts when the pH in the mouth falls below 5.5; bacteria make acids from sugar left on teeth. Toothpastes are basic.\n"
         "- **Soil:** plants need a suitable pH; acidic soil is treated with quicklime, slaked lime or chalk.\n"
         "- **Self-defence:** bee stings and nettle leaves inject methanoic acid; baking soda, or the dock plant's leaf, gives relief."),
  blk("s5.check", "knowledge_check", question="Solution A has pH 6 and solution B has pH 8. Which statement is correct?",
    options=["A has more hydrogen ions; A is acidic and B is basic", "B has more hydrogen ions; B is acidic", "Both are acidic", "Both are neutral"], correct_index=0,
    explanation="A lower pH means more H⁺ ions; pH 6 is acidic and pH 8 is basic."),
 ]},
 {"id": "s6", "title": "Salts", "blocks": [
  blk("s6.thm", "theory", title="Families and pH of salts", revision=True,
    body="Salts with the same positive or negative radical belong to a **family**: sodium chloride and sodium sulphate are both sodium salts; sodium chloride and potassium chloride are chloride salts.\n\n"
         "- Strong acid + strong base → **neutral** salt (pH 7), such as NaCl.\n- Strong acid + weak base → **acidic** salt (pH < 7), such as NH₄Cl.\n- Weak acid + strong base → **basic** salt (pH > 7), such as Na₂CO₃ and CH₃COONa."),
  blk("s6.chloralkali", "theory", title="From common salt", revision=True,
    body=f"Electricity passed through brine (a solution of sodium chloride) splits it; this is the **chlor-alkali process**: {E['chloralkali']} "
         "Chlorine forms at the anode, hydrogen at the cathode and sodium hydroxide near the cathode.\n\n"
         f"- **Bleaching powder**, from chlorine and dry slaked lime: {E['bleach']}\n- **Baking soda**: {E['solvay']}. On heating: {E['soda_heat']} "
         "The carbon dioxide makes bread and cake soft and spongy.\n"
         f"- **Washing soda**: heat baking soda to get sodium carbonate, then recrystallise: {E['washing']}"),
  blk("s6.crystal", "theory", title="Water of crystallisation", revision=True,
    body=f"Many salt crystals contain a fixed number of water molecules, the **water of crystallisation**. Blue copper sulphate crystals turn white on heating as this water is lost: {E['cuso4']} "
         "Adding water makes them blue again. Gypsum is CaSO₄·2H₂O.\n\n"
         f"**Plaster of Paris** is made by heating gypsum at 373 K: {POP_FORM} With water it sets into a hard mass of gypsum: {POP_SET} "
         "So plaster of Paris is kept in moisture-proof containers."),
  blk("s6.table", "markdown_table", title="Important salts", revision=True, body=SALTS),
  blk("s6.check", "knowledge_check", question="Which sodium compound is used for softening hard water?",
    options=["Washing soda", "Baking soda", "Common salt", "Sodium hydroxide"], correct_index=0, explanation="Washing soda (sodium carbonate) removes permanent hardness of water."),
  blk("s6.memory", "memory_trick", title="Five salts, one source", revision=True,
    body="Almost all of them start from **common salt**:\n\n- Electrolyse brine → NaOH + Cl₂ + H₂ → Cl₂ + slaked lime → **bleaching powder**.\n- NaCl + CO₂ + NH₃ → **baking soda** → heat → soda ash → + 10 water → **washing soda**.\n"
         "- **Gypsum** (2 water) → heat → **plaster of Paris** (half water) → + water → gypsum again."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Saying 'the lower the pH, the weaker the acid': a lower pH means a **stronger** acid.\n- Writing that all bases are alkalis: only bases that dissolve in water are alkalis.\n"
         "- Confusing baking soda (NaHCO₃) with washing soda (Na₂CO₃·10H₂O).\n- Adding water to concentrated acid.\n- Forgetting that the milkiness of lime water disappears with excess carbon dioxide."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why glucose contains hydrogen but is not an acid, and why a milkman might add a pinch of baking soda to fresh milk."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** neutralisation is a double displacement reaction.\n- **Chapter 3, Metals and Non-metals:** basic and acidic oxides, and amphoteric oxides that behave as both.\n"
         "- **Chapter 5, Life Processes:** hydrochloric acid in the stomach and the role of pH in digestion."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="10 mL of a sodium hydroxide solution is exactly neutralised by 8 mL of a hydrochloric acid solution. How much of the same acid is needed for 20 mL of the same base?\n\n"
         "**Answer:** The amount of acid needed is proportional to the amount of base. Twice the base needs twice the acid: $2 \\times 8 = 16$ mL."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Acids are sour, turn blue litmus red and give H⁺ (H₃O⁺) ions in water. Bases are bitter and soapy, turn red litmus blue and give OH⁻ ions.\n"
         "- Acid + metal → salt + hydrogen; acid + carbonate → salt + carbon dioxide + water; acid + base → salt + water (neutralisation).\n"
         "- Metal oxides are basic; non-metal oxides are acidic.\n- pH 7 is neutral; below 7 acidic; above 7 basic.\n"
         "- Common salt is the raw material for sodium hydroxide, bleaching powder, baking soda and washing soda. Plaster of Paris sets into gypsum with water."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Learn the general equations (acid + metal, acid + carbonate, acid + base) and one balanced example of each.\n- Know the colours of litmus, phenolphthalein and methyl orange in acids and bases.\n"
         "- For pH questions, remember: more H⁺ means lower pH.\n- Learn the formulas, preparation and two uses of bleaching powder, baking soda, washing soda and plaster of Paris."),
  blk("s7.flash1", "flashcard", front="pH of a neutral solution", back="$7$"),
  blk("s7.flash2", "flashcard", front="Chemical name of washing soda", back="Sodium carbonate decahydrate, " + chem("Na2CO3.10H2O")),
  blk("s7.flash3", "flashcard", front="Below which pH does tooth decay start?", back="$5.5$"),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Acids, Bases and Salts",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 2,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: definitions in terms of furnishing H⁺ and OH⁻ ions, general properties, examples and uses, neutralisation, the concept of pH scale, importance of pH in everyday life; preparation and uses of sodium hydroxide, bleaching powder, baking soda, washing soda and plaster of Paris.",
  "concepts": ["indicators_properties", "ph", "salts"], "sections": sections}

# ---------------------------------------------------------------- questions
IP, PH, SL = "indicators_properties", "ph", "salts"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 2 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2 = ["1 mark: answer", "1 mark: reason or equation"]

# In-text
C.q("it1.q1", "short_answer", 3, [IP], it("2.1", 1), "You have been provided with three test tubes. One of them contains distilled water and the other two contain an acidic solution and a basic solution, respectively. If you are given only red litmus paper, how will you identify the contents of each test tube?",
    answer_steps=["Dip the red litmus paper in each test tube. The solution that turns it blue is the base.", "Dip this blue litmus paper in the other two. The one that turns it red again is the acid.",
                  "The remaining test tube, which changes neither colour, contains distilled water."], marking_scheme=["1 mark: base", "1 mark: acid", "1 mark: water"])
C.q("it2.q1", "very_short_answer", 2, [IP], it("2.2", 1), "Why should curd and sour substances not be kept in brass and copper vessels?", "easy",
    answer_steps=["Curd and sour substances contain acids.", "The acids react with copper and brass to form poisonous compounds that spoil the food."], marking_scheme=MS2)
C.q("it2.q2", "short_answer", 3, [IP], it("2.2", 2), "Which gas is usually liberated when an acid reacts with a metal? Illustrate with an example. How will you test for the presence of this gas?",
    answer_steps=["Hydrogen gas is liberated.", "Example: " + E["zn_h2so4"], "Bring a burning candle near the gas: it burns with a pop sound."], marking_scheme=["1 mark: gas", "1 mark: equation", "1 mark: test"])
C.q("it2.q3", "very_short_answer", 2, [IP], it("2.2", 3), "Metal compound A reacts with dilute hydrochloric acid to produce effervescence. The gas evolved extinguishes a burning candle. Write a balanced chemical equation for the reaction if one of the compounds formed is calcium chloride.",
    answer_steps=["The gas is carbon dioxide and A is calcium carbonate.", E["caco3_hcl"]], marking_scheme=["1 mark: A and the gas", "1 mark: equation"])
C.q("it3.q1", "very_short_answer", 2, [IP], it("2.3", 1), "Why do HCl, HNO₃, etc., show acidic characters in aqueous solutions while solutions of compounds like alcohol and glucose do not show acidic character?",
    answer_steps=["HCl and HNO₃ give hydrogen ions (H⁺, as H₃O⁺) in water.", "Alcohol and glucose contain hydrogen but do not release H⁺ ions in water, so they are not acidic."], marking_scheme=MS2)
C.q("it3.q2", "very_short_answer", 2, [IP], it("2.3", 2), "Why does an aqueous solution of an acid conduct electricity?", "easy",
    answer_steps=["An acid in water gives ions: " + ION_HCL, "These moving ions carry the electric current."], marking_scheme=MS2)
C.q("it3.q3", "very_short_answer", 2, [IP], it("2.3", 3), "Why does dry HCl gas not change the colour of the dry litmus paper?", "easy",
    answer_steps=["HCl shows acidic behaviour only when it gives H⁺ ions, and that needs water.", "Dry HCl and dry litmus have no water, so no H⁺ ions form and the colour does not change."], marking_scheme=MS2)
C.q("it3.q4", "very_short_answer", 2, [IP], it("2.3", 4), "While diluting an acid, why is it recommended that the acid should be added to water and not water to the acid?",
    answer_steps=["Mixing a concentrated acid with water is highly exothermic.", "If water is added to the acid, the heat can make the mixture boil and splash out, and the glass can break; adding acid slowly to water keeps it safe."], marking_scheme=MS2)
C.q("it3.q5", "very_short_answer", 2, [PH], it("2.3", 5), "How is the concentration of hydronium ions (H₃O⁺) affected when a solution of an acid is diluted?", "easy",
    answer_steps=["On dilution the same ions are spread through a larger volume.", "So the concentration of H₃O⁺ ions per unit volume decreases."], marking_scheme=MS2)
C.q("it3.q6", "very_short_answer", 2, [PH], it("2.3", 6), "How is the concentration of hydroxide ions (OH⁻) affected when excess base is dissolved in a solution of sodium hydroxide?", "easy",
    answer_steps=["More base gives more OH⁻ ions in the same volume.", "So the concentration of OH⁻ ions increases (up to a limit)."], marking_scheme=MS2)
C.q("it4.q1", "very_short_answer", 2, [PH], it("2.4", 1), "You have two solutions, A and B. The pH of solution A is 6 and pH of solution B is 8. Which solution has more hydrogen ion concentration? Which of this is acidic and which one is basic?", "easy",
    answer_steps=["A has more hydrogen ion concentration (lower pH).", "A is acidic (pH less than 7) and B is basic (pH more than 7)."], marking_scheme=MS2)
C.q("it4.q2", "very_short_answer", 2, [PH], it("2.4", 2), "What effect does the concentration of H⁺(aq) ions have on the nature of the solution?", "easy",
    answer_steps=["The higher the concentration of H⁺ ions, the lower the pH and the more acidic the solution.", "A lower H⁺ concentration makes the solution less acidic or basic."], marking_scheme=MS2)
C.q("it4.q3", "very_short_answer", 2, [PH], it("2.4", 3), "Do basic solutions also have H⁺(aq) ions? If yes, then why are these basic?",
    answer_steps=["Yes, basic solutions also have some H⁺ ions.", "They are basic because the concentration of OH⁻ ions is greater than that of H⁺ ions."], marking_scheme=MS2)
C.q("it4.q4", "very_short_answer", 2, [PH], it("2.4", 4), "Under what soil condition do you think a farmer would treat the soil of his fields with quick lime (calcium oxide) or slaked lime (calcium hydroxide) or chalk (calcium carbonate)?",
    answer_steps=["When the soil is too acidic.", "These are bases (or a carbonate) and neutralise the extra acid, bringing the pH to a level suitable for crops."], marking_scheme=MS2)
C.mcq("it5.q1", [SL], "What is the common name of the compound " + chem("Ca(ClO)2") + "?", ["Bleaching powder", "Baking soda", "Washing soda", "Plaster of Paris"], 0,
      "Ca(ClO)₂ (calcium hypochlorite) is how bleaching powder is represented.", source=it("2.5", 1))
C.mcq("it5.q2", [SL], "Name the substance which on treatment with chlorine yields bleaching powder.", ["Dry slaked lime", "Quicklime", "Limestone", "Gypsum"], 0, "Chlorine reacts with dry slaked lime, Ca(OH)₂: " + E["bleach"], source=it("2.5", 2))
C.mcq("it5.q3", [SL], "Name the sodium compound which is used for softening hard water.", ["Washing soda", "Baking soda", "Sodium chloride", "Sodium hydroxide"], 0, "Washing soda (Na₂CO₃·10H₂O) removes permanent hardness.", source=it("2.5", 3))
C.q("it5.q4", "very_short_answer", 2, [SL], it("2.5", 4), "What will happen if a solution of sodium hydrocarbonate is heated? Give the equation of the reaction involved.",
    answer_steps=["It decomposes into sodium carbonate, water and carbon dioxide gas.", E["soda_heat"]], marking_scheme=MS2)
C.q("it5.q5", "very_short_answer", 2, [SL], it("2.5", 5), "Write an equation to show the reaction between Plaster of Paris and water.", "easy",
    answer_steps=[POP_SET, "Plaster of Paris sets into a hard solid mass of gypsum."], marking_scheme=MS2)
# Exercises
C.mcq("ex.q1", [PH], "A solution turns red litmus blue, its pH is likely to be", ["$1$", "$4$", "$5$", "$10$"], 3, "Turning red litmus blue means the solution is basic, so its pH is above 7.", source=ex(1))
C.mcq("ex.q2", [IP], "A solution reacts with crushed egg-shells to give a gas that turns lime-water milky. The solution contains", [chem("NaCl"), chem("HCl"), chem("LiCl"), chem("KCl")], 1,
      "Egg-shells are calcium carbonate; an acid releases carbon dioxide from them.", "medium", source=ex(2))
C.mcq("ex.q3", [IP], "10 mL of a solution of NaOH is found to be completely neutralised by 8 mL of a given solution of HCl. If we take 20 mL of the same solution of NaOH, the amount of HCl solution (the same solution as before) required to neutralise it will be",
      ["$4$ mL", "$8$ mL", "$12$ mL", "$16$ mL"], 3, "Twice the base needs twice the acid: $2 \\times 8 = 16$ mL.", "medium", source=ex(3))
C.mcq("ex.q4", [PH], "Which one of the following types of medicines is used for treating indigestion?", ["Antibiotic", "Analgesic", "Antacid", "Antiseptic"], 2, "An antacid is a mild base that neutralises the extra acid in the stomach.", source=ex(4))
C.q("ex.q5", "long_answer", 5, [IP], ex(5), "Write word equations and then balanced equations for the reaction taking place when –\n\n(a) dilute sulphuric acid reacts with zinc granules.\n\n(b) dilute hydrochloric acid reacts with magnesium ribbon.\n\n(c) dilute sulphuric acid reacts with aluminium powder.\n\n(d) dilute hydrochloric acid reacts with iron filings.",
    answer_steps=["(a) Zinc + sulphuric acid → zinc sulphate + hydrogen: " + E["zn_h2so4"], "(b) Magnesium + hydrochloric acid → magnesium chloride + hydrogen: " + E["mg_hcl"],
                  "(c) Aluminium + sulphuric acid → aluminium sulphate + hydrogen: " + E["al_h2so4"], "(d) Iron + hydrochloric acid → iron(II) chloride + hydrogen: " + E["fe_hcl"]],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: word equations"])
C.q("ex.q6", "short_answer", 3, [IP], ex(6), "Compounds such as alcohols and glucose also contain hydrogen but are not categorised as acids. Describe an Activity to prove it.",
    answer_steps=["Fix two nails on a cork in a beaker and connect them through a bulb and a 6 V battery.", "Pour dilute HCl into the beaker: the bulb glows. Repeat with glucose solution and with alcohol: the bulb does not glow.",
                  "So acids give ions (H⁺) that conduct electricity, while glucose and alcohol do not give H⁺ ions; they are not acids."], marking_scheme=["1 mark: set-up", "1 mark: observations", "1 mark: conclusion"])
C.q("ex.q7", "very_short_answer", 2, [IP], ex(7), "Why does distilled water not conduct electricity, whereas rain water does?", "easy",
    answer_steps=["Distilled water has almost no ions.", "Rain water dissolves gases such as carbon dioxide and other substances from the air, which form ions, so it conducts electricity."], marking_scheme=MS2)
C.q("ex.q8", "very_short_answer", 2, [IP], ex(8), "Why do acids not show acidic behaviour in the absence of water?", "easy",
    answer_steps=["Acidic behaviour is due to H⁺ ions.", "Acids release H⁺ ions only in water; without water there are no H⁺ ions."], marking_scheme=MS2)
C.q("ex.q9", "short_answer", 3, [PH], ex(9), "Five solutions A, B, C, D and E when tested with universal indicator showed pH as 4, 1, 11, 7 and 9, respectively. Which solution is\n\n(a) neutral?\n\n(b) strongly alkaline?\n\n(c) strongly acidic?\n\n(d) weakly acidic?\n\n(e) weakly alkaline?\n\nArrange the pH in increasing order of hydrogen-ion concentration.",
    answer_steps=["(a) D (pH 7) (b) C (pH 11) (c) B (pH 1)", "(d) A (pH 4) (e) E (pH 9)", "Increasing H⁺ concentration: C (11) < E (9) < D (7) < A (4) < B (1)."],
    marking_scheme=["1 mark: (a) to (c)", "1 mark: (d) and (e)", "1 mark: order"])
C.q("ex.q10", "very_short_answer", 2, [PH], ex(10), "Equal lengths of magnesium ribbons are taken in test tubes A and B. Hydrochloric acid (HCl) is added to test tube A, while acetic acid (CH₃COOH) is added to test tube B. Amount and concentration taken for both the acids are same. In which test tube will the fizzing occur more vigorously and why?",
    answer_steps=["In test tube A.", "HCl is a strong acid and gives many more H⁺ ions than acetic acid, a weak acid, so hydrogen forms faster."], marking_scheme=MS2)
C.q("ex.q11", "very_short_answer", 2, [PH], ex(11), "Fresh milk has a pH of 6. How do you think the pH will change as it turns into curd? Explain your answer.", "easy",
    answer_steps=["The pH will decrease (go below 6).", "Curd contains lactic acid, so the milk becomes more acidic as it sets."], marking_scheme=MS2)
C.q("ex.q12", "very_short_answer", 2, [PH], ex(12), "A milkman adds a very small amount of baking soda to fresh milk.\n\n(a) Why does he shift the pH of the fresh milk from 6 to slightly alkaline?\n\n(b) Why does this milk take a long time to set as curd?",
    answer_steps=["(a) Slightly alkaline milk does not turn sour quickly, so it stays fresh for longer.", "(b) The lactic acid formed must first neutralise the baking soda before the milk can become acidic and set."], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("ex.q13", "very_short_answer", 2, [SL], ex(13), "Plaster of Paris should be stored in a moisture-proof container. Explain why?", "easy",
    answer_steps=["Plaster of Paris reacts with water (moisture) and sets into hard gypsum:", POP_SET], marking_scheme=MS2)
C.q("ex.q14", "short_answer", 3, [IP], ex(14), "What is a neutralisation reaction? Give two examples.",
    answer_steps=["The reaction of an acid with a base to give a salt and water is neutralisation.", "Example: " + E["neutral"], "Example: " + E["mgoh2"] + " (an antacid in the stomach)"],
    marking_scheme=["1 mark: definition", "1 mark: first example", "1 mark: second example"])
C.q("ex.q15", "very_short_answer", 2, [SL], ex(15), "Give two important uses of washing soda and baking soda.", "easy",
    answer_steps=["Washing soda: in glass, soap and paper industries; for removing permanent hardness of water; as a cleaning agent.", "Baking soda: in baking powder for making cakes and bread soft; as an antacid; in soda-acid fire extinguishers."],
    marking_scheme=["1 mark: washing soda", "1 mark: baking soda"])
# CBSE sample paper
C.mcq("sqp20", [IP], "Methyl orange is added to dilute hydrochloric acid and to aqueous sodium hydroxide. What is the colour of the methyl orange in each solution?",
      ["Orange in the acid, red in the base", "Red in the acid, yellow in the base", "Red in the acid, orange in the base", "Yellow in the acid, red in the base"], 1, "Methyl orange is red in acids and yellow in bases.", source=SQP(20))
C.mcq("sqp21", [PH], "Which of the following substances when dissolved in equal volume of water, will have the highest pH value?", ["Sulphuric acid", "Acetic acid", "Magnesium hydroxide", "Sodium hydroxide"], 3,
      "Sodium hydroxide is a strong base: it gives the most OH⁻ ions and the highest pH. Magnesium hydroxide is a weak base.", "medium", source=SQP(21))
C.mcq("sqp22", [IP], "When excess of carbon dioxide is passed through lime water, the milkiness disappears because",
      ["water soluble calcium carbonate converts to water soluble calcium bicarbonate.", "insoluble calcium carbonate converts to water soluble calcium bicarbonate.",
       "water soluble calcium carbonate converts to insoluble calcium bicarbonate.", "insoluble calcium carbonate converts to insoluble calcium bicarbonate."], 1, E["bicarb"], "medium", source=SQP(22))
C.q("sqp28", "case_based", 4, [IP, PH], SQP(28), "Sara took 2 mL of dilute NaOH solution in a test tube and added two drops of phenolphthalein solution. The solution turned pink. She added dilute H₂SO₄ drop by drop until the solution became colourless. "
    "Then she repeated the activity: 2 mL of NaOH needed 20 drops of acid, 3 mL needed 30 drops and 4 mL needed 40 drops.\n\n"
    "A. If Sara used concentrated H₂SO₄ in place of dilute H₂SO₄, will the number of drops needed be 40, less than 40 or more than 40 (for 4 mL of NaOH)? Justify your answer. (1)\n\n"
    "B. Sara measured 20 drops of dilute H₂SO₄ and found its volume to be 1 mL. If she observed the change in colour by using 3 mL of H₂SO₄, how many mL of NaOH did she take? "
    "OR Sara takes 10 drops of dilute H₂SO₄ with two drops of phenolphthalein and adds NaOH dropwise. What change in colour would she observe after 20 drops of NaOH, and why? (2)\n\n"
    "C. Write a balanced chemical equation for the reaction. Is it (a) neutralisation and double displacement, (b) neutralisation and precipitation, (c) precipitation and double displacement, or (d) all three? (1)", "hard",
    answer_steps=["A. Less than 40: concentrated acid gives more H⁺ ions per drop.", "B. 3 mL = 60 drops, and each 10 drops neutralise 1 mL of NaOH, so she took 6 mL of NaOH. OR The colour changes from colourless to pink: once all the acid is neutralised, the solution becomes basic and phenolphthalein turns pink.",
                  "C. " + E["naoh_h2so4"] + ": (a) neutralisation and double displacement. It is not precipitation, because sodium sulphate is soluble."],
    marking_scheme=["A: 1 mark", "B: 2 marks", "C: 1 mark"])
# GSEB
C.mcq("gseb2024_1", [IP], "Which of the following is a synthetic indicator?", ["Phenolphthalein", "Litmus", "Turmeric", "Onion"], 0, "Phenolphthalein is made in the laboratory; litmus, turmeric and onion are natural.", source=gseb(2024, "1"))
C.mcq("gseb2025_2", [IP], "Which of the following is an olfactory indicator?", ["Methyl orange", "Phenolphthalein", "Vanilla", "Turmeric"], 2, "The smell of vanilla essence disappears in a base, so it is an olfactory (smell) indicator.", source=gseb(2025, "2"))
C.q("gseb2024_47", "short_answer", 3, [SL], gseb(2024, "47", 4), "Explain the manufacture of bleaching powder with chemical reactions. Write any two uses of bleaching powder.",
    answer_steps=["Chlorine from the chlor-alkali process (" + E["chloralkali"] + ") is passed over dry slaked lime.", E["bleach"],
                  "Uses: bleaching cotton, linen and wood pulp; disinfecting drinking water; as an oxidising agent in industry."], marking_scheme=["1 mark: chlorine", "1 mark: equation", "1 mark: uses"])
C.q("gseb2024_48", "short_answer", 3, [PH], gseb(2024, "48", 4), "(a) Explain the importance of pH in the human digestive system.\n\n(b) Explain how a change of pH causes tooth decay.",
    answer_steps=["(a) The stomach makes hydrochloric acid for digestion. Too much acid causes pain and irritation (indigestion); an antacid such as milk of magnesia neutralises the extra acid.",
                  "(b) Bacteria in the mouth make acids from sugar and food left after eating. When the pH falls below 5.5, tooth enamel (calcium hydroxyapatite) starts to corrode.",
                  "Brushing with basic toothpaste neutralises the acid and prevents decay."], marking_scheme=["1 mark: (a)", "1 mark: (b) cause", "1 mark: prevention"])
C.q("gseb2025_48", "short_answer", 3, [SL], gseb(2025, "48", 4), "How is plaster of Paris formed? Write an equation to show the reaction between plaster of Paris and water. Write the uses of plaster of Paris.",
    answer_steps=["Gypsum is heated at 373 K: " + POP_FORM, "With water: " + POP_SET, "Uses: plaster for supporting fractured bones, making toys and decorative materials, and making surfaces smooth."],
    marking_scheme=["1 mark: formation", "1 mark: equation", "1 mark: uses"])
# Shine MCQs
C.mcq("mcq01", [IP], "Blue litmus paper is dipped in a solution and turns red. The solution may be:", ["vinegar", "soap solution", "lime water", "baking soda solution"], 0, "Vinegar contains acetic acid; acids turn blue litmus red.")
C.mcq("mcq02", [IP], "Which gas is evolved when sodium hydrogencarbonate reacts with dilute hydrochloric acid?", ["Carbon dioxide", "Hydrogen", "Oxygen", "Chlorine"], 0, E["nahco3"])
C.mcq("mcq03", [PH], "The pH of gastric juice is about:", ["$1.2$", "$7.0$", "$7.4$", "$10$"], 0, "Gastric juice contains hydrochloric acid and is strongly acidic.")
C.mcq("mcq04", [PH], "Tooth decay starts when the pH of the mouth falls below:", ["$5.5$", "$7.5$", "$8.5$", "$3.5$"], 0, "Below pH 5.5, acids start to corrode tooth enamel.")
C.mcq("mcq05", [SL], "The chemical formula of baking soda is:", [chem("NaHCO3"), chem("Na2CO3"), chem("NaOH"), chem("NaCl")], 0, "Baking soda is sodium hydrogencarbonate.")
C.mcq("mcq06", [SL], "In the chlor-alkali process, the gas formed at the anode is:", ["Chlorine", "Hydrogen", "Oxygen", "Carbon dioxide"], 0, "Chlorine forms at the anode and hydrogen at the cathode.", "medium")
C.mcq("mcq07", [SL], "Which salt gives a solution with pH more than 7?", ["Sodium carbonate", "Sodium chloride", "Ammonium chloride", "Potassium sulphate"], 0, "Sodium carbonate comes from a weak acid and a strong base, so its solution is basic.", "medium")
C.mcq("mcq08", [IP], "A bee sting injects methanoic acid. The best first aid is to rub:", ["baking soda", "vinegar", "lemon juice", "common salt"], 0, "Baking soda is a mild base that neutralises the acid.")
C.mcq("mcq09", [SL], "Number of water molecules in one formula unit of gypsum:", ["$2$", "$\\dfrac{1}{2}$", "$5$", "$10$"], 0, "Gypsum is CaSO₄·2H₂O; plaster of Paris has half a molecule; copper sulphate has 5; washing soda has 10.")
C.mcq("mcq10", [IP], "Which oxide will turn red litmus blue when dissolved in water?", ["Calcium oxide", "Carbon dioxide", "Sulphur dioxide", "Phosphorus pentoxide"], 0, "Calcium oxide is a metal oxide, so it is basic.")
# Assertion-reason
C.ar("ar1", [IP], "A solution of glucose does not conduct electricity.", "Glucose does not give ions in water.", 0, "With no ions to carry charge, the solution cannot conduct: R explains A.")
C.ar("ar2", [PH], "A solution of pH 2 is more acidic than one of pH 5.", "The lower the pH, the lower the concentration of hydrogen ions.", 2, "A is true. R is false: a lower pH means a higher concentration of hydrogen ions.")
C.ar("ar3", [SL], "Plaster of Paris is stored in moisture-proof containers.", "Plaster of Paris sets into gypsum when it absorbs water.", 0, "Moisture would turn it into hard gypsum: R explains A.")
C.ar("ar4", [IP], "Water should be added to a concentrated acid for dilution.", "Dilution of a concentrated acid is highly exothermic.", 3, "A is false: acid must be added to water slowly. R is true.")
C.ar("ar5", [SL], "Washing soda is used to remove the permanent hardness of water.", "Baking soda is used in fire extinguishers.", 1, "Both are true, but the use of baking soda does not explain the use of washing soda.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [SL], SHINE, "What is water of crystallisation? Give an example.", "easy",
    answer_steps=["It is the fixed number of water molecules present in one formula unit of a salt crystal.", "Example: copper sulphate, CuSO₄·5H₂O, has five; on heating, " + E["cuso4"]], marking_scheme=["1 mark: definition", "1 mark: example"])
C.q("vsa2", "very_short_answer", 2, [IP], SHINE, "Why does lime water turn milky when carbon dioxide is passed through it, and why does the milkiness disappear when excess gas is passed?", "medium",
    answer_steps=["Insoluble calcium carbonate forms: " + E["limewater"], "With excess carbon dioxide, soluble calcium hydrogencarbonate forms: " + E["bicarb"]], marking_scheme=["1 mark: milky", "1 mark: clear again"])
C.q("sa1", "short_answer", 3, [SL], SHINE, "Starting from common salt, how are (i) sodium hydroxide, (ii) baking soda and (iii) washing soda obtained? Write one equation for each.", "hard",
    answer_steps=["(i) Electrolysis of brine: " + E["chloralkali"], "(ii) " + E["solvay"], "(iii) Heat baking soda: " + E["soda_heat"] + ", then recrystallise: " + E["washing"]],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("sa2", "short_answer", 3, [IP], SHINE, "Explain why metal oxides are called basic oxides and non-metal oxides are called acidic oxides, with one equation each.",
    answer_steps=["Metal oxides react with acids to give a salt and water, like bases: " + E["cuo"], "Non-metal oxides react with bases to give a salt and water, like acids: " + E["limewater"],
                  "So metal oxides are basic and non-metal oxides are acidic."], marking_scheme=["1 mark: metal oxide", "1 mark: non-metal oxide", "1 mark: conclusion"])
C.q("la1", "long_answer", 5, [PH], SHINE, "What is the pH scale? Explain the importance of pH in (i) our digestive system (ii) tooth decay (iii) agriculture (iv) self-defence by animals and plants.", "medium",
    answer_steps=["The pH scale (0 to 14) measures the hydrogen ion concentration: 7 is neutral, below 7 acidic, above 7 basic.", "(i) Extra stomach acid causes indigestion; an antacid such as milk of magnesia neutralises it.",
                  "(ii) Tooth enamel corrodes below pH 5.5; brushing with basic toothpaste neutralises the acids.", "(iii) Plants need a suitable pH; acidic soil is treated with lime or chalk.",
                  "(iv) Bee stings and nettle leaves inject methanoic acid; a base such as baking soda, or the dock leaf, relieves the pain."],
    marking_scheme=["1 mark: pH scale", "1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)"])
C.q("la2", "long_answer", 5, [IP], SHINE, "Describe how acids react with (i) metals (ii) metal carbonates (iii) metal oxides (iv) bases, giving a balanced equation for each. How would you test the gas in (i)?", "medium",
    answer_steps=["(i) " + E["zn_h2so4"], "(ii) " + E["na2co3"], "(iii) " + E["cuo"], "(iv) " + E["neutral"], "The hydrogen in (i) burns with a pop sound near a burning candle."],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)", "1 mark: test"])
C.q("cb1", "case_based", 4, [PH], SHINE,
    "Meera tested five liquids with a universal indicator: lemon juice (pH 2.2), pure water (7), soap solution (10), vinegar (3) and milk of magnesia (10.5).\n\n"
    "(i) Which liquid is neutral? (1)\n\n(ii) Which two liquids are basic? (1)\n\n(iii) Arrange lemon juice, vinegar and pure water in increasing order of hydrogen ion concentration. OR Which liquid would you use to relieve acidity in the stomach, and why? (2)",
    answer_steps=["(i) Pure water.", "(ii) Soap solution and milk of magnesia.", "(iii) Pure water < vinegar < lemon juice (lower pH means more H⁺ ions). OR Milk of magnesia: it is a mild base that neutralises the extra acid."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [SL], SHINE,
    "A doctor puts a white plaster on Ravi's fractured arm. At home, his mother uses washing soda to clean clothes and baking soda to make dhokla soft.\n\n"
    "(i) What is the chemical formula of the substance used for the plaster? (1)\n\n(ii) Why does baking soda make dhokla soft and spongy? (1)\n\n(iii) How is washing soda prepared from baking soda? Write the equations. OR Why must the plaster powder be stored in an airtight container? Write the equation. (2)",
    answer_steps=["(i) Plaster of Paris, $\\mathrm{CaSO_{4} \\cdot \\tfrac{1}{2}H_{2}O}$.", "(ii) On heating or with an acid it gives carbon dioxide, whose bubbles make the batter rise.",
                  "(iii) " + E["soda_heat"] + ", then " + E["washing"] + ". OR It absorbs moisture and sets into gypsum: " + POP_SET],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark equation"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch02.q.ex."))
