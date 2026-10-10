"""Builds CBSE Class 10 Maths Ch 1 (Real Numbers) in the new content format.

Every number used in an answer is recomputed here with sympy; the script
aborts if any stated answer is wrong.
"""
import json, os, sys
from math import gcd
from functools import reduce
from sympy import factorint, sqrt, Rational, nsimplify, isprime

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch01"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch01_real_numbers"

def hcf(*n): return reduce(gcd, n)
def lcm(*n): return reduce(lambda a, b: a * b // gcd(a, b), n)
def tex_factor(n):
    f = factorint(n)
    return r" \times ".join(f"{p}^{{{e}}}" if e > 1 else f"{p}" for p, e in sorted(f.items()))
def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)

# ---------------------------------------------------------------- verifications
for n, s in [(140, "2^{2} \\times 5 \\times 7"), (156, "2^{2} \\times 3 \\times 13"), (3825, "3^{2} \\times 5^{2} \\times 17"),
             (5005, "5 \\times 7 \\times 11 \\times 13"), (7429, "17 \\times 19 \\times 23"), (96, "2^{5} \\times 3"),
             (404, "2^{2} \\times 101"), (72, "2^{3} \\times 3^{2}"), (120, "2^{3} \\times 3 \\times 5"),
             (26, "2 \\times 13"), (91, "7 \\times 13"), (510, "2 \\times 3 \\times 5 \\times 17"), (92, "2^{2} \\times 23"),
             (336, "2^{4} \\times 3 \\times 7"), (54, "2 \\times 3^{3}"), (144, "2^{4} \\times 3^{2}"), (420, "2^{2} \\times 3 \\times 5 \\times 7"),
             (130, "2 \\times 5 \\times 13"), (1014, "2 \\times 3 \\times 13^{2}"), (5045, "5 \\times 1009")]:
    check(tex_factor(n) == s, f"{n} = {tex_factor(n)} not {s}")
check(isprime(1009), "1009 prime")
for a, b, h, l in [(26, 91, 13, 182), (510, 92, 2, 23460), (336, 54, 6, 3024), (6, 20, 2, 60), (96, 404, 4, 9696), (120, 144, 24, 720),
                   (420, 130, 10, 5460), (18, 12, 6, 36)]:
    check(hcf(a, b) == h and lcm(a, b) == l and h * l == a * b, f"hcf/lcm {a},{b}")
