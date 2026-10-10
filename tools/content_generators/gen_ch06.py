"""CBSE Class 10 Maths Ch 6: Triangles.
Numerical answers are checked with exact fractions; figure coordinates are built
from the stated ratios so parallel lines and right angles are exact."""
import json, math, os, sys
from collections import Counter
from fractions import Fraction as Fr

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch06"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch06_triangles"

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

# ---------------------------------------------------------------- verification
check(Fr(3, 2) / 3 == Fr(1) / 2 and 1 * Fr(3) / Fr(3, 2) == 2, "6.2 Q1 i: EC = 2")
check(Fr(18, 10) * Fr(72, 10) / Fr(54, 10) == Fr(24, 10), "6.2 Q1 ii: AD = 2.4")
check(Fr(39, 30) != Fr(36, 24), "6.2 Q2 i"); check(4 / Fr(45, 10) == Fr(8, 9) == Fr(8, 9), "6.2 Q2 ii")
check(Fr(18, 100) / (Fr(128, 100) - Fr(18, 100)) == Fr(36, 100) / (Fr(256, 100) - Fr(36, 100)), "6.2 Q2 iii")
check(Fr(6, 4) * 28 == 42, "6.3 Q15"); check(180 - 125 == 55 and 180 - 70 - 55 == 55, "6.3 Q2")
check(Fr(57, 10) * Fr(55, 10) / (Fr(152, 10) - Fr(57, 10)) == Fr(33, 10), "sqp33 PM = 3.3")
check(Fr(6, 9) * (9 + 6 + 12) == 18, "sqp14 perimeter 18")
check(Fr(2, 3) * 6 == 4 and 4 * Fr(3, 2) == 6, "mcq01 EC = 6"); check(8 * Fr(3, 2) == 12, "mcq02")
check(180 - 50 - 60 == 70, "mcq04"); check(Fr(15, 10) / 2 * 12 == 9, "mcq07"); check(6 + 6 * Fr(5, 3) == 16, "mcq09")
check(18 * Fr(6, 4) == 27, "mcq11"); check(Fr(2, 4) == Fr(3, 6), "ar1"); check(Fr(2, 4) == Fr(3, 6) == Fr(4, 8), "ar4")
check(14 * Fr(3, 7) == 6, "vsa1"); check(180 - 32 - 65 == 83, "vsa2")
check([x for x in range(3, 20) if Fr(x, x - 2) == Fr(x + 2, x - 1)] == [4], "sa1 x = 4")
check((Fr(6, 3) * 4, Fr(6, 3) * 5, Fr(6, 3) * 12) == (8, 10, 24), "sa2"); check(Fr(32, 10) * Fr(10, 4) == 8, "sa3")
check(18 * Fr(2, 5) == Fr(36, 5), "la1 AE = 7.2"); check(Fr(12, 10) / Fr(9, 10) * 6 == 8 and Fr(12, 10) / Fr(9, 10) * 15 == 20 and 4 * Fr(9, 12) == 3, "cb1")
check(9 * Fr(2, 6) == 3 and Fr(5, 2) * 3 == Fr(15, 2) and Fr(5, 2) * 2 == 5, "cb2")

# ---------------------------------------------------------------- figures
def lerp(p, q, t): return [p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t]
def r9(p): return [round(p[0], 9), round(p[1], 9)]

A, B, C = [1.5, 4.5], [0, 0], [6, 0]
D, E = lerp(A, B, 1 / 3), lerp(A, C, 1 / 3)
FIG_BPT = {"type": "geometry_figure", "title": "DE is parallel to BC", "points": {"A": A, "B": B, "C": C, "D": r9(D), "E": r9(E)},
           "segments": [["A", "B"], ["B", "C"], ["C", "A"], {"from": "D", "to": "E", "highlight": True}], "parallel": [["D", "E", "B", "C"]]}
FIG_BPT_PROOF = dict(FIG_BPT, title="Proof: join BE and CD",
                     segments=FIG_BPT["segments"] + [{"from": "B", "to": "E", "dashed": True}, {"from": "C", "to": "D", "dashed": True}])
# Ex 6.2 Q1 (i): AD = 1.5, DB = 3, AE = 1 (drawn to scale along the sides).
a1, b1 = [2.0, 3.3], [0.0, 0.0]
ab = math.dist(a1, b1); d1 = lerp(a1, b1, 1.5 / 4.5)
c1 = lerp(a1, [6.0, 0.0], 1.0)  # direction for AC
e1 = lerp(a1, c1, 1 / 3)
FIG_621 = {"type": "geometry_figure", "title": "DE ∥ BC", "points": {"A": a1, "B": b1, "C": c1, "D": r9(d1), "E": r9(e1)},
           "segments": [["A", "B"], ["B", "C"], ["C", "A"], {"from": "D", "to": "E", "highlight": True}], "parallel": [["D", "E", "B", "C"]],
           "lengths": [{"from": "A", "to": "D", "label": "1.5 cm"}, {"from": "D", "to": "B", "label": "3 cm"}, {"from": "A", "to": "E", "label": "1 cm"}]}
# Similar triangles (AA): PQR is ABC enlarged 1.5 times.
FIG_SIM = {"type": "geometry_figure", "title": "Same shape, different size",
           "points": {"A": [1, 3], "B": [0, 0], "C": [4, 0], "P": [7.5, 4.5], "Q": [6, 0], "R": [12, 0]},
           "segments": [["A", "B"], ["B", "C"], ["C", "A"], ["P", "Q"], ["Q", "R"], ["R", "P"]],
           "angles": [{"points": ["C", "B", "A"], "label": "x"}, {"points": ["R", "Q", "P"], "label": "x"},
                      {"points": ["A", "C", "B"], "label": "y"}, {"points": ["P", "R", "Q"], "label": "y"}]}
# Shadows: pole 6 m with shadow 4 m; tower h with shadow 28 m (to scale).
FIG_SHADOW = {"type": "geometry_figure", "title": "Same sun, same angle",
              "points": {"A": [0, 6], "B": [0, 0], "C": [4, 0], "P": [10, 42], "Q": [10, 0], "R": [38, 0]},
              "segments": [{"from": "A", "to": "B", "highlight": True}, ["B", "C"], {"from": "A", "to": "C", "dashed": True},
                           {"from": "P", "to": "Q", "highlight": True}, ["Q", "R"], {"from": "P", "to": "R", "dashed": True}],
              "right_angles": [["A", "B", "C"], ["P", "Q", "R"]], "parallel": [["A", "C", "P", "R"]],
              "lengths": [{"from": "A", "to": "B", "label": "6 m"}, {"from": "B", "to": "C", "label": "4 m"}, {"from": "Q", "to": "R", "label": "28 m"}, {"from": "P", "to": "Q", "label": "h"}]}
# Ex 6.3 Q2: ΔODC ~ ΔOBA, ∠BOC = 125°, ∠CDO = 70° (so ∠DOC = ∠DCO = 55°).
k, s55, c55 = 4.0, math.sin(math.radians(55)), math.cos(math.radians(55))
od, oc = k * s55, k * math.sin(math.radians(70))
Dq, Cq = [od * c55, od * s55], [oc, 0.0]
Bq, Aq = [-1.3 * Dq[0], -1.3 * Dq[1]], [-1.3 * oc, 0.0]
FIG_632 = {"type": "geometry_figure", "title": "ΔODC ~ ΔOBA", "points": {"O": [0, 0], "D": r9(Dq), "C": r9(Cq), "B": r9(Bq), "A": r9(Aq)},
           "segments": [["A", "C"], ["B", "D"], ["D", "C"], ["A", "B"]], "parallel": [["D", "C", "A", "B"]],
           "angles": [{"points": ["C", "O", "B"], "label": "125°"}, {"points": ["O", "D", "C"], "label": "70°"}]}
# Ex 6.3 Q7: altitudes AD and CE meet at P.
FIG_637 = {"type": "geometry_figure", "title": "Altitudes AD and CE meet at P",
           "points": {"A": [2, 4], "B": [0, 0], "C": [6, 0], "D": [2, 0], "E": [1.2, 2.4], "P": [2, 2]},
           "segments": [["A", "B"], ["B", "C"], ["C", "A"], {"from": "A", "to": "D", "highlight": True}, {"from": "C", "to": "E", "highlight": True}],
           "right_angles": [["A", "D", "B"], ["C", "E", "A"]]}
check(abs(math.degrees(math.atan2(Dq[1], Dq[0])) - 55) < 1e-9, "fig 6.3 Q2 angle")

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch06.{id_}", "type": type_, **kw}
def fig(id_, figure): return {"id": f"ch06.{id_}", **figure}

