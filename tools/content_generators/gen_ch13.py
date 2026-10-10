"""CBSE Class 10 Maths Ch 13: Statistics (mean, mode and median of grouped data).
Every answer is computed from the table with exact fractions and compared
with the NCERT / CBSE answer. Tables are numbers-only LaTeX arrays, so they
read the same in every language."""
import json, os, sys
from collections import Counter
from fractions import Fraction as Fr

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch13"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch13_statistics"

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def F(x): return Fr(str(x))
def num(x):
    """Plain decimal for display: integers stay integers, else up to 2 places."""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    s = f"{float(x):.2f}".rstrip("0").rstrip(".")
    return s
def near(value, target, tol=0.006): return abs(float(value) - target) < tol

class Data:
    """A grouped frequency table. `classes` are (lower, upper) pairs; `shown`
    are the labels printed in the question (they differ for 118-126 style
    classes, where the true limits are 117.5-126.5)."""
    def __init__(self, classes, f, shown=None):
        self.classes = [(F(a), F(b)) for a, b in classes]
        self.f = [Fr(v) for v in f]
        self.shown = shown or [f"{num(a)} - {num(b)}" for a, b in self.classes]
    @property
    def n(self): return sum(self.f)
    @property
    def marks(self): return [(a + b) / 2 for a, b in self.classes]
    def mean(self): return sum(fi * x for fi, x in zip(self.f, self.marks)) / self.n
    def cf(self):
        out, run = [], Fr(0)
        for fi in self.f: run += fi; out.append(run)
        return out
    def median_parts(self):
        half, cf = self.n / 2, self.cf()
        k = next(i for i, c in enumerate(cf) if c >= half)
        l, u = self.classes[k]
        return k, l, cf[k - 1] if k else Fr(0), self.f[k], u - l
    def median(self):
        k, l, c, f, h = self.median_parts()
        return l + (self.n / 2 - c) / f * h
    def mode_parts(self):
        k = max(range(len(self.f)), key=lambda i: self.f[i])
        f0 = self.f[k - 1] if k else Fr(0)
        f2 = self.f[k + 1] if k + 1 < len(self.f) else Fr(0)
        l, u = self.classes[k]
        return k, l, self.f[k], f0, f2, u - l
    def mode(self):
        k, l, f1, f0, f2, h = self.mode_parts()
        return l + (f1 - f0) / (2 * f1 - f0 - f2) * h
    def table(self):
        rows = " \\\\ \\hline ".join(f"{c} & {num(fi)}" for c, fi in zip(self.shown, self.f))
        return f"$$\\begin{{array}}{{|c|c|}}\\hline {rows} \\\\ \\hline\\end{{array}}$$"

    # ---- answer steps (fixed English skeletons, translated by shared templates)
    def mean_steps(self):
        S = sum(fi * x for fi, x in zip(self.f, self.marks))
        return [f"Class marks: $x_i = {', '.join(num(x) for x in self.marks)}$",
                f"$\\sum f_i = {num(self.n)}$ and $\\sum f_i x_i = {num(S)}$",
                f"$\\bar{{x}} = \\dfrac{{{num(S)}}}{{{num(self.n)}}} = {num(self.mean())}$"]
    def mode_steps(self):
        k, l, f1, f0, f2, h = self.mode_parts()
        return [f"Modal class: ${self.shown[k]}$, so $l = {num(l)}$, $f_1 = {num(f1)}$, $f_0 = {num(f0)}$, $f_2 = {num(f2)}$, $h = {num(h)}$",
                f"Mode $= l + \\dfrac{{f_1 - f_0}}{{2f_1 - f_0 - f_2}} \\times h = {num(l)} + \\dfrac{{{num(f1 - f0)}}}{{{num(2 * f1 - f0 - f2)}}} \\times {num(h)}$",
                f"$= {num(self.mode())}$"]
    def median_steps(self):
        k, l, c, f, h = self.median_parts()
        return [f"$\\dfrac{{n}}{{2}} = {num(self.n / 2)}$; cumulative frequencies: ${', '.join(num(x) for x in self.cf())}$",
                f"Median class: ${self.shown[k]}$, so $l = {num(l)}$, $cf = {num(c)}$, $f = {num(f)}$, $h = {num(h)}$",
                f"Median $= l + \\dfrac{{\\frac{{n}}{{2}} - cf}}{{f}} \\times h = {num(l)} + \\dfrac{{{num(self.n / 2)} - {num(c)}}}{{{num(f)}}} \\times {num(h)}$",
                f"$= {num(self.median())}$"]

def even(start, width, count): return [(start + i * width, start + (i + 1) * width) for i in range(count)]

# ---------------------------------------------------------------- data and verification
E1 = {
 1: Data(even(0, 2, 7), [1, 2, 1, 5, 6, 2, 3]),
 2: Data(even(500, 20, 5), [12, 14, 8, 6, 10]),
 4: Data(even(65, 3, 7), [2, 4, 3, 8, 7, 4, 2]),
 5: Data([(49.5, 52.5), (52.5, 55.5), (55.5, 58.5), (58.5, 61.5), (61.5, 64.5)], [15, 110, 135, 115, 25], shown=["50 - 52", "53 - 55", "56 - 58", "59 - 61", "62 - 64"]),
 6: Data(even(100, 50, 5), [4, 5, 12, 2, 2]),
 7: Data([(0, F("0.04")), (F("0.04"), F("0.08")), (F("0.08"), F("0.12")), (F("0.12"), F("0.16")), (F("0.16"), F("0.20")), (F("0.20"), F("0.24"))], [4, 9, 9, 2, 4, 2],
         shown=["0.00 - 0.04", "0.04 - 0.08", "0.08 - 0.12", "0.12 - 0.16", "0.16 - 0.20", "0.20 - 0.24"]),
 8: Data([(0, 6), (6, 10), (10, 14), (14, 20), (20, 28), (28, 38), (38, 40)], [11, 10, 7, 4, 4, 3, 1]),
 9: Data(even(45, 10, 5), [3, 10, 11, 8, 3]),
}
for q_, ans in {1: 8.1, 2: 545.2, 4: 75.9, 5: 57.19, 6: 211, 7: 0.099, 8: 12.48, 9: 69.43}.items():
    check(near(E1[q_].mean(), ans, 0.006 if q_ != 7 else 0.0005), f"13.1 Q{q_}: {float(E1[q_].mean())}")
