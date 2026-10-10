"""CBSE Class 10 Science Ch 12: Magnetic Effects of Electric Current.
Direction questions are checked with cross products (F = q v x B, or I L x B)."""
import sys
from sci_common import Chapter, check, SQP, SHINE, pyq_gseb

ROOT = sys.argv[1]
CH_ID = "cbse.c10.science.ncert_rationalised.ch12"
PATH = "app_core/content/cbse/class10/science/ncert_rationalised/ch12_magnetic_effects_of_current"
C = Chapter("sci10ch12")
blk = C.blk

def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
EAST, NORTH, UP = (1, 0, 0), (0, 1, 0), (0, 0, 1)
neg = lambda v: tuple(-x for x in v)
check(cross(neg(EAST), UP) == NORTH, "12.3 Q3: alpha particle going west, pushed north -> field upward")
FORWARD, RIGHT = (0, 1, 0), (1, 0, 0)
check(cross(neg(FORWARD), neg(UP)) == RIGHT, "ex 6: electron beam forward (current backward), force right -> field downward")
check(round(2000 / 220, 2) == 9.09, "12.4 Q2: oven draws 9.09 A")

RULES = ("| Rule | Gives | How to use it |\n|---|---|---|\n"
         "| Right-hand thumb rule | direction of the magnetic field around a straight current-carrying wire | hold the wire in the right hand with the thumb along the current; the curled fingers show the field |\n"
         "| Fleming's left-hand rule | direction of the force on a current-carrying conductor in a magnetic field | stretch thumb, forefinger and middle finger of the left hand at right angles: forefinger = field, middle finger = current, thumb = force (motion) |")
WIRES = ("| Wire | Insulation colour | Role |\n|---|---|---|\n| Live (positive) | red | brings current in at 220 V |\n| Neutral (negative) | black | returns the current |\n"
         "| Earth | green | safety: connects the metal body of an appliance to the ground |")

