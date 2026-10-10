"""CBSE Class 10 Maths Ch 14: Probability.
Every probability is checked by listing the whole sample space and counting."""
import json, os, sys, math
from collections import Counter
from fractions import Fraction as Fr
from itertools import product

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch14"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch14_probability"

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def P(space, event): return Fr(sum(1 for s in space if event(s)), len(space))

DIE = range(1, 7); TWO_DICE = list(product(DIE, DIE)); COINS3 = ["".join(t) for t in product("HT", repeat=3)]
SUITS = {"spades": "black", "clubs": "black", "hearts": "red", "diamonds": "red"}
DECK = [(r, s) for s in SUITS for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
FACE = {"J", "Q", "K"}
def is_prime(n): return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))

# ---------------------------------------------------------------- verification
check(1 - Fr(5, 100) == Fr(95, 100), "14.1 Q5"); check(1 - Fr(992, 1000) == Fr(8, 1000), "14.1 Q7")
check((Fr(3, 8), Fr(5, 8)) == (Fr(3, 3 + 5), 1 - Fr(3, 8)), "14.1 Q8")
check((Fr(5, 17), Fr(8, 17), Fr(13, 17)) == (Fr(5, 17), Fr(8, 17), 1 - Fr(4, 17)), "14.1 Q9")
check(Fr(100, 180) == Fr(5, 9) and Fr(170, 180) == Fr(17, 18), "14.1 Q10"); check(Fr(5, 13) == Fr(5, 5 + 8), "14.1 Q11")
SPIN = range(1, 9)
check((P(SPIN, lambda n: n == 8), P(SPIN, lambda n: n % 2), P(SPIN, lambda n: n > 2), P(SPIN, lambda n: n < 9)) == (Fr(1, 8), Fr(1, 2), Fr(3, 4), 1), "14.1 Q12")
check((P(DIE, is_prime), P(DIE, lambda n: 2 < n < 6), P(DIE, lambda n: n % 2)) == (Fr(1, 2), Fr(1, 2), Fr(1, 2)), "14.1 Q13")
check((P(DECK, lambda c: c[0] == "K" and SUITS[c[1]] == "red"), P(DECK, lambda c: c[0] in FACE), P(DECK, lambda c: c[0] in FACE and SUITS[c[1]] == "red"),
       P(DECK, lambda c: c == ("J", "hearts")), P(DECK, lambda c: c[1] == "spades"), P(DECK, lambda c: c == ("Q", "diamonds"))) ==
      (Fr(1, 26), Fr(3, 13), Fr(3, 26), Fr(1, 52), Fr(1, 4), Fr(1, 52)), "14.1 Q14")
check((Fr(1, 5), Fr(1, 4), 0) == (Fr(1, 5), Fr(1, 4), Fr(0)), "14.1 Q15"); check(Fr(132, 144) == Fr(11, 12), "14.1 Q16")
check(Fr(4, 20) == Fr(1, 5) and Fr(15, 19) == Fr(16 - 1, 19), "14.1 Q17")
DISCS = range(1, 91)
check((P(DISCS, lambda n: n >= 10), P(DISCS, lambda n: math.isqrt(n) ** 2 == n), P(DISCS, lambda n: n % 5 == 0)) == (Fr(9, 10), Fr(1, 10), Fr(1, 5)), "14.1 Q18")
FACES19 = "ABCDEA"; check((P(FACES19, lambda c: c == "A"), P(FACES19, lambda c: c == "D")) == (Fr(1, 3), Fr(1, 6)), "14.1 Q19")
check(Fr(124, 144) == Fr(31, 36) and Fr(20, 144) == Fr(5, 36), "14.1 Q21")
SUMS = {s: P(TWO_DICE, lambda t, s=s: sum(t) == s) for s in range(2, 13)}
check([SUMS[s] * 36 for s in range(2, 13)] == [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], "14.1 Q22")
check(P(COINS3, lambda s: len(set(s)) > 1) == Fr(3, 4), "14.1 Q23")
check(P(TWO_DICE, lambda t: 5 not in t) == Fr(25, 36) and P(TWO_DICE, lambda t: 5 in t) == Fr(11, 36), "14.1 Q24")
check(P(list(product("HT", repeat=2)), lambda t: t[0] != t[1]) == Fr(1, 2), "14.1 Q25 (one of each is 1/2, not 1/3)")
check(P(TWO_DICE, lambda t: sum(t) != 8) == Fr(31, 36), "sqp8")
MATHS = "mathematics"; pv = P(MATHS, lambda c: c in "aeiou")
check(pv == Fr(4, 11) and Fr(2) / pv == 2 * Fr(9, 4) + 1, "sqp15: 2/(2x + 1) = 4/11 gives x = 9/4")
vidhi = [s for s in COINS3 if "HH" in s]; unnati = [s for s in COINS3 if "HT" in s]
check(sorted(vidhi) == ["HHH", "HHT", "THH"] and sorted(unnati) == ["HHT", "HTH", "HTT", "THT"], "sqp30")
check(P(TWO_DICE, lambda t: is_prime(sum(t))) == Fr(5, 12), "mastery")
check(P(DIE, is_prime) == Fr(1, 2) and P(DECK, lambda c: c[0] in FACE) == Fr(3, 13), "lesson examples")
check(P(list(product("HT", repeat=2)), lambda t: "H" in t) == Fr(3, 4) and P(DECK, lambda c: c[0] == "A") == Fr(1, 13), "mcq04, mcq05")
check(P("PROBABILITY", lambda c: c == "B") == Fr(2, 11) and P(TWO_DICE, lambda t: t[0] == t[1]) == Fr(1, 6) and P(range(1, 21), lambda n: n % 4 == 0) == Fr(1, 4), "mcq06-08")
check(P(TWO_DICE, lambda t: sum(t) == 13) == 0 and Fr(6, 10) == Fr(3, 5), "mcq09, mcq10")
check(P(DECK, lambda c: c[0] in FACE and SUITS[c[1]] == "red") == Fr(3, 26), "ar5")
check(Fr(2, 7) == Fr(sum(1 for extra in [("Sun", "Mon"), ("Mon", "Tue"), ("Tue", "Wed"), ("Wed", "Thu"), ("Thu", "Fri"), ("Fri", "Sat"), ("Sat", "Sun")] if "Sun" in extra), 7), "vsa2")
check((P(TWO_DICE, lambda t: sum(t) == 7), P(TWO_DICE, lambda t: sum(t) >= 10)) == (Fr(1, 6), Fr(1, 6)), "sa1")
N30 = range(1, 31); check((P(N30, is_prime), P(N30, lambda n: n % 3 == 0 or n % 5 == 0)) == (Fr(1, 3), Fr(7, 15)), "sa2")
x = next(x for x in range(1, 12) if Fr(x + 6, 18) == 2 * Fr(x, 12)); check(x == 3, "sa3")
REST = [c for c in DECK if not (c[0] in FACE and SUITS[c[1]] == "black")]
check(len(REST) == 46 and (P(REST, lambda c: SUITS[c[1]] == "red"), P(REST, lambda c: c[0] in FACE), P(REST, lambda c: c[0] == "Q"),
       P(REST, lambda c: c[0] == "K" and SUITS[c[1]] == "black"), P(REST, lambda c: c[1] == "spades")) == (Fr(13, 23), Fr(3, 23), Fr(1, 23), 0, Fr(5, 23)), "la1")
