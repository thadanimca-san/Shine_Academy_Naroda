import '../../models/lesson.dart';
import '../../simulators/heat_engines_sim.dart';
import '../../theme/tokens.dart';

/// Heat Engines — efficiency, the Carnot limit, and why 100% efficiency is impossible.
final Lesson heatEnginesLesson = Lesson(
  topicId: 'heat-engines',
  title: 'Heat Engines',
  accentColor: Palette.chThermal,
  bigQuestion:
      'Car engines waste roughly two-thirds of the fuel\'s energy as heat, and no engineer has ever built one that doesn\'t. Is this just a matter of needing better materials and cleverer design — or is there a fundamental LAW of physics that makes a 100% efficient heat engine flatly impossible, no matter how good the technology gets?',
  whyItMatters:
      'Heat engines power nearly all of civilization — car engines, power plants, jet turbines — and the Carnot efficiency limit is one of the deepest results in all of physics, setting a hard ceiling that no engine can ever cross. NEET and JEE test both the practical efficiency formula and the conceptual weight of the second law, which is a favourite for assertion-reasoning and conceptual multiple-choice questions.',
  prediction: const PredictionPrompt(
    scenario:
        'An engineer claims to have built a heat engine that absorbs heat from a single hot reservoir and converts 100% of it into useful work, with no heat rejected anywhere. Is this possible?',
    options: [
      'Yes, with sufficiently advanced technology',
      'Yes, but only using exotic materials not yet discovered',
      'No — the second law of thermodynamics forbids any cyclic engine from being 100% efficient',
      'Yes, but only for very small engines',
    ],
    correctIndex: 2,
    reveal:
        'The second law of thermodynamics states that no cyclic heat engine can convert heat completely into work without rejecting SOME heat to a colder reservoir — this is a fundamental law, not an engineering limitation. In the lab, try pushing the cold-reservoir temperature down toward the hot-reservoir temperature and watch the efficiency formula η = 1 − Tc/Th approach but never reach 100%, and note it hits exactly 100% only in the impossible limit Tc = 0.',
  ),
  experiments: [
    'Increase the hot reservoir temperature Th and watch Carnot efficiency rise',
    'Decrease the cold reservoir temperature Tc and watch efficiency rise further',
    'Try to set Tc = Th and observe efficiency drop to zero — no temperature difference, no work possible',
    'Compare a real engine\'s efficiency reading against the theoretical Carnot maximum for the same Th, Tc',
    'Trace the engine cycle on a P-V or T-S style diagram and see heat absorbed vs heat rejected',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A heat engine is any device that operates in a repeating CYCLE, absorbing heat Qh from a hot reservoir, converting part of it into useful work W, and rejecting the remaining heat Qc to a cold reservoir. Because the engine returns to its starting state every cycle, its internal energy change over a full cycle is zero, so by the first law, the work output must exactly equal the net heat absorbed: W = Qh − Qc.',
      title: 'What a heat engine does',
    ),
    ContentBlock.formula('η = W/Qh = 1 − Qc/Qh', title: 'EFFICIENCY OF A HEAT ENGINE'),
    ContentBlock.paragraph(
      'Efficiency η measures what fraction of the absorbed heat becomes useful work, rather than being wasted as rejected heat. Since Qc is never zero for any real cyclic engine, η is always strictly less than 1 (100%). The larger the fraction of heat that must be rejected, the lower the efficiency.',
      title: 'Efficiency as a fraction of energy converted',
    ),
    ContentBlock.formula('η_Carnot = 1 − Tc/Th', title: 'CARNOT EFFICIENCY — THE THEORETICAL MAXIMUM'),
    ContentBlock.paragraph(
      'The Carnot engine is an idealized, perfectly reversible heat engine operating between two fixed temperatures Th (hot) and Tc (cold, both in Kelvin). Sadi Carnot proved that NO engine operating between the same two temperatures can be more efficient than this ideal — it represents the absolute theoretical ceiling. Real engines, with friction, turbulence, and other irreversibilities, always fall short of the Carnot limit.',
      title: 'The Carnot limit',
    ),
    ContentBlock.bullets([
      'η_Carnot depends ONLY on the two reservoir temperatures — not on the working substance, size, or design',
      'Higher Th or lower Tc both increase the theoretical maximum efficiency',
      'η_Carnot = 100% only if Tc = 0 K (absolute zero) — physically unreachable',
      'Real engines are always less efficient than the Carnot limit for the same Th, Tc',
    ]),
    ContentBlock.paragraph(
      'The second law of thermodynamics (Kelvin-Planck statement) says: it is impossible to construct a cyclic engine that converts heat completely into work with no other effect — some heat MUST always be rejected to a colder reservoir. This is not a statement about imperfect engineering; it is a fundamental limit on what is physically possible, on the same level of certainty as conservation of energy.',
      title: 'Why 100% efficiency is fundamentally impossible',
    ),
    ContentBlock.realLife(
      'Power plants boost efficiency mainly by increasing Th (using higher-temperature steam or combustion) since that is usually easier to engineer than lowering Tc (limited by the environment, typically a river or the atmosphere). Car engines are inherently limited to roughly 25-35% efficiency partly because their combustion (hot side) and exhaust/cooling (cold side) temperatures are much less extreme than a power plant\'s, so their Carnot ceiling itself is lower.',
    ),
    ContentBlock.mistake(
      'Believing efficiency can be improved indefinitely just by better engineering. Even a PERFECT, frictionless, idealized engine (the Carnot engine) still cannot exceed η = 1 − Tc/Th — the limit comes from the second law itself, not from imperfections. Better engineering can only bring a real engine CLOSER to the Carnot limit, never past it.',
    ),
    ContentBlock.mistake(
      'Forgetting to convert reservoir temperatures to Kelvin before computing Carnot efficiency. Since η_Carnot = 1 − Tc/Th is a RATIO of absolute temperatures, using Celsius values directly gives a completely wrong (and often nonsensical) efficiency.',
    ),
    ContentBlock.example(
      'A heat engine operates between a hot reservoir at 600 K and a cold reservoir at 300 K. Find its maximum possible (Carnot) efficiency, and the work output if it absorbs 1000 J of heat at this ideal efficiency.\n\nη_Carnot = 1 − Tc/Th = 1 − 300/600 = 1 − 0.5 = 0.5 = 50%.\nW = η × Qh = 0.5 × 1000 = 500 J (with 500 J rejected to the cold reservoir).',
    ),
    ContentBlock.jeeTip(
      'When a problem gives TWO engines operating between the SAME pair of reservoir temperatures, both share the SAME Carnot efficiency ceiling — regardless of their working substance (steam, air, etc.) or mechanical design. Any efficiency difference between them must come from irreversibilities (friction, non-ideal processes), not from the temperatures themselves.',
    ),
    ContentBlock.neetNote(
      'NEET frequently phrases the second law as: "Whenever heat is converted completely into work in a cyclic process, some other change must also occur in the system or surroundings" — this is the Kelvin-Planck statement in words. Also remember refrigerators/heat pumps are heat engines run in REVERSE, with coefficient of performance (COP) rather than efficiency as the relevant figure of merit.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Apply the first law over one complete cycle',
      math: 'ΔU_cycle = 0  (engine returns to starting state)  →  W = Qh − Qc',
      note: 'Net work output equals net heat absorbed minus heat rejected.',
    ),
    DerivationStep(
      title: 'Define efficiency as useful output over heat input',
      math: 'η = W/Qh',
    ),
    DerivationStep(
      title: 'Substitute W = Qh − Qc',
      math: 'η = (Qh − Qc)/Qh = 1 − Qc/Qh',
    ),
    DerivationStep(
      title: 'For a Carnot (reversible) cycle, heat ratio equals temperature ratio',
      math: 'Qc/Qh = Tc/Th',
      note: 'A key result proved via the reversibility and entropy properties of the Carnot cycle — heat exchanged is proportional to absolute temperature.',
    ),
    DerivationStep(
      title: 'Substitute to get the Carnot efficiency',
      math: 'η_Carnot = 1 − Tc/Th',
      note: 'Depends only on the two reservoir temperatures, setting the absolute maximum for ANY engine operating between them.',
    ),
  ],
  formulas: const [
    FormulaEntry('First law over a cycle', 'W = Qh − Qc'),
    FormulaEntry('Efficiency', 'η = W/Qh = 1 − Qc/Qh'),
    FormulaEntry('Carnot efficiency', 'η_Carnot = 1 − Tc/Th', condition: 'T in Kelvin'),
    FormulaEntry('Carnot heat ratio', 'Qc/Qh = Tc/Th'),
    FormulaEntry('Percentage efficiency', 'η% = η × 100'),
    FormulaEntry('Coefficient of performance (refrigerator)', 'COP = Qc/W = Tc/(Th−Tc)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The efficiency of a heat engine is defined as:',
      options: ['Qc/Qh', 'W/Qh', 'Qh/W', 'Qh − Qc'],
      correctIndex: 1,
      solution: 'Efficiency is useful work output divided by heat input: η = W/Qh.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'According to the second law of thermodynamics, a heat engine can never be:',
      options: ['Less than 50% efficient', '100% efficient', 'More than 0% efficient', 'Reversible'],
      correctIndex: 1,
      solution: 'The second law (Kelvin-Planck statement) forbids any cyclic engine from converting heat completely into work — 100% efficiency is impossible.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A Carnot engine operates between 500 K and 300 K. Its maximum efficiency is:',
      options: ['20%', '40%', '60%', '167%'],
      correctIndex: 1,
      solution: 'η = 1 − Tc/Th = 1 − 300/500 = 1 − 0.6 = 0.4 = 40%.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'To increase the Carnot efficiency of an engine, one should:',
      options: [
        'Increase Tc only',
        'Increase Th and/or decrease Tc',
        'Decrease both Th and Tc equally',
        'Efficiency cannot be changed',
      ],
      correctIndex: 1,
      solution: 'η = 1 − Tc/Th increases when Th increases or Tc decreases (or both), since this raises the ratio\'s complement.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A heat engine absorbs 800 J of heat and does 200 J of useful work per cycle. Its efficiency is:',
      options: ['20%', '25%', '75%', '80%'],
      correctIndex: 1,
      solution: 'η = W/Qh = 200/800 = 0.25 = 25%.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A Carnot engine operating between 600 K and 400 K absorbs 3000 J of heat from the hot reservoir. The work done is:',
      options: ['500 J', '1000 J', '1500 J', '2000 J'],
      correctIndex: 1,
      solution: 'η = 1 − 400/600 = 1/3. W = η×Qh = (1/3)×3000 = 1000 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two Carnot engines operate between the same pair of reservoirs (Th, Tc), one using steam and the other using air as the working substance. Their efficiencies are:',
      options: [
        'Different — steam is inherently more efficient',
        'Different — air is inherently more efficient',
        'Exactly the same — Carnot efficiency depends only on Th and Tc',
        'Cannot be compared without more data',
      ],
      correctIndex: 2,
      solution: 'Carnot efficiency η = 1 − Tc/Th depends ONLY on the reservoir temperatures, never on the working substance.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A Carnot engine has efficiency 25% with the cold reservoir at 300 K. If Th is increased so efficiency becomes 40% (Tc unchanged), the new Th is:',
      options: ['400 K', '500 K', '600 K', '450 K'],
      correctIndex: 1,
      solution:
          'First: 0.25 = 1 − 300/Th → 300/Th = 0.75 → Th = 400 K (consistency check). New: 0.40 = 1 − 300/Th\' → 300/Th\' = 0.6 → Th\' = 500 K.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A refrigerator is essentially a heat engine operating:',
      options: [
        'In the forward direction, extracting work from heat',
        'In reverse, using work input to move heat from cold to hot',
        'Without any heat exchange',
        'At 100% efficiency always',
      ],
      correctIndex: 1,
      solution: 'A refrigerator runs the heat-engine cycle backward: it uses external work to pump heat from a cold interior to a hotter exterior, against the natural direction of heat flow.',
    ),
  ],
  revision: [
    'Heat engine: absorbs Qh, does work W, rejects Qc, with W = Qh − Qc over a full cycle.',
    'Efficiency η = W/Qh = 1 − Qc/Qh — always less than 100% for any real cyclic engine.',
    'Carnot efficiency η = 1 − Tc/Th (Kelvin) is the theoretical maximum for given reservoir temperatures.',
    'Carnot efficiency depends ONLY on Th and Tc — never on the working substance or engine design.',
    'Second law (Kelvin-Planck): no cyclic engine can convert heat completely into work.',
    'Raising Th or lowering Tc both increase the maximum possible efficiency.',
    'A refrigerator is a heat engine run in reverse, using work input to move heat from cold to hot.',
  ],
  sandboxBuilder: (_) => const HeatEnginesSimulator(),
);
