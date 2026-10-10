"""CBSE Class 10 Maths Ch 7: Coordinate Geometry.
Every distance, section point and unknown is checked with sympy."""
import json, os, sys
from collections import Counter
from sympy import sqrt, Rational as R, simplify, symbols, solve, Eq, nsimplify

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch07"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch07_coordinate_geometry"
x, y, k, a, b = symbols("x y k a b")

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def d(p, q): return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
def sec(p, q, m, n): return ((m * q[0] + n * p[0]) / R(m + n), (m * q[1] + n * p[1]) / R(m + n))
def same(u, v): return simplify(u - v) == 0

# ---------------------------------------------------------------- verification
check(same(d((2, 3), (4, 1)), 2 * sqrt(2)) and same(d((-5, 7), (-1, 3)), 4 * sqrt(2)), "7.1 Q1")
check(simplify(d((a, b), (-a, -b)) - 2 * sqrt(a ** 2 + b ** 2)) == 0, "7.1 Q1 iii")
check(d((0, 0), (36, 15)) == 39, "7.1 Q2")
ab, bc, ac = d((1, 5), (2, 3)), d((2, 3), (-2, -11)), d((1, 5), (-2, -11))
check(same(ab, sqrt(5)) and same(bc, 2 * sqrt(53)) and same(ac, sqrt(265)) and abs(float(ab + bc - ac)) > 0.1 and abs(float(ab + ac - bc)) > 0.1 and abs(float(bc + ac - ab)) > 0.1, "7.1 Q3 not collinear")
check(d((5, -2), (6, 4)) == d((6, 4), (7, -2)) == sqrt(37) and d((5, -2), (7, -2)) == 2, "7.1 Q4")
SQ = [(3, 4), (6, 7), (9, 4), (6, 1)]
check(all(d(SQ[i], SQ[(i + 1) % 4]) == sqrt(18) for i in range(4)) and d(SQ[0], SQ[2]) == d(SQ[1], SQ[3]) == 6, "7.1 Q5 square")
Q6i = [(-1, -2), (1, 0), (-1, 2), (-3, 0)]
check(all(d(Q6i[i], Q6i[(i + 1) % 4]) == sqrt(8) for i in range(4)) and d(Q6i[0], Q6i[2]) == d(Q6i[1], Q6i[3]) == 4, "7.1 Q6 i")
check(R(3 - 5, 0 + 3) == R(1 - 3, 3 - 0), "7.1 Q6 ii collinear (-3,5),(0,3),(3,1)")
Q6iii = [(4, 5), (7, 6), (4, 3), (1, 2)]
check(d(Q6iii[0], Q6iii[1]) == d(Q6iii[2], Q6iii[3]) == sqrt(10) and d(Q6iii[1], Q6iii[2]) == d(Q6iii[3], Q6iii[0]) == sqrt(18) and d(Q6iii[0], Q6iii[2]) != d(Q6iii[1], Q6iii[3]), "7.1 Q6 iii")
check(solve(Eq((x - 2) ** 2 + 25, (x + 2) ** 2 + 81), x) == [-7], "7.1 Q7")
check(set(solve(Eq(64 + (y + 3) ** 2, 100), y)) == {3, -9}, "7.1 Q8")
check(set(solve(Eq(25 + 16, x ** 2 + 25), x)) == {4, -4} and d((0, 1), (4, 6)) == sqrt(41) and d((5, -3), (4, 6)) == sqrt(82) and d((5, -3), (-4, 6)) == 9 * sqrt(2), "7.1 Q9")
check(simplify(((x - 3) ** 2 + (y - 6) ** 2 - (x + 3) ** 2 - (y - 4) ** 2) + 4 * (3 * x + y - 5)) == 0, "7.1 Q10")
check(sec((-1, 7), (4, -3), 2, 3) == (1, 3), "7.2 Q1")
check(sec((4, -1), (-2, -3), 1, 2) == (2, R(-5, 3)) and sec((4, -1), (-2, -3), 2, 1) == (0, R(-7, 3)), "7.2 Q2")
check(d((2, 25), (8, 20)) == sqrt(61) and ((2 + 8) / R(2), (25 + 20) / R(2)) == (5, R(45, 2)), "7.2 Q3")
check(solve(Eq((6 * k - 3) / (k + 1), -1), k) == [R(2, 7)] and sec((-3, 10), (6, -8), 2, 7) == (-1, 6), "7.2 Q4")
check(solve(Eq((5 * k - 5) / (k + 1), 0), k) == [1] and sec((1, -5), (-4, 5), 1, 1) == (R(-3, 2), 0), "7.2 Q5")
check(solve(Eq((1 + x) / 2, R(7, 2)), x) == [6] and solve(Eq(R(2 + 6, 2), (y + 5) / 2), y) == [3], "7.2 Q6")
check((2 * 2 - 1, 2 * -3 - 4) == (3, -10), "7.2 Q7")
check(sec((-2, -2), (2, -4), 3, 4) == (R(-2, 7), R(-20, 7)), "7.2 Q8")
check([sec((-2, 2), (2, 8), m, 4 - m) for m in (1, 2, 3)] == [(-1, R(7, 2)), (0, 5), (1, R(13, 2))], "7.2 Q9")
check(d((3, 0), (-1, 4)) * d((4, 5), (-2, -1)) / 2 == 24, "7.2 Q10")
# examples
P, Qp, Rp = (3, 2), (-2, -3), (2, 3)
check(d(P, Qp) ** 2 + d(P, Rp) ** 2 == d(Qp, Rp) ** 2, "eg right triangle")
check(sec((4, -3), (8, 5), 3, 1) == (7, 3), "eg section"); check(solve(Eq((3 * k - 6) / (k + 1), -4), k) == [R(2, 7)] and sec((-6, 10), (3, -8), 2, 7) == (-4, 6), "eg ratio")
check(sec((2, -2), (-7, 4), 1, 2) == (-1, 0) and sec((2, -2), (-7, 4), 2, 1) == (-4, 2), "eg trisection")
check(solve(Eq((-1 * k + 5) / (k + 1), 0), k) == [5] and sec((5, -6), (-1, -4), 5, 1) == (0, R(-13, 3)), "eg y-axis")
check(((6 + 9) / R(2), (1 + 4) / R(2)) == ((8 + 7) / R(2), (2 + 3) / R(2)), "eg parallelogram p = 7")
check(solve(Eq(36 + (y - 5) ** 2, 16 + (y - 3) ** 2), y) == [9], "mastery")
check(d((1, 2), (5, 5)) == 5, "lesson figure"); check(sec((1, 1), (7, 4), 2, 1) == (5, 3), "section figure")
# lesson checks, MCQs, Shine
check(d((0, 0), (3, 4)) == 5 and d((2, 3), (5, 7)) == 5 and ((2 + 6) / R(2), (5 - 1) / R(2)) == (4, 2), "mcq01-03")
check(sec((0, 0), (6, 9), 1, 2) == (2, 3) and d((0, 0), (-6, 8)) == 10 and set(solve(Eq(9 + y ** 2, 25), y)) == {4, -4}, "mcq05-07")
check(d((0, 0), (3, 0)) + d((0, 0), (0, 4)) + d((3, 0), (0, 4)) == 12 and (2 * 0 - 3, 2 * 0 + 2) == (-3, 2), "mcq09-10")
check(d((-7, 0), (2, -5)) == d((-7, 0), (-2, 9)), "ar4")
check(solve(Eq((x / 2 + x + 1) / 2, 5), x) == [6] and solve(Eq(((y + 1) / 2 + y - 3) / 2, -2), y) == [-1], "vsa1")
check(solve(Eq(25 + (y + 2) ** 2, 9 + (y - 2) ** 2), y) == [-2], "vsa2")
SQ2 = [(1, 7), (4, 2), (-1, -1), (-4, 4)]
check(all(d(SQ2[i], SQ2[(i + 1) % 4]) == sqrt(34) for i in range(4)) and d(SQ2[0], SQ2[2]) == d(SQ2[1], SQ2[3]) == sqrt(68), "sa1")
check(solve(Eq((-2 + 4) / R(2), (a + 1) / 2), a) == [1] and solve(Eq((1 + b) / 2, R(0 + 2, 2)), b) == [1], "sa2")
check(solve(Eq((3 * 8 * a + 3 * a + 1) / 4, 9 * a - 2), a) == [1] and (3 * 5 + 1 * -3) / R(4) == 3, "sa3 a = 1, b = -3")
check(d((3, 0), (6, 4)) == 5 and d((3, 0), (-1, 3)) == 5 and d((6, 4), (-1, 3)) ** 2 == 50, "sa4")
D_, E_ = sec((4, 6), (1, 5), 1, 3), sec((4, 6), (7, 2), 1, 3)
check(D_ == (R(13, 4), R(23, 4)) and E_ == (R(19, 4), 5) and same(d(D_, E_), 3 * sqrt(5) / 4) and same(d((1, 5), (7, 2)), 3 * sqrt(5)), "la1")
P2, Q2 = sec((2, 1), (5, -8), 1, 2), sec((2, 1), (5, -8), 2, 1)
check(P2 == (3, -2) and Q2 == (4, -5) and 2 * 3 - (-2) - 8 == 0 and d((2, 1), P2) == d(P2, Q2) == d(Q2, (5, -8)) == sqrt(10), "la2")
check(d((2, 5), (8, 3)) == 2 * sqrt(10) and ((2 + 8) / R(2), (5 + 3) / R(2)) == (5, 4) and solve(Eq((x - 2) ** 2 + 25, (x - 4) ** 2 + 16), x) == [R(3, 4)] and sec((2, 5), (4, 4), 2, 3) == (R(14, 5), R(23, 5)), "sqp37")
check(d((2, 3), (8, 11)) == 10 and ((2 + 8) / R(2), (3 + 11) / R(2)) == (5, 7) and sec((2, 3), (8, 11), 1, 3) == (R(7, 2), 5) and solve(Eq((x - 2) ** 2 + 9, (x - 8) ** 2 + 121), x) == [R(43, 3)], "cb2")
check([(9, 0), (9, -6), (-9, 0), (-9, 6)] and R(0 - (-6), -9 - 9) == R(0 - 6, 9 - (-9)), "sqp16 parallelogram"); check(d((9, 0), (9, -6)) != d((9, -6), (-9, 0)), "sqp16 not rhombus")

