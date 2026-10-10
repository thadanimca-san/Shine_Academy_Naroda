"""CBSE Class 10 Maths Ch 11: Areas Related to Circles.
Numerical answers are checked with exact fractions; figure coordinates are
computed so shaded sectors and segments really have the stated angles."""
import json, math, os, sys
from collections import Counter
from fractions import Fraction as Fr

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch11"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch11_areas_related_to_circles"
PI7, PI314 = Fr(22, 7), Fr(314, 100)

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def sector(theta, r, pi=PI7): return Fr(theta, 360) * pi * Fr(r) ** 2
def arc(theta, r, pi=PI7): return Fr(theta, 360) * 2 * pi * Fr(r)
def near(value, target, tol=0.005): return abs(float(value) - target) < tol

# ---------------------------------------------------------------- verification
check(sector(60, 6) == Fr(132, 7), "11.1 Q1")
check(sector(90, Fr(7, 2)) == Fr(77, 8) and 2 * PI7 * Fr(7, 2) == 22, "11.1 Q2")
check(sector(30, 14) == Fr(154, 3) and 5 * 6 == 30, "11.1 Q3")
check(sector(90, 10, PI314) == Fr(785, 10) and sector(90, 10, PI314) - 50 == Fr(285, 10) and PI314 * 100 - Fr(785, 10) == Fr(2355, 10), "11.1 Q4")
check(arc(60, 21) == 22 and sector(60, 21) == 231, "11.1 Q5")
s6 = sector(60, 15, PI314) - Fr(173, 100) / 4 * 225
check(s6 == Fr(204375, 10000) and PI314 * 225 - s6 == Fr(6860625, 10000), "11.1 Q6")
check(sector(120, 12, PI314) == Fr(15072, 100) and Fr(173, 100) / 4 * 144 == Fr(6228, 100) and Fr(15072 - 6228, 100) == Fr(8844, 100), "11.1 Q7")
check(sector(90, 5, PI314) == Fr(19625, 1000) and sector(90, 10, PI314) - sector(90, 5, PI314) == Fr(58875, 1000), "11.1 Q8")
check(PI7 * 35 + 5 * 35 == 285 and sector(36, Fr(35, 2)) == Fr(385, 4), "11.1 Q9")
check(sector(45, 45) == Fr(22275, 28) and near(Fr(22275, 28), 795.54), "11.1 Q10")
check(2 * sector(115, 25) == Fr(158125, 126) and near(Fr(158125, 126), 1254.96), "11.1 Q11")
check(sector(80, Fr(33, 2), PI314) == Fr(18997, 100), "11.1 Q12")
seg13 = sector(60, 28) - Fr(17, 10) / 4 * 784
check(6 * seg13 == Fr(4648, 10) and 6 * seg13 * Fr(35, 100) == Fr(16268, 100), "11.1 Q13")
check(sector(30, 4, PI314) == Fr(5024, 1200) and near(sector(30, 4, PI314), 4.19) and near(PI314 * 16 - Fr(419, 100), 46.05), "Example 1")
check(sector(120, 21) == 462, "Example 2 (sector; triangle 441√3/4 by OM = r/2, AB = r√3)")
check(sector(60, 1, Fr(1)) == Fr(1, 6), "sqp7: 8 segments of 60° with r = 1 (in terms of π)")
check(Fr(1, 2) * 22 * 21 == 231 and sector(Fr(22 * 360, 1) / (2 * PI7 * 21), 21) == 231, "sqp13")
check(sector(180, 14) == 308, "sqp24a: the three angles add up to 180°")
# sqp24b: major = 25π − (25π/4 − 25/2) = 75π/4 + 25/2 (coefficients of π and constant checked separately)
check((Fr(25) - Fr(25, 4), Fr(25, 2)) == (Fr(75, 4), Fr(25, 2)), "sqp24b")
check(arc(60, 21) == 22 and sector(90, 14) == 154 and sector(90, 7) == Fr(77, 2) and Fr(60, 360) == Fr(1, 6), "mcqs")
check(sector(90, 10, PI314) - 50 == Fr(285, 10) and 7 + 7 + arc(90, 7) == 25, "mcq07, mcq08")
check(sector(90, 14) == 154 and arc(60, 21) == 22, "ar1, ar3")
check(21 + 21 + arc(60, 21) == 64, "vsa1")
check(Fr(6) / 36 * 360 == 60, "vsa2: 6π = θ/360 × π × 36")
check(sector(60, 14) == Fr(308, 3) and near(Fr(308, 3) - 49 * 1.732, 17.80), "sa1")
check(Fr(88, 10) / (Fr(30, 360) * 2 * PI7) == Fr(168, 10), "sa2")
check(14 * 14 - 4 * sector(90, 7) == 42, "sa3")
la1_minor = sector(60, 10, PI314) - Fr(173, 100) / 4 * 100
check(near(la1_minor, 9.08) and near(PI314 * 100 - Fr(908, 100), 304.92), "la1")
la2_seg = sector(120, 21) - Fr(173, 100) / 4 * 441
check(arc(120, 21) == 44 and la2_seg == Fr(2712675, 10000) and PI7 * 441 - la2_seg == Fr(11147325, 10000), "la2")
check(sector(45, 14) == 77 and arc(45, 14) == 11 and 14 + 14 + 11 == 39, "cb1")
cb2 = sector(120, 7)
check(cb2 == Fr(154, 3) and arc(120, 7) == Fr(44, 3) and near(cb2 - Fr(173, 100) / 4 * 49, 30.14) and cb2 - sector(90, 7) == Fr(77, 6), "cb2")
two = 2 * (sector(120, 6, PI314) - Fr(173, 100) / 4 * 36)
check(near(two, 44.22), "mastery: two circles through each other's centres")

# ---------------------------------------------------------------- figures
def r9(p): return [round(p[0], 9), round(p[1], 9)]
def on(r, deg_, c=(0, 0)): return (c[0] + r * math.cos(math.radians(deg_)), c[1] + r * math.sin(math.radians(deg_)))
def fig(title, points, segments, **kw):
    f = {"type": "geometry_figure", "title": title, "points": {k: r9(v) for k, v in points.items()}, "segments": segments}
    f.update(kw); return f