sections = [
 {"id": "s1", "title": "Electricity makes magnets", "blocks": [
  blk("s1.hook", "hook", title="A compass near a wire",
    body="Put a compass needle under a wire and switch the current on: the needle suddenly turns. Switch it off and the needle swings back. A wire carrying current behaves like a magnet!\n\n"
         "This discovery, made by Hans Christian Oersted in 1820, joined electricity and magnetism. In this chapter you will learn about magnetic fields, the fields made by currents, the force on a current in a magnetic field, and how your house is wired safely."),
  blk("s1.inspiration", "inspiration", title="Measuring magnetism in molecules", person="Shanti Swarup Bhatnagar", years="1894–1955",
    body="Shanti Swarup Bhatnagar, born in Bhera (now in Pakistan), worked on **magnetochemistry**: using magnetic properties to understand how molecules are built. With K. N. Mathur he designed the **Bhatnagar–Mathur magnetic interference balance**.\n\n"
         "He was the first Director-General of India's **Council of Scientific and Industrial Research (CSIR)**, which set up many national laboratories. India's top science award for young scientists, the **Shanti Swarup Bhatnagar Prize**, is named after him.",
    future="Electromagnetism leads to careers in electrical engineering, electric vehicles, power distribution, medical imaging (MRI), electronics and the design of motors and speakers."),
  blk("s1.socratic", "socratic_question", question="A compass needle placed near a current-carrying wire turns. What does this tell you?",
    options=["The current produces a magnetic field around the wire", "The wire has become hot", "The compass has lost its magnetism"], correct_index=0,
    explanation="A compass needle is a small magnet; it turns only in a magnetic field, so the current must be producing one."),
 ]},
 {"id": "s2", "title": "Magnetic field and field lines", "blocks": [
  blk("s2.reveal", "theory", title="The region around a magnet", revision=True,
    body="A **compass needle** is a small bar magnet; its north-seeking end is the **north pole**. It is deflected near a bar magnet because it experiences a force in the magnet's **magnetic field**, the region around a magnet where its force can be detected. "
         "A magnetic field has both **magnitude and direction**.\n\n"
         "**Magnetic field lines** (seen with iron filings or traced with a compass):\n- Outside the magnet they go from the **north pole to the south pole**; inside, from south to north, so they are **closed curves**.\n"
         "- The direction of the field at a point is the direction in which a compass north pole would point there.\n"
         "- Where the lines are **crowded**, the field is **stronger** (near the poles).\n- **No two field lines ever cross**: if they did, a compass at that point would have to point in two directions at once."),
  blk("s2.check", "knowledge_check", question="Why do two magnetic field lines never intersect?",
    options=["A compass at the crossing would point in two directions at once", "Field lines repel each other", "Field lines exist only inside the magnet", "They do cross near the poles"], correct_index=0,
    explanation="At any point the field has only one direction, so two lines cannot pass through the same point."),
 ]},
 {"id": "s3", "title": "Magnetic field due to a current", "blocks": [
  blk("s3.thm", "theory", title="Wire, loop and solenoid", revision=True,
    body="**Straight wire:** the field lines are **concentric circles** centred on the wire, in a plane perpendicular to it. The field is stronger for a **larger current** and **closer to the wire**. "
         "Reversing the current reverses the field. Its direction is given by the **right-hand thumb rule**.\n\n"
         "**Circular loop:** each small part of the loop makes circles around itself; near the centre they look like **straight lines**. A coil of n turns gives a field n times as strong as a single turn, because the fields add up.\n\n"
         "**Solenoid:** a coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder. Its field pattern is like that of a **bar magnet**: one end acts as a north pole and the other as a south pole. "
         "Inside, the field lines are **parallel straight lines**: the field is **uniform**. A soft iron core placed inside makes a strong **electromagnet**, whose magnetism can be switched on and off.\n\n" + RULES),
  blk("s3.check", "knowledge_check", question="The magnetic field inside a long current-carrying solenoid is:",
    options=["the same at all points (uniform)", "zero", "strongest near the wire only", "made of concentric circles"], correct_index=0,
    explanation="Inside a solenoid the field lines are parallel straight lines, so the field is uniform."),
 ]},
 {"id": "s4", "title": "Force on a current-carrying conductor", "blocks": [
  blk("s4.thm", "theory", title="Fleming's left-hand rule", revision=True,
    body="Just as a current exerts a force on a magnet, a magnet exerts an equal and opposite force on a current-carrying conductor (suggested by André-Marie Ampère).\n\n"
         "In the activity with an aluminium rod AB hung between the poles of a horse-shoe magnet, the rod is pushed sideways when current flows. Reversing the current, or the field, reverses the push.\n\n"
         "- The force is **largest** when the current is **perpendicular** to the magnetic field (and zero when it is parallel).\n"
         "- The force increases with the **current**, the **strength of the field** and the **length** of the conductor in the field.\n"
         "- Its direction is given by **Fleming's left-hand rule**: forefinger along the field, middle finger along the current, thumb gives the force.\n"
         "- A moving charged particle is also a current: a beam of electrons moving one way is a current in the opposite direction.\n\n"
         "Devices such as electric motors, loudspeakers and measuring instruments use this force. In medicine, the weak magnetic fields produced inside the body by nerve currents are used for imaging; **MRI** (magnetic resonance imaging) shows the inside of the body."),
  blk("s4.check", "knowledge_check", question="When is the force on a current-carrying conductor in a magnetic field the largest?",
    options=["When the current is perpendicular to the field", "When the current is parallel to the field", "When the current is zero", "It is the same in all directions"], correct_index=0,
    explanation="The force is maximum when the conductor is at right angles to the field and zero when it is along the field."),
 ]},
 {"id": "s5", "title": "Domestic electric circuits", "blocks": [
  blk("s5.thm", "theory", title="How your house is wired", revision=True,
    body="**AC and DC:** a cell gives **direct current (DC)**, which flows in one direction only. Power stations supply **alternating current (AC)**, which reverses its direction periodically. "
         "In India the frequency of AC is **50 Hz**: it changes direction every 1/100 second. The advantage of AC is that it can be transmitted over long distances without much loss of energy.\n\n"
         "Electricity reaches the house through the mains at **220 V**, through three wires:\n\n" + WIRES + "\n\n"
         "- After the meter and the main **fuse**, there are usually two circuits: a **15 A** circuit for heavy appliances (geyser, air cooler, iron) and a **5 A** circuit for bulbs and fans.\n"
         "- All appliances are connected in **parallel**, each with its own switch, so each gets the same voltage.\n"
         "- The **earth wire** connects the metal body of an appliance to a metal plate deep in the ground. If the live wire touches the body, current leaks to the earth, so the user does not get a severe shock.\n"
         "- A **short circuit** happens when the live wire and the neutral wire come in direct contact (for example through damaged insulation). The resistance falls almost to zero and the current **increases heavily**.\n"
         "- **Overloading** happens when too many appliances are run from one socket or the supply voltage rises suddenly.\n"
         "- The **fuse** melts and breaks the circuit when the current is too large, preventing damage and fire. Today, **miniature circuit breakers (MCBs)** are also used."),
  blk("s5.check", "knowledge_check", question="At the time of a short circuit, the current in the circuit:",
    options=["increases heavily", "reduces substantially", "does not change", "becomes zero"], correct_index=0,
    explanation="Live and neutral touch directly, the resistance becomes nearly zero, and a very large current flows."),
 ]},
 {"id": "s6", "title": "Rules and safety at a glance", "blocks": [
  blk("s6.thm", "theory", title="Putting it together", revision=True,
    body="- **Two ways to produce a magnetic field:** a permanent magnet, and an electric current (a straight wire, a loop, a solenoid or an electromagnet).\n"
         "- **Two rules, two hands:** the right hand for the field around a current; the left hand for the force on a current.\n"
         "- **Field strength:** more current, more turns and an iron core give a stronger field.\n"
         "- **Safety devices:** the fuse (or MCB) and the earth wire.\n- **Avoid overloading:** do not connect too many appliances to one socket, and use appliances within the current rating of the circuit."),
  blk("s6.check", "knowledge_check", question="An electric oven of 2 kW is operated on a 220 V circuit with a current rating of 5 A. What happens?",
    options=["It draws about 9 A, so the fuse blows or the circuit overloads", "It works normally", "It draws only 2 A", "The voltage doubles"], correct_index=0,
    explanation="I = P/V = 2000/220 ≈ 9.1 A, more than the 5 A rating."),
  blk("s6.memory", "memory_trick", title="Hands and colours",
    body="- **Fleming's left-hand rule, \"FBI\":** thumb = **F**orce, forefinger = **B** (field), middle finger = **I** (current).\n"
         "- **Right-hand thumb rule:** thumb = current, curled fingers = field (like gripping a cricket bat).\n"
         "- **Wire colours:** **R**ed = **R**isky live; **B**lack = **B**ack (neutral); **G**reen = **G**round (earth)."),
  blk("s6.mistakes", "common_mistakes", title="Common mistakes",
    body="- Using the right hand for the force on a conductor: the force needs the **left** hand.\n- Forgetting that a beam of electrons is a current in the **opposite** direction.\n"
         "- Saying field lines go from south to north outside a magnet: outside, they go from **north to south**.\n- Writing that the earth wire carries current all the time: it carries current only when there is a leakage.\n"
         "- Saying that a fuse is connected in parallel: it is in series with the live wire."),
  blk("s6.tip", "teacher_tip", title="Try it in class",
    body="Sprinkle iron filings on a card over a bar magnet and tap it to show field lines; repeat with a thick wire passing through the card connected to a battery for a moment to show circles. "
         "Wind insulated wire round an iron nail, connect a cell, and pick up pins: a simple electromagnet. Show students the three coloured wires in a plug top, with the supply switched off."),
 ]},
 {"id": "s7", "title": "Think, connect, master", "blocks": [
  blk("s7.reflection", "reflection", title="Explain it in your own words",
    body="Explain to a friend how the earth wire protects us from a shock, and how a fuse protects the house from a fire."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 11:** current, resistance and power; the fuse uses the heating effect.\n- **Class 12 Physics:** moving charges and magnetism, electromagnetic induction, alternating current and motors.\n"
         "- **Everyday life:** electric fans, mixers, loudspeakers, MRI machines and the wiring of every house."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="A positively charged particle (alpha particle) is projected towards the west and is deflected towards the north by a magnetic field.\n\n(a) What is the direction of the field? (b) Which rule did you use? (c) What would happen to an electron moving the same way in the same field?\n\n"
         "**Answer:** (a) Upward (vertically up). (b) Fleming's left-hand rule: middle finger (current) towards the west, thumb (force) towards the north, so the forefinger (field) points upward. "
         "(c) An electron moving west is a current towards the east, so it is pushed the opposite way: towards the south."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- A magnetic field has magnitude and direction; field lines go from north to south outside a magnet, are closed curves, are crowded where the field is strong, and never cross.\n"
         "- A current produces a magnetic field: concentric circles around a straight wire (right-hand thumb rule), straight lines at the centre of a loop, and a uniform field inside a solenoid.\n"
         "- A current-carrying conductor in a magnetic field feels a force, largest when perpendicular to the field; direction by Fleming's left-hand rule.\n"
         "- India's mains supply is AC at 220 V and 50 Hz; houses use live, neutral and earth wires, parallel connections, fuses and MCBs.\n"
         "- Short circuits and overloading cause very large currents; fuses and earthing protect us."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- Practise diagrams: field lines of a bar magnet, a straight wire, a circular loop and a solenoid, and a domestic circuit with fuse and earth wire.\n"
         "- Learn to state both rules with the finger meanings.\n- For direction questions, convert electron motion into current direction first.\n"
         "- Know the colours of the three wires and the ratings 5 A and 15 A."),
  blk("s7.flash1", "flashcard", front="Shape of the field lines around a straight current-carrying wire", back="Concentric circles centred on the wire."),
  blk("s7.flash2", "flashcard", front="Frequency of AC in India", back="50 Hz"),
  blk("s7.flash3", "flashcard", front="Colour of the earth wire", back="Green (live is red, neutral is black)."),
 ]},
]
chapter = {"schema_version": 1, "id": CH_ID, "title": "Magnetic Effects of Electric Current",
  "book": "NCERT Science, Class 10 (rationalised edition)", "board": "CBSE", "class": 10, "subject": "science", "chapter_number": 12,
  "languages": ["en"], "status": "reviewed", "reviewed_by": "Claude (AI) - awaiting teacher approval", "reviewed_on": "2026-10-10",
  "syllabus_note": "Follows the CBSE 2025-26 syllabus: magnetic field, field lines, field due to a current-carrying conductor, field due to a current-carrying coil or solenoid; force on a current-carrying conductor, Fleming's left-hand rule; direct current, alternating current, frequency of AC, advantage of AC over DC; domestic electric circuits.",
  "concepts": ["field_lines", "field_of_current", "force_domestic"], "sections": sections}

