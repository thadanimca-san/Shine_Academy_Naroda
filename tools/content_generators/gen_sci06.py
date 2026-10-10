"""CBSE Class 10 Science Ch 6: Control and Coordination. No equations in this chapter."""
import sys
from sci_common import Chapter, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch06"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch06_control_and_coordination"
C = Chapter("sci10ch06")
blk = C.blk

PLANT_HORMONES = ("| Hormone | Main effect |\n|---|---|\n| Auxin | made at the shoot tip; makes cells grow longer (bending towards light, tendrils coiling) |\n"
                  "| Gibberellins | help in the growth of the stem |\n| Cytokinins | promote cell division; present in fruits and seeds |\n| Abscisic acid | inhibits growth; causes wilting of leaves |")
GLANDS = ("| Gland | Hormone | Function |\n|---|---|---|\n| Hypothalamus | releasing hormones | control the release of hormones from the pituitary |\n"
          "| Pituitary | growth hormone | growth and development (too little: dwarfism; too much: gigantism) |\n"
          "| Thyroid | thyroxin (needs iodine) | metabolism of carbohydrates, proteins and fats (lack of iodine: goitre) |\n"
          "| Pancreas | insulin | lowers the blood sugar level (too little: diabetes) |\n| Adrenal | adrenaline | prepares the body for emergencies |\n"
          "| Testes | testosterone | changes at puberty in boys |\n| Ovaries | oestrogen | changes at puberty in girls |")
COMPARE = ("| Nervous control | Hormonal control |\n|---|---|\n| electrical impulses along nerves | chemicals carried in the blood |\n"
           "| very fast | slower |\n| reaches only cells connected by nerves | reaches all cells of the body |\n| short-lived; a cell needs time to reset | steady and long-lasting |")

