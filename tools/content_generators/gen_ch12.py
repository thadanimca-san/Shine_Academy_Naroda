"""CBSE Class 10 Maths Ch 12: Surface Areas and Volumes.
Numerical answers are checked with exact fractions; figures are side views of
the solids drawn to scale."""
import json, math, os, sys
from collections import Counter
from fractions import Fraction as Fr

ROOT = sys.argv[1]
CH_ID = "cbse.c10.maths.ncert_rationalised.ch12"
PATH = "app_core/content/cbse/class10/maths/ncert_rationalised/ch12_surface_areas_and_volumes"
P7, P314 = Fr(22, 7), Fr(314, 100)

def check(cond, msg):
    if not cond: raise SystemExit("WRONG ANSWER: " + msg)
def near(value, target, tol=0.005): return abs(float(value) - target) < tol
def F(x): return Fr(x) if not isinstance(x, float) else Fr(str(x))

# ---------------------------------------------------------------- verification
check(2 * (8 * 4 + 4 * 4 + 8 * 4) == 160 and 4 ** 3 == 64, "12.1 Q1")
check(2 * P7 * 7 * 6 + 2 * P7 * 49 == 572, "12.1 Q2")
check(F(12) ** 2 + F(3.5) ** 2 == F(12.5) ** 2 and P7 * F(3.5) * F(12.5) + 2 * P7 * F(3.5) ** 2 == F(214.5), "12.1 Q3")
check(6 * 49 + P7 * F(3.5) ** 2 == F(332.5), "12.1 Q4")
check(2 * P7 * F(2.5) * (9 + 5) == 220, "12.1 Q6")
check(2 * P7 * 2 * F(2.1) == F(26.4) and P7 * 2 * F(2.8) == F(17.6) and F(26.4) + F(17.6) == 44 and 44 * 500 == 22000, "12.1 Q7")
check(F(2.4) ** 2 + F(0.7) ** 2 == F(2.5) ** 2 and P7 * F(0.7) * (F(4.8) + F(0.7) + F(2.5)) == F(17.6), "12.1 Q8")
check(2 * P7 * F(3.5) * (10 + 7) == 374, "12.1 Q9")
check(Fr(1, 3) + Fr(2, 3) == 1, "12.2 Q1: volume π")
check(P7 * F(1.5) ** 2 * (8 + Fr(4, 3)) == 66, "12.2 Q2")
gj = P7 * F(1.4) ** 2 * (F(2.2) + Fr(4, 3) * F(1.4))
check(near(gj * 45 * F(0.3), 338.18), "12.2 Q3")
check(525 - 4 * Fr(1, 3) * P7 * F(0.25) * F(1.4) == Fr(7853, 15) and near(Fr(7853, 15), 523.53), "12.2 Q4")
check((Fr(1, 4) * Fr(1, 3) * 25 * 8) / (Fr(4, 3) * F(0.5) ** 3) == 100, "12.2 Q5")
check(P314 * (144 * 220 + 64 * 60) == F(111532.8) and F(111532.8) * 8 / 1000 == F(892.2624), "12.2 Q6")
check(3600 * 180 - (Fr(1, 3) * 3600 * 120 + Fr(2, 3) * 60 ** 3) == 360000 and near(P7 * 360000, 1131428.57), "12.2 Q7")
v8 = P314 * 8 + Fr(4, 3) * P314 * F(4.25) ** 3
check(near(v8, 346.51) and v8 != 345, "12.2 Q8")
check(Fr(85) / (Fr(1, 3) * 51) == 5, "sqp11")
check(12 ** 2 + 6 ** 2 == 180 and 12 * math.sqrt(180) == 72 * math.sqrt(5) and 144 - 16 + 16 + 2 * 4 * 3 == 168, "sqp34a: (168 + 72√5)π")
check(Fr(5, 6) * Fr(1, 3) * 9 * 12 + Fr(2, 3) * 27 == 48 and near(48 * P7, 150.86), "sqp34b: 48π")
check(150 + P7 * F(2.1) ** 2 == F(163.86), "Example 2")
check(near(P314 * F(2.5) ** 2 * 10, 196.25) and near(Fr(2, 3) * P314 * F(2.5) ** 3, 32.71) and near(F(196.25) - F(32.71), 163.54), "Example 6")
toy = Fr(2, 3) * P314 * 8 + Fr(1, 3) * P314 * 4 * 2
check(toy == F(25.12) and P314 * 4 * 4 - toy == F(25.12), "Example 7")
check(2 * (50 + 25 + 50) == 250, "mcq01"); check(6 ** 2 + 8 ** 2 == 10 ** 2, "mcq06")
check(2 * P7 * 49 == 308 and 4 * P7 * F(3.5) ** 2 == 154, "mcq05, mcq07")
check(P7 * 49 * 10 - Fr(1, 3) * P7 * 49 * 10 == Fr(3080, 3), "mcq10")
check(2 * (8 * 4 + 4 * 4 + 8 * 4) != 192 and 5 ** 2 + 12 ** 2 == 13 ** 2, "ar3, ar4")
check(Fr(2, 3) * P7 * F(2.1) ** 3 == F(19.404), "vsa1"); check(P7 * 7 * 25 == 550 and 7 ** 2 + 24 ** 2 == 625, "vsa2")
check(P7 * (Fr(1, 3) * 49 * 24 + Fr(2, 3) * 343) == Fr(40964, 21) and near(Fr(40964, 21), 1950.67), "sa1")
check(3 ** 2 + 4 ** 2 == 25 and 3 * (3 + 16 + 5) == 72 and near(72 * P7, 226.29), "sa2")
check(Fr(144) * F(6.75) * Fr(3, 4) == 729 and 9 ** 3 == 729, "sa3")
check(Fr(1408, 21) * Fr(81, 8) / P7 == 216 and 6 ** 3 == 216, "la2: H = 6 m")
check(near(Fr(2, 3) * P7 * F(3.5) ** 3, 89.83) and Fr(1, 3) * P7 * F(3.5) ** 2 * 12 == 154 and near(154 + Fr(2, 3) * P7 * F(3.5) ** 3, 243.83) and P7 * F(3.5) * F(12.5) == F(137.5), "cb1")
check(2 * P7 * 7 * 3 == 132 and P7 * 7 * 10 == 220 and 352 * 100 == 35200 and near(math.sqrt(51), 7.14), "cb2")

# ---------------------------------------------------------------- figures
def r9(p): return [round(p[0], 9), round(p[1], 9)]
def fig(title, points, segments, **kw):
    f = {"type": "geometry_figure", "title": title, "points": {k: r9(v) for k, v in points.items()}, "segments": segments}
    f.update(kw); return f
def arc(kind, centre, a, b): return {"kind": kind, "centre": centre, "from": a, "to": b}
def L(a, b, label): return {"from": a, "to": b, "label": label}

def cone_on_hemisphere(title, r, h, labels):
    return fig(title, {"O": (0, 0), "A": (-r, 0), "B": (r, 0), "V": (0, h)},
               [["V", "A"], ["V", "B"], {"from": "A", "to": "B", "dashed": True}, {"from": "O", "to": "V", "dashed": True}],
               shaded=[arc("arc", "O", "A", "B")], right_angles=[["V", "O", "B"]], lengths=[L("O", "V", labels[0]), L("O", "B", labels[1])])
