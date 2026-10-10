"""CBSE Class 10 Science Ch 13: Our Environment.
The ozone equations go through ce(), which refuses unbalanced ones; the 10% energy figures are checked below."""
import sys
from fractions import Fraction as Fr
from sci_common import Chapter, ce, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch13"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch13_our_environment"
C = Chapter("sci10ch13")
blk = C.blk

E = {"split": ce("O2 -> O + O"), "ozone": ce("O + O2 -> O3")}
check(10000 * Fr(1, 10) ** 3 == 10, "10% law: 10000 J at producers -> 10 J at tertiary consumers")
check(Fr(10, 100) ** 2 * 1000 == 10, "mcq: 1000 J at producers -> 10 J at secondary consumers")

TROPHIC = ("| Trophic level | Who | Example (grass → grasshopper → frog → snake → eagle) |\n|---|---|---|\n| First | producers (autotrophs) | grass |\n"
           "| Second | primary consumers (herbivores) | grasshopper |\n| Third | secondary consumers (small carnivores) | frog |\n| Fourth | tertiary consumers (large carnivores) | snake |\n| Fifth | top carnivore | eagle |")
WASTE = ("| Biodegradable | Non-biodegradable |\n|---|---|\n| broken down by bacteria and other decomposers | not broken down by biological processes |\n"
         "| vegetable peels, paper, cotton, wood, leaves, cow dung | plastic, polythene, glass, metals, DDT, many synthetic chemicals |\n"
         "| return nutrients to the soil, but harm the environment if in large amounts | stay for a very long time, pile up, and harm soil, water and living things |")