sections = [
 {"id": "s1", "title": "Why control and coordination?", "blocks": [
  blk("s1.hook", "hook", title="Catch!",
    body="A friend throws a ball to you without warning. In less than a second your eyes see it, your brain works out where it will go, your arm moves, and your fingers close around it.\n\n"
         "Many organs worked together, in the right order, very fast. This is **control and coordination**. Animals use the **nervous system** and **hormones**; plants, which have no nerves, use **chemicals** alone. "
         "In this chapter you will learn how both work."),
  blk("s1.inspiration", "inspiration", title="He showed that plants respond", person="Jagadish Chandra Bose", years="1858–1937",
    body="Jagadish Chandra Bose of Bengal was a physicist and a plant scientist. He built the **crescograph**, an instrument that could magnify the tiny growth of a plant thousands of times, "
         "and showed that plants respond to touch, light and other stimuli with electrical signals, much as animal tissues do.\n\n"
         "He was also a pioneer of radio and microwave research. The Bose Institute in Kolkata, which he founded in 1917, still carries on his work.",
    future="The study of nerves, hormones and plant responses leads to careers in medicine, neuroscience, psychology, sports science, agriculture and plant biotechnology."),
  blk("s1.socratic", "socratic_question", question="You touch a very hot plate and pull your hand back before you even feel the pain. Which part decided to move your hand?",
    options=["The spinal cord", "The fore-brain, after thinking", "The muscles of the hand themselves"], correct_index=0,
    explanation="This is a reflex action: the decision is made in the spinal cord, which is quicker than sending the signal up to the brain and waiting for thinking."),
 ]},
 {"id": "s2", "title": "The nervous system", "blocks": [
  blk("s2.reveal", "theory", title="Neurons and reflexes", revision=True,
    body="The nervous system is made of nerve cells, **neurons**. Information from the environment is detected by **receptors**, for example in the inner ear (hearing and balance), nose (smell), tongue (taste) and eyes (sight).\n\n"
         "**How a message travels:**\n1. Information reaches the tip of a **dendrite** and starts a chemical reaction that creates an **electrical impulse**.\n"
         "2. The impulse travels from the dendrite to the **cell body**, and then along the **axon** to its end.\n"
         "3. At the end of the axon, the impulse releases chemicals. These cross the gap between two neurons, the **synapse**, and start a similar impulse in the dendrite of the next neuron.\n"
         "4. Finally the message reaches a muscle or gland (the **effector**), which acts.\n\n"
         "A **reflex action** is a sudden, automatic response to a stimulus, done without thinking, such as pulling back the hand from a flame. Its path is the **reflex arc**: "
         "receptor → sensory neuron → relay neuron in the **spinal cord** → motor neuron → effector (muscle). Reflex arcs are formed in the spinal cord, so the response is quick; the information also goes on to the brain."),
  blk("s2.check", "knowledge_check", question="The gap between two neurons, where chemicals carry the message across, is called the:",
    options=["synapse", "axon", "dendrite", "cell body"], correct_index=0,
    explanation="At the synapse, chemicals released by the axon ending start a new impulse in the next neuron."),
 ]},
 {"id": "s3", "title": "The human brain", "blocks": [
  blk("s3.thm", "theory", title="Three parts of the brain", revision=True,
    body="The brain and the spinal cord form the **central nervous system**. The nerves from them to all parts of the body form the **peripheral nervous system**.\n\n"
         "- **Fore-brain:** the main thinking part. It has areas that receive sensory impulses (hearing, smell, sight), areas that control voluntary muscles, and areas that store information. It also has the centre for **hunger**.\n"
         "- **Mid-brain** and **hind-brain:** control many **involuntary** actions. The **medulla** in the hind-brain controls blood pressure, salivation and vomiting. "
         "The **cerebellum** in the hind-brain controls **posture and balance** and the precision of voluntary actions, such as walking in a straight line, riding a bicycle or picking up a pencil.\n\n"
         "**Protection:** the brain sits inside a bony box, the **skull**, cushioned by a fluid-filled balloon that absorbs shocks. The spinal cord is protected by the **vertebral column** (backbone).\n\n"
         "**Movement:** when a nerve impulse reaches a muscle, special proteins in the muscle cells change their shape and arrangement, and the muscle fibre becomes shorter."),
  blk("s3.check", "knowledge_check", question="Which part of the brain maintains posture and balance of the body?",
    options=["Cerebellum", "Medulla", "Fore-brain", "Pons"], correct_index=0,
    explanation="The cerebellum, in the hind-brain, controls posture, balance and the precision of voluntary actions."),
 ]},
 {"id": "s4", "title": "Coordination in plants", "blocks": [
  blk("s4.thm", "theory", title="Movements without nerves", revision=True,
    body="Plants have neither a nervous system nor muscles. They respond to stimuli in two ways:\n\n"
         "**1. Immediate movement, not due to growth.** The leaves of the **sensitive plant** (touch-me-not, Mimosa) fold up when touched. Plant cells pass the information from cell to cell electrically and chemically; "
         "the cells then change shape by changing the amount of water in them, so they swell or shrink.\n\n"
         "**2. Slow movement due to growth (tropisms):** the direction of growth depends on the stimulus.\n"
         "- **Phototropism** (light): shoots bend towards light; roots grow away from it.\n- **Geotropism** (gravity): roots grow downwards; shoots grow upwards.\n"
         "- **Hydrotropism** (water): roots grow towards water.\n- **Chemotropism** (chemicals): pollen tubes grow towards the ovules.\n\n"
         "**How a shoot bends towards light:** the hormone **auxin** is made at the shoot tip. When light comes from one side, auxin diffuses to the shady side. "
         "There it makes the cells grow longer, so the shoot bends towards the light. In the same way, a **tendril** coils around a support: the part away from the support grows faster than the part touching it."),
  blk("s4.table", "markdown_table", title="Plant hormones", revision=True, body=PLANT_HORMONES),
  blk("s4.check", "knowledge_check", question="A plant hormone that inhibits growth and causes wilting of leaves is:",
    options=["abscisic acid", "auxin", "gibberellin", "cytokinin"], correct_index=0,
    explanation="Abscisic acid inhibits growth; the other three promote growth or cell division."),
 ]},
 {"id": "s5", "title": "Hormones in animals", "blocks": [
  blk("s5.thm", "theory", title="Chemical messengers", revision=True,
    body="**Hormones** are chemicals made by **endocrine glands** and released directly into the **blood**, which carries them to all parts of the body. They act only on cells that have the right receptors.\n\n"
         "**Adrenaline** from the adrenal glands prepares the body for an emergency (fight or flight): the heart beats faster to supply more oxygen to the muscles, blood to the digestive system and skin is reduced, "
         "blood is diverted to the skeletal muscles, and breathing becomes faster because the diaphragm and rib muscles contract more.\n\n"
         "**Iodised salt** is advised because iodine is needed to make **thyroxin**. Without enough iodine, a person may suffer from **goitre**, a swollen neck.\n\n"
         "**Insulin** from the pancreas lowers the blood sugar level. If it is not secreted in proper amounts, sugar in the blood rises (**diabetes**); such patients are given injections of insulin."),
  blk("s5.table", "markdown_table", title="Endocrine glands and their hormones", revision=True, body=GLANDS),
  blk("s5.check", "knowledge_check", question="Which hormone needs iodine for its synthesis?",
    options=["Thyroxin", "Insulin", "Adrenaline", "Growth hormone"], correct_index=0,
    explanation="The thyroid gland needs iodine to make thyroxin; lack of iodine can cause goitre."),
 ]},
 {"id": "s6", "title": "Nerves and hormones together", "blocks": [
  blk("s6.thm", "theory", title="Feedback and comparison", revision=True,
    body="**Feedback mechanism:** the timing and amount of a hormone are regulated by feedback. For example, when the sugar level in the blood rises, cells of the pancreas detect it and secrete more insulin; "
         "as the sugar level falls, insulin secretion is reduced.\n\n" + COMPARE),
  blk("s6.check", "knowledge_check", question="Which of these is true of hormonal control compared with nervous control?",
    options=["It reaches all cells of the body through the blood", "It is faster", "It uses electrical impulses", "It reaches only cells connected by nerves"], correct_index=0,
    explanation="Hormones travel in the blood and reach every cell; nerve impulses are faster but reach only the cells they are connected to."),
  blk("s6.memory", "memory_trick", title="Remember the path and the parts",
    body="- **Reflex arc:** **R**eceptor → **S**ensory → **R**elay (spinal cord) → **M**otor → **E**ffector: \"**R**ats **S**ometimes **R**un **M**any **E**rrands\".\n"
         "- **Hind-brain:** **C**erebellum = **C**ontrol of balance; **M**edulla = **M**achine jobs (blood pressure, salivation, vomiting).\n"
         "- **Plant hormones:** **A**uxin = **A**rches towards light; **G**ibberellin = **G**rows stem; **C**ytokinin = **C**ell division; **A**bscisic acid = **A**rrests growth."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing that reflex actions are controlled by the brain: the reflex arc is in the spinal cord.\n"
         "- Saying that Mimosa leaves fold because of growth: they fold because cells lose water and change shape.\n"
         "- Writing that insulin is made by the pituitary: it is made by the pancreas.\n"
         "- Mixing up dendrite and axon: the impulse goes dendrite → cell body → axon.\n"
         "- Writing that the cerebrum controls balance: the cerebellum does."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="Do the ruler-drop test: one student holds a ruler, another catches it when it falls; the distance shows reaction time. Tap below the knee to show the knee-jerk reflex. "
         "Grow a seedling in a box with a hole on one side to show phototropism over a week, and bring a touch-me-not plant to class."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend how your body reacts when a dog suddenly barks at you: which actions are reflexes, which are controlled by the brain, and what adrenaline does."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 5:** adrenaline changes breathing and heartbeat; insulin controls the use of glucose.\n- **Chapter 7, How do Organisms Reproduce?:** testosterone and oestrogen bring changes at puberty.\n"
         "- **Class 11 and 12 Biology:** neural control, chemical coordination and plant growth regulators in detail."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A potted plant is kept near a window. After a week its shoot has bent towards the window. The pot is then turned around by 180°.\n\n"
         "(a) What will happen to the shoot over the next few days? (b) Which hormone is responsible, and where is it made? (c) Will the roots respond in the same way?\n\n"
         "**Answer:** (a) The shoot will bend back towards the window, because the light now comes from the other side. (b) Auxin, made at the shoot tip; it moves to the shady side and makes those cells grow longer. "
         "(c) No: roots are negatively phototropic and grow away from light, mainly responding to gravity and water."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Control and coordination are done by the nervous system and hormones in animals, and by chemicals in plants.\n"
         "- A message travels as an electrical impulse from dendrite to cell body to axon, and crosses the synapse as chemicals.\n"
         "- Reflex actions are fast, automatic and controlled by the spinal cord through the reflex arc.\n"
         "- The fore-brain is for thinking; the medulla controls involuntary actions; the cerebellum controls posture and balance.\n"
         "- Plants respond by quick movements (Mimosa) or by growth (tropisms), using hormones such as auxin, gibberellins, cytokinins and abscisic acid.\n"
         "- Endocrine glands release hormones into the blood; their amount is regulated by feedback."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Practise labelled diagrams of a neuron, the reflex arc and the human brain.\n- Learn the endocrine glands table: gland, hormone, function, and the disorder when it goes wrong.\n"
         "- In tropism answers, name the stimulus, the direction of growth, and the hormone.\n- Use a table for differences: nervous vs hormonal control, Mimosa movement vs growth movement."),
  blk("s7.flash1", "flashcard", front="Path of a nerve impulse in a neuron", back="Dendrite → cell body → axon → synapse → next neuron"),
  blk("s7.flash2", "flashcard", front="What is phototropism?", back="Growth movement of a plant part in response to light: shoots bend towards light, roots away from it."),
  blk("s7.flash3", "flashcard", front="Why is iodised salt advised?", back="Iodine is needed by the thyroid to make thyroxin; lack of it can cause goitre."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Control and Coordination",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 6,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: tropic movements in plants; introduction of plant hormones; control and coordination in animals: nervous system; voluntary, involuntary and reflex action; chemical coordination: animal hormones.",
  "concepts": ["nervous_system", "plant_coordination", "hormones"], "sections": sections}

# ---------------------------------------------------------------- questions
NS, PC, HO = "nervous_system", "plant_coordination", "hormones"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 6 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [NS], it("6.1", 1), "What is the difference between a reflex action and walking?", "easy",
    answer_steps=["A reflex action is sudden, automatic and done without thinking; it is controlled by the spinal cord.", "Walking is a voluntary action: we decide to do it, and it is controlled by the brain (with the cerebellum keeping balance)."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [NS], it("6.1", 2), "What happens at the synapse between two neurons?",
    answer_steps=["The electrical impulse at the end of the axon releases some chemicals.", "These chemicals cross the synapse and start a similar electrical impulse in a dendrite of the next neuron."], marking_scheme=MS2P)
C.q("it1.q3", "very_short_answer", 2, [NS], it("6.1", 3), "Which part of the brain maintains posture and equilibrium of the body?", "easy",
    answer_steps=["The cerebellum.", "It is a part of the hind-brain and also controls the precision of voluntary actions."], marking_scheme=["1 mark: answer", "1 mark: location"])
C.q("it1.q4", "very_short_answer", 2, [NS], it("6.1", 4), "How do we detect the smell of an agarbatti (incense stick)?",
    answer_steps=["Smell receptors (olfactory receptors) in the nose detect the chemicals of the smoke.", "They send impulses through nerves to the fore-brain, which interprets them as the smell of the agarbatti."], marking_scheme=MS2P)
C.q("it1.q5", "very_short_answer", 2, [NS], it("6.1", 5), "What is the role of the brain in reflex action?",
    answer_steps=["The reflex action itself is decided in the spinal cord; the brain is not needed for the quick response.", "But the information also reaches the brain, which becomes aware of what happened and can use it for thinking and later actions."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [PC], it("6.2", 1), "What are plant hormones?", "easy",
    answer_steps=["Plant hormones are chemical compounds made by plants that help to coordinate growth, development and responses to the environment.", "Examples: auxin, gibberellins, cytokinins and abscisic acid."], marking_scheme=["1 mark: definition", "1 mark: examples"])
C.q("it2.q2", "short_answer", 3, [PC], it("6.2", 2), "How is the movement of leaves of the sensitive plant different from the movement of a shoot towards light?",
    answer_steps=["Sensitive plant: the movement is immediate and is not due to growth; cells change shape by changing the amount of water in them.",
                  "Shoot towards light: the movement is slow and is due to growth (phototropism).", "It is directional, caused by auxin making the cells on the shady side grow longer."], marking_scheme=MS3)
C.q("it2.q3", "very_short_answer", 2, [PC], it("6.2", 3), "Give an example of a plant hormone that promotes growth.", "easy",
    answer_steps=["Auxin (it makes cells grow longer).", "Gibberellins also promote the growth of the stem."], marking_scheme=["1 mark: answer", "1 mark: example of effect"])
C.q("it2.q4", "very_short_answer", 2, [PC], it("6.2", 4), "How do auxins promote the growth of a tendril around a support?",
    answer_steps=["When a tendril touches a support, auxin moves to the side away from the support.", "The cells on that side grow longer than those touching the support, so the tendril coils around it."], marking_scheme=MS2P)
C.q("it2.q5", "short_answer", 3, [PC], it("6.2", 5), "Design an experiment to demonstrate hydrotropism.", "hard",
    answer_steps=["Plant a few seeds in a box of dry soil, and place a small porous clay pot full of water in the soil on one side.",
                  "Water only the clay pot, so water seeps into the soil near it; keep the box in the same conditions for a week.",
                  "Dig out the seedlings carefully: the roots will have grown towards the clay pot, showing that roots grow towards water (hydrotropism)."],
    marking_scheme=["1 mark: set-up", "1 mark: method", "1 mark: observation"])
C.q("it3.q1", "very_short_answer", 2, [HO], it("6.3", 1), "How does chemical coordination take place in animals?",
    answer_steps=["Endocrine glands release hormones directly into the blood.", "The blood carries them to all parts of the body, where they act on specific target cells; their amount is controlled by feedback."], marking_scheme=MS2P)
C.q("it3.q2", "very_short_answer", 2, [HO], it("6.3", 2), "Why is the use of iodised salt advisable?", "easy",
    answer_steps=["Iodine is needed by the thyroid gland to make the hormone thyroxin, which regulates the metabolism of carbohydrates, proteins and fats.", "Lack of iodine can cause goitre (a swollen neck)."], marking_scheme=MS2P)
C.q("it3.q3", "short_answer", 3, [HO], it("6.3", 3), "How does our body respond when adrenaline is secreted into the blood?",
    answer_steps=["The heart beats faster, supplying more oxygen to the muscles.", "Blood supply to the digestive system and skin is reduced, and blood is diverted to the skeletal muscles.",
                  "Breathing becomes faster because of contractions of the diaphragm and rib muscles. All this prepares the body for an emergency."], marking_scheme=MS3)
C.q("it3.q4", "very_short_answer", 2, [HO], it("6.3", 4), "Why are some patients of diabetes treated by giving injections of insulin?",
    answer_steps=["In these patients the pancreas does not secrete enough insulin, so the blood sugar level stays high.", "Insulin injections lower the blood sugar level by helping the body use and store glucose."], marking_scheme=MS2P)
# Exercises
C.mcq("ex.q1", [PC], "Which of the following is a plant hormone?", ["Insulin", "Thyroxin", "Oestrogen", "Cytokinin."], 3, "Cytokinins promote cell division in plants; the others are animal hormones.", source=ex(1))
C.mcq("ex.q2", [NS], "The gap between two neurons is called a", ["dendrite.", "synapse.", "axon.", "impulse."], 1, "The synapse is the gap; chemicals carry the message across it.", source=ex(2))
C.mcq("ex.q3", [NS], "The brain is responsible for", ["thinking.", "regulating the heart beat.", "balancing the body.", "all of the above."], 3, "The fore-brain thinks, the medulla regulates the heart beat, and the cerebellum balances the body.", source=ex(3))
C.q("ex.q4", "short_answer", 3, [NS], ex(4), "What is the function of receptors in our body? Think of situations where receptors do not work properly. What problems are likely to arise?",
    answer_steps=["Receptors detect information from the environment (light, sound, smell, taste, touch, heat) and pass it to the nervous system as impulses.",
                  "If receptors do not work properly, for example the skin's heat receptors are damaged or the nose is blocked by a cold, the information is not detected.",
                  "Then the body cannot respond: we may not pull back from a hot object and get burnt, or may not smell gas leaking or food going bad."], marking_scheme=MS3)
C.q("ex.q5", "short_answer", 3, [NS], ex(5), "Draw the structure of a neuron and explain its function.",
    answer_steps=["Labels: dendrites, cell body (with nucleus), axon, and nerve ending.",
                  "Dendrites receive information and start an electrical impulse, which travels to the cell body and along the axon.",
                  "At the nerve ending, chemicals are released that pass the message across the synapse to the next neuron or to a muscle or gland."], marking_scheme=["1 mark: diagram", "1 mark: labels", "1 mark: function"])
C.q("ex.q6", "very_short_answer", 2, [PC], ex(6), "How does phototropism occur in plants?",
    answer_steps=["When light falls on a shoot from one side, auxin made at the tip diffuses to the shady side.", "Auxin makes the cells on the shady side grow longer, so the shoot bends towards the light."], marking_scheme=MS2P)
C.q("ex.q7", "very_short_answer", 2, [NS], ex(7), "Which signals will get disrupted in case of a spinal cord injury?",
    answer_steps=["Reflex actions controlled by the spinal cord will be disrupted.", "Messages between the brain and the body below the injury will also be blocked, so sensations from there will not reach the brain and the brain cannot move those muscles."], marking_scheme=MS2P)
C.q("ex.q8", "very_short_answer", 2, [PC], ex(8), "How does chemical coordination occur in plants?",
    answer_steps=["Plants make hormones (auxin, gibberellins, cytokinins, abscisic acid) in one part, which diffuse to the area of action.", "These hormones control growth, cell division, bending towards stimuli and wilting, so the plant responds as a whole."], marking_scheme=MS2P)
C.q("ex.q9", "very_short_answer", 2, [NS, HO], ex(9), "What is the need for a system of control and coordination in an organism?", "easy",
    answer_steps=["An organism has many organs that must work together, in the right order, to respond to changes in the environment.", "Control and coordination make sure the right organs act at the right time, for example the muscles moving the hand away from a flame."], marking_scheme=MS2P)
C.q("ex.q10", "very_short_answer", 2, [NS], ex(10), "How are involuntary actions and reflex actions different from each other?",
    answer_steps=["Involuntary actions, such as the heart beat, breathing and salivation, go on all the time without our thinking; they are controlled by the mid-brain and hind-brain.",
                  "Reflex actions are sudden responses to a stimulus, such as pulling back from a hot object; they are controlled by the spinal cord."], marking_scheme=MS2P)
C.q("ex.q11", "short_answer", 3, [NS, HO], ex(11), "Compare and contrast nervous and hormonal mechanisms for control and coordination in animals.",
    answer_steps=["Similarity: both pass information from one part of the body to another and coordinate the body's responses.",
                  "Nervous: electrical impulses along nerves; very fast; reach only cells connected by nerves; short-lived.",
                  "Hormonal: chemicals carried by the blood; slower; reach all cells; steady and long-lasting."], marking_scheme=MS3)
C.q("ex.q12", "very_short_answer", 2, [PC, NS], ex(12), "What is the difference between the manner in which movement takes place in a sensitive plant and the movement in our legs?",
    answer_steps=["Sensitive plant: there are no nerves or muscles; cells change shape by changing their water content, and the information passes from cell to cell.",
                  "Our legs: nerve impulses reach the muscles, whose proteins change shape and arrangement so the muscle fibres shorten, and the legs move."], marking_scheme=MS2P)
# CBSE sample paper
C.mcq("sqp3", [NS], "Which of the following is a correct combination of function and part of the brain?",
      ["Posture and balance: Cerebrum", "Salivation: Medulla in midbrain", "Hunger: Pons in hindbrain", "Blood pressure: Medulla in hindbrain"], 3,
      "The medulla, in the hind-brain, controls blood pressure; balance is the cerebellum, salivation is the medulla (hind-brain), and hunger is the fore-brain.", "medium", source=SQP(3))
C.mcq("sqp4", [HO], "The blood glucose level in a patient was very high. It may be due to inadequate secretion of:",
      ["growth hormone from pituitary gland", "oestrogen from ovary", "insulin from pituitary gland", "insulin from pancreas"], 3,
      "Insulin, made by the pancreas, lowers blood glucose; too little of it causes a high level.", source=SQP(4))
C.q("sqp13", "short_answer", 3, [NS], SQP(13), "Draw and explain how the nerve cells help in transmission of impulses?",
    answer_steps=["Information is detected at the end of the dendritic tip of a nerve cell, where it sets off a chemical reaction that creates an electrical impulse.",
                  "The impulse travels from the dendrite to the cell body, and then along the axon to its end, where it releases some chemicals.",
                  "These chemicals cross the synapse and start a similar electrical impulse in a dendrite of the next neuron. (Diagram: two neurons with dendrite, cell body, axon, nerve ending and the synapse between them.)"],
    marking_scheme=MS3)
# GSEB
C.mcq("gseb2025_17", [HO], "Iodine is necessary for the synthesis of which hormone in the human body?", ["Thyroxin", "Insulin", "Adrenaline", "Growth hormone"], 0,
      "The thyroid gland uses iodine to make thyroxin.", source=gseb(2025, "17"))
C.mcq("gseb2025_21", [PC], "Match the plant hormone with its function: Cytokinin", ["Help in the growth of stem", "Wilting of leaves", "Promote cell division"], 2,
      "Cytokinins promote cell division; gibberellins help stem growth; abscisic acid causes wilting.", source=gseb(2025, "21"))
C.mcq("gseb2025_22", [PC], "Match the plant hormone with its function: Gibberellins", ["Help in the growth of stem", "Wilting of leaves", "Promote cell division"], 0,
      "Gibberellins help in the growth of the stem.", source=gseb(2025, "22"))
C.q("gseb2024_41", "short_answer", 3, [NS], gseb(2024, "41"), "What is Reflex arc? Draw a neat labelled diagram of Reflex arc.",
    answer_steps=["The pathway followed by a reflex action, from the receptor to the effector through the spinal cord, is the reflex arc.",
                  "Path: receptor (e.g. in the skin) → sensory neuron → relay neuron in the spinal cord → motor neuron → effector (muscle).",
                  "Diagram labels: receptor, sensory neuron, spinal cord (with relay neuron), motor neuron, effector muscle."], marking_scheme=["1 mark: definition", "1 mark: path", "1 mark: diagram"])
C.q("gseb2025_41", "short_answer", 3, [NS], gseb(2025, "41"), "Write a short note on neuron.",
    answer_steps=["A neuron (nerve cell) is the structural and functional unit of the nervous system.",
                  "Parts: dendrites (receive information), cell body (with nucleus), axon (carries the impulse away from the cell body) and nerve ending.",
                  "Information starts an electrical impulse at the dendrite; at the nerve ending, chemicals carry it across the synapse to the next cell."], marking_scheme=MS3)
# Shine MCQs
C.mcq("mcq01", [NS], "In a neuron, the impulse travels in the order:", ["dendrite → cell body → axon", "axon → cell body → dendrite", "cell body → dendrite → axon", "axon → dendrite → cell body"], 0,
      "Information enters at the dendrite, passes through the cell body and leaves along the axon.")
C.mcq("mcq02", [NS], "Reflex arcs are formed in the:", ["spinal cord", "cerebrum", "cerebellum", "heart"], 0, "Reflex arcs are formed in the spinal cord, so reflexes are quick.")
C.mcq("mcq03", [NS], "Salivation, vomiting and blood pressure are controlled by the:", ["medulla", "cerebellum", "fore-brain", "spinal cord"], 0, "The medulla in the hind-brain controls these involuntary actions.", "medium")
C.mcq("mcq04", [NS], "The centre for hunger is located in the:", ["fore-brain", "cerebellum", "medulla", "spinal cord"], 0, "The fore-brain has the hunger centre.", "medium")
C.mcq("mcq05", [PC], "Roots growing downwards is an example of:", ["positive geotropism", "negative phototropism only", "chemotropism", "hydrotropism"], 0,
      "Roots grow towards gravity: positive geotropism.", "medium")
C.mcq("mcq06", [PC], "The growth of a pollen tube towards the ovule is:", ["chemotropism", "hydrotropism", "phototropism", "geotropism"], 0, "The pollen tube grows towards chemicals from the ovule.")
C.mcq("mcq07", [PC], "Which hormone is made at the shoot tip and helps the shoot bend towards light?", ["Auxin", "Abscisic acid", "Cytokinin", "Insulin"], 0, "Auxin moves to the shady side and makes those cells grow longer.")
C.mcq("mcq08", [HO], "Which gland secretes growth hormone?", ["Pituitary", "Thyroid", "Adrenal", "Pancreas"], 0, "The pituitary secretes growth hormone.")
C.mcq("mcq09", [HO], "Hormones reach their target cells through:", ["the blood", "nerves", "the synapse", "the lymph only"], 0, "Endocrine glands release hormones into the blood, which carries them everywhere.")
C.mcq("mcq10", [HO], "Deficiency of growth hormone in childhood causes:", ["dwarfism", "goitre", "diabetes", "gigantism"], 0, "Too little growth hormone causes dwarfism; too much causes gigantism.")
# Assertion-reason
C.ar("ar1", [NS], "Reflex actions are faster than voluntary actions.", "In a reflex action, the response is decided in the spinal cord without involving thinking in the brain.", 0,
     "Skipping the trip to the brain and the thinking saves time: R explains A.")
C.ar("ar2", [PC], "The leaves of the sensitive plant fold up when touched.", "The folding of these leaves is a growth movement.", 2,
     "A is true. R is false: the cells change shape by losing water; there is no growth.")
C.ar("ar3", [HO], "Iodised salt is advised in our diet.", "Iodine is needed for the synthesis of thyroxin.", 0,
     "Without iodine the thyroid cannot make thyroxin, which can cause goitre: R explains A.")
C.ar("ar4", [HO], "Adrenaline makes the heart beat faster.", "Adrenaline is secreted by the pancreas.", 2,
     "A is true. R is false: adrenaline is secreted by the adrenal glands.")
C.ar("ar5", [PC], "A shoot bends towards light.", "Auxin makes the cells on the shady side of the shoot grow longer.", 0,
     "Longer cells on the shady side make the shoot bend towards the light: R explains A.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [NS], SHINE, "Name the two parts of the central nervous system and the bony structures that protect them.", "easy",
    answer_steps=["The brain, protected by the skull (and a fluid-filled balloon that absorbs shocks).", "The spinal cord, protected by the vertebral column (backbone)."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [HO], SHINE, "What is a feedback mechanism? Give an example.", "medium",
    answer_steps=["A feedback mechanism regulates the amount and timing of a hormone according to the body's needs.", "Example: when blood sugar rises, the pancreas secretes more insulin; as it falls, insulin secretion is reduced."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [NS], SHINE, "Name the three main parts of the brain and give one function of each.",
    answer_steps=["Fore-brain: thinking, and receiving sensory impulses (also the hunger centre).", "Mid-brain: controls some involuntary actions.",
                  "Hind-brain: the medulla controls blood pressure, salivation and vomiting; the cerebellum controls posture and balance."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [PC], SHINE, "Name the four plant hormones and give one function of each.",
    answer_steps=["Auxin: makes cells grow longer (shoot bending towards light). Gibberellins: help the stem grow.", "Cytokinins: promote cell division.",
                  "Abscisic acid: inhibits growth and causes wilting of leaves."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [NS], SHINE, "What is a reflex action? Explain the reflex arc with an example. Why have reflex arcs evolved?", "medium",
    answer_steps=["A reflex action is a sudden, automatic response to a stimulus, without thinking.", "Example: pulling the hand back on touching a hot object.",
                  "Path: heat receptors in the skin → sensory neuron → relay neuron in the spinal cord → motor neuron → muscles of the arm, which pull the hand away.",
                  "The information also reaches the brain, so we become aware of it.", "Reflex arcs give a very quick response that protects the body from harm, because the slower thinking in the brain is skipped."],
    marking_scheme=["1 mark: definition", "1 mark: example", "1 mark: path", "1 mark: brain", "1 mark: need"])
C.q("la2", "long_answer", 5, [HO], SHINE, "Name the endocrine glands of the human body and the hormones they secrete. State the effect of deficiency of any two hormones.", "medium",
    answer_steps=["Pituitary: growth hormone. Thyroid: thyroxin.", "Pancreas: insulin. Adrenal: adrenaline.", "Testes: testosterone. Ovaries: oestrogen. Hypothalamus: releasing hormones.",
                  "Deficiency of thyroxin (due to lack of iodine): goitre.", "Deficiency of insulin: diabetes; deficiency of growth hormone in childhood: dwarfism."],
    marking_scheme=["1 mark: pituitary and thyroid", "1 mark: pancreas and adrenal", "1 mark: gonads", "1 mark: first deficiency", "1 mark: second deficiency"])
C.q("cb1", "case_based", 4, [NS], SHINE,
    "While cooking, Sana accidentally touched a hot pan and pulled her hand away at once. A moment later she felt the pain and said, \"That was hot!\"\n\n"
    "(i) What type of action was pulling the hand away? (1)\n\n(ii) Where was the decision to pull the hand away made? (1)\n\n(iii) Write the path of this action from receptor to effector. OR Why did she feel the pain only after pulling her hand away? (2)",
    answer_steps=["(i) A reflex action.", "(ii) In the spinal cord.",
                  "(iii) Receptor in the skin → sensory neuron → relay neuron in the spinal cord → motor neuron → arm muscle (effector). OR The quick response was made in the spinal cord; the message took longer to reach the brain, where pain is felt."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [HO], SHINE,
    "A health worker in a hilly village found many people with swollen necks. She advised them to use iodised salt. In the same village, an elderly man was found to have a very high blood sugar level.\n\n"
    "(i) Name the disease that causes a swollen neck. (1)\n\n(ii) Which gland is affected in this disease? (1)\n\n(iii) Which hormone is lacking in the elderly man, and which gland makes it? OR How is the secretion of this hormone regulated? (2)",
    answer_steps=["(i) Goitre.", "(ii) The thyroid gland.",
                  "(iii) Insulin, made by the pancreas. OR By feedback: when blood sugar rises, the pancreas secretes more insulin; as it falls, secretion is reduced."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch06.q.ex."))