FIG_TOP = cone_on_hemisphere("Side view of the top", 1.75, 3.25, ["3.25 cm", "1.75 cm"])
FIG_TOY = cone_on_hemisphere("Side view of the toy", 3.5, 12, ["12 cm", "3.5 cm"])
FIG_CUBE = fig("A hemisphere on a cube", {"A": (0, 0), "B": (5, 0), "C": (5, 5), "D": (0, 5), "M": (2.5, 5), "P": (0.4, 5), "Q": (4.6, 5)},
               [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]], shaded=[arc("segment", "M", "Q", "P")], lengths=[L("A", "B", "5 cm"), L("P", "Q", "4.2 cm")])
FIG_GLASS = fig("Glass with a raised hemispherical bottom", {"A": (-2.5, 0), "B": (2.5, 0), "C": (2.5, 10), "D": (-2.5, 10), "O": (0, 0)},
                [["A", "B"], ["B", "C"], ["D", "A"], {"from": "C", "to": "D", "dashed": True}], shaded=[arc("segment", "O", "B", "A")],
                lengths=[L("B", "C", "10 cm"), L("A", "B", "5 cm")])
FIG_CAPSULE = fig("Side view of the capsule", {"A": (-4.5, -2.5), "B": (4.5, -2.5), "C": (4.5, 2.5), "D": (-4.5, 2.5), "M": (-4.5, 0), "N": (4.5, 0), "L": (-7, 0), "R": (7, 0)},
                  [["A", "B"], ["D", "C"], {"from": "L", "to": "R", "dashed": True}],
                  shaded=[arc("arc", "N", "B", "C"), arc("arc", "M", "D", "A")], lengths=[L("L", "R", "14 mm"), L("D", "A", "5 mm")], labels={"M": "", "N": ""})
TENT_H = math.sqrt(2.8 ** 2 - 2 ** 2)
FIG_TENT = fig("Side view of the tent", {"A": (-2, 0), "B": (2, 0), "C": (2, 2.1), "D": (-2, 2.1), "V": (0, 2.1 + TENT_H)},
               [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], ["D", "V"], ["V", "C"]], lengths=[L("A", "B", "4 m"), L("B", "C", "2.1 m"), L("D", "V", "2.8 m")])
FIG_VESSEL = fig("Hemisphere with a cylinder on it", {"O": (0, 0), "A": (-7, 0), "B": (7, 0), "C": (7, 6), "D": (-7, 6)},
                 [["B", "C"], ["D", "A"], {"from": "A", "to": "B", "dashed": True}], shaded=[arc("arc", "O", "A", "B")], lengths=[L("A", "B", "14 cm"), L("B", "C", "6 cm")])
FIG_HOLLOW = fig("Conical cavity in a cylinder", {"A": (-0.7, 0), "B": (0.7, 0), "C": (0.7, 2.4), "D": (-0.7, 2.4), "V": (0, 2.4)},
                 [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], {"from": "A", "to": "V", "dashed": True}, {"from": "B", "to": "V", "dashed": True}],
                 lengths=[L("B", "C", "2.4 cm"), L("A", "B", "1.4 cm")])
FIG_SCOOP = fig("Hemispheres scooped out of a cylinder", {"A": (-3.5, 0), "B": (3.5, 0), "C": (3.5, 10), "D": (-3.5, 10), "M": (0, 0), "N": (0, 10)},
                [["B", "C"], ["D", "A"]], shaded=[arc("arc", "M", "B", "A"), arc("arc", "N", "D", "C")], lengths=[L("B", "C", "10 cm")], labels={"M": "", "N": ""})
FIG_ICE = fig("Ice-cream cone", {"V": (0, 0), "A": (-3, 12), "B": (3, 12), "O": (0, 12)},
              [["V", "A"], ["V", "B"], {"from": "A", "to": "B", "dashed": True}, {"from": "V", "to": "O", "dashed": True}],
              shaded=[arc("segment", "O", "B", "A")], right_angles=[["V", "O", "B"]], lengths=[L("V", "O", "12 cm"), L("O", "B", "3 cm")])
FIG_SQP34 = fig("Cylindrical cavity in a cone", {"A": (-12, 0), "B": (12, 0), "V": (0, 6), "P": (-4, 0), "Q": (4, 0), "R": (4, 3), "S": (-4, 3), "O": (0, 0)},
                [["A", "B"], ["V", "A"], ["V", "B"], {"from": "Q", "to": "R", "dashed": True}, {"from": "R", "to": "S", "dashed": True}, {"from": "S", "to": "P", "dashed": True}],
                right_angles=[["P", "Q", "R"]], lengths=[L("O", "B", "12 cm"), L("Q", "R", "3 cm")], labels={"O": ""})
FIG_MODEL = fig("Rachel's model", {"L": (-6, 0), "R": (6, 0), "A": (-4, -1.5), "B": (4, -1.5), "C": (4, 1.5), "D": (-4, 1.5)},
                [["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"], ["L", "A"], ["L", "D"], ["R", "B"], ["R", "C"]], lengths=[L("A", "B", "8 cm"), L("B", "C", "3 cm")])

# ---------------------------------------------------------------- learn content
def blk(id_, type_, **kw): return {"id": f"ch12.{id_}", "type": type_, **kw}
def placed(id_, figure): return {"id": f"ch12.{id_}", **figure}