check((P(TWO_DICE, lambda t: t[0] * t[1] % 2 == 0), P(TWO_DICE, lambda t: sum(t) % 3 == 0), P(TWO_DICE, lambda t: is_prime(sum(t))), P(TWO_DICE, lambda t: t[0] == t[1]),
       P(TWO_DICE, lambda t: abs(t[0] - t[1]) == 2)) == (Fr(3, 4), Fr(1, 3), Fr(5, 12), Fr(1, 6), Fr(2, 9)), "la2")
C20 = range(1, 21)
check((P(C20, lambda n: n % 2 == 0), P(C20, is_prime), P(C20, lambda n: n % 3 == 0 or n % 4 == 0), P(C20, lambda n: math.isqrt(n) ** 2 == n)) == (Fr(1, 2), Fr(2, 5), Fr(1, 2), Fr(1, 5)), "cb1")
check((Fr(4, 40), Fr(26, 40), Fr(22, 40), Fr(18, 40)) == (Fr(1, 10), Fr(13, 20), Fr(11, 20), Fr(9, 20)) and 14 + 10 + 12 + 4 == 40, "cb2")

def frac(f):
    f = Fr(f)
    return str(f.numerator) if f.denominator == 1 else f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"

# ---------------------------------------------------------------- figures and tables
FIG_RECT = {"type": "geometry_figure", "title": "A circle inside a 3 m by 2 m rectangle",
            "points": {"A": [0, 0], "B": [3, 0], "C": [3, 2], "D": [0, 2], "O": [1.5, 1], "P": [2, 1]},
            "segments": [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], {"from": "O", "to": "P", "dashed": True}],
            "circles": [{"centre": "O", "radius": 0.5, "through": ["P"]}], "right_angles": [["A", "B", "C"]],
            "lengths": [{"from": "A", "to": "B", "label": "3 m"}, {"from": "B", "to": "C", "label": "2 m"}]}
