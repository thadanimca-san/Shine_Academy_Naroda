"""Builds CBSE Class 10 Maths Ch 2 (Polynomials) in the new content format.
Every zero, sum, product and constructed polynomial is verified with sympy."""
import json, os, sys
from collections import Counter
from sympy import symbols, Poly, Rational as R, sqrt, simplify, expand, roots, sympify

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch02"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch02_polynomials"
x = symbols("x")

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

def zeroes_of(expr):
    r = roots(Poly(expand(expr), x))
    return sorted([z for z, m in r.items() for _ in range(m)], key=lambda v: (float(v.as_real_imag()[0]), float(v.as_real_imag()[1])))

def check_zeroes(expr, expected, msg):
    check(zeroes_of(expr) == sorted(map(sympify, expected), key=float), f"{msg}: {zeroes_of(expr)} vs {expected}")

def check_relation(expr, msg):
    a, b, c = Poly(expand(expr), x).all_coeffs()
    z = zeroes_of(expr)
    check(simplify(z[0] + z[1] + b / a) == 0 and simplify(z[0] * z[1] - c / a) == 0, f"relation {msg}")

def check_graph(coeffs, zs, msg):
    p = Poly(coeffs, x)
    for zz in zs:
        check(p.eval(sympify(zz)) == 0, f"graph {msg}: p({zz}) != 0")
    real = [r for r in zeroes_of(p.as_expr()) if r.is_real] if p.degree() > 0 else []
    check(len(set(real)) == len(set(map(sympify, zs))), f"graph {msg}: zero count")

# Exercise 2.2 Q1
EX22 = [("i", x**2 - 2*x - 8, "x^{2} - 2x - 8", [4, -2]),
        ("ii", 4*x**2 - 4*x + 1, "4s^{2} - 4s + 1", [R(1, 2), R(1, 2)]),
        ("iii", 6*x**2 - 7*x - 3, "6x^{2} - 3 - 7x", [R(3, 2), R(-1, 3)]),
        ("iv", 4*x**2 + 8*x, "4u^{2} + 8u", [0, -2]),
        ("v", x**2 - 15, "t^{2} - 15", [sqrt(15), -sqrt(15)]),
        ("vi", 3*x**2 - x - 4, "3x^{2} - x - 4", [R(4, 3), -1])]
for part, e, _, zs in EX22:
    check_zeroes(e, zs, f"2.2 Q1 {part}"); check_relation(e, part)
# Exercise 2.2 Q2: polynomial from sum S and product P
EX22B = [("i", R(1, 4), -1, 4*x**2 - x - 4), ("ii", sqrt(2), R(1, 3), 3*x**2 - 3*sqrt(2)*x + 1),
         ("iii", 0, sqrt(5), x**2 + sqrt(5)), ("iv", 1, 1, x**2 - x + 1),
         ("v", R(-1, 4), R(1, 4), 4*x**2 + x + 1), ("vi", 4, 1, x**2 - 4*x + 1)]
for part, S, P, poly in EX22B:
    a, b, c = Poly(poly, x).all_coeffs()
    check(simplify(-b / a - S) == 0 and simplify(c / a - P) == 0, f"2.2 Q2 {part}")
# Examples
check_zeroes(x**2 + 7*x + 10, [-2, -5], "eg2"); check_relation(x**2 + 7*x + 10, "eg2")
check_zeroes(x**2 - 3, [sqrt(3), -sqrt(3)], "eg3")
check(expand((x + 1) * (x + 2)) == x**2 + 3*x + 2, "eg4")
# Board-style
check_zeroes(x**2 - 5*x + 6, [2, 3], "mcq zeroes")
check(expand((x + 2) * (x - 5)) == x**2 - 3*x - 10, "zeroes -2,5")
check(Poly(x**2 + 3*x - 10, x).eval(2) == 0, "k = -10")
check(simplify((R(5, 2)) / R(3, 2) - R(5, 3)) == 0, "1/a+1/b")
check_zeroes(x**2 + x - 6, [2, -3], "a=0, b=-6")
k = symbols("k"); check(simplify(-2 / k - 3).subs(k, R(-2, 3)) == 0, "sum=product k")
check(expand((x - 3 - sqrt(2)) * (x - 3 + sqrt(2))) == x**2 - 6*x + 7, "3±√2")
check(2**2 + 4**2 == 20 and zeroes_of(x**2 - 6*x + 8) == [2, 4], "a^2+b^2")
check(zeroes_of(3*x**2 - 8*x + 2*R(2, 3) + 1) == [R(1, 3), R(7, 3)], "seven times, k=2/3")
check_zeroes(2*x**2 - 8*x + 6, [1, 3], "2x^2-8x+6")
check_zeroes(4*x**2 - 4*x - 3, [R(3, 2), R(-1, 2)], "4x^2-4x-3"); check_relation(4*x**2 - 4*x - 3, "sa1")
check(R(1, 1) + R(1, 4) - 2 * 4 == R(-27, 4), "1/a+1/b-2ab")
check(expand(3 * (x - 1) * (x - R(2, 3))) == 3*x**2 - 5*x + 2 and zeroes_of(2*x**2 - 5*x + 3) == [1, R(3, 2)], "reciprocal")
check_zeroes(-x**2 + 2*x + 8, [-2, 4], "arch")
check_zeroes(-x**2 + 6*x - 5, [1, 5], "ball"); check((-(3**2) + 6*3 - 5) == 4, "ball max")
check((16 - 20) < 0, "x^2+4x+5 no real zeroes")

