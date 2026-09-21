import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/ohms_law_drift_sandbox.dart';

/// Ohm's Law & Drift Velocity — how a "sea" of jittering electrons becomes
/// a steady, useful current.
final Lesson ohmsLawDriftLesson = Lesson(
  topicId: 'ohms-law-drift',
  title: 'Ohm\'s Law & Drift Velocity',
  bigQuestion:
      'Flip a switch and a lamp across the room lights up almost instantly. Yet the electrons actually doing the work inside the wire creep along slower than a snail. How can the "signal" be so fast if the charge carriers themselves are so slow?',
  whyItMatters:
      'Ohm\'s law, V = IR, is the single most-used equation in circuits — but underneath it is a beautiful microscopic story about billions of electrons colliding with atoms while a tiny electric field nudges them forward. Understanding drift velocity resolves one of the most common misconceptions in all of physics, and R = ρL/A connects the everyday idea of "resistance" to the geometry and material of a wire, setting up everything from household wiring to resistors in circuits.',
  prediction: const PredictionPrompt(
    scenario:
        'A copper wire carries a steady current of a few amperes. Roughly how fast do the individual conduction electrons actually drift along the wire, on average?',
    options: [
      'Close to the speed of light (3×10⁸ m/s)',
      'A few metres per second, like a slow walk',
      'A few millimetres per second — slower than a snail',
      'Exactly zero — only the field moves, not the electrons',
    ],
    correctIndex: 2,
    reveal:
        'Drift velocity is astonishingly small — typically under a millimetre per second for household currents. In the lab, watch the electron dots: their jittery zig-zag thermal motion (hundreds of km/s in reality) is dramatic, but their slow net creep to the right is what the drift-velocity meter reports. The "signal" that seems instant is actually the electric field establishing itself through the wire at nearly light speed — a completely different thing from the electrons\' own sluggish drift.',
  ),
  experiments: [
    'Raise the voltage slider and watch both current I and the electrons\' net drift speed increase',
    'Raise resistivity (simulating heating the wire) and see R climb while I = V/R falls',
    'Shrink the cross-section A and watch drift velocity rise for the same current (v_d = I/nAe)',
    'Lengthen the wire L and see resistance rise proportionally, current fall',
    'Compare the huge random jitter of each electron dot to its tiny net rightward creep — that creep IS the current',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Georg Ohm found that for many conductors (called ohmic conductors), the current through them is directly proportional to the voltage applied across them, provided physical conditions like temperature stay constant. The constant of proportionality is the resistance R, measured in ohms (Ω).',
      title: 'Ohm\'s law',
    ),
    ContentBlock.formula('V = IR   (Ohm\'s law, for ohmic conductors at constant temperature)',
        title: 'OHM\'S LAW'),
    ContentBlock.paragraph(
      'Metals like copper are ohmic over a wide range — a graph of V against I is a straight line through the origin, its slope giving R. Devices like diodes and filament bulbs (where R changes noticeably with current/temperature) are NON-ohmic, and V vs I becomes a curve.',
      title: 'Ohmic vs non-ohmic',
    ),
    ContentBlock.paragraph(
      'A wire full of free electrons, with no field applied, has electrons zipping around randomly at very high thermal speeds (hundreds of km/s), colliding constantly with the vibrating metal ions. On average, a resting wire has zero NET electron motion in any direction — the random directions cancel. Switch on a battery, and a tiny additional electric field pushes every electron with a small extra velocity in one direction, superimposed on their chaotic thermal motion. This extra, average velocity is the drift velocity v_d — and it is what current actually is, at the microscopic level.',
      title: 'The microscopic picture',
    ),
    ContentBlock.paragraph(
      'To connect drift velocity to current: consider a wire of cross-sectional area A with n free electrons per unit volume, each of charge e, all drifting at speed v_d. In a time interval t, every electron within a distance v_d·t of a cross-section will cross it. The volume swept is A·v_d·t, containing n·A·v_d·t electrons, carrying total charge n·A·v_d·t·e. Current is charge per unit time.',
      title: 'Deriving I = nAev_d',
    ),
    ContentBlock.formula('I = nAev_d   (microscopic current)', title: 'CURRENT FROM DRIFT VELOCITY'),
    ContentBlock.bullets([
      'n = free-electron number density (huge for metals, ~10²⁸–10²⁹ per m³)',
      'A = cross-sectional area of the conductor',
      'e = charge of an electron = 1.6×10⁻¹⁹ C',
      'v_d = drift velocity — typically a fraction of a millimetre per second for ordinary currents',
    ]),
    ContentBlock.realLife(
      'When you flip a light switch, the bulb glows almost instantly not because electrons race across the wire from the switch to the bulb, but because the electric field is established throughout the circuit at a speed close to that of light — every electron everywhere in the wire begins drifting at nearly the same moment, even though each one individually creeps forward incredibly slowly. It is like a already-full pipe of marbles: push one marble in at one end, and one pops out the other end almost instantly, even though no single marble travelled the whole pipe.',
    ),
    ContentBlock.mistake(
      'The single most common misconception in this topic: believing that because current "travels" through a circuit almost instantly, the electrons themselves must be moving at similarly high speed. In reality the ELECTRIC FIELD (and hence the "signal" or information that current should start flowing) propagates at a speed close to light, while the electrons\' drift velocity remains agonisingly slow (mm/s). Two completely different speeds are involved — never confuse signal speed with drift speed.',
    ),
    ContentBlock.example(
      'A copper wire of cross-sectional area 1×10⁻⁶ m² carries a current of 1.6 A. Given free-electron density n = 8.5×10²⁸ /m³, find the drift velocity.\n\nv_d = I/(nAe) = 1.6 / (8.5×10²⁸ × 1×10⁻⁶ × 1.6×10⁻¹⁹)\n= 1.6 / (1.36×10⁴)\n≈ 1.18×10⁻⁴ m/s\n= 0.118 mm/s.\n\nEven a substantial current like 1.6 A corresponds to a drift velocity under 0.15 millimetres per second.',
    ),
    ContentBlock.jeeTip(
      'Resistivity ρ (an intrinsic material property, unlike resistance R which also depends on geometry) increases with temperature for METALS — more thermal vibration of the lattice means more frequent electron collisions, reducing the time between collisions and hence the drift velocity for a given field. For SEMICONDUCTORS, resistivity DECREASES with temperature instead, because more thermally-generated charge carriers become available (see the Semiconductor Diodes lesson) — this opposite behaviour is a favourite exam contrast.',
    ),
    ContentBlock.jeeTip(
      'R = ρL/A: resistance is directly proportional to length (longer wire, more collisions along the way) and inversely proportional to cross-sectional area (wider wire, more parallel "lanes" for current to flow). If a wire is stretched to twice its length with volume conserved, its area halves, so R increases by a factor of 4 (both effects compound) — a classic numerical trap.',
    ),
    ContentBlock.neetNote(
      'NEET tests the drift-velocity paradox directly and often asks for the relationship between drift velocity and current-carrying capacity: v_d ∝ I/A, so thinner wires need HIGHER drift velocities to carry the same current, which generates more heat (see Heating Effect lesson) — one reason very thin wires are unsuitable for carrying large currents.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Picture a wire of cross-section A, n carriers per unit volume',
      math: 'Each carrier has charge e and drifts at average velocity v_d.',
    ),
    DerivationStep(
      title: 'Find how many electrons cross a section in time t',
      math: 'Volume swept in time t = A · v_d · t\nNumber of electrons in that volume = n · A · v_d · t',
    ),
    DerivationStep(
      title: 'Convert to charge, then to current',
      math: 'Charge crossing = n·A·v_d·t·e\nI = charge/time = nAev_d',
    ),
    DerivationStep(
      title: 'Relate resistance to geometry: R = ρL/A',
      math: 'Longer wire (bigger L) → more collisions → larger R\nWider wire (bigger A) → more parallel paths → smaller R',
      note: 'ρ (resistivity) is the material\'s intrinsic property; R also depends on shape.',
    ),
    DerivationStep(
      title: 'Combine with Ohm\'s law',
      math: 'V = IR = I·ρL/A  →  current density J = I/A = V/(ρL) = σE',
      note: 'σ = 1/ρ is conductivity; this form connects the macroscopic Ohm\'s law to the microscopic field E and current density J.',
    ),
  ],
  formulas: const [
    FormulaEntry('Ohm\'s law', 'V = IR'),
    FormulaEntry('Microscopic current', 'I = nAev_d'),
    FormulaEntry('Drift velocity', 'v_d = I/(nAe)'),
    FormulaEntry('Resistance from geometry', 'R = ρL/A'),
    FormulaEntry('Conductivity', 'σ = 1/ρ'),
    FormulaEntry('Current density', 'J = I/A = σE'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A conductor obeys Ohm\'s law if a graph of V against I is:',
      options: ['A curve through the origin', 'A straight line through the origin', 'A straight line not through the origin', 'A horizontal line'],
      correctIndex: 1,
      solution: 'Ohm\'s law states V ∝ I at constant temperature, so V vs I is a straight line through the origin, with slope equal to the resistance R.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The drift velocity of electrons in a typical current-carrying copper wire is of the order of:',
      options: ['3×10⁸ m/s', '10² m/s', '10⁻⁴ m/s', '10⁻⁹ m/s'],
      correctIndex: 2,
      solution: 'Drift velocity for ordinary household currents is typically of order 10⁻⁴ m/s (a fraction of a mm/s) — far slower than the speed of light, which is instead the speed at which the electric field/signal propagates.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A wire of resistance R is stretched uniformly to twice its original length, keeping its volume constant. Its new resistance is:',
      options: ['R', '2R', '4R', 'R/2'],
      correctIndex: 2,
      solution: 'Volume constant: A₁L₁ = A₂L₂. With L₂ = 2L₁, A₂ = A₁/2. New R = ρL₂/A₂ = ρ(2L₁)/(A₁/2) = 4ρL₁/A₁ = 4R.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A copper wire carries current I with drift velocity v_d. If the same current flows through a wire of the same material but HALF the cross-sectional area, the new drift velocity is:',
      options: ['v_d/2', 'v_d', '2v_d', '4v_d'],
      correctIndex: 2,
      solution: 'v_d = I/(nAe). For the same I, n, and e, halving A doubles v_d. Thinner wires need faster-drifting carriers to sustain the same current.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'As the temperature of a metallic conductor increases, its resistivity:',
      options: ['Increases', 'Decreases', 'Remains constant', 'First increases then decreases'],
      correctIndex: 0,
      solution: 'In metals, higher temperature increases lattice vibrations, causing more frequent electron collisions and reducing the average time between collisions — resistivity increases. (Semiconductors show the opposite trend.)',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A conductor has resistivity ρ = 1.7×10⁻⁸ Ω·m, length 2 m and cross-sectional area 1×10⁻⁶ m². Its resistance is:',
      options: ['0.034 Ω', '0.34 Ω', '3.4 Ω', '34 Ω'],
      correctIndex: 0,
      solution: 'R = ρL/A = (1.7×10⁻⁸ × 2) / (1×10⁻⁶) = 3.4×10⁻⁸/10⁻⁶ = 3.4×10⁻² = 0.034 Ω.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Why does a light bulb appear to switch on almost instantly even though the drift velocity of electrons is only about 0.1 mm/s?',
      options: [
        'The electrons near the bulb were already there before the switch was flipped',
        'The electric field that drives the electrons propagates through the circuit at a speed close to that of light, so all electrons everywhere begin drifting almost simultaneously',
        'Electrons actually travel at the speed of light despite the low calculated drift velocity',
        'The bulb does not actually turn on instantly; it only appears so due to human reaction time',
      ],
      correctIndex: 1,
      solution: 'The propagation speed of the electromagnetic field/signal through the circuit is close to the speed of light, so every electron in the wire (including those already inside the bulb\'s filament) starts drifting almost simultaneously. The bulb glows immediately because the ALREADY-PRESENT electrons near the filament instantly begin drifting there — no electron needs to travel from the switch to the bulb.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The number of free electrons crossing a cross-section of a conductor per second is directly related to:',
      options: ['Voltage only', 'The current flowing through it', 'The resistivity only', 'The length of the conductor only'],
      correctIndex: 1,
      solution: 'Current I is defined as the rate of flow of charge, I = nAev_d — directly the count of charge carriers crossing a section per second, multiplied by their charge.',
    ),
  ],
  revision: [
    'Ohm\'s law: V = IR, valid for ohmic conductors at constant temperature (straight line V–I graph through origin).',
    'Microscopically, I = nAev_d — current is carried by the slow net drift of electrons, not their fast thermal jitter.',
    'Drift velocity is astonishingly slow (~10⁻⁴ m/s); the "signal" travels near light speed because the FIELD propagates that fast, not the electrons.',
    'R = ρL/A: resistance grows with length, shrinks with cross-sectional area.',
    'Resistivity increases with temperature for metals (more collisions); decreases for semiconductors (more carriers thermally generated).',
    'Stretching a wire (constant volume) to double length quadruples its resistance — both L↑ and A↓ compound.',
  ],
  sandboxBuilder: (_) => const OhmsLawDriftSandbox(),
  accentColor: Palette.chElectroMag,
);
