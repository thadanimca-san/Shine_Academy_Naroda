"""CBSE Class 10 Maths Ch 9: Some Applications of Trigonometry (heights and distances).
Every answer is checked with sympy; figures are drawn to scale, so the marked
angles are the true angles."""
import json, math, os, sys
from collections import Counter
from sympy import sqrt, Rational as R, simplify, radsimp, tan, sin, cos, pi, atan, symbols, solve, Eq, nsimplify

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch09"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch09_some_applications_of_trigonometry"
deg = lambda d: d * pi / 180
s3 = sqrt(3)
x, h, w = symbols("x h w", positive=True)

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def eq(u, v): return simplify(radsimp(u - v)) == 0

# ---------------------------------------------------------------- verification
check(eq(20 * sin(deg(30)), 10), "Q1")
check(eq(8 * tan(deg(30)) + 8 / cos(deg(30)), 8 * s3), "Q2 tree = 8 sqrt3")
check(eq(R(3, 2) / sin(deg(30)), 3) and eq(3 / sin(deg(60)), 2 * s3), "Q3 slides")
check(eq(30 * tan(deg(30)), 10 * s3), "Q4"); check(eq(60 / sin(deg(60)), 40 * s3), "Q5")
check(eq(R(57, 2) / tan(deg(30)) - R(57, 2) / tan(deg(60)), 19 * s3), "Q6 19 sqrt3")
check(eq(20 * tan(deg(60)) - 20, 20 * (s3 - 1)), "Q7")
ped = solve(Eq((x + R(8, 5)) / x, s3), x)[0]; check(eq(ped, R(4, 5) * (s3 + 1)), "Q8")
check(eq((50 / tan(deg(60))) * tan(deg(30)), R(50, 3)), "Q9")
d10 = solve(Eq(x * s3, (80 - x) / s3), x)[0]; check(d10 == 20 and eq(d10 * s3, 20 * s3), "Q10")
w11 = solve(Eq(x * s3, (x + 20) / s3), x)[0]; check(w11 == 10 and eq(w11 * s3, 10 * s3), "Q11")
check(eq(7 + 7 * tan(deg(60)), 7 * (s3 + 1)), "Q12")
check(eq(75 / tan(deg(30)) - 75 / tan(deg(45)), 75 * (s3 - 1)), "Q13")
check(eq(87 / tan(deg(30)) - 87 / tan(deg(60)), 58 * s3), "Q14")
check(eq((h / tan(deg(60))) / ((h / tan(deg(30)) - h / tan(deg(60))) / 6), 3), "Q15 3 seconds")
# examples
check(eq(15 * tan(deg(60)), 15 * s3), "eg1")
L = R(37, 10) / sin(deg(60)); check(abs(float(L) - 4.27) < 0.01 and abs(float(R(37, 10) / tan(deg(60))) - 2.14) < 0.01, "eg2 ladder 4.28 m, foot 2.14 m")
check(eq(R(57, 2) * tan(deg(45)) + R(3, 2), 30), "eg3 chimney")
check(eq(10 / tan(deg(30)), 10 * s3) and eq(10 * s3 * tan(deg(45)) - 10, 10 * (s3 - 1)), "eg4 flagstaff")
hs = solve(Eq(x / tan(deg(30)) - x / tan(deg(60)), 40), x)[0]; check(eq(hs, 20 * s3), "eg5 shadow")
dd = solve(Eq(x - x * tan(deg(30)), 8), x)[0]; check(eq(dd, 4 * (3 + s3)), "eg6 building = distance = 4(3 + sqrt3)")
check(eq(3 / tan(deg(30)) + 3 / tan(deg(45)), 3 * (s3 + 1)), "eg7 river")
# MCQs and Shine questions
check(eq(30 * tan(deg(30)), 10 * s3) and eq(10 * sin(deg(60)), 5 * s3) and eq(6 / (2 * s3), s3), "mcq01-03")
check(eq(50 / tan(deg(45)), 50) and eq(100 * sin(deg(30)), 50) and eq(R(3, 2) / sin(deg(30)), 3) and eq(100 * s3 / 100, tan(deg(60))), "mcq05-12")
check(eq(10 * sin(deg(30)), 5) and not eq(10 * sin(deg(60)), 5), "ar3")
check(eq(2 / cos(deg(60)), 4), "vsa2")
check(eq(10 / tan(deg(30)) * tan(deg(60)) + 10, 40), "sa1")
check(eq((50 / tan(deg(30))) * tan(deg(60)), 150), "sa2")
hs3 = solve(Eq(x / tan(deg(45)) - x / tan(deg(60)), 20), x)[0]; check(eq(hs3, 30 + 10 * s3), "sa3")
check(eq(100 / tan(deg(45)) + 100 / tan(deg(30)), 100 * (1 + s3)), "la1")
check(eq((1500 * s3 / tan(deg(30)) - 1500 * s3 / tan(deg(60))) / 15, 200) and 200 * R(18, 5) == 720, "la2 720 km/h")
check(eq(atan(R(41, 41)), deg(45)) and eq(41 / tan(deg(60)), 41 / s3) and eq(41 / tan(deg(30)) - 41, 41 * (s3 - 1)) and eq(41 / (41 / s3), s3), "sqp38")
check(eq(60 / tan(deg(30)), 60 * s3) and eq(60 / tan(deg(60)), 20 * s3) and eq((60 * s3 - 20 * s3) / (2 * s3), 20), "cb2")

# ---------------------------------------------------------------- figures (to scale)
r3 = math.sqrt(3)
def fig(title, points, segments, **kw):
    f = {"type": "geometry_figure", "title": title, "points": {k: [round(v[0], 9), round(v[1], 9)] for k, v in points.items()}, "segments": segments}
    f.update(kw); return f
def elevation(title, d, hgt, angle, labels):
    return fig(title, {"P": (0, 0), "B": (d, 0), "T": (d, hgt)},
               [["P", "B"], {"from": "B", "to": "T", "highlight": True}, {"from": "P", "to": "T", "dashed": True}],
               right_angles=[["P", "B", "T"]], angles=[{"points": ["B", "P", "T"], "label": angle}], lengths=labels)