# ---------------------------------------------------------------- figures
def plane(title, points, segments=(), labels=None, **kw):
    fig = {"type": "geometry_figure", "title": title, "axes": True, "points": {n: list(p) for n, p in points.items()}, "segments": [list(s) if isinstance(s, tuple) else s for s in segments]}
    fig["labels"] = labels or {n: f"{n}({p[0]}, {p[1]})" for n, p in points.items()}
    fig.update(kw); return fig
FIG_DIST = plane("Distance between two points", {"P": (1, 2), "Q": (5, 5), "T": (5, 2)},
                 [{"from": "P", "to": "Q", "highlight": True}, {"from": "P", "to": "T", "dashed": True}, {"from": "T", "to": "Q", "dashed": True}],
                 labels={"P": "P(x₁, y₁)", "Q": "Q(x₂, y₂)", "T": "T"}, right_angles=[["P", "T", "Q"]],
                 lengths=[{"from": "P", "to": "T", "label": "x₂ − x₁"}, {"from": "T", "to": "Q", "label": "y₂ − y₁"}])
FIG_SEC = plane("P divides AB in the ratio 2 : 1", {"A": (1, 1), "B": (7, 4), "P": (5, 3)}, [("A", "P"), {"from": "P", "to": "B", "highlight": True}],
                lengths=[{"from": "A", "to": "P", "label": "2 parts"}, {"from": "P", "to": "B", "label": "1 part"}])
