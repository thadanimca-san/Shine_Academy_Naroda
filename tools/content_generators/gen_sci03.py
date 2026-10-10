"""CBSE Class 10 Science Ch 3: Metals and Non-metals.
Molecular equations go through ce(), which refuses unbalanced ones; equations
with ions or electrons are written by hand."""
import sys
from sci_common import Chapter, ce, chem, check, balanced, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch03"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch03_metals_and_non_metals"
C = Chapter("sci10ch03")
blk = C.blk

E = {k: ce(v) for k, v in {
 "cu_o2": "2Cu + O2 -> 2CuO", "al_o2": "4Al + 3O2 -> 2Al2O3", "na_o2": "4Na(s) + O2(g) -> 2Na2O(s)", "mg_o2": "2Mg + O2 -> 2MgO",
 "al2o3_hcl": "Al2O3 + 6HCl -> 2AlCl3 + 3H2O", "al2o3_naoh": "Al2O3 + 2NaOH -> 2NaAlO2 + H2O", "na2o_h2o": "Na2O(s) + H2O(l) -> 2NaOH(aq)",
 "k_h2o": "2K(s) + 2H2O(l) -> 2KOH(aq) + H2(g)", "na_h2o": "2Na(s) + 2H2O(l) -> 2NaOH(aq) + H2(g)", "ca_h2o": "Ca(s) + 2H2O(l) -> Ca(OH)2(aq) + H2(g)",
 "al_steam": "2Al(s) + 3H2O(g) -> Al2O3(s) + 3H2(g)", "fe_steam": "3Fe(s) + 4H2O(g) -> Fe3O4(s) + 4H2(g)", "fe_h2so4": "Fe(s) + H2SO4(aq) -> FeSO4(aq) + H2(g)",
 "zn_feso4": "Zn(s) + FeSO4(aq) -> ZnSO4(aq) + Fe(s)", "cu_agno3": "Cu(s) + 2AgNO3(aq) -> Cu(NO3)2(aq) + 2Ag(s)", "fe_cuso4": "Fe(s) + CuSO4(aq) -> FeSO4(aq) + Cu(s)",
 "hgs": "2HgS(s) + 3O2(g) -[D]-> 2HgO(s) + 2SO2(g)", "hgo": "2HgO(s) -[D]-> 2Hg(l) + O2(g)", "cu2s": "2Cu2S + 3O2 -[D]-> 2Cu2O + 2SO2", "cu2o": "2Cu2O + Cu2S -[D]-> 6Cu + SO2",
 "zns": "2ZnS(s) + 3O2(g) -[D]-> 2ZnO(s) + 2SO2(g)", "znco3": "ZnCO3(s) -[D]-> ZnO(s) + CO2(g)", "zno_c": "ZnO(s) + C(s) -> Zn(s) + CO(g)",
 "thermite": "Fe2O3(s) + 2Al(s) -> 2Fe(l) + Al2O3(s)", "mno2_al": "3MnO2(s) + 4Al(s) -> 3Mn(l) + 2Al2O3(s)", "s_o2": "S(s) + O2(g) -> SO2(g)",
 "so2_h2o": "SO2(g) + H2O(l) -> H2SO3(aq)", "zn_cuo": "Zn + CuO -> ZnO + Cu", "mg_zno": "Mg + ZnO -> MgO + Zn", "mg_cuo": "Mg + CuO -> MgO + Cu",
 "zn_hcl": "Zn + 2HCl -> ZnCl2 + H2", "mg_hcl": "Mg + 2HCl -> MgCl2 + H2", "na_cl2": "2Na + Cl2 -> 2NaCl", "mg_h2o": "Mg(s) + 2H2O(l) -> Mg(OH)2(aq) + H2(g)",
}.items()}
NA_ION = "$\\mathrm{Na \\rightarrow Na^{+} + e^{-}}$"; CL_ION = "$\\mathrm{Cl + e^{-} \\rightarrow Cl^{-}}$"
MG_ION = "$\\mathrm{Mg \\rightarrow Mg^{2+} + 2e^{-}}$"; O_ION = "$\\mathrm{O + 2e^{-} \\rightarrow O^{2-}}$"
NA_CATH = "$\\mathrm{Na^{+} + e^{-} \\rightarrow Na}$"; CL_AN = "$\\mathrm{2Cl^{-} \\rightarrow Cl_{2} + 2e^{-}}$"

SERIES = ("| Metal | Symbol | Reactivity |\n|---|---|---|\n| Potassium | K | most reactive |\n| Sodium | Na | |\n| Calcium | Ca | |\n| Magnesium | Mg | |\n| Aluminium | Al | |\n"
          "| Zinc | Zn | |\n| Iron | Fe | |\n| Lead | Pb | |\n| [Hydrogen] | [H] | |\n| Copper | Cu | |\n| Mercury | Hg | |\n| Silver | Ag | |\n| Gold | Au | least reactive |")
COMPARE = ("| Property | Metals | Non-metals |\n|---|---|---|\n| Lustre | shiny | dull (iodine is an exception) |\n| Malleability and ductility | yes | no: brittle |\n"
           "| Conduction of heat and electricity | good | poor (graphite conducts electricity) |\n| State at room temperature | solid (mercury is a liquid) | solid, liquid (bromine) or gas |\n"
           "| Oxides | basic (some amphoteric) | acidic or neutral |\n| Ions | positive (lose electrons) | negative (gain electrons) |")
IONIC_MP = ("| Ionic compound | Melting point (K) | Boiling point (K) |\n|---|---|---|\n| NaCl | $1074$ | $1686$ |\n| LiCl | $887$ | $1600$ |\n| CaCl₂ | $1045$ | $1900$ |\n"
            "| CaO | $2850$ | $3120$ |\n| MgCl₂ | $981$ | $1685$ |")