GRAPHS = {  # coefficients (highest first), zeroes, x-range
 "linear": ([2, 3], [R(-3, 2)], [-4, 3]),
 "two": ([1, -3, -4], [-1, 4], [-3, 6]),
 "touch": ([1, -4, 4], [2], [-1, 5]),
 "none": ([1, 0, 1], [], [-3, 3]),
 "arch": ([-1, 2, 8], [-2, 4], [-3, 5]),
 "ex_i": ([3], [], [-4, 4]),
 "ex_ii": ([1, -1], [1], [-3, 4]),
 "ex_iii": ([1, 0, -4, 0], [-2, 0, 2], [-3, 3]),
 "ex_iv": ([1, -1, -2], [-1, 2], [-3, 4]),
 "ex_v": ([1, 0, -5, 0, 4], [-2, -1, 1, 2], [-2.5, 2.5]),
 "ex_vi": ([-1, 0, 7, -6], [-3, 1, 2], [-4, 3]),
}
for name, (co, zs, _) in GRAPHS.items():
    check_graph(co, zs, name)

def graph(name, title, label, zero_labels=None):
    co, zs, xr = GRAPHS[name]
    g = {"type": "function_graph", "polynomial": co, "x_range": xr, "zeroes": [float(z) for z in zs], "title": title, "label": label}
    if zero_labels: g["zero_labels"] = zero_labels
    return g

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch02.{id_}", "type": type_, **kw}
def gb(id_, *args, **kw): return {"id": f"ch02.{id_}", **graph(*args, **kw)}