def shade(kind, centre, a, b): return {"kind": kind, "centre": centre, "from": a, "to": b}

FIG_SECTOR = fig("Minor sector OAPB", {"O": (0, 0), "A": on(3, -10), "P": on(3, 30), "B": on(3, 70)},
                 [["O", "A"], ["O", "B"]], circles=[{"centre": "O", "radius": 3, "through": ["A", "P", "B"]}],
                 shaded=[shade("sector", "O", "A", "B")], angles=[{"points": ["A", "O", "B"], "label": "θ"}])
FIG_SEGMENT = fig("Segment cut off by the chord AB", {"O": (0, 0), "A": on(3, 30), "B": on(3, 150), "M": (0, 1.5)},
                  [["O", "A"], ["O", "B"], {"from": "A", "to": "B", "highlight": True}, {"from": "O", "to": "M", "dashed": True}],
                  circles=[{"centre": "O", "radius": 3, "through": ["A", "B"]}], shaded=[shade("segment", "O", "A", "B")],
                  right_angles=[["O", "M", "A"]], angles=[{"points": ["A", "O", "B"], "label": "120°"}])
FIG_MAJOR = fig("Major segment of a circle of radius 5 cm", {"O": (0, 0), "A": (5, 0), "B": (0, 5)},
                [["O", "A"], ["O", "B"], {"from": "A", "to": "B", "highlight": True}], circles=[{"centre": "O", "radius": 5, "through": ["A", "B"]}],
                shaded=[shade("segment", "O", "B", "A")], right_angles=[["A", "O", "B"]], lengths=[{"from": "O", "to": "A", "label": "5 cm"}])
FIG_HORSE = fig("Grazing area at corner A", {"A": (0, 0), "B": (15, 0), "C": (15, 15), "D": (0, 15), "P": (5, 0), "Q": (0, 5)},
                [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]], shaded=[shade("sector", "A", "P", "Q")],
                lengths=[{"from": "A", "to": "P", "label": "5 m"}, {"from": "B", "to": "C", "label": "15 m"}])
HEX = {n: on(28, 90 + 60 * i) for i, n in enumerate("ABCDEF")}
FIG_TABLE = fig("Six equal designs on the table cover", {"O": (0, 0), **HEX},
                [["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"], ["F", "A"], {"from": "O", "to": "A", "dashed": True}],
                circles=[{"centre": "O", "radius": 28, "through": list("ABCDEF")}],
                shaded=[shade("segment", "O", n, "ABCDEF"[(i + 1) % 6]) for i, n in enumerate("ABCDEF")],
                lengths=[{"from": "O", "to": "A", "label": "28 cm"}])
SQ = {"A": (0, 0), "B": (14, 0), "C": (14, 14), "D": (0, 14), "P": (7, 0), "Q": (14, 7), "R": (7, 14), "S": (0, 7)}
FIG_SQUARE = fig("Quadrants at the corners of square ABCD", SQ, [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]],
                 shaded=[shade("sector", "A", "P", "S"), shade("sector", "B", "Q", "P"), shade("sector", "C", "R", "Q"), shade("sector", "D", "S", "R")],
                 lengths=[{"from": "A", "to": "B", "label": "14 cm"}])
# Two circles of radius 6 through each other's centres: they meet where the chord subtends 120°.
X2, Y2 = (3, 3 * math.sqrt(3)), (3, -3 * math.sqrt(3))
FIG_TWO = fig("Two circles through each other's centres", {"O": (0, 0), "O′": (6, 0), "X": X2, "Y": Y2},
              [{"from": "X", "to": "Y", "highlight": True}, ["O", "O′"]],
              circles=[{"centre": "O", "radius": 6, "through": ["X", "Y", "O′"]}, {"centre": "O′", "radius": 6, "through": ["X", "Y", "O"]}],
              shaded=[shade("segment", "O", "Y", "X"), shade("segment", "O′", "X", "Y")])
check(abs(math.degrees(math.atan2(X2[1], X2[0]) - math.atan2(Y2[1], Y2[0])) - 120) < 1e-9, "two-circle figure angle")
# Olympic rings: radius 1, neighbouring centres √3 apart so each common chord is 1 cm (60° at each centre).
A_, B_ = 1.15, math.sqrt(3 - 1.15 ** 2)
RINGS = {"T1": (0, 0), "T2": (2 * A_, 0), "T3": (4 * A_, 0), "U1": (A_, -B_), "U2": (3 * A_, -B_)}
ring_points, ring_shades, ring_through = dict(RINGS), [], {n: [] for n in RINGS}
for k, (c1, c2) in enumerate([("T1", "U1"), ("T2", "U1"), ("T2", "U2"), ("T3", "U2")]):
    p1, p2 = RINGS[c1], RINGS[c2]
    d = math.dist(p1, p2); u = ((p2[0] - p1[0]) / d, (p2[1] - p1[1]) / d); n = (-u[1], u[0]); h = math.sqrt(1 - (d / 2) ** 2)
    m = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    X, Y = f"X{k + 1}", f"Y{k + 1}"
    ring_points[X], ring_points[Y] = (m[0] + h * n[0], m[1] + h * n[1]), (m[0] - h * n[0], m[1] - h * n[1])
    check(abs(math.dist(ring_points[X], ring_points[Y]) - 1) < 1e-9, "ring chord is 1 cm")
    ring_shades += [shade("segment", c1, Y, X), shade("segment", c2, X, Y)]
    ring_through[c1] += [X, Y]; ring_through[c2] += [X, Y]
FIG_RINGS = fig("Five rings of radius 1 cm", ring_points, [],
                circles=[{"centre": c, "radius": 1, "through": ring_through[c]} for c in RINGS], shaded=ring_shades,
                labels={n: "" for n in ring_points})

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch11.{id_}", "type": type_, **kw}
def placed(id_, figure): return {"id": f"ch11.{id_}", **figure}

