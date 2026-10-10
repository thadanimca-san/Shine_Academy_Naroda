"""CBSE Class 10 Maths Ch 10: Circles.
Numerical answers are checked with sympy; figure coordinates are computed so
tangents are exactly perpendicular to radii and marked points lie on circles."""
import json, math, os, sys
from collections import Counter
from sympy import sqrt, Rational as R, symbols, solve, Eq, simplify

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch10"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch10_circles"
x = symbols("x", positive=True)

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

# ---------------------------------------------------------------- verification
check(sqrt(12 ** 2 - 5 ** 2) == sqrt(119), "10.1 Q3"); check(sqrt(25 ** 2 - 24 ** 2) == 7, "10.2 Q1")
check(180 - 110 == 70 and (180 - 80) / 2 == 50, "10.2 Q2, Q3"); check(sqrt(5 ** 2 - 4 ** 2) == 3, "10.2 Q6")
check(2 * sqrt(5 ** 2 - 3 ** 2) == 8, "10.2 Q7")
s12 = solve(Eq(48 * x * (14 + x), 16 * (14 + x) ** 2), x); check(s12 == [7] and (8 + 7, 6 + 7) == (15, 13), "10.2 Q12")
check(sqrt(41 ** 2 - 9 ** 2) == 40, "sqp18"); check(7 + 3 - 4 == 6, "sqp4 AB = 6")
check(solve(Eq(R(1, 2) * 4 * (2 * x + 36), 90), x) == [R(9, 2)] and (R(9, 2) + 10, R(9, 2) + 8) == (R(29, 2), R(25, 2)), "sqp25")
check(sqrt(13 ** 2 - 5 ** 2) == 12 and 180 - 60 == 120 and 2 * sqrt(10 ** 2 - 6 ** 2) == 16 and 6 + 4 - 7 == 3, "mcqs")
check(sqrt(5 ** 2 - 3 ** 2) == 4 and 180 - 70 == 110, "ar1, ar4")
check(sqrt(17 ** 2 - 8 ** 2) == 15 and 90 - (180 - 50) / 2 == 25, "vsa1, vsa2")
check(sqrt(24 ** 2 + 7 ** 2) == 25 and (24 + 7 - 25) / 2 == 3, "sa3 r = 3")
check(8 + 12 - 10 == 10, "la1 AD = 10")
la2 = solve(Eq(3 * (15 + x), 54), x); check(la2 == [3] and (6 + 3, 9 + 3) == (9, 12) and 9 ** 2 + 12 ** 2 == 15 ** 2, "la2")
check(sqrt(13 ** 2 - 5 ** 2) == 12 and 2 * R(1, 2) * 5 * 12 == 60 and 5 + 5 + 12 + 12 == 34, "cb1")
check(solve(Eq(4 * (14 + x), sqrt((14 + x) * x * 6 * 8)), x) == [7] and 2 * (14 + 7) == 42, "cb2")

# ---------------------------------------------------------------- figures
def r9(p): return [round(p[0], 9), round(p[1], 9)]
def on(r, deg_): return (r * math.cos(math.radians(deg_)), r * math.sin(math.radians(deg_)))
def tangent_meet(r, a1, a2):
    """Intersection of the tangents at angles a1 and a2 (degrees) of a circle of radius r at the origin."""
    c1, s1, c2, s2 = math.cos(math.radians(a1)), math.sin(math.radians(a1)), math.cos(math.radians(a2)), math.sin(math.radians(a2))
    det = c1 * s2 - c2 * s1
    return ((r * s2 - r * s1) / det, (c1 * r - c2 * r) / det)
def fig(title, points, segments, **kw):
    f = {"type": "geometry_figure", "title": title, "points": {k: r9(v) for k, v in points.items()}, "segments": segments}
    f.update(kw); return f

C1, D1 = on(3, 200), on(3, -20)
FIG_LINES = fig("A tangent and a secant", {"O": (0, 0), "P": (0, 3), "A": (-4, 3), "B": (4, 3), "C": C1, "D": D1, "E": (-4.5, C1[1]), "F": (4.5, C1[1])},
                [{"from": "A", "to": "B", "highlight": True}, ["E", "F"], {"from": "O", "to": "P", "dashed": True}],
                circles=[{"centre": "O", "radius": 3, "through": ["P", "C", "D"]}], right_angles=[["O", "P", "B"]], parallel=[["A", "B", "E", "F"]])
A2, B2 = on(3, 60), on(3, -60)
FIG_TWO = fig("Two tangents from P", {"O": (0, 0), "P": (6, 0), "A": A2, "B": B2},
              [{"from": "P", "to": "A", "highlight": True}, {"from": "P", "to": "B", "highlight": True}, ["O", "A"], ["O", "B"], {"from": "O", "to": "P", "dashed": True}],
              circles=[{"centre": "O", "radius": 3, "through": ["A", "B"]}], right_angles=[["O", "A", "P"], ["O", "B", "P"]])
angles = [80, 190, 260, 350]
quad = {n: tangent_meet(3, angles[i], angles[(i + 1) % 4]) for i, n in enumerate("ABCD")}
touch = {n: on(3, a) for n, a in zip("PQRS", angles)}
FIG_QUAD = fig("ABCD circumscribes the circle", {"O": (0, 0), **quad, **touch},
               [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]], circles=[{"centre": "O", "radius": 3, "through": list("PQRS")}],
               right_angles=[["O", "P", "A"], ["O", "Q", "B"], ["O", "R", "C"], ["O", "S", "D"]])
