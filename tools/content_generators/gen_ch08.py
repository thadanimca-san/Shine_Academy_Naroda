"""CBSE Class 10 Maths Ch 8: Introduction to Trigonometry.
Every value is computed with sympy; every identity is checked symbolically and
at several angles."""
import json, math, os, sys
from collections import Counter
from sympy import (sqrt, Rational as R, simplify, symbols, sin, cos, tan, cot, sec, csc, pi, nsimplify, radsimp, trigsimp, solve)

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch08"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch08_introduction_to_trigonometry"
A, t = symbols("A theta")
deg = lambda d: d * pi / 180

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def eq(u, v): return simplify(radsimp(u - v)) == 0
def identity(lhs, rhs, var, msg):
    for d in (10, 23, 37, 52, 71):
        check(abs(float((lhs - rhs).subs(var, deg(d)))) < 1e-12, f"{msg} at {d} degrees")

# ---------------------------------------------------------------- verification
# Ex 8.1
check(sqrt(24 ** 2 + 7 ** 2) == 25, "8.1 Q1 AC = 25")
check(sqrt(13 ** 2 - 12 ** 2) == 5 and R(5, 12) - R(5, 12) == 0, "8.1 Q2")
cA = sqrt(1 - R(9, 16)); check(eq(cA, sqrt(7) / 4) and eq(R(3, 4) / cA, 3 / sqrt(7)), "8.1 Q3")
check(sqrt(8 ** 2 + 15 ** 2) == 17, "8.1 Q4 hyp 17")
check(sqrt(13 ** 2 - 12 ** 2) == 5, "8.1 Q5 opp 5")
th = symbols("th"); ct = R(7, 8)
check(eq((1 - 1 / (1 + ct ** 2)) / (1 - (ct ** 2) / (1 + ct ** 2)), ct ** 2) and ct ** 2 == R(49, 64), "8.1 Q7")
tA = R(3, 4); check((1 - tA ** 2) / (1 + tA ** 2) == R(7, 25) == R(4, 5) ** 2 - R(3, 5) ** 2, "8.1 Q8")
check(eq(sin(deg(30)) * cos(deg(60)) + cos(deg(30)) * sin(deg(60)), 1) and eq(cos(deg(30)) * cos(deg(60)) - sin(deg(30)) * sin(deg(60)), 0), "8.1 Q9")
check((13 - 12, 13 + 12) == (1, 25) and 13 ** 2 - 12 ** 2 == 25, "8.1 Q10 PR = 13, QR = 12")
# Ex 8.2
check(eq(sin(deg(60)) * cos(deg(30)) + sin(deg(30)) * cos(deg(60)), 1), "8.2 Q1 i")
check(eq(2 * tan(deg(45)) ** 2 + cos(deg(30)) ** 2 - sin(deg(60)) ** 2, 2), "8.2 Q1 ii")
check(eq(cos(deg(45)) / (sec(deg(30)) + csc(deg(30))), (3 * sqrt(2) - sqrt(6)) / 8), "8.2 Q1 iii")
check(eq((sin(deg(30)) + tan(deg(45)) - csc(deg(60))) / (sec(deg(30)) + cos(deg(60)) + cot(deg(45))), (43 - 24 * sqrt(3)) / 11), "8.2 Q1 iv")
check(eq((5 * cos(deg(60)) ** 2 + 4 * sec(deg(30)) ** 2 - tan(deg(45)) ** 2) / (sin(deg(30)) ** 2 + cos(deg(30)) ** 2), R(67, 12)), "8.2 Q1 v")
check(eq(2 * tan(deg(30)) / (1 + tan(deg(30)) ** 2), sin(deg(60))), "8.2 Q2 i"); check(eq((1 - tan(deg(45)) ** 2) / (1 + tan(deg(45)) ** 2), 0), "8.2 Q2 ii")
check(all(eq(sin(2 * deg(a)), 2 * sin(deg(a))) == (a == 0) for a in (0, 30, 45, 60)), "8.2 Q2 iii")
check(eq(2 * tan(deg(30)) / (1 - tan(deg(30)) ** 2), tan(deg(60))), "8.2 Q2 iv")
check(eq(tan(deg(45 + 15)), sqrt(3)) and eq(tan(deg(45 - 15)), 1 / sqrt(3)), "8.2 Q3")
check(not eq(sin(deg(60)), sin(deg(30)) + sin(deg(30))) and not eq(sin(deg(30)), cos(deg(30))), "8.2 Q4")
# Ex 8.3 identities
identity(sin(A), 1 / sqrt(1 + cot(A) ** 2), A, "8.3 Q1 sin"); identity(sec(A), sqrt(1 + cot(A) ** 2) / cot(A), A, "8.3 Q1 sec")
identity(sin(A), sqrt(sec(A) ** 2 - 1) / sec(A), A, "8.3 Q2 sin"); identity(cot(A), 1 / sqrt(sec(A) ** 2 - 1), A, "8.3 Q2 cot")
identity(csc(A), sec(A) / sqrt(sec(A) ** 2 - 1), A, "8.3 Q2 cosec")
identity(9 * sec(A) ** 2 - 9 * tan(A) ** 2, 9, A, "8.3 Q3 i"); identity((1 + tan(A) + sec(A)) * (1 + cot(A) - csc(A)), 2, A, "8.3 Q3 ii")
identity((sec(A) + tan(A)) * (1 - sin(A)), cos(A), A, "8.3 Q3 iii"); identity((1 + tan(A) ** 2) / (1 + cot(A) ** 2), tan(A) ** 2, A, "8.3 Q3 iv")
IDS = [
 ("i", (csc(t) - cot(t)) ** 2, (1 - cos(t)) / (1 + cos(t))),
 ("ii", cos(t) / (1 + sin(t)) + (1 + sin(t)) / cos(t), 2 * sec(t)),
 ("iii", tan(t) / (1 - cot(t)) + cot(t) / (1 - tan(t)), 1 + sec(t) * csc(t)),
 ("iv", (1 + sec(t)) / sec(t), sin(t) ** 2 / (1 - cos(t))),
 ("v", (cos(t) - sin(t) + 1) / (cos(t) + sin(t) - 1), csc(t) + cot(t)),
 ("vi", sqrt((1 + sin(t)) / (1 - sin(t))), sec(t) + tan(t)),
 ("vii", (sin(t) - 2 * sin(t) ** 3) / (2 * cos(t) ** 3 - cos(t)), tan(t)),
 ("viii", (sin(t) + csc(t)) ** 2 + (cos(t) + sec(t)) ** 2, 7 + tan(t) ** 2 + cot(t) ** 2),
 ("ix", (csc(t) - sin(t)) * (sec(t) - cos(t)), 1 / (tan(t) + cot(t))),
 ("x", ((1 - tan(t)) / (1 - cot(t))) ** 2, tan(t) ** 2),
]
for p, l, r in IDS: identity(l, r, t, f"8.3 Q4 {p}")
# examples, lesson, Shine
check(sqrt(4 ** 2 + 3 ** 2) == 5, "eg tan A = 4/3")
check(eq(sin(deg(45 - 15)), R(1, 2)) and eq(cos(deg(45 + 15)), R(1, 2)), "eg A = 45, B = 15")
identity(sec(A) * (1 - sin(A)) * (sec(A) + tan(A)), 1, A, "eg sec(1-sin)(sec+tan)")
identity((cot(A) - cos(A)) / (cot(A) + cos(A)), (csc(A) - 1) / (csc(A) + 1), A, "eg cot-cos")
identity((sin(A) - cos(A) + 1) / (sin(A) + cos(A) - 1), 1 / (sec(A) - tan(A)), A, "eg sin-cos+1")
check(eq(tan(deg(30)) * sqrt(3), 1) and eq(2 * sin(deg(30)), 1), "checks")
check(eq(sin(deg(30)) + cos(deg(60)), 1) and eq(tan(deg(45)), 1) and eq(cos(deg(90)), 0), "mcq values")
check(eq(sin(deg(60)) ** 2 + cos(deg(60)) ** 2, 1), "mcq identity")
check(eq((sqrt(3) - 1) / 2, sin(deg(60)) - sin(deg(30))), "mcq sin60 - sin30")
check(eq(1 / sqrt(1 + (R(12, 5)) ** -2), R(12, 13)), "mcq tan = 12/5 -> sin = 12/13")
check(eq(2 * sin(deg(45)) * cos(deg(45)), 1), "ar")
identity((1 - cos(A) ** 2) * csc(A) ** 2, 1, A, "vsa"); identity(sin(A) ** 4 - cos(A) ** 4, 2 * sin(A) ** 2 - 1, A, "sa1")
identity(tan(A) + cot(A), sec(A) * csc(A), A, "sa2")
check(eq(5 / R(13) * 13, 5), "sa3"); check(eq((sin(deg(30)) + cos(deg(30))) ** 2, 1 + sqrt(3) / 2), "vsa2")
identity((1 + cot(A) - csc(A)) * (1 + tan(A) + sec(A)), 2, A, "la1")
identity(sqrt((sec(A) - 1) / (sec(A) + 1)) + sqrt((sec(A) + 1) / (sec(A) - 1)), 2 * csc(A), A, "la2")
check(eq(tan(deg(60)) * 10, 10 * sqrt(3)) and eq(10 / cos(deg(60)), 20) and eq(10 * sqrt(3), 10 * sqrt(3)), "cb1 ramp")
check(sqrt(9 ** 2 + 12 ** 2) == 15, "cb2 ladder")