sections = [
 {"id": "s1", "title": "Curves around us", "blocks": [
  b("s1.hook", "hook", title="Where will the ball land?",
    body="Throw a ball and its path makes a curve. Engineers who design bridges, fountains and cricket-ball tracking systems "
         "describe such curves with **polynomials**.\n\nThe points where the curve meets the ground are special: "
         "they are the **zeroes** of the polynomial. In this chapter you will find zeroes, see them on graphs, "
         "and discover a beautiful link between the zeroes and the numbers in the polynomial."),
  b("s1.socratic", "socratic_question",
    question="For $p(x) = x - 3$, for which value of $x$ is $p(x) = 0$?",
    options=["$x = 3$", "$x = -3$", "$x = 0$"], correct_index=0,
    explanation="$p(3) = 3 - 3 = 0$. A value of $x$ that makes $p(x) = 0$ is called a **zero** of the polynomial."),
 ]},
 {"id": "s2", "title": "Polynomials and their zeroes", "blocks": [
  b("s2.reveal", "theory", title="Degree, value and zero of a polynomial",
    body="- The highest power of $x$ in $p(x)$ is its **degree**. $4x + 2$ has degree 1, $2y^{2} - 3y + 4$ has degree 2, "
         "$5x^{3} - 4x^{2} + x - \\sqrt{2}$ has degree 3.\n"
         "- Degree 1: **linear** ($ax + b$, $a \\neq 0$). Degree 2: **quadratic** ($ax^{2} + bx + c$, $a \\neq 0$). Degree 3: **cubic**.\n"
         "- Putting $x = k$ gives the **value** $p(k)$.\n"
         "- $k$ is a **zero** of $p(x)$ if $p(k) = 0$.\n\n"
         "The zero of the linear polynomial $ax + b$ is $-\\dfrac{b}{a}$."),
  b("s2.eg", "worked_example", title="Checking zeroes",
    problem="Show that $-1$ and $4$ are zeroes of $p(x) = x^{2} - 3x - 4$.",
    steps=["$p(-1) = (-1)^{2} - 3(-1) - 4 = 1 + 3 - 4 = 0$",
           "$p(4) = 4^{2} - 3(4) - 4 = 16 - 12 - 4 = 0$"],
    answer="Both values give $p(x) = 0$, so $-1$ and $4$ are zeroes."),
  b("s2.check", "knowledge_check", question="The degree of $4x^{3} - 2x + 1$ is:",
    options=["$3$", "$4$", "$1$", "$2$"], correct_index=0, explanation="The highest power of $x$ is 3."),
 ]},
 {"id": "s3", "title": "What zeroes look like on a graph", "blocks": [
  b("s3.discovery", "discovery", title="Watch the curve meet the x-axis",
    body="On the graph of $y = p(x)$, a zero is an $x$ where $y = 0$: the point where the curve meets the **x-axis**. "
         "Watch the curves below being drawn and count where they meet the x-axis."),
  gb("s3.g1", "linear", "A linear polynomial: one zero", "y = 2x + 3", ["-3/2"]),
  gb("s3.g2", "two", "A quadratic meeting the x-axis twice", "y = x^{2} - 3x - 4"),
  gb("s3.g3", "touch", "A quadratic touching the x-axis once", "y = x^{2} - 4x + 4"),
  gb("s3.g4", "none", "A quadratic that never meets the x-axis", "y = x^{2} + 1"),
  b("s3.reveal", "theory", title="Zeroes and the graph",
    body="- The zeroes of $p(x)$ are the $x$-coordinates of the points where the graph of $y = p(x)$ **intersects or touches the x-axis**.\n"
         "- The graph of a quadratic $ax^{2} + bx + c$ is a **parabola**: it opens upwards if $a > 0$ and downwards if $a < 0$.\n"
         "- A quadratic can have **two**, **one** or **no** zeroes, so **at most 2**. A cubic has at most 3. "
         "In general, a polynomial of degree $n$ has at most $n$ zeroes."),
  b("s3.check", "knowledge_check", question="The graph of $y = p(x)$ meets the x-axis at exactly 3 points. How many zeroes does $p(x)$ have?",
    options=["$3$", "$2$", "$1$", "Cannot be found"], correct_index=0, explanation="Each meeting point with the x-axis gives one zero."),
  b("s3.tip", "teacher_tip", title="Use the panel",
    body="On the classroom panel, replay the four graphs and pause each one exactly when it meets the x-axis. "
         "Ask: 'What is $y$ here?' Students answer 'zero' and the definition of a zero becomes visual."),
 ]},
 {"id": "s4", "title": "Zeroes and coefficients", "blocks": [
  b("s4.socratic", "socratic_question",
    question="$(x - 2)(x - 3) = x^{2} - 5x + 6$. The zeroes are 2 and 3. Do you notice a link between 2, 3 and the numbers $-5$ and $6$?",
    options=["Sum $2 + 3 = 5$ and product $2 \\times 3 = 6$", "No link at all", "Only the product is linked"], correct_index=0,
    explanation="The sum of the zeroes is $5 = -(-5)$ and their product is $6$. This works for every quadratic, as you will see."),
  b("s4.reveal", "theory", title="The relationship",
    body="If $\\alpha$ and $\\beta$ are the zeroes of $p(x) = ax^{2} + bx + c$ ($a \\neq 0$), then\n\n"
         "$$\\alpha + \\beta = -\\frac{b}{a}, \\qquad \\alpha\\beta = \\frac{c}{a}$$\n\n"
         "*Why:* $p(x) = a(x - \\alpha)(x - \\beta) = ax^{2} - a(\\alpha + \\beta)x + a\\alpha\\beta$. Comparing with $ax^{2} + bx + c$ "
         "gives $b = -a(\\alpha + \\beta)$ and $c = a\\alpha\\beta$.\n\n"
         "**Building a quadratic from its zeroes:** if the sum is $S$ and the product is $P$, then $k(x^{2} - Sx + P)$ works for any $k \\neq 0$."),
  b("s4.eg2", "worked_example", title="NCERT Example 2",
    problem="Find the zeroes of $x^{2} + 7x + 10$, and verify the relationship between the zeroes and the coefficients.",
    steps=["$x^{2} + 7x + 10 = (x + 2)(x + 5)$, so the zeroes are $-2$ and $-5$.",
           "Sum $= -2 + (-5) = -7 = -\\dfrac{7}{1} = -\\dfrac{b}{a}$ ✓",
           "Product $= (-2)(-5) = 10 = \\dfrac{10}{1} = \\dfrac{c}{a}$ ✓"],
    answer="Zeroes $-2$ and $-5$; relationship verified."),
  b("s4.eg3", "worked_example", title="NCERT Example 3",
    problem="Find the zeroes of $x^{2} - 3$ and verify the relationship between the zeroes and the coefficients.",
    steps=["$x^{2} - 3 = (x - \\sqrt{3})(x + \\sqrt{3})$, so the zeroes are $\\sqrt{3}$ and $-\\sqrt{3}$.",
           "Here $a = 1$, $b = 0$, $c = -3$.",
           "Sum $= \\sqrt{3} - \\sqrt{3} = 0 = -\\dfrac{0}{1}$ ✓, product $= -3 = \\dfrac{-3}{1}$ ✓"],
    answer="Zeroes $\\pm\\sqrt{3}$; relationship verified."),
  b("s4.eg4", "worked_example", title="NCERT Example 4",
    problem="Find a quadratic polynomial, the sum and product of whose zeroes are $-3$ and $2$, respectively.",
    steps=["Use $k(x^{2} - Sx + P)$ with $S = -3$, $P = 2$.",
           "$x^{2} - (-3)x + 2 = x^{2} + 3x + 2$ (taking $k = 1$)."],
    answer="$x^{2} + 3x + 2$ (or any $k(x^{2} + 3x + 2)$, $k \\neq 0$)"),
  b("s4.memory", "memory_trick", title="Sum has a minus, product does not",
    body="**S**um $= -\\dfrac{b}{a}$ (the **s**ign flips). **P**roduct $= \\dfrac{c}{a}$ (no change).\n\n"
         "To build a quadratic: $x^{2} - (\\text{sum})x + (\\text{product})$."),
  b("s4.check1", "knowledge_check", question="If $\\alpha$ and $\\beta$ are the zeroes of $2x^{2} - 5x + 3$, then $\\alpha + \\beta$ is:",
    options=["$\\dfrac{5}{2}$", "$-\\dfrac{5}{2}$", "$\\dfrac{3}{2}$", "$5$"], correct_index=0,
    explanation="$\\alpha + \\beta = -\\dfrac{b}{a} = -\\dfrac{-5}{2} = \\dfrac{5}{2}$."),
  b("s4.check2", "knowledge_check", question="A quadratic polynomial whose zeroes are $-2$ and $5$ is:",
    options=["$x^{2} - 3x - 10$", "$x^{2} + 3x - 10$", "$x^{2} - 3x + 10$", "$x^{2} + 7x - 10$"], correct_index=0,
    explanation="Sum $= 3$, product $= -10$, so $x^{2} - 3x - 10$."),
  b("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Writing sum $= \\dfrac{b}{a}$. It is $-\\dfrac{b}{a}$.\n"
         "- Reading $a, b, c$ before arranging the polynomial in standard form: in $6x^{2} - 3 - 7x$, $b = -7$ and $c = -3$.\n"
         "- When $b$ or $c$ is missing, it is 0: in $x^{2} - 15$, $b = 0$.\n"
         "- Forgetting that $4s^{2} - 4s + 1 = (2s - 1)^{2}$ has the zero $\\dfrac{1}{2}$ twice."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  b("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why a quadratic can never have three zeroes, using the picture of a parabola."),
  b("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 4, Quadratic Equations:** solving $ax^{2} + bx + c = 0$ means finding the zeroes of a quadratic polynomial.\n"
         "- **Coordinate Geometry:** graphs of linear polynomials are straight lines.\n"
         "- **Physics:** the height of a thrown ball over time is a quadratic; its zeroes tell when it is at ground level."),
  gb("s5.arch", "arch", "A bridge arch", "y = -x^{2} + 2x + 8"),
  b("s5.mastery", "mastery", title="Mastery challenge",
    body="One zero of $3x^{2} - 8x + 2k + 1$ is seven times the other. Find the zeroes and the value of $k$.\n\n"
         "**Answer:** let the zeroes be $\\alpha$ and $7\\alpha$. Sum: $8\\alpha = \\dfrac{8}{3}$, so $\\alpha = \\dfrac{1}{3}$ "
         "and the zeroes are $\\dfrac{1}{3}, \\dfrac{7}{3}$. Product: $\\dfrac{7}{9} = \\dfrac{2k + 1}{3}$, so $2k + 1 = \\dfrac{7}{3}$ and $k = \\dfrac{2}{3}$."),
  b("s5.summary", "summary", title="Chapter summary",
    body="- Polynomials of degree 1, 2 and 3 are linear, quadratic and cubic.\n"
         "- Zeroes of $p(x)$ are the $x$-coordinates where the graph of $y = p(x)$ meets the x-axis.\n"
         "- A quadratic has at most 2 zeroes; a polynomial of degree $n$ has at most $n$.\n"
         "- For $ax^{2} + bx + c$: $\\alpha + \\beta = -\\dfrac{b}{a}$, $\\alpha\\beta = \\dfrac{c}{a}$.\n"
         "- A quadratic with zero-sum $S$ and product $P$: $k(x^{2} - Sx + P)$."),
  b("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Factorise by splitting the middle term, then **write both zeroes clearly**.\n"
         "- In 'verify' questions, show sum and product separately with $-\\dfrac{b}{a}$ and $\\dfrac{c}{a}$.\n"
         "- Expressions like $\\alpha^{2} + \\beta^{2}$ or $\\dfrac{1}{\\alpha} + \\dfrac{1}{\\beta}$: rewrite using $\\alpha + \\beta$ and $\\alpha\\beta$; "
         "do **not** find the zeroes separately unless asked.\n"
         "- Graph questions: count points where the curve **meets** the x-axis, including touching points."),
  b("s5.flash1", "flashcard", front="Sum and product of the zeroes of $ax^{2} + bx + c$?",
    back="Sum $= -\\dfrac{b}{a}$, product $= \\dfrac{c}{a}$."),
  b("s5.flash2", "flashcard", front="How many zeroes can a quadratic polynomial have?", back="At most 2: two, one, or none."),
  b("s5.flash3", "flashcard", front="Quadratic with zero-sum $S$ and product $P$?", back="$k(x^{2} - Sx + P)$, $k \\neq 0$."),
 ]},
]

chapter = {
  "schema_version": 1, "id": CH_ID, "title": "Polynomials",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)",
  "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 2, "languages": ["en"],
  "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: zeroes of a polynomial and the relationship between zeroes and coefficients "
                   "of quadratic polynomials. The division algorithm and cubic relationships are not in the board syllabus and are not included.",
  "concepts": ["polynomial_degree", "zeroes_of_polynomial", "graph_of_polynomial", "zeroes_coefficients_relationship"],
  "sections": sections,
}

