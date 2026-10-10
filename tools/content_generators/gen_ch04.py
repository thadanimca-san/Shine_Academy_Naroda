"""CBSE Class 10 Maths Ch 4: Quadratic Equations.
Every root, discriminant, k-value and word-problem answer is checked with sympy."""
import json, os, sys
from collections import Counter
from sympy import symbols, solve, expand, sqrt, Rational as R, simplify, Poly, nsimplify, discriminant

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch04"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch04_quadratic_equations"
x, k, t = symbols("x k t")

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

def same_set(a, b):
    a = sorted(simplify(v) for v in a); b = sorted(simplify(nsimplify(v)) for v in b)
    return len(a) == len(b) and all(simplify(p - q) == 0 for p, q in zip(a, b))

def roots(expr, expected, msg):
    got = solve(expr, x)
    check(same_set(got, set(expected)), f"{msg}: {got} vs {expected}")

def same_up_to_sign(e, mine, msg):
    d = expand(e)
    check(expand(d - mine) == 0 or expand(d + mine) == 0, f"{msg}: {d} vs {mine}")

def D(expr, var=x):
    p = Poly(expand(expr), var); a, b, c = [p.coeff_monomial(var**i) for i in (2, 1, 0)]
    return expand(b * b - 4 * a * c)

# ---------------------------------------------------------------- verification
EX41Q1 = [  # part, latex, lhs, rhs, simplified latex, simplified expr, is quadratic
 ("i", "(x + 1)^{2} = 2(x - 3)", (x + 1)**2, 2*(x - 3), "x^{2} + 7 = 0", x**2 + 7, True),
 ("ii", "x^{2} - 2x = (-2)(3 - x)", x**2 - 2*x, -2*(3 - x), "x^{2} - 4x + 6 = 0", x**2 - 4*x + 6, True),
 ("iii", "(x - 2)(x + 1) = (x - 1)(x + 3)", (x - 2)*(x + 1), (x - 1)*(x + 3), "-3x + 1 = 0", -3*x + 1, False),
 ("iv", "(x - 3)(2x + 1) = x(x + 5)", (x - 3)*(2*x + 1), x*(x + 5), "x^{2} - 10x - 3 = 0", x**2 - 10*x - 3, True),
 ("v", "(2x - 1)(x - 3) = (x + 5)(x - 1)", (2*x - 1)*(x - 3), (x + 5)*(x - 1), "x^{2} - 11x + 8 = 0", x**2 - 11*x + 8, True),
 ("vi", "x^{2} + 3x + 1 = (x - 2)^{2}", x**2 + 3*x + 1, (x - 2)**2, "7x - 3 = 0", 7*x - 3, False),
 ("vii", "(x + 2)^{3} = 2x(x^{2} - 1)", (x + 2)**3, 2*x*(x**2 - 1), "x^{3} - 6x^{2} - 14x - 8 = 0", x**3 - 6*x**2 - 14*x - 8, False),
 ("viii", "x^{3} - 4x^{2} - x + 1 = (x - 2)^{3}", x**3 - 4*x**2 - x + 1, (x - 2)**3, "2x^{2} - 13x + 9 = 0", 2*x**2 - 13*x + 9, True),
]
for p, _, l, r, _, s, quad in EX41Q1:
    same_up_to_sign(l - r, s, f"4.1 Q1 {p}"); check((Poly(s, x).degree() == 2) == quad, f"4.1 Q1 {p} degree")
# SQP Q6: only (D) is not quadratic
for l, r, quad in [((x + 2)**2, 2*(x + 3), True), (x**2 + 3*x, -(1 - 3*x)**2, True), (x**3 - x**2 + 2*x + 1, (x + 1)**3, True), ((x + 2)*(x + 1), x**2 + 2*x + 3, False)]:
    check((Poly(expand(l - r), x).degree() == 2) == quad, "sqp6")
# Ex 4.1 Q2 (forming) and their answers
roots(x*(2*x + 1) - 528, [16, R(-33, 2)], "4.1 Q2 i"); roots(x*(x + 1) - 306, [17, -18], "4.1 Q2 ii")
roots((x + 3)*(x + 29) - 360, [7, -39], "4.1 Q2 iii"); same_up_to_sign((x + 3)*(x + 29) - 360, x**2 + 32*x - 273, "4.1 Q2 iii form")
check(simplify(480/(x - 8) - 480/x - 3 - (-3*(x**2 - 8*x - 1280))/(x*(x - 8))) == 0, "4.1 Q2 iv form"); roots(x**2 - 8*x - 1280, [40, -32], "4.1 Q2 iv")
# Ex 4.2 Q1
EX42Q1 = [("i", "x^{2} - 3x - 10 = 0", x**2 - 3*x - 10, None, "x^{2} - 5x + 2x - 10 = (x - 5)(x + 2) = 0", (x - 5)*(x + 2), "5", "-2", [5, -2]),
          ("ii", "2x^{2} + x - 6 = 0", 2*x**2 + x - 6, None, "2x^{2} + 4x - 3x - 6 = (2x - 3)(x + 2) = 0", (2*x - 3)*(x + 2), "\\dfrac{3}{2}", "-2", [R(3, 2), -2]),
          ("iii", "\\sqrt{2}x^{2} + 7x + 5\\sqrt{2} = 0", sqrt(2)*x**2 + 7*x + 5*sqrt(2), None, "\\sqrt{2}x^{2} + 5x + 2x + 5\\sqrt{2} = (\\sqrt{2}x + 5)(x + \\sqrt{2}) = 0",
           (sqrt(2)*x + 5)*(x + sqrt(2)), "-\\dfrac{5}{\\sqrt{2}}", "-\\sqrt{2}", [-5/sqrt(2), -sqrt(2)]),
          ("iv", "2x^{2} - x + \\dfrac{1}{8} = 0", 2*x**2 - x + R(1, 8), ("8", "16x^{2} - 8x + 1 = 0"), "16x^{2} - 4x - 4x + 1 = (4x - 1)^{2} = 0", (4*x - 1)**2, "\\dfrac{1}{4}", "\\dfrac{1}{4}", [R(1, 4)]),
          ("v", "100x^{2} - 20x + 1 = 0", 100*x**2 - 20*x + 1, None, "100x^{2} - 10x - 10x + 1 = (10x - 1)^{2} = 0", (10*x - 1)**2, "\\dfrac{1}{10}", "\\dfrac{1}{10}", [R(1, 10)])]
for p, _, e, mult, _, f, _, _, r in EX42Q1:
    scale = int(mult[0]) if mult else 1
    check(expand(scale * e - f) == 0, f"4.2 Q1 {p} factorisation"); roots(e, r, f"4.2 Q1 {p}")
