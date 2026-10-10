"""CBSE Class 10 Science Ch 7: How do Organisms Reproduce? No equations in this chapter."""
import sys
from sci_common import Chapter, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch07"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch07_how_do_organisms_reproduce"
C = Chapter("sci10ch07")
blk = C.blk

ASEXUAL = ("| Method | How it happens | Example |\n|---|---|---|\n| Binary fission | one cell splits into two | Amoeba, Leishmania |\n"
           "| Multiple fission | one cell divides into many daughter cells | Plasmodium |\n| Fragmentation | the body breaks into pieces; each grows into a new individual | Spirogyra |\n"
           "| Regeneration | a cut piece grows into a complete organism, using specialised cells | Hydra, Planaria |\n| Budding | an outgrowth (bud) grows and separates | Hydra, yeast |\n"
           "| Vegetative propagation | a new plant grows from a root, stem or leaf | sugarcane, rose, grapes, Bryophyllum |\n| Spore formation | spores in sporangia grow on a moist surface | Rhizopus (bread mould) |")
CONTRA = ("| Method | How it works |\n|---|---|\n| Mechanical barrier | condoms or similar coverings stop the sperm from reaching the egg; also protect against many infections |\n"
          "| Hormonal | oral pills change the hormonal balance so that eggs are not released |\n| Copper-T or loop | placed in the uterus to prevent pregnancy |\n"
          "| Surgical | vas deferens blocked in males, or fallopian tube blocked in females |")

