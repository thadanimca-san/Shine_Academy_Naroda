import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../simulators/transformers_sandbox.dart';

/// Transformers — stepping AC voltage up or down via mutual induction.
final Lesson transformersLesson = Lesson(
  topicId: 'transformers',
  title: 'Transformers',
  bigQuestion:
      'Electricity leaves a power plant at hundreds of kilovolts, then arrives at your wall socket at a gentle 220 V — with no moving parts and no battery in between. What device can change a voltage that dramatically, using nothing but two coils of wire wrapped around an iron ring?',
  whyItMatters:
      'The transformer is the reason a nationwide electric grid is even possible. Without it, transmitting power over long distances would waste most of the energy as heat in the wires. The turns-ratio formula Vs/Vp = Ns/Np is simple, but the reasoning behind WHY high-voltage transmission saves energy (via I²R losses) is a classic high-yield conceptual thread connecting this topic to the heating-effect-of-current chapter.',
  prediction: const PredictionPrompt(
    scenario:
        'A transformer has 100 turns on its primary coil and 500 turns on its secondary. If you feed 20 V AC into the primary, the secondary voltage is:',
    options: [
      '20 V (voltage never changes across a transformer)',
      '4 V (fewer effective turns means lower voltage)',
      '100 V (5 times as many turns gives 5 times the voltage)',
      '500 V (equal to the number of secondary turns)',
    ],
    correctIndex: 2,
    reveal:
        'Vs/Vp = Ns/Np = 500/100 = 5, so Vs = 5×20 = 100 V. In the lab, drag the turns-ratio slider to 5 with Vp = 20 V and watch the secondary-voltage meter read exactly 100 V. Notice the secondary current drops by the same factor of 5 — power in equals power out for an ideal transformer.',
  ),
  experiments: [
    'Set the turns ratio above 1 (step-up) and watch Vs grow larger than Vp while Is shrinks below Ip',
    'Set the turns ratio below 1 (step-down) and watch the opposite: Vs shrinks, Is grows',
    'Increase primary current Ip and confirm the power readout VpIp stays equal to VsIs (ideal transformer)',
    'Set the turns ratio to exactly 1 — secondary voltage and current match the primary exactly (an "isolation transformer")',
    'Notice the coil turn-count drawing in the scene visually thickens on whichever side has more turns',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A transformer consists of two coils — primary and secondary — wound on a common soft-iron core. An alternating current in the primary coil creates a continuously changing magnetic flux; since the iron core channels nearly all of this flux through the secondary coil as well, that changing flux induces an EMF in the secondary purely by mutual induction — with no direct electrical connection between the two coils.',
      title: 'Working principle: mutual induction',
    ),
    ContentBlock.paragraph(
      'Because the same changing flux threads every turn of both coils, each turn (on either side) has the same induced EMF per turn. A coil with more turns simply adds up more of these equal contributions, so the total EMF is proportional to the number of turns.',
      title: 'Why voltage scales with turns',
    ),
    ContentBlock.formula('V_s/V_p = N_s/N_p', title: 'IDEAL TRANSFORMER: TURNS-RATIO RELATION'),
    ContentBlock.paragraph(
      'For an IDEAL transformer (no losses), the power delivered to the secondary circuit equals the power drawn from the primary — energy is neither created nor destroyed, only voltage and current are traded off against each other.',
      title: 'Power conservation fixes the current relation',
    ),
    ContentBlock.formula('V_p·I_p = V_s·I_s   ⟹   I_s/I_p = N_p/N_s', title: 'CURRENT RELATION (ideal, lossless)'),
    ContentBlock.bullets([
      'STEP-UP transformer: Ns > Np, so Vs > Vp, but Is < Ip — more voltage, less current',
      'STEP-DOWN transformer: Ns < Np, so Vs < Vp, but Is > Ip — less voltage, more current',
      'A transformer changes voltage and current, but NEVER changes the frequency of the AC supply',
    ]),
    ContentBlock.paragraph(
      'Long-distance power lines carry current over tens or hundreds of kilometres of wire, and every wire has some resistance R, so power is lost as heat at a rate I²R. For a FIXED amount of power P = VI to be delivered, choosing a HIGHER transmission voltage means a proportionally LOWER current — and since the loss depends on the SQUARE of current, even a modest increase in voltage causes a dramatic drop in I²R line losses. This is exactly why power is transmitted at very high voltage (and correspondingly low current) using step-up transformers at the generating station, then stepped back down for safe household use.',
      title: 'Why power transmission uses high voltage',
    ),
    ContentBlock.formula('P_loss = I²R  ⟹  raise V (step-up), current I falls, I²R losses fall sharply',
        title: 'THE STEP-UP TRANSMISSION ARGUMENT'),
    ContentBlock.realLife(
      'The pole-mounted transformer outside your house is a step-down transformer converting the grid\'s high transmission voltage down to safe household voltage. Mobile phone chargers contain a small transformer (or its switched-mode equivalent) to bring mains voltage down to a few volts DC-equivalent for the battery. Power-station step-up transformers routinely push voltages to 100 kV–765 kV for cross-country transmission.',
    ),
    ContentBlock.mistake(
      'Trying to run a transformer on DC. A transformer needs a CONTINUOUSLY CHANGING flux to induce any secondary EMF at all. A steady DC current creates a constant flux (once fully established) with dΦ/dt = 0, so a transformer connected to DC induces nothing in steady state — it only works with AC, whose flux is always changing.',
    ),
    ContentBlock.mistake(
      'Assuming a real transformer is perfectly lossless. Real transformers lose some energy as heat: copper loss (I²R heating in the resistance of the actual windings) and iron/hysteresis loss (energy dissipated repeatedly magnetising and demagnetising the core material each AC cycle, plus eddy currents in the core itself — reduced by laminating the core). Well-designed transformers are still highly efficient (often >95%), but never perfectly ideal.',
    ),
    ContentBlock.example(
      'A step-down transformer has 2000 primary turns and 100 secondary turns. If the primary is connected to 220 V AC and draws 2 A, find the secondary voltage and current (assume ideal).\n\nVs = Vp × (Ns/Np) = 220 × (100/2000) = 220 × 0.05 = 11 V.\n\nIs = Ip × (Np/Ns) = 2 × (2000/100) = 2 × 20 = 40 A.\n\nCheck power: Pp = 220×2 = 440 W;  Ps = 11×40 = 440 W. Power matches — the ideal assumption holds.',
    ),
    ContentBlock.jeeTip(
      'A transformer never changes power in the ideal case and never changes frequency, ever (real or ideal) — only voltage and current trade off. If a question mentions the secondary frequency being different from the primary, something else (like a rectifier or oscillator) must be involved, not a plain transformer.',
    ),
    ContentBlock.jeeTip(
      'Efficiency η = P_output/P_input × 100% for a real transformer, where the difference (P_input − P_output) is the sum of copper loss and iron loss. JEE sometimes gives efficiency and asks you to back-calculate the output power or secondary current — always start from η = Ps/Pp.',
    ),
    ContentBlock.neetNote(
      'NEET commonly asks to identify step-up vs step-down purely from the turns ratio, and to state the "why AC only" fact directly: a transformer works only on alternating current because it depends entirely on a continuously changing magnetic flux (mutual induction), which a steady direct current cannot provide.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'EMF induced per turn is the same on both sides',
      math: 'ε_per turn = -dΦ/dt   (same Φ threads every turn, both coils)',
      note: 'The iron core ensures nearly all flux from the primary links the secondary.',
    ),
    DerivationStep(
      title: 'Total EMF scales with number of turns',
      math: 'V_p = N_p (dΦ/dt),   V_s = N_s (dΦ/dt)',
    ),
    DerivationStep(
      title: 'Divide to eliminate the common flux rate',
      math: 'V_s/V_p = N_s/N_p',
      note: 'The turns-ratio relation — independent of the actual value of dΦ/dt.',
    ),
    DerivationStep(
      title: 'Apply conservation of energy (ideal transformer)',
      math: 'P_p = P_s  ⟹  V_p I_p = V_s I_s',
    ),
    DerivationStep(
      title: 'Combine to get the current relation',
      math: 'I_s/I_p = V_p/V_s = N_p/N_s',
      note: 'Voltage and current always trade off inversely with the turns ratio for an ideal transformer.',
    ),
  ],
  formulas: const [
    FormulaEntry('Turns-ratio relation', 'V_s/V_p = N_s/N_p'),
    FormulaEntry('Current relation (ideal)', 'I_s/I_p = N_p/N_s'),
    FormulaEntry('Power conservation (ideal)', 'V_p I_p = V_s I_s'),
    FormulaEntry('Transformer efficiency', 'η = P_s/P_p × 100%'),
    FormulaEntry('Line loss', 'P_loss = I²R', condition: 'reduced by transmitting at high V, low I'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A transformer works on the principle of:',
      options: ['Self-induction only', 'Mutual induction', 'Electrostatic induction', 'Thermionic emission'],
      correctIndex: 1,
      solution: 'A changing flux in the primary coil induces an EMF in the secondary coil via mutual induction — the two coils share a common iron core but have no direct electrical connection.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A transformer cannot be used with:',
      options: ['High-frequency AC', 'Low-frequency AC', 'Steady DC', 'Any AC voltage'],
      correctIndex: 2,
      solution: 'A transformer requires a continuously changing flux, which only AC provides. Steady DC produces constant flux once established, inducing no secondary EMF.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A transformer has 500 turns on the primary and 2500 turns on the secondary. If the primary voltage is 40 V, the secondary voltage is:',
      options: ['8 V', '40 V', '200 V', '400 V'],
      correctIndex: 2,
      solution: 'Vs = Vp(Ns/Np) = 40×(2500/500) = 40×5 = 200 V.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An ideal step-up transformer has a turns ratio Ns:Np = 10:1. If the primary current is 5 A, the secondary current is:',
      options: ['50 A', '5 A', '0.5 A', '2.5 A'],
      correctIndex: 2,
      solution: 'Is = Ip(Np/Ns) = 5×(1/10) = 0.5 A. Stepping voltage UP means stepping current DOWN by the same factor.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Power is transmitted over long distances at high voltage mainly to:',
      options: [
        'Increase the total power generated',
        'Reduce I²R losses in the transmission lines by lowering the current',
        'Make transformers cheaper to build',
        'Increase the frequency of the AC supply',
      ],
      correctIndex: 1,
      solution: 'For a fixed power P = VI, raising V lowers I proportionally. Since resistive loss depends on I² (not I), a modest voltage increase causes a much larger drop in I²R losses in the line.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The energy loss in a transformer due to repeated magnetisation and demagnetisation of the core each cycle is called:',
      options: ['Copper loss', 'Hysteresis (iron) loss', 'Flux leakage', 'Dielectric loss'],
      correctIndex: 1,
      solution: 'Hysteresis loss is the energy dissipated as heat while the core material is repeatedly magnetised and demagnetised each AC cycle — distinct from copper loss (I²R heating in the windings).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A transformer steps down 11 kV to 220 V for a load drawing 100 A on the secondary. Assuming an ideal transformer, the primary current is:',
      options: ['5000 A', '20 A', '2 A', '0.05 A'],
      correctIndex: 2,
      solution: 'VpIp = VsIs ⟹ Ip = VsIs/Vp = (220×100)/11000 = 22000/11000 = 2 A.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A transformer with primary power input of 2200 W delivers 2000 W to the secondary. Its efficiency, and the nature of the 200 W difference, are:',
      options: [
        '90.9% efficient; the 200 W is stored permanently in the core',
        '90.9% efficient; the 200 W is lost as copper and iron losses (heat)',
        '100% efficient; the 200 W is a measurement error',
        '9.1% efficient; the 200 W is the useful output',
      ],
      correctIndex: 1,
      solution: 'η = Ps/Pp × 100 = 2000/2200 × 100 ≈ 90.9%. The missing 200 W is dissipated as heat via copper loss (winding resistance) and iron/hysteresis + eddy-current loss in the core — it is not stored or recoverable.',
    ),
  ],
  revision: [
    'Transformer principle: mutual induction between primary and secondary coils sharing an iron core.',
    'Turns-ratio relation: Vs/Vp = Ns/Np; ideal current relation: Is/Ip = Np/Ns.',
    'Step-up: Ns>Np, Vs>Vp, Is<Ip. Step-down: Ns<Np, Vs<Vp, Is>Ip.',
    'Ideal power conservation: VpIp = VsIs — a transformer never changes frequency, ever.',
    'Works ONLY on AC — steady DC gives zero dΦ/dt, hence no induced secondary EMF.',
    'High-voltage transmission minimises I²R line losses (P=VI fixed, lower I sharply cuts I²R loss).',
    'Real losses: copper loss (winding resistance) and iron/hysteresis loss (core), both reduced by good design and lamination.',
  ],
  sandboxBuilder: (_) => const TransformersSandbox(),
  accentColor: const Color(0xFF6D28D9),
);