roots((x - 5)*(40 - x) - 124, [36, 9], "4.2 Q2 i"); same_up_to_sign((x - 5)*(40 - x) - 124, x**2 - 45*x + 324, "4.2 Q2 i form")
roots(x*(55 - x) - 750, [25, 30], "4.2 Q2 ii")
roots(x*(27 - x) - 182, [13, 14], "4.2 Q3"); roots(x**2 + (x + 1)**2 - 365, [13, -14], "4.2 Q4")
roots(x**2 + (x - 7)**2 - 169, [12, -5], "4.2 Q5"); roots(x*(2*x + 3) - 90, [6, R(-15, 2)], "4.2 Q6"); check(2 * 6 + 3 == 15, "4.2 Q6 cost")
# Ex 4.3
check(D(2*x**2 - 3*x + 5) == -31, "4.3 Q1 i")
check(D(3*x**2 - 4*sqrt(3)*x + 4) == 0, "4.3 Q1 ii"); roots(3*x**2 - 4*sqrt(3)*x + 4, [2/sqrt(3)], "4.3 Q1 ii roots")
check(D(2*x**2 - 6*x + 3) == 12, "4.3 Q1 iii"); roots(2*x**2 - 6*x + 3, [(3 + sqrt(3))/2, (3 - sqrt(3))/2], "4.3 Q1 iii roots")
check(same_set(solve(D(2*x**2 + k*x + 3), k), [2*sqrt(6), -2*sqrt(6)]), "4.3 Q2 i")
check(same_set(solve(D(k*x*(x - 2) + 6), k), [0, 6]), "4.3 Q2 ii")
roots(2*x**2 - 800, [20, -20], "4.3 Q3")
same_up_to_sign((x - 4)*(16 - x) - 48, x**2 - 20*x + 112, "4.3 Q4 form"); check(D(x**2 - 20*x + 112) == -48, "4.3 Q4")
same_up_to_sign(x*(40 - x) - 400, x**2 - 40*x + 400, "4.3 Q5 form"); check(D(x**2 - 40*x + 400) == 0, "4.3 Q5"); roots(x**2 - 40*x + 400, [20], "4.3 Q5 root")
# Examples
same_up_to_sign((x - 2)**2 + 1 - (2*x - 3), x**2 - 6*x + 8, "eg check i"); same_up_to_sign(x*(x + 1) + 8 - (x + 2)*(x - 2), x + 12, "eg check ii")
roots(2*x**2 - 5*x + 3, [1, R(3, 2)], "eg 2x2-5x+3"); check(expand((2*x - 3)*(x - 1)) == 2*x**2 - 5*x + 3, "eg 2x2-5x+3 factor")
roots(6*x**2 - x - 2, [R(2, 3), R(-1, 2)], "eg 6x2"); check(expand((3*x - 2)*(2*x + 1)) == 6*x**2 - x - 2, "eg 6x2 factor")
check(expand((sqrt(3)*x - sqrt(2))**2 - (3*x**2 - 2*sqrt(6)*x + 2)) == 0, "eg root6 factor"); roots(3*x**2 - 2*sqrt(6)*x + 2, [sqrt(2)/sqrt(3)], "eg root6")
roots(2*x**2 + x - 300, [12, R(-25, 2)], "eg hall"); check(expand((2*x + 25)*(x - 12)) == 2*x**2 + x - 300, "eg hall factor")
same_up_to_sign(x**2 + (x + 7)**2 - 169, 2*(x**2 + 7*x - 60), "eg pole form"); check(D(x**2 + 7*x - 60) == 289, "eg pole D"); roots(x**2 + 7*x - 60, [5, -12], "eg pole")
check(D(2*x**2 - 4*x + 3) == -8, "eg nature"); check(D(3*x**2 - 2*x + R(1, 3)) == 0, "eg equal"); roots(3*x**2 - 2*x + R(1, 3), [R(1, 3)], "eg equal root")
roots(x**2 - 3*x - 10, [5, -2], "check x2-3x-10")
# Lesson checks and MCQs
check(Poly(expand(x*(x + 3) - 10), x).degree() == 2 and Poly(expand(x**2 + 2*x - x**2 + 5), x).degree() == 1, "s2.check")
roots(x**2 - 4*x + 1, [2 + sqrt(3), 2 - sqrt(3)], "s4.check"); check(D(x**2 - 4*x + 1) == 12 and (16 + 4) == 20, "s4.check distractor")
check(D(4*x**2 - 12*x + 9) == 0, "s5.check1"); check(same_set(solve(D(2*x**2 + k*x + 2), k), [4, -4]), "s5.check2")
check(Poly(expand((x - 2)**2 + 1 - 2*x + 3), x).degree() == 2 and Poly(expand(x**2 + 3*x + 1 - (x - 2)**2), x).degree() == 1, "mcq01")
check(Poly(expand((x + 2)**3 - 2*x*(x**2 - 1)), x).degree() == 3, "mcq01 cubic")
roots(x**2 - 5*x + 6, [2, 3], "mcq02"); roots(x**2 - 5*x - 6, [6, -1], "mcq02 distractor")
check(D(2*x**2 - 4*x + 3) == -8, "mcq03"); check(D(x**2 + 4*x + 5) == -4, "mcq04")
check(same_set(solve(D(x**2 - k*x + 9), k), [6, -6]), "mcq05"); check(solve((2**2 + k*2 - 6), k) == [1], "mcq06")
roots(x*(x + 1) - 132, [11, -12], "mcq07"); roots(x**2 - 9*x, [0, 9], "mcq08")
check(D(2*x**2 - 3*x + 1) == 1 and D(x**2 + x + 1) == -3 and D(4*x**2 - 4*x + 1) == 0 and D(x**2 + 2*x + 3) == -8, "mcq09")
roots(x*(x + 2) - 24, [4, -6], "mcq12")
check(D(x**2 + 2*x + 5) == -16, "ar1"); check(2**2 - 3*2 + 2 == 0, "ar2"); check(Poly(expand((x - 1)**2 - x**2 - 1), x).degree() == 1, "ar3")
check(D(9*x**2 - 6*x + 1) == 0, "ar4"); roots(x**2 - 4, [2, -2], "ar5"); check(D(x**2 + 1) < 0, "ar5 R false")
check(D(3*x**2 - 5*x + 2) == 1, "vsa1"); check(solve(3*R(1, 4) + 2*k*R(-1, 2) - 3, k) == [R(-9, 4)], "vsa2")
roots(sqrt(3)*x**2 - 2*sqrt(2)*x - 2*sqrt(3), [sqrt(6), -sqrt(6)/3], "sa1"); check(D(sqrt(3)*x**2 - 2*sqrt(2)*x - 2*sqrt(3)) == 32, "sa1 D")
check(same_set(solve(D((k + 4)*x**2 + (k + 1)*x + 1), k), [5, -3]), "sa2")
roots((x - 5)*(x + 8) - 30, [7, -10], "sa3"); roots(x**2 + (x + 5)**2 - 625, [15, -20], "sa4")
check(simplify(63/x + 72/(x + 6) - 3 + 3*(x**2 - 39*x - 126)/(x*(x + 6))) == 0, "sqp32 form"); roots(x**2 - 39*x - 126, [42, -3], "sqp32")
roots(x**2 + (x + 30)**2 - (x + 60)**2, [90, -30], "la diagonal"); same_up_to_sign(x**2 + (x + 30)**2 - (x + 60)**2, x**2 - 60*x - 2700, "la diagonal form")
check(simplify(24/(18 - x) - 24/(18 + x) - 1 - (x**2 + 48*x - 324)/((18 - x)*(18 + x))) == 0, "la boat form"); roots(x**2 + 48*x - 324, [6, -54], "la boat")
roots(x*(x + 4) - 96, [8, -12], "cb1"); check(D(x**2 + 4*x - 96) == 400 and 2 * (8 + 12) == 40, "cb1 iii")
check(set(solve(-5*t**2 + 20*t - 15, t)) == {1, 3}, "cb2 ii"); check(D(t**2 - 4*t + 5, t) == -4, "cb2 iii"); check(set(solve(-5*t**2 + 20*t, t)) == {0, 4}, "cb2 iii or")

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch04.{id_}", "type": type_, **kw}
def graph(id_, title, poly, label, zeroes, xr):
    return {"id": f"ch04.{id_}", "type": "function_graph", "title": title, "polynomial": poly, "label": label, "zeroes": zeroes, "x_range": xr}