sections = [
 {"id": "s1", "title": "Living together", "blocks": [
  blk("s1.hook", "hook", title="Where does your garbage go?",
    body="Every day each home throws away vegetable peels, plastic wrappers, paper and broken things. Some of it disappears into the soil within weeks; some of it will still be lying around when you are a grandparent.\n\n"
         "In this chapter you will see how living and non-living things work together in an **ecosystem**, how energy flows through food chains, how harmful chemicals collect in our bodies, why the ozone layer matters, and how each of us can manage waste better."),
  blk("s1.inspiration", "inspiration", title="The man who cleaned a beach", person="Afroz Shah", years="born 1982",
    body="In 2015, Afroz Shah, a young lawyer in Mumbai, was upset to see Versova beach buried under knee-deep plastic. With one elderly neighbour he began picking up rubbish every weekend.\n\n"
         "Thousands of volunteers joined him, and over the next years they removed millions of kilograms of waste; turtles came back to nest on the beach. In 2016 the United Nations named him a **Champion of the Earth**.",
    future="Environmental science leads to careers in ecology, waste management, pollution control, climate science, environmental law and sustainable design."),
  blk("s1.socratic", "socratic_question", question="If all the frogs in a field disappeared, what would happen to the number of insects?",
    options=["It would increase", "It would decrease", "It would not change"], correct_index=0,
    explanation="Frogs eat insects; without them, the insects would multiply. Removing one link disturbs the whole food chain."),
 ]},
 {"id": "s2", "title": "What is an ecosystem?", "blocks": [
  blk("s2.reveal", "theory", title="Biotic and abiotic components", revision=True,
    body="An **ecosystem** is made up of all the living organisms in an area together with the non-living components, interacting with one another.\n\n"
         "- **Biotic components:** the living things: plants, animals and microorganisms.\n- **Abiotic components:** the non-living things: temperature, rainfall, wind, soil and minerals.\n\n"
         "Forests, ponds and lakes are **natural ecosystems**; gardens, crop fields and aquariums are **artificial (human-made) ecosystems**.\n\n"
         "By the way they get food, organisms are:\n- **Producers:** green plants and blue-green algae, which make food by photosynthesis.\n"
         "- **Consumers:** herbivores, carnivores, omnivores and parasites, which eat food made by producers directly or indirectly.\n"
         "- **Decomposers:** bacteria and fungi, which break down dead remains and waste into simple substances that go back into the soil and are used again by plants."),
  blk("s2.check", "knowledge_check", question="Which of these is an artificial ecosystem?",
    options=["Aquarium", "Forest", "Lake", "Pond"], correct_index=0,
    explanation="An aquarium is made and maintained by humans; forests, lakes and ponds are natural."),
 ]},
 {"id": "s3", "title": "Food chains and the flow of energy", "blocks": [
  blk("s3.thm", "theory", title="Trophic levels and the 10% law", revision=True,
    body="A **food chain** is a series of organisms in which each one eats the one before it: grass → deer → lion. Each step is a **trophic level**.\n\n"
         "**Energy flow:**\n- Green plants capture only about **1%** of the sunlight falling on their leaves.\n"
         "- At each step, a large part of the food energy is used by the organism for its own life processes and lost as heat; only about **10%** is passed on to the next level (the **10 per cent law**).\n"
         "- So food chains usually have only **three or four** steps; there is too little energy left for more. The number of organisms is also usually largest at the producer level.\n"
         "- Energy flow is **unidirectional**: energy captured by producers does not go back to the Sun, and energy passed to herbivores does not come back to plants.\n\n"
         "In nature, food chains are interconnected: one organism is eaten by several others, forming a **food web**."),
  blk("s3.table", "markdown_table", title="Trophic levels in a food chain", revision=True, body=TROPHIC),
  blk("s3.check", "knowledge_check", question="If 10 000 J of energy is available at the producer level, how much reaches the tertiary consumers?",
    options=["10 J", "100 J", "1000 J", "1 J"], correct_index=0,
    explanation="10% at each step: 10 000 → 1000 (herbivores) → 100 (secondary) → 10 J (tertiary)."),
 ]},
 {"id": "s4", "title": "Biological magnification", "blocks": [
  blk("s4.thm", "theory", title="Poisons that pile up", revision=True,
    body="Many **pesticides and chemicals** are used to protect crops. Some of them are washed into the soil and water, absorbed by plants and taken up by animals.\n\n"
         "Such chemicals are **not degradable**, so they are not broken down in the body and they accumulate. Each organism eats many organisms from the level below, so the concentration **increases at each trophic level**. "
         "This is **biological magnification**. Since humans are at the top of many food chains, the maximum concentration of these chemicals collects in our bodies.\n\n"
         "This is why food grains, vegetables and fruits, and even ready-made foods, can contain pesticide residues; washing food and reducing pesticide use help."),
  blk("s4.check", "knowledge_check", question="In the food chain grass → grasshopper → frog → snake → eagle, which organism will have the highest concentration of a non-degradable pesticide?",
    options=["Eagle", "Grass", "Grasshopper", "Frog"], correct_index=0,
    explanation="The concentration increases at every level, so the top consumer, the eagle, has the most."),
 ]},
 {"id": "s5", "title": "The ozone layer", "blocks": [
  blk("s5.thm", "theory", title="Earth's sunscreen", revision=True,
    body=f"**Ozone (O₃)** is a molecule made of three oxygen atoms. At ground level it is a deadly poison, but high in the atmosphere it forms a layer that **shields the earth from harmful ultraviolet (UV) radiation** of the Sun. "
         "UV radiation can cause skin cancer and damages living things.\n\n"
         f"**How ozone forms:** high-energy UV radiation splits some oxygen molecules into free oxygen atoms: {E['split']} The oxygen atoms then combine with oxygen molecules to form ozone: {E['ozone']}\n\n"
         "**Ozone depletion:** the amount of ozone began to drop sharply in the 1980s. This was linked to synthetic chemicals such as **chlorofluorocarbons (CFCs)**, used as refrigerants and in fire extinguishers. "
         "In 1987 the United Nations Environment Programme (UNEP) succeeded in forging an agreement to freeze CFC production at 1986 levels. It is now mandatory for manufacturing companies worldwide to make CFC-free refrigerators."),
  blk("s5.check", "knowledge_check", question="The ozone layer protects us by:",
    options=["absorbing harmful UV radiation from the Sun", "producing oxygen for breathing", "keeping the earth warm at night", "blocking all sunlight"], correct_index=0,
    explanation="The ozone layer absorbs most of the Sun's harmful ultraviolet radiation."),
 ]},
 {"id": "s6", "title": "Managing our garbage", "blocks": [
  blk("s6.thm", "theory", title="Biodegradable and non-biodegradable", revision=True,
    body="Substances that are broken down by biological processes (by bacteria and other decomposers) are **biodegradable**; those that are not are **non-biodegradable**. Enzymes are specific: they break down only certain substances, so plastics and many synthetic chemicals are not digested by microbes.\n\n" + WASTE + "\n\n"
         "**Changes in packaging:** once, food came wrapped in leaves or paper, and tea was served in clay cups (kulhads). Now plastic packaging and disposable cups create mountains of waste. "
         "(Using kulhads on a huge scale also has a cost: it uses up the fertile topsoil.)\n\n"
         "**What each of us can do:** separate wet (biodegradable) and dry waste; compost kitchen waste; carry cloth bags; avoid single-use plastic; **reduce, reuse and recycle**; dispose of electronic items carefully, because they contain hazardous materials."),
  blk("s6.check", "knowledge_check", question="Which of these groups contains only biodegradable items?",
    options=["Cake, wood and grass", "Grass, wood and plastic", "Glass, paper and leaves", "Polythene, fruit peel and cotton"], correct_index=0,
    explanation="Cake, wood and grass are all broken down by decomposers; plastic, glass and polythene are not."),
  blk("s6.memory", "memory_trick", title="Ten per cent and three R's",
    body="- **10% law:** \"Each step keeps 90, passes 10.\" 10 000 → 1000 → 100 → 10.\n- **Magnification goes up, energy goes down** the food chain.\n"
         "- **Ozone:** O₂ splits (UV), O joins O₂ → O₃; CFCs destroy it.\n- **Waste:** Reduce → Reuse → Recycle, in that order of priority."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Saying that energy flows in a cycle: energy flow is one-way; it is nutrients that cycle.\n- Saying that the top consumer has the least pesticide: it has the **most** (biological magnification), even though it gets the least energy.\n"
         "- Calling ozone harmless everywhere: at ground level it is a poison.\n- Assuming that biodegradable waste has no effect: in large amounts it produces foul smell, disease and greenhouse gases.\n"
         "- Writing that decomposers are consumers that eat living things: they break down dead remains."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="Bury a vegetable peel, a paper scrap, a piece of plastic and a piece of glass in pots of moist soil; dig them up after a month and compare. "
         "Play a food-chain game with energy tokens: start with 1000 beads at the producer, and pass only one bead in ten to each next player to show why chains are short."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why an eagle has more pesticide in its body than a grasshopper, even though it eats far less grass."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 5, Life Processes:** autotrophs and heterotrophs are the producers and consumers of ecosystems.\n- **Chapter 4:** CFCs and polythene are carbon compounds that do not break down easily.\n"
         "- **Class 12 Biology:** ecosystems, biodiversity and environmental issues in detail."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="In a pond, the food chain is: algae → water insects → small fish → large fish → fish-eating bird. The algae trap 50 000 J of energy.\n\n"
         "(a) How much energy reaches the large fish? (b) Which organism will have the highest concentration of a pesticide that entered the pond? (c) What would happen if all the small fish were removed?\n\n"
         "**Answer:** (a) 10% at each step: 50 000 → 5000 (insects) → 500 (small fish) → **50 J** (large fish). (b) The fish-eating bird, at the top. "
         "(c) The water insects would increase (no predators), and the large fish and birds would decline for lack of food; the balance of the pond would be disturbed."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- An ecosystem has biotic (living) and abiotic (non-living) components; it can be natural (forest, pond) or artificial (garden, aquarium).\n"
         "- Producers, consumers and decomposers form food chains and food webs; each step is a trophic level.\n"
         "- Energy flow is one-way and only about 10% passes to the next level, so food chains are short.\n"
         "- Non-degradable chemicals increase in concentration at each level: biological magnification.\n"
         "- The ozone layer absorbs harmful UV radiation; CFCs deplete it, and their production has been controlled.\n- Biodegradable and non-biodegradable wastes must be separated and managed: reduce, reuse, recycle."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Always write food chains with arrows from food to eater (grass → deer → lion).\n- Use the 10% law step by step in energy questions.\n"
         "- Learn the ozone equations and the role of CFCs and UNEP (1987).\n- In 'give two ways' questions about waste, give specific actions (cloth bags, composting, separating wet and dry waste)."),
  blk("s7.flash1", "flashcard", front="What is the 10 per cent law?", back="Only about 10% of the energy at one trophic level is passed on to the next."),
  blk("s7.flash2", "flashcard", front="What is biological magnification?", back="The increase in concentration of non-degradable chemicals at each successive trophic level."),
  blk("s7.flash3", "flashcard", front="Which chemicals deplete the ozone layer?", back="Chlorofluorocarbons (CFCs)."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Our Environment",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 13,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: eco-system, environmental problems, ozone depletion, waste production and their solutions; biodegradable and non-biodegradable substances.",
  "concepts": ["ecosystem", "food_chain", "ozone_waste"], "sections": sections}

# ---------------------------------------------------------------- questions
EC, FC, OW = "ecosystem", "food_chain", "ozone_waste"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 13 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "short_answer", 3, [FC], it("13.1", 1), "What are trophic levels? Give an example of a food chain and state the different trophic levels in it.", "easy",
    answer_steps=["The various steps in a food chain, at which energy is transferred, are trophic levels.", "Example: grass → grasshopper → frog → snake.",
                  "Grass: producer (first level); grasshopper: primary consumer (second); frog: secondary consumer (third); snake: tertiary consumer (fourth)."], marking_scheme=["1 mark: definition", "1 mark: example", "1 mark: levels"])
C.q("it1.q2", "very_short_answer", 2, [EC], it("13.1", 2), "What is the role of decomposers in the ecosystem?", "easy",
    answer_steps=["Decomposers such as bacteria and fungi break down the dead remains and wastes of organisms into simple substances.", "These substances go back into the soil and are used again by plants: decomposers recycle nutrients and keep the environment clean."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [OW], it("13.2", 1), "Why are some substances biodegradable and some non-biodegradable?",
    answer_steps=["Microorganisms break down substances using enzymes, and enzymes are specific: each acts only on certain substances.", "Natural materials (peels, paper) can be broken down; many synthetic materials (plastics, DDT) cannot, so they are non-biodegradable."], marking_scheme=MS2P)
C.q("it2.q2", "very_short_answer", 2, [OW], it("13.2", 2), "Give any two ways in which biodegradable substances would affect the environment.", "easy",
    answer_steps=["In large amounts they rot, give a foul smell and breed flies and germs that spread disease.", "Their decomposition can release gases such as methane and carbon dioxide; if properly composted, they enrich the soil."], marking_scheme=MS2P)
C.q("it2.q3", "very_short_answer", 2, [OW], it("13.2", 3), "Give any two ways in which non-biodegradable substances would affect the environment.", "easy",
    answer_steps=["They remain for a very long time and pile up, polluting soil and water and blocking drains.", "Animals may swallow plastics and die, and toxic chemicals can enter food chains and undergo biological magnification."], marking_scheme=MS2P)
C.q("it3.q1", "short_answer", 3, [OW], it("13.2.1", 1), "What is ozone and how does it affect any ecosystem?",
    answer_steps=["Ozone (O₃) is a molecule of three oxygen atoms. At ground level it is a deadly poison.", "High in the atmosphere, the ozone layer shields the earth from the Sun's harmful ultraviolet (UV) radiation.",
                  "If it is depleted, more UV reaches the earth, causing skin cancer and damage to plants, animals and the whole ecosystem."], marking_scheme=MS3)
C.q("it3.q2", "very_short_answer", 2, [OW], it("13.2.2", 2), "How can you help in reducing the problem of waste disposal? Give any two methods.", "easy",
    answer_steps=["Separate wet (biodegradable) and dry (non-biodegradable) waste, and compost kitchen waste.", "Carry cloth bags, avoid single-use plastic, and reuse and recycle things wherever possible."], marking_scheme=MS2P)
# Exercises
C.mcq("ex.q1", [OW], "Which of the following groups contain only biodegradable items?", ["Grass, flowers and leather", "Grass, wood and plastic", "Fruit-peels, cake and lime-juice", "Cake, wood and grass"], 3,
      "Cake, wood and grass are all broken down by decomposers. (Option (c) is also biodegradable; the NCERT answer is (d).)", "medium", source=ex(1))
C.mcq("ex.q2", [FC], "Which of the following constitute a food-chain?", ["Grass, wheat and mango", "Grass, goat and human", "Goat, cow and elephant", "Grass, fish and goat"], 1, "Grass (producer) → goat (herbivore) → human (consumer).", source=ex(2))
C.mcq("ex.q3", [OW], "Which of the following are environment-friendly practices?", ["Carrying cloth-bags to put purchases in while shopping", "Switching off unnecessary lights and fans",
      "Walking to school instead of getting your mother to drop you on her scooter", "All of the above"], 3, "Each of these reduces waste or saves energy.", source=ex(3))
C.q("ex.q4", "very_short_answer", 2, [FC], ex(4), "What will happen if we kill all the organisms in one trophic level?",
    answer_steps=["The organisms of the next trophic level would lose their food and decline or die.", "The organisms of the level below would increase without control. The food chain breaks and the balance of the ecosystem is disturbed."], marking_scheme=MS2P)
C.q("ex.q5", "short_answer", 3, [FC], ex(5), "Will the impact of removing all the organisms in a trophic level be different for different trophic levels? Can the organisms of any trophic level be removed without causing any damage to the ecosystem?", "hard",
    answer_steps=["Yes, the impact differs. Removing producers would remove the food and energy for every other level, and the whole ecosystem would collapse.",
                  "Removing a consumer level would let the level below multiply and starve the level above; removing decomposers would stop the recycling of nutrients and let dead matter pile up.",
                  "No trophic level can be removed without causing damage, because all levels are linked."], marking_scheme=MS3)
C.q("ex.q6", "very_short_answer", 2, [FC], ex(6), "What is biological magnification? Will the levels of this magnification be different at different levels of the ecosystem?",
    answer_steps=["The increase in concentration of non-degradable harmful chemicals (such as pesticides) at successive trophic levels is biological magnification.", "Yes: the concentration is lowest at the producer level and highest at the top consumer level."], marking_scheme=MS2P)
C.q("ex.q7", "short_answer", 3, [OW], ex(7), "What are the problems caused by the non-biodegradable wastes that we generate?",
    answer_steps=["They do not break down, so they pile up as heaps of garbage and occupy land.", "They pollute soil and water; plastics block drains and harm animals that swallow them.",
                  "Toxic chemicals from them enter food chains and undergo biological magnification, harming humans."], marking_scheme=MS3)
C.q("ex.q8", "very_short_answer", 2, [OW], ex(8), "If all the waste we generate is biodegradable, will this have no impact on the environment?",
    answer_steps=["It will still have an impact: large amounts of biodegradable waste rot, give a foul smell and spread disease.", "Decomposition also releases gases such as methane; the waste must be managed, for example by composting."], marking_scheme=MS2P)
# CBSE sample paper
C.mcq("sqp6", [OW], "Which are the correct statements related to ozone?\n\n(i) Ozone layer helps in increasing the UV radiations reaching earth.\n\n(ii) Ozone is a deadly poison.\n\n(iii) Ozone layer shields the earth from UV radiations.\n\n"
      "(iv) Ozone layer prevents UV rays which cause skin cancer.\n\n(v) Ozone is formed with the help of Chloroflurocarbons.", ["(i), (ii), (iii)", "(ii), (iii), (iv)", "(iii), (iv), (v)", "(i), (iv), (v)"], 1,
      "Ozone is a poison at ground level and shields the earth from UV; it does not increase UV, and CFCs destroy it rather than form it.", "medium", source=SQP(6))
C.mcq("sqp7", [OW], "Which of the following human activities has resulted in an increase of non-biodegradable substances?", ["Organic farming", "Increase in tree plantation", "Use of plastic as packaging material", "Composting of kitchen waste"], 2,
      "Plastic packaging is non-biodegradable.", source=SQP(7))
C.ar("sqp9", [FC], "Vulture will always have the least amount of pesticides in a food chain.", "Vulture occupies the last trophic level and it gets only 10% of energy of the previous trophic level.", 3,
     "A is false: being at the top, the vulture has the highest amount of pesticides (biological magnification). R is true.", source=SQP(9))
C.q("sqp12", "very_short_answer", 2, [FC], SQP(12), "About 100 acres of forest land was declared as Natural reserve park. The following organisms were predominant in the Natural reserve park: rabbit, frog, grass, fish, fox, water insects, zebra, peacock, snake, trees, bird, owl, insects, tiger, vulture, duck.\n\nCreate a food web comprising two separate food chains with different producers by using the above data.", "medium",
    answer_steps=["Tree food chain: trees → zebra → tiger (any other correct chain).", "Grassland food chain: grass → zebra → tiger. Join the two chains at the common point, zebra, to make a food web."], marking_scheme=["1 mark: two chains", "1 mark: food web"])
# GSEB
C.mcq("gseb2024_23", [FC], "Match the trophic level with the type of consumer: 2nd trophic level", ["Primary consumer", "Secondary consumer", "Tertiary consumer"], 0, "The second level is herbivores: primary consumers.", source=gseb(2024, "23"))
C.mcq("gseb2024_24", [FC], "Match the trophic level with the type of consumer: 3rd trophic level", ["Primary consumer", "Secondary consumer", "Tertiary consumer"], 1, "The third level is small carnivores: secondary consumers.", source=gseb(2024, "24"))
C.q("gseb2024_34", "very_short_answer", 2, [EC], gseb(2024, "34"), "Write the differences between biotic factor and abiotic factor.", "easy",
    answer_steps=["Biotic factors are the living components of an ecosystem: plants, animals and microorganisms.", "Abiotic factors are the non-living components: temperature, rainfall, wind, soil and minerals."], marking_scheme=MS2P)
C.q("gseb2024_35", "very_short_answer", 2, [FC], gseb(2024, "35"), "Write a note on biological magnification.",
    answer_steps=["Non-degradable chemicals such as pesticides enter food chains through soil and water and are not broken down in the body.", "Their concentration increases at each trophic level; humans at the top collect the most."], marking_scheme=MS2P)
C.q("gseb2024_54", "short_answer", 3, [OW], gseb(2024, "54", 4), "(a) Explain the formation of ozone with equations.\n\n(b) How can you help in reducing the problem of waste disposal? Write two methods.",
    answer_steps=["(a) Ultraviolet radiation splits oxygen molecules into free oxygen atoms: " + E["split"], "The oxygen atoms combine with oxygen molecules to form ozone: " + E["ozone"],
                  "(b) Separate wet and dry waste and compost the wet waste; carry cloth bags and avoid single-use plastic."], marking_scheme=["1 mark: first equation", "1 mark: second equation", "1 mark: (b)"])
C.mcq("gseb2025_23", [EC], "The organisms which prepare their own food are called ____.", ["Herbivores", "Producers", "Carnivores"], 1, "Green plants make their own food: producers.", source=gseb(2025, "23"))
C.mcq("gseb2025_24", [EC], "The organisms which feed on plants are called ____.", ["Herbivores", "Producers", "Carnivores"], 0, "Plant eaters are herbivores.", source=gseb(2025, "24"))
C.q("gseb2025_34", "very_short_answer", 2, [OW], gseb(2025, "34"), "How can you help in reducing the problem of waste disposal? Give any two methods.", "easy",
    answer_steps=["Separate wet and dry waste, and compost kitchen waste at home.", "Use cloth bags and reusable containers instead of plastic, and send paper, glass and metal for recycling."], marking_scheme=MS2P)
C.q("gseb2025_35", "very_short_answer", 2, [EC], gseb(2025, "35"), "Classify the following ecosystems into natural ecosystem and artificial ecosystems: Forest, garden, aquarium, sea", "easy",
    answer_steps=["Natural ecosystems: forest, sea.", "Artificial ecosystems: garden, aquarium."], marking_scheme=["1 mark: natural", "1 mark: artificial"])
# Shine MCQs
C.mcq("mcq01", [EC], "Which of these is an abiotic component of an ecosystem?", ["Temperature", "Grass", "Bacteria", "Deer"], 0, "Temperature is non-living.")
C.mcq("mcq02", [EC], "Decomposers are mainly:", ["bacteria and fungi", "green plants", "herbivores", "carnivores"], 0, "Bacteria and fungi break down dead remains.")
C.mcq("mcq03", [FC], "Green plants capture about what percentage of the sunlight falling on their leaves?", ["1%", "10%", "50%", "90%"], 0, "Only about 1% is converted into food energy.", "medium")
C.mcq("mcq04", [FC], "If producers have 1000 J of energy, the secondary consumers get about:", ["10 J", "100 J", "1 J", "500 J"], 0, "1000 → 100 (primary) → 10 J (secondary).", "medium")
C.mcq("mcq05", [FC], "The flow of energy in an ecosystem is:", ["unidirectional", "cyclic", "bidirectional", "random"], 0, "Energy passes one way: Sun → producers → consumers; it does not return.")
C.mcq("mcq06", [FC], "In the food chain grass → deer → lion, the deer is a:", ["primary consumer", "producer", "secondary consumer", "decomposer"], 0, "The deer eats plants: herbivore, primary consumer.")
C.mcq("mcq07", [OW], "The chemicals mainly responsible for the depletion of the ozone layer are:", ["chlorofluorocarbons (CFCs)", "carbon dioxide", "oxygen", "nitrogen"], 0, "CFCs used in refrigerants and fire extinguishers deplete ozone.")
C.mcq("mcq08", [OW], "Which of these is non-biodegradable?", ["Polythene bag", "Vegetable peel", "Paper", "Cotton cloth"], 0, "Polythene is not broken down by decomposers.")
C.mcq("mcq09", [FC], "Food chains are usually short (3 or 4 steps) because:", ["energy decreases sharply at each step", "animals do not like long chains", "plants are few", "decomposers stop them"], 0, "Only about 10% passes on, so little energy is left after a few steps.", "medium")
C.mcq("mcq10", [OW], "The UNEP agreement of 1987 aimed to:", ["freeze CFC production at 1986 levels", "ban all plastics", "plant more trees", "increase ozone at ground level"], 0, "It froze CFC production at 1986 levels.")
# Assertion-reason
C.ar("ar1", [FC], "The concentration of pesticides is highest in the top consumer of a food chain.", "Non-degradable chemicals accumulate at each trophic level.", 0, "Accumulation at each step makes the top consumer the most contaminated: R explains A.")
C.ar("ar2", [FC], "Food chains generally have only three or four trophic levels.", "Only about 10% of energy is transferred from one trophic level to the next.", 0, "Too little energy is left after a few steps: R explains A.")
C.ar("ar3", [OW], "Ozone at ground level is beneficial for living organisms.", "The ozone layer in the upper atmosphere absorbs harmful UV radiation.", 3, "A is false: at ground level ozone is a deadly poison. R is true.")
C.ar("ar4", [EC], "Decomposers are essential for an ecosystem.", "Decomposers break down dead remains and return nutrients to the soil.", 0, "Recycling nutrients keeps the ecosystem going: R explains A.")
C.ar("ar5", [OW], "Plastics are non-biodegradable.", "Plastics can be recycled.", 1, "Both are true, but recyclability does not explain why plastics are not broken down by microbes.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [FC], SHINE, "What is a food web? How is it different from a food chain?", "easy",
    answer_steps=["A food chain is a single series of organisms, each eating the one before it.", "A food web is a network of many interconnected food chains, since one organism is eaten by several others."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [OW], SHINE, "Why should we use CFC-free refrigerators?", "easy",
    answer_steps=["CFCs released from old refrigerators and air conditioners deplete the ozone layer.", "A depleted ozone layer lets more harmful UV radiation reach the earth, causing skin cancer and harming living things."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [FC], SHINE, "State the 10 per cent law. If a plant captures 20 000 J of energy, how much energy will reach a tertiary consumer? Why is the flow of energy called unidirectional?",
    answer_steps=["10% law: only about 10% of the energy at one trophic level passes on to the next.", "20 000 → 2000 (primary) → 200 (secondary) → 20 J (tertiary).",
                  "Energy captured by producers does not go back to the Sun, and energy passed to consumers does not return to the lower levels."], marking_scheme=MS3)
check(20000 * Fr(1, 10) ** 3 == 20, "Shine sa1")
C.q("sa2", "short_answer", 3, [OW], SHINE, "Distinguish between biodegradable and non-biodegradable substances with two examples each. Why are some substances not biodegradable?",
    answer_steps=["Biodegradable: broken down by decomposers, e.g. vegetable peels, paper.", "Non-biodegradable: not broken down by biological processes, e.g. plastic, glass.",
                  "Enzymes of microbes are specific, so they cannot act on many synthetic materials."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [OW], SHINE, "What is the ozone layer? How is ozone formed? How is it being depleted, and what steps have been taken to protect it?", "medium",
    answer_steps=["The ozone layer is a layer of ozone (O₃) high in the atmosphere that shields the earth from harmful UV radiation.", "UV radiation splits oxygen molecules: " + E["split"],
                  "Oxygen atoms combine with oxygen molecules: " + E["ozone"], "Synthetic chemicals such as CFCs, used as refrigerants and in fire extinguishers, deplete the ozone layer.",
                  "In 1987 UNEP forged an agreement to freeze CFC production at 1986 levels; CFC-free refrigerators are now mandatory."],
    marking_scheme=["1 mark: definition", "1 mark: first equation", "1 mark: second equation", "1 mark: depletion", "1 mark: steps taken"])
C.q("la2", "long_answer", 5, [FC], SHINE, "Explain, with a food chain, how energy flows through an ecosystem and how pesticides become concentrated. Why should humans be most concerned?", "medium",
    answer_steps=["Food chain: grass → grasshopper → frog → snake → eagle.", "Producers capture about 1% of sunlight; at each step only about 10% of the energy passes on, the rest being used and lost as heat.",
                  "So energy decreases sharply up the chain, and chains are short.", "Non-degradable pesticides are not broken down, so their concentration increases at each level (biological magnification).",
                  "Humans are at the top of many food chains, so the highest concentrations collect in our bodies."],
    marking_scheme=["1 mark: food chain", "1 mark: 10% law", "1 mark: energy decreases", "1 mark: magnification", "1 mark: humans"])
C.q("cb1", "case_based", 4, [FC], SHINE,
    "Farmers near a lake sprayed a pesticide on their crops. A few years later, scientists found traces of it in the lake water, much more in the fish, and the highest amount in fish-eating birds, whose eggshells had become thin.\n\n"
    "(i) Name the process shown in the case. (1)\n\n(ii) Which organism had the highest concentration of the pesticide? (1)\n\n(iii) Why did the concentration increase along the food chain? OR Suggest two ways to reduce our intake of pesticides. (2)",
    answer_steps=["(i) Biological magnification.", "(ii) The fish-eating birds.",
                  "(iii) The pesticide is not broken down in the body; each organism eats many organisms from the level below, so the chemical accumulates and its concentration rises at each step. OR Wash fruits and vegetables well before use; prefer organically grown food and support reduced pesticide use."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [OW], SHINE,
    "A school started separating its garbage into green bins (wet waste) and blue bins (dry waste). The green-bin waste was turned into compost for the school garden, and the dry waste was sent for recycling.\n\n"
    "(i) Give two examples of waste that should go into the green bin. (1)\n\n(ii) Is plastic biodegradable? (1)\n\n(iii) How does composting help the environment? OR Give two problems caused if dry waste such as plastic is burnt or dumped. (2)",
    answer_steps=["(i) Vegetable and fruit peels, leftover food (any two biodegradable items).", "(ii) No, plastic is non-biodegradable.",
                  "(iii) Composting turns biodegradable waste into manure that enriches the soil, and reduces the garbage sent to landfills. OR Burning plastic releases harmful gases that pollute the air; dumped plastic pollutes soil and water and harms animals."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch13.q.ex."))