FIG_SQUARE = plane("Champa and Chameli's classroom", {"A": (3, 4), "B": (6, 7), "C": (9, 4), "D": (6, 1)}, [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
                   right_angles=[["D", "A", "B"]])
FIG_PICNIC = plane("Aman (P), Kirti (Q) and Chahat (R)", {"P": (2, 5), "Q": (4, 4), "R": (8, 3)}, [])
FIG_FLAGS = plane("Green flag (G) and red flag (R)", {"G": (2, 25), "R": (8, 20)}, [{"from": "G", "to": "R", "highlight": True}])
check(abs(float(FIG_DIST["points"]["T"][0] - 5)) < 1e-9, "fig")

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch07.{id_}", "type": type_, **kw}
def fig(id_, figure): return {"id": f"ch07.{id_}", **figure}

sections = [
 {"id": "s1", "title": "Points on a plane", "blocks": [
  blk("s1.hook", "hook", title="Two numbers that find you anywhere",
    body="When you share your location on a phone, it sends just two numbers: how far north and how far east you are. With only those two numbers, anyone can find you on a map.\n\n"
         "In Class 9 you learnt to mark points like $(3, 4)$ on a graph. In this chapter you will use the coordinates of points to find **distances** between them and to find the point that **divides** a line segment in a given ratio, without measuring anything."),
  blk("s1.inspiration", "inspiration", title="The thinker who joined algebra and geometry", person="René Descartes", years="1596–1650",
    body="René Descartes was a French philosopher and mathematician. A popular story says that, lying in bed, he watched a fly on the ceiling and realised its position could be described by two numbers: its distances from two walls.\n\n"
         "In 1637 he published *La Géométrie*, which turned shapes into equations and equations into shapes. In his honour, the $x$-$y$ system is called the **Cartesian** coordinate system.",
    quote="Join two ideas that seem far apart, and you can create something new.",
    future="Coordinate geometry powers GPS and maps, computer graphics and video games, robotics, and the design of buildings and bridges."),
  blk("s1.socratic", "socratic_question", question="Which of these points lies on the $y$-axis?",
    options=["$(0, 5)$", "$(5, 0)$", "$(5, 5)$"], correct_index=0,
    explanation="Every point on the $y$-axis has $x$-coordinate 0, so $(0, 5)$ lies on it. Points on the $x$-axis have $y$-coordinate 0, like $(5, 0)$."),
 ]},
 {"id": "s2", "title": "Distance formula", "blocks": [
  blk("s2.recap", "theory", title="Coordinates: a quick recap",
    body="A point $P(x, y)$ is $|x|$ units from the $y$-axis and $|y|$ units from the $x$-axis. The $x$-coordinate is called the **abscissa** and the $y$-coordinate the **ordinate**.\n\n"
         "Points on the $x$-axis have the form $(x, 0)$ and points on the $y$-axis have the form $(0, y)$. The origin is $O(0, 0)$."),
  blk("s2.discovery", "discovery", title="Make a right triangle",
    body="To find the distance between $P(x_1, y_1)$ and $Q(x_2, y_2)$, draw a horizontal line through $P$ and a vertical line through $Q$. They meet at $T$, making a right angle. "
         "The horizontal side is $x_2 - x_1$ and the vertical side is $y_2 - y_1$. Now Pythagoras does the rest."),
  fig("s2.fig", FIG_DIST),
  blk("s2.reveal", "theory", title="The distance formula", revision=True,
    body="The distance between $P(x_1, y_1)$ and $Q(x_2, y_2)$ is\n\n$$PQ = \\sqrt{(x_2 - x_1)^{2} + (y_2 - y_1)^{2}}$$\n\n"
         "The distance of $P(x, y)$ from the origin is $\\sqrt{x^{2} + y^{2}}$.\n\n"
         "**Uses:** three points are **collinear** when the sum of two of the distances equals the third; a triangle is **isosceles** when two sides are equal; "
         "a quadrilateral with four equal sides and equal diagonals is a **square**."),
  blk("s2.eg1", "worked_example", title="Finding a distance",
    problem="Find the distance between the points $(2, 3)$ and $(4, 1)$.",
    steps=["$x_2 - x_1 = 4 - 2 = 2$ and $y_2 - y_1 = 1 - 3 = -2$.", "Distance $= \\sqrt{2^{2} + (-2)^{2}} = \\sqrt{8}$"], answer="$2\\sqrt{2}$ units"),
  blk("s2.eg2", "worked_example", title="NCERT example: is it a triangle?",
    problem="Do the points $P(3, 2)$, $Q(-2, -3)$ and $R(2, 3)$ form a triangle? If so, name the type of triangle.",
    steps=["$PQ = \\sqrt{25 + 25} = \\sqrt{50}$, $QR = \\sqrt{16 + 36} = \\sqrt{52}$, $PR = \\sqrt{1 + 1} = \\sqrt{2}$.",
           "No distance equals the sum of the other two, so the points are not collinear: they form a triangle.",
           "$PQ^{2} + PR^{2} = 50 + 2 = 52 = QR^{2}$, so by the converse of Pythagoras the angle at $P$ is $90^\\circ$."],
    answer="Yes: a right triangle, right-angled at $P$."),
  blk("s2.eg3", "worked_example", title="NCERT exercise: a point on the x-axis",
    problem="Find the point on the $x$-axis which is equidistant from $(2, -5)$ and $(-2, 9)$.",
    steps=["Let the point be $(x, 0)$.", "$(x - 2)^{2} + 25 = (x + 2)^{2} + 81$", "$-4x + 29 = 4x + 85$, so $x = -7$."], answer="$(-7, 0)$"),
  blk("s2.check1", "knowledge_check", question="The distance of the point $(3, 4)$ from the origin is:",
    options=["$5$", "$7$", "$25$", "$1$"], correct_index=0, explanation="$\\sqrt{3^{2} + 4^{2}} = \\sqrt{25} = 5$."),
  blk("s2.check2", "knowledge_check", question="The distance of the point $(2, 3)$ from the $y$-axis is:",
    options=["$2$", "$3$", "$\\sqrt{13}$", "$5$"], correct_index=0, explanation="The distance from the $y$-axis is the $x$-coordinate (in absolute value): 2."),
  blk("s2.tip", "teacher_tip", title="Square both sides",
    body="When a question says 'equidistant', write $PA^{2} = PB^{2}$ straight away: squaring removes the roots and the algebra becomes linear. "
         "On the panel, draw the right triangle under every distance once or twice so students see that the formula is only Pythagoras."),
 ]},
 {"id": "s3", "title": "Section formula", "blocks": [
  blk("s3.discovery", "discovery", title="Dividing a segment",
    body="On the graph, $P$ lies on $AB$ with $AP : PB = 2 : 1$. Going from $A(1, 1)$ to $B(7, 4)$, $x$ rises by 6 and $y$ by 3. Two-thirds of the way along, $x$ has risen by 4 and $y$ by 2, so $P = (5, 3)$. "
         "The section formula does this for any ratio."),
  fig("s3.fig", FIG_SEC),
  blk("s3.reveal", "theory", title="Section formula", revision=True,
    body="The point $P$ that divides the line segment joining $A(x_1, y_1)$ and $B(x_2, y_2)$ internally in the ratio $m_1 : m_2$ is\n\n"
         "$$P\\left(\\dfrac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\; \\dfrac{m_1y_2 + m_2y_1}{m_1 + m_2}\\right)$$\n\n"
         "**Mid-point** (ratio $1 : 1$): $\\left(\\dfrac{x_1 + x_2}{2}, \\dfrac{y_1 + y_2}{2}\\right)$.\n\n"
         "To find an unknown ratio, take it as $k : 1$, use the section formula for one coordinate, and solve for $k$. "
         "The points of **trisection** divide a segment in the ratios $1 : 2$ and $2 : 1$."),
  blk("s3.eg1", "worked_example", title="NCERT example",
    problem="Find the coordinates of the point which divides the line segment joining $(4, -3)$ and $(8, 5)$ in the ratio $3 : 1$ internally.",
    steps=["$m_1 = 3$, $m_2 = 1$, $(x_1, y_1) = (4, -3)$, $(x_2, y_2) = (8, 5)$.", "$x = \\dfrac{3 \\times 8 + 1 \\times 4}{4} = 7$ and $y = \\dfrac{3 \\times 5 + 1 \\times (-3)}{4} = 3$"],
    answer="$(7, 3)$"),
  blk("s3.eg2", "worked_example", title="NCERT example: finding the ratio",
    problem="In what ratio does the point $(-4, 6)$ divide the line segment joining $A(-6, 10)$ and $B(3, -8)$?",
    steps=["Let the ratio be $k : 1$. Then $\\dfrac{3k - 6}{k + 1} = -4$.", "$3k - 6 = -4k - 4$, so $k = \\dfrac{2}{7}$.", "Check $y$: $\\dfrac{-8 \\times \\frac{2}{7} + 10}{\\frac{2}{7} + 1} = 6$ ✓"],
    answer="$2 : 7$"),
  blk("s3.eg3", "worked_example", title="NCERT example: points of trisection",
    problem="Find the coordinates of the points of trisection of the line segment joining $A(2, -2)$ and $B(-7, 4)$.",
    steps=["$P$ divides $AB$ in $1 : 2$: $P = \\left(\\dfrac{-7 + 4}{3}, \\dfrac{4 - 4}{3}\\right) = (-1, 0)$.", "$Q$ divides $AB$ in $2 : 1$: $Q = \\left(\\dfrac{-14 + 2}{3}, \\dfrac{8 - 2}{3}\\right) = (-4, 2)$."],
    answer="$(-1, 0)$ and $(-4, 2)$"),
  blk("s3.eg4", "worked_example", title="NCERT example: a parallelogram",
    problem="If the points $A(6, 1)$, $B(8, 2)$, $C(9, 4)$ and $D(p, 3)$ are the vertices of a parallelogram, taken in order, find the value of $p$.",
    steps=["The diagonals of a parallelogram bisect each other, so the mid-points of $AC$ and $BD$ are the same.", "Mid-point of $AC = \\left(\\dfrac{15}{2}, \\dfrac{5}{2}\\right)$, mid-point of $BD = \\left(\\dfrac{8 + p}{2}, \\dfrac{5}{2}\\right)$.",
           "$\\dfrac{8 + p}{2} = \\dfrac{15}{2}$"], answer="$p = 7$"),
  blk("s3.check1", "knowledge_check", question="The mid-point of the line segment joining $(2, 5)$ and $(6, -1)$ is:",
    options=["$(4, 2)$", "$(8, 4)$", "$(2, 3)$", "$(4, 3)$"], correct_index=0, explanation="$\\left(\\dfrac{2 + 6}{2}, \\dfrac{5 - 1}{2}\\right) = (4, 2)$."),
  blk("s3.check2", "knowledge_check", question="The point dividing the join of $(0, 0)$ and $(6, 9)$ in the ratio $1 : 2$ is:",
    options=["$(2, 3)$", "$(4, 6)$", "$(3, 4.5)$", "$(1, 1.5)$"], correct_index=0,
    explanation="$\\left(\\dfrac{1 \\times 6 + 2 \\times 0}{3}, \\dfrac{1 \\times 9 + 2 \\times 0}{3}\\right) = (2, 3)$: one-third of the way from $(0, 0)$."),
  blk("s3.memory", "memory_trick", title="Cross over", revision=True,
    body="In the section formula, each ratio number multiplies the **far** end: $m_1$ goes with $B(x_2, y_2)$ and $m_2$ with $A(x_1, y_1)$. "
         "Think: 'the bigger the share near $A$, the more the point is pulled towards $B$'. Check your answer: $P$ must lie between $A$ and $B$."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Multiplying $m_1$ with $x_1$ instead of $x_2$ in the section formula.\n"
         "- Forgetting to square negative differences correctly: $(-3)^{2} = 9$, not $-9$.\n"
         "- Writing a point on the $x$-axis as $(0, y)$: it is $(x, 0)$.\n"
         "- Checking only three sides for a square: you also need equal diagonals.\n"
         "- In ratio questions, using both coordinates to find $k$ and getting confused: one coordinate is enough, and the other is a check."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why the distance formula is just the Pythagoras theorem, using the figure of the right triangle."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 3:** the graph of a linear equation is a line made of points $(x, y)$; now you can measure along it.\n"
         "- **Chapter 6, Triangles:** the section formula is the Basic Proportionality Theorem written with coordinates.\n"
         "- **Class 11:** straight lines, circles and parabolas are all studied with coordinates."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="Find the point on the $y$-axis which is equidistant from $A(6, 5)$ and $B(-4, 3)$.\n\n"
         "**Answer:** Let the point be $(0, y)$. $36 + (y - 5)^{2} = 16 + (y - 3)^{2}$ gives $61 - 10y = 25 - 6y$, so $y = 9$. The point is $(0, 9)$."),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- Distance between $(x_1, y_1)$ and $(x_2, y_2)$: $\\sqrt{(x_2 - x_1)^{2} + (y_2 - y_1)^{2}}$.\n"
         "- Distance of $(x, y)$ from the origin: $\\sqrt{x^{2} + y^{2}}$.\n"
         "- Point dividing the join in the ratio $m_1 : m_2$: $\\left(\\dfrac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\dfrac{m_1y_2 + m_2y_1}{m_1 + m_2}\\right)$.\n"
         "- Mid-point: $\\left(\\dfrac{x_1 + x_2}{2}, \\dfrac{y_1 + y_2}{2}\\right)$."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Write the formula first, then substitute with brackets around negative numbers.\n"
         "- For 'equidistant' questions, equate the squares of the distances.\n"
         "- To prove a figure is a square, rhombus or parallelogram, show all the sides **and** the diagonals you need, and state the conclusion.\n"
         "- In ratio questions, take the ratio as $k : 1$ and write the final answer as a ratio of whole numbers."),
  blk("s4.flash1", "flashcard", front="What is the distance formula?", back="$\\sqrt{(x_2 - x_1)^{2} + (y_2 - y_1)^{2}}$"),
  blk("s4.flash2", "flashcard", front="What is the section formula?", back="$\\left(\\dfrac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\dfrac{m_1y_2 + m_2y_1}{m_1 + m_2}\\right)$ for the ratio $m_1 : m_2$."),
  blk("s4.flash3", "flashcard", front="What form does a point on the x-axis have?", back="$(x, 0)$. A point on the $y$-axis has the form $(0, y)$."),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Coordinate Geometry",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 7,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: distance formula and section formula (internal division). The area of a triangle is not in the board syllabus and is not included.",
  "concepts": ["coordinates", "distance_formula", "section_formula", "coordinate_applications"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
CO, DIST, SEC, APP = "coordinates", "distance_formula", "section_formula", "coordinate_applications"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch07.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS2_D = ["1 mark: correct substitution in the formula", "1 mark: answer"]
MS3_SHAPE = ["1 mark: lengths of the sides", "1 mark: diagonals or the needed comparison", "1 mark: conclusion"]
MS3_SOLVE = ["1 mark: forming the equation", "1 mark: solving", "1 mark: answer"]
MS3_SEC = ["1 mark: correct formula and ratio", "1 mark: first coordinate", "1 mark: second coordinate"]

# Exercise 7.1
for p, A, B, steps in [("i", "(2, 3)", "(4, 1)", ["$\\sqrt{(4 - 2)^{2} + (1 - 3)^{2}} = \\sqrt{4 + 4}$", "$= \\sqrt{8} = 2\\sqrt{2}$"]),
                       ("ii", "(-5, 7)", "(-1, 3)", ["$\\sqrt{(-1 + 5)^{2} + (3 - 7)^{2}} = \\sqrt{16 + 16}$", "$= \\sqrt{32} = 4\\sqrt{2}$"]),
                       ("iii", "(a, b)", "(-a, -b)", ["$\\sqrt{(-a - a)^{2} + (-b - b)^{2}} = \\sqrt{4a^{2} + 4b^{2}}$", "$= 2\\sqrt{a^{2} + b^{2}}$"])]:
    q(f"ex7_1.q1.{p}", "very_short_answer", 2, [DIST], ex("7.1", 1, p), f"Find the distance between the points ${A}$ and ${B}$.", "easy", answer_steps=steps, marking_scheme=MS2_D)
q("ex7_1.q2", "very_short_answer", 2, [DIST], ex("7.1", 2), "Find the distance between the points $(0, 0)$ and $(36, 15)$. Can you now find the distance between two towns A and B located at these points?", "easy",
  answer_steps=["$\\sqrt{36^{2} + 15^{2}} = \\sqrt{1296 + 225} = \\sqrt{1521} = 39$", "So the towns are 39 km apart (taking 1 unit = 1 km)."], marking_scheme=MS2_D)
q("ex7_1.q3", "short_answer", 3, [DIST, APP], ex("7.1", 3), "Determine if the points $(1, 5)$, $(2, 3)$ and $(-2, -11)$ are collinear.",
  answer_steps=["$AB = \\sqrt{1 + 4} = \\sqrt{5}$, $BC = \\sqrt{16 + 196} = \\sqrt{212} = 2\\sqrt{53}$, $AC = \\sqrt{9 + 256} = \\sqrt{265}$.",
                "$\\sqrt{5} + 2\\sqrt{53} \\approx 16.80$, while $\\sqrt{265} \\approx 16.28$; no distance equals the sum of the other two.", "So the points are not collinear."],
  marking_scheme=["1 mark: the three distances", "1 mark: comparison", "1 mark: conclusion"])
q("ex7_1.q4", "short_answer", 3, [DIST, APP], ex("7.1", 4), "Check whether $(5, -2)$, $(6, 4)$ and $(7, -2)$ are the vertices of an isosceles triangle.", "easy",
  answer_steps=["$AB = \\sqrt{1 + 36} = \\sqrt{37}$, $BC = \\sqrt{1 + 36} = \\sqrt{37}$, $AC = \\sqrt{4 + 0} = 2$.", "$AB = BC$", "Two sides are equal, so it is an isosceles triangle."],
  marking_scheme=["1 mark: the three sides", "1 mark: two equal sides", "1 mark: conclusion"])
q("ex7_1.q5", "short_answer", 3, [DIST, APP], ex("7.1", 5),
  "In a classroom, 4 friends are seated at the points A, B, C and D. Champa and Chameli walk into the class and after observing for a few minutes Champa asks Chameli, \"Don't you think ABCD is a square?\" Chameli disagrees. Using the distance formula, find which of them is correct. Take $A(3, 4)$, $B(6, 7)$, $C(9, 4)$ and $D(6, 1)$.",
  answer_steps=["$AB = BC = CD = DA = \\sqrt{9 + 9} = \\sqrt{18}$.", "Diagonals: $AC = \\sqrt{36 + 0} = 6$ and $BD = \\sqrt{0 + 36} = 6$.", "All sides are equal and the diagonals are equal, so $ABCD$ is a square: Champa is correct."],
  marking_scheme=MS3_SHAPE, figure=dict(FIG_SQUARE))
for p, pts, steps in [
 ("i", "(-1, -2), (1, 0), (-1, 2), (-3, 0)", ["All four sides are $\\sqrt{4 + 4} = \\sqrt{8}$.", "Diagonals: $\\sqrt{0 + 16} = 4$ and $\\sqrt{16 + 0} = 4$.", "Equal sides and equal diagonals: a **square**."]),
 ("ii", "(-3, 5), (3, 1), (0, 3), (-1, -4)", ["The points $(-3, 5)$, $(0, 3)$ and $(3, 1)$: distances $\\sqrt{13}$, $\\sqrt{13}$ and $\\sqrt{52} = 2\\sqrt{13}$.", "Since $\\sqrt{13} + \\sqrt{13} = 2\\sqrt{13}$, these three points are collinear.", "So the four points do not form a quadrilateral."]),
 ("iii", "(4, 5), (7, 6), (4, 3), (1, 2)", ["Opposite sides: $AB = CD = \\sqrt{10}$ and $BC = DA = \\sqrt{18}$.", "Diagonals: $AC = 2$ and $BD = \\sqrt{52}$ are not equal.", "Opposite sides equal, diagonals unequal: a **parallelogram**."]),
]:
    q(f"ex7_1.q6.{p}", "short_answer", 3, [DIST, APP], ex("7.1", 6, p), f"Name the type of quadrilateral formed, if any, by the points ${pts}$, and give reasons for your answer.",
      "hard" if p == "ii" else "medium", answer_steps=steps, marking_scheme=MS3_SHAPE)
q("ex7_1.q7", "short_answer", 3, [DIST], ex("7.1", 7), "Find the point on the $x$-axis which is equidistant from $(2, -5)$ and $(-2, 9)$.",
  answer_steps=["Let the point be $(x, 0)$: $(x - 2)^{2} + 25 = (x + 2)^{2} + 81$.", "$-4x + 29 = 4x + 85$, so $8x = -56$.", "$x = -7$: the point is $(-7, 0)$."], marking_scheme=MS3_SOLVE)
q("ex7_1.q8", "short_answer", 3, [DIST], ex("7.1", 8), "Find the values of $y$ for which the distance between the points $P(2, -3)$ and $Q(10, y)$ is 10 units.",
  answer_steps=["$(10 - 2)^{2} + (y + 3)^{2} = 100$", "$(y + 3)^{2} = 36$, so $y + 3 = \\pm 6$.", "$y = 3$ or $y = -9$"], marking_scheme=MS3_SOLVE)
q("ex7_1.q9", "short_answer", 3, [DIST], ex("7.1", 9), "If $Q(0, 1)$ is equidistant from $P(5, -3)$ and $R(x, 6)$, find the values of $x$. Also find the distances $QR$ and $PR$.", "hard",
  answer_steps=["$QP^{2} = 25 + 16 = 41$ and $QR^{2} = x^{2} + 25$, so $x^{2} = 16$ and $x = \\pm 4$.", "$QR = \\sqrt{41}$",
                "For $R(4, 6)$: $PR = \\sqrt{1 + 81} = \\sqrt{82}$. For $R(-4, 6)$: $PR = \\sqrt{81 + 81} = 9\\sqrt{2}$."], marking_scheme=MS3_SOLVE)
q("ex7_1.q10", "short_answer", 3, [DIST], ex("7.1", 10), "Find a relation between $x$ and $y$ such that the point $(x, y)$ is equidistant from the point $(3, 6)$ and $(-3, 4)$.",
  answer_steps=["$(x - 3)^{2} + (y - 6)^{2} = (x + 3)^{2} + (y - 4)^{2}$", "$-6x + 9 - 12y + 36 = 6x + 9 - 8y + 16$, i.e. $-12x - 4y + 20 = 0$.", "$3x + y - 5 = 0$"], marking_scheme=MS3_SOLVE)
# Exercise 7.2
q("ex7_2.q1", "very_short_answer", 2, [SEC], ex("7.2", 1), "Find the coordinates of the point which divides the join of $(-1, 7)$ and $(4, -3)$ in the ratio $2 : 3$.", "easy",
  answer_steps=["$x = \\dfrac{2 \\times 4 + 3 \\times (-1)}{5} = 1$, $y = \\dfrac{2 \\times (-3) + 3 \\times 7}{5} = 3$", "The point is $(1, 3)$."], marking_scheme=MS2_D)
q("ex7_2.q2", "short_answer", 3, [SEC], ex("7.2", 2), "Find the coordinates of the points of trisection of the line segment joining $(4, -1)$ and $(-2, -3)$.",
  answer_steps=["The points of trisection divide the segment in the ratios $1 : 2$ and $2 : 1$.", "$1 : 2$: $\\left(\\dfrac{-2 + 8}{3}, \\dfrac{-3 - 2}{3}\\right) = \\left(2, -\\dfrac{5}{3}\\right)$", "$2 : 1$: $\\left(\\dfrac{-4 + 4}{3}, \\dfrac{-6 - 1}{3}\\right) = \\left(0, -\\dfrac{7}{3}\\right)$"],
  marking_scheme=["1 mark: ratios", "1 mark: first point", "1 mark: second point"])
q("ex7_2.q3", "short_answer", 3, [DIST, SEC, APP], ex("7.2", 3),
  "To conduct Sports Day activities, lines have been drawn with chalk powder at a distance of 1 m each, in a rectangular ground. 100 flower pots are placed at a distance of 1 m from each other along each line. Niharika runs $\\dfrac{1}{4}$th the distance along the 2nd line and posts a green flag. Preet runs $\\dfrac{1}{5}$th the distance along the eighth line and posts a red flag. What is the distance between both the flags? If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post her flag?",
  answer_steps=["Taking the starting corner as the origin, the green flag is at $(2, 25)$ and the red flag at $(8, 20)$.", "Distance $= \\sqrt{6^{2} + 5^{2}} = \\sqrt{61}$ m",
                "Mid-point $= \\left(5, \\dfrac{45}{2}\\right)$: the blue flag goes on the 5th line, 22.5 m from the start."],
  marking_scheme=["1 mark: coordinates of the flags", "1 mark: distance", "1 mark: position of the blue flag"], figure=dict(FIG_FLAGS))
q("ex7_2.q4", "short_answer", 3, [SEC], ex("7.2", 4), "Find the ratio in which the line segment joining the points $(-3, 10)$ and $(6, -8)$ is divided by $(-1, 6)$.",
  answer_steps=["Let the ratio be $k : 1$: $\\dfrac{6k - 3}{k + 1} = -1$.", "$6k - 3 = -k - 1$, so $k = \\dfrac{2}{7}$.", "The ratio is $2 : 7$."], marking_scheme=MS3_SOLVE)
q("ex7_2.q5", "short_answer", 3, [SEC], ex("7.2", 5), "Find the ratio in which the line segment joining $A(1, -5)$ and $B(-4, 5)$ is divided by the $x$-axis. Also find the coordinates of the point of division.",
  answer_steps=["Let the ratio be $k : 1$. On the $x$-axis, $y = 0$: $\\dfrac{5k - 5}{k + 1} = 0$, so $k = 1$.", "The ratio is $1 : 1$ (the point is the mid-point).", "Point $= \\left(\\dfrac{1 - 4}{2}, 0\\right) = \\left(-\\dfrac{3}{2}, 0\\right)$"],
  marking_scheme=["1 mark: equation for $k$", "1 mark: ratio", "1 mark: point"])
q("ex7_2.q6", "short_answer", 3, [SEC, APP], ex("7.2", 6), "If $(1, 2)$, $(4, y)$, $(x, 6)$ and $(3, 5)$ are the vertices of a parallelogram taken in order, find $x$ and $y$.",
  answer_steps=["The diagonals bisect each other: mid-point of $(1, 2)$ and $(x, 6)$ = mid-point of $(4, y)$ and $(3, 5)$.", "$\\dfrac{1 + x}{2} = \\dfrac{7}{2}$, so $x = 6$.", "$\\dfrac{2 + 6}{2} = \\dfrac{y + 5}{2}$, so $y = 3$."],
  marking_scheme=["1 mark: diagonals bisect each other", "1 mark: $x = 6$", "1 mark: $y = 3$"])
q("ex7_2.q7", "very_short_answer", 2, [SEC], ex("7.2", 7), "Find the coordinates of a point A, where AB is the diameter of a circle whose centre is $(2, -3)$ and B is $(1, 4)$.", "easy",
  answer_steps=["The centre is the mid-point of $AB$: $\\dfrac{x + 1}{2} = 2$ and $\\dfrac{y + 4}{2} = -3$.", "$A = (3, -10)$"], marking_scheme=MS2_D)
q("ex7_2.q8", "short_answer", 3, [SEC], ex("7.2", 8), "If A and B are $(-2, -2)$ and $(2, -4)$, respectively, find the coordinates of P such that $AP = \\dfrac{3}{7}AB$ and P lies on the line segment AB.",
  answer_steps=["$AP = \\dfrac{3}{7}AB$, so $AP : PB = 3 : 4$.", "$x = \\dfrac{3 \\times 2 + 4 \\times (-2)}{7} = -\\dfrac{2}{7}$", "$y = \\dfrac{3 \\times (-4) + 4 \\times (-2)}{7} = -\\dfrac{20}{7}$"], marking_scheme=MS3_SEC)
q("ex7_2.q9", "short_answer", 3, [SEC], ex("7.2", 9), "Find the coordinates of the points which divide the line segment joining $A(-2, 2)$ and $B(2, 8)$ into four equal parts.",
  answer_steps=["The middle point is the mid-point of $AB$: $(0, 5)$.", "The first point is the mid-point of $A$ and $(0, 5)$: $\\left(-1, \\dfrac{7}{2}\\right)$.", "The third point is the mid-point of $(0, 5)$ and $B$: $\\left(1, \\dfrac{13}{2}\\right)$."],
  marking_scheme=["1 mark: each point"] * 3)
q("ex7_2.q10", "short_answer", 3, [DIST, APP], ex("7.2", 10), "Find the area of a rhombus if its vertices are $(3, 0)$, $(4, 5)$, $(-1, 4)$ and $(-2, -1)$ taken in order. [Hint: Area of a rhombus $= \\dfrac{1}{2}$(product of its diagonals)]",
  answer_steps=["Diagonal 1: $(3, 0)$ to $(-1, 4)$: $\\sqrt{16 + 16} = 4\\sqrt{2}$.", "Diagonal 2: $(4, 5)$ to $(-2, -1)$: $\\sqrt{36 + 36} = 6\\sqrt{2}$.", "Area $= \\dfrac{1}{2} \\times 4\\sqrt{2} \\times 6\\sqrt{2} = 24$ square units"],
  marking_scheme=["1 mark: first diagonal", "1 mark: second diagonal", "1 mark: area"])
# NCERT examples
q("eg_triangle", "short_answer", 3, [DIST, APP], {"kind": "ncert_example"}, "Do the points $(3, 2)$, $(-2, -3)$ and $(2, 3)$ form a triangle? If so, name the type of triangle formed.",
  answer_steps=["$PQ = \\sqrt{50}$, $QR = \\sqrt{52}$, $PR = \\sqrt{2}$: no distance is the sum of the other two, so they form a triangle.", "$PQ^{2} + PR^{2} = 50 + 2 = 52 = QR^{2}$",
                "By the converse of Pythagoras, it is a right triangle with the right angle at $P(3, 2)$."], marking_scheme=MS3_SHAPE)
q("eg_yaxis", "short_answer", 3, [SEC], {"kind": "ncert_example"}, "Find the ratio in which the $y$-axis divides the line segment joining the points $(5, -6)$ and $(-1, -4)$. Also find the point of intersection.",
  answer_steps=["Let the ratio be $k : 1$. On the $y$-axis, $x = 0$: $\\dfrac{-k + 5}{k + 1} = 0$, so $k = 5$.", "The ratio is $5 : 1$.", "$y = \\dfrac{5 \\times (-4) + 1 \\times (-6)}{6} = -\\dfrac{13}{3}$: the point is $\\left(0, -\\dfrac{13}{3}\\right)$."],
  marking_scheme=["1 mark: equation for $k$", "1 mark: ratio", "1 mark: point"])
q("eg_parallelogram", "very_short_answer", 2, [SEC, APP], {"kind": "ncert_example"}, "If the points $A(6, 1)$, $B(8, 2)$, $C(9, 4)$ and $D(p, 3)$ are the vertices of a parallelogram, taken in order, find the value of $p$.",
  answer_steps=["Mid-point of $AC$ = mid-point of $BD$: $\\dfrac{15}{2} = \\dfrac{8 + p}{2}$", "$p = 7$"], marking_scheme=MS2_D)
# MCQs
mcq("mcq01", [DIST], "The distance of the point $(3, 4)$ from the origin is:", ["$5$", "$7$", "$25$", "$1$"], 0, "$\\sqrt{9 + 16} = 5$.")
mcq("mcq02", [DIST], "The distance between the points $(2, 3)$ and $(5, 7)$ is:", ["$5$", "$25$", "$7$", "$\\sqrt{7}$"], 0, "$\\sqrt{3^{2} + 4^{2}} = 5$.")
mcq("mcq03", [SEC], "The mid-point of the line segment joining $(2, 5)$ and $(6, -1)$ is:", ["$(4, 2)$", "$(8, 4)$", "$(2, 3)$", "$(4, 3)$"], 0, "$\\left(\\dfrac{8}{2}, \\dfrac{4}{2}\\right) = (4, 2)$.")
mcq("mcq04", [CO], "A point on the $x$-axis has the general form:", ["$(x, 0)$", "$(0, y)$", "$(x, x)$", "$(0, 0)$"], 0, "On the $x$-axis the $y$-coordinate is 0.")
mcq("mcq05", [SEC], "The point which divides the join of $(0, 0)$ and $(6, 9)$ in the ratio $1 : 2$ is:", ["$(2, 3)$", "$(4, 6)$", "$(3, 4.5)$", "$(1, 1.5)$"], 0,
    "$\\left(\\dfrac{6}{3}, \\dfrac{9}{3}\\right) = (2, 3)$.", "medium")
mcq("mcq06", [DIST], "The distance of the point $(-6, 8)$ from the origin is:", ["$10$", "$2$", "$14$", "$6$"], 0, "$\\sqrt{36 + 64} = 10$.")
mcq("mcq07", [DIST], "If the distance between $(4, p)$ and $(1, 0)$ is 5, then $p$ is:", ["$\\pm 4$", "$4$ only", "$-4$ only", "$0$"], 0, "$9 + p^{2} = 25$, so $p = \\pm 4$.", "medium")
mcq("mcq08", [SEC], "The ratio in which the $x$-axis divides the segment joining $(1, -5)$ and $(-4, 5)$ is:", ["$1 : 1$", "$1 : 2$", "$2 : 1$", "$5 : 1$"], 0,
    "$\\dfrac{5k - 5}{k + 1} = 0$ gives $k = 1$.", "medium")
mcq("mcq09", [DIST, APP], "The perimeter of the triangle with vertices $(0, 0)$, $(3, 0)$ and $(0, 4)$ is:", ["$12$", "$7$", "$10$", "$5$"], 0, "The sides are 3, 4 and 5, so the perimeter is 12.")
mcq("mcq10", [SEC], "If the mid-point of $AB$ is $(0, 0)$ and $A$ is $(3, -2)$, then $B$ is:", ["$(-3, 2)$", "$(3, -2)$", "$(6, -4)$", "$(-6, 4)$"], 0, "$\\dfrac{3 + x}{2} = 0$ and $\\dfrac{-2 + y}{2} = 0$ give $B(-3, 2)$.")
mcq("mcq11", [CO], "The distance of the point $(2, 3)$ from the $x$-axis is:", ["$3$", "$2$", "$\\sqrt{13}$", "$5$"], 0, "The distance from the $x$-axis is the $y$-coordinate: 3.")
mcq("mcq12", [SEC], "The point which divides the join of $(-1, 7)$ and $(4, -3)$ in the ratio $2 : 3$ is:", ["$(1, 3)$", "$(2, 1)$", "$(3, 1)$", "$(1, 5)$"], 0,
    "$\\left(\\dfrac{8 - 3}{5}, \\dfrac{-6 + 21}{5}\\right) = (1, 3)$.", "medium")
mcq("sqp2", [CO], "The shortest distance (in units) of the point $(2, 3)$ from the $y$-axis is", ["$2$", "$3$", "$5$", "$1$"], 0,
    "The shortest distance from the $y$-axis is the $x$-coordinate, i.e. 2.", source=SQP(2))
mcq("sqp16", [DIST, APP], "The points $A(9, 0)$, $B(9, -6)$, $C(-9, 0)$ and $D(-9, 6)$ are the vertices of a", ["Square", "Rectangle", "Parallelogram", "Trapezium"], 2,
    "$AB$ and $CD$ are both vertical with length 6, and $BC$ and $DA$ both have length $\\sqrt{360}$: opposite sides are equal and parallel, but the sides are not perpendicular, so it is a parallelogram.", "medium", source=SQP(16))

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [CO], "The point $(0, 4)$ lies on the $y$-axis.", "Every point on the $y$-axis has $x$-coordinate 0.", 0, "The $x$-coordinate of $(0, 4)$ is 0, which is exactly why it lies on the $y$-axis.")
ar("ar2", [DIST], "The distance of the point $(3, 4)$ from the origin is 5.", "The distance of $(x, y)$ from the origin is $x + y$.", 2, "A is true: $\\sqrt{9 + 16} = 5$. R is false: the distance is $\\sqrt{x^{2} + y^{2}}$.")
ar("ar3", [SEC], "The mid-point of the line segment joining $(2, 3)$ and $(4, 7)$ is $(6, 10)$.", "The mid-point of the join of $(x_1, y_1)$ and $(x_2, y_2)$ is $\\left(\\dfrac{x_1 + x_2}{2}, \\dfrac{y_1 + y_2}{2}\\right)$.", 3,
   "A is false: the mid-point is $(3, 5)$. R is true.")
ar("ar4", [DIST], "The point $(-7, 0)$ is equidistant from $(2, -5)$ and $(-2, 9)$.", "Every point on the $x$-axis has $y$-coordinate 0.", 1,
   "A is true: both distances are $\\sqrt{106}$. R is true, but it does not show why the distances are equal.")
ar("ar5", [SEC], "The point $\\left(-\\dfrac{2}{7}, -\\dfrac{20}{7}\\right)$ divides the join of $A(-2, -2)$ and $B(2, -4)$ in the ratio $3 : 4$.", "The point dividing the join in the ratio $m_1 : m_2$ is $\\left(\\dfrac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\dfrac{m_1y_2 + m_2y_1}{m_1 + m_2}\\right)$.", 0,
   "Using the section formula in R with $m_1 = 3$, $m_2 = 4$ gives exactly this point.")

q("vsa1", "very_short_answer", 2, [SEC], SHINE, "If the mid-point of the line segment joining $A\\left(\\dfrac{x}{2}, \\dfrac{y + 1}{2}\\right)$ and $B(x + 1, y - 3)$ is $C(5, -2)$, find $x$ and $y$.",
  answer_steps=["$\\dfrac{\\frac{x}{2} + x + 1}{2} = 5$ gives $\\dfrac{3x}{2} = 9$, so $x = 6$.", "$\\dfrac{\\frac{y + 1}{2} + y - 3}{2} = -2$ gives $\\dfrac{3y}{2} = -\\dfrac{3}{2}$, so $y = -1$."],
  marking_scheme=["1 mark: $x = 6$", "1 mark: $y = -1$"])
q("vsa2", "very_short_answer", 2, [DIST], SHINE, "Find the point on the $y$-axis which is equidistant from $(-5, -2)$ and $(3, 2)$.",
  answer_steps=["Let the point be $(0, y)$: $25 + (y + 2)^{2} = 9 + (y - 2)^{2}$, so $8y = -16$.", "$y = -2$: the point is $(0, -2)$."], marking_scheme=MS2_D)
q("sa1", "short_answer", 3, [DIST, APP], SHINE, "Show that the points $(1, 7)$, $(4, 2)$, $(-1, -1)$ and $(-4, 4)$ are the vertices of a square.",
  answer_steps=["All four sides are $\\sqrt{9 + 25} = \\sqrt{34}$.", "Diagonals: $\\sqrt{4 + 64} = \\sqrt{68}$ and $\\sqrt{64 + 4} = \\sqrt{68}$.", "Equal sides and equal diagonals, so it is a square."], marking_scheme=MS3_SHAPE)
q("sa2", "short_answer", 3, [SEC, APP], SHINE, "If $A(-2, 1)$, $B(a, 0)$, $C(4, b)$ and $D(1, 2)$ are the vertices of a parallelogram $ABCD$, find the values of $a$ and $b$.",
  answer_steps=["The diagonals bisect each other: mid-point of $AC$ = mid-point of $BD$.", "$\\dfrac{-2 + 4}{2} = \\dfrac{a + 1}{2}$, so $a = 1$.", "$\\dfrac{1 + b}{2} = \\dfrac{0 + 2}{2}$, so $b = 1$."],
  marking_scheme=["1 mark: diagonals bisect each other", "1 mark: $a = 1$", "1 mark: $b = 1$"])
q("sa3", "short_answer", 3, [SEC], SHINE, "If the point $P(9a - 2, -b)$ divides the line segment joining $A(3a + 1, -3)$ and $B(8a, 5)$ in the ratio $3 : 1$, find the values of $a$ and $b$.", "hard",
  answer_steps=["$x$: $\\dfrac{3 \\times 8a + 1 \\times (3a + 1)}{4} = 9a - 2$, i.e. $27a + 1 = 36a - 8$, so $a = 1$.", "$y$: $\\dfrac{3 \\times 5 + 1 \\times (-3)}{4} = 3 = -b$", "$b = -3$"],
  marking_scheme=["1 mark: section formula", "1 mark: $a = 1$", "1 mark: $b = -3$"])
q("sa4", "short_answer", 3, [DIST, APP], SHINE, "Prove that the points $(3, 0)$, $(6, 4)$ and $(-1, 3)$ are the vertices of a right-angled isosceles triangle.",
  answer_steps=["$AB = \\sqrt{9 + 16} = 5$, $AC = \\sqrt{16 + 9} = 5$, $BC = \\sqrt{49 + 1} = \\sqrt{50}$.", "$AB = AC$, so the triangle is isosceles.", "$AB^{2} + AC^{2} = 25 + 25 = 50 = BC^{2}$, so the angle at $A$ is $90^\\circ$."],
  marking_scheme=MS3_SHAPE)
q("la1", "long_answer", 5, [SEC, DIST, APP], SHINE, "The vertices of $\\triangle ABC$ are $A(4, 6)$, $B(1, 5)$ and $C(7, 2)$. A line is drawn to intersect sides $AB$ and $AC$ at $D$ and $E$ respectively, such that $\\dfrac{AD}{AB} = \\dfrac{AE}{AC} = \\dfrac{1}{4}$. Find the coordinates of $D$ and $E$, and show that $DE = \\dfrac{1}{4}BC$.", "hard",
  answer_steps=["$\\dfrac{AD}{AB} = \\dfrac{1}{4}$ means $AD : DB = 1 : 3$, and likewise $AE : EC = 1 : 3$.", "$D = \\left(\\dfrac{1 \\times 1 + 3 \\times 4}{4}, \\dfrac{1 \\times 5 + 3 \\times 6}{4}\\right) = \\left(\\dfrac{13}{4}, \\dfrac{23}{4}\\right)$",
                "$E = \\left(\\dfrac{1 \\times 7 + 3 \\times 4}{4}, \\dfrac{1 \\times 2 + 3 \\times 6}{4}\\right) = \\left(\\dfrac{19}{4}, 5\\right)$",
                "$DE = \\sqrt{\\left(\\dfrac{6}{4}\\right)^{2} + \\left(\\dfrac{3}{4}\\right)^{2}} = \\dfrac{\\sqrt{45}}{4} = \\dfrac{3\\sqrt{5}}{4}$", "$BC = \\sqrt{36 + 9} = 3\\sqrt{5}$, so $DE = \\dfrac{1}{4}BC$."],
  marking_scheme=["1 mark: ratios", "1 mark: $D$", "1 mark: $E$", "1 mark: $DE$", "1 mark: $BC$ and conclusion"])
q("la2", "long_answer", 5, [SEC, DIST], SHINE, "$P$ and $Q$ are the points of trisection of the line segment joining $A(2, 1)$ and $B(5, -8)$, with $P$ nearer to $A$. (i) Find $P$ and $Q$. (ii) If $P$ lies on the line $2x - y + k = 0$, find $k$. (iii) Show that $AP = PQ = QB$.", "hard",
  answer_steps=["(i) $P$ divides $AB$ in $1 : 2$: $P = \\left(\\dfrac{5 + 4}{3}, \\dfrac{-8 + 2}{3}\\right) = (3, -2)$.", "$Q$ divides $AB$ in $2 : 1$: $Q = \\left(\\dfrac{10 + 2}{3}, \\dfrac{-16 + 1}{3}\\right) = (4, -5)$.",
                "(ii) $2 \\times 3 - (-2) + k = 0$, so $k = -8$.", "(iii) $AP = \\sqrt{1 + 9} = \\sqrt{10}$, $PQ = \\sqrt{1 + 9} = \\sqrt{10}$, $QB = \\sqrt{1 + 9} = \\sqrt{10}$.", "So $AP = PQ = QB$."],
  marking_scheme=["1 mark: $P$", "1 mark: $Q$", "1 mark: $k = -8$", "1 mark: the three distances", "1 mark: conclusion"])
q("sqp37", "case_based", 4, [DIST, SEC], SQP(37),
  "A group of class X students goes to a picnic during the winter holidays. The positions of three friends Aman, Kirti and Chahat are shown by the points $P(2, 5)$, $Q(4, 4)$ and $R(8, 3)$.\n\n(i) Find the distance between P and R. (1)\n\n(ii) Is Q the mid-point of PR? Justify by finding the mid-point of PR. (1)\n\n(iii) Find the point on the $x$-axis which is equidistant from P and Q. OR Let S be a point which divides the line joining PQ in the ratio $2 : 3$. Find the coordinates of S. (2)",
  answer_steps=["(i) $PR = \\sqrt{36 + 4} = \\sqrt{40} = 2\\sqrt{10}$", "(ii) Mid-point of $PR = \\left(\\dfrac{2 + 8}{2}, \\dfrac{5 + 3}{2}\\right) = (5, 4) \\neq Q(4, 4)$, so Q is not the mid-point.",
                "(iii) $(x - 2)^{2} + 25 = (x - 4)^{2} + 16$ gives $4x = 3$: the point is $\\left(\\dfrac{3}{4}, 0\\right)$. OR $S = \\left(\\dfrac{2 \\times 4 + 3 \\times 2}{5}, \\dfrac{2 \\times 4 + 3 \\times 5}{5}\\right) = \\left(\\dfrac{14}{5}, \\dfrac{23}{5}\\right)$"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"], figure=dict(FIG_PICNIC))
q("cb2", "case_based", 4, [DIST, SEC], SHINE,
  "On a town map, the school is at $S(2, 3)$ and the hospital at $H(8, 11)$, with 1 unit $= 1$ km.\n\n(i) How far is the hospital from the school? (1)\n\n(ii) A library is exactly halfway between them. Find its position. (1)\n\n(iii) A bus stop divides $SH$ in the ratio $1 : 3$. Find its position. OR Find the point on the $x$-axis equidistant from $S$ and $H$. (2)",
  answer_steps=["(i) $SH = \\sqrt{36 + 64} = 10$ km", "(ii) Mid-point $= \\left(\\dfrac{2 + 8}{2}, \\dfrac{3 + 11}{2}\\right) = (5, 7)$",
                "(iii) $\\left(\\dfrac{1 \\times 8 + 3 \\times 2}{4}, \\dfrac{1 \\times 11 + 3 \\times 3}{4}\\right) = \\left(\\dfrac{7}{2}, 5\\right)$. OR $(x - 2)^{2} + 9 = (x - 8)^{2} + 121$ gives $12x = 172$: the point is $\\left(\\dfrac{43}{3}, 0\\right)$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch07.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