sections = [
 {"id": "s1", "title": "Slices of a circle", "blocks": [
  blk("s1.hook", "hook", title="How big is one slice?",
    body="A round pizza is cut into 8 equal slices. Each slice is a **sector**: a part of the circle between two radii and an arc. "
         "Its corner angle is $360^\\circ \\div 8 = 45^\\circ$, so it is $\\dfrac{45}{360} = \\dfrac{1}{8}$ of the whole pizza.\n\n"
         "In this chapter you will find the area of such a slice, the length of its curved edge, and the area of the piece cut off by a straight chord."),
  blk("s1.inspiration", "inspiration", title="The number that measures every circle", person="Aryabhata", years="476–550 CE",
    body="In his book *Aryabhatiya*, written in 499 CE, the young astronomer Aryabhata gave this rule: add 4 to 100, multiply by 8 and add 62,000. "
         "The result is the circumference of a circle of diameter 20,000, *approximately*.\n\n"
         "That gives $\\pi \\approx \\dfrac{62832}{20000} = 3.1416$, correct to four decimal places. Aryabhata even used the word *āsanna*, 'approaching', "
         "as if he knew that $\\pi$ can never be written exactly as a fraction. Every area in this chapter uses his number.",
    quote="A good approximation, honestly labelled, is real knowledge.",
    future="Areas of sectors are used in designing gears, clock faces, fans, stadium seating, radar and lighthouse beams, and pie charts."),
  blk("s1.socratic", "socratic_question", question="A circle is cut into 8 equal sectors. What is the angle at the centre of each sector?",
    options=["$45^\\circ$", "$8^\\circ$", "$80^\\circ$"], correct_index=0, explanation="The full angle at the centre is $360^\\circ$, and $360^\\circ \\div 8 = 45^\\circ$."),
 ]},
 {"id": "s2", "title": "Sector and arc", "blocks": [
  blk("s2.reveal", "theory", title="Sectors and arcs", revision=True,
    body="The part of a circle between two radii and the arc joining their ends is a **sector**. The smaller one is the **minor sector**; the rest of the circle is the **major sector**.\n\n"
         "A sector of angle $\\theta$ is $\\dfrac{\\theta}{360}$ of the whole circle, so:\n\n"
         "- Area of the sector $= \\dfrac{\\theta}{360} \\times \\pi r^{2}$\n"
         "- Length of the arc $= \\dfrac{\\theta}{360} \\times 2 \\pi r$\n"
         "- Area of the major sector $= \\pi r^{2} -$ area of the minor sector (its angle is $360^\\circ - \\theta$)\n\n"
         "Dividing the two formulas gives a useful shortcut: area of the sector $= \\dfrac{1}{2} \\times l \\times r$, where $l$ is the arc length."),
  placed("s2.fig", FIG_SECTOR),
  blk("s2.eg1", "worked_example", title="NCERT Example 1",
    problem="Find the area of the sector of a circle with radius 4 cm and of angle $30^\\circ$. Also, find the area of the corresponding major sector. (Use $\\pi = 3.14$)",
    steps=["Area of the sector $= \\dfrac{30}{360} \\times 3.14 \\times 4 \\times 4 = \\dfrac{50.24}{12} \\approx 4.19$ cm²", "Area of the circle $= 3.14 \\times 16 = 50.24$ cm²",
           "Area of the major sector $= 50.24 - 4.19$"], answer="$4.19$ cm² (approx.) and $46.05$ cm² (approx.)"),
  blk("s2.eg2", "worked_example", title="CBSE sample paper",
    problem="Find the area of a sector of a circle of radius 21 cm cut off by an arc of length 22 cm.",
    steps=["Area of the sector $= \\dfrac{1}{2} \\times l \\times r$", "$= \\dfrac{1}{2} \\times 22 \\times 21$"], answer="$231$ cm²"),
  blk("s2.check", "knowledge_check", question="The area of a quadrant of a circle of radius 14 cm is:",
    options=["$154$ cm²", "$616$ cm²", "$22$ cm²", "$308$ cm²"], correct_index=0, explanation="$\\dfrac{90}{360} \\times \\dfrac{22}{7} \\times 14 \\times 14 = 154$ cm²."),
 ]},
 {"id": "s3", "title": "Segment of a circle", "blocks": [
  blk("s3.discovery", "discovery", title="Cut the slice with a straight line",
    body="Join the ends of the arc of a sector with a straight chord. The sector splits into two pieces: the triangle $OAB$ and the curved piece between the chord and the arc. "
         "That curved piece is a **segment**. So the segment is simply the sector with the triangle taken away."),
  placed("s3.fig", FIG_SEGMENT),
  blk("s3.thm", "theory", title="Area of a segment", revision=True,
    body="- Area of the minor segment $=$ area of the sector $-$ area of $\\triangle OAB$\n"
         "- Area of the major segment $= \\pi r^{2} -$ area of the minor segment\n\n"
         "The CBSE syllabus uses only the angles $60^\\circ$, $90^\\circ$ and $120^\\circ$, and the triangle is easy for each:\n\n"
         "- $60^\\circ$: $\\triangle OAB$ is equilateral, area $= \\dfrac{\\sqrt{3}}{4} r^{2}$\n"
         "- $90^\\circ$: right triangle, area $= \\dfrac{1}{2} r^{2}$\n"
         "- $120^\\circ$: draw $OM \\perp AB$. Then $OM = \\dfrac{r}{2}$ and $AB = \\sqrt{3}\\, r$, so the area $= \\dfrac{1}{2} \\times \\sqrt{3}\\, r \\times \\dfrac{r}{2} = \\dfrac{\\sqrt{3}}{4} r^{2}$"),
  blk("s3.eg1", "worked_example", title="NCERT Example 2",
    problem="Find the area of the segment of a circle of radius 21 cm, if the chord subtends $\\angle AOB = 120^\\circ$ at the centre. (Use $\\pi = \\dfrac{22}{7}$)",
    steps=["Area of the sector $= \\dfrac{120}{360} \\times \\dfrac{22}{7} \\times 21 \\times 21 = 462$ cm²", "Draw $OM \\perp AB$: $OM = \\dfrac{21}{2}$ cm and $AB = 21\\sqrt{3}$ cm.",
           "Area of $\\triangle OAB = \\dfrac{1}{2} \\times 21\\sqrt{3} \\times \\dfrac{21}{2} = \\dfrac{441\\sqrt{3}}{4}$ cm²"],
    answer="Area of the segment $= \\left(462 - \\dfrac{441\\sqrt{3}}{4}\\right)$ cm²"),
  blk("s3.eg2", "worked_example", title="CBSE sample paper",
    problem="Find the area of the major segment (in terms of $\\pi$) of a circle of radius 5 cm, formed by a chord subtending an angle of $90^\\circ$ at the centre.",
    steps=["Minor segment $= \\dfrac{90}{360} \\times \\pi \\times 5^{2} - \\dfrac{1}{2} \\times 5 \\times 5 = \\left(\\dfrac{25\\pi}{4} - \\dfrac{25}{2}\\right)$ cm²",
           "Major segment $= 25\\pi - \\left(\\dfrac{25\\pi}{4} - \\dfrac{25}{2}\\right)$"], answer="$\\left(\\dfrac{75\\pi}{4} + \\dfrac{25}{2}\\right)$ cm²"),
  placed("s3.fig2", FIG_MAJOR),
  blk("s3.check1", "knowledge_check", question="The area of the minor segment of a circle of radius 10 cm whose chord subtends $90^\\circ$ at the centre is ($\\pi = 3.14$):",
    options=["$28.5$ cm²", "$78.5$ cm²", "$50$ cm²", "$235.5$ cm²"], correct_index=0, explanation="Sector $78.5$ minus triangle $\\dfrac{1}{2} \\times 10 \\times 10 = 50$ gives $28.5$ cm²."),
  blk("s3.check2", "knowledge_check", question="The area of the minor segment + the area of the major segment of the same chord equals:",
    options=["the area of the circle", "the area of the major sector", "the area of the triangle", "the area of the minor sector"], correct_index=0,
    explanation="Together the two segments make up the whole circle."),
  blk("s3.memory", "memory_trick", title="Slice minus triangle", revision=True,
    body="- **Sector** = fraction of the circle: $\\dfrac{\\theta}{360}$ of $\\pi r^{2}$ (area) or of $2\\pi r$ (arc).\n"
         "- **Segment** = slice minus triangle.\n"
         "- **Major** = whole circle minus minor.\n"
         "- Clock: the minute hand turns $6^\\circ$ every minute, the hour hand $30^\\circ$ every hour."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Using the diameter in place of the radius.\n"
         "- Using $2\\pi r$ for area or $\\pi r^{2}$ for arc length.\n"
         "- Forgetting to subtract the triangle when a segment is asked.\n"
         "- Using $\\dfrac{\\theta}{180}$ instead of $\\dfrac{\\theta}{360}$.\n"
         "- Writing the perimeter of a sector as only the arc: the perimeter also includes the two radii.\n"
         "- Using a different value of $\\pi$ from the one given in the question."),
  blk("s3.tip", "teacher_tip", title="Fold a paper circle",
    body="Give each student a paper circle. Fold it into halves, quarters and eighths, and colour one piece: the fraction of the circle they coloured is the fraction $\\dfrac{\\theta}{360}$. "
         "Then draw the chord of the coloured piece and cut along it, so they literally hold the triangle and the segment separately."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why the area of a sector of angle $\\theta$ is $\\dfrac{\\theta}{360} \\times \\pi r^{2}$, and why a segment is smaller than its sector."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 10, Circles:** radii, chords and tangents give the triangles you subtract here.\n"
         "- **Chapter 12, Surface Areas and Volumes:** the curved surfaces of cylinders and cones are made from rectangles and sectors.\n"
         "- **Real life:** pie charts, wiper blades, fans, clock faces and lighthouse beams all sweep out sectors."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="Two circles of radius 6 cm are drawn so that each passes through the centre of the other. Find the area common to both circles. (Use $\\pi = 3.14$, $\\sqrt{3} = 1.73$)\n\n"
         "**Answer:** The common chord $XY$ subtends $120^\\circ$ at each centre, because $\\triangle OXO'$ is equilateral. Each segment is "
         "$\\dfrac{120}{360} \\times 3.14 \\times 36 - \\dfrac{\\sqrt{3}}{4} \\times 36 = 37.68 - 15.57 = 22.11$ cm². The common area is two such segments: $44.22$ cm²."),
  placed("s4.fig", FIG_TWO),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- Area of a sector of angle $\\theta$ $= \\dfrac{\\theta}{360} \\times \\pi r^{2}$\n"
         "- Length of an arc of angle $\\theta$ $= \\dfrac{\\theta}{360} \\times 2 \\pi r$\n"
         "- Area of a segment $=$ area of the sector $-$ area of the corresponding triangle\n"
         "- Area of the major sector or major segment $= \\pi r^{2} -$ the minor one"),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Use exactly the value of $\\pi$ (and $\\sqrt{3}$) given in the question; if none is given, CBSE expects $\\pi = \\dfrac{22}{7}$.\n"
         "- Write the formula first, then substitute: the formula step earns a mark.\n"
         "- When the answer is asked 'in terms of $\\pi$', do not substitute a value.\n"
         "- Always write units: cm for lengths, cm² for areas."),
  blk("s4.flash1", "flashcard", front="Area of a sector of angle $\\theta$", back="$\\dfrac{\\theta}{360} \\times \\pi r^{2}$"),
  blk("s4.flash2", "flashcard", front="Length of an arc of angle $\\theta$", back="$\\dfrac{\\theta}{360} \\times 2 \\pi r$"),
  blk("s4.flash3", "flashcard", front="Area of a segment", back="Area of the sector minus the area of the corresponding triangle."),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Areas Related to Circles",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 11,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: areas of sectors and segments of a circle, and problems on areas and perimeters of these figures; segments only with central angles of 60°, 90° and 120°.",
  "concepts": ["sector_arc", "segment", "applications"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
SC, SG, AP = "sector_arc", "segment", "applications"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "11.1", "question": n}
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch11.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS2 = ["1 mark: formula with values", "1 mark: answer with units"]
MS3S = ["1 mark: area of the sector", "1 mark: area of the triangle", "1 mark: area of the segment"]

q("ex11_1.q1", "very_short_answer", 2, [SC], ex(1), "Find the area of a sector of a circle with radius 6 cm if angle of the sector is $60^\\circ$.", "easy",
  answer_steps=["Area $= \\dfrac{60}{360} \\times \\dfrac{22}{7} \\times 6 \\times 6$", "$= \\dfrac{132}{7}$ cm²"], marking_scheme=MS2)
q("ex11_1.q2", "very_short_answer", 2, [SC], ex(2), "Find the area of a quadrant of a circle whose circumference is 22 cm.", "easy",
  answer_steps=["$2\\pi r = 22$ gives $r = \\dfrac{7}{2}$ cm.", "Area of the quadrant $= \\dfrac{1}{4} \\times \\dfrac{22}{7} \\times \\dfrac{7}{2} \\times \\dfrac{7}{2} = \\dfrac{77}{8}$ cm²"],
  marking_scheme=["1 mark: radius", "1 mark: area"])
q("ex11_1.q3", "very_short_answer", 2, [SC, AP], ex(3), "The length of the minute hand of a clock is 14 cm. Find the area swept by the minute hand in 5 minutes.", "easy",
  answer_steps=["In 5 minutes the minute hand turns through $5 \\times 6^\\circ = 30^\\circ$.", "Area $= \\dfrac{30}{360} \\times \\dfrac{22}{7} \\times 14 \\times 14 = \\dfrac{154}{3}$ cm²"],
  marking_scheme=["1 mark: angle $30^\\circ$", "1 mark: area"])
q("ex11_1.q4", "short_answer", 3, [SG], ex(4), "A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding: (i) minor segment (ii) major sector. (Use $\\pi = 3.14$)",
  answer_steps=["Minor sector $= \\dfrac{90}{360} \\times 3.14 \\times 10 \\times 10 = 78.5$ cm², and $\\triangle OAB = \\dfrac{1}{2} \\times 10 \\times 10 = 50$ cm².",
                "(i) Minor segment $= 78.5 - 50 = 28.5$ cm²", "(ii) Major sector $= 3.14 \\times 100 - 78.5 = 235.5$ cm²"],
  marking_scheme=["1 mark: minor sector and triangle", "1 mark: minor segment", "1 mark: major sector"])
q("ex11_1.q5", "short_answer", 3, [SC, SG], ex(5), "In a circle of radius 21 cm, an arc subtends an angle of $60^\\circ$ at the centre. Find: (i) the length of the arc (ii) area of the sector formed by the arc (iii) area of the segment formed by the corresponding chord",
  answer_steps=["(i) Arc $= \\dfrac{60}{360} \\times 2 \\times \\dfrac{22}{7} \\times 21 = 22$ cm", "(ii) Sector $= \\dfrac{60}{360} \\times \\dfrac{22}{7} \\times 21 \\times 21 = 231$ cm²",
                "(iii) The triangle is equilateral, area $\\dfrac{\\sqrt{3}}{4} \\times 21^{2} = \\dfrac{441\\sqrt{3}}{4}$ cm², so the segment $= \\left(231 - \\dfrac{441\\sqrt{3}}{4}\\right)$ cm²"],
  marking_scheme=["1 mark: arc", "1 mark: sector", "1 mark: segment"])
q("ex11_1.q6", "short_answer", 3, [SG], ex(6), "A chord of a circle of radius 15 cm subtends an angle of $60^\\circ$ at the centre. Find the areas of the corresponding minor and major segments of the circle. (Use $\\pi = 3.14$ and $\\sqrt{3} = 1.73$)",
  answer_steps=["Sector $= \\dfrac{60}{360} \\times 3.14 \\times 15 \\times 15 = 117.75$ cm²; equilateral $\\triangle OAB = \\dfrac{1.73}{4} \\times 225 = 97.3125$ cm².",
                "Minor segment $= 117.75 - 97.3125 = 20.4375$ cm²", "Major segment $= 3.14 \\times 225 - 20.4375 = 706.5 - 20.4375 = 686.0625$ cm²"], marking_scheme=MS3S[:2] + ["1 mark: both segments"])
q("ex11_1.q7", "short_answer", 3, [SG], ex(7), "A chord of a circle of radius 12 cm subtends an angle of $120^\\circ$ at the centre. Find the area of the corresponding segment of the circle. (Use $\\pi = 3.14$ and $\\sqrt{3} = 1.73$)",
  answer_steps=["Sector $= \\dfrac{120}{360} \\times 3.14 \\times 12 \\times 12 = 150.72$ cm²", "$\\triangle OAB = \\dfrac{\\sqrt{3}}{4} \\times 12^{2} = 36 \\times 1.73 = 62.28$ cm²",
                "Segment $= 150.72 - 62.28 = 88.44$ cm²"], marking_scheme=MS3S, figure=dict(FIG_SEGMENT))
q("ex11_1.q8", "short_answer", 3, [AP], ex(8), "A horse is tied to a peg at one corner of a square shaped grass field of side 15 m by means of a 5 m long rope. Find (i) the area of that part of the field in which the horse can graze. (ii) the increase in the grazing area if the rope were 10 m long instead of 5 m. (Use $\\pi = 3.14$)",
  answer_steps=["The horse grazes a quadrant (the corner angle is $90^\\circ$).", "(i) $\\dfrac{1}{4} \\times 3.14 \\times 5^{2} = 19.625$ m²",
                "(ii) With 10 m: $\\dfrac{1}{4} \\times 3.14 \\times 10^{2} = 78.5$ m², so the increase $= 78.5 - 19.625 = 58.875$ m²"],
  marking_scheme=["1 mark: quadrant", "1 mark: (i)", "1 mark: (ii)"], figure=dict(FIG_HORSE))
q("ex11_1.q9", "short_answer", 3, [SC, AP], ex(9), "A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters which divide the circle into 10 equal sectors. Find: (i) the total length of the silver wire required. (ii) the area of each sector of the brooch.",
  answer_steps=["(i) Circumference $= \\dfrac{22}{7} \\times 35 = 110$ mm; five diameters $= 5 \\times 35 = 175$ mm.", "Total wire $= 110 + 175 = 285$ mm",
                "(ii) Each sector $= \\dfrac{1}{10} \\times \\dfrac{22}{7} \\times \\dfrac{35}{2} \\times \\dfrac{35}{2} = \\dfrac{385}{4}$ mm²"],
  marking_scheme=["1 mark: circumference", "1 mark: total wire", "1 mark: sector area"])
q("ex11_1.q10", "very_short_answer", 2, [SC, AP], ex(10), "An umbrella has 8 ribs which are equally spaced. Assuming umbrella to be a flat circle of radius 45 cm, find the area between the two consecutive ribs of the umbrella.", "easy",
  answer_steps=["Each sector has angle $\\dfrac{360^\\circ}{8} = 45^\\circ$.", "Area $= \\dfrac{45}{360} \\times \\dfrac{22}{7} \\times 45 \\times 45 = \\dfrac{22275}{28} \\approx 795.54$ cm²"],
  marking_scheme=["1 mark: angle", "1 mark: area"])
q("ex11_1.q11", "short_answer", 3, [SC, AP], ex(11), "A car has two wipers which do not overlap. Each wiper has a blade of length 25 cm sweeping through an angle of $115^\\circ$. Find the total area cleaned at each sweep of the blades.",
  answer_steps=["Each blade sweeps a sector of radius 25 cm and angle $115^\\circ$.", "Area of one sector $= \\dfrac{115}{360} \\times \\dfrac{22}{7} \\times 25 \\times 25 = \\dfrac{158125}{252}$ cm²",
                "Total $= 2 \\times \\dfrac{158125}{252} = \\dfrac{158125}{126} \\approx 1254.96$ cm²"], marking_scheme=["1 mark: sector", "1 mark: one blade", "1 mark: total"])
q("ex11_1.q12", "very_short_answer", 2, [SC, AP], ex(12), "To warn ships for underwater rocks, a lighthouse spreads a red coloured light over a sector of angle $80^\\circ$ to a distance of 16.5 km. Find the area of the sea over which the ships are warned. (Use $\\pi = 3.14$)",
  answer_steps=["Area $= \\dfrac{80}{360} \\times 3.14 \\times 16.5 \\times 16.5$", "$= 189.97$ km²"], marking_scheme=MS2)
q("ex11_1.q13", "long_answer", 5, [SG, AP], ex(13), "A round table cover has six equal designs as shown in the figure. If the radius of the cover is 28 cm, find the cost of making the designs at the rate of ₹ 0.35 per cm². (Use $\\sqrt{3} = 1.7$)", "hard",
  answer_steps=["The six chords form a regular hexagon, so each chord subtends $60^\\circ$ at the centre and each triangle is equilateral.",
                "Sector $= \\dfrac{60}{360} \\times \\dfrac{22}{7} \\times 28 \\times 28 = \\dfrac{1232}{3}$ cm²", "Triangle $= \\dfrac{\\sqrt{3}}{4} \\times 28^{2} = 196 \\times 1.7 = 333.2$ cm²",
                "Six designs $= 6 \\times \\left(\\dfrac{1232}{3} - 333.2\\right) = 2464 - 1999.2 = 464.8$ cm²", "Cost $= 464.8 \\times 0.35 =$ ₹ 162.68"],
  marking_scheme=["1 mark: angle $60^\\circ$", "1 mark: sector", "1 mark: triangle", "1 mark: area of the designs", "1 mark: cost"], figure=dict(FIG_TABLE))
mcq("ex11_1.q14", [SC], "Tick the correct answer: Area of a sector of angle $p$ (in degrees) of a circle with radius $R$ is",
    ["$\\dfrac{p}{180} \\times 2\\pi R$", "$\\dfrac{p}{180} \\times \\pi R^{2}$", "$\\dfrac{p}{360} \\times 2\\pi R$", "$\\dfrac{p}{720} \\times 2\\pi R^{2}$"], 3,
    "$\\dfrac{p}{720} \\times 2\\pi R^{2} = \\dfrac{p}{360} \\times \\pi R^{2}$, the area of the sector.", "medium", source=ex(14))
# Sample paper
mcq("sqp7", [SG], "The Olympic rings are made of five congruent circles of radius 1 cm, intersecting so that the chord joining the points of intersection of two circles is also of length 1 cm. The total area of all the regions common to two rings (assuming the thickness of the rings to be negligible) is",
    ["$4\\left[\\dfrac{\\pi}{12} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²", "$\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²", "$4\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²", "$8\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm²"], 3,
    "A chord of 1 cm in a circle of radius 1 cm makes an equilateral triangle, so it subtends $60^\\circ$. Each common region is 2 segments, and there are 4 such regions: $8\\left[\\dfrac{\\pi}{6} - \\dfrac{\\sqrt{3}}{4}\\right]$ cm².",
    "hard", source=SQP(7))
Q[-1]["figure"] = dict(FIG_RINGS)
mcq("sqp13", [SC], "The area (in cm²) of a sector of a circle of radius 21 cm cut off by an arc of length 22 cm is", ["$441$", "$321$", "$231$", "$221$"], 2,
    "Area $= \\dfrac{1}{2} \\times l \\times r = \\dfrac{1}{2} \\times 22 \\times 21 = 231$.", "medium", source=SQP(13))
q("sqp24a", "very_short_answer", 2, [SC, AP], SQP("24(A)"), "A horse, a cow and a goat are tied, each by ropes of length 14 m, at the corners A, B and C respectively, of a grassy triangular field ABC with sides of lengths 35 m, 40 m and 50 m. Find the area of grass field that can be grazed by them.", "hard",
  answer_steps=["Each animal grazes a sector of radius 14 m; the angles are $\\angle A$, $\\angle B$, $\\angle C$, and $\\angle A + \\angle B + \\angle C = 180^\\circ$.",
                "Total area $= \\dfrac{180}{360} \\times \\dfrac{22}{7} \\times 14 \\times 14 = 308$ m²"], marking_scheme=["1 mark: sum of angles $180^\\circ$", "1 mark: area"])
q("sqp24b", "very_short_answer", 2, [SG], SQP("24(B)"), "Find the area of the major segment (in terms of $\\pi$) of a circle of radius 5 cm, formed by a chord subtending an angle of $90^\\circ$ at the centre.",
  answer_steps=["Minor segment $= \\dfrac{90}{360} \\times \\pi \\times 5^{2} - \\dfrac{1}{2} \\times 5^{2} = \\left(\\dfrac{25\\pi}{4} - \\dfrac{25}{2}\\right)$ cm²",
                "Major segment $= 25\\pi - \\left(\\dfrac{25\\pi}{4} - \\dfrac{25}{2}\\right) = \\left(\\dfrac{75\\pi}{4} + \\dfrac{25}{2}\\right)$ cm²"],
  marking_scheme=["1 mark: minor segment", "1 mark: major segment"], figure=dict(FIG_MAJOR))
# Shine MCQs
mcq("mcq01", [SC], "The length of an arc of a sector of angle $\\theta$ of a circle of radius $r$ is:",
    ["$\\dfrac{\\theta}{360} \\times 2\\pi r$", "$\\dfrac{\\theta}{360} \\times \\pi r^{2}$", "$\\dfrac{\\theta}{180} \\times \\pi r^{2}$", "$\\dfrac{\\theta}{720} \\times \\pi r$"], 0, "The arc is the fraction $\\dfrac{\\theta}{360}$ of the circumference $2\\pi r$.")
mcq("mcq02", [SC], "The area of a quadrant of a circle of radius 14 cm is:", ["$154$ cm²", "$616$ cm²", "$44$ cm²", "$308$ cm²"], 0, "$\\dfrac{1}{4} \\times \\dfrac{22}{7} \\times 196 = 154$ cm².")
mcq("mcq03", [AP], "In 15 minutes, the minute hand of a clock turns through:", ["$90^\\circ$", "$15^\\circ$", "$60^\\circ$", "$180^\\circ$"], 0, "It turns $6^\\circ$ every minute: $15 \\times 6^\\circ = 90^\\circ$.")
mcq("mcq04", [SC], "The length of an arc of a circle of radius 21 cm which subtends $60^\\circ$ at the centre is:", ["$22$ cm", "$44$ cm", "$231$ cm", "$11$ cm"], 0, "$\\dfrac{60}{360} \\times 2 \\times \\dfrac{22}{7} \\times 21 = 22$ cm.", "medium")
mcq("mcq05", [SC], "The area of a sector of angle $90^\\circ$ of a circle of radius 7 cm is:", ["$38.5$ cm²", "$154$ cm²", "$11$ cm²", "$77$ cm²"], 0, "$\\dfrac{1}{4} \\times \\dfrac{22}{7} \\times 49 = 38.5$ cm².")
mcq("mcq06", [SC], "If the area of a sector is $\\dfrac{1}{6}$ of the area of its circle, the angle of the sector is:", ["$60^\\circ$", "$30^\\circ$", "$6^\\circ$", "$120^\\circ$"], 0, "$\\dfrac{\\theta}{360} = \\dfrac{1}{6}$ gives $\\theta = 60^\\circ$.")
mcq("mcq07", [SG], "The area of the minor segment of a circle of radius 10 cm whose chord subtends $90^\\circ$ at the centre is ($\\pi = 3.14$):", ["$28.5$ cm²", "$78.5$ cm²", "$50$ cm²", "$235.5$ cm²"], 0,
    "Sector $78.5$ cm² minus triangle $50$ cm².", "medium")
mcq("mcq08", [SC], "The perimeter of a sector of angle $90^\\circ$ of a circle of radius 7 cm is:", ["$25$ cm", "$11$ cm", "$18$ cm", "$38.5$ cm"], 0, "Arc $11$ cm plus two radii: $11 + 7 + 7 = 25$ cm.", "medium")
mcq("mcq09", [SG], "Area of the minor segment + area of the major segment of the same chord equals:", ["the area of the circle", "the area of the major sector", "the area of the triangle", "the area of the minor sector"], 0,
    "Together the two segments make up the whole circle.")
mcq("mcq10", [SC], "The area of a sector with arc length $l$ and radius $r$ is:", ["$\\dfrac{1}{2} l r$", "$l r$", "$2 l r$", "$\\pi l r$"], 0, "Dividing the area by the arc length gives $\\dfrac{r}{2}$, so the area is $\\dfrac{1}{2} l r$.", "medium")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [SC], "The area of a sector of angle $90^\\circ$ of a circle of radius 14 cm is 154 cm².", "The area of a sector of angle $\\theta$ is $\\dfrac{\\theta}{360} \\times \\pi r^{2}$.", 0,
   "R gives $\\dfrac{90}{360} \\times \\dfrac{22}{7} \\times 196 = 154$ cm².")