sections = [
 {"id": "s1", "title": "Same shape, different size", "blocks": [
  b("s1.hook", "hook", title="Measuring a pyramid with a stick",
    body="How would you find the height of a building without climbing it? You cannot reach the top with a measuring tape.\n\n"
         "On a sunny day, stand a stick upright and measure its shadow. At the same moment, measure the building's shadow. "
         "The stick and its shadow make a small triangle; the building and its shadow make a big triangle of **the same shape**. "
         "In this chapter you will learn why such triangles are *similar*, and how that lets you measure what you cannot reach."),
  b("s1.inspiration", "inspiration", title="The man who measured a pyramid", person="Thales of Miletus", years="about 624–546 BCE",
    body="Thales was a Greek merchant who became one of the first mathematicians known by name. Ancient writers tell that he found the height of the Great Pyramid of Egypt by comparing its shadow with the shadow of a stick: "
         "he waited until a stick's shadow was as long as the stick itself, and then the pyramid's shadow was as long as the pyramid was tall.\n\n"
         "The Basic Proportionality Theorem you will prove in this chapter is often called **Thales' theorem** in his honour.",
    quote="You don't need to climb the mountain to know its height. Think, and the triangle will tell you.",
    future="Similar triangles are used to make maps and scale models, in cameras and projectors, by surveyors and engineers, and in Chapter 9 of this book to find heights and distances."),
  b("s1.socratic", "socratic_question", question="A photo of you is enlarged to twice its size. Which of these changes?",
    options=["The lengths double, but the angles stay the same", "The angles double, but the lengths stay the same", "Both the lengths and the angles double"], correct_index=0,
    explanation="Enlarging keeps the shape: every angle stays the same and every length is multiplied by the same number. Figures with the same shape are called similar."),
 ]},
 {"id": "s2", "title": "Similar figures", "blocks": [
  b("s2.reveal", "theory", title="Similar and congruent", revision=True,
    body="Two figures with the **same shape** (but not necessarily the same size) are **similar**. Two figures with the same shape **and** the same size are **congruent**. "
         "So all congruent figures are similar, but similar figures need not be congruent.\n\n"
         "Two polygons with the same number of sides are **similar** if\n\n"
         "1. their corresponding angles are **equal**, and\n"
         "2. their corresponding sides are in the **same ratio** (proportional).\n\n"
         "Both conditions are needed. All circles are similar, all squares are similar and all equilateral triangles are similar."),
  b("s2.eg1", "worked_example", title="Why both conditions are needed",
    problem="Is a square of side 2 cm similar to (i) a rhombus of side 4 cm with an angle of $60^\\circ$? (ii) a rectangle of sides 2 cm and 5 cm?",
    steps=["(i) The sides are in the ratio $2 : 4$, all the same, but the angles ($90^\\circ$ and $60^\\circ$) are not equal: not similar.",
           "(ii) All angles are $90^\\circ$, but the sides are not in the same ratio ($\\dfrac{2}{2} \\neq \\dfrac{2}{5}$): not similar."],
    answer="Neither is similar to the square."),
  fig("s2.fig", FIG_SIM),
  b("s2.check", "knowledge_check", question="Which pair of figures is always similar?",
    options=["Two squares", "Two rectangles", "Two rhombuses", "Two isosceles triangles"], correct_index=0,
    explanation="Every square has four $90^\\circ$ angles and four equal sides, so any two squares have equal angles and proportional sides."),
 ]},
 {"id": "s3", "title": "Basic Proportionality Theorem", "blocks": [
  b("s3.discovery", "discovery", title="Cut a triangle with a parallel line",
    body="Draw any triangle ABC and a line DE parallel to BC, cutting AB at D and AC at E. Measure AD, DB, AE and EC. "
         "Whatever triangle you draw, you will find $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$. In the figure, $AD : DB = AE : EC = 1 : 2$."),
  fig("s3.fig", FIG_BPT),
  b("s3.reveal", "theory", title="Theorem 6.1 and its converse", revision=True,
    body="**Theorem 6.1 (Basic Proportionality Theorem):** If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.\n\n"
         "In $\\triangle ABC$, if $DE \\parallel BC$, then $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.\n\n"
         "**Theorem 6.2 (Converse):** If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.\n\n"
         "Useful forms: $\\dfrac{AD}{AB} = \\dfrac{AE}{AC}$ and $\\dfrac{DB}{AB} = \\dfrac{EC}{AC}$."),
  b("s3.proof", "worked_example", title="Proof of Theorem 6.1",
    problem="In $\\triangle ABC$, a line parallel to $BC$ meets $AB$ at $D$ and $AC$ at $E$. Prove that $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
    steps=["Join $BE$ and $CD$. Draw $DM \\perp AC$ and $EN \\perp AB$.",
           "$\\text{ar}(ADE) = \\dfrac{1}{2} \\times AD \\times EN$ and $\\text{ar}(BDE) = \\dfrac{1}{2} \\times DB \\times EN$, so $\\dfrac{\\text{ar}(ADE)}{\\text{ar}(BDE)} = \\dfrac{AD}{DB}$.",
           "Similarly, $\\dfrac{\\text{ar}(ADE)}{\\text{ar}(DEC)} = \\dfrac{AE}{EC}$.",
           "$\\triangle BDE$ and $\\triangle DEC$ are on the same base $DE$ and between the same parallels $BC$ and $DE$, so $\\text{ar}(BDE) = \\text{ar}(DEC)$.",
           "Hence $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$."],
    answer="Proved."),
  fig("s3.prooffig", FIG_BPT_PROOF),
  b("s3.eg1", "worked_example", title="Using the theorem",
    problem="In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $AD = 1.5$ cm, $DB = 3$ cm and $AE = 1$ cm, find $EC$.",
    steps=["By Theorem 6.1, $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.", "$\\dfrac{1.5}{3} = \\dfrac{1}{EC}$, so $EC = \\dfrac{3}{1.5} = 2$."], answer="$EC = 2$ cm"),
  b("s3.eg2", "worked_example", title="Using the converse",
    problem="In $\\triangle PQR$, $E$ and $F$ are points on $PQ$ and $PR$ with $PE = 4$ cm, $QE = 4.5$ cm, $PF = 8$ cm and $RF = 9$ cm. Is $EF \\parallel QR$?",
    steps=["$\\dfrac{PE}{EQ} = \\dfrac{4}{4.5} = \\dfrac{8}{9}$ and $\\dfrac{PF}{FR} = \\dfrac{8}{9}$.", "The sides are divided in the same ratio, so by Theorem 6.2, $EF \\parallel QR$."],
    answer="Yes, $EF \\parallel QR$."),
  b("s3.check", "knowledge_check", question="In $\\triangle ABC$, $DE \\parallel BC$, $AD = 2$ cm, $DB = 3$ cm and $AE = 4$ cm. Then $EC$ is:",
    options=["$6$ cm", "$\\dfrac{8}{3}$ cm", "$1.5$ cm", "$5$ cm"], correct_index=0,
    explanation="$\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$ gives $\\dfrac{2}{3} = \\dfrac{4}{EC}$, so $EC = 6$ cm."),
  b("s3.tip", "teacher_tip", title="Let students discover it",
    body="Before stating the theorem, ask each student to draw a different triangle and a parallel line, measure the four lengths and report $\\dfrac{AD}{DB}$ and $\\dfrac{AE}{EC}$. "
         "When the whole class finds the ratios equal, the proof feels necessary rather than imposed. In the board exam, the proof of Theorem 6.1 often comes as a 5-mark question."),
 ]},
 {"id": "s4", "title": "Criteria for similarity of triangles", "blocks": [
  b("s4.reveal", "theory", title="AAA, SSS and SAS", revision=True,
    body="$\\triangle ABC \\sim \\triangle DEF$ means $\\angle A = \\angle D$, $\\angle B = \\angle E$, $\\angle C = \\angle F$ and $\\dfrac{AB}{DE} = \\dfrac{BC}{EF} = \\dfrac{CA}{FD}$. The **order of letters** shows which parts correspond.\n\n"
         "You do not need to check all six facts. Any one of these is enough:\n\n"
         "- **AAA (or AA):** the corresponding angles are equal. Two equal angles are enough, because the third then also matches.\n"
         "- **SSS:** the corresponding sides are in the same ratio.\n"
         "- **SAS:** one angle is equal and the sides **including** that angle are in the same ratio."),
  b("s4.eg1", "worked_example", title="NCERT exercise: the tower's height",
    problem="A vertical pole of length 6 m casts a shadow 4 m long on the ground, and at the same time a tower casts a shadow 28 m long. Find the height of the tower.",
    steps=["The pole and the tower are vertical, so each makes a right angle with the ground.", "The sun's rays fall at the same angle on both, so the two triangles are similar (AA).",
           "$\\dfrac{h}{6} = \\dfrac{28}{4}$, so $h = 6 \\times 7 = 42$."],
    answer="The tower is 42 m high."),
  fig("s4.fig", FIG_SHADOW),
  b("s4.eg2", "worked_example", title="NCERT exercise: angles in similar triangles",
    problem="The lines $AC$ and $BD$ meet at $O$, and $\\triangle ODC \\sim \\triangle OBA$. If $\\angle BOC = 125^\\circ$ and $\\angle CDO = 70^\\circ$, find $\\angle DOC$, $\\angle DCO$ and $\\angle OAB$.",
    steps=["$\\angle DOC = 180^\\circ - 125^\\circ = 55^\\circ$ (linear pair).", "In $\\triangle ODC$: $\\angle DCO = 180^\\circ - 70^\\circ - 55^\\circ = 55^\\circ$.",
           "Since $\\triangle ODC \\sim \\triangle OBA$, $\\angle OAB = \\angle OCD = 55^\\circ$."],
    answer="$\\angle DOC = \\angle DCO = \\angle OAB = 55^\\circ$"),
  fig("s4.fig2", FIG_632),
  b("s4.eg3", "worked_example", title="NCERT exercise: a proof with AA",
    problem="$D$ is a point on side $BC$ of $\\triangle ABC$ such that $\\angle ADC = \\angle BAC$. Show that $CA^{2} = CB \\cdot CD$.",
    steps=["In $\\triangle ADC$ and $\\triangle BAC$: $\\angle ADC = \\angle BAC$ (given) and $\\angle C$ is common.", "So $\\triangle ADC \\sim \\triangle BAC$ (AA).",
           "Corresponding sides are proportional: $\\dfrac{CA}{CB} = \\dfrac{CD}{CA}$."],
    answer="$CA^{2} = CB \\cdot CD$"),
  b("s4.check1", "knowledge_check", question="Triangles with sides 3 cm, 4 cm, 5 cm and 6 cm, 8 cm, 10 cm are similar by the criterion:",
    options=["SSS", "SAS", "AAA", "RHS"], correct_index=0, explanation="$\\dfrac{3}{6} = \\dfrac{4}{8} = \\dfrac{5}{10} = \\dfrac{1}{2}$: all three sides are in the same ratio."),
  b("s4.check2", "knowledge_check", question="If $\\triangle ABC \\sim \\triangle PQR$, which of these is true?",
    options=["$\\dfrac{AB}{PQ} = \\dfrac{AC}{PR}$", "$\\dfrac{AB}{PR} = \\dfrac{BC}{QR}$", "$\\dfrac{AB}{QR} = \\dfrac{AC}{PQ}$", "$\\dfrac{AB}{PQ} = \\dfrac{AC}{QR}$"], correct_index=0,
    explanation="Match the letters in order: $A \\leftrightarrow P$, $B \\leftrightarrow Q$, $C \\leftrightarrow R$. So $AB \\leftrightarrow PQ$ and $AC \\leftrightarrow PR$."),
  b("s4.memory", "memory_trick", title="Read the name in order", revision=True,
    body="In $\\triangle ABC \\sim \\triangle PQR$, write the letters one below the other:\n\n$$\\begin{matrix} A & B & C \\\\ P & Q & R \\end{matrix}$$\n\n"
         "Pairs of letters give the matching angles ($A$ with $P$), and pairs of pairs give the matching sides ($AB$ with $PQ$, $BC$ with $QR$, $CA$ with $RP$)."),
  b("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing the similarity in the wrong order, e.g. $\\triangle ABC \\sim \\triangle QPR$ when $A$ matches $P$.\n"
         "- Using SAS with an angle that is **not** between the two sides.\n"
         "- Using $\\dfrac{AD}{AB} = \\dfrac{AE}{EC}$, which mixes two different forms of the theorem.\n"
         "- Calling ASA or RHS a similarity criterion: those are congruence criteria.\n"
         "- In proofs, not writing the reason (given, common, alternate angles, etc.) for each step."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  b("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why two equal angles are enough to show that two triangles are similar, while for quadrilaterals equal angles are not enough."),
  b("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 8, Trigonometry:** trigonometric ratios make sense only because similar right triangles have equal ratios of sides.\n"
         "- **Chapter 9, Heights and Distances:** the shadow method grows into a full method for measuring heights.\n"
         "- **Geography and design:** map scales, architects' plans and scale models are all similar figures."),
  b("s5.mastery", "mastery", title="Mastery challenge",
    body="$ABCD$ is a trapezium with $AB \\parallel DC$. Its diagonals meet at $O$. Show that $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$.\n\n"
         "**Answer:** In $\\triangle AOB$ and $\\triangle COD$: $\\angle OAB = \\angle OCD$ and $\\angle OBA = \\angle ODC$ (alternate angles, $AB \\parallel DC$). "
         "So $\\triangle AOB \\sim \\triangle COD$ (AA), giving $\\dfrac{AO}{CO} = \\dfrac{BO}{DO}$, i.e. $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$."),
  b("s5.summary", "summary", title="Chapter summary",
    body="- Figures with the same shape are similar; with the same shape and size they are congruent.\n"
         "- Polygons with the same number of sides are similar if corresponding angles are equal **and** corresponding sides are proportional.\n"
         "- **Basic Proportionality Theorem:** a line parallel to one side of a triangle divides the other two sides in the same ratio. Its converse is also true.\n"
         "- Triangles are similar by **AAA (AA)**, **SSS** or **SAS**."),
  b("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Learn the statement and proof of Theorem 6.1 thoroughly: it is a frequent 5-mark question.\n"
         "- Write similarity statements with the letters in corresponding order.\n"
         "- In every proof, give a reason for each step and name the criterion (AA, SSS or SAS).\n"
         "- In numerical questions, write the proportion first, then substitute."),
  b("s5.flash1", "flashcard", front="State the Basic Proportionality Theorem.", back="If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio."),
  b("s5.flash2", "flashcard", front="Name the three criteria for similarity of triangles.", back="AAA (or AA), SSS and SAS."),
  b("s5.flash3", "flashcard", front="Are all congruent figures similar?", back="Yes. But similar figures need not be congruent, because their sizes can differ."),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Triangles",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 6,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: similar figures, Basic Proportionality Theorem (proof) and its converse, and the AAA, SSS and SAS criteria. Areas of similar triangles and the Pythagoras theorem are not in the board syllabus and are not included. NCERT Exercise 6.3 Q1 depends on the textbook figure and is not reproduced.",
  "concepts": ["similar_figures", "basic_proportionality_theorem", "similarity_criteria", "similarity_applications"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
SIMF, BPT, CRIT, APPL = "similar_figures", "basic_proportionality_theorem", "similarity_criteria", "similarity_applications"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch06.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS3_PROOF = ["1 mark: correct figure / pairs of triangles", "1 mark: similarity or theorem with reasons", "1 mark: conclusion"]
MS2_NUM = ["1 mark: correct proportion", "1 mark: answer"]

# Exercise 6.1
mcq("ex6_1.q1.i", [SIMF], "Fill in the blank: All circles are ____.", ["similar", "congruent", "equal in area", "concentric"], 0,
    "Every circle has the same shape; only the radius changes.", source=ex("6.1", 1, "i"))
mcq("ex6_1.q1.ii", [SIMF], "Fill in the blank: All squares are ____.", ["similar", "congruent", "equal in area", "equal in perimeter"], 0,
    "All squares have $90^\\circ$ angles and equal sides, so they have the same shape.", source=ex("6.1", 1, "ii"))
mcq("ex6_1.q1.iii", [SIMF], "Fill in the blank: All ____ triangles are similar.", ["equilateral", "isosceles", "right-angled", "scalene"], 0,
    "Every equilateral triangle has all angles $60^\\circ$.", source=ex("6.1", 1, "iii"))
mcq("ex6_1.q1.iv", [SIMF], "Fill in the blanks: Two polygons of the same number of sides are similar, if (a) their corresponding angles are ____ and (b) their corresponding sides are ____.",
    ["equal; proportional", "proportional; equal", "equal; equal", "supplementary; proportional"], 0,
    "Similar polygons have equal corresponding angles and proportional corresponding sides.", source=ex("6.1", 1, "iv"))
q("ex6_1.q2", "very_short_answer", 2, [SIMF], ex("6.1", 2), "Give two different examples of a pair of (i) similar figures, (ii) non-similar figures.", "easy",
  answer_steps=["(i) Similar: two circles of radii 2 cm and 5 cm; two equilateral triangles of sides 3 cm and 6 cm.",
                "(ii) Non-similar: a square and a rectangle that is not a square; an equilateral triangle and a right triangle."],
  marking_scheme=["1 mark: two similar pairs", "1 mark: two non-similar pairs"])
q("ex6_1.q3", "very_short_answer", 2, [SIMF], ex("6.1", 3), "State whether a square of side 1.5 cm and a rhombus of side 3 cm whose angles are not right angles are similar. Give a reason.", "easy",
  answer_steps=["The sides are proportional ($\\dfrac{1.5}{3}$ for every pair), but the angles of the rhombus are not $90^\\circ$.", "The corresponding angles are not equal, so they are not similar."],
  marking_scheme=["1 mark: checking sides and angles", "1 mark: conclusion"])
# Exercise 6.2
q("ex6_2.q1.i", "very_short_answer", 2, [BPT], ex("6.2", 1, "i"), "In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $AD = 1.5$ cm, $DB = 3$ cm and $AE = 1$ cm, find $EC$.", "easy",
  answer_steps=["$\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$ (Theorem 6.1)", "$\\dfrac{1.5}{3} = \\dfrac{1}{EC}$, so $EC = 2$ cm."], marking_scheme=MS2_NUM, figure=dict(FIG_621))
q("ex6_2.q1.ii", "very_short_answer", 2, [BPT], ex("6.2", 1, "ii"), "In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $DB = 7.2$ cm, $AE = 1.8$ cm and $EC = 5.4$ cm, find $AD$.", "easy",
  answer_steps=["$\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$ (Theorem 6.1)", "$\\dfrac{AD}{7.2} = \\dfrac{1.8}{5.4}$, so $AD = 2.4$ cm."], marking_scheme=MS2_NUM)
for p, given, steps in [
 ("i", "PE = 3.9 \\text{ cm}, EQ = 3 \\text{ cm}, PF = 3.6 \\text{ cm and } FR = 2.4 \\text{ cm}", ["$\\dfrac{PE}{EQ} = \\dfrac{3.9}{3} = 1.3$ and $\\dfrac{PF}{FR} = \\dfrac{3.6}{2.4} = 1.5$", "The ratios are not equal, so $EF$ is not parallel to $QR$."]),
 ("ii", "PE = 4 \\text{ cm}, QE = 4.5 \\text{ cm}, PF = 8 \\text{ cm and } RF = 9 \\text{ cm}", ["$\\dfrac{PE}{EQ} = \\dfrac{4}{4.5} = \\dfrac{8}{9}$ and $\\dfrac{PF}{FR} = \\dfrac{8}{9}$", "The ratios are equal, so $EF \\parallel QR$ (Theorem 6.2)."]),
 ("iii", "PQ = 1.28 \\text{ cm}, PR = 2.56 \\text{ cm}, PE = 0.18 \\text{ cm and } PF = 0.36 \\text{ cm}", ["$\\dfrac{PE}{PQ} = \\dfrac{0.18}{1.28} = \\dfrac{9}{64}$ and $\\dfrac{PF}{PR} = \\dfrac{0.36}{2.56} = \\dfrac{9}{64}$", "The ratios are equal, so $EF \\parallel QR$ (Theorem 6.2)."]),
]:
    q(f"ex6_2.q2.{p}", "very_short_answer", 2, [BPT], ex("6.2", 2, p), f"$E$ and $F$ are points on the sides $PQ$ and $PR$ of $\\triangle PQR$. If ${given}$, state whether $EF \\parallel QR$.", "easy" if p != "iii" else "medium",
      answer_steps=steps, marking_scheme=["1 mark: both ratios", "1 mark: conclusion with theorem"])
PROOFS62 = [
 ("q3", "In a figure, $L$ is a point on $AC$, $M$ on $AB$ and $N$ on $AD$, such that $LM \\parallel CB$ and $LN \\parallel CD$. Prove that $\\dfrac{AM}{AB} = \\dfrac{AN}{AD}$.",
  ["In $\\triangle ABC$, $LM \\parallel CB$, so $\\dfrac{AM}{AB} = \\dfrac{AL}{AC}$ (Theorem 6.1).", "In $\\triangle ADC$, $LN \\parallel CD$, so $\\dfrac{AN}{AD} = \\dfrac{AL}{AC}$ (Theorem 6.1).", "Hence $\\dfrac{AM}{AB} = \\dfrac{AN}{AD}$."]),
 ("q4", "In $\\triangle ABC$, $D$ is a point on $AB$, and $E$ and $F$ are points on $BC$ (with $F$ between $B$ and $E$), such that $DE \\parallel AC$ and $DF \\parallel AE$. Prove that $\\dfrac{BF}{FE} = \\dfrac{BE}{EC}$.",
  ["In $\\triangle ABC$, $DE \\parallel AC$, so $\\dfrac{BD}{DA} = \\dfrac{BE}{EC}$ (Theorem 6.1).", "In $\\triangle ABE$, $DF \\parallel AE$, so $\\dfrac{BD}{DA} = \\dfrac{BF}{FE}$ (Theorem 6.1).", "Hence $\\dfrac{BF}{FE} = \\dfrac{BE}{EC}$."]),
 ("q5", "$O$ is a point inside $\\triangle PQR$. $D$ is a point on $PO$, $E$ on $PQ$ and $F$ on $PR$, such that $DE \\parallel OQ$ and $DF \\parallel OR$. Show that $EF \\parallel QR$.",
  ["In $\\triangle POQ$, $DE \\parallel OQ$, so $\\dfrac{PE}{EQ} = \\dfrac{PD}{DO}$ (Theorem 6.1).", "In $\\triangle POR$, $DF \\parallel OR$, so $\\dfrac{PF}{FR} = \\dfrac{PD}{DO}$ (Theorem 6.1).", "So $\\dfrac{PE}{EQ} = \\dfrac{PF}{FR}$, and in $\\triangle PQR$, $EF \\parallel QR$ (Theorem 6.2)."]),
 ("q6", "$A$, $B$ and $C$ are points on $OP$, $OQ$ and $OR$ respectively such that $AB \\parallel PQ$ and $AC \\parallel PR$. Show that $BC \\parallel QR$.",
  ["In $\\triangle OPQ$, $AB \\parallel PQ$, so $\\dfrac{OA}{AP} = \\dfrac{OB}{BQ}$ (Theorem 6.1).", "In $\\triangle OPR$, $AC \\parallel PR$, so $\\dfrac{OA}{AP} = \\dfrac{OC}{CR}$ (Theorem 6.1).", "So $\\dfrac{OB}{BQ} = \\dfrac{OC}{CR}$, and in $\\triangle OQR$, $BC \\parallel QR$ (Theorem 6.2)."]),
 ("q7", "Using Theorem 6.1, prove that a line drawn through the mid-point of one side of a triangle parallel to another side bisects the third side.",
  ["Let $D$ be the mid-point of $AB$ in $\\triangle ABC$, and let the line through $D$ parallel to $BC$ meet $AC$ at $E$.", "By Theorem 6.1, $\\dfrac{AE}{EC} = \\dfrac{AD}{DB} = 1$ (since $AD = DB$).", "So $AE = EC$: the line bisects $AC$."]),
 ("q8", "Using Theorem 6.2, prove that the line joining the mid-points of any two sides of a triangle is parallel to the third side.",
  ["Let $D$ and $E$ be the mid-points of $AB$ and $AC$ in $\\triangle ABC$.", "Then $\\dfrac{AD}{DB} = 1 = \\dfrac{AE}{EC}$.", "By Theorem 6.2, $DE \\parallel BC$."]),
 ("q9", "$ABCD$ is a trapezium in which $AB \\parallel DC$ and its diagonals intersect each other at the point $O$. Show that $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$.",
  ["Through $O$ draw $OE \\parallel DC$ (and so $\\parallel AB$), meeting $AD$ at $E$.", "In $\\triangle ADC$, $OE \\parallel DC$: $\\dfrac{AE}{ED} = \\dfrac{AO}{OC}$. In $\\triangle DAB$, $OE \\parallel AB$: $\\dfrac{AE}{ED} = \\dfrac{BO}{OD}$.",
   "So $\\dfrac{AO}{OC} = \\dfrac{BO}{OD}$, i.e. $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$."]),
 ("q10", "The diagonals of a quadrilateral $ABCD$ intersect each other at the point $O$ such that $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$. Show that $ABCD$ is a trapezium.",
  ["Through $O$ draw $OE \\parallel AB$, meeting $AD$ at $E$. In $\\triangle DAB$: $\\dfrac{AE}{ED} = \\dfrac{BO}{OD}$ (Theorem 6.1).",
   "Given $\\dfrac{AO}{BO} = \\dfrac{CO}{DO}$, so $\\dfrac{AO}{OC} = \\dfrac{BO}{OD} = \\dfrac{AE}{ED}$.", "In $\\triangle ADC$, $OE \\parallel DC$ (Theorem 6.2). So $AB \\parallel OE \\parallel DC$: $ABCD$ is a trapezium."]),
]
for p, text, steps in PROOFS62:
    q(f"ex6_2.{p}", "short_answer", 3, [BPT], ex("6.2", int(p[1:])), text, "hard" if p in ("q9", "q10") else "medium", answer_steps=steps, marking_scheme=MS3_PROOF)
# Exercise 6.3
q("ex6_3.q2", "short_answer", 3, [CRIT], ex("6.3", 2), "The lines $AC$ and $BD$ meet at $O$, and $\\triangle ODC \\sim \\triangle OBA$. If $\\angle BOC = 125^\\circ$ and $\\angle CDO = 70^\\circ$, find $\\angle DOC$, $\\angle DCO$ and $\\angle OAB$.",
  answer_steps=["$\\angle DOC = 180^\\circ - 125^\\circ = 55^\\circ$ (linear pair)", "$\\angle DCO = 180^\\circ - 70^\\circ - 55^\\circ = 55^\\circ$ (angle sum of $\\triangle ODC$)",
                "$\\angle OAB = \\angle OCD = 55^\\circ$ (corresponding angles of similar triangles)"],
  marking_scheme=["1 mark: $\\angle DOC$", "1 mark: $\\angle DCO$", "1 mark: $\\angle OAB$"], figure=dict(FIG_632))
PROOFS63 = [
 ("q3", 3, "Diagonals $AC$ and $BD$ of a trapezium $ABCD$ with $AB \\parallel DC$ intersect each other at the point $O$. Using a similarity criterion for two triangles, show that $\\dfrac{OA}{OC} = \\dfrac{OB}{OD}$.",
  ["In $\\triangle OAB$ and $\\triangle OCD$: $\\angle OAB = \\angle OCD$ and $\\angle OBA = \\angle ODC$ (alternate angles, $AB \\parallel DC$).", "So $\\triangle OAB \\sim \\triangle OCD$ (AA).", "Hence $\\dfrac{OA}{OC} = \\dfrac{OB}{OD}$."]),
 ("q4", 3, "$S$ is a point on side $QR$ of $\\triangle PQR$, and $T$ is a point on $QP$ produced beyond $P$. If $\\dfrac{QR}{QS} = \\dfrac{QT}{PR}$ and $\\angle PQR = \\angle PRQ$, show that $\\triangle PQS \\sim \\triangle TQR$.",
  ["$\\angle PQR = \\angle PRQ$, so $PQ = PR$ (sides opposite equal angles).", "Then $\\dfrac{QR}{QS} = \\dfrac{QT}{PQ}$, i.e. $\\dfrac{QP}{QT} = \\dfrac{QS}{QR}$, and $\\angle Q$ is common to both triangles.", "So $\\triangle PQS \\sim \\triangle TQR$ (SAS)."]),
 ("q5", 3, "$S$ and $T$ are points on sides $PR$ and $QR$ of $\\triangle PQR$ such that $\\angle P = \\angle RTS$. Show that $\\triangle RPQ \\sim \\triangle RTS$.",
  ["In $\\triangle RPQ$ and $\\triangle RTS$: $\\angle RPQ = \\angle RTS$ (given).", "$\\angle R$ is common to both triangles.", "So $\\triangle RPQ \\sim \\triangle RTS$ (AA)."]),
 ("q6", 3, "$D$ and $E$ are points on sides $AB$ and $AC$ of $\\triangle ABC$, and $\\triangle ABE \\cong \\triangle ACD$. Show that $\\triangle ADE \\sim \\triangle ABC$.",
  ["$\\triangle ABE \\cong \\triangle ACD$ gives $AB = AC$ and $AE = AD$ (CPCT).", "So $\\dfrac{AD}{AB} = \\dfrac{AE}{AC}$, and $\\angle A$ is common.", "Hence $\\triangle ADE \\sim \\triangle ABC$ (SAS)."]),
 ("q8", 3, "$E$ is a point on the side $AD$ produced of a parallelogram $ABCD$ and $BE$ intersects $CD$ at $F$. Show that $\\triangle ABE \\sim \\triangle CFB$.",
  ["$\\angle A = \\angle C$ (opposite angles of a parallelogram).", "$\\angle AEB = \\angle CBF$ (alternate angles, $AE \\parallel BC$).", "So $\\triangle ABE \\sim \\triangle CFB$ (AA)."]),
]
for p, marks, text, steps in PROOFS63:
    q(f"ex6_3.{p}", "short_answer", marks, [CRIT], ex("6.3", int(p[1:])), text, "hard" if p == "q4" else "medium", answer_steps=steps, marking_scheme=MS3_PROOF)
q("ex6_3.q7", "long_answer", 5, [CRIT], ex("6.3", 7), "Altitudes $AD$ and $CE$ of $\\triangle ABC$ intersect each other at the point $P$. Show that: (i) $\\triangle AEP \\sim \\triangle CDP$ (ii) $\\triangle ABD \\sim \\triangle CBE$ (iii) $\\triangle AEP \\sim \\triangle ADB$ (iv) $\\triangle PDC \\sim \\triangle BEC$", "hard",
  answer_steps=["(i) $\\angle AEP = \\angle CDP = 90^\\circ$ and $\\angle APE = \\angle CPD$ (vertically opposite), so $\\triangle AEP \\sim \\triangle CDP$ (AA).",
                "(ii) $\\angle ADB = \\angle CEB = 90^\\circ$ and $\\angle B$ is common, so $\\triangle ABD \\sim \\triangle CBE$ (AA).",
                "(iii) $\\angle AEP = \\angle ADB = 90^\\circ$ and $\\angle A$ ($\\angle PAE = \\angle BAD$) is common, so $\\triangle AEP \\sim \\triangle ADB$ (AA).",
                "(iv) $\\angle PDC = \\angle BEC = 90^\\circ$ and $\\angle C$ ($\\angle PCD = \\angle BCE$) is common, so $\\triangle PDC \\sim \\triangle BEC$ (AA)."],
  marking_scheme=["1 mark: figure", "1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)", "1 mark: (iv)"], figure=dict(FIG_637))
q("ex6_3.q9", "short_answer", 3, [CRIT], ex("6.3", 9), "$ABC$ and $AMP$ are two right triangles, right angled at $B$ and $M$ respectively, and they share the angle at $A$. Prove that: (i) $\\triangle ABC \\sim \\triangle AMP$ (ii) $\\dfrac{CA}{PA} = \\dfrac{BC}{MP}$",
  answer_steps=["(i) $\\angle ABC = \\angle AMP = 90^\\circ$ and $\\angle A$ is common.", "So $\\triangle ABC \\sim \\triangle AMP$ (AA).", "(ii) Corresponding sides of similar triangles are proportional: $\\dfrac{CA}{PA} = \\dfrac{BC}{MP}$."],
  marking_scheme=["1 mark: equal angles", "1 mark: similarity", "1 mark: ratio"])
q("ex6_3.q10", "long_answer", 5, [CRIT], ex("6.3", 10), "$CD$ and $GH$ are respectively the bisectors of $\\angle ACB$ and $\\angle EGF$ such that $D$ and $H$ lie on sides $AB$ and $FE$ of $\\triangle ABC$ and $\\triangle EFG$ respectively. If $\\triangle ABC \\sim \\triangle FEG$, show that: (i) $\\dfrac{CD}{GH} = \\dfrac{AC}{FG}$ (ii) $\\triangle DCB \\sim \\triangle HGE$ (iii) $\\triangle DCA \\sim \\triangle HGF$", "hard",
  answer_steps=["$\\triangle ABC \\sim \\triangle FEG$ gives $\\angle A = \\angle F$, $\\angle B = \\angle E$ and $\\angle ACB = \\angle FGE$, so $\\angle ACD = \\angle FGH$ and $\\angle DCB = \\angle HGE$ (halves of equal angles).",
                "(iii) In $\\triangle DCA$ and $\\triangle HGF$: $\\angle A = \\angle F$ and $\\angle ACD = \\angle FGH$, so $\\triangle DCA \\sim \\triangle HGF$ (AA).",
                "(i) From (iii), $\\dfrac{CD}{GH} = \\dfrac{AC}{FG}$.",
                "(ii) In $\\triangle DCB$ and $\\triangle HGE$: $\\angle B = \\angle E$ and $\\angle DCB = \\angle HGE$, so $\\triangle DCB \\sim \\triangle HGE$ (AA)."],
  marking_scheme=["1 mark: equal half-angles", "2 marks: (iii) with reasons", "1 mark: (i)", "1 mark: (ii)"])
q("ex6_3.q11", "short_answer", 3, [CRIT], ex("6.3", 11), "$E$ is a point on side $CB$ produced of an isosceles triangle $ABC$ with $AB = AC$. If $AD \\perp BC$ and $EF \\perp AC$, prove that $\\triangle ABD \\sim \\triangle ECF$.",
  answer_steps=["$AB = AC$, so $\\angle ABD = \\angle ECF$ (angles opposite equal sides; $\\angle ABC = \\angle ACB$).", "$\\angle ADB = \\angle EFC = 90^\\circ$.", "So $\\triangle ABD \\sim \\triangle ECF$ (AA)."], marking_scheme=MS3_PROOF)
q("ex6_3.q12", "long_answer", 5, [CRIT], ex("6.3", 12), "Sides $AB$ and $BC$ and median $AD$ of $\\triangle ABC$ are respectively proportional to sides $PQ$ and $QR$ and median $PM$ of $\\triangle PQR$. Show that $\\triangle ABC \\sim \\triangle PQR$.", "hard",
  answer_steps=["Given $\\dfrac{AB}{PQ} = \\dfrac{BC}{QR} = \\dfrac{AD}{PM}$.", "$BD = \\dfrac{1}{2}BC$ and $QM = \\dfrac{1}{2}QR$ (medians), so $\\dfrac{BD}{QM} = \\dfrac{BC}{QR}$.",
                "So $\\dfrac{AB}{PQ} = \\dfrac{BD}{QM} = \\dfrac{AD}{PM}$, and $\\triangle ABD \\sim \\triangle PQM$ (SSS).", "Hence $\\angle B = \\angle Q$.",
                "In $\\triangle ABC$ and $\\triangle PQR$: $\\dfrac{AB}{PQ} = \\dfrac{BC}{QR}$ and $\\angle B = \\angle Q$, so $\\triangle ABC \\sim \\triangle PQR$ (SAS)."],
  marking_scheme=["1 mark: halves of the bases", "1 mark: SSS for the small triangles", "1 mark: $\\angle B = \\angle Q$", "2 marks: SAS conclusion"])
q("ex6_3.q13", "short_answer", 3, [CRIT], ex("6.3", 13), "$D$ is a point on the side $BC$ of a triangle $ABC$ such that $\\angle ADC = \\angle BAC$. Show that $CA^{2} = CB \\cdot CD$.",
  answer_steps=["In $\\triangle ADC$ and $\\triangle BAC$: $\\angle ADC = \\angle BAC$ (given) and $\\angle C$ is common.", "So $\\triangle ADC \\sim \\triangle BAC$ (AA).", "$\\dfrac{CA}{CB} = \\dfrac{CD}{CA}$, so $CA^{2} = CB \\cdot CD$."], marking_scheme=MS3_PROOF)
q("ex6_3.q14", "long_answer", 5, [CRIT], ex("6.3", 14), "Sides $AB$ and $AC$ and median $AD$ of a triangle $ABC$ are respectively proportional to sides $PQ$ and $PR$ and median $PM$ of another triangle $PQR$. Show that $\\triangle ABC \\sim \\triangle PQR$.", "hard",
  answer_steps=["Produce $AD$ to $E$ so that $DE = AD$, and $PM$ to $L$ so that $ML = PM$. Join $CE$ and $RL$.",
                "$\\triangle ABD \\cong \\triangle ECD$ (SAS: $BD = CD$, $AD = ED$, vertically opposite angles), so $CE = AB$. Similarly $RL = PQ$.",
                "Given $\\dfrac{AB}{PQ} = \\dfrac{AC}{PR} = \\dfrac{AD}{PM}$, so $\\dfrac{CE}{RL} = \\dfrac{AC}{PR} = \\dfrac{AE}{PL}$ and $\\triangle AEC \\sim \\triangle PLR$ (SSS). So $\\angle CAE = \\angle RPL$.",
                "Similarly $\\triangle ABE \\sim \\triangle PQL$ gives $\\angle BAE = \\angle QPL$, so $\\angle BAC = \\angle QPR$ (adding).",
                "In $\\triangle ABC$ and $\\triangle PQR$: $\\dfrac{AB}{PQ} = \\dfrac{AC}{PR}$ and $\\angle A = \\angle P$, so $\\triangle ABC \\sim \\triangle PQR$ (SAS)."],
  marking_scheme=["1 mark: construction", "1 mark: congruent triangles", "1 mark: first similarity", "1 mark: $\\angle A = \\angle P$", "1 mark: SAS conclusion"])
q("ex6_3.q15", "short_answer", 3, [APPL, CRIT], ex("6.3", 15), "A vertical pole of length 6 m casts a shadow 4 m long on the ground and at the same time a tower casts a shadow 28 m long. Find the height of the tower.", "easy",
  answer_steps=["Both make right angles with the ground, and the sun's rays make equal angles with the ground at the same time, so the triangles are similar (AA).",
                "$\\dfrac{h}{6} = \\dfrac{28}{4}$", "$h = 42$: the tower is 42 m high."],
  marking_scheme=["1 mark: similarity with reason", "1 mark: proportion", "1 mark: answer"], figure=dict(FIG_SHADOW))
q("ex6_3.q16", "short_answer", 3, [CRIT], ex("6.3", 16), "If $AD$ and $PM$ are medians of triangles $ABC$ and $PQR$, respectively, where $\\triangle ABC \\sim \\triangle PQR$, prove that $\\dfrac{AB}{PQ} = \\dfrac{AD}{PM}$.",
  answer_steps=["$\\triangle ABC \\sim \\triangle PQR$ gives $\\angle B = \\angle Q$ and $\\dfrac{AB}{PQ} = \\dfrac{BC}{QR} = \\dfrac{2BD}{2QM} = \\dfrac{BD}{QM}$.", "So $\\triangle ABD \\sim \\triangle PQM$ (SAS).",
                "Hence $\\dfrac{AB}{PQ} = \\dfrac{AD}{PM}$."], marking_scheme=MS3_PROOF)
# NCERT examples
q("eg_bpt_ratio", "short_answer", 3, [BPT], {"kind": "ncert_example"}, "If a line intersects sides $AB$ and $AC$ of a $\\triangle ABC$ at $D$ and $E$ respectively and is parallel to $BC$, prove that $\\dfrac{AD}{AB} = \\dfrac{AE}{AC}$.",
  answer_steps=["$DE \\parallel BC$, so $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$ (Theorem 6.1), i.e. $\\dfrac{DB}{AD} = \\dfrac{EC}{AE}$.", "Adding 1: $\\dfrac{DB + AD}{AD} = \\dfrac{EC + AE}{AE}$, i.e. $\\dfrac{AB}{AD} = \\dfrac{AC}{AE}$.", "So $\\dfrac{AD}{AB} = \\dfrac{AE}{AC}$."],
  marking_scheme=MS3_PROOF)
q("eg_trapezium", "short_answer", 3, [BPT], {"kind": "ncert_example"}, "$ABCD$ is a trapezium with $AB \\parallel DC$. $E$ and $F$ are points on the non-parallel sides $AD$ and $BC$ respectively such that $EF$ is parallel to $AB$. Show that $\\dfrac{AE}{ED} = \\dfrac{BF}{FC}$.", "hard",
  answer_steps=["Join $AC$, meeting $EF$ at $G$. In $\\triangle ADC$, $EG \\parallel DC$, so $\\dfrac{AE}{ED} = \\dfrac{AG}{GC}$.", "In $\\triangle CAB$, $GF \\parallel AB$, so $\\dfrac{CG}{GA} = \\dfrac{CF}{FB}$, i.e. $\\dfrac{AG}{GC} = \\dfrac{BF}{FC}$.", "Hence $\\dfrac{AE}{ED} = \\dfrac{BF}{FC}$."],
  marking_scheme=MS3_PROOF)
# Shine MCQs
mcq("mcq01", [BPT], "In $\\triangle ABC$, $DE \\parallel BC$, $AD = 2$ cm, $DB = 3$ cm and $AE = 4$ cm. Then $EC$ is:", ["$6$ cm", "$\\dfrac{8}{3}$ cm", "$1.5$ cm", "$5$ cm"], 0,
    "$\\dfrac{2}{3} = \\dfrac{4}{EC}$ gives $EC = 6$ cm.")
mcq("mcq02", [CRIT], "$\\triangle ABC \\sim \\triangle PQR$ with $\\dfrac{AB}{PQ} = \\dfrac{2}{3}$. If $BC = 8$ cm, then $QR$ is:", ["$12$ cm", "$\\dfrac{16}{3}$ cm", "$10$ cm", "$24$ cm"], 0,
    "$\\dfrac{BC}{QR} = \\dfrac{2}{3}$, so $QR = 8 \\times \\dfrac{3}{2} = 12$ cm.")
mcq("mcq03", [SIMF], "Which pair of figures is always similar?", ["two squares", "two rectangles", "two rhombuses", "two isosceles triangles"], 0,
    "Squares always have equal angles and proportional sides; the others can differ in angles or in side ratios.")
mcq("mcq04", [CRIT], "If $\\triangle ABC \\sim \\triangle DEF$, $\\angle A = 50^\\circ$ and $\\angle E = 60^\\circ$, then $\\angle C$ is:", ["$70^\\circ$", "$60^\\circ$", "$50^\\circ$", "$110^\\circ$"], 0,
    "$\\angle B = \\angle E = 60^\\circ$, so $\\angle C = 180^\\circ - 50^\\circ - 60^\\circ = 70^\\circ$.")
mcq("mcq05", [CRIT], "Triangles with sides 3 cm, 4 cm, 5 cm and 6 cm, 8 cm, 10 cm are similar by:", ["SSS", "SAS", "AAA", "RHS"], 0, "All three sides are in the ratio $1 : 2$.")
mcq("mcq06", [BPT], "In $\\triangle ABC$, $D$ and $E$ are points on $AB$ and $AC$ with $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$. Then:", ["$DE \\parallel BC$", "$DE \\perp BC$", "$DE = BC$", "$AD = AE$"], 0,
    "By the converse of the Basic Proportionality Theorem, $DE \\parallel BC$.")
mcq("mcq07", [APPL], "A girl 1.5 m tall casts a shadow 2 m long. At the same time a tree casts a shadow 12 m long. The height of the tree is:", ["$9$ m", "$16$ m", "$8$ m", "$10$ m"], 0,
    "$\\dfrac{h}{1.5} = \\dfrac{12}{2}$, so $h = 9$ m.", "medium")
mcq("mcq08", [CRIT], "If $\\triangle ABC \\sim \\triangle PQR$, which of these is true?",
    ["$\\dfrac{AB}{PQ} = \\dfrac{AC}{PR}$", "$\\dfrac{AB}{PR} = \\dfrac{BC}{QR}$", "$\\dfrac{AB}{QR} = \\dfrac{AC}{PQ}$", "$\\dfrac{AB}{PQ} = \\dfrac{AC}{QR}$"], 0,
    "$A \\leftrightarrow P$, $B \\leftrightarrow Q$, $C \\leftrightarrow R$, so $AB \\leftrightarrow PQ$ and $AC \\leftrightarrow PR$.", "medium")
mcq("mcq09", [BPT], "In $\\triangle ABC$, $DE \\parallel BC$, $\\dfrac{AD}{DB} = \\dfrac{3}{5}$ and $AE = 6$ cm. Then $AC$ is:", ["$16$ cm", "$10$ cm", "$18$ cm", "$14$ cm"], 0,
    "$\\dfrac{AE}{EC} = \\dfrac{3}{5}$ gives $EC = 10$ cm, so $AC = 6 + 10 = 16$ cm.", "medium")
mcq("mcq10", [CRIT], "If the corresponding angles of two triangles are equal, the triangles are similar. This is the criterion:", ["AAA", "SSS", "SAS", "ASA"], 0, "Equal corresponding angles: the AAA criterion.")
mcq("mcq11", [CRIT], "$\\triangle ABC \\sim \\triangle DEF$, $AB = 4$ cm, $DE = 6$ cm and the perimeter of $\\triangle ABC$ is 18 cm. The perimeter of $\\triangle DEF$ is:", ["$27$ cm", "$12$ cm", "$24$ cm", "$36$ cm"], 0,
    "Perimeters are in the same ratio as the sides: $18 \\times \\dfrac{6}{4} = 27$ cm.", "medium")
mcq("mcq12", [SIMF], "Which statement is true?", ["All congruent figures are similar.", "All similar figures are congruent.", "Similar figures always have equal areas.", "Two rectangles are always similar."], 0,
    "Congruent figures have the same shape and size, so they are similar; similar figures can differ in size.")
mcq("sqp14", [CRIT], "If $\\triangle ABC \\sim \\triangle DEF$, $AB = 6$ cm, $DE = 9$ cm, $EF = 6$ cm and $FD = 12$ cm, then the perimeter of $\\triangle ABC$ is",
    ["$28$ cm", "$28.5$ cm", "$18$ cm", "$23$ cm"], 2, "Perimeter of $\\triangle DEF = 27$ cm; the ratio is $\\dfrac{6}{9} = \\dfrac{2}{3}$, so the perimeter of $\\triangle ABC = 18$ cm.", "medium", source=SQP(14))

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [BPT], "In $\\triangle ABC$, $DE \\parallel BC$ with $AD = 2$ cm, $DB = 4$ cm and $AE = 3$ cm. Then $EC = 6$ cm.", "A line parallel to one side of a triangle divides the other two sides in the same ratio.", 0,
   "$\\dfrac{2}{4} = \\dfrac{3}{EC}$ gives $EC = 6$ cm, using exactly the theorem in R.")
ar("ar2", [SIMF], "Any two equilateral triangles are similar.", "Any two equilateral triangles are congruent.", 2, "A is true (all angles are $60^\\circ$). R is false: their sides can be of different lengths.")
ar("ar3", [SIMF], "A square and a rhombus with an angle of $60^\\circ$ are similar.", "The sides of a square and of a rhombus are proportional.", 3,
   "A is false: their angles are not equal. R is true: all four sides of each are equal.")
ar("ar4", [CRIT], "Triangles with sides 2 cm, 3 cm, 4 cm and 4 cm, 6 cm, 8 cm are similar.", "If the corresponding sides of two triangles are in the same ratio, the triangles are similar.", 0,
   "$\\dfrac{2}{4} = \\dfrac{3}{6} = \\dfrac{4}{8}$, so they are similar by SSS, which is R.")
ar("ar5", [SIMF], "Two congruent triangles are similar.", "The sum of the angles of a triangle is $180^\\circ$.", 1,
   "Both are true, but A holds because congruent triangles have the same shape, not because of the angle sum.")

q("vsa1", "very_short_answer", 2, [BPT], SHINE, "In $\\triangle ABC$, $DE \\parallel BC$ with $D$ on $AB$ and $E$ on $AC$. If $\\dfrac{AD}{DB} = \\dfrac{3}{4}$ and $AC = 14$ cm, find $AE$.",
  answer_steps=["$\\dfrac{AE}{EC} = \\dfrac{3}{4}$ (Theorem 6.1), so $AE = \\dfrac{3}{7} \\times AC$.", "$AE = \\dfrac{3}{7} \\times 14 = 6$ cm"], marking_scheme=MS2_NUM)
q("vsa2", "very_short_answer", 2, [CRIT], SHINE, "If $\\triangle ABC \\sim \\triangle PQR$, $\\angle A = 32^\\circ$ and $\\angle R = 65^\\circ$, find $\\angle B$.", "easy",
  answer_steps=["$\\angle C = \\angle R = 65^\\circ$ (corresponding angles).", "$\\angle B = 180^\\circ - 32^\\circ - 65^\\circ = 83^\\circ$"], marking_scheme=["1 mark: $\\angle C = 65^\\circ$", "1 mark: answer"])
q("sqp23", "very_short_answer", 2, [CRIT], SQP(23), "If $AP$ and $DQ$ are medians of triangles $ABC$ and $DEF$ respectively, where $\\triangle ABC \\sim \\triangle DEF$, then prove that $\\dfrac{AB}{DE} = \\dfrac{AP}{DQ}$.",
  answer_steps=["$\\triangle ABC \\sim \\triangle DEF$ gives $\\angle B = \\angle E$ and $\\dfrac{AB}{DE} = \\dfrac{BC}{EF} = \\dfrac{2BP}{2EQ} = \\dfrac{BP}{EQ}$.", "So $\\triangle ABP \\sim \\triangle DEQ$ (SAS), and $\\dfrac{AB}{DE} = \\dfrac{AP}{DQ}$."],
  marking_scheme=["1 mark: $\\dfrac{AB}{DE} = \\dfrac{BP}{EQ}$ with $\\angle B = \\angle E$", "1 mark: SAS and conclusion"])
q("sa1", "short_answer", 3, [BPT], SHINE, "In $\\triangle ABC$, $D$ and $E$ are points on $AB$ and $AC$ such that $DE \\parallel BC$. If $AD = x$, $DB = x - 2$, $AE = x + 2$ and $EC = x - 1$, find $x$.", "hard",
  answer_steps=["$\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$: $\\dfrac{x}{x - 2} = \\dfrac{x + 2}{x - 1}$", "$x(x - 1) = (x + 2)(x - 2)$, i.e. $x^{2} - x = x^{2} - 4$", "$x = 4$"],
  marking_scheme=["1 mark: proportion", "1 mark: simplifying", "1 mark: $x = 4$"])
q("sa2", "short_answer", 3, [CRIT], SHINE, "$\\triangle ABC \\sim \\triangle DEF$ with $AB = 3$ cm, $BC = 4$ cm and $CA = 5$ cm. If $DE = 6$ cm, find $EF$, $FD$ and the perimeter of $\\triangle DEF$.", "easy",
  answer_steps=["The ratio is $\\dfrac{DE}{AB} = \\dfrac{6}{3} = 2$.", "$EF = 2 \\times 4 = 8$ cm and $FD = 2 \\times 5 = 10$ cm.", "Perimeter $= 6 + 8 + 10 = 24$ cm"],
  marking_scheme=["1 mark: ratio", "1 mark: sides", "1 mark: perimeter"])
q("sa3", "short_answer", 3, [BPT, CRIT], SHINE, "In $\\triangle PQR$, $S$ and $T$ are points on $PQ$ and $PR$ such that $ST \\parallel QR$. If $PS = 4$ cm, $SQ = 6$ cm and $ST = 3.2$ cm, find $QR$.",
  answer_steps=["$ST \\parallel QR$, so $\\angle PST = \\angle PQR$ and $\\angle PTS = \\angle PRQ$ (corresponding angles): $\\triangle PST \\sim \\triangle PQR$ (AA).", "$\\dfrac{ST}{QR} = \\dfrac{PS}{PQ} = \\dfrac{4}{10}$",
                "$QR = 3.2 \\times \\dfrac{10}{4} = 8$ cm"], marking_scheme=["1 mark: similarity", "1 mark: proportion", "1 mark: answer"])
q("sqp33", "long_answer", 5, [BPT], SQP(33),
  "Prove that if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio. Hence, in $\\triangle PQR$, a line $\\ell$ intersects the sides $PQ$ and $PR$ at $L$ and $M$ respectively such that $LM \\parallel QR$. If $PL = 5.7$ cm, $PQ = 15.2$ cm and $MR = 5.5$ cm, find the length of $PM$ (in cm).", "hard",
  answer_steps=["Given $\\triangle ABC$ with $DE \\parallel BC$, $D$ on $AB$, $E$ on $AC$. To prove $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$. Join $BE$, $CD$; draw $DM \\perp AC$ and $EN \\perp AB$.",
                "$\\dfrac{\\text{ar}(ADE)}{\\text{ar}(BDE)} = \\dfrac{\\frac{1}{2} AD \\cdot EN}{\\frac{1}{2} DB \\cdot EN} = \\dfrac{AD}{DB}$ and $\\dfrac{\\text{ar}(ADE)}{\\text{ar}(DEC)} = \\dfrac{AE}{EC}$.",
                "$\\text{ar}(BDE) = \\text{ar}(DEC)$ (same base $DE$, between the same parallels), so $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
                "In $\\triangle PQR$, $LM \\parallel QR$: $\\dfrac{PL}{LQ} = \\dfrac{PM}{MR}$, with $LQ = 15.2 - 5.7 = 9.5$ cm.", "$\\dfrac{5.7}{9.5} = \\dfrac{PM}{5.5}$, so $PM = 3.3$ cm."],
  marking_scheme=["2 marks: given, figure and construction", "2 marks: correct proof", "1 mark: $PM = 3.3$ cm"], figure=dict(FIG_BPT_PROOF))
q("la1", "long_answer", 5, [BPT], SHINE, "State and prove the Basic Proportionality Theorem. Using it, find $AE$ if in $\\triangle ABC$, $DE \\parallel BC$, $\\dfrac{AD}{DB} = \\dfrac{2}{3}$ and $AC = 18$ cm.", "hard",
  answer_steps=["Statement: if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.",
                "Proof: join $BE$ and $CD$, draw $EN \\perp AB$ and $DM \\perp AC$; then $\\dfrac{\\text{ar}(ADE)}{\\text{ar}(BDE)} = \\dfrac{AD}{DB}$ and $\\dfrac{\\text{ar}(ADE)}{\\text{ar}(DEC)} = \\dfrac{AE}{EC}$.",
                "$\\text{ar}(BDE) = \\text{ar}(DEC)$ (same base, same parallels), so $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.",
                "Here $\\dfrac{AE}{EC} = \\dfrac{2}{3}$, so $AE = \\dfrac{2}{5} \\times AC$.", "$AE = \\dfrac{2}{5} \\times 18 = 7.2$ cm"],
  marking_scheme=["1 mark: statement", "2 marks: proof", "1 mark: proportion", "1 mark: answer"])
q("cb1", "case_based", 4, [APPL, CRIT], SHINE,
  "At 4 pm, a student 1.2 m tall casts a shadow 0.9 m long, while the school flagpole casts a shadow 6 m long.\n\n(i) Which criterion shows that the two triangles are similar? (1)\n\n(ii) Find the height of the flagpole. (1)\n\n(iii) At the same time, a building casts a shadow 15 m long. Find its height. OR How long is the shadow of a 4 m tall tree at that time? (2)",
  answer_steps=["(i) AA: both have a right angle, and the sun's rays make the same angle with the ground.", "(ii) $\\dfrac{h}{1.2} = \\dfrac{6}{0.9}$, so $h = 8$ m.",
                "(iii) $\\dfrac{H}{1.2} = \\dfrac{15}{0.9}$, so $H = 20$ m. OR $\\dfrac{s}{0.9} = \\dfrac{4}{1.2}$, so $s = 3$ m."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [BPT, CRIT], SHINE,
  "A roof frame is a triangle $ABC$ with a horizontal beam $DE$ parallel to the base $BC$, where $D$ is on $AB$ and $E$ is on $AC$. $AB = 6$ m, $AD = 2$ m and $BC = 9$ m.\n\n(i) Why is $\\triangle ADE \\sim \\triangle ABC$? (1)\n\n(ii) Find the length of the beam $DE$. (1)\n\n(iii) If $AE = 2.5$ m, find $AC$. OR If $AE = 2.5$ m, find $EC$. (2)",
  answer_steps=["(i) $DE \\parallel BC$, so $\\angle ADE = \\angle ABC$ and $\\angle AED = \\angle ACB$ (corresponding angles): AA.", "(ii) $\\dfrac{DE}{BC} = \\dfrac{AD}{AB} = \\dfrac{2}{6}$, so $DE = 3$ m.",
                "(iii) $\\dfrac{AE}{AC} = \\dfrac{1}{3}$, so $AC = 7.5$ m. OR $\\dfrac{AE}{EC} = \\dfrac{AD}{DB} = \\dfrac{2}{4}$, so $EC = 5$ m."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch06.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
        return
    shift = sum(map(ord, item["id"])) % len(opts)
    correct = opts[item["correct_index"]]
    item["options"] = opts[shift:] + opts[:shift]
    item["correct_index"] = item["options"].index(correct)
for it in Q: spread(it)
for sec in sections:
    for blk in sec["blocks"]: spread(blk)
for it in Q:
    if "figure" in it: it["figure"].pop("id", None)
print("answer positions:", Counter(it["correct_index"] for it in Q if it["type"] == "mcq"))
os.makedirs(os.path.join(ROOT, PATH), exist_ok=True)
for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": CH_ID, "questions": Q})]:
    with open(os.path.join(ROOT, PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
print(f"blocks={sum(len(s['blocks']) for s in sections)} questions={len(Q)} ncert_exercise_items={sum(1 for it in Q if it['source']['kind'] == 'ncert_exercise')}")
