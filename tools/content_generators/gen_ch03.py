"""CBSE Class 10 Maths Ch 3: Pair of Linear Equations in Two Variables.
Every solution, ratio verdict and constructed equation is checked with sympy."""
import json, os, sys
from collections import Counter
from fractions import Fraction as Fr
from sympy import symbols, linsolve, Rational as R, nsimplify, sqrt, simplify, Eq, solve

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch03"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch03_pair_of_linear_equations"
x, y = symbols("x y")

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

def sol(e1, e2):
    s = linsolve([e1, e2], [x, y])
    return list(s)

def unique(e1, e2, expected, msg):
    s = sol(e1, e2)
    check(len(s) == 1 and tuple(simplify(v) for v in s[0]) == tuple(nsimplify(v) for v in expected), f"{msg}: {s} vs {expected}")

def nature(a1, b1, c1, a2, b2, c2):
    """For a1x+b1y+c1=0 and a2x+b2y+c2=0."""
    if Fr(a1) * b2 != Fr(a2) * b1:
        return "intersecting"
    if Fr(a1) * c2 == Fr(a2) * c1 and Fr(b1) * c2 == Fr(b2) * c1:
        return "coincident"
    return "parallel"

def line(a, b, c):
    """ax + by = c as y = mx + k, coefficients [m, k] for the graph block."""
    return [float(Fr(-a) / b), float(Fr(c) / b)]

# ---------------------------------------------------------------- verification
# Exercise 3.1
unique(x + y - 10, x - y - 4, (7, 3), "3.1 Q1 i")
unique(5*x + 7*y - 50, 7*x + 5*y - 46, (3, 5), "3.1 Q1 ii")
EX31Q2 = [("i", (5, -4, 8, 7, 6, -9), "intersecting"), ("ii", (9, 3, 12, 18, 6, 24), "coincident"), ("iii", (6, -3, 10, 2, -1, 9), "parallel")]
for p, co, v in EX31Q2: check(nature(*co) == v, f"3.1 Q2 {p}")
EX31Q3 = [("i", (3, 2, -5, 2, -3, -7), "intersecting"), ("ii", (2, -3, -8, 4, -6, -9), "parallel"),
          ("iii", (Fr(3, 2), Fr(5, 3), -7, 9, -10, -14), "intersecting"), ("iv", (5, -3, -11, -10, 6, 22), "coincident"),
          ("v", (Fr(4, 3), 2, -8, 2, 3, -12), "coincident")]
for p, co, v in EX31Q3: check(nature(*co) == v, f"3.1 Q3 {p}")
EX31Q4 = [("i", (1, 1, -5, 2, 2, -10), "coincident"), ("ii", (1, -1, -8, 3, -3, -16), "parallel"),
          ("iii", (2, 1, -6, 4, -2, -4), "intersecting"), ("iv", (2, -2, -2, 4, -4, -5), "parallel")]
for p, co, v in EX31Q4: check(nature(*co) == v, f"3.1 Q4 {p}")
unique(2*x + y - 6, 4*x - 2*y - 4, (2, 2), "3.1 Q4 iii")
unique(x + y - 36, x - y - 4, (20, 16), "3.1 Q5")
check(nature(2, 3, -8, 3, 2, -7) == "intersecting" and nature(2, 3, -8, 4, 6, -9) == "parallel" and nature(2, 3, -8, 4, 6, -16) == "coincident", "3.1 Q6")
unique(x - y + 1, 3*x + 2*y - 12, (2, 3), "3.1 Q7")
# Exercise 3.2
unique(x + y - 14, x - y - 4, (9, 5), "3.2 Q1 i")
unique(x - y - 3, x/3 + y/2 - 6, (9, 6), "3.2 Q1 ii (s, t)")
check(nature(3, -1, -3, 9, -3, -9) == "coincident", "3.2 Q1 iii")
unique(R(2, 10)*x + R(3, 10)*y - R(13, 10), R(4, 10)*x + R(5, 10)*y - R(23, 10), (2, 3), "3.2 Q1 iv")
check(sol(sqrt(2)*x + sqrt(3)*y, sqrt(3)*x - sqrt(8)*y) == [(0, 0)], "3.2 Q1 v")
unique(R(3, 2)*x - R(5, 3)*y + 2, x/3 + y/2 - R(13, 6), (2, 3), "3.2 Q1 vi")
unique(2*x + 3*y - 11, 2*x - 4*y + 24, (-2, 5), "3.2 Q2"); check(5 == -1 * -2 + 3, "m = -1")
unique(x - y - 26, x - 3*y, (39, 13), "3.2 Q3 i")
unique(x + y - 180, x - y - 18, (99, 81), "3.2 Q3 ii")
unique(7*x + 6*y - 3800, 3*x + 5*y - 1750, (500, 50), "3.2 Q3 iii")
unique(x + 10*y - 105, x + 15*y - 155, (5, 10), "3.2 Q3 iv"); check(5 + 25 * 10 == 255, "taxi 25 km")
unique(11*(x + 2) - 9*(y + 2), 6*(x + 3) - 5*(y + 3), (7, 9), "3.2 Q3 v")
unique(x + 5 - 3*(y + 5), x - 5 - 7*(y - 5), (40, 10), "3.2 Q3 vi")
# Exercise 3.3
unique(x + y - 5, 2*x - 3*y - 4, (R(19, 5), R(6, 5)), "3.3 Q1 i")
unique(3*x + 4*y - 10, 2*x - 2*y - 2, (2, 1), "3.3 Q1 ii")
unique(3*x - 5*y - 4, 9*x - 2*y - 7, (R(9, 13), R(-5, 13)), "3.3 Q1 iii")
unique(x/2 + 2*y/3 + 1, x - y/3 - 3, (2, -3), "3.3 Q1 iv")
unique(x + 1 - (y - 1), 2*x - (y + 1), (3, 5), "3.3 Q2 i")
unique(x - 5 - 3*(y - 5), x + 10 - 2*(y + 10), (50, 20), "3.3 Q2 ii")
unique(x + y - 9, 9*(10*x + y) - 2*(10*y + x), (1, 8), "3.3 Q2 iii")
unique(x + y - 25, 50*x + 100*y - 2000, (10, 15), "3.3 Q2 iv")
unique(x + 4*y - 27, x + 2*y - 21, (15, 3), "3.3 Q2 v")
# Examples and board-style
unique(x + 3*y - 6, 2*x - 3*y - 12, (6, 0), "eg graphical")
unique(7*x - 15*y - 2, x + 2*y - 3, (R(49, 29), R(19, 29)), "eg substitution")
unique(x - 7 - 7*(y - 7), x + 3 - 3*(y + 3), (42, 12), "eg ages")
unique(9*x - 4*y - 2000, 7*x - 3*y - 2000, (2000, 4000), "eg incomes"); check((9 * 2000, 7 * 2000) == (18000, 14000), "incomes")
check(nature(2, 3, -8, 4, 6, -7) == "parallel", "eg no solution")
unique(x + y - 6, x - y - 2, (4, 2), "eg digits 42"); unique(x + y - 6, x - y + 2, (2, 4), "eg digits 24")
check(nature(1, 2, 5, -3, -6, 1) == "parallel", "mcq01")
check(nature(2, 3, -7, 4, 6, -14) == "coincident", "mcq02 k=6")
check(nature(1, 2, -3, 5, 10, 7) == "parallel", "mcq03 k=10")
unique(x - y - 2, x + y - 4, (3, 1), "mcq04")
check(nature(6, -3, 10, 2, -1, 9) == "parallel", "mcq05")
unique(x - 3*y, x + 10 - 2*(y + 10), (30, 10), "mcq06 father son")
unique(x + y - 35, x - y - 13, (24, 11), "mcq07")
unique(2*x + 3*y - 12, 3*x - 2*y - 5, (3, 2), "mcq08 x+y=5")
check(nature(2, 1, -6, 4, -2, -4) == "intersecting" and nature(2, -2, -2, 4, -4, -5) == "parallel" and nature(1, 1, -5, 2, 2, -12) == "parallel", "mcq09")
check(nature(3, -1, -3, 9, -3, -9) == "coincident", "mcq10")
check(nature(2, -1, -5, 6, -3, -15) == "coincident" and nature(2, -1, -5, 6, -3, -14) == "parallel", "mcq11 c=15")
check(nature(1, 1, -4, 2, 2, -8) == "coincident", "ar1"); check(nature(3, -2, -5, 6, -4, -9) == "parallel", "ar2")
unique(x - y - 1, x + y - 5, (3, 2), "ar3"); check(nature(2, 3, -5, 4, 6, -10) == "coincident", "ar4"); check(3 * 2 + 1 * 1 == 7, "ar5")
k = symbols("k")
check(set(solve(Eq(k * k, 36), k)) == {-6, 6} and nature(-6, 3, 9, 12, -6, 6) == "parallel" and nature(6, 3, -3, 12, 6, -6) == "coincident", "sa k=-6")
unique(x + y - 7, 3*x - y - 1, (2, 5), "vsa1")
check(nature(4, 6, -7, 2, 3, -9) == "parallel", "vsa2")
unique(x + y - 11, x - y - 3, (7, 4), "sa digits 74"); check(7 * 10 + 4 + 4 * 10 + 7 == 121, "121")
unique(x - y - 20, x + y - 100, (60, 40), "sa cars")
unique(x + 20*y - 1000, x + 26*y - 1180, (400, 30), "sa hostel")
unique(R(108, 100)*x + R(90, 100)*y - 1008, R(110, 100)*x + R(92, 100)*y - 1028, (600, 400), "la saree")
unique(2*x + 3*y - 12, x - y - 1, (3, 2), "la graphical"); check(R(1, 2) * (6 - 1) * 2 == 5, "la area")
unique(2*x + 3*y - 55, 4*x + y - 65, (14, 9), "cb cafe"); check(5 * 14 + 2 * 9 == 88, "cb cafe iii")
unique(3*x + 2*y - 800, 2*x + 3*y - 700, (200, 100), "cb tickets"); check(2 * 200 + 2 * 100 == 600, "cb tickets iii")
# CBSE SQP 2025-26
unique(3*x - 5*y - 15000, 4*x - 7*y - 15000, (30000, 15000), "sqp31A"); check((3 * 30000, 4 * 30000) == (90000, 120000), "incomes")
unique(2*x + y - 6, 2*x - y - 2, (2, 2), "sqp31B"); check(R(1, 2) * (3 - 1) * 2 == 2, "sqp31B area")

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch03.{id_}", "type": type_, **kw}
def graph(id_, title, lines, points, xr, **kw):
    return {"id": f"ch03.{id_}", "type": "function_graph", "title": title, "x_range": xr,
            "curves": [{"polynomial": line(*l[0]), "label": l[1]} for l in lines], "points": points, **kw}

