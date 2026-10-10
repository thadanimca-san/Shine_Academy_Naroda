"""CBSE Class 10 Science Ch 11: Electricity.
Every numerical answer is recomputed below (exact fractions where possible)."""
import sys, math
from fractions import Fraction as Fr
from sci_common import Chapter, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch11"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch11_electricity"
C = Chapter("sci10ch11")
blk = C.blk

def par(*rs): return 1 / sum(Fr(1) / Fr(r) for r in rs)
def near(a, b, tol): return abs(a - b) <= tol
# In-text
check(near(1 / 1.6e-19, 6.25e18, 1e12), "11.1 Q3")
check(sum([5, 8, 12]) == 25 and Fr(6, 25) == Fr(24, 100) and Fr(6, 25) * 12 == Fr(288, 100), "11.6.1 Q2: 0.24 A, 2.88 V")
check(par(100, 50, 500) == Fr(125, 4) and 220 / Fr(125, 4) == Fr(704, 100), "11.6.2 Q2: 31.25 ohm, 7.04 A")
check(2 + par(3, 6) == 4 and par(2, 3, 6) == 1, "11.6.2 Q4")
check(4 + 8 + 12 + 24 == 48 and par(4, 8, 12, 24) == 2, "11.6.2 Q5")
check(par(1, 10**6) < 1 and par(1, 10**3, 10**6) < 1, "11.6.2 Q1")
check(50 * 96000 == 4_800_000 and 5**2 * 20 * 30 == 15000, "11.7 Q2, Q3")
check(220 * 5 == 1100 and 1100 * 2 * 3600 == 7_920_000, "11.8 Q2: 1100 W, 2.2 kWh")
# Exercises
check(Fr(1) / par(*[Fr(1, 5)] * 5) == 25, "ex 1: R/R' = 25")
check(Fr(110**2, 220**2) * 100 == 25, "ex 3: 25 W")
check(Fr(1, 2 * 1) / Fr(1, Fr(1, 2)) == Fr(1, 4), "ex 4: H_series : H_parallel = 1 : 4")
A6 = math.pi * (0.25e-3) ** 2
check(near(10 * A6 / 1.6e-8, 122.7, 0.05), "ex 6: l = 122.7 m")
check(Fr(13.2) / 4 > 3 and Fr(102, 10) - Fr(34, 10) == Fr(68, 10) and Fr(68, 10) / 2 == Fr(34, 10), "ex 7: about 3.4 ohm")
check(Fr(12) / Fr(25, 10000) == 4800, "ex 8")
check(Fr(2, 10) + Fr(3, 10) + Fr(4, 10) + Fr(5, 10) + 12 == Fr(134, 10) and near(9 / 13.4, 0.67, 0.005), "ex 9")
check(Fr(220, 5) == 44 and Fr(176, 44) == 4, "ex 10")
check(6 + par(6, 6) == 9 and par(6, 12) == 4, "ex 11")
check(Fr(5) / Fr(10, 220) == 110, "ex 12")
check(near(220 / 24, 9.17, 0.005) and near(220 / 48, 4.58, 0.005) and near(220 / 12, 18.33, 0.005), "ex 13")
check(Fr(6, 3) ** 2 * 2 == 8 and Fr(4) ** 2 / 2 == 8, "ex 14")
check(near(160 / 220, 0.73, 0.005), "ex 15")
check(250 * 1 == 250 and 1200 * Fr(10, 60) == 200, "ex 16")
check(5**2 * 44 == 1100, "ex 17")
# SQP
check(near(1.7e-8 * 2 / 0.5e-6, 0.068, 1e-9) and near(1.7e-8 * 4 / 0.5e-6, 0.136, 1e-9), "SQP 34B")
A36 = math.pi * (0.4e-3) ** 2
check(near(A36, 5.03e-7, 0.01e-7) and near(0.12 * 5e-7 / 1.8e-8, 3.33, 0.005), "SQP 36")
check(near(2000 / 220, 9.09, 0.005), "SQP 39A")
check(Fr(24**2, 6) == 96 and Fr(24**2, 12) == 48 and (96 + 48) * 300 == 43200, "SQP 39B")
# GSEB
check(Fr(1, 2) * 20 * 60 == 600 and 12 * 2 == 24, "GSEB charge and work")

FORMULAS = ("| Quantity | Formula | SI unit |\n|---|---|---|\n| Current | I = Q/t | ampere (A) |\n| Potential difference | V = W/Q | volt (V) |\n| Ohm's law | V = IR | ohm (Ω) for R |\n"
            "| Resistance of a wire | R = ρl/A | ohm metre (Ω m) for ρ |\n| Resistors in series | R = R₁ + R₂ + R₃ | ohm (Ω) |\n| Resistors in parallel | 1/R = 1/R₁ + 1/R₂ + 1/R₃ | ohm (Ω) |\n"
            "| Heat produced (Joule's law) | H = I²Rt | joule (J) |\n| Electric power | P = VI = I²R = V²/R | watt (W) |\n| Commercial unit of energy | 1 kWh = 3.6 × 10⁶ J | kilowatt hour (kWh) |")
RESISTIVITY = ("| Material | Resistivity (Ω m) | Material | Resistivity (Ω m) |\n|---|---|---|---|\n| Silver | 1.60 × 10⁻⁸ | Mercury | 94.0 × 10⁻⁸ |\n| Copper | 1.62 × 10⁻⁸ | Nichrome (alloy) | 100 × 10⁻⁶ |\n"
               "| Aluminium | 2.63 × 10⁻⁸ | Manganin (alloy) | 44 × 10⁻⁶ |\n| Tungsten | 5.20 × 10⁻⁸ | Glass (insulator) | 10¹⁰ to 10¹⁴ |\n| Iron | 10.0 × 10⁻⁸ | Rubber (insulator) | 10¹³ to 10¹⁶ |")

