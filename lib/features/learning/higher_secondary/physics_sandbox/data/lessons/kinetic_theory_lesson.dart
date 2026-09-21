import '../../models/lesson.dart';
import '../../simulators/kinetic_theory_sandbox.dart';
import '../../theme/tokens.dart';

/// Kinetic Theory of Gases — pressure and temperature explained by molecular motion.
final Lesson kineticTheoryLesson = Lesson(
  topicId: 'kinetic-theory',
  title: 'Kinetic Theory of Gases',
  accentColor: Palette.chThermal,
  bigQuestion:
      'A thermometer reads a number — "300 K" — but what IS temperature, physically? It isn\'t a substance you can hold, and it isn\'t force or energy in any way you\'ve been taught yet. What is actually happening inside a "hot" gas that a thermometer is detecting?',
  whyItMatters:
      'Kinetic theory is the bridge between the microscopic world (molecules zipping around, colliding) and macroscopic, measurable quantities (pressure, temperature) — it is one of the most conceptually important derivations in the entire syllabus because it explains WHY the ideal gas law works, rather than just stating it. NEET and JEE both test the pressure derivation, the v_rms/v_avg/v_mp ordering, and especially the average-KE-per-molecule result, repeatedly.',
  prediction: const PredictionPrompt(
    scenario:
        'A sealed rigid box of gas is heated so its temperature quadruples (say, from 300 K to 1200 K), with no molecules added or removed. The rms speed of the molecules:',
    options: [
      'Also becomes 4 times as large',
      'Becomes 2 times as large (v_rms ∝ √T)',
      'Stays exactly the same — only pressure changes',
      'Becomes 16 times as large',
    ],
    correctIndex: 1,
    reveal:
        'v_rms = √(3RT/M), so v_rms ∝ √T — quadrupling T only DOUBLES v_rms, not quadruples it. In the lab, drag the temperature slider from 300 K toward 1200 K and watch the dots visibly speed up (and shift color hotter), while the v_rms readout climbs by exactly a factor of 2, not 4 — the square root relationship in action.',
  ),
  experiments: [
    'Set T to a low value (100 K) and watch the molecules move sluggishly, mostly cool-colored',
    'Raise T toward 900 K and watch every dot speed up together, shifting toward hot colors',
    'Compare the v_rms, v_avg, and v_mp readouts at any temperature — note the fixed ordering v_rms > v_avg > v_mp',
    'Note the average-KE readout rises in direct proportion to T, confirming KE_avg = (3/2)kT',
    'Imagine doubling T and predict what happens to v_rms before checking the readout (it rises by √2, not by 2)',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The kinetic theory of an IDEAL gas rests on a few simplifying postulates: gas molecules are treated as point masses (negligible volume compared to the container), they are in constant random motion, colliding elastically with each other and the container walls (no kinetic energy lost overall), and — crucially — there are NO intermolecular forces between them except during the instant of collision. These assumptions let us derive macroscopic gas laws purely from Newtonian mechanics applied to a huge number of molecules.',
      title: 'Postulates of kinetic theory',
    ),
    ContentBlock.bullets([
      'Molecules are point masses — their own size is negligible compared to the space between them',
      'Collisions (molecule-molecule and molecule-wall) are perfectly ELASTIC — no kinetic energy is lost',
      'No intermolecular forces act except during collisions (this is what makes it an IDEAL gas)',
      'Molecular motion is completely random — no preferred direction on average',
      'The time of collision is negligible compared to the time between collisions',
    ]),
    ContentBlock.paragraph(
      'Pressure on the container wall arises from the constant bombardment of molecules, each transferring a tiny bit of momentum on every collision. A single molecule bouncing elastically off a wall perpendicular to its velocity reverses that velocity component, transferring momentum 2mvₓ to the wall. Averaging over the enormous number of molecules and collisions per second, summed over the container\'s wall area, gives a steady, macroscopically-measurable force per unit area — pressure.',
      title: 'Where pressure comes from, microscopically',
    ),
    ContentBlock.formula('PV = ⅓Nm(v_rms)²   or equivalently   P = ⅓ρ(v_rms)²',
        title: 'PRESSURE FROM KINETIC THEORY'),
    ContentBlock.paragraph(
      'Combining this kinetic-theory pressure result with the ideal gas law PV = nRT reveals something remarkable: the AVERAGE TRANSLATIONAL KINETIC ENERGY of a single gas molecule depends ONLY on the absolute temperature, not on the type of gas, its mass, or its pressure. This is the single most important result of kinetic theory — it gives temperature a genuine physical meaning for the first time in the syllabus.',
      title: 'The key result: KE and temperature',
    ),
    ContentBlock.formula('Average KE per molecule = (3/2)kT', title: 'THE CENTRAL RESULT (k = Boltzmann constant)'),
    ContentBlock.paragraph(
      'Temperature, in this microscopic picture, is LITERALLY a measure of the average kinetic energy of random molecular motion — nothing more mysterious than that. "Hotter" simply means the molecules are, on average, moving faster (carrying more kinetic energy); "colder" means slower. Absolute zero (0 K) is the (unreachable) temperature at which molecular translational kinetic energy would fall to its theoretical minimum.',
      title: 'Temperature demystified',
    ),
    ContentBlock.paragraph(
      'Not every molecule moves at exactly the same speed — there is a whole distribution (the Maxwell-Boltzmann distribution) of molecular speeds at any given temperature. Three characteristic speeds summarize this distribution: v_rms (root-mean-square, relevant to kinetic energy and pressure), v_avg (the simple arithmetic mean speed), and v_mp (the most probable speed — the peak of the distribution curve). These three always appear in the SAME fixed order at any temperature.',
      title: 'v_rms, v_avg, v_mp — three characteristic speeds',
    ),
    ContentBlock.formula('v_rms > v_avg > v_mp   (always, at any temperature)', title: 'SPEED ORDERING'),
    ContentBlock.realLife(
      'This is why gases diffuse and spread out to fill any container — random, ceaseless molecular motion at speeds of hundreds of meters per second (even at room temperature!) constantly explores all available space. It is also why balloons slowly deflate over days (small, fast molecules like helium leak through microscopic pores) and why the smell of perfume spreads across a room even in still air.',
    ),
    ContentBlock.mistake(
      'Assuming v_rms ∝ T (linear). The correct relation is v_rms ∝ √T — a square-root dependence, meaning you need to QUADRUPLE the absolute temperature to merely DOUBLE the rms speed.',
    ),
    ContentBlock.mistake(
      'Forgetting that the average-KE-per-molecule result, (3/2)kT, depends ONLY on temperature — NOT on the molar mass M or the type of gas. A helium molecule and an oxygen molecule at the same temperature have the SAME average kinetic energy, even though the heavier oxygen molecule must therefore be moving SLOWER on average (since KE = ½mv² is fixed, larger m means smaller v).',
    ),
    ContentBlock.example(
      'Find the rms speed of oxygen (O₂, M = 0.032 kg/mol) molecules at 300 K. (R = 8.314 J/mol·K)\n\nv_rms = √(3RT/M) = √(3 × 8.314 × 300 / 0.032)\n= √(7482.6/0.032)\n= √233831\n≈ 483.6 m/s.\n\nThis is comparable to (in fact a bit faster than) the speed of sound in air — molecular speeds really are that fast, even though the gas as a whole appears still.',
    ),
    ContentBlock.jeeTip(
      'When comparing v_rms for TWO different gases at the SAME temperature, use v_rms ∝ 1/√M directly — no need to recompute the full formula each time. A lighter gas (smaller M) always has a higher rms speed at the same T. This ratio trick saves significant time on JEE numericals.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the direct recall: average KE per molecule = (3/2)kT, and total internal energy of n moles of an ideal MONATOMIC gas = (3/2)nRT (since each molecule contributes only translational KE, no rotational/vibrational modes at typical temperatures). Diatomic gases get extra rotational degrees of freedom, raising this to (5/2)nRT — but that\'s a topic for degrees of freedom / specific heats, not needed here.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up: one molecule bouncing off a wall',
      math: 'Momentum change per collision (elastic, perpendicular wall) = 2mvₓ',
      note: 'Consider a cubical box of side L; a molecule with x-velocity vₓ hits the right wall and rebounds with −vₓ.',
    ),
    DerivationStep(
      title: 'Find the collision rate on that wall',
      math: 'Time between successive hits on the same wall = 2L/vₓ\nForce from one molecule = 2mvₓ ÷ (2L/vₓ) = mvₓ²/L',
    ),
    DerivationStep(
      title: 'Sum over all N molecules, then average over the x-direction',
      math: 'Total force on wall = (m/L)·Σvₓ² = (m/L)·N·⟨vₓ²⟩',
      note: '⟨vₓ²⟩ is the mean-square x-velocity, averaged over all N molecules.',
    ),
    DerivationStep(
      title: 'Use isotropy: motion is random, so ⟨vₓ²⟩=⟨vy²⟩=⟨vz²⟩',
      math: '⟨v²⟩ = ⟨vₓ²⟩+⟨vy²⟩+⟨vz²⟩ = 3⟨vₓ²⟩   →   ⟨vₓ²⟩ = ⟨v²⟩/3',
      note: 'No direction is preferred, so the mean-square speed splits equally among the three perpendicular directions.',
    ),
    DerivationStep(
      title: 'Compute pressure = force / area',
      math: 'P = Force/L² = (m/L³)·N·⟨v²⟩/3 = (Nm/3V)·v_rms²   (V=L³, ⟨v²⟩≡v_rms²)',
      note: 'Rearranged: PV = ⅓Nm(v_rms)² — the central kinetic-theory pressure formula.',
    ),
    DerivationStep(
      title: 'Compare with the ideal gas law to extract average KE',
      math: 'PV = nRT = ⅓Nm(v_rms)²  →  ⅓m(v_rms)² = nRT/N = RT/Nₐ = kT\n→  ½m(v_rms)² = (3/2)kT',
      note: 'k = R/Nₐ is the Boltzmann constant. The final result: average translational KE per molecule = (3/2)kT — independent of the gas\'s identity.',
    ),
  ],
  formulas: const [
    FormulaEntry('Kinetic theory pressure', 'PV = ⅓Nm(v_rms)²   or   P = ⅓ρv_rms²'),
    FormulaEntry('rms speed', 'v_rms = √(3RT/M) = √(3kT/m)'),
    FormulaEntry('Average speed', 'v_avg = √(8RT/πM)'),
    FormulaEntry('Most probable speed', 'v_mp = √(2RT/M)'),
    FormulaEntry('Average KE per molecule', 'KE_avg = (3/2)kT', condition: 'k = Boltzmann constant = R/Nₐ'),
    FormulaEntry('Internal energy of n moles (monatomic ideal gas)', 'U = (3/2)nRT'),
    FormulaEntry('Speed ordering', 'v_rms > v_avg > v_mp'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'According to kinetic theory, the average kinetic energy of a gas molecule depends on:',
      options: ['Its mass only', 'The type of gas only', 'The absolute temperature only', 'Its pressure only'],
      correctIndex: 2,
      solution: 'KE_avg = (3/2)kT depends only on absolute temperature T — not on the mass or identity of the molecule.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the absolute temperature of a gas is doubled, its rms speed becomes:',
      options: ['2 times', '4 times', '√2 times', 'Unchanged'],
      correctIndex: 2,
      solution: 'v_rms ∝ √T, so doubling T multiplies v_rms by √2, not by 2.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The correct ordering of characteristic molecular speeds at any given temperature is:',
      options: ['v_mp > v_avg > v_rms', 'v_avg > v_rms > v_mp', 'v_rms > v_avg > v_mp', 'v_rms = v_avg = v_mp always'],
      correctIndex: 2,
      solution: 'From the Maxwell-Boltzmann distribution, v_rms > v_avg > v_mp always holds, regardless of temperature or gas.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Find v_rms for helium gas (M = 0.004 kg/mol) at 300 K. (R = 8.314 J/mol·K)',
      options: ['1367 m/s', '683 m/s', '2734 m/s', '967 m/s'],
      correctIndex: 0,
      solution: 'v_rms = √(3RT/M) = √(3×8.314×300/0.004) = √(7482.6/0.004) = √1870650 ≈ 1367.7 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'At the same temperature, oxygen (M=32 g/mol) and hydrogen (M=2 g/mol) have rms speeds in ratio v_O2 : v_H2 equal to:',
      options: ['1:4', '1:16', '4:1', '16:1'],
      correctIndex: 0,
      solution: 'v_rms ∝ 1/√M. Ratio v_O2/v_H2 = √(M_H2/M_O2) = √(2/32) = √(1/16) = 1/4. So v_O2:v_H2 = 1:4.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'The average translational kinetic energy of an oxygen molecule and a hydrogen molecule in the same container (thermal equilibrium, same T) is:',
      options: [
        'Equal for both, since KE_avg=(3/2)kT depends only on T',
        'Larger for oxygen since it is heavier',
        'Larger for hydrogen since it moves faster',
        'Cannot be compared without knowing pressure',
      ],
      correctIndex: 0,
      solution: 'Average KE per molecule = (3/2)kT depends only on temperature, which is the same for both gases in thermal equilibrium — so their average kinetic energies are equal, even though hydrogen moves faster (being lighter).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A gas has pressure P and density ρ. According to kinetic theory, v_rms equals:',
      options: ['√(P/ρ)', '√(3P/ρ)', '√(2P/ρ)', '√(P/3ρ)'],
      correctIndex: 1,
      solution: 'From P = ⅓ρv_rms², rearranging gives v_rms² = 3P/ρ, so v_rms = √(3P/ρ).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The internal energy of 2 moles of a monatomic ideal gas at 400 K is: (R = 8.314 J/mol·K)',
      options: ['4988 J', '9977 J', '2494 J', '6650 J'],
      correctIndex: 1,
      solution: 'U = (3/2)nRT = 1.5 × 2 × 8.314 × 400 = 1.5 × 6651.2 = 9976.8 J ≈ 9977 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A key postulate of kinetic theory for an IDEAL gas is that:',
      options: [
        'Molecules attract each other strongly at all separations',
        'Collisions between molecules are perfectly elastic and molecules exert no force on each other except during collision',
        'Molecules have significant volume compared to the container',
        'Molecular motion is directed, not random',
      ],
      correctIndex: 1,
      solution: 'Ideal gas postulates: point-mass molecules, negligible intermolecular force except during collision, perfectly elastic collisions, and random motion.',
    ),
  ],
  revision: [
    'Kinetic theory postulates: point-mass molecules, elastic collisions, no intermolecular forces except at collision, random motion.',
    'Pressure derivation: momentum transfer per wall collision, summed over N molecules and averaged isotropically, gives PV = ⅓Nm(v_rms)².',
    'Combining with PV=nRT gives the central result: average KE per molecule = (3/2)kT — depends ONLY on temperature.',
    'Temperature IS a measure of average molecular kinetic energy — nothing more.',
    'v_rms = √(3RT/M) ∝ √T — doubling T only multiplies v_rms by √2.',
    'Fixed speed ordering at any T: v_rms > v_avg > v_mp.',
    'Internal energy of n moles of monatomic ideal gas: U = (3/2)nRT.',
  ],
  sandboxBuilder: (_) => const KineticTheorySandbox(),
);