FIG_ELEV = elevation("Angle of elevation", 4 * r3, 4, "30°", [{"from": "P", "to": "B", "label": "d"}, {"from": "B", "to": "T", "label": "h"}])
FIG_DEP = fig("Angle of depression", {"A": (0, 4), "B": (0, 0), "P": (4 * r3, 0), "X": (4 * r3 + 2, 4)},
              [{"from": "A", "to": "B", "highlight": True}, ["B", "P"], {"from": "A", "to": "X", "dashed": True}, {"from": "A", "to": "P", "dashed": True}],
              right_angles=[["A", "B", "P"]], parallel=[["A", "X", "B", "P"]], angles=[{"points": ["X", "A", "P"], "label": "30°"}, {"points": ["B", "P", "A"], "label": "30°"}])
FIG_EG1 = elevation("A tower 15 m away", 15, 15 * r3, "60°", [{"from": "P", "to": "B", "label": "15 m"}, {"from": "B", "to": "T", "label": "h"}])
FIG_FLAG = fig("Building BC with flagstaff CD", {"P": (0, 0), "B": (10 * r3, 0), "C": (10 * r3, 10), "D": (10 * r3, 10 * r3)},
               [["P", "B"], ["B", "C"], {"from": "C", "to": "D", "highlight": True}, {"from": "P", "to": "C", "dashed": True}, {"from": "P", "to": "D", "dashed": True}],
               right_angles=[["P", "B", "C"]], angles=[{"points": ["B", "P", "C"], "label": "30°"}, {"points": ["C", "P", "D"], "label": "15°"}],
               lengths=[{"from": "B", "to": "C", "label": "10 m"}])
FIG_SHADOW = fig("The shadow is 40 m longer", {"T": (0, 20 * r3), "B": (0, 0), "C": (20, 0), "S": (60, 0)},
                 [{"from": "T", "to": "B", "highlight": True}, ["B", "S"], {"from": "T", "to": "C", "dashed": True}, {"from": "T", "to": "S", "dashed": True}],
                 right_angles=[["T", "B", "C"]], angles=[{"points": ["B", "C", "T"], "label": "60°"}, {"points": ["B", "S", "T"], "label": "30°"}],
                 lengths=[{"from": "C", "to": "S", "label": "40 m"}])
dist6 = 4 * (3 + r3)
FIG_BUILD = fig("Looking down at a shorter building", {"A": (0, dist6), "B": (0, 0), "C": (dist6, 0), "D": (dist6, 8), "X": (dist6 + 3, dist6)},
                [{"from": "A", "to": "B", "highlight": True}, ["B", "C"], {"from": "C", "to": "D", "highlight": True}, {"from": "A", "to": "X", "dashed": True},
                 {"from": "A", "to": "D", "dashed": True}, {"from": "A", "to": "C", "dashed": True}],
                right_angles=[["A", "B", "C"]], parallel=[["A", "X", "B", "C"]], lengths=[{"from": "C", "to": "D", "label": "8 m"}])
FIG_Q6 = fig("The boy walks from P to Q", {"P": (0, 0), "Q": (19 * r3, 0), "B": (28.5 * r3, 0), "T": (28.5 * r3, 28.5)},
             [["P", "B"], {"from": "B", "to": "T", "highlight": True}, {"from": "P", "to": "T", "dashed": True}, {"from": "Q", "to": "T", "dashed": True}],
             right_angles=[["P", "B", "T"]], angles=[{"points": ["B", "P", "T"], "label": "30°"}, {"points": ["B", "Q", "T"], "label": "60°"}],
             lengths=[{"from": "B", "to": "T", "label": "28.5 m"}])
FIG_Q10 = fig("Two equal poles across an 80 m road", {"A": (0, 0), "B": (0, 20 * r3), "P": (20, 0), "C": (80, 0), "D": (80, 20 * r3)},
              [["A", "C"], {"from": "A", "to": "B", "highlight": True}, {"from": "C", "to": "D", "highlight": True}, {"from": "P", "to": "B", "dashed": True}, {"from": "P", "to": "D", "dashed": True}],
              right_angles=[["B", "A", "P"], ["P", "C", "D"]], angles=[{"points": ["A", "P", "B"], "label": "60°"}, {"points": ["C", "P", "D"], "label": "30°"}])
FIG_Q13 = fig("Two ships seen from a lighthouse", {"A": (0, 75), "B": (0, 0), "C": (75, 0), "D": (75 * r3, 0), "X": (75 * r3 + 10, 75)},
              [{"from": "A", "to": "B", "highlight": True}, ["B", "D"], {"from": "A", "to": "X", "dashed": True}, {"from": "A", "to": "C", "dashed": True}, {"from": "A", "to": "D", "dashed": True}],
              right_angles=[["A", "B", "C"]], parallel=[["A", "X", "B", "D"]], lengths=[{"from": "A", "to": "B", "label": "75 m"}])
FIG_GATE = elevation("Shreya and India Gate (above eye level)", 41, 41, "45°", [{"from": "P", "to": "B", "label": "41 m"}, {"from": "B", "to": "T", "label": "41 m"}])
check(abs(math.degrees(math.atan2(FIG_Q6["points"]["T"][1], FIG_Q6["points"]["T"][0] - FIG_Q6["points"]["Q"][0])) - 60) < 1e-6, "fig Q6 angle")
check(abs(math.degrees(math.atan2(75, 75 * r3)) - 30) < 1e-9 and abs(math.degrees(math.atan2(8 - dist6, dist6)) + 30) < 1e-9, "fig angles")

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch09.{id_}", "type": type_, **kw}
def placed(id_, figure): return {"id": f"ch09.{id_}", **figure}