sections = [
 {"id": "s1", "title": "Solids made of solids", "blocks": [
  blk("s1.hook", "hook", title="What shape is an ice-cream cone?",
    body="An ice-cream cone is a **cone** with a **hemisphere** of ice-cream on top. A medicine capsule is a **cylinder** with a hemisphere at each end. A tent is a cylinder with a cone on top.\n\n"
         "Most things around us are made by joining simple solids. In this chapter you will find how much material covers them (**surface area**) and how much they hold (**volume**)."),
  blk("s1.inspiration", "inspiration", title="The sphere in a poem", person="Bhaskaracharya", years="1114–1185 CE",
    body="Bhaskaracharya (Bhaskara II) of Ujjain wrote the *Lilavati*, a mathematics book in verse, said to be named after his daughter. Its problems were set as puzzles about bees, peacocks and lotuses.\n\n"
         "In it he gave the rules we still use: the surface of a sphere is **four times** the area of its largest circle, and the volume of a sphere is its surface multiplied by the diameter and divided by six. "
         "In today's symbols: $4\\pi r^{2}$ and $4\\pi r^{2} \\times \\dfrac{2r}{6} = \\dfrac{4}{3}\\pi r^{3}$.",
    quote="A difficult idea becomes easy when it is taught with love and a good example.",
    future="Engineers use these formulas to design water tanks, silos, domes, rockets, capsules and packaging, and to estimate material and cost."),
  blk("s1.socratic", "socratic_question", question="A cone is stuck on a hemisphere of the same radius to make a toy. Which surface of the two pieces can no longer be seen?",
    options=["The two circular bases", "The curved surface of the cone", "The curved surface of the hemisphere"], correct_index=0,
    explanation="The flat circular bases are glued together and hidden. Only the two curved surfaces are on the outside."),
 ]},
 {"id": "s2", "title": "Surface area of a combination", "blocks": [
  blk("s2.table", "markdown_table", title="Formulas you need", revision=True,
    body="| Solid | Curved / lateral surface area | Total surface area | Volume |\n|---|---|---|---|\n"
         "| Cuboid $l \\times b \\times h$ | $2h(l + b)$ | $2(lb + bh + hl)$ | $lbh$ |\n"
         "| Cube of edge $a$ | $4a^{2}$ | $6a^{2}$ | $a^{3}$ |\n"
         "| Cylinder | $2\\pi r h$ | $2\\pi r(r + h)$ | $\\pi r^{2} h$ |\n"
         "| Cone | $\\pi r l$ | $\\pi r(l + r)$ | $\\dfrac{1}{3}\\pi r^{2} h$ |\n"
         "| Sphere | $4\\pi r^{2}$ | $4\\pi r^{2}$ | $\\dfrac{4}{3}\\pi r^{3}$ |\n"
         "| Hemisphere | $2\\pi r^{2}$ | $3\\pi r^{2}$ | $\\dfrac{2}{3}\\pi r^{3}$ |\n\n"
         "For a cone, the slant height is $l = \\sqrt{r^{2} + h^{2}}$."),
  blk("s2.reveal", "theory", title="Add only what you can see", revision=True,
    body="When solids are joined, the faces that are glued together are hidden. So:\n\n"
         "**Surface area of the combination = sum of the surface areas of the parts that are on the outside.**\n\n"
         "For a cone on a hemisphere: TSA $= \\pi r l + 2\\pi r^{2}$. For a capsule: TSA $= 2\\pi r h + 4\\pi r^{2}$. "
         "When a hemisphere is placed on a cube, the circle it covers is lost from the cube, but the hemisphere's curved surface is added."),
  blk("s2.eg1", "worked_example", title="NCERT Example 1",
    problem="Rasheed got a playing top (lattu) as his birthday present: a cone surmounted by a hemisphere. The entire top is 5 cm in height and the diameter of the top is 3.5 cm. Find the area he has to colour. (Take $\\pi = \\dfrac{22}{7}$)",
    steps=["Radius $r = 1.75$ cm. Hemisphere: $2\\pi r^{2} = 2 \\times \\dfrac{22}{7} \\times 1.75 \\times 1.75 = 19.25$ cm²",
           "Cone: height $= 5 - 1.75 = 3.25$ cm, slant height $l = \\sqrt{1.75^{2} + 3.25^{2}} \\approx 3.7$ cm",
           "Curved surface of the cone $= \\pi r l = \\dfrac{22}{7} \\times 1.75 \\times 3.7 \\approx 20.35$ cm²", "Total $= 19.25 + 20.35$"],
    answer="$39.6$ cm² (approx.)"),
  placed("s2.fig", FIG_TOP),
  blk("s2.eg2", "worked_example", title="NCERT Example 2",
    problem="A decorative block is made of a cube of edge 5 cm and a hemisphere fixed on top, of diameter 4.2 cm. Find the total surface area of the block. (Take $\\pi = \\dfrac{22}{7}$)",
    steps=["Cube: $6 \\times 5 \\times 5 = 150$ cm²", "The hemisphere hides a circle of area $\\pi r^{2}$ and adds its curved surface $2\\pi r^{2}$: a net gain of $\\pi r^{2}$.",
           "$\\pi r^{2} = \\dfrac{22}{7} \\times 2.1 \\times 2.1 = 13.86$ cm²", "Total $= 150 + 13.86$"],
    answer="$163.86$ cm²"),
  placed("s2.fig2", FIG_CUBE),
  blk("s2.check", "knowledge_check", question="Two cubes of edge 5 cm are joined end to end. The surface area of the cuboid formed is:",
    options=["$250$ cm²", "$300$ cm²", "$150$ cm²", "$125$ cm²"], correct_index=0, explanation="The cuboid is $10 \\times 5 \\times 5$: $2(50 + 25 + 50) = 250$ cm²."),
 ]},
 {"id": "s3", "title": "Volume of a combination", "blocks": [
  blk("s3.discovery", "discovery", title="Volumes simply add",
    body="Surface area needs care because glued faces disappear. Volume is easier: the space inside the combination is the space inside the parts put together. "
         "And when a part is **cut out** (a cavity), its volume is **subtracted**."),
  blk("s3.thm", "theory", title="Volume of a combination", revision=True,
    body="- Joined solids: volume $=$ sum of the volumes of the parts.\n"
         "- Solid with a cavity: volume $=$ volume of the solid $-$ volume of the cavity.\n\n"
         "Examples: capsule $= \\pi r^{2} h + \\dfrac{4}{3}\\pi r^{3}$; cone on a hemisphere $= \\dfrac{1}{3}\\pi r^{2} h + \\dfrac{2}{3}\\pi r^{3}$."),
  blk("s3.eg1", "worked_example", title="NCERT Example 6",
    problem="A juice seller serves his customers in glasses with an inner diameter of 5 cm, but the bottom of each glass has a raised hemispherical portion. The height of a glass is 10 cm. Find the apparent capacity of the glass and its actual capacity. (Use $\\pi = 3.14$)",
    steps=["Apparent capacity $= \\pi r^{2} h = 3.14 \\times 2.5 \\times 2.5 \\times 10 = 196.25$ cm³",
           "The raised hemisphere takes up $\\dfrac{2}{3}\\pi r^{3} = \\dfrac{2}{3} \\times 3.14 \\times 2.5 \\times 2.5 \\times 2.5 \\approx 32.71$ cm³", "Actual capacity $= 196.25 - 32.71$"],
    answer="$196.25$ cm³ and $163.54$ cm³"),
  placed("s3.fig", FIG_GLASS),
  blk("s3.eg2", "worked_example", title="CBSE sample paper",
    problem="An empty cone of radius 3 cm and height 12 cm is filled with ice-cream such that the lower part of the cone, which is $\\dfrac{1}{6}$th of the volume of the cone, is unfilled but a hemisphere is formed on the top. Find the volume of the ice-cream.",
    steps=["Volume of the cone $= \\dfrac{1}{3}\\pi \\times 3 \\times 3 \\times 12 = 36\\pi$ cm³", "Ice-cream in the cone $= \\dfrac{5}{6} \\times 36\\pi = 30\\pi$ cm³",
           "Hemisphere $= \\dfrac{2}{3}\\pi \\times 3^{3} = 18\\pi$ cm³", "Total $= 30\\pi + 18\\pi = 48\\pi$ cm³"],
    answer="$48\\pi \\approx 150.86$ cm³"),
  placed("s3.fig2", FIG_ICE),
  blk("s3.check1", "knowledge_check", question="The volume of a hemisphere of radius $r$ is:",
    options=["$\\dfrac{2}{3}\\pi r^{3}$", "$\\dfrac{4}{3}\\pi r^{3}$", "$2\\pi r^{2}$", "$\\dfrac{1}{3}\\pi r^{3}$"], correct_index=0, explanation="Half of the sphere's volume $\\dfrac{4}{3}\\pi r^{3}$."),
  blk("s3.check2", "knowledge_check", question="A cone of the same base and height is hollowed out of a solid cylinder. The volume left is what fraction of the cylinder?",
    options=["$\\dfrac{2}{3}$", "$\\dfrac{1}{3}$", "$\\dfrac{1}{2}$", "$\\dfrac{3}{4}$"], correct_index=0, explanation="The cone is $\\dfrac{1}{3}$ of the cylinder, so $1 - \\dfrac{1}{3} = \\dfrac{2}{3}$ is left."),
  blk("s3.memory", "memory_trick", title="See it, then add it", revision=True,
    body="- **Surface area:** only the outside counts. Glued faces vanish; a cavity *adds* its inner surface.\n"
         "- **Volume:** joined parts add; cavities subtract.\n"
         "- A cone is one-third of the cylinder with the same base and height; a hemisphere is two-thirds of it when the height is $r$."),
  blk("s3.mistakes", "common_mistakes", title="Common mistakes",
    body="- Adding the total surface areas of the parts, including the hidden circular faces.\n"
         "- Using the height $h$ of a cone in place of its slant height $l$ in $\\pi r l$.\n"
         "- Forgetting to subtract the hemisphere's or cone's height from the total height.\n"
         "- Using the diameter as the radius.\n"
         "- Mixing units: convert everything to cm (or m) before calculating, and write cm² for area, cm³ for volume."),
  blk("s3.tip", "teacher_tip", title="Bring real objects",
    body="Bring a capsule, an ice-cream cone, a pencil (cylinder + cone) and a ball cut in half. Let students point to the surfaces they can touch: those are the ones to add. "
         "Then fill a cone with sand and pour it into a cylinder of the same base and height three times to show the $\\dfrac{1}{3}$."),
 ]},
 {"id": "s4", "title": "Think, connect, master", "blocks": [
  blk("s4.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why the total surface area of a toy made of a cone and a hemisphere is not the sum of their total surface areas, but its volume is the sum of their volumes."),
  blk("s4.connection", "connection", title="Where this leads",
    body="- **Chapter 11, Areas Related to Circles:** the curved surface of a cone opens out into a sector.\n"
         "- **Chapter 6, Triangles:** Pythagoras gives the slant height $l = \\sqrt{r^{2} + h^{2}}$.\n"
         "- **Real life:** estimating paint, tin sheet, canvas and cost; capacities of tanks, glasses and silos."),
  blk("s4.mastery", "mastery", title="Mastery challenge",
    body="A building is a cylinder with a hemispherical dome on top. The diameter of the dome is $\\dfrac{2}{3}$ of the total height of the building, and the building holds $67\\dfrac{1}{21}$ m³ of air. Find the height of the building.\n\n"
         "**Answer:** Let the total height be $H$. Then $r = \\dfrac{H}{3}$ and the cylinder's height is $H - r = \\dfrac{2H}{3}$. "
         "Volume $= \\pi r^{2} \\cdot \\dfrac{2H}{3} + \\dfrac{2}{3}\\pi r^{3} = \\dfrac{8}{81}\\pi H^{3} = \\dfrac{1408}{21}$, so $H^{3} = 216$ and $H = 6$ m."),
  placed("s4.fig", FIG_CAPSULE),
  blk("s4.summary", "summary", title="Chapter summary",
    body="- Surface area of a combination $=$ sum of the surface areas of the visible parts only.\n"
         "- Volume of a combination $=$ sum of the volumes of the parts; a cavity is subtracted.\n"
         "- Slant height of a cone: $l = \\sqrt{r^{2} + h^{2}}$.\n"
         "- Hemisphere: curved surface $2\\pi r^{2}$, total surface $3\\pi r^{2}$, volume $\\dfrac{2}{3}\\pi r^{3}$."),
  blk("s4.examtips", "exam_tips", title="Board exam tips",
    body="- Draw a rough figure and write which surfaces are visible before using any formula.\n"
         "- Write each part separately (cone, cylinder, hemisphere), then add or subtract.\n"
         "- Use the value of $\\pi$ given; if the answer is 'in terms of $\\pi$', keep $\\pi$.\n"
         "- Check units: m² and m³ for large objects, and convert litres if asked (1000 cm³ $=$ 1 litre)."),
  blk("s4.flash1", "flashcard", front="Volume of a cone", back="$\\dfrac{1}{3}\\pi r^{2} h$"),
  blk("s4.flash2", "flashcard", front="Curved surface area of a hemisphere", back="$2\\pi r^{2}$"),
  blk("s4.flash3", "flashcard", front="Surface area of a capsule (cylinder of height $h$ with two hemispheres)", back="$2\\pi r h + 4\\pi r^{2}$"),
 ]},
]
check(near(2 * P7 * F(1.75) ** 2, 19.25) and near(math.sqrt(1.75 ** 2 + 3.25 ** 2), 3.69) and near(P7 * F(1.75) * F(3.7), 20.35) and F(19.25) + F(20.35) == F(39.6), "Example 1 (NCERT values)")

