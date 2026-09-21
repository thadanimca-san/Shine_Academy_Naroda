import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/heating_effect_sandbox.dart';

/// Heating Effect of Current — Joule heating, from toasters to transmission lines.
final Lesson heatingEffectLesson = Lesson(
  topicId: 'heating-effect',
  title: 'Heating Effect of Current',
  bigQuestion:
      'Push electricity through a metal coil and it glows white-hot in a toaster, yet the very same current flowing through a thick transmission cable barely warms it at all. What decides how much heat a current actually produces?',
  whyItMatters:
      'Every electric heater, incandescent bulb, fuse, and soldering iron works by deliberately exploiting the heat a current generates in a resistor. But the same effect is a nuisance in power transmission and wiring, where it wastes energy and can start fires. Understanding P = I²R lets you explain both — why heaters are DESIGNED to have this effect, and why power grids go to great lengths to AVOID it.',
  prediction: const PredictionPrompt(
    scenario:
        'A resistor carries a fixed current I. You double the current flowing through it (same resistance R). What happens to the rate of heat generation?',
    options: [
      'It stays the same — heat depends only on resistance',
      'It doubles',
      'It quadruples',
      'It depends on the voltage, not the current',
    ],
    correctIndex: 2,
    reveal:
        'P = I²R means power depends on the SQUARE of the current. In the lab, drag the current slider to double its value and watch the glow shoot from a dull red toward a searing white — power has jumped four-fold, not two-fold. This I² dependence, not a simple I dependence, is the single most important fact in this chapter.',
  ),
  experiments: [
    'Double the current and watch the power meter jump 4× while the element glow shifts from red to white-hot',
    'Keep current fixed and raise resistance — watch power climb linearly (P ∝ R at fixed I)',
    'Set a low current and high resistance vs a high current and low resistance for the SAME power — notice both routes exist',
    'Stretch the time slider and watch total heat Q accumulate even as power stays fixed (Q = Pt)',
    'Compare the heat-in-joules and heat-in-calories readouts — remember 1 cal = 4.186 J',
  ],
  concept: const [
    ContentBlock.paragraph(
      'When current flows through a resistor, moving charge carriers collide constantly with the vibrating lattice ions, transferring kinetic energy to the lattice as heat — this irreversible conversion of electrical energy to heat is called the Joule heating effect (or I²R loss). The rate of heat generation is the electrical power dissipated in the resistor.',
      title: 'Where the heat comes from',
    ),
    ContentBlock.formula('P = I²R = VI = V²/R   (three equivalent forms of Joule\'s law)',
        title: 'JOULE\'S LAW OF HEATING'),
    ContentBlock.bullets([
      'Use P = I²R when current and resistance are known (e.g. a series circuit with fixed current)',
      'Use P = V²/R when voltage and resistance are known (e.g. a component connected across a fixed supply voltage)',
      'Use P = VI when both voltage and current are directly measured, without needing R at all',
      'All three forms are algebraically identical via V = IR — pick whichever uses the quantities you already have',
    ]),
    ContentBlock.paragraph(
      'Total heat generated over a time t is simply the power multiplied by the duration, since power is the RATE of heat production. In SI units heat is measured in joules, but the older unit calorie is still common in numerical problems — 1 calorie is the heat needed to raise 1 gram of water by 1°C, and 1 cal = 4.186 J exactly (a conversion factor worth memorising cold).',
      title: 'Total heat over time',
    ),
    ContentBlock.formula('Q = I²Rt   (heat in joules)', title: 'HEAT GENERATED OVER TIME'),
    ContentBlock.formula('1 cal = 4.186 J', title: 'CALORIE-JOULE CONVERSION'),
    ContentBlock.realLife(
      'Toasters, electric kettles, hair dryers, and incandescent bulb filaments are all deliberately designed with a thin, high-resistance wire (like nichrome) so that I²R heating is large and useful. A fuse works on the same principle in reverse as a safety device: it is a thin wire designed to melt and break the circuit if current exceeds a safe limit, since I²R heating in a thin wire (small A, hence higher R by R = ρL/A) rises fast enough to melt it before the rest of the circuit is damaged.',
    ),
    ContentBlock.mistake(
      'Assuming thicker wires are "better conductors" and therefore heat up MORE. The opposite is true: thin wires have higher resistance (R = ρL/A, smaller A means larger R) and so dissipate MORE heat for the same current, since P = I²R. This is exactly why household wiring uses thick copper cables for high-current circuits, while thin fuse wire is chosen deliberately to overheat and melt first.',
    ),
    ContentBlock.example(
      'A heater has resistance 40 Ω and is connected to a 200 V supply for 5 minutes. Find the power and the total heat generated (in joules and calories).\n\nP = V²/R = 200²/40 = 40000/40 = 1000 W = 1 kW.\n\nQ = Pt = 1000 × (5×60) = 1000 × 300 = 3×10⁵ J.\n\nIn calories: Q = 3×10⁵ / 4.186 ≈ 71670 cal ≈ 71.7 kcal.',
    ),
    ContentBlock.jeeTip(
      'Power transmission over long distances is done at HIGH VOLTAGE and correspondingly LOW CURRENT (via step-up transformers at the power plant), specifically to minimise transmission losses. Since loss = I²R_line, and the SAME power P = VI can be delivered either with high V, low I or low V, high I, choosing high V and low I reduces I² dramatically — a 10× increase in voltage (for the same delivered power) cuts the current to 1/10, and the I²R loss to just 1/100 of what it would otherwise be. This is one of the highest-yield conceptual facts in the entire electricity syllabus.',
    ),
    ContentBlock.jeeTip(
      'When resistors are in SERIES, the same current flows through each — so P = I²R shows the LARGER resistor dissipates MORE power. When resistors are in PARALLEL, the same voltage is across each — so P = V²/R shows the SMALLER resistor dissipates MORE power. Getting this backwards is a very common exam trap.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests fuse-wire reasoning and bulb-brightness comparisons using P = I²R or P = V²/R depending on whether the bulbs are in series (same I) or parallel (same V) with each other. Also expect direct numerical use of Q = I²Rt with a calorie-joule conversion, so 4.186 J/cal is worth memorising precisely.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the definition of electrical power',
      math: 'P = work done per unit time = (charge moved × potential drop) / time = VI',
      note: 'V is the potential difference across the resistor, I is the current through it.',
    ),
    DerivationStep(
      title: 'Substitute Ohm\'s law V = IR',
      math: 'P = VI = (IR)(I) = I²R',
    ),
    DerivationStep(
      title: 'Equivalently substitute I = V/R',
      math: 'P = VI = V(V/R) = V²/R',
      note: 'All three forms — P = I²R = VI = V²/R — are algebraically equivalent.',
    ),
    DerivationStep(
      title: 'Integrate power over time for total heat',
      math: 'Q = ∫P dt = P·t  (for constant P)  =  I²Rt',
    ),
    DerivationStep(
      title: 'Transmission-loss argument',
      math: 'Loss = I²R_line,  with P_delivered = VI fixed\nIncreasing V by factor n → I decreases by factor n → loss decreases by factor n²',
      note: 'This is why grids step up voltage before long-distance transmission and step it back down near consumers.',
    ),
  ],
  formulas: const [
    FormulaEntry('Joule\'s law of heating (three forms)', 'P = I²R = VI = V²/R'),
    FormulaEntry('Total heat over time t', 'Q = I²Rt = Pt'),
    FormulaEntry('Calorie-joule conversion', '1 cal = 4.186 J'),
    FormulaEntry('Transmission loss', 'P_loss = I²R_line'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the current through a fixed resistor is tripled, the power dissipated becomes:',
      options: ['3 times', '6 times', '9 times', 'Unchanged'],
      correctIndex: 2,
      solution: 'P = I²R. Tripling I multiplies I² by 9, so power becomes 9 times larger.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A 100 Ω resistor carries a current of 2 A for 10 seconds. The heat generated is:',
      options: ['400 J', '2000 J', '4000 J', '40000 J'],
      correctIndex: 2,
      solution: 'Q = I²Rt = (2²)(100)(10) = 4×100×10 = 4000 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A bulb rated 100 W, 200 V is connected to its rated voltage. Its resistance is:',
      options: ['200 Ω', '400 Ω', '100 Ω', '2 Ω'],
      correctIndex: 1,
      solution: 'P = V²/R ⟹ R = V²/P = 200²/100 = 40000/100 = 400 Ω.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two resistors, 2 Ω and 4 Ω, are connected in SERIES to a battery. Which resistor dissipates more power?',
      options: ['The 2 Ω resistor', 'The 4 Ω resistor', 'Both dissipate equal power', 'Cannot be determined'],
      correctIndex: 1,
      solution: 'In series, the same current flows through both. P = I²R, so with I fixed, the LARGER resistance (4 Ω) dissipates more power.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two resistors, 2 Ω and 4 Ω, are connected in PARALLEL across a battery. Which resistor dissipates more power?',
      options: ['The 2 Ω resistor', 'The 4 Ω resistor', 'Both dissipate equal power', 'Cannot be determined'],
      correctIndex: 0,
      solution: 'In parallel, the same voltage is across both. P = V²/R, so with V fixed, the SMALLER resistance (2 Ω) dissipates more power.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A heater dissipates 2400 J of heat in 2 minutes. Its power rating is:',
      options: ['20 W', '200 W', '1200 W', '2400 W'],
      correctIndex: 1,
      solution: 'P = Q/t = 2400 / (2×60) = 2400/120 = 20 W. (Note: check units — 2400 J over 120 s gives 20 W.)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Electric power is transmitted at high voltage and low current rather than low voltage and high current mainly because:',
      options: [
        'High voltage is cheaper to generate at the power plant',
        'It minimises I²R power loss in the transmission lines for the same power delivered',
        'High voltage lines require less insulation',
        'Transformers only work efficiently at high voltage',
      ],
      correctIndex: 1,
      solution: 'For the same delivered power P = VI, raising V (and correspondingly lowering I) sharply reduces I²R_line loss, since the loss depends on the SQUARE of the current. A 10× rise in voltage cuts current to 1/10 and loss to 1/100.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A fuse wire is designed to melt and break a circuit because:',
      options: [
        'It has very low resistance and carries huge current safely',
        'It has a small cross-section, giving it high resistance and hence rapid I²R heating that melts it before other components are damaged',
        'It is made of an insulating material',
        'It converts current directly into light',
      ],
      correctIndex: 1,
      solution: 'A fuse wire\'s thin cross-section gives it high resistance (R = ρL/A), so it heats up (P = I²R) faster than the thicker wiring around it when current exceeds a safe limit, melting and breaking the circuit protectively.',
    ),
  ],
  revision: [
    'Joule\'s law: P = I²R = VI = V²/R — three equivalent forms, pick based on known quantities.',
    'Q = I²Rt is total heat in joules; 1 cal = 4.186 J for calorie conversions.',
    'In series (same I), larger R dissipates more power; in parallel (same V), smaller R dissipates more power.',
    'Thin wires have higher resistance and heat up MORE for the same current — the basis of fuse-wire design.',
    'Power transmission uses high voltage, low current specifically to minimise I²R losses (loss ∝ I²).',
    'Real-life uses: heaters, toasters, bulbs (deliberate I²R heating); fuses (protective I²R melting).',
  ],
  sandboxBuilder: (_) => const HeatingEffectSandbox(),
  accentColor: Palette.chElectroMag,
);