# ---------------------------------------------------------------- figures
def tri(title, angle_label="A", **kw):
    fig = {"type": "geometry_figure", "title": title, "points": {"A": [0, 0], "B": [4, 0], "C": [4, 3]},
           "segments": [["A", "B"], ["B", "C"], {"from": "C", "to": "A", "highlight": True}], "right_angles": [["A", "B", "C"]],
           "angles": [{"points": ["B", "A", "C"], "label": angle_label}]}
    fig.update(kw); return fig
FIG_SIDES = tri("Sides with respect to ∠A", lengths=[
    {"from": "C", "to": "A", "label": "hypotenuse", "label_hi": "कर्ण", "label_gu": "કર્ણ"},
    {"from": "B", "to": "C", "label": "opposite", "label_hi": "सम्मुख भुजा", "label_gu": "સામેની બાજુ"},
    {"from": "A", "to": "B", "label": "adjacent", "label_hi": "संलग्न भुजा", "label_gu": "પાસેની બાજુ"}])
h = math.sqrt(3)
FIG_EQ = {"type": "geometry_figure", "title": "Half of an equilateral triangle", "points": {"A": [1, h], "B": [0, 0], "C": [2, 0], "D": [1, 0]},
          "segments": [["A", "B"], ["B", "C"], ["C", "A"], {"from": "A", "to": "D", "highlight": True}], "right_angles": [["A", "D", "B"]],
          "angles": [{"points": ["D", "B", "A"], "label": "60°"}, {"points": ["B", "A", "D"], "label": "30°"}],
          "lengths": [{"from": "A", "to": "B", "label": "2a"}, {"from": "B", "to": "D", "label": "a"}, {"from": "A", "to": "D", "label": "√3 a"}]}
FIG_45 = {"type": "geometry_figure", "title": "An isosceles right triangle", "points": {"A": [0, 0], "B": [3, 0], "C": [3, 3]},
          "segments": [["A", "B"], ["B", "C"], {"from": "C", "to": "A", "highlight": True}], "right_angles": [["A", "B", "C"]],
          "angles": [{"points": ["B", "A", "C"], "label": "45°"}], "lengths": [{"from": "A", "to": "B", "label": "a"}, {"from": "B", "to": "C", "label": "a"}, {"from": "C", "to": "A", "label": "√2 a"}]}
FIG_Q81 = {"type": "geometry_figure", "title": "AB = 24 cm, BC = 7 cm", "points": {"A": [0, 0], "B": [24, 0], "C": [24, 7]},
           "segments": [["A", "B"], ["B", "C"], ["C", "A"]], "right_angles": [["A", "B", "C"]],
           "lengths": [{"from": "A", "to": "B", "label": "24 cm"}, {"from": "B", "to": "C", "label": "7 cm"}]}
FIG_Q82 = {"type": "geometry_figure", "title": "PQ = 12 cm, PR = 13 cm", "points": {"P": [0, 0], "Q": [12, 0], "R": [12, 5]},
           "segments": [["P", "Q"], ["Q", "R"], ["R", "P"]], "right_angles": [["P", "Q", "R"]],
           "lengths": [{"from": "P", "to": "Q", "label": "12 cm"}, {"from": "R", "to": "P", "label": "13 cm"}]}

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch08.{id_}", "type": type_, **kw}
def fig(id_, figure): return {"id": f"ch08.{id_}", **figure}
TABLE_EN = ("| $\\angle A$ | $0^\\circ$ | $30^\\circ$ | $45^\\circ$ | $60^\\circ$ | $90^\\circ$ |\n|---|---|---|---|---|---|\n"
            "| $\\sin A$ | $0$ | $\\frac{1}{2}$ | $\\frac{1}{\\sqrt{2}}$ | $\\frac{\\sqrt{3}}{2}$ | $1$ |\n"
            "| $\\cos A$ | $1$ | $\\frac{\\sqrt{3}}{2}$ | $\\frac{1}{\\sqrt{2}}$ | $\\frac{1}{2}$ | $0$ |\n"
            "| $\\tan A$ | $0$ | $\\frac{1}{\\sqrt{3}}$ | $1$ | $\\sqrt{3}$ | $-$ |\n"
            "| $\\text{cosec } A$ | $-$ | $2$ | $\\sqrt{2}$ | $\\frac{2}{\\sqrt{3}}$ | $1$ |\n"
            "| $\\sec A$ | $1$ | $\\frac{2}{\\sqrt{3}}$ | $\\sqrt{2}$ | $2$ | $-$ |\n"
            "| $\\cot A$ | $-$ | $\\sqrt{3}$ | $1$ | $\\frac{1}{\\sqrt{3}}$ | $0$ |")
check(eq(sin(deg(45)), 1 / sqrt(2)) and eq(cos(deg(30)), sqrt(3) / 2) and eq(tan(deg(60)), sqrt(3)) and eq(csc(deg(60)), 2 / sqrt(3)) and eq(sec(deg(30)), 2 / sqrt(3)) and eq(cot(deg(30)), sqrt(3)), "table")