sections = [
 {"id": "s1", "title": "The power behind the switch", "blocks": [
  blk("s1.hook", "hook", title="What happens when you flip a switch?",
    body="Press a switch and a bulb glows, a fan spins, and a phone charges. Something flows through the wires, but you cannot see it. Why does one bulb glow brighter than another, and why does a fuse blow when too many appliances run together?\n\n"
         "In this chapter you will learn what electric current is, what pushes it, what opposes it, how to combine resistors, and how electrical energy turns into heat and light. You will also learn to read the electricity bill."),
  blk("s1.inspiration", "inspiration", title="Electrifying India's villages", person="Homi J. Bhabha", years="1909–1966",
    body="Homi Jehangir Bhabha, a brilliant physicist from Mumbai, believed that cheap, plentiful electricity was the key to India's progress. He founded the **Tata Institute of Fundamental Research** (1945) "
         "and led India's atomic energy programme, which today generates electricity from nuclear power stations.\n\nThe Bhabha Atomic Research Centre in Mumbai is named after him.",
    future="Electricity leads to careers in electrical and electronics engineering, power generation, renewable energy, electric vehicles and the design of household appliances."),
  blk("s1.socratic", "socratic_question", question="Two bulbs are joined one after another to a battery. If one bulb fuses, what happens to the other?",
    options=["It goes off too", "It glows brighter", "Nothing changes"], correct_index=0,
    explanation="In series there is only one path for the current; a break anywhere stops the current everywhere. That is why houses use parallel wiring."),
 ]},
 {"id": "s2", "title": "Current and potential difference", "blocks": [
  blk("s2.reveal", "theory", title="Charge on the move", revision=True,
    body="**Electric current** is the rate of flow of electric charge: **I = Q/t**. Its SI unit is the **ampere (A)**: 1 A is a flow of 1 coulomb per second. In metal wires the moving charges are **electrons**; "
         "by convention, current is taken in the direction opposite to the flow of electrons (from the positive to the negative terminal outside the cell).\n\n"
         "- 1 coulomb is the charge on about 6 × 10¹⁸ electrons (one electron carries 1.6 × 10⁻¹⁹ C).\n- 1 mA = 10⁻³ A; 1 µA = 10⁻⁶ A.\n- An **ammeter** measures current and is always connected **in series**.\n\n"
         "**Potential difference** is what makes charge flow, just as a difference in water level makes water flow. It is the work done to move a unit charge from one point to another: **V = W/Q**. "
         "Its SI unit is the **volt (V)**: 1 V means 1 joule of work is done to move 1 coulomb. A **cell** or **battery** maintains the potential difference by chemical action. "
         "A **voltmeter** measures potential difference and is always connected **in parallel**.\n\n"
         "A **circuit diagram** uses symbols for the cell, battery, plug key or switch, wire joint, bulb, resistor, rheostat (variable resistance), ammeter and voltmeter. A circuit is a continuous closed path for the current."),
  blk("s2.check", "knowledge_check", question="How is a voltmeter connected to measure the potential difference across a resistor?",
    options=["In parallel with the resistor", "In series with the resistor", "Across the battery only", "Either way, it does not matter"], correct_index=0,
    explanation="A voltmeter goes in parallel, across the two points; an ammeter goes in series."),
 ]},
 {"id": "s3", "title": "Ohm's law and resistance", "blocks": [
  blk("s3.thm", "theory", title="What opposes the current", revision=True,
    body="**Ohm's law:** at a constant temperature, the current through a metallic wire is directly proportional to the potential difference across its ends: **V = IR**. "
         "The V–I graph is a straight line through the origin, and its slope is the **resistance R**, measured in **ohm (Ω)**: 1 Ω = 1 V/1 A.\n\n"
         "**Resistance of a wire depends on:**\n- its **length**: R ∝ l (a longer wire has more resistance);\n- its **area of cross-section**: R ∝ 1/A (a thicker wire has less resistance);\n- its **material** and **temperature**.\n\n"
         "So **R = ρl/A**, where ρ (rho) is the **resistivity** of the material, in **ohm metre (Ω m)**. Resistivity does not depend on the shape or size of the wire.\n\n"
         "- Metals and alloys have low resistivity (10⁻⁸ to 10⁻⁶ Ω m): good conductors. Insulators such as rubber and glass have very high resistivity (10¹² to 10¹⁷ Ω m).\n"
         "- **Alloys** have higher resistivity than their metals and do not oxidise (burn) easily at high temperatures, so they are used in heating devices such as toasters and irons.\n"
         "- Copper and aluminium have low resistivity, so they are used for transmission wires.\n- A **rheostat** changes the resistance, and so the current, in a circuit."),
  blk("s3.table", "markdown_table", title="Electrical resistivity of some substances at 20 °C", revision=True, body=RESISTIVITY),
  blk("s3.check", "knowledge_check", question="The diameter of a wire is doubled, keeping its length the same. Its resistance becomes:",
    options=["one-fourth", "half", "double", "four times"], correct_index=0,
    explanation="Doubling the diameter makes the area four times, and R ∝ 1/A, so R becomes one-fourth."),
 ]},
 {"id": "s4", "title": "Resistors in series and parallel", "blocks": [
  blk("s4.thm", "theory", title="Two ways to join", revision=True,
    body="**In series** (end to end):\n- the **same current** flows through every resistor;\n- the potential differences add up: V = V₁ + V₂ + V₃;\n- the equivalent resistance is the **sum**: **R = R₁ + R₂ + R₃**, more than the largest one.\n\n"
         "**In parallel** (all across the same two points):\n- the **same potential difference** is across every resistor;\n- the currents add up: I = I₁ + I₂ + I₃;\n"
         "- **1/R = 1/R₁ + 1/R₂ + 1/R₃**, so the equivalent resistance is **less than the smallest** one.\n\n"
         "**Why houses use parallel wiring:** in series, if one appliance fails the whole circuit breaks, and all appliances share the voltage and cannot get the current they each need. "
         "In parallel, each appliance gets the full voltage, draws its own current, and can be switched on or off independently. The total resistance also falls."),
  blk("s4.example", "worked_example", title="Worked example: parallel appliances",
    problem="A lamp of 100 Ω, a toaster of 50 Ω and a water filter of 500 Ω are connected in parallel to a 220 V source. What is the resistance of an electric iron that takes as much current as all three, and what is the current through it?",
    steps=["$\\dfrac{1}{R} = \\dfrac{1}{100} + \\dfrac{1}{50} + \\dfrac{1}{500} = \\dfrac{5 + 10 + 1}{500} = \\dfrac{16}{500}$", "$R = \\dfrac{500}{16} = 31.25$ Ω",
           "$I = \\dfrac{V}{R} = \\dfrac{220}{31.25} = 7.04$ A"],
    answer="The iron has a resistance of 31.25 Ω and draws 7.04 A."),
  blk("s4.check", "knowledge_check", question="Three resistors of 6 Ω each are connected in parallel. The equivalent resistance is:",
    options=["2 Ω", "18 Ω", "6 Ω", "3 Ω"], correct_index=0,
    explanation="1/R = 1/6 + 1/6 + 1/6 = 1/2, so R = 2 Ω."),
 ]},
 {"id": "s5", "title": "Heating effect of current", "blocks": [
  blk("s5.thm", "theory", title="Joule's law of heating", revision=True,
    body="When current flows through a resistor, part of the source's energy is turned into heat. The heat produced is **H = VIt = I²Rt** (Joule's law of heating): it is proportional to the square of the current, to the resistance and to the time.\n\n"
         "**Useful applications:**\n- **Electric iron, toaster, oven, kettle, heater:** coils of an alloy such as nichrome get hot.\n"
         "- **Electric bulb:** the thin **tungsten** filament (melting point 3380 °C) glows white-hot; the bulb is filled with inert nitrogen and argon so that the filament lasts longer.\n"
         "- **Electric fuse:** a wire of a metal or alloy of low melting point (for example aluminium, copper, iron or lead) in **series** with the circuit. If a large current flows, the fuse wire melts and breaks the circuit, protecting the appliances. "
         "Fuses for home use are rated 1 A, 2 A, 3 A, 5 A, 10 A and so on.\n\n"
         "**Unwanted heating** wastes energy and can damage cables and appliances."),
  blk("s5.check", "knowledge_check", question="Why does the cord of an electric heater not glow while the heating element does?",
    options=["The cord has a much lower resistance than the element", "The cord carries less current", "The cord is made of tungsten", "The element is connected in parallel with the cord"], correct_index=0,
    explanation="The same current flows through both, but H = I²Rt, and the copper cord's resistance is tiny compared with the nichrome element's."),
 ]},
 {"id": "s6", "title": "Electric power and energy", "blocks": [
  blk("s6.thm", "theory", title="Watts and units", revision=True,
    body="**Electric power** is the rate at which electrical energy is consumed or dissipated: **P = VI = I²R = V²/R**. Its SI unit is the **watt (W)**: 1 W = 1 V × 1 A. 1 kW = 1000 W.\n\n"
         "**Electrical energy** = power × time. The commercial unit is the **kilowatt hour (kWh)**, the '**unit**' on the electricity bill: the energy used in one hour at a rate of 1000 W. "
         "**1 kWh = 3.6 × 10⁶ J.**\n\n"
         "An appliance rated '220 V, 100 W' uses 100 W when connected to 220 V. Its resistance is R = V²/P = 220²/100 = 484 Ω. On 110 V it would use only P = 110²/484 = 25 W.\n\n" + FORMULAS),
  blk("s6.check", "knowledge_check", question="How many units (kWh) does a 2 kW heater use in 3 hours?",
    options=["6 units", "1.5 units", "5 units", "0.67 units"], correct_index=0,
    explanation="Energy = power × time = 2 kW × 3 h = 6 kWh."),
  blk("s6.memory", "memory_trick", title="One triangle, many formulas",
    body="- **V = IR**: cover the letter you want. V on top; I and R side by side below.\n- **P = VI**, then replace V by IR (**P = I²R**) or I by V/R (**P = V²/R**).\n"
         "- **Series: same current, add resistances. Parallel: same voltage, add reciprocals.**\n- **Ammeter in series, voltmeter in parallel** (\"A**S**, V**P**\": Ammeter Series, Voltmeter Parallel)."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Forgetting to take the reciprocal at the end in parallel: 1/R = 1/2 means R = 2 Ω, not 0.5 Ω.\n- Using mm or mm² in R = ρl/A: convert diameter to metres and use A = πr².\n"
         "- Using time in hours with power in watts to get joules: convert hours to seconds, or use kW and h to get kWh.\n"
         "- Saying that the current is 'used up' by a bulb: the same current flows in and out; energy is used.\n- Writing that a fuse is connected in parallel: it is in series."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="With two torch bulbs, a 4.5 V battery and wires, show series and parallel connections: in series both bulbs are dim and go off together; in parallel both glow brightly and work independently. "
         "Ask students to bring last month's electricity bill and work out how many units each appliance at home uses in a day."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend why household appliances are connected in parallel, and why the filament of a bulb glows but the wires leading to it stay cool."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 12, Magnetic Effects of Electric Current:** a current produces a magnetic field; domestic circuits, earthing and fuses.\n"
         "- **Class 12 Physics:** current electricity, Kirchhoff's rules, cells and the potentiometer.\n- **Everyday life:** reading the electricity bill, choosing efficient appliances and using electricity safely."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A 4 Ω resistor and a 12 Ω resistor are connected in parallel, and this combination is connected in series with a 3 Ω resistor to a 12 V battery.\n\n(a) Find the total resistance. (b) Find the current from the battery. (c) Find the current through the 12 Ω resistor.\n\n"
         "**Answer:** (a) Parallel part: $\\dfrac{1}{R_p} = \\dfrac{1}{4} + \\dfrac{1}{12} = \\dfrac{1}{3}$, so $R_p = 3$ Ω; total $R = 3 + 3 = 6$ Ω. "
         "(b) $I = \\dfrac{12}{6} = 2$ A. (c) The potential difference across the parallel part is $2 \\times 3 = 6$ V, so the current through 12 Ω is $\\dfrac{6}{12} = 0.5$ A."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- Current is the rate of flow of charge (I = Q/t), measured in amperes with an ammeter in series.\n- Potential difference is work done per unit charge (V = W/Q), measured in volts with a voltmeter in parallel.\n"
         "- Ohm's law: V = IR. Resistance R = ρl/A depends on length, area, material and temperature.\n"
         "- Series: R = R₁ + R₂ + R₃, same current. Parallel: 1/R = 1/R₁ + 1/R₂ + 1/R₃, same voltage; houses use parallel wiring.\n"
         "- Heat produced: H = I²Rt; used in heaters, bulbs and fuses.\n- Power P = VI = I²R = V²/R, in watts; energy in kWh, 1 kWh = 3.6 × 10⁶ J."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Write the formula first, substitute with units, and give the answer with its unit.\n- For combinations, solve the parallel parts first, then add the series parts.\n"
         "- For rated appliances, find R = V²/P first, then use it at the new voltage.\n- Learn the reasons: tungsten for filaments, alloys for heaters, copper and aluminium for transmission, parallel wiring at home."),
  blk("s7.flash1", "flashcard", front="Ohm's law", back="V = IR, at constant temperature."),
  blk("s7.flash2", "flashcard", front="1 kWh in joules", back="3.6 × 10⁶ J"),
  blk("s7.flash3", "flashcard", front="Equivalent resistance in parallel", back="1/R = 1/R₁ + 1/R₂ + 1/R₃: less than the smallest resistance."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Electricity",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 11,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: electric current, potential difference and electric current; Ohm's law; resistance, resistivity, factors on which the resistance of a conductor depends; series and parallel combination of resistors and their applications in daily life; heating effect of electric current and its applications in daily life; electric power, interrelation between P, V, I and R.",
  "concepts": ["current_pd", "resistance", "heating_power"], "sections": sections}

# ---------------------------------------------------------------- questions
CP, RS, HP = "current_pd", "resistance", "heating_power"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 11 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]
MSN = ["1 mark: formula", "1 mark: substitution", "1 mark: answer"]
MS2N = ["1 mark: formula", "1 mark: answer"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [CP], it("11.1", 1), "What does an electric circuit mean?", "easy",
    answer_steps=["An electric circuit is a continuous and closed path of an electric current.", "It usually has a source (cell or battery), a switch or key, connecting wires and a device such as a bulb."], marking_scheme=MS2P)
C.q("it1.q2", "very_short_answer", 2, [CP], it("11.1", 2), "Define the unit of current.", "easy",
    answer_steps=["The SI unit of current is the ampere (A).", "1 ampere is the current when 1 coulomb of charge flows through a conductor in 1 second: 1 A = 1 C/1 s."], marking_scheme=MS2P)
C.q("it1.q3", "very_short_answer", 2, [CP], it("11.1", 3), "Calculate the number of electrons constituting one coulomb of charge.",
    answer_steps=["Charge on one electron $= 1.6 \\times 10^{-19}$ C", "$n = \\dfrac{1}{1.6 \\times 10^{-19}} = 6.25 \\times 10^{18}$ electrons"], marking_scheme=MS2N)
C.q("it2.q1", "very_short_answer", 2, [CP], it("11.2", 1), "Name a device that helps to maintain a potential difference across a conductor.", "easy",
    answer_steps=["A cell or a battery.", "The chemical action within it maintains the potential difference between its terminals."], marking_scheme=["1 mark: device", "1 mark: reason"])
C.q("it2.q2", "very_short_answer", 2, [CP], it("11.2", 2), "What is meant by saying that the potential difference between two points is 1 V?", "easy",
    answer_steps=["1 joule of work is done to move a charge of 1 coulomb from one point to the other.", "$1 \\text{ V} = \\dfrac{1 \\text{ J}}{1 \\text{ C}}$"], marking_scheme=MS2P)
C.q("it2.q3", "very_short_answer", 2, [CP], it("11.2", 3), "How much energy is given to each coulomb of charge passing through a 6 V battery?", "easy",
    answer_steps=["$W = VQ$", "$= 6 \\times 1 = 6$ J"], marking_scheme=MS2N)
C.q("it3.q1", "very_short_answer", 2, [RS], it("11.5", 1), "On what factors does the resistance of a conductor depend?", "easy",
    answer_steps=["The length of the conductor (R ∝ l) and its area of cross-section (R ∝ 1/A).", "The nature of its material (resistivity) and its temperature."], marking_scheme=MS2P)
C.q("it3.q2", "very_short_answer", 2, [RS], it("11.5", 2), "Will current flow more easily through a thick wire or a thin wire of the same material, when connected to the same source? Why?",
    answer_steps=["Through the thick wire.", "Resistance is inversely proportional to the area of cross-section; a thick wire has a larger area and so less resistance."], marking_scheme=["1 mark: answer", "1 mark: reason"])
C.q("it3.q3", "very_short_answer", 2, [RS], it("11.5", 3), "Let the resistance of an electrical component remains constant while the potential difference across the two ends of the component decreases to half of its former value. What change will occur in the current through it?",
    answer_steps=["By Ohm's law, $I = \\dfrac{V}{R}$; R stays the same.", "So if V becomes half, the current also becomes half."], marking_scheme=MS2P)
C.q("it3.q4", "very_short_answer", 2, [RS], it("11.5", 4), "Why are coils of electric toasters and electric irons made of an alloy rather than a pure metal?",
    answer_steps=["An alloy has a higher resistivity than a pure metal, so it produces more heat.", "An alloy does not oxidise (burn) readily at high temperatures."], marking_scheme=MS2P)
C.q("it3.q5", "very_short_answer", 2, [RS], it("11.5", 5), "Use the data in Table 11.2 to answer the following: (a) Which among iron and mercury is a better conductor? (b) Which material is the best conductor?", "easy",
    answer_steps=["(a) Iron (resistivity 10.0 × 10⁻⁸ Ω m) is a better conductor than mercury (94.0 × 10⁻⁸ Ω m).", "(b) Silver, which has the lowest resistivity (1.60 × 10⁻⁸ Ω m)."], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("it4.q1", "very_short_answer", 2, [RS], it("11.6.1", 1), "Draw a schematic diagram of a circuit consisting of a battery of three cells of 2 V each, a 5 Ω resistor, an 8 Ω resistor, and a 12 Ω resistor, and a plug key, all connected in series.", "easy",
    answer_steps=["Draw a battery of three 2 V cells joined positive to negative (6 V in all).", "Connect, one after another in a single loop, the 5 Ω, 8 Ω and 12 Ω resistors and a plug key back to the battery."], marking_scheme=["1 mark: battery", "1 mark: series loop"])
C.q("it4.q2", "short_answer", 3, [RS], it("11.6.1", 2), "Redraw the circuit of Question 1, putting in an ammeter to measure the current through the resistors and a voltmeter to measure the potential difference across the 12 Ω resistor. What would be the readings in the ammeter and the voltmeter?",
    answer_steps=["The ammeter goes in series in the loop; the voltmeter goes in parallel across the 12 Ω resistor.", "$R = 5 + 8 + 12 = 25$ Ω, $I = \\dfrac{V}{R} = \\dfrac{6}{25} = 0.24$ A",
                  "Voltmeter reading: $V = IR = 0.24 \\times 12 = 2.88$ V"], marking_scheme=["1 mark: placing meters", "1 mark: ammeter", "1 mark: voltmeter"])
C.q("it5.q1", "very_short_answer", 2, [RS], it("11.6.2", 1), "Judge the equivalent resistance when the following are connected in parallel – (a) 1 Ω and 10⁶ Ω, (b) 1 Ω and 10³ Ω, and 10⁶ Ω.", "medium",
    answer_steps=["In parallel, the equivalent resistance is less than the smallest resistance.", "(a) Slightly less than 1 Ω (about 0.999999 Ω). (b) Also slightly less than 1 Ω (about 0.999 Ω)."], marking_scheme=["1 mark: rule", "1 mark: answers"])
C.q("it5.q2", "short_answer", 3, [RS], it("11.6.2", 2), "An electric lamp of 100 Ω, a toaster of resistance 50 Ω, and a water filter of resistance 500 Ω are connected in parallel to a 220 V source. What is the resistance of an electric iron connected to the same source that takes as much current as all three appliances, and what is the current through it?",
    answer_steps=["$\\dfrac{1}{R} = \\dfrac{1}{100} + \\dfrac{1}{50} + \\dfrac{1}{500} = \\dfrac{16}{500}$", "$R = \\dfrac{500}{16} = 31.25$ Ω", "$I = \\dfrac{V}{R} = \\dfrac{220}{31.25} = 7.04$ A"], marking_scheme=MSN)
C.q("it5.q3", "very_short_answer", 2, [RS], it("11.6.2", 3), "What are the advantages of connecting electrical devices in parallel with the battery instead of connecting them in series?",
    answer_steps=["Each device gets the full voltage and draws the current it needs; if one device fails, the others keep working.", "Each device can be switched on or off independently, and the total resistance of the circuit is lower."], marking_scheme=MS2P)
C.q("it5.q4", "very_short_answer", 2, [RS], it("11.6.2", 4), "How can three resistors of resistances 2 Ω, 3 Ω, and 6 Ω be connected to give a total resistance of (a) 4 Ω, (b) 1 Ω?",
    answer_steps=["(a) 3 Ω and 6 Ω in parallel ($\\dfrac{3 \\times 6}{3 + 6} = 2$ Ω), in series with 2 Ω: $2 + 2 = 4$ Ω",
                  "(b) All three in parallel: $\\dfrac{1}{R} = \\dfrac{1}{2} + \\dfrac{1}{3} + \\dfrac{1}{6} = 1$, so $R = 1$ Ω"], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("it5.q5", "very_short_answer", 2, [RS], it("11.6.2", 5), "What is (a) the highest, (b) the lowest total resistance that can be secured by combinations of four coils of resistance 4 Ω, 8 Ω, 12 Ω, 24 Ω?",
    answer_steps=["(a) Highest, all in series: $4 + 8 + 12 + 24 = 48$ Ω",
                  "(b) Lowest, all in parallel: $\\dfrac{1}{R} = \\dfrac{1}{4} + \\dfrac{1}{8} + \\dfrac{1}{12} + \\dfrac{1}{24} = \\dfrac{12}{24}$, so $R = 2$ Ω"], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("it6.q1", "very_short_answer", 2, [HP], it("11.7", 1), "Why does the cord of an electric heater not glow while the heating element does?",
    answer_steps=["The same current flows through the cord and the element, and the heat produced is $H = I^{2}Rt$.", "The element has a high resistance, so it gets very hot and glows; the copper cord has a very low resistance and stays cool."], marking_scheme=MS2P)
C.q("it6.q2", "very_short_answer", 2, [HP], it("11.7", 2), "Compute the heat generated while transferring 96000 coulomb of charge in one hour through a potential difference of 50 V.",
    answer_steps=["$H = VQ$", "$= 50 \\times 96000 = 4.8 \\times 10^{6}$ J"], marking_scheme=MS2N)
C.q("it6.q3", "very_short_answer", 2, [HP], it("11.7", 3), "An electric iron of resistance 20 Ω takes a current of 5 A. Calculate the heat developed in 30 s.", "easy",
    answer_steps=["$H = I^{2}Rt$", "$= 5^{2} \\times 20 \\times 30 = 15000$ J $= 1.5 \\times 10^{4}$ J"], marking_scheme=MS2N)
C.q("it7.q1", "very_short_answer", 2, [HP], it("11.8", 1), "What determines the rate at which energy is delivered by a current?", "easy",
    answer_steps=["Electric power determines it.", "$P = VI$: the product of the potential difference and the current."], marking_scheme=MS2P)
C.q("it7.q2", "very_short_answer", 2, [HP], it("11.8", 2), "An electric motor takes 5 A from a 220 V line. Determine the power of the motor and the energy consumed in 2 h.",
    answer_steps=["$P = VI = 220 \\times 5 = 1100$ W", "Energy $= P \\times t = 1.1$ kW $\\times 2$ h $= 2.2$ kWh $= 7.92 \\times 10^{6}$ J"], marking_scheme=["1 mark: power", "1 mark: energy"])
# Exercises
C.mcq("ex.q1", [RS], "A piece of wire of resistance R is cut into five equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R′, then the ratio R/R′ is –",
      ["1/25", "1/5", "5", "25"], 3, "Each part has R/5; five of them in parallel give R′ = R/25, so R/R′ = 25.", "hard", source=ex(1))
C.mcq("ex.q2", [HP], "Which of the following terms does not represent electrical power in a circuit?", ["$I^{2}R$", "$IR^{2}$", "$VI$", "$\\dfrac{V^{2}}{R}$"], 1, "P = VI = I²R = V²/R; IR² is not power.", source=ex(2))
C.mcq("ex.q3", [HP], "An electric bulb is rated 220 V and 100 W. When it is operated on 110 V, the power consumed will be –", ["100 W", "75 W", "50 W", "25 W"], 3,
      "R = 220²/100 = 484 Ω; at 110 V, P = 110²/484 = 25 W.", "medium", source=ex(3))
C.mcq("ex.q4", [HP], "Two conducting wires of the same material and of equal lengths and equal diameters are first connected in series and then parallel in a circuit across the same potential difference. The ratio of heat produced in series and parallel combinations would be –",
      ["1:2", "2:1", "1:4", "4:1"], 2, "Series 2R, parallel R/2; at the same V, H = V²t/R, so the ratio is (1/2R) : (2/R) = 1 : 4.", "hard", source=ex(4))
C.q("ex.q5", "very_short_answer", 2, [CP], ex(5), "How is a voltmeter connected in the circuit to measure the potential difference between two points?", "easy",
    answer_steps=["A voltmeter is connected in parallel across the two points.", "Its positive terminal goes to the point at higher potential (towards the positive terminal of the cell)."], marking_scheme=MS2P)
C.q("ex.q6", "short_answer", 3, [RS], ex(6), "A copper wire has diameter 0.5 mm and resistivity of 1.6 × 10⁻⁸ Ω m. What will be the length of this wire to make its resistance 10 Ω? How much does the resistance change if the diameter is doubled?", "hard",
    answer_steps=["$A = \\pi r^{2} = 3.14 \\times (0.25 \\times 10^{-3})^{2} \\approx 1.96 \\times 10^{-7}$ m²", "$l = \\dfrac{RA}{\\rho} = \\dfrac{10 \\times 1.96 \\times 10^{-7}}{1.6 \\times 10^{-8}} \\approx 122.7$ m",
                  "If the diameter is doubled, the area becomes 4 times, so the resistance becomes one-fourth: 2.5 Ω (it decreases by 7.5 Ω)."], marking_scheme=["1 mark: area", "1 mark: length", "1 mark: new resistance"])
C.q("ex.q7", "short_answer", 3, [RS], ex(7), "The values of current I flowing in a given resistor for the corresponding values of potential difference V across the resistor are given below (I in amperes : V in volts): 0.5 : 1.6, 1.0 : 3.4, 2.0 : 6.7, 3.0 : 10.2, 4.0 : 13.2. Plot a graph between V and I and calculate the resistance of that resistor.",
    answer_steps=["Plot V on the y-axis against I on the x-axis: the points lie close to a straight line through the origin.", "Slope of the line $= \\dfrac{\\Delta V}{\\Delta I} = \\dfrac{10.2 - 3.4}{3.0 - 1.0} = 3.4$ Ω",
                  "The resistance of the resistor is about 3.4 Ω."], marking_scheme=["1 mark: graph", "1 mark: slope", "1 mark: answer"])
C.q("ex.q8", "very_short_answer", 2, [RS], ex(8), "When a 12 V battery is connected across an unknown resistor, there is a current of 2.5 mA in the circuit. Find the value of the resistance of the resistor.", "easy",
    answer_steps=["$R = \\dfrac{V}{I}$", "$= \\dfrac{12}{2.5 \\times 10^{-3}} = 4800$ Ω $= 4.8$ kΩ"], marking_scheme=MS2N)
C.q("ex.q9", "very_short_answer", 2, [RS], ex(9), "A battery of 9 V is connected in series with resistors of 0.2 Ω, 0.3 Ω, 0.4 Ω, 0.5 Ω and 12 Ω, respectively. How much current would flow through the 12 Ω resistor?",
    answer_steps=["$R = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4$ Ω", "$I = \\dfrac{9}{13.4} \\approx 0.67$ A; in series the same current flows through the 12 Ω resistor."], marking_scheme=["1 mark: total R", "1 mark: current"])
C.q("ex.q10", "very_short_answer", 2, [RS], ex(10), "How many 176 Ω resistors (in parallel) are required to carry 5 A on a 220 V line?",
    answer_steps=["Required resistance $R = \\dfrac{V}{I} = \\dfrac{220}{5} = 44$ Ω", "n equal resistors in parallel give $\\dfrac{176}{n} = 44$, so $n = 4$"], marking_scheme=["1 mark: R", "1 mark: n"])
C.q("ex.q11", "very_short_answer", 2, [RS], ex(11), "Show how you would connect three resistors, each of resistance 6 Ω, so that the combination has a resistance of (i) 9 Ω, (ii) 4 Ω.",
    answer_steps=["(i) Two in parallel (3 Ω) in series with the third: $3 + 6 = 9$ Ω", "(ii) Two in series (12 Ω) in parallel with the third: $\\dfrac{12 \\times 6}{12 + 6} = 4$ Ω"], marking_scheme=["1 mark: (i)", "1 mark: (ii)"])
C.q("ex.q12", "very_short_answer", 2, [HP], ex(12), "Several electric bulbs designed to be used on a 220 V electric supply line, are rated 10 W. How many lamps can be connected in parallel with each other across the two wires of 220 V line if the maximum allowable current is 5 A?",
    answer_steps=["Current through one lamp $= \\dfrac{P}{V} = \\dfrac{10}{220} = \\dfrac{1}{22}$ A", "Number of lamps $= \\dfrac{5}{1/22} = 110$"], marking_scheme=["1 mark: current per lamp", "1 mark: number"])
C.q("ex.q13", "short_answer", 3, [RS], ex(13), "A hot plate of an electric oven connected to a 220 V line has two resistance coils A and B, each of 24 Ω resistance, which may be used separately, in series, or in parallel. What are the currents in the three cases?",
    answer_steps=["Separately: $I = \\dfrac{220}{24} \\approx 9.17$ A", "In series: $R = 48$ Ω, $I = \\dfrac{220}{48} \\approx 4.58$ A", "In parallel: $R = 12$ Ω, $I = \\dfrac{220}{12} \\approx 18.33$ A"],
    marking_scheme=["1 mark: separately", "1 mark: series", "1 mark: parallel"])
C.q("ex.q14", "short_answer", 3, [HP], ex(14), "Compare the power used in the 2 Ω resistor in each of the following circuits: (i) a 6 V battery in series with 1 Ω and 2 Ω resistors, and (ii) a 4 V battery in parallel with 12 Ω and 2 Ω resistors.",
    answer_steps=["(i) $I = \\dfrac{6}{1 + 2} = 2$ A, $P = I^{2}R = 2^{2} \\times 2 = 8$ W", "(ii) The 2 Ω resistor has the full 4 V across it: $P = \\dfrac{V^{2}}{R} = \\dfrac{4^{2}}{2} = 8$ W",
                  "The power used in the 2 Ω resistor is the same, 8 W, in both circuits."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: comparison"])
C.q("ex.q15", "very_short_answer", 2, [HP], ex(15), "Two lamps, one rated 100 W at 220 V, and the other 60 W at 220 V, are connected in parallel to electric mains supply. What current is drawn from the line if the supply voltage is 220 V?",
    answer_steps=["Total power $= 100 + 60 = 160$ W", "$I = \\dfrac{P}{V} = \\dfrac{160}{220} \\approx 0.73$ A"], marking_scheme=["1 mark: total power", "1 mark: current"])
C.q("ex.q16", "very_short_answer", 2, [HP], ex(16), "Which uses more energy, a 250 W TV set in 1 hr, or a 1200 W toaster in 10 minutes?",
    answer_steps=["TV: $250 \\times 1 = 250$ Wh. Toaster: $1200 \\times \\dfrac{10}{60} = 200$ Wh", "The TV set uses more energy."], marking_scheme=["1 mark: energies", "1 mark: answer"])
C.q("ex.q17", "very_short_answer", 2, [HP], ex(17), "An electric heater of resistance 44 Ω draws 5 A from the service mains for 2 hours. Calculate the rate at which heat is developed in the heater.", "easy",
    answer_steps=["$P = I^{2}R$", "$= 5^{2} \\times 44 = 1100$ W (1100 J of heat every second)"], marking_scheme=MS2N)
C.q("ex.q18", "long_answer", 5, [RS, HP], ex(18), "Explain the following.\n\n(a) Why is the tungsten used almost exclusively for filament of electric lamps?\n\n(b) Why are the conductors of electric heating devices, such as bread-toasters and electric irons, made of an alloy rather than a pure metal?\n\n"
    "(c) Why is the series arrangement not used for domestic circuits?\n\n(d) How does the resistance of a wire vary with its area of cross-section?\n\n(e) Why are copper and aluminium wires usually employed for electricity transmission?", "medium",
    answer_steps=["(a) Tungsten has a very high melting point (3380 °C) and high resistivity, so it can glow white-hot without melting.", "(b) Alloys have higher resistivity and do not oxidise (burn) readily at high temperatures.",
                  "(c) In series, all appliances share the voltage, cannot get the current each needs, and all stop if one fails; they cannot be switched independently.",
                  "(d) Resistance is inversely proportional to the area of cross-section: a thicker wire has less resistance.", "(e) Copper and aluminium have very low resistivity, so little energy is lost as heat in the wires."],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: (c)", "1 mark: (d)", "1 mark: (e)"])
# CBSE sample paper
C.q("sqp34a", "very_short_answer", 2, [RS], SQP("34(A)"), "You are given four resistors each having resistance of R ohm. Find the maximum and minimum resistance that can be made with these four resistors.", "easy",
    answer_steps=["Maximum, all four in series: $R + R + R + R = 4R$", "Minimum, all four in parallel: $\\dfrac{1}{R_{min}} = \\dfrac{4}{R}$, so $R_{min} = \\dfrac{R}{4}$"], marking_scheme=["1 mark: maximum", "1 mark: minimum"])
C.q("sqp34b", "very_short_answer", 2, [RS], SQP("34(B)"), "A copper wire has a length L = 2 m, a cross-sectional area A = 0.5 mm², and resistivity ρ = 1.7 × 10⁻⁸ Ω m. Calculate the resistance of another wire made of the same material whose length is twice the length of the wire but has the same cross-sectional area.",
    answer_steps=["$R_{1} = \\dfrac{\\rho l}{A} = \\dfrac{1.7 \\times 10^{-8} \\times 2}{0.5 \\times 10^{-6}} = 0.068$ Ω", "With double the length, $R_{2} = 2R_{1} = 0.136$ Ω"], marking_scheme=["1 mark: first wire", "1 mark: new wire"])
C.q("sqp36", "short_answer", 3, [RS], SQP(36), "A student needs to make a 0.12 Ω resistor. She has some copper wire of 0.80 mm diameter. Resistivity of copper is 1.8 × 10⁻⁸ Ω m.\n\n(i) Determine the cross-sectional area of the wire.\n\n(ii) Calculate the length of wire required for the 0.12 Ω resistor.",
    answer_steps=["(i) $A = \\pi r^{2} = 3.14 \\times (0.40 \\times 10^{-3})^{2} \\approx 5 \\times 10^{-7}$ m²", "(ii) $l = \\dfrac{RA}{\\rho}$", "$= \\dfrac{0.12 \\times 5 \\times 10^{-7}}{1.8 \\times 10^{-8}} \\approx 3.33$ m"],
    marking_scheme=["1 mark: area", "1 mark: formula", "1 mark: length"])
C.q("sqp39a", "long_answer", 5, [HP], SQP("39(A)"), "(i) Explain why in household circuits only the fuse is connected in series with all the rest of the appliances but all appliances are connected in parallel to each other.\n\n"
    "(ii) In a household circuit, an electric heater of power 1500 W and a fan of power 500 W are connected in parallel to a 220 V supply. A fuse rated for 10 A is connected to the circuit to protect it from excessive current.\n\n(a) Calculate the total current drawn by the heater and the fan.\n\n(b) Determine whether the 10 A fuse is appropriate for this circuit or if it will blow.", "medium",
    answer_steps=["(i) The fuse is in series with all appliances so that it can cut off the whole circuit if the current becomes too large (overload or short circuit).",
                  "The appliances are in parallel so that each gets the same full voltage, draws only the current it needs, and works independently.",
                  "(ii)(a) Heater: $I = \\dfrac{1500}{220} \\approx 6.82$ A; fan: $I = \\dfrac{500}{220} \\approx 2.27$ A", "Total current $\\approx 9.09$ A",
                  "(b) 9.09 A is less than 10 A, so the 10 A fuse is appropriate and will not blow."],
    marking_scheme=["1 mark: fuse in series", "1 mark: parallel appliances", "1 mark: currents", "1 mark: total", "1 mark: fuse"])
C.q("sqp39b", "long_answer", 5, [HP], SQP("39(B)"), "Two resistors, R₁ = 6 Ω and R₂ = 12 Ω, are connected in parallel to a 24 V battery. The circuit operates for 5 minutes.\n\n(i) Calculate the total heat generated in both resistors.\n\n(ii) If each resistor has a power rating of 100 W, determine whether it is safe to use these resistors in the circuit.", "medium",
    answer_steps=["Each resistor has 24 V across it. $P_{1} = \\dfrac{V^{2}}{R_{1}} = \\dfrac{24^{2}}{6} = 96$ W", "$P_{2} = \\dfrac{24^{2}}{12} = 48$ W",
                  "(i) $H = (P_{1} + P_{2})t = 144 \\times 300 = 43200$ J", "(ii) 96 W and 48 W are both less than the 100 W rating.", "So it is safe to use these resistors."],
    marking_scheme=["1 mark: P1", "1 mark: P2", "1 mark: heat", "1 mark: comparison", "1 mark: conclusion"])
# GSEB
C.mcq("gseb2025_3", [CP], "1 µA = ____ A", ["$10^{-6}$", "$10^{-3}$", "$10^{3}$", "$10^{6}$"], 0, "Micro means 10⁻⁶.", source=gseb(2025, "3"))
C.mcq("gseb2025_8", [CP], "The SI unit of electric potential difference is named after the scientist ____.", ["Andre-Marie Ampere", "Alessandro Volta", "Georg Simon Ohm"], 1, "The volt is named after Alessandro Volta.", source=gseb(2025, "8"))
C.q("gseb2025_31", "very_short_answer", 2, [CP], gseb(2025, "31"), "A current of 0.5 A is drawn by a filament of an electric bulb for 20 minutes. Find the amount of electric charge that flows through the circuit.", "easy",
    answer_steps=["$Q = It$, with $t = 20 \\times 60 = 1200$ s", "$Q = 0.5 \\times 1200 = 600$ C"], marking_scheme=MS2N)
C.q("gseb2025_32", "very_short_answer", 2, [RS], gseb(2025, "32"), "The resistivities of some materials are: silver 1.60 × 10⁻⁸ Ω m, copper 1.62 × 10⁻⁸ Ω m, iron 10.0 × 10⁻⁸ Ω m, mercury 94.0 × 10⁻⁸ Ω m, manganese 1.84 × 10⁻⁶ Ω m.\n\n(a) Which among iron and mercury is a better conductor?\n\n(b) Which material is the best conductor?", "easy",
    answer_steps=["(a) Iron, because its resistivity is lower than that of mercury.", "(b) Silver, which has the lowest resistivity."], marking_scheme=["1 mark: (a)", "1 mark: (b)"])
C.q("gseb2024_32", "very_short_answer", 2, [CP], gseb(2024, "32"), "How much work is done in moving a charge of 2 C across two points having a potential difference 12 V?", "easy",
    answer_steps=["$W = VQ$", "$= 12 \\times 2 = 24$ J"], marking_scheme=MS2N)
C.q("gseb2024_46", "short_answer", 3, [HP], gseb(2024, "46"), "Explain the practical applications of heating effect of electric current with examples.",
    answer_steps=["Heating appliances: electric iron, toaster, oven, kettle and room heater use coils of an alloy such as nichrome that get hot when current flows.",
                  "Electric bulb: the thin tungsten filament gets so hot that it glows and gives light; the bulb is filled with nitrogen and argon.",
                  "Electric fuse: a wire of low melting point in series melts when the current is too large, breaking the circuit and protecting the appliances."], marking_scheme=MS3)
# Shine MCQs
C.mcq("mcq01", [CP], "The SI unit of electric charge is:", ["coulomb", "ampere", "volt", "ohm"], 0, "Charge is measured in coulombs; current in amperes.")
C.mcq("mcq02", [CP], "An ammeter is connected in a circuit:", ["in series", "in parallel", "across the battery only", "either way"], 0, "An ammeter must carry the whole current, so it goes in series.")
C.mcq("mcq03", [RS], "The resistance of a wire is 10 Ω. If its length is doubled (same thickness), its resistance becomes:", ["20 Ω", "5 Ω", "40 Ω", "10 Ω"], 0, "R ∝ l, so doubling the length doubles R.", "medium")
C.mcq("mcq04", [RS], "The SI unit of resistivity is:", ["ohm metre", "ohm", "ohm per metre", "volt metre"], 0, "From ρ = RA/l: Ω × m² / m = Ω m.")
C.mcq("mcq05", [RS], "Two resistors of 4 Ω and 12 Ω in parallel have an equivalent resistance of:", ["3 Ω", "16 Ω", "8 Ω", "0.33 Ω"], 0, "R = (4 × 12)/(4 + 12) = 3 Ω.", "medium")
C.mcq("mcq06", [HP], "If the current through a resistor is doubled, the heat produced in the same time becomes:", ["four times", "double", "half", "the same"], 0, "H = I²Rt, so doubling I makes H four times.", "medium")
C.mcq("mcq07", [HP], "1 kWh is equal to:", ["$3.6 \\times 10^{6}$ J", "$3.6 \\times 10^{3}$ J", "1000 J", "3600 J"], 0, "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J.")
C.mcq("mcq08", [HP], "The filament of an electric bulb is made of:", ["tungsten", "copper", "nichrome", "aluminium"], 0, "Tungsten has a very high melting point.")
C.mcq("mcq09", [HP], "A fuse wire should have:", ["a low melting point", "a high melting point", "very low resistance like copper", "no resistance"], 0, "It must melt quickly when the current is too large.")
C.mcq("mcq10", [HP], "An appliance rated 1000 W, 220 V is used for 2 hours daily. Energy used in 30 days is:", ["60 kWh", "2 kWh", "60 000 kWh", "6 kWh"], 0, "1 kW × 2 h × 30 = 60 kWh.", "medium")
# Assertion-reason
C.ar("ar1", [RS], "Household appliances are connected in parallel.", "In parallel, each appliance gets the same voltage and can work independently.", 0, "That is exactly what a home needs: R explains A.")
C.ar("ar2", [HP], "The filament of a bulb glows but the connecting wires do not.", "The filament has a much higher resistance than the connecting wires.", 0, "With the same current, H = I²Rt is far larger in the filament: R explains A.")
C.ar("ar3", [RS], "The equivalent resistance of resistors in parallel is more than the largest resistance.", "In parallel, the reciprocals of the resistances add up.", 3, "A is false: it is less than the smallest resistance. R is true.")
C.ar("ar4", [RS], "A thick wire has less resistance than a thin wire of the same length and material.", "Resistance is inversely proportional to the area of cross-section.", 0, "A larger area gives less resistance: R explains A.")
C.ar("ar5", [CP], "A voltmeter is connected in series in a circuit.", "A voltmeter has a very high resistance.", 3, "A is false: a voltmeter is connected in parallel. R is true.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [RS], SHINE, "State Ohm's law. Draw the shape of the V–I graph for a metallic conductor.", "easy",
    answer_steps=["At constant temperature, the current through a metallic conductor is directly proportional to the potential difference across its ends: V = IR.", "The V–I graph is a straight line passing through the origin; its slope gives the resistance."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [HP], SHINE, "An electric bulb is rated 60 W, 220 V. Find its resistance and the current it draws.",
    answer_steps=["$R = \\dfrac{V^{2}}{P} = \\dfrac{220^{2}}{60} \\approx 806.7$ Ω", "$I = \\dfrac{P}{V} = \\dfrac{60}{220} \\approx 0.27$ A"], marking_scheme=["1 mark: R", "1 mark: I"])
check(near(220**2 / 60, 806.7, 0.05) and near(60 / 220, 0.27, 0.005), "Shine vsa2")
C.q("sa1", "short_answer", 3, [RS], SHINE, "Derive the expression for the equivalent resistance of three resistors connected in series.",
    answer_steps=["In series the same current I flows through each resistor, and the total potential difference is the sum: $V = V_{1} + V_{2} + V_{3}$",
                  "By Ohm's law, $V_{1} = IR_{1}$, $V_{2} = IR_{2}$, $V_{3} = IR_{3}$, and for the combination $V = IR$", "So $IR = IR_{1} + IR_{2} + IR_{3}$, giving $R = R_{1} + R_{2} + R_{3}$"],
    marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [HP], SHINE, "A family uses a 1.5 kW geyser for 1 hour and five 20 W LED bulbs for 6 hours every day. Find the energy used in 30 days and the cost at ₹ 6 per unit.",
    answer_steps=["Daily: geyser $1.5 \\times 1 = 1.5$ kWh; bulbs $5 \\times 0.02 \\times 6 = 0.6$ kWh; total 2.1 kWh", "In 30 days: $2.1 \\times 30 = 63$ kWh (units)", "Cost $= 63 \\times 6 = $ ₹ 378"],
    marking_scheme=["1 mark: daily energy", "1 mark: monthly energy", "1 mark: cost"])
check(Fr(15, 10) + 5 * Fr(2, 100) * 6 == Fr(21, 10) and Fr(21, 10) * 30 == 63 and 63 * 6 == 378, "Shine sa2")
C.q("la1", "long_answer", 5, [RS], SHINE, "Derive the expression for the equivalent resistance of three resistors in parallel. Find the equivalent resistance of 2 Ω, 3 Ω and 6 Ω in parallel and the current drawn from a 6 V battery.", "medium",
    answer_steps=["In parallel the potential difference V is the same across each resistor, and the total current is the sum: $I = I_{1} + I_{2} + I_{3}$",
                  "By Ohm's law, $\\dfrac{V}{R} = \\dfrac{V}{R_{1}} + \\dfrac{V}{R_{2}} + \\dfrac{V}{R_{3}}$, so $\\dfrac{1}{R} = \\dfrac{1}{R_{1}} + \\dfrac{1}{R_{2}} + \\dfrac{1}{R_{3}}$",
                  "$\\dfrac{1}{R} = \\dfrac{1}{2} + \\dfrac{1}{3} + \\dfrac{1}{6} = 1$", "$R = 1$ Ω", "$I = \\dfrac{V}{R} = \\dfrac{6}{1} = 6$ A"],
    marking_scheme=["1 mark: same V", "1 mark: derivation", "1 mark: substitution", "1 mark: R", "1 mark: current"])
C.q("la2", "long_answer", 5, [HP], SHINE, "State Joule's law of heating. An electric iron of 1 kW is operated on 220 V for 30 minutes. Find (a) the current drawn (b) its resistance (c) the heat produced.", "medium",
    answer_steps=["Joule's law: the heat produced in a resistor is $H = I^{2}Rt$: proportional to the square of the current, the resistance and the time.",
                  "(a) $I = \\dfrac{P}{V} = \\dfrac{1000}{220} \\approx 4.55$ A", "(b) $R = \\dfrac{V^{2}}{P} = \\dfrac{220^{2}}{1000} = 48.4$ Ω", "(c) $H = Pt = 1000 \\times 1800$", "$= 1.8 \\times 10^{6}$ J"],
    marking_scheme=["1 mark: law", "1 mark: (a)", "1 mark: (b)", "1 mark: (c) formula", "1 mark: (c) answer"])
check(near(1000 / 220, 4.55, 0.005) and Fr(220**2, 1000) == Fr(484, 10) and 1000 * 1800 == 1_800_000, "Shine la2")
C.q("cb1", "case_based", 4, [HP], SHINE,
    "In Riya's house, the electricity bill showed 240 units for a month. Her father said the AC (1.5 kW) runs 4 hours a day for 30 days, and the rest is used by other appliances.\n\n"
    "(i) What is one 'unit' of electricity? (1)\n\n(ii) How many units does the AC use in the month? (1)\n\n(iii) How many units are used by the other appliances, and what is the cost of the AC's energy at ₹ 7 per unit? OR Express one unit in joules. (2)",
    answer_steps=["(i) 1 kilowatt hour (kWh).", "(ii) $1.5 \\times 4 \\times 30 = 180$ kWh",
                  "(iii) Other appliances: $240 - 180 = 60$ units; cost of the AC's energy $= 180 \\times 7 = $ ₹ 1260. OR $1 \\text{ kWh} = 3.6 \\times 10^{6}$ J"],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [RS], SHINE,
    "In the lab, Karan joined two identical bulbs to a battery, first one after the other, and then side by side. In the first case both bulbs were dim; in the second both glowed brightly. When he removed one bulb, in the first case the other went off, but in the second it kept glowing.\n\n"
    "(i) Name the first and the second arrangement. (1)\n\n(ii) Why did the other bulb go off in the first arrangement? (1)\n\n(iii) Why were the bulbs brighter in the second arrangement? OR Two 10 Ω resistors are joined in each way. Find the equivalent resistance in both cases. (2)",
    answer_steps=["(i) Series, then parallel.", "(ii) In series there is only one path; removing a bulb breaks the circuit and the current stops.",
                  "(iii) In parallel each bulb gets the full battery voltage, so more current flows through each and more power is used. OR Series: $10 + 10 = 20$ Ω; parallel: $\\dfrac{10 \\times 10}{10 + 10} = 5$ Ω"],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch11.q.ex."))