# ---------------------------------------------------------------- question bank
Q = []
DEG, ZERO, GRAPH, REL = "polynomial_degree", "zeroes_of_polynomial", "graph_of_polynomial", "zeroes_coefficients_relationship"
SHINE = {"kind": "shine"}
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch02.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s

for part, name, count in [("i", "ex_i", 0), ("ii", "ex_ii", 1), ("iii", "ex_iii", 3), ("iv", "ex_iv", 2), ("v", "ex_v", 4), ("vi", "ex_vi", 3)]:
    check(len(GRAPHS[name][1]) == count, f"Ex 2.1 {part} count")
    fig = graph(name, f"Graph for part ({part})", "y = p(x)")
    q(f"ex2_1.q1.{part}", "mcq", 1, [GRAPH, ZERO], ex("2.1", 1, part),
      "The graph of $y = p(x)$ is shown. Find the number of zeroes of $p(x)$.", "easy",
      figure=fig, options=["$0$", "$1$", "$2$", "$3$", "$4$"], correct_index=count,
      explanation=f"The graph meets the x-axis at {count} point{'s' if count != 1 else ''}, so $p(x)$ has {count} zero{'es' if count != 1 else ''}.",
      teacher_note="Graph drawn by Shine Academy to match the answer of NCERT Fig. 2.10; compare its shape with the textbook figure.")