# ---------------------------------------------------------------- questions
FL, FC, FD = "field_lines", "field_of_current", "force_domestic"
def it(sec, n): return {"kind": "ncert_intext", "section": sec, "question": n}
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 12 exercises", "question": n}
def gseb(year, n, marks=None):
    s = pyq_gseb(year, n)
    if marks: s["original_marks"] = marks
    return s
MS2P = ["1 mark: first point", "1 mark: second point"]
MS3 = ["1 mark: first point", "1 mark: second point", "1 mark: third point"]

# In-text
C.q("it1.q1", "very_short_answer", 2, [FL], it("12.1", 1), "Why does a compass needle get deflected when brought near a bar magnet?", "easy",
    answer_steps=["A compass needle is itself a small magnet.", "Near a bar magnet it experiences a force in the magnet's magnetic field, so it turns (attraction of unlike poles, repulsion of like poles)."], marking_scheme=MS2P)
C.q("it2.q1", "very_short_answer", 2, [FL], it("12.2", 1), "Draw magnetic field lines around a bar magnet.", "easy",
    answer_steps=["Draw closed curves that leave the north pole and enter the south pole outside the magnet, with arrows from N to S.", "Draw the lines crowded near the poles and spread out away from them; no two lines cross."], marking_scheme=["1 mark: shape", "1 mark: arrows"])
