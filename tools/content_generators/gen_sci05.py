"""CBSE Class 10 Science Ch 5: Life Processes.
The few chemical equations go through ce(), which refuses unbalanced ones; the
respiration pathways are word equations, written as text."""
import sys
from sci_common import Chapter, ce, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch05"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch05_life_processes"
C = Chapter("sci10ch05")
blk = C.blk

E = {k: ce(v) for k, v in {
 "photo": "6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O", "aerobic": "C6H12O6 + 6O2 -> 6CO2 + 6H2O",
 "ferment": "C6H12O6 -> 2C2H5OH + 2CO2", "lactic": "C6H12O6 -> 2C3H6O3",
}.items()}

PATHWAYS = ("| Where | Oxygen | Glucose (6-carbon) is broken down to | Energy |\n|---|---|---|---|\n"
            "| Cytoplasm (all cells) | not needed | pyruvate (3-carbon) | a little |\n"
            "| Yeast (fermentation) | absent | ethanol + carbon dioxide | a little |\n"
            "| Our muscle cells | lack of oxygen | lactic acid (3-carbon) | a little |\n"
            "| Mitochondria | present | carbon dioxide + water | a lot |")
ENZYMES = ("| Part | Gland or juice | What it does |\n|---|---|---|\n"
           "| Mouth | Salivary glands: saliva (salivary amylase) | starch to sugar |\n"
           "| Stomach | Gastric glands: hydrochloric acid, pepsin, mucus | acid medium; pepsin digests proteins; mucus protects the lining |\n"
           "| Small intestine | Liver: bile | makes the food alkaline; breaks fats into small globules (emulsification) |\n"
           "| Small intestine | Pancreas: pancreatic juice (trypsin, lipase) | trypsin digests proteins; lipase digests emulsified fats |\n"
           "| Small intestine | Intestinal wall: intestinal juice | proteins to amino acids, carbohydrates to glucose, fats to fatty acids and glycerol |\n"
           "| Large intestine | – | absorbs water; the rest leaves through the anus |")