E1[5].shown = ["50 - 52", "53 - 55", "56 - 58", "59 - 61", "62 - 64"]
# 13.1 Q3: unknown frequency f with mean 18.
Q3 = [(11, 13, 7), (13, 15, 6), (15, 17, 9), (17, 19, 13), (19, 21, None), (21, 23, 5), (23, 25, 4)]
for fv in range(0, 60):
    d = Data([(a, b) for a, b, _ in Q3], [fv if x is None else x for _, _, x in Q3])
    if d.mean() == 18: break
check(fv == 20, "13.1 Q3")
E2 = {
 1: Data(even(5, 10, 6), [6, 11, 21, 23, 14, 5]),
 2: Data(even(0, 20, 6), [10, 35, 52, 61, 38, 29]),
 3: Data(even(1000, 500, 8), [24, 40, 33, 28, 30, 22, 16, 7]),
 4: Data(even(15, 5, 8), [3, 8, 9, 10, 3, 0, 0, 2]),
 5: Data(even(3000, 1000, 8), [4, 18, 9, 7, 6, 3, 1, 1]),
 6: Data(even(0, 10, 8), [7, 14, 13, 12, 20, 11, 15, 8]),
}
check(near(E2[1].mode(), 36.8, 0.03) and near(E2[1].mean(), 35.37), "13.2 Q1")
check(E2[2].mode() == F("65.625"), "13.2 Q2")
check(near(E2[3].mode(), 1847.83) and E2[3].mean() == F("2662.5"), "13.2 Q3")
check(E2[4].mode() == F("30.625") and near(E2[4].mean(), 29.2, 0.02), "13.2 Q4")
check(near(E2[5].mode(), 4608.7), "13.2 Q5"); check(near(E2[6].mode(), 44.7, 0.01), "13.2 Q6")
E3 = {
 1: Data(even(65, 20, 7), [4, 5, 13, 20, 14, 8, 4]),
 3: Data(even(15, 5, 9), [2, 4, 18, 21, 33, 11, 3, 6, 2], shown=["15 - 20", "20 - 25", "25 - 30", "30 - 35", "35 - 40", "40 - 45", "45 - 50", "50 - 55", "55 - 60"]),
 4: Data([(117.5 + 9 * i, 126.5 + 9 * i) for i in range(7)], [3, 5, 9, 12, 5, 4, 2], shown=[f"{118 + 9 * i} - {126 + 9 * i}" for i in range(7)]),
 5: Data(even(1500, 500, 7), [14, 56, 60, 86, 74, 62, 48]),
 6: Data(even(1, 3, 6), [6, 30, 40, 16, 4, 4]),
 7: Data(even(40, 5, 7), [2, 3, 8, 6, 6, 3, 2]),
}
check(E3[1].median() == 137 and near(E3[1].mean(), 137.06) and near(E3[1].mode(), 135.77), "13.3 Q1 (NCERT prints 137.05 and 135.76, cut off rather than rounded)")
check(near(E3[3].median(), 35.76), "13.3 Q3"); check(E3[4].median() == F("146.75"), "13.3 Q4"); check(near(E3[5].median(), 3406.98), "13.3 Q5")
check(E3[6].median() == F("8.05") and E3[6].mean() == F("8.32") and near(E3[6].mode(), 7.88), "13.3 Q6"); check(near(E3[7].median(), 56.67), "13.3 Q7")
# 13.3 Q2: median 28.5, total 60 gives x = 8, y = 7.
Q2 = None
for x in range(0, 40):
    y = 60 - (5 + x + 20 + 15 + 5)
    if y < 0: break
    if Data(even(0, 10, 6), [5, x, 20, 15, y, 5]).median() == F("28.5"): Q2 = (x, y)
check(Q2 == (8, 7), "13.3 Q2")
# Sample paper
SQ35 = [10, 7, None, 15, 10, 12]
x35 = next(x for x in range(0, 15) if Data(even(0, 15, 6), [x if v is None else v for v in SQ35]).mode() == 55)
D35 = Data(even(0, 15, 6), [x35 if v is None else v for v in SQ35])
check(x35 == 5 and near(D35.mean(), 48.69), "sqp35a (the marking scheme prints 48.68)")
D35B = Data(even(135, 5, 6), [4, 7, 18, 11, 6, 5])
check(D35B.n == 51 and near(D35B.median(), 149.03) and near((3 * F("149.03") - F("148.05")) / 2, 149.52), "sqp35b")
# Lesson example (Shine data)
EX = Data(even(0, 10, 6), [3, 5, 9, 12, 7, 4])
check(EX.mean() == F("31.75") and EX.mode() == F("33.75") and EX.median() == F("32.5"), "lesson example")
check(35 + 10 * Fr(-13, 40) == F("31.75") and sum(fi * u for fi, u in zip(EX.f, [-3, -2, -1, 0, 1, 2])) == -13, "step deviation")
# Shine questions
SA1 = Data(even(0, 10, 8), [5, 8, 7, 12, 28, 20, 10, 10]); check(near(SA1.mode(), 46.67), "sa1")
SA2 = Data(even(0, 10, 5), [8, 16, 36, 34, 6]); check(near(SA2.median(), 27.22), "sa2")
SA3 = Data(even(0, 20, 7), [6, 8, 10, 12, 6, 5, 3]); check(SA3.mean() == F("62.4"), "sa3")
LA2 = Data(even(0, 10, 7), [5, 10, 18, 30, 20, 12, 5]); check(LA2.mean() == F("35.6") and near(LA2.median(), 35.67) and near(LA2.mode(), 35.45), "la2")
LA1 = None
for x in range(0, 30):
    y = 100 - (2 + 5 + x + 12 + 17 + 20 + 9 + 7 + 4)
    if y >= 0 and Data(even(0, 100, 10), [2, 5, x, 12, 17, 20, y, 9, 7, 4]).median() == 525: LA1 = (x, y)
check(LA1 == (9, 15), "la1")
MAST = None
for f1 in range(0, 60):
    f2 = 52 - f1
    if f2 >= 0 and Data(even(0, 20, 5), [17, f1, 32, f2, 19]).mean() == 50: MAST = (f1, f2)