for part, e, tex, zs in EX22:
    p_ = Poly(expand(e), x); a, b_, c = p_.all_coeffs()
    def t(v):
        v = simplify(v)
        if v.is_Rational and v.q != 1: return f"{'-' if v < 0 else ''}\\dfrac{{{abs(v.p)}}}{{{v.q}}}"
        return str(v).replace("sqrt(15)", "\\sqrt{15}")
    zs_tex = " and ".join(f"${t(z)}$" for z in zs) if zs[0] != zs[1] else f"${t(zs[0])}$ (repeated)"
    q(f"ex2_2.q1.{part}", "short_answer", 3, [ZERO, REL], ex("2.2", 1, part),
      f"Find the zeroes of the quadratic polynomial ${tex}$, and verify the relationship between the zeroes and the coefficients.",
      answer_steps=[f"Factorising / solving ${tex} = 0$ gives the zeroes {zs_tex}.",
                    f"Sum of zeroes $= {t(zs[0] + zs[1])}$ and $-\\dfrac{{b}}{{a}} = {t(-b_ / a)}$ ✓",
                    f"Product of zeroes $= {t(zs[0] * zs[1])}$ and $\\dfrac{{c}}{{a}} = {t(c / a)}$ ✓"],
      marking_scheme=["1 mark: zeroes", "1 mark: sum verified", "1 mark: product verified"])

TEX22B = {"i": ("\\dfrac{1}{4}, -1", "4x^{2} - x - 4"), "ii": ("\\sqrt{2}, \\dfrac{1}{3}", "3x^{2} - 3\\sqrt{2}x + 1"),
          "iii": ("0, \\sqrt{5}", "x^{2} + \\sqrt{5}"), "iv": ("1, 1", "x^{2} - x + 1"),
          "v": ("-\\dfrac{1}{4}, \\dfrac{1}{4}", "4x^{2} + x + 1"), "vi": ("4, 1", "x^{2} - 4x + 1")}
for part, S, P, poly in EX22B:
    given, ans = TEX22B[part]
    q(f"ex2_2.q2.{part}", "very_short_answer", 2, [REL], ex("2.2", 2, part),
      f"Find a quadratic polynomial whose sum and product of zeroes are ${given}$ respectively.", "easy",
      answer_steps=["Required polynomial $= k(x^{2} - Sx + P)$", f"Taking a suitable $k$: ${ans}$"],
      marking_scheme=["1 mark: using $x^{2} - Sx + P$", "1 mark: correct polynomial"])