check(hcf(12, 15, 21) == 3 and lcm(12, 15, 21) == 420, "12,15,21")
check(hcf(17, 23, 29) == 1 and lcm(17, 23, 29) == 11339, "17,23,29")
check(hcf(8, 9, 25) == 1 and lcm(8, 9, 25) == 1800, "8,9,25")
check(hcf(6, 72, 120) == 6 and lcm(6, 72, 120) == 360, "6,72,120")
check(306 * 657 // 9 == 22338 and hcf(306, 657) == 9, "306,657")
check(7 * 11 * 13 + 13 == 1014 and 7 * 6 * 5 * 4 * 3 * 2 * 1 + 5 == 5045, "composites")
p, q = 2**3 * 3**2 * 5, 2**2 * 3**3 * 7
check(hcf(p, q) == 36 and lcm(p, q) == 7560, "2^3 3^2 5 vs 2^2 3^3 7")
check(lcm(10, 4) == 20 and hcf(2, 4) == 2, "smallest composites")
check(factorint(144)[2] == 4, "exponent of 2 in 144")
check((3 + sqrt(5)) * (3 - sqrt(5)) == 4 or nsimplify((3 + sqrt(5)) * (3 - sqrt(5))) == 4, "(3+√5)(3-√5)")
check(hcf(240, 1024) == 16, "245,1029 remainder 5")
check(lcm(12, 16, 24, 36) == 144, "lcm 12,16,24,36")
check(lcm(9, 12, 15) == 180, "bells")
check(hcf(60, 84, 108) == 12 and (60 + 84 + 108) // 12 == 21, "seminar rooms")
check(lcm(12, 18) == 36 and lcm(12, 18, 15) == 180, "track")
check(3 * 5 * 7 + 7 == 112 == 7 * 16, "3x5x7+7")
check(1215 // 9 == 135 and hcf(9, 135) == 9 and lcm(9, 135) == 135 and 9 * 135 == 1215, "AR hcf 9 product 1215")
check(12 * 240 == 2880 and hcf(48, 60) == 12 and lcm(48, 60) == 240, "hcf 12 lcm 240")
check(4 ** 3 == 64 and sqrt(Rational(36, 25)) == Rational(6, 5), "sqrt checks")
check(hcf(6, 72, 120) * lcm(6, 72, 120) == 2160 != 6 * 72 * 120 == 51840, "3-number product rule fails")

# ---------------------------------------------------------------- learn content
def b(id_, type_, **kw): return {"id": f"ch01.{id_}", "type": type_, **kw}

sections = [
 {"id": "s1", "title": "Why real numbers?", "blocks": [
  b("s1.hook", "hook", title="The secret code inside every number",
    body="A bank locker opens only with the right combination. Numbers work the same way. "
         "Every whole number bigger than 1 is built from a few **prime numbers**, multiplied together, "
         "and each number has **exactly one** such combination.\n\n"
         "In this chapter you will learn to read that code, use it to find HCF and LCM quickly, "
         "and prove that numbers like $\\sqrt{2}$ can never be written as a fraction."),
  b("s1.socratic", "socratic_question",
    question="Riya writes $12 = 2 \\times 6$, Aman writes $12 = 3 \\times 4$, and Neha writes $12 = 2 \\times 2 \\times 3$. "
             "If everyone keeps breaking their factors until only primes are left, what will happen?",
    options=["Everyone ends with the same primes: $2 \\times 2 \\times 3$",
             "Everyone ends with different primes",
             "It depends on where you start"],
    correct_index=0,
    explanation="Break $6 = 2 \\times 3$ and $4 = 2 \\times 2$. All three reach $2 \\times 2 \\times 3$. "
                "Only the order can change. Keep this idea in mind: it is the heart of this chapter.",
    feedback_incorrect="Try it: break 6 and 4 into primes and compare with Neha's answer."),
 ]},
 {"id": "s2", "title": "The Fundamental Theorem of Arithmetic", "blocks": [
  b("s2.discovery", "discovery", title="Build a factor tree",
    body="Take 140. Split it into any two factors, then keep splitting until every branch ends in a prime.\n\n"
         "$140 = 2 \\times 70$, $70 = 2 \\times 35$, $35 = 5 \\times 7$.\n\n"
         "The primes at the ends of the branches are $2, 2, 5, 7$. So $140 = 2^{2} \\times 5 \\times 7$.\n\n"
         "Now start differently: $140 = 10 \\times 14 = (2 \\times 5) \\times (2 \\times 7)$. Same primes! Watch the tree below grow."),
  b("s2.tree", "factor_tree", number=140, title="Factor tree of 140"),
  b("s2.reveal", "theory", title="Theorem 1.1: The Fundamental Theorem of Arithmetic",
    body="**Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, "
         "apart from the order in which the prime factors occur.**\n\n"
         "In general, a composite number $x$ can be written as\n\n"
         "$$x = p_1 \\, p_2 \\, p_3 \\cdots p_n$$\n\n"
         "where $p_1, p_2, \\ldots, p_n$ are primes written in ascending order. Collecting equal primes gives powers, "
         "for example $32760 = 2^{3} \\times 3^{2} \\times 5 \\times 7 \\times 13$.\n\n"
         "- **Prime number:** has exactly two factors, 1 and itself (2, 3, 5, 7, 11, ...).\n"
         "- **Composite number:** has more than two factors (4, 6, 8, 9, ...).\n"
         "- **1 is neither prime nor composite.**"),
  b("s2.ex1", "worked_example", title="NCERT Example 1",
    problem="Consider the numbers $4^{n}$, where $n$ is a natural number. Check whether there is any value of $n$ for which $4^{n}$ ends with the digit zero.",
    steps=["A number ends with 0 only if it is divisible by 10, that is, by both 2 and 5.",
           "So the prime factorisation of $4^{n}$ would have to contain the prime 5.",
           "But $4^{n} = (2^{2})^{n} = 2^{2n}$. The only prime in its factorisation is 2.",
           "By the uniqueness in the Fundamental Theorem of Arithmetic, no other prime can appear, so 5 is never a factor."],
    answer="There is no natural number $n$ for which $4^{n}$ ends with the digit 0."),
  b("s2.check", "knowledge_check",
    question="Which is the prime factorisation of 156?",
    options=["$2^{2} \\times 3 \\times 13$", "$2 \\times 78$", "$4 \\times 3 \\times 13$", "$2^{2} \\times 39$"],
    correct_index=0,
    explanation="$156 = 2 \\times 78 = 2 \\times 2 \\times 39 = 2 \\times 2 \\times 3 \\times 13 = 2^{2} \\times 3 \\times 13$. "
                "The other options still contain composite factors (78, 4, 39)."),
  b("s2.tip", "teacher_tip", title="Teaching the factor tree",
    body="Ask three students to factorise the same number starting from different pairs, on the board at the same time. "
         "When all three trees end with the same primes, students *see* uniqueness instead of memorising it. "
         "Always ask them to write the final answer with primes in ascending order and powers."),
 ]},
 {"id": "s3", "title": "HCF and LCM by prime factorisation", "blocks": [
  b("s3.socratic", "socratic_question",
    question="$6 = 2 \\times 3$ and $20 = 2^{2} \\times 5$. The HCF must divide both numbers. Which primes can the HCF contain?",
    options=["Only primes that appear in both numbers", "Every prime that appears in either number", "Only the prime 5"],
    correct_index=0,
    explanation="A factor of both numbers can only use primes present in **both**, and no more copies than either has. "
                "Here only 2 is common, and the smaller power is $2^{1}$, so $\\text{HCF}(6, 20) = 2$."),
  b("s3.reveal", "theory", title="The rule for HCF and LCM",
    body="Write each number as a product of primes with powers. Then:\n\n"
         "- **HCF** = product of the **smallest power** of each **common** prime factor.\n"
         "- **LCM** = product of the **greatest power** of **each** prime factor involved.\n\n"
         "For any two positive integers $a$ and $b$:\n\n"
         "$$\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b$$\n\n"
         "**Careful:** this product rule is true for **two** numbers only. "
         "For $6, 72, 120$: $\\text{HCF} \\times \\text{LCM} = 6 \\times 360 = 2160$, while $6 \\times 72 \\times 120 = 51840$."),
  b("s3.ex2", "worked_example", title="NCERT Example 2",
    problem="Find the LCM and HCF of 6 and 20 by the prime factorisation method.",
    steps=["$6 = 2^{1} \\times 3^{1}$ and $20 = 2^{2} \\times 5^{1}$",
           "Common prime: 2. Smallest power: $2^{1}$. So $\\text{HCF}(6, 20) = 2$.",
           "All primes: 2, 3, 5. Greatest powers: $2^{2}, 3^{1}, 5^{1}$. So $\\text{LCM}(6, 20) = 2^{2} \\times 3 \\times 5 = 60$.",
           "Check: $\\text{HCF} \\times \\text{LCM} = 2 \\times 60 = 120 = 6 \\times 20$ ✓"],
    answer="HCF = 2, LCM = 60"),
  b("s3.ex3", "worked_example", title="NCERT Example 3",
    problem="Find the HCF of 96 and 404 by the prime factorisation method. Hence, find their LCM.",
    steps=["$96 = 2^{5} \\times 3$ and $404 = 2^{2} \\times 101$",
           "Common prime: 2, smallest power $2^{2}$. So $\\text{HCF}(96, 404) = 4$.",
           "$\\text{LCM} = \\dfrac{96 \\times 404}{\\text{HCF}} = \\dfrac{96 \\times 404}{4} = 9696$"],
    answer="HCF = 4, LCM = 9696"),
  b("s3.ex4", "worked_example", title="NCERT Example 4",
    problem="Find the HCF and LCM of 6, 72 and 120, using the prime factorisation method.",
    steps=["$6 = 2 \\times 3$, $72 = 2^{3} \\times 3^{2}$, $120 = 2^{3} \\times 3 \\times 5$",
           "Common primes: 2 and 3, smallest powers $2^{1}$ and $3^{1}$. So HCF $= 2 \\times 3 = 6$.",
           "All primes: 2, 3, 5, greatest powers $2^{3}, 3^{2}, 5^{1}$. So LCM $= 2^{3} \\times 3^{2} \\times 5 = 360$.",
           "Note: $6 \\times 72 \\times 120 \\neq \\text{HCF} \\times \\text{LCM}$. The product rule is only for two numbers."],
    answer="HCF = 6, LCM = 360"),
  b("s3.memory", "memory_trick", title="HCF is humble, LCM is large",
    body="**H**CF takes the **h**umble (smallest) power of the **common** primes.\n\n"
         "**L**CM takes the **l**argest power of **all** the primes."),
  b("s3.check1", "knowledge_check",
    question="What is the HCF of $2^{3} \\times 3^{2} \\times 5$ and $2^{2} \\times 3^{3} \\times 7$?",
    options=["$36$", "$7560$", "$6$", "$180$"], correct_index=0,
    explanation="Common primes are 2 and 3. Smallest powers: $2^{2}$ and $3^{2}$. HCF $= 4 \\times 9 = 36$."),
  b("s3.check2", "knowledge_check",
    question="Two numbers have HCF 12 and LCM 240. What is their product?",
    options=["$2880$", "$252$", "$20$", "$228$"], correct_index=0,
    explanation="For two numbers, product $= \\text{HCF} \\times \\text{LCM} = 12 \\times 240 = 2880$ (for example 48 and 60)."),
  b("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Using $\\text{HCF} \\times \\text{LCM} = $ product for **three** numbers. It works for two only.\n"
         "- Writing $4$ or $9$ as a 'prime factor'. Break everything down to primes.\n"
         "- For HCF, taking primes that are **not common** to all the numbers.\n"
         "- Forgetting that the LCM is always a multiple of the HCF. If your LCM is not, recheck."),
 ]},
 {"id": "s4", "title": "Irrational numbers", "blocks": [
  b("s4.socratic", "socratic_question",
    question="Suppose $\\sqrt{2} = \\dfrac{a}{b}$ in lowest terms. Squaring gives $a^{2} = 2b^{2}$. What can you say about $a$?",
    options=["$a$ must be even", "$a$ must be odd", "Nothing can be said"], correct_index=0,
    explanation="$a^{2} = 2b^{2}$ is even. If $a$ were odd, $a^{2}$ would be odd. So $a$ is even. "
                "Hold on to this: it is the first step of a famous proof."),
  b("s4.reveal", "theory", title="What is an irrational number?",
    body="A number $s$ is **irrational** if it **cannot** be written as $\\dfrac{p}{q}$, where $p$ and $q$ are integers and $q \\neq 0$.\n\n"
         "Examples: $\\sqrt{2}, \\sqrt{3}, \\sqrt{15}, \\pi, 0.10110111011110\\ldots$\n\n"
         "**Theorem 1.2:** Let $p$ be a prime number. If $p$ divides $a^{2}$, then $p$ divides $a$, where $a$ is a positive integer.\n\n"
         "*Why:* write $a = p_1 p_2 \\cdots p_n$. Then $a^{2} = (p_1 p_2 \\cdots p_n)(p_1 p_2 \\cdots p_n)$. "
         "If $p$ divides $a^{2}$, then by the Fundamental Theorem of Arithmetic $p$ is one of $p_1, \\ldots, p_n$, so $p$ divides $a$."),
  b("s4.proof2", "worked_example", title="Theorem 1.3: $\\sqrt{2}$ is irrational",
    problem="Prove that $\\sqrt{2}$ is irrational.",
    steps=["Assume the opposite: $\\sqrt{2}$ is rational. Then $\\sqrt{2} = \\dfrac{r}{s}$ for integers $r, s$ with $s \\neq 0$.",
           "Remove common factors so that $r$ and $s$ are coprime (their HCF is 1).",
           "Then $s\\sqrt{2} = r$. Squaring: $2s^{2} = r^{2}$, so 2 divides $r^{2}$, and by Theorem 1.2, 2 divides $r$.",
           "Write $r = 2c$. Then $2s^{2} = 4c^{2}$, so $s^{2} = 2c^{2}$. Hence 2 divides $s^{2}$, and so 2 divides $s$.",
           "Now 2 divides both $r$ and $s$. This contradicts that $r$ and $s$ are coprime.",
           "The contradiction came from assuming $\\sqrt{2}$ is rational. So $\\sqrt{2}$ is irrational."],
    answer="$\\sqrt{2}$ is irrational."),
  b("s4.ex5", "worked_example", title="NCERT Example 5",
    problem="Prove that $\\sqrt{3}$ is irrational.",
    steps=["Assume $\\sqrt{3} = \\dfrac{a}{b}$ where $a, b$ are coprime integers and $b \\neq 0$.",
           "Then $b\\sqrt{3} = a$. Squaring: $3b^{2} = a^{2}$, so 3 divides $a^{2}$ and hence 3 divides $a$ (Theorem 1.2).",
           "Write $a = 3c$: $3b^{2} = 9c^{2}$, so $b^{2} = 3c^{2}$. Hence 3 divides $b^{2}$ and so 3 divides $b$.",
           "So 3 divides both $a$ and $b$, contradicting that they are coprime. Hence $\\sqrt{3}$ is irrational."],
    answer="$\\sqrt{3}$ is irrational."),
  b("s4.facts", "theory", title="Building new irrational numbers",
    body="If $q$ is rational and $s$ is irrational, then:\n\n"
         "- $q + s$ and $q - s$ are irrational;\n"
         "- $qs$ and $\\dfrac{q}{s}$ are irrational, provided $q \\neq 0$.\n\n"
         "**Method:** assume the number is rational, rearrange to make $\\sqrt{\\;}$ the subject, and show it would then be rational. Contradiction!"),
  b("s4.ex6", "worked_example", title="NCERT Example 6",
    problem="Show that $5 - \\sqrt{3}$ is irrational.",
    steps=["Assume $5 - \\sqrt{3} = \\dfrac{a}{b}$, with $a, b$ coprime integers and $b \\neq 0$.",
           "Then $\\sqrt{3} = 5 - \\dfrac{a}{b} = \\dfrac{5b - a}{b}$.",
           "Since $a, b$ are integers, $\\dfrac{5b - a}{b}$ is rational, so $\\sqrt{3}$ would be rational.",
           "This contradicts the fact that $\\sqrt{3}$ is irrational. Hence $5 - \\sqrt{3}$ is irrational."],
    answer="$5 - \\sqrt{3}$ is irrational."),
  b("s4.ex7", "worked_example", title="NCERT Example 7",
    problem="Show that $3\\sqrt{2}$ is irrational.",
    steps=["Assume $3\\sqrt{2} = \\dfrac{a}{b}$, with $a, b$ coprime integers and $b \\neq 0$.",
           "Then $\\sqrt{2} = \\dfrac{a}{3b}$, which is rational because $a$ and $3b$ are integers.",
           "This contradicts the fact that $\\sqrt{2}$ is irrational. Hence $3\\sqrt{2}$ is irrational."],
    answer="$3\\sqrt{2}$ is irrational."),
  b("s4.tip", "teacher_tip", title="Proof by contradiction as detective work",
    body="Tell students: we pretend the suspect is innocent ($\\sqrt{2}$ is rational) and follow the clues. "
         "When the clues lead to something impossible (a fraction in lowest terms that still has a common factor 2), "
         "the pretending must be wrong. In exams, the first line **'Let us assume, to the contrary, that ... is rational'** "
         "and the word **coprime** each carry marks."),
  b("s4.check1", "knowledge_check",
    question="Which of these numbers is irrational?",
    options=["$\\sqrt{12}$", "$\\sqrt{49}$", "$\\sqrt{\\dfrac{36}{25}}$", "$0.\\overline{3}$"], correct_index=0,
    explanation="$\\sqrt{49} = 7$, $\\sqrt{36/25} = 6/5$ and $0.\\overline{3} = 1/3$ are rational. "
                "$\\sqrt{12} = 2\\sqrt{3}$, a non-zero rational times an irrational, so it is irrational."),
  b("s4.check2", "knowledge_check",
    question="$(3 + \\sqrt{5})(3 - \\sqrt{5})$ is:",
    options=["a rational number", "an irrational number", "zero", "not a real number"], correct_index=0,
    explanation="$(3 + \\sqrt{5})(3 - \\sqrt{5}) = 3^{2} - (\\sqrt{5})^{2} = 9 - 5 = 4$, which is rational. "
                "The product of two irrationals can be rational!"),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  b("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend, without using the word 'theorem', why $6^{n}$ can never end in 0. "
         "Then explain why the proof that $\\sqrt{2}$ is irrational needs the words 'in lowest terms'."),
  b("s5.connection", "connection", title="Where this leads",
    body="- **Class 9:** you met irrational numbers on the number line; now you can *prove* a number is irrational.\n"
         "- **Polynomials (Chapter 2) and Quadratic Equations (Chapter 4):** roots like $2 + \\sqrt{3}$ are irrational numbers.\n"
         "- **Real life:** gear wheels, traffic signals and bus timetables repeat after the **LCM** of their cycles; "
         "cutting cloth or tiles into the largest equal pieces uses the **HCF**.\n"
         "- **Computers:** internet security (RSA encryption) relies on how hard it is to find the prime factors of very large numbers."),
  b("s5.mastery", "mastery", title="Mastery challenge",
    body="Three traffic lights change after every 48 seconds, 72 seconds and 108 seconds. They change together at 7:00:00 am. "
         "At what time will they next change together?\n\n"
         "*Hint:* write each number as a product of primes first.\n\n"
         "**Answer:** $48 = 2^{4} \\times 3$, $72 = 2^{3} \\times 3^{2}$, $108 = 2^{2} \\times 3^{3}$. "
         "LCM $= 2^{4} \\times 3^{3} = 432$ seconds $= 7$ min $12$ s, so at **7:07:12 am**."),
  b("s5.summary", "summary", title="Chapter summary",
    body="- **Fundamental Theorem of Arithmetic:** every composite number is a product of primes in exactly one way, apart from order.\n"
         "- **HCF** = smallest powers of common primes. **LCM** = greatest powers of all primes.\n"
         "- For two numbers: $\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b$.\n"
         "- If a prime $p$ divides $a^{2}$, then $p$ divides $a$.\n"
         "- $\\sqrt{2}, \\sqrt{3}, \\sqrt{5}$ (in general $\\sqrt{p}$ for prime $p$) are irrational, proved by contradiction.\n"
         "- Rational $\\pm$ irrational, and non-zero rational $\\times$ or $\\div$ irrational, are irrational."),
  b("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Write prime factorisations in **power form, ascending order**: $2^{3} \\times 3^{2} \\times 5$.\n"
         "- In 'verify' questions, show both sides of $\\text{HCF} \\times \\text{LCM} = a \\times b$ separately.\n"
         "- In irrationality proofs, write: *assume to the contrary*, *coprime*, *$p$ divides $a^{2}$ so $p$ divides $a$*, *contradiction*.\n"
         "- For 'when will they meet again' questions use **LCM**; for 'largest equal group or piece' questions use **HCF**."),
  b("s5.flash1", "flashcard", front="State the Fundamental Theorem of Arithmetic.",
    back="Every composite number can be expressed as a product of primes, and this factorisation is unique apart from the order of the factors."),
  b("s5.flash2", "flashcard", front="HCF and LCM of two numbers: what is the relation?",
    back="$\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b$ (two numbers only)."),
  b("s5.flash3", "flashcard", front="If a prime $p$ divides $a^{2}$, then ...?", back="$p$ divides $a$ (Theorem 1.2)."),
  b("s5.flash4", "flashcard", front="Why can $6^{n}$ never end with 0?",
    back="$6^{n} = 2^{n} \\times 3^{n}$ has no factor 5, and by uniqueness of prime factorisation it can never get one."),
 ]},
]

chapter = {
  "schema_version": 1, "id": CH_ID, "title": "Real Numbers",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)",
  "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 1, "languages": ["en"],
  "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: Fundamental Theorem of Arithmetic and proofs of irrationality. "
                   "Euclid's division lemma and decimal expansions were removed from the syllabus and are not included.",
  "concepts": ["prime_factorisation", "fundamental_theorem_of_arithmetic", "hcf", "lcm", "irrational_numbers"],
  "sections": sections,
}

# ---------------------------------------------------------------- question bank
Q = []
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch01.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def ex(e, n, part=None):
    s = {"kind": "ncert_exercise", "exercise": e, "question": n}
    if part: s["part"] = part
    return s
SHINE = {"kind": "shine"}
PF, FTA, HCF, LCM, IRR = "prime_factorisation", "fundamental_theorem_of_arithmetic", "hcf", "lcm", "irrational_numbers"

# Exercise 1.1 Q1
for part, n in zip(["i", "ii", "iii", "iv", "v"], [140, 156, 3825, 5005, 7429]):
    q(f"ex1_1.q1.{part}", "very_short_answer", 2, [PF], ex("1.1", 1, part),
      f"Express {n} as a product of its prime factors.", "easy",
      answer_steps=[f"Divide repeatedly by primes: ${n} = {tex_factor(n)}$"],
      marking_scheme=["1 mark: correct repeated division / factor tree", "1 mark: final answer in power form"])
# Exercise 1.1 Q2
for part, (a, bb) in zip(["i", "ii", "iii"], [(26, 91), (510, 92), (336, 54)]):
    h, l = hcf(a, bb), lcm(a, bb)
    q(f"ex1_1.q2.{part}", "short_answer", 3, [HCF, LCM, PF], ex("1.1", 2, part),
      f"Find the LCM and HCF of {a} and {bb} and verify that LCM $\\times$ HCF = product of the two numbers.",
      answer_steps=[f"${a} = {tex_factor(a)}$, ${bb} = {tex_factor(bb)}$",
                    f"HCF = {h}, LCM = {l}",
                    f"LCM $\\times$ HCF $= {l} \\times {h} = {l*h}$ and ${a} \\times {bb} = {a*bb}$. Verified."],
      marking_scheme=["1 mark: both prime factorisations", "1 mark: HCF and LCM", "1 mark: verification"])
# Exercise 1.1 Q3
for part, nums in zip(["i", "ii", "iii"], [(12, 15, 21), (17, 23, 29), (8, 9, 25)]):
    h, l = hcf(*nums), lcm(*nums)
    facts = ", ".join(f"${n} = {tex_factor(n)}$" for n in nums)
    q(f"ex1_1.q3.{part}", "very_short_answer", 2, [HCF, LCM, PF], ex("1.1", 3, part),
      f"Find the LCM and HCF of {', '.join(map(str, nums[:-1]))} and {nums[-1]} by applying the prime factorisation method.",
      answer_steps=[facts, f"HCF = {h}, LCM = {l}"],
      marking_scheme=["1 mark: prime factorisations", "1 mark: HCF and LCM"])
q("ex1_1.q4", "very_short_answer", 2, [HCF, LCM], ex("1.1", 4), "Given that HCF(306, 657) = 9, find LCM(306, 657).", "easy",
  answer_steps=["HCF $\\times$ LCM = product of the two numbers",
                "LCM $= \\dfrac{306 \\times 657}{9} = \\dfrac{201042}{9} = 22338$"],
  marking_scheme=["1 mark: using HCF × LCM = product", "1 mark: LCM = 22338"])
q("ex1_1.q5", "very_short_answer", 2, [FTA], ex("1.1", 5), "Check whether $6^{n}$ can end with the digit 0 for any natural number $n$.",
  answer_steps=["To end with 0, $6^{n}$ must be divisible by 5.", "$6^{n} = 2^{n} \\times 3^{n}$, whose only primes are 2 and 3.",
                "By uniqueness of prime factorisation, 5 is not a factor, so $6^{n}$ cannot end with 0 for any $n$."],
  marking_scheme=["1 mark: $6^{n} = 2^{n} \\times 3^{n}$", "1 mark: conclusion with reason (no factor 5)"])
q("ex1_1.q6.i", "very_short_answer", 2, [FTA], ex("1.1", 6, "i"), "Explain why $7 \\times 11 \\times 13 + 13$ is a composite number.",
  answer_steps=["$7 \\times 11 \\times 13 + 13 = 13 \\times (7 \\times 11 + 1) = 13 \\times 78 = 1014$",
                "It has factors other than 1 and itself (for example 13), so it is composite."],
  marking_scheme=["1 mark: taking 13 common", "1 mark: conclusion"])
q("ex1_1.q6.ii", "very_short_answer", 2, [FTA], ex("1.1", 6, "ii"), "Explain why $7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 + 5$ is a composite number.",
  answer_steps=["$7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 + 5 = 5 \\times (7 \\times 6 \\times 4 \\times 3 \\times 2 \\times 1 + 1) = 5 \\times 1009 = 5045$",
                "It has 5 as a factor other than 1 and itself, so it is composite."],
  marking_scheme=["1 mark: taking 5 common", "1 mark: conclusion"])
q("ex1_1.q7", "very_short_answer", 2, [LCM], ex("1.1", 7),
  "There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. "
  "Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?",
  answer_steps=["They meet at the start after a time that is a multiple of both 18 and 12, the least such being the LCM.",
                "$18 = 2 \\times 3^{2}$, $12 = 2^{2} \\times 3$, so LCM $= 2^{2} \\times 3^{2} = 36$", "They meet after 36 minutes."],
  marking_scheme=["1 mark: identifying LCM with factorisations", "1 mark: 36 minutes"])
# Exercise 1.2
def irr_proof(id_, src, num, steps, marks=3, typ="short_answer", difficulty="medium"):
    q(id_, typ, marks, [IRR], src, f"Prove that {num} is irrational.", difficulty, answer_steps=steps,
      marking_scheme=(["1 mark: assuming the contrary with coprime $a, b$", "1 mark: squaring and using Theorem 1.2 twice",
                       "1 mark: contradiction and conclusion"] if marks == 3 else
                      ["1 mark: assuming the contrary and isolating the surd", "1 mark: contradiction and conclusion"]))
irr_proof("ex1_2.q1", ex("1.2", 1), "$\\sqrt{5}$", [
  "Assume, to the contrary, $\\sqrt{5} = \\dfrac{a}{b}$, where $a, b$ are coprime integers and $b \\neq 0$.",
  "Then $5b^{2} = a^{2}$, so 5 divides $a^{2}$ and hence 5 divides $a$.",
  "Let $a = 5c$. Then $5b^{2} = 25c^{2}$, so $b^{2} = 5c^{2}$; 5 divides $b^{2}$ and hence 5 divides $b$.",
  "5 divides both $a$ and $b$, contradicting that they are coprime. So $\\sqrt{5}$ is irrational."])
irr_proof("ex1_2.q2", ex("1.2", 2), "$3 + 2\\sqrt{5}$", [
  "Assume $3 + 2\\sqrt{5} = \\dfrac{a}{b}$ with $a, b$ coprime integers, $b \\neq 0$.",
  "Then $\\sqrt{5} = \\dfrac{a - 3b}{2b}$, which is rational since $a, b$ are integers.",
  "This contradicts the fact that $\\sqrt{5}$ is irrational. Hence $3 + 2\\sqrt{5}$ is irrational."])
for part, num, steps in [
  ("i", "$\\dfrac{1}{\\sqrt{2}}$", ["Assume $\\dfrac{1}{\\sqrt{2}} = \\dfrac{a}{b}$ with $a, b$ integers, $a, b \\neq 0$.",
                                   "Then $\\sqrt{2} = \\dfrac{b}{a}$, which is rational. This contradicts that $\\sqrt{2}$ is irrational."]),
  ("ii", "$7\\sqrt{5}$", ["Assume $7\\sqrt{5} = \\dfrac{a}{b}$ with $a, b$ integers, $b \\neq 0$.",
                         "Then $\\sqrt{5} = \\dfrac{a}{7b}$, which is rational. This contradicts that $\\sqrt{5}$ is irrational."]),
  ("iii", "$6 + \\sqrt{2}$", ["Assume $6 + \\sqrt{2} = \\dfrac{a}{b}$ with $a, b$ integers, $b \\neq 0$.",
                             "Then $\\sqrt{2} = \\dfrac{a - 6b}{b}$, which is rational. This contradicts that $\\sqrt{2}$ is irrational."])]:
    irr_proof(f"ex1_2.q3.{part}", ex("1.2", 3, part), num, steps, marks=2, typ="very_short_answer")
# NCERT examples as practice
q("eg1", "very_short_answer", 2, [FTA], {"kind": "ncert_example", "example": 1},
  "Check whether there is any natural number $n$ for which $4^{n}$ ends with the digit zero.",
  answer_steps=["$4^{n} = 2^{2n}$ has only the prime 2.", "To end in 0 it needs the prime 5, which uniqueness of factorisation rules out. So no such $n$."],
  marking_scheme=["1 mark: $4^{n} = 2^{2n}$", "1 mark: conclusion with reason"])
q("eg3", "very_short_answer", 2, [HCF, LCM], {"kind": "ncert_example", "example": 3},
  "Find the HCF of 96 and 404 by the prime factorisation method. Hence, find their LCM.",
  answer_steps=["$96 = 2^{5} \\times 3$, $404 = 2^{2} \\times 101$, HCF $= 2^{2} = 4$", "LCM $= \\dfrac{96 \\times 404}{4} = 9696$"],
  marking_scheme=["1 mark: HCF = 4", "1 mark: LCM = 9696"])
q("eg4", "very_short_answer", 2, [HCF, LCM], {"kind": "ncert_example", "example": 4},
  "Find the HCF and LCM of 6, 72 and 120, using the prime factorisation method.",
  answer_steps=["$6 = 2 \\times 3$, $72 = 2^{3} \\times 3^{2}$, $120 = 2^{3} \\times 3 \\times 5$", "HCF $= 6$, LCM $= 2^{3} \\times 3^{2} \\times 5 = 360$"],
  marking_scheme=["1 mark: factorisations", "1 mark: HCF and LCM"])
irr_proof("eg5", {"kind": "ncert_example", "example": 5}, "$\\sqrt{3}$", [
  "Assume $\\sqrt{3} = \\dfrac{a}{b}$, $a, b$ coprime, $b \\neq 0$. Then $3b^{2} = a^{2}$, so 3 divides $a$.",
  "Let $a = 3c$: $b^{2} = 3c^{2}$, so 3 divides $b$.",
  "3 divides both $a$ and $b$: contradiction. So $\\sqrt{3}$ is irrational."])
irr_proof("eg6", {"kind": "ncert_example", "example": 6}, "$5 - \\sqrt{3}$", [
  "Assume $5 - \\sqrt{3} = \\dfrac{a}{b}$. Then $\\sqrt{3} = \\dfrac{5b - a}{b}$, rational.",
  "Contradiction, since $\\sqrt{3}$ is irrational. So $5 - \\sqrt{3}$ is irrational."], marks=2, typ="very_short_answer")
irr_proof("eg7", {"kind": "ncert_example", "example": 7}, "$3\\sqrt{2}$", [
  "Assume $3\\sqrt{2} = \\dfrac{a}{b}$. Then $\\sqrt{2} = \\dfrac{a}{3b}$, rational.",
  "Contradiction, since $\\sqrt{2}$ is irrational. So $3\\sqrt{2}$ is irrational."], marks=2, typ="very_short_answer")

# Board-style MCQs (our own, numbers verified above)
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy"):
    q(id_, "mcq", 1, concepts, SHINE, question, difficulty, options=options, correct_index=correct, explanation=explanation)
mcq("mcq01", [HCF, PF], "The HCF of $2^{3} \\times 3^{2} \\times 5$ and $2^{2} \\times 3^{3} \\times 7$ is:",
    ["$36$", "$7560$", "$6$", "$180$"], 0, "Smallest powers of the common primes: $2^{2} \\times 3^{2} = 36$.")
mcq("mcq02", [LCM, PF], "The LCM of $2^{3} \\times 3^{2} \\times 5$ and $2^{2} \\times 3^{3} \\times 7$ is:",
    ["$7560$", "$36$", "$1260$", "$3780$"], 0, "Greatest powers of all primes: $2^{3} \\times 3^{3} \\times 5 \\times 7 = 7560$.")
mcq("mcq03", [HCF, LCM], "The HCF of two numbers is 12 and their LCM is 240. The product of the numbers is:",
    ["$2880$", "$252$", "$20$", "$228$"], 0, "Product $= 12 \\times 240 = 2880$.")
mcq("mcq04", [IRR], "Which of the following is irrational?",
    ["$\\sqrt{12}$", "$\\sqrt{49}$", "$\\sqrt{\\dfrac{36}{25}}$", "$0.\\overline{3}$"], 0, "$\\sqrt{12} = 2\\sqrt{3}$ is irrational; the others are rational.")
mcq("mcq05", [PF], "The prime factorisation of 156 is:",
    ["$2^{2} \\times 3 \\times 13$", "$2 \\times 3 \\times 26$", "$2^{2} \\times 39$", "$4 \\times 3 \\times 13$"], 0,
    "Only $2^{2} \\times 3 \\times 13$ contains primes alone.")
mcq("mcq06", [IRR], "If $p$ is a prime number and $p$ divides $a^{2}$, where $a$ is a positive integer, then:",
    ["$p$ divides $a$", "$a$ divides $p$", "$p^{2}$ divides $a$", "$p$ does not divide $a$"], 0, "This is Theorem 1.2.")
mcq("mcq07", [PF], "The exponent of 2 in the prime factorisation of 144 is:",
    ["$4$", "$2$", "$3$", "$5$"], 0, "$144 = 2^{4} \\times 3^{2}$.")
mcq("mcq08", [LCM], "The LCM of the smallest two-digit composite number and the smallest composite number is:",
    ["$20$", "$10$", "$40$", "$4$"], 0, "Smallest two-digit composite is 10, smallest composite is 4; $\\text{LCM}(10, 4) = 20$.")
mcq("mcq09", [HCF], "The HCF of the smallest prime number and the smallest composite number is:",
    ["$2$", "$4$", "$1$", "$8$"], 0, "$\\text{HCF}(2, 4) = 2$.")
mcq("mcq10", [HCF, PF], "If $p = a^{2}b^{3}$ and $q = a^{3}b$, where $a$ and $b$ are prime numbers, then $\\text{HCF}(p, q)$ is:",
    ["$a^{2}b$", "$a^{3}b^{3}$", "$ab$", "$a^{2}b^{2}$"], 0, "Smallest powers: $a^{2}$ and $b^{1}$.", "medium")
mcq("mcq11", [LCM, PF], "If $p = a^{2}b^{3}$ and $q = a^{3}b$, where $a$ and $b$ are prime numbers, then $\\text{LCM}(p, q)$ is:",
    ["$a^{3}b^{3}$", "$a^{2}b$", "$a^{5}b^{4}$", "$ab$"], 0, "Greatest powers: $a^{3}$ and $b^{3}$.", "medium")
mcq("mcq12", [FTA], "For any natural number $n$, $6^{n}$ cannot end with the digit:",
    ["$0$", "$6$", "$2$", "$4$"], 0, "$6^{n}$ has no factor 5, so it cannot end with 0. (In fact $6^{n}$ always ends with 6.)")
mcq("mcq13", [IRR], "The product of a non-zero rational number and an irrational number is:",
    ["always irrational", "always rational", "rational or irrational", "one"], 0,
    "If $q \\neq 0$ is rational and $s$ is irrational, $qs$ is irrational.")
mcq("mcq14", [IRR], "$(3 + \\sqrt{5})(3 - \\sqrt{5})$ is:",
    ["a rational number", "an irrational number", "equal to $0$", "not a real number"], 0, "$9 - 5 = 4$, rational.", "medium")
mcq("mcq15", [HCF], "The HCF of two consecutive natural numbers is:",
    ["$1$", "$0$", "the smaller number", "their product"], 0, "Any common factor would divide their difference, 1.")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.",
              "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.",
              "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a, r, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE,
      f"**Assertion (A):** {a}\n\n**Reason (R):** {r}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [FTA], "$12^{n}$ cannot end with the digit 0 for any natural number $n$.",
   "The prime factorisation of $12^{n}$ does not contain the prime 5.", 0,
   "$12^{n} = 2^{2n} \\times 3^{n}$ has no factor 5, which is exactly why it cannot end in 0.")
ar("ar2", [HCF, LCM], "If HCF of two numbers is 9 and their product is 1215, then their LCM is 135.",
   "For any two positive integers $a$ and $b$, $\\text{HCF}(a, b) \\times \\text{LCM}(a, b) = a \\times b$.", 0,
   "LCM $= 1215 \\div 9 = 135$ (for example 9 and 135), using the reason.")
ar("ar3", [IRR], "$5 - \\sqrt{3}$ is an irrational number.",
   "The difference of a rational number and an irrational number is irrational.", 0, "5 is rational and $\\sqrt{3}$ is irrational.")
ar("ar4", [HCF, LCM], "$\\text{LCM}(8, 9, 25) = 1800$.",
   "For any three positive integers, HCF $\\times$ LCM equals their product.", 2,
   "A is true. R is false: for 6, 72, 120, HCF $\\times$ LCM $= 6 \\times 360 = 2160$ but the product is 51840.")
ar("ar5", [IRR], "$\\sqrt{9}$ is an irrational number.",
   "The square root of a prime number is irrational.", 3, "$\\sqrt{9} = 3$ is rational, so A is false; R is true.")

# Board-style written questions
q("vsa1", "very_short_answer", 2, [HCF, LCM, PF], SHINE, "Find the HCF and LCM of 120 and 144 by the prime factorisation method.",
  answer_steps=["$120 = 2^{3} \\times 3 \\times 5$, $144 = 2^{4} \\times 3^{2}$", "HCF $= 2^{3} \\times 3 = 24$, LCM $= 2^{4} \\times 3^{2} \\times 5 = 720$"],
  marking_scheme=["1 mark: factorisations", "1 mark: HCF and LCM"])
q("vsa2", "very_short_answer", 2, [FTA], SHINE, "Check whether $12^{n}$ can end with the digit 0 for any natural number $n$.",
  answer_steps=["$12^{n} = 2^{2n} \\times 3^{n}$; the only primes are 2 and 3.", "No factor 5, so $12^{n}$ cannot end with 0."],
  marking_scheme=["1 mark: prime factorisation", "1 mark: conclusion"])
q("vsa3", "very_short_answer", 2, [FTA], SHINE, "Explain why $3 \\times 5 \\times 7 + 7$ is a composite number.",
  answer_steps=["$3 \\times 5 \\times 7 + 7 = 7 \\times (15 + 1) = 7 \\times 16 = 112$", "It has factors other than 1 and itself, so it is composite."],
  marking_scheme=["1 mark: taking 7 common", "1 mark: conclusion"])
q("vsa4", "very_short_answer", 2, [HCF], SHINE, "Find the largest number which divides 245 and 1029 leaving remainder 5 in each case.", "medium",
  answer_steps=["The number divides $245 - 5 = 240$ and $1029 - 5 = 1024$.", "$240 = 2^{4} \\times 3 \\times 5$, $1024 = 2^{10}$, HCF $= 2^{4} = 16$"],
  marking_scheme=["1 mark: subtracting the remainders", "1 mark: HCF = 16"])
q("vsa5", "very_short_answer", 2, [IRR], SHINE, "Given that $\\sqrt{7}$ is irrational, prove that $3 + \\sqrt{7}$ is irrational.",
  answer_steps=["Assume $3 + \\sqrt{7} = \\dfrac{a}{b}$ with integers $a, b$, $b \\neq 0$.", "Then $\\sqrt{7} = \\dfrac{a - 3b}{b}$ is rational: contradiction."],
  marking_scheme=["1 mark: assuming the contrary and isolating $\\sqrt{7}$", "1 mark: contradiction and conclusion"])
q("sa1", "short_answer", 3, [IRR], SHINE, "Prove that $\\sqrt{7}$ is irrational.",
  answer_steps=["Assume $\\sqrt{7} = \\dfrac{a}{b}$, $a, b$ coprime, $b \\neq 0$. Then $7b^{2} = a^{2}$, so 7 divides $a$.",
                "Let $a = 7c$: $b^{2} = 7c^{2}$, so 7 divides $b$.", "7 divides both $a$ and $b$: contradiction. Hence $\\sqrt{7}$ is irrational."],
  marking_scheme=["1 mark: assumption with coprime", "1 mark: 7 divides $a$ and $b$", "1 mark: contradiction"])
q("sa2", "short_answer", 3, [IRR], SHINE, "Given that $\\sqrt{5}$ is irrational, prove that $2 - 3\\sqrt{5}$ is irrational.",
  answer_steps=["Assume $2 - 3\\sqrt{5} = \\dfrac{a}{b}$ with integers $a, b$, $b \\neq 0$.", "Then $\\sqrt{5} = \\dfrac{2b - a}{3b}$, which is rational.",
                "This contradicts that $\\sqrt{5}$ is irrational. Hence $2 - 3\\sqrt{5}$ is irrational."],
  marking_scheme=["1 mark: assumption", "1 mark: isolating $\\sqrt{5}$", "1 mark: contradiction"])
q("sa3", "short_answer", 3, [LCM], SHINE, "Find the smallest number which, when divided by 12, 16, 24 and 36, leaves remainder 7 in each case.", "medium",
  answer_steps=["$12 = 2^{2} \\times 3$, $16 = 2^{4}$, $24 = 2^{3} \\times 3$, $36 = 2^{2} \\times 3^{2}$", "LCM $= 2^{4} \\times 3^{2} = 144$",
                "Required number $= 144 + 7 = 151$"],
  marking_scheme=["1 mark: factorisations", "1 mark: LCM = 144", "1 mark: 151"])
q("sa4", "short_answer", 3, [LCM], SHINE, "Three bells toll at intervals of 9, 12 and 15 minutes. If they start tolling together, after what time will they next toll together?",
  answer_steps=["$9 = 3^{2}$, $12 = 2^{2} \\times 3$, $15 = 3 \\times 5$", "LCM $= 2^{2} \\times 3^{2} \\times 5 = 180$ minutes", "They toll together again after 180 minutes = 3 hours."],
  marking_scheme=["1 mark: factorisations", "1 mark: LCM", "1 mark: answer in hours"])
q("sa5", "short_answer", 3, [HCF], SHINE,
  "In a seminar, the numbers of participants in Hindi, English and Mathematics are 60, 84 and 108. Find the minimum number of rooms required if, in each room, "
  "the same number of participants are to be seated and all of them are of the same subject.", "medium",
  answer_steps=["Participants per room must divide 60, 84 and 108; for the fewest rooms take the HCF.",
                "$60 = 2^{2} \\times 3 \\times 5$, $84 = 2^{2} \\times 3 \\times 7$, $108 = 2^{2} \\times 3^{3}$, HCF $= 12$",
                "Rooms $= \\dfrac{60 + 84 + 108}{12} = \\dfrac{252}{12} = 21$"],
  marking_scheme=["1 mark: recognising HCF", "1 mark: HCF = 12", "1 mark: 21 rooms"])
q("cb1", "case_based", 4, [HCF, LCM, PF], SHINE,
  "A sweet seller has 420 kaju barfis and 130 badam barfis. She wants to stack them so that each stack has the same number of barfis "
  "and contains only one kind, using the least area of the tray.\n\n"
  "(i) What is the maximum number of barfis that can be placed in each stack? (1)\n\n"
  "(ii) Write the prime factorisation of 420. (1)\n\n"
  "(iii) How many stacks will there be in all? OR Find the LCM of 420 and 130. (2)", "medium",
  answer_steps=["(i) HCF(420, 130): $420 = 2^{2} \\times 3 \\times 5 \\times 7$, $130 = 2 \\times 5 \\times 13$, HCF $= 10$",
                "(ii) $420 = 2^{2} \\times 3 \\times 5 \\times 7$",
                "(iii) Stacks $= \\dfrac{420}{10} + \\dfrac{130}{10} = 42 + 13 = 55$. OR LCM $= 2^{2} \\times 3 \\times 5 \\times 7 \\times 13 = 5460$"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [LCM], SHINE,
  "Ram and Shyam jog on a circular track. Ram takes 12 minutes and Shyam takes 18 minutes for one round. They start together from the same point "
  "in the same direction.\n\n"
  "(i) After how many minutes will they meet again at the starting point? (1)\n\n"
  "(ii) How many rounds will Ram have completed by then? (1)\n\n"
  "(iii) If Mohan, who takes 15 minutes per round, also starts with them, after how many minutes will all three meet at the starting point? (2)", "medium",
  answer_steps=["(i) LCM(12, 18) $= 36$ minutes", "(ii) $36 \\div 12 = 3$ rounds",
                "(iii) $12 = 2^{2} \\times 3$, $18 = 2 \\times 3^{2}$, $15 = 3 \\times 5$, LCM $= 2^{2} \\times 3^{2} \\times 5 = 180$ minutes"],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark factorisation, 1 mark answer"])

def spread_answers(item):
    """Rotates options by a fixed amount per id so the answer is not always the first option."""
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason":
        return
    shift = sum(map(ord, item["id"])) % len(opts)
    correct = opts[item["correct_index"]]
    item["options"] = opts[shift:] + opts[:shift]
    item["correct_index"] = item["options"].index(correct)
for x in Q: spread_answers(x)
for sec in sections:
    for blk in sec["blocks"]: spread_answers(blk)
from collections import Counter
print("answer positions:", Counter(x["correct_index"] for x in Q if x["type"] == "mcq"))

bank = {"schema_version": 1, "chapter_id": CH_ID, "questions": Q}

os.makedirs(os.path.join(ROOT, PATH), exist_ok=True)
for name, data in [("chapter.json", chapter), ("questions.json", bank)]:
    with open(os.path.join(ROOT, PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
ncert = [x for x in Q if x["source"]["kind"] == "ncert_exercise"]
print(f"blocks={sum(len(s['blocks']) for s in sections)} questions={len(Q)} ncert_exercise_items={len(ncert)}")