Cc = on(3, 30); Aa = ((3 - 3 * math.sin(math.radians(30))) / math.cos(math.radians(30)), 3); Bb = ((3 + 3 * math.sin(math.radians(30))) / math.cos(math.radians(30)), -3)
FIG_PAR = fig("Parallel tangents XY and X′Y′", {"O": (0, 0), "P": (0, 3), "Q": (0, -3), "C": Cc, "A": Aa, "B": Bb, "X": (-4, 3), "Y": (7, 3), "X′": (-4, -3), "Y′": (7, -3)},
              [["X", "Y"], ["X′", "Y′"], {"from": "A", "to": "B", "highlight": True}, {"from": "O", "to": "A", "dashed": True}, {"from": "O", "to": "B", "dashed": True}],
              circles=[{"centre": "O", "radius": 3, "through": ["P", "Q", "C"]}], parallel=[["X", "Y", "X′", "Y′"]], right_angles=[["O", "C", "A"], ["O", "P", "Y"]])
FIG_CONC = fig("Chord AB touches the inner circle at P", {"O": (0, 0), "P": (0, 3), "A": (-4, 3), "B": (4, 3)},
               [{"from": "A", "to": "B", "highlight": True}, ["O", "P"], {"from": "O", "to": "A", "dashed": True}],
               circles=[{"centre": "O", "radius": 5, "through": ["A", "B"]}, {"centre": "O", "radius": 3, "through": ["P"]}], right_angles=[["O", "P", "B"]],
               lengths=[{"from": "O", "to": "A", "label": "5 cm"}, {"from": "O", "to": "P", "label": "3 cm"}])
Ftri, Etri = (4.8, 6.4), (14 - 30 / 13, 72 / 13)
FIG_TRI = fig("The incircle of △ABC", {"A": (9, 12), "B": (0, 0), "C": (14, 0), "O": (8, 4), "D": (8, 0), "E": Etri, "F": Ftri},
              [["A", "B"], ["B", "C"], ["C", "A"], {"from": "O", "to": "D", "dashed": True}], circles=[{"centre": "O", "radius": 4, "through": ["D", "E", "F"]}],
              right_angles=[["O", "D", "C"], ["O", "E", "A"], ["O", "F", "B"]], lengths=[{"from": "B", "to": "D", "label": "8 cm"}, {"from": "D", "to": "C", "label": "6 cm"}])
check(abs(math.dist((8, 4), Etri) - 4) < 1e-9 and abs(math.dist((8, 4), Ftri) - 4) < 1e-9 and abs(math.dist((9, 12), (0, 0)) - 15) < 1e-9 and abs(math.dist((9, 12), (14, 0)) - 13) < 1e-9, "incircle figure")
check(abs(math.dist((6, 0), A2) - math.sqrt(27)) < 1e-9, "two tangents figure")

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch10.{id_}", "type": type_, **kw}
def placed(id_, figure): return {"id": f"ch10.{id_}", **figure}

