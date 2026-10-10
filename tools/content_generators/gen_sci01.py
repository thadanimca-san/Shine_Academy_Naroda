"""CBSE Class 10 Science Ch 1: Chemical Reactions and Equations.
Every chemical equation goes through ce(), which refuses unbalanced ones."""
import sys
from sci_common import Chapter, ce, chem, check, balanced, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch01"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch01_chemical_reactions_and_equations"
C = Chapter("sci10ch01")
blk = C.blk

# Equations used in the chapter (all checked for balance)
E = {k: ce(v) for k, v in {
 "mg": "2Mg(s) + O2(g) -> 2MgO(s)", "zn_acid": "Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g)", "fe_steam": "3Fe(s) + 4H2O(g) -> Fe3O4(s) + 4H2(g)",
 "lime": "CaO(s) + H2O(l) -> Ca(OH)2(aq)", "whitewash": "Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l)", "coal": "C(s) + O2(g) -> CO2(g)",
 "h2o_form": "2H2(g) + O2(g) -> 2H2O(l)", "ch4": "CH4(g) + 2O2(g) -> CO2(g) + 2H2O(g)", "resp": "C6H12O6(aq) + 6O2(g) -> 6CO2(g) + 6H2O(l)",
 "feso4": "2FeSO4(s) -[D]-> Fe2O3(s) + SO2(g) + SO3(g)", "caco3": "CaCO3(s) -[D]-> CaO(s) + CO2(g)", "pbno3": "2Pb(NO3)2(s) -[D]-> 2PbO(s) + 4NO2(g) + O2(g)",
 "electro": "2H2O(l) -> 2H2(g) + O2(g)", "agcl": "2AgCl(s) -> 2Ag(s) + Cl2(g)", "agbr": "2AgBr(s) -> 2Ag(s) + Br2(g)",
 "fe_cu": "Fe(s) + CuSO4(aq) -> FeSO4(aq) + Cu(s)", "zn_cu": "Zn(s) + CuSO4(aq) -> ZnSO4(aq) + Cu(s)", "pb_cu": "Pb(s) + CuCl2(aq) -> PbCl2(aq) + Cu(s)",
 "baso4": "Na2SO4(aq) + BaCl2(aq) -> BaSO4(s) + 2NaCl(aq)", "cu_o": "2Cu + O2 -[D]-> 2CuO", "cuo_h2": "CuO + H2 -[D]-> Cu + H2O",
 "zno_c": "ZnO + C -> Zn + CO", "mno2": "MnO2 + 4HCl -> MnCl2 + 2H2O + Cl2", "pbi2": "Pb(NO3)2(aq) + 2KI(aq) -> PbI2(s) + 2KNO3(aq)",
}.items()}
SKELETAL = ce("Fe + H2O -> Fe3O4 + H2", check_balance=False)
check(not balanced("Fe + H2O -> Fe3O4 + H2"), "the skeletal equation is shown as unbalanced on purpose")

# ---------------------------------------------------------------- learn content
TYPES_TABLE = ("| Type | What happens | Example |\n|---|---|---|\n"
               f"| Combination | Two or more substances form one product | {E['lime']} |\n"
               f"| Decomposition | One substance breaks into two or more | {E['caco3']} |\n"
               f"| Displacement | A more reactive element pushes out a less reactive one | {E['fe_cu']} |\n"
               f"| Double displacement | Two compounds exchange ions | {E['baso4']} |\n"
               f"| Redox | One substance is oxidised while another is reduced | {E['cuo_h2']} |")
