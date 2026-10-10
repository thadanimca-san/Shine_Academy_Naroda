"""CBSE Class 10 Science Ch 8: Heredity.
Every cross used in the chapter is checked by enumerating the gametes below."""
import sys
from collections import Counter
from itertools import product
from sci_common import Chapter, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch08"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch08_heredity"
C = Chapter("sci10ch08")
blk = C.blk

def gametes(genotype):
    """'TtWW' -> every gamete, one letter from each gene pair."""
    pairs = [genotype[i:i + 2] for i in range(0, len(genotype), 2)]
    return ["".join(g) for g in product(*pairs)]
def cross(a, b):
    """Counter of offspring phenotypes; a capital letter in a gene pair means the dominant trait shows."""
    out = Counter()
    for x, y in product(gametes(a), gametes(b)):
        out[tuple(any(c.isupper() for c in (p, q)) for p, q in zip(x, y))] += 1
    from math import gcd
    from functools import reduce
    g = reduce(gcd, out.values())
    return Counter({k: v // g for k, v in out.items()})
# Fig. 8.3: TT x tt gives all tall; F1 selfed gives 3 tall : 1 short (TT : Tt : tt = 1 : 2 : 1)
check(cross("TT", "tt") == Counter({(True,): 1}), "F1 all tall")
check(cross("Tt", "Tt") == Counter({(True,): 3, (False,): 1}), "F2 3 : 1")
# Exercise 1: tall violet x short white (ttww) gives all violet, about half short -> TtWW
check(cross("TtWW", "ttww") == Counter({(True, True): 1, (False, True): 1}), "exercise 1: TtWW")
check(any(not w for _, w in cross("TtWw", "ttww")), "TtWw would give some white flowers")
# SQP 14: RRyy x rrYY -> F1 RrYy; selfed gives 9 : 3 : 3 : 1, i.e. 81 : 27 : 27 : 9 of 144
f2 = cross("RrYy", "RrYy")
check(sorted(f2.values(), reverse=True) == [9, 3, 3, 1] and sum(f2.values()) == 16, "dihybrid 9:3:3:1")
check([144 * f2[k] // 16 for k in [(True, True), (True, False), (False, True), (False, False)]] == [81, 27, 27, 9], "SQP 14 counts")
check(sorted(gametes("RrYy")) == sorted(["RY", "Ry", "rY", "ry"]), "SQP 14 gametes")
# SQP 5: BB x bb gives all black; Bb x bb would give some white
check(set(cross("BB", "bb")) == {(True,)} and (False,) in cross("Bb", "bb") and (False,) in cross("Bb", "Bb"), "SQP 5")

MONO = ("| Gametes | T | t |\n|---|---|---|\n| **T** | TT (tall) | Tt (tall) |\n| **t** | Tt (tall) | tt (short) |")
DI = ("| Gametes | RY | Ry | rY | ry |\n|---|---|---|---|---|\n| **RY** | RRYY | RRYy | RrYY | RrYy |\n| **Ry** | RRYy | RRyy | RrYy | Rryy |\n"
      "| **rY** | RrYY | RrYy | rrYY | rrYy |\n| **ry** | RrYy | Rryy | rrYy | rryy |")
check(all(cell.count("R") + cell.count("r") == 2 for row in DI.splitlines()[2:] for cell in row.split(" | ")[1:]), "dihybrid table cells")
SEX = ("| Gametes from mother | X | X |\n|---|---|---|\n| **X** (from father) | XX (girl) | XX (girl) |\n| **Y** (from father) | XY (boy) | XY (boy) |")

sections = [
 {"id": "s1", "title": "Like parent, like child?", "blocks": [
  blk("s1.hook", "hook", title="Where did those eyes come from?",
    body="People often say a baby has the mother's eyes and the father's smile. Sometimes a child has a feature that neither parent shows, but a grandparent did.\n\n"
         "How are features passed on, and why do some skip a generation? About 160 years ago, a monk named **Gregor Mendel** found the answer by counting pea plants. "
         "In this chapter you will learn his rules of **heredity**, how genes control traits, and how the sex of a child is decided."),
  blk("s1.inspiration", "inspiration", title="Reading the language of genes", person="Har Gobind Khorana", years="1922–2011",
    body="Har Gobind Khorana was born in Raipur, a small village in Punjab (now in Pakistan), and studied in Lahore and Liverpool. He worked out how the order of the bases in DNA spells out the order of amino acids in a protein: the **genetic code**.\n\n"
         "For this he shared the **Nobel Prize** in Physiology or Medicine in 1968. Later his team made the first **artificial gene**.",
    future="Genetics leads to careers in medicine, genetic counselling, plant and animal breeding, forensic science and biotechnology."),
  blk("s1.socratic", "socratic_question", question="Two tall pea plants are crossed and some of their offspring are short. What does this tell you?",
    options=["Both parents carried a hidden factor for shortness", "Shortness appeared from nowhere", "The plants were not peas"], correct_index=0,
    explanation="Each parent must have carried one copy of the factor for shortness (Tt), which is hidden by the factor for tallness."),
 ]},
 {"id": "s2", "title": "Variation during reproduction", "blocks": [
  blk("s2.reveal", "theory", title="Variations add up", revision=True,
    body="Each generation inherits the basic body design of the previous one, with small **variations**.\n\n"
         "- In **asexual** reproduction, variations are few, coming only from small errors in DNA copying. The second generation shows the variations of the first plus its own.\n"
         "- In **sexual** reproduction, DNA from two parents combines, so there is much more variety.\n\n"
         "Not all variations are equally useful. Depending on the environment, some variants have an advantage: for example, bacteria that can stand heat survive a heat wave better. "
         "The environment **selects** such variants, and this is the basis of **evolution**.\n\n"
         "In an asexually reproducing population, a variation found in more individuals has usually been passed on for more generations, so it probably **arose earlier**."),
  blk("s2.check", "knowledge_check", question="Which kind of reproduction produces more variation?",
    options=["Sexual reproduction", "Asexual reproduction", "Both produce the same", "Neither produces any variation"], correct_index=0,
    explanation="Sexual reproduction combines DNA from two parents, while asexual reproduction depends only on small copying errors."),
 ]},
 {"id": "s3", "title": "Mendel's experiments: one trait", "blocks": [
  blk("s3.thm", "theory", title="Dominant and recessive", revision=True,
    body="**Gregor Johann Mendel (1822–1884)** grew garden peas and was the first to **count** how many plants showed each trait in each generation. He used contrasting traits: tall/short plants, round/wrinkled seeds, violet/white flowers.\n\n"
         "- He crossed a pure **tall** plant with a pure **short** plant. All the first-generation (**F1**) plants were tall; there were no medium-height plants.\n"
         "- When F1 plants were **self-pollinated**, the second generation (**F2**) had both tall and short plants, in the ratio **3 tall : 1 short**.\n\n"
         "So both traits were inherited in F1, but only tallness was **expressed**. Mendel proposed that each trait is controlled by **two copies of a factor** (now called **genes**), one from each parent. "
         "A single copy of **T** is enough to make the plant tall (**dominant**); both copies must be **t** for the plant to be short (**recessive**).\n\n"
         "The F2 plants are **TT : Tt : tt = 1 : 2 : 1** (genotype), which look **3 tall : 1 short** (phenotype)."),
  blk("s3.table", "markdown_table", title="Crossing two F1 plants (Tt × Tt)", revision=True, body=MONO),
  blk("s3.check", "knowledge_check", question="In Mendel's cross of pure tall and pure short plants, what fraction of the F2 plants were short?",
    options=["One quarter", "One half", "Three quarters", "None"], correct_index=0,
    explanation="Tt × Tt gives TT, Tt, Tt and tt: only tt (one in four) is short."),
 ]},
 {"id": "s4", "title": "Two traits together", "blocks": [
  blk("s4.thm", "theory", title="Independent inheritance", revision=True,
    body="Mendel then crossed plants differing in **two** traits: a tall plant with round seeds and a short plant with wrinkled seeds. All the F1 plants were tall with round seeds, so tallness and round seeds are dominant.\n\n"
         "When the F1 plants were self-pollinated, the F2 had tall-round and short-wrinkled plants, but also **new combinations**: tall-wrinkled and short-round. "
         "This shows that the traits are **inherited independently**: the factor for height does not travel with the factor for seed shape.\n\n"
         "For seed shape (R round, r wrinkled) and seed colour (Y yellow, y green), an F1 plant RrYy makes four kinds of gametes: RY, Ry, rY and ry. Crossing two such plants gives "
         "**9 round yellow : 3 round green : 3 wrinkled yellow : 1 wrinkled green**."),
  blk("s4.table", "markdown_table", title="F2 of a cross with two traits (RrYy × RrYy)", revision=False, body=DI),
  blk("s4.check", "knowledge_check", question="Which gametes can a plant with genotype RrYy produce?",
    options=["RY, Ry, rY, ry", "Rr and Yy", "RY and ry only", "RR, rr, YY, yy"], correct_index=0,
    explanation="Each gamete gets one copy of each gene, in every combination: RY, Ry, rY and ry."),
 ]},
 {"id": "s5", "title": "How traits are expressed", "blocks": [
  blk("s5.thm", "theory", title="Genes, proteins and traits", revision=True,
    body="The cell's DNA carries the information for making proteins. A section of DNA that provides the information for one protein is a **gene**.\n\n"
         "**Example, plant height:** plants have hormones that trigger growth. The amount of hormone depends on how efficiently an **enzyme** makes it. "
         "If the gene for the enzyme works well, plenty of hormone is made and the plant is tall. If the gene has an alteration that makes the enzyme less efficient, less hormone is made and the plant is short. "
         "So genes control characteristics (traits).\n\n"
         "**Why the two copies come in halves:** genes are carried on **chromosomes**. Each body cell has two copies of each chromosome, one from each parent. "
         "Each germ cell takes **one chromosome from each pair**, so when two germ cells combine, the offspring has the normal number again. This also explains independent inheritance: each pair separates on its own."),
  blk("s5.check", "knowledge_check", question="A gene affects plant height by controlling the making of:",
    options=["an enzyme that makes a growth hormone", "chlorophyll only", "the cell wall only", "water in the cells"], correct_index=0,
    explanation="The gene gives the information for an enzyme; the efficiency of the enzyme decides how much growth hormone is made."),
 ]},
 {"id": "s6", "title": "Sex determination", "blocks": [
  blk("s6.thm", "theory", title="X and Y", revision=True,
    body="Different species use different ways to decide the sex of a new individual:\n- In some reptiles, the **temperature** at which the fertilised eggs are kept decides whether the young are male or female.\n"
         "- Some animals, such as **snails**, can **change sex**.\n- In **humans**, sex is decided **genetically**.\n\n"
         "Humans have 23 pairs of chromosomes. 22 pairs are the same in men and women. The remaining pair are the **sex chromosomes**: women have a perfect pair, **XX**; men have a mismatched pair, **XY** (Y is shorter).\n\n"
         "All of a mother's eggs carry an X. Half of a father's sperms carry X and half carry Y. So the sex of the child depends on the **father's** sperm: an X-sperm gives a girl (XX), a Y-sperm gives a boy (XY). "
         "The chance is half and half each time.\n\n" + SEX),
  blk("s6.check", "knowledge_check", question="A child who inherits a Y chromosome from the father will be a:",
    options=["boy", "girl", "either, depending on the mother", "either, depending on the temperature"], correct_index=0,
    explanation="The mother always gives an X; X from the mother plus Y from the father gives XY, a boy."),
  blk("s6.memory", "memory_trick", title="Ratios to remember",
    body="- **One trait:** F2 = **3 : 1** (look), **1 : 2 : 1** (genes).\n- **Two traits:** F2 = **9 : 3 : 3 : 1** (all 16 boxes of the square).\n"
         "- **Capital wins:** one capital letter is enough to show the dominant trait; you need two small letters to see the recessive one.\n- **Y makes the boy, and only the father has Y.**"),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing that the mother decides the sex of the child: the father's sperm (X or Y) decides it.\n- Writing the F2 ratio of a one-trait cross as 1 : 2 : 1 when the question asks what the plants look like: that is 3 : 1.\n"
         "- Writing the gametes of RrYy as Rr and Yy: a gamete has one copy of each gene (RY, Ry, rY, ry).\n"
         "- Saying a trait is dominant just because a child has it: the blood group example shows you need more information."),
  blk("s6.tip", "teacher_tip", title="Count it in class",
    body="Give each pair of students two bags, each with 10 red and 10 white beads (red = T, white = t). They draw one bead from each bag, note the pair, and put the beads back; after 40 draws, count TT, Tt and tt. "
         "The class total comes close to 1 : 2 : 1, which is exactly what Mendel did with peas. Toss a coin for the father's X or Y to show the half-and-half chance of a boy or girl."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why two tall pea plants can have a short offspring, but two short pea plants can never have a tall offspring."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 7:** germ cells with half the chromosomes make sexual reproduction possible.\n- **Class 12 Biology:** principles of inheritance and variation, molecular basis of inheritance, and evolution.\n"
         "- **Everyday life:** plant breeders use these rules to develop better crops, and doctors use them to explain inherited diseases."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A tall pea plant with violet flowers is crossed with a short plant with white flowers (ttww). All the offspring have violet flowers, and about half are tall and half short.\n\n"
         "(a) What is the genotype of the tall parent? (b) Explain.\n\n"
         "**Answer:** (a) TtWW. (b) All flowers are violet, so the tall parent must have given W every time: it is WW (if it were Ww, half the offspring would be white). "
         "Half are short, so the tall parent gave t to half of its gametes: it is Tt. Crossing TtWW × ttww gives TtWw (tall violet) and ttWw (short violet) in equal numbers."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Variations accumulate over generations; sexual reproduction gives the most variety, and the environment selects useful variants.\n"
         "- Mendel found that traits are controlled by pairs of factors (genes), one from each parent; one is dominant and the other recessive.\n"
         "- One-trait cross: F2 is 3 : 1 in appearance and 1 : 2 : 1 in genes. Two-trait cross: F2 is 9 : 3 : 3 : 1, showing independent inheritance.\n"
         "- Genes make proteins such as enzymes, which control traits like plant height.\n"
         "- Germ cells take one chromosome of each pair. In humans, women are XX and men XY; the father's sperm decides the sex of the child."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Always draw a checkerboard (Punnett square) for crosses: write the gametes along the top and side.\n- Learn both ratios: 3 : 1 and 9 : 3 : 3 : 1, and be able to scale them (for example 144 seeds: 81 : 27 : 27 : 9).\n"
         "- In sex-determination answers, show the cross XX × XY and conclude that the chance is 50% for each sex.\n- Read data questions carefully: one family's children are not enough to decide which trait is dominant."),
  blk("s7.flash1", "flashcard", front="F2 phenotype ratio of a monohybrid (one-trait) cross", back="3 : 1 (genotype ratio 1 : 2 : 1)"),
  blk("s7.flash2", "flashcard", front="F2 phenotype ratio of a dihybrid (two-trait) cross", back="9 : 3 : 3 : 1"),
  blk("s7.flash3", "flashcard", front="Sex chromosomes in human males and females", back="Males XY, females XX"),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Heredity",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 8,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: heredity; Mendel's contribution - laws for inheritance of traits; sex determination: brief introduction.",
  "concepts": ["variation", "mendel", "sex_determination"], "sections": sections}

# ---------------------------------------------------------------- questions
VA, ME, SD = "variation", "mendel", "sex_determination"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 8 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [VA], it("8.1", 1), "If a trait A exists in 10% of a population of an asexually reproducing species and a trait B exists in 60% of the same population, which trait is likely to have arisen earlier?",
    answer_steps=["Trait B.", "In asexual reproduction a variation spreads only as it is passed on through generations, so the trait found in more individuals (60%) has probably been passed on for longer."], marking_scheme=["1 mark: answer", "1 mark: reason"])
C.q("it1.q2", "very_short_answer", 2, [VA], it("8.1", 2), "How does the creation of variations in a species promote survival?",
    answer_steps=["When the environment changes, some variants may be better suited to the new conditions.", "These variants survive and reproduce, so the species continues even if others die; for example, heat-resistant bacteria survive a heat wave."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [ME], it("8.2", 1), "How do Mendel's experiments show that traits may be dominant or recessive?",
    answer_steps=["When pure tall and pure short plants were crossed, all F1 plants were tall: only the tall trait was expressed, so it is dominant.",
                  "On self-pollinating F1, one quarter of the F2 plants were short: the short trait had been inherited but hidden in F1, so it is recessive."], marking_scheme=MS2P)
C.q("it2.q2", "short_answer", 3, [ME], it("8.2", 2), "How do Mendel's experiments show that traits are inherited independently?",
    answer_steps=["Mendel crossed tall plants with round seeds and short plants with wrinkled seeds; all F1 plants were tall with round seeds.",
                  "On self-pollinating F1, the F2 had the parental types and also new combinations: tall with wrinkled seeds and short with round seeds.",
                  "The new combinations show that height and seed shape were inherited independently of each other (ratio 9 : 3 : 3 : 1)."], marking_scheme=MS3)
C.q("it2.q3", "very_short_answer", 2, [ME], it("8.2", 3), "A man with blood group A marries a woman with blood group O and their daughter has blood group O. Is this information enough to tell you which of the traits – blood group A or O – is dominant? Why or why not?", "hard",
    answer_steps=["No, it is not enough.", "The daughter may have got O from both parents if the father carries a hidden O (then A would be dominant), or O may itself be dominant; one child from one family cannot tell which. Data from many families is needed."],
    marking_scheme=["1 mark: answer", "1 mark: reason"])
C.q("it2.q4", "short_answer", 3, [SD], it("8.2", 4), "How is the sex of the child determined in human beings?",
    answer_steps=["Women have a perfect pair of sex chromosomes, XX; men have a mismatched pair, XY.", "All eggs carry an X; half the sperms carry X and half carry Y.",
                  "If an X-sperm fertilises the egg, the child is a girl (XX); if a Y-sperm does, the child is a boy (XY). So the father's sperm decides the sex."], marking_scheme=MS3)
# Exercises
C.mcq("ex.q1", [ME], "A Mendelian experiment consisted of breeding tall pea plants bearing violet flowers with short pea plants bearing white flowers. The progeny all bore violet flowers, but almost half of them were short. This suggests that the genetic make-up of the tall parent can be depicted as",
      ["TTWW", "TTww", "TtWW", "TtWw"], 2, "All violet means the tall parent is WW; half short means it is Tt: TtWW.", "hard", source=ex(1))
C.q("ex.q2", "very_short_answer", 2, [ME], ex(2), "A study found that children with light-coloured eyes are likely to have parents with light-coloured eyes. On this basis, can we say anything about whether the light eye colour trait is dominant or recessive? Why or why not?", "hard",
    answer_steps=["No.", "Children having the same eye colour as their parents happens whether the trait is dominant or recessive; to decide, we would need families where parents of one type have children of the other type, and their numbers."],
    marking_scheme=["1 mark: answer", "1 mark: reason"])
C.q("ex.q3", "short_answer", 3, [ME], ex(3), "Outline a project which aims to find the dominant coat colour in dogs.",
    answer_steps=["Choose pure-breeding dogs of two coat colours, say black and brown (whose ancestors have shown only one colour for many generations).",
                  "Cross a black dog with a brown dog and record the coat colour of all the puppies (F1). The colour that appears in all F1 puppies is dominant.",
                  "To confirm, cross F1 dogs with each other: the F2 puppies should show about 3 of the dominant colour to 1 of the recessive colour."], marking_scheme=["1 mark: pure parents", "1 mark: F1", "1 mark: F2"])
C.q("ex.q4", "very_short_answer", 2, [ME, SD], ex(4), "How is the equal genetic contribution of male and female parents ensured in the progeny?",
    answer_steps=["Each germ cell (sperm or egg) carries only one chromosome of each pair, that is, half the genetic material.", "When a sperm and an egg fuse, each parent gives one set, so the offspring gets equal genetic material from both and the normal chromosome number is restored."], marking_scheme=MS2P)
# CBSE sample paper
C.mcq("sqp5", [ME], "In a cross between black furred rabbit (B) and white furred rabbit (b), all offspring were found to have black fur. What can be inferred about the genetic makeup of the parent rabbits?",
      ["BB X bb", "Bb X Bb", "Bb X bb", "bb X bb"], 0, "All black offspring means the black parent gave B every time: BB × bb gives only Bb (black).", "medium", source=SQP(5))
C.ar("sqp8", [ME], "Tallness of a pea plant is controlled by an enzyme.", "The gene for that enzyme makes proteins which help the plant to be tall.", 0,
     "The gene makes an enzyme that controls the amount of growth hormone, so it decides tallness: R explains A.", source=SQP(8))
C.q("sqp14", "short_answer", 3, [ME], SQP(14), "In a genetic experiment, plants with pure round green seeds (RRyy) were crossed with plants with wrinkled yellow seeds (rrYY).\n\n(i) Show the gametes formed when F1 was self-pollinated.\n\n"
    "(ii) A total of 144 seeds were produced which developed into saplings. Show the ratio in which these traits are independently inherited in these 144 saplings.", "hard",
    answer_steps=["F1 plants are RrYy (round, yellow).", "(i) Gametes: RY, Ry, rY, ry.",
                  "(ii) Round yellow 81, round green 27, wrinkled yellow 27, wrinkled green 9: ratio 9 : 3 : 3 : 1. (The official marking scheme prints the classes as tall/short; for seeds they are round/wrinkled and yellow/green.)"],
    marking_scheme=["1 mark: F1", "1 mark: (i)", "1 mark: (ii)"])
# GSEB
C.mcq("gseb2024_18", [ME], "In Mendel's experiment with pea plants, the F2 generation has the factor combinations TT, Tt and tt. Which of these plants show the recessive trait?",
      ["tt only", "TT only", "Tt only", "TT and Tt"], 0, "TT and Tt show the dominant trait (tall); only tt shows the recessive trait (short).", source=gseb(2024, "18"))
C.mcq("gseb2025_10", [SD], "____ animal can change sex.", ["Lizard", "Snail", "Frog"], 1, "Some animals, such as snails, can change sex.", source=gseb(2025, "10"))
C.tf("gseb2025_14", [SD], "A child who inherits a 'Y' chromosome from the father will be a girl.", False,
     "The child will be a boy: X from the mother and Y from the father give XY.", source=gseb(2025, "14"))
C.mcq("gseb2025_18", [VA], "If a trait A exists in 10% of a population of an asexually reproducing species and a trait B exists in 60% of the same population, which trait is likely to have arisen earlier?",
      ["Trait A", "Trait B", "Both arose at the same time", "It cannot be said"], 1, "The trait in more individuals has probably been passed on for more generations: trait B.", "medium", source=gseb(2025, "18"))
# Shine MCQs
C.mcq("mcq01", [ME], "Mendel's experiments were done on:", ["garden pea", "fruit fly", "maize", "rose"], 0, "Mendel used garden peas.")
C.mcq("mcq02", [ME], "In a cross between a pure tall (TT) and a pure short (tt) pea plant, the F1 plants are:", ["all tall", "all short", "half tall, half short", "medium height"], 0, "All F1 are Tt, which look tall.")
C.mcq("mcq03", [ME], "The genotype ratio in the F2 of a monohybrid cross is:", ["1 : 2 : 1", "3 : 1", "9 : 3 : 3 : 1", "1 : 1"], 0, "TT : Tt : tt = 1 : 2 : 1; the phenotype ratio is 3 : 1.", "medium")
C.mcq("mcq04", [ME], "The phenotype ratio in the F2 of a dihybrid cross is:", ["9 : 3 : 3 : 1", "3 : 1", "1 : 2 : 1", "1 : 1 : 1 : 1"], 0, "Two traits inherited independently give 9 : 3 : 3 : 1.")
C.mcq("mcq05", [ME], "A section of DNA that provides information for one protein is called a:", ["gene", "chromosome", "nucleus", "gamete"], 0, "That is a gene; chromosomes carry many genes.")
C.mcq("mcq06", [SD], "The sex chromosomes of a human male are:", ["XY", "XX", "YY", "XO"], 0, "Males have a mismatched pair, XY.")
C.mcq("mcq07", [SD], "In some reptiles, the sex of the young is decided by:", ["the temperature at which the eggs are kept", "the X and Y chromosomes", "the food of the mother", "the size of the egg"], 0,
      "In some reptiles, the incubation temperature of the fertilised eggs decides the sex.", "medium")
C.mcq("mcq08", [ME], "How many types of gametes does a plant with genotype Tt produce?", ["Two: T and t", "One: Tt", "Four", "One: T"], 0, "Each gamete gets one copy: T or t.", "medium")
C.mcq("mcq09", [ME], "A cross Tt × tt gives offspring in the ratio:", ["1 tall : 1 short", "3 tall : 1 short", "all tall", "all short"], 0, "Tt × tt gives Tt and tt in equal numbers.", "hard")
C.mcq("mcq10", [VA], "Variations are more in organisms that reproduce:", ["sexually", "asexually by fission", "by budding", "by fragmentation"], 0, "Sexual reproduction combines DNA from two parents.")
# Assertion-reason
C.ar("ar1", [SD], "The sex of a child in humans is decided by the father.", "Half of the sperms carry an X chromosome and half carry a Y chromosome.", 0,
     "All eggs carry X, so whether the sperm carries X or Y decides the sex: R explains A.")
C.ar("ar2", [ME], "All F1 plants of a cross between pure tall and pure short pea plants are tall.", "Tallness is a recessive trait.", 2,
     "A is true. R is false: tallness is dominant, which is why all F1 plants (Tt) are tall.")
C.ar("ar3", [ME], "A short pea plant always has the genotype tt.", "A recessive trait is expressed only when both copies of the gene are recessive.", 0,
     "Shortness is recessive, so it shows only in tt: R explains A.")
C.ar("ar4", [VA], "Variations are always useful to the individual.", "Variations help a species survive changes in the environment.", 3,
     "A is false: a variation may not help the individual at all. R is true.")
C.ar("ar5", [ME], "Germ cells have one chromosome from each pair.", "This keeps the chromosome number the same from one generation to the next.", 0,
     "Halving in the germ cells is restored when they fuse: R explains A.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [ME], SHINE, "Define dominant and recessive traits with one example each.", "easy",
    answer_steps=["Dominant trait: one that is expressed even when only one copy of its gene is present, e.g. tallness (T) in pea.", "Recessive trait: one that is expressed only when both copies are recessive, e.g. shortness (tt) in pea."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [SD], SHINE, "Why is the chance of having a boy or a girl equal in humans?", "easy",
    answer_steps=["The mother always gives an X; the father gives either X or Y.", "Half the sperms carry X and half carry Y, so each fertilisation has a 50% chance of XX (girl) and 50% of XY (boy)."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [ME], SHINE, "With the help of a checkerboard, show the F2 generation of a cross between pure tall (TT) and pure short (tt) pea plants. Write the phenotype and genotype ratios.",
    answer_steps=["F1: TT × tt gives all Tt (tall). F1 selfed: Tt × Tt; gametes T and t from each parent.", "Checkerboard: TT, Tt, Tt, tt.", "Phenotype ratio 3 tall : 1 short; genotype ratio TT : Tt : tt = 1 : 2 : 1."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [ME], SHINE, "How do genes control traits? Explain with the example of plant height.",
    answer_steps=["A gene is a section of DNA that provides information for one protein, often an enzyme.", "Plant height depends on a growth hormone, whose amount depends on the efficiency of the enzyme that makes it.",
                  "If the gene works well, more hormone is made and the plant is tall; if an alteration makes the enzyme less efficient, less hormone is made and the plant is short."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [ME], SHINE, "Describe Mendel's dihybrid cross between a pea plant with round yellow seeds (RRYY) and one with wrinkled green seeds (rryy). Give the F1 and F2 results. What do they show?", "hard",
    answer_steps=["F1: all RrYy, with round yellow seeds; round and yellow are dominant.", "F1 gametes: RY, Ry, rY, ry.",
                  "F2 (16 combinations): 9 round yellow, 3 round green, 3 wrinkled yellow, 1 wrinkled green.", "Round green and wrinkled yellow are new combinations not present in the parents.",
                  "So seed shape and seed colour are inherited independently of each other."],
    marking_scheme=["1 mark: F1", "1 mark: gametes", "1 mark: F2", "1 mark: new combinations", "1 mark: conclusion"])
C.q("la2", "long_answer", 5, [SD], SHINE, "Explain sex determination in humans with a flow chart. Name two other ways in which sex is decided in other animals.", "medium",
    answer_steps=["Humans have 23 pairs of chromosomes; one pair is the sex chromosomes: XX in women, XY in men.", "Eggs all carry X; sperms carry X or Y in equal numbers.",
                  "X-sperm + X-egg gives XX (girl); Y-sperm + X-egg gives XY (boy). So the sex is decided by the father's sperm, with an equal chance each time.",
                  "In some reptiles, the temperature at which the eggs are kept decides the sex.", "Some animals, such as snails, can change sex."],
    marking_scheme=["1 mark: chromosomes", "1 mark: gametes", "1 mark: cross", "1 mark: reptiles", "1 mark: snails"])
C.q("cb1", "case_based", 4, [ME], SHINE,
    "Anu crossed a pure-breeding pea plant with violet flowers (VV) with one with white flowers (vv). All the F1 plants had violet flowers. She then self-pollinated the F1 plants and got 400 F2 plants.\n\n"
    "(i) Which flower colour is dominant? (1)\n\n(ii) What is the genotype of the F1 plants? (1)\n\n(iii) About how many F2 plants will have white flowers? Show your working. OR What are the genotypes of the F2 plants and their ratio? (2)",
    answer_steps=["(i) Violet.", "(ii) Vv.", "(iii) Vv × Vv gives 3 violet : 1 white, so white = 400 × 1/4 = 100 plants. OR VV : Vv : vv = 1 : 2 : 1."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [SD], SHINE,
    "A family has three daughters. Some relatives blamed the mother for not having a son. A biology teacher explained that this is wrong, and that each child has an equal chance of being a boy or a girl.\n\n"
    "(i) Which sex chromosomes does the mother have? (1)\n\n(ii) Which parent's gamete decides the sex of the child? (1)\n\n(iii) Show with a cross why the chance of a boy is 50%. OR Why is it wrong to blame the mother? (2)",
    answer_steps=["(i) XX.", "(ii) The father's sperm.",
                  "(iii) XX × XY: eggs X, X; sperms X, Y; children XX, XX, XY, XY, so half are boys. OR All the mother's eggs carry X; whether the child is a boy depends on the father's sperm carrying Y, and that is a matter of chance."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch08.q.ex."))