sections = [
 {"id": "s1", "title": "Two kinds of elements", "blocks": [
  blk("s1.hook", "hook", title="Why are wires made of copper?",
    body="A gold ring still shines after a hundred years, but an iron nail rusts in a few weeks. Electric wires are made of copper or aluminium, but never of sulphur. A spoon can be hammered flat; a piece of coal breaks.\n\n"
         "Elements behave so differently because some are **metals** and some are **non-metals**. In this chapter you will study their properties, how they react, how metals are taken out of their ores, and how corrosion can be stopped."),
  blk("s1.inspiration", "inspiration", title="The pillar that does not rust", person="The iron-smiths of ancient India", years="about 1600 years ago",
    body="The **Iron Pillar** at the Qutub complex in Delhi is about 7 metres tall and was made in the Gupta period, roughly 1600 years ago. In all this time it has hardly rusted. "
         "Studies show that a thin protective film forms on its surface because of the way the iron was made.\n\n"
         "Indian metal workers were also famous for **wootz steel**, which was traded far and wide, and zinc was produced by distillation at Zawar in Rajasthan centuries ago.",
    quote="Knowing how materials behave lets us build things that last.",
    future="Metallurgists and materials scientists make stronger steels, lighter alloys for aircraft, rust-proof bridges, batteries and electronic chips."),
  blk("s1.socratic", "socratic_question", question="Which property tells you most simply that a sample is a metal?",
    options=["It conducts electricity well", "It is a solid", "It is heavy"], correct_index=0,
    explanation="Many non-metals are solids and some metals are light. Good electrical conduction (with lustre and malleability) is typical of metals."),
 ]},
 {"id": "s2", "title": "Physical properties", "blocks": [
  blk("s2.table", "markdown_table", title="Metals and non-metals compared", revision=True, body=COMPARE),
  blk("s2.reveal", "theory", title="Rules and their exceptions", revision=True,
    body="- Metals are **lustrous**, **malleable** (can be beaten into thin sheets) and **ductile** (can be drawn into wires). Gold and silver are the most malleable and ductile metals.\n"
         "- Metals are **sonorous**: they ring when struck.\n- Silver and copper are the best conductors of heat; lead and mercury are poor conductors.\n\n"
         "**Exceptions:** mercury is a liquid metal; sodium and potassium are soft enough to cut with a knife and have low melting points; gallium and caesium melt in your palm. "
         "Iodine is a lustrous non-metal; graphite, a form of carbon, conducts electricity; diamond, another form of carbon, is the hardest natural substance."),
  blk("s2.check", "knowledge_check", question="Which metal is a liquid at room temperature?", options=["Mercury", "Sodium", "Gallium", "Lead"], correct_index=0,
    explanation="Mercury is the only metal that is liquid at room temperature; gallium melts only at about body temperature."),
 ]},
 {"id": "s3", "title": "Chemical properties of metals", "blocks": [
  blk("s3.oxygen", "theory", title="With oxygen", revision=True,
    body=f"Metal + oxygen → metal oxide: {E['cu_o2']}; {E['al_o2']}\n\n"
         "Metal oxides are **basic**. Some, like aluminium oxide and zinc oxide, react with both acids and bases: they are **amphoteric**.\n\n"
         f"- {E['al2o3_hcl']}\n- {E['al2o3_naoh']} (sodium aluminate)\n\n"
         "Soluble metal oxides form **alkalis**: " + E["na2o_h2o"] + "\n\n"
         "Sodium and potassium react so vigorously that they catch fire in air, so they are **kept under kerosene**. Magnesium, aluminium, zinc and lead form a thin oxide layer that protects them; "
         "aluminium's oxide layer is made thicker by **anodising**. Iron burns only as filings; copper only forms a black coat; silver and gold do not react with oxygen even at high temperature."),
  blk("s3.water", "theory", title="With water", revision=True,
    body="Metal + water → metal oxide or hydroxide + hydrogen.\n\n"
         f"- Potassium and sodium react violently with cold water, and the hydrogen catches fire: {E['k_h2o']}; {E['na_h2o']}\n"
         f"- Calcium reacts less violently and floats, because bubbles of hydrogen stick to it: {E['ca_h2o']} Magnesium floats too, and reacts with hot water.\n"
         f"- Aluminium, iron and zinc react only with steam: {E['al_steam']}; {E['fe_steam']}\n"
         "- Lead, copper, silver and gold do not react with water at all."),
  blk("s3.acids", "theory", title="With acids and salt solutions", revision=True,
    body=f"Metal + dilute acid → salt + hydrogen: {E['zn_hcl']} The rate decreases in the order Mg > Al > Zn > Fe. Copper does not react with dilute HCl.\n\n"
         "With nitric acid hydrogen is usually not given off, because HNO₃ is a strong oxidising agent; only magnesium and manganese give hydrogen with very dilute HNO₃. "
         "**Aqua regia** (3 parts concentrated HCl to 1 part concentrated HNO₃) dissolves even gold and platinum.\n\n"
         f"A more reactive metal displaces a less reactive one from its salt solution: {E['cu_agno3']}"),
  blk("s3.series", "markdown_table", title="The reactivity series", revision=True, body=SERIES),
  blk("s3.check1", "knowledge_check", question="Which pair will give a displacement reaction?",
    options=["Silver nitrate solution and copper", "Sodium chloride solution and copper", "Iron sulphate solution and silver", "Magnesium chloride solution and aluminium"], correct_index=0,
    explanation="Copper is above silver in the reactivity series, so it displaces silver: " + E["cu_agno3"]),
  blk("s3.check2", "knowledge_check", question="Which metal will NOT give hydrogen with dilute hydrochloric acid?", options=["Copper", "Zinc", "Magnesium", "Iron"], correct_index=0,
    explanation="Copper is below hydrogen in the reactivity series."),
 ]},
 {"id": "s4", "title": "How metals and non-metals bond", "blocks": [
  blk("s4.thm", "theory", title="Ionic compounds", revision=True,
    body="Noble gases have a full outer shell, so they hardly react. Other atoms react to get such a stable arrangement.\n\n"
         f"Sodium (2, 8, 1) loses one electron and chlorine (2, 8, 7) gains it: {NA_ION} and {CL_ION}. The ions Na⁺ and Cl⁻ are held by strong electrostatic attraction in **sodium chloride**: {E['na_cl2']}\n\n"
         f"In magnesium oxide, {MG_ION} and {O_ION}. Compounds formed by such transfer of electrons are **ionic** (electrovalent) compounds."),
  blk("s4.props", "theory", title="Properties of ionic compounds", revision=True,
    body="- They are hard, brittle solids because of the strong attraction between ions.\n- They have **high melting and boiling points**: a lot of energy is needed to overcome the attraction.\n"
         "- They usually dissolve in water but not in kerosene or petrol.\n- They conduct electricity when **molten or dissolved**, because the ions can then move; in the solid they cannot."),
  blk("s4.table", "markdown_table", title="Melting and boiling points of some ionic compounds", revision=False, body=IONIC_MP),
  blk("s4.check", "knowledge_check", question="Solid sodium chloride does not conduct electricity, but molten sodium chloride does, because:",
    options=["the ions can move only in the molten state", "the solid has no ions", "molten salt has free electrons", "heat makes it a metal"], correct_index=0,
    explanation="The solid contains ions too, but they are fixed in place; in the melt they are free to move."),
 ]},
 {"id": "s5", "title": "Getting metals from their ores", "blocks": [
  blk("s5.thm", "theory", title="Minerals, ores and gangue", revision=True,
    body="Elements or compounds found naturally in the earth's crust are **minerals**. A mineral from which a metal can be extracted profitably is an **ore**. The earth, sand and other impurities in the ore are the **gangue**, removed first (enrichment).\n\n"
         "Metals at the bottom of the reactivity series, such as gold and platinum, are found **free**; reactive metals are found as oxides, sulphides or carbonates."),
  blk("s5.extract", "theory", title="Extraction by reactivity", revision=True,
    body=f"- **Low reactivity (Hg, Cu):** heat the ore alone. {E['hgs']} then {E['hgo']} Similarly {E['cu2s']} and {E['cu2o']}\n"
         f"- **Middle (Zn, Fe, Pb):** convert to the oxide first: sulphide ores by **roasting** (heating in air), {E['zns']}; carbonate ores by **calcination** (heating with little air), {E['znco3']} "
         f"Then **reduce** the oxide with carbon: {E['zno_c']} Aluminium can also be the reducing agent; the **thermite reaction** is so exothermic that the iron melts and is used to join railway tracks: {E['thermite']}\n"
         f"- **High reactivity (Na, Mg, Ca, Al):** carbon cannot reduce them, so their molten chlorides or oxides are **electrolysed**: at the cathode {NA_CATH}, at the anode {CL_AN}\n\n"
         "**Refining:** in electrolytic refining the impure metal is the anode, a thin strip of pure metal is the cathode, and a solution of a salt of the metal is the electrolyte. "
         "Pure metal collects on the cathode; impurities fall below the anode as **anode mud**."),
  blk("s5.check", "knowledge_check", question="Converting a sulphide ore into its oxide by heating it strongly in air is called:",
    options=["roasting", "calcination", "electrolysis", "refining"], correct_index=0, explanation="Roasting is heating in excess air; calcination is heating in limited air, used for carbonate ores."),
 ]},
 {"id": "s6", "title": "Corrosion and alloys", "blocks": [
  blk("s6.discovery", "discovery", title="Activity 3.14: what does iron need to rust?",
    body="Take three test tubes with clean iron nails. In **A**, put tap water and cork it: air and water are present. In **B**, put boiled distilled water with a layer of oil on top: no air. "
         "In **C**, put anhydrous calcium chloride, which absorbs moisture: dry air only. After a few days, only the nails in **A** rust. **Both air and water are needed for rusting.**"),
  blk("s6.thm", "theory", title="Preventing corrosion; alloys", revision=True,
    body="Rusting can be prevented by **painting, oiling, greasing, galvanising** (coating with zinc), chrome plating, anodising, or making alloys. "
         "In galvanised iron, zinc protects the iron even if the coating is broken.\n\n"
         "An **alloy** is a homogeneous mixture of two or more metals, or of a metal and a non-metal. Alloys are made to improve properties:\n\n"
         "- **Stainless steel:** iron with nickel and chromium; hard and does not rust.\n- **Brass:** copper and zinc. **Bronze:** copper and tin.\n"
         "- **Solder:** lead and tin; low melting point, used to weld electrical wires.\n- **Amalgam:** any alloy of mercury.\n"
         "- Pure gold (24 carat) is very soft, so ornaments use **22 carat** gold: 22 parts gold alloyed with 2 parts silver or copper.\n\n"
         "The electrical conductivity and melting point of an alloy are lower than those of the pure metals."),
  blk("s6.check", "knowledge_check", question="Solder is an alloy of:", options=["lead and tin", "copper and zinc", "copper and tin", "iron and nickel"], correct_index=0,
    explanation="Lead and tin give solder its low melting point. Brass is copper and zinc; bronze is copper and tin; stainless steel contains iron, nickel and chromium."),
  blk("s6.memory", "memory_trick", title="Remember the series", revision=True,
    body="**K**ing **N**apoleon **C**an **M**arch **A**lone; **Z**ebras **I**n **L**ondon **H**ate **C**old **M**orning **S**now; **G**o!\n\n"
         "K, Na, Ca, Mg, Al, Zn, Fe (Iron), Pb (Lead), H, Cu, Hg (Mercury), Ag (Silver), Au (Gold). A metal **above** another displaces it from its salt; metals **above H** give hydrogen with dilute acids."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Saying all metals are solids, or that all non-metals are poor conductors: remember mercury and graphite.\n- Forgetting that amphoteric oxides (Al₂O₃, ZnO) react with both acids and bases.\n"
         "- Expecting hydrogen from nitric acid: HNO₃ oxidises the hydrogen to water.\n- Mixing up roasting (sulphide ores, excess air) and calcination (carbonate ores, limited air).\n"
         "- In electrolytic refining, putting the impure metal at the cathode: it is the anode."),
  blk("s6.tip", "teacher_tip", title="Rust in a week",
    body="Set up Activity 3.14 on a Monday and let students check the three test tubes each morning. Also put one nail in salt water: it rusts fastest, which explains why ships and coastal bridges need extra protection."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why aluminium is very reactive but still used for cooking pots, and why sodium is kept under kerosene but gold can lie in the ground for centuries."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** displacement and redox reactions explain extraction and corrosion.\n- **Chapter 4, Carbon and its Compounds:** non-metals share electrons instead of transferring them (covalent bonds).\n"
         "- **Chapter 11, Electricity:** why copper and aluminium make good wires, and nichrome makes heating elements."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A metal X is found as its sulphide ore XS and is used to galvanise iron. Identify X and describe how it is obtained from XS.\n\n"
         f"**Answer:** X is zinc. The ore is concentrated, then roasted: {E['zns']} The zinc oxide is then reduced with carbon: {E['zno_c']} Finally the zinc can be refined electrolytically."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Metals are lustrous, malleable, ductile and good conductors; they form positive ions and basic (or amphoteric) oxides.\n- Non-metals are mostly dull and brittle, poor conductors; they form negative ions and acidic or neutral oxides.\n"
         "- The reactivity series lists metals from most to least reactive; a more reactive metal displaces a less reactive one.\n"
         "- Ionic compounds form by transfer of electrons; they have high melting points and conduct when molten or dissolved.\n"
         "- Extraction depends on reactivity: heat alone, reduction with carbon, or electrolysis; refining is often electrolytic.\n- Corrosion needs air and water; it is prevented by painting, galvanising and alloying."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Learn the reactivity series with the position of hydrogen; most 'what happens when' questions depend on it.\n- Show electron transfer with electron-dot structures and arrows for ionic compounds.\n"
         "- Write the extraction steps in order (concentration, roasting or calcination, reduction, refining) with equations.\n- Know the three test-tube activity for rusting and the conditions needed."),
  blk("s7.flash1", "flashcard", front="Two amphoteric oxides", back="Aluminium oxide and zinc oxide"),
  blk("s7.flash2", "flashcard", front="What is aqua regia?", back="A mixture of concentrated HCl and concentrated HNO₃ in the ratio 3 : 1; it dissolves gold."),
  blk("s7.flash3", "flashcard", front="Composition of brass and bronze", back="Brass: copper and zinc. Bronze: copper and tin."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Metals and Non-metals",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 3,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: properties of metals and non-metals, reactivity series, formation and properties of ionic compounds, basic metallurgical processes, corrosion and its prevention.",
  "concepts": ["properties", "reactivity", "ionic_metallurgy"], "sections": sections}

# ---------------------------------------------------------------- questions
PR, RE, IM = "properties", "reactivity", "ionic_metallurgy"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 3 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2 = ["1 mark: answer", "1 mark: reason or equation"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [PR], it("3.1", 1), "Give an example of a metal which\n\n(i) is a liquid at room temperature.\n\n(ii) can be easily cut with a knife.\n\n(iii) is the best conductor of heat.\n\n(iv) is a poor conductor of heat.", "easy",
    answer_steps=["(i) Mercury (ii) Sodium (or potassium)", "(iii) Silver (iv) Lead (or mercury)"], marking_scheme=["1 mark: (i) and (ii)", "1 mark: (iii) and (iv)"])
C.q("it1.q2", "very_short_answer", 2, [PR], it("3.1", 2), "Explain the meanings of malleable and ductile.", "easy",
    answer_steps=["Malleable: can be beaten into thin sheets (like aluminium foil).", "Ductile: can be drawn into thin wires (like copper wire)."], marking_scheme=["1 mark: malleable", "1 mark: ductile"])
C.q("it2.q1", "very_short_answer", 2, [RE], it("3.2", 1), "Why is sodium kept immersed in kerosene oil?", "easy",
    answer_steps=["Sodium reacts so vigorously with oxygen and moisture in air that it catches fire.", "Kerosene does not react with sodium and keeps air and water away from it."], marking_scheme=MS2)
C.q("it2.q2", "short_answer", 3, [RE], it("3.2", 2), "Write equations for the reactions of\n\n(i) iron with steam\n\n(ii) calcium and potassium with water",
    answer_steps=["(i) " + E["fe_steam"], "(ii) " + E["ca_h2o"], E["k_h2o"]], marking_scheme=["1 mark: (i)", "1 mark: calcium", "1 mark: potassium"])
C.q("it2.q3", "short_answer", 3, [RE], it("3.2", 3), "Samples of four metals A, B, C and D were added one by one to the following solutions.\n\n"
    "Metal A: no reaction with iron(II) sulphate; displacement with copper(II) sulphate.\n\nMetal B: displacement with iron(II) sulphate; no reaction with zinc sulphate.\n\n"
    "Metal C: no reaction with iron(II) sulphate, copper(II) sulphate or zinc sulphate; displacement with silver nitrate.\n\nMetal D: no reaction with any of the four solutions.\n\n"
    "(i) Which is the most reactive metal?\n\n(ii) What would you observe if B is added to a solution of copper(II) sulphate?\n\n(iii) Arrange the metals A, B, C and D in the order of decreasing reactivity.",
    answer_steps=["(i) B: it displaces iron, so it is the most reactive of the four.", "(ii) B displaces copper: the blue colour fades and a reddish-brown layer of copper forms.", "(iii) B > A > C > D"],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("it2.q4", "very_short_answer", 2, [RE], it("3.2", 4), "Which gas is produced when dilute hydrochloric acid is added to a reactive metal? Write the chemical reaction when iron reacts with dilute H₂SO₄.", "easy",
    answer_steps=["Hydrogen gas.", E["fe_h2so4"]], marking_scheme=MS2)
C.q("it2.q5", "very_short_answer", 2, [RE], it("3.2", 5), "What would you observe when zinc is added to a solution of iron(II) sulphate? Write the chemical reaction that takes place.",
    answer_steps=["Zinc is more reactive than iron, so the pale green colour fades and iron is deposited.", E["zn_feso4"]], marking_scheme=MS2)
C.q("it3.q1", "short_answer", 3, [IM], it("3.3", 1), "(i) Write the electron-dot structures for sodium, oxygen and magnesium.\n\n(ii) Show the formation of Na₂O and MgO by the transfer of electrons.\n\n(iii) What are the ions present in these compounds?", "hard",
    answer_steps=["(i) Sodium (2, 8, 1) has one dot around its symbol; oxygen (2, 6) has six dots; magnesium (2, 8, 2) has two dots.",
                  "(ii) Each of two sodium atoms gives one electron to oxygen: " + NA_ION + " (twice) and " + O_ION + ", giving Na₂O. Magnesium gives two electrons to oxygen: " + MG_ION + " and " + O_ION + ", giving MgO.",
                  "(iii) Na₂O: Na⁺ and O²⁻ ions. MgO: Mg²⁺ and O²⁻ ions."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("it3.q2", "very_short_answer", 2, [IM], it("3.3", 2), "Why do ionic compounds have high melting points?", "easy",
    answer_steps=["The ions are held together by strong forces of electrostatic attraction.", "A lot of energy is needed to overcome these forces, so the melting points are high."], marking_scheme=MS2)
C.q("it4.q1", "short_answer", 3, [IM], it("3.4", 1), "Define the following terms.\n\n(i) Mineral\n\n(ii) Ore\n\n(iii) Gangue", "easy",
    answer_steps=["(i) Mineral: an element or compound that occurs naturally in the earth's crust.", "(ii) Ore: a mineral from which a metal can be extracted profitably.", "(iii) Gangue: the earth, sand and other impurities present in the ore."],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.mcq("it4.q2", [IM], "Which two metals are found in nature in the free state?", ["Gold and platinum", "Sodium and potassium", "Iron and zinc", "Aluminium and magnesium"], 0,
      "Metals at the bottom of the reactivity series are so unreactive that they occur free.", source=it("3.4", 2))
C.mcq("it4.q3", [IM], "What chemical process is used for obtaining a metal from its oxide?", ["Reduction", "Oxidation", "Calcination", "Neutralisation"], 0,
      "Removing oxygen from the oxide is reduction, for example " + E["zno_c"], source=it("3.4", 3))
C.q("it5.q1", "short_answer", 3, [RE], it("3.5", 1), "Metallic oxides of zinc, magnesium and copper were heated with the following metals: zinc, magnesium and copper. In which cases will you find displacement reactions taking place?", "medium",
    answer_steps=["A metal displaces another only if it is more reactive: Mg > Zn > Cu.", "Zinc with copper oxide: " + E["zn_cuo"], "Magnesium with zinc oxide and with copper oxide: " + E["mg_zno"] + "; " + E["mg_cuo"]],
    marking_scheme=["1 mark: rule", "1 mark: zinc", "1 mark: magnesium"])
C.mcq("it5.q2", [RE], "Which metals do not corrode easily?", ["Gold and platinum", "Iron and zinc", "Sodium and potassium", "Copper and lead"], 0,
      "Gold and platinum are very unreactive, so moisture and air do not attack them.", source=it("3.5", 2))
C.q("it5.q3", "very_short_answer", 2, [IM], it("3.5", 3), "What are alloys?", "easy",
    answer_steps=["An alloy is a homogeneous mixture of two or more metals, or of a metal and a non-metal.", "Examples: brass (copper and zinc), stainless steel (iron, nickel and chromium)."], marking_scheme=["1 mark: definition", "1 mark: example"])
# Exercises
C.mcq("ex.q1", [RE], "Which of the following pairs will give displacement reactions?", ["NaCl solution and copper metal", "MgCl₂ solution and aluminium metal", "FeSO₄ solution and silver metal", "AgNO₃ solution and copper metal."], 3,
      "Only copper is more reactive than the metal in the salt (silver).", source=ex(1))
C.mcq("ex.q2", [IM], "Which of the following methods is suitable for preventing an iron frying pan from rusting?", ["Applying grease", "Applying paint", "Applying a coating of zinc", "All of the above."], 3,
      "Each of them keeps air and moisture away from the iron.", source=ex(2))
C.mcq("ex.q3", [PR], "An element reacts with oxygen to give a compound with a high melting point. This compound is also soluble in water. The element is likely to be", ["calcium", "carbon", "silicon", "iron."], 0,
      "Calcium oxide is an ionic compound with a high melting point, and it dissolves in water.", "medium", source=ex(3))
C.mcq("ex.q4", [RE], "Food cans are coated with tin and not with zinc because", ["zinc is costlier than tin.", "zinc has a higher melting point than tin.", "zinc is more reactive than tin.", "zinc is less reactive than tin."], 2,
      "Zinc could react with acids in the food; tin is less reactive.", source=ex(4))
C.q("ex.q5", "short_answer", 3, [PR], ex(5), "You are given a hammer, a battery, a bulb, wires and a switch.\n\n(a) How could you use them to distinguish between samples of metals and non-metals?\n\n(b) Assess the usefulness of these tests in distinguishing between metals and non-metals.",
    answer_steps=["(a) Hammer each sample: metals flatten into sheets (malleable); non-metals break into pieces.", "Connect each sample in a circuit with the battery, bulb and switch: metals make the bulb glow; non-metals do not.",
                  "(b) These tests are useful, but there are exceptions: graphite (a non-metal) conducts electricity, and mercury is a liquid metal that cannot be hammered."],
    marking_scheme=["1 mark: hammer test", "1 mark: conduction test", "1 mark: usefulness"])
C.q("ex.q6", "very_short_answer", 2, [RE], ex(6), "What are amphoteric oxides? Give two examples of amphoteric oxides.", "easy",
    answer_steps=["Metal oxides that react with both acids and bases to give salt and water are amphoteric oxides.", "Examples: aluminium oxide and zinc oxide."], marking_scheme=["1 mark: definition", "1 mark: examples"])
C.q("ex.q7", "very_short_answer", 2, [RE], ex(7), "Name two metals which will displace hydrogen from dilute acids, and two metals which will not.", "easy",
    answer_steps=["Displace hydrogen: zinc and magnesium (metals above hydrogen in the reactivity series).", "Do not: copper and silver (below hydrogen)."], marking_scheme=["1 mark: first pair", "1 mark: second pair"])
C.q("ex.q8", "short_answer", 3, [IM], ex(8), "In the electrolytic refining of a metal M, what would you take as the anode, the cathode and the electrolyte?", "easy",
    answer_steps=["Anode: a thick block of impure metal M.", "Cathode: a thin strip of pure metal M.", "Electrolyte: a solution of a soluble salt of M."], marking_scheme=["1 mark: anode", "1 mark: cathode", "1 mark: electrolyte"])
C.q("ex.q9", "short_answer", 3, [PR], ex(9), "Pratyush took sulphur powder on a spatula and heated it. He collected the gas evolved by inverting a test tube over it.\n\n(a) What will be the action of the gas on (i) dry litmus paper? (ii) moist litmus paper?\n\n(b) Write a balanced chemical equation for the reaction taking place.",
    answer_steps=["(a) (i) No change on dry litmus paper.", "(ii) Moist blue litmus turns red: sulphur dioxide dissolves to form an acid, " + E["so2_h2o"], "(b) " + E["s_o2"]],
    marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (b)"])
C.q("ex.q10", "very_short_answer", 2, [IM], ex(10), "State two ways to prevent the rusting of iron.", "easy",
    answer_steps=["Painting, oiling or greasing the iron.", "Galvanising (coating with zinc), or making alloys such as stainless steel."], marking_scheme=["1 mark: first way", "1 mark: second way"])
C.q("ex.q11", "very_short_answer", 2, [PR], ex(11), "What type of oxides are formed when non-metals combine with oxygen?", "easy",
    answer_steps=["Acidic oxides, such as sulphur dioxide and carbon dioxide.", "Some are neutral, such as carbon monoxide and water."], marking_scheme=["1 mark: acidic", "1 mark: neutral examples"])
C.q("ex.q12", "long_answer", 5, [RE, IM], ex(12), "Give reasons\n\n(a) Platinum, gold and silver are used to make jewellery.\n\n(b) Sodium, potassium and lithium are stored under oil.\n\n(c) Aluminium is a highly reactive metal, yet it is used to make utensils for cooking.\n\n(d) Carbonate and sulphide ores are usually converted into oxides during the process of extraction.",
    answer_steps=["(a) They are lustrous, malleable and ductile, and so unreactive that they do not corrode.", "(b) They react vigorously with air and water and may catch fire; oil keeps air and water away.",
                  "(c) Aluminium is protected by a thin layer of aluminium oxide that stops further reaction; it is also light and a good conductor of heat.",
                  "(d) It is easier to obtain a metal from its oxide by reduction than from its carbonate or sulphide.", "For example: " + E["zns"] + ", then " + E["zno_c"]],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: example or equation"])
C.q("ex.q13", "very_short_answer", 2, [RE], ex(13), "You must have seen tarnished copper vessels being cleaned with lemon or tamarind juice. Explain why these sour substances are effective in cleaning the vessels.",
    answer_steps=["Tarnished copper has a coating of basic copper carbonate (and copper oxide), which is basic.", "Lemon and tamarind contain acids that react with and dissolve this coating, so the vessel shines again."], marking_scheme=MS2)
C.q("ex.q14", "short_answer", 3, [PR], ex(14), "Differentiate between metal and non-metal on the basis of their chemical properties.",
    answer_steps=["Metals form basic (or amphoteric) oxides; non-metals form acidic or neutral oxides.", "Metals above hydrogen displace hydrogen from dilute acids; non-metals do not.",
                  "Metals lose electrons to form positive ions; non-metals gain electrons to form negative ions."], marking_scheme=["1 mark: oxides", "1 mark: acids", "1 mark: ions"])
C.q("ex.q15", "very_short_answer", 2, [RE], ex(15), "A man went door to door posing as a goldsmith. He promised to bring back the glitter of old and dull gold ornaments. An unsuspecting lady gave a set of gold bangles to him which he dipped in a particular solution. "
    "The bangles sparkled like new but their weight was reduced drastically. The lady was upset but after a futile argument the man beat a hasty retreat. Can you play the detective to find out the nature of the solution he had used?", "medium",
    answer_steps=["He used aqua regia: a freshly prepared mixture of concentrated hydrochloric acid and concentrated nitric acid in the ratio 3 : 1.", "Aqua regia dissolves gold, so the outer layer dissolved away, the bangles shone, and their weight decreased."],
    marking_scheme=["1 mark: aqua regia", "1 mark: explanation"])
C.q("ex.q16", "very_short_answer", 2, [RE], ex(16), "Give reasons why copper is used to make hot water tanks and not steel (an alloy of iron).",
    answer_steps=["Copper does not react with cold water, hot water or steam, so it does not corrode.", "Iron in steel reacts with steam and rusts; copper is also a better conductor of heat."], marking_scheme=MS2)
# CBSE sample paper
C.mcq("sqp18", [RE], "Four statements about the reactions of oxides with dilute hydrochloric acid and aqueous sodium hydroxide are listed.\n\nI. Aluminium oxide reacts with both dilute hydrochloric acid and aqueous sodium hydroxide.\n\n"
      "II. Calcium oxide reacts with dilute hydrochloric acid and aqueous sodium hydroxide.\n\nIII. Zinc oxide reacts with both dilute hydrochloric acid and aqueous sodium hydroxide.\n\n"
      "IV. Sulphur dioxide does not react with either dilute hydrochloric acid or aqueous sodium hydroxide.\n\nWhich statements are correct?", ["I and II", "I and III", "II and IV", "III and IV"], 1,
      "Aluminium oxide and zinc oxide are amphoteric. Calcium oxide is basic (it does not react with NaOH) and sulphur dioxide is acidic (it reacts with NaOH).", "medium", source=SQP(18))
C.mcq("sqp19", [RE], "An iron nail is added to each of two test tubes P and Q containing aqueous copper(II) sulphate and aqueous silver nitrate respectively. Which of the following observations is correct?",
      ["In test tube P the iron nail gets a blue coating and in test tube Q there is no reaction.", "The iron nail gets a brown coating in test tube P and a silver coating in test tube Q.",
       "There is no reaction in either test tube P or Q.", "There is no reaction in test tube P but a silver coating forms on the iron nail in test tube Q."], 1,
      "Iron is more reactive than both copper and silver, so it displaces copper (brown) in P and silver in Q.", "medium", source=SQP(19))
C.q("sqp25", "very_short_answer", 2, [PR], SQP(25), "A teacher clamped an aluminium wire on a stand and fixed a pin to the free end using wax. He heated the wire from the clamped end, and the pin fell off.\n\n"
    "A. If the teacher replaces the aluminium wire by a silver wire, will the students' observation change? Justify your answer.\n\nB. Will the aluminium wire melt? Give reason for your answer.",
    answer_steps=["A. The pin will still drop, but sooner, because silver is a better conductor of heat than aluminium.", "B. No: metals have high melting points, and the burner does not reach the melting point of aluminium."],
    marking_scheme=["1 mark: A", "1 mark: B"])
C.q("sqp26a", "short_answer", 3, [RE, IM], SQP("26(A)"), "An element 'X' is stored in kerosene, and cannot be extracted from its ore using a reducing agent. 'X' forms an ionic compound on reaction with chlorine.\n\n"
    "(i) Can we store 'X' in water? Give reason to support your answer.\n\n(ii) Identify element 'X'. Name the process used and write the equations for the extraction of 'X' from its ore.", "hard",
    answer_steps=["(i) No: X is highly reactive and reacts violently with water; it would catch fire.", "(ii) X is sodium (potassium is also correct). It is extracted by electrolytic reduction of molten sodium chloride.",
                  "Cathode: " + NA_CATH + "; anode: " + CL_AN], marking_scheme=["1 mark: (i)", "1 mark: X and process", "1 mark: equations"])
C.q("sqp26b", "short_answer", 3, [IM], SQP("26(B)"), "The domes of many buildings in Europe are made of copper. These domes now appear greenish in colour.\n\n(i) Why do the domes appear greenish though copper is orange-red in colour?\n\n"
    "(ii) In your opinion, should the copper domes be replaced by iron domes to overcome the problem of change of colour?\n\n(iii) Domes used to be made from thin sheets of metal. Why did the ancient architects use copper to make domes?",
    answer_steps=["(i) Copper corrodes slowly in moist air to form basic copper carbonate, which is green.", "(ii) No: iron would rust, and the flaky rust would expose more iron, weakening the dome. The green layer on copper protects it from further corrosion.",
                  "(iii) Copper is highly malleable, so thin sheets can be shaped into a dome."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("sqp29b", "long_answer", 5, [IM], SQP("29(B), for visually impaired students"), "Oxygen can combine with both metals and non-metals. It combines with calcium to form CaO and with carbon to form CO₂.\n\n"
    "(a) What type of bond is formed between carbon and oxygen?\n\n(b) Identify the type of bond formed between calcium and oxygen.\n\n(c) Which of the above compounds will be a good conductor of electricity in molten state and why?\n\n"
    "(d) Comment on the physical state (solid, liquid or gas) of CaO and CO₂.\n\n(e) What is the valency of carbon in CO₂?", "medium",
    answer_steps=["(a) Covalent bond (sharing of electrons).", "(b) Ionic bond (transfer of electrons from calcium to oxygen).", "(c) CaO: in the molten state its ions are free to move.",
                  "(d) CaO is a solid (strong ionic forces); CO₂ is a gas (weak forces between molecules).", "(e) 4"],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: (e)"])
# GSEB
C.q("gseb2024_40", "short_answer", 3, [IM], gseb(2024, "40"), "Metal X is found in nature as its sulphide ore XS. This metal is used in the galvanisation of iron articles.\n\n(a) Identify the metal X.\n\n(b) Explain, with chemical equations, how this sulphide ore XS is converted into the metal X.",
    answer_steps=["(a) X is zinc (ore: zinc blende, ZnS).", "(b) Roasting in excess air: " + E["zns"], "Reduction with carbon: " + E["zno_c"]], marking_scheme=["1 mark: (a)", "1 mark: roasting", "1 mark: reduction"])
C.mcq("gseb2025_12", [IM], "____ is the chemical formula of cinnabar.", [chem("HgS"), chem("ZnS"), chem("Cu2S")], 0, "Cinnabar, the ore of mercury, is mercury sulphide; ZnS is zinc blende and Cu₂S is copper glance.", source=gseb(2025, "12"))
C.tf("gseb2025_13", [IM], "Solder is an alloy of lead and tin.", True, "True: solder is an alloy of lead and tin with a low melting point, used for welding electrical wires.", source=gseb(2025, "13"))
C.q("gseb2025_39", "short_answer", 3, [IM], gseb(2025, "39"), "The electronic configurations of two elements X and Y are: X = 2, 8, 1 and Y = 2, 8, 7.\n\n(a) Identify the metal and write its name.\n\n(b) Identify the non-metal and write its name.\n\n(c) Which ionic compound is formed by X and Y?", "easy",
    answer_steps=["(a) X is the metal: sodium (it loses one electron).", "(b) Y is the non-metal: chlorine (it gains one electron).", "(c) Sodium chloride, NaCl: " + E["na_cl2"]],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
C.q("gseb2025_40", "short_answer", 3, [IM], gseb(2025, "40"), "In an experiment, iron nails are kept in three test tubes: A with tap water (air and water), B with boiled distilled water covered by oil (no air), and C with anhydrous calcium chloride (dry air).\n\n"
    "(a) In which test tube will the colour of the iron nail change?\n\n(b) Name the chemical reaction associated with it.\n\n(c) Write the essential conditions required for this reaction.",
    answer_steps=["(a) Test tube A.", "(b) Rusting of iron (corrosion).", "(c) Both air (oxygen) and water (moisture) must be present."], marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
C.q("gseb2025_40vi", "short_answer", 3, [PR], gseb(2025, "40 (for visually impaired students)"), "Give an example of a metal which\n\n(a) melts if you keep it on your palm.\n\n(b) can be easily cut with a knife.\n\n(c) is found in nature in the free state.", "easy",
    answer_steps=["(a) Gallium (or caesium).", "(b) Sodium (or potassium).", "(c) Gold (or platinum)."], marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)"])
# Shine MCQs
C.mcq("mcq01", [PR], "Which non-metal is lustrous?", ["Iodine", "Sulphur", "Phosphorus", "Carbon (coal)"], 0, "Iodine has a shiny lustre although it is a non-metal.")
C.mcq("mcq02", [PR], "Which form of carbon is a good conductor of electricity?", ["Graphite", "Diamond", "Coal", "Charcoal powder"], 0, "Graphite conducts electricity; diamond does not.")
C.mcq("mcq03", [RE], "Which metal reacts with cold water so vigorously that the hydrogen catches fire?", ["Potassium", "Magnesium", "Iron", "Copper"], 0, "Potassium (like sodium) reacts violently with cold water.")
C.mcq("mcq04", [RE], "Calcium floats when it reacts with water because:", ["bubbles of hydrogen stick to its surface", "it is lighter than water", "it melts", "it forms an oxide layer"], 0, "The hydrogen bubbles make it float.", "medium")
C.mcq("mcq05", [IM], "The process of heating a carbonate ore in limited air is called:", ["calcination", "roasting", "smelting", "refining"], 0, "Calcination is used for carbonate ores; roasting for sulphide ores.")
C.mcq("mcq06", [IM], "In the thermite reaction, the reducing agent is:", ["aluminium", "iron oxide", "carbon", "hydrogen"], 0, "Aluminium removes oxygen from iron oxide: " + E["thermite"], "medium")
C.mcq("mcq07", [IM], "Highly reactive metals such as sodium are extracted by:", ["electrolysis of their molten chlorides", "heating with carbon", "heating alone", "roasting"], 0, "Carbon cannot reduce them, so electrolysis is used.")
C.mcq("mcq08", [IM], "22 carat gold contains:", ["22 parts gold and 2 parts silver or copper", "22 parts gold and 24 parts copper", "pure gold", "2 parts gold and 22 parts copper"], 0, "Pure gold is 24 carat; 22 carat gold is alloyed with 2 parts silver or copper to make it harder.")
C.mcq("mcq09", [IM], "Which property is shown by ionic compounds?", ["High melting point", "Conduction in the solid state", "Solubility in kerosene", "Low boiling point"], 0, "Strong forces between ions give them high melting points.")
C.mcq("mcq10", [IM], "Galvanisation is coating iron with:", ["zinc", "tin", "chromium", "copper"], 0, "Galvanised iron has a coating of zinc.")
# Assertion-reason
C.ar("ar1", [RE], "Sodium is stored under kerosene.", "Sodium reacts vigorously with oxygen and water.", 0, "Kerosene keeps air and water away from the reactive metal: R explains A.")
C.ar("ar2", [RE], "Copper reacts with dilute hydrochloric acid to give hydrogen.", "Copper is below hydrogen in the reactivity series.", 3, "A is false: copper does not give hydrogen with dilute HCl. R is true.")
C.ar("ar3", [IM], "Ionic compounds conduct electricity in the molten state.", "In the molten state, the ions are free to move.", 0, "Moving ions carry the current: R explains A.")
C.ar("ar4", [RE], "Aluminium oxide is an amphoteric oxide.", "Aluminium is a good conductor of heat.", 1, "Both are true, but conduction of heat does not explain why the oxide reacts with both acids and bases.")
C.ar("ar5", [IM], "Pure gold is used for making ornaments.", "Pure gold is very soft.", 3, "A is false: pure gold is too soft, so 22 carat gold is used. R is true.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [IM], SHINE, "Show the formation of sodium chloride by the transfer of electrons.", "medium",
    answer_steps=["Sodium loses one electron: " + NA_ION, "Chlorine gains it: " + CL_ION + ". The oppositely charged ions attract to form Na⁺Cl⁻."], marking_scheme=["1 mark: sodium", "1 mark: chlorine"])
C.q("vsa2", "very_short_answer", 2, [IM], SHINE, "What is the thermite reaction? Give one use.", "easy",
    answer_steps=["The highly exothermic reduction of iron oxide by aluminium: " + E["thermite"], "The molten iron is used to join railway tracks and cracked machine parts."], marking_scheme=["1 mark: equation", "1 mark: use"])
C.q("sa1", "short_answer", 3, [IM], SHINE, "How is mercury obtained from its ore cinnabar? Write the equations.", "medium",
    answer_steps=["Mercury is low in the reactivity series, so heating alone is enough.", "Cinnabar is heated in air: " + E["hgs"], "On further heating, mercury oxide decomposes: " + E["hgo"]],
    marking_scheme=["1 mark: method", "1 mark: first equation", "1 mark: second equation"])
C.q("sa2", "short_answer", 3, [RE], SHINE, "Arrange magnesium, potassium, copper and zinc in decreasing order of reactivity. What would you observe when zinc is added to copper sulphate solution? Write the equation.", "medium",
    answer_steps=["K > Mg > Zn > Cu.", "The blue colour of the solution fades and a reddish-brown layer of copper forms on the zinc.", ce("Zn(s) + CuSO4(aq) -> ZnSO4(aq) + Cu(s)")],
    marking_scheme=["1 mark: order", "1 mark: observation", "1 mark: equation"])
C.q("la1", "long_answer", 5, [IM], SHINE, "Describe, with a labelled description, the electrolytic refining of copper. What is anode mud?", "medium",
    answer_steps=["The anode is a thick block of impure copper; the cathode is a thin strip of pure copper.", "The electrolyte is acidified copper sulphate solution.",
                  "When current flows, copper dissolves from the anode into the solution, and an equal amount of pure copper is deposited on the cathode.",
                  "Soluble impurities go into the solution.", "Insoluble impurities, such as silver and gold, settle at the bottom below the anode: this is the anode mud."],
    marking_scheme=["1 mark: anode and cathode", "1 mark: electrolyte", "1 mark: process", "1 mark: soluble impurities", "1 mark: anode mud"])
C.q("la2", "long_answer", 5, [IM], SHINE, "Explain, with equations, the extraction of a metal of medium reactivity such as zinc from (i) its sulphide ore (ii) its carbonate ore. Why can carbon not be used to extract sodium?", "hard",
    answer_steps=["(i) Zinc blende is roasted: " + E["zns"], "(ii) Calamine is calcined: " + E["znco3"], "The zinc oxide is reduced with carbon: " + E["zno_c"],
                  "The zinc can be purified by electrolytic refining.", "Sodium is more reactive than carbon and has a greater affinity for oxygen, so carbon cannot reduce its compounds; electrolysis is used."],
    marking_scheme=["1 mark: roasting", "1 mark: calcination", "1 mark: reduction", "1 mark: refining", "1 mark: sodium"])
C.q("cb1", "case_based", 4, [IM], SHINE,
    "Neha's school is near the sea. The iron gate rusts quickly, but the steel handrail labelled 'stainless' does not. The electrician uses solder to join wires, and her grandmother's bangles are 22 carat gold.\n\n"
    "(i) What two conditions are needed for iron to rust? (1)\n\n(ii) Name the metals mixed with iron in stainless steel. (1)\n\n(iii) Why is solder suitable for joining electrical wires? OR Why is 22 carat gold used for ornaments instead of 24 carat gold? (2)",
    answer_steps=["(i) Air (oxygen) and water (moisture).", "(ii) Nickel and chromium.", "(iii) Solder is an alloy of lead and tin with a low melting point, so it melts easily and joins the wires. OR Pure (24 carat) gold is too soft; adding 2 parts silver or copper makes it harder."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark reason, 1 mark property"])
C.q("cb2", "case_based", 4, [RE], SHINE,
    "Students placed small pieces of four metals P, Q, R and S in cold water. P reacted violently and caught fire. Q did not react with cold water but reacted with hot water. R reacted only with steam. S did not react even with steam.\n\n"
    "(i) Which metal is the most reactive? (1)\n\n(ii) Arrange the four metals in decreasing order of reactivity. (1)\n\n(iii) If R is iron, write the equation for its reaction with steam. OR If S is copper, why is it used for hot water tanks? (2)",
    answer_steps=["(i) P.", "(ii) P > Q > R > S.", "(iii) " + E["fe_steam"] + " OR Copper does not react with water or steam, so it does not corrode, and it conducts heat well."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch03.q.ex."))