chapter = {"schema_version": 1, "id": CH_ID, "title": "Surface Areas and Volumes",
  "book": "NCERT Mathematics, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "maths", "chapter_number": 12,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: surface areas and volumes of combinations of any two of cubes, cuboids, spheres, hemispheres and right circular cylinders/cones.",
  "concepts": ["surface_area_combination", "volume_combination", "applications"],
  "sections": sections}

# ---------------------------------------------------------------- questions
Q = []
SA, VO, AP = "surface_area_combination", "volume_combination", "applications"
SHINE = {"kind": "shine"}
SQP = lambda n: {"kind": "sample_paper", "paper": "CBSE Sample Question Paper 2025-26, Mathematics Standard (041)", "question": n}
def ex(e, n): return {"kind": "ncert_exercise", "exercise": e, "question": n}
def q(id_, type_, marks, concepts, source, question, difficulty="medium", **kw):
    Q.append({"id": f"ch12.q.{id_}", "type": type_, "marks": marks, "difficulty": difficulty, "concepts": concepts,
              "source": source, "question": question, "status": "reviewed", **kw})
def mcq(id_, concepts, question, options, correct, explanation, difficulty="easy", source=SHINE):
    q(id_, "mcq", 1, concepts, source, question, difficulty, options=options, correct_index=correct, explanation=explanation)
MS3 = ["1 mark: identify the visible parts", "1 mark: area of each part", "1 mark: total with units"]
MS3V = ["1 mark: identify the parts", "1 mark: volume of each part", "1 mark: total with units"]

# Exercise 12.1
q("ex12_1.q1", "very_short_answer", 2, [SA], ex("12.1", 1), "2 cubes each of volume 64 cm³ are joined end to end. Find the surface area of the resulting cuboid.", "easy",
  answer_steps=["Edge $= \\sqrt[3]{64} = 4$ cm, so the cuboid is $8 \\times 4 \\times 4$.", "Surface area $= 2(8 \\times 4 + 4 \\times 4 + 4 \\times 8) = 160$ cm²"], marking_scheme=["1 mark: dimensions", "1 mark: surface area"])
q("ex12_1.q2", "short_answer", 3, [SA], ex("12.1", 2), "A vessel is in the form of a hollow hemisphere mounted by a hollow cylinder. The diameter of the hemisphere is 14 cm and the total height of the vessel is 13 cm. Find the inner surface area of the vessel.",
  answer_steps=["$r = 7$ cm; height of the cylinder $= 13 - 7 = 6$ cm.", "Curved surface of the cylinder $= 2\\pi r h = 2 \\times \\dfrac{22}{7} \\times 7 \\times 6 = 264$ cm²; hemisphere $= 2\\pi r^{2} = 308$ cm².",
                "Inner surface area $= 264 + 308 = 572$ cm²"], marking_scheme=MS3, figure=dict(FIG_VESSEL))