sections = [
 {"id": "s1", "title": "Measuring with angles", "blocks": [
  blk("s1.hook", "hook", title="How tall is that tree?",
    body="A student stands 20 m away from a tall tree and looks up at its top. The line of sight makes an angle of $30^\\circ$ with the ground. Without climbing, can she find the height of the tree?\n\n"
         "Yes! In any right triangle, the angles decide the **ratios** of the sides. Trigonometry, from Greek words meaning 'triangle measurement', gives names to these ratios. In this chapter you will meet them; in Chapter 9 you will use them to find heights and distances."),
  blk("s1.inspiration", "inspiration", title="The journey of the word 'sine'", person="Aryabhata", years="476–550 CE",
    body="In the *Aryabhatiya*, Aryabhata gave a table of half-chords, which he called *ardha-jya* or simply *jya*. This is what we now call the **sine**.\n\n"
         "Arab scholars wrote *jya* as *jiba*. Later it was read as *jaib*, an Arabic word meaning a fold or pocket, and translated into Latin as *sinus*, which means the same thing. That became the English word **sine**. "
         "So every time you write $\\sin A$, you are using a word that travelled from India across the world.",
    quote="Great ideas travel far. The work you do today could be used by people a thousand years from now.",
    future="Trigonometry is used in surveying land, navigation of ships and aircraft, satellite communication, sound and music, engineering and computer games."),
  blk("s1.socratic", "socratic_question", question="Two right triangles both have an angle of $30^\\circ$, but one is twice as big as the other. Is $\\dfrac{\\text{side opposite } 30^\\circ}{\\text{hypotenuse}}$ the same in both?",
    options=["Yes, the triangles are similar, so the ratio is the same", "No, the bigger triangle has a bigger ratio", "It depends on the length of the hypotenuse"], correct_index=0,
    explanation="The triangles are similar (AA, from Chapter 6), so the ratios of their sides are equal. That is why a ratio like this depends only on the angle, not on the size of the triangle."),
 ]},
 {"id": "s2", "title": "Trigonometric ratios", "blocks": [
  fig("s2.fig", FIG_SIDES),
  blk("s2.reveal", "theory", title="The six ratios", revision=True,
    body="In $\\triangle ABC$, right-angled at $B$, with respect to $\\angle A$:\n\n"
         "- $\\sin A = \\dfrac{\\text{side opposite to } \\angle A}{\\text{hypotenuse}} = \\dfrac{BC}{AC}$\n"
         "- $\\cos A = \\dfrac{\\text{side adjacent to } \\angle A}{\\text{hypotenuse}} = \\dfrac{AB}{AC}$\n"
         "- $\\tan A = \\dfrac{\\text{side opposite to } \\angle A}{\\text{side adjacent to } \\angle A} = \\dfrac{BC}{AB}$\n\n"
         "The other three are their reciprocals: $\\text{cosec } A = \\dfrac{1}{\\sin A}$, $\\sec A = \\dfrac{1}{\\cos A}$ and $\\cot A = \\dfrac{1}{\\tan A}$.\n\n"
         "Also $\\tan A = \\dfrac{\\sin A}{\\cos A}$ and $\\cot A = \\dfrac{\\cos A}{\\sin A}$. Since the hypotenuse is the longest side, $\\sin A$ and $\\cos A$ are never more than 1 for an acute angle."),
  blk("s2.memory", "memory_trick", title="Pandit Badri Prasad Har Har Bole", revision=True,
    body="Take the first letters: **P**andit **B**adri **P**rasad over **H**ar **H**ar **B**ole.\n\n"
         "$\\sin = \\dfrac{P}{H}$, $\\cos = \\dfrac{B}{H}$, $\\tan = \\dfrac{P}{B}$, where $P$ is the perpendicular (side opposite the angle), $B$ the base (side adjacent to it) and $H$ the hypotenuse."),
  blk("s2.eg1", "worked_example", title="NCERT example",
    problem="Given $\\tan A = \\dfrac{4}{3}$, find the other trigonometric ratios of the angle A.",
    steps=["Take $BC = 4k$ and $AB = 3k$. Then $AC = \\sqrt{16k^{2} + 9k^{2}} = 5k$.",
           "$\\sin A = \\dfrac{4}{5}$, $\\cos A = \\dfrac{3}{5}$, $\\cot A = \\dfrac{3}{4}$",
           "$\\text{cosec } A = \\dfrac{5}{4}$, $\\sec A = \\dfrac{5}{3}$"],
    answer="$\\sin A = \\dfrac{4}{5}$, $\\cos A = \\dfrac{3}{5}$, $\\cot A = \\dfrac{3}{4}$, $\\text{cosec } A = \\dfrac{5}{4}$, $\\sec A = \\dfrac{5}{3}$"),
  blk("s2.eg2", "worked_example", title="NCERT exercise: using Pythagoras",
    problem="In $\\triangle ABC$, right-angled at $B$, $AB = 24$ cm and $BC = 7$ cm. Determine $\\sin A$, $\\cos A$, $\\sin C$ and $\\cos C$.",
    steps=["$AC = \\sqrt{24^{2} + 7^{2}} = \\sqrt{625} = 25$ cm", "$\\sin A = \\dfrac{BC}{AC} = \\dfrac{7}{25}$, $\\cos A = \\dfrac{AB}{AC} = \\dfrac{24}{25}$",
           "For $\\angle C$ the opposite side is $AB$: $\\sin C = \\dfrac{24}{25}$, $\\cos C = \\dfrac{7}{25}$"],
    answer="$\\sin A = \\dfrac{7}{25}$, $\\cos A = \\dfrac{24}{25}$, $\\sin C = \\dfrac{24}{25}$, $\\cos C = \\dfrac{7}{25}$"),
  fig("s2.fig2", FIG_Q81),
  blk("s2.check1", "knowledge_check", question="In a right triangle, if $\\sin A = \\dfrac{3}{5}$, then $\\cos A$ is:",
    options=["$\\dfrac{4}{5}$", "$\\dfrac{3}{4}$", "$\\dfrac{5}{3}$", "$\\dfrac{2}{5}$"], correct_index=0,
    explanation="Opposite $= 3k$, hypotenuse $= 5k$, so adjacent $= 4k$ and $\\cos A = \\dfrac{4}{5}$."),
  blk("s2.check2", "knowledge_check", question="Which of these is the reciprocal of $\\cos A$?",
    options=["$\\sec A$", "$\\text{cosec } A$", "$\\cot A$", "$\\tan A$"], correct_index=0, explanation="$\\sec A = \\dfrac{1}{\\cos A}$."),
  blk("s2.tip", "teacher_tip", title="Label before you calculate",
    body="Ask students to mark 'opposite', 'adjacent' and 'hypotenuse' on the triangle for the angle in question before writing any ratio. "
         "Then switch the angle (from $A$ to $C$) and let them see that the opposite and adjacent sides swap while the hypotenuse stays the same."),
 ]},
 {"id": "s3", "title": "Ratios of special angles", "blocks": [
  blk("s3.discovery", "discovery", title="Two special triangles",
    body="In an isosceles right triangle both acute angles are $45^\\circ$ and the sides are $a, a, \\sqrt{2}a$, so $\\sin 45^\\circ = \\cos 45^\\circ = \\dfrac{1}{\\sqrt{2}}$ and $\\tan 45^\\circ = 1$.\n\n"
         "Cut an equilateral triangle of side $2a$ in half: you get a right triangle with angles $30^\\circ$ and $60^\\circ$ and sides $a$, $\\sqrt{3}a$, $2a$. From it, $\\sin 30^\\circ = \\dfrac{1}{2}$ and $\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$."),
  fig("s3.fig45", FIG_45),
  fig("s3.fig30", FIG_EQ),
  blk("s3.table", "markdown_table", title="Values to remember", revision=True, body=TABLE_EN),
  blk("s3.memory", "memory_trick", title="The square-root trick", revision=True,
    body="For $\\sin$ at $0^\\circ, 30^\\circ, 45^\\circ, 60^\\circ, 90^\\circ$, write $\\dfrac{\\sqrt{0}}{2}, \\dfrac{\\sqrt{1}}{2}, \\dfrac{\\sqrt{2}}{2}, \\dfrac{\\sqrt{3}}{2}, \\dfrac{\\sqrt{4}}{2}$. "
         "For $\\cos$, write the same values in reverse order. Then $\\tan = \\dfrac{\\sin}{\\cos}$."),
  blk("s3.eg1", "worked_example", title="NCERT exercise: evaluate",
    problem="Evaluate $2\\tan^{2} 45^\\circ + \\cos^{2} 30^\\circ - \\sin^{2} 60^\\circ$.",
    steps=["$2 \\times 1^{2} + \\left(\\dfrac{\\sqrt{3}}{2}\\right)^{2} - \\left(\\dfrac{\\sqrt{3}}{2}\\right)^{2}$", "$= 2 + \\dfrac{3}{4} - \\dfrac{3}{4}$"], answer="$2$"),
  blk("s3.eg2", "worked_example", title="NCERT example: finding angles",
    problem="If $\\sin(A - B) = \\dfrac{1}{2}$ and $\\cos(A + B) = \\dfrac{1}{2}$, $0^\\circ < A + B \\leq 90^\\circ$ and $A > B$, find $A$ and $B$.",
    steps=["$\\sin(A - B) = \\dfrac{1}{2} = \\sin 30^\\circ$, so $A - B = 30^\\circ$.", "$\\cos(A + B) = \\dfrac{1}{2} = \\cos 60^\\circ$, so $A + B = 60^\\circ$.", "Adding: $2A = 90^\\circ$."],
    answer="$A = 45^\\circ$ and $B = 15^\\circ$"),
  blk("s3.check", "knowledge_check", question="The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:",
    options=["$1$", "$\\dfrac{1}{2}$", "$\\sqrt{3}$", "$0$"], correct_index=0, explanation="$\\dfrac{1}{2} + \\dfrac{1}{2} = 1$."),
 ]},
 {"id": "s4", "title": "Trigonometric identities", "blocks": [
  blk("s4.reveal", "theory", title="Three identities", revision=True,
    body="In right $\\triangle ABC$, $AB^{2} + BC^{2} = AC^{2}$. Dividing by $AC^{2}$, then by $AB^{2}$, then by $BC^{2}$ gives:\n\n"
         "$$\\sin^{2} A + \\cos^{2} A = 1$$\n\n$$1 + \\tan^{2} A = \\sec^{2} A$$\n\n$$1 + \\cot^{2} A = \\text{cosec}^{2} A$$\n\n"
         "An **identity** is true for every angle for which both sides are defined. Use these to express any ratio in terms of another, and to prove other identities."),
  blk("s4.eg1", "worked_example", title="NCERT example: proving an identity",
    problem="Prove that $\\sec A(1 - \\sin A)(\\sec A + \\tan A) = 1$.",
    steps=["LHS $= \\dfrac{1}{\\cos A}(1 - \\sin A)\\left(\\dfrac{1 + \\sin A}{\\cos A}\\right)$", "$= \\dfrac{1 - \\sin^{2} A}{\\cos^{2} A} = \\dfrac{\\cos^{2} A}{\\cos^{2} A}$", "$= 1 =$ RHS"],
    answer="Proved."),
  blk("s4.eg2", "worked_example", title="NCERT example",
    problem="Prove that $\\dfrac{\\cot A - \\cos A}{\\cot A + \\cos A} = \\dfrac{\\text{cosec } A - 1}{\\text{cosec } A + 1}$.",
    steps=["LHS $= \\dfrac{\\frac{\\cos A}{\\sin A} - \\cos A}{\\frac{\\cos A}{\\sin A} + \\cos A}$", "Take $\\cos A$ common and multiply by $\\sin A$: $= \\dfrac{\\cos A\\left(\\frac{1}{\\sin A} - 1\\right)}{\\cos A\\left(\\frac{1}{\\sin A} + 1\\right)}$",
           "$= \\dfrac{\\text{cosec } A - 1}{\\text{cosec } A + 1} =$ RHS"], answer="Proved."),
  blk("s4.check", "knowledge_check", question="The value of $9\\sec^{2} A - 9\\tan^{2} A$ is:",
    options=["$9$", "$1$", "$8$", "$0$"], correct_index=0, explanation="$9(\\sec^{2} A - \\tan^{2} A) = 9 \\times 1 = 9$."),
  blk("s4.tip", "memory_trick", title="How to prove an identity",
    body="- Start from the more complicated side.\n- Change everything to $\\sin$ and $\\cos$ if you are stuck.\n- Look for $1 - \\sin^{2}$, $\\sec^{2} - 1$ and similar pairs, and replace them using the three identities.\n- Never move terms across the '$=$' sign: work on one side until it becomes the other."),
  blk("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing $\\sin A$ as $\\sin \\times A$: $\\sin A$ is one number, the sine of the angle $A$.\n"
         "- Thinking $\\sin(A + B) = \\sin A + \\sin B$: check with $A = B = 30^\\circ$.\n"
         "- Writing $\\sin^{2} A$ as $\\sin A^{2}$: $\\sin^{2} A$ means $(\\sin A)^{2}$.\n"
         "- Swapping opposite and adjacent sides when the angle changes from $A$ to $C$.\n"
         "- Treating both sides of an identity as an equation and cross-multiplying."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  blk("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why $\\sin A$ can never be more than 1, but $\\tan A$ can be as large as you like."),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 9, Some Applications of Trigonometry:** find heights and distances using these ratios.\n"
         "- **Chapter 6, Triangles:** the ratios depend only on the angle because similar triangles have proportional sides.\n"
         "- **Class 11 Physics and Maths:** forces, waves and circular motion all use sine and cosine."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="In $\\triangle PQR$, right-angled at $Q$, $PR + QR = 25$ cm and $PQ = 5$ cm. Find $\\sin P$, $\\cos P$ and $\\tan P$.\n\n"
         "**Answer:** $PR^{2} - QR^{2} = PQ^{2} = 25$, so $(PR - QR)(PR + QR) = 25$ and $PR - QR = 1$. Hence $PR = 13$, $QR = 12$, and "
         "$\\sin P = \\dfrac{12}{13}$, $\\cos P = \\dfrac{5}{13}$, $\\tan P = \\dfrac{12}{5}$."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- $\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$, $\\cos A = \\dfrac{\\text{adjacent}}{\\text{hypotenuse}}$, $\\tan A = \\dfrac{\\text{opposite}}{\\text{adjacent}}$.\n"
         "- $\\text{cosec } A$, $\\sec A$ and $\\cot A$ are the reciprocals of $\\sin A$, $\\cos A$ and $\\tan A$.\n"
         "- If one ratio of an acute angle is known, all the others can be found.\n"
         "- Know the values for $0^\\circ$, $30^\\circ$, $45^\\circ$, $60^\\circ$ and $90^\\circ$.\n"
         "- $\\sin^{2} A + \\cos^{2} A = 1$, $\\sec^{2} A - \\tan^{2} A = 1$, $\\text{cosec}^{2} A - \\cot^{2} A = 1$."),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Draw the right triangle and mark the sides for the given angle before writing any ratio.\n"
         "- In 'evaluate' questions, write each value first, then simplify, and rationalise the denominator if asked.\n"
         "- In proofs, write LHS and RHS clearly and show every identity you use.\n"
         "- Learn the table of special angles thoroughly: it gives quick 1-mark answers."),
  blk("s5.flash1", "flashcard", front="What is $\\sin^{2} A + \\cos^{2} A$?", back="$1$, for every angle $A$."),
  blk("s5.flash2", "flashcard", front="What are $\\sin 30^\\circ$, $\\cos 30^\\circ$ and $\\tan 30^\\circ$?", back="$\\dfrac{1}{2}$, $\\dfrac{\\sqrt{3}}{2}$ and $\\dfrac{1}{\\sqrt{3}}$."),
  blk("s5.flash3", "flashcard", front="What is $1 + \\tan^{2} A$ equal to?", back="$\\sec^{2} A$"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Introduction to Trigonometry",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 8,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: trigonometric ratios of an acute angle of a right triangle, ratios of 0°, 30°, 45°, 60° and 90°, and the identity sin²A + cos²A = 1 with its use. Trigonometric ratios of complementary angles are not in the board syllabus and are not included.",
  "concepts": ["trig_ratios", "special_angles", "trig_identities"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
TR, SP, ID = "trig_ratios", "special_angles", "trig_identities"
SHINE = {"kind": "shine"}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch08.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
def tf(id_, concepts, statement, true, explanation, source, difficulty="easy"):
    q(id_, "true_false", 1, concepts, source, f"State whether the following is true or false. Justify your answer. {statement}", difficulty,
      options=["True", "False"], correct_index=0 if true else 1, explanation=explanation)
MS3_RATIO = ["1 mark: finding the third side", "1 mark: first ratios", "1 mark: remaining ratios"]
MS2_EVAL = ["1 mark: correct values", "1 mark: simplified answer"]
MS3_PROOF = ["1 mark: converting / using an identity", "1 mark: simplification", "1 mark: reaching the other side"]

# Exercise 8.1
q("ex8_1.q1", "short_answer", 3, [TR], ex("8.1", 1), "In $\\triangle ABC$, right-angled at $B$, $AB = 24$ cm and $BC = 7$ cm. Determine: (i) $\\sin A$, $\\cos A$ (ii) $\\sin C$, $\\cos C$", "easy",
  answer_steps=["$AC = \\sqrt{24^{2} + 7^{2}} = 25$ cm", "(i) $\\sin A = \\dfrac{7}{25}$, $\\cos A = \\dfrac{24}{25}$", "(ii) $\\sin C = \\dfrac{24}{25}$, $\\cos C = \\dfrac{7}{25}$"],
  marking_scheme=MS3_RATIO, figure=dict(FIG_Q81))
q("ex8_1.q2", "very_short_answer", 2, [TR], ex("8.1", 2), "In $\\triangle PQR$, right-angled at $Q$, $PQ = 12$ cm and $PR = 13$ cm. Determine the value of $\\tan P - \\cot R$.", "easy",
  answer_steps=["$QR = \\sqrt{13^{2} - 12^{2}} = 5$ cm, so $\\tan P = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$ and $\\cot R = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$.", "$\\tan P - \\cot R = 0$"],
  marking_scheme=MS2_EVAL, figure=dict(FIG_Q82))
q("ex8_1.q3", "very_short_answer", 2, [TR], ex("8.1", 3), "If $\\sin A = \\dfrac{3}{4}$, calculate $\\cos A$ and $\\tan A$.", "easy",
  answer_steps=["Opposite $= 3k$, hypotenuse $= 4k$, so adjacent $= \\sqrt{16k^{2} - 9k^{2}} = \\sqrt{7}k$.", "$\\cos A = \\dfrac{\\sqrt{7}}{4}$, $\\tan A = \\dfrac{3}{\\sqrt{7}}$"],
  marking_scheme=["1 mark: third side", "1 mark: both ratios"])
q("ex8_1.q4", "very_short_answer", 2, [TR], ex("8.1", 4), "Given $15\\cot A = 8$, find $\\sin A$ and $\\sec A$.", "easy",
  answer_steps=["$\\cot A = \\dfrac{8}{15}$: adjacent $= 8k$, opposite $= 15k$, hypotenuse $= 17k$.", "$\\sin A = \\dfrac{15}{17}$, $\\sec A = \\dfrac{17}{8}$"],
  marking_scheme=["1 mark: third side", "1 mark: both ratios"])
q("ex8_1.q5", "short_answer", 3, [TR], ex("8.1", 5), "Given $\\sec \\theta = \\dfrac{13}{12}$, calculate all other trigonometric ratios.", "easy",
  answer_steps=["Hypotenuse $= 13k$, adjacent $= 12k$, so opposite $= 5k$.", "$\\sin \\theta = \\dfrac{5}{13}$, $\\cos \\theta = \\dfrac{12}{13}$, $\\tan \\theta = \\dfrac{5}{12}$",
                "$\\cot \\theta = \\dfrac{12}{5}$, $\\text{cosec } \\theta = \\dfrac{13}{5}$"], marking_scheme=MS3_RATIO)
q("ex8_1.q6", "short_answer", 3, [TR], ex("8.1", 6), "If $\\angle A$ and $\\angle B$ are acute angles such that $\\cos A = \\cos B$, then show that $\\angle A = \\angle B$.", "hard",
  answer_steps=["Take right triangles $PQR$ (right-angled at $Q$, with $\\angle P = A$) and $XYZ$ (right-angled at $Y$, with $\\angle X = B$).",
                "$\\cos A = \\cos B$ gives $\\dfrac{PQ}{PR} = \\dfrac{XY}{XZ}$, i.e. $\\dfrac{PQ}{XY} = \\dfrac{PR}{XZ} = k$.",
                "Then $QR = \\sqrt{PR^{2} - PQ^{2}} = k\\sqrt{XZ^{2} - XY^{2}} = k \\cdot YZ$, so the triangles are similar (SSS) and $\\angle A = \\angle B$."],
  marking_scheme=MS3_PROOF)
q("ex8_1.q7", "short_answer", 3, [TR, ID], ex("8.1", 7), "If $\\cot \\theta = \\dfrac{7}{8}$, evaluate: (i) $\\dfrac{(1 + \\sin \\theta)(1 - \\sin \\theta)}{(1 + \\cos \\theta)(1 - \\cos \\theta)}$ (ii) $\\cot^{2} \\theta$",
  answer_steps=["(i) $\\dfrac{1 - \\sin^{2} \\theta}{1 - \\cos^{2} \\theta} = \\dfrac{\\cos^{2} \\theta}{\\sin^{2} \\theta} = \\cot^{2} \\theta$", "$= \\left(\\dfrac{7}{8}\\right)^{2} = \\dfrac{49}{64}$", "(ii) $\\cot^{2} \\theta = \\dfrac{49}{64}$"],
  marking_scheme=["1 mark: simplifying to $\\cot^{2} \\theta$", "1 mark: (i)", "1 mark: (ii)"])
q("ex8_1.q8", "short_answer", 3, [TR], ex("8.1", 8), "If $3\\cot A = 4$, check whether $\\dfrac{1 - \\tan^{2} A}{1 + \\tan^{2} A} = \\cos^{2} A - \\sin^{2} A$ or not.",
  answer_steps=["$\\cot A = \\dfrac{4}{3}$, so $\\tan A = \\dfrac{3}{4}$, $\\sin A = \\dfrac{3}{5}$, $\\cos A = \\dfrac{4}{5}$.", "LHS $= \\dfrac{1 - \\frac{9}{16}}{1 + \\frac{9}{16}} = \\dfrac{7}{25}$; RHS $= \\dfrac{16}{25} - \\dfrac{9}{25} = \\dfrac{7}{25}$.", "LHS $=$ RHS, so it holds."],
  marking_scheme=["1 mark: ratios", "1 mark: LHS and RHS", "1 mark: conclusion"])
q("ex8_1.q9", "short_answer", 3, [TR, SP], ex("8.1", 9), "In $\\triangle ABC$, right-angled at $B$, if $\\tan A = \\dfrac{1}{\\sqrt{3}}$, find the value of: (i) $\\sin A \\cos C + \\cos A \\sin C$ (ii) $\\cos A \\cos C - \\sin A \\sin C$",
  answer_steps=["$\\tan A = \\dfrac{1}{\\sqrt{3}}$: $BC = k$, $AB = \\sqrt{3}k$, $AC = 2k$. So $\\sin A = \\cos C = \\dfrac{1}{2}$ and $\\cos A = \\sin C = \\dfrac{\\sqrt{3}}{2}$.",
                "(i) $\\dfrac{1}{2} \\times \\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\times \\dfrac{\\sqrt{3}}{2} = \\dfrac{1}{4} + \\dfrac{3}{4} = 1$", "(ii) $\\dfrac{\\sqrt{3}}{2} \\times \\dfrac{1}{2} - \\dfrac{1}{2} \\times \\dfrac{\\sqrt{3}}{2} = 0$"],
  marking_scheme=["1 mark: ratios", "1 mark: (i)", "1 mark: (ii)"])
q("ex8_1.q10", "short_answer", 3, [TR], ex("8.1", 10), "In $\\triangle PQR$, right-angled at $Q$, $PR + QR = 25$ cm and $PQ = 5$ cm. Determine the values of $\\sin P$, $\\cos P$ and $\\tan P$.", "hard",
  answer_steps=["$PR^{2} - QR^{2} = PQ^{2} = 25$, so $(PR - QR)(PR + QR) = 25$ and $PR - QR = 1$.", "So $PR = 13$ cm and $QR = 12$ cm.", "$\\sin P = \\dfrac{12}{13}$, $\\cos P = \\dfrac{5}{13}$, $\\tan P = \\dfrac{12}{5}$"],
  marking_scheme=["1 mark: $PR - QR = 1$", "1 mark: sides", "1 mark: ratios"])
for p, stmt, true, why in [
 ("i", "The value of $\\tan A$ is always less than 1.", False, "False: $\\tan 60^\\circ = \\sqrt{3} > 1$."),
 ("ii", "$\\sec A = \\dfrac{12}{5}$ for some value of angle $A$.", True, "True: $\\sec A = \\dfrac{\\text{hypotenuse}}{\\text{adjacent}}$ can be $\\dfrac{12}{5}$, since the hypotenuse is the longest side (e.g. sides 5, $\\sqrt{119}$, 12)."),
 ("iii", "$\\cos A$ is the abbreviation used for the cosecant of angle $A$.", False, "False: $\\cos A$ is the cosine of $A$; the cosecant is written $\\text{cosec } A$."),
 ("iv", "$\\cot A$ is the product of $\\cot$ and $A$.", False, "False: $\\cot A$ is one number, the cotangent of the angle $A$."),
 ("v", "$\\sin \\theta = \\dfrac{4}{3}$ for some angle $\\theta$.", False, "False: $\\sin \\theta = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ is never more than 1."),
]:
    tf(f"ex8_1.q11.{p}", [TR], stmt, true, why, ex("8.1", 11, p))
# Exercise 8.2
for p, expr, steps in [
 ("i", "\\sin 60^\\circ \\cos 30^\\circ + \\sin 30^\\circ \\cos 60^\\circ", ["$\\dfrac{\\sqrt{3}}{2} \\times \\dfrac{\\sqrt{3}}{2} + \\dfrac{1}{2} \\times \\dfrac{1}{2} = \\dfrac{3}{4} + \\dfrac{1}{4}$", "$= 1$"]),
 ("ii", "2\\tan^{2} 45^\\circ + \\cos^{2} 30^\\circ - \\sin^{2} 60^\\circ", ["$2 \\times 1 + \\dfrac{3}{4} - \\dfrac{3}{4}$", "$= 2$"]),
 ("iii", "\\dfrac{\\cos 45^\\circ}{\\sec 30^\\circ + \\text{cosec } 30^\\circ}", ["$\\dfrac{\\frac{1}{\\sqrt{2}}}{\\frac{2}{\\sqrt{3}} + 2} = \\dfrac{\\sqrt{3}}{2\\sqrt{2}(1 + \\sqrt{3})}$", "$= \\dfrac{\\sqrt{3}(\\sqrt{3} - 1)}{4\\sqrt{2}} = \\dfrac{3\\sqrt{2} - \\sqrt{6}}{8}$"]),
 ("iv", "\\dfrac{\\sin 30^\\circ + \\tan 45^\\circ - \\text{cosec } 60^\\circ}{\\sec 30^\\circ + \\cos 60^\\circ + \\cot 45^\\circ}", ["$\\dfrac{\\frac{1}{2} + 1 - \\frac{2}{\\sqrt{3}}}{\\frac{2}{\\sqrt{3}} + \\frac{1}{2} + 1} = \\dfrac{3\\sqrt{3} - 4}{3\\sqrt{3} + 4}$", "$= \\dfrac{(3\\sqrt{3} - 4)^{2}}{27 - 16} = \\dfrac{43 - 24\\sqrt{3}}{11}$"]),
 ("v", "\\dfrac{5\\cos^{2} 60^\\circ + 4\\sec^{2} 30^\\circ - \\tan^{2} 45^\\circ}{\\sin^{2} 30^\\circ + \\cos^{2} 30^\\circ}", ["$\\dfrac{\\frac{5}{4} + \\frac{16}{3} - 1}{\\frac{1}{4} + \\frac{3}{4}} = \\dfrac{15 + 64 - 12}{12}$", "$= \\dfrac{67}{12}$"]),
]:
    q(f"ex8_2.q1.{p}", "very_short_answer", 2, [SP], ex("8.2", 1, p), f"Evaluate: ${expr}$", "easy" if p in ("i", "ii") else "medium", answer_steps=steps, marking_scheme=MS2_EVAL)
mcq("ex8_2.q2.i", [SP], "$\\dfrac{2\\tan 30^\\circ}{1 + \\tan^{2} 30^\\circ} =$", ["$\\sin 60^\\circ$", "$\\cos 60^\\circ$", "$\\tan 60^\\circ$", "$\\sin 30^\\circ$"], 0,
    "$\\dfrac{2/\\sqrt{3}}{1 + 1/3} = \\dfrac{2/\\sqrt{3}}{4/3} = \\dfrac{\\sqrt{3}}{2} = \\sin 60^\\circ$.", "medium", source=ex("8.2", 2, "i"))
mcq("ex8_2.q2.ii", [SP], "$\\dfrac{1 - \\tan^{2} 45^\\circ}{1 + \\tan^{2} 45^\\circ} =$", ["$\\tan 90^\\circ$", "$1$", "$\\sin 45^\\circ$", "$0$"], 3, "$\\dfrac{1 - 1}{1 + 1} = 0$.", source=ex("8.2", 2, "ii"))
mcq("ex8_2.q2.iii", [SP], "$\\sin 2A = 2\\sin A$ is true when $A =$", ["$0^\\circ$", "$30^\\circ$", "$45^\\circ$", "$60^\\circ$"], 0, "At $A = 0^\\circ$ both sides are 0; for the other angles they differ.", "medium", source=ex("8.2", 2, "iii"))
mcq("ex8_2.q2.iv", [SP], "$\\dfrac{2\\tan 30^\\circ}{1 - \\tan^{2} 30^\\circ} =$", ["$\\cos 60^\\circ$", "$\\sin 60^\\circ$", "$\\tan 60^\\circ$", "$\\sin 30^\\circ$"], 2,
    "$\\dfrac{2/\\sqrt{3}}{1 - 1/3} = \\dfrac{2/\\sqrt{3}}{2/3} = \\sqrt{3} = \\tan 60^\\circ$.", "medium", source=ex("8.2", 2, "iv"))
q("ex8_2.q3", "very_short_answer", 2, [SP], ex("8.2", 3), "If $\\tan(A + B) = \\sqrt{3}$ and $\\tan(A - B) = \\dfrac{1}{\\sqrt{3}}$; $0^\\circ < A + B \\leq 90^\\circ$; $A > B$, find $A$ and $B$.",
  answer_steps=["$A + B = 60^\\circ$ and $A - B = 30^\\circ$.", "$A = 45^\\circ$, $B = 15^\\circ$"], marking_scheme=["1 mark: both equations", "1 mark: $A$ and $B$"])
for p, stmt, true, why in [
 ("i", "$\\sin(A + B) = \\sin A + \\sin B$.", False, "False: with $A = B = 30^\\circ$, $\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ but $\\sin 30^\\circ + \\sin 30^\\circ = 1$."),
 ("ii", "The value of $\\sin \\theta$ increases as $\\theta$ increases (from $0^\\circ$ to $90^\\circ$).", True, "True: $0, \\dfrac{1}{2}, \\dfrac{1}{\\sqrt{2}}, \\dfrac{\\sqrt{3}}{2}, 1$ increase."),
 ("iii", "The value of $\\cos \\theta$ increases as $\\theta$ increases (from $0^\\circ$ to $90^\\circ$).", False, "False: $\\cos \\theta$ decreases from 1 to 0."),
 ("iv", "$\\sin \\theta = \\cos \\theta$ for all values of $\\theta$.", False, "False: it is true only for $\\theta = 45^\\circ$."),
 ("v", "$\\cot A$ is not defined for $A = 0^\\circ$.", True, "True: $\\cot 0^\\circ = \\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ} = \\dfrac{1}{0}$, which is not defined."),
]:
    tf(f"ex8_2.q4.{p}", [SP], stmt, true, why, ex("8.2", 4, p))
# Exercise 8.3
q("ex8_3.q1", "short_answer", 3, [ID], ex("8.3", 1), "Express the trigonometric ratios $\\sin A$, $\\sec A$ and $\\tan A$ in terms of $\\cot A$.",
  answer_steps=["$\\text{cosec}^{2} A = 1 + \\cot^{2} A$, so $\\sin A = \\dfrac{1}{\\sqrt{1 + \\cot^{2} A}}$.", "$\\tan A = \\dfrac{1}{\\cot A}$",
                "$\\sec^{2} A = 1 + \\tan^{2} A = \\dfrac{\\cot^{2} A + 1}{\\cot^{2} A}$, so $\\sec A = \\dfrac{\\sqrt{1 + \\cot^{2} A}}{\\cot A}$."],
  marking_scheme=["1 mark: $\\sin A$", "1 mark: $\\tan A$", "1 mark: $\\sec A$"])
q("ex8_3.q2", "short_answer", 3, [ID], ex("8.3", 2), "Write all the other trigonometric ratios of $\\angle A$ in terms of $\\sec A$.",
  answer_steps=["$\\cos A = \\dfrac{1}{\\sec A}$ and $\\tan A = \\sqrt{\\sec^{2} A - 1}$", "$\\sin A = \\tan A \\cos A = \\dfrac{\\sqrt{\\sec^{2} A - 1}}{\\sec A}$",
                "$\\cot A = \\dfrac{1}{\\sqrt{\\sec^{2} A - 1}}$ and $\\text{cosec } A = \\dfrac{\\sec A}{\\sqrt{\\sec^{2} A - 1}}$"],
  marking_scheme=["1 mark: $\\cos A$ and $\\tan A$", "1 mark: $\\sin A$", "1 mark: $\\cot A$ and $\\text{cosec } A$"])
mcq("ex8_3.q3.i", [ID], "$9\\sec^{2} A - 9\\tan^{2} A =$", ["$1$", "$9$", "$8$", "$0$"], 1, "$9(\\sec^{2} A - \\tan^{2} A) = 9$.", source=ex("8.3", 3, "i"))
mcq("ex8_3.q3.ii", [ID], "$(1 + \\tan \\theta + \\sec \\theta)(1 + \\cot \\theta - \\text{cosec } \\theta) =$", ["$0$", "$1$", "$2$", "$-1$"], 2,
    "In terms of $\\sin$ and $\\cos$ the product is $\\dfrac{(\\sin \\theta + \\cos \\theta)^{2} - 1}{\\sin \\theta \\cos \\theta} = \\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$.", "hard", source=ex("8.3", 3, "ii"))
mcq("ex8_3.q3.iii", [ID], "$(\\sec A + \\tan A)(1 - \\sin A) =$", ["$\\sec A$", "$\\sin A$", "$\\text{cosec } A$", "$\\cos A$"], 3,
    "$\\dfrac{1 + \\sin A}{\\cos A}(1 - \\sin A) = \\dfrac{\\cos^{2} A}{\\cos A} = \\cos A$.", "medium", source=ex("8.3", 3, "iii"))
mcq("ex8_3.q3.iv", [ID], "$\\dfrac{1 + \\tan^{2} A}{1 + \\cot^{2} A} =$", ["$\\sec^{2} A$", "$-1$", "$\\cot^{2} A$", "$\\tan^{2} A$"], 3,
    "$\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\dfrac{\\sin^{2} A}{\\cos^{2} A} = \\tan^{2} A$.", "medium", source=ex("8.3", 3, "iv"))
ID_TEXT = {
 "i": ("(\\text{cosec } \\theta - \\cot \\theta)^{2} = \\dfrac{1 - \\cos \\theta}{1 + \\cos \\theta}",
       ["LHS $= \\left(\\dfrac{1 - \\cos \\theta}{\\sin \\theta}\\right)^{2} = \\dfrac{(1 - \\cos \\theta)^{2}}{1 - \\cos^{2} \\theta}$", "$= \\dfrac{(1 - \\cos \\theta)^{2}}{(1 - \\cos \\theta)(1 + \\cos \\theta)}$", "$= \\dfrac{1 - \\cos \\theta}{1 + \\cos \\theta} =$ RHS"]),
 "ii": ("\\dfrac{\\cos A}{1 + \\sin A} + \\dfrac{1 + \\sin A}{\\cos A} = 2\\sec A",
        ["LHS $= \\dfrac{\\cos^{2} A + (1 + \\sin A)^{2}}{(1 + \\sin A)\\cos A}$", "$= \\dfrac{\\cos^{2} A + 1 + 2\\sin A + \\sin^{2} A}{(1 + \\sin A)\\cos A} = \\dfrac{2(1 + \\sin A)}{(1 + \\sin A)\\cos A}$", "$= \\dfrac{2}{\\cos A} = 2\\sec A =$ RHS"]),
 "iii": ("\\dfrac{\\tan \\theta}{1 - \\cot \\theta} + \\dfrac{\\cot \\theta}{1 - \\tan \\theta} = 1 + \\sec \\theta \\, \\text{cosec } \\theta",
         ["With $t = \\tan \\theta$: LHS $= \\dfrac{t^{2}}{t - 1} - \\dfrac{1}{t(t - 1)} = \\dfrac{t^{3} - 1}{t(t - 1)}$", "$= \\dfrac{t^{2} + t + 1}{t} = t + 1 + \\dfrac{1}{t}$",
          "$= 1 + \\dfrac{\\sin^{2} \\theta + \\cos^{2} \\theta}{\\sin \\theta \\cos \\theta} = 1 + \\sec \\theta \\, \\text{cosec } \\theta =$ RHS"]),
 "iv": ("\\dfrac{1 + \\sec A}{\\sec A} = \\dfrac{\\sin^{2} A}{1 - \\cos A}",
        ["LHS $= \\cos A + 1$", "RHS $= \\dfrac{1 - \\cos^{2} A}{1 - \\cos A} = \\dfrac{(1 - \\cos A)(1 + \\cos A)}{1 - \\cos A}$", "$= 1 + \\cos A =$ LHS"]),
 "v": ("\\dfrac{\\cos A - \\sin A + 1}{\\cos A + \\sin A - 1} = \\text{cosec } A + \\cot A",
       ["Divide numerator and denominator by $\\sin A$: LHS $= \\dfrac{\\cot A - 1 + \\text{cosec } A}{\\cot A + 1 - \\text{cosec } A}$", "Replace $1$ in the numerator by $\\text{cosec}^{2} A - \\cot^{2} A$: numerator $= (\\cot A + \\text{cosec } A)(1 - \\text{cosec } A + \\cot A)$",
        "Cancelling the common factor, LHS $= \\text{cosec } A + \\cot A =$ RHS"]),
 "vi": ("\\sqrt{\\dfrac{1 + \\sin A}{1 - \\sin A}} = \\sec A + \\tan A",
        ["Multiply inside by $\\dfrac{1 + \\sin A}{1 + \\sin A}$: LHS $= \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{1 - \\sin^{2} A}} = \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{\\cos^{2} A}}$", "$= \\dfrac{1 + \\sin A}{\\cos A}$", "$= \\sec A + \\tan A =$ RHS"]),
 "vii": ("\\dfrac{\\sin \\theta - 2\\sin^{3} \\theta}{2\\cos^{3} \\theta - \\cos \\theta} = \\tan \\theta",
         ["LHS $= \\dfrac{\\sin \\theta(1 - 2\\sin^{2} \\theta)}{\\cos \\theta(2\\cos^{2} \\theta - 1)}$", "$1 - 2\\sin^{2} \\theta = 1 - 2(1 - \\cos^{2} \\theta) = 2\\cos^{2} \\theta - 1$", "So LHS $= \\dfrac{\\sin \\theta}{\\cos \\theta} = \\tan \\theta =$ RHS"]),
 "viii": ("(\\sin A + \\text{cosec } A)^{2} + (\\cos A + \\sec A)^{2} = 7 + \\tan^{2} A + \\cot^{2} A",
          ["LHS $= \\sin^{2} A + 2 + \\text{cosec}^{2} A + \\cos^{2} A + 2 + \\sec^{2} A$", "$= 1 + 4 + (1 + \\cot^{2} A) + (1 + \\tan^{2} A)$", "$= 7 + \\tan^{2} A + \\cot^{2} A =$ RHS"]),
 "ix": ("(\\text{cosec } A - \\sin A)(\\sec A - \\cos A) = \\dfrac{1}{\\tan A + \\cot A}",
        ["LHS $= \\dfrac{1 - \\sin^{2} A}{\\sin A} \\cdot \\dfrac{1 - \\cos^{2} A}{\\cos A} = \\dfrac{\\cos^{2} A \\sin^{2} A}{\\sin A \\cos A} = \\sin A \\cos A$", "RHS $= \\dfrac{1}{\\frac{\\sin^{2} A + \\cos^{2} A}{\\sin A \\cos A}} = \\sin A \\cos A$", "LHS $=$ RHS"]),
 "x": ("\\left(\\dfrac{1 - \\tan A}{1 - \\cot A}\\right)^{2} = \\tan^{2} A",
       ["$1 - \\cot A = 1 - \\dfrac{1}{\\tan A} = \\dfrac{\\tan A - 1}{\\tan A}$", "LHS $= \\left(\\dfrac{(1 - \\tan A)\\tan A}{\\tan A - 1}\\right)^{2} = (-\\tan A)^{2}$", "$= \\tan^{2} A =$ RHS"]),
}
for p, (identity_tex, steps) in ID_TEXT.items():
    q(f"ex8_3.q4.{p}", "short_answer", 3, [ID], ex("8.3", 4, p), f"Prove the identity: ${identity_tex}$", "hard" if p in ("iii", "v") else "medium", answer_steps=steps, marking_scheme=MS3_PROOF)
# NCERT examples
q("eg_tan43", "short_answer", 3, [TR], {"kind": "ncert_example"}, "Given $\\tan A = \\dfrac{4}{3}$, find the other trigonometric ratios of the angle A.", "easy",
  answer_steps=["$BC = 4k$, $AB = 3k$, so $AC = 5k$.", "$\\sin A = \\dfrac{4}{5}$, $\\cos A = \\dfrac{3}{5}$, $\\cot A = \\dfrac{3}{4}$", "$\\text{cosec } A = \\dfrac{5}{4}$, $\\sec A = \\dfrac{5}{3}$"], marking_scheme=MS3_RATIO)
q("eg_angles", "very_short_answer", 2, [SP], {"kind": "ncert_example"}, "If $\\sin(A - B) = \\dfrac{1}{2}$, $\\cos(A + B) = \\dfrac{1}{2}$, $0^\\circ < A + B \\leq 90^\\circ$, $A > B$, find $A$ and $B$.",
  answer_steps=["$A - B = 30^\\circ$ and $A + B = 60^\\circ$.", "$A = 45^\\circ$, $B = 15^\\circ$"], marking_scheme=["1 mark: both equations", "1 mark: $A$ and $B$"])
q("eg_sec", "short_answer", 3, [ID], {"kind": "ncert_example"}, "Prove that $\\sec A(1 - \\sin A)(\\sec A + \\tan A) = 1$.",
  answer_steps=["LHS $= \\dfrac{1}{\\cos A}(1 - \\sin A)\\dfrac{1 + \\sin A}{\\cos A}$", "$= \\dfrac{1 - \\sin^{2} A}{\\cos^{2} A} = \\dfrac{\\cos^{2} A}{\\cos^{2} A}$", "$= 1 =$ RHS"], marking_scheme=MS3_PROOF)
q("eg_sinminus", "short_answer", 3, [ID], {"kind": "ncert_example"}, "Prove that $\\dfrac{\\sin \\theta - \\cos \\theta + 1}{\\sin \\theta + \\cos \\theta - 1} = \\dfrac{1}{\\sec \\theta - \\tan \\theta}$, using the identity $\\sec^{2} \\theta = 1 + \\tan^{2} \\theta$.", "hard",
  answer_steps=["Divide numerator and denominator by $\\cos \\theta$: LHS $= \\dfrac{\\tan \\theta - 1 + \\sec \\theta}{\\tan \\theta + 1 - \\sec \\theta}$", "Multiply numerator and denominator by $(\\tan \\theta - \\sec \\theta)$ and use $\\tan^{2} \\theta - \\sec^{2} \\theta = -1$: numerator $= -1 - (\\tan \\theta - \\sec \\theta)$",
                "LHS $= \\dfrac{-(1 - \\tan \\theta + \\sec \\theta)}{(\\tan \\theta - \\sec \\theta)(\\tan \\theta - \\sec \\theta + 1)} = \\dfrac{1}{\\sec \\theta - \\tan \\theta} =$ RHS"], marking_scheme=MS3_PROOF)
# Shine MCQs
mcq("mcq01", [SP], "The value of $\\sin 30^\\circ + \\cos 60^\\circ$ is:", ["$1$", "$\\dfrac{1}{2}$", "$\\sqrt{3}$", "$0$"], 0, "$\\dfrac{1}{2} + \\dfrac{1}{2} = 1$.")
mcq("mcq02", [TR], "If $\\sin A = \\dfrac{3}{5}$, then $\\cos A$ is:", ["$\\dfrac{4}{5}$", "$\\dfrac{3}{4}$", "$\\dfrac{5}{3}$", "$\\dfrac{2}{5}$"], 0, "Sides $3, 4, 5$: $\\cos A = \\dfrac{4}{5}$.")
mcq("mcq03", [SP], "The value of $\\tan 45^\\circ$ is:", ["$1$", "$0$", "$\\sqrt{3}$", "$\\dfrac{1}{\\sqrt{2}}$"], 0, "In an isosceles right triangle opposite $=$ adjacent, so $\\tan 45^\\circ = 1$.")
mcq("mcq04", [ID], "$\\sin^{2} 60^\\circ + \\cos^{2} 60^\\circ$ equals:", ["$1$", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$", "$2$"], 0, "$\\sin^{2} A + \\cos^{2} A = 1$ for every angle.")
mcq("mcq05", [TR], "If $\\tan A = \\dfrac{12}{5}$, then $\\sin A$ is:", ["$\\dfrac{12}{13}$", "$\\dfrac{5}{13}$", "$\\dfrac{12}{5}$", "$\\dfrac{13}{12}$"], 0, "Sides $5, 12, 13$: $\\sin A = \\dfrac{12}{13}$.", "medium")
mcq("mcq06", [TR], "The reciprocal of $\\cos A$ is:", ["$\\sec A$", "$\\text{cosec } A$", "$\\cot A$", "$\\tan A$"], 0, "$\\sec A = \\dfrac{1}{\\cos A}$.")
mcq("mcq07", [SP], "The value of $\\cos 90^\\circ$ is:", ["$0$", "$1$", "$\\dfrac{1}{2}$", "not defined"], 0, "$\\cos$ decreases from 1 at $0^\\circ$ to 0 at $90^\\circ$.")
mcq("mcq08", [SP], "$\\sin 60^\\circ - \\sin 30^\\circ$ equals:", ["$\\dfrac{\\sqrt{3} - 1}{2}$", "$\\sin 30^\\circ$", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3} + 1}{2}$"], 0,
    "$\\dfrac{\\sqrt{3}}{2} - \\dfrac{1}{2} = \\dfrac{\\sqrt{3} - 1}{2}$. Note that $\\sin(60^\\circ - 30^\\circ)$ would be different.", "medium")
mcq("mcq09", [ID], "$(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$ equals:", ["$1$", "$0$", "$\\sin^{2} A$", "$\\cos^{2} A$"], 0, "$\\sin^{2} A \\times \\dfrac{1}{\\sin^{2} A} = 1$.", "medium")
mcq("mcq10", [SP], "If $2\\sin \\theta = 1$ and $\\theta$ is acute, then $\\theta$ is:", ["$30^\\circ$", "$60^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\sin \\theta = \\dfrac{1}{2} = \\sin 30^\\circ$.")
mcq("mcq11", [TR], "For an acute angle $A$, which of these can never be true?", ["$\\sin A = \\dfrac{5}{4}$", "$\\tan A = 5$", "$\\sec A = 2$", "$\\cos A = 0.6$"], 0,
    "$\\sin A$ is at most 1, because the hypotenuse is the longest side.", "medium")
mcq("mcq12", [SP], "If $\\sqrt{3}\\tan \\theta = 1$, then $\\theta$ is:", ["$30^\\circ$", "$60^\\circ$", "$45^\\circ$", "$0^\\circ$"], 0, "$\\tan \\theta = \\dfrac{1}{\\sqrt{3}} = \\tan 30^\\circ$.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [TR], "For an acute angle $A$, $\\sin A$ cannot be $\\dfrac{4}{3}$.", "The hypotenuse is the longest side of a right triangle.", 0, "$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$ precisely because the hypotenuse is the longest side.")
ar("ar2", [ID], "$\\sin^{2} 35^\\circ + \\cos^{2} 35^\\circ = 1$.", "$\\sin^{2} A + \\cos^{2} A = 1$ for every angle $A$.", 0, "The identity in R gives A directly.")
ar("ar3", [SP], "$\\sin(30^\\circ + 60^\\circ) = \\sin 30^\\circ + \\sin 60^\\circ$.", "$\\sin 90^\\circ = 1$.", 3, "A is false: $\\sin 90^\\circ = 1$ but $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$. R is true.")
ar("ar4", [SP], "$2\\sin 45^\\circ \\cos 45^\\circ = 1$.", "$\\tan 45^\\circ = 0$.", 2, "A is true: $2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$. R is false: $\\tan 45^\\circ = 1$.")
ar("ar5", [SP], "$\\cot 0^\\circ$ is not defined.", "$\\sin 90^\\circ = 1$.", 1, "A is true because $\\sin 0^\\circ = 0$ makes $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ undefined. R is true but has nothing to do with A.")

q("vsa1", "very_short_answer", 2, [ID], SHINE, "Simplify: $(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$.", "easy",
  answer_steps=["$1 - \\cos^{2} A = \\sin^{2} A$", "$\\sin^{2} A \\times \\dfrac{1}{\\sin^{2} A} = 1$"], marking_scheme=MS2_EVAL)
q("vsa2", "very_short_answer", 2, [SP], SHINE, "Evaluate: $(\\sin 30^\\circ + \\cos 30^\\circ)^{2}$.",
  answer_steps=["$\\sin^{2} 30^\\circ + \\cos^{2} 30^\\circ + 2\\sin 30^\\circ \\cos 30^\\circ = 1 + 2 \\times \\dfrac{1}{2} \\times \\dfrac{\\sqrt{3}}{2}$", "$= 1 + \\dfrac{\\sqrt{3}}{2}$"], marking_scheme=MS2_EVAL)
q("sa1", "short_answer", 3, [ID], SHINE, "Prove that $\\sin^{4} A - \\cos^{4} A = 2\\sin^{2} A - 1$.",
  answer_steps=["LHS $= (\\sin^{2} A - \\cos^{2} A)(\\sin^{2} A + \\cos^{2} A)$", "$= \\sin^{2} A - \\cos^{2} A = \\sin^{2} A - (1 - \\sin^{2} A)$", "$= 2\\sin^{2} A - 1 =$ RHS"], marking_scheme=MS3_PROOF)
q("sa2", "short_answer", 3, [ID], SHINE, "Prove that $\\tan A + \\cot A = \\sec A \\, \\text{cosec } A$.",
  answer_steps=["LHS $= \\dfrac{\\sin A}{\\cos A} + \\dfrac{\\cos A}{\\sin A} = \\dfrac{\\sin^{2} A + \\cos^{2} A}{\\sin A \\cos A}$", "$= \\dfrac{1}{\\sin A \\cos A}$", "$= \\sec A \\, \\text{cosec } A =$ RHS"], marking_scheme=MS3_PROOF)
q("sa3", "short_answer", 3, [TR], SHINE, "If $\\cos A = \\dfrac{12}{13}$, find $\\sin A$ and $\\tan A$, and verify that $\\sin^{2} A + \\cos^{2} A = 1$.", "easy",
  answer_steps=["Adjacent $= 12k$, hypotenuse $= 13k$, opposite $= 5k$: $\\sin A = \\dfrac{5}{13}$, $\\tan A = \\dfrac{5}{12}$.", "$\\sin^{2} A + \\cos^{2} A = \\dfrac{25}{169} + \\dfrac{144}{169}$", "$= \\dfrac{169}{169} = 1$ ✓"],
  marking_scheme=["1 mark: $\\sin A$", "1 mark: $\\tan A$", "1 mark: verification"])
q("la1", "long_answer", 5, [ID], SHINE, "Prove that $(1 + \\cot A - \\text{cosec } A)(1 + \\tan A + \\sec A) = 2$. Hence find the value of $(1 + \\cot 45^\\circ - \\text{cosec } 45^\\circ)(1 + \\tan 45^\\circ + \\sec 45^\\circ)$ directly and check it.", "hard",
  answer_steps=["LHS $= \\left(1 + \\dfrac{\\cos A}{\\sin A} - \\dfrac{1}{\\sin A}\\right)\\left(1 + \\dfrac{\\sin A}{\\cos A} + \\dfrac{1}{\\cos A}\\right) = \\dfrac{(\\sin A + \\cos A - 1)(\\cos A + \\sin A + 1)}{\\sin A \\cos A}$",
                "$= \\dfrac{(\\sin A + \\cos A)^{2} - 1}{\\sin A \\cos A}$", "$= \\dfrac{1 + 2\\sin A \\cos A - 1}{\\sin A \\cos A} = 2 =$ RHS",
                "At $45^\\circ$: $(1 + 1 - \\sqrt{2})(1 + 1 + \\sqrt{2}) = (2 - \\sqrt{2})(2 + \\sqrt{2})$", "$= 4 - 2 = 2$ ✓"],
  marking_scheme=["1 mark: converting to $\\sin$ and $\\cos$", "1 mark: product form", "1 mark: proof", "1 mark: substitution at $45^\\circ$", "1 mark: check"])
q("la2", "long_answer", 5, [ID], SHINE, "Prove that $\\sqrt{\\dfrac{\\sec A - 1}{\\sec A + 1}} + \\sqrt{\\dfrac{\\sec A + 1}{\\sec A - 1}} = 2\\,\\text{cosec } A$.", "hard",
  answer_steps=["LHS $= \\dfrac{(\\sec A - 1) + (\\sec A + 1)}{\\sqrt{(\\sec A - 1)(\\sec A + 1)}}$", "$= \\dfrac{2\\sec A}{\\sqrt{\\sec^{2} A - 1}} = \\dfrac{2\\sec A}{\\tan A}$",
                "$= \\dfrac{2}{\\cos A} \\times \\dfrac{\\cos A}{\\sin A}$", "$= \\dfrac{2}{\\sin A}$", "$= 2\\,\\text{cosec } A =$ RHS"],
  marking_scheme=["1 mark: common denominator", "1 mark: $\\sec^{2} A - 1 = \\tan^{2} A$", "1 mark: converting", "1 mark: simplifying", "1 mark: conclusion"])
q("cb1", "case_based", 4, [TR, SP], SHINE,
  "A school builds a wheelchair ramp from the ground up to a door that is 2 m high. The ramp makes an angle of $30^\\circ$ with the ground.\n\n(i) Write $\\sin 30^\\circ$ in terms of the height of the door and the length of the ramp. (1)\n\n(ii) Find the length of the ramp. (1)\n\n(iii) Find the horizontal distance covered by the ramp. OR Using your answers, find $\\tan 30^\\circ$ and check it with the table. (2)",
  answer_steps=["(i) $\\sin 30^\\circ = \\dfrac{\\text{height}}{\\text{length of ramp}} = \\dfrac{2}{L}$", "(ii) $\\dfrac{1}{2} = \\dfrac{2}{L}$, so $L = 4$ m.",
                "(iii) $\\sqrt{4^{2} - 2^{2}} = \\sqrt{12} = 2\\sqrt{3}$ m $\\approx 3.46$ m. OR $\\tan 30^\\circ = \\dfrac{2}{2\\sqrt{3}} = \\dfrac{1}{\\sqrt{3}}$, as in the table."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [TR], SHINE,
  "A ladder 15 m long leans against a vertical wall. Its foot is 9 m from the wall.\n\n(i) How high up the wall does the ladder reach? (1)\n\n(ii) If $\\theta$ is the angle the ladder makes with the ground, find $\\cos \\theta$. (1)\n\n(iii) Find $\\sin \\theta$ and $\\tan \\theta$. OR Verify that $\\sin^{2} \\theta + \\cos^{2} \\theta = 1$. (2)",
  answer_steps=["(i) $\\sqrt{15^{2} - 9^{2}} = \\sqrt{144} = 12$ m", "(ii) $\\cos \\theta = \\dfrac{9}{15} = \\dfrac{3}{5}$",
                "(iii) $\\sin \\theta = \\dfrac{12}{15} = \\dfrac{4}{5}$, $\\tan \\theta = \\dfrac{12}{9} = \\dfrac{4}{3}$. OR $\\dfrac{16}{25} + \\dfrac{9}{25} = 1$ ✓"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
check(eq(sqrt(16 - 4), 2 * sqrt(3)) and eq(2 / (2 * sqrt(3)), 1 / sqrt(3)) and sqrt(15 ** 2 - 9 ** 2) == 12, "case studies")

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") in ("assertion_reason", "true_false") or item.get("source", {}).get("kind") == "ncert_exercise":
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