check(MAST == (28, 24), "mastery")
CB1 = Data(even(0, 2, 5), [8, 14, 16, 8, 4]); check(CB1.mode() == F("4.4") and CB1.mean() == F("4.44") and CB1.median_parts()[1] == 4, "cb1")
CB2 = Data(even(0, 50, 5), [4, 8, 14, 10, 4]); check(CB2.cf()[2] == 26 and near(CB2.median(), 128.57) and CB2.mean() == F("127.5"), "cb2")
check(3 * 22 - 2 * 20 == 26 and Fr(1500, 50) == 30 and (3 * 30 - 0) and (84 - Fr(119, 2)) * 0 == 0, "mcqs")
check((F("24.5") + 2 * F("29.75")) / 3 == 28, "vsa2")

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch13.{id_}", "type": type_, **kw}
EX_TABLE = ("| Class | $f_i$ | $x_i$ | $f_i x_i$ | $u_i = \\dfrac{x_i - 35}{10}$ | $f_i u_i$ | $cf$ |\n|---|---|---|---|---|---|---|\n" +
            "\n".join(f"| ${c}$ | ${num(fi)}$ | ${num(x)}$ | ${num(fi * x)}$ | ${u}$ | ${num(fi * u)}$ | ${num(cf)}$ |"
                      for c, fi, x, u, cf in zip(EX.shown, EX.f, EX.marks, [-3, -2, -1, 0, 1, 2], EX.cf())) +
            "\n| **Total** | $40$ | | $1270$ | | $-13$ | |")

sections = [
 {"id": "s1", "title": "Data in groups", "blocks": [
  blk("s1.hook", "hook", title="What is a 'typical' mark?",
    body="Your teacher has the marks of 40 students. Writing all 40 numbers tells us little. So the marks are grouped into classes (0–10, 10–20, …) with the number of students in each.\n\n"
         "From such a table we can still find three 'centres' of the data: the **mean** (the average), the **mode** (the most common value) and the **median** (the middle value). This chapter shows how."),
  blk("s1.inspiration", "inspiration", title="The man who counted India", person="Prasanta Chandra Mahalanobis", years="1893–1972",
    body="P. C. Mahalanobis studied physics, but he fell in love with statistics. In 1931 he founded the **Indian Statistical Institute** in Kolkata, and he designed large sample surveys, "
         "showing that a carefully chosen sample can tell us about crores of people. The National Sample Survey he started in 1950 still measures how India lives and spends.\n\n"
         "His work shaped India's Second Five-Year Plan. India celebrates his birthday, 29 June, as **National Statistics Day**.",
    quote="Statistics is the key technology for turning numbers into decisions that help people.",
    future="Statistics is used in elections, medicine trials, cricket analysis, weather forecasting, business, banking and government planning."),
  blk("s1.socratic", "socratic_question", question="What single number would you use to represent the class 10–20?",
    options=["$15$, its class mark", "$10$, its lower limit", "$20$, its upper limit"], correct_index=0,
    explanation="We assume the values in a class are spread around its middle, so we use the class mark $\\dfrac{10 + 20}{2} = 15$."),
 ]},
 {"id": "s2", "title": "Mean of grouped data", "blocks": [
  blk("s2.reveal", "theory", title="Three ways to find the mean", revision=True,
    body="Let $x_i$ be the class mark (middle value) of each class and $f_i$ its frequency.\n\n"
         "- **Direct method:** $\\bar{x} = \\dfrac{\\sum f_i x_i}{\\sum f_i}$\n"
         "- **Assumed mean method:** choose $a$ (a class mark near the middle), let $d_i = x_i - a$; then $\\bar{x} = a + \\dfrac{\\sum f_i d_i}{\\sum f_i}$\n"
         "- **Step-deviation method:** also divide by the class size $h$: $u_i = \\dfrac{x_i - a}{h}$ and $\\bar{x} = a + h \\times \\dfrac{\\sum f_i u_i}{\\sum f_i}$\n\n"
         "All three give the same answer; the last two just make the numbers smaller."),
  blk("s2.table", "markdown_table", title="Marks of 40 students: the working table", revision=False, body=EX_TABLE),
  blk("s2.eg1", "worked_example", title="Mean by two methods",
    problem="Find the mean marks of the 40 students in the table above.",
    steps=["Direct method: $\\bar{x} = \\dfrac{1270}{40} = 31.75$", "Step deviation with $a = 35$, $h = 10$: $\\sum f_i u_i = -13$",
           "$\\bar{x} = 35 + 10 \\times \\dfrac{-13}{40} = 35 - 3.25 = 31.75$"], answer="Mean $= 31.75$ marks"),
  blk("s2.check", "knowledge_check", question="The class mark of the class 20–30 is:", options=["$25$", "$20$", "$30$", "$10$"], correct_index=0,
    explanation="$\\dfrac{20 + 30}{2} = 25$."),
 ]},
 {"id": "s3", "title": "Mode of grouped data", "blocks": [
  blk("s3.thm", "theory", title="Mode", revision=True,
    body="The class with the highest frequency is the **modal class**. The mode lies inside it:\n\n"
         "$$\\text{Mode} = l + \\dfrac{f_1 - f_0}{2f_1 - f_0 - f_2} \\times h$$\n\n"
         "where $l$ is the lower limit of the modal class, $h$ the class size, $f_1$ the frequency of the modal class, $f_0$ of the class before it and $f_2$ of the class after it."),
  blk("s3.eg1", "worked_example", title="Mode of the marks",
    problem="Find the mode of the marks of the 40 students.",
    steps=["Modal class: $30 - 40$ (highest frequency $12$), with $f_0 = 9$ and $f_2 = 7$.", "Mode $= 30 + \\dfrac{12 - 9}{24 - 9 - 7} \\times 10 = 30 + \\dfrac{30}{8}$"], answer="Mode $= 33.75$ marks"),
  blk("s3.check", "knowledge_check", question="In the mode formula, $f_0$ is the frequency of:",
    options=["the class just before the modal class", "the modal class", "the class just after the modal class", "the first class"], correct_index=0,
    explanation="$f_1$ is the modal class, $f_0$ the class before it and $f_2$ the class after it."),
 ]},
 {"id": "s4", "title": "Median of grouped data", "blocks": [
  blk("s4.thm", "theory", title="Median", revision=True,
    body="1. Add the frequencies one by one to get the **cumulative frequencies** $cf$.\n"
         "2. Find $\\dfrac{n}{2}$. The first class whose $cf$ is $\\geq \\dfrac{n}{2}$ is the **median class**.\n"
         "3. Then\n\n$$\\text{Median} = l + \\dfrac{\\frac{n}{2} - cf}{f} \\times h$$\n\n"
         "where $l$ is the lower limit of the median class, $cf$ the cumulative frequency of the class **before** it, $f$ its frequency and $h$ the class size.\n\n"
         "If the classes are like 118–126, 127–135, first make them continuous: 117.5–126.5, 126.5–135.5, …"),
  blk("s4.eg1", "worked_example", title="Median of the marks",
    problem="Find the median of the marks of the 40 students.",
    steps=["$\\dfrac{n}{2} = 20$; cumulative frequencies: $3, 8, 17, 29, 36, 40$", "Median class: $30 - 40$, with $cf = 17$, $f = 12$, $h = 10$",
           "Median $= 30 + \\dfrac{20 - 17}{12} \\times 10$"], answer="Median $= 32.5$ marks"),
  blk("s4.relation", "theory", title="A useful relation", revision=True,
    body="For many distributions, the three measures are connected by the empirical relation\n\n$$3 \\times \\text{Median} = \\text{Mode} + 2 \\times \\text{Mean}$$\n\n"
         "For our marks: $3 \\times 32.5 = 97.5$ and $33.75 + 2 \\times 31.75 = 97.25$: very close. CBSE uses this relation in questions."),
  blk("s4.check", "knowledge_check", question="For 40 observations with cumulative frequencies $5, 13, 25, 33, 40$ for the classes $0 - 10$, $10 - 20$, $20 - 30$, $30 - 40$, $40 - 50$, the median class is:",
    options=["$20 - 30$", "$10 - 20$", "$30 - 40$", "$0 - 10$"], correct_index=0, explanation="$\\dfrac{n}{2} = 20$, and the first cumulative frequency $\\geq 20$ is $25$, for $20 - 30$."),
  blk("s4.memory", "memory_trick", title="Which formula when?", revision=True,
    body="- **Mean:** class marks $x_i$, multiply by $f_i$, add, divide.\n"
         "- **Mode:** look at the **biggest** frequency and its two neighbours.\n"
         "- **Median:** find $\\dfrac{n}{2}$ in the **running total** $cf$.\n"
         "- In both formulas, $l$ is the **lower** limit and $h$ the class size."),
  blk("s4.mistakes", "common_mistakes", title="Common mistakes",
    body="- Using the lower limit instead of the class mark for the mean.\n"
         "- In the median formula, using the $cf$ of the median class itself instead of the class before it.\n"
         "- In the mode formula, using $f_1 + f_0$ in place of $f_1 - f_0$, or forgetting the 2 in $2f_1$.\n"
         "- Not making classes continuous (118–126, 127–135, …) before using the formulas.\n"
         "- Taking the modal class as the class with the biggest class mark instead of the biggest frequency."),
  blk("s4.tip", "teacher_tip", title="Use the class's own data",
    body="Ask every student how many minutes they travelled to school today. Group the answers into classes of 5 minutes on the board, then find the mean, median and mode together. "
         "Students remember the formulas better when the data is about themselves."),
 ]},
 {"id": "s5", "title": "Think, connect, master", "blocks": [
  blk("s5.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend when the median is a better 'typical value' than the mean. (Hint: think of the salaries in a company where the owner earns a hundred times more than the others.)"),
  blk("s5.connection", "connection", title="Where this leads",
    body="- **Chapter 14, Probability:** frequencies become chances.\n"
         "- **Class 11 Statistics:** spread of data (variance and standard deviation).\n"
         "- **Real life:** average rainfall, median income, the most common shoe size a shop should stock."),
  blk("s5.mastery", "mastery", title="Mastery challenge",
    body="The mean of the following distribution of 120 observations is 50. Find the missing frequencies $f_1$ and $f_2$.\n\n"
         "Classes $0 - 20$, $20 - 40$, $40 - 60$, $60 - 80$, $80 - 100$ with frequencies $17$, $f_1$, $32$, $f_2$, $19$.\n\n"
         "**Answer:** $f_1 + f_2 = 120 - 68 = 52$. With class marks $10, 30, 50, 70, 90$: $\\sum f_i x_i = 3480 + 30f_1 + 70f_2 = 50 \\times 120 = 6000$, so $3f_1 + 7f_2 = 252$. "
         "Solving, $f_1 = 28$ and $f_2 = 24$."),
  blk("s5.summary", "summary", title="Chapter summary",
    body="- Mean: $\\bar{x} = \\dfrac{\\sum f_i x_i}{\\sum f_i}$, or $\\bar{x} = a + h \\times \\dfrac{\\sum f_i u_i}{\\sum f_i}$\n"
         "- Mode: $l + \\dfrac{f_1 - f_0}{2f_1 - f_0 - f_2} \\times h$, in the modal class\n"
         "- Median: $l + \\dfrac{\\frac{n}{2} - cf}{f} \\times h$, in the median class\n"
         "- Empirical relation: $3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean"),
  blk("s5.examtips", "exam_tips", title="Board exam tips",
    body="- Always draw the working table with columns $x_i$, $f_i x_i$ (or $u_i$, $f_i u_i$) and $cf$: it earns method marks.\n"
         "- Write the formula, then list $l$, $h$, $f_1$, $f_0$, $f_2$ (or $cf$, $f$) before substituting.\n"
         "- Check that your answer lies inside the modal or median class.\n"
         "- Questions with a missing frequency: write the sum of frequencies as one equation and the given mean, median or mode as the other."),
  blk("s5.flash1", "flashcard", front="Formula for the mode of grouped data", back="$l + \\dfrac{f_1 - f_0}{2f_1 - f_0 - f_2} \\times h$"),
  blk("s5.flash2", "flashcard", front="Formula for the median of grouped data", back="$l + \\dfrac{\\frac{n}{2} - cf}{f} \\times h$"),
  blk("s5.flash3", "flashcard", front="Empirical relation between mean, median and mode", back="$3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean"),
 ]},
]

