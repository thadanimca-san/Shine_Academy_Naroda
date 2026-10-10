"""CBSE Class 10 Maths Ch 5: Arithmetic Progressions.
Every term, sum and count is checked with exact arithmetic (Fraction / sympy)."""
import json, os, sys
from collections import Counter
from fractions import Fraction as Fr
from sympy import sqrt, simplify, symbols, solve, Rational

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch05"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch05_arithmetic_progressions"
n_ = symbols("n")

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def term(a, d, n): return a + (n - 1) * d
def S(a, d, n): return Fr(n, 2) * (2 * a + (n - 1) * d)
def is_ap(seq): return len({simplify(seq[i + 1] - seq[i]) for i in range(len(seq) - 1)}) == 1
def nth_index(a, d, value):  # n for which a_n = value, as a Fraction
    return Fr(value - a) / d + 1

# ---------------------------------------------------------------- verification
# Ex 5.1 Q1
check(is_ap([15 + 8 * k for k in range(4)]), "5.1 Q1 i"); check(not is_ap([Fr(3, 4) ** k for k in range(4)]), "5.1 Q1 ii")
check(is_ap([150 + 50 * k for k in range(4)]), "5.1 Q1 iii"); check(not is_ap([10000 * Fr(108, 100) ** k for k in range(4)]), "5.1 Q1 iv")
EX51Q2 = [("i", 10, 10), ("ii", -2, 0), ("iii", 4, -3), ("iv", -1, Fr(1, 2)), ("v", Fr(-125, 100), Fr(-25, 100))]
EX51Q2_TEX = {"i": ("a = 10, d = 10", "10, 20, 30, 40"), "ii": ("a = -2, d = 0", "-2, -2, -2, -2"), "iii": ("a = 4, d = -3", "4, 1, -2, -5"),
              "iv": ("a = -1, d = \\dfrac{1}{2}", "-1, -\\dfrac{1}{2}, 0, \\dfrac{1}{2}"), "v": ("a = -1.25, d = -0.25", "-1.25, -1.50, -1.75, -2.00")}
check([term(-1, Fr(1, 2), k) for k in (1, 2, 3, 4)] == [-1, Fr(-1, 2), 0, Fr(1, 2)], "5.1 Q2 iv"); check([term(4, -3, k) for k in (1, 2, 3, 4)] == [4, 1, -2, -5], "5.1 Q2 iii")
check([term(Fr(-125, 100), Fr(-25, 100), k) for k in (1, 2, 3, 4)] == [Fr(-5, 4), Fr(-3, 2), Fr(-7, 4), -2], "5.1 Q2 v")
EX51Q3 = [("i", "3, 1, -1, -3, \\ldots", "a = 3, d = 1 - 3 = -2", [3, 1, -1, -3], 3, -2), ("ii", "-5, -1, 3, 7, \\ldots", "a = -5, d = -1 - (-5) = 4", [-5, -1, 3, 7], -5, 4),
          ("iii", "\\dfrac{1}{3}, \\dfrac{5}{3}, \\dfrac{9}{3}, \\dfrac{13}{3}, \\ldots", "a = \\dfrac{1}{3}, d = \\dfrac{5}{3} - \\dfrac{1}{3} = \\dfrac{4}{3}", [Fr(1, 3), Fr(5, 3), Fr(9, 3), Fr(13, 3)], Fr(1, 3), Fr(4, 3)),
          ("iv", "0.6, 1.7, 2.8, 3.9, \\ldots", "a = 0.6, d = 1.7 - 0.6 = 1.1", [Fr(6, 10), Fr(17, 10), Fr(28, 10), Fr(39, 10)], Fr(6, 10), Fr(11, 10))]
for p, _, _, seq, a, d in EX51Q3: check(is_ap(seq) and seq[0] == a and seq[1] - seq[0] == d, f"5.1 Q3 {p}")
r2, r3 = sqrt(2), sqrt(3)
EX51Q4 = [  # part, latex, values, (d latex, next three latex) or (diff1, diff2) for non-AP
 ("i", "2, 4, 8, 16, \\ldots", [2, 4, 8, 16], None, ("a_2 - a_1 = 2", "a_3 - a_2 = 4")),
 ("ii", "2, \\dfrac{5}{2}, 3, \\dfrac{7}{2}, \\ldots", [2, Fr(5, 2), 3, Fr(7, 2)], ("d = \\dfrac{1}{2}", "4, \\dfrac{9}{2}, 5", [4, Fr(9, 2), 5]), None),
 ("iii", "-1.2, -3.2, -5.2, -7.2, \\ldots", [Fr(-12, 10), Fr(-32, 10), Fr(-52, 10), Fr(-72, 10)], ("d = -2", "-9.2, -11.2, -13.2", [Fr(-92, 10), Fr(-112, 10), Fr(-132, 10)]), None),
 ("iv", "-10, -6, -2, 2, \\ldots", [-10, -6, -2, 2], ("d = 4", "6, 10, 14", [6, 10, 14]), None),
 ("v", "3, 3 + \\sqrt{2}, 3 + 2\\sqrt{2}, 3 + 3\\sqrt{2}, \\ldots", [3, 3 + r2, 3 + 2 * r2, 3 + 3 * r2], ("d = \\sqrt{2}", "3 + 4\\sqrt{2}, 3 + 5\\sqrt{2}, 3 + 6\\sqrt{2}", [3 + 4 * r2, 3 + 5 * r2, 3 + 6 * r2]), None),
 ("vi", "0.2, 0.22, 0.222, 0.2222, \\ldots", [Fr(2, 10), Fr(22, 100), Fr(222, 1000), Fr(2222, 10000)], None, ("a_2 - a_1 = 0.02", "a_3 - a_2 = 0.002")),
 ("vii", "0, -4, -8, -12, \\ldots", [0, -4, -8, -12], ("d = -4", "-16, -20, -24", [-16, -20, -24]), None),
 ("viii", "-\\dfrac{1}{2}, -\\dfrac{1}{2}, -\\dfrac{1}{2}, -\\dfrac{1}{2}, \\ldots", [Fr(-1, 2)] * 4, ("d = 0", "-\\dfrac{1}{2}, -\\dfrac{1}{2}, -\\dfrac{1}{2}", [Fr(-1, 2)] * 3), None),
 ("ix", "1, 3, 9, 27, \\ldots", [1, 3, 9, 27], None, ("a_2 - a_1 = 2", "a_3 - a_2 = 6")),
 ("x", "a, 2a, 3a, 4a, \\ldots", [1, 2, 3, 4], ("d = a", "5a, 6a, 7a", [5, 6, 7]), None),
 ("xi", "a, a^{2}, a^{3}, a^{4}, \\ldots", [2, 4, 8, 16], None, ("a_2 - a_1 = a^{2} - a", "a_3 - a_2 = a^{3} - a^{2}")),
 ("xii", "\\sqrt{2}, \\sqrt{8}, \\sqrt{18}, \\sqrt{32}, \\ldots", [r2, sqrt(8), sqrt(18), sqrt(32)], ("d = \\sqrt{8} - \\sqrt{2} = \\sqrt{2}", "\\sqrt{50}, \\sqrt{72}, \\sqrt{98}", [sqrt(50), sqrt(72), sqrt(98)]), None),
 ("xiii", "\\sqrt{3}, \\sqrt{6}, \\sqrt{9}, \\sqrt{12}, \\ldots", [r3, sqrt(6), 3, sqrt(12)], None, ("a_2 - a_1 = \\sqrt{6} - \\sqrt{3}", "a_3 - a_2 = 3 - \\sqrt{6}")),
 ("xiv", "1^{2}, 3^{2}, 5^{2}, 7^{2}, \\ldots", [1, 9, 25, 49], None, ("a_2 - a_1 = 8", "a_3 - a_2 = 16")),
 ("xv", "1^{2}, 5^{2}, 7^{2}, 73, \\ldots", [1, 25, 49, 73], ("d = 24", "97, 121, 145", [97, 121, 145]), None),
]
for p, _, seq, yes, no in EX51Q4:
    check(is_ap(seq) == (yes is not None), f"5.1 Q4 {p}")
    if yes: d = simplify(seq[1] - seq[0]); check(all(simplify(v - (seq[-1] + (i + 1) * d)) == 0 for i, v in enumerate(yes[2])), f"5.1 Q4 {p} next")
