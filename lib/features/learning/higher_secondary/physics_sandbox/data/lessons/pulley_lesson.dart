import '../../models/lesson.dart';
import '../../simulators/pulley_sim.dart';
import '../../theme/tokens.dart';

/// Pulley Systems — the Atwood machine, tension, and constraint relations.
final Lesson pulleyLesson = Lesson(
  topicId: 'pulleys',
  title: 'Pulley Systems',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Two unequal weights hang from a rope over a pulley. The heavier one obviously wins and falls — but does it fall at full free-fall acceleration g, or does the lighter weight on the other side somehow "hold it back"? And is the string tension the same on both sides, even though the weights are different?',
  whyItMatters:
      'The Atwood machine is the classic gateway problem to multi-body dynamics — it teaches you that tension is an unknown to be SOLVED FOR (not assumed), and that a shared string forces two bodies to share exactly one acceleration (a constraint relation). Every JEE/NEET pulley, connected-block, or pulley-on-incline problem is a variation on the same two-equation trick you learn here.',
  prediction: const PredictionPrompt(
    scenario:
        'A 3 kg mass and a 1 kg mass hang from opposite ends of a string over a frictionless, massless pulley. The system is released from rest. Compared to free fall (g), the 3 kg mass falls:',
    options: [
      'At exactly g, same as free fall',
      'Faster than g, since it is heavier',
      'Slower than g, because the string tension partly holds it back',
      'It does not move at all, since the pulley balances it',
    ],
    correctIndex: 2,
    reveal:
        'The Atwood machine gives a = (m1 − m2)g/(m1 + m2) = (3−1)×g/(3+1) = g/2 — HALF of free fall. The lighter mass being pulled up "costs" the heavier mass some of its acceleration, transmitted through string tension. In the lab, set the two masses, release the system, and compare the measured acceleration to g — watch it match (m1−m2)g/(m1+m2) exactly, and watch the tension reading sit between m1g and m2g, never equal to either weight alone.',
  ),
  experiments: [
    'Set m1 = 3 kg, m2 = 1 kg, release, and confirm a = (m1−m2)g/(m1+m2) = g/2',
    'Set m1 = m2 — confirm the system stays in equilibrium (a = 0) and tension equals each weight',
    'Make the mass difference huge (e.g. m1 = 10, m2 = 1) and watch a approach g — the light mass barely matters',
    'Read the tension value and confirm it is ALWAYS between m2g and m1g, never equal to either',
    'Add friction at the pulley axle (if available) and observe how it reduces the acceleration below the ideal formula',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A pulley is a simple machine that changes the direction of a tension force without changing its magnitude — PROVIDED the pulley is treated as ideal: massless and frictionless. This assumption means the pulley itself needs no net force or torque to move it, so whatever tension enters the string on one side leaves unchanged on the other side.',
      title: 'The ideal pulley',
    ),
    ContentBlock.bullets([
      'Tension is the same throughout an ideal (massless, inextensible) string',
      'A massless, frictionless pulley only redirects the string — it never changes the tension magnitude',
      'The string is INEXTENSIBLE: it cannot stretch, so connected masses share a single common acceleration',
      'This shared acceleration (from the string constraint) is what lets you write one equation for the whole system',
    ]),
    ContentBlock.paragraph(
      'The Atwood machine — two masses m1 and m2 connected by a string over a single fixed pulley — is the simplest and most important pulley problem. Because the string is inextensible, when m1 moves down by some distance, m2 moves up by exactly the same distance, at exactly the same speed and acceleration. This one fact (the "constraint relation") is what makes the two-body problem solvable with simple algebra.',
      title: 'The Atwood machine',
    ),
    ContentBlock.formula('a = (m1 − m2)g / (m1 + m2)', title: 'ATWOOD MACHINE — ACCELERATION'),
    ContentBlock.formula('T = 2m1m2g / (m1 + m2)', title: 'ATWOOD MACHINE — TENSION'),
    ContentBlock.paragraph(
      'Notice tension T always lies strictly between the two weights: m2g < T < m1g (for m1 > m2). This makes physical sense — the heavier mass is partially "held back" by a tension less than its own weight (so it accelerates down), while the lighter mass is pulled up by a tension greater than its own weight (so it accelerates up). Neither weight alone equals the tension.',
      title: 'Why tension sits between the two weights',
    ),
    ContentBlock.realLife(
      'Elevators and construction cranes both use counterweight systems that are large-scale Atwood machines. A counterweight roughly matching the cabin\'s mass means the motor only has to supply a small NET force (proportional to m1 − m2), rather than lifting the full cabin weight from scratch — this is why elevator motors can be much smaller than the total weight they move would suggest.',
    ),
    ContentBlock.mistake(
      'Assuming the tension equals the weight of one of the hanging masses (T = m1g or T = m2g). This is only true if the system is in equilibrium (m1 = m2, a = 0). Whenever the masses are unequal and the system accelerates, tension is a genuinely new unknown that must be solved for using both masses\' equations — never just assumed.',
    ),
    ContentBlock.mistake(
      'Forgetting the string constraint when masses are connected over MULTIPLE pulleys, or one mass is on a table while the other hangs. Always write the constraint relation first (how the displacements/accelerations of the two masses relate through the fixed string length) before writing Newton\'s second law — guessing the relation is a common source of sign and factor errors.',
    ),
    ContentBlock.example(
      'Masses m1 = 5 kg and m2 = 3 kg hang from a string over an ideal pulley (g = 10 m/s²). Find the acceleration and tension.\n\na = (m1−m2)g/(m1+m2) = (5−3)×10/(5+3) = 20/8 = 2.5 m/s².\n\nT = 2m1m2g/(m1+m2) = 2×5×3×10/8 = 300/8 = 37.5 N.\n\nCheck: m2g = 30 N < T = 37.5 N < m1g = 50 N. Tension correctly lies between the two weights.',
    ),
    ContentBlock.jeeTip(
      'For a mass on a frictionless table connected via a pulley at the table\'s edge to a hanging mass, treat the STRING as one rigid constraint: both masses share the same acceleration magnitude a. Write F_net = ma separately for each mass (tension pulls the table mass horizontally, gravity minus tension accelerates the hanging mass vertically), then add the two equations to eliminate T first — solving for a becomes one line: a = m2g/(m1+m2) when m1 is on the table and m2 hangs.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the special (equilibrium) case: if m1 = m2 in an Atwood machine, a = 0 and T = m1g = m2g — the system just balances. Also remember that for an IDEAL pulley, the pulley\'s own mass and friction are both ignored; a "pulley with mass" (a common JEE extension) requires torque and moment of inertia, which is beyond the ideal case covered here.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the two masses with the string constraint',
      math: 'm1 > m2, connected over an ideal pulley. |a1| = |a2| = a (same string, same magnitude)',
      note: 'm1 accelerates downward, m2 accelerates upward, both with magnitude a.',
    ),
    DerivationStep(
      title: 'Write Newton\'s second law for m1 (taking downward as positive for m1)',
      math: 'm1g − T = m1a',
      note: 'Gravity pulls m1 down; tension resists, pulling it up.',
    ),
    DerivationStep(
      title: 'Write Newton\'s second law for m2 (taking upward as positive for m2)',
      math: 'T − m2g = m2a',
      note: 'Tension pulls m2 up; gravity resists, pulling it down. Same tension T (ideal string/pulley).',
    ),
    DerivationStep(
      title: 'Add the two equations to eliminate T',
      math: '(m1g − T) + (T − m2g) = m1a + m2a  ⟹  (m1 − m2)g = (m1 + m2)a',
      note: 'Tension cancels exactly because it appears with opposite signs in the two equations.',
    ),
    DerivationStep(
      title: 'Solve for a, then back-substitute to find T',
      math: 'a = (m1 − m2)g/(m1 + m2)\nT = m1(g − a) = 2m1m2g/(m1 + m2)',
      note: 'Substituting a into either original equation and simplifying gives the tension formula.',
    ),
  ],
  formulas: const [
    FormulaEntry('Atwood machine acceleration', 'a = (m1 − m2)g / (m1 + m2)'),
    FormulaEntry('Atwood machine tension', 'T = 2m1m2g / (m1 + m2)'),
    FormulaEntry('Equilibrium special case', 'a = 0, T = m1g = m2g', condition: 'when m1 = m2'),
    FormulaEntry('One mass on table, one hanging', 'a = m2g / (m1 + m2)', condition: 'm1 on frictionless table, m2 hangs'),
    FormulaEntry('Tension bound', 'm2g < T < m1g', condition: 'for m1 > m2, accelerating system'),
    FormulaEntry('String constraint', '|a1| = |a2|', condition: 'single ideal inextensible string over one pulley'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In an ideal (massless, frictionless) pulley system, the tension in the string is:',
      options: [
        'Different on each side of the pulley',
        'The same throughout the string',
        'Equal to the average of the two weights',
        'Zero if the masses are unequal',
      ],
      correctIndex: 1,
      solution: 'An ideal massless, frictionless pulley only redirects the string; tension is the same throughout.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two equal masses m hang from an ideal pulley on either side. The system:',
      options: ['Accelerates at g', 'Accelerates at g/2', 'Remains in equilibrium', 'Accelerates at 2g'],
      correctIndex: 2,
      solution: 'With m1 = m2, a = (m1−m2)g/(m1+m2) = 0 — the system is balanced.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In an Atwood machine with m1 = 4 kg and m2 = 2 kg (g = 10 m/s²), the acceleration of the system is:',
      options: ['10/3 m/s²', '5 m/s²', '2 m/s²', '10 m/s²'],
      correctIndex: 0,
      solution: 'a = (4−2)×10/(4+2) = 20/6 = 10/3 ≈ 3.33 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'For the same Atwood machine (m1 = 4 kg, m2 = 2 kg, g = 10 m/s²), the tension in the string is:',
      options: ['20 N', '26.7 N', '30 N', '40 N'],
      correctIndex: 1,
      solution: 'T = 2m1m2g/(m1+m2) = 2×4×2×10/6 = 160/6 ≈ 26.7 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In an accelerating Atwood machine with m1 > m2, the string tension T satisfies:',
      options: ['T = m1g', 'T = m2g', 'm2g < T < m1g', 'T > m1g'],
      correctIndex: 2,
      solution: 'Tension must be less than the heavier weight (to allow it to accelerate down) but more than the lighter weight (to accelerate it up), so it lies strictly between the two: m2g < T < m1g.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A 2 kg block on a frictionless table is connected via a string over a pulley at the table\'s edge to a hanging 3 kg mass (g = 10 m/s²). The acceleration of the system is:',
      options: ['4 m/s²', '5 m/s²', '6 m/s²', '2 m/s²'],
      correctIndex: 2,
      solution: 'a = m2g/(m1+m2) = 3×10/(2+3) = 30/5 = 6 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'In the previous table-and-hanging-mass setup (2 kg on table, 3 kg hanging), the tension in the string is:',
      options: ['12 N', '20 N', '30 N', '18 N'],
      correctIndex: 0,
      solution: 'For the table mass: T = m1·a = 2×6 = 12 N. Check with the hanging mass: m2g − T = m2a → 30 − 12 = 18 = 3×6 ✓.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'As m1 becomes much larger than m2 in an Atwood machine (m1 ≫ m2), the acceleration a approaches:',
      options: ['0', 'g/2', 'g', '2g'],
      correctIndex: 2,
      solution: 'a = (m1−m2)g/(m1+m2). As m1 ≫ m2, both m1−m2 and m1+m2 approach m1, so a → g — the heavy mass essentially free-falls, barely slowed by the negligible m2.',
    ),
  ],
  revision: [
    'An ideal pulley (massless, frictionless) only redirects tension — it never changes its magnitude.',
    'An inextensible string forces connected masses to share the same acceleration magnitude (the constraint relation).',
    'Atwood machine: a = (m1−m2)g/(m1+m2), T = 2m1m2g/(m1+m2).',
    'Tension always lies strictly between the two weights: m2g < T < m1g (for m1 > m2) — never assume T equals either weight.',
    'Equal masses on an ideal pulley give a = 0 and T = mg — pure equilibrium.',
    'For one mass on a frictionless table connected to a hanging mass: a = m2g/(m1+m2).',
    'Always write the string constraint and both masses\' equations before eliminating T — never guess the tension directly.',
  ],
  sandboxBuilder: (_) => const PulleyDynamicsSimulator(),
);