q("ex12_1.q3", "short_answer", 3, [SA], ex("12.1", 3), "A toy is in the form of a cone of radius 3.5 cm mounted on a hemisphere of same radius. The total height of the toy is 15.5 cm. Find the total surface area of the toy.",
  answer_steps=["Height of the cone $= 15.5 - 3.5 = 12$ cm; $l = \\sqrt{12^{2} + 3.5^{2}} = 12.5$ cm", "Cone: $\\pi r l = \\dfrac{22}{7} \\times 3.5 \\times 12.5 = 137.5$ cm²; hemisphere: $2\\pi r^{2} = 77$ cm²",
                "Total surface area $= 137.5 + 77 = 214.5$ cm²"], marking_scheme=MS3, figure=dict(FIG_TOY))
q("ex12_1.q4", "short_answer", 3, [SA], ex("12.1", 4), "A cubical block of side 7 cm is surmounted by a hemisphere. What is the greatest diameter the hemisphere can have? Find the surface area of the solid.",
  answer_steps=["The greatest diameter equals the side of the cube: 7 cm, so $r = 3.5$ cm.", "Surface area $= 6a^{2} - \\pi r^{2} + 2\\pi r^{2} = 6a^{2} + \\pi r^{2}$",
                "$= 294 + \\dfrac{22}{7} \\times 3.5 \\times 3.5 = 294 + 38.5 = 332.5$ cm²"], marking_scheme=["1 mark: diameter", "1 mark: method", "1 mark: answer"])
q("ex12_1.q5", "short_answer", 3, [SA], ex("12.1", 5), "A hemispherical depression is cut out from one face of a cubical wooden block such that the diameter $l$ of the hemisphere is equal to the edge of the cube. Determine the surface area of the remaining solid.", "hard",
  answer_steps=["The depression removes a circle of radius $\\dfrac{l}{2}$ from one face and adds a curved surface $2\\pi \\left(\\dfrac{l}{2}\\right)^{2}$.",
                "Surface area $= 6l^{2} - \\pi \\dfrac{l^{2}}{4} + 2\\pi \\dfrac{l^{2}}{4} = 6l^{2} + \\dfrac{\\pi l^{2}}{4}$", "$= \\dfrac{l^{2}}{4}(\\pi + 24)$"],
  marking_scheme=["1 mark: circle removed, curved surface added", "1 mark: expression", "1 mark: simplified answer"])
q("ex12_1.q6", "short_answer", 3, [SA], ex("12.1", 6), "A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. The length of the entire capsule is 14 mm and the diameter of the capsule is 5 mm. Find its surface area.",
  answer_steps=["$r = 2.5$ mm; length of the cylinder $= 14 - 5 = 9$ mm.", "Surface area $= 2\\pi r h + 4\\pi r^{2} = 2\\pi r(h + 2r)$", "$= 2 \\times \\dfrac{22}{7} \\times 2.5 \\times 14 = 220$ mm²"],
  marking_scheme=MS3, figure=dict(FIG_CAPSULE))
q("ex12_1.q7", "short_answer", 3, [SA, AP], ex("12.1", 7), "A tent is in the shape of a cylinder surmounted by a conical top. If the height and diameter of the cylindrical part are 2.1 m and 4 m respectively, and the slant height of the top is 2.8 m, find the area of the canvas used for making the tent. Also, find the cost of the canvas of the tent at the rate of ₹ 500 per m². (Note that the base of the tent will not be covered with canvas.)",
  answer_steps=["Cylinder: $2\\pi r h = 2 \\times \\dfrac{22}{7} \\times 2 \\times 2.1 = 26.4$ m²", "Cone: $\\pi r l = \\dfrac{22}{7} \\times 2 \\times 2.8 = 17.6$ m²", "Canvas $= 44$ m²; cost $= 44 \\times 500 =$ ₹ 22000"],
  marking_scheme=["1 mark: cylinder", "1 mark: cone", "1 mark: area and cost"], figure=dict(FIG_TENT))
q("ex12_1.q8", "short_answer", 3, [SA], ex("12.1", 8), "From a solid cylinder whose height is 2.4 cm and diameter 1.4 cm, a conical cavity of the same height and same diameter is hollowed out. Find the total surface area of the remaining solid to the nearest cm².", "hard",
  answer_steps=["$r = 0.7$ cm, $h = 2.4$ cm, slant height $l = \\sqrt{2.4^{2} + 0.7^{2}} = 2.5$ cm", "Surface $= 2\\pi r h + \\pi r^{2} + \\pi r l = \\pi r(2h + r + l)$ (curved cylinder, bottom circle, inside of the cone)",
                "$= \\dfrac{22}{7} \\times 0.7 \\times 8 = 17.6 \\approx 18$ cm²"], marking_scheme=MS3, figure=dict(FIG_HOLLOW))
q("ex12_1.q9", "short_answer", 3, [SA], ex("12.1", 9), "A wooden article was made by scooping out a hemisphere from each end of a solid cylinder. If the height of the cylinder is 10 cm, and its base is of radius 3.5 cm, find the total surface area of the article.",
  answer_steps=["Visible surfaces: the curved cylinder and the insides of two hemispheres.", "Total $= 2\\pi r h + 2 \\times 2\\pi r^{2} = 2\\pi r(h + 2r)$", "$= 2 \\times \\dfrac{22}{7} \\times 3.5 \\times 17 = 374$ cm²"],
  marking_scheme=MS3, figure=dict(FIG_SCOOP))
# Exercise 12.2
q("ex12_2.q1", "very_short_answer", 2, [VO], ex("12.2", 1), "A solid is in the shape of a cone standing on a hemisphere with both their radii being equal to 1 cm and the height of the cone is equal to its radius. Find the volume of the solid in terms of $\\pi$.", "easy",
  answer_steps=["Volume $= \\dfrac{1}{3}\\pi r^{2} h + \\dfrac{2}{3}\\pi r^{3} = \\dfrac{1}{3}\\pi + \\dfrac{2}{3}\\pi$", "$= \\pi$ cm³"], marking_scheme=["1 mark: method", "1 mark: answer"])
q("ex12_2.q2", "short_answer", 3, [VO], ex("12.2", 2), "Rachel, an engineering student, was asked to make a model shaped like a cylinder with two cones attached at its two ends by using a thin aluminium sheet. The diameter of the model is 3 cm and its length is 12 cm. If each cone has a height of 2 cm, find the volume of air contained in the model that Rachel made. (Assume the outer and inner dimensions of the model to be nearly the same.)",
  answer_steps=["$r = 1.5$ cm; length of the cylinder $= 12 - 2 - 2 = 8$ cm.", "Volume $= \\pi r^{2} \\times 8 + 2 \\times \\dfrac{1}{3}\\pi r^{2} \\times 2 = \\pi r^{2}\\left(8 + \\dfrac{4}{3}\\right)$",
                "$= \\dfrac{22}{7} \\times 2.25 \\times \\dfrac{28}{3} = 66$ cm³"], marking_scheme=MS3V, figure=dict(FIG_MODEL))