ar("ar2", [SC], "If the angle of a sector is doubled, its area is doubled.", "The area of a sector is proportional to its angle.", 0, "Area $= \\dfrac{\\theta}{360} \\times \\pi r^{2}$ grows in the same ratio as $\\theta$: R explains A.")
ar("ar3", [SC], "The length of an arc of angle $60^\\circ$ of a circle of radius 21 cm is 22 cm.", "The area of a circle is $\\pi r^{2}$.", 1, "Both are true, but the arc length comes from $2\\pi r$, not from the area.")
ar("ar4", [SG], "The area of the minor segment of a circle of radius 10 cm, whose chord subtends $90^\\circ$ at the centre, is 50 cm².", "Area of a segment = area of the sector − area of the corresponding triangle.", 3,
   "A is false: $78.5 - 50 = 28.5$ cm² ($\\pi = 3.14$). R is true.")
ar("ar5", [AP], "The minute hand of a clock turns through $6^\\circ$ in one minute.", "The minute hand completes one round in 30 minutes.", 2, "A is true. R is false: one round takes 60 minutes.")

q("vsa1", "very_short_answer", 2, [SC], SHINE, "Find the perimeter of a sector of a circle of radius 21 cm and angle $60^\\circ$.", "easy",
  answer_steps=["Arc $= \\dfrac{60}{360} \\times 2 \\times \\dfrac{22}{7} \\times 21 = 22$ cm", "Perimeter $= 22 + 21 + 21 = 64$ cm"], marking_scheme=["1 mark: arc", "1 mark: perimeter"])
