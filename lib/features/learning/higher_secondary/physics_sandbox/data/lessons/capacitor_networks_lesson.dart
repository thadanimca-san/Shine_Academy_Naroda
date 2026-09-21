import '../../models/lesson.dart';
import '../../simulators/capacitor_networks_sandbox.dart';
import '../../theme/tokens.dart';

/// Series & Parallel Capacitors — combination rules, the mirror image of resistors.
final Lesson capacitorNetworksLesson = Lesson(
  topicId: 'capacitor-networks',
  title: 'Series & Parallel Capacitors',
  accentColor: Palette.chElectroMag,
  bigQuestion:
      'Put two identical resistors in series and resistance goes UP. Put two identical capacitors in series and capacitance goes DOWN. Both circuits look the same — components chained end to end — so why do they respond in exactly opposite ways?',
  whyItMatters:
      'Capacitor networks are the single most common numerical topic in the capacitance chapter of NEET and JEE, and the series/parallel rules are notoriously easy to mix up with resistor rules because they are exact opposites. Understanding WHY they\'re opposite — grounded in charge and voltage behaviour, not memorised formulas — makes this topic bulletproof for exams.',
  prediction: const PredictionPrompt(
    scenario:
        'Two identical capacitors, each of capacitance C, are connected in SERIES. What is the combined (equivalent) capacitance?',
    options: [
      '2C — capacitances simply add, just like resistors in series',
      'C — combining them changes nothing',
      'C/2 — series combination always reduces capacitance',
      '4C — series combination multiplies capacitance',
    ],
    correctIndex: 2,
    reveal:
        'For capacitors in series, 1/C_eq = 1/C + 1/C = 2/C, so C_eq = C/2 — series REDUCES capacitance (opposite of resistors, where series increases resistance). In the lab, wire two equal capacitors in series and watch the equivalent capacitance readout drop to half of a single capacitor\'s value, then switch to parallel and watch it double instead.',
  ),
  experiments: [
    'Wire two identical capacitors in series and observe C_eq drop to C/2',
    'Wire the same two capacitors in parallel and observe C_eq rise to 2C',
    'In series, verify each capacitor holds the SAME charge Q, but different voltage',
    'In parallel, verify each capacitor holds the SAME voltage V, but different charge',
    'Combine capacitors of different values and confirm the series/parallel formulas numerically',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A capacitor stores charge Q proportional to the voltage V across it, following Q = CV, where C is its capacitance. When capacitors are wired together, whether the SAME charge or the SAME voltage is shared between them determines whether we\'re dealing with a series or parallel combination — and this determines exactly opposite combination rules from resistors.',
      title: 'Capacitance and the two ways to combine',
    ),
    ContentBlock.formula('1/C_eq = 1/C₁ + 1/C₂ + …', title: 'SERIES COMBINATION'),
    ContentBlock.paragraph(
      'In series, capacitors are connected end-to-end in a single chain, so the SAME charge Q flows onto every capacitor in the chain (charge has nowhere else to go — it\'s the same current path). But each capacitor, having a different capacitance, develops a DIFFERENT voltage V = Q/C across it. The total voltage across the whole series chain is the SUM of the individual voltages: V_total = V₁ + V₂ + …, which is exactly what produces the reciprocal-sum rule for capacitance.',
      title: 'Series: same charge, different voltage',
    ),
    ContentBlock.formula('C_eq = C₁ + C₂ + …', title: 'PARALLEL COMBINATION'),
    ContentBlock.paragraph(
      'In parallel, capacitors are connected across the SAME two nodes, so they all share the SAME voltage V (both plates of every capacitor sit at the same two potentials). But each capacitor stores a DIFFERENT charge Q = CV depending on its own capacitance. The total charge stored is the SUM of individual charges: Q_total = Q₁ + Q₂ + …, which directly gives the simple-sum rule for capacitance.',
      title: 'Parallel: same voltage, different charge',
    ),
    ContentBlock.bullets([
      'Series capacitors: same Q, split V → capacitance DECREASES (like resistors in PARALLEL)',
      'Parallel capacitors: same V, split Q → capacitance INCREASES (like resistors in SERIES)',
      'Capacitor combination rules are the exact MIRROR IMAGE of resistor combination rules',
    ]),
    ContentBlock.formula('U = ½CV² = ½QV = Q²/(2C)', title: 'ENERGY STORED IN A CAPACITOR'),
    ContentBlock.paragraph(
      'The energy stored differs between series and parallel configurations of the same capacitors, because both C_eq AND how charge/voltage distribute change. For a FIXED total charge (as often happens after disconnecting from a battery), series storage (smaller C, same Q) stores MORE energy than parallel (since U = Q²/2C and smaller C means larger U for fixed Q) — this is a subtle but frequently tested distinction.',
      title: 'Energy depends on the configuration',
    ),
    ContentBlock.realLife(
      'Camera flash circuits use large capacitors in parallel to store more total charge (and hence more energy) for a bigger, brighter flash; high-voltage capacitor banks sometimes use series combinations specifically because splitting voltage across multiple capacitors lets each one survive with a lower individual voltage rating, protecting them from breakdown.',
    ),
    ContentBlock.mistake(
      'Applying resistor combination rules to capacitors, or vice versa. Resistors: series ADDS (R_eq=R₁+R₂), parallel does reciprocal-sum. Capacitors: series does reciprocal-sum, parallel ADDS (C_eq=C₁+C₂). This is the single most common error in this topic — always pause and ask "is this a capacitor or a resistor?" before applying a combination rule.',
    ),
    ContentBlock.mistake(
      'Assuming charge is the same on all capacitors in a PARALLEL combination, or that voltage is the same on all capacitors in a SERIES combination. It is exactly the opposite: series shares charge, parallel shares voltage. Mixing this up leads to using the wrong Q = CV computation for individual capacitors.',
    ),
    ContentBlock.example(
      'Two capacitors, C₁ = 2 µF and C₂ = 3 µF, are connected in series across a 10 V battery. Find the equivalent capacitance, the charge on each, and the voltage across each.\n\n1/C_eq = 1/2 + 1/3 = 3/6 + 2/6 = 5/6 → C_eq = 6/5 = 1.2 µF.\nCharge (same on both, series): Q = C_eq × V = 1.2 × 10 = 12 µC.\nV₁ = Q/C₁ = 12/2 = 6 V.   V₂ = Q/C₂ = 12/3 = 4 V.\nCheck: V₁ + V₂ = 6 + 4 = 10 V ✓ matches the battery voltage.',
    ),
    ContentBlock.jeeTip(
      'For two capacitors in series, use the shortcut C_eq = (C₁C₂)/(C₁+C₂) (the "product over sum" rule, exactly like two resistors in parallel) instead of manually inverting fractions — much faster for two-capacitor problems. For more than two, the reciprocal-sum formula is still needed.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests: "N identical capacitors of capacitance C, all in series, give C_eq = C/N; the same N capacitors all in parallel give C_eq = NC." Also remember the voltage DIVISION in series capacitors is INVERSELY proportional to capacitance (smaller capacitor gets MORE voltage) — the opposite of resistors, where the larger resistor gets more voltage in series.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Series: state the shared quantity',
      math: 'Same charge Q on every capacitor in the chain',
      note: 'Charge conservation along a single current path with no branching.',
    ),
    DerivationStep(
      title: 'Series: express each voltage and sum them',
      math: 'V₁ = Q/C₁,  V₂ = Q/C₂,  …   V_total = V₁+V₂+… = Q(1/C₁ + 1/C₂ + …)',
    ),
    DerivationStep(
      title: 'Series: define C_eq via V_total = Q/C_eq',
      math: 'Q/C_eq = Q(1/C₁+1/C₂+…)  →  1/C_eq = 1/C₁ + 1/C₂ + …',
      note: 'Reciprocal-sum rule — combination is always SMALLER than the smallest individual C.',
    ),
    DerivationStep(
      title: 'Parallel: state the shared quantity',
      math: 'Same voltage V across every capacitor (same two nodes)',
    ),
    DerivationStep(
      title: 'Parallel: express each charge and sum them',
      math: 'Q₁ = C₁V,  Q₂ = C₂V,  …   Q_total = Q₁+Q₂+… = V(C₁+C₂+…)',
    ),
    DerivationStep(
      title: 'Parallel: define C_eq via Q_total = C_eq·V',
      math: 'C_eq·V = V(C₁+C₂+…)  →  C_eq = C₁ + C₂ + …',
      note: 'Simple-sum rule — combination is always LARGER than the largest individual C.',
    ),
  ],
  formulas: const [
    FormulaEntry('Charge on a capacitor', 'Q = CV'),
    FormulaEntry('Series combination', '1/C_eq = 1/C₁ + 1/C₂ + …'),
    FormulaEntry('Series (two capacitors)', 'C_eq = C₁C₂/(C₁+C₂)'),
    FormulaEntry('Parallel combination', 'C_eq = C₁ + C₂ + …'),
    FormulaEntry('Energy stored', 'U = ½CV² = ½QV = Q²/(2C)'),
    FormulaEntry('N identical capacitors, series', 'C_eq = C/N'),
    FormulaEntry('N identical capacitors, parallel', 'C_eq = NC'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two identical capacitors of capacitance C are connected in parallel. The equivalent capacitance is:',
      options: ['C/2', 'C', '2C', '4C'],
      correctIndex: 2,
      solution: 'Parallel: C_eq = C₁+C₂ = C+C = 2C.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In a series combination of capacitors, which quantity is the SAME across all of them?',
      options: ['Voltage', 'Charge', 'Energy', 'Capacitance'],
      correctIndex: 1,
      solution: 'Series capacitors share the same charge Q, since they lie along a single unbranched path.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two capacitors of 4 µF and 6 µF are connected in series. The equivalent capacitance is:',
      options: ['10 µF', '2.4 µF', '5 µF', '24 µF'],
      correctIndex: 1,
      solution: 'C_eq = (4×6)/(4+6) = 24/10 = 2.4 µF.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'For capacitors connected in parallel, which quantity is the SAME across all of them?',
      options: ['Charge', 'Voltage', 'Neither', 'Capacitance'],
      correctIndex: 1,
      solution: 'Parallel capacitors share the same nodes, hence the same voltage V across each.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Three identical capacitors of capacitance C are all connected in series. The equivalent capacitance is:',
      options: ['3C', 'C', 'C/3', 'C/9'],
      correctIndex: 2,
      solution: 'For N identical capacitors in series, C_eq = C/N = C/3.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A 2 µF and a 3 µF capacitor are connected in series across a 10 V battery. The voltage across the 2 µF capacitor is:',
      options: ['4 V', '6 V', '10 V', '2 V'],
      correctIndex: 1,
      solution:
          'C_eq = (2×3)/5 = 1.2 µF. Q = C_eq×V = 12 µC (same on both). V(2µF) = Q/C = 12/2 = 6 V.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two capacitors, 3 µF and 6 µF, are first connected in series and then in parallel across the same battery of voltage V. The ratio of energy stored (series : parallel) is:',
      options: ['1:9', '1:3', '2:9', '1:4.5'],
      correctIndex: 2,
      solution:
          'Series C_eq = (3×6)/9 = 2 µF; U_series = ½(2)V². Parallel C_eq = 9 µF; U_parallel = ½(9)V². Ratio = 2:9.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A capacitor network has C₁ = 2 µF and C₂ = 2 µF in series, and this combination is in parallel with a third capacitor C₃ = 3 µF. The total equivalent capacitance is:',
      options: ['4 µF', '5 µF', '1 µF', '7 µF'],
      correctIndex: 0,
      solution:
          'C₁ and C₂ in series: C_eq = (2×2)/4 = 1 µF. This is in parallel with C₃=3 µF: total = 1+3 = 4 µF.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'In a series combination of two UNEQUAL capacitors, the smaller capacitor:',
      options: [
        'Has less voltage across it',
        'Has more voltage across it',
        'Has the same voltage as the larger one',
        'Has zero voltage',
      ],
      correctIndex: 1,
      solution: 'Same charge Q on both (series); V = Q/C means smaller C gives LARGER V — voltage divides inversely with capacitance in series.',
    ),
  ],
  revision: [
    'Q = CV relates charge, capacitance, and voltage for every capacitor.',
    'Series: 1/C_eq = 1/C₁+1/C₂+… — same charge, split voltage; C_eq is always smaller than the smallest C.',
    'Parallel: C_eq = C₁+C₂+… — same voltage, split charge; C_eq is always larger than the largest C.',
    'Capacitor rules are the MIRROR IMAGE of resistor rules — series capacitors behave like parallel resistors.',
    'In series, the SMALLER capacitor gets MORE voltage (opposite to resistors, where larger R gets more V).',
    'Energy stored: U = ½CV² = Q²/(2C) — configuration (series vs parallel) changes both C_eq and how U distributes.',
    'N identical capacitors: series gives C/N, parallel gives NC.',
  ],
  sandboxBuilder: (_) => const CapacitorNetworksSandbox(),
);