sections = [
 {"id": "s1", "title": "Measuring what you cannot reach", "blocks": [
  blk("s1.hook", "hook", title="How do we know the height of Mount Everest?",
    body="Nobody dropped a measuring tape from the top of Mount Everest. Yet its height was known long before anyone climbed it.\n\n"
         "Surveyors stood on the ground far away, measured the **angle** at which they had to look up to see the peak, and used trigonometry to calculate the height. "
         "In this chapter you will do the same with towers, trees, kites and ships."),
  blk("s1.inspiration", "inspiration", title="The man who found the highest peak", person="Radhanath Sikdar", years="1813–1870",
    body="Radhanath Sikdar was a brilliant mathematician from Bengal who joined the Great Trigonometrical Survey of India as a 'computer', the name then given to people who did calculations.\n\n"
         "Working from angles measured at survey stations more than 150 km away, he calculated in 1852 that a mountain then called 'Peak XV' was the highest in the world. "
         "That mountain is Mount Everest. His careful calculation with angles and distances changed the map of the world.",
    quote="Patience and careful calculation can measure even the highest mountain.",
    future="Heights and distances are found this way in surveying, map-making, navigation, astronomy, construction, and by the sensors in phones and drones."),
  blk("s1.socratic", "socratic_question", question="As you walk towards a tall tower, what happens to the angle at which you look up at its top?",
    options=["It increases", "It decreases", "It stays the same"], correct_index=0,
    explanation="The height stays the same but the distance gets smaller, so $\\tan \\theta = \\dfrac{\\text{height}}{\\text{distance}}$ gets larger and the angle increases."),
 ]},
 {"id": "s2", "title": "Elevation and depression", "blocks": [
  blk("s2.reveal", "theory", title="Line of sight", revision=True,
    body="The **line of sight** is the line drawn from the eye of an observer to the point being viewed.\n\n"
         "- The **angle of elevation** is the angle between the line of sight and the horizontal when the object is **above** the eye level, so we raise our head.\n"
         "- The **angle of depression** is the angle between the line of sight and the horizontal when the object is **below** the eye level, so we lower our head.\n\n"
         "The angle of depression from $A$ to $P$ equals the angle of elevation from $P$ to $A$: they are alternate angles between parallel horizontal lines."),
  placed("s2.fig1", FIG_ELEV),
  placed("s2.fig2", FIG_DEP),
  blk("s2.check", "knowledge_check", question="A person on a cliff looks down at a boat. The angle between the horizontal and the line of sight to the boat is called the:",
    options=["angle of depression", "angle of elevation", "right angle", "angle of the cliff"], correct_index=0,
    explanation="The boat is below the eye level, so the angle with the horizontal is the angle of depression."),
 ]},
 {"id": "s3", "title": "Solving height and distance problems", "blocks": [
  blk("s3.reveal", "theory", title="A method that always works", revision=True,
    body="1. Draw a neat figure. Mark the vertical object, the horizontal ground and the **right angle** between them.\n"
         "2. Mark the given angle at the correct place: elevation at the observer on the ground; depression along the horizontal at the observer's eye.\n"
         "3. In the right triangle, choose the ratio that links the **known** side with the **unknown** side:\n"
         "   - height and horizontal distance: use $\\tan$;\n"
         "   - height and slant length (rope, ladder, string): use $\\sin$;\n"
         "   - horizontal distance and slant length: use $\\cos$.\n"
         "4. Solve, and remember to add the observer's height if the angle is measured from the eye."),
  blk("s3.eg1", "worked_example", title="NCERT example: a tower",
    problem="A tower stands vertically on the ground. From a point on the ground, which is 15 m away from the foot of the tower, the angle of elevation of the top of the tower is found to be $60^\\circ$. Find the height of the tower.",
    steps=["Height $h$ and distance 15 m: use $\\tan$.", "$\\tan 60^\\circ = \\dfrac{h}{15}$, so $h = 15\\sqrt{3}$."], answer="The tower is $15\\sqrt{3}$ m high."),
  placed("s3.fig1", FIG_EG1),
  blk("s3.eg2", "worked_example", title="NCERT example: the electrician's ladder",
    problem="An electrician has to repair an electric fault on a pole of height 5 m. She needs to reach a point 1.3 m below the top of the pole to undertake the repair work. What should be the length of the ladder that she should use which, when inclined at an angle of $60^\\circ$ to the horizontal, would enable her to reach the required position? Also, how far from the foot of the pole should she place the foot of the ladder? (Take $\\sqrt{3} = 1.73$)",
    steps=["Required height $= 5 - 1.3 = 3.7$ m.", "$\\sin 60^\\circ = \\dfrac{3.7}{L}$, so $L = \\dfrac{3.7 \\times 2}{\\sqrt{3}} \\approx 4.28$ m.", "$\\tan 60^\\circ = \\dfrac{3.7}{d}$, so $d = \\dfrac{3.7}{\\sqrt{3}} \\approx 2.14$ m."],
    answer="A ladder of about 4.28 m, with its foot about 2.14 m from the pole."),
  blk("s3.eg3", "worked_example", title="NCERT example: a flagstaff",
    problem="From a point P on the ground the angle of elevation of the top of a 10 m tall building is $30^\\circ$. A flag is hoisted at the top of the building and the angle of elevation of the top of the flagstaff from P is $45^\\circ$. Find the length of the flagstaff and the distance of the building from the point P. (Take $\\sqrt{3} = 1.732$)",
    steps=["$\\tan 30^\\circ = \\dfrac{10}{PB}$, so $PB = 10\\sqrt{3} \\approx 17.32$ m.", "$\\tan 45^\\circ = \\dfrac{10 + x}{PB}$, so $10 + x = 10\\sqrt{3}$.", "$x = 10(\\sqrt{3} - 1) \\approx 7.32$ m"],
    answer="The flagstaff is about 7.32 m long and the building is about 17.32 m from P."),
  placed("s3.fig2", FIG_FLAG),
  blk("s3.eg4", "worked_example", title="NCERT example: shadows",
    problem="The shadow of a tower standing on a level ground is found to be 40 m longer when the Sun's altitude is $30^\\circ$ than when it is $60^\\circ$. Find the height of the tower.",
    steps=["Let the height be $h$ and the shorter shadow $x$: $\\tan 60^\\circ = \\dfrac{h}{x}$, so $h = \\sqrt{3}x$.", "$\\tan 30^\\circ = \\dfrac{h}{x + 40}$, so $\\sqrt{3}h = x + 40$, i.e. $3x = x + 40$ and $x = 20$."],
    answer="$h = 20\\sqrt{3}$ m"),
  placed("s3.fig3", FIG_SHADOW),
  blk("s3.eg5", "worked_example", title="NCERT example: angles of depression",
    problem="The angles of depression of the top and the bottom of an 8 m tall building from the top of a multi-storeyed building are $30^\\circ$ and $45^\\circ$, respectively. Find the height of the multi-storeyed building and the distance between the two buildings.",
    steps=["Let the tall building be $H$ m high and the distance between them $d$ m.", "Depression $45^\\circ$ to the bottom: $\\tan 45^\\circ = \\dfrac{H}{d}$, so $H = d$.",
           "Depression $30^\\circ$ to the top: $\\tan 30^\\circ = \\dfrac{H - 8}{d}$, so $d - 8 = \\dfrac{d}{\\sqrt{3}}$ and $d = \\dfrac{8\\sqrt{3}}{\\sqrt{3} - 1} = 4(3 + \\sqrt{3})$."],
    answer="Both the height and the distance are $4(3 + \\sqrt{3})$ m."),
  placed("s3.fig4", FIG_BUILD),
  blk("s3.check1", "knowledge_check", question="The angle of elevation of the top of a tower from a point 30 m from its foot is $30^\\circ$. The height of the tower is:",
    options=["$10\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$15$ m", "$10$ m"], correct_index=0, explanation="$h = 30\\tan 30^\\circ = \\dfrac{30}{\\sqrt{3}} = 10\\sqrt{3}$ m."),
  blk("s3.check2", "knowledge_check", question="A kite string is 100 m long and makes an angle of $30^\\circ$ with the ground. The height of the kite is:",
    options=["$50$ m", "$50\\sqrt{3}$ m", "$100\\sqrt{3}$ m", "$200$ m"], correct_index=0, explanation="The string is the slant side: $h = 100\\sin 30^\\circ = 50$ m."),
  blk("s3.memory", "memory_trick", title="Which ratio?", revision=True,
    body="- Height and ground distance? **tan**.\n- A slanting length (ladder, rope, string, slide) and the height? **sin**.\n- A slanting length and the ground distance? **cos**.\n"
         "Remember the two numbers: $\\tan 30^\\circ = \\dfrac{1}{\\sqrt{3}}$ and $\\tan 60^\\circ = \\sqrt{3}$. Most problems use only these and $\\tan 45^\\circ = 1$."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Forgetting to add the observer's height when the angle is measured from the eye.\n"
         "- Marking the angle of depression inside the triangle at the wrong vertex: it is measured from the horizontal at the observer.\n"
         "- Using $\\tan$ when the slant length is given or asked.\n"
         "- Rounding $\\sqrt{3}$ too early: keep it until the last step.\n"
         "- Drawing the figure carelessly: a wrong figure almost always leads to a wrong equation."),
  blk("s3.tip", "teacher_tip", title="Make it real",
    body="Take the class to the playground with a protractor and a straw taped to it as a simple clinometer. Let students measure the angle of elevation of the school building from a measured distance and calculate its height. "
         "Comparing their answers with the real height makes the chapter unforgettable."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why the angle of depression from the top of a lighthouse to a boat is equal to the angle of elevation of the lighthouse top from the boat."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 8:** this chapter is trigonometric ratios at work.\n"
         "- **Geography and surveying:** heights of mountains and widths of rivers are measured with angles.\n"
         "- **Physics (Class 11):** projectile motion and the resolution of forces use the same right triangles."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of $30^\\circ$, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be $60^\\circ$. Find the time taken by the car to reach the foot of the tower from this point.\n\n"
         "**Answer:** If the tower is $h$ high, the car is first $\\sqrt{3}h$ away and then $\\dfrac{h}{\\sqrt{3}}$ away. It covers $\\sqrt{3}h - \\dfrac{h}{\\sqrt{3}} = \\dfrac{2h}{\\sqrt{3}}$ in 6 seconds, "
         "so the remaining $\\dfrac{h}{\\sqrt{3}}$, which is half of that, takes **3 seconds**."),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- The line of sight joins the observer's eye to the object.\n"
         "- Angle of elevation: object above eye level. Angle of depression: object below eye level.\n"
         "- The angle of depression from $A$ to $B$ equals the angle of elevation from $B$ to $A$.\n"
         "- Draw the figure, find the right triangle and use $\\tan$, $\\sin$ or $\\cos$ to find the unknown height or distance."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- A correct, labelled figure usually carries a mark: always draw one.\n"
         "- Write the trigonometric ratio you use, for example $\\tan 60^\\circ = \\dfrac{h}{x}$, before solving.\n"
         "- When two angles are given, form two equations and eliminate the common unknown.\n"
         "- Use the value of $\\sqrt{3}$ given in the question only at the end, and write the units."),
  blk("s4.flash1", "flashcard", front="What is the angle of elevation?", back="The angle between the line of sight and the horizontal when the object is above the observer's eye level."),
  blk("s4.flash2", "flashcard", front="What is the angle of depression?", back="The angle between the line of sight and the horizontal when the object is below the observer's eye level."),
  blk("s4.flash3", "flashcard", front="Which ratio links a height with a horizontal distance?", back="$\\tan \\theta = \\dfrac{\\text{height}}{\\text{distance}}$"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Some Applications of Trigonometry",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 9,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: simple problems on heights and distances, with not more than two right triangles and angles of elevation or depression of 30°, 45° and 60°.",
  "concepts": ["elevation_depression", "heights_distances"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
ED, HD = "elevation_depression", "heights_distances"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "9.1", "question": n}
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch09.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, question, options, correct, explanation, difficulty="easy"):
    q(id_, "mcq", 1, [HD], SHINE, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS3 = ["1 mark: correct figure", "1 mark: correct trigonometric ratio", "1 mark: answer"]
MS5 = ["1 mark: correct figure", "1 mark: first equation", "1 mark: second equation", "1 mark: solving", "1 mark: answer with units"]

EX = [
 (1, 3, "A circus artist is climbing a 20 m long rope, which is tightly stretched and tied from the top of a vertical pole to the ground. Find the height of the pole, if the angle made by the rope with the ground level is $30^\\circ$.", "easy",
  ["The rope is the slant side: $\\sin 30^\\circ = \\dfrac{h}{20}$.", "$h = 20 \\times \\dfrac{1}{2}$", "The pole is 10 m high."]),
 (2, 3, "A tree breaks due to storm and the broken part bends so that the top of the tree touches the ground making an angle $30^\\circ$ with it. The distance between the foot of the tree to the point where the top touches the ground is 8 m. Find the height of the tree.", "medium",
  ["Standing part: $\\tan 30^\\circ = \\dfrac{a}{8}$, so $a = \\dfrac{8}{\\sqrt{3}}$.", "Broken part: $\\cos 30^\\circ = \\dfrac{8}{b}$, so $b = \\dfrac{16}{\\sqrt{3}}$.", "Height $= a + b = \\dfrac{24}{\\sqrt{3}} = 8\\sqrt{3}$ m"]),
 (3, 3, "A contractor plans to install two slides for the children to play in a park. For the children below the age of 5 years, she prefers to have a slide whose top is at a height of 1.5 m, and is inclined at an angle of $30^\\circ$ to the ground, whereas for elder children, she wants to have a steep slide at a height of 3 m, and inclined at an angle of $60^\\circ$ to the ground. What should be the length of the slide in each case?", "easy",
  ["Small slide: $\\sin 30^\\circ = \\dfrac{1.5}{L_1}$, so $L_1 = 3$ m.", "Big slide: $\\sin 60^\\circ = \\dfrac{3}{L_2}$, so $L_2 = \\dfrac{6}{\\sqrt{3}}$.", "$L_2 = 2\\sqrt{3}$ m"]),
 (4, 3, "The angle of elevation of the top of a tower from a point on the ground, which is 30 m away from the foot of the tower, is $30^\\circ$. Find the height of the tower.", "easy",
  ["$\\tan 30^\\circ = \\dfrac{h}{30}$", "$h = \\dfrac{30}{\\sqrt{3}}$", "The tower is $10\\sqrt{3}$ m high."]),
 (5, 3, "A kite is flying at a height of 60 m above the ground. The string attached to the kite is temporarily tied to a point on the ground. The inclination of the string with the ground is $60^\\circ$. Find the length of the string, assuming that there is no slack in the string.", "easy",
  ["The string is the slant side: $\\sin 60^\\circ = \\dfrac{60}{L}$.", "$L = \\dfrac{120}{\\sqrt{3}}$", "The string is $40\\sqrt{3}$ m long."]),
 (6, 5, "A 1.5 m tall boy is standing at some distance from a 30 m tall building. The angle of elevation from his eyes to the top of the building increases from $30^\\circ$ to $60^\\circ$ as he walks towards the building. Find the distance he walked towards the building.", "hard",
  ["Height of the building above his eyes $= 30 - 1.5 = 28.5$ m.", "At first: $\\tan 30^\\circ = \\dfrac{28.5}{d_1}$, so $d_1 = 28.5\\sqrt{3}$.", "Later: $\\tan 60^\\circ = \\dfrac{28.5}{d_2}$, so $d_2 = \\dfrac{28.5}{\\sqrt{3}}$.",
   "Distance walked $= 28.5\\left(\\sqrt{3} - \\dfrac{1}{\\sqrt{3}}\\right) = \\dfrac{57}{\\sqrt{3}}$", "$= 19\\sqrt{3}$ m"]),
 (7, 3, "From a point on the ground, the angles of elevation of the bottom and the top of a transmission tower fixed at the top of a 20 m high building are $45^\\circ$ and $60^\\circ$ respectively. Find the height of the tower.", "medium",
  ["Bottom of the tower: $\\tan 45^\\circ = \\dfrac{20}{d}$, so $d = 20$ m.", "Top of the tower: $\\tan 60^\\circ = \\dfrac{20 + t}{20}$, so $20 + t = 20\\sqrt{3}$.", "The tower is $20(\\sqrt{3} - 1)$ m high."]),
 (8, 3, "A statue, 1.6 m tall, stands on the top of a pedestal. From a point on the ground, the angle of elevation of the top of the statue is $60^\\circ$ and from the same point the angle of elevation of the top of the pedestal is $45^\\circ$. Find the height of the pedestal.", "medium",
  ["Pedestal of height $p$: $\\tan 45^\\circ = \\dfrac{p}{d}$, so $d = p$.", "$\\tan 60^\\circ = \\dfrac{p + 1.6}{p}$, so $p\\sqrt{3} = p + 1.6$.", "$p = \\dfrac{1.6}{\\sqrt{3} - 1} = 0.8(\\sqrt{3} + 1)$ m"]),
 (9, 3, "The angle of elevation of the top of a building from the foot of the tower is $30^\\circ$ and the angle of elevation of the top of the tower from the foot of the building is $60^\\circ$. If the tower is 50 m high, find the height of the building.", "medium",
  ["From the foot of the building: $\\tan 60^\\circ = \\dfrac{50}{d}$, so $d = \\dfrac{50}{\\sqrt{3}}$.", "From the foot of the tower: $\\tan 30^\\circ = \\dfrac{b}{d}$, so $b = \\dfrac{50}{\\sqrt{3}} \\times \\dfrac{1}{\\sqrt{3}}$.", "$b = \\dfrac{50}{3} = 16\\dfrac{2}{3}$ m"]),
 (10, 5, "Two poles of equal heights are standing opposite each other on either side of the road, which is 80 m wide. From a point between them on the road, the angles of elevation of the top of the poles are $60^\\circ$ and $30^\\circ$, respectively. Find the height of the poles and the distances of the point from the poles.", "hard",
  ["Let the point be $x$ m from the first pole and $(80 - x)$ m from the second; height $h$.", "$\\tan 60^\\circ = \\dfrac{h}{x}$, so $h = \\sqrt{3}x$.", "$\\tan 30^\\circ = \\dfrac{h}{80 - x}$, so $h = \\dfrac{80 - x}{\\sqrt{3}}$.",
   "$3x = 80 - x$, so $x = 20$.", "Height $= 20\\sqrt{3}$ m; the point is 20 m and 60 m from the poles."]),
 (11, 5, "A TV tower stands vertically on a bank of a canal. From a point on the other bank directly opposite the tower, the angle of elevation of the top of the tower is $60^\\circ$. From another point 20 m away from this point on the line joining this point to the foot of the tower, the angle of elevation of the top of the tower is $30^\\circ$. Find the height of the tower and the width of the canal.", "hard",
  ["Let the width be $w$ and the height $h$.", "$\\tan 60^\\circ = \\dfrac{h}{w}$, so $h = \\sqrt{3}w$.", "$\\tan 30^\\circ = \\dfrac{h}{w + 20}$, so $\\sqrt{3}h = w + 20$.", "$3w = w + 20$, so $w = 10$.", "The canal is 10 m wide and the tower is $10\\sqrt{3}$ m high."]),
 (12, 3, "From the top of a 7 m high building, the angle of elevation of the top of a cable tower is $60^\\circ$ and the angle of depression of its foot is $45^\\circ$. Determine the height of the tower.", "medium",
  ["Depression $45^\\circ$ to the foot: the distance between them $= 7$ m.", "Elevation $60^\\circ$: the part of the tower above the building's top $= 7\\tan 60^\\circ = 7\\sqrt{3}$ m.", "The tower is $7(\\sqrt{3} + 1)$ m high."]),
 (13, 5, "As observed from the top of a 75 m high lighthouse from the sea-level, the angles of depression of two ships are $30^\\circ$ and $45^\\circ$. If one ship is exactly behind the other on the same side of the lighthouse, find the distance between the two ships.", "hard",
  ["Nearer ship (depression $45^\\circ$): $\\tan 45^\\circ = \\dfrac{75}{d_1}$, so $d_1 = 75$ m.", "Farther ship (depression $30^\\circ$): $\\tan 30^\\circ = \\dfrac{75}{d_2}$, so $d_2 = 75\\sqrt{3}$ m.",
   "Distance between the ships $= d_2 - d_1$", "$= 75\\sqrt{3} - 75$", "$= 75(\\sqrt{3} - 1)$ m"]),
 (14, 5, "A 1.2 m tall girl spots a balloon moving with the wind in a horizontal line at a height of 88.2 m from the ground. The angle of elevation of the balloon from the eyes of the girl at any instant is $60^\\circ$. After some time, the angle of elevation reduces to $30^\\circ$. Find the distance travelled by the balloon during the interval.", "hard",
  ["Height of the balloon above her eyes $= 88.2 - 1.2 = 87$ m.", "At first: $\\tan 60^\\circ = \\dfrac{87}{d_1}$, so $d_1 = \\dfrac{87}{\\sqrt{3}} = 29\\sqrt{3}$.", "Later: $\\tan 30^\\circ = \\dfrac{87}{d_2}$, so $d_2 = 87\\sqrt{3}$.",
   "Distance travelled $= 87\\sqrt{3} - 29\\sqrt{3}$", "$= 58\\sqrt{3}$ m"]),
 (15, 5, "A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of $30^\\circ$, which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be $60^\\circ$. Find the time taken by the car to reach the foot of the tower from this point.", "hard",
  ["Let the tower be $h$ high. At first the car is $\\sqrt{3}h$ away (depression $30^\\circ$).", "Six seconds later it is $\\dfrac{h}{\\sqrt{3}}$ away (depression $60^\\circ$).", "Distance covered in 6 s $= \\sqrt{3}h - \\dfrac{h}{\\sqrt{3}} = \\dfrac{2h}{\\sqrt{3}}$.",
   "The remaining distance $\\dfrac{h}{\\sqrt{3}}$ is half of this.", "At the same speed it takes 3 seconds."]),
]
FIGS = {6: FIG_Q6, 10: FIG_Q10, 13: FIG_Q13}
for n, marks, text, diff, steps in EX:
    extra = {"figure": dict(FIGS[n])} if n in FIGS else {}
    q(f"ex9_1.q{n}", "short_answer" if marks == 3 else "long_answer", marks, [HD, ED] if n >= 12 else [HD], ex(n), text, diff, answer_steps=steps, marking_scheme=MS3 if marks == 3 else MS5, **extra)
# NCERT examples
q("eg_tower", "short_answer", 3, [HD], {"kind": "ncert_example"}, "A tower stands vertically on the ground. From a point on the ground, which is 15 m away from the foot of the tower, the angle of elevation of the top of the tower is found to be $60^\\circ$. Find the height of the tower.", "easy",
  answer_steps=["$\\tan 60^\\circ = \\dfrac{h}{15}$", "$h = 15\\sqrt{3}$", "The tower is $15\\sqrt{3}$ m high."], marking_scheme=MS3, figure=dict(FIG_EG1))
q("eg_chimney", "very_short_answer", 2, [HD], {"kind": "ncert_example"}, "An observer 1.5 m tall is 28.5 m away from a chimney. The angle of elevation of the top of the chimney from her eyes is $45^\\circ$. What is the height of the chimney?", "easy",
  answer_steps=["$\\tan 45^\\circ = \\dfrac{h - 1.5}{28.5}$, so $h - 1.5 = 28.5$.", "The chimney is 30 m high."], marking_scheme=["1 mark: ratio", "1 mark: answer including her height"])
q("eg_flagstaff", "short_answer", 3, [HD], {"kind": "ncert_example"}, "From a point P on the ground the angle of elevation of the top of a 10 m tall building is $30^\\circ$. A flag is hoisted at the top of the building and the angle of elevation of the top of the flagstaff from P is $45^\\circ$. Find the length of the flagstaff and the distance of the building from the point P.",
  answer_steps=["$\\tan 30^\\circ = \\dfrac{10}{PB}$, so $PB = 10\\sqrt{3}$ m.", "$\\tan 45^\\circ = \\dfrac{10 + x}{10\\sqrt{3}}$, so $x = 10\\sqrt{3} - 10$.", "Flagstaff $= 10(\\sqrt{3} - 1) \\approx 7.32$ m; distance $= 10\\sqrt{3} \\approx 17.32$ m."],
  marking_scheme=MS3, figure=dict(FIG_FLAG))
q("eg_shadow", "short_answer", 3, [HD], {"kind": "ncert_example"}, "The shadow of a tower standing on a level ground is found to be 40 m longer when the Sun's altitude is $30^\\circ$ than when it is $60^\\circ$. Find the height of the tower.",
  answer_steps=["$\\tan 60^\\circ = \\dfrac{h}{x}$, so $h = \\sqrt{3}x$.", "$\\tan 30^\\circ = \\dfrac{h}{x + 40}$, so $3x = x + 40$ and $x = 20$.", "$h = 20\\sqrt{3}$ m"], marking_scheme=MS3, figure=dict(FIG_SHADOW))
q("eg_buildings", "long_answer", 5, [HD, ED], {"kind": "ncert_example"}, "The angles of depression of the top and the bottom of an 8 m tall building from the top of a multi-storeyed building are $30^\\circ$ and $45^\\circ$, respectively. Find the height of the multi-storeyed building and the distance between the two buildings.", "hard",
  answer_steps=["Let the height of the multi-storeyed building be $H$ and the distance between the buildings $d$.", "Depression $45^\\circ$: $\\tan 45^\\circ = \\dfrac{H}{d}$, so $H = d$.", "Depression $30^\\circ$: $\\tan 30^\\circ = \\dfrac{H - 8}{d}$, so $d - 8 = \\dfrac{d}{\\sqrt{3}}$.",
                "$d\\left(1 - \\dfrac{1}{\\sqrt{3}}\\right) = 8$, so $d = \\dfrac{8\\sqrt{3}}{\\sqrt{3} - 1} = 4(3 + \\sqrt{3})$.", "Height $=$ distance $= 4(3 + \\sqrt{3})$ m"],
  marking_scheme=MS5, figure=dict(FIG_BUILD))
q("eg_river", "short_answer", 3, [HD, ED], {"kind": "ncert_example"}, "From a point on a bridge across a river, the angles of depression of the banks on opposite sides of the river are $30^\\circ$ and $45^\\circ$, respectively. If the bridge is at a height of 3 m from the banks, find the width of the river.",
  answer_steps=["Bank on the $45^\\circ$ side: distance $= \\dfrac{3}{\\tan 45^\\circ} = 3$ m.", "Bank on the $30^\\circ$ side: distance $= \\dfrac{3}{\\tan 30^\\circ} = 3\\sqrt{3}$ m.", "Width $= 3(\\sqrt{3} + 1)$ m"], marking_scheme=MS3)
# MCQs
mcq("mcq01", "The angle of elevation of the top of a tower from a point 30 m from its foot is $30^\\circ$. The height of the tower is:", ["$10\\sqrt{3}$ m", "$30\\sqrt{3}$ m", "$15$ m", "$10$ m"], 0, "$h = 30\\tan 30^\\circ = 10\\sqrt{3}$ m.")
mcq("mcq02", "A ladder 10 m long makes an angle of $60^\\circ$ with the ground. The height it reaches on the wall is:", ["$5\\sqrt{3}$ m", "$5$ m", "$10\\sqrt{3}$ m", "$20$ m"], 0, "$h = 10\\sin 60^\\circ = 5\\sqrt{3}$ m.")
mcq("mcq03", "A pole 6 m high casts a shadow $2\\sqrt{3}$ m long. The angle of elevation of the Sun is:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\tan \\theta = \\dfrac{6}{2\\sqrt{3}} = \\sqrt{3}$, so $\\theta = 60^\\circ$.", "medium")
mcq("mcq04", "As an observer walks towards a tower, the angle of elevation of its top:", ["increases", "decreases", "stays the same", "becomes zero"], 0, "The distance decreases while the height stays the same, so $\\tan \\theta$ and $\\theta$ increase.")
mcq("mcq05", "The angle of depression of a boat from the top of a 50 m high cliff is $45^\\circ$. The distance of the boat from the foot of the cliff is:", ["$50$ m", "$50\\sqrt{3}$ m", "$25$ m", "$100$ m"], 0, "$\\tan 45^\\circ = 1$, so the distance equals the height: 50 m.")
mcq("mcq06", "A kite string 100 m long makes an angle of $30^\\circ$ with the ground. The height of the kite is:", ["$50$ m", "$50\\sqrt{3}$ m", "$100\\sqrt{3}$ m", "$200$ m"], 0, "$h = 100\\sin 30^\\circ = 50$ m.")
mcq("mcq07", "If the length of the shadow of a pole is equal to its height, the angle of elevation of the Sun is:", ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0, "$\\tan \\theta = 1$, so $\\theta = 45^\\circ$.")
mcq("mcq08", "From the top of a 7 m high building, the angle of depression of the foot of a tower is $45^\\circ$. The distance between the building and the tower is:", ["$7$ m", "$7\\sqrt{3}$ m", "$\\dfrac{7}{\\sqrt{3}}$ m", "$14$ m"], 0, "$\\tan 45^\\circ = 1$, so the distance is 7 m.")
mcq("mcq09", "The ratio of the height of a tower to the length of its shadow is $\\sqrt{3} : 1$. The angle of elevation of the Sun is:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\tan \\theta = \\sqrt{3}$, so $\\theta = 60^\\circ$.")
mcq("mcq10", "The angle of depression from $A$ to $B$ equals the angle of elevation from $B$ to $A$ because they are:", ["alternate angles", "vertically opposite angles", "complementary angles", "supplementary angles"], 0,
    "Both are measured from horizontal lines, which are parallel, so they are alternate angles.", "medium")
mcq("mcq11", "A slide's top is 1.5 m high and it makes an angle of $30^\\circ$ with the ground. The length of the slide is:", ["$3$ m", "$1.5\\sqrt{3}$ m", "$0.75$ m", "$\\sqrt{3}$ m"], 0, "$\\sin 30^\\circ = \\dfrac{1.5}{L}$, so $L = 3$ m.")
mcq("mcq12", "The angle of elevation of the top of a tower $100\\sqrt{3}$ m high, from a point 100 m from its foot, is:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\tan \\theta = \\sqrt{3}$, so $\\theta = 60^\\circ$.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, [HD, ED], SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", "If the shadow of a pole is equal to its height, the Sun's angle of elevation is $45^\\circ$.", "$\\tan 45^\\circ = 1$.", 0, "$\\tan \\theta = \\dfrac{\\text{height}}{\\text{shadow}} = 1$, and $\\tan 45^\\circ = 1$ gives the angle.")
ar("ar2", "The angle of elevation of the top of a tower increases as one walks towards it.", "The height of the tower changes as one walks towards it.", 2, "A is true: the distance decreases. R is false: the height does not change.")
ar("ar3", "A ladder 10 m long that reaches a height of 5 m on a wall makes an angle of $60^\\circ$ with the ground.", "$\\sin 30^\\circ = \\dfrac{1}{2}$.", 3, "A is false: $\\sin \\theta = \\dfrac{5}{10} = \\dfrac{1}{2}$ gives $\\theta = 30^\\circ$. R is true.")
ar("ar4", "The angle of depression from $P$ to $Q$ is equal to the angle of elevation from $Q$ to $P$.", "They are alternate angles between parallel horizontal lines.", 0, "Alternate angles between parallel lines are equal, which is exactly why A holds.")
ar("ar5", "From a point 20 m away, the angle of elevation of the top of a 20 m high tower is $45^\\circ$.", "The angle of depression is measured below the horizontal.", 1, "A is true since $\\tan \\theta = 1$. R is true but is about depression, not about A.")

q("vsa1", "very_short_answer", 2, [HD], SHINE, "A pole 6 m high casts a shadow $2\\sqrt{3}$ m long on the ground. Find the Sun's angle of elevation.", "easy",
  answer_steps=["$\\tan \\theta = \\dfrac{6}{2\\sqrt{3}} = \\sqrt{3}$", "$\\theta = 60^\\circ$"], marking_scheme=["1 mark: ratio", "1 mark: angle"])
q("vsa2", "very_short_answer", 2, [HD], SHINE, "A ladder makes an angle of $60^\\circ$ with the ground, and its foot is 2 m from the wall. Find the length of the ladder.", "easy",
  answer_steps=["$\\cos 60^\\circ = \\dfrac{2}{L}$", "$L = 4$ m"], marking_scheme=["1 mark: ratio", "1 mark: length"])
q("sa1", "short_answer", 3, [HD, ED], SHINE, "From the top of a 10 m high house, the angle of elevation of the top of a tower is $60^\\circ$ and the angle of depression of its foot is $30^\\circ$. Find the height of the tower.",
  answer_steps=["Depression $30^\\circ$: distance $= \\dfrac{10}{\\tan 30^\\circ} = 10\\sqrt{3}$ m.", "Elevation $60^\\circ$: height above the house's top $= 10\\sqrt{3} \\times \\sqrt{3} = 30$ m.", "Tower $= 30 + 10 = 40$ m"], marking_scheme=MS3)
q("sa2", "short_answer", 3, [HD], SHINE, "The angle of elevation of the top of a hill from the foot of a tower is $60^\\circ$, and the angle of elevation of the top of the tower from the foot of the hill is $30^\\circ$. If the tower is 50 m high, find the height of the hill.", "medium",
  answer_steps=["From the foot of the hill: $\\tan 30^\\circ = \\dfrac{50}{d}$, so $d = 50\\sqrt{3}$ m.", "From the foot of the tower: $\\tan 60^\\circ = \\dfrac{H}{50\\sqrt{3}}$", "$H = 150$ m"], marking_scheme=MS3)
q("sa3", "short_answer", 3, [HD], SHINE, "The shadow of a tower is 20 m longer when the Sun's altitude is $45^\\circ$ than when it is $60^\\circ$. Find the height of the tower.", "hard",
  answer_steps=["Shorter shadow: $\\dfrac{h}{\\sqrt{3}}$; longer shadow: $h$.", "$h - \\dfrac{h}{\\sqrt{3}} = 20$, so $h = \\dfrac{20\\sqrt{3}}{\\sqrt{3} - 1}$.", "$h = 10\\sqrt{3}(\\sqrt{3} + 1) = 30 + 10\\sqrt{3} \\approx 47.32$ m"], marking_scheme=MS3)
q("la1", "long_answer", 5, [HD, ED], SHINE, "Two ships are on opposite sides of a lighthouse, in line with its foot. The angles of depression of the two ships from the top of the lighthouse, which is 100 m high, are $45^\\circ$ and $30^\\circ$. Find the distance between the ships. (Take $\\sqrt{3} = 1.732$)", "medium",
  answer_steps=["Let the lighthouse be $AB = 100$ m, with the ships at $C$ and $D$ on either side.", "$\\tan 45^\\circ = \\dfrac{100}{BC}$, so $BC = 100$ m.", "$\\tan 30^\\circ = \\dfrac{100}{BD}$, so $BD = 100\\sqrt{3}$ m.", "Distance $= BC + BD = 100(1 + \\sqrt{3})$", "$\\approx 273.2$ m"],
  marking_scheme=MS5)
q("la2", "long_answer", 5, [HD], SHINE, "The angle of elevation of a jet plane from a point on the ground is $60^\\circ$. After a flight of 15 seconds, the angle of elevation changes to $30^\\circ$. If the jet is flying at a constant height of $1500\\sqrt{3}$ m, find the speed of the jet in km/h.", "hard",
  answer_steps=["First position: horizontal distance $= \\dfrac{1500\\sqrt{3}}{\\tan 60^\\circ} = 1500$ m.", "Second position: horizontal distance $= \\dfrac{1500\\sqrt{3}}{\\tan 30^\\circ} = 4500$ m.", "Distance flown $= 3000$ m in 15 s.",
                "Speed $= 200$ m/s", "$= 200 \\times \\dfrac{18}{5} = 720$ km/h"], marking_scheme=MS5)
q("sqp38", "case_based", 4, [HD], SQP(38),
  "India Gate (formerly known as All India War Memorial) is located near Kartavya Path (formerly Rajpath) in New Delhi. It stands as a memorial to 74187 soldiers of the Indian Army who gave their lives in the First World War. This 42 m tall structure was designed by Sir Edwin Lutyens in the style of Roman triumphal arches. A student Shreya of height 1 m visited India Gate as a part of her study tour.\n\n(i) What is the angle of elevation from Shreya's eye to the top of India Gate, if she is standing at a distance of 41 m away from the India Gate? (1)\n\n(ii) If Shreya observes the angle of elevation from her eye to the top of India Gate to be $60^\\circ$, then how far is she standing from the base of the India Gate? (1)\n\n(iii) If the angle of elevation from Shreya's eye changes from $45^\\circ$ to $30^\\circ$ when she moves some distance back from the original position, find the distance she moves back. OR If Shreya moves to a point which is at a distance of $\\dfrac{41}{\\sqrt{3}}$ m from the India Gate, find the angle of elevation made by her eye to the top of India Gate. (2)",
  answer_steps=["Height of India Gate above her eye $= 42 - 1 = 41$ m.", "(i) $\\tan \\theta = \\dfrac{41}{41} = 1$, so the angle is $45^\\circ$.", "(ii) $\\tan 60^\\circ = \\dfrac{41}{x}$, so $x = \\dfrac{41}{\\sqrt{3}}$ m.",
                "(iii) $\\tan 30^\\circ = \\dfrac{41}{41 + x}$ gives $41 + x = 41\\sqrt{3}$, so she moves back $41(\\sqrt{3} - 1)$ m. OR $\\tan \\theta = \\dfrac{41}{41/\\sqrt{3}} = \\sqrt{3}$, so $\\theta = 60^\\circ$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"], figure=dict(FIG_GATE))
q("cb2", "case_based", 4, [HD, ED], SHINE,
  "A lighthouse is 60 m tall. From its top, a guard sees a boat at an angle of depression of $30^\\circ$. The boat sails straight towards the lighthouse, and later the angle of depression is $60^\\circ$.\n\n(i) How far was the boat from the lighthouse at first? (1)\n\n(ii) How far is it from the lighthouse later? (1)\n\n(iii) How far did the boat travel? OR If the boat sails at $2\\sqrt{3}$ m/s, how long did it take? (2)",
  answer_steps=["(i) $\\dfrac{60}{\\tan 30^\\circ} = 60\\sqrt{3}$ m", "(ii) $\\dfrac{60}{\\tan 60^\\circ} = 20\\sqrt{3}$ m", "(iii) $60\\sqrt{3} - 20\\sqrt{3} = 40\\sqrt{3}$ m. OR time $= \\dfrac{40\\sqrt{3}}{2\\sqrt{3}} = 20$ s"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch09.q.sqp"):
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