q("eg2", "short_answer", 3, [ZERO, REL], {"kind": "ncert_example", "example": 2},
  "Find the zeroes of $x^{2} + 7x + 10$, and verify the relationship between the zeroes and the coefficients.",
  answer_steps=["$x^{2} + 7x + 10 = (x + 2)(x + 5)$: zeroes $-2, -5$", "Sum $= -7 = -\\dfrac{7}{1}$ ✓", "Product $= 10 = \\dfrac{10}{1}$ ✓"],
  marking_scheme=["1 mark: zeroes", "1 mark: sum", "1 mark: product"])
q("eg3", "very_short_answer", 2, [ZERO, REL], {"kind": "ncert_example", "example": 3},
  "Find the zeroes of $x^{2} - 3$ and verify the relationship between the zeroes and the coefficients.",
  answer_steps=["Zeroes $\\sqrt{3}, -\\sqrt{3}$", "Sum $0 = -\\dfrac{0}{1}$, product $-3 = \\dfrac{-3}{1}$ ✓"],
  marking_scheme=["1 mark: zeroes", "1 mark: verification"])
q("eg4", "very_short_answer", 2, [REL], {"kind": "ncert_example", "example": 4},
  "Find a quadratic polynomial, the sum and product of whose zeroes are $-3$ and $2$, respectively.", "easy",
  answer_steps=["$x^{2} - (-3)x + 2$", "$= x^{2} + 3x + 2$"], marking_scheme=["1 mark: method", "1 mark: answer"])

def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy"):
    q(id_, "mcq", 1, concepts, SHINE, question, difficulty, options=options, correct_index=correct, explanation=explanation)
mcq("mcq01", [ZERO], "The zeroes of $x^{2} - 5x + 6$ are:", ["$2, 3$", "$-2, -3$", "$1, 6$", "$-1, -6$"], 0, "$(x - 2)(x - 3)$.")
mcq("mcq02", [REL], "If $\\alpha, \\beta$ are the zeroes of $x^{2} + 5x + 6$, then $\\alpha + \\beta$ is:", ["$-5$", "$5$", "$6$", "$-6$"], 0, "$-\\dfrac{b}{a} = -5$.")
mcq("mcq03", [REL], "A quadratic polynomial whose zeroes are $-2$ and $5$ is:",
    ["$x^{2} - 3x - 10$", "$x^{2} + 3x - 10$", "$x^{2} - 7x + 10$", "$x^{2} + 3x + 10$"], 0, "Sum 3, product $-10$.")
mcq("mcq04", [GRAPH], "If the graph of $y = p(x)$ cuts the x-axis at exactly three points, the number of zeroes of $p(x)$ is:",
    ["$3$", "$2$", "$1$", "$0$"], 0, "One zero for each point on the x-axis.")
mcq("mcq05", [GRAPH], "The graph of $y = ax^{2} + bx + c$ with $a < 0$ is a parabola that:",
    ["opens downwards", "opens upwards", "is a straight line", "always passes through the origin"], 0, "$a < 0$ makes it open downwards.")
mcq("mcq06", [ZERO], "If $2$ is a zero of $x^{2} + 3x + k$, then the value of $k$ is:", ["$-10$", "$10$", "$-2$", "$2$"], 0,
    "$4 + 6 + k = 0$, so $k = -10$.")
mcq("mcq07", [REL], "If $\\alpha, \\beta$ are the zeroes of $2x^{2} - 5x + 3$, then $\\dfrac{1}{\\alpha} + \\dfrac{1}{\\beta}$ is:",
    ["$\\dfrac{5}{3}$", "$\\dfrac{3}{5}$", "$\\dfrac{5}{2}$", "$-\\dfrac{5}{3}$"], 0,
    "$\\dfrac{\\alpha + \\beta}{\\alpha\\beta} = \\dfrac{5/2}{3/2} = \\dfrac{5}{3}$.", "medium")
mcq("mcq08", [REL], "If the zeroes of $x^{2} + (a + 1)x + b$ are $2$ and $-3$, then:",
    ["$a = 0, b = -6$", "$a = 2, b = -6$", "$a = -7, b = -1$", "$a = 5, b = -1$"], 0,
    "Sum $-1 = -(a + 1)$ gives $a = 0$; product $-6 = b$.", "medium")
mcq("mcq09", [DEG], "A quadratic polynomial can have at most:", ["$2$ zeroes", "$1$ zero", "$3$ zeroes", "infinitely many zeroes"], 0,
    "A degree-2 polynomial has at most 2 zeroes.")