sections = [
 {"id": "s1", "title": "Signs of a chemical change", "blocks": [
  blk("s1.hook", "hook", title="What changed?",
    body="Milk turns sour in summer. An iron nail left in damp air turns brown. Food is cooked, digested, and gives us energy when we breathe.\n\n"
         "In each case the substance we started with is gone and something new has formed. That is a **chemical reaction**. In this chapter you will learn to recognise reactions, "
         "write them as balanced chemical equations, and sort them into types."),
  blk("s1.inspiration", "inspiration", title="The father of Indian chemistry", person="Acharya Prafulla Chandra Ray", years="1861–1944",
    body="P. C. Ray taught chemistry at Presidency College, Kolkata. In 1896 he prepared a new compound, **mercurous nitrite**, and went on to study many more.\n\n"
         "He believed India must make its own chemicals and medicines, so in 1901 he founded **Bengal Chemicals and Pharmaceuticals**, one of India's first chemical companies. "
         "He also wrote *A History of Hindu Chemistry*, showing that Indians had practised chemistry since ancient times.",
    quote="Science can wait, but Swaraj cannot.",
    future="Chemists design medicines, fertilisers, cleaner fuels, batteries, paints and plastics, and they test food and water for safety."),
  blk("s1.discovery", "discovery", title="Activities 1.1 to 1.3: watch for the signs",
    body="- **Burn a magnesium ribbon** (with your teacher): it burns with a dazzling white flame and leaves a white powder, magnesium oxide.\n"
         "- **Add potassium iodide solution to lead nitrate solution:** a yellow solid (precipitate) appears.\n"
         "- **Add dilute acid to zinc granules:** bubbles of hydrogen gas form and the flask gets warm.\n\n"
         "So a chemical reaction can be recognised by a **change in state, a change in colour, the evolution of a gas, or a change in temperature**."),
  blk("s1.socratic", "socratic_question", question="Which of these is NOT a sign that a chemical reaction has taken place?",
    options=["Ice melting into water", "A gas being given off", "A change in colour"], correct_index=0,
    explanation="Melting is a physical change: water is still water. No new substance forms."),
 ]},
 {"id": "s2", "title": "Chemical equations", "blocks": [
  blk("s2.reveal", "theory", title="Writing a chemical equation", revision=True,
    body=f"A reaction written in words is a **word equation**: magnesium + oxygen → magnesium oxide. Using formulas, it becomes a **chemical equation**: {E['mg']}\n\n"
         "- Substances on the left are **reactants**; those on the right are **products**. The arrow shows the direction of the reaction.\n"
         "- **State symbols** show the physical state: (s) solid, (l) liquid, (g) gas, (aq) solution in water.\n"
         "- Conditions such as heat are written above the arrow; Δ means heat.\n"
         "- Mass can neither be created nor destroyed, so the number of atoms of each element must be the **same on both sides**: the equation must be **balanced**."),
  blk("s2.eg1", "worked_example", title="Balancing step by step",
    problem=f"Balance the equation for iron reacting with steam: {SKELETAL}",
    steps=["Start with the compound having the most atoms, $\\mathrm{Fe_{3}O_{4}}$: it has 4 oxygen atoms, so take 4 molecules of water.",
           "Now there are 8 hydrogen atoms on the left, so take 4 molecules of hydrogen on the right.",
           "There are 3 iron atoms on the right, so take 3 atoms of iron on the left. Check every element: Fe 3 = 3, O 4 = 4, H 8 = 8."],
    answer=E["fe_steam"]),
  blk("s2.check", "knowledge_check", question=f"In the balanced equation for {ce('H2 + Cl2 -> 2HCl')}, how many molecules of hydrogen chloride form?",
    options=["$2$", "$1$", "$4$", "$3$"], correct_index=0, explanation="One molecule each of hydrogen and chlorine gives two molecules of hydrogen chloride: 2 H and 2 Cl on each side."),
 ]},
 {"id": "s3", "title": "Types of chemical reactions", "blocks": [
  blk("s3.combination", "theory", title="Combination reaction", revision=True,
    body=f"Two or more substances combine to form a single product.\n\n- Quicklime and water (Activity 1.4): {E['lime']} A lot of heat is given out.\n"
         f"- Burning coal: {E['coal']}\n- Forming water: {E['h2o_form']}\n\n"
         "Reactions that give out heat are **exothermic**. Burning natural gas, respiration and the decomposition of vegetable matter into compost are exothermic.\n\n"
         f"The slaked lime used for whitewashing reacts slowly with carbon dioxide in air to form a thin shiny layer of calcium carbonate: {E['whitewash']}"),
  blk("s3.decomposition", "theory", title="Decomposition reaction", revision=True,
    body="A single substance breaks down into two or more simpler substances. It needs energy, so decomposition reactions are usually **endothermic**.\n\n"
         f"- By **heat** (thermal decomposition): {E['feso4']} (green crystals turn brown); {E['caco3']}; {E['pbno3']} (brown fumes of nitrogen dioxide).\n"
         f"- By **electricity** (electrolysis of water): {E['electro']} The volume of hydrogen is double that of oxygen.\n"
         f"- By **light** (in sunlight): {E['agcl']} White silver chloride turns grey. Silver bromide behaves the same way, which is used in black and white photography."),
  blk("s3.displacement", "theory", title="Displacement reaction", revision=True,
    body=f"A more reactive element displaces a less reactive element from its compound.\n\n- An iron nail in copper sulphate solution (Activity 1.9): {E['fe_cu']} "
         "The nail gets a brownish coating of copper and the blue colour fades as pale green iron sulphate forms.\n"
         f"- {E['zn_cu']}\n- {E['pb_cu']}\n\nZinc, lead and iron are more reactive than copper."),
  blk("s3.double", "theory", title="Double displacement reaction", revision=True,
    body=f"Two compounds exchange their ions. Mixing sodium sulphate and barium chloride solutions (Activity 1.10): {E['baso4']}\n\n"
         f"The white insoluble barium sulphate is a **precipitate**, so this is also a **precipitation reaction**. Another example: {E['pbi2']} gives yellow lead iodide."),
  blk("s3.redox", "theory", title="Oxidation and reduction", revision=True,
    body="- **Oxidation:** gain of oxygen or loss of hydrogen.\n- **Reduction:** loss of oxygen or gain of hydrogen.\n\n"
         f"Heating copper powder (Activity 1.11): {E['cu_o']} The brown surface turns black. Passing hydrogen over the hot black copper oxide reverses it: {E['cuo_h2']}\n\n"
         "In the second reaction copper oxide loses oxygen (it is **reduced**) and hydrogen gains oxygen (it is **oxidised**). One substance is oxidised while another is reduced, "
         f"so these are **redox** reactions. More examples: {E['zno_c']} and {E['mno2']}"),
  blk("s3.table", "markdown_table", title="The types at a glance", revision=True, body=TYPES_TABLE),
  blk("s3.check1", "knowledge_check", question=f"The reaction {E['caco3']} is a:",
    options=["decomposition reaction", "combination reaction", "displacement reaction", "double displacement reaction"], correct_index=0,
    explanation="One substance, calcium carbonate, breaks down into two."),
  blk("s3.check2", "knowledge_check", question=f"In {E['cuo_h2']}, the substance that is reduced is:",
    options=[chem("CuO"), chem("H2"), chem("Cu"), chem("H2O")], correct_index=0, explanation="Copper oxide loses oxygen, so it is reduced; hydrogen gains oxygen and is oxidised."),
  blk("s3.memory", "memory_trick", title="Sort it by counting", revision=True,
    body="- **1 product** from many → combination.\n- **1 reactant** into many → decomposition.\n- **Element + compound** → element + compound: displacement.\n"
         "- **Compound + compound** swapping partners → double displacement.\n- **Oxygen in = oxidation; oxygen out = reduction** (and the opposite for hydrogen)."),
 ]},
 {"id": "s4", "title": "Oxidation in everyday life", "blocks": [
  blk("s4.corrosion", "theory", title="Corrosion and rancidity", revision=True,
    body="- **Corrosion:** a metal is slowly attacked by moisture, air or acids around it. Iron gets a reddish-brown coating of **rust**, silver turns black, copper gets a green coating. "
         "Corrosion damages car bodies, bridges, iron railings and ships; painting, oiling and galvanising prevent it.\n"
         "- **Rancidity:** fats and oils in food get oxidised and their smell and taste change. Antioxidants are added, and bags of chips are flushed with **nitrogen**, "
         "an unreactive gas, to slow this oxidation."),
  blk("s4.check", "knowledge_check", question="Why are bags of potato chips filled with nitrogen?",
    options=["To prevent the oil in them from getting oxidised", "To make the chips crisper by heating", "To add flavour", "To make the bag heavier"], correct_index=0,
    explanation="Nitrogen keeps out oxygen, so the oils do not become rancid."),
  blk("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Changing the small numbers inside a formula to balance an equation: change only the coefficients in front.\n"
         "- Forgetting state symbols when the question asks for them.\n"
         "- Calling a reaction 'oxidation' when a substance is reduced at the same time: name both, it is redox.\n"
         "- Mixing up displacement (element + compound) and double displacement (compound + compound).\n"
         "- Writing 'lead is reduced' when it is lead oxide that loses oxygen."),
  blk("s4.tip", "teacher_tip", title="Make the signs visible",
    body="Do Activities 1.2, 1.9 and 1.10 as a quick demonstration with very small amounts. Ask students to write only what they see (colour, gas, heat, solid) before naming the reaction. "
         "Then let pairs balance the equation on mini whiteboards and check each other's atom counts."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  blk("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why we must balance a chemical equation, and why decomposition reactions usually need energy while combination reactions often give it out."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 2, Acids, Bases and Salts:** neutralisation is a double displacement reaction.\n- **Chapter 3, Metals and Non-metals:** the reactivity series explains displacement reactions and corrosion.\n"
         "- **Chapter 5, Life Processes:** respiration is an exothermic reaction inside every cell."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="A student heats green crystals of a salt in a dry boiling tube. The crystals turn white and then brown, and a gas with the smell of burning sulphur is given off.\n\n"
         f"**Answer:** The salt is ferrous sulphate. It first loses its water of crystallisation and then decomposes: {E['feso4']} "
         "The brown solid is ferric oxide and the gases are sulphur dioxide and sulphur trioxide. It is a thermal decomposition, and it is endothermic."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- A complete chemical equation shows the reactants, the products and their states, and it must be balanced.\n"
         "- Combination: one product. Decomposition: one reactant. Displacement: a more reactive element takes the place of a less reactive one. Double displacement: ions are exchanged.\n"
         "- Precipitation reactions give insoluble salts.\n- Exothermic reactions give out heat; endothermic reactions absorb energy.\n"
         "- Oxidation is the gain of oxygen or loss of hydrogen; reduction is the loss of oxygen or gain of hydrogen.\n- Corrosion and rancidity are effects of oxidation in daily life."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Always write balanced equations, with state symbols when asked; an unbalanced equation loses marks.\n"
         "- When asked 'identify the type', give every type that applies (for example: double displacement and precipitation).\n"
         "- Learn the colour changes: green ferrous sulphate to brown, white silver chloride to grey, blue copper sulphate to pale green, yellow lead iodide.\n"
         "- For redox, name the substance oxidised and the substance reduced."),
  blk("s5.flash1", "flashcard", front="Oxidation and reduction (in terms of oxygen)", back="Oxidation: gain of oxygen. Reduction: loss of oxygen."),
  blk("s5.flash2", "flashcard", front="What is a precipitation reaction?", back="A reaction that produces an insoluble substance (a precipitate)."),
  blk("s5.flash3", "flashcard", front="Name the gas used to flush bags of chips", back="Nitrogen"),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Chemical Reactions and Equations",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 1,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: chemical equations, balanced chemical equations and their implications, and the types of chemical reactions: combination, decomposition, displacement, double displacement, precipitation, endothermic and exothermic reactions, oxidation and reduction.",
  "concepts": ["equations", "reaction_types", "redox"], "sections": sections}

# ---------------------------------------------------------------- questions
EQ, TY, RX = "equations", "reaction_types", "redox"
def it(sec, n, part=None):
    s = {"kind": "ncert_intext", "section": sec, "question": n}
    if part: s["part"] = part
    return s
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 1 exercises", "question": n}
MS2 = ["1 mark: answer", "1 mark: reason or equation"]
MS3 = ["1 mark: first part", "1 mark: second part", "1 mark: balanced equation"]

# In-text questions
C.q("it1.q1", "very_short_answer", 2, [EQ], it("1.1", 1), "Why should a magnesium ribbon be cleaned before burning in air?", "easy",
    answer_steps=["A magnesium ribbon gets a layer of magnesium oxide on standing in air.", "Rubbing it with sandpaper removes this layer, so the pure metal can burn properly."], marking_scheme=MS2)
C.q("it1.q2", "short_answer", 3, [EQ], it("1.1", 2), "Write the balanced equation for the following chemical reactions.\n\n(i) Hydrogen + Chlorine → Hydrogen chloride\n\n(ii) Barium chloride + Aluminium sulphate → Barium sulphate + Aluminium chloride\n\n(iii) Sodium + Water → Sodium hydroxide + Hydrogen",
    answer_steps=["(i) " + ce("H2 + Cl2 -> 2HCl"), "(ii) " + ce("3BaCl2 + Al2(SO4)3 -> 3BaSO4 + 2AlCl3"), "(iii) " + ce("2Na + 2H2O -> 2NaOH + H2")],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("it1.q3", "very_short_answer", 2, [EQ], it("1.1", 3), "Write a balanced chemical equation with state symbols for the following reactions.\n\n(i) Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate and the solution of sodium chloride.\n\n"
    "(ii) Sodium hydroxide solution (in water) reacts with hydrochloric acid solution (in water) to produce sodium chloride solution and water.",
    answer_steps=["(i) " + ce("BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)"), "(ii) " + ce("NaOH(aq) + HCl(aq) -> NaCl(aq) + H2O(l)")], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
C.q("it2.q1", "very_short_answer", 2, [TY], it("1.2", 1), "A solution of a substance 'X' is used for whitewashing.\n\n(i) Name the substance 'X' and write its formula.\n\n(ii) Write the reaction of the substance 'X' named in (i) above with water.", "easy",
    answer_steps=["(i) X is calcium oxide (quicklime), " + chem("CaO") + ".", "(ii) " + E["lime"] + " (slaked lime forms and heat is given out)."], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
C.q("it2.q2", "very_short_answer", 2, [TY], it("1.2", 2), "Why is the amount of gas collected in one of the test tubes in Activity 1.7 double of the amount collected in the other? Name this gas.",
    answer_steps=["Water is broken down by electricity: " + E["electro"], "Each water molecule gives two hydrogen atoms for one oxygen atom, so the volume of hydrogen is double that of oxygen. The gas is hydrogen."], marking_scheme=MS2)
C.q("it3.q1", "very_short_answer", 2, [TY], it("1.3", 1), "Why does the colour of copper sulphate solution change when an iron nail is dipped in it?", "easy",
    answer_steps=["Iron is more reactive than copper, so it displaces copper: " + E["fe_cu"], "Blue copper sulphate is used up and pale green iron sulphate forms, so the colour changes."], marking_scheme=MS2)
C.q("it3.q2", "very_short_answer", 2, [TY], it("1.3", 2), "Give an example of a double displacement reaction other than the one given in Activity 1.10.", "easy",
    answer_steps=["Lead nitrate and potassium iodide exchange ions:", E["pbi2"] + " (a yellow precipitate of lead iodide forms)."], marking_scheme=MS2)
C.q("it3.q3", "very_short_answer", 2, [RX], it("1.3", 3), f"Identify the substances that are oxidised and the substances that are reduced in the following reactions.\n\n(i) {ce('4Na(s) + O2(g) -> 2Na2O(s)')}\n\n(ii) {ce('CuO(s) + H2(g) -> Cu(s) + H2O(l)')}",
    answer_steps=["(i) Sodium gains oxygen, so sodium is oxidised and oxygen is reduced.", "(ii) Copper oxide loses oxygen, so it is reduced; hydrogen gains oxygen, so it is oxidised."], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
# Exercises
C.mcq("ex.q1", [RX], f"Which of the statements about the reaction below are incorrect?\n\n{ce('2PbO(s) + C(s) -> 2Pb(s) + CO2(g)')}\n\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.",
      ["(a) and (b)", "(a) and (c)", "(a), (b) and (c)", "all"], 0, "Lead oxide (not lead) is reduced, and carbon dioxide is a product, not something being oxidised. So (a) and (b) are incorrect; (c) and (d) are correct.", "medium", source=ex(1))
C.mcq("ex.q2", [TY], f"{ce('Fe2O3 + 2Al -> Al2O3 + 2Fe')}\n\nThe above reaction is an example of a", ["combination reaction.", "double displacement reaction.", "decomposition reaction.", "displacement reaction."], 3,
      "Aluminium, an element, displaces iron from its oxide.", source=ex(2))
C.mcq("ex.q3", [TY], "What happens when dilute hydrochloric acid is added to iron filings?", ["Hydrogen gas and iron chloride are produced.", "Chlorine gas and iron hydroxide are produced.", "No reaction takes place.", "Iron salt and water are produced."], 0,
      "Iron displaces hydrogen from the acid: " + ce("Fe + 2HCl -> FeCl2 + H2"), source=ex(3))
C.q("ex.q4", "very_short_answer", 2, [EQ], ex(4), "What is a balanced chemical equation? Why should chemical equations be balanced?", "easy",
    answer_steps=["A balanced chemical equation has the same number of atoms of each element on the reactant and product sides.", "Mass can neither be created nor destroyed in a reaction (law of conservation of mass), so the equation must be balanced."], marking_scheme=MS2)
C.q("ex.q5", "long_answer", 5, [EQ], ex(5), "Translate the following statements into chemical equations and then balance them.\n\n(a) Hydrogen gas combines with nitrogen to form ammonia.\n\n(b) Hydrogen sulphide gas burns in air to give water and sulphur dioxide.\n\n"
    "(c) Barium chloride reacts with aluminium sulphate to give aluminium chloride and a precipitate of barium sulphate.\n\n(d) Potassium metal reacts with water to give potassium hydroxide and hydrogen gas.", "medium",
    answer_steps=["(a) " + ce("3H2(g) + N2(g) -> 2NH3(g)"), "(b) " + ce("2H2S(g) + 3O2(g) -> 2H2O(l) + 2SO2(g)"), "(c) " + ce("3BaCl2(aq) + Al2(SO4)3(aq) -> 2AlCl3(aq) + 3BaSO4(s)"),
                  "(d) " + ce("2K(s) + 2H2O(l) -> 2KOH(aq) + H2(g)")],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: correct formulas throughout"])
C.q("ex.q6", "short_answer", 3, [EQ], ex(6), f"Balance the following chemical equations.\n\n(a) {ce('HNO3 + Ca(OH)2 -> Ca(NO3)2 + H2O', False)}\n\n(b) {ce('NaOH + H2SO4 -> Na2SO4 + H2O', False)}\n\n(c) {ce('NaCl + AgNO3 -> AgCl + NaNO3')}\n\n(d) {ce('BaCl2 + H2SO4 -> BaSO4 + HCl', False)}",
    answer_steps=["(a) " + ce("2HNO3 + Ca(OH)2 -> Ca(NO3)2 + 2H2O"), "(b) " + ce("2NaOH + H2SO4 -> Na2SO4 + 2H2O"), "(c) " + ce("NaCl + AgNO3 -> AgCl + NaNO3") + " (already balanced)", "(d) " + ce("BaCl2 + H2SO4 -> BaSO4 + 2HCl")],
    marking_scheme=["1 mark: (a) and (b)", "1 mark: (c)", "1 mark: (d)"])
C.q("ex.q7", "short_answer", 3, [EQ], ex(7), "Write the balanced chemical equations for the following reactions.\n\n(a) Calcium hydroxide + Carbon dioxide → Calcium carbonate + Water\n\n(b) Zinc + Silver nitrate → Zinc nitrate + Silver\n\n(c) Aluminium + Copper chloride → Aluminium chloride + Copper\n\n(d) Barium chloride + Potassium sulphate → Barium sulphate + Potassium chloride",
    answer_steps=["(a) " + ce("Ca(OH)2 + CO2 -> CaCO3 + H2O"), "(b) " + ce("Zn + 2AgNO3 -> Zn(NO3)2 + 2Ag"), "(c) " + ce("2Al + 3CuCl2 -> 2AlCl3 + 3Cu"), "(d) " + ce("BaCl2 + K2SO4 -> BaSO4 + 2KCl")],
    marking_scheme=["1 mark: (a) and (b)", "1 mark: (c)", "1 mark: (d)"])
C.q("ex.q8", "long_answer", 5, [EQ, TY], ex(8), "Write the balanced chemical equation for the following and identify the type of reaction in each case.\n\n(a) Potassium bromide(aq) + Barium iodide(aq) → Potassium iodide(aq) + Barium bromide(s)\n\n(b) Zinc carbonate(s) → Zinc oxide(s) + Carbon dioxide(g)\n\n"
    "(c) Hydrogen(g) + Chlorine(g) → Hydrogen chloride(g)\n\n(d) Magnesium(s) + Hydrochloric acid(aq) → Magnesium chloride(aq) + Hydrogen(g)", "medium",
    answer_steps=["(a) " + ce("2KBr(aq) + BaI2(aq) -> 2KI(aq) + BaBr2(s)") + ": double displacement (and precipitation)", "(b) " + ce("ZnCO3(s) -[D]-> ZnO(s) + CO2(g)") + ": decomposition",
                  "(c) " + ce("H2(g) + Cl2(g) -> 2HCl(g)") + ": combination", "(d) " + ce("Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)") + ": displacement"],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: types named correctly"])
C.q("ex.q9", "short_answer", 3, [TY], ex(9), "What does one mean by exothermic and endothermic reactions? Give examples.",
    answer_steps=["Exothermic reactions give out heat, for example burning natural gas: " + E["ch4"], "Endothermic reactions absorb energy, for example the decomposition of calcium carbonate: " + E["caco3"],
                  "Respiration is exothermic; photosynthesis and the decomposition of silver chloride in sunlight absorb energy."],
    marking_scheme=["1 mark: exothermic with example", "1 mark: endothermic with example", "1 mark: equations"])
C.q("ex.q10", "very_short_answer", 2, [TY], ex(10), "Why is respiration considered an exothermic reaction? Explain.", "easy",
    answer_steps=["In respiration, glucose combines with oxygen in our cells: " + E["resp"], "Energy is released in this reaction, so it is exothermic."], marking_scheme=MS2)
C.q("ex.q11", "short_answer", 3, [TY], ex(11), "Why are decomposition reactions called the opposite of combination reactions? Write equations for these reactions.",
    answer_steps=["In a combination reaction, two or more substances form one product; in a decomposition reaction, one substance breaks into two or more.", "Combination: " + E["lime"],
                  "Decomposition: " + E["caco3"]], marking_scheme=["1 mark: explanation", "1 mark: combination equation", "1 mark: decomposition equation"])
C.q("ex.q12", "short_answer", 3, [TY], ex(12), "Write one equation each for decomposition reactions where energy is supplied in the form of heat, light or electricity.",
    answer_steps=["Heat: " + E["caco3"], "Light: " + E["agcl"], "Electricity: " + E["electro"]], marking_scheme=["1 mark: heat", "1 mark: light", "1 mark: electricity"])
C.q("ex.q13", "short_answer", 3, [TY], ex(13), "What is the difference between displacement and double displacement reactions? Write equations for these reactions.",
    answer_steps=["In a displacement reaction a more reactive element displaces a less reactive element from its compound: " + E["fe_cu"],
                  "In a double displacement reaction two compounds exchange ions: " + E["baso4"], "So displacement involves an element and a compound; double displacement involves two compounds."],
    marking_scheme=["1 mark: displacement", "1 mark: double displacement", "1 mark: difference"])
C.q("ex.q14", "very_short_answer", 2, [TY], ex(14), "In the refining of silver, the recovery of silver from silver nitrate solution involved displacement by copper metal. Write down the reaction involved.", "easy",
    answer_steps=[ce("Cu(s) + 2AgNO3(aq) -> Cu(NO3)2(aq) + 2Ag(s)"), "Copper is more reactive than silver, so it displaces silver."], marking_scheme=MS2)
C.q("ex.q15", "short_answer", 3, [TY], ex(15), "What do you mean by a precipitation reaction? Explain by giving examples.",
    answer_steps=["A reaction in which an insoluble substance (precipitate) forms is a precipitation reaction.", "Example: " + E["baso4"] + " (white precipitate)", "Example: " + E["pbi2"] + " (yellow precipitate)"],
    marking_scheme=["1 mark: definition", "1 mark: first example", "1 mark: second example"])
C.q("ex.q16", "short_answer", 3, [RX], ex(16), "Explain the following in terms of gain or loss of oxygen with two examples each.\n\n(a) Oxidation\n\n(b) Reduction",
    answer_steps=["(a) Oxidation is the gain of oxygen: " + E["cu_o"] + " (copper is oxidised); " + E["coal"] + " (carbon is oxidised).",
                  "(b) Reduction is the loss of oxygen: " + E["cuo_h2"] + " (copper oxide is reduced); " + E["zno_c"] + " (zinc oxide is reduced).",
                  "In each pair, one substance is oxidised while the other is reduced."], marking_scheme=["1 mark: oxidation with examples", "1 mark: reduction with examples", "1 mark: naming what is oxidised and reduced"])
C.q("ex.q17", "very_short_answer", 2, [RX], ex(17), "A shiny brown coloured element 'X' on heating in air becomes black in colour. Name the element 'X' and the black coloured compound formed.", "easy",
    answer_steps=["X is copper; the black compound is copper(II) oxide, " + chem("CuO") + ".", E["cu_o"]], marking_scheme=MS2)
C.q("ex.q18", "very_short_answer", 2, [RX], ex(18), "Why do we apply paint on iron articles?", "easy",
    answer_steps=["Iron rusts when it is exposed to moist air.", "Paint keeps air and moisture away from the iron, so it prevents rusting (corrosion)."], marking_scheme=MS2)
C.q("ex.q19", "very_short_answer", 2, [RX], ex(19), "Oil and fat containing food items are flushed with nitrogen. Why?", "easy",
    answer_steps=["Oxygen in air oxidises oils and fats, making the food rancid (bad smell and taste).", "Nitrogen is unreactive and keeps oxygen away, so it prevents rancidity."], marking_scheme=MS2)
C.q("ex.q20", "short_answer", 3, [RX], ex(20), "Explain the following terms with one example each.\n\n(a) Corrosion\n\n(b) Rancidity",
    answer_steps=["(a) Corrosion: a metal is slowly eaten away by moisture, air or acids. Example: iron gets a reddish-brown coating of rust; silver turns black.",
                  "(b) Rancidity: fats and oils in food get oxidised, changing their smell and taste. Example: chips or butter kept open for a long time.", "Painting prevents corrosion; nitrogen or antioxidants prevent rancidity."],
    marking_scheme=["1 mark: corrosion with example", "1 mark: rancidity with example", "1 mark: prevention"])
# CBSE sample paper
C.mcq("sqp17", [RX, EQ], "Which of the following equations represent redox reactions and what are the values for 'p' and 'q' in these equations?\n\nEquation 1: $\\mathrm{Fe_{2}O_{3}(s) + 2Al(s) \\rightarrow Al_{2}O_{3}(s) + p\\,Fe(l)}$ + heat\n\n"
      "Equation 2: $\\mathrm{2C_{4}H_{10}(g) + 13O_{2}(g) \\xrightarrow{\\Delta} 8CO_{2}(g) + q\\,H_{2}O(g)}$",
      ["Only equation 1 is a redox reaction, p = 1 and q = 3", "Both equations 1 and 2 are redox reactions, p = 2 and q = 4", "Only equation 2 is a redox reaction, p = 2 and q = 10", "Both equations 1 and 2 are redox reactions, p = 2 and q = 10"], 3,
      "Balancing gives p = 2 (2 Fe atoms) and q = 10 (20 H atoms). In both, one substance gains oxygen while another loses it or burns, so both are redox reactions.", "hard", source=SQP(17))
check(balanced("Fe2O3 + 2Al -> Al2O3 + 2Fe") and balanced("2C4H10 + 13O2 -> 8CO2 + 10H2O"), "sqp17 p and q")
C.mcq("sqp23", [TY], "In the reaction of aqueous solution of barium chloride with aqueous solution of sodium sulphate, the aqueous solution formed will be:", [chem("BaCl2"), chem("BaSO4"), chem("Na2SO4"), chem("NaCl")], 3,
      "Barium sulphate is the insoluble precipitate; sodium chloride stays dissolved: " + E["baso4"], "medium", source=SQP(23))
C.q("sqp27", "short_answer", 3, [TY], SQP(27), "Amrita set up an electrolysis apparatus with distilled water, expecting two gases to be evolved at the anode and the cathode. She realised that the bulb in the circuit did not glow when she used distilled water. "
    "She then added a substance to the distilled water so that electrolysis could take place.\n\nA. Which gas was she expecting to be formed at the anode and which one at the cathode?\n\nB. Why did the bulb not glow when Amrita passed electricity through distilled water?\n\n"
    "C. Which substance was added by Amrita to distilled water to get the expected result?",
    answer_steps=["A. Oxygen at the anode and hydrogen at the cathode.", "B. Distilled water is a poor conductor of electricity: it has almost no ions.", "C. A few drops of dilute sulphuric acid (or some sodium chloride, any strong electrolyte)."],
    marking_scheme=["1 mark: A", "1 mark: B", "1 mark: C"])
C.q("sqp27vi", "short_answer", 3, [TY, RX], SQP("27 (for visually impaired students)"), f"Identify the type of reaction:\n\nA. {ce('ZnO + C -> Zn + CO')}\n\nB. {ce('ZnCO3 -[D]-> ZnO + CO2')}\n\nC. {ce('2Mg + O2 -> 2MgO')} + heat",
    answer_steps=["A. Redox reaction (zinc oxide is reduced, carbon is oxidised).", "B. Decomposition reaction; it is endothermic.", "C. Combination reaction; it is exothermic."], marking_scheme=["1 mark: A", "1 mark: B", "1 mark: C"])
# GSEB board papers
C.q("gseb2024_38", "short_answer", 3, [TY], pyq_gseb(2024, "38"), "Silver chloride is kept in a china dish in sunlight.\n\n(a) Identify the type of chemical reaction and define it.\n\n(b) Write the change in colour of the salt placed in the china dish.\n\n(c) Write the balanced chemical equation of the reaction.",
    answer_steps=["(a) Decomposition reaction (by light): a single substance breaks down into two or more simpler substances.", "(b) White silver chloride turns grey.", "(c) " + E["agcl"]],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
C.q("gseb2025_38", "short_answer", 3, [TY], pyq_gseb(2025, "38"), "What is a combination reaction? Explain with two examples.",
    answer_steps=["In a combination reaction, two or more substances combine to form a single product.", "Example: " + E["lime"], "Example: " + E["coal"]],
    marking_scheme=["1 mark: definition", "1 mark: first example", "1 mark: second example"])
# Shine MCQs
C.mcq("mcq01", [EQ], "Which state symbol shows a solution in water?", ["(aq)", "(l)", "(s)", "(g)"], 0, "(aq) stands for aqueous: dissolved in water.")
C.mcq("mcq02", [TY], "When quicklime reacts with water, the reaction is:", ["combination and exothermic", "decomposition and endothermic", "displacement and exothermic", "combination and endothermic"], 0,
      "Calcium oxide and water combine into one product and give out a lot of heat.", "medium")
C.mcq("mcq03", [TY], "On heating, green ferrous sulphate crystals give a smell of burning sulphur. The residue is:", ["brown ferric oxide", "white ferrous oxide", "black copper oxide", "green ferrous sulphate"], 0,
      "Ferrous sulphate decomposes into ferric oxide (brown), sulphur dioxide and sulphur trioxide.", "medium")
C.mcq("mcq04", [TY], "In the electrolysis of water, the ratio of the volumes of hydrogen and oxygen collected is:", ["$2 : 1$", "$1 : 2$", "$1 : 1$", "$8 : 1$"], 0, "Water has two hydrogen atoms for every oxygen atom.")
C.mcq("mcq05", [TY], "Silver bromide is used in black and white photography because it:", ["decomposes in light", "combines with oxygen", "dissolves in water", "is a good conductor"], 0, "Light decomposes silver bromide into silver and bromine.")
C.mcq("mcq06", [TY], "A yellow precipitate forms when lead nitrate solution is mixed with:", ["potassium iodide solution", "sodium chloride solution", "copper sulphate solution", "water"], 0, "Lead iodide, the yellow precipitate, forms by double displacement.")
C.mcq("mcq07", [RX], "Which of these is an oxidation?", ["Copper turning into copper oxide on heating", "Copper oxide turning into copper with hydrogen", "Ice melting", "Salt dissolving in water"], 0, "Copper gains oxygen when it forms copper oxide.")
C.mcq("mcq08", [TY], "Which metal can displace copper from copper sulphate solution?", ["Zinc", "Silver", "Gold", "Platinum"], 0, "Zinc is more reactive than copper; silver, gold and platinum are less reactive.", "medium")
C.mcq("mcq09", [EQ], f"To balance {ce('Na + H2O -> NaOH + H2', False)}, the coefficients are:", ["2, 2, 2, 1", "1, 1, 1, 1", "2, 1, 2, 1", "1, 2, 1, 2"], 0, "Balanced: " + ce("2Na + 2H2O -> 2NaOH + H2"), "medium")
C.mcq("mcq10", [RX], "The black coating on silver articles is an example of:", ["corrosion", "rancidity", "precipitation", "decomposition"], 0, "Silver reacts slowly with sulphur compounds in air and gets a black coating: corrosion.")
# Assertion-reason
C.ar("ar1", [EQ], "A chemical equation must be balanced.", "Mass can neither be created nor destroyed in a chemical reaction.", 0, "Because mass is conserved, the atoms on both sides must be equal: R explains A.")
C.ar("ar2", [TY], "The reaction of zinc with copper sulphate solution is a displacement reaction.", "Copper is more reactive than zinc.", 2, "A is true. R is false: zinc is more reactive than copper, which is why it displaces copper.")
C.ar("ar3", [TY], "Decomposition of calcium carbonate is an endothermic reaction.", "Calcium oxide is used in the manufacture of cement.", 1, "Both are true, but the use of calcium oxide does not explain why the decomposition absorbs heat.")
C.ar("ar4", [RX], "In the reaction of copper oxide with hydrogen, copper oxide is oxidised.", "Reduction is the loss of oxygen.", 3, "A is false: copper oxide loses oxygen, so it is reduced. R is true.")
C.ar("ar5", [RX], "Food items with oils are packed with nitrogen gas.", "Nitrogen prevents the oxidation of oils and fats.", 0, "Nitrogen keeps oxygen out, so rancidity is prevented: R explains A.")
# Written Shine questions
C.q("vsa1", "very_short_answer", 2, [EQ], SHINE, "Balance the equation: " + ce("Al + O2 -> Al2O3", False), "easy",
    answer_steps=[ce("4Al + 3O2 -> 2Al2O3"), "Check: Al 4 = 4, O 6 = 6."], marking_scheme=["1 mark: coefficients", "1 mark: check"])
C.q("vsa2", "very_short_answer", 2, [TY], SHINE, "Why does a lead nitrate crystal give off brown fumes on heating? Write the equation.", "medium",
    answer_steps=["Lead nitrate decomposes on heating and gives nitrogen dioxide, a brown gas:", E["pbno3"]], marking_scheme=MS2)
C.q("sa1", "short_answer", 3, [TY], SHINE, "A student dips an iron nail in copper sulphate solution and a zinc rod in iron sulphate solution. What does she observe in each case after 20 minutes? Write the equations.", "medium",
    answer_steps=["Iron nail: a brown coating of copper forms and the blue solution turns pale green. " + E["fe_cu"],
                  "Zinc rod: zinc is more reactive than iron, so it displaces iron; the pale green solution becomes colourless. " + ce("Zn(s) + FeSO4(aq) -> ZnSO4(aq) + Fe(s)"),
                  "Both are displacement reactions."], marking_scheme=["1 mark: first observation and equation", "1 mark: second observation and equation", "1 mark: type"])
C.q("sa2", "short_answer", 3, [RX], SHINE, f"In the reaction {E['mno2']}, name the substance (i) oxidised (ii) reduced (iii) the oxidising agent.", "hard",
    answer_steps=["(i) HCl is oxidised: it loses hydrogen and gives chlorine.", "(ii) MnO₂ is reduced: it loses oxygen.", "(iii) MnO₂ is the oxidising agent, because it oxidises HCl."],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("la1", "long_answer", 5, [TY], SHINE, "Describe an activity to show the electrolysis of water. Which gas collects at each electrode, and in what ratio? Why are a few drops of dilute sulphuric acid added? How will you test the gases?", "medium",
    answer_steps=["Fill a plastic mug with water, fix two carbon electrodes through its base and connect them to a 6 V battery. Invert two test tubes filled with water over the electrodes.",
                  "Add a few drops of dilute sulphuric acid: pure water conducts electricity very poorly.", "Bubbles form at both electrodes: hydrogen at the cathode (negative) and oxygen at the anode (positive).",
                  "The volume of hydrogen is double that of oxygen: " + E["electro"], "Hydrogen burns with a pop sound near a burning candle; oxygen makes a glowing splinter burst into flame."],
    marking_scheme=["1 mark: set-up", "1 mark: acid", "1 mark: gases at electrodes", "1 mark: ratio and equation", "1 mark: tests"])
C.q("la2", "long_answer", 5, [TY, RX], SHINE, "Give one example each, with a balanced equation, of (i) a combination reaction (ii) a thermal decomposition (iii) a displacement reaction (iv) a precipitation reaction (v) a redox reaction.", "medium",
    answer_steps=["(i) " + E["lime"], "(ii) " + E["caco3"], "(iii) " + E["zn_cu"], "(iv) " + E["baso4"], "(v) " + E["zno_c"] + " (ZnO reduced, C oxidised)"],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)", "1 mark: (v)"])
C.q("cb1", "case_based", 4, [RX], SHINE,
    "Rohan's grandmother keeps her old silver anklets in a cupboard. After a few months they look black. His mother says that the iron gate also needs painting before the monsoon, and that chips must be kept in sealed packets.\n\n"
    "(i) What is the black coating on silver called, and what process causes it? (1)\n\n(ii) Why is the iron gate painted before the monsoon? (1)\n\n(iii) What happens to chips kept in an open packet for many days, and how do manufacturers prevent it? OR Name the green coating that forms on copper and explain why it is an example of corrosion. (2)",
    answer_steps=["(i) Silver sulphide; it is corrosion (tarnishing) caused by sulphur compounds in air.", "(ii) Paint keeps moisture and air away, so the iron does not rust.",
                  "(iii) The oils get oxidised and the chips become rancid (bad smell and taste); packets are flushed with nitrogen and antioxidants are added. OR Basic copper carbonate; copper is slowly attacked by moist carbon dioxide in air, which is corrosion."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark reason, 1 mark prevention"])
C.q("cb2", "case_based", 4, [TY], SHINE,
    "In a school laboratory, students mixed solutions in three test tubes:\n\nTest tube A: lead nitrate + potassium iodide\n\nTest tube B: sodium sulphate + barium chloride\n\nTest tube C: copper sulphate + an iron nail\n\n"
    "(i) In which test tube does a yellow precipitate form? (1)\n\n(ii) Name the white precipitate formed in test tube B. (1)\n\n(iii) Write the balanced equation for test tube C and state the type of reaction. OR Write the balanced equation for test tube A and state two types of reaction it belongs to. (2)",
    answer_steps=["(i) Test tube A (lead iodide).", "(ii) Barium sulphate.", "(iii) " + E["fe_cu"] + ": displacement reaction. OR " + E["pbi2"] + ": double displacement and precipitation reaction."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark equation, 1 mark type"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch01.q.ex."))