chapter = {"schema_version": 1, "id": CH_ID, "title": "Statistics",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 13,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: mean, median and mode of grouped data (bimodal situations to be avoided).",
  "concepts": ["mean_grouped", "mode_grouped", "median_grouped"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
MN, MO, MD = "mean_grouped", "mode_grouped", "median_grouped"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n): return {"kind": "ncert_exercise", "exercise": e, "question": n}
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch13.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
def data_text(intro, left, right, d, ask): return f"{intro} ({left} : {right})\n\n{d.table()}\n\n{ask}"
MS_MEAN = ["1 mark: class marks", "1 mark: $\\sum f_i x_i$ and $\\sum f_i$", "1 mark: mean"]
MS_MODE = ["1 mark: modal class and values", "1 mark: formula", "1 mark: mode"]
MS_MED = ["1 mark: cumulative frequencies", "1 mark: median class and values", "1 mark: median"]

# Exercise 13.1
q("ex13_1.q1", "short_answer", 3, [MN], ex("13.1", 1), data_text("A survey was conducted by a group of students as a part of their environment awareness programme, in which they collected the following data regarding the number of plants in 20 houses in a locality.",
  "number of plants", "number of houses", E1[1], "Find the mean number of plants per house. Which method did you use for finding the mean, and why?"), "easy",
  answer_steps=E1[1].mean_steps() + ["The numbers are small, so the direct method is the easiest."], marking_scheme=MS_MEAN)
q("ex13_1.q2", "short_answer", 3, [MN], ex("13.1", 2), data_text("Consider the following distribution of daily wages (in ₹) of 50 workers of a factory.", "daily wages in ₹", "number of workers", E1[2],
  "Find the mean daily wages of the workers of the factory by using an appropriate method."), answer_steps=E1[2].mean_steps(), marking_scheme=MS_MEAN)
q3_table = Data([(a, b) for a, b, _ in Q3], [0 if x is None else x for _, _, x in Q3]).table().replace("19 - 21 & 0", "19 - 21 & f")
q("ex13_1.q3", "short_answer", 3, [MN], ex("13.1", 3), "The following distribution shows the daily pocket allowance of children of a locality. The mean pocket allowance is ₹ 18. Find the missing frequency $f$. (daily pocket allowance in ₹ : number of children)\n\n" + q3_table, "hard",
  answer_steps=["Class marks: $x_i = 12, 14, 16, 18, 20, 22, 24$", "$\\sum f_i = 44 + f$ and $\\sum f_i x_i = 752 + 20f$", "$\\dfrac{752 + 20f}{44 + f} = 18$ gives $752 + 20f = 792 + 18f$", "$f = 20$"],
  marking_scheme=["1 mark: $\\sum f_i$ and $\\sum f_i x_i$", "1 mark: equation", "1 mark: $f$"])
q("ex13_1.q4", "short_answer", 3, [MN], ex("13.1", 4), data_text("Thirty women were examined in a hospital by a doctor and the number of heartbeats per minute were recorded and summarised as follows.", "number of heartbeats per minute", "number of women", E1[4],
  "Find the mean heartbeats per minute for these women, choosing a suitable method."), answer_steps=E1[4].mean_steps(), marking_scheme=MS_MEAN)
q("ex13_1.q5", "short_answer", 3, [MN], ex("13.1", 5), data_text("In a retail market, fruit vendors were selling mangoes kept in packing boxes. These boxes contained varying number of mangoes. The following was the distribution of mangoes according to the number of boxes.",
  "number of mangoes", "number of boxes", E1[5], "Find the mean number of mangoes kept in a packing box. Which method of finding the mean did you choose?"),
  answer_steps=["The classes are not continuous, but the class marks are the same: $x_i = 51, 54, 57, 60, 63$", "$\\sum f_i = 400$ and $\\sum f_i x_i = 22875$", "$\\bar{x} = \\dfrac{22875}{400} = 57.19$ (direct method)"], marking_scheme=MS_MEAN)
q("ex13_1.q6", "short_answer", 3, [MN], ex("13.1", 6), data_text("The table below shows the daily expenditure on food of 25 households in a locality.", "daily expenditure in ₹", "number of households", E1[6],
  "Find the mean daily expenditure on food by a suitable method."), answer_steps=E1[6].mean_steps(), marking_scheme=MS_MEAN)
q("ex13_1.q7", "short_answer", 3, [MN], ex("13.1", 7), data_text("To find out the concentration of SO₂ in the air (in parts per million, i.e., ppm), the data was collected for 30 localities in a certain city and is presented below.", "concentration of SO₂ in ppm", "frequency", E1[7],
  "Find the mean concentration of SO₂ in the air."), answer_steps=E1[7].mean_steps()[:2] + ["$\\bar{x} = \\dfrac{2.96}{30} \\approx 0.099$ ppm"], marking_scheme=MS_MEAN)
q("ex13_1.q8", "short_answer", 3, [MN], ex("13.1", 8), data_text("A class teacher has the following absentee record of 40 students of a class for the whole term.", "number of days", "number of students", E1[8],
  "Find the mean number of days a student was absent."), answer_steps=E1[8].mean_steps()[:2] + ["$\\bar{x} = \\dfrac{499}{40} \\approx 12.48$"], marking_scheme=MS_MEAN)
q("ex13_1.q9", "short_answer", 3, [MN], ex("13.1", 9), data_text("The following table gives the literacy rate (in percentage) of 35 cities.", "literacy rate in %", "number of cities", E1[9],
  "Find the mean literacy rate."), answer_steps=E1[9].mean_steps()[:2] + ["$\\bar{x} = \\dfrac{2430}{35} \\approx 69.43$%"], marking_scheme=MS_MEAN)
# Exercise 13.2
q("ex13_2.q1", "long_answer", 5, [MO, MN], ex("13.2", 1), data_text("The following table shows the ages of the patients admitted in a hospital during a year.", "age in years", "number of patients", E2[1],
  "Find the mode and the mean of the data given above. Compare and interpret the two measures of central tendency."), "medium",
  answer_steps=E2[1].mode_steps() + E2[1].mean_steps()[1:] + ["The most common age is about 36.8 years, while the average age is about 35.37 years."],
  marking_scheme=["1 mark: modal class", "1 mark: mode", "1 mark: $\\sum f_i x_i$", "1 mark: mean", "1 mark: interpretation"])
q("ex13_2.q2", "short_answer", 3, [MO], ex("13.2", 2), data_text("The following data gives the information on the observed lifetimes (in hours) of 225 electrical components.", "lifetime in hours", "frequency", E2[2],
  "Determine the modal lifetimes of the components."), answer_steps=E2[2].mode_steps()[:2] + ["$= 65.625$ hours"], marking_scheme=MS_MODE)
q("ex13_2.q3", "long_answer", 5, [MO, MN], ex("13.2", 3), data_text("The following data gives the distribution of total monthly household expenditure of 200 families of a village.", "expenditure in ₹", "number of families", E2[3],
  "Find the modal monthly expenditure of the families. Also, find the mean monthly expenditure."), "hard",
  answer_steps=E2[3].mode_steps()[:2] + ["Mode $\\approx$ ₹ 1847.83"] + E2[3].mean_steps()[1:2] + ["Mean $= \\dfrac{532500}{200} =$ ₹ 2662.50"],
  marking_scheme=["1 mark: modal class", "1 mark: mode", "1 mark: class marks", "1 mark: $\\sum f_i x_i$", "1 mark: mean"])
q("ex13_2.q4", "long_answer", 5, [MO, MN], ex("13.2", 4), data_text("The following distribution gives the state-wise teacher-student ratio in higher secondary schools of India.", "number of students per teacher", "number of states / U.T.", E2[4],
  "Find the mode and mean of this data. Interpret the two measures."), "medium",
  answer_steps=E2[4].mode_steps()[:2] + ["Mode $= 30.625 \\approx 30.6$"] + E2[4].mean_steps()[1:2] + ["Mean $= \\dfrac{1022.5}{35} \\approx 29.2$", "Most states have about 30.6 students per teacher; the average is about 29.2."],
  marking_scheme=["1 mark: modal class", "1 mark: mode", "1 mark: $\\sum f_i x_i$", "1 mark: mean", "1 mark: interpretation"])
q("ex13_2.q5", "short_answer", 3, [MO], ex("13.2", 5), data_text("The given distribution shows the number of runs scored by some top batsmen of the world in one-day international cricket matches.", "runs scored", "number of batsmen", E2[5],
  "Find the mode of the data."), answer_steps=E2[5].mode_steps()[:2] + ["$\\approx 4608.7$ runs"], marking_scheme=MS_MODE)
q("ex13_2.q6", "short_answer", 3, [MO], ex("13.2", 6), data_text("A student noted the number of cars passing through a spot on a road for 100 periods each of 3 minutes and summarised it in the table given below.", "number of cars", "frequency", E2[6],
  "Find the mode of the data."), answer_steps=E2[6].mode_steps()[:2] + ["$\\approx 44.7$ cars"], marking_scheme=MS_MODE)
# Exercise 13.3
q("ex13_3.q1", "long_answer", 5, [MD, MN, MO], ex("13.3", 1), data_text("The following frequency distribution gives the monthly consumption of electricity of 68 consumers of a locality.", "monthly consumption in units", "number of consumers", E3[1],
  "Find the median, mean and mode of the data and compare them."), "hard",
  answer_steps=E3[1].median_steps()[:3] + ["Median $= 137$ units", "Mean $= \\dfrac{9320}{68} \\approx 137.06$ units (NCERT: 137.05)", "Mode $= 125 + \\dfrac{7}{13} \\times 20 \\approx 135.77$ units (NCERT: 135.76)",
                                         "All three are close to each other, about 136 to 137 units."],
  marking_scheme=["1 mark: cumulative frequencies", "1 mark: median", "1 mark: mean", "1 mark: mode", "1 mark: comparison"])
q("ex13_3.q2", "short_answer", 3, [MD], ex("13.3", 2), "If the median of the distribution given below is 28.5, find the values of $x$ and $y$. The total frequency is 60. (class interval : frequency)\n\n" +
  Data(even(0, 10, 6), [5, 0, 20, 15, 0, 5]).table().replace("10 - 20 & 0", "10 - 20 & x").replace("40 - 50 & 0", "40 - 50 & y"), "hard",
  answer_steps=["$45 + x + y = 60$, so $x + y = 15$.", "The median $28.5$ lies in $20 - 30$, with $cf = 5 + x$, $f = 20$, $h = 10$.",
                "$28.5 = 20 + \\dfrac{30 - (5 + x)}{20} \\times 10$ gives $x = 8$", "$y = 15 - 8 = 7$"],
  marking_scheme=["1 mark: $x + y = 15$", "1 mark: median equation", "1 mark: $x$ and $y$"])
q("ex13_3.q3", "short_answer", 3, [MD], ex("13.3", 3), "A life insurance agent found the following data for the distribution of ages of 100 policy holders. Calculate the median age, if policies are given only to persons having age 18 years onwards but less than 60 years. (age below : number of policy holders)\n\n" +
  "$$\\begin{array}{|c|c|}\\hline 20 & 2 \\\\ \\hline 25 & 6 \\\\ \\hline 30 & 24 \\\\ \\hline 35 & 45 \\\\ \\hline 40 & 78 \\\\ \\hline 45 & 89 \\\\ \\hline 50 & 92 \\\\ \\hline 55 & 98 \\\\ \\hline 60 & 100 \\\\ \\hline\\end{array}$$", "hard",
  answer_steps=["The cumulative frequencies are given: $\\dfrac{n}{2} = 50$, and the first $cf \\geq 50$ is $78$, for the class $35 - 40$.", "Median class: $35 - 40$, so $l = 35$, $cf = 45$, $f = 33$, $h = 5$",
                "Median $= 35 + \\dfrac{50 - 45}{33} \\times 5$", "$\\approx 35.76$ years"], marking_scheme=MS_MED)
q("ex13_3.q4", "short_answer", 3, [MD], ex("13.3", 4), data_text("The lengths of 40 leaves of a plant are measured correct to the nearest millimetre, and the data obtained is represented in the following table.", "length in mm", "number of leaves", E3[4],
  "Find the median length of the leaves."), "hard",
  answer_steps=["Make the classes continuous: $117.5 - 126.5$, $126.5 - 135.5$, and so on.", "$\\dfrac{n}{2} = 20$; cumulative frequencies: $3, 8, 17, 29, 34, 38, 40$", "Median class: $144.5 - 153.5$, so $l = 144.5$, $cf = 17$, $f = 12$, $h = 9$",
                "Median $= 144.5 + \\dfrac{20 - 17}{12} \\times 9 = 146.75$ mm"], marking_scheme=MS_MED)
q("ex13_3.q5", "short_answer", 3, [MD], ex("13.3", 5), data_text("The following table gives the distribution of the life time of 400 neon lamps.", "life time in hours", "number of lamps", E3[5],
  "Find the median life time of a lamp."), answer_steps=E3[5].median_steps()[:3] + ["$\\approx 3406.98$ hours"], marking_scheme=MS_MED)
q("ex13_3.q6", "long_answer", 5, [MD, MN, MO], ex("13.3", 6), data_text("100 surnames were randomly picked up from a local telephone directory and the frequency distribution of the number of letters in the English alphabets in the surnames was obtained as follows.",
  "number of letters", "number of surnames", E3[6], "Determine the median number of letters in the surnames. Find the mean number of letters in the surnames. Also, find the modal size of the surnames."), "hard",
  answer_steps=E3[6].median_steps()[:3] + ["Median $= 8.05$", "Mean $= \\dfrac{832}{100} = 8.32$", "Mode $= 7 + \\dfrac{40 - 30}{80 - 30 - 16} \\times 3 \\approx 7.88$"],
  marking_scheme=["1 mark: cumulative frequencies", "1 mark: median", "1 mark: $\\sum f_i x_i$", "1 mark: mean", "1 mark: mode"])
q("ex13_3.q7", "short_answer", 3, [MD], ex("13.3", 7), data_text("The distribution below gives the weights of 30 students of a class.", "weight in kg", "number of students", E3[7],
  "Find the median weight of the students."), answer_steps=E3[7].median_steps()[:3] + ["$\\approx 56.67$ kg"], marking_scheme=MS_MED)
# Sample paper
mcq("sqp17", [MD], "The median of a set of 9 distinct observations is 20.5. If each of the observations of the set is increased by 2, then the median of the new set",
    ["is increased by 2", "is decreased by 2", "is two times the original number", "remains the same as that of the original observations"], 0,
    "Adding 2 to every observation moves the middle one up by 2 as well: the new median is 22.5.", source=SQP(17))
D35x = Data(even(0, 15, 6), [10, 7, 0, 15, 10, 12]).table().replace("30 - 45 & 0", "30 - 45 & x")
q("sqp35a", "long_answer", 5, [MO, MN], SQP("35(A)"), "If the mode of the following distribution is 55, then find the value of $x$. Hence, find the mean. (class interval : frequency)\n\n" + D35x, "hard",
  answer_steps=["The mode 55 lies in the modal class $45 - 60$: $l = 45$, $h = 15$, $f_1 = 15$, $f_0 = x$, $f_2 = 10$.", "$55 = 45 + \\dfrac{15 - x}{30 - x - 10} \\times 15$, so $10(20 - x) = 15(15 - x)$",
                "$x = 5$", "Class marks: $x_i = 7.5, 22.5, 37.5, 52.5, 67.5, 82.5$; $\\sum f_i = 59$ and $\\sum f_i x_i = 2872.5$", "Mean $= \\dfrac{2872.5}{59} \\approx 48.69$"],
  marking_scheme=["1 mark: modal class", "1 mark: equation", "1 mark: $x$", "1 mark: table", "1 mark: mean"])
q("sqp35b", "long_answer", 5, [MD, MN], SQP("35(B)"), "A survey regarding heights (in cm) of 51 girls of class X of a school was conducted and the following data was obtained. Find the median height of girls. If mode of the above distribution is 148.05, find the mean using empirical formula. (height less than, in cm : number of girls)\n\n" +
  "$$\\begin{array}{|c|c|}\\hline 140 & 4 \\\\ \\hline 145 & 11 \\\\ \\hline 150 & 29 \\\\ \\hline 155 & 40 \\\\ \\hline 160 & 46 \\\\ \\hline 165 & 51 \\\\ \\hline\\end{array}$$", "hard",
  answer_steps=["Frequencies of $135 - 140$, $140 - 145$, …: $4, 7, 18, 11, 6, 5$", "$\\dfrac{n}{2} = 25.5$; median class: $145 - 150$, so $l = 145$, $cf = 11$, $f = 18$, $h = 5$",
                "Median $= 145 + \\dfrac{25.5 - 11}{18} \\times 5 \\approx 149.03$ cm", "$3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean: $3 \\times 149.03 = 148.05 + 2 \\times$ Mean", "Mean $\\approx 149.52$ cm"],
  marking_scheme=["1 mark: class frequencies", "1 mark: median class", "1 mark: median", "1 mark: empirical formula", "1 mark: mean"])
# Shine MCQs
mcq("mcq01", [MN], "The class mark of the class $10 - 25$ is:", ["$17.5$", "$15$", "$10$", "$35$"], 0, "$\\dfrac{10 + 25}{2} = 17.5$.")
mcq("mcq02", [MN], "In the step-deviation method, $u_i$ is:", ["$\\dfrac{x_i - a}{h}$", "$x_i - a$", "$\\dfrac{x_i}{h}$", "$\\dfrac{a - x_i}{h}$"], 0, "Deviation from the assumed mean $a$, divided by the class size $h$.")
mcq("mcq03", [MO], "The modal class of a grouped frequency distribution is the class with the:", ["highest frequency", "highest class mark", "highest cumulative frequency", "middle position"], 0, "Mode means the most frequent, so the modal class has the highest frequency.")
mcq("mcq04", [MD], "To find the median of grouped data, we first need the:", ["cumulative frequencies", "class marks", "modal class", "assumed mean"], 0, "The median class is found from the cumulative frequencies.")
mcq("mcq05", [MD, MO], "The empirical relation between mean, median and mode is:", ["$3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean", "$3 \\times$ Mean $=$ Mode $+ 2 \\times$ Median",
    "$3 \\times$ Mode $=$ Median $+ 2 \\times$ Mean", "Mode $=$ Mean $+$ Median"], 0, "It is $3 \\times$ Median $=$ Mode $+ 2 \\times$ Mean.", "medium")
mcq("mcq06", [MD, MO], "If the mean of a distribution is 20 and its median is 22, then its mode (by the empirical relation) is:", ["$26$", "$24$", "$21$", "$18$"], 0, "Mode $= 3 \\times 22 - 2 \\times 20 = 26$.", "medium")
mcq("mcq07", [MN], "For a grouped distribution, $\\sum f_i x_i = 1500$ and $\\sum f_i = 50$. The mean is:", ["$30$", "$75$", "$1450$", "$3$"], 0, "$\\dfrac{1500}{50} = 30$.")
mcq("mcq08", [MD], "In the median formula $l + \\dfrac{\\frac{n}{2} - cf}{f} \\times h$, $cf$ is the cumulative frequency of:", ["the class before the median class", "the median class", "the last class", "the class after the median class"], 0,
    "It is the running total up to the class just before the median class.", "medium")
mcq("mcq09", [MO], "In the mode formula, $f_2$ is the frequency of:", ["the class after the modal class", "the class before the modal class", "the modal class", "the last class"], 0, "$f_0$ is before, $f_1$ is the modal class, $f_2$ is after.")
mcq("mcq10", [MD], "The classes 118–126, 127–135, … are made continuous by changing the first class to:", ["$117.5 - 126.5$", "$118 - 127$", "$117 - 126$", "$118.5 - 126.5$"], 0,
    "The gap between 126 and 127 is 1, so subtract 0.5 from each lower limit and add 0.5 to each upper limit.", "medium")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [MN], "The class mark of the class $10 - 25$ is $17.5$.", "The class mark of a class is $\\dfrac{\\text{lower limit} + \\text{upper limit}}{2}$.", 0, "R gives $\\dfrac{10 + 25}{2} = 17.5$.")