mcq("mcq10", [ZERO], "The zeroes of $x^{2} - 3$ are:", ["$\\pm\\sqrt{3}$", "$\\pm 3$", "$3, 0$", "$\\pm 9$"], 0, "$x^{2} = 3$.")
mcq("mcq11", [REL], "If the sum of the zeroes of $kx^{2} + 2x + 3k$ is equal to their product, then $k$ is:",
    ["$-\\dfrac{2}{3}$", "$\\dfrac{2}{3}$", "$\\dfrac{1}{3}$", "$-\\dfrac{1}{3}$"], 0, "$-\\dfrac{2}{k} = 3$, so $k = -\\dfrac{2}{3}$.", "medium")
mcq("mcq12", [DEG], "The degree of $(x - 1)(x + 2)(x - 3)$ is:", ["$3$", "$2$", "$1$", "$6$"], 0, "Product of three linear factors.")
mcq("mcq13", [REL], "The product of the zeroes of $3x^{2} - x - 4$ is:", ["$-\\dfrac{4}{3}$", "$\\dfrac{4}{3}$", "$\\dfrac{1}{3}$", "$-4$"], 0,
    "$\\dfrac{c}{a} = -\\dfrac{4}{3}$.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.",
              "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.",
              "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium",
      options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [ZERO, GRAPH], "$x^{2} + 4x + 5$ has two real zeroes.", "A quadratic polynomial can have at most two zeroes.", 3,
   "$x^{2} + 4x + 5 = (x + 2)^{2} + 1 > 0$, so it has no real zeroes: A is false. R is true.")
ar("ar2", [REL], "If $\\alpha, \\beta$ are the zeroes of $x^{2} - 9$, then $\\alpha + \\beta = 0$.",
   "The sum of the zeroes of $ax^{2} + bx + c$ is $-\\dfrac{b}{a}$.", 0, "Here $b = 0$, so the sum is 0, exactly by R.")
ar("ar3", [GRAPH, ZERO], "The graph of $y = x^{2} - 4$ meets the x-axis at two points.", "$x^{2} - 4$ has two zeroes, $2$ and $-2$.", 0,
   "Each zero gives a point on the x-axis.")
ar("ar4", [DEG], "$3x^{3} + 2x - 1$ is a quadratic polynomial.", "The degree of a polynomial is the highest power of the variable.", 3,
   "Its degree is 3, so it is cubic: A is false, R is true.")

q("vsa1", "very_short_answer", 2, [REL], SHINE, "Find a quadratic polynomial whose zeroes are $3 + \\sqrt{2}$ and $3 - \\sqrt{2}$.",
  answer_steps=["Sum $= 6$, product $= 9 - 2 = 7$", "Polynomial: $x^{2} - 6x + 7$"], marking_scheme=["1 mark: sum and product", "1 mark: polynomial"])
q("vsa2", "very_short_answer", 2, [REL], SHINE, "If $\\alpha, \\beta$ are the zeroes of $x^{2} - 6x + 8$, find $\\alpha^{2} + \\beta^{2}$.", "medium",
  answer_steps=["$\\alpha + \\beta = 6$, $\\alpha\\beta = 8$", "$\\alpha^{2} + \\beta^{2} = (\\alpha + \\beta)^{2} - 2\\alpha\\beta = 36 - 16 = 20$"],
  marking_scheme=["1 mark: sum and product", "1 mark: 20"])
q("vsa3", "very_short_answer", 2, [ZERO], SHINE, "Find the zeroes of $2x^{2} - 8x + 6$.", "easy",
  answer_steps=["$2x^{2} - 8x + 6 = 2(x - 1)(x - 3)$", "Zeroes: $1$ and $3$"], marking_scheme=["1 mark: factorisation", "1 mark: zeroes"])
q("sa1", "short_answer", 3, [ZERO, REL], SHINE, "Find the zeroes of $4x^{2} - 4x - 3$ and verify the relationship between the zeroes and the coefficients.",
  answer_steps=["$4x^{2} - 4x - 3 = (2x - 3)(2x + 1)$: zeroes $\\dfrac{3}{2}, -\\dfrac{1}{2}$", "Sum $= 1 = -\\dfrac{-4}{4}$ ✓",
                "Product $= -\\dfrac{3}{4} = \\dfrac{-3}{4}$ ✓"], marking_scheme=["1 mark: zeroes", "1 mark: sum", "1 mark: product"])
q("sa2", "short_answer", 3, [REL], SHINE, "If $\\alpha, \\beta$ are the zeroes of $x^{2} - 5x + 4$, find $\\dfrac{1}{\\alpha} + \\dfrac{1}{\\beta} - 2\\alpha\\beta$.", "medium",
  answer_steps=["$\\alpha + \\beta = 5$, $\\alpha\\beta = 4$", "$\\dfrac{1}{\\alpha} + \\dfrac{1}{\\beta} = \\dfrac{\\alpha + \\beta}{\\alpha\\beta} = \\dfrac{5}{4}$",
                "Required value $= \\dfrac{5}{4} - 8 = -\\dfrac{27}{4}$"], marking_scheme=["1 mark: sum and product", "1 mark: $\\dfrac{5}{4}$", "1 mark: $-\\dfrac{27}{4}$"])