DICE_TABLE = ("| | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |\n|---|---|---|---|---|---|---|\n" +
              "\n".join(f"| **${a}$** | " + " | ".join(f"${a + b}$" for b in DIE) + " |" for a in DIE))

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch14.{id_}", "type": type_, **kw}
sections = [
 {"id": "s1", "title": "How likely is it?", "blocks": [
  blk("s1.hook", "hook", title="Heads or tails?",
    body="Before a cricket match, the umpire tosses a coin. Nobody can say which face will land up, yet everybody agrees the toss is **fair**: both teams have the same chance.\n\n"
         "Probability puts a number on such chances: 0 for impossible, 1 for certain, and a fraction in between for everything else."),
  blk("s1.inspiration", "inspiration", title="A hundred years with numbers", person="C. R. Rao", years="1920–2023",
    body="Calyampudi Radhakrishna Rao was born in Karnataka and studied at the Indian Statistical Institute under P. C. Mahalanobis. "
         "At just 25 he published results, now called the **Cramér–Rao bound** and the **Rao–Blackwell theorem**, that tell scientists how accurately anything can be estimated from data.\n\n"
         "His ideas are used in medicine, economics, genetics and signal processing. In 2023, at the age of 102, he received the International Prize in Statistics. "
         "He also received the Padma Vibhushan.",
    quote="All knowledge is, in the final analysis, history; all sciences are, in the abstract, mathematics; and all judgements are, in their rationale, statistics.",
    future="Probability is used in weather forecasts, insurance, medicine trials, games, cricket strategy, quality control and artificial intelligence."),
  blk("s1.socratic", "socratic_question", question="A fair coin is tossed. What is the chance of getting a head?",
    options=["$\\dfrac{1}{2}$", "$1$", "$0$"], correct_index=0, explanation="There are two equally likely outcomes, head and tail, and one of them is a head."),
 ]},
 {"id": "s2", "title": "Theoretical probability", "blocks": [
  blk("s2.reveal", "theory", title="Probability of an event", revision=True,
    body="When all the outcomes of an experiment are **equally likely**, the probability of an event $E$ is\n\n"
         "$$P(E) = \\dfrac{\\text{number of outcomes favourable to } E}{\\text{number of all possible outcomes}}$$\n\n"
         "- $0 \\leq P(E) \\leq 1$\n"
         "- An **impossible event** has probability $0$; a **sure (certain) event** has probability $1$.\n"
         "- The probabilities of all the elementary events (single outcomes) add up to $1$.\n"
         "- $P(\\text{not } E) = 1 - P(E)$, because $E$ and 'not $E$' are **complementary**."),
  blk("s2.eg1", "worked_example", title="A die",
    problem="A die is thrown once. Find the probability of getting a prime number.",
    steps=["Possible outcomes: $1, 2, 3, 4, 5, 6$, all equally likely: 6 outcomes.", "Prime numbers: $2, 3, 5$: 3 favourable outcomes.", "$P(\\text{prime}) = \\dfrac{3}{6}$"],
    answer="$\\dfrac{1}{2}$"),
  blk("s2.cards", "theory", title="A deck of cards", revision=True,
    body="A deck has **52** cards in **4 suits** of 13 cards each: spades ♠ and clubs ♣ are black; hearts ♥ and diamonds ♦ are red. "
         "Each suit has an ace, 2 to 10, and three **face cards**: king, queen and jack. So there are 12 face cards, 4 aces and 26 red cards."),
  blk("s2.eg2", "worked_example", title="A card",
    problem="One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting a face card.",
    steps=["There are 12 face cards among 52 cards.", "$P(\\text{face card}) = \\dfrac{12}{52}$"], answer="$\\dfrac{3}{13}$"),
  blk("s2.check1", "knowledge_check", question="If $P(E) = 0.05$, then $P(\\text{not } E)$ is:", options=["$0.95$", "$0.05$", "$1.05$", "$0.5$"], correct_index=0,
    explanation="$P(\\text{not } E) = 1 - 0.05 = 0.95$."),
  blk("s2.check2", "knowledge_check", question="Which of these cannot be the probability of an event?", options=["$-1.5$", "$\\dfrac{2}{3}$", "$15\\%$", "$0.7$"], correct_index=0,
    explanation="A probability always lies between $0$ and $1$; $-1.5$ is negative."),
 ]},
 {"id": "s3", "title": "Two coins, two dice", "blocks": [
  blk("s3.discovery", "discovery", title="List every outcome",
    body="When two coins are tossed, it is tempting to say there are three results: two heads, two tails, or one of each. But 'one of each' can happen in two ways, HT and TH. "
         "The equally likely outcomes are **HH, HT, TH, TT**. Always list them all before counting."),
  blk("s3.table", "markdown_table", title="Sum of the numbers on two dice", revision=True, body=DICE_TABLE),
  blk("s3.thm", "theory", title="Using the table", revision=True,
    body="Two dice give $6 \\times 6 = 36$ equally likely outcomes. Read the favourable cells from the table: for example, the sum 7 appears 6 times, so $P(\\text{sum } 7) = \\dfrac{6}{36} = \\dfrac{1}{6}$. "
         "Three coins give $2 \\times 2 \\times 2 = 8$ outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT."),
  blk("s3.eg1", "worked_example", title="CBSE sample paper",
    problem="A pair of dice is tossed. Find the probability of not getting the sum eight.",
    steps=["The sum 8 comes from $(2, 6)$, $(3, 5)$, $(4, 4)$, $(5, 3)$, $(6, 2)$: 5 outcomes.", "$P(\\text{sum } 8) = \\dfrac{5}{36}$", "$P(\\text{not sum } 8) = 1 - \\dfrac{5}{36}$"],
    answer="$\\dfrac{31}{36}$"),
  blk("s3.eg2", "worked_example", title="CBSE sample paper: who drives?",
    problem="Vidhi and Unnati each flip a coin exactly three times. Vidhi drives if she gets two heads in a row; Unnati drives if she gets a head immediately followed by a tail. Who has the greater probability of driving?",
    steps=["The 8 outcomes are HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.", "Two heads in a row: HHH, HHT, THH, so $P(\\text{Vidhi}) = \\dfrac{3}{8}$.",
           "A head followed by a tail: HHT, HTH, HTT, THT, so $P(\\text{Unnati}) = \\dfrac{4}{8}$."],
    answer="Unnati, because $\\dfrac{4}{8} > \\dfrac{3}{8}$."),
  blk("s3.check", "knowledge_check", question="Two coins are tossed. The probability of getting at least one head is:", options=["$\\dfrac{3}{4}$", "$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$", "$\\dfrac{2}{3}$"], correct_index=0,
    explanation="HH, HT and TH have at least one head: 3 of the 4 outcomes."),
  blk("s3.memory", "memory_trick", title="Count, don't guess", revision=True,
    body="1. **List** all equally likely outcomes (use a table for two dice).\n2. **Count** the favourable ones.\n3. **Divide**: favourable ÷ total.\n\n"
         "For 'not', 'at least one' or 'neither', it is often quicker to find the opposite and subtract from 1."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Treating outcomes as equally likely when they are not (two heads, two tails, one of each).\n"
         "- Forgetting that an ace is not a face card, and that there are 12 face cards, not 16.\n"
         "- Counting 1 as a prime number.\n"
         "- In questions without replacement, forgetting that the total goes down by one for the second draw.\n"
         "- Writing a probability greater than 1 or less than 0."),
  blk("s3.tip", "teacher_tip", title="Toss it 100 times",
    body="Let pairs of students toss two coins 20 times each and record HH, HT, TH, TT on the board. Adding up the whole class's results, 'one of each' comes close to half of all tosses, not a third. "
         "The experiment convinces students why HT and TH must be counted separately."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why tossing a coin is a fair way to decide which team bats first, but 'a car starts or does not start' does not have equally likely outcomes."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 13, Statistics:** frequencies in a table become probabilities when divided by the total.\n"
         "- **Class 11 and 12:** permutations, combinations and conditional probability.\n"
         "- **Real life:** a 70% chance of rain, insurance premiums, quality checks in factories."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="Two dice are thrown together. Find the probability that the sum is a prime number.\n\n"
         "**Answer:** Prime sums are 2, 3, 5, 7 and 11. From the table they occur $1 + 2 + 4 + 6 + 2 = 15$ times out of 36, so the probability is $\\dfrac{15}{36} = \\dfrac{5}{12}$."),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- $P(E) = \\dfrac{\\text{favourable outcomes}}{\\text{total outcomes}}$, for equally likely outcomes\n"
         "- $0 \\leq P(E) \\leq 1$; impossible event: $0$; sure event: $1$\n"
         "- $P(E) + P(\\text{not } E) = 1$\n"
         "- The probabilities of all elementary events add up to $1$."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Write the total number of outcomes and list the favourable ones before dividing.\n"
         "- Simplify the fraction in the final answer.\n"
         "- For two dice, draw the $6 \\times 6$ table; for three coins, list all 8 outcomes.\n"
         "- Know the deck of cards: 52 cards, 4 suits, 26 red, 26 black, 12 face cards, 4 aces."),
  blk("s4.flash1", "flashcard", front="Probability of an impossible event and of a sure event", back="$0$ and $1$"),
  blk("s4.flash2", "flashcard", front="$P(E) + P(\\text{not } E) =$ ?", back="$1$"),
  blk("s4.flash3", "flashcard", front="Number of outcomes when two dice are thrown", back="$36$"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Probability",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 14,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: classical definition of probability and simple problems on finding the probability of an event.",
  "concepts": ["probability_basics", "single_experiment", "two_stage"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
PB, SE, TS = "probability_basics", "single_experiment", "two_stage"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(n, part=None):
    s = {"kind": "ncert_exercise", "exercise": "14.1", "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch14.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS2 = ["1 mark: total and favourable outcomes", "1 mark: probability"]
MS3 = ["1 mark: total outcomes", "1 mark: favourable outcomes", "1 mark: probabilities"]

FILL = "Fill in the blank: "
mcq("ex14_1.q1.i", [PB], FILL + "Probability of an event E + Probability of the event 'not E' = ____.", ["$1$", "$0$", "$2$", "$\\dfrac{1}{2}$"], 0, "E and 'not E' are complementary, so their probabilities add up to 1.", source=ex(1, "i"))
mcq("ex14_1.q1.ii", [PB], FILL + "The probability of an event that cannot happen is ____. Such an event is called ____.", ["$0$, an impossible event", "$1$, a sure event", "$0$, a sure event", "$1$, an impossible event"], 0,
    "No outcome is favourable, so the probability is 0: an impossible event.", source=ex(1, "ii"))
mcq("ex14_1.q1.iii", [PB], FILL + "The probability of an event that is certain to happen is ____. Such an event is called ____.", ["$1$, a sure or certain event", "$0$, an impossible event", "$1$, an impossible event", "$\\dfrac{1}{2}$, a sure event"], 0,
    "Every outcome is favourable, so the probability is 1: a sure (certain) event.", source=ex(1, "iii"))
mcq("ex14_1.q1.iv", [PB], FILL + "The sum of the probabilities of all the elementary events of an experiment is ____.", ["$1$", "$0$", "the number of outcomes", "$\\dfrac{1}{2}$"], 0,
    "Together the elementary events cover every outcome, so their probabilities add up to 1.", source=ex(1, "iv"))
mcq("ex14_1.q1.v", [PB], FILL + "The probability of an event is greater than or equal to ____ and less than or equal to ____.", ["$0$ and $1$", "$-1$ and $1$", "$0$ and $100$", "$1$ and $2$"], 0,
    "$0 \\leq P(E) \\leq 1$.", source=ex(1, "v"))
q("ex14_1.q2", "short_answer", 3, [PB], ex(2), "Which of the following experiments have equally likely outcomes? Explain.\n\n(i) A driver attempts to start a car. The car starts or does not start.\n\n(ii) A player attempts to shoot a basketball. She/he shoots or misses the shot.\n\n"
  "(iii) A trial is made to answer a true-false question. The answer is right or wrong.\n\n(iv) A baby is born. It is a boy or a girl.", "easy",
  answer_steps=["(i) Not equally likely: a car usually starts; it depends on its condition.", "(ii) Not equally likely: it depends on the player's skill.",
                "(iii) Equally likely: a right or a wrong answer is equally possible when guessed.", "(iv) Equally likely: a boy and a girl are (taken to be) equally likely."],
  marking_scheme=["1 mark: (i) and (ii)", "1 mark: (iii) and (iv)", "1 mark: reasons"])
q("ex14_1.q3", "very_short_answer", 2, [PB], ex(3), "Why is tossing a coin considered to be a fair way of deciding which team should get the ball at the beginning of a football game?", "easy",
  answer_steps=["Head and tail are equally likely outcomes, each with probability $\\dfrac{1}{2}$.", "So neither team has an advantage: the result cannot be predicted or favoured."],
  marking_scheme=["1 mark: equally likely", "1 mark: conclusion"])
mcq("ex14_1.q4", [PB], "Which of the following cannot be the probability of an event?", ["$\\dfrac{2}{3}$", "$-1.5$", "$15\\%$", "$0.7$"], 1, "A probability is never negative: $0 \\leq P(E) \\leq 1$.", source=ex(4))
q("ex14_1.q5", "very_short_answer", 2, [PB], ex(5), "If $P(E) = 0.05$, what is the probability of 'not E'?", "easy", answer_steps=["$P(\\text{not } E) = 1 - P(E) = 1 - 0.05$", "$= 0.95$"], marking_scheme=["1 mark: formula", "1 mark: answer"])
q("ex14_1.q6", "very_short_answer", 2, [PB], ex(6), "A bag contains lemon flavoured candies only. Malini takes out one candy without looking into the bag. What is the probability that she takes out (i) an orange flavoured candy? (ii) a lemon flavoured candy?", "easy",
  answer_steps=["(i) There are no orange candies: an impossible event, probability $0$.", "(ii) Every candy is lemon: a sure event, probability $1$."], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
q("ex14_1.q7", "very_short_answer", 2, [PB], ex(7), "It is given that in a group of 3 students, the probability of 2 students not having the same birthday is 0.992. What is the probability that the 2 students have the same birthday?", "easy",
  answer_steps=["The two events are complementary.", "$P(\\text{same birthday}) = 1 - 0.992 = 0.008$"], marking_scheme=["1 mark: complement", "1 mark: answer"])
q("ex14_1.q8", "very_short_answer", 2, [SE], ex(8), "A bag contains 3 red balls and 5 black balls. A ball is drawn at random from the bag. What is the probability that the ball drawn is (i) red? (ii) not red?", "easy",
  answer_steps=["(i) $P(\\text{red}) = \\dfrac{3}{8}$", "(ii) $P(\\text{not red}) = 1 - \\dfrac{3}{8} = \\dfrac{5}{8}$"], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
q("ex14_1.q9", "short_answer", 3, [SE], ex(9), "A box contains 5 red marbles, 8 white marbles and 4 green marbles. One marble is taken out of the box at random. What is the probability that the marble taken out will be (i) red? (ii) white? (iii) not green?", "easy",
  answer_steps=["Total marbles $= 5 + 8 + 4 = 17$", "(i) $\\dfrac{5}{17}$ (ii) $\\dfrac{8}{17}$", "(iii) $1 - \\dfrac{4}{17} = \\dfrac{13}{17}$"], marking_scheme=MS3)
q("ex14_1.q10", "short_answer", 3, [SE], ex(10), "A piggy bank contains hundred 50p coins, fifty ₹1 coins, twenty ₹2 coins and ten ₹5 coins. If it is equally likely that one of the coins will fall out when the bank is turned upside down, what is the probability that the coin (i) will be a 50 p coin? (ii) will not be a ₹5 coin?",
  answer_steps=["Total coins $= 100 + 50 + 20 + 10 = 180$", "(i) $P(50\\text{ p}) = \\dfrac{100}{180} = \\dfrac{5}{9}$", "(ii) $P(\\text{not ₹ } 5) = \\dfrac{170}{180} = \\dfrac{17}{18}$"], marking_scheme=MS3)
q("ex14_1.q11", "very_short_answer", 2, [SE], ex(11), "Gopi buys a fish from a shop for his aquarium. The shopkeeper takes out one fish at random from a tank containing 5 male fish and 8 female fish. What is the probability that the fish taken out is a male fish?", "easy",
  answer_steps=["Total fish $= 5 + 8 = 13$", "$P(\\text{male}) = \\dfrac{5}{13}$"], marking_scheme=MS2)
q("ex14_1.q12", "short_answer", 3, [SE], ex(12), "A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers 1, 2, 3, 4, 5, 6, 7, 8, and these are equally likely outcomes. What is the probability that it will point at (i) 8? (ii) an odd number? (iii) a number greater than 2? (iv) a number less than 9?", "easy",
  answer_steps=["8 equally likely outcomes.", "(i) $\\dfrac{1}{8}$ (ii) odd numbers 1, 3, 5, 7: $\\dfrac{4}{8} = \\dfrac{1}{2}$", "(iii) 3 to 8: $\\dfrac{6}{8} = \\dfrac{3}{4}$ (iv) all 8 numbers: $\\dfrac{8}{8} = 1$"], marking_scheme=MS3)
q("ex14_1.q13", "short_answer", 3, [SE], ex(13), "A die is thrown once. Find the probability of getting (i) a prime number; (ii) a number lying between 2 and 6; (iii) an odd number.", "easy",
  answer_steps=["(i) Primes 2, 3, 5: $\\dfrac{3}{6} = \\dfrac{1}{2}$", "(ii) 3, 4, 5: $\\dfrac{3}{6} = \\dfrac{1}{2}$", "(iii) 1, 3, 5: $\\dfrac{3}{6} = \\dfrac{1}{2}$"], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
q("ex14_1.q14", "long_answer", 5, [SE], ex(14), "One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting (i) a king of red colour (ii) a face card (iii) a red face card (iv) the jack of hearts (v) a spade (vi) the queen of diamonds", "medium",
  answer_steps=["(i) 2 red kings: $\\dfrac{2}{52} = \\dfrac{1}{26}$", "(ii) 12 face cards: $\\dfrac{12}{52} = \\dfrac{3}{13}$", "(iii) 6 red face cards: $\\dfrac{6}{52} = \\dfrac{3}{26}$",
                "(iv) $\\dfrac{1}{52}$ (v) 13 spades: $\\dfrac{13}{52} = \\dfrac{1}{4}$", "(vi) $\\dfrac{1}{52}$"],
  marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv) and (v)", "1 mark: (vi)"])
q("ex14_1.q15", "short_answer", 3, [SE], ex(15), "Five cards, the ten, jack, queen, king and ace of diamonds, are well-shuffled with their face downwards. One card is then picked up at random. (i) What is the probability that the card is the queen? (ii) If the queen is drawn and put aside, what is the probability that the second card picked up is (a) an ace? (b) a queen?",
  answer_steps=["(i) $\\dfrac{1}{5}$", "(ii) 4 cards are left. (a) $\\dfrac{1}{4}$", "(b) No queen is left: $0$"], marking_scheme=["1 mark: (i)", "1 mark: (a)", "1 mark: (b)"])
q("ex14_1.q16", "very_short_answer", 2, [SE], ex(16), "12 defective pens are accidentally mixed with 132 good ones. It is not possible to just look at a pen and tell whether or not it is defective. One pen is taken out at random from this lot. Determine the probability that the pen taken out is a good one.", "easy",
  answer_steps=["Total pens $= 12 + 132 = 144$", "$P(\\text{good}) = \\dfrac{132}{144} = \\dfrac{11}{12}$"], marking_scheme=MS2)
q("ex14_1.q17", "short_answer", 3, [SE, TS], ex(17), "(i) A lot of 20 bulbs contain 4 defective ones. One bulb is drawn at random from the lot. What is the probability that this bulb is defective?\n\n(ii) Suppose the bulb drawn in (i) is not defective and is not replaced. Now one bulb is drawn at random from the rest. What is the probability that this bulb is not defective?",
  answer_steps=["(i) $P(\\text{defective}) = \\dfrac{4}{20} = \\dfrac{1}{5}$", "(ii) 19 bulbs are left, of which $16 - 1 = 15$ are good.", "$P(\\text{not defective}) = \\dfrac{15}{19}$"], marking_scheme=["1 mark: (i)", "1 mark: bulbs left", "1 mark: (ii)"])
q("ex14_1.q18", "short_answer", 3, [SE], ex(18), "A box contains 90 discs which are numbered from 1 to 90. If one disc is drawn at random from the box, find the probability that it bears (i) a two-digit number (ii) a perfect square number (iii) a number divisible by 5.",
  answer_steps=["(i) 10 to 90: 81 numbers, $\\dfrac{81}{90} = \\dfrac{9}{10}$", "(ii) 1, 4, 9, …, 81: 9 numbers, $\\dfrac{9}{90} = \\dfrac{1}{10}$", "(iii) 5, 10, …, 90: 18 numbers, $\\dfrac{18}{90} = \\dfrac{1}{5}$"],
  marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
q("ex14_1.q19", "very_short_answer", 2, [SE], ex(19), "A child has a die whose six faces show the letters A, B, C, D, E and A. The die is thrown once. What is the probability of getting (i) A? (ii) D?", "easy",
  answer_steps=["(i) A is on 2 of the 6 faces: $\\dfrac{2}{6} = \\dfrac{1}{3}$", "(ii) $\\dfrac{1}{6}$"], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
q("ex14_1.q20", "short_answer", 3, [SE], ex(20), "Suppose you drop a die at random on the rectangular region shown in the figure. What is the probability that it will land inside the circle with diameter 1 m?", "hard",
  answer_steps=["Area of the rectangle $= 3 \\times 2 = 6$ m²", "Area of the circle $= \\pi \\times \\left(\\dfrac{1}{2}\\right)^{2} = \\dfrac{\\pi}{4}$ m²", "$P = \\dfrac{\\pi / 4}{6} = \\dfrac{\\pi}{24}$"],
  marking_scheme=["1 mark: rectangle", "1 mark: circle", "1 mark: probability"], figure=dict(FIG_RECT))
q("ex14_1.q21", "very_short_answer", 2, [SE], ex(21), "A lot consists of 144 ball pens of which 20 are defective and the others are good. Nuri will buy a pen if it is good, but will not buy if it is defective. The shopkeeper draws one pen at random and gives it to her. What is the probability that (i) she will buy it? (ii) she will not buy it?", "easy",
  answer_steps=["(i) Good pens $= 124$: $\\dfrac{124}{144} = \\dfrac{31}{36}$", "(ii) $\\dfrac{20}{144} = \\dfrac{5}{36}$"], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
sum_row = " & ".join(str(s) for s in range(2, 13)); prob_row = " & ".join(frac(SUMS[s]) for s in range(2, 13))
q("ex14_1.q22", "long_answer", 5, [TS], ex(22), "Two dice, one blue and one grey, are thrown at the same time. (i) Complete the table of the probabilities of the sums 2, 3, …, 12.\n\n"
  "(ii) A student argues that 'there are 11 possible outcomes 2, 3, 4, …, 12. Therefore, each of them has a probability $\\dfrac{1}{11}$.' Do you agree with this argument? Justify your answer.", "medium",
  answer_steps=["There are 36 equally likely outcomes. Counting the pairs for each sum:", f"$$\\begin{{array}}{{|c|c|c|c|c|c|c|c|c|c|c|}}\\hline {sum_row} \\\\ \\hline {prob_row} \\\\ \\hline\\end{{array}}$$",
                "The probabilities add up to $\\dfrac{36}{36} = 1$.", "(ii) No. The 11 sums are not equally likely: the sum 7 comes in 6 ways but the sum 2 in only 1 way.", "So $P(\\text{sum } 2) = \\dfrac{1}{36}$, not $\\dfrac{1}{11}$."],
  marking_scheme=["2 marks: table", "1 mark: check", "1 mark: answer (ii)", "1 mark: reason"])
q("ex14_1.q23", "short_answer", 3, [TS], ex(23), "A game consists of tossing a one rupee coin 3 times and noting its outcome each time. Hanif wins if all the tosses give the same result i.e., three heads or three tails, and loses otherwise. Calculate the probability that Hanif will lose the game.",
  answer_steps=["The 8 outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.", "Hanif wins only with HHH or TTT.", "$P(\\text{lose}) = \\dfrac{6}{8} = \\dfrac{3}{4}$"], marking_scheme=MS3)
q("ex14_1.q24", "short_answer", 3, [TS], ex(24), "A die is thrown twice. What is the probability that (i) 5 will not come up either time? (ii) 5 will come up at least once?",
  answer_steps=["Total outcomes $= 6 \\times 6 = 36$", "(i) 5 does not come up: $5 \\times 5 = 25$ outcomes, $\\dfrac{25}{36}$", "(ii) $1 - \\dfrac{25}{36} = \\dfrac{11}{36}$"], marking_scheme=MS3)
q("ex14_1.q25", "short_answer", 3, [TS], ex(25), "Which of the following arguments are correct and which are not correct? Give reasons for your answer.\n\n(i) If two coins are tossed simultaneously there are three possible outcomes: two heads, two tails or one of each. Therefore, for each of these outcomes, the probability is $\\dfrac{1}{3}$.\n\n"
  "(ii) If a die is thrown, there are two possible outcomes: an odd number or an even number. Therefore, the probability of getting an odd number is $\\dfrac{1}{2}$.",
  answer_steps=["(i) Incorrect. The equally likely outcomes are HH, HT, TH, TT; 'one of each' happens in 2 ways, so its probability is $\\dfrac{2}{4} = \\dfrac{1}{2}$.",
                "(ii) Correct. Odd (1, 3, 5) and even (2, 4, 6) each have 3 of the 6 outcomes.", "So $P(\\text{odd}) = \\dfrac{3}{6} = \\dfrac{1}{2}$."],
  marking_scheme=["1 mark: (i) with reason", "1 mark: (ii)", "1 mark: reason"])
# Sample paper
mcq("sqp8", [TS], "A pair of dice is tossed. The probability of not getting the sum eight is", ["$\\dfrac{5}{36}$", "$\\dfrac{31}{36}$", "$\\dfrac{5}{18}$", "$\\dfrac{5}{9}$"], 1,
    "Sum 8 in 5 ways, so $1 - \\dfrac{5}{36} = \\dfrac{31}{36}$.", "medium", source=SQP(8))
mcq("sqp15", [SE], "If the probability of a letter chosen at random from the letters of the word 'MATHEMATICS' to be a vowel is $\\dfrac{2}{2x + 1}$, then $x$ is equal to",
    ["$\\dfrac{4}{11}$", "$\\dfrac{9}{4}$", "$\\dfrac{11}{4}$", "$\\dfrac{4}{9}$"], 1, "Vowels A, E, A, I: $P = \\dfrac{4}{11}$. So $\\dfrac{2}{2x + 1} = \\dfrac{4}{11}$, $2x + 1 = \\dfrac{11}{2}$ and $x = \\dfrac{9}{4}$.", "hard", source=SQP(15))
q("sqp30", "short_answer", 3, [TS], SQP(30), "On a particular day, Vidhi and Unnati couldn't decide on who would get to drive the car. They had one coin each and flipped their coin exactly three times. The following was agreed upon:\n\n"
  "1. If Vidhi gets two heads in a row, she would drive the car.\n\n2. If Unnati gets a head immediately followed by a tail, she would drive the car.\n\nWho has greater probability to drive the car that day? Justify your answer.", "hard",
  answer_steps=["Each has 8 outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.", "Vidhi: HHH, HHT, THH, so $P = \\dfrac{3}{8}$. Unnati: HHT, HTH, HTT, THT, so $P = \\dfrac{4}{8}$.", "Unnati has the greater probability."],
  marking_scheme=["1 mark: Vidhi", "1 mark: Unnati", "1 mark: conclusion"])
# Shine MCQs
mcq("mcq01", [PB], "The probability of a sure event is:", ["$1$", "$0$", "$\\dfrac{1}{2}$", "$-1$"], 0, "Every outcome is favourable, so the probability is 1.")
mcq("mcq02", [PB], "If $P(E) = 0.3$, then $P(\\text{not } E)$ is:", ["$0.7$", "$0.3$", "$1.3$", "$0.03$"], 0, "$1 - 0.3 = 0.7$.")
mcq("mcq03", [SE], "The probability of getting a number greater than 6 when a die is thrown is:", ["$0$", "$1$", "$\\dfrac{1}{6}$", "$\\dfrac{5}{6}$"], 0, "No face shows a number greater than 6: an impossible event.")
mcq("mcq04", [TS], "Two coins are tossed together. The probability of getting at least one head is:", ["$\\dfrac{3}{4}$", "$\\dfrac{1}{2}$", "$\\dfrac{1}{4}$", "$1$"], 0, "HH, HT, TH: 3 of 4 outcomes.", "medium")
mcq("mcq05", [SE], "A card is drawn from a well-shuffled deck of 52 cards. The probability of getting an ace is:", ["$\\dfrac{1}{13}$", "$\\dfrac{1}{52}$", "$\\dfrac{1}{4}$", "$\\dfrac{4}{13}$"], 0, "4 aces in 52 cards: $\\dfrac{4}{52} = \\dfrac{1}{13}$.")
mcq("mcq06", [SE], "A letter is chosen at random from the word 'PROBABILITY'. The probability that it is B is:", ["$\\dfrac{2}{11}$", "$\\dfrac{1}{11}$", "$\\dfrac{1}{10}$", "$\\dfrac{2}{9}$"], 0, "B appears 2 times among 11 letters.", "medium")
mcq("mcq07", [TS], "Two dice are thrown. The probability of getting the same number on both dice is:", ["$\\dfrac{1}{6}$", "$\\dfrac{1}{36}$", "$\\dfrac{1}{12}$", "$\\dfrac{1}{3}$"], 0, "6 doublets out of 36: $\\dfrac{6}{36} = \\dfrac{1}{6}$.", "medium")
mcq("mcq08", [SE], "A number is chosen at random from 1 to 20. The probability that it is a multiple of 4 is:", ["$\\dfrac{1}{4}$", "$\\dfrac{1}{5}$", "$\\dfrac{4}{20}$", "$\\dfrac{1}{2}$"], 0, "4, 8, 12, 16, 20: $\\dfrac{5}{20} = \\dfrac{1}{4}$.")
mcq("mcq09", [TS], "Two dice are thrown. The probability that the sum is 13 is:", ["$0$", "$\\dfrac{1}{36}$", "$\\dfrac{1}{13}$", "$1$"], 0, "The largest possible sum is 12, so a sum of 13 is impossible.")
mcq("mcq10", [SE], "A bag has 4 red and 6 blue balls. A ball is drawn at random. The probability that it is blue is:", ["$\\dfrac{3}{5}$", "$\\dfrac{2}{5}$", "$\\dfrac{1}{6}$", "$\\dfrac{3}{2}$"], 0, "$\\dfrac{6}{10} = \\dfrac{3}{5}$.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [PB], "The probability of getting a number less than 7 on a die is 1.", "An event that is certain to happen has probability 1.", 0, "Every face is less than 7, so the event is sure: R explains A.")
ar("ar2", [PB], "The probability of getting a head when a coin is tossed is $\\dfrac{1}{2}$.", "The sum of the probabilities of all the elementary events of an experiment is 1.", 1,
   "Both are true, but A follows from the two equally likely outcomes, not from R.")
ar("ar3", [TS], "When two coins are tossed, the probability of getting one head and one tail is $\\dfrac{1}{3}$.", "The outcomes HH, HT, TH and TT are equally likely.", 3,
   "A is false: HT and TH give $\\dfrac{2}{4} = \\dfrac{1}{2}$. R is true.")
ar("ar4", [PB], "$P(E) + P(\\text{not } E) = 1$.", "$P(E)$ is always greater than $P(\\text{not } E)$.", 2, "A is true. R is false: for example, $P(E) = 0.2$ and $P(\\text{not } E) = 0.8$.")
ar("ar5", [SE], "The probability of drawing a red face card from a deck of 52 cards is $\\dfrac{3}{26}$.", "There are 6 red face cards in a deck of 52 cards.", 0, "R gives $\\dfrac{6}{52} = \\dfrac{3}{26}$.")

q("vsa1", "very_short_answer", 2, [SE], SHINE, "A bag contains 5 red and 3 green balls. A ball is drawn at random. Find the probability that it is not green.", "easy",
  answer_steps=["Total $= 8$; balls that are not green $= 5$.", "$P(\\text{not green}) = \\dfrac{5}{8}$"], marking_scheme=MS2)
q("vsa2", "very_short_answer", 2, [SE], SHINE, "Find the probability that a leap year, selected at random, has 53 Sundays.", "medium",
  answer_steps=["A leap year has 366 days $= 52$ weeks and 2 extra days. The 2 extra days can be (Sun, Mon), (Mon, Tue), …, (Sat, Sun): 7 ways.",
                "Two of these contain a Sunday, so $P = \\dfrac{2}{7}$."], marking_scheme=MS2)
q("sa1", "short_answer", 3, [TS], SHINE, "Two dice are thrown at the same time. Find the probability that (i) the sum is 7; (ii) the sum is at least 10.",
  answer_steps=["Total outcomes $= 36$", "(i) $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$: $\\dfrac{6}{36} = \\dfrac{1}{6}$", "(ii) Sums 10, 11, 12 occur $3 + 2 + 1 = 6$ times: $\\dfrac{6}{36} = \\dfrac{1}{6}$"], marking_scheme=MS3)
q("sa2", "short_answer", 3, [SE], SHINE, "A number is chosen at random from the numbers 1 to 30. Find the probability that it is (i) a prime number; (ii) a multiple of 3 or 5.",
  answer_steps=["(i) Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29: $\\dfrac{10}{30} = \\dfrac{1}{3}$", "(ii) Multiples of 3: 10; of 5: 6; of both (15, 30): 2. So $10 + 6 - 2 = 14$ numbers.",
                "$P = \\dfrac{14}{30} = \\dfrac{7}{15}$"], marking_scheme=MS3)
q("sa3", "short_answer", 3, [SE], SHINE, "A bag contains 12 balls, of which $x$ are black. If one ball is drawn at random, the probability that it is black is $p$. If 6 more black balls are put in the bag, the probability of drawing a black ball becomes $2p$. Find $x$.", "hard",
  answer_steps=["$p = \\dfrac{x}{12}$; after adding, $\\dfrac{x + 6}{18} = 2 \\times \\dfrac{x}{12}$", "$12(x + 6) = 36x$, so $24x = 72$", "$x = 3$"], marking_scheme=["1 mark: first probability", "1 mark: equation", "1 mark: $x$"])
q("la1", "long_answer", 5, [SE], SHINE, "All the black face cards are removed from a deck of 52 cards. The remaining cards are well shuffled and one card is drawn at random. Find the probability of getting (i) a red card (ii) a face card (iii) a queen (iv) a black king (v) a spade.", "medium",
  answer_steps=["6 black face cards are removed, leaving 46 cards.", "(i) 26 red cards: $\\dfrac{26}{46} = \\dfrac{13}{23}$; (ii) 6 red face cards: $\\dfrac{6}{46} = \\dfrac{3}{23}$", "(iii) 2 red queens: $\\dfrac{2}{46} = \\dfrac{1}{23}$",
                "(iv) No black king is left: $0$", "(v) $13 - 3 = 10$ spades: $\\dfrac{10}{46} = \\dfrac{5}{23}$"],
  marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)", "1 mark: (v)"])
q("la2", "long_answer", 5, [TS], SHINE, "Two dice are thrown together. Find the probability that (i) the product of the numbers is even; (ii) the sum is a multiple of 3; (iii) the sum is a prime number; (iv) both show the same number; (v) the difference of the numbers is 2.", "hard",
  answer_steps=["(i) The product is odd only when both are odd: $3 \\times 3 = 9$ ways, so $P(\\text{even}) = 1 - \\dfrac{9}{36} = \\dfrac{3}{4}$",
                "(ii) Sums 3, 6, 9, 12: $2 + 5 + 4 + 1 = 12$ ways, $\\dfrac{12}{36} = \\dfrac{1}{3}$", "(iii) Sums 2, 3, 5, 7, 11: $1 + 2 + 4 + 6 + 2 = 15$ ways, $\\dfrac{15}{36} = \\dfrac{5}{12}$",
                "(iv) 6 doublets: $\\dfrac{6}{36} = \\dfrac{1}{6}$", "(v) $(1, 3), (2, 4), (3, 5), (4, 6)$ and the reverse pairs: 8 ways, $\\dfrac{8}{36} = \\dfrac{2}{9}$"],
  marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)", "1 mark: (v)"])
q("cb1", "case_based", 4, [SE], SHINE,
  "At a school fair, a box contains 20 cards numbered 1 to 20. A player draws one card at random.\n\n(i) Find the probability that the number is even. (1)\n\n(ii) Find the probability that the number is prime. (1)\n\n(iii) Find the probability that the number is a multiple of 3 or 4. OR Find the probability that the number is a perfect square. (2)",
  answer_steps=["(i) 10 even numbers: $\\dfrac{10}{20} = \\dfrac{1}{2}$", "(ii) 2, 3, 5, 7, 11, 13, 17, 19: $\\dfrac{8}{20} = \\dfrac{2}{5}$",
                "(iii) Multiples of 3: 6; of 4: 5; of both (12): 1, so 10 numbers: $\\dfrac{10}{20} = \\dfrac{1}{2}$. OR 1, 4, 9, 16: $\\dfrac{4}{20} = \\dfrac{1}{5}$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [SE], SHINE,
  "In a blood donation camp, the blood groups of 40 students were recorded: O: 14, A: 10, B: 12, AB: 4. One student is chosen at random.\n\n(i) Find the probability that the student has blood group AB. (1)\n\n(ii) Find the probability that the student does not have blood group O. (1)\n\n(iii) Find the probability that the student has blood group A or B. OR Find the probability that the blood group is neither A nor B. (2)",
  answer_steps=["(i) $\\dfrac{4}{40} = \\dfrac{1}{10}$", "(ii) $\\dfrac{40 - 14}{40} = \\dfrac{26}{40} = \\dfrac{13}{20}$", "(iii) $\\dfrac{10 + 12}{40} = \\dfrac{22}{40} = \\dfrac{11}{20}$. OR $\\dfrac{14 + 4}{40} = \\dfrac{18}{40} = \\dfrac{9}{20}$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch14.q.sqp") or (item.get("source", {}).get("kind") == "ncert_exercise" and not item["id"].startswith("ch14.q.ex14_1.q1.")):
        return
    shift = sum(map(ord, item["id"])) % len(opts)
    correct = opts[item["correct_index"]]
    item["options"] = opts[shift:] + opts[:shift]
    item["correct_index"] = item["options"].index(correct)
for it in Q: spread(it)
for sec_ in sections:
    for bl in sec_["blocks"]: spread(bl)
print("answer positions:", Counter(it["correct_index"] for it in Q if it["type"] == "mcq"))
os.makedirs(os.path.join(ROOT, PATH), exist_ok=True)
for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": CH_ID, "questions": Q})]:
    with open(os.path.join(ROOT, PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
print(f"blocks={sum(len(s['blocks']) for s in sections)} questions={len(Q)} ncert_exercise_items={sum(1 for it in Q if it['source']['kind'] == 'ncert_exercise')}")