sections = [
 {"id": "s1", "title": "When the unknown is squared", "blocks": [
  b("s1.hook", "hook", title="The prayer hall puzzle",
    body="A charity trust wants to build a prayer hall with a carpet area of 300 square metres. The length must be one metre more than twice the breadth. What should the breadth be?\n\n"
         "Try guessing: a breadth of 10 m gives $10 \\times 21 = 210$, too small. A breadth of 15 m gives $15 \\times 31 = 465$, too big. "
         "Writing breadth $= x$ gives $x(2x + 1) = 300$, i.e. $2x^{2} + x - 300 = 0$. The unknown is **squared**. In this chapter you will learn to solve such **quadratic equations** without guessing."),
  b("s1.inspiration", "inspiration", title="The formula that India gave the world", person="Brahmagupta and Sridharacharya", years="7th–10th century CE",
    body="In 628 CE, Brahmagupta wrote the *Brahmasphutasiddhanta*. He gave rules for calculating with zero and with negative numbers, which he called 'debts', and a rule for solving equations with a squared unknown.\n\n"
         "Around three centuries later, Sridharacharya gave a method that solves **every** quadratic equation. "
         "Today we write it as the quadratic formula, and in India it is often called **Sridharacharya's formula**. You will use it in this chapter.",
    quote="A good method works every time. Learn the method, and no question can scare you.",
    future="Quadratic equations describe the path of a cricket ball, the shape of a satellite dish, the stopping distance of a car and the price at which a business earns the most profit."),
  b("s1.socratic", "socratic_question",
    question="A square plot has an area of 49 square metres. If its side is $x$ metres, which equation describes it?",
    options=["$x^{2} = 49$", "$4x = 49$", "$2x = 49$"], correct_index=0,
    explanation="Area of a square $=$ side $\\times$ side, so $x^{2} = 49$. Both $7$ and $-7$ satisfy it, but a length cannot be negative, so the side is 7 m. A quadratic equation can have two roots, and in word problems we keep only the ones that make sense."),
 ]},
 {"id": "s2", "title": "Quadratic equations", "blocks": [
  b("s2.reveal", "theory", title="What is a quadratic equation?", revision=True,
    body="A **quadratic equation** in the variable $x$ is an equation of the form\n\n$$ax^{2} + bx + c = 0, \\qquad a \\neq 0$$\n\n"
         "where $a, b, c$ are real numbers. This is called the **standard form**.\n\n"
         "A real number $\\alpha$ is a **root** of the equation if $a\\alpha^{2} + b\\alpha + c = 0$. The roots of $ax^{2} + bx + c = 0$ are the same as the **zeroes** of the polynomial $ax^{2} + bx + c$. "
         "A quadratic equation has **at most two** roots."),
  b("s2.eg1", "worked_example", title="NCERT example: is it quadratic?",
    problem="Check whether the following are quadratic equations: (i) $(x - 2)^{2} + 1 = 2x - 3$ (ii) $x(x + 1) + 8 = (x + 2)(x - 2)$",
    steps=["(i) LHS $= x^{2} - 4x + 5$. So $x^{2} - 4x + 5 = 2x - 3$, i.e. $x^{2} - 6x + 8 = 0$. This is of the form $ax^{2} + bx + c = 0$: **quadratic**.",
           "(ii) LHS $= x^{2} + x + 8$ and RHS $= x^{2} - 4$. So $x^{2} + x + 8 = x^{2} - 4$, i.e. $x + 12 = 0$. The $x^{2}$ terms cancel: **not quadratic**."],
    answer="(i) is a quadratic equation; (ii) is not. Always simplify before deciding."),
  b("s2.eg2", "worked_example", title="NCERT example: forming the equation",
    problem="John and Jivanti together have 45 marbles. Both of them lost 5 marbles each, and the product of the number of marbles they now have is 124. Write a quadratic equation to find how many marbles they had to start with.",
    steps=["Let John have $x$ marbles. Then Jivanti has $45 - x$.", "After losing 5 each: $x - 5$ and $40 - x$.",
           "$(x - 5)(40 - x) = 124$, i.e. $-x^{2} + 45x - 200 = 124$."],
    answer="$x^{2} - 45x + 324 = 0$"),
  b("s2.check", "knowledge_check", question="Which of these is a quadratic equation?",
    options=["$x(x + 3) = 10$", "$x^{2} + 2x = x^{2} - 5$", "$x^{3} - x = 0$", "$2x + 3 = 7$"], correct_index=0,
    explanation="$x(x + 3) = 10$ becomes $x^{2} + 3x - 10 = 0$: degree 2. In $x^{2} + 2x = x^{2} - 5$ the squares cancel, leaving $2x + 5 = 0$."),
 ]},
 {"id": "s3", "title": "Solving by factorisation", "blocks": [
  b("s3.socratic", "socratic_question", question="If $(x - 2)(x - 5) = 0$, what can you say about $x$?",
    options=["$x = 2$ or $x = 5$", "$x = 2$ and $x = 5$ at the same time", "$x = -2$ or $x = -5$"], correct_index=0,
    explanation="If a product of two numbers is zero, at least one of them is zero. So $x - 2 = 0$ or $x - 5 = 0$, giving $x = 2$ or $x = 5$. Both are roots."),
  b("s3.reveal", "theory", title="Steps of the factorisation method", revision=True,
    body="1. Write the equation in standard form $ax^{2} + bx + c = 0$.\n"
         "2. **Split the middle term**: find two numbers whose **product** is $ac$ and whose **sum** is $b$.\n"
         "3. Factorise into two linear factors.\n"
         "4. Put each factor equal to zero and solve.\n\n"
         "Example: $2x^{2} - 5x + 3 = 0$. Here $ac = 6$ and $b = -5$; the numbers are $-2$ and $-3$. "
         "$2x^{2} - 2x - 3x + 3 = 2x(x - 1) - 3(x - 1) = (2x - 3)(x - 1)$. So $x = \\dfrac{3}{2}$ or $x = 1$."),
  graph("s3.g1", "The roots are where the graph meets the x-axis", [2, -5, 3], "y = 2x^{2} - 5x + 3", [1.0, 1.5], [-1, 3]),
  b("s3.eg1", "worked_example", title="NCERT example",
    problem="Find the roots of $6x^{2} - x - 2 = 0$.",
    steps=["$ac = -12$, $b = -1$: the numbers are $-4$ and $3$.", "$6x^{2} - 4x + 3x - 2 = 2x(3x - 2) + 1(3x - 2) = (3x - 2)(2x + 1)$",
           "$3x - 2 = 0$ or $2x + 1 = 0$"],
    answer="$x = \\dfrac{2}{3}$ or $x = -\\dfrac{1}{2}$"),
  b("s3.eg2", "worked_example", title="NCERT example: equal roots",
    problem="Find the roots of $3x^{2} - 2\\sqrt{6}x + 2 = 0$.",
    steps=["$3x^{2} - \\sqrt{6}x - \\sqrt{6}x + 2 = \\sqrt{3}x(\\sqrt{3}x - \\sqrt{2}) - \\sqrt{2}(\\sqrt{3}x - \\sqrt{2})$", "$= (\\sqrt{3}x - \\sqrt{2})(\\sqrt{3}x - \\sqrt{2})$",
           "Both factors give $x = \\sqrt{\\dfrac{2}{3}}$."],
    answer="$x = \\sqrt{\\dfrac{2}{3}}$, twice (equal roots)"),
  b("s3.eg3", "worked_example", title="NCERT example: the prayer hall",
    problem="Solve the prayer hall problem: $2x^{2} + x - 300 = 0$, where $x$ m is the breadth.",
    steps=["$ac = -600$, $b = 1$: the numbers are $25$ and $-24$.", "$2x^{2} - 24x + 25x - 300 = 2x(x - 12) + 25(x - 12) = (x - 12)(2x + 25)$",
           "$x = 12$ or $x = -\\dfrac{25}{2}$. A breadth cannot be negative, so $x = 12$."],
    answer="Breadth 12 m, length $2 \\times 12 + 1 = 25$ m"),
  b("s3.check", "knowledge_check", question="The roots of $x^{2} - 3x - 10 = 0$ are:",
    options=["$5$ and $-2$", "$-5$ and $2$", "$10$ and $-1$", "$2$ and $5$"], correct_index=0,
    explanation="$x^{2} - 5x + 2x - 10 = (x - 5)(x + 2)$, so $x = 5$ or $x = -2$."),
  b("s3.tip", "teacher_tip", title="Finding the two numbers",
    body="Ask students to list the factor pairs of $ac$ in a column and look for the pair with the right sum. Signs first: if $ac$ is negative, the two numbers have opposite signs. "
         "Then show the graph on the panel: the roots are exactly where the curve crosses the x-axis, which links back to zeroes of polynomials in Chapter 2."),
 ]},
 {"id": "s4", "title": "The quadratic formula", "blocks": [
  b("s4.reveal", "theory", title="Sridharacharya's formula", revision=True,
    body="The roots of $ax^{2} + bx + c = 0$ (with $a \\neq 0$) are\n\n$$x = \\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$$\n\n"
         "provided $b^{2} - 4ac \\geq 0$. This works for **every** quadratic equation, even when factorising is hard.\n\n"
         "Steps: write the equation in standard form, read off $a$, $b$, $c$ (with their signs), find $b^{2} - 4ac$ first, then substitute."),
  b("s4.eg1", "worked_example", title="Using the formula",
    problem="Solve $2x^{2} - 6x + 3 = 0$ using the quadratic formula.",
    steps=["$a = 2$, $b = -6$, $c = 3$.", "$b^{2} - 4ac = 36 - 24 = 12$", "$x = \\dfrac{6 \\pm \\sqrt{12}}{4} = \\dfrac{6 \\pm 2\\sqrt{3}}{4}$"],
    answer="$x = \\dfrac{3 + \\sqrt{3}}{2}$ or $x = \\dfrac{3 - \\sqrt{3}}{2}$"),
  b("s4.eg2", "worked_example", title="NCERT example: the pole in the park",
    problem="A pole has to be erected at a point on the boundary of a circular park of diameter 13 m, so that the difference of its distances from two diametrically opposite fixed gates A and B is 7 m. Is it possible? If so, how far from the two gates should the pole be erected?",
    steps=["Let the pole be $x$ m from gate B. Then it is $(x + 7)$ m from gate A.", "The angle in a semicircle is $90^\\circ$, so by Pythagoras: $x^{2} + (x + 7)^{2} = 13^{2}$, i.e. $x^{2} + 7x - 60 = 0$.",
           "$b^{2} - 4ac = 49 + 240 = 289 > 0$, so real roots exist: $x = \\dfrac{-7 \\pm 17}{2}$, i.e. $x = 5$ or $x = -12$.", "A distance cannot be negative, so $x = 5$."],
    answer="Yes: 5 m from gate B and 12 m from gate A."),
  b("s4.check", "knowledge_check", question="Using the quadratic formula, the roots of $x^{2} - 4x + 1 = 0$ are:",
    options=["$2 \\pm \\sqrt{3}$", "$4 \\pm \\sqrt{3}$", "$-2 \\pm \\sqrt{3}$", "$2 \\pm \\sqrt{5}$"], correct_index=0,
    explanation="$b^{2} - 4ac = 16 - 4 = 12$, so $x = \\dfrac{4 \\pm \\sqrt{12}}{2} = 2 \\pm \\sqrt{3}$."),
 ]},
 {"id": "s5", "title": "Nature of roots", "blocks": [
  b("s5.socratic", "socratic_question", question="The graph of $y = ax^{2} + bx + c$ is a U-shaped curve (a parabola). In how many points can it meet the x-axis?",
    options=["0, 1 or 2 points", "Always exactly 2 points", "Any number of points"], correct_index=0,
    explanation="A parabola can cross the x-axis twice, just touch it once, or stay completely above or below it. So a quadratic equation has two, one (repeated) or no real roots. The number $b^{2} - 4ac$ tells us which."),
  graph("s5.g1", "D > 0: two distinct real roots", [1, -2, -3], "y = x^{2} - 2x - 3", [-1.0, 3.0], [-3, 5]),
  graph("s5.g2", "D = 0: two equal real roots", [1, -4, 4], "y = x^{2} - 4x + 4", [2.0], [-1, 5]),
  graph("s5.g3", "D < 0: no real roots", [1, -2, 3], "y = x^{2} - 2x + 3", [], [-2, 4]),
  b("s5.reveal", "theory", title="The discriminant", revision=True,
    body="For $ax^{2} + bx + c = 0$, the number $D = b^{2} - 4ac$ is called the **discriminant**: it *discriminates* between the kinds of roots.\n\n"
         "- If $b^{2} - 4ac > 0$: **two distinct real roots**.\n"
         "- If $b^{2} - 4ac = 0$: **two equal real roots**, each $-\\dfrac{b}{2a}$.\n"
         "- If $b^{2} - 4ac < 0$: **no real roots**."),
  b("s5.eg1", "worked_example", title="NCERT example",
    problem="Find the discriminant of $2x^{2} - 4x + 3 = 0$ and hence find the nature of its roots.",
    steps=["$a = 2$, $b = -4$, $c = 3$.", "$b^{2} - 4ac = 16 - 24 = -8 < 0$"], answer="The equation has no real roots."),
  b("s5.eg2", "worked_example", title="NCERT example: equal roots",
    problem="Find the nature of the roots of $3x^{2} - 2x + \\dfrac{1}{3} = 0$. If real roots exist, find them.",
    steps=["$b^{2} - 4ac = 4 - 4 \\times 3 \\times \\dfrac{1}{3} = 0$: two equal real roots.", "Each root is $-\\dfrac{b}{2a} = \\dfrac{2}{6}$."],
    answer="$x = \\dfrac{1}{3}$, twice"),
  b("s5.eg3", "worked_example", title="Finding k for equal roots",
    problem="Find the value of $k$ for which $kx(x - 2) + 6 = 0$ has two equal roots.",
    steps=["Standard form: $kx^{2} - 2kx + 6 = 0$, so $a = k$, $b = -2k$, $c = 6$.", "Equal roots: $b^{2} - 4ac = 4k^{2} - 24k = 0$, i.e. $4k(k - 6) = 0$.",
           "$k = 0$ or $k = 6$. But $k = 0$ makes $a = 0$ and the equation is no longer quadratic."],
    answer="$k = 6$"),
  b("s5.memory", "memory_trick", title="Read the discriminant like a signal", revision=True,
    body="- $D > 0$: **green**, two different roots.\n- $D = 0$: **yellow**, one root repeated: the curve just touches the x-axis.\n- $D < 0$: **red**, no real roots: the curve never meets the x-axis."),
  b("s5.check1", "knowledge_check", question="The roots of $4x^{2} - 12x + 9 = 0$ are:",
    options=["real and equal", "real and distinct", "not real", "more than two in number"], correct_index=0,
    explanation="$b^{2} - 4ac = 144 - 144 = 0$, so the roots are real and equal (each $\\dfrac{3}{2}$)."),
  b("s5.check2", "knowledge_check", question="For what values of $k$ does $2x^{2} + kx + 2 = 0$ have equal roots?",
    options=["$\\pm 4$", "$\\pm 2$", "$4$ only", "$\\pm 16$"], correct_index=0,
    explanation="Equal roots: $k^{2} - 4 \\times 2 \\times 2 = 0$, so $k^{2} = 16$ and $k = \\pm 4$."),
  b("s5.mistakes", "common_mistakes", title="Common mistakes",
    body="- Dividing both sides by $x$, as in $x^{2} = 9x$ giving only $x = 9$. This loses the root $x = 0$: write $x(x - 9) = 0$ instead.\n"
         "- Taking the sign of $b$ wrongly in the formula: for $x^{2} - 4x + 1 = 0$, $b = -4$, so $-b = 4$.\n"
         "- Forgetting to put the equation in standard form before reading $a$, $b$, $c$.\n"
         "- In word problems, not rejecting a negative length, age or speed.\n"
         "- In 'find $k$' questions, keeping a value that makes $a = 0$."),
 ]},
 {"id": "s6", "title": "Think, connect, master", "blocks": [
  b("s6.reflection", "reflection", title="Explain it in your own words",
    body="Using the three graphs in this chapter, explain to a friend why a quadratic equation can never have three roots."),
  b("s6.connection", "connection", title="Where this leads",
    body="- **Chapter 5, Arithmetic Progressions:** finding how many terms give a certain sum leads to a quadratic equation.\n"
         "- **Physics (Class 11):** the equations of motion, like $s = ut + \\dfrac{1}{2}at^{2}$, are quadratic in time.\n"
         "- **Economics and Commerce:** profit often depends on price through a quadratic, and the best price is found from it."),
  b("s6.mastery", "mastery", title="Mastery challenge",
    body="The diagonal of a rectangular field is 60 m more than its shorter side. If the longer side is 30 m more than the shorter side, find the sides of the field.\n\n"
         "**Answer:** With shorter side $x$: $x^{2} + (x + 30)^{2} = (x + 60)^{2}$, so $x^{2} - 60x - 2700 = 0$ and $(x - 90)(x + 30) = 0$. "
         "So $x = 90$: the sides are 90 m and 120 m."),
  b("s6.summary", "summary", title="Chapter summary",
    body="- A quadratic equation has the form $ax^{2} + bx + c = 0$, $a \\neq 0$.\n"
         "- Its roots are the zeroes of $ax^{2} + bx + c$; there are at most two.\n"
         "- **Factorisation:** split the middle term, factorise and set each factor to zero.\n"
         "- **Quadratic formula:** $x = \\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$, when $b^{2} - 4ac \\geq 0$.\n"
         "- **Discriminant** $D = b^{2} - 4ac$: $D > 0$ two distinct real roots, $D = 0$ two equal real roots, $D < 0$ no real roots."),
  b("s6.examtips", "exam_tips", title="Board exam tips",
    body="- Always reduce the equation to standard form first and write $a$, $b$, $c$ clearly.\n"
         "- In word problems, write 'Let ... be $x$', form the equation, solve, and **state why** you reject a negative root.\n"
         "- In 'nature of roots' questions, show the value of $b^{2} - 4ac$ and write the conclusion in words.\n"
         "- In 'find $k$' questions, write the condition (like $b^{2} - 4ac = 0$) before solving."),
  b("s6.flash1", "flashcard", front="What is the quadratic formula?", back="$x = \\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$, valid when $b^{2} - 4ac \\geq 0$."),
  b("s6.flash2", "flashcard", front="What is the discriminant of $ax^{2} + bx + c = 0$?", back="$D = b^{2} - 4ac$. It tells the nature of the roots."),
  b("s6.flash3", "flashcard", front="When does a quadratic equation have equal roots?", back="When $b^{2} - 4ac = 0$. Each root is $-\\dfrac{b}{2a}$."),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Quadratic Equations",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 4,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: standard form, solution by factorisation and by the quadratic formula (real roots only), discriminant and nature of roots, situational problems. Completing the square and equations reducible to quadratic form are not in the board syllabus and are not included.",
  "concepts": ["quadratic_equation", "factorisation_method", "quadratic_formula", "discriminant", "quadratic_word_problems"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
QE, FAC, FOR, DIS, WORD = "quadratic_equation", "factorisation_method", "quadratic_formula", "discriminant", "quadratic_word_problems"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch04.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
MS2_CHECK = ["1 mark: simplifying to standard form", "1 mark: conclusion"]
MS2_FORM = ["1 mark: choosing the variable", "1 mark: correct quadratic equation"]
MS2_FACT = ["1 mark: splitting the middle term", "1 mark: both roots"]
MS3_WORD = ["1 mark: forming the equation", "1 mark: solving", "1 mark: answer with the invalid root rejected"]
MS3_NATURE = ["1 mark: discriminant", "1 mark: nature of roots", "1 mark: roots (if real)"]
MS2_K = ["1 mark: condition $b^{2} - 4ac = 0$", "1 mark: value(s) of $k$"]

# Exercise 4.1
for p, latex, _, _, simp, s, quad in EX41Q1:
    deg3 = Poly(s, x).degree() == 3
    verdict = ("It is of the form $ax^{2} + bx + c = 0$ with $a \\neq 0$, so it is a quadratic equation." if quad else
               "The highest power of $x$ is 3, so it is not a quadratic equation." if deg3 else
               "The $x^{2}$ terms cancel, so it is not a quadratic equation.")
    q(f"ex4_1.q1.{p}", "very_short_answer", 2, [QE], ex("4.1", 1, p), f"Check whether ${latex}$ is a quadratic equation.", "easy",
      answer_steps=[f"Simplifying gives ${simp}$.", verdict], marking_scheme=MS2_CHECK)
EX41Q2 = [
 ("i", "The area of a rectangular plot is 528 m². The length of the plot (in metres) is one more than twice its breadth. We need to find the length and breadth of the plot.",
  ["Let the breadth be $x$ m; then the length is $(2x + 1)$ m.", "$x(2x + 1) = 528$, i.e. $2x^{2} + x - 528 = 0$."]),
 ("ii", "The product of two consecutive positive integers is 306. We need to find the integers.",
  ["Let the integers be $x$ and $x + 1$.", "$x(x + 1) = 306$, i.e. $x^{2} + x - 306 = 0$."]),
 ("iii", "Rohan's mother is 26 years older than him. The product of their ages (in years) 3 years from now will be 360. We would like to find Rohan's present age.",
  ["Let Rohan's present age be $x$ years; his mother's is $x + 26$.", "$(x + 3)(x + 29) = 360$, i.e. $x^{2} + 32x - 273 = 0$."]),
 ("iv", "A train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. We need to find the speed of the train.",
  ["Let the speed be $x$ km/h. Time taken $= \\dfrac{480}{x}$ hours.", "$\\dfrac{480}{x - 8} - \\dfrac{480}{x} = 3$, which simplifies to $x^{2} - 8x - 1280 = 0$."]),
]
for p, text, steps in EX41Q2:
    q(f"ex4_1.q2.{p}", "very_short_answer", 2, [QE, WORD], ex("4.1", 2, p), "Represent the following situation in the form of a quadratic equation: " + text,
      answer_steps=steps, marking_scheme=MS2_FORM)
# Exercise 4.2
for p, latex, _, mult, split, _, r1, r2, _ in EX42Q1:
    steps = ([f"Multiply by {mult[0]}: ${mult[1]}$."] if mult else []) + [f"Splitting the middle term: ${split}$"]
    steps.append(f"So the roots are ${r1}$ and ${r2}$ (equal roots)." if r1 == r2 else f"So the roots are ${r1}$ and ${r2}$.")
    q(f"ex4_2.q1.{p}", "very_short_answer", 2, [FAC], ex("4.2", 1, p), f"Find the roots of the quadratic equation ${latex}$ by factorisation.",
      "easy" if p in ("i", "ii") else "medium", answer_steps=steps, marking_scheme=MS2_FACT)
WORD42 = [
 ("q2.i", "Solve: John and Jivanti together have 45 marbles. Both of them lost 5 marbles each, and the product of the number of marbles they now have is 124. Find how many marbles they had to start with.",
  ["Let John have $x$ marbles; Jivanti has $45 - x$. $(x - 5)(40 - x) = 124$ gives $x^{2} - 45x + 324 = 0$.", "$(x - 36)(x - 9) = 0$, so $x = 36$ or $x = 9$.", "John had 36 and Jivanti 9, or John had 9 and Jivanti 36."]),
 ("q2.ii", "Solve: A cottage industry produces a certain number of toys in a day. The cost of production of each toy (in rupees) was found to be 55 minus the number of toys produced in a day. On a particular day, the total cost of production was ₹750. Find the number of toys produced on that day.",
  ["Let $x$ toys be produced. Cost of each toy $= 55 - x$, so $x(55 - x) = 750$, i.e. $x^{2} - 55x + 750 = 0$.", "$(x - 25)(x - 30) = 0$, so $x = 25$ or $x = 30$.", "25 or 30 toys were produced (both fit the conditions)."]),
 ("q3", "Find two numbers whose sum is 27 and product is 182.",
  ["Let the numbers be $x$ and $27 - x$: $x(27 - x) = 182$, i.e. $x^{2} - 27x + 182 = 0$.", "$(x - 13)(x - 14) = 0$, so $x = 13$ or $x = 14$.", "The numbers are 13 and 14."]),
 ("q4", "Find two consecutive positive integers, sum of whose squares is 365.",
  ["Let the integers be $x$ and $x + 1$: $x^{2} + (x + 1)^{2} = 365$, i.e. $x^{2} + x - 182 = 0$.", "$(x + 14)(x - 13) = 0$, so $x = 13$ ($x = -14$ is not positive).", "The integers are 13 and 14."]),
 ("q5", "The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.",
  ["Let the base be $x$ cm; the altitude is $(x - 7)$ cm. By Pythagoras: $x^{2} + (x - 7)^{2} = 169$, i.e. $x^{2} - 7x - 60 = 0$.", "$(x - 12)(x + 5) = 0$, so $x = 12$ ($x = -5$ is rejected).", "The base is 12 cm and the altitude is 5 cm."]),
 ("q6", "A cottage industry produces a certain number of pottery articles in a day. It was observed on a particular day that the cost of production of each article (in rupees) was 3 more than twice the number of articles produced on that day. If the total cost of production on that day was ₹90, find the number of articles produced and the cost of each article.",
  ["Let $x$ articles be produced; each costs ₹$(2x + 3)$. $x(2x + 3) = 90$, i.e. $2x^{2} + 3x - 90 = 0$.", "$(x - 6)(2x + 15) = 0$, so $x = 6$ ($x = -\\dfrac{15}{2}$ is rejected).", "6 articles were produced, each costing ₹15."]),
]
for p, text, steps in WORD42:
    num = int(p.split(".")[0][1:]); part = p.split(".")[1] if "." in p else None
    q(f"ex4_2.{p}", "short_answer", 3, [WORD, FAC], ex("4.2", num, part), text, answer_steps=steps, marking_scheme=MS3_WORD)
# Exercise 4.3
for p, latex, steps in [
 ("i", "2x^{2} - 3x + 5 = 0", ["$a = 2$, $b = -3$, $c = 5$: $b^{2} - 4ac = 9 - 40 = -31$.", "Since $b^{2} - 4ac < 0$, the equation has no real roots."]),
 ("ii", "3x^{2} - 4\\sqrt{3}x + 4 = 0", ["$b^{2} - 4ac = 48 - 48 = 0$: two equal real roots.", "Each root is $-\\dfrac{b}{2a} = \\dfrac{4\\sqrt{3}}{6} = \\dfrac{2}{\\sqrt{3}}$."]),
 ("iii", "2x^{2} - 6x + 3 = 0", ["$b^{2} - 4ac = 36 - 24 = 12 > 0$: two distinct real roots.", "$x = \\dfrac{6 \\pm \\sqrt{12}}{4} = \\dfrac{3 \\pm \\sqrt{3}}{2}$"]),
]:
    q(f"ex4_3.q1.{p}", "short_answer", 3, [DIS, FOR], ex("4.3", 1, p), f"Find the nature of the roots of the quadratic equation ${latex}$. If the real roots exist, find them.",
      "easy" if p == "i" else "medium", answer_steps=steps, marking_scheme=MS3_NATURE)
q("ex4_3.q2.i", "very_short_answer", 2, [DIS], ex("4.3", 2, "i"), "Find the values of $k$ for which the quadratic equation $2x^{2} + kx + 3 = 0$ has two equal roots.",
  answer_steps=["Equal roots: $k^{2} - 4 \\times 2 \\times 3 = 0$, so $k^{2} = 24$.", "$k = \\pm 2\\sqrt{6}$"], marking_scheme=MS2_K)
q("ex4_3.q2.ii", "very_short_answer", 2, [DIS], ex("4.3", 2, "ii"), "Find the values of $k$ for which the quadratic equation $kx(x - 2) + 6 = 0$ has two equal roots.", "hard",
  answer_steps=["$kx^{2} - 2kx + 6 = 0$. Equal roots: $4k^{2} - 24k = 0$, i.e. $4k(k - 6) = 0$.", "$k = 0$ is rejected (the equation would not be quadratic), so $k = 6$."], marking_scheme=MS2_K)
q("ex4_3.q3", "short_answer", 3, [WORD, DIS], ex("4.3", 3), "Is it possible to design a rectangular mango grove whose length is twice its breadth, and the area is 800 m²? If so, find its length and breadth.",
  answer_steps=["Let the breadth be $x$ m; the length is $2x$ m. $2x^{2} = 800$, i.e. $x^{2} - 400 = 0$.", "$b^{2} - 4ac = 1600 > 0$, so real roots exist: $x = \\pm 20$, and $x = 20$ (breadth is positive).", "Yes: breadth 20 m and length 40 m."],
  marking_scheme=MS3_WORD)
q("ex4_3.q4", "short_answer", 3, [WORD, DIS], ex("4.3", 4), "Is the following situation possible? If so, determine their present ages. The sum of the ages of two friends is 20 years. Four years ago, the product of their ages in years was 48.", "hard",
  answer_steps=["Let the ages be $x$ and $20 - x$. Four years ago: $(x - 4)(16 - x) = 48$, i.e. $x^{2} - 20x + 112 = 0$.", "$b^{2} - 4ac = 400 - 448 = -48 < 0$", "No real roots, so the situation is not possible."],
  marking_scheme=MS3_WORD)
q("ex4_3.q5", "short_answer", 3, [WORD, DIS], ex("4.3", 5), "Is it possible to design a rectangular park of perimeter 80 m and area 400 m²? If so, find its length and breadth.",
  answer_steps=["Let the length be $x$ m; the breadth is $(40 - x)$ m. $x(40 - x) = 400$, i.e. $x^{2} - 40x + 400 = 0$.", "$b^{2} - 4ac = 1600 - 1600 = 0$: equal roots, $x = 20$.", "Yes: length 20 m and breadth 20 m (the park is a square)."],
  marking_scheme=MS3_WORD)
# NCERT examples
q("eg_factor", "very_short_answer", 2, [FAC], {"kind": "ncert_example"}, "Find the roots of the quadratic equation $6x^{2} - x - 2 = 0$.", "easy",
  answer_steps=["Splitting the middle term: $6x^{2} - 4x + 3x - 2 = (3x - 2)(2x + 1) = 0$", "So the roots are $\\dfrac{2}{3}$ and $-\\dfrac{1}{2}$."], marking_scheme=MS2_FACT)
q("eg_equal", "very_short_answer", 2, [FAC], {"kind": "ncert_example"}, "Find the roots of the quadratic equation $3x^{2} - 2\\sqrt{6}x + 2 = 0$.",
  answer_steps=["Splitting the middle term: $3x^{2} - \\sqrt{6}x - \\sqrt{6}x + 2 = (\\sqrt{3}x - \\sqrt{2})^{2} = 0$", "So the roots are $\\sqrt{\\dfrac{2}{3}}$ and $\\sqrt{\\dfrac{2}{3}}$ (equal roots)."], marking_scheme=MS2_FACT)
q("eg_hall", "short_answer", 3, [WORD, FAC], {"kind": "ncert_example"},
  "A charity trust decides to build a prayer hall having a carpet area of 300 square metres with the length one metre more than twice its breadth. What should be the length and breadth of the hall?",
  answer_steps=["Let the breadth be $x$ m; the length is $(2x + 1)$ m. $x(2x + 1) = 300$, i.e. $2x^{2} + x - 300 = 0$.", "$(x - 12)(2x + 25) = 0$, so $x = 12$ ($x = -\\dfrac{25}{2}$ is rejected).", "Breadth 12 m and length 25 m."],
  marking_scheme=MS3_WORD)
q("eg_pole", "long_answer", 5, [WORD, FOR, DIS], {"kind": "ncert_example"},
  "A pole has to be erected at a point on the boundary of a circular park of diameter 13 metres in such a way that the differences of its distances from two diametrically opposite fixed gates A and B on the boundary is 7 metres. Is it possible to do so? If yes, at what distances from the two gates should the pole be erected?", "hard",
  answer_steps=["Let the pole P be $x$ m from gate B; then $AP = (x + 7)$ m, and $AB = 13$ m.", "$\\angle APB = 90^\\circ$ (angle in a semicircle), so $x^{2} + (x + 7)^{2} = 169$, i.e. $x^{2} + 7x - 60 = 0$.",
                "$b^{2} - 4ac = 49 + 240 = 289 > 0$, so the situation is possible.", "$x = \\dfrac{-7 \\pm 17}{2}$, so $x = 5$ or $x = -12$; reject $-12$.", "The pole is 5 m from gate B and 12 m from gate A."],
  marking_scheme=["1 mark: assigning $x$ and $x + 7$", "1 mark: using the right angle to form the equation", "1 mark: discriminant", "1 mark: roots", "1 mark: distances from both gates"])
q("eg_nature", "very_short_answer", 2, [DIS], {"kind": "ncert_example"}, "Find the discriminant of the quadratic equation $2x^{2} - 4x + 3 = 0$, and hence find the nature of its roots.", "easy",
  answer_steps=["$b^{2} - 4ac = 16 - 24 = -8$", "Since $b^{2} - 4ac < 0$, the equation has no real roots."], marking_scheme=["1 mark: discriminant", "1 mark: nature of roots"])
q("eg_equal_d", "very_short_answer", 2, [DIS], {"kind": "ncert_example"}, "Find the nature of the roots of $3x^{2} - 2x + \\dfrac{1}{3} = 0$. If they are real, find them.",
  answer_steps=["$b^{2} - 4ac = 4 - 4 = 0$: two equal real roots.", "Each root is $-\\dfrac{b}{2a} = \\dfrac{2}{6} = \\dfrac{1}{3}$."], marking_scheme=["1 mark: discriminant", "1 mark: roots"])

def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
mcq("mcq01", [QE], "Which of the following is a quadratic equation?",
    ["$(x - 2)^{2} + 1 = 2x - 3$", "$x(x + 1) + 8 = (x + 2)(x - 2)$", "$x^{2} + 3x + 1 = (x - 2)^{2}$", "$(x + 2)^{3} = 2x(x^{2} - 1)$"], 0,
    "$(x - 2)^{2} + 1 = 2x - 3$ simplifies to $x^{2} - 6x + 8 = 0$. In the next two the squares cancel, and the last has degree 3.", "medium")
mcq("mcq02", [FAC], "The roots of $x^{2} - 5x + 6 = 0$ are:", ["$2$ and $3$", "$-2$ and $-3$", "$6$ and $-1$", "$1$ and $6$"], 0, "$(x - 2)(x - 3) = 0$, so $x = 2$ or $x = 3$.")
mcq("mcq03", [DIS], "The discriminant of $2x^{2} - 4x + 3 = 0$ is:", ["$-8$", "$8$", "$40$", "$4$"], 0, "$b^{2} - 4ac = 16 - 24 = -8$.")
mcq("mcq04", [DIS], "The equation $x^{2} + 4x + 5 = 0$ has:", ["no real roots", "two distinct real roots", "two equal real roots", "more than two real roots"], 0,
    "$b^{2} - 4ac = 16 - 20 = -4 < 0$: no real roots.")
mcq("mcq05", [DIS], "The values of $k$ for which $x^{2} - kx + 9 = 0$ has equal roots are:", ["$\\pm 6$", "$6$ only", "$\\pm 3$", "$\\pm 9$"], 0,
    "Equal roots: $k^{2} - 36 = 0$, so $k = \\pm 6$.", "medium")
mcq("mcq06", [QE], "If $x = 2$ is a root of $x^{2} + kx - 6 = 0$, then $k$ is:", ["$1$", "$-1$", "$2$", "$3$"], 0, "$4 + 2k - 6 = 0$, so $k = 1$.")
mcq("mcq07", [WORD], "Two consecutive positive integers whose product is 132 are:", ["$11$ and $12$", "$12$ and $13$", "$10$ and $11$", "$13$ and $14$"], 0,
    "$x(x + 1) = 132$ gives $x^{2} + x - 132 = 0$, $(x + 12)(x - 11) = 0$, so $x = 11$.")
mcq("mcq08", [FAC], "The roots of $x^{2} = 9x$ are:", ["$0$ and $9$", "$9$ only", "$3$ and $-3$", "$0$ only"], 0, "$x^{2} - 9x = 0$, so $x(x - 9) = 0$: $x = 0$ or $x = 9$.", "medium")
mcq("mcq09", [DIS], "Which of these equations has two distinct real roots?", ["$2x^{2} - 3x + 1 = 0$", "$x^{2} + x + 1 = 0$", "$4x^{2} - 4x + 1 = 0$", "$x^{2} + 2x + 3 = 0$"], 0,
    "For $2x^{2} - 3x + 1 = 0$, $b^{2} - 4ac = 9 - 8 = 1 > 0$. The others give $-3$, $0$ and $-8$.", "medium")
mcq("mcq10", [FOR], "The roots of $ax^{2} + bx + c = 0$ (with $b^{2} - 4ac \\geq 0$) are given by:",
    ["$\\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$", "$\\dfrac{b \\pm \\sqrt{b^{2} - 4ac}}{2a}$", "$\\dfrac{-b \\pm \\sqrt{b^{2} + 4ac}}{2a}$", "$-b \\pm \\dfrac{\\sqrt{b^{2} - 4ac}}{2a}$"], 0,
    "Sridharacharya's formula: $x = \\dfrac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$.")
mcq("mcq11", [QE], "The maximum number of roots a quadratic equation can have is:", ["$2$", "$1$", "$3$", "infinitely many"], 0, "A polynomial of degree 2 has at most 2 zeroes, so the equation has at most 2 roots.")
mcq("mcq12", [WORD], "The area of a rectangle is 24 cm² and its length is 2 cm more than its breadth. Its breadth is:", ["$4$ cm", "$6$ cm", "$3$ cm", "$2$ cm"], 0,
    "$x(x + 2) = 24$ gives $(x + 6)(x - 4) = 0$, so $x = 4$.")
mcq("sqp6", [QE], "Which one of the following is not a quadratic equation?",
    ["$(x + 2)^{2} = 2(x + 3)$", "$x^{2} + 3x = (-1)(1 - 3x)^{2}$", "$x^{3} - x^{2} + 2x + 1 = (x + 1)^{3}$", "$(x + 2)(x + 1) = x^{2} + 2x + 3$"], 3,
    "$(x + 2)(x + 1) = x^{2} + 3x + 2$, so the equation becomes $x - 1 = 0$, which is linear. The others reduce to degree 2.", "medium", source=SQP(6))

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [DIS], "The equation $x^{2} + 2x + 5 = 0$ has no real roots.", "If $b^{2} - 4ac < 0$, a quadratic equation has no real roots.", 0,
   "$b^{2} - 4ac = 4 - 20 = -16 < 0$, which is exactly the reason.")
ar("ar2", [QE], "$x = 2$ is a root of $x^{2} - 3x + 2 = 0$.", "A quadratic equation has at most two roots.", 1,
   "A is true: $4 - 6 + 2 = 0$. R is true, but it does not explain why 2 is a root.")
ar("ar3", [QE], "$(x - 1)^{2} = x^{2} + 1$ is a quadratic equation.", "An equation of the form $ax^{2} + bx + c = 0$ with $a \\neq 0$ is a quadratic equation.", 3,
   "A is false: it simplifies to $-2x = 0$, which is linear. R is true.")
ar("ar4", [DIS], "The equation $9x^{2} - 6x + 1 = 0$ has two equal roots.", "A quadratic equation has equal roots when $b^{2} - 4ac = 0$.", 0,
   "$b^{2} - 4ac = 36 - 36 = 0$, which is exactly the reason.")
ar("ar5", [FAC], "The roots of $x^{2} - 4 = 0$ are $2$ and $-2$.", "Every quadratic equation has two distinct real roots.", 2,
   "A is true. R is false: for example, $x^{2} + 1 = 0$ has no real roots.")

q("vsa1", "very_short_answer", 2, [DIS], SHINE, "Find the discriminant of $3x^{2} - 5x + 2 = 0$ and hence the nature of its roots.", "easy",
  answer_steps=["$b^{2} - 4ac = 25 - 24 = 1$", "Since $b^{2} - 4ac > 0$, the equation has two distinct real roots."], marking_scheme=["1 mark: discriminant", "1 mark: nature of roots"])
q("vsa2", "very_short_answer", 2, [QE], SHINE, "If $x = -\\dfrac{1}{2}$ is a root of $3x^{2} + 2kx - 3 = 0$, find the value of $k$.",
  answer_steps=["Substitute: $3 \\times \\dfrac{1}{4} + 2k \\times \\left(-\\dfrac{1}{2}\\right) - 3 = 0$, i.e. $\\dfrac{3}{4} - k - 3 = 0$.", "$k = -\\dfrac{9}{4}$"],
  marking_scheme=["1 mark: substitution", "1 mark: value of $k$"])
q("sa1", "short_answer", 3, [FOR], SHINE, "Solve $\\sqrt{3}x^{2} - 2\\sqrt{2}x - 2\\sqrt{3} = 0$ using the quadratic formula.", "hard",
  answer_steps=["$a = \\sqrt{3}$, $b = -2\\sqrt{2}$, $c = -2\\sqrt{3}$: $b^{2} - 4ac = 8 + 24 = 32$.", "$x = \\dfrac{2\\sqrt{2} \\pm 4\\sqrt{2}}{2\\sqrt{3}}$",
                "$x = \\dfrac{6\\sqrt{2}}{2\\sqrt{3}} = \\sqrt{6}$ or $x = \\dfrac{-2\\sqrt{2}}{2\\sqrt{3}} = -\\dfrac{\\sqrt{6}}{3}$"],
  marking_scheme=["1 mark: discriminant", "1 mark: substitution in the formula", "1 mark: both roots"])
q("sa2", "short_answer", 3, [DIS], SHINE, "Find the values of $k$ for which $(k + 4)x^{2} + (k + 1)x + 1 = 0$ has equal roots.", "hard",
  answer_steps=["Equal roots: $(k + 1)^{2} - 4(k + 4) = 0$.", "$k^{2} - 2k - 15 = 0$, i.e. $(k - 5)(k + 3) = 0$.", "$k = 5$ or $k = -3$ (both keep $k + 4 \\neq 0$)."],
  marking_scheme=["1 mark: condition", "1 mark: simplifying", "1 mark: both values of $k$"])
q("sa3", "short_answer", 3, [WORD, FAC], SHINE, "The product of Ramu's age (in years) five years ago and his age eight years from now is 30. Find his present age.",
  answer_steps=["Let his present age be $x$: $(x - 5)(x + 8) = 30$, i.e. $x^{2} + 3x - 70 = 0$.", "$(x + 10)(x - 7) = 0$, so $x = 7$ or $x = -10$.", "Age cannot be negative: Ramu is 7 years old."],
  marking_scheme=MS3_WORD)
q("sa4", "short_answer", 3, [WORD, FAC], SHINE, "The hypotenuse of a right triangle is 25 cm. The difference between the lengths of the other two sides is 5 cm. Find the lengths of these sides.",
  answer_steps=["Let the shorter side be $x$ cm; the other is $(x + 5)$ cm. $x^{2} + (x + 5)^{2} = 625$, i.e. $x^{2} + 5x - 300 = 0$.", "$(x + 20)(x - 15) = 0$, so $x = 15$ ($x = -20$ is rejected).", "The sides are 15 cm and 20 cm."],
  marking_scheme=MS3_WORD)
q("sqp32", "long_answer", 5, [WORD, FAC], SQP(32),
  "A train travels at a certain average speed for a distance of 63 km and then travels a distance of 72 km at an average speed of 6 km/h more than its original speed. If it takes 3 hours to complete the total journey, what is its original average speed?", "hard",
  answer_steps=["Let the original speed be $x$ km/h. Time for 63 km $= \\dfrac{63}{x}$ hours; time for 72 km $= \\dfrac{72}{x + 6}$ hours.", "$\\dfrac{63}{x} + \\dfrac{72}{x + 6} = 3$",
                "$63(x + 6) + 72x = 3x(x + 6)$, i.e. $3x^{2} - 117x - 378 = 0$, i.e. $x^{2} - 39x - 126 = 0$.", "$(x - 42)(x + 3) = 0$, so $x = 42$ or $x = -3$.", "Speed cannot be negative: the original average speed is 42 km/h."],
  marking_scheme=["1 mark: both time expressions", "1 mark: equation", "1 mark: quadratic in standard form", "1 mark: factorisation", "1 mark: answer with $-3$ rejected"])
q("la1", "long_answer", 5, [WORD, FAC], SHINE, "The diagonal of a rectangular field is 60 m more than the shorter side. If the longer side is 30 m more than the shorter side, find the sides of the field.", "hard",
  answer_steps=["Let the shorter side be $x$ m. Longer side $= (x + 30)$ m, diagonal $= (x + 60)$ m.", "By Pythagoras: $x^{2} + (x + 30)^{2} = (x + 60)^{2}$.", "$x^{2} + 60x + 900 = 120x + 3600$, i.e. $x^{2} - 60x - 2700 = 0$.",
                "$(x - 90)(x + 30) = 0$, so $x = 90$ ($x = -30$ is rejected).", "The sides are 90 m and 120 m."],
  marking_scheme=["1 mark: expressions for the sides", "1 mark: Pythagoras equation", "1 mark: standard form", "1 mark: factorisation", "1 mark: answer"])
q("la2", "long_answer", 5, [WORD, FAC], SHINE, "A motorboat whose speed in still water is 18 km/h takes 1 hour more to go 24 km upstream than to return downstream to the same spot. Find the speed of the stream.", "hard",
  answer_steps=["Let the speed of the stream be $x$ km/h. Upstream speed $= 18 - x$, downstream speed $= 18 + x$.", "$\\dfrac{24}{18 - x} - \\dfrac{24}{18 + x} = 1$",
                "$24(18 + x) - 24(18 - x) = (18 - x)(18 + x)$, i.e. $48x = 324 - x^{2}$, i.e. $x^{2} + 48x - 324 = 0$.", "$(x + 54)(x - 6) = 0$, so $x = 6$ or $x = -54$.", "Speed cannot be negative: the stream flows at 6 km/h."],
  marking_scheme=["1 mark: upstream and downstream speeds", "1 mark: equation", "1 mark: standard form", "1 mark: factorisation", "1 mark: answer"])
q("cb1", "case_based", 4, [WORD, FAC, DIS], SHINE,
  "A school is designing a rectangular garden whose length is 4 m more than its breadth. The area of the garden is to be 96 m².\n\n(i) Taking the breadth as $x$ m, form the quadratic equation. (1)\n\n(ii) Find the breadth of the garden. (1)\n\n(iii) Find the perimeter of the garden. OR Find the discriminant of the equation formed in (i). (2)",
  answer_steps=["(i) $x(x + 4) = 96$, i.e. $x^{2} + 4x - 96 = 0$", "(ii) $(x + 12)(x - 8) = 0$, so the breadth is 8 m ($x = -12$ is rejected).",
                "(iii) Length $= 12$ m, perimeter $= 2(8 + 12) = 40$ m. OR $b^{2} - 4ac = 16 + 384 = 400$."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [WORD, DIS], SHINE,
  "In a cricket match, a ball is hit upwards. Its height (in metres) after $t$ seconds is $h = 20t - 5t^{2}$.\n\n(i) Write the quadratic equation for the time when the ball is 15 m high. (1)\n\n(ii) At what times is the ball 15 m high? (1)\n\n(iii) Can the ball reach a height of 25 m? Justify. OR After how many seconds does the ball come back to the ground? (2)",
  answer_steps=["(i) $20t - 5t^{2} = 15$, i.e. $t^{2} - 4t + 3 = 0$", "(ii) $(t - 1)(t - 3) = 0$: at $t = 1$ s (going up) and $t = 3$ s (coming down).",
                "(iii) $20t - 5t^{2} = 25$ gives $t^{2} - 4t + 5 = 0$, with $b^{2} - 4ac = 16 - 20 = -4 < 0$: no real roots, so the ball cannot reach 25 m. OR $20t - 5t^{2} = 0$ gives $t = 0$ or $t = 4$: it lands after 4 seconds."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch04.q.sqp"):
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