# Ex 5.2
check(term(7, 3, 8) == 28 and Fr(0 - (-18), 9) == 2 and -5 - 17 * -3 == 46 and nth_index(Fr(-189, 10), Fr(5, 2), Fr(36, 10)) == 10 and term(Fr(7, 2), 0, 105) == Fr(7, 2), "5.2 Q1")
check(term(10, -3, 30) == -77 and term(-3, Fr(5, 2), 11) == 22, "5.2 Q2")
check(term(2, 12, 2) == 14 and is_ap([18, 13, 8, 3]) and is_ap([5, Fr(13, 2), 8, Fr(19, 2)]) and is_ap([-4, -2, 0, 2, 4, 6]) and is_ap([53, 38, 23, 8, -7, -22]), "5.2 Q3")
check(nth_index(3, 5, 78) == 16, "5.2 Q4"); check(nth_index(7, 6, 205) == 34 and nth_index(18, Fr(-5, 2), -47) == 27, "5.2 Q5")
check(nth_index(11, -3, -150) == Fr(164, 3), "5.2 Q6")
check(term(-32, 7, 11) == 38 and term(-32, 7, 16) == 73 and term(-32, 7, 31) == 178, "5.2 Q7")
check(term(8, 2, 3) == 12 and term(8, 2, 50) == 106 and term(8, 2, 29) == 64, "5.2 Q8")
check(term(8, -2, 3) == 4 and term(8, -2, 9) == -8 and term(8, -2, 5) == 0, "5.2 Q9")
check(term(0, 1, 17) - term(0, 1, 10) == 7, "5.2 Q10"); check(nth_index(3, 12, term(3, 12, 54) + 132) == 65, "5.2 Q11")
check(nth_index(105, 7, 994) == 128, "5.2 Q13"); check(nth_index(12, 4, 248) == 60, "5.2 Q14")
check(term(63, 2, 13) == term(3, 7, 13), "5.2 Q15"); check(term(4, 6, 3) == 16 and term(4, 6, 7) - term(4, 6, 5) == 12, "5.2 Q16")
check(term(253, -5, 20) == 158, "5.2 Q17"); check(term(-13, 5, 4) + term(-13, 5, 8) == 24 and term(-13, 5, 6) + term(-13, 5, 10) == 44, "5.2 Q18")
check(nth_index(5000, 200, 7000) == 11, "5.2 Q19"); check(nth_index(5, Fr(7, 4), Fr(83, 4)) == 10, "5.2 Q20")
# Ex 5.3
check(S(2, 5, 10) == 245 and S(-37, 4, 12) == -180 and S(Fr(6, 10), Fr(11, 10), 100) == 5505 and S(Fr(1, 15), Fr(1, 60), 11) == Fr(33, 20), "5.3 Q1")
check(Fr(1, 12) - Fr(1, 15) == Fr(1, 60) and Fr(1, 10) - Fr(1, 12) == Fr(1, 60), "5.3 Q1 iv d")
check(nth_index(7, Fr(7, 2), 84) == 23 and S(7, Fr(7, 2), 23) == Fr(2093, 2), "5.3 Q2 i"); check(nth_index(34, -2, 10) == 13 and S(34, -2, 13) == 286, "5.3 Q2 ii")
check(nth_index(-5, -3, -230) == 76 and S(-5, -3, 76) == -8930, "5.3 Q2 iii")
check(nth_index(5, 3, 50) == 16 and S(5, 3, 16) == 440, "5.3 Q3 i"); check(S(7, Fr(7, 3), 13) == 273 and term(7, Fr(7, 3), 13) == 35, "5.3 Q3 ii")
check(term(4, 3, 12) == 37 and S(4, 3, 12) == 246, "5.3 Q3 iii"); check(term(17, -1, 3) == 15 and S(17, -1, 10) == 125 and term(17, -1, 10) == 8, "5.3 Q3 iv")
check(S(Fr(-35, 3), 5, 9) == 75 and term(Fr(-35, 3), 5, 9) == Fr(85, 3), "5.3 Q3 v")
check(solve(n_ / 2 * (4 + 8 * (n_ - 1)) - 90, n_) == [Fr(-9, 2), 5] or set(solve(n_ / 2 * (4 + 8 * (n_ - 1)) - 90, n_)) == {Fr(-9, 2), 5}, "5.3 Q3 vi"); check(term(2, 8, 5) == 34, "5.3 Q3 vi an")
check(S(8, Fr(54, 5), 6) == 210 and term(8, Fr(54, 5), 6) == 62, "5.3 Q3 vii"); check(S(-8, 2, 7) == -14 and term(-8, 2, 7) == 4, "5.3 Q3 viii")
check(S(3, 6, 8) == 192, "5.3 Q3 ix"); check(Fr(9, 2) * (4 + 28) == 144, "5.3 Q3 x")
check(set(solve(n_ / 2 * (18 + 8 * (n_ - 1)) - 636, n_)) == {12, Rational(-53, 4)}, "5.3 Q4")
check(Fr(16, 2) * 50 == 400 and term(5, Fr(8, 3), 16) == 45, "5.3 Q5"); check(nth_index(17, 9, 350) == 38 and S(17, 9, 38) == 6973, "5.3 Q6")
check(term(2, 7, 22) == 149 and S(2, 7, 22) == 1661, "5.3 Q7"); check(term(10, 4, 2) == 14 and S(10, 4, 51) == 5610, "5.3 Q8")
check(S(1, 2, 7) == 49 and S(1, 2, 17) == 289 and all(S(1, 2, k) == k * k for k in range(1, 30)), "5.3 Q9")
check(S(7, 4, 15) == 525 and S(4, -5, 15) == -465, "5.3 Q10")
Sn = lambda k: 4 * k - k * k
check(Sn(1) == 3 and Sn(2) - Sn(1) == 1 and Sn(3) - Sn(2) == -1 and Sn(10) - Sn(9) == -15 and all(Sn(k) - Sn(k - 1) == 5 - 2 * k for k in range(2, 20)), "5.3 Q11")
check(S(6, 6, 40) == 4920 and S(8, 8, 15) == 960 and S(1, 2, 25) == 625, "5.3 Q12-14")
check(S(200, 50, 30) == 27750, "5.3 Q15"); check(S(160, -20, 7) == 700, "5.3 Q16"); check(3 * S(1, 1, 12) == 234, "5.3 Q17")
check(Fr(22, 7) * S(Fr(1, 2), Fr(1, 2), 13) == 143, "5.3 Q18")
check(set(solve(n_ / 2 * (40 - (n_ - 1)) - 200, n_)) == {16, 25} and term(20, -1, 16) == 5, "5.3 Q19")
check(2 * S(5, 3, 10) == 370, "5.3 Q20")
# Examples, lesson and Shine questions
check(term(2, 5, 10) == 47 and nth_index(21, -3, -81) == 35 and nth_index(21, -3, 0) == 8, "eg terms"); check(nth_index(12, 3, 99) == 30, "eg div3")
check(term(-62, 3, 11) == -32, "eg from last"); check(set(solve(n_ / 2 * (48 - 3 * (n_ - 1)) - 78, n_)) == {4, 13}, "eg 78")
check(S(8, -5, 22) == -979 and S(1, 1, 1000) == 500500, "eg sums"); check(S(105, 7, 128) == 70336, "mastery")
check(term(2, 3, 4) == 11 and [3 * k - 1 for k in (1, 2, 3, 4)] == [2, 5, 8, 11], "graph")
check(term(1, 4, 8) == 29, "s3.check"); check(S(3, 4, 10) == 210, "s4.check"); check(S(1, 1, 100) == 5050, "gauss")
check(term(3, 4, 4) - term(3, 4, 3) == 4, "mcq01"); check(term(5, 4, 10) == 41, "mcq02"); check(is_ap([-3, -1, 1, 3]) and not is_ap([1, 4, 9, 16]) and not is_ap([1, -1, 1, -1]), "mcq03")
check(S(1, 2, 20) == 400, "mcq04"); check(solve(2 * (n_ + 10) - (2 * n_ + 3 * n_ + 2), n_) == [6], "mcq05")
check(all(term(7, -3, k) == 10 - 3 * k for k in range(1, 10)), "mcq06"); check(25 - 16 == 9, "mcq07"); check(nth_index(7, 4, 139) == 34, "mcq08")
check(term(99, -3, 15) == 57, "mcq09"); check((2 * 2 + 3) - (2 * 1 + 3) == 2, "mcq11")
check(term(5, 3, 10) == 32, "ar4"); check(nth_index(5, 6, 301) == Fr(151, 3) and all(term(5, 6, k) % 6 == 5 for k in range(1, 50)) and 301 % 6 == 1, "ar2")
check(S(2, 2, 10) == 110, "ar3"); check(nth_index(3, 4, 184) == Fr(185, 4), "vsa2"); check(term(5, -3, 20) == -52, "vsa1")
check(nth_index(306, 9, 693) == 44 and S(306, 9, 44) == 21978 and 297 < 300 < 306 and 693 < 700 < 702, "sa1")
check(term(Fr(1, 63), Fr(1, 63), 7) == Fr(1, 9) and term(Fr(1, 63), Fr(1, 63), 9) == Fr(1, 7) and term(Fr(1, 63), Fr(1, 63), 63) == 1, "sa2")
check(set(solve(n_ / 2 * (108 - 3 * (n_ - 1)) - 513, n_)) == {18, 19} and term(54, -3, 19) == 0, "sa3")
check(all(3 * k * k + 5 * k - (3 * (k - 1) ** 2 + 5 * (k - 1)) == 6 * k + 2 for k in range(1, 30)) and 6 * 20 + 2 == 122, "sa4")
check(S(1200, 100, 10) == 16500 and term(1200, 100, 10) == 2100 and nth_index(1200, 100, 1700) == 6, "la1")
dd = symbols("dd"); check(simplify((4 * dd + 10 * dd) / (4 * dd + 17 * dd) - Fr(2, 3)) == 0, "la2 ratio")
check(simplify((4 * dd + 4 * dd) / (4 * dd + 20 * dd) - Fr(1, 3)) == 0 and simplify(S(4 * dd, dd, 5) / S(4 * dd, dd, 21) - Fr(5, 49)) == 0, "la2")
check(term(20, 2, 10) == 38 and term(20, 2, 30) == 78 and S(20, 2, 30) == 1470 and nth_index(20, 2, 50) == 16, "cb1")
check(term(50, 10, 8) == 120 and S(50, 10, 8) == 680 and nth_index(50, 10, 200) == 16 and S(50, 10, 20) == 2900, "cb2")
check(S(8, 2, 60) - S(8, 2, 50) == 1170 and term(8, 2, 51) == 108 and term(8, 2, 60) == 126, "sqp21a")
check(nth_index(6, 7, 230) == 33 and term(6, 7, 17) == 118, "sqp21b")
check(3 + -3 == 0 and term(187, -3, 34) == 88 and S(-5, 3, 10) == 85 and term(-5, 3, 33) == term(187, -3, 33), "sqp36")

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch05.{id_}", "type": type_, **kw}