C.q("it2.q2", "short_answer", 3, [FL], it("12.2", 2), "List the properties of magnetic field lines.", "easy",
    answer_steps=["Outside a magnet they go from the north pole to the south pole; inside, from south to north: they are closed curves.", "They are crowded where the field is strong and spread out where it is weak.",
                  "No two field lines intersect."], marking_scheme=MS3)
C.q("it2.q3", "very_short_answer", 2, [FL], it("12.2", 3), "Why don't two magnetic field lines intersect each other?",
    answer_steps=["At the point of intersection a compass needle would have to point in two directions at once.", "This is impossible, because the field has only one direction at any point."], marking_scheme=MS2P)
C.q("it3.q1", "short_answer", 3, [FC], it("12.2.3", 1), "Consider a circular loop of wire lying in the plane of the table. Let the current pass through the loop clockwise. Apply the right-hand rule to find out the direction of the magnetic field inside and outside the loop.", "medium",
    answer_steps=["Hold each part of the loop in the right hand with the thumb along the clockwise current.", "Inside the loop, the curled fingers point downward: the field is into the table.",
                  "Outside the loop, the field points upward: out of the table."], marking_scheme=["1 mark: rule", "1 mark: inside", "1 mark: outside"])
C.q("it3.q2", "very_short_answer", 2, [FL], it("12.2.3", 2), "The magnetic field in a given region is uniform. Draw a diagram to represent it.", "easy",
    answer_steps=["Draw equally spaced, parallel straight lines.", "Put arrows all pointing the same way, to show the same strength and direction everywhere."], marking_scheme=MS2P)
C.mcq("it4.q1", [FD], "Which of the following property of a proton can change while it moves freely in a magnetic field? (There may be more than one correct answer.)", ["velocity and momentum", "mass", "speed", "mass and speed"], 0,
      "The magnetic force is perpendicular to the motion, so it changes the direction (velocity, momentum) but not the speed or the mass.", "hard", source=it("12.3", 1))