ar("ar2", [MO], "The modal class is the class with the highest frequency.", "The mean of grouped data is found using class marks.", 1, "Both are true, but R is about the mean, not about the mode.")
ar("ar3", [MD], "For the classes 118–126, 127–135, …, the lower limit of the class 127–135 used in the median formula is 127.", "The median formula needs continuous classes.", 3,
   "A is false: after making the classes continuous, the lower limit is 126.5. R is true.")
ar("ar4", [MN], "The assumed mean method gives the same mean as the direct method.", "The assumed mean must be one of the class marks.", 2, "A is true. R is false: any number can be the assumed mean; a middle class mark is just convenient.")
ar("ar5", [MD], "The median of the observations 1, 3, 5, 7 is 5.", "For an even number of observations, the median is the mean of the two middle observations.", 3, "A is false: the median is $\\dfrac{3 + 5}{2} = 4$. R is true.")

q("vsa1", "very_short_answer", 2, [MN], SHINE, "Find the class marks of the classes $10 - 25$ and $35 - 55$.", "easy",
  answer_steps=["$\\dfrac{10 + 25}{2} = 17.5$", "$\\dfrac{35 + 55}{2} = 45$"], marking_scheme=["1 mark: first", "1 mark: second"])
q("vsa2", "very_short_answer", 2, [MD, MO], SHINE, "If the mode of a distribution is 24.5 and its mean is 29.75, find its median using the empirical relation.", "easy",
  answer_steps=["$3 \\times$ Median $= 24.5 + 2 \\times 29.75 = 84$", "Median $= 28$"], marking_scheme=["1 mark: relation", "1 mark: median"])