q("ex12_2.q3", "short_answer", 3, [VO, AP], ex("12.2", 3), "A gulab jamun, contains sugar syrup up to about 30% of its volume. Find approximately how much syrup would be found in 45 gulab jamuns, each shaped like a cylinder with two hemispherical ends with length 5 cm and diameter 2.8 cm.", "hard",
  answer_steps=["$r = 1.4$ cm; cylinder length $= 5 - 2.8 = 2.2$ cm.", "One gulab jamun $= \\pi r^{2} h + \\dfrac{4}{3}\\pi r^{3} = \\dfrac{22}{7} \\times 1.96 \\times \\left(2.2 + \\dfrac{4}{3} \\times 1.4\\right) \\approx 25.05$ cm³",
                "Syrup $= 0.3 \\times 45 \\times 25.05 \\approx 338$ cm³"], marking_scheme=MS3V)
q("ex12_2.q4", "short_answer", 3, [VO, AP], ex("12.2", 4), "A pen stand made of wood is in the shape of a cuboid with four conical depressions to hold pens. The dimensions of the cuboid are 15 cm by 10 cm by 3.5 cm. The radius of each of the depressions is 0.5 cm and the depth is 1.4 cm. Find the volume of wood in the entire stand.",
  answer_steps=["Cuboid $= 15 \\times 10 \\times 3.5 = 525$ cm³", "Four cones $= 4 \\times \\dfrac{1}{3} \\times \\dfrac{22}{7} \\times 0.5 \\times 0.5 \\times 1.4 \\approx 1.47$ cm³", "Wood $= 525 - 1.47 = 523.53$ cm³"],
  marking_scheme=["1 mark: cuboid", "1 mark: cones", "1 mark: answer"])
q("ex12_2.q5", "short_answer", 3, [VO, AP], ex("12.2", 5), "A vessel is in the form of an inverted cone. Its height is 8 cm and the radius of its top, which is open, is 5 cm. It is filled with water up to the brim. When lead shots, each of which is a sphere of radius 0.5 cm are dropped into the vessel, one-fourth of the water flows out. Find the number of lead shots dropped in the vessel.", "hard",
  answer_steps=["Water that flows out $= \\dfrac{1}{4} \\times \\dfrac{1}{3}\\pi \\times 5^{2} \\times 8 = \\dfrac{50\\pi}{3}$ cm³", "One shot $= \\dfrac{4}{3}\\pi (0.5)^{3} = \\dfrac{\\pi}{6}$ cm³",
                "Number of shots $= \\dfrac{50\\pi}{3} \\div \\dfrac{\\pi}{6} = 100$"], marking_scheme=["1 mark: water displaced", "1 mark: one shot", "1 mark: number"])
q("ex12_2.q6", "short_answer", 3, [VO, AP], ex("12.2", 6), "A solid iron pole consists of a cylinder of height 220 cm and base diameter 24 cm, which is surmounted by another cylinder of height 60 cm and radius 8 cm. Find the mass of the pole, given that 1 cm³ of iron has approximately 8 g mass. (Use $\\pi = 3.14$)",
  answer_steps=["Volume $= 3.14 \\times (12^{2} \\times 220 + 8^{2} \\times 60) = 3.14 \\times 35520 = 111532.8$ cm³", "Mass $= 111532.8 \\times 8 = 892262.4$ g", "$= 892.26$ kg (approx.)"],
  marking_scheme=["1 mark: volume", "1 mark: mass in g", "1 mark: in kg"])
q("ex12_2.q7", "long_answer", 5, [VO], ex("12.2", 7), "A solid consisting of a right circular cone of height 120 cm and radius 60 cm standing on a hemisphere of radius 60 cm is placed upright in a right circular cylinder full of water such that it touches the bottom. Find the volume of water left in the cylinder, if the radius of the cylinder is 60 cm and its height is 180 cm.", "hard",
  answer_steps=["Cylinder $= \\pi \\times 60^{2} \\times 180 = 648000\\pi$ cm³", "Cone $= \\dfrac{1}{3}\\pi \\times 60^{2} \\times 120 = 144000\\pi$ cm³", "Hemisphere $= \\dfrac{2}{3}\\pi \\times 60^{3} = 144000\\pi$ cm³",
                "Water left $= 648000\\pi - 288000\\pi = 360000\\pi$ cm³", "$= \\dfrac{22}{7} \\times 360000 \\approx 1131428.57$ cm³ $\\approx 1.131$ m³"],
  marking_scheme=["1 mark: cylinder", "1 mark: cone", "1 mark: hemisphere", "1 mark: subtraction", "1 mark: answer"])
q("ex12_2.q8", "short_answer", 3, [VO, AP], ex("12.2", 8), "A spherical glass vessel has a cylindrical neck 8 cm long, 2 cm in diameter; the diameter of the spherical part is 8.5 cm. By measuring the amount of water it holds, a child finds its volume to be 345 cm³. Check whether she is correct, taking the above as the inside measurements, and $\\pi = 3.14$.",
  answer_steps=["Neck $= 3.14 \\times 1^{2} \\times 8 = 25.12$ cm³", "Sphere $= \\dfrac{4}{3} \\times 3.14 \\times 4.25^{3} \\approx 321.39$ cm³", "Total $\\approx 346.51$ cm³, so she is not correct: the volume is 346.51 cm³."],
  marking_scheme=["1 mark: neck", "1 mark: sphere", "1 mark: conclusion"])
# NCERT example as a question
q("eg7", "long_answer", 5, [VO], {"kind": "ncert_example", "example": 7}, "A solid toy is in the form of a hemisphere surmounted by a right circular cone. The height of the cone is 2 cm and the diameter of the base is 4 cm. Determine the volume of the toy. If a right circular cylinder circumscribes the toy, find the difference of the volumes of the cylinder and the toy. (Take $\\pi = 3.14$)", "medium",
  answer_steps=["$r = 2$ cm. Hemisphere $= \\dfrac{2}{3} \\times 3.14 \\times 2^{3} \\approx 16.75$ cm³", "Cone $= \\dfrac{1}{3} \\times 3.14 \\times 2^{2} \\times 2 \\approx 8.37$ cm³", "Toy $= \\dfrac{2}{3}\\pi r^{3} + \\dfrac{1}{3}\\pi r^{2} h = 25.12$ cm³",
                "The cylinder has radius 2 cm and height $2 + 2 = 4$ cm: $3.14 \\times 2^{2} \\times 4 = 50.24$ cm³", "Difference $= 50.24 - 25.12 = 25.12$ cm³"],
  marking_scheme=["1 mark: hemisphere", "1 mark: cone", "1 mark: toy", "1 mark: cylinder", "1 mark: difference"])
# Sample paper
mcq("sqp11", [VO], "If the area of the base of a right circular cone is 51 cm² and its volume is 85 cm³, then the height of the cone is given as",
    ["$\\dfrac{5}{6}$ cm", "$\\dfrac{5}{3}$ cm", "$\\dfrac{5}{2}$ cm", "$5$ cm"], 3, "Volume $= \\dfrac{1}{3} \\times$ base area $\\times h$, so $85 = \\dfrac{1}{3} \\times 51 \\times h$ and $h = 5$ cm.", "medium", source=SQP(11))