C.q("it4.q2", "short_answer", 3, [FD], it("12.3", 2), "In Activity 12.7, how do we think the displacement of rod AB will be affected if (i) current in rod AB is increased; (ii) a stronger horse-shoe magnet is used; and (iii) length of the rod AB is increased?",
    answer_steps=["(i) The displacement increases, because the force increases with the current.", "(ii) The displacement increases, because the force increases with the strength of the field.",
                  "(iii) The displacement increases, because a longer rod in the field feels a larger force."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.mcq("it4.q3", [FD], "A positively-charged particle (alpha-particle) projected towards west is deflected towards north by a magnetic field. The direction of magnetic field is", ["towards south", "towards east", "downward", "upward"], 3,
      "Fleming's left-hand rule: current (middle finger) west, force (thumb) north, so the field (forefinger) points upward.", "hard", source=it("12.3", 3))
C.q("it5.q1", "very_short_answer", 2, [FD], it("12.4", 1), "Name two safety measures commonly used in electric circuits and appliances.", "easy",
    answer_steps=["An electric fuse (or a miniature circuit breaker) in series with the live wire.", "Earthing: an earth wire connecting the metal body of an appliance to the ground."], marking_scheme=MS2P)
C.q("it5.q2", "very_short_answer", 2, [FD], it("12.4", 2), "An electric oven of 2 kW power rating is operated in a domestic electric circuit (220 V) that has a current rating of 5 A. What result do you expect? Explain.",
    answer_steps=["$I = \\dfrac{P}{V} = \\dfrac{2000}{220} \\approx 9.1$ A", "This is more than the 5 A rating, so the circuit is overloaded and the fuse will blow (melt), cutting off the supply."], marking_scheme=["1 mark: current", "1 mark: result"])
C.q("it5.q3", "very_short_answer", 2, [FD], it("12.4", 3), "What precaution should be taken to avoid the overloading of domestic electric circuits?", "easy",
    answer_steps=["Do not connect too many appliances to a single socket at the same time.", "Use appliances whose current is within the rating of the circuit (heavy appliances on the 15 A circuit), and use a fuse or MCB of the correct rating."], marking_scheme=MS2P)
# Exercises
C.mcq("ex.q1", [FC], "Which of the following correctly describes the magnetic field near a long straight wire?",
      ["The field consists of straight lines perpendicular to the wire.", "The field consists of straight lines parallel to the wire.", "The field consists of radial lines originating from the wire.", "The field consists of concentric circles centred on the wire."], 3,
      "The field lines are concentric circles around the wire.", source=ex(1))
C.mcq("ex.q2", [FD], "At the time of short circuit, the current in the circuit", ["reduces substantially.", "does not change.", "increases heavily.", "vary continuously."], 2, "The resistance becomes nearly zero, so the current becomes very large.", source=ex(2))
C.tf("ex.q3a", [FC], "The field at the centre of a long circular coil carrying current will be parallel straight lines.", True,
     "Near the centre of a current-carrying circular coil, the field lines are straight and parallel.", source=ex("3(a)"))
C.tf("ex.q3b", [FD], "A wire with a green insulation is usually the live wire of an electric supply.", False,
     "The green wire is the earth wire; the live wire has red insulation.", source=ex("3(b)"))
C.q("ex.q4", "very_short_answer", 2, [FC], ex(4), "List two methods of producing magnetic fields.", "easy",
    answer_steps=["Using a permanent magnet, such as a bar magnet.", "Passing an electric current through a conductor: a straight wire, a circular loop or a solenoid (electromagnet)."], marking_scheme=MS2P)
C.q("ex.q5", "very_short_answer", 2, [FD], ex(5), "When is the force experienced by a current–carrying conductor placed in a magnetic field largest?", "easy",
    answer_steps=["When the direction of the current is perpendicular to the magnetic field.", "(It is zero when the current is parallel to the field.)"], marking_scheme=["1 mark: answer", "1 mark: contrast"])
C.q("ex.q6", "very_short_answer", 2, [FD], ex(6), "Imagine that you are sitting in a chamber with your back to one wall. An electron beam, moving horizontally from back wall towards the front wall, is deflected by a strong magnetic field to your right side. What is the direction of magnetic field?", "hard",
    answer_steps=["The electrons move towards the front wall, so the current is towards the back wall; the force is to the right.", "By Fleming's left-hand rule, the magnetic field is vertically downward."], marking_scheme=["1 mark: current direction", "1 mark: answer"])
C.q("ex.q7", "short_answer", 3, [FC, FD], ex(7), "State the rule to determine the direction of a (i) magnetic field produced around a straight conductor-carrying current, (ii) force experienced by a current-carrying straight conductor placed in a magnetic field which is perpendicular to it, and (iii) current induced in a coil due to its rotation in a magnetic field.",
    answer_steps=["(i) Right-hand thumb rule: hold the conductor in the right hand with the thumb along the current; the curled fingers give the direction of the field.",
                  "(ii) Fleming's left-hand rule: stretch the thumb, forefinger and middle finger of the left hand at right angles; forefinger = field, middle finger = current, thumb = force.",
                  "(iii) Fleming's right-hand rule: with the right hand, forefinger = field, thumb = motion of the conductor, middle finger = induced current."], marking_scheme=["1 mark: (i)", "1 mark: (ii)", "1 mark: (iii)"])
C.q("ex.q8", "very_short_answer", 2, [FD], ex(8), "When does an electric short circuit occur?", "easy",
    answer_steps=["When the live wire and the neutral wire come in direct contact, for example when the insulation is damaged or an appliance is faulty.", "The resistance becomes nearly zero, and the current increases heavily."], marking_scheme=MS2P)
C.q("ex.q9", "very_short_answer", 2, [FD], ex(9), "What is the function of an earth wire? Why is it necessary to earth metallic appliances?",
    answer_steps=["The earth wire provides a low-resistance path from the metal body of an appliance to the ground.", "If the live wire touches the metal body, the leaking current flows to the earth, so the user does not get a severe electric shock."], marking_scheme=MS2P)
# CBSE sample paper
C.q("sqp37", "short_answer", 3, [FL], SQP(37), "Magnetic field lines around a bar magnet are shown in a diagram: point X is close to a pole, where the lines are crowded, and point Y is farther away, where the lines are spread out. A student makes a statement that the magnetic field at X is stronger than at Y.\n\n(i) Explain with reason if the student's claim is correct.\n\n(ii) Also redraw the diagram and mark the direction of magnetic field lines.", "medium",
    answer_steps=["(i) The claim is correct: the closeness of the field lines shows the strength of the field.", "The lines are more crowded at X (near the pole) than at Y, so the field at X is stronger.",
                  "(ii) Arrows on the field lines should go from the north pole to the south pole outside the magnet."], marking_scheme=MS3)
# GSEB
C.q("gseb2024_33", "very_short_answer", 2, [FL], gseb(2024, "33"), "Write down the characteristics of field lines around a bar magnet.", "easy",
    answer_steps=["They go from the north pole to the south pole outside the magnet and form closed curves.", "They are crowded near the poles where the field is strong, and no two lines intersect."], marking_scheme=MS2P)
C.q("gseb2024_37", "very_short_answer", 2, [FC], gseb(2024, "37"), "Explain the right-hand thumb rule.", "easy",
    answer_steps=["Imagine holding a current-carrying straight conductor in your right hand, with the thumb pointing in the direction of the current.", "Then the fingers wrapped around the conductor give the direction of the magnetic field lines."], marking_scheme=MS2P)
C.q("gseb2024_53", "short_answer", 3, [FD], gseb(2024, "53", 4), "(a) Draw a schematic diagram of domestic electric circuit.\n\n(b) What is the importance of fuse and earth wire in domestic electric circuit?",
    answer_steps=["(a) Mains (live, neutral, earth) → meter → main fuse → distribution box → separate circuits (15 A and 5 A), with appliances connected in parallel, each with its own switch; the earth wire goes to every metal body.",
                  "(b) Fuse: it melts and breaks the circuit when the current becomes too large (short circuit or overloading), preventing damage to appliances and fire.",
                  "Earth wire: it carries any leaking current from the metal body of an appliance to the ground, protecting the user from a severe shock."], marking_scheme=["1 mark: diagram", "1 mark: fuse", "1 mark: earth wire"])
C.q("gseb2025_33", "very_short_answer", 2, [FC], gseb(2025, "33"), "Explain: Solenoid", "easy",
    answer_steps=["A solenoid is a coil of many circular turns of insulated copper wire wrapped closely in the shape of a cylinder.", "When current flows, its field is like that of a bar magnet, and the field inside is uniform; with a soft iron core it becomes an electromagnet."], marking_scheme=MS2P)
C.q("gseb2025_37", "very_short_answer", 2, [FD], gseb(2025, "37"), "Explain Fleming's left-hand rule.", "easy",
    answer_steps=["Stretch the thumb, forefinger and middle finger of the left hand so that they are mutually perpendicular.", "If the forefinger points along the magnetic field and the middle finger along the current, the thumb gives the direction of the force (motion) on the conductor."], marking_scheme=MS2P)
C.q("gseb2025_53", "short_answer", 3, [FL, FD], gseb(2025, "53", 4), "(a) List the properties of magnetic field lines.\n\n(b) When does an electric short circuit occur?",
    answer_steps=["(a) They go from the north pole to the south pole outside a magnet and form closed curves; they are crowded where the field is strong.", "No two field lines intersect.",
                  "(b) When the live wire and the neutral wire come in direct contact; the resistance becomes nearly zero and the current increases heavily."], marking_scheme=["1 mark: (a)", "1 mark: (a)", "1 mark: (b)"])
# Shine MCQs
C.mcq("mcq01", [FL], "Outside a bar magnet, magnetic field lines go from:", ["north pole to south pole", "south pole to north pole", "the middle to the ends", "nowhere; they are absent outside"], 0, "Outside, from N to S; inside, from S to N.")
C.mcq("mcq02", [FL], "The magnetic field is strongest where the field lines are:", ["closest together", "farthest apart", "curved the most", "straight"], 0, "Crowded lines mean a strong field.")
C.mcq("mcq03", [FC], "The field around a straight wire becomes stronger when:", ["the current is increased", "the wire is made longer", "the current is reduced", "you move away from the wire"], 0, "The field increases with current and decreases with distance.")
C.mcq("mcq04", [FC], "A soft iron core inside a solenoid makes it:", ["a strong electromagnet", "a permanent magnet always", "non-magnetic", "a resistor"], 0, "The iron core greatly strengthens the field while the current flows.")
C.mcq("mcq05", [FD], "In Fleming's left-hand rule, the thumb shows the direction of:", ["force (motion)", "current", "magnetic field", "voltage"], 0, "Forefinger = field, middle finger = current, thumb = force.")
C.mcq("mcq06", [FD], "The frequency of AC supply in India is:", ["50 Hz", "60 Hz", "220 Hz", "100 Hz"], 0, "Indian mains supply is 220 V, 50 Hz.")
C.mcq("mcq07", [FD], "The live wire in a domestic circuit usually has insulation of colour:", ["red", "green", "black", "blue"], 0, "Live is red, neutral is black, earth is green.")
C.mcq("mcq08", [FD], "Heavy appliances such as a geyser are connected to a circuit of rating:", ["15 A", "5 A", "1 A", "50 A"], 0, "Heavy appliances use the 15 A circuit; bulbs and fans use the 5 A circuit.", "medium")
C.mcq("mcq09", [FD], "An advantage of AC over DC is that AC:", ["can be transmitted over long distances without much energy loss", "flows in one direction only", "can be stored in a cell", "has no frequency"], 0, "AC can be sent over long distances with little loss.", "medium")
C.mcq("mcq10", [FD], "A beam of electrons moving towards the east is equivalent to a current towards the:", ["west", "east", "north", "south"], 0, "Current is opposite to the motion of electrons.", "medium")
# Assertion-reason
C.ar("ar1", [FL], "Two magnetic field lines never intersect.", "At any point the magnetic field has only one direction.", 0, "Crossing would need two directions at one point: R explains A.")
C.ar("ar2", [FD], "A fuse is connected in series with the live wire.", "A fuse melts and breaks the circuit when the current becomes too large.", 0, "Being in series, its melting cuts off the whole supply: R explains A.")
C.ar("ar3", [FD], "The metal body of an electric iron is earthed.", "The earth wire carries current all the time the iron is in use.", 2, "A is true. R is false: the earth wire carries current only when there is a leakage.")
C.ar("ar4", [FC], "The magnetic field inside a long solenoid is uniform.", "Inside a solenoid the field lines are parallel straight lines.", 0, "Parallel, equally spaced lines mean a uniform field: R explains A.")
C.ar("ar5", [FD], "The force on a current-carrying conductor is zero when it is parallel to the magnetic field.", "The force is largest when the conductor is perpendicular to the field.", 1,
     "Both are true, but the maximum at 90° does not explain why the force is zero at 0°.")
# Written Shine
C.q("vsa1", "very_short_answer", 2, [FD], SHINE, "Differentiate between direct current and alternating current.", "easy",
    answer_steps=["Direct current (DC) flows in one direction only, for example from a cell.", "Alternating current (AC) reverses its direction periodically; in India it has a frequency of 50 Hz."], marking_scheme=MS2P)
C.q("vsa2", "very_short_answer", 2, [FD], SHINE, "What is overloading? Give two causes.", "easy",
    answer_steps=["Overloading is when the current drawn in a circuit becomes more than its rated value.", "Causes: too many appliances connected to a single socket; an accidental rise in the supply voltage."], marking_scheme=MS2P)
C.q("sa1", "short_answer", 3, [FC], SHINE, "Describe the magnetic field produced by a current-carrying solenoid. How can it be used to make an electromagnet?",
    answer_steps=["A current-carrying solenoid produces a field like that of a bar magnet: one end behaves as a north pole and the other as a south pole.", "Inside, the field lines are parallel straight lines, so the field is uniform.",
                  "Placing a soft iron core inside and passing current makes a strong electromagnet, whose magnetism disappears when the current is switched off."], marking_scheme=MS3)
C.q("sa2", "short_answer", 3, [FD], SHINE, "On what factors does the force on a current-carrying conductor in a magnetic field depend? How can its direction be reversed?",
    answer_steps=["The force increases with the current, the strength of the magnetic field and the length of the conductor in the field.", "It also depends on the angle: it is largest when the conductor is perpendicular to the field.",
                  "Its direction is reversed by reversing either the current or the magnetic field."], marking_scheme=MS3)
C.q("la1", "long_answer", 5, [FC], SHINE, "Describe the magnetic field produced by (a) a straight current-carrying wire (b) a circular loop. State the rule used to find its direction, and the factors on which the field of a straight wire depends.", "medium",
    answer_steps=["(a) Straight wire: the field lines are concentric circles centred on the wire, in a plane perpendicular to it.", "(b) Circular loop: near the centre the field lines are nearly straight and parallel; the field of n turns is n times that of one turn.",
                  "Rule: the right-hand thumb rule, with the thumb along the current and the curled fingers showing the field.", "The field of a straight wire increases with the current.", "It decreases as the distance from the wire increases."],
    marking_scheme=["1 mark: (a)", "1 mark: (b)", "1 mark: rule", "1 mark: current", "1 mark: distance"])
C.q("la2", "long_answer", 5, [FD], SHINE, "Describe a domestic electric circuit. Explain the functions of the live wire, neutral wire, earth wire and fuse. What is a short circuit?", "medium",
    answer_steps=["Mains supply at 220 V, 50 Hz enters through the meter and the main fuse; appliances are connected in parallel on 15 A and 5 A circuits, each with its own switch.",
                  "Live wire (red) brings the current at 220 V; neutral wire (black) returns it.", "Earth wire (green) connects metal bodies to the ground and carries leaking current away, preventing shocks.",
                  "Fuse: in series with the live wire, it melts when the current is too large and breaks the circuit.", "Short circuit: live and neutral touch directly, the resistance becomes nearly zero, and the current rises heavily."],
    marking_scheme=["1 mark: circuit", "1 mark: live and neutral", "1 mark: earth", "1 mark: fuse", "1 mark: short circuit"])
C.q("cb1", "case_based", 4, [FD], SHINE,
    "During Diwali, Aman plugged a heater, an iron and several decorative lights into one multi-plug socket. After some time, the fuse blew and the house went dark. An electrician advised using the 15 A circuit for the heater and the iron.\n\n"
    "(i) What is this situation called? (1)\n\n(ii) Why did the fuse blow? (1)\n\n(iii) Why are heavy appliances connected to the 15 A circuit? OR Why is the fuse connected in the live wire and not in the neutral wire? (2)",
    answer_steps=["(i) Overloading.", "(ii) The total current drawn became more than the fuse's rating, so the fuse wire heated up and melted.",
                  "(iii) Heavy appliances draw a large current; the 15 A circuit has thicker wires and a higher-rated fuse that can carry it safely. OR If the fuse melts in the live wire, the appliance is completely cut off from the high-voltage supply, so it is safe to touch."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])
C.q("cb2", "case_based", 4, [FC], SHINE,
    "In a scrap yard, a crane lifts old cars with a huge electromagnet. When the operator switches off the current, the car drops. Nearby, a compass placed under the crane's cable turned when the current was on.\n\n"
    "(i) What does the electromagnet consist of? (1)\n\n(ii) Why does the car drop when the current is switched off? (1)\n\n(iii) Why did the compass turn? OR Give two ways to make the electromagnet stronger. (2)",
    answer_steps=["(i) A solenoid (coil of insulated wire) with a soft iron core.", "(ii) The soft iron core loses its magnetism when the current stops.",
                  "(iii) The current in the cable produces a magnetic field around it, which exerts a force on the compass needle. OR Increase the current; increase the number of turns of the coil."],
    marking_scheme=["(i) 1 mark", "(ii) 1 mark", "(iii) 1 mark method, 1 mark answer"])

C.write(ROOT, PATH, chapter, keep=lambda item: item["id"].startswith("sci10ch12.q.ex.") or item["id"].startswith("sci10ch12.q.it4."))