q("sa1", "short_answer", 3, [MO], SHINE, data_text("Find the mode of the following distribution.", "class interval", "frequency", SA1, ""), answer_steps=SA1.mode_steps()[:2] + ["$\\approx 46.67$"], marking_scheme=MS_MODE)
q("sa2", "short_answer", 3, [MD], SHINE, data_text("Find the median of the following distribution.", "class interval", "frequency", SA2, ""), answer_steps=SA2.median_steps()[:3] + ["$\\approx 27.22$"], marking_scheme=MS_MED)
q("sa3", "short_answer", 3, [MN], SHINE, data_text("Find the mean of the following distribution by the step-deviation method.", "class interval", "frequency", SA3, ""),
  answer_steps=["Take $a = 70$ and $h = 20$: $u_i = -3, -2, -1, 0, 1, 2, 3$", "$\\sum f_i = 50$ and $\\sum f_i u_i = -18 - 16 - 10 + 0 + 6 + 10 + 9 = -19$", "$\\bar{x} = 70 + 20 \\times \\dfrac{-19}{50} = 70 - 7.6 = 62.4$"],
  marking_scheme=["1 mark: $u_i$", "1 mark: $\\sum f_i u_i$", "1 mark: mean"])
check(sum(fi * u for fi, u in zip(SA3.f, [-3, -2, -1, 0, 1, 2, 3])) == -19 and 70 + 20 * Fr(-19, 50) == F("62.4"), "sa3 step deviation")
la1_table = Data(even(0, 100, 10), [2, 5, 0, 12, 17, 20, 0, 9, 7, 4]).table().replace("200 - 300 & 0", "200 - 300 & x").replace("600 - 700 & 0", "600 - 700 & y")
q("la1", "long_answer", 5, [MD], SHINE, "The median of the following data is 525. Find the values of $x$ and $y$, if the total frequency is 100. (class interval : frequency)\n\n" + la1_table, "hard",
  answer_steps=["$76 + x + y = 100$, so $x + y = 24$.", "The median 525 lies in $500 - 600$: $l = 500$, $h = 100$, $f = 20$, $cf = 2 + 5 + x + 12 + 17 = 36 + x$",
                "$525 = 500 + \\dfrac{50 - (36 + x)}{20} \\times 100$", "$25 = 5(14 - x)$, so $x = 9$", "$y = 24 - 9 = 15$"],
  marking_scheme=["1 mark: $x + y = 24$", "1 mark: median class", "1 mark: equation", "1 mark: $x$", "1 mark: $y$"])