sections = [
 {"id": "s1", "title": "Why do organisms reproduce?", "blocks": [
  blk("s1.hook", "hook", title="Same, but not quite the same",
    body="Puppies look like dogs, mango seeds grow into mango trees, and you look like your parents. Yet no two puppies, or two mango trees, or two brothers, are exactly alike.\n\n"
         "Reproduction makes new individuals that are **similar** to their parents, but not identical. In this chapter you will see why this small difference matters, how single cells, plants and humans reproduce, "
         "and how people can take care of their reproductive health."),
  blk("s1.inspiration", "inspiration", title="Fertilisation in a test tube", person="Panchanan Maheshwari", years="1904–1966",
    body="Panchanan Maheshwari, born in Jaipur, was one of the world's leading experts on how flowering plants form embryos. His book on the **embryology of flowering plants** (1950) became a standard text.\n\n"
         "At the University of Delhi, his group grew flower parts in test tubes and achieved **fertilisation in a test tube**, opening the way to new methods of plant breeding. He was elected a Fellow of the Royal Society in 1965.",
    future="Reproductive biology leads to careers in medicine and nursing, plant breeding and seed science, animal husbandry, tissue culture and biotechnology."),
  blk("s1.socratic", "socratic_question", question="If DNA were copied perfectly every time, what would all the offspring of an asexual organism be like?",
    options=["Exactly identical to the parent and to each other", "Very different from the parent", "Half like the parent"], correct_index=0,
    explanation="Variation comes from small errors in DNA copying; with perfect copying there would be no variation at all."),
 ]},
 {"id": "s2", "title": "DNA copying and variation", "blocks": [
  blk("s2.reveal", "theory", title="Copies with small changes", revision=True,
    body="The **DNA** in the nucleus carries the information for making proteins, and so for the body design. The basic event in reproduction is making a **copy of the DNA**, along with extra cell apparatus, so that two cells form.\n\n"
         "- The copying is very accurate but never perfect, so the copies are similar but have small **variations**.\n"
         "- Consistency in DNA copying keeps the body design that suits the organism's **niche** (its place in the environment).\n"
         "- Variation is useful for the **species**, not necessarily for the individual. If the niche changes drastically, for example the water gets hotter, most bacteria may die, but a few variants that resist heat survive and grow. "
         "Variation is therefore the basis for **evolution**."),
  blk("s2.check", "knowledge_check", question="Why is variation useful for a species?",
    options=["Some variants may survive if the environment changes", "It makes every individual stronger", "It stops DNA copying", "It makes all offspring identical"], correct_index=0,
    explanation="When conditions change, some variants may be suited to the new conditions, so the species survives."),
 ]},
 {"id": "s3", "title": "Asexual reproduction", "blocks": [
  blk("s3.thm", "theory", title="One parent", revision=True,
    body="In **asexual reproduction** a single parent produces offspring, with no gametes. The offspring are almost identical to the parent.\n\n"
         "- **Fission:** unicellular organisms split. Amoeba can split in any plane; **Leishmania** (which causes kala-azar) has a whip-like structure at one end and splits in a definite plane. "
         "The malaria parasite **Plasmodium** divides into many daughter cells at once (multiple fission).\n"
         "- **Fragmentation:** simple multicellular organisms such as **Spirogyra** break into pieces that grow into new individuals.\n"
         "- **Regeneration:** **Hydra** and **Planaria** can be cut into pieces, and each piece grows into a complete organism, using specialised cells that divide and develop into different tissues. "
         "Complex organisms cannot do this, because their cells are highly specialised.\n"
         "- **Budding:** in **Hydra** a bud develops as an outgrowth and detaches when mature.\n"
         "- **Vegetative propagation:** new plants grow from roots, stems or leaves (layering, grafting). Buds in the notches of **Bryophyllum** leaves grow into new plants. "
         "It is used for plants that have lost the ability to produce seeds (banana, orange, rose, jasmine); the plants are genetically similar to the parent and bear flowers and fruits earlier. **Tissue culture** grows many plants from a few cells.\n"
         "- **Spore formation:** bread mould (**Rhizopus**) forms spores in sporangia. Spores have thick walls that protect them until they reach a moist surface."),
  blk("s3.table", "markdown_table", title="Methods of asexual reproduction", revision=True, body=ASEXUAL),
  blk("s3.check", "knowledge_check", question="Which organism reproduces by multiple fission?",
    options=["Plasmodium", "Amoeba", "Hydra", "Spirogyra"], correct_index=0,
    explanation="The malaria parasite Plasmodium divides into many daughter cells at once."),
 ]},
 {"id": "s4", "title": "Sexual reproduction in flowering plants", "blocks": [
  blk("s4.thm", "theory", title="Flowers, pollination and fertilisation", revision=True,
    body="In **sexual reproduction**, two **germ cells (gametes)**, one from each parent, fuse. Each gamete has **half** the usual number of chromosomes and half the DNA, so the zygote has the full amount again. "
         "Combining DNA from two individuals produces more variation. The male gamete is usually small and motile; the female gamete is larger and stores food.\n\n"
         "**Parts of a flower:** sepals, petals, **stamens** (male; the anther makes pollen grains) and **pistil** (female; ovary, style and stigma). The ovary contains **ovules**, each with an egg cell. "
         "A flower with only stamens or only a pistil is **unisexual** (papaya, watermelon); one with both is **bisexual** (Hibiscus, mustard).\n\n"
         "- **Pollination:** transfer of pollen from the anther to the stigma: of the same flower (**self-pollination**) or of another flower (**cross-pollination**, by wind, water or animals).\n"
         "- **Fertilisation:** a **pollen tube** grows from the pollen grain through the style to the ovule, and the male germ cell fuses with the egg to form a **zygote**.\n"
         "- **After fertilisation:** the zygote divides to form the **embryo**; the ovule develops a tough coat and becomes the **seed**; the ovary grows and ripens into the **fruit**; petals, sepals, stamens, style and stigma may shrivel and fall off.\n"
         "- The seed contains the future plant, which grows into a seedling under the right conditions (**germination**)."),
  blk("s4.check", "knowledge_check", question="After fertilisation, the ovary develops into the:",
    options=["fruit", "seed", "embryo", "pollen tube"], correct_index=0,
    explanation="The ovule becomes the seed and the ovary ripens into the fruit."),
 ]},
 {"id": "s5", "title": "Reproduction in human beings", "blocks": [
  blk("s5.thm", "theory", title="Puberty and the reproductive systems", revision=True,
    body="**Puberty** is the period when the reproductive tissues begin to mature.\n- Common changes: thick hair in the armpits and genital area; thinner hair on the legs, arms and face; oily skin and pimples.\n"
         "- In girls: breasts begin to grow and the skin of the nipples darkens; **menstruation** starts.\n- In boys: hair on the face, the voice begins to crack, and the penis occasionally becomes enlarged and erect.\n\n"
         "**Male reproductive system:** the **testes**, in the scrotum outside the abdomen (because sperm formation needs a lower temperature), produce **sperms** and the hormone **testosterone**. "
         "Sperms travel through the **vas deferens**, which joins a tube from the urinary bladder; the **urethra** is a common passage for sperms and urine. "
         "The **seminal vesicles** and **prostate gland** add secretions, so the sperms are in a fluid that makes their transport easier and gives them nutrition.\n\n"
         "**Female reproductive system:** the **ovaries** release one egg every month and make the hormones oestrogen and progesterone. The egg travels through the **oviduct (fallopian tube)** to the **uterus**, "
         "which opens into the vagina through the cervix. Fertilisation happens in the oviduct. The zygote is implanted in the thick lining of the uterus.\n\n"
         "**Placenta:** a disc-like tissue embedded in the uterine wall. Villi on the embryo's side face blood spaces on the mother's side, giving a large surface for **glucose and oxygen** to pass to the embryo and **wastes** to pass to the mother. "
         "The child develops in about nine months.\n\n"
         "**Menstruation:** every month the uterus prepares a thick, spongy lining with blood vessels. If the egg is not fertilised, this lining slowly breaks down and comes out through the vagina as blood and mucus. "
         "This cycle takes place roughly every month and usually lasts about two to eight days."),
  blk("s5.check", "knowledge_check", question="Where does fertilisation take place in the human female?",
    options=["Oviduct (fallopian tube)", "Uterus", "Ovary", "Vagina"], correct_index=0,
    explanation="The sperm meets the egg in the oviduct; the zygote then moves to the uterus and is implanted."),
 ]},
 {"id": "s6", "title": "Reproductive health", "blocks": [
  blk("s6.thm", "theory", title="Health, contraception and the sex ratio", revision=True,
    body="Reproductive health means physical and emotional well-being related to reproduction, including the right age and readiness for having children.\n\n"
         "**Sexually transmitted diseases (STDs)** spread through sexual contact: bacterial, such as **gonorrhoea** and **syphilis**; viral, such as **warts** and **HIV-AIDS**. A condom helps to prevent many of them.\n\n"
         "**Contraception** prevents pregnancy:\n\n" + CONTRA + "\n\n"
         "**Sex ratio:** prenatal sex determination is prohibited by law in India. Selective killing of female foetuses (**female foeticide**) is a crime, and it is reducing the number of girls in some parts of the country. "
         "A healthy society needs a healthy sex ratio."),
  blk("s6.check", "knowledge_check", question="Which contraceptive method also protects against many sexually transmitted diseases?",
    options=["Condom", "Copper-T", "Oral pills", "Surgery"], correct_index=0,
    explanation="A condom is a mechanical barrier, so it also stops the spread of many infections; the others do not."),
  blk("s6.memory", "memory_trick", title="Ovule to seed, ovary to fruit",
    body="- **Ovul-e → s-e-ed** (both have an 'e' sound); **ovar-y → fruit-y** (the bigger part becomes the bigger thing).\n"
         "- **Asexual methods, in order of the chapter:** **F**ission, **F**ragmentation, **R**egeneration, **B**udding, **V**egetative propagation, **S**pores: \"**F**ive **F**riends **R**ode **B**ikes **V**ery **S**lowly\".\n"
         "- **Sperm path:** testis → vas deferens → urethra (with seminal vesicles and prostate adding fluid)."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing that pollination and fertilisation are the same: pollination moves pollen; fertilisation is the fusion of gametes.\n"
         "- Writing that the ovary becomes the seed: the ovule becomes the seed; the ovary becomes the fruit.\n"
         "- Saying that Amoeba reproduces by budding: Amoeba uses binary fission; Hydra and yeast use budding.\n"
         "- Writing that copper-T protects against STDs: only barrier methods such as condoms do.\n- Writing that the testes are inside the abdomen: they are in the scrotum, outside, because they need a lower temperature."),
  blk("s6.tip", "teacher_tip", title="Show it in class",
    body="Cut a Hibiscus or mustard flower lengthwise and let students find the sepals, petals, anthers, stigma, style and ovary with a hand lens. Grow bread mould on moist bread for Rhizopus, and put a Bryophyllum leaf on moist soil to show buds growing from its edges. "
         "Handle the human reproduction topic factually and respectfully, and let students ask questions in writing if they are shy."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why bananas are grown from suckers and not seeds, and why sexual reproduction gives more variation than asexual reproduction."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 6:** testosterone and oestrogen bring the changes of puberty.\n- **Chapter 8, Heredity:** how traits pass from parents to offspring through DNA.\n"
         "- **Class 12 Biology:** reproduction in flowering plants, human reproduction and reproductive health in detail."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A farmer has a mango tree that gives very sweet fruit. He wants many trees with exactly the same fruit.\n\n"
         "(a) Should he grow them from seeds? (b) What method should he use? (c) Give one advantage and one disadvantage of this method.\n\n"
         "**Answer:** (a) No: seeds come from sexual reproduction, so the new trees would show variation and the fruit may not be as sweet. "
         "(b) Vegetative propagation, for example grafting. (c) Advantage: the new plants are genetically similar to the parent and bear fruit earlier. Disadvantage: there is no variation, so all the trees may be harmed alike by a new disease."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Reproduction involves copying DNA; small copying errors cause variation, which helps a species survive changes and is the basis of evolution.\n"
         "- Asexual reproduction: fission, fragmentation, regeneration, budding, vegetative propagation and spore formation.\n"
         "- Sexual reproduction combines DNA from two parents through gametes with half the chromosomes, giving more variation.\n"
         "- In flowering plants, pollination is followed by fertilisation; the ovule becomes the seed and the ovary the fruit.\n"
         "- In humans, puberty prepares the body; testes make sperms, ovaries release eggs; the embryo is nourished through the placenta; menstruation occurs when the egg is not fertilised.\n"
         "- Contraceptive methods and awareness of STDs protect reproductive health; female foeticide is illegal."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Practise labelled diagrams: longitudinal section of a flower, germination of pollen on the stigma, binary fission in Amoeba, budding in Hydra, and the human male and female reproductive systems.\n"
         "- Learn one example for each asexual method.\n- Know the three changes in a flower after fertilisation (SQP marking scheme).\n"
         "- In 'difference' questions (pollination vs fertilisation, asexual vs sexual, binary vs multiple fission), write points in a table."),
  blk("s7.flash1", "flashcard", front="What does the ovule become after fertilisation?", back="The seed (the ovary becomes the fruit)."),
  blk("s7.flash2", "flashcard", front="Function of the placenta", back="Passes glucose and oxygen from the mother to the embryo, and wastes from the embryo to the mother."),
  blk("s7.flash3", "flashcard", front="Why are the testes outside the abdomen?", back="Sperm formation needs a temperature lower than the normal body temperature."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "How do Organisms Reproduce?",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 7,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: reproduction in animals and plants (asexual and sexual), reproductive health, need for and methods of family planning, safe sex vs HIV/AIDS, childbearing and women's health.",
  "concepts": ["asexual", "sexual_plants", "human_reproduction"], "sections": sections}

# ---------------------------------------------------------------- questions
AS, SP, HR = "asexual", "sexual_plants", "human_reproduction"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 7 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [AS], it("7.1", 1), "What is the importance of DNA copying in reproduction?",
    answer_steps=["DNA carries the information for making proteins and so for the body design; copying it passes this design to the offspring.", "Small variations in copying give rise to variation, which helps the species survive changes."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [AS], it("7.1", 2), "Why is variation beneficial to the species but not necessarily for the individual?",
    answer_steps=["If the niche changes drastically, some variants may be suited to the new conditions and survive, so the species continues.", "For an individual, a variation may not help at all, and may even make it less suited to its present niche."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [AS], it("7.2", 1), "How does binary fission differ from multiple fission?", "easy",
    answer_steps=["Binary fission: one cell divides into two daughter cells (Amoeba, Leishmania).", "Multiple fission: one cell divides into many daughter cells at the same time (Plasmodium)."], marking_scheme=MS2P)
C.q("it2.q2", "very_short_answer", 2, [AS], it("7.2", 2), "How will an organism be benefited if it reproduces through spores?",
    answer_steps=["A large number of spores are produced, and they spread easily to new places.", "Spores have thick walls that protect them in unfavourable conditions until they reach a moist surface and grow."], marking_scheme=MS2P)
C.q("it2.q3", "very_short_answer", 2, [AS], it("7.2", 3), "Can you think of reasons why more complex organisms cannot give rise to new individuals through regeneration?",
    answer_steps=["Complex organisms have highly specialised cells, tissues and organ systems that work together.", "A cut piece does not have the specialised cells needed to grow all these again, so it cannot form a complete organism."], marking_scheme=MS2P)
C.q("it2.q4", "very_short_answer", 2, [AS], it("7.2", 4), "Why is vegetative propagation practised for growing some types of plants?",
    answer_steps=["It grows plants that have lost the ability to produce seeds (banana, orange, rose, jasmine).", "The new plants are genetically similar to the parent, so good qualities are kept, and they bear flowers and fruits earlier than plants from seeds."], marking_scheme=MS2P)
C.q("it2.q5", "very_short_answer", 2, [AS], it("7.2", 5), "Why is DNA copying an essential part of the process of reproduction?",
    answer_steps=["DNA has the information for the body design; a new cell needs its own copy of the DNA to work.", "So in reproduction the DNA is copied, and one copy goes into each new cell or offspring."], marking_scheme=MS2P)
C.q("it3.q1", "very_short_answer", 2, [SP], it("7.3", 1), "How is the process of pollination different from fertilisation?", "easy",
    answer_steps=["Pollination is the transfer of pollen grains from the anther to the stigma.", "Fertilisation is the fusion of the male germ cell with the egg cell in the ovule, forming a zygote; it happens after pollination."], marking_scheme=MS2P)
C.q("it3.q2", "very_short_answer", 2, [HR], it("7.3", 2), "What is the role of the seminal vesicles and the prostate gland?",
    answer_steps=["They add their secretions to the sperms, so that the sperms are in a fluid.", "This fluid makes their transport easier and also provides nutrition."], marking_scheme=MS2P)
C.q("it3.q3", "very_short_answer", 2, [HR], it("7.3", 3), "What are the changes seen in girls at the time of puberty?", "easy",
    answer_steps=["Thick hair grows in the armpits and genital area; the skin becomes oily and pimples may appear.", "The breasts begin to grow, the skin of the nipples darkens, and menstruation starts."], marking_scheme=MS2P)
C.q("it3.q4", "very_short_answer", 2, [HR], it("7.3", 4), "How does the embryo get nourishment inside the mother's body?",
    answer_steps=["Through the placenta, a disc-like tissue embedded in the uterine wall.", "Villi on the embryo's side face blood spaces on the mother's side, so glucose and oxygen pass from the mother to the embryo."], marking_scheme=MS2P)
C.q("it3.q5", "very_short_answer", 2, [HR], it("7.3", 5), "If a woman is using a copper-T, will it help in protecting her from sexually transmitted diseases?",
    answer_steps=["No.", "A copper-T only prevents pregnancy; it does not stop contact with body fluids. Only barrier methods such as condoms protect against many STDs."], marking_scheme=["1 mark: answer", "1 mark: reason"])
# Exercises
C.mcq("ex.q1", [AS], "Asexual reproduction takes place through budding in", ["Amoeba.", "Yeast.", "Plasmodium.", "Leishmania."], 1, "Yeast reproduces by budding; the others use fission.", source=ex(1))
C.mcq("ex.q2", [HR], "Which of the following is not a part of the female reproductive system in human beings?", ["Ovary", "Uterus", "Vas deferens", "Fallopian tube"], 2,
      "The vas deferens carries sperms in the male.", source=ex(2))
C.mcq("ex.q3", [SP], "The anther contains", ["sepals.", "ovules.", "pistil.", "pollen grains."], 3, "The anther of the stamen produces pollen grains.", source=ex(3))
C.q("ex.q4", "very_short_answer", 2, [SP], ex(4), "What are the advantages of sexual reproduction over asexual reproduction?",
    answer_steps=["DNA from two parents combines, so the offspring show more variation.", "This variation helps the species survive changes in the environment and is the basis of evolution."], marking_scheme=MS2P)
C.q("ex.q5", "very_short_answer", 2, [HR], ex(5), "What are the functions performed by the testis in human beings?", "easy",
    answer_steps=["The testes produce the male germ cells, sperms.", "They also secrete the hormone testosterone, which regulates sperm formation and brings changes at puberty in boys."], marking_scheme=MS2P)
C.q("ex.q6", "very_short_answer", 2, [HR], ex(6), "Why does menstruation occur?",
    answer_steps=["Every month the uterus prepares a thick, spongy lining with blood vessels to receive and nourish a fertilised egg.", "If the egg is not fertilised, this lining is not needed; it breaks down and comes out through the vagina as blood and mucus."], marking_scheme=MS2P)
C.q("ex.q7", "short_answer", 3, [SP], ex(7), "Draw a labelled diagram of the longitudinal section of a flower.",
    answer_steps=["Outer whorls: sepals and petals on the receptacle.", "Stamens: filament and anther (with pollen grains).", "Pistil in the centre: stigma, style and ovary containing ovules."],
    marking_scheme=["1 mark: diagram", "1 mark: labels", "1 mark: labels"])
C.q("ex.q8", "short_answer", 3, [HR], ex(8), "What are the different methods of contraception?",
    answer_steps=["Mechanical barrier: condoms or similar coverings stop sperms from reaching the egg (and protect against many infections).",
                  "Hormonal: oral pills change the hormonal balance so that eggs are not released; or a copper-T or loop is placed in the uterus.",
                  "Surgical: the vas deferens is blocked in males, or the fallopian tube is blocked in females."], marking_scheme=MS3)
C.q("ex.q9", "very_short_answer", 2, [AS], ex(9), "How are the modes for reproduction different in unicellular and multicellular organisms?",
    answer_steps=["Unicellular organisms reproduce by simple cell division: fission (binary or multiple) or budding.", "Multicellular organisms have specialised cells, so they use special methods: fragmentation, regeneration, vegetative propagation, spores or sexual reproduction with gametes."], marking_scheme=MS2P)
C.q("ex.q10", "very_short_answer", 2, [AS], ex(10), "How does reproduction help in providing stability to populations of species?",
    answer_steps=["Reproduction replaces individuals that die, so the number in the population stays steady.", "Consistent DNA copying keeps the body design suited to the niche, while some variation helps the species survive changes."], marking_scheme=MS2P)
C.q("ex.q11", "very_short_answer", 2, [HR], ex(11), "What could be the reasons for adopting contraceptive methods?", "easy",
    answer_steps=["To avoid unwanted pregnancies, keep a gap between children and protect the mother's health.", "To control the population, and (with condoms) to prevent the spread of sexually transmitted diseases."], marking_scheme=MS2P)
# CBSE sample paper
C.q("sqp16a", "long_answer", 5, [AS], SQP("16(A)"), "Puneet wanted to grow banana plants.\n\n(i) Based on your knowledge on plant reproduction should he opt for seeds or any alternate method of reproduction. Justify your answer.\n\n"
    "(ii) Offsprings of a banana plant usually show very little variation. What causes variation and are variations good or bad? Justify.", "medium",
    answer_steps=["(i) Puneet should not choose seeds, as banana plants have lost the capacity to produce seeds.", "He should go for vegetative propagation of banana (by stem cutting).",
                  "(ii) Errors and variations in DNA copying cause variation.", "Variation is good, as it can help a population tide over unfavourable conditions by the survival of some variants.",
                  "It can be bad, as the parents' desirable characters may be lost, or some variants may not be able to survive in the new conditions."],
    marking_scheme=["1 mark: (i) answer", "1 mark: (i) method", "1 mark: (ii) cause", "1 mark: (ii) good", "1 mark: (ii) bad"])
C.q("sqp16b", "long_answer", 5, [SP], SQP("16(B)"), "Annie was conducting research on the number of fruits produced by watermelon under different conditions. She grew 25 watermelon plants each in both glass house A and B. She introduced pollinators in glass house A only.\n\n"
    "(i) What difference will she observe in the number of fruits produced in the two glass houses? Explain with reason.\n\n(ii) List 3 changes that will occur in a flower once it gets fertilized.", "medium",
    answer_steps=["(i) Watermelon has unisexual flowers; the male and female flowers are separate.",
                  "Pollinators help cross-pollination, increasing the chance of fertilisation, so glass house A will produce more fruits; without pollinators, pollen rarely reaches the stigma and fewer fruits form in B.",
                  "(ii) The ovule develops a tough coat and becomes the seed.", "The ovary grows and ripens to form the fruit.", "Petals, sepals, stamens, style and stigma may shrivel and fall off."],
    marking_scheme=["1 mark: (i) unisexual", "1 mark: (i) difference", "1 mark: (ii) seed", "1 mark: (ii) fruit", "1 mark: (ii) other parts"])
# GSEB
C.q("gseb2024_29", "very_short_answer", 2, [HR], gseb(2024, "29"), "Gonorrhoea, syphilis, HIV-AIDS and warts are sexually transmitted diseases.\n\n(a) Classify these infections into those spread by bacteria and those spread by viruses.\n\n(b) Write the mechanical barrier method of contraception for unwanted pregnancies.",
    answer_steps=["(a) Bacterial: gonorrhoea and syphilis. Viral: HIV-AIDS and warts.", "(b) Condoms on the penis, or similar coverings worn in the vagina, which stop the sperm from reaching the egg."], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("gseb2024_42", "short_answer", 3, [AS], gseb(2024, "42"), "Write the names of different types of asexual reproduction. Explain any two types of asexual reproduction.",
    answer_steps=["Types: fission, fragmentation, regeneration, budding, vegetative propagation and spore formation.",
                  "Binary fission: a unicellular organism such as Amoeba splits into two daughter cells.",
                  "Budding: in Hydra, a bud develops as an outgrowth due to repeated cell division at one site; it grows into a tiny individual and detaches when mature."], marking_scheme=MS3)
C.q("gseb2024_43", "short_answer", 3, [HR], gseb(2024, "43"), "(a) Draw a neat labelled diagram of human male reproductive system.\n\n(b) Write the functions of testis.",
    answer_steps=["(a) Labels: testis, scrotum, vas deferens, seminal vesicle, prostate gland, urethra, penis, urinary bladder.",
                  "(b) The testes produce sperms.", "They secrete testosterone, which regulates sperm formation and brings the changes of puberty in boys."], marking_scheme=["1 mark: diagram", "1 mark: sperms", "1 mark: testosterone"])
C.q("gseb2025_28", "very_short_answer", 2, [AS], gseb(2025, "28"), "Name any four modes of reproduction used by single organisms.", "easy",
    answer_steps=["Fission (binary or multiple) and budding.", "Fragmentation, regeneration, vegetative propagation or spore formation (any two)."], marking_scheme=MS2P)
C.q("gseb2025_29", "very_short_answer", 2, [SP], gseb(2025, "29"), "What is called an unisexual flower? Write its examples.", "easy",
    answer_steps=["A flower that has either stamens or a pistil, but not both, is a unisexual flower.", "Examples: papaya and watermelon."], marking_scheme=["1 mark: definition", "1 mark: examples"])
C.q("gseb2025_42", "short_answer", 3, [HR], gseb(2025, "42"), "What are the changes seen in girls at the time of puberty?",
    answer_steps=["Thick hair grows in the armpits and genital area, and thinner hair on the legs and arms.", "The skin becomes oily and pimples may appear; the breasts begin to grow and the skin of the nipples darkens.",
                  "Menstruation starts."], marking_scheme=MS3)
# Shine MCQs
C.mcq("mcq01", [AS], "Leishmania reproduces by:", ["binary fission in a definite plane", "multiple fission", "budding", "spore formation"], 0, "Leishmania has a whip-like structure at one end and splits in a definite plane.", "medium")
C.mcq("mcq02", [AS], "Spirogyra reproduces asexually by:", ["fragmentation", "budding", "multiple fission", "regeneration only"], 0, "A Spirogyra filament breaks into pieces that grow into new filaments.")
C.mcq("mcq03", [AS], "Buds in the notches of the leaf margin grow into new plants in:", ["Bryophyllum", "Rose", "Mango", "Wheat"], 0, "Bryophyllum leaves carry buds along their edges.")
C.mcq("mcq04", [AS], "Rhizopus (bread mould) reproduces by:", ["spore formation", "binary fission", "fragmentation", "budding"], 0, "Rhizopus forms spores in sporangia.")
C.mcq("mcq05", [SP], "A bisexual flower is:", ["Hibiscus", "Papaya", "Watermelon", "None of these"], 0, "Hibiscus has both stamens and a pistil; papaya and watermelon have unisexual flowers.", "medium")
C.mcq("mcq06", [SP], "The transfer of pollen from the anther to the stigma is called:", ["pollination", "fertilisation", "germination", "regeneration"], 0, "That is pollination; fertilisation is the fusion of gametes that follows.")
C.mcq("mcq07", [HR], "The testes are located in the scrotum because:", ["sperm formation needs a lower temperature", "they need more blood", "they are too large", "they make urine"], 0, "Sperms form at a temperature lower than the normal body temperature.")
C.mcq("mcq08", [HR], "The embryo gets oxygen and glucose from the mother through the:", ["placenta", "ovary", "oviduct", "cervix"], 0, "The placenta passes oxygen and glucose to the embryo and removes its wastes.")
C.mcq("mcq09", [HR], "Which of these diseases is caused by a virus?", ["HIV-AIDS", "Gonorrhoea", "Syphilis", "None of these"], 0, "HIV-AIDS and warts are viral; gonorrhoea and syphilis are bacterial.", "medium")
C.mcq("mcq10", [AS], "The number of chromosomes in a gamete compared to a body cell is:", ["half", "double", "the same", "one-fourth"], 0, "Gametes have half, so the zygote has the full number again.", "medium")
# Assertion-reason
C.ar("ar1", [SP], "Gametes have half the number of chromosomes of body cells.", "When two gametes fuse, the zygote must have the normal number of chromosomes.", 0,
     "Halving in the gametes restores the full number in the zygote: R explains A.")
C.ar("ar2", [AS], "Banana is grown by vegetative propagation.", "Banana plants have lost the capacity to produce seeds.", 0,
     "Without seeds, vegetative propagation is the way to grow banana: R explains A.")
C.ar("ar3", [SP], "Pollination and fertilisation are the same process.", "Fertilisation takes place after pollination.", 3,
     "A is false: pollination transfers pollen; fertilisation is the fusion of gametes. R is true.")
C.ar("ar4", [HR], "A copper-T protects a woman from sexually transmitted diseases.", "A copper-T is placed in the uterus to prevent pregnancy.", 3,
     "A is false: a copper-T only prevents pregnancy; it gives no protection against STDs. R is true.")
C.ar("ar5", [AS], "Planaria can regenerate a complete body from a small piece.", "Planaria has specialised cells that can divide and develop into different tissues.", 0,
     "These cells rebuild all the tissues: R explains A.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [SP], SHINE, "Name the male and female reproductive parts of a flower, with their parts.", "easy",
    answer_steps=["Male: stamen, made of the filament and the anther (which makes pollen grains).", "Female: pistil (carpel), made of the stigma, style and ovary (which contains ovules)."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [HR], SHINE, "Why is prenatal sex determination prohibited by law?", "easy",
    answer_steps=["Some people misuse it for female foeticide, the selective killing of female foetuses.", "This is reducing the number of girls in some places; a healthy society needs a healthy sex ratio."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [AS], SHINE, "Describe regeneration and budding in Hydra. Why can complex animals not reproduce by regeneration?",
    answer_steps=["Regeneration: if Hydra is cut into pieces, each piece grows into a complete organism, using specialised cells that divide and develop into tissues.",
                  "Budding: a bud forms as an outgrowth by repeated cell division at one site, grows into a tiny Hydra and detaches when mature.",
                  "Complex animals have highly specialised cells and organ systems that a cut piece cannot rebuild."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [SP], SHINE, "Describe the process of fertilisation in a flowering plant after the pollen lands on the stigma.",
    answer_steps=["The pollen grain germinates on the stigma and a pollen tube grows through the style towards the ovule.", "The male germ cell travels down the tube and fuses with the egg cell in the ovule, forming a zygote.",
                  "The zygote develops into an embryo; the ovule becomes the seed and the ovary the fruit."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [HR], SHINE, "Describe the human female reproductive system. Where does fertilisation take place? How is the embryo nourished?", "medium",
    answer_steps=["Two ovaries release one egg every month and make the hormones oestrogen and progesterone.", "The egg is carried through the oviduct (fallopian tube) to the uterus, which opens into the vagina through the cervix.",
                  "Fertilisation takes place in the oviduct.", "The zygote is implanted in the thick lining of the uterus and develops into an embryo.",
                  "The placenta passes glucose and oxygen from the mother's blood to the embryo, and wastes from the embryo to the mother."],
    marking_scheme=["1 mark: ovaries", "1 mark: oviduct and uterus", "1 mark: fertilisation", "1 mark: implantation", "1 mark: placenta"])
C.q("la2", "long_answer", 5, [AS], SHINE, "What is vegetative propagation? Give two natural and one artificial example. List its advantages.", "medium",
    answer_steps=["Vegetative propagation is the growth of a new plant from a vegetative part (root, stem or leaf) of the parent.", "Natural: buds on the leaf margin of Bryophyllum; stem of potato or ginger.",
                  "Artificial: layering or grafting (for example roses, grapes, mango); tissue culture.", "Advantage: plants that have lost the ability to make seeds (banana, orange, rose, jasmine) can be grown.",
                  "Advantage: the new plants are genetically similar to the parent and bear flowers and fruits earlier."],
    marking_scheme=["1 mark: definition", "1 mark: natural examples", "1 mark: artificial example", "1 mark: first advantage", "1 mark: second advantage"])
C.q("cb1", "case_based", 4, [SP], SHINE,
    "Kiran observed bees visiting the flowers of a mustard field. Later, the flowers dried up and pods full of seeds formed. His teacher said the bees help the plants to produce seeds.\n\n"
    "(i) What process do the bees help with? (1)\n\n(ii) Is mustard a unisexual or a bisexual flower? (1)\n\n(iii) What happens after the pollen reaches the stigma? OR Which parts of the flower become the seed and the fruit? (2)",
    answer_steps=["(i) Pollination (cross-pollination).", "(ii) Bisexual.", "(iii) A pollen tube grows through the style to the ovule, and the male germ cell fuses with the egg to form a zygote. OR The ovule becomes the seed, and the ovary becomes the fruit (the pod)."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [AS], SHINE,
    "In a science club, students kept a slice of moist bread in a closed box. After a few days, a black cottony growth appeared. They also cut a Planaria into three pieces in a petri dish, and after some days found three complete Planaria.\n\n"
    "(i) Name the organism growing on the bread. (1)\n\n(ii) How does it reproduce? (1)\n\n(iii) What is the process seen in Planaria, and why can it happen? OR Why do spores survive for a long time? (2)",
    answer_steps=["(i) Rhizopus (bread mould).", "(ii) By spore formation.",
                  "(iii) Regeneration: Planaria has specialised cells that can divide and develop into all the tissues. OR Spores have thick walls that protect them until they reach a moist surface."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch07.q.ex."))