q("vsa2", "very_short_answer", 2, [SC], SHINE, "The area of a sector of a circle of radius 6 cm is $6\\pi$ cm². Find the angle of the sector.", "easy",
  answer_steps=["$\\dfrac{\\theta}{360} \\times \\pi \\times 36 = 6\\pi$", "$\\theta = 60^\\circ$"], marking_scheme=["1 mark: equation", "1 mark: angle"])
q("sa1", "short_answer", 3, [SG], SHINE, "Find the area of the minor segment of a circle of radius 14 cm, when the angle of the corresponding sector is $60^\\circ$. (Use $\\sqrt{3} = 1.732$)",
  answer_steps=["Sector $= \\dfrac{60}{360} \\times \\dfrac{22}{7} \\times 14 \\times 14 = \\dfrac{308}{3} \\approx 102.67$ cm²", "Equilateral triangle $= \\dfrac{\\sqrt{3}}{4} \\times 196 = 49\\sqrt{3} \\approx 84.87$ cm²",
                "Segment $\\approx 102.67 - 84.87 = 17.80$ cm²"], marking_scheme=MS3S)
q("sa2", "short_answer", 3, [SC, AP], SHINE, "A pendulum swings through an angle of $30^\\circ$ and describes an arc 8.8 cm in length. Find the length of the pendulum.",
  answer_steps=["The pendulum is the radius $r$, and $\\dfrac{30}{360} \\times 2 \\times \\dfrac{22}{7} \\times r = 8.8$.", "$\\dfrac{11}{21} r = 8.8$", "$r = 16.8$ cm"],
  marking_scheme=["1 mark: arc formula", "1 mark: equation", "1 mark: length"])