sections = [
 {"id": "s1", "title": "What makes something alive?", "blocks": [
  blk("s1.hook", "hook", title="Even when you sleep, you are busy",
    body="When you sleep, you do not walk, talk or play. Yet you are alive. Inside you, food is being digested, air is moving in and out, blood is flowing and waste is being removed.\n\n"
         "These **maintenance** jobs never stop, even at the level of molecules. They are called **life processes**: **nutrition, respiration, transportation and excretion**. "
         "In this chapter you will see how plants and animals, including you, carry out each of them."),
  blk("s1.inspiration", "inspiration", title="The man who found the cell's energy coin", person="Yellapragada SubbaRow", years="1895–1948",
    body="Yellapragada SubbaRow was born in Bhimavaram, Andhra Pradesh. At Harvard, with Cyrus Fiske, he discovered **phosphocreatine** and **ATP** in muscle: the molecule that every cell uses as its energy currency.\n\n"
         "Later he led the teams that made **methotrexate**, a cancer medicine, and **aureomycin**, one of the first tetracycline antibiotics. Few people knew his name, but his work saved millions of lives.",
    future="Physiology and biochemistry lead to careers in medicine, nursing, pharmacy, nutrition, sports science, agriculture and biotechnology."),
  blk("s1.socratic", "socratic_question", question="Why can a single-celled amoeba get oxygen by diffusion alone, but a human cannot?",
    options=["Most human cells are far from the air, so diffusion is too slow", "Humans need less oxygen", "Amoebae do not respire"], correct_index=0,
    explanation="In a large body, most cells are not in contact with the air; diffusion over such distances is far too slow, so we need special organs for breathing and transport."),
 ]},
 {"id": "s2", "title": "Nutrition", "blocks": [
  blk("s2.reveal", "theory", title="Autotrophs and heterotrophs", revision=True,
    body="- **Autotrophic nutrition:** the organism makes its own food from simple inorganic substances, carbon dioxide and water, using sunlight. Green plants and some bacteria are **autotrophs**.\n"
         "- **Heterotrophic nutrition:** the organism takes in food made by others. Animals, fungi and most bacteria are **heterotrophs**. Some break food down outside the body (fungi such as bread mould), "
         "some take in whole food and break it down inside (amoeba, humans), and some feed on living hosts without killing them (**parasites** such as cuscuta, ticks, lice, leeches and tapeworms).\n\n"
         "**Photosynthesis** has three events:\n1. Chlorophyll absorbs light energy.\n2. Light energy becomes chemical energy, and water is split into hydrogen and oxygen.\n3. Carbon dioxide is reduced to carbohydrates.\n\n"
         f"In the presence of sunlight and chlorophyll: {E['photo']}\n\n"
         "Plants take in carbon dioxide through **stomata**, tiny pores on the leaf. Each pore is opened and closed by two **guard cells**: they swell when water flows in, opening the pore, and shrink when they lose water, closing it. "
         "Water comes from the soil through the roots; nitrogen, phosphorus, iron and magnesium are taken up from the soil as minerals."),
  blk("s2.amoeba", "theory", title="How amoeba and paramecium eat", revision=False,
    body="- **Amoeba** pushes out finger-like extensions of its cell surface (**pseudopodia**), which fuse around a food particle to form a **food vacuole**. Inside the vacuole, food is broken down and diffuses into the cytoplasm; the undigested remains are thrown out at the surface.\n"
         "- **Paramecium** has a fixed shape, so food enters at a specific spot. Movements of the **cilia** covering its body sweep food to that spot."),
  blk("s2.check", "knowledge_check", question="A destarched potted plant is kept in the dark for a day. Which of these is it unable to do?",
    options=["Make starch by photosynthesis", "Take in water through its roots", "Respire", "Lose water from its leaves"], correct_index=0,
    explanation="Photosynthesis needs sunlight; in the dark the plant still absorbs water, respires and loses some water."),
 ]},
 {"id": "s3", "title": "Nutrition in human beings", "blocks": [
  blk("s3.thm", "theory", title="The alimentary canal", revision=True,
    body="The **alimentary canal** is a long tube from the mouth to the anus. Food is pushed along it by rhythmic contraction of its muscles, called **peristalsis**.\n\n"
         "1. **Mouth:** teeth crush the food; the tongue mixes it with saliva. **Salivary amylase** breaks starch into sugar.\n"
         "2. **Oesophagus:** carries food to the stomach by peristalsis.\n"
         "3. **Stomach:** gastric glands release **hydrochloric acid** (makes the medium acidic so that **pepsin** can act), pepsin (digests proteins) and **mucus** (protects the lining from the acid). A **sphincter** muscle lets food out a little at a time.\n"
         "4. **Small intestine:** the longest part. **Bile** from the liver makes the food alkaline and breaks fats into small globules; the pancreas adds **trypsin** (proteins) and **lipase** (fats); the intestinal wall completes digestion.\n"
         "5. **Villi**, finger-like projections of the inner lining, give a huge surface for **absorption**; they are richly supplied with blood vessels.\n"
         "6. **Large intestine:** absorbs more water; the waste leaves through the anus, controlled by the anal sphincter."),
  blk("s3.table", "markdown_table", title="Digestive juices at a glance", revision=True, body=ENZYMES),
  blk("s3.check", "knowledge_check", question="Which juice makes the food alkaline and breaks fats into small globules?",
    options=["Bile", "Saliva", "Gastric juice", "Pancreatic juice"], correct_index=0,
    explanation="Bile from the liver neutralises the acid from the stomach and emulsifies fats, so that lipase can act on them."),
 ]},
 {"id": "s4", "title": "Respiration", "blocks": [
  blk("s4.thm", "theory", title="Releasing energy from food", revision=True,
    body="In every cell, glucose is first broken down in the **cytoplasm** into **pyruvate**. What happens next depends on oxygen:\n\n"
         f"- **Anaerobic** (without oxygen), in yeast: pyruvate gives ethanol and carbon dioxide (fermentation). Overall: {E['ferment']}\n"
         f"- When there is a **lack of oxygen** in our muscle cells (during hard exercise): pyruvate becomes **lactic acid**, which causes cramps. Overall: {E['lactic']}\n"
         f"- **Aerobic** (with oxygen), in the **mitochondria**: pyruvate is broken down to carbon dioxide and water, releasing much more energy. Overall: {E['aerobic']}\n\n"
         "The energy released is used to make **ATP**, the energy currency of the cell. Breaking ATP into ADP releases energy for muscle contraction, making proteins, nerve impulses and so on."),
  blk("s4.table", "markdown_table", title="Pathways of breakdown of glucose", revision=True, body=PATHWAYS),
  blk("s4.breathing", "theory", title="Breathing in humans", revision=True,
    body="- Air enters through the **nostrils**; fine hairs and mucus filter it. It passes through the **pharynx** and the **trachea** (wind-pipe), kept open by rings of **cartilage**.\n"
         "- In the lungs the trachea divides into **bronchi**, then **bronchioles**, which end in balloon-like **alveoli**. The alveoli have very thin walls and an extensive network of blood vessels; "
         "spread out, their surface would cover about 80 m².\n"
         "- **Breathing in:** the ribs are lifted and the **diaphragm** flattens, so the chest cavity becomes larger and air is sucked into the lungs. The lungs always keep some residual air, so there is time for gas exchange.\n"
         "- **Haemoglobin**, the red pigment in red blood cells, carries oxygen. Carbon dioxide is more soluble in water, so it is mostly carried dissolved in the blood.\n\n"
         "Aquatic animals get oxygen dissolved in water, which is far less than in air; so fish breathe much faster than land animals and take in water through the mouth and pass it over the gills."),
  blk("s4.check", "knowledge_check", question="Where in the cell is pyruvate broken down to carbon dioxide and water?",
    options=["Mitochondria", "Cytoplasm", "Nucleus", "Chloroplast"], correct_index=0,
    explanation="The first step, glucose to pyruvate, happens in the cytoplasm; the aerobic breakdown of pyruvate happens in the mitochondria."),
 ]},
 {"id": "s5", "title": "Transportation", "blocks": [
  blk("s5.thm", "theory", title="Blood, heart and blood vessels", revision=True,
    body="**Blood** is a fluid connective tissue: **plasma** (carries food, carbon dioxide and nitrogenous waste in dissolved form), **red blood cells** (carry oxygen), **white blood cells** (fight infection) and **platelets** (help blood to clot at a cut).\n\n"
         "The **heart** is a muscular pump about the size of a fist, with four chambers:\n"
         "- **Right side:** receives **deoxygenated** blood from the body in the right atrium and pumps it from the right ventricle to the lungs.\n"
         "- **Left side:** receives **oxygenated** blood from the lungs in the left atrium and pumps it from the left ventricle to the body.\n"
         "- **Valves** stop blood flowing backwards. The ventricles have thicker walls than the atria because they pump blood to other organs.\n\n"
         "Blood passes through the heart **twice** in one cycle of the body: **double circulation**. Separating oxygenated and deoxygenated blood gives a highly efficient supply of oxygen, which birds and mammals need to keep their body temperature constant.\n\n"
         "**Arteries** carry blood away from the heart (thick, elastic walls); **veins** bring it back (thinner walls, valves); **capillaries** are one cell thick and exchange materials with the cells. "
         "Normal blood pressure is about 120/80 mm of Hg (systolic/diastolic), measured with a sphygmomanometer.\n\n"
         "**Lymph** (tissue fluid) is formed from plasma that escapes through capillary walls into the spaces between cells. It is colourless, has fewer proteins, carries digested and absorbed fat from the intestine, and drains excess fluid back into the blood."),
  blk("s5.plants", "theory", title="Transport in plants", revision=True,
    body="- **Xylem** carries water and minerals from the roots to all parts. Root cells take up ions actively, so water moves into the root; as water evaporates from the leaves (**transpiration**), a suction (**transpiration pull**) draws water up. "
         "At night, **root pressure** is the main force. Transpiration also helps in temperature regulation.\n"
         "- **Phloem** carries food (sucrose, amino acids and other substances) from the leaves to other parts, upwards and downwards. This **translocation** uses energy from ATP to load sucrose into the phloem; "
         "water then enters by osmosis and the pressure moves the food to where it is needed."),
  blk("s5.check", "knowledge_check", question="Which chamber of the human heart pumps oxygenated blood to the body?",
    options=["Left ventricle", "Right ventricle", "Left atrium", "Right atrium"], correct_index=0,
    explanation="Oxygenated blood from the lungs enters the left atrium and is pumped to the body by the thick-walled left ventricle."),
 ]},
 {"id": "s6", "title": "Excretion", "blocks": [
  blk("s6.thm", "theory", title="Kidneys and nephrons", revision=True,
    body="The human excretory system has a pair of **kidneys**, a pair of **ureters**, a **urinary bladder** and a **urethra**. Urine formed in the kidneys flows through the ureters to the bladder, where it is stored until released through the urethra.\n\n"
         "Each kidney has many filtering units called **nephrons**:\n"
         "1. A cluster of thin-walled capillaries, the **glomerulus**, sits in a cup-shaped **Bowman's capsule**. Blood is filtered here.\n"
         "2. The filtrate passes along the **tubule**. Glucose, amino acids, salts and a major amount of water are **selectively reabsorbed** into the blood.\n"
         "3. What remains is **urine**, which goes to the collecting duct.\n\n"
         "The kidneys filter about 180 L of filtrate a day, but only 1–2 L of urine is made. The amount depends on how much excess water and dissolved waste there is in the body.\n\n"
         "If the kidneys fail, an **artificial kidney** removes waste by **dialysis**: blood flows through tubes in a dialysing fluid, and waste diffuses out. Unlike a kidney, it does not reabsorb.\n\n"
         "**Plants** get rid of oxygen and excess water through stomata; other wastes are stored in vacuoles or old xylem, removed in falling leaves, stored as gums and resins, or excreted into the soil."),
  blk("s6.check", "knowledge_check", question="In a nephron, glucose and amino acids are returned to the blood in the:",
    options=["tubule", "Bowman's capsule", "urinary bladder", "ureter"], correct_index=0,
    explanation="Blood is filtered in the glomerulus and Bowman's capsule; useful substances are reabsorbed along the tubule."),
  blk("s6.memory", "memory_trick", title="Follow the oxygen, follow the food",
    body="- **Oxygen:** nostrils → trachea → bronchi → bronchioles → alveoli → blood (haemoglobin) → left side of heart → body cells → mitochondria.\n"
         "- **Food:** mouth (starch) → stomach (proteins) → small intestine (everything finishes, absorbed by villi) → blood → cells.\n"
         "- **Waste:** blood → kidney (nephron) → ureter → bladder → urethra.\n\nIn the heart: **R**ight = **R**eturns from body, to lungs; **L**eft = from **L**ungs, to body."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing that respiration means breathing: breathing moves air; respiration releases energy from food in cells.\n"
         "- Saying that lactic acid forms in yeast: yeast makes ethanol and carbon dioxide; our muscles make lactic acid.\n"
         "- Writing that bile is an enzyme: it has no enzymes; it makes the medium alkaline and emulsifies fats.\n"
         "- Mixing up xylem and phloem: xylem carries water and minerals upwards only; phloem carries food both ways.\n"
         "- Writing that all arteries carry oxygenated blood: the pulmonary artery carries deoxygenated blood to the lungs."),
  blk("s6.tip", "teacher_tip", title="Model it in class",
    body="Ask students to blow through a straw into lime water to show carbon dioxide in exhaled air. Use a balloon in a bottle with a rubber sheet as the base to show how the diaphragm moves air. "
         "For the heart, draw the four chambers on the floor with chalk and let four students be the blood, walking the double circulation route."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why a fish breathes faster than a dog, and why the human heart keeps oxygenated and deoxygenated blood apart."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 4:** carbohydrates, fats and proteins are carbon compounds; respiration is their combustion inside the cell.\n"
         "- **Chapter 6, Control and Coordination:** nerves and hormones control these processes.\n- **Class 11 and 12 Biology:** photosynthesis, respiration and human physiology in detail."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="An athlete runs a 100 m sprint and gets cramps in the leg muscles. A day later, the pain is gone.\n\n"
         f"(a) What caused the cramps? (b) Why did they go away? (c) Why does the body make this substance and not carbon dioxide during the sprint?\n\n"
         f"**Answer:** (a) During the sprint the muscles did not get enough oxygen, so pyruvate was converted to **lactic acid**: {E['lactic']} Its build-up causes cramps. "
         "(b) With rest and enough oxygen, the lactic acid is carried away by the blood and broken down. (c) The aerobic pathway in the mitochondria needs oxygen, which was not supplied fast enough; the anaerobic pathway still gives a little energy quickly."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Life processes are nutrition, respiration, transportation and excretion.\n- Autotrophs make food by photosynthesis; heterotrophs take in food made by others.\n"
         "- In humans, digestion starts in the mouth (starch), continues in the stomach (proteins) and finishes in the small intestine, where villi absorb the food.\n"
         "- Glucose is broken down to pyruvate in the cytoplasm, then to carbon dioxide and water in the mitochondria (aerobic), or to ethanol or lactic acid without enough oxygen; the energy is stored as ATP.\n"
         "- Blood, a four-chambered heart and blood vessels give double circulation; lymph returns fluid to the blood. In plants, xylem carries water and phloem carries food.\n"
         "- Nephrons in the kidneys filter blood and make urine; plants remove waste through stomata, leaves, vacuoles, gums and resins."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Practise labelled diagrams: human digestive system, respiratory system, heart (sectional view), nephron, stomata (open and closed), and nutrition in amoeba.\n"
         "- Learn the three pathways of breakdown of glucose as a flow chart, with where each happens.\n"
         "- Name the enzyme, its gland and its substrate together: salivary amylase (starch), pepsin (proteins), trypsin (proteins), lipase (fats).\n"
         "- In difference questions (xylem/phloem, aerobic/anaerobic, artery/vein), write the points in a two-column table."),
  blk("s7.flash1", "flashcard", front="Energy currency of the cell", back="ATP (adenosine triphosphate)"),
  blk("s7.flash2", "flashcard", front="Basic filtering unit of the kidney", back="The nephron"),
  blk("s7.flash3", "flashcard", front="What is double circulation?", back="Blood passes through the heart twice in one complete cycle of the body: once to the lungs and once to the rest of the body."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Life Processes",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 5,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: 'living beings' and their basic concept of nutrition, respiration, transport and excretion in plants and animals.",
  "concepts": ["nutrition", "respiration", "transport", "excretion"], "sections": sections}

# ---------------------------------------------------------------- questions
NU, RE, TR, EX = "nutrition", "respiration", "transport", "excretion"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 5 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2 = ["1 mark: answer", "1 mark: reason or equation"]
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [RE], it("5.1", 1), "Why is diffusion insufficient to meet the oxygen requirements of multicellular organisms like humans?",
    answer_steps=["In a large multicellular body, most cells are not in direct contact with the air.", "Diffusion over such distances is far too slow to supply enough oxygen, so special organs for breathing and transport are needed."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [NU], it("5.1", 2), "What criteria do we use to decide whether something is alive?", "easy",
    answer_steps=["Visible movement, such as walking or growth, is one sign.", "But even without visible movement, living things show molecular movement: life processes such as nutrition, respiration, transport and excretion keep going."], marking_scheme=MS2P)
C.q("it1.q3", "very_short_answer", 2, [NU], it("5.1", 3), "What are outside raw materials used for by an organism?", "easy",
    answer_steps=["Food is a source of energy and of materials for growth and repair of the body.", "Oxygen is used to break down food to release energy, and water is needed for all the chemical reactions in the body."], marking_scheme=MS2P)
C.q("it1.q4", "very_short_answer", 2, [NU, RE, TR, EX], it("5.1", 4), "What processes would you consider essential for maintaining life?", "easy",
    answer_steps=["Nutrition and respiration (to get energy from food).", "Transportation and excretion (to move materials around the body and to remove wastes)."], marking_scheme=MS2P)
C.q("it2.q1", "short_answer", 3, [NU], it("5.2", 1), "What are the differences between autotrophic nutrition and heterotrophic nutrition?",
    answer_steps=["Autotrophic: the organism makes its own food from carbon dioxide and water; heterotrophic: it takes in food made by other organisms.",
                  "Autotrophic needs chlorophyll and sunlight; heterotrophic does not.", "Examples: green plants (autotrophs); animals, fungi and most bacteria (heterotrophs)."], marking_scheme=MS3)
C.q("it2.q2", "short_answer", 3, [NU], it("5.2", 2), "Where do plants get each of the raw materials required for photosynthesis?", "easy",
    answer_steps=["Carbon dioxide: from the air, through the stomata of leaves.", "Water: from the soil, absorbed by the roots and carried up by the xylem.",
                  "Sunlight is absorbed by chlorophyll in the chloroplasts; minerals such as nitrogen and magnesium come from the soil."], marking_scheme=MS3)
C.q("it2.q3", "very_short_answer", 2, [NU], it("5.2", 3), "What is the role of the acid in our stomach?", "easy",
    answer_steps=["Hydrochloric acid makes the medium in the stomach acidic, which the enzyme pepsin needs to digest proteins.", "It also kills many germs that enter with food."], marking_scheme=MS2P)
C.q("it2.q4", "very_short_answer", 2, [NU], it("5.2", 4), "What is the function of digestive enzymes?", "easy",
    answer_steps=["Digestive enzymes break down large, complex food molecules into small, simple, soluble ones.", "For example, salivary amylase breaks starch into sugar, so that it can be absorbed into the blood."], marking_scheme=MS2P)
C.q("it2.q5", "very_short_answer", 2, [NU], it("5.2", 5), "How is the small intestine designed to absorb digested food?",
    answer_steps=["Its inner lining has many finger-like projections called villi, which greatly increase the surface area for absorption.", "The villi are richly supplied with blood vessels, which carry the absorbed food to every cell."], marking_scheme=MS2P)
C.q("it3.q1", "very_short_answer", 2, [RE], it("5.3", 1), "What advantage over an aquatic organism does a terrestrial organism have with regard to obtaining oxygen for respiration?",
    answer_steps=["Air has much more oxygen than the oxygen dissolved in water.", "So a terrestrial organism gets enough oxygen with a slower breathing rate, while aquatic organisms must breathe much faster."], marking_scheme=MS2P)
C.q("it3.q2", "short_answer", 3, [RE], it("5.3", 2), "What are the different ways in which glucose is oxidised to provide energy in various organisms?",
    answer_steps=["In all cells, glucose is first broken down to pyruvate in the cytoplasm.", "Without oxygen, in yeast, pyruvate gives ethanol and carbon dioxide; with a lack of oxygen, in our muscle cells, it gives lactic acid.",
                  "With oxygen, in the mitochondria, pyruvate is broken down to carbon dioxide and water, releasing much more energy."], marking_scheme=MS3)
C.q("it3.q3", "very_short_answer", 2, [RE, TR], it("5.3", 3), "How is oxygen and carbon dioxide transported in human beings?",
    answer_steps=["Oxygen is carried by haemoglobin, the red pigment in red blood cells, from the lungs to the tissues.", "Carbon dioxide is more soluble in water, so it is mostly carried dissolved in the blood plasma from the tissues to the lungs."], marking_scheme=MS2P)
C.q("it3.q4", "very_short_answer", 2, [RE], it("5.3", 4), "How are the lungs designed in human beings to maximise the area for exchange of gases?",
    answer_steps=["The bronchioles end in millions of balloon-like alveoli; spread out, their surface would cover about 80 m².", "The alveoli have very thin walls and an extensive network of blood vessels, so gases exchange quickly."], marking_scheme=MS2P)
C.q("it4.q1", "short_answer", 3, [TR], it("5.4", 1), "What are the components of the transport system in human beings? What are the functions of these components?",
    answer_steps=["Heart: pumps blood around the body.", "Blood vessels: arteries carry blood away from the heart, veins bring it back, and capillaries exchange materials with the cells.",
                  "Blood: plasma carries food, carbon dioxide and wastes; red blood cells carry oxygen; platelets help clotting. Lymph returns tissue fluid and carries absorbed fat."], marking_scheme=MS3)
C.q("it4.q2", "very_short_answer", 2, [TR], it("5.4", 2), "Why is it necessary to separate oxygenated and deoxygenated blood in mammals and birds?",
    answer_steps=["Separation gives a highly efficient supply of oxygen to the body.", "Birds and mammals need a lot of energy to keep their body temperature constant, so they need this efficient oxygen supply."], marking_scheme=MS2P)
C.q("it4.q3", "very_short_answer", 2, [TR], it("5.4", 3), "What are the components of the transport system in highly organised plants?", "easy",
    answer_steps=["Xylem: carries water and minerals from the roots to the other parts of the plant.", "Phloem: carries food made in the leaves to the other parts of the plant."], marking_scheme=MS2P)
C.q("it4.q4", "short_answer", 3, [TR], it("5.4", 4), "How are water and minerals transported in plants?",
    answer_steps=["The xylem vessels and tracheids of roots, stems and leaves form a continuous system of water-conducting channels.",
                  "Root cells take up ions actively, so water moves into the root from the soil and is pushed up (root pressure, the main force at night).",
                  "Water evaporates from the leaves through stomata (transpiration); this creates a suction, the transpiration pull, which draws water up the xylem during the day."], marking_scheme=MS3)
C.q("it4.q5", "very_short_answer", 2, [TR], it("5.4", 5), "How is food transported in plants?",
    answer_steps=["Food (sucrose and other substances) is moved through the phloem, upwards and downwards; this is translocation.", "Energy from ATP loads sucrose into the phloem; water enters by osmosis, and the pressure moves the food to where it is needed."], marking_scheme=MS2P)
C.q("it5.q1", "short_answer", 3, [EX], it("5.5", 1), "Describe the structure and functioning of nephrons.",
    answer_steps=["Structure: a cup-shaped Bowman's capsule containing a cluster of capillaries (the glomerulus), followed by a long tubule that joins a collecting duct.",
                  "Filtration: blood is filtered in the glomerulus, and the filtrate enters Bowman's capsule.",
                  "Reabsorption: glucose, amino acids, salts and a major amount of water are reabsorbed along the tubule; the rest is urine."], marking_scheme=MS3)
C.q("it5.q2", "very_short_answer", 2, [EX], it("5.5", 2), "What are the methods used by plants to get rid of excretory products?",
    answer_steps=["Oxygen and excess water are removed through stomata.", "Other wastes are stored in vacuoles or old xylem, removed in falling leaves, stored as gums and resins, or excreted into the soil."], marking_scheme=MS2P)
C.q("it5.q3", "very_short_answer", 2, [EX], it("5.5", 3), "How is the amount of urine produced regulated?",
    answer_steps=["It depends on how much excess water and dissolved waste there is in the body.", "When the body has less water, more water is reabsorbed in the tubules and less urine is made; with excess water, more urine is made."], marking_scheme=MS2P)
# Exercises
C.mcq("ex.q1", [EX], "The kidneys in human beings are a part of the system for", ["nutrition.", "respiration.", "excretion.", "transportation."], 2, "The kidneys filter waste from the blood and make urine.", source=ex(1))
C.mcq("ex.q2", [TR], "The xylem in plants are responsible for", ["transport of water.", "transport of food.", "transport of amino acids.", "transport of oxygen."], 0, "Xylem carries water and minerals; phloem carries food.", source=ex(2))
C.mcq("ex.q3", [NU], "The autotrophic mode of nutrition requires", ["carbon dioxide and water.", "chlorophyll.", "sunlight.", "all of the above."], 3, "Photosynthesis needs carbon dioxide, water, chlorophyll and sunlight.", source=ex(3))
C.mcq("ex.q4", [RE], "The breakdown of pyruvate to give carbon dioxide, water and energy takes place in", ["cytoplasm.", "mitochondria.", "chloroplast.", "nucleus."], 1, "Aerobic breakdown of pyruvate happens in the mitochondria.", source=ex(4))
C.q("ex.q5", "short_answer", 3, [NU], ex(5), "How are fats digested in our bodies? Where does this process take place?",
    answer_steps=["Fats are digested in the small intestine.", "Bile from the liver breaks large fat globules into small ones (emulsification) and makes the medium alkaline.",
                  "Lipase from the pancreas digests the emulsified fats, and intestinal juice finally converts them into fatty acids and glycerol."], marking_scheme=MS3)
C.q("ex.q6", "very_short_answer", 2, [NU], ex(6), "What is the role of saliva in the digestion of food?", "easy",
    answer_steps=["Saliva wets the food, making it easy to chew and swallow.", "It contains the enzyme salivary amylase, which breaks down starch into sugar."], marking_scheme=MS2P)
C.q("ex.q7", "short_answer", 3, [NU], ex(7), "What are the necessary conditions for autotrophic nutrition and what are its byproducts?",
    answer_steps=["Conditions: sunlight, chlorophyll, carbon dioxide and water.", "Products: carbohydrates (glucose, stored as starch), with oxygen given out as a byproduct.",
                  "In the presence of sunlight and chlorophyll: " + E["photo"]], marking_scheme=["1 mark: conditions", "1 mark: byproducts", "1 mark: equation"])
C.q("ex.q8", "short_answer", 3, [RE], ex(8), "What are the differences between aerobic and anaerobic respiration? Name some organisms that use the anaerobic mode of respiration.",
    answer_steps=["Aerobic respiration uses oxygen and happens in the mitochondria; anaerobic respiration happens without oxygen, in the cytoplasm.",
                  "Aerobic respiration gives carbon dioxide and water and much more energy; anaerobic respiration gives ethanol and carbon dioxide (or lactic acid) and less energy.",
                  "Organisms: yeast, some bacteria, and tapeworm (our muscle cells also respire anaerobically for a short time)."], marking_scheme=MS3)
C.q("ex.q9", "very_short_answer", 2, [RE], ex(9), "How are the alveoli designed to maximise the exchange of gases?",
    answer_steps=["There are millions of alveoli, giving a very large surface (about 80 m²) for exchange.", "Their walls are very thin and have an extensive network of capillaries, so gases diffuse quickly between air and blood."], marking_scheme=MS2P)
C.q("ex.q10", "very_short_answer", 2, [RE, TR], ex(10), "What would be the consequences of a deficiency of haemoglobin in our bodies?",
    answer_steps=["Haemoglobin carries oxygen, so less oxygen reaches the cells and less energy is released.", "The person feels tired and weak, looks pale and gets breathless easily: a condition called anaemia."], marking_scheme=MS2P)
C.q("ex.q11", "long_answer", 5, [TR], ex(11), "Describe double circulation of blood in human beings. Why is it necessary?", "hard",
    answer_steps=["Deoxygenated blood from the body enters the right atrium, passes to the right ventricle and is pumped to the lungs.",
                  "In the lungs it takes in oxygen and gives up carbon dioxide; the oxygenated blood returns to the left atrium.",
                  "From the left atrium it passes to the left ventricle and is pumped to the rest of the body.",
                  "So blood passes through the heart twice in one cycle of the body: this is double circulation. Valves prevent backflow.",
                  "It keeps oxygenated and deoxygenated blood apart, giving an efficient oxygen supply, which humans need for their high energy use and constant body temperature."],
    marking_scheme=["1 mark: right side", "1 mark: lungs", "1 mark: left side", "1 mark: definition", "1 mark: need"])
C.q("ex.q12", "short_answer", 3, [TR], ex(12), "What are the differences between the transport of materials in xylem and phloem?",
    answer_steps=["Xylem carries water and minerals; phloem carries food (sucrose, amino acids).", "Xylem transport is only upwards, from roots to leaves; phloem transport is both upwards and downwards.",
                  "Xylem transport needs no energy from the cells (transpiration pull, root pressure); phloem transport uses energy from ATP."], marking_scheme=MS3)
C.q("ex.q13", "long_answer", 5, [RE, EX], ex(13), "Compare the functioning of alveoli in the lungs and nephrons in the kidneys with respect to their structure and functioning.", "hard",
    answer_steps=["Structure, alveoli: tiny balloon-like sacs at the ends of the bronchioles, with very thin walls and a network of capillaries.",
                  "Structure, nephrons: a Bowman's capsule with a glomerulus (cluster of capillaries) and a long tubule, also surrounded by capillaries.",
                  "Function, alveoli: exchange of gases; oxygen diffuses into the blood and carbon dioxide out of it.",
                  "Function, nephrons: filtration of blood, reabsorption of useful substances and formation of urine.",
                  "Both have a very large surface area and thin walls in close contact with blood capillaries."],
    marking_scheme=["1 mark: alveoli structure", "1 mark: nephron structure", "1 mark: alveoli function", "1 mark: nephron function", "1 mark: similarity"])
# CBSE sample paper
C.mcq("sqp1", [NU], "Select the group in which all organisms have the same mode of nutrition.",
      ["Cuscuta, yeast, legumes, leeches and tapeworm", "Cactus, ticks, lice, leeches and cow", "Cuscuta, ticks, lice, leeches and tapeworm", "Cactus, grass, lice, lion and tapeworm"], 2,
      "Cuscuta, ticks, lice, leeches and tapeworm are all parasites.", "medium", source=SQP(1))
C.mcq("sqp2", [RE], "Which of the following options indicates the products formed after breakdown of the glucose in our muscle cells when there is lack of oxygen?",
      ["Ethanol + carbon dioxide + Energy", "Lactic acid + Energy", "Lactic acid + carbon monoxide + Energy", "Carbon dioxide + Water + Energy"], 1,
      "With a lack of oxygen, our muscle cells convert pyruvate into lactic acid, releasing a little energy.", source=SQP(2))
C.q("sqp10", "very_short_answer", 2, [EX], SQP(10), "Unlike animals, plants do not have any excretory products as they do not eat food. Comment upon the statement with justification.",
    answer_steps=["The statement is wrong: plants do produce excretory products, but get rid of them in different ways from animals.",
                  "Oxygen and excess water are removed through stomata; other wastes are stored in vacuoles, dead cells, gums and resins, or removed in falling leaves."], marking_scheme=MS2P)
C.q("sqp11a", "very_short_answer", 2, [TR], SQP("11(A)"), "How many chambers are there in the heart of the following organisms? How is mixing of oxygenated and deoxygenated blood prevented in their body?\n\n(i) Fishes\n\n(ii) Humans",
    answer_steps=["(i) Fishes: two chambers. Blood is pumped to the gills, oxygenated there and passes directly to the rest of the body, so it goes through the heart only once.",
                  "(ii) Humans: four chambers. The septum separates the right and left sides of the heart, preventing mixing."], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
C.q("sqp11b", "very_short_answer", 2, [TR], SQP("11(B)"), "Explain the mechanism by which the water is transported in plants?",
    answer_steps=["Roots take up ions actively, creating a concentration difference, so water moves from the soil into the root xylem.",
                  "Transpiration from the leaves creates a suction (transpiration pull) in the xylem tracheids and vessels, which draws water upwards."], marking_scheme=MS2P)
C.q("sqp15", "case_based", 4, [NU], SQP(15),
    "Neha consumed boiled sweet potatoes and boiled eggs for breakfast. Help her to understand some steps in the process of digestion of the food taken by her.\n\n"
    "(i) Which of these food items is rich in proteins? In which part of the alimentary canal is the digestion of this component initiated? Name the enzymes, conditions required and the glands associated with the digestion here. "
    "OR Which of these food items contains fats? How is it digested? (2)\n\n(ii) Which of these food items is rich in starch? How is its digestion initiated? (1)\n\n"
    "(iii) In which part of the alimentary canal will the maximum amount of digested food be present as soon as the process of digestion is completed? (1)",
    answer_steps=["(i) Eggs are rich in proteins. Their digestion starts in the stomach: gastric glands in the stomach wall release hydrochloric acid, the enzyme pepsin and mucus; the acid makes the medium acidic so that pepsin can act. "
                  "OR Eggs contain fats. Bile from the liver breaks large fat globules into smaller ones and makes the medium alkaline; lipase from the pancreas digests the emulsified fats.",
                  "(ii) Sweet potatoes are rich in starch. Salivary amylase in saliva, from the salivary glands in the mouth, starts breaking starch into sugar.",
                  "(iii) The small intestine, because digestion is completed there."],
    marking_scheme=["(i) 2 marks", "(ii) 1 mark", "(iii) 1 mark"])
# GSEB
C.mcq("gseb2025_4", [RE], "The lungs in human beings are a part of the system for ____.", ["nutrition", "transportation", "excretion", "respiration"], 3,
      "The lungs take in oxygen and give out carbon dioxide: they belong to the respiratory system.", source=gseb(2025, "4"))
C.mcq("gseb2025_9", [RE], "In anaerobic respiration by our muscle cells, the pyruvate is converted into ____.", ["ethanol", "acetic acid", "lactic acid"], 2,
      "With a lack of oxygen, muscle cells make lactic acid; yeast makes ethanol.", source=gseb(2025, "9"))
C.q("gseb2025_27", "very_short_answer", 2, [NU], gseb(2025, "27"), "Explain nutrition in Amoeba.",
    answer_steps=["Amoeba takes in food using temporary finger-like extensions of the cell surface (pseudopodia), which fuse over the food particle to form a food vacuole.",
                  "Inside the food vacuole, complex substances are broken down into simpler ones, which diffuse into the cytoplasm; the undigested material is moved to the surface and thrown out."], marking_scheme=MS2P)
C.q("gseb2025_36", "very_short_answer", 2, [RE], gseb(2025, "36"), "State the organs of human respiratory system.", "easy",
    answer_steps=["Nostrils (nasal passage), pharynx, larynx and trachea (wind-pipe).", "Bronchi, bronchioles and the lungs, with the alveoli; the diaphragm and ribs help in breathing."], marking_scheme=MS2P)
C.q("gseb2025_50", "short_answer", 3, [TR], gseb(2025, "50", 4), "(a) Write short note on Lymph.\n\n(b) What are the components of the transport system in highly organised plants? Write their functions also.",
    answer_steps=["(a) Lymph is a colourless fluid formed from plasma, proteins and blood cells that escape through the pores of capillaries into the spaces between cells; it has less protein than plasma.",
                  "It carries digested and absorbed fat from the intestine and drains excess fluid from the spaces between cells back into the blood.",
                  "(b) Xylem carries water and minerals from the roots to the other parts; phloem carries food from the leaves to the other parts."], marking_scheme=["1 mark: lymph", "1 mark: functions of lymph", "1 mark: xylem and phloem"])
C.q("gseb2025_51", "short_answer", 3, [NU, EX], gseb(2025, "51", 4), "(a) What are the differences between autotrophic nutrition and heterotrophic nutrition?\n\n(b) Draw a neat and labelled structure of a nephron.",
    answer_steps=["(a) Autotrophs make their own food from carbon dioxide and water using sunlight and chlorophyll (green plants); heterotrophs take in food made by others (animals, fungi).",
                  "(b) Labels: Bowman's capsule (cup-shaped), glomerulus (cluster of capillaries inside it), tubule, collecting duct, and the branch of the renal artery and the renal vein.",
                  "Blood is filtered from the glomerulus into Bowman's capsule; useful substances are reabsorbed along the tubule."], marking_scheme=["1 mark: (a)", "1 mark: labels", "1 mark: diagram"])
# Shine MCQs
C.mcq("mcq01", [NU], "In which part of the alimentary canal does the digestion of starch begin?", ["Mouth", "Stomach", "Small intestine", "Large intestine"], 0, "Salivary amylase in the mouth starts breaking starch into sugar.")
C.mcq("mcq02", [NU], "Opening and closing of the stomatal pore is controlled by:", ["guard cells", "root hairs", "xylem vessels", "chloroplasts alone"], 0, "Guard cells swell when water flows in, opening the pore, and shrink to close it.")
C.mcq("mcq03", [NU], "Which enzyme of pancreatic juice digests proteins?", ["Trypsin", "Lipase", "Salivary amylase", "Pepsin"], 0, "Trypsin from the pancreas digests proteins; pepsin is from the stomach.", "medium")
C.mcq("mcq04", [RE], "The energy currency of the cell is:", ["ATP", "Glucose", "Pyruvate", "ADP"], 0, "Energy released in respiration is stored as ATP; breaking ATP into ADP releases it for use.")
C.mcq("mcq05", [RE], "Yeast, in the absence of oxygen, converts pyruvate into:", ["ethanol and carbon dioxide", "lactic acid", "carbon dioxide and water", "glucose"], 0, "This is fermentation: " + E["ferment"])
C.mcq("mcq06", [TR], "Which blood vessel carries deoxygenated blood from the heart to the lungs?", ["Pulmonary artery", "Pulmonary vein", "Aorta", "Vena cava"], 0,
      "The pulmonary artery leaves the right ventricle carrying deoxygenated blood to the lungs.", "medium")
C.mcq("mcq07", [TR], "How many chambers does the heart of a fish have?", ["Two", "Three", "Four", "One"], 0, "A fish heart has two chambers; blood goes through it only once in each cycle.")
C.mcq("mcq08", [TR], "The upward movement of water in tall trees during the day is mainly due to:", ["transpiration pull", "root pressure", "gravity", "translocation"], 0,
      "Evaporation from the leaves creates the suction that draws water up; root pressure matters more at night.", "medium")
C.mcq("mcq09", [EX], "The basic filtering unit of the kidney is the:", ["nephron", "neuron", "alveolus", "villus"], 0, "Each kidney has many nephrons, which filter the blood.")
C.mcq("mcq10", [EX], "A patient whose kidneys have failed is treated by:", ["dialysis", "transfusion", "vaccination", "photosynthesis"], 0, "An artificial kidney removes nitrogenous waste from the blood by dialysis.")
# Assertion-reason
C.ar("ar1", [NU], "Bile juice does not contain any digestive enzyme, yet it helps in digestion.", "Bile breaks large fat globules into smaller ones and makes the medium alkaline.", 0,
     "Emulsifying fats and making the medium alkaline help lipase to act: R explains A.")
C.ar("ar2", [TR], "The walls of the ventricles are thicker than the walls of the atria.", "The ventricles pump blood to the various organs of the body.", 0,
     "Pumping blood to the organs needs more force, so the ventricles have thicker muscular walls: R explains A.")
C.ar("ar3", [RE], "Aquatic organisms breathe faster than terrestrial organisms.", "The amount of dissolved oxygen in water is fairly low compared to the amount of oxygen in air.", 0,
     "Because water holds little oxygen, aquatic organisms must move more water over their gills: R explains A.")
C.ar("ar4", [TR], "Arteries carry oxygenated blood to all organs.", "Arteries carry blood away from the heart.", 3,
     "A is false: the pulmonary artery carries deoxygenated blood to the lungs. R is true.")
C.ar("ar5", [EX], "The kidneys make about 180 L of filtrate a day but only 1 to 2 L of urine.", "Most of the water in the filtrate is reabsorbed in the tubules.", 0,
     "Selective reabsorption returns most of the water to the blood: R explains A.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [NU], SHINE, "What are the three events that occur during photosynthesis?", "easy",
    answer_steps=["(i) Chlorophyll absorbs light energy. (ii) Light energy is converted to chemical energy and water is split into hydrogen and oxygen.", "(iii) Carbon dioxide is reduced to carbohydrates."],
    marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [TR], SHINE, "State two functions of lymph.", "easy",
    answer_steps=["It carries digested and absorbed fat from the intestine.", "It drains excess fluid from the spaces between cells back into the blood."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [RE], SHINE, "Show the three pathways of breakdown of glucose with the help of a flow chart, stating where each occurs.",
    answer_steps=["Glucose (6-carbon) is broken down in the cytoplasm into pyruvate (3-carbon) and a little energy.",
                  "Without oxygen (yeast): pyruvate gives ethanol, carbon dioxide and a little energy. Lack of oxygen (our muscle cells): pyruvate gives lactic acid and a little energy.",
                  "With oxygen (mitochondria): pyruvate gives carbon dioxide, water and a lot of energy."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [NU], SHINE, "Describe how stomata open and close. Give two functions of stomata.",
    answer_steps=["Each stomatal pore is surrounded by two guard cells. When water flows into the guard cells they swell and the pore opens; when they lose water they shrink and the pore closes.",
                  "Function 1: exchange of gases (carbon dioxide in, oxygen out) for photosynthesis.", "Function 2: loss of water vapour by transpiration, which helps in the upward movement of water."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [NU], SHINE, "Describe the process of digestion of food in human beings, from the mouth to the large intestine.", "medium",
    answer_steps=["Mouth: teeth chew the food; salivary amylase in saliva breaks starch into sugar.",
                  "Stomach: hydrochloric acid makes the medium acidic; pepsin digests proteins; mucus protects the lining.",
                  "Small intestine: bile makes the food alkaline and emulsifies fats; trypsin digests proteins and lipase digests fats; intestinal juice converts them into amino acids, glucose, fatty acids and glycerol.",
                  "Villi of the small intestine absorb the digested food into the blood.", "Large intestine: absorbs water; the waste is removed through the anus."],
    marking_scheme=["1 mark: mouth", "1 mark: stomach", "1 mark: small intestine", "1 mark: absorption", "1 mark: large intestine"])
C.q("la2", "long_answer", 5, [EX], SHINE, "Describe the human excretory system. How is urine formed in a nephron? What is dialysis?", "medium",
    answer_steps=["The excretory system has two kidneys, two ureters, a urinary bladder and a urethra.",
                  "In each nephron, blood is filtered from the glomerulus into Bowman's capsule.", "Glucose, amino acids, salts and a major amount of water are reabsorbed along the tubule; the rest is urine.",
                  "Urine flows through the ureters to the bladder, where it is stored, and is released through the urethra.",
                  "Dialysis: when the kidneys fail, an artificial kidney removes nitrogenous waste from the blood as it flows through tubes in a dialysing fluid."],
    marking_scheme=["1 mark: organs", "1 mark: filtration", "1 mark: reabsorption", "1 mark: path of urine", "1 mark: dialysis"])
C.q("cb1", "case_based", 4, [RE], SHINE,
    "During a school race, Kabir ran very fast and got painful cramps in his legs. His teacher explained that his muscles were not getting enough oxygen. Meanwhile, in the school kitchen, yeast was added to dough, which rose and smelled slightly of alcohol.\n\n"
    "(i) Which substance caused the cramps in Kabir's legs? (1)\n\n(ii) Why did the dough rise? (1)\n\n(iii) Where in the cell is pyruvate broken down when enough oxygen is available, and what are the products? OR Why does aerobic respiration release more energy than anaerobic respiration? (2)",
    answer_steps=["(i) Lactic acid, formed from pyruvate when there is a lack of oxygen in the muscle cells.", "(ii) Yeast respires anaerobically and releases carbon dioxide, which makes the dough rise.",
                  "(iii) In the mitochondria; the products are carbon dioxide, water and a lot of energy. OR In aerobic respiration glucose is broken down completely to carbon dioxide and water; in anaerobic respiration it is broken down only partly."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [TR], SHINE,
    "At a health camp, a doctor measured Meera's grandfather's blood pressure as 150/95 mm of Hg, and told the class that normal blood pressure is about 120/80 mm of Hg. She also explained that the heart has four chambers and that the blood goes through it twice.\n\n"
    "(i) Name the instrument used to measure blood pressure. (1)\n\n(ii) Is the grandfather's blood pressure normal? (1)\n\n(iii) Which side of the heart receives deoxygenated blood, and where is it sent? OR Why do veins have valves? (2)",
    answer_steps=["(i) Sphygmomanometer.", "(ii) No: it is higher than normal (high blood pressure, hypertension).",
                  "(iii) The right side: the right atrium receives deoxygenated blood from the body, and the right ventricle pumps it to the lungs. OR Blood in veins is under low pressure; valves make sure it flows only towards the heart."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch05.q.ex."))