q("sqp34a", "long_answer", 5, [SA], SQP("34(A)"), "From a solid right circular cone, whose height is 6 cm and radius of base is 12 cm, a right circular cylindrical cavity of height 3 cm and radius 4 cm is hollowed out such that bases of cone and cylinder form concentric circles. Find the surface area of the remaining solid in terms of $\\pi$.", "hard",
  answer_steps=["Slant height $L = \\sqrt{12^{2} + 6^{2}} = \\sqrt{180} = 6\\sqrt{5}$ cm; curved surface of the cone $= \\pi \\times 12 \\times 6\\sqrt{5} = 72\\sqrt{5}\\pi$ cm²",
                "Base: the ring $144\\pi - 16\\pi$ plus the top of the cavity $16\\pi$ gives $144\\pi$ cm².", "Curved surface of the cavity $= 2\\pi \\times 4 \\times 3 = 24\\pi$ cm²",
                "Surface area $= 72\\sqrt{5}\\pi + 144\\pi + 24\\pi$", "$= (168 + 72\\sqrt{5})\\pi$ cm²"],
  marking_scheme=["1 mark: slant height and curved surface", "1 mark: base", "1 mark: cavity", "1 mark: adding", "1 mark: answer"], figure=dict(FIG_SQP34))
q("sqp34b", "long_answer", 5, [VO], SQP("34(B)"), "An empty cone of radius 3 cm and height 12 cm is filled with ice-cream such that the lower part of the cone which is $\\dfrac{1}{6}$th of the volume of the cone is unfilled (empty) but a hemisphere is formed on the top. Find the volume of the ice-cream.",
  answer_steps=["Volume of the cone $= \\dfrac{1}{3}\\pi \\times 3 \\times 3 \\times 12 = 36\\pi$ cm³", "Ice-cream in the cone $= \\dfrac{5}{6} \\times 36\\pi = 30\\pi$ cm³", "Hemisphere $= \\dfrac{2}{3}\\pi \\times 3^{3} = 18\\pi$ cm³",
                "Total $= 30\\pi + 18\\pi = 48\\pi$ cm³", "$\\approx 150.86$ cm³"],
  marking_scheme=["1 mark: cone", "1 mark: filled part", "1 mark: hemisphere", "1 mark: total", "1 mark: value"], figure=dict(FIG_ICE))
# Shine MCQs
mcq("mcq01", [SA], "Two cubes of edge 5 cm are joined end to end. The surface area of the resulting cuboid is:", ["$250$ cm²", "$300$ cm²", "$150$ cm²", "$125$ cm²"], 0, "The cuboid is $10 \\times 5 \\times 5$: $2(50 + 25 + 50) = 250$ cm².", "medium")
mcq("mcq02", [SA], "A toy is a cone of radius $r$ and slant height $l$ on a hemisphere of radius $r$. Its total surface area is:",
    ["$\\pi r l + 2\\pi r^{2}$", "$\\pi r l + 3\\pi r^{2}$", "$\\pi r(l + r) + 2\\pi r^{2}$", "$\\pi r l + \\pi r^{2}$"], 0, "Only the two curved surfaces are visible: $\\pi r l + 2\\pi r^{2}$.", "medium")
mcq("mcq03", [VO], "The volume of a hemisphere of radius $r$ is:", ["$\\dfrac{2}{3}\\pi r^{3}$", "$\\dfrac{4}{3}\\pi r^{3}$", "$2\\pi r^{3}$", "$\\dfrac{1}{3}\\pi r^{3}$"], 0, "Half of $\\dfrac{4}{3}\\pi r^{3}$.")
mcq("mcq04", [VO], "A cylinder and a cone have the same base and the same height. The ratio of their volumes is:", ["$3 : 1$", "$1 : 3$", "$2 : 1$", "$1 : 1$"], 0, "$\\pi r^{2} h : \\dfrac{1}{3}\\pi r^{2} h = 3 : 1$.")
mcq("mcq05", [SA], "The curved surface area of a hemisphere of radius 7 cm is:", ["$308$ cm²", "$462$ cm²", "$154$ cm²", "$616$ cm²"], 0, "$2\\pi r^{2} = 2 \\times \\dfrac{22}{7} \\times 49 = 308$ cm².")
mcq("mcq06", [SA], "The slant height of a cone of radius 6 cm and height 8 cm is:", ["$10$ cm", "$14$ cm", "$2$ cm", "$\\sqrt{28}$ cm"], 0, "$l = \\sqrt{6^{2} + 8^{2}} = 10$ cm.")
mcq("mcq07", [SA], "The surface area of a sphere of radius 3.5 cm is:", ["$154$ cm²", "$38.5$ cm²", "$179.67$ cm²", "$77$ cm²"], 0, "$4\\pi r^{2} = 4 \\times \\dfrac{22}{7} \\times 12.25 = 154$ cm².")
mcq("mcq08", [SA], "The greatest diameter of a hemisphere that can be placed on a cube of edge 7 cm is:", ["$7$ cm", "$3.5$ cm", "$14$ cm", "$49$ cm"], 0, "The hemisphere's base must fit on a face of the cube, so its diameter is at most the edge, 7 cm.")
mcq("mcq09", [SA], "A hemispherical depression of radius $r$ is cut from one face of a cube. The total surface area of the cube:",
    ["increases by $\\pi r^{2}$", "decreases by $\\pi r^{2}$", "increases by $2\\pi r^{2}$", "does not change"], 0, "It loses a circle $\\pi r^{2}$ and gains a curved surface $2\\pi r^{2}$: a net increase of $\\pi r^{2}$.", "medium")
mcq("mcq10", [VO], "A cone of the same base and height is hollowed out of a solid cylinder of radius 7 cm and height 10 cm. The volume of the remaining solid is:",
    ["$\\dfrac{3080}{3}$ cm³", "$1540$ cm³", "$\\dfrac{1540}{3}$ cm³", "$\\dfrac{4620}{3}$ cm³"], 0, "$\\dfrac{2}{3}$ of the cylinder: $\\dfrac{2}{3} \\times \\dfrac{22}{7} \\times 49 \\times 10 = \\dfrac{3080}{3}$ cm³.", "medium")

AR_OPTIONS = ["Both Assertion (A) and Reason (R) are true and R is the correct explanation of A.", "Both Assertion (A) and Reason (R) are true but R is not the correct explanation of A.",
              "Assertion (A) is true but Reason (R) is false.", "Assertion (A) is false but Reason (R) is true."]
def ar(id_, concepts, a_, r_, correct, explanation):
    q(id_, "assertion_reason", 1, concepts, SHINE, f"**Assertion (A):** {a_}\n\n**Reason (R):** {r_}", "medium", options=AR_OPTIONS, correct_index=correct, explanation=explanation)
ar("ar1", [SA], "The total surface area of a toy made of a cone on a hemisphere is the sum of the curved surface areas of the cone and the hemisphere.", "The common circular base is hidden inside the toy.", 0,
   "Because the bases are hidden, only the curved surfaces are counted: R explains A.")
ar("ar2", [VO], "The volume of a capsule made of a cylinder with a hemisphere at each end is $\\pi r^{2} h + \\dfrac{4}{3}\\pi r^{3}$.", "The two hemispheres together make one sphere.", 0,
   "Two hemispheres give $\\dfrac{4}{3}\\pi r^{3}$, which is added to the cylinder: R explains A.")