q("sa3", "short_answer", 3, [AP], SHINE, "Quadrants of radius 7 cm are drawn at the four corners of a square ABCD of side 14 cm. Find the area of the part of the square not covered by the quadrants.", "easy",
  answer_steps=["Four quadrants make one full circle of radius 7 cm: $\\dfrac{22}{7} \\times 7 \\times 7 = 154$ cm².", "Square $= 14 \\times 14 = 196$ cm²", "Uncovered part $= 196 - 154 = 42$ cm²"],
  marking_scheme=["1 mark: four quadrants", "1 mark: square", "1 mark: answer"], figure=dict(FIG_SQUARE))
q("la1", "long_answer", 5, [SG], SHINE, "A chord PQ of a circle of radius 10 cm subtends an angle of $60^\\circ$ at the centre. Find the areas of the minor and major segments. (Use $\\pi = 3.14$, $\\sqrt{3} = 1.73$)",
  answer_steps=["Sector $= \\dfrac{60}{360} \\times 3.14 \\times 100 \\approx 52.33$ cm²", "$\\triangle OPQ$ is equilateral: area $= \\dfrac{1.73}{4} \\times 100 = 43.25$ cm²",
                "Minor segment $\\approx 52.33 - 43.25 = 9.08$ cm²", "Circle $= 3.14 \\times 100 = 314$ cm²", "Major segment $\\approx 314 - 9.08 = 304.92$ cm²"],
  marking_scheme=["1 mark: sector", "1 mark: triangle", "1 mark: minor segment", "1 mark: circle", "1 mark: major segment"])