sections = [
 {"id": "s1", "title": "A line that just touches", "blocks": [
  blk("s1.hook", "hook", title="Where does a wheel touch the road?",
    body="Look at a bicycle wheel standing on a flat road. The wheel touches the road at exactly **one** point, and the spoke to that point stands straight up, at right angles to the road.\n\n"
         "The road is a **tangent** to the wheel. In this chapter you will prove why a tangent is always perpendicular to the radius, and why the two tangents from an outside point are always equal."),
  blk("s1.inspiration", "inspiration", title="Geometry at the altar", person="Baudhayana", years="about 800 BCE",
    body="Long ago in India, fire altars had to be built in exact shapes, some square and some circular, with equal areas. The rules for building them were written in the *Sulba Sutras*.\n\n"
         "The *Baudhayana Sulba Sutra* gives ways to turn a square into a circle of nearly equal area, and it states the rule we now call the **Pythagoras theorem**, centuries before Pythagoras. "
         "You will use that rule again and again in this chapter, because every tangent makes a right angle with a radius.",
    quote="Careful work done for a small task can carry ideas that last thousands of years.",
    future="Tangents and circles appear in the design of gears, wheels and belts, roads and railway curves, lenses, and in computer graphics."),
  blk("s1.socratic", "socratic_question", question="In how many points can a straight line and a circle meet?",
    options=["0, 1 or 2", "Only 2", "Any number"], correct_index=0,
    explanation="A line can miss the circle (0 points), just touch it (1 point: a tangent) or cut it (2 points: a secant). It can never meet a circle in three points."),
 ]},
 {"id": "s2", "title": "Tangent to a circle", "blocks": [
  blk("s2.reveal", "theory", title="Tangents and secants", revision=True,
    body="A line and a circle can be related in three ways:\n\n"
         "- **non-intersecting**: no common point;\n"
         "- **secant**: two common points;\n"
         "- **tangent**: exactly one common point, called the **point of contact**.\n\n"
         "There is only one tangent at a point of a circle, and a circle has infinitely many tangents. A circle can have at most two tangents parallel to a given line."),
  placed("s2.fig", FIG_LINES),
  blk("s2.thm", "theory", title="Theorem 10.1", revision=True,
    body="**The tangent at any point of a circle is perpendicular to the radius through the point of contact.**\n\n"
         "*Proof idea:* Let the tangent $XY$ touch the circle with centre $O$ at $P$. Take any other point $Q$ on $XY$. $Q$ lies outside the circle (a tangent meets the circle only at $P$), so $OQ > OP$. "
         "So $OP$ is the shortest distance from $O$ to the line $XY$, and the shortest segment from a point to a line is perpendicular to it. Hence $OP \\perp XY$."),
  blk("s2.eg1", "worked_example", title="CBSE sample paper",
    problem="Find the length of a tangent drawn to a circle of radius 9 cm from a point at a distance of 41 cm from the centre.",
    steps=["The tangent is perpendicular to the radius, so the triangle $OPT$ is right-angled at $T$.", "$TP^{2} = OP^{2} - OT^{2} = 41^{2} - 9^{2} = 1681 - 81 = 1600$"],
    answer="$TP = 40$ cm"),
  blk("s2.check", "knowledge_check", question="A tangent PQ at a point P of a circle of radius 5 cm meets a line through the centre O at Q so that OQ = 12 cm. The length PQ is:",
    options=["$\\sqrt{119}$ cm", "$12$ cm", "$13$ cm", "$8.5$ cm"], correct_index=0, explanation="$PQ^{2} = OQ^{2} - OP^{2} = 144 - 25 = 119$."),
 ]},
 {"id": "s3", "title": "Tangents from a point outside", "blocks": [
  blk("s3.discovery", "discovery", title="How many tangents?",
    body="From a point **inside** a circle, no tangent can be drawn: every line through it cuts the circle twice. From a point **on** the circle there is exactly one. "
         "From a point **outside** there are exactly two, and when you measure them you always find them equal."),
  placed("s3.fig", FIG_TWO),
  blk("s3.thm", "theory", title="Theorem 10.2", revision=True,
    body="**The lengths of tangents drawn from an external point to a circle are equal.**\n\n"
         "*Proof:* Let $PA$ and $PB$ be tangents from $P$ to the circle with centre $O$. In $\\triangle OAP$ and $\\triangle OBP$: $OA = OB$ (radii), $OP$ is common, and $\\angle OAP = \\angle OBP = 90^\\circ$ (Theorem 10.1). "
         "So $\\triangle OAP \\cong \\triangle OBP$ (RHS), and $PA = PB$ (CPCT).\n\n"
         "The same congruence also gives $\\angle OPA = \\angle OPB$: the centre lies on the bisector of the angle between the tangents. In quadrilateral $OAPB$, $\\angle AOB + \\angle APB = 180^\\circ$."),
  blk("s3.eg1", "worked_example", title="NCERT exercise: angle between tangents",
    problem="TP and TQ are two tangents to a circle with centre O so that $\\angle POQ = 110^\\circ$. Find $\\angle PTQ$.",
    steps=["In quadrilateral $OPTQ$, $\\angle OPT = \\angle OQT = 90^\\circ$.", "$\\angle PTQ = 360^\\circ - 90^\\circ - 90^\\circ - 110^\\circ$"], answer="$\\angle PTQ = 70^\\circ$"),
  blk("s3.eg2", "worked_example", title="NCERT exercise: concentric circles",
    problem="Two concentric circles are of radii 5 cm and 3 cm. Find the length of the chord of the larger circle which touches the smaller circle.",
    steps=["The chord $AB$ touches the smaller circle at $P$, so $OP \\perp AB$ (Theorem 10.1) and $OP = 3$ cm.", "In right $\\triangle OPA$: $AP = \\sqrt{5^{2} - 3^{2}} = 4$ cm.",
           "The perpendicular from the centre bisects the chord, so $AB = 2 \\times 4$."], answer="$AB = 8$ cm"),
  placed("s3.fig2", FIG_CONC),
  blk("s3.eg3", "worked_example", title="NCERT exercise: a circumscribed quadrilateral",
    problem="A quadrilateral ABCD is drawn to circumscribe a circle. Prove that $AB + CD = AD + BC$.",
    steps=["Let the sides touch the circle at $P$ (on $AB$), $Q$ (on $BC$), $R$ (on $CD$) and $S$ (on $DA$).", "Tangents from a point are equal: $AP = AS$, $BP = BQ$, $CR = CQ$, $DR = DS$.",
           "Adding: $(AP + BP) + (CR + DR) = (AS + DS) + (BQ + CQ)$, i.e. $AB + CD = AD + BC$."],
    answer="Proved."),
  placed("s3.fig3", FIG_QUAD),
  blk("s3.check1", "knowledge_check", question="If tangents PA and PB from P to a circle with centre O are inclined to each other at $80^\\circ$, then $\\angle POA$ is:",
    options=["$50^\\circ$", "$40^\\circ$", "$80^\\circ$", "$100^\\circ$"], correct_index=0,
    explanation="$\\angle AOB = 180^\\circ - 80^\\circ = 100^\\circ$, and $OP$ bisects it, so $\\angle POA = 50^\\circ$."),
  blk("s3.check2", "knowledge_check", question="How many tangents can be drawn to a circle from a point inside it?",
    options=["None", "One", "Two", "Infinitely many"], correct_index=0, explanation="Every line through an inside point cuts the circle in two points, so none of them is a tangent."),
  blk("s3.memory", "memory_trick", title="Two facts solve almost everything", revision=True,
    body="1. **Radius ⊥ tangent** at the point of contact: look for a right triangle and use Pythagoras.\n"
         "2. **Tangents from one point are equal**: mark equal lengths with the same letter (like $x$) and add up sides.\n\n"
         "And in the kite $OAPB$: $\\angle AOB + \\angle APB = 180^\\circ$."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Forgetting to write the reason 'radius ⊥ tangent' before using a right angle.\n"
         "- Using the hypotenuse wrongly: the line to the centre $OP$ is the hypotenuse, not the tangent.\n"
         "- Taking $\\angle AOB = \\angle APB$ instead of $\\angle AOB + \\angle APB = 180^\\circ$.\n"
         "- In circumscribed figures, pairing the wrong tangent segments: each vertex has its own two equal tangents.\n"
         "- Calling a line a tangent because it 'looks' like one: it must meet the circle at exactly one point."),
  blk("s3.tip", "teacher_tip", title="Measure, then prove",
    body="Ask each student to draw a circle, mark a point outside it, draw both tangents with a ruler and measure them. Everyone finds them equal. "
         "Then the RHS proof answers the question 'why?'. For circumscribed figures, colour each pair of equal tangents in the same colour on the board."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why no tangent can be drawn to a circle from a point inside it, and why exactly two can be drawn from a point outside it."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 6:** the congruence and similarity ideas you used here come from triangles.\n"
         "- **Chapter 11, Areas Related to Circles:** sectors and segments of circles.\n"
         "- **Engineering:** belts over pulleys and gears touch along tangents; railway curves join straight tracks along tangents."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="A triangle ABC is drawn to circumscribe a circle of radius 4 cm such that the segments BD and DC into which BC is divided by the point of contact D are of lengths 8 cm and 6 cm. Find AB and AC.\n\n"
         "**Answer:** Let the tangents from $A$ be $x$. Then $AB = x + 8$, $AC = x + 6$, $BC = 14$ and $s = 14 + x$. "
         "Area $= rs = 4(14 + x)$ and, by Heron's formula, $\\sqrt{(14 + x) \\cdot x \\cdot 6 \\cdot 8}$. Equating gives $x = 7$, so $AB = 15$ cm and $AC = 13$ cm."),
  placed("s4.fig", FIG_TRI),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- A tangent meets a circle in exactly one point; a secant meets it in two.\n"
         "- The tangent at any point of a circle is perpendicular to the radius through the point of contact.\n"
         "- From a point inside a circle no tangent can be drawn; from a point on it, one; from a point outside, two.\n"
         "- The lengths of the two tangents from an external point are equal."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Learn the proofs of Theorems 10.1 and 10.2: they are asked as 3-mark questions.\n"
         "- Draw the figure, join the centre to the points of contact, and mark the right angles.\n"
         "- In every step write the reason: 'radius ⊥ tangent', 'tangents from an external point are equal', 'CPCT'.\n"
         "- For numerical questions, the right triangle with the line to the centre as hypotenuse is almost always the key."),
  blk("s4.flash1", "flashcard", front="What angle does a tangent make with the radius at the point of contact?", back="$90^\\circ$"),
  blk("s4.flash2", "flashcard", front="What do you know about the two tangents from an external point?", back="They are equal in length, and the line to the centre bisects the angle between them."),
  blk("s4.flash3", "flashcard", front="If ABCD circumscribes a circle, what is true?", back="$AB + CD = AD + BC$"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Circles",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 10,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: tangent to a circle at the point of contact; proofs that the tangent is perpendicular to the radius and that the tangents from an external point are equal.",
  "concepts": ["tangent_basics", "tangent_radius", "equal_tangents"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
TB, TR, ET = "tangent_basics", "tangent_radius", "equal_tangents"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch10.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS3P = ["1 mark: figure with radii to the points of contact", "1 mark: correct reasons (radius ⊥ tangent / equal tangents)", "1 mark: conclusion"]
MS2N = ["1 mark: right triangle with reason", "1 mark: answer"]

# Exercise 10.1
mcq("ex10_1.q1", [TB], "How many tangents can a circle have?", ["infinitely many", "one", "two", "none"], 0, "There is a tangent at every point of the circle, so there are infinitely many.", source=ex("10.1", 1))
mcq("ex10_1.q2.i", [TB], "Fill in the blank: A tangent to a circle intersects it in ____ point(s).", ["one", "two", "no", "infinitely many"], 0, "A tangent has exactly one common point with the circle.", source=ex("10.1", 2, "i"))
mcq("ex10_1.q2.ii", [TB], "Fill in the blank: A line intersecting a circle in two points is called a ____.", ["secant", "tangent", "chord", "radius"], 0, "A line that cuts a circle in two points is a secant.", source=ex("10.1", 2, "ii"))
mcq("ex10_1.q2.iii", [TB], "Fill in the blank: A circle can have ____ parallel tangents at the most.", ["two", "one", "three", "infinitely many"], 0, "Only the two tangents at the ends of one diameter are parallel to each other.", source=ex("10.1", 2, "iii"))
mcq("ex10_1.q2.iv", [TB], "Fill in the blank: The common point of a tangent to a circle and the circle is called ____.", ["point of contact", "centre", "end point", "point of intersection of chords"], 0,
    "It is called the point of contact.", source=ex("10.1", 2, "iv"))
mcq("ex10_1.q3", [TR], "A tangent PQ at a point P of a circle of radius 5 cm meets a line through the centre O at a point Q so that OQ = 12 cm. Length PQ is:", ["$12$ cm", "$13$ cm", "$8.5$ cm", "$\\sqrt{119}$ cm"], 3,
    "$OP \\perp PQ$, so $PQ = \\sqrt{12^{2} - 5^{2}} = \\sqrt{119}$ cm.", "medium", source=ex("10.1", 3))
q("ex10_1.q4", "very_short_answer", 2, [TB], ex("10.1", 4), "Draw a circle and two lines parallel to a given line such that one is a tangent and the other, a secant to the circle.", "easy",
  answer_steps=["Draw the circle and the given line. Draw the diameter perpendicular to the given line; the line through one end of this diameter, parallel to the given line, is a tangent.",
                "A line parallel to the given line passing between the centre and that end of the diameter cuts the circle in two points: it is a secant."],
  marking_scheme=["1 mark: tangent", "1 mark: secant"], figure=dict(FIG_LINES))
# Exercise 10.2
mcq("ex10_2.q1", [TR], "From a point Q, the length of the tangent to a circle is 24 cm and the distance of Q from the centre is 25 cm. The radius of the circle is", ["$7$ cm", "$12$ cm", "$15$ cm", "$24.5$ cm"], 0,
    "$r = \\sqrt{25^{2} - 24^{2}} = 7$ cm.", source=ex("10.2", 1))
mcq("ex10_2.q2", [ET], "TP and TQ are two tangents to a circle with centre O so that $\\angle POQ = 110^\\circ$. Then $\\angle PTQ$ is equal to", ["$60^\\circ$", "$70^\\circ$", "$80^\\circ$", "$90^\\circ$"], 1,
    "$\\angle PTQ = 180^\\circ - 110^\\circ = 70^\\circ$.", "medium", source=ex("10.2", 2))
mcq("ex10_2.q3", [ET], "If tangents PA and PB from a point P to a circle with centre O are inclined to each other at an angle of $80^\\circ$, then $\\angle POA$ is equal to", ["$50^\\circ$", "$60^\\circ$", "$70^\\circ$", "$80^\\circ$"], 0,
    "$\\angle AOB = 100^\\circ$ and $OP$ bisects it: $\\angle POA = 50^\\circ$.", "medium", source=ex("10.2", 3))
PROOFS = [
 ("q4", "Prove that the tangents drawn at the ends of a diameter of a circle are parallel.", "easy",
  ["Let $AB$ be a diameter, with tangents $l$ at $A$ and $m$ at $B$.", "$OA \\perp l$ and $OB \\perp m$ (radius ⊥ tangent), so both tangents are perpendicular to the line $AB$.", "Lines perpendicular to the same line are parallel, so $l \\parallel m$."]),
 ("q5", "Prove that the perpendicular at the point of contact to the tangent to a circle passes through the centre.", "medium",
  ["Let the tangent touch the circle at $P$ and suppose the perpendicular to it at $P$ does not pass through the centre $O$.", "But $OP$ is also perpendicular to the tangent at $P$ (Theorem 10.1).",
   "Only one perpendicular can be drawn to a line at a given point, so the perpendicular is $OP$ and passes through $O$."]),
 ("q8", "A quadrilateral ABCD is drawn to circumscribe a circle. Prove that $AB + CD = AD + BC$.", "medium",
  ["Let the sides $AB$, $BC$, $CD$, $DA$ touch the circle at $P$, $Q$, $R$, $S$.", "Tangents from a point are equal: $AP = AS$, $BP = BQ$, $CR = CQ$, $DR = DS$.", "Adding: $AB + CD = (AP + PB) + (CR + RD) = AS + BQ + CQ + DS = AD + BC$."]),
 ("q9", "XY and X′Y′ are two parallel tangents to a circle with centre O and another tangent AB with point of contact C intersecting XY at A and X′Y′ at B. Prove that $\\angle AOB = 90^\\circ$.", "hard",
  ["Let $XY$ and $X'Y'$ touch the circle at $P$ and $Q$; $PQ$ is a diameter. $\\triangle OPA \\cong \\triangle OCA$ (RHS), so $\\angle POA = \\angle COA$.", "Similarly $\\triangle OQB \\cong \\triangle OCB$, so $\\angle QOB = \\angle COB$.",
   "$\\angle POA + \\angle COA + \\angle COB + \\angle QOB = 180^\\circ$, so $2(\\angle COA + \\angle COB) = 180^\\circ$ and $\\angle AOB = 90^\\circ$."]),
 ("q10", "Prove that the angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line-segment joining the points of contact at the centre.", "medium",
  ["Let $PA$ and $PB$ be the tangents from $P$, touching the circle with centre $O$ at $A$ and $B$.", "$\\angle OAP = \\angle OBP = 90^\\circ$ (radius ⊥ tangent).", "In quadrilateral $OAPB$: $\\angle AOB + \\angle APB = 360^\\circ - 180^\\circ = 180^\\circ$."]),
 ("q11", "Prove that the parallelogram circumscribing a circle is a rhombus.", "medium",
  ["For the circumscribing parallelogram $ABCD$, equal tangents give $AB + CD = AD + BC$.", "In a parallelogram $AB = CD$ and $AD = BC$, so $2AB = 2AD$, i.e. $AB = AD$.", "A parallelogram with two adjacent sides equal is a rhombus."]),
 ("q13", "Prove that opposite sides of a quadrilateral circumscribing a circle subtend supplementary angles at the centre of the circle.", "hard",
  ["Join $O$ to the vertices and to the points of contact. Congruent triangles (RHS) at each vertex give equal pairs of angles at $O$: call them $a, a, b, b, c, c, d, d$.", "Their sum is $360^\\circ$, so $a + b + c + d = 180^\\circ$.",
   "$\\angle AOB + \\angle COD = (a + b) + (c + d) = 180^\\circ$, and similarly $\\angle BOC + \\angle DOA = 180^\\circ$."]),
]
for p, text, diff, steps in PROOFS:
    extra = {"figure": dict(FIG_QUAD)} if p == "q8" else ({"figure": dict(FIG_PAR)} if p == "q9" else {})
    q(f"ex10_2.{p}", "short_answer", 3, [ET, TR], ex("10.2", int(p[1:])), text, diff, answer_steps=steps, marking_scheme=MS3P, **extra)
q("ex10_2.q6", "very_short_answer", 2, [TR], ex("10.2", 6), "The length of a tangent from a point A at distance 5 cm from the centre of the circle is 4 cm. Find the radius of the circle.", "easy",
  answer_steps=["Radius ⊥ tangent, so $r^{2} + 4^{2} = 5^{2}$.", "$r = 3$ cm"], marking_scheme=MS2N)
q("ex10_2.q7", "short_answer", 3, [TR], ex("10.2", 7), "Two concentric circles are of radii 5 cm and 3 cm. Find the length of the chord of the larger circle which touches the smaller circle.",
  answer_steps=["The chord touches the smaller circle at $P$, so $OP \\perp AB$ and $OP = 3$ cm.", "$AP = \\sqrt{5^{2} - 3^{2}} = 4$ cm", "The perpendicular from the centre bisects the chord: $AB = 8$ cm."],
  marking_scheme=["1 mark: $OP \\perp AB$", "1 mark: $AP = 4$ cm", "1 mark: $AB = 8$ cm"], figure=dict(FIG_CONC))
q("ex10_2.q12", "long_answer", 5, [ET], ex("10.2", 12), "A triangle ABC is drawn to circumscribe a circle of radius 4 cm such that the segments BD and DC into which BC is divided by the point of contact D are of lengths 8 cm and 6 cm respectively. Find the sides AB and AC.", "hard",
  answer_steps=["Equal tangents: $BF = BD = 8$, $CE = CD = 6$, and let $AE = AF = x$.", "So $AB = x + 8$, $AC = x + 6$, $BC = 14$ and $s = 14 + x$.", "Area $= \\dfrac{1}{2} \\times 4 \\times (\\text{perimeter}) = 4(14 + x)$.",
                "By Heron's formula, area $= \\sqrt{(14 + x) \\cdot x \\cdot 6 \\cdot 8}$. Squaring: $48x(14 + x) = 16(14 + x)^{2}$, so $3x = 14 + x$ and $x = 7$.", "$AB = 15$ cm and $AC = 13$ cm"],
  marking_scheme=["1 mark: equal tangents", "1 mark: sides in terms of $x$", "1 mark: area as $rs$", "1 mark: equation", "1 mark: answer"], figure=dict(FIG_TRI))
# Theorems
q("thm10_1", "short_answer", 3, [TR], {"kind": "ncert_theorem", "theorem": "10.1"}, "Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.", "medium",
  answer_steps=["Let the tangent $XY$ touch the circle with centre $O$ at $P$. Take any point $Q$ on $XY$ other than $P$, and join $OQ$.", "$Q$ lies outside the circle (the tangent meets the circle only at $P$), so $OQ > OP$.",
                "So $OP$ is the shortest of all the segments from $O$ to points of $XY$, and the shortest such segment is perpendicular to the line: $OP \\perp XY$."], marking_scheme=MS3P)
q("thm10_2", "short_answer", 3, [ET], {"kind": "ncert_theorem", "theorem": "10.2"}, "Prove that the lengths of tangents drawn from an external point to a circle are equal.", "medium",
  answer_steps=["Let $PQ$ and $PR$ be tangents from $P$ to the circle with centre $O$. Join $OP$, $OQ$ and $OR$.", "In $\\triangle OQP$ and $\\triangle ORP$: $OQ = OR$ (radii), $OP$ is common and $\\angle OQP = \\angle ORP = 90^\\circ$ (radius ⊥ tangent).",
                "So $\\triangle OQP \\cong \\triangle ORP$ (RHS), and $PQ = PR$ (CPCT)."], marking_scheme=MS3P, figure=dict(FIG_TWO))
# Sample paper
mcq("sqp4", [ET], "A quadrilateral ABCD is drawn to circumscribe a circle. If BC = 7 cm, CD = 4 cm and AD = 3 cm, then the length of AB is", ["$3$ cm", "$4$ cm", "$6$ cm", "$7$ cm"], 2,
    "$AB + CD = AD + BC$, so $AB + 4 = 3 + 7$ and $AB = 6$ cm.", "medium", source=SQP(4))
mcq("sqp18", [TR], "The length of a tangent drawn to a circle of radius 9 cm from a point at a distance of 41 cm from the centre of the circle is", ["$40$ cm", "$9$ cm", "$41$ cm", "$50$ cm"], 0,
    "$TP^{2} = 41^{2} - 9^{2} = 1600$, so $TP = 40$ cm.", source=SQP(18))
q("sqp25", "very_short_answer", 2, [ET], SQP(25), "A $\\triangle ABC$ is drawn to circumscribe a circle of radius 4 cm such that the segments BD and DC are of lengths 10 cm and 8 cm respectively. Find the lengths of the sides AB and AC, if it is given that ar($\\triangle ABC$) $= 90$ cm².", "hard",
  answer_steps=["Equal tangents: $BE = BD = 10$, $CF = CD = 8$, $AE = AF = x$. Area $= \\dfrac{1}{2} \\times 4 \\times (AB + BC + CA) = 2(2x + 36)$.", "$2(2x + 36) = 90$ gives $x = 4.5$, so $AB = 14.5$ cm and $AC = 12.5$ cm."],
  marking_scheme=["1 mark: area as sum of three triangles", "1 mark: sides"])
q("sqp26", "short_answer", 3, [ET, TR], SQP(26), "XY and X′Y′ are two parallel tangents to a circle with centre O and another tangent AB with point of contact C intersecting XY at A and X′Y′ at B. Prove that $\\angle AOB = 90^\\circ$.", "hard",
  answer_steps=["In $\\triangle APO$ and $\\triangle ACO$: $AP = AC$ (tangents from an external point), $AO$ is common, $OP = OC$ (radii), so $\\triangle APO \\cong \\triangle ACO$ and $\\angle POA = \\angle COA$.",
                "Similarly $\\angle QOB = \\angle COB$, where $PQ$ is the diameter through the points of contact, so $\\angle POQ = 180^\\circ$.", "$2\\angle COA + 2\\angle COB = 180^\\circ$, so $\\angle AOB = 90^\\circ$."],
  marking_scheme=["1 mark: congruent triangles", "1 mark: angles on the diameter", "1 mark: conclusion"], figure=dict(FIG_PAR))
# Shine MCQs
mcq("mcq01", [TB], "The number of tangents that can be drawn to a circle from a point inside it is:", ["$0$", "$1$", "$2$", "infinitely many"], 0, "Every line through an inside point cuts the circle twice.")
mcq("mcq02", [TB], "The number of tangents that can be drawn to a circle from a point on the circle is:", ["$1$", "$0$", "$2$", "infinitely many"], 0, "There is exactly one tangent at each point of a circle.")
mcq("mcq03", [TR], "The angle between a tangent and the radius at the point of contact is:", ["$90^\\circ$", "$60^\\circ$", "$45^\\circ$", "$180^\\circ$"], 0, "Theorem 10.1: the tangent is perpendicular to the radius.")
mcq("mcq04", [TR], "The length of the tangent from a point 13 cm away from the centre of a circle of radius 5 cm is:", ["$12$ cm", "$8$ cm", "$18$ cm", "$\\sqrt{194}$ cm"], 0, "$\\sqrt{13^{2} - 5^{2}} = 12$ cm.")
mcq("mcq05", [ET], "PA and PB are tangents to a circle with centre O. If $\\angle APB = 60^\\circ$, then $\\angle AOB$ is:", ["$120^\\circ$", "$60^\\circ$", "$30^\\circ$", "$90^\\circ$"], 0, "$\\angle AOB = 180^\\circ - 60^\\circ = 120^\\circ$.", "medium")
mcq("mcq06", [ET], "PA and PB are tangents from P to a circle. If PA = 10 cm, then PB is:", ["$10$ cm", "$5$ cm", "$20$ cm", "cannot be found"], 0, "Tangents from an external point are equal.")
mcq("mcq07", [TR], "Two concentric circles have radii 10 cm and 6 cm. The length of the chord of the larger circle which touches the smaller circle is:", ["$16$ cm", "$8$ cm", "$12$ cm", "$4$ cm"], 0,
    "Half the chord is $\\sqrt{10^{2} - 6^{2}} = 8$ cm, so the chord is 16 cm.", "medium")
mcq("mcq08", [TR], "The tangents drawn at the ends of a diameter of a circle are:", ["parallel", "perpendicular", "intersecting at the centre", "equal to the diameter"], 0, "Both are perpendicular to the same diameter, so they are parallel.")
mcq("mcq09", [ET], "A quadrilateral ABCD circumscribes a circle. If AB = 6 cm, BC = 7 cm and CD = 4 cm, then AD is:", ["$3$ cm", "$5$ cm", "$9$ cm", "$17$ cm"], 0, "$AB + CD = AD + BC$, so $10 = AD + 7$ and $AD = 3$ cm.", "medium")
mcq("mcq10", [TB], "At most how many tangents to a circle can be parallel to a given line?", ["$2$", "$1$", "$3$", "infinitely many"], 0, "Only the tangents at the two ends of one diameter are parallel to a given direction.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [TR], "The length of the tangent from a point 5 cm from the centre of a circle of radius 3 cm is 4 cm.", "The tangent at any point of a circle is perpendicular to the radius through the point of contact.", 0,
   "The right angle in R gives $\\sqrt{5^{2} - 3^{2}} = 4$ cm.")
ar("ar2", [TB], "No tangent can be drawn to a circle from a point inside it.", "Every line through a point inside a circle meets the circle in two points.", 0, "Since every such line is a secant, none can be a tangent: R explains A.")
ar("ar3", [ET], "The lengths of the two tangents from an external point to a circle are equal.", "A circle has infinitely many tangents.", 1, "Both are true, but A follows from congruent triangles, not from R.")
ar("ar4", [ET], "If the angle between two tangents from a point P is $70^\\circ$, the angle between the radii to the points of contact is $120^\\circ$.", "The angle between the tangents and the angle between the radii add up to $180^\\circ$.", 3,
   "A is false: the angle is $180^\\circ - 70^\\circ = 110^\\circ$. R is true.")
ar("ar5", [TR], "The perpendicular at the point of contact to the tangent passes through the centre.", "A circle can have at most one tangent.", 2, "A is true. R is false: a circle has infinitely many tangents.")

q("vsa1", "very_short_answer", 2, [TR], SHINE, "From a point P, 17 cm away from the centre O of a circle of radius 8 cm, a tangent PT is drawn. Find PT.", "easy",
  answer_steps=["$OT \\perp PT$ (radius ⊥ tangent), so $PT^{2} = 17^{2} - 8^{2} = 225$.", "$PT = 15$ cm"], marking_scheme=MS2N)
q("vsa2", "very_short_answer", 2, [ET], SHINE, "PA and PB are tangents from P to a circle with centre O. If $\\angle APB = 50^\\circ$, find $\\angle OAB$.",
  answer_steps=["$PA = PB$, so $\\angle PAB = \\angle PBA = \\dfrac{180^\\circ - 50^\\circ}{2} = 65^\\circ$.", "$\\angle OAB = 90^\\circ - 65^\\circ = 25^\\circ$"], marking_scheme=["1 mark: $\\angle PAB$", "1 mark: $\\angle OAB$"])
q("sa1", "short_answer", 3, [ET], SHINE, "Two tangents PA and PB are drawn to a circle with centre O from an external point P. Prove that $\\angle APB = 2\\angle OAB$.", "hard",
  answer_steps=["Let $\\angle APB = \\theta$. $PA = PB$ (tangents from an external point), so $\\angle PAB = \\angle PBA = 90^\\circ - \\dfrac{\\theta}{2}$.", "$\\angle OAP = 90^\\circ$ (radius ⊥ tangent), so $\\angle OAB = 90^\\circ - \\angle PAB = \\dfrac{\\theta}{2}$.",
                "Hence $\\angle APB = 2\\angle OAB$."], marking_scheme=MS3P)
q("sa2", "short_answer", 3, [ET], SHINE, "Prove that the tangents drawn at the ends of a chord of a circle make equal angles with the chord.",
  answer_steps=["Let the tangents at the ends $A$ and $B$ of chord $AB$ meet at $P$.", "$PA = PB$ (tangents from an external point).", "So $\\triangle PAB$ is isosceles and $\\angle PAB = \\angle PBA$."], marking_scheme=MS3P)
q("sa3", "short_answer", 3, [ET, TR], SHINE, "A circle is inscribed in a right-angled triangle ABC, right-angled at B. If BC = 7 cm and AB = 24 cm, find the radius of the circle.", "hard",
  answer_steps=["$AC = \\sqrt{24^{2} + 7^{2}} = 25$ cm.", "The radii to $AB$ and $BC$ with the corner $B$ form a square of side $r$, so the tangents from $B$ are $r$; equal tangents give $AC = (24 - r) + (7 - r)$.", "$25 = 31 - 2r$, so $r = 3$ cm."],
  marking_scheme=["1 mark: hypotenuse", "1 mark: equal tangents", "1 mark: radius"])
q("la1", "long_answer", 5, [ET], SHINE, "Prove that the lengths of tangents drawn from an external point to a circle are equal. Hence, if a quadrilateral ABCD circumscribes a circle with AB = 8 cm, BC = 10 cm and CD = 12 cm, find AD.", "medium",
  answer_steps=["Let $PQ$ and $PR$ be tangents from $P$ to the circle with centre $O$; join $OQ$, $OR$, $OP$.", "$OQ = OR$ (radii), $OP$ common, $\\angle OQP = \\angle ORP = 90^\\circ$, so $\\triangle OQP \\cong \\triangle ORP$ (RHS) and $PQ = PR$.",
                "For $ABCD$, equal tangents from each vertex give $AB + CD = AD + BC$.", "$8 + 12 = AD + 10$", "$AD = 10$ cm"],
  marking_scheme=["1 mark: figure", "2 marks: proof", "1 mark: $AB + CD = AD + BC$", "1 mark: $AD$"])
q("la2", "long_answer", 5, [ET], SHINE, "A triangle ABC circumscribes a circle of radius 3 cm. The point of contact D divides BC into BD = 6 cm and DC = 9 cm. If the area of the triangle is 54 cm², find AB and AC, and show that the triangle is right-angled.", "hard",
  answer_steps=["Equal tangents: let $AE = AF = x$; then $AB = x + 6$, $AC = x + 9$, $BC = 15$.", "Area $= \\dfrac{1}{2} \\times 3 \\times (\\text{perimeter}) = 3(15 + x)$.", "$3(15 + x) = 54$, so $x = 3$.", "$AB = 9$ cm, $AC = 12$ cm",
                "$9^{2} + 12^{2} = 81 + 144 = 225 = 15^{2}$, so the angle at $A$ is $90^\\circ$."],
  marking_scheme=["1 mark: equal tangents", "1 mark: area", "1 mark: $x$", "1 mark: sides", "1 mark: right angle"])
q("cb1", "case_based", 4, [TR, ET], SHINE,
  "A circular garden has radius 5 m and centre O. From a gate P, 13 m from O, two straight paths PA and PB touch the garden's boundary at A and B.\n\n(i) Find the length of the path PA. (1)\n\n(ii) Without calculating again, find PB. Give the reason. (1)\n\n(iii) Find the area of the quadrilateral OAPB. OR Find the perimeter of OAPB. (2)",
  answer_steps=["(i) $OA \\perp PA$, so $PA = \\sqrt{13^{2} - 5^{2}} = 12$ m.", "(ii) $PB = 12$ m, because tangents from an external point are equal.",
                "(iii) Area $= 2 \\times \\dfrac{1}{2} \\times 5 \\times 12 = 60$ m². OR Perimeter $= 5 + 12 + 12 + 5 = 34$ m."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [ET], SHINE,
  "A triangular park ABC has a circular fountain of radius 4 m touching all three sides. The fountain touches BC at D, CA at E and AB at F, with BD = 8 m and DC = 6 m.\n\n(i) Name the pairs of equal tangent segments. (1)\n\n(ii) If AF = x, write AB and AC in terms of x. (1)\n\n(iii) Using area $= r \\times s$ (where $s$ is the semi-perimeter) and Heron's formula, find x. OR If x = 7, find the perimeter of the park. (2)",
  answer_steps=["(i) $BD = BF$, $CD = CE$, $AE = AF$.", "(ii) $AB = x + 8$, $AC = x + 6$", "(iii) $4(14 + x) = \\sqrt{(14 + x) \\cdot x \\cdot 6 \\cdot 8}$ gives $x = 7$. OR Perimeter $= 15 + 13 + 14 = 42$ m."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"], figure=dict(FIG_TRI))

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch10.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