ar("ar3", [SA], "If two cubes of edge 4 cm are joined end to end, the surface area of the cuboid formed is 192 cm².", "The surface area of a cube of edge $a$ is $6a^{2}$.", 3,
   "A is false: two faces are hidden, so the area is $2 \\times 96 - 2 \\times 16 = 160$ cm². R is true.")
ar("ar4", [SA], "The slant height of a cone of radius 5 cm and height 12 cm is 13 cm.", "The volume of a cone is $\\dfrac{1}{3}\\pi r^{2} h$.", 1, "Both are true, but the slant height comes from Pythagoras, not from the volume.")
ar("ar5", [SA], "The curved surface area of a hemisphere of radius $r$ is $2\\pi r^{2}$.", "The total surface area of a solid hemisphere is $2\\pi r^{2}$.", 2,
   "A is true. R is false: the total surface area also includes the flat circle, so it is $3\\pi r^{2}$.")

q("vsa1", "very_short_answer", 2, [VO], SHINE, "Find the volume of a solid hemisphere of radius 2.1 cm.", "easy",
  answer_steps=["Volume $= \\dfrac{2}{3}\\pi r^{3} = \\dfrac{2}{3} \\times \\dfrac{22}{7} \\times 2.1 \\times 2.1 \\times 2.1$", "$= 19.404$ cm³"], marking_scheme=["1 mark: formula with values", "1 mark: answer with units"])
q("vsa2", "very_short_answer", 2, [SA], SHINE, "Find the curved surface area of a cone of radius 7 cm and height 24 cm.", "easy",
  answer_steps=["$l = \\sqrt{7^{2} + 24^{2}} = 25$ cm", "$\\pi r l = \\dfrac{22}{7} \\times 7 \\times 25 = 550$ cm²"], marking_scheme=["1 mark: slant height", "1 mark: area"])
q("sa1", "short_answer", 3, [VO], SHINE, "A solid is in the shape of a cone mounted on a hemisphere of the same radius 7 cm. The total height of the solid is 31 cm. Find its volume.",
  answer_steps=["Height of the cone $= 31 - 7 = 24$ cm.", "Volume $= \\dfrac{1}{3}\\pi r^{2} h + \\dfrac{2}{3}\\pi r^{3} = \\dfrac{22}{7}\\left(\\dfrac{1}{3} \\times 49 \\times 24 + \\dfrac{2}{3} \\times 343\\right)$",
                "$= \\dfrac{40964}{21} \\approx 1950.67$ cm³"], marking_scheme=MS3V)
q("sa2", "short_answer", 3, [SA], SHINE, "A wooden toy is a solid cylinder of radius 3 cm and height 8 cm with a cone of the same radius and height 4 cm on top. Find the total surface area of the toy.",
  answer_steps=["Slant height of the cone $= \\sqrt{3^{2} + 4^{2}} = 5$ cm", "Visible surfaces: base circle $\\pi r^{2}$, curved cylinder $2\\pi r h$ and curved cone $\\pi r l$.",
                "Total $= \\pi \\times 3(3 + 16 + 5) = 72\\pi \\approx 226.29$ cm²"], marking_scheme=MS3)
q("sa3", "short_answer", 3, [VO, AP], SHINE, "A cylindrical tub of radius 12 cm contains water to a depth of 20 cm. A spherical iron ball is dropped into the tub, and the level of water rises by 6.75 cm. Find the radius of the ball.", "hard",
  answer_steps=["Volume of the ball $=$ volume of water raised: $\\dfrac{4}{3}\\pi r^{3} = \\pi \\times 12^{2} \\times 6.75$", "$r^{3} = 729$", "$r = 9$ cm"],
  marking_scheme=["1 mark: equation", "1 mark: $r^{3}$", "1 mark: radius"])
q("la1", "long_answer", 5, [VO], SHINE, "A building is in the form of a cylinder surmounted by a hemispherical dome. The base diameter of the dome is equal to $\\dfrac{2}{3}$ of the total height of the building. Find the height of the building, if it contains $67\\dfrac{1}{21}$ m³ of air.", "hard",
  answer_steps=["Let the total height be $H$. Then $2r = \\dfrac{2H}{3}$, so $r = \\dfrac{H}{3}$.", "Height of the cylinder $= H - r = \\dfrac{2H}{3}$",
                "Volume $= \\pi r^{2} \\cdot \\dfrac{2H}{3} + \\dfrac{2}{3}\\pi r^{3} = \\dfrac{2\\pi H^{3}}{27} + \\dfrac{2\\pi H^{3}}{81} = \\dfrac{8\\pi H^{3}}{81}$",
                "$\\dfrac{8}{81} \\times \\dfrac{22}{7} \\times H^{3} = \\dfrac{1408}{21}$ gives $H^{3} = 216$", "$H = 6$ m"],
  marking_scheme=["1 mark: radius in terms of $H$", "1 mark: cylinder height", "1 mark: volume", "1 mark: equation", "1 mark: answer"])
q("cb1", "case_based", 4, [SA, VO, AP], SHINE,
  "An ice-cream cone has radius 3.5 cm and height 12 cm. It is filled with ice-cream, with a hemisphere of ice-cream on top.\n\n(i) Find the slant height of the cone. (1)\n\n(ii) Find the volume of the hemisphere of ice-cream. (1)\n\n(iii) Find the total volume of ice-cream. OR Find the area of the paper wrapped around the cone (its curved surface). (2)",
  answer_steps=["(i) $l = \\sqrt{3.5^{2} + 12^{2}} = 12.5$ cm", "(ii) $\\dfrac{2}{3} \\times \\dfrac{22}{7} \\times 3.5^{3} \\approx 89.83$ cm³",
                "(iii) Cone $= \\dfrac{1}{3} \\times \\dfrac{22}{7} \\times 3.5^{2} \\times 12 = 154$ cm³, total $\\approx 243.83$ cm³. OR $\\pi r l = \\dfrac{22}{7} \\times 3.5 \\times 12.5 = 137.5$ cm²."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
q("cb2", "case_based", 4, [SA, AP], SHINE,
  "A camping tent is a cylinder of diameter 14 m and height 3 m with a conical top of slant height 10 m. The base is not covered with canvas.\n\n(i) Find the curved surface area of the cylindrical part. (1)\n\n(ii) Find the curved surface area of the conical part. (1)\n\n(iii) Find the cost of the canvas at ₹ 100 per m². OR Find the height of the conical part. (2)",
  answer_steps=["(i) $2\\pi r h = 2 \\times \\dfrac{22}{7} \\times 7 \\times 3 = 132$ m²", "(ii) $\\pi r l = \\dfrac{22}{7} \\times 7 \\times 10 = 220$ m²",
                "(iii) Canvas $= 352$ m², cost $= 352 \\times 100 =$ ₹ 35200. OR $h = \\sqrt{10^{2} - 7^{2}} = \\sqrt{51} \\approx 7.14$ m."],
  marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

def spread(item):
    opts = item.get("options")
    if not opts or item.get("type") == "assertion_reason" or item["id"].startswith("ch12.q.sqp") or item.get("source", {}).get("kind") == "ncert_exercise":
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