q("la2", "long_answer", 5, [SC, SG], SHINE, "An arc of a circle of radius 21 cm subtends an angle of $120^\\circ$ at the centre. Find (i) the length of the arc, (ii) the area of the minor sector, (iii) the area of the minor segment, (iv) the area of the major segment. (Use $\\sqrt{3} = 1.73$)", "hard",
  answer_steps=["(i) Arc $= \\dfrac{120}{360} \\times 2 \\times \\dfrac{22}{7} \\times 21 = 44$ cm", "(ii) Sector $= \\dfrac{120}{360} \\times \\dfrac{22}{7} \\times 441 = 462$ cm²",
                "Triangle $= \\dfrac{\\sqrt{3}}{4} \\times 441 = \\dfrac{1.73 \\times 441}{4} = 190.7325$ cm²", "(iii) Minor segment $= 462 - 190.7325 = 271.2675$ cm²",
                "(iv) Major segment $= \\dfrac{22}{7} \\times 441 - 271.2675 = 1386 - 271.2675 = 1114.7325$ cm²"],
  marking_scheme=["1 mark: arc", "1 mark: sector", "1 mark: triangle", "1 mark: minor segment", "1 mark: major segment"], figure=dict(FIG_SEGMENT))
q("cb1", "case_based", 4, [SC, AP], SHINE,
  "A round pizza of diameter 28 cm is cut into 8 equal slices.\n\n(i) Find the angle at the centre of each slice. (1)\n\n(ii) Find the area of one slice. (1)\n\n(iii) Find the length of the curved crust of one slice. OR Find the perimeter of one slice. (2)",
  answer_steps=["(i) $360^\\circ \\div 8 = 45^\\circ$", "(ii) $\\dfrac{45}{360} \\times \\dfrac{22}{7} \\times 14 \\times 14 = 77$ cm²",
                "(iii) Arc $= \\dfrac{45}{360} \\times 2 \\times \\dfrac{22}{7} \\times 14 = 11$ cm. OR Perimeter $= 11 + 14 + 14 = 39$ cm."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [SC, SG, AP], SHINE,
  "A garden sprinkler throws water up to 7 m and turns back and forth through an angle of $120^\\circ$.\n\n(i) Find the area of the lawn watered. (1)\n\n(ii) Find the length of the outer edge (arc) of the watered region. (1)\n\n(iii) Find the area between that arc and the straight line joining its ends (use $\\sqrt{3} = 1.73$). OR If the angle is reduced to $90^\\circ$, how much less area is watered? (2)",
  answer_steps=["(i) $\\dfrac{120}{360} \\times \\dfrac{22}{7} \\times 7 \\times 7 = \\dfrac{154}{3} \\approx 51.33$ m²", "(ii) $\\dfrac{120}{360} \\times 2 \\times \\dfrac{22}{7} \\times 7 = \\dfrac{44}{3} \\approx 14.67$ m",
                "(iii) Triangle $= \\dfrac{1.73}{4} \\times 49 \\approx 21.19$ m², so the segment $\\approx 51.33 - 21.19 = 30.14$ m². OR $\\dfrac{154}{3} - \\dfrac{77}{2} = \\dfrac{77}{6} \\approx 12.83$ m² less."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch11.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