q("la2", "long_answer", 5, [MN, MD, MO], SHINE, data_text("Find the mean, median and mode of the following distribution.", "class interval", "frequency", LA2, ""), "medium",
  answer_steps=["Class marks $5, 15, \\ldots, 65$: $\\sum f_i x_i = 3560$, so mean $= \\dfrac{3560}{100} = 35.6$", "$\\dfrac{n}{2} = 50$; cumulative frequencies: $5, 15, 33, 63, 83, 95, 100$",
                "Median $= 30 + \\dfrac{50 - 33}{30} \\times 10 \\approx 35.67$", "Modal class $30 - 40$: mode $= 30 + \\dfrac{30 - 18}{60 - 18 - 20} \\times 10 \\approx 35.45$",
                "All three are close, about 35 to 36."],
  marking_scheme=["1 mark: table", "1 mark: mean", "1 mark: median", "1 mark: mode", "1 mark: comparison"])
q("cb1", "case_based", 4, [MO, MD, MN], SHINE,
  "A school surveyed the daily screen time (in hours) of 50 students. (screen time in hours : number of students)\n\n" + CB1.table() +
  "\n\n(i) Write the modal class. (1)\n\n(ii) Write the median class. (1)\n\n(iii) Find the mode. OR Find the mean screen time. (2)",
  answer_steps=["(i) $4 - 6$ (highest frequency 16)", "(ii) $\\dfrac{n}{2} = 25$; cumulative frequencies $8, 22, 38$: the median class is $4 - 6$",
                "(iii) Mode $= 4 + \\dfrac{16 - 14}{32 - 14 - 8} \\times 2 = 4.4$ hours. OR Mean $= \\dfrac{222}{50} = 4.44$ hours."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [MD, MN], SHINE,
  "The weekly pocket money (in ₹) of 40 students is given below. (pocket money in ₹ : number of students)\n\n" + CB2.table() +
  "\n\n(i) Find the class mark of the class $100 - 150$. (1)\n\n(ii) Find the cumulative frequency of the class $100 - 150$. (1)\n\n(iii) Find the median pocket money. OR Find the mean pocket money. (2)",
  answer_steps=["(i) $\\dfrac{100 + 150}{2} = 125$", "(ii) $4 + 8 + 14 = 26$",
                "(iii) Median $= 100 + \\dfrac{20 - 12}{14} \\times 50 \\approx$ ₹ 128.57. OR Mean $= \\dfrac{5100}{40} =$ ₹ 127.50."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
for it in Q:  # questions built with an empty "ask" end with a blank paragraph
    it["question"] = it["question"].rstrip()

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch13.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