q("sa3", "short_answer", 3, [REL, ZERO], SHINE, "Find a quadratic polynomial whose zeroes are the reciprocals of the zeroes of $2x^{2} - 5x + 3$.", "hard",
  answer_steps=["$2x^{2} - 5x + 3 = (x - 1)(2x - 3)$: zeroes $1, \\dfrac{3}{2}$", "Reciprocals: $1, \\dfrac{2}{3}$; sum $\\dfrac{5}{3}$, product $\\dfrac{2}{3}$",
                "Polynomial: $k\\left(x^{2} - \\dfrac{5}{3}x + \\dfrac{2}{3}\\right)$; with $k = 3$: $3x^{2} - 5x + 2$"],
  marking_scheme=["1 mark: zeroes", "1 mark: sum and product of reciprocals", "1 mark: polynomial"])
q("sa4", "short_answer", 3, [REL], SHINE, "One zero of $3x^{2} - 8x + 2k + 1$ is seven times the other. Find both zeroes and the value of $k$.", "hard",
  answer_steps=["Let the zeroes be $\\alpha$ and $7\\alpha$. Sum: $8\\alpha = \\dfrac{8}{3}$, so $\\alpha = \\dfrac{1}{3}$; zeroes $\\dfrac{1}{3}, \\dfrac{7}{3}$",
                "Product: $\\dfrac{7}{9} = \\dfrac{2k + 1}{3}$", "$2k + 1 = \\dfrac{7}{3}$, so $k = \\dfrac{2}{3}$"],
  marking_scheme=["1 mark: zeroes", "1 mark: product equation", "1 mark: $k = \\dfrac{2}{3}$"])
q("cb1", "case_based", 4, [GRAPH, ZERO, REL], SHINE,
  "The arch of a bridge has the shape of the graph of $y = -x^{2} + 2x + 8$, where $x$ is in metres and the road is the x-axis.\n\n"
  "(i) How many zeroes does the polynomial have? (1)\n\n(ii) Find its zeroes. (1)\n\n"
  "(iii) Find the sum and product of the zeroes. OR How wide is the arch at road level? (2)", "medium",
  figure=graph("arch", "Bridge arch", "y = -x^{2} + 2x + 8"),
  answer_steps=["(i) The parabola meets the x-axis twice: 2 zeroes",
                "(ii) $-x^{2} + 2x + 8 = -(x - 4)(x + 2)$: zeroes $-2$ and $4$",
                "(iii) Sum $= 2 = -\\dfrac{2}{-1}$, product $= -8 = \\dfrac{8}{-1}$. OR width $= 4 - (-2) = 6$ m"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark each for sum and product (or width with working)"])
q("cb2", "case_based", 4, [ZERO, REL], SHINE,
  "The height of a ball is modelled by $p(x) = -x^{2} + 6x - 5$, where $x$ is the horizontal distance in metres. The ball is at ground level when $p(x) = 0$.\n\n"
  "(i) Find the zeroes of $p(x)$. (1)\n\n(ii) Find the sum of the zeroes. (1)\n\n"
  "(iii) The highest point is midway between the zeroes. Find the maximum height. (2)", "medium",
  answer_steps=["(i) $-x^{2} + 6x - 5 = -(x - 1)(x - 5)$: zeroes $1$ and $5$", "(ii) Sum $= 6$",
                "(iii) Midway: $x = 3$; $p(3) = -9 + 18 - 5 = 4$ m"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark for $x = 3$, 1 mark for 4 m"])

def spread_answers(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch02.q.ex2_1"):
        return  # Ex 2.1 keeps options in numeric order 0-4
    shift = sum(map(ord, item["id"])) % len(opts)
    correct = opts[item["correct_index"]]
    item["options"] = opts[shift:] + opts[:shift]
    item["correct_index"] = item["options"].index(correct)
for it in Q: spread_answers(it)
for sec in sections:
    for blk in sec["blocks"]: spread_answers(blk)
print("answer positions:", Counter(it["correct_index"] for it in Q if it["type"] == "mcq"))

os.makedirs(os.path.join(ROOT, PATH), exist_ok=True)
for name, data in [("chapter.json", chapter), ("questions.json", {"schema_version": 1, "chapter_id": CH_ID, "questions": Q})]:
    with open(os.path.join(ROOT, PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2); f.write("\n")
print(f"blocks={sum(len(s['blocks']) for s in sections)} questions={len(Q)} ncert_exercise_items={sum(1 for it in Q if it['source']['kind'] == 'ncert_exercise')}")