sections = [
 {"id": "s1", "title": "Patterns that grow evenly", "blocks": [
  b("s1.hook", "hook", title="Reena's piggy bank",
    body="Reena puts ₹5 in her piggy bank in the first week, ₹10 in the second week, ₹15 in the third, and keeps adding ₹5 more every week.\n\n"
         "How much will she put in during the 20th week? How much will she have saved in a year? You could add week by week, but there is a much faster way. "
         "Lists of numbers that grow (or shrink) by the **same amount** every step are called **arithmetic progressions**, and in this chapter you will find any term and any sum in seconds."),
  b("s1.inspiration", "inspiration", title="Adding 1 to 100 in a minute", person="Carl Friedrich Gauss and Aryabhata", years="1777–1855 and 476–550 CE",
    body="The story goes that a schoolteacher in Germany asked his class to add all the numbers from 1 to 100, hoping to keep them busy. Within a minute, young Carl Gauss had the answer: **5050**.\n\n"
         "He paired the numbers: $1 + 100$, $2 + 99$, $3 + 98$, and so on. Each pair makes 101, and there are 50 pairs, so the sum is $50 \\times 101 = 5050$.\n\n"
         "Long before that, in 499 CE, Aryabhata had already written rules for the sum of such series in his *Aryabhatiya*. Gauss grew up to be one of the greatest mathematicians in history.",
    quote="Don't just work hard; look for the pattern. One clever idea can save an hour of work.",
    future="Arithmetic progressions are used in loan instalments (EMIs), salary increments, seating plans in stadiums, and in computer programs that count in steps."),
  b("s1.socratic", "socratic_question", question="What is the next number in the list $2, 5, 8, 11, \\ldots$?",
    options=["$14$", "$13$", "$22$"], correct_index=0,
    explanation="Each number is 3 more than the one before it: $11 + 3 = 14$. A list where you always add the same number is an arithmetic progression."),
 ]},
 {"id": "s2", "title": "Arithmetic progressions", "blocks": [
  b("s2.reveal", "theory", title="What is an arithmetic progression?", revision=True,
    body="An **arithmetic progression (AP)** is a list of numbers in which each term is obtained by adding a fixed number to the preceding term (except the first term).\n\n"
         "The fixed number is the **common difference** $d$. It can be positive, negative or zero. If the first term is $a$, the AP is\n\n$$a, \\; a + d, \\; a + 2d, \\; a + 3d, \\; \\ldots$$\n\n"
         "To find $d$, subtract any term from the next one: $d = a_2 - a_1 = a_3 - a_2 = \\ldots$ If these differences are not all equal, the list is **not** an AP.\n\n"
         "An AP with a last term is **finite**; one without a last term is **infinite**."),
  {"id": "ch05.s2.g1", "type": "function_graph", "title": "Terms of an AP lie on a straight line", "polynomial": [3, -1], "label": "a_n = 3n - 1",
                  "x_range": [0, 5], "zeroes": [], "points": [{"x": k, "y": 3 * k - 1, "label": f"({k}, {3 * k - 1})", "on": [0]} for k in (1, 2, 3, 4)]},
  b("s2.eg1", "worked_example", title="Is it an AP?",
    problem="Which of these lists are APs? (i) $4, 10, 16, 22, \\ldots$ (ii) $1, -1, -3, -5, \\ldots$ (iii) $1, 1, 2, 2, 3, 3, \\ldots$",
    steps=["(i) $10 - 4 = 16 - 10 = 22 - 16 = 6$: an AP with $d = 6$.", "(ii) $-1 - 1 = -3 - (-1) = -2$: an AP with $d = -2$.", "(iii) $1 - 1 = 0$ but $2 - 1 = 1$: the differences are not equal, so it is not an AP."],
    answer="(i) and (ii) are APs; (iii) is not."),
  b("s2.check", "knowledge_check", question="The common difference of the AP $3, 1, -1, -3, \\ldots$ is:",
    options=["$-2$", "$2$", "$3$", "$-1$"], correct_index=0, explanation="$d = 1 - 3 = -2$. Check: $-1 - 1 = -2$ too."),
 ]},
 {"id": "s3", "title": "The nth term", "blocks": [
  b("s3.discovery", "discovery", title="Spot the pattern",
    body="In the AP $a, a + d, a + 2d, \\ldots$: the 2nd term has one $d$, the 3rd term has two $d$'s, the 4th term has three. So the $n$th term has $(n - 1)$ $d$'s."),
  b("s3.reveal", "theory", title="The nth term formula", revision=True,
    body="The $n$th term (general term) of an AP with first term $a$ and common difference $d$ is\n\n$$a_n = a + (n - 1)d$$\n\n"
         "If the AP has $m$ terms, $a_m$ is the **last term** $l$. The $n$th term **from the end** is $l - (n - 1)d$.\n\n"
         "To check whether a number is a term, solve $a + (n - 1)d = $ number: it is a term only if $n$ comes out as a **positive integer**."),
  b("s3.eg1", "worked_example", title="NCERT example",
    problem="Find the 10th term of the AP $2, 7, 12, \\ldots$",
    steps=["$a = 2$, $d = 7 - 2 = 5$, $n = 10$.", "$a_{10} = 2 + (10 - 1) \\times 5 = 2 + 45$"], answer="$a_{10} = 47$"),
  b("s3.eg2", "worked_example", title="NCERT example: which term?",
    problem="Which term of the AP $21, 18, 15, \\ldots$ is $-81$? Also, is any term $0$?",
    steps=["$a = 21$, $d = -3$. Solve $21 + (n - 1)(-3) = -81$: $(n - 1) = 34$, so $n = 35$.", "For $0$: $21 + (n - 1)(-3) = 0$ gives $n - 1 = 7$, so $n = 8$."],
    answer="$-81$ is the 35th term, and the 8th term is $0$."),
  b("s3.eg3", "worked_example", title="NCERT example: counting with an AP",
    problem="How many two-digit numbers are divisible by 3?",
    steps=["The two-digit multiples of 3 are $12, 15, 18, \\ldots, 99$: an AP with $a = 12$, $d = 3$, $a_n = 99$.", "$12 + (n - 1) \\times 3 = 99$ gives $n - 1 = 29$, so $n = 30$."],
    answer="30 two-digit numbers are divisible by 3."),
  b("s3.eg4", "worked_example", title="NCERT example: from the end",
    problem="Find the 11th term from the last term of the AP $10, 7, 4, \\ldots, -62$.",
    steps=["Reading from the end, the AP is $-62, -59, -56, \\ldots$ with first term $-62$ and $d = 3$.", "11th term from the end $= -62 + (11 - 1) \\times 3 = -62 + 30$"],
    answer="$-32$"),
  b("s3.check", "knowledge_check", question="The 8th term of the AP $1, 5, 9, \\ldots$ is:",
    options=["$29$", "$33$", "$32$", "$36$"], correct_index=0, explanation="$a_8 = 1 + 7 \\times 4 = 29$."),
  b("s3.tip", "teacher_tip", title="Why (n − 1)?",
    body="Ask students to count the 'jumps' between terms on a number line: from the 1st to the 5th term there are 4 jumps, not 5. "
         "This one picture removes the most common error in this chapter. For 'is it a term?' questions, insist that $n$ must be a natural number."),
 ]},
 {"id": "s4", "title": "Sum of the first n terms", "blocks": [
  b("s4.socratic", "socratic_question", question="Gauss paired $1 + 100$, $2 + 99$, $3 + 98$, ... to add 1 to 100. What is special about each pair?",
    options=["Every pair has the same sum, 101", "Every pair has a different sum", "The pairs get bigger each time"], correct_index=0,
    explanation="As the first number goes up by 1, the second goes down by 1, so the pair sum never changes. That is why the sum of an AP is (number of terms ÷ 2) × (first term + last term)."),
  b("s4.reveal", "theory", title="Sum formulas", revision=True,
    body="The sum of the first $n$ terms of an AP is\n\n$$S_n = \\dfrac{n}{2}\\left[2a + (n - 1)d\\right]$$\n\n"
         "If the last term $l$ is known, this becomes\n\n$$S_n = \\dfrac{n}{2}(a + l)$$\n\n"
         "Also, the $n$th term can be found from the sums: $a_n = S_n - S_{n-1}$.\n\n"
         "The sum of the first $n$ positive integers is $\\dfrac{n(n + 1)}{2}$."),
  b("s4.eg1", "worked_example", title="NCERT example",
    problem="Find the sum of the first 22 terms of the AP $8, 3, -2, \\ldots$",
    steps=["$a = 8$, $d = -5$, $n = 22$.", "$S_{22} = \\dfrac{22}{2}\\left[16 + 21 \\times (-5)\\right] = 11 \\times (16 - 105) = 11 \\times (-89)$"],
    answer="$S_{22} = -979$"),
  b("s4.eg2", "worked_example", title="NCERT example: two answers",
    problem="How many terms of the AP $24, 21, 18, \\ldots$ must be taken so that their sum is 78?",
    steps=["$a = 24$, $d = -3$: $\\dfrac{n}{2}\\left[48 - 3(n - 1)\\right] = 78$, i.e. $n^{2} - 17n + 52 = 0$.", "$(n - 4)(n - 13) = 0$, so $n = 4$ or $n = 13$.",
           "Both are valid: the terms from the 5th to the 13th ($12, 9, \\ldots, -12$) add up to 0."],
    answer="4 terms or 13 terms"),
  b("s4.check", "knowledge_check", question="The sum of the first 10 terms of $3, 7, 11, \\ldots$ is:",
    options=["$210$", "$195$", "$420$", "$39$"], correct_index=0, explanation="$S_{10} = \\dfrac{10}{2}(6 + 9 \\times 4) = 5 \\times 42 = 210$."),
  b("s4.memory", "memory_trick", title="Average × count", revision=True,
    body="The sum of an AP $=$ (number of terms) $\\times$ (average of the first and last terms). That is just $S_n = n \\times \\dfrac{a + l}{2}$. "
         "If you remember 'pairs from the ends', you will never forget the formula."),
  b("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Using $a + nd$ instead of $a + (n - 1)d$ for the $n$th term.\n"
         "- Taking $d$ the wrong way round: $d = a_2 - a_1$, not $a_1 - a_2$.\n"
         "- Accepting a fraction or negative value of $n$: the number of terms must be a natural number.\n"
         "- Mixing up $a_n$ (one term) and $S_n$ (the sum of $n$ terms).\n"
         "- Forgetting that 'between 10 and 250' does not include 10 and 250 themselves."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  b("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend, using Gauss's pairing idea, why $1 + 2 + 3 + \\ldots + n = \\dfrac{n(n + 1)}{2}$."),
  b("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 4, Quadratic Equations:** finding how many terms give a certain sum leads to a quadratic equation in $n$.\n"
         "- **Class 11:** geometric progressions, where each term is *multiplied* by a fixed number, and series.\n"
         "- **Commerce:** simple interest grows as an AP, and instalment plans are built from progressions."),
  b("s5.mastery", "mastery", title="Mastery challenge",
    body="Find the sum of all three-digit numbers that are divisible by 7.\n\n"
         "**Answer:** They are $105, 112, \\ldots, 994$. From $105 + (n - 1) \\times 7 = 994$, $n = 128$. "
         "So $S = \\dfrac{128}{2}(105 + 994) = 64 \\times 1099 = 70336$."),
  b("s5.summary", "summary", title="Chapter summary",
    body="- An AP is a list where each term after the first is obtained by adding a fixed number $d$, the common difference.\n"
         "- General form: $a, a + d, a + 2d, \\ldots$\n"
         "- $n$th term: $a_n = a + (n - 1)d$; $n$th term from the end: $l - (n - 1)d$.\n"
         "- Sum of the first $n$ terms: $S_n = \\dfrac{n}{2}\\left[2a + (n - 1)d\\right] = \\dfrac{n}{2}(a + l)$.\n"
         "- $a_n = S_n - S_{n-1}$."),
  b("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Always write $a$, $d$ and $n$ before using a formula.\n"
         "- In 'is it a term?' questions, show the value of $n$ and say clearly whether it is a natural number.\n"
         "- When a quadratic in $n$ gives two values, check both and reject any that is negative or not an integer.\n"
         "- In word problems, write the AP formed by the situation (for example, savings $50, 60, 70, \\ldots$) before calculating."),
  b("s5.flash1", "flashcard", front="What is the nth term of an AP?", back="$a_n = a + (n - 1)d$"),
  b("s5.flash2", "flashcard", front="What is the sum of the first n terms of an AP?", back="$S_n = \\dfrac{n}{2}\\left[2a + (n - 1)d\\right]$, or $\\dfrac{n}{2}(a + l)$ when the last term $l$ is known."),
  b("s5.flash3", "flashcard", front="How do you find a term from the sums?", back="$a_n = S_n - S_{n-1}$"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Arithmetic Progressions",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 5,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: motivation for studying AP, derivation of the nth term and the sum of the first n terms, and their application in solving daily life problems.",
  "concepts": ["arithmetic_progression", "nth_term", "sum_of_ap", "ap_word_problems"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
AP, NT, SUM, WORD = "arithmetic_progression", "nth_term", "sum_of_ap", "ap_word_problems"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch05.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
MS2_TERM = ["1 mark: correct formula with $a$ and $d$", "1 mark: answer"]
MS3_WORD = ["1 mark: identifying the AP ($a$, $d$)", "1 mark: using the correct formula", "1 mark: answer"]
MS2_AP = ["1 mark: checking the differences", "1 mark: conclusion"]

# Exercise 5.1
for p, text, steps in [
 ("i", "The taxi fare after each km when the fare is ₹15 for the first km and ₹8 for each additional km.", ["Fares: $15, 23, 31, 39, \\ldots$", "Each fare is ₹8 more than the previous one, so it is an AP with $d = 8$."]),
 ("ii", "The amount of air present in a cylinder when a vacuum pump removes $\\dfrac{1}{4}$ of the air remaining in the cylinder at a time.", ["Amounts: $V, \\dfrac{3}{4}V, \\dfrac{9}{16}V, \\ldots$", "The differences $\\dfrac{V}{4}$ and $\\dfrac{3V}{16}$ are not equal, so it is not an AP."]),
 ("iii", "The cost of digging a well after every metre of digging, when it costs ₹150 for the first metre and rises by ₹50 for each subsequent metre.", ["Costs: $150, 200, 250, 300, \\ldots$", "Each cost is ₹50 more than the previous one, so it is an AP with $d = 50$."]),
 ("iv", "The amount of money in the account every year, when ₹10000 is deposited at compound interest at 8% per annum.", ["Amounts: $10000, 10800, 11664, \\ldots$", "The differences 800 and 864 are not equal, so it is not an AP."]),
]:
    q(f"ex5_1.q1.{p}", "very_short_answer", 2, [AP], ex("5.1", 1, p), "Does the following list of numbers form an AP? Give a reason. " + text, "easy", answer_steps=steps, marking_scheme=MS2_AP)
for p, a, d in EX51Q2:
    given, terms = EX51Q2_TEX[p]
    q(f"ex5_1.q2.{p}", "very_short_answer", 2, [AP], ex("5.1", 2, p), f"Write the first four terms of the AP when the first term $a$ and the common difference $d$ are: ${given}$.", "easy",
      answer_steps=["$a, \\; a + d, \\; a + 2d, \\; a + 3d$", f"${terms}$"], marking_scheme=["1 mark: method", "1 mark: four terms"])
for p, seq, ans, *_ in EX51Q3:
    q(f"ex5_1.q3.{p}", "very_short_answer", 2, [AP], ex("5.1", 3, p), f"For the AP ${seq}$, write the first term and the common difference.", "easy",
      answer_steps=[f"${ans}$"], marking_scheme=["1 mark: first term", "1 mark: common difference"])
for p, seq, _, yes, no in EX51Q4:
    steps = ([f"${yes[0]}$, the same for every pair of consecutive terms, so it is an AP.", f"Next three terms: ${yes[1]}$"] if yes else
             [f"${no[0]}$ but ${no[1]}$.", "The differences are not equal, so it is not an AP."])
    q(f"ex5_1.q4.{p}", "very_short_answer", 2, [AP], ex("5.1", 4, p), f"Is ${seq}$ an AP? If it is, find the common difference $d$ and write the next three terms.",
      "easy" if p in ("i", "iv", "vii") else "medium", answer_steps=steps, marking_scheme=MS2_AP)
# Exercise 5.2
for p, given, find, ans in [("i", "a = 7, d = 3, n = 8", "a_n", "a_8 = 7 + 7 \\times 3 = 28"), ("ii", "a = -18, n = 10, a_n = 0", "d", "0 = -18 + 9d, \\; d = 2"),
                            ("iii", "d = -3, n = 18, a_n = -5", "a", "-5 = a + 17 \\times (-3), \\; a = 46"), ("iv", "a = -18.9, d = 2.5, a_n = 3.6", "n", "3.6 = -18.9 + (n - 1) \\times 2.5, \\; n = 10"),
                            ("v", "a = 3.5, d = 0, n = 105", "a_n", "a_{105} = 3.5 + 104 \\times 0 = 3.5")]:
    q(f"ex5_2.q1.{p}", "very_short_answer", 2, [NT], ex("5.2", 1, p), f"For an AP, ${given}$. Find ${find}$.", "easy",
      answer_steps=["$a_n = a + (n - 1)d$", f"${ans}$"], marking_scheme=MS2_TERM)
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
mcq("ex5_2.q2.i", [NT], "The 30th term of the AP $10, 7, 4, \\ldots$ is:", ["$97$", "$77$", "$-77$", "$-87$"], 2, "$a_{30} = 10 + 29 \\times (-3) = -77$.", source=ex("5.2", 2, "i"))
mcq("ex5_2.q2.ii", [NT], "The 11th term of the AP $-3, -\\dfrac{1}{2}, 2, \\ldots$ is:", ["$28$", "$22$", "$-38$", "$-48\\dfrac{1}{2}$"], 1,
    "$d = \\dfrac{5}{2}$, so $a_{11} = -3 + 10 \\times \\dfrac{5}{2} = 22$.", source=ex("5.2", 2, "ii"))
for p, seq, steps in [
 ("i", "2, \\square, 26", ["$a_3 = 2 + 2d = 26$, so $d = 12$.", "Missing term: $14$"]),
 ("ii", "\\square, 13, \\square, 3", ["$a_2 = a + d = 13$ and $a_4 = a + 3d = 3$, so $d = -5$, $a = 18$.", "Missing terms: $18$ and $8$"]),
 ("iii", "5, \\square, \\square, 9\\dfrac{1}{2}", ["$a_4 = 5 + 3d = \\dfrac{19}{2}$, so $d = \\dfrac{3}{2}$.", "Missing terms: $6\\dfrac{1}{2}$ and $8$"]),
 ("iv", "-4, \\square, \\square, \\square, \\square, 6", ["$a_6 = -4 + 5d = 6$, so $d = 2$.", "Missing terms: $-2, 0, 2, 4$"]),
 ("v", "\\square, 38, \\square, \\square, \\square, -22", ["$a + d = 38$ and $a + 5d = -22$, so $d = -15$, $a = 53$.", "Missing terms: $53, 23, 8, -7$"]),
]:
    q(f"ex5_2.q3.{p}", "very_short_answer", 2, [NT], ex("5.2", 3, p), f"Fill in the missing terms (shown as $\\square$) in the AP: ${seq}$.", "medium" if p in ("ii", "v") else "easy",
      answer_steps=steps, marking_scheme=["1 mark: finding $d$", "1 mark: missing terms"])
WORD52 = [
 ("q4", 2, "Which term of the AP $3, 8, 13, 18, \\ldots$ is $78$?", ["$3 + (n - 1) \\times 5 = 78$, so $n - 1 = 15$.", "$78$ is the 16th term."]),
 ("q5.i", 2, "Find the number of terms in the AP $7, 13, 19, \\ldots, 205$.", ["$7 + (n - 1) \\times 6 = 205$, so $n - 1 = 33$.", "There are 34 terms."]),
 ("q5.ii", 2, "Find the number of terms in the AP $18, 15\\dfrac{1}{2}, 13, \\ldots, -47$.", ["$d = -\\dfrac{5}{2}$: $18 + (n - 1)\\left(-\\dfrac{5}{2}\\right) = -47$, so $n - 1 = 26$.", "There are 27 terms."]),
 ("q6", 2, "Check whether $-150$ is a term of the AP $11, 8, 5, 2, \\ldots$", ["$11 + (n - 1)(-3) = -150$ gives $n = \\dfrac{164}{3}$.", "$n$ is not a natural number, so $-150$ is not a term."]),
 ("q7", 3, "Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.", ["$a + 10d = 38$ and $a + 15d = 73$.", "Subtracting: $5d = 35$, so $d = 7$ and $a = -32$.", "$a_{31} = -32 + 30 \\times 7 = 178$"]),
 ("q8", 3, "An AP consists of 50 terms of which the 3rd term is 12 and the last term is 106. Find the 29th term.", ["$a + 2d = 12$ and $a + 49d = 106$.", "Subtracting: $47d = 94$, so $d = 2$ and $a = 8$.", "$a_{29} = 8 + 28 \\times 2 = 64$"]),
 ("q9", 3, "If the 3rd and the 9th terms of an AP are 4 and $-8$ respectively, which term of this AP is zero?", ["$a + 2d = 4$ and $a + 8d = -8$, so $d = -2$ and $a = 8$.", "$8 + (n - 1)(-2) = 0$ gives $n - 1 = 4$.", "The 5th term is zero."]),
 ("q10", 2, "The 17th term of an AP exceeds its 10th term by 7. Find the common difference.", ["$a_{17} - a_{10} = (a + 16d) - (a + 9d) = 7d = 7$", "$d = 1$"]),
 ("q11", 3, "Which term of the AP $3, 15, 27, 39, \\ldots$ will be 132 more than its 54th term?", ["$a = 3$, $d = 12$: $a_{54} = 3 + 53 \\times 12 = 639$.", "The required term is $639 + 132 = 771$.", "$3 + (n - 1) \\times 12 = 771$ gives $n = 65$: the 65th term."]),
 ("q12", 3, "Two APs have the same common difference. The difference between their 100th terms is 100. What is the difference between their 1000th terms?", ["Let the first terms be $a$ and $b$, and the common difference $d$.", "$a_{100} - b_{100} = (a + 99d) - (b + 99d) = a - b = 100$.", "$a_{1000} - b_{1000} = a - b = 100$: the difference is always 100."]),
 ("q13", 2, "How many three-digit numbers are divisible by 7?", ["They are $105, 112, \\ldots, 994$: $105 + (n - 1) \\times 7 = 994$, so $n - 1 = 127$.", "128 three-digit numbers are divisible by 7."]),
 ("q14", 2, "How many multiples of 4 lie between 10 and 250?", ["They are $12, 16, \\ldots, 248$: $12 + (n - 1) \\times 4 = 248$, so $n - 1 = 59$.", "60 multiples of 4 lie between 10 and 250."]),
 ("q15", 3, "For what value of $n$ are the $n$th terms of two APs $63, 65, 67, \\ldots$ and $3, 10, 17, \\ldots$ equal?", ["$63 + (n - 1) \\times 2 = 3 + (n - 1) \\times 7$", "$60 = 5(n - 1)$, so $n - 1 = 12$.", "$n = 13$"]),
 ("q16", 3, "Determine the AP whose third term is 16 and the 7th term exceeds the 5th term by 12.", ["$a_7 - a_5 = 2d = 12$, so $d = 6$.", "$a + 2d = 16$ gives $a = 4$.", "The AP is $4, 10, 16, 22, \\ldots$"]),
 ("q17", 2, "Find the 20th term from the last term of the AP $3, 8, 13, \\ldots, 253$.", ["From the end: $l = 253$, $d = -5$.", "20th term from the end $= 253 + 19 \\times (-5) = 158$"]),
 ("q18", 3, "The sum of the 4th and 8th terms of an AP is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms of the AP.", ["$2a + 10d = 24$ and $2a + 14d = 44$.", "Subtracting: $4d = 20$, so $d = 5$ and $a = -13$.", "The first three terms are $-13, -8, -3$."]),
 ("q19", 3, "Subba Rao started work in 1995 at an annual salary of ₹5000 and received an increment of ₹200 each year. In which year did his income reach ₹7000?", ["Salaries form an AP: $5000, 5200, 5400, \\ldots$ with $a = 5000$, $d = 200$.", "$5000 + (n - 1) \\times 200 = 7000$ gives $n = 11$.", "The 11th year of work: his income reached ₹7000 in 2005."]),
 ("q20", 3, "Ramkali saved ₹5 in the first week of a year and then increased her weekly savings by ₹1.75. If in the $n$th week, her weekly savings become ₹20.75, find $n$.", ["Savings form an AP with $a = 5$, $d = 1.75$.", "$5 + (n - 1) \\times 1.75 = 20.75$ gives $n - 1 = 9$.", "$n = 10$"]),
]
for p, marks, text, steps in WORD52:
    num = int(p.split(".")[0][1:]); part = p.split(".")[1] if "." in p else None
    q(f"ex5_2.{p}", "very_short_answer" if marks == 2 else "short_answer", marks, [NT, WORD] if num >= 19 else [NT], ex("5.2", num, part), text,
      "easy" if num in (4, 5, 10) else "medium", answer_steps=steps, marking_scheme=MS2_TERM if marks == 2 else MS3_WORD)
# Exercise 5.3
for p, seq, n, steps in [("i", "2, 7, 12, \\ldots", 10, ["$a = 2$, $d = 5$", "$S_{10} = \\dfrac{10}{2}(4 + 9 \\times 5) = 5 \\times 49 = 245$"]),
                         ("ii", "-37, -33, -29, \\ldots", 12, ["$a = -37$, $d = 4$", "$S_{12} = \\dfrac{12}{2}(-74 + 11 \\times 4) = 6 \\times (-30) = -180$"]),
                         ("iii", "0.6, 1.7, 2.8, \\ldots", 100, ["$a = 0.6$, $d = 1.1$", "$S_{100} = \\dfrac{100}{2}(1.2 + 99 \\times 1.1) = 50 \\times 110.1 = 5505$"]),
                         ("iv", "\\dfrac{1}{15}, \\dfrac{1}{12}, \\dfrac{1}{10}, \\ldots", 11, ["$a = \\dfrac{1}{15}$, $d = \\dfrac{1}{60}$", "$S_{11} = \\dfrac{11}{2}\\left(\\dfrac{2}{15} + \\dfrac{10}{60}\\right) = \\dfrac{11}{2} \\times \\dfrac{3}{10} = \\dfrac{33}{20}$"])]:
    q(f"ex5_3.q1.{p}", "very_short_answer", 2, [SUM], ex("5.3", 1, p), f"Find the sum of the AP ${seq}$ to {n} terms.", "easy" if p in ("i", "ii") else "medium",
      answer_steps=steps, marking_scheme=["1 mark: $a$ and $d$", "1 mark: sum"])
for p, expr, steps in [("i", "7 + 10\\dfrac{1}{2} + 14 + \\ldots + 84", ["$a = 7$, $d = \\dfrac{7}{2}$: $7 + (n - 1)\\dfrac{7}{2} = 84$ gives $n = 23$.", "$S_{23} = \\dfrac{23}{2}(7 + 84) = \\dfrac{2093}{2} = 1046\\dfrac{1}{2}$"]),
                       ("ii", "34 + 32 + 30 + \\ldots + 10", ["$a = 34$, $d = -2$: $34 + (n - 1)(-2) = 10$ gives $n = 13$.", "$S_{13} = \\dfrac{13}{2}(34 + 10) = 286$"]),
                       ("iii", "-5 + (-8) + (-11) + \\ldots + (-230)", ["$a = -5$, $d = -3$: $-5 + (n - 1)(-3) = -230$ gives $n = 76$.", "$S_{76} = \\dfrac{76}{2}(-5 - 230) = 38 \\times (-235) = -8930$"])]:
    q(f"ex5_3.q2.{p}", "short_answer", 3, [SUM, NT], ex("5.3", 2, p), f"Find the sum ${expr}$.", answer_steps=steps,
      marking_scheme=["1 mark: $a$ and $d$", "1 mark: number of terms", "1 mark: sum"])
for p, given, find, steps in [
 ("i", "a = 5, d = 3, a_n = 50", "n, S_n", ["$5 + (n - 1) \\times 3 = 50$, so $n = 16$.", "$S_{16} = \\dfrac{16}{2}(5 + 50) = 440$"]),
 ("ii", "a = 7, a_{13} = 35", "d, S_{13}", ["$7 + 12d = 35$, so $d = \\dfrac{7}{3}$.", "$S_{13} = \\dfrac{13}{2}(7 + 35) = 273$"]),
 ("iii", "a_{12} = 37, d = 3", "a, S_{12}", ["$a + 11 \\times 3 = 37$, so $a = 4$.", "$S_{12} = \\dfrac{12}{2}(4 + 37) = 246$"]),
 ("iv", "a_3 = 15, S_{10} = 125", "d, a_{10}", ["$a + 2d = 15$ and $5(2a + 9d) = 125$, i.e. $2a + 9d = 25$.", "So $d = -1$, $a = 17$, and $a_{10} = 17 + 9 \\times (-1) = 8$."]),
 ("v", "d = 5, S_9 = 75", "a, a_9", ["$\\dfrac{9}{2}(2a + 40) = 75$, so $a = -\\dfrac{35}{3}$.", "$a_9 = -\\dfrac{35}{3} + 8 \\times 5 = \\dfrac{85}{3}$"]),
 ("vi", "a = 2, d = 8, S_n = 90", "n, a_n", ["$\\dfrac{n}{2}\\left[4 + 8(n - 1)\\right] = 90$, i.e. $2n^{2} - n - 45 = 0$, so $(n - 5)(2n + 9) = 0$ and $n = 5$.", "$a_5 = 2 + 4 \\times 8 = 34$"]),
 ("vii", "a = 8, a_n = 62, S_n = 210", "n, d", ["$\\dfrac{n}{2}(8 + 62) = 210$, so $n = 6$.", "$8 + 5d = 62$, so $d = \\dfrac{54}{5}$."]),
 ("viii", "a_n = 4, d = 2, S_n = -14", "n, a", ["$a = 4 - 2(n - 1)$ and $\\dfrac{n}{2}(a + 4) = -14$ give $n^{2} - 5n - 14 = 0$, so $n = 7$.", "$a = 4 - 2 \\times 6 = -8$"]),
 ("ix", "a = 3, n = 8, S = 192", "d", ["$\\dfrac{8}{2}(6 + 7d) = 192$, so $6 + 7d = 48$.", "$d = 6$"]),
 ("x", "l = 28, S = 144, n = 9", "a", ["$\\dfrac{9}{2}(a + 28) = 144$, so $a + 28 = 32$.", "$a = 4$"]),
]:
    q(f"ex5_3.q3.{p}", "short_answer", 3, [SUM, NT], ex("5.3", 3, p), f"In an AP, given ${given}$, find ${find}$.", "hard" if p in ("vi", "viii") else "medium",
      answer_steps=steps, marking_scheme=["1 mark: correct formula", "1 mark: first unknown", "1 mark: second unknown"])
WORD53 = [
 ("q4", 3, "How many terms of the AP $9, 17, 25, \\ldots$ must be taken to give a sum of 636?", ["$\\dfrac{n}{2}\\left[18 + 8(n - 1)\\right] = 636$, i.e. $4n^{2} + 5n - 636 = 0$.", "$(n - 12)(4n + 53) = 0$, so $n = 12$ ($n$ must be a natural number).", "12 terms"]),
 ("q5", 3, "The first term of an AP is 5, the last term is 45 and the sum is 400. Find the number of terms and the common difference.", ["$\\dfrac{n}{2}(5 + 45) = 400$, so $n = 16$.", "$5 + 15d = 45$, so $d = \\dfrac{8}{3}$.", "16 terms, $d = \\dfrac{8}{3}$"]),
 ("q6", 3, "The first and the last terms of an AP are 17 and 350 respectively. If the common difference is 9, how many terms are there and what is their sum?", ["$17 + (n - 1) \\times 9 = 350$, so $n = 38$.", "$S_{38} = \\dfrac{38}{2}(17 + 350) = 19 \\times 367$", "38 terms with sum 6973"]),
 ("q7", 3, "Find the sum of the first 22 terms of an AP in which $d = 7$ and the 22nd term is 149.", ["$a + 21 \\times 7 = 149$, so $a = 2$.", "$S_{22} = \\dfrac{22}{2}(2 + 149) = 11 \\times 151$", "$S_{22} = 1661$"]),
 ("q8", 3, "Find the sum of the first 51 terms of an AP whose second and third terms are 14 and 18 respectively.", ["$d = 18 - 14 = 4$ and $a = 14 - 4 = 10$.", "$S_{51} = \\dfrac{51}{2}(20 + 50 \\times 4) = 51 \\times 110$", "$S_{51} = 5610$"]),
 ("q9", 3, "If the sum of the first 7 terms of an AP is 49 and that of 17 terms is 289, find the sum of the first $n$ terms.", ["$\\dfrac{7}{2}(2a + 6d) = 49$ gives $a + 3d = 7$; $\\dfrac{17}{2}(2a + 16d) = 289$ gives $a + 8d = 17$.", "So $d = 2$ and $a = 1$.", "$S_n = \\dfrac{n}{2}\\left[2 + 2(n - 1)\\right] = n^{2}$"]),
 ("q10.i", 3, "Show that $a_1, a_2, \\ldots, a_n, \\ldots$ form an AP where $a_n = 3 + 4n$. Also find the sum of the first 15 terms.", ["$a_{n+1} - a_n = 4$, a constant, so it is an AP with $a_1 = 7$, $d = 4$.", "$a_{15} = 63$", "$S_{15} = \\dfrac{15}{2}(7 + 63) = 525$"]),
 ("q10.ii", 3, "Show that $a_1, a_2, \\ldots, a_n, \\ldots$ form an AP where $a_n = 9 - 5n$. Also find the sum of the first 15 terms.", ["$a_{n+1} - a_n = -5$, a constant, so it is an AP with $a_1 = 4$, $d = -5$.", "$a_{15} = -66$", "$S_{15} = \\dfrac{15}{2}(4 - 66) = -465$"]),
 ("q11", 3, "If the sum of the first $n$ terms of an AP is $4n - n^{2}$, what is the first term? What is the sum of the first two terms? What is the second term? Similarly, find the 3rd, the 10th and the $n$th terms.",
  ["$a_1 = S_1 = 3$; $S_2 = 4$, so $a_2 = 1$; $S_3 = 3$, so $a_3 = -1$.", "$a_{10} = S_{10} - S_9 = -60 - (-45) = -15$", "$a_n = S_n - S_{n-1} = 5 - 2n$"]),
 ("q12", 2, "Find the sum of the first 40 positive integers divisible by 6.", ["They are $6, 12, \\ldots, 240$.", "$S_{40} = \\dfrac{40}{2}(6 + 240) = 4920$"]),
 ("q13", 2, "Find the sum of the first 15 multiples of 8.", ["They are $8, 16, \\ldots, 120$.", "$S_{15} = \\dfrac{15}{2}(8 + 120) = 960$"]),
 ("q14", 2, "Find the sum of the odd numbers between 0 and 50.", ["They are $1, 3, \\ldots, 49$: 25 terms.", "$S_{25} = \\dfrac{25}{2}(1 + 49) = 625$"]),
 ("q15", 3, "A contract on construction job specifies a penalty for delay of completion beyond a certain date as follows: ₹200 for the first day, ₹250 for the second day, ₹300 for the third day, etc., the penalty for each succeeding day being ₹50 more than for the preceding day. How much money does the contractor have to pay as penalty, if he has delayed the work by 30 days?",
  ["The penalties form an AP with $a = 200$, $d = 50$, $n = 30$.", "$S_{30} = \\dfrac{30}{2}(400 + 29 \\times 50) = 15 \\times 1850$", "The penalty is ₹27750."]),
 ("q16", 3, "A sum of ₹700 is to be used to give seven cash prizes to students of a school for their overall academic performance. If each prize is ₹20 less than its preceding prize, find the value of each of the prizes.",
  ["The prizes form an AP with $d = -20$, $n = 7$: $\\dfrac{7}{2}(2a - 120) = 700$.", "$2a - 120 = 200$, so $a = 160$.", "The prizes are ₹160, ₹140, ₹120, ₹100, ₹80, ₹60 and ₹40."]),
 ("q17", 3, "In a school, students thought of planting trees in and around the school to reduce air pollution. It was decided that the number of trees that each section of each class will plant will be the same as the class in which they are studying, e.g., a section of Class I will plant 1 tree, a section of Class II will plant 2 trees and so on till Class XII. There are three sections of each class. How many trees will be planted by the students?",
  ["Trees by the classes: $3, 6, 9, \\ldots, 36$ (three sections each).", "This is an AP with $a = 3$, $d = 3$, $n = 12$.", "$S_{12} = \\dfrac{12}{2}(3 + 36) = 234$ trees"]),
 ("q18", 3, "A spiral is made up of successive semicircles, with centres alternately at A and B, starting with centre at A, of radii 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... What is the total length of such a spiral made up of thirteen consecutive semicircles? (Take $\\pi = \\dfrac{22}{7}$)",
  ["The length of a semicircle of radius $r$ is $\\pi r$, so the lengths are $\\pi(0.5), \\pi(1.0), \\pi(1.5), \\ldots$, 13 terms.", "Total $= \\pi \\times \\dfrac{13}{2}(0.5 + 6.5) = \\dfrac{22}{7} \\times 45.5$", "The total length is 143 cm."]),
 ("q19", 3, "200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next row, 18 in the row next to it and so on. In how many rows are the 200 logs placed and how many logs are in the top row?",
  ["$\\dfrac{n}{2}\\left[40 - (n - 1)\\right] = 200$, i.e. $n^{2} - 41n + 400 = 0$, so $n = 16$ or $n = 25$.", "For $n = 25$ the top row would have $20 - 24 = -4$ logs, which is impossible, so $n = 16$.", "16 rows, with $20 - 15 = 5$ logs in the top row."]),
 ("q20", 3, "In a potato race, a bucket is placed at the starting point, which is 5 m from the first potato, and the other potatoes are placed 3 m apart in a straight line. There are ten potatoes in the line. A competitor starts from the bucket, picks up the nearest potato, runs back with it, drops it in the bucket, runs back to pick up the next potato, runs to the bucket to drop it in, and she continues in the same way until all the potatoes are in the bucket. What is the total distance the competitor has to run?",
  ["The potatoes are $5, 8, 11, \\ldots$ m from the bucket: 10 terms.", "For each potato she runs there and back: total $= 2 \\times \\dfrac{10}{2}(5 + 32) = 2 \\times 185$", "The total distance is 370 m."]),
]
for p, marks, text, steps in WORD53:
    num = int(p.split(".")[0][1:]); part = p.split(".")[1] if "." in p else None
    q(f"ex5_3.{p}", "very_short_answer" if marks == 2 else "short_answer", marks, [SUM, WORD] if num >= 15 else [SUM], ex("5.3", num, part), text,
      "hard" if num in (11, 18, 19, 20) else "medium", answer_steps=steps, marking_scheme=["1 mark: identifying the AP", "1 mark: sum"] if marks == 2 else MS3_WORD)
# NCERT examples
q("eg_div3", "very_short_answer", 2, [NT, WORD], {"kind": "ncert_example"}, "How many two-digit numbers are divisible by 3?", "easy",
  answer_steps=["They are $12, 15, \\ldots, 99$: $12 + (n - 1) \\times 3 = 99$, so $n - 1 = 29$.", "30 two-digit numbers are divisible by 3."], marking_scheme=MS2_TERM)
q("eg_from_last", "very_short_answer", 2, [NT], {"kind": "ncert_example"}, "Find the 11th term from the last term (towards the first term) of the AP $10, 7, 4, \\ldots, -62$.",
  answer_steps=["From the end: first term $-62$, $d = 3$.", "11th term from the end $= -62 + 10 \\times 3 = -32$"], marking_scheme=MS2_TERM)
q("eg_78", "short_answer", 3, [SUM], {"kind": "ncert_example"}, "How many terms of the AP $24, 21, 18, \\ldots$ must be taken so that their sum is 78?", "hard",
  answer_steps=["$\\dfrac{n}{2}\\left[48 - 3(n - 1)\\right] = 78$, i.e. $n^{2} - 17n + 52 = 0$.", "$(n - 4)(n - 13) = 0$, so $n = 4$ or $n = 13$.", "Both are valid (terms 5 to 13 add up to 0): 4 or 13 terms."],
  marking_scheme=["1 mark: equation", "1 mark: both roots", "1 mark: conclusion"])
# Shine MCQs
mcq("mcq01", [AP], "The common difference of the AP $3, 7, 11, 15, \\ldots$ is:", ["$4$", "$-4$", "$3$", "$\\dfrac{7}{3}$"], 0, "$d = 7 - 3 = 4$.")
mcq("mcq02", [NT], "The 10th term of the AP $5, 9, 13, \\ldots$ is:", ["$41$", "$45$", "$37$", "$50$"], 0, "$a_{10} = 5 + 9 \\times 4 = 41$.")
mcq("mcq03", [AP], "Which of the following is an AP?", ["$-3, -1, 1, 3, \\ldots$", "$1, 4, 9, 16, \\ldots$", "$2, 4, 8, 16, \\ldots$", "$1, -1, 1, -1, \\ldots$"], 0,
    "Only $-3, -1, 1, 3, \\ldots$ has a constant difference, $2$.")
mcq("mcq04", [SUM], "The sum of the first 20 odd natural numbers is:", ["$400$", "$200$", "$420$", "$441$"], 0, "$S_{20} = \\dfrac{20}{2}(2 + 19 \\times 2) = 400$, or simply $20^{2}$.", "medium")
mcq("mcq05", [AP], "If $2x$, $x + 10$ and $3x + 2$ are in AP, then $x$ is:", ["$6$", "$4$", "$5$", "$8$"], 0, "The middle term is the average: $2(x + 10) = 2x + 3x + 2$, so $x = 6$.", "medium")
mcq("mcq06", [NT], "The $n$th term of the AP $7, 4, 1, -2, \\ldots$ is:", ["$10 - 3n$", "$7 - 3n$", "$3n + 4$", "$4 - 3n$"], 0, "$a_n = 7 + (n - 1)(-3) = 10 - 3n$.", "medium")
mcq("mcq07", [SUM], "If the sum of the first $n$ terms of an AP is $n^{2}$, then its 5th term is:", ["$9$", "$25$", "$16$", "$10$"], 0, "$a_5 = S_5 - S_4 = 25 - 16 = 9$.", "medium")
mcq("mcq08", [NT], "The number of terms in the AP $7, 11, 15, \\ldots, 139$ is:", ["$34$", "$33$", "$35$", "$32$"], 0, "$7 + (n - 1) \\times 4 = 139$ gives $n = 34$.")
mcq("mcq09", [NT], "The 15th term from the end of the AP $3, 6, 9, \\ldots, 99$ is:", ["$57$", "$45$", "$54$", "$60$"], 0, "From the end: $99 + 14 \\times (-3) = 57$.", "medium")
mcq("mcq10", [AP], "The AP with first term $-5$ and common difference $0$ is:", ["$-5, -5, -5, \\ldots$", "$-5, 0, 5, \\ldots$", "$0, -5, -10, \\ldots$", "$-5, -10, -15, \\ldots$"], 0, "Adding 0 each time keeps every term equal to $-5$.")
mcq("mcq11", [AP], "If $a_n = 2n + 3$, the common difference of the AP is:", ["$2$", "$3$", "$5$", "$2n$"], 0, "$a_{n+1} - a_n = 2$.")
mcq("mcq12", [SUM], "The sum $1 + 2 + 3 + \\ldots + 100$ is:", ["$5050$", "$5000$", "$10100$", "$5100$"], 0, "$\\dfrac{100 \\times 101}{2} = 5050$.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [AP], "$3, 7, 11, 15, \\ldots$ is an AP with common difference 4.", "In an AP, the difference between consecutive terms is constant.", 0,
   "Every difference is 4, which is exactly what makes it an AP.")
ar("ar2", [NT], "$301$ is not a term of the AP $5, 11, 17, 23, \\ldots$", "Every term of this AP leaves remainder 5 when divided by 6.", 0,
   "$301 = 6 \\times 50 + 1$ leaves remainder 1, so it cannot be a term, exactly as the reason says.")
ar("ar3", [SUM], "The sum of the first 10 terms of the AP $2, 4, 6, \\ldots$ is 100.", "For this AP, $S_n = n(n + 1)$.", 3,
   "A is false: $S_{10} = 10 \\times 11 = 110$. R is true.")
ar("ar4", [NT], "The 10th term of the AP $5, 8, 11, \\ldots$ is 32.", "The common difference of an AP is always positive.", 2,
   "A is true: $5 + 9 \\times 3 = 32$. R is false: $d$ can be negative or zero.")
ar("ar5", [SUM], "If $S_n = n^{2}$, then the first term is 1.", "The sum of the first $n$ odd numbers is $n^{2}$.", 1,
   "A is true because $a_1 = S_1 = 1$. R is true, but A follows from $a_1 = S_1$, not from R.")

q("vsa1", "very_short_answer", 2, [NT], SHINE, "Find the 20th term of the AP $5, 2, -1, \\ldots$", "easy",
  answer_steps=["$a = 5$, $d = -3$", "$a_{20} = 5 + 19 \\times (-3) = -52$"], marking_scheme=MS2_TERM)
q("vsa2", "very_short_answer", 2, [NT], SHINE, "Is $184$ a term of the AP $3, 7, 11, \\ldots$? Justify.",
  answer_steps=["$3 + (n - 1) \\times 4 = 184$ gives $n = \\dfrac{185}{4}$.", "$n$ is not a natural number, so $184$ is not a term."], marking_scheme=MS2_TERM)
q("sqp21a", "very_short_answer", 2, [SUM], SQP("21(A)"), "The AP $8, 10, 12, \\ldots$ has 60 terms. Find the sum of its last 10 terms.",
  answer_steps=["$a_{51} = 8 + 50 \\times 2 = 108$ and $a_{60} = 8 + 59 \\times 2 = 126$.", "Sum of the last 10 terms $= \\dfrac{10}{2}(108 + 126) = 1170$"],
  marking_scheme=["1 mark: $a_{51}$ and $a_{60}$", "1 mark: sum"])
q("sqp21b", "very_short_answer", 2, [NT], SQP("21(B)"), "Find the middle term of the AP $6, 13, 20, \\ldots, 230$.",
  answer_steps=["$6 + (n - 1) \\times 7 = 230$ gives $n = 33$, so the middle term is the 17th.", "$a_{17} = 6 + 16 \\times 7 = 118$"],
  marking_scheme=["1 mark: number of terms", "1 mark: middle term"])
q("sa1", "short_answer", 3, [SUM, NT], SHINE, "Find the sum of all multiples of 9 lying between 300 and 700.", "medium",
  answer_steps=["They are $306, 315, \\ldots, 693$: $306 + (n - 1) \\times 9 = 693$ gives $n = 44$.", "$S_{44} = \\dfrac{44}{2}(306 + 693) = 22 \\times 999$", "$= 21978$"], marking_scheme=MS3_WORD)
q("sa2", "short_answer", 3, [NT], SHINE, "The 7th term of an AP is $\\dfrac{1}{9}$ and its 9th term is $\\dfrac{1}{7}$. Find its 63rd term.", "hard",
  answer_steps=["$a + 6d = \\dfrac{1}{9}$ and $a + 8d = \\dfrac{1}{7}$, so $2d = \\dfrac{2}{63}$ and $d = \\dfrac{1}{63}$.", "$a = \\dfrac{1}{9} - \\dfrac{6}{63} = \\dfrac{1}{63}$", "$a_{63} = \\dfrac{1}{63} + 62 \\times \\dfrac{1}{63} = 1$"],
  marking_scheme=["1 mark: $d$", "1 mark: $a$", "1 mark: $a_{63}$"])
q("sa3", "short_answer", 3, [SUM], SHINE, "How many terms of the AP $54, 51, 48, \\ldots$ must be taken so that their sum is 513? Explain the double answer.", "hard",
  answer_steps=["$\\dfrac{n}{2}\\left[108 - 3(n - 1)\\right] = 513$, i.e. $n^{2} - 37n + 342 = 0$.", "$(n - 18)(n - 19) = 0$, so $n = 18$ or $n = 19$.", "Both work because the 19th term is $54 + 18 \\times (-3) = 0$."],
  marking_scheme=["1 mark: equation", "1 mark: both values", "1 mark: explanation"])
q("sa4", "short_answer", 3, [SUM, NT], SHINE, "The sum of the first $n$ terms of an AP is $3n^{2} + 5n$. Find the AP and its 20th term.", "medium",
  answer_steps=["$a_1 = S_1 = 8$ and $S_2 = 22$, so $a_2 = 14$ and $d = 6$.", "The AP is $8, 14, 20, \\ldots$", "$a_{20} = 8 + 19 \\times 6 = 122$"],
  marking_scheme=["1 mark: first two terms", "1 mark: AP", "1 mark: 20th term"])
q("la1", "long_answer", 5, [SUM, WORD], SHINE, "A man saved ₹16500 in ten years. In each year after the first, he saved ₹100 more than he did in the preceding year. (i) How much did he save in the first year? (ii) How much did he save in the tenth year? (iii) In which year did he save ₹1700?", "medium",
  answer_steps=["The savings form an AP with $d = 100$, $n = 10$, $S_{10} = 16500$.", "$\\dfrac{10}{2}(2a + 900) = 16500$, so $2a + 900 = 3300$.", "(i) $a = 1200$: ₹1200 in the first year.",
                "(ii) $a_{10} = 1200 + 9 \\times 100 = 2100$: ₹2100.", "(iii) $1200 + (n - 1) \\times 100 = 1700$ gives $n = 6$: the 6th year."],
  marking_scheme=["1 mark: identifying the AP", "1 mark: equation", "1 mark: first year", "1 mark: tenth year", "1 mark: year with ₹1700"])
q("la2", "long_answer", 5, [NT, SUM], SHINE, "The ratio of the 11th term to the 18th term of an AP is $2 : 3$. Find the ratio of the 5th term to the 21st term, and also the ratio of the sum of the first five terms to the sum of the first 21 terms.", "hard",
  answer_steps=["$\\dfrac{a + 10d}{a + 17d} = \\dfrac{2}{3}$ gives $3a + 30d = 2a + 34d$, so $a = 4d$.", "$a_5 = a + 4d = 8d$ and $a_{21} = a + 20d = 24d$, so $a_5 : a_{21} = 1 : 3$.",
                "$S_5 = \\dfrac{5}{2}(8d + 4d) = 30d$", "$S_{21} = \\dfrac{21}{2}(8d + 20d) = 294d$", "$S_5 : S_{21} = 30 : 294 = 5 : 49$"],
  marking_scheme=["1 mark: $a = 4d$", "1 mark: $a_5 : a_{21}$", "1 mark: $S_5$", "1 mark: $S_{21}$", "1 mark: ratio of sums"])
q("cb1", "case_based", 4, [NT, SUM, WORD], SHINE,
  "In a school auditorium, the first row has 20 seats, and each row after that has 2 more seats than the row in front of it. There are 30 rows.\n\n(i) How many seats are there in the 10th row? (1)\n\n(ii) How many seats are there in the last row? (1)\n\n(iii) Find the total number of seats in the auditorium. OR Which row has 50 seats? (2)",
  answer_steps=["(i) $a_{10} = 20 + 9 \\times 2 = 38$", "(ii) $a_{30} = 20 + 29 \\times 2 = 78$", "(iii) $S_{30} = \\dfrac{30}{2}(20 + 78) = 1470$ seats. OR $20 + (n - 1) \\times 2 = 50$ gives $n = 16$: the 16th row."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [NT, SUM, WORD], SHINE,
  "Rahul wants to buy a bicycle. He saves ₹50 in the first week and increases his saving by ₹10 every week.\n\n(i) How much does he save in the 8th week? (1)\n\n(ii) How much has he saved in total after 8 weeks? (1)\n\n(iii) In which week will his weekly saving be ₹200? OR In how many weeks will his total savings be ₹2900? (2)",
  answer_steps=["(i) $a_8 = 50 + 7 \\times 10 = 120$: ₹120", "(ii) $S_8 = \\dfrac{8}{2}(50 + 120) = 680$: ₹680",
                "(iii) $50 + (n - 1) \\times 10 = 200$ gives $n = 16$: the 16th week. OR $\\dfrac{n}{2}\\left[100 + 10(n - 1)\\right] = 2900$ gives $n^{2} + 9n - 580 = 0$, so $n = 20$ weeks."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("sqp36", "case_based", 4, [AP, NT, SUM], SQP(36),
  "In a class, the teacher asks every student to write an example of an AP. Two boys, Aryan and Roshan, write the progressions $-5, -2, 1, 4, \\ldots$ and $187, 184, 181, \\ldots$ respectively.\n\n(i) Find the sum of the common differences of the two progressions. (1)\n\n(ii) Find the 34th term of the progression written by Roshan. (1)\n\n(iii) Find the sum of the first 10 terms of the progression written by Aryan. OR Which term of the two progressions will have the same value? (2)",
  answer_steps=["(i) The common differences are $3$ and $-3$; their sum is $0$.", "(ii) $a_{34} = 187 + 33 \\times (-3) = 88$",
                "(iii) $S_{10} = \\dfrac{10}{2}\\left[2(-5) + 9 \\times 3\\right] = 85$. OR $-5 + (n - 1) \\times 3 = 187 + (n - 1)(-3)$ gives $6(n - 1) = 192$, so the 33rd terms are equal."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch05.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