sections = [
 {"id": "s1", "title": "Two clues, one answer", "blocks": [
  b("s1.hook", "hook", title="The shopkeeper's puzzle",
    body="At a stationery shop, 5 pencils and 7 pens cost ₹50, while 7 pencils and 5 pens cost ₹46. The shopkeeper has forgotten the price of one pencil and one pen!\n\n"
         "One clue alone cannot tell you the prices: many combinations fit. But **two clues together** pin down exactly one answer. "
         "In this chapter you will learn three ways to solve such puzzles: by drawing graphs, by substitution and by elimination."),
  b("s1.inspiration", "inspiration", title="The 23-year-old who wrote a mathematics classic", person="Aryabhata", years="476–550 CE",
    body="Aryabhata wrote his famous book, the *Aryabhatiya*, in the year 499, when he was just 23 years old. In it he gave the value of $\\pi$ correct to four decimal places "
         "and explained that the Earth rotates on its axis.\n\nHe also invented the *kuttaka* ('pulveriser') method to solve equations like $ax + by = c$ in whole numbers, "
         "a problem that kept mathematicians busy for centuries. In 1975 India named its first satellite **Aryabhata** in his honour.",
    quote="Age is no barrier: Aryabhata changed mathematics at 23. What will you change?",
    future="Systems of equations run the world: GPS finds your location by solving equations, airlines plan routes with them, and businesses use them to set prices and plan production."),
  b("s1.socratic", "socratic_question",
    question="Riya says: 'I am thinking of two numbers. Their sum is 10.' Can you find the two numbers?",
    options=["No: many pairs work, like 3 and 7 or 4 and 6", "Yes, they must be 5 and 5", "Yes, they must be 1 and 9"], correct_index=0,
    explanation="With only one clue there are infinitely many answers. Riya then adds: 'Their difference is 4.' Now only one pair works: 7 and 3. Two clues together give one answer."),
 ]},
 {"id": "s2", "title": "Pair of linear equations", "blocks": [
  b("s2.reveal", "theory", title="What is a pair of linear equations?", revision=True,
    body="An equation of the form $ax + by + c = 0$, where $a, b, c$ are real numbers and $a$ and $b$ are not both zero, is a **linear equation in two variables**. "
         "Its graph is a **straight line**.\n\nTwo such equations in the same variables form a **pair of linear equations**:\n\n"
         "$$a_1x + b_1y + c_1 = 0, \\qquad a_2x + b_2y + c_2 = 0$$\n\n"
         "A **solution** is a pair of values $(x, y)$ that satisfies **both** equations at the same time."),
  b("s2.form", "worked_example", title="Forming the equations",
    problem="10 students of Class X took part in a Mathematics quiz. The number of girls is 4 more than the number of boys. Form the pair of equations.",
    steps=["Let the number of girls be $x$ and the number of boys be $y$.", "Total students: $x + y = 10$", "Girls are 4 more than boys: $x - y = 4$"],
    answer="$x + y = 10$ and $x - y = 4$"),
  b("s2.check", "knowledge_check", question="Is $(3, 2)$ a solution of the pair $x + y = 5$ and $2x - y = 4$?",
    options=["Yes, it satisfies both equations", "No, it satisfies only the first equation", "No, it satisfies only the second equation", "No, it satisfies neither equation"],
    correct_index=0, explanation="$3 + 2 = 5$ ✓ and $2 \\times 3 - 2 = 4$ ✓. It satisfies both, so it is a solution."),
 ]},
 {"id": "s3", "title": "The graphical method", "blocks": [
  b("s3.discovery", "discovery", title="Draw both lines and look",
    body="Each equation is a line. A solution of the pair is a point on **both** lines, so it is where the lines **meet**. "
         "For the quiz: $x + y = 10$ and $x - y = 4$. Watch the two lines being drawn."),
  graph("s3.g1", "Intersecting lines: exactly one solution", [((1, 1, 10), "x + y = 10"), ((1, -1, 4), "x - y = 4")],
        [{"x": 7, "y": 3, "label": "(7, 3)", "on": [0, 1]}], [-1, 11]),
  b("s3.g1note", "theory", title="Reading the graph",
    body="The lines meet at $(7, 3)$: 7 girls and 3 boys. Check: $7 + 3 = 10$ ✓, $7 - 3 = 4$ ✓."),
  graph("s3.g2", "Parallel lines: no solution", [((1, -1, 8), "x - y = 8"), ((3, -3, 16), "3x - 3y = 16")], [], [-1, 10]),
  graph("s3.g3", "Coincident lines: infinitely many solutions", [((1, 1, 5), "x + y = 5"), ((2, 2, 10), "2x + 2y = 10")], [], [-1, 6]),
  b("s3.reveal", "theory", title="Three possibilities", revision=True,
    body="For $a_1x + b_1y + c_1 = 0$ and $a_2x + b_2y + c_2 = 0$:\n\n"
         "- If $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$: the lines **intersect** at one point. **Exactly one solution**: the pair is **consistent**.\n"
         "- If $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$: the lines are **parallel**. **No solution**: the pair is **inconsistent**.\n"
         "- If $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} = \\dfrac{c_1}{c_2}$: the lines are **coincident**. **Infinitely many solutions**: the pair is **dependent** (and consistent)."),
  b("s3.eg", "worked_example", title="NCERT example: solve graphically",
    problem="Check graphically whether the pair $x + 3y = 6$ and $2x - 3y = 12$ is consistent. If so, solve it graphically.",
    steps=["For $x + 3y = 6$: points $(0, 2)$ and $(6, 0)$.", "For $2x - 3y = 12$: points $(0, -4)$ and $(6, 0)$.",
           "Both lines pass through $(6, 0)$, so they intersect there."],
    answer="Consistent; the solution is $x = 6$, $y = 0$."),
  graph("s3.g4", "The lines meet at (6, 0)", [((1, 3, 6), "x + 3y = 6"), ((2, -3, 12), "2x - 3y = 12")], [{"x": 6, "y": 0, "label": "(6, 0)", "on": [0, 1]}], [-1, 8]),
  b("s3.check1", "knowledge_check", question="The pair $6x - 3y + 10 = 0$ and $2x - y + 9 = 0$ represents:",
    options=["parallel lines", "intersecting lines", "coincident lines", "perpendicular lines"], correct_index=0,
    explanation="$\\dfrac{6}{2} = 3$, $\\dfrac{-3}{-1} = 3$, $\\dfrac{10}{9} \\neq 3$. So $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$: parallel."),
  b("s3.check2", "knowledge_check", question="For what value of $k$ do $2x + 3y = 7$ and $4x + ky = 14$ have infinitely many solutions?",
    options=["$6$", "$3$", "$7$", "$14$"], correct_index=0,
    explanation="Coincident lines need $\\dfrac{2}{4} = \\dfrac{3}{k} = \\dfrac{7}{14}$, so $k = 6$."),
  b("s3.tip", "teacher_tip", title="Two points are enough",
    body="Remind students that two points fix a line, and a third point checks the drawing. Choosing points where $x = 0$ or $y = 0$ makes the arithmetic easy. "
         "On the panel, pause the graph as the lines meet and ask the class to read the coordinates."),
 ]},
 {"id": "s4", "title": "Substitution method", "blocks": [
  b("s4.socratic", "socratic_question",
    question="From $x + y = 14$, we can write $y = 14 - x$. What can we do with this in the other equation $x - y = 4$?",
    options=["Put $14 - x$ in place of $y$, leaving one variable", "Nothing: the equations stay separate", "Add 14 to both sides"], correct_index=0,
    explanation="Replacing $y$ by $14 - x$ gives $x - (14 - x) = 4$, an equation in $x$ alone: $2x = 18$, $x = 9$, and $y = 5$."),
  b("s4.reveal", "theory", title="Steps of the substitution method", revision=True,
    body="1. From one equation, write one variable in terms of the other, e.g. $y = \\ldots$\n"
         "2. **Substitute** it into the other equation, which now has one variable. Solve it.\n"
         "3. Put this value back to find the other variable.\n"
         "4. **Check** in both original equations.\n\n"
         "If the variable disappears and you get a **true** statement like $9 = 9$, there are infinitely many solutions; "
         "a **false** statement like $0 = 5$ means no solution."),
  b("s4.eg1", "worked_example", title="NCERT example",
    problem="Solve $7x - 15y = 2$ and $x + 2y = 3$ by the substitution method.",
    steps=["From $x + 2y = 3$: $x = 3 - 2y$.", "Substitute: $7(3 - 2y) - 15y = 2$, so $21 - 29y = 2$ and $y = \\dfrac{19}{29}$.",
           "Then $x = 3 - 2 \\times \\dfrac{19}{29} = \\dfrac{49}{29}$.", "Check: $7 \\times \\dfrac{49}{29} - 15 \\times \\dfrac{19}{29} = \\dfrac{343 - 285}{29} = 2$ ✓"],
    answer="$x = \\dfrac{49}{29}$, $y = \\dfrac{19}{29}$"),
  b("s4.eg2", "worked_example", title="NCERT example: ages",
    problem="Aftab tells his daughter, 'Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be.' Find their present ages.",
    steps=["Let Aftab's age be $x$ and his daughter's age be $y$.", "Seven years ago: $x - 7 = 7(y - 7)$, i.e. $x - 7y = -42$.",
           "Three years from now: $x + 3 = 3(y + 3)$, i.e. $x - 3y = 6$.", "From the second, $x = 3y + 6$. Substitute: $3y + 6 - 7y = -42$, so $y = 12$ and $x = 42$."],
    answer="Aftab is 42 years old and his daughter is 12."),
  b("s4.check", "knowledge_check", question="Solving $x + y = 14$ and $x - y = 4$ by substitution gives:",
    options=["$x = 9, y = 5$", "$x = 5, y = 9$", "$x = 10, y = 4$", "$x = 7, y = 7$"], correct_index=0,
    explanation="$y = 14 - x$, so $x - (14 - x) = 4$, $x = 9$, $y = 5$."),
 ]},
 {"id": "s5", "title": "Elimination method", "blocks": [
  b("s5.reveal", "theory", title="Steps of the elimination method", revision=True,
    body="1. Multiply the equations by suitable non-zero numbers so that the coefficients of one variable become **equal** (or opposite).\n"
         "2. **Subtract** (or add) the equations to **eliminate** that variable.\n"
         "3. Solve for the remaining variable, then substitute back.\n\n"
         "As in substitution: a true statement with no variable left means infinitely many solutions; a false one means no solution."),
  b("s5.eg1", "worked_example", title="NCERT example: incomes",
    problem="The ratio of incomes of two persons is 9 : 7 and the ratio of their expenditures is 4 : 3. If each of them manages to save ₹2000 per month, find their monthly incomes.",
    steps=["Let the incomes be $9x$ and $7x$ and the expenditures $4y$ and $3y$.", "Savings: $9x - 4y = 2000$ and $7x - 3y = 2000$.",
           "Multiply the first by 3 and the second by 4: $27x - 12y = 6000$ and $28x - 12y = 8000$.", "Subtract: $x = 2000$. So incomes are $9 \\times 2000 = 18000$ and $7 \\times 2000 = 14000$."],
    answer="₹18000 and ₹14000 per month"),
  b("s5.eg2", "worked_example", title="NCERT example: digits",
    problem="The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits differ by 2, find the number. How many such numbers are there?",
    steps=["Let the tens digit be $x$ and the units digit be $y$. Number $= 10x + y$, reversed $= 10y + x$.",
           "$(10x + y) + (10y + x) = 66$, so $x + y = 6$.", "Digits differ by 2: $x - y = 2$ or $y - x = 2$.",
           "Adding to $x + y = 6$: $x = 4, y = 2$ (number 42) or $x = 2, y = 4$ (number 24)."],
    answer="42 or 24: two such numbers."),
  b("s5.memory", "memory_trick", title="Which method?", revision=True,
    body="- A variable already has coefficient 1 (like $x + 2y = 3$)? **Substitution** is quickest.\n"
         "- Coefficients easy to match (like $3x$ and $6x$)? **Elimination**.\n"
         "- Asked about the *nature* of solutions? Compare the **ratios** first: no solving needed."),
  b("s5.check", "knowledge_check", question="To eliminate $y$ from $2x + 3y = 12$ and $3x - 2y = 5$, a good first step is to:",
    options=["multiply the first by 2 and the second by 3, then add", "add the equations as they are", "multiply both by 3", "subtract the equations as they are"],
    correct_index=0, explanation="$4x + 6y = 24$ and $9x - 6y = 15$; adding gives $13x = 39$, $x = 3$, then $y = 2$."),
  b("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="- Subtracting when the signs call for adding (or the other way round). Look at the signs of the matched coefficients.\n"
         "- Multiplying only one side of an equation.\n"
         "- In word problems, not writing what $x$ and $y$ stand for, which costs marks.\n"
         "- Forgetting to check the answer in **both** original equations.\n"
         "- In ratio questions, comparing $\\dfrac{c_1}{c_2}$ without first writing both equations in the form $ax + by + c = 0$."),
 ]},
 {"id": "s6", "title": "Think, connect, master", "blocks": [
  b("s6.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend, using a drawing of two lines, why a pair of linear equations can never have exactly two solutions."),
  b("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 4, Quadratic Equations** and **Chapter 7, Coordinate Geometry** use the same skills of forming and solving equations.\n"
         "- **Commerce and Economics:** finding the break-even point where cost equals revenue is solving a pair of linear equations.\n"
         "- **Chemistry:** balancing chemical equations can be done by solving simultaneous equations."),
  b("s6.mastery", "mastery", title="Mastery challenge",
    body="A shopkeeper sells a saree at 8% profit and a sweater at 10% discount and gets ₹1008. If she sells the saree at 10% profit and the sweater at 8% discount, she gets ₹1028. "
         "Find the cost price of the saree and the list price of the sweater.\n\n"
         "**Answer:** $1.08x + 0.9y = 1008$ and $1.1x + 0.92y = 1028$ give $x = 600$, $y = 400$: the saree costs ₹600 and the sweater is listed at ₹400."),
  b("s6.summary", "summary", title="Chapter summary",
    body="- A pair of linear equations in two variables can be solved by the **graphical**, **substitution** or **elimination** method.\n"
         "- Intersecting lines: one solution (consistent). Parallel lines: no solution (inconsistent). Coincident lines: infinitely many solutions (dependent).\n"
         "- $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$: unique solution. $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$: none. $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} = \\dfrac{c_1}{c_2}$: infinitely many.\n"
         "- Always check the solution in both equations."),
  b("s6.examtips", "exam_tips", title="Board exam tips",
    body="- In word problems, start with 'Let ... be $x$ and ... be $y$': this line carries marks.\n"
         "- For 'find $k$' questions, write the required ratio condition first, then solve for $k$.\n"
         "- In graph questions, show a table of at least two points for each line, label the lines, and mark the intersection clearly.\n"
         "- When asked 'consistent or inconsistent', state the ratios and the conclusion in words."),
  b("s6.flash1", "flashcard", front="When does a pair of linear equations have no solution?", back="When $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$: the lines are parallel."),
  b("s6.flash2", "flashcard", front="When does it have infinitely many solutions?", back="When $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} = \\dfrac{c_1}{c_2}$: the lines coincide."),
  b("s6.flash3", "flashcard", front="What does 'consistent' mean?", back="The pair has at least one solution (one, or infinitely many)."),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Pair of Linear Equations in Two Variables",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 3,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: graphical method, consistency, substitution and elimination. Cross-multiplication and equations reducible to linear form are not in the board syllabus and are not included.",
  "concepts": ["linear_equation_two_variables", "graphical_solution", "consistency", "substitution_method", "elimination_method"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
LIN, GR, CON, SUB, ELI = "linear_equation_two_variables", "graphical_solution", "consistency", "substitution_method", "elimination_method"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch03.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
MS3_SOLVE = ["1 mark: forming / rearranging the equations", "1 mark: eliminating or substituting correctly", "1 mark: both values"]
MS2_SOLVE = ["1 mark: method", "1 mark: both values"]
MS2_RATIO = ["1 mark: ratios $\\dfrac{a_1}{a_2}, \\dfrac{b_1}{b_2}, \\dfrac{c_1}{c_2}$", "1 mark: conclusion"]
MS3_GRAPH = ["1 mark: table of points for both lines", "1 mark: correct graphs", "1 mark: solution / conclusion"]

q("ex3_1.q1.i", "short_answer", 3, [LIN, GR], ex("3.1", 1, "i"),
  "10 students of Class X took part in a Mathematics quiz. If the number of girls is 4 more than the number of boys, find the number of boys and girls who took part in the quiz. Form the pair of linear equations and solve it graphically.",
  answer_steps=["Let girls $= x$, boys $= y$: $x + y = 10$ and $x - y = 4$.", "Points: $x + y = 10$: $(0, 10), (10, 0)$; $x - y = 4$: $(4, 0), (0, -4)$.", "The lines meet at $(7, 3)$: 7 girls and 3 boys."],
  marking_scheme=MS3_GRAPH)
q("ex3_1.q1.ii", "short_answer", 3, [LIN, GR], ex("3.1", 1, "ii"),
  "5 pencils and 7 pens together cost ₹50, whereas 7 pencils and 5 pens together cost ₹46. Find the cost of one pencil and that of one pen. Form the pair of linear equations and solve it graphically.",
  answer_steps=["Let a pencil cost ₹$x$ and a pen ₹$y$: $5x + 7y = 50$ and $7x + 5y = 46$.", "Points: $5x + 7y = 50$: $(10, 0), (3, 5)$; $7x + 5y = 46$: $(3, 5), (8, -2)$.", "The lines meet at $(3, 5)$: a pencil costs ₹3 and a pen ₹5."],
  marking_scheme=MS3_GRAPH)
VERDICT = {"intersecting": "intersect at a point", "parallel": "are parallel", "coincident": "are coincident"}
EQ31Q2 = {"i": ("5x - 4y + 8 = 0", "7x + 6y - 9 = 0", "\\dfrac{5}{7} \\neq \\dfrac{-4}{6}"),
          "ii": ("9x + 3y + 12 = 0", "18x + 6y + 24 = 0", "\\dfrac{9}{18} = \\dfrac{3}{6} = \\dfrac{12}{24}"),
          "iii": ("6x - 3y + 10 = 0", "2x - y + 9 = 0", "\\dfrac{6}{2} = \\dfrac{-3}{-1} \\neq \\dfrac{10}{9}")}
for p, co, v in EX31Q2:
    e1, e2, ratio = EQ31Q2[p]
    q(f"ex3_1.q2.{p}", "very_short_answer", 2, [CON], ex("3.1", 2, p),
      f"On comparing the ratios $\\dfrac{{a_1}}{{a_2}}$, $\\dfrac{{b_1}}{{b_2}}$ and $\\dfrac{{c_1}}{{c_2}}$, find out whether the lines representing the pair ${e1}$ and ${e2}$ intersect at a point, are parallel or are coincident.", "easy",
      answer_steps=[f"${ratio}$", f"Hence the lines {VERDICT[v]}."], marking_scheme=MS2_RATIO)
EQ31Q3 = {"i": ("3x + 2y = 5", "2x - 3y = 7", "\\dfrac{3}{2} \\neq \\dfrac{2}{-3}"),
          "ii": ("2x - 3y = 8", "4x - 6y = 9", "\\dfrac{2}{4} = \\dfrac{-3}{-6} \\neq \\dfrac{8}{9}"),
          "iii": ("\\dfrac{3}{2}x + \\dfrac{5}{3}y = 7", "9x - 10y = 14", "\\dfrac{3/2}{9} = \\dfrac{1}{6} \\neq \\dfrac{5/3}{-10} = -\\dfrac{1}{6}"),
          "iv": ("5x - 3y = 11", "-10x + 6y = -22", "\\dfrac{5}{-10} = \\dfrac{-3}{6} = \\dfrac{11}{-22} = -\\dfrac{1}{2}"),
          "v": ("\\dfrac{4}{3}x + 2y = 8", "2x + 3y = 12", "\\dfrac{4/3}{2} = \\dfrac{2}{3} = \\dfrac{8}{12} = \\dfrac{2}{3}")}
CONS = {"intersecting": "consistent (unique solution)", "parallel": "inconsistent (no solution)", "coincident": "consistent (infinitely many solutions)"}
for p, co, v in EX31Q3:
    e1, e2, ratio = EQ31Q3[p]
    q(f"ex3_1.q3.{p}", "very_short_answer", 2, [CON], ex("3.1", 3, p),
      f"On comparing the ratios $\\dfrac{{a_1}}{{a_2}}$, $\\dfrac{{b_1}}{{b_2}}$ and $\\dfrac{{c_1}}{{c_2}}$, find out whether the pair ${e1}$; ${e2}$ is consistent or inconsistent.", "easy",
      answer_steps=[f"${ratio}$", f"Hence the pair is {CONS[v]}."], marking_scheme=MS2_RATIO)
EQ31Q4 = {"i": ("x + y = 5", "2x + 2y = 10", "\\dfrac{1}{2} = \\dfrac{1}{2} = \\dfrac{5}{10}", "Consistent: the lines coincide, so every point on $x + y = 5$ is a solution (infinitely many), e.g. $(0, 5), (5, 0)$."),
          "ii": ("x - y = 8", "3x - 3y = 16", "\\dfrac{1}{3} = \\dfrac{-1}{-3} \\neq \\dfrac{8}{16}", "Inconsistent: the lines are parallel, so there is no solution."),
          "iii": ("2x + y - 6 = 0", "4x - 2y - 4 = 0", "\\dfrac{2}{4} \\neq \\dfrac{1}{-2}", "Consistent: plotting $(0, 6), (3, 0)$ and $(0, -2), (1, 0)$, the lines meet at $(2, 2)$, so $x = 2$, $y = 2$."),
          "iv": ("2x - 2y - 2 = 0", "4x - 4y - 5 = 0", "\\dfrac{2}{4} = \\dfrac{-2}{-4} \\neq \\dfrac{-2}{-5}", "Inconsistent: the lines are parallel, so there is no solution.")}
for p, co, v in EX31Q4:
    e1, e2, ratio, concl = EQ31Q4[p]
    q(f"ex3_1.q4.{p}", "short_answer", 3, [CON, GR], ex("3.1", 4, p),
      f"Is the pair ${e1}$, ${e2}$ consistent or inconsistent? If consistent, obtain the solution graphically.",
      answer_steps=[f"${ratio}$", concl], marking_scheme=MS3_GRAPH)
q("ex3_1.q5", "short_answer", 3, [LIN], ex("3.1", 5),
  "Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m. Find the dimensions of the garden.",
  answer_steps=["Let length $= x$ m and width $= y$ m: $x + y = 36$ and $x - y = 4$.", "Adding: $2x = 40$, $x = 20$; then $y = 16$.", "The garden is 20 m long and 16 m wide."],
  marking_scheme=MS3_SOLVE)
for p, kind, eqn, why in [("i", "intersecting lines", "3x + 2y - 7 = 0", "\\dfrac{2}{3} \\neq \\dfrac{3}{2}"),
                          ("ii", "parallel lines", "4x + 6y - 9 = 0", "\\dfrac{2}{4} = \\dfrac{3}{6} \\neq \\dfrac{-8}{-9}"),
                          ("iii", "coincident lines", "4x + 6y - 16 = 0", "\\dfrac{2}{4} = \\dfrac{3}{6} = \\dfrac{-8}{-16}")]:
    q(f"ex3_1.q6.{p}", "very_short_answer", 2, [CON], ex("3.1", 6, p),
      f"Given the linear equation $2x + 3y - 8 = 0$, write another linear equation in two variables such that the geometrical representation of the pair so formed is {kind}.", "easy",
      answer_steps=[f"One answer: ${eqn}$ (many answers are possible).", f"Check: ${why}$"], marking_scheme=["1 mark: suitable equation", "1 mark: justification by ratios"])
q("ex3_1.q7", "short_answer", 3, [GR], ex("3.1", 7),
  "Draw the graphs of the equations $x - y + 1 = 0$ and $3x + 2y - 12 = 0$. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.",
  answer_steps=["$x - y + 1 = 0$ passes through $(-1, 0)$ and $(0, 1)$; $3x + 2y - 12 = 0$ through $(4, 0)$ and $(0, 6)$.", "The lines meet at $(2, 3)$.",
                "The vertices of the triangle are $(-1, 0)$, $(4, 0)$ and $(2, 3)$."], marking_scheme=MS3_GRAPH)
# Exercise 3.2
for p, e1, e2, ans in [("i", "x + y = 14", "x - y = 4", "$x = 9$, $y = 5$"), ("ii", "s - t = 3", "\\dfrac{s}{3} + \\dfrac{t}{2} = 6", "$s = 9$, $t = 6$"),
                       ("iv", "0.2x + 0.3y = 1.3", "0.4x + 0.5y = 2.3", "$x = 2$, $y = 3$"),
                       ("v", "\\sqrt{2}x + \\sqrt{3}y = 0", "\\sqrt{3}x - \\sqrt{8}y = 0", "$x = 0$, $y = 0$"),
                       ("vi", "\\dfrac{3x}{2} - \\dfrac{5y}{3} = -2", "\\dfrac{x}{3} + \\dfrac{y}{2} = \\dfrac{13}{6}", "$x = 2$, $y = 3$")]:
    q(f"ex3_2.q1.{p}", "very_short_answer", 2, [SUB], ex("3.2", 1, p), f"Solve the pair of linear equations ${e1}$ and ${e2}$ by the substitution method.", "easy" if p in ("i",) else "medium",
      answer_steps=["Express one variable in terms of the other from one equation and substitute it into the other equation.", f"Solving gives {ans}."], marking_scheme=MS2_SOLVE)
q("ex3_2.q1.iii", "very_short_answer", 2, [SUB, CON], ex("3.2", 1, "iii"), "Solve the pair of linear equations $3x - y = 3$ and $9x - 3y = 9$ by the substitution method.",
  answer_steps=["From the first, $y = 3x - 3$. Substituting: $9x - 3(3x - 3) = 9$, i.e. $9 = 9$, which is always true.",
                "So the pair has infinitely many solutions: every $(x, 3x - 3)$, e.g. $(1, 0), (2, 3)$."], marking_scheme=MS2_SOLVE)
q("ex3_2.q2", "short_answer", 3, [SUB], ex("3.2", 2), "Solve $2x + 3y = 11$ and $2x - 4y = -24$ and hence find the value of $m$ for which $y = mx + 3$.",
  answer_steps=["From the first, $2x = 11 - 3y$. Substituting: $11 - 3y - 4y = -24$, so $y = 5$ and $x = -2$.", "Put $x = -2, y = 5$ in $y = mx + 3$: $5 = -2m + 3$.", "$m = -1$"],
  marking_scheme=["1 mark: $y = 5$", "1 mark: $x = -2$", "1 mark: $m = -1$"])
WORD32 = [
 ("i", "The difference between two numbers is 26 and one number is three times the other. Find them.", ["Let the numbers be $x$ and $y$ ($x > y$): $x - y = 26$ and $x = 3y$.", "$3y - y = 26$, so $y = 13$ and $x = 39$.", "The numbers are 39 and 13."]),
 ("ii", "The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.", ["Let the angles be $x$ and $y$ ($x > y$): $x + y = 180$ and $x - y = 18$.", "$x = y + 18$, so $2y + 18 = 180$, $y = 81$ and $x = 99$.", "The angles are $99^\\circ$ and $81^\\circ$."]),
 ("iii", "The coach of a cricket team buys 7 bats and 6 balls for ₹3800. Later, she buys 3 bats and 5 balls for ₹1750. Find the cost of each bat and each ball.", ["Let a bat cost ₹$x$ and a ball ₹$y$: $7x + 6y = 3800$ and $3x + 5y = 1750$.", "From the second, $x = \\dfrac{1750 - 5y}{3}$. Substituting and solving: $y = 50$, then $x = 500$.", "A bat costs ₹500 and a ball costs ₹50."]),
 ("iv", "The taxi charges in a city consist of a fixed charge together with the charge for the distance covered. For a distance of 10 km, the charge paid is ₹105 and for a journey of 15 km, the charge paid is ₹155. What are the fixed charges and the charge per km? How much does a person have to pay for travelling a distance of 25 km?", ["Let the fixed charge be ₹$x$ and the charge per km ₹$y$: $x + 10y = 105$ and $x + 15y = 155$.", "$x = 105 - 10y$, so $105 + 5y = 155$, $y = 10$ and $x = 5$.", "Fixed charge ₹5, ₹10 per km; for 25 km: $5 + 25 \\times 10 = 255$, i.e. ₹255."]),
 ("v", "A fraction becomes $\\dfrac{9}{11}$, if 2 is added to both the numerator and the denominator. If 3 is added to both the numerator and the denominator, it becomes $\\dfrac{5}{6}$. Find the fraction.", ["Let the fraction be $\\dfrac{x}{y}$: $11(x + 2) = 9(y + 2)$ and $6(x + 3) = 5(y + 3)$, i.e. $11x - 9y = -4$ and $6x - 5y = -3$.", "From the second, $x = \\dfrac{5y - 3}{6}$. Substituting and solving: $y = 9$, $x = 7$.", "The fraction is $\\dfrac{7}{9}$."]),
 ("vi", "Five years hence, the age of Jacob will be three times that of his son. Five years ago, Jacob's age was seven times that of his son. What are their present ages?", ["Let Jacob's age be $x$ and his son's $y$: $x + 5 = 3(y + 5)$ and $x - 5 = 7(y - 5)$.", "$x = 3y + 10$, so $3y + 5 = 7y - 35$, $y = 10$ and $x = 40$.", "Jacob is 40 years old and his son is 10."]),
]
for p, text, steps in WORD32:
    q(f"ex3_2.q3.{p}", "short_answer", 3, [LIN, SUB], ex("3.2", 3, p), "Form the pair of linear equations and solve it by the substitution method: " + text, answer_steps=steps, marking_scheme=MS3_SOLVE)
# Exercise 3.3
for p, e1, e2, ans in [("i", "x + y = 5", "2x - 3y = 4", "$x = \\dfrac{19}{5}$, $y = \\dfrac{6}{5}$"), ("ii", "3x + 4y = 10", "2x - 2y = 2", "$x = 2$, $y = 1$"),
                       ("iii", "3x - 5y - 4 = 0", "9x = 2y + 7", "$x = \\dfrac{9}{13}$, $y = -\\dfrac{5}{13}$"), ("iv", "\\dfrac{x}{2} + \\dfrac{2y}{3} = -1", "x - \\dfrac{y}{3} = 3", "$x = 2$, $y = -3$")]:
    q(f"ex3_3.q1.{p}", "very_short_answer", 2, [ELI, SUB], ex("3.3", 1, p), f"Solve the pair of linear equations ${e1}$ and ${e2}$ by the elimination method and the substitution method.",
      answer_steps=["Make the coefficients of one variable equal, subtract (or add) to eliminate it, and check by substitution.", f"Both methods give {ans}."], marking_scheme=MS2_SOLVE)
WORD33 = [
 ("i", "A fraction becomes 1 if we add 1 to the numerator and subtract 1 from the denominator. It becomes $\\dfrac{1}{2}$ if we only add 1 to the denominator. What is the fraction?", ["Let the fraction be $\\dfrac{x}{y}$: $x + 1 = y - 1$ and $2x = y + 1$, i.e. $x - y = -2$ and $2x - y = 1$.", "Subtracting: $x = 3$; then $y = 5$.", "The fraction is $\\dfrac{3}{5}$."]),
 ("ii", "Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu?", ["Let Nuri's age be $x$ and Sonu's $y$: $x - 5 = 3(y - 5)$ and $x + 10 = 2(y + 10)$, i.e. $x - 3y = -10$ and $x - 2y = 10$.", "Subtracting: $y = 20$; then $x = 50$.", "Nuri is 50 years old and Sonu is 20."]),
 ("iii", "The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.", ["Let the tens digit be $x$ and the units digit $y$: $x + y = 9$ and $9(10x + y) = 2(10y + x)$, i.e. $88x - 11y = 0$, so $y = 8x$.", "Then $x + 8x = 9$, $x = 1$, $y = 8$.", "The number is 18."]),
 ("iv", "Meena went to a bank to withdraw ₹2000. She asked the cashier to give her ₹50 and ₹100 notes only. Meena got 25 notes in all. Find how many notes of ₹50 and ₹100 she received.", ["Let the ₹50 notes be $x$ and the ₹100 notes $y$: $x + y = 25$ and $50x + 100y = 2000$, i.e. $x + 2y = 40$.", "Subtracting: $y = 15$; then $x = 10$.", "She received ten ₹50 notes and fifteen ₹100 notes."]),
 ("v", "A lending library has a fixed charge for the first three days and an additional charge for each day thereafter. Saritha paid ₹27 for a book kept for seven days, while Susy paid ₹21 for the book she kept for five days. Find the fixed charge and the charge for each extra day.", ["Let the fixed charge be ₹$x$ and the charge per extra day ₹$y$: $x + 4y = 27$ and $x + 2y = 21$.", "Subtracting: $2y = 6$, $y = 3$; then $x = 15$.", "Fixed charge ₹15 and ₹3 for each extra day."]),
]
for p, text, steps in WORD33:
    q(f"ex3_3.q2.{p}", "short_answer", 3, [LIN, ELI], ex("3.3", 2, p), "Form the pair of linear equations and solve it by the elimination method: " + text, answer_steps=steps, marking_scheme=MS3_SOLVE)
# NCERT examples
q("eg_graph", "short_answer", 3, [GR, CON], {"kind": "ncert_example"}, "Check graphically whether the pair of equations $x + 3y = 6$ and $2x - 3y = 12$ is consistent. If so, solve them graphically.",
  answer_steps=["$x + 3y = 6$: points $(0, 2), (6, 0)$; $2x - 3y = 12$: points $(0, -4), (6, 0)$.", "The lines intersect at $(6, 0)$, so the pair is consistent.", "Solution: $x = 6$, $y = 0$."], marking_scheme=MS3_GRAPH)
q("eg_ages", "short_answer", 3, [LIN, SUB], {"kind": "ncert_example"},
  "Aftab tells his daughter, 'Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be.' Find their present ages.",
  answer_steps=["Let Aftab's age be $x$ and his daughter's $y$: $x - 7y = -42$ and $x - 3y = 6$.", "$x = 3y + 6$, so $3y + 6 - 7y = -42$, $y = 12$.", "$x = 42$: Aftab is 42 and his daughter is 12."], marking_scheme=MS3_SOLVE)
q("eg_incomes", "short_answer", 3, [LIN, ELI], {"kind": "ncert_example"},
  "The ratio of incomes of two persons is 9 : 7 and the ratio of their expenditures is 4 : 3. If each of them manages to save ₹2000 per month, find their monthly incomes.",
  answer_steps=["Incomes $9x, 7x$; expenditures $4y, 3y$: $9x - 4y = 2000$ and $7x - 3y = 2000$.", "Multiply by 3 and 4: $27x - 12y = 6000$, $28x - 12y = 8000$; subtracting, $x = 2000$.", "Incomes: ₹18000 and ₹14000."], marking_scheme=MS3_SOLVE)
q("eg_digits", "short_answer", 3, [LIN, ELI], {"kind": "ncert_example"},
  "The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits of the number differ by 2, find the number. How many such numbers are there?",
  answer_steps=["Tens digit $x$, units digit $y$: $11(x + y) = 66$, so $x + y = 6$.", "$x - y = 2$ gives $x = 4, y = 2$; $y - x = 2$ gives $x = 2, y = 4$.", "The numbers are 42 and 24: two such numbers."], marking_scheme=MS3_SOLVE)

def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
mcq("mcq01", [CON], "The pair of equations $x + 2y + 5 = 0$ and $-3x - 6y + 1 = 0$ has:", ["no solution", "a unique solution", "exactly two solutions", "infinitely many solutions"], 0,
    "$\\dfrac{1}{-3} = \\dfrac{2}{-6} \\neq \\dfrac{5}{1}$: parallel lines, no solution.", "medium")
mcq("mcq02", [CON], "The value of $k$ for which $2x + 3y = 7$ and $4x + ky = 14$ have infinitely many solutions is:", ["$6$", "$3$", "$-6$", "$12$"], 0,
    "$\\dfrac{2}{4} = \\dfrac{3}{k} = \\dfrac{7}{14}$ gives $k = 6$.")
mcq("mcq03", [CON], "The value of $k$ for which $x + 2y = 3$ and $5x + ky + 7 = 0$ have no solution is:", ["$10$", "$5$", "$-10$", "$2$"], 0,
    "$\\dfrac{1}{5} = \\dfrac{2}{k}$ gives $k = 10$, and $\\dfrac{-3}{7} \\neq \\dfrac{1}{5}$, so there is no solution.", "medium")
mcq("mcq04", [SUB, ELI], "If $x = a$, $y = b$ is the solution of $x - y = 2$ and $x + y = 4$, then $a$ and $b$ are:", ["$3$ and $1$", "$1$ and $3$", "$2$ and $2$", "$4$ and $0$"], 0,
    "Adding: $2x = 6$, $x = 3$; then $y = 1$.")
mcq("mcq05", [CON, GR], "Graphically, the pair $6x - 3y + 10 = 0$ and $2x - y + 9 = 0$ represents two lines which are:", ["parallel", "intersecting at exactly one point", "coincident", "intersecting at exactly two points"], 0,
    "$\\dfrac{6}{2} = \\dfrac{-3}{-1} \\neq \\dfrac{10}{9}$.")
mcq("mcq06", [LIN], "A father's age is three times his son's age. After 10 years, he will be twice as old as his son. The present ages are:", ["$30$ and $10$", "$45$ and $15$", "$36$ and $12$", "$24$ and $8$"], 0,
    "$x = 3y$ and $x + 10 = 2(y + 10)$ give $y = 10$, $x = 30$.", "medium")
mcq("mcq07", [LIN], "The sum of two numbers is 35 and their difference is 13. The numbers are:", ["$24$ and $11$", "$23$ and $12$", "$25$ and $10$", "$22$ and $13$"], 0,
    "Adding: $2x = 48$, $x = 24$; $y = 11$.")
mcq("mcq08", [ELI], "If $2x + 3y = 12$ and $3x - 2y = 5$, then $x + y$ equals:", ["$5$", "$6$", "$7$", "$4$"], 0, "$x = 3$, $y = 2$, so $x + y = 5$.", "medium")
mcq("mcq09", [CON], "Which of the following pairs is consistent?", ["$2x + y - 6 = 0$ and $4x - 2y - 4 = 0$", "$x - y = 8$ and $3x - 3y = 16$", "$x + y = 5$ and $2x + 2y = 12$", "$2x - 2y - 2 = 0$ and $4x - 4y - 5 = 0$"], 0,
    "Only the first pair has $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$ ($\\dfrac{2}{4} \\neq \\dfrac{1}{-2}$); the others are parallel.", "medium")
mcq("mcq10", [CON], "The number of solutions of $3x - y = 3$ and $9x - 3y = 9$ is:", ["infinitely many", "one", "two", "zero"], 0, "All three ratios equal $\\dfrac{1}{3}$: coincident lines.")
mcq("mcq11", [CON], "The lines $2x - y = 5$ and $6x - 3y = c$ are coincident when $c$ equals:", ["$15$", "$5$", "$10$", "$-15$"], 0, "$\\dfrac{2}{6} = \\dfrac{-1}{-3} = \\dfrac{5}{c}$ gives $c = 15$.")
mcq("mcq12", [CON, GR], "If $\\dfrac{a_1}{a_2} \\neq \\dfrac{b_1}{b_2}$, the lines representing the pair:", ["intersect at exactly one point", "are parallel", "coincide", "do not exist"], 0, "Different slopes: the lines cross at one point.")
mcq("sqp3", [CON], "If the lines given by $3x + 2ky = 2$ and $2x + 5y + 1 = 0$ are not parallel, then $k$ has to be",
    ["$\\dfrac{15}{4}$", "$\\neq \\dfrac{15}{4}$", "any rational number", "any rational number having 4 as denominator"], 1,
    "Not parallel means $\\dfrac{3}{2} \\neq \\dfrac{2k}{5}$, so $k \\neq \\dfrac{15}{4}$.", "medium", source=SQP(3))

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [CON], "The pair $x + y = 4$ and $2x + 2y = 8$ has infinitely many solutions.", "If $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} = \\dfrac{c_1}{c_2}$, the lines coincide.", 0,
   "All ratios equal $\\dfrac{1}{2}$, so the lines coincide: exactly the reason.")
ar("ar2", [CON], "The pair $3x - 2y = 5$ and $6x - 4y = 9$ has no solution.", "The lines are parallel when $\\dfrac{a_1}{a_2} = \\dfrac{b_1}{b_2} \\neq \\dfrac{c_1}{c_2}$.", 0,
   "$\\dfrac{3}{6} = \\dfrac{-2}{-4} \\neq \\dfrac{5}{9}$: parallel lines, as the reason says.")
ar("ar3", [SUB], "The pair $x - y = 1$ and $x + y = 5$ has the unique solution $(3, 2)$.", "Any two lines in a plane always intersect.", 2,
   "A is true ($3 - 2 = 1$, $3 + 2 = 5$). R is false: parallel lines never meet.")
ar("ar4", [CON], "The pair $2x + 3y = 5$ and $4x + 6y = 10$ is inconsistent.", "Coincident lines have infinitely many common points.", 3,
   "A is false: all ratios equal $\\dfrac{1}{2}$, so the lines coincide and the pair is consistent. R is true.")
ar("ar5", [LIN], "If $(2, 1)$ is a solution of $3x + ky = 7$, then $k = 1$.", "A solution of an equation satisfies the equation.", 0,
   "$3 \\times 2 + k \\times 1 = 7$ gives $k = 1$, using the reason.")

q("vsa1", "very_short_answer", 2, [ELI], SHINE, "Solve: $x + y = 7$ and $3x - y = 1$.", "easy",
  answer_steps=["Adding: $4x = 8$, $x = 2$.", "Then $y = 7 - 2 = 5$."], marking_scheme=MS2_SOLVE)
q("vsa2", "very_short_answer", 2, [CON], SHINE, "Find whether the lines $4x + 6y = 7$ and $2x + 3y = 9$ intersect, are parallel or coincide.", "easy",
  answer_steps=["$\\dfrac{4}{2} = \\dfrac{6}{3} = 2$ but $\\dfrac{7}{9} \\neq 2$.", "The lines are parallel."], marking_scheme=MS2_RATIO)
q("sa1", "short_answer", 3, [CON], SHINE, "For what value of $k$ will the pair $kx + 3y = k - 3$ and $12x + ky = k$ have no solution?", "hard",
  answer_steps=["No solution needs $\\dfrac{k}{12} = \\dfrac{3}{k} \\neq \\dfrac{k - 3}{k}$.", "$\\dfrac{k}{12} = \\dfrac{3}{k}$ gives $k^{2} = 36$, so $k = \\pm 6$.",
                "$\\dfrac{3}{k} \\neq \\dfrac{k - 3}{k}$ needs $k \\neq 6$. Hence $k = -6$."], marking_scheme=["1 mark: condition", "1 mark: $k = \\pm 6$", "1 mark: rejecting $k = 6$"])
q("sa2", "short_answer", 3, [LIN, ELI], SHINE, "The sum of a two-digit number and the number obtained by reversing its digits is 121. If the digits differ by 3, find the number.",
  answer_steps=["Tens digit $x$, units digit $y$: $11(x + y) = 121$, so $x + y = 11$.", "$x - y = 3$ gives $x = 7, y = 4$; $y - x = 3$ gives $x = 4, y = 7$.", "The number is 74 or 47."], marking_scheme=MS3_SOLVE)
q("sa3", "short_answer", 3, [LIN, ELI], SHINE, "Places A and B are 100 km apart on a highway. One car starts from A and another from B at the same time. If they travel in the same direction, they meet in 5 hours. If they travel towards each other, they meet in 1 hour. Find the speeds of the two cars.",
  answer_steps=["Let the speeds be $x$ km/h and $y$ km/h ($x > y$). Same direction: $5x - 5y = 100$, so $x - y = 20$.", "Towards each other: $x + y = 100$.", "Adding: $x = 60$, $y = 40$: the speeds are 60 km/h and 40 km/h."], marking_scheme=MS3_SOLVE)
q("sa4", "short_answer", 3, [LIN, ELI], SHINE, "A part of monthly hostel charges is fixed and the remaining depends on the number of days one has taken food in the mess. When Amit takes food for 20 days he pays ₹1000, and when Bina takes food for 26 days she pays ₹1180. Find the fixed charges and the cost of food per day.",
  answer_steps=["Let the fixed charge be ₹$x$ and the cost per day ₹$y$: $x + 20y = 1000$ and $x + 26y = 1180$.", "Subtracting: $6y = 180$, $y = 30$.", "$x = 400$: fixed charges ₹400 and ₹30 per day."], marking_scheme=MS3_SOLVE)
q("la1", "long_answer", 5, [LIN, ELI], SHINE, "A shopkeeper sells a saree at 8% profit and a sweater at 10% discount, thereby getting a sum of ₹1008. If she had sold the saree at 10% profit and the sweater at 8% discount, she would have got ₹1028. Find the cost price of the saree and the list price (price before discount) of the sweater.", "hard",
  answer_steps=["Let the cost price of the saree be ₹$x$ and the list price of the sweater ₹$y$.", "$1.08x + 0.9y = 1008$, i.e. $108x + 90y = 100800$, i.e. $6x + 5y = 5600$.",
                "$1.1x + 0.92y = 1028$, i.e. $110x + 92y = 102800$, i.e. $55x + 46y = 51400$.", "Multiply the first by 46 and the second by 5: $276x + 230y = 257600$ and $275x + 230y = 257000$; subtracting, $x = 600$.",
                "Then $6 \\times 600 + 5y = 5600$, so $y = 400$: the saree costs ₹600 and the sweater is listed at ₹400."],
  marking_scheme=["1 mark: forming both equations", "1 mark: simplifying", "2 marks: elimination and $x = 600$", "1 mark: $y = 400$"])
q("la2", "long_answer", 5, [GR], SHINE, "Solve graphically: $2x + 3y = 12$ and $x - y = 1$. Also find the area of the triangle formed by these lines and the x-axis.", "medium",
  answer_steps=["$2x + 3y = 12$: points $(0, 4), (6, 0), (3, 2)$.", "$x - y = 1$: points $(1, 0), (0, -1), (3, 2)$.", "The lines meet at $(3, 2)$, so $x = 3$, $y = 2$.",
                "The triangle has vertices $(1, 0)$, $(6, 0)$ and $(3, 2)$: base $= 5$, height $= 2$.", "Area $= \\dfrac{1}{2} \\times 5 \\times 2 = 5$ square units."],
  marking_scheme=["1 mark: table for each line", "1 mark: graphs", "1 mark: solution $(3, 2)$", "1 mark: vertices", "1 mark: area"])
q("sqp31a", "short_answer", 3, [LIN, ELI], SQP("31(A)"), "The monthly incomes of Aryan and Babban are in the ratio 3 : 4 and their monthly expenditures are in the ratio 5 : 7. If each saves ₹15,000 per month, find their monthly incomes.",
  answer_steps=["Incomes $3x, 4x$; expenditures $5y, 7y$: $3x - 5y = 15000$ and $4x - 7y = 15000$.", "Multiply by 4 and 3: $12x - 20y = 60000$, $12x - 21y = 45000$; subtracting, $y = 15000$, then $x = 30000$.",
                "Monthly incomes: ₹90,000 and ₹1,20,000."], marking_scheme=MS3_SOLVE)
q("sqp31b", "short_answer", 3, [GR], SQP("31(B)"), "Solve the following system of equations graphically: $2x + y = 6$, $2x - y - 2 = 0$. Find the area of the triangle so formed by the two lines and the x-axis.",
  answer_steps=["$2x + y = 6$: points $(0, 6), (3, 0)$; $2x - y = 2$: points $(0, -2), (1, 0)$.", "The lines meet at $(2, 2)$, so $x = 2$, $y = 2$.", "Triangle with vertices $(1, 0), (3, 0), (2, 2)$: area $= \\dfrac{1}{2} \\times 2 \\times 2 = 2$ square units."],
  marking_scheme=["1 mark: graphs of both lines", "1 mark: solution $(2, 2)$", "1 mark: area"])
q("cb1", "case_based", 4, [LIN, ELI], SHINE,
  "At a school canteen, Meena pays ₹55 for 2 samosas and 3 cups of tea, and Rohan pays ₹65 for 4 samosas and 1 cup of tea.\n\n(i) Form the pair of linear equations. (1)\n\n(ii) Find the cost of one samosa. (1)\n\n(iii) Find the cost of 5 samosas and 2 cups of tea. OR Is the pair consistent? Justify. (2)",
  answer_steps=["(i) Samosa ₹$x$, tea ₹$y$: $2x + 3y = 55$, $4x + y = 65$", "(ii) $y = 65 - 4x$, so $2x + 195 - 12x = 55$, $x = 14$: a samosa costs ₹14 (and tea ₹9).",
                "(iii) $5 \\times 14 + 2 \\times 9 = 88$: ₹88. OR $\\dfrac{2}{4} \\neq \\dfrac{3}{1}$, so the lines intersect: consistent with a unique solution."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [LIN, ELI], SHINE,
  "For a school play, 3 adult tickets and 2 child tickets cost ₹800, while 2 adult tickets and 3 child tickets cost ₹700.\n\n(i) Form the pair of linear equations. (1)\n\n(ii) Find the price of an adult ticket. (1)\n\n(iii) How much will a family of 2 adults and 2 children pay? OR Solve the pair using the elimination method. (2)",
  answer_steps=["(i) Adult ₹$x$, child ₹$y$: $3x + 2y = 800$, $2x + 3y = 700$", "(ii) Multiply by 3 and 2: $9x + 6y = 2400$, $4x + 6y = 1400$; subtracting, $x = 200$.",
                "(iii) $y = 100$, so $2 \\times 200 + 2 \\times 100 = 600$: ₹600. OR elimination as in (ii) gives $x = 200$, $y = 100$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch03.q.sqp"):
        return
    shift = sum(map(ord, item["id"])) % len(opts)
    correct = opts[item["correct_index"]]
    item["options"] = opts[shift:] + opts[:shift]
    item["correct_index"] = item["options"].index(correct)
for it in Q: spread(it)
for sec in sections:
    for blk in sec["blocks"]: spread(blk)
print("answer positions:", Counter(it["correct_index"] for it in Q if it["type"] == "mcq"))
os.makedirs(os.path.join(ROOT, PATH), exist_ok=True)
for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": CH_ID, "questions": Q})]:
    with open(os.path.join(ROOT, PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
print(f"blocks={sum(len(s['blocks']) for s in sections)} questions={len(Q)} ncert_exercise_items={sum(1 for it in Q if it['source']['kind'] == 'ncert_exercise')}")
