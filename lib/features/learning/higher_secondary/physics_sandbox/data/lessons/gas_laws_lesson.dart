import '../../models/lesson.dart';
import '../../simulators/gas_laws_sim.dart';
import '../../theme/tokens.dart';

/// Ideal Gas Laws — Boyle's, Charles's and Gay-Lussac's laws unified into PV=nRT.
final Lesson gasLawsLesson = Lesson(
  topicId: 'gas-laws',
  title: 'Ideal Gas Laws',
  accentColor: Palette.chThermal,
  bigQuestion:
      'A sealed syringe full of air has its plunger pushed in, squeezing the gas to half its volume. The pressure inside doesn\'t just increase a little — it roughly doubles. Why does squeezing gas into a smaller space make it push back so predictably harder?',
  whyItMatters:
      'The ideal gas law PV = nRT is the single equation that ties together pressure, volume, temperature and amount of gas — and it underlies weather systems, engines, refrigerators, and even why a bag of chips puffs up on a mountain flight. NEET and JEE test each individual law (Boyle\'s, Charles\'s, Gay-Lussac\'s) as well as the combined PV = nRT, and this topic is the direct gateway into thermodynamics.',
  prediction: const PredictionPrompt(
    scenario:
        'A fixed amount of gas in a sealed cylinder is compressed to HALF its original volume while temperature is kept constant. What happens to the pressure?',
    options: [
      'Pressure stays the same — only volume changed',
      'Pressure halves — less volume means less pressure',
      'Pressure doubles — Boyle\'s law: PV = constant at fixed T',
      'Pressure becomes zero',
    ],
    correctIndex: 2,
    reveal:
        'Boyle\'s law says PV = constant when temperature and amount of gas are fixed — so halving V must double P to keep the product the same. In the lab, drag the volume slider down to half its starting value at constant temperature and watch the pressure readout jump to roughly twice its original value.',
  ),
  experiments: [
    'Compress the gas at constant temperature and watch pressure rise following PV = constant',
    'Heat the gas at constant pressure and watch volume expand following V/T = constant',
    'Heat the gas in a rigid, fixed-volume container and watch pressure rise following P/T = constant',
    'Combine changes in P, V and T simultaneously and verify PV/T stays constant throughout',
    'Push temperature toward very low values or pressure toward very high values and note where ideal behavior starts to break down',
  ],
  concept: const [
    ContentBlock.paragraph(
      'An ideal gas is a simplified model where gas molecules are treated as point particles with no volume of their own and no intermolecular forces except during brief, perfectly elastic collisions. Real gases behave very close to this ideal at ordinary pressures and temperatures, which is why the ideal gas laws work so well for everyday physics — air in a tyre, gas in a balloon, or air in your lungs.',
      title: 'What "ideal gas" means',
    ),
    ContentBlock.formula('PV = constant  (at fixed T, n)', title: 'BOYLE\'S LAW'),
    ContentBlock.formula('V/T = constant  (at fixed P, n)', title: 'CHARLES\'S LAW'),
    ContentBlock.formula('P/T = constant  (at fixed V, n)', title: 'GAY-LUSSAC\'S LAW'),
    ContentBlock.bullets([
      'Boyle\'s law: at constant temperature, pressure and volume are inversely proportional',
      'Charles\'s law: at constant pressure, volume grows linearly with absolute temperature',
      'Gay-Lussac\'s law: at constant volume, pressure grows linearly with absolute temperature',
      'All three are special cases of one single, more general law',
    ]),
    ContentBlock.formula('PV = nRT', title: 'THE IDEAL GAS LAW'),
    ContentBlock.paragraph(
      'PV = nRT combines all three individual laws into one equation: n is the number of moles of gas, and R = 8.314 J/(mol·K) is the universal gas constant. If you hold n fixed and any ONE of P, V, T fixed, the equation reduces exactly to one of Boyle\'s, Charles\'s, or Gay-Lussac\'s laws — they are not three separate laws so much as three different "slices" through the same underlying relationship.',
      title: 'One law to rule them all',
    ),
    ContentBlock.bullets([
      'No intermolecular forces (molecules interact only via elastic collisions)',
      'Molecules themselves occupy negligible volume compared to the container',
      'Collisions with walls and each other are perfectly elastic (no energy lost)',
      'Molecular motion is random and follows Newtonian mechanics',
    ], title: 'Key assumptions of the ideal gas model'),
    ContentBlock.realLife(
      'A sealed bag of chips puffs up when you take it on a flight because cabin pressure drops (lower P outside), and the trapped air inside expands to balance — a direct real-world Boyle\'s law demonstration. A car tyre\'s pressure rises noticeably after highway driving because friction heats the air inside (Gay-Lussac\'s law at roughly constant volume), which is why tyre pressure should always be checked when tyres are cold.',
    ),
    ContentBlock.mistake(
      'Using Celsius temperature directly in gas law equations. All gas laws require ABSOLUTE temperature in Kelvin (K = °C + 273), because the proportionalities (V∝T, P∝T) are only true when T is measured from absolute zero. Plugging in Celsius gives systematically wrong answers, especially for ratio problems.',
    ),
    ContentBlock.mistake(
      'Assuming real gases obey PV = nRT exactly under ALL conditions. At very high pressure (molecules are forced close together, so their own volume becomes significant) or very low temperature (intermolecular attractive forces become significant, sometimes even causing condensation), real gases deviate substantially from ideal behavior — this is where the Van der Waals correction becomes relevant.',
    ),
    ContentBlock.example(
      '2 moles of an ideal gas occupy 0.02 m³ at temperature 300 K. Find the pressure. (R = 8.314 J/mol·K)\n\nPV = nRT\nP = nRT/V = (2 × 8.314 × 300) / 0.02\n= 4988.4 / 0.02\n= 249,420 Pa ≈ 2.49×10⁵ Pa.',
    ),
    ContentBlock.jeeTip(
      'For problems comparing gas in TWO different states (before and after some change), use the combined gas law P₁V₁/T₁ = P₂V₂/T₂ directly — it avoids computing n or R altogether, since both sides equal nR (a constant for a fixed amount of gas). This shortcut handles the vast majority of gas-law numericals cleanly.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests graph interpretation: a P-V graph at constant T is a hyperbola (Boyle\'s law); a V-T graph at constant P is a straight line through the origin (in Kelvin); a P-T graph at constant V is also a straight line through the origin. Recognising which variable is held constant from the graph shape is a fast way to identify the law being tested.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Boyle\'s law at fixed temperature T₁',
      math: 'P₁V₁ = P₂V₁\' at same T₁ (relating two states via isothermal change)',
      note: 'Boyle\'s law alone connects P and V only when T does not change.',
    ),
    DerivationStep(
      title: 'Then apply Gay-Lussac\'s law to change temperature at fixed volume',
      math: 'P₂/T₁ = P_final/T₂ at fixed V₂',
      note: 'This connects the intermediate state to a second temperature.',
    ),
    DerivationStep(
      title: 'Chain the two steps together for a general process',
      math: 'P₁V₁/T₁ = P₂V₂/T₂',
      note: 'This is the combined gas law, valid for any change of state of a fixed amount of gas.',
    ),
    DerivationStep(
      title: 'Recognise the ratio PV/T is constant for a fixed amount of gas',
      math: 'PV/T = constant = nR',
      note: 'Experimentally, this constant is found to be proportional to the number of moles n, with proportionality constant R (same for all ideal gases).',
    ),
    DerivationStep(
      title: 'Write the full ideal gas law',
      math: 'PV = nRT,   R = 8.314 J/(mol·K)',
      note: 'Setting n or one of P, V, T fixed recovers each individual gas law as a special case.',
    ),
  ],
  formulas: const [
    FormulaEntry('Ideal gas law', 'PV = nRT'),
    FormulaEntry('Boyle\'s law', 'P₁V₁ = P₂V₂', condition: 'constant T, n'),
    FormulaEntry('Charles\'s law', 'V₁/T₁ = V₂/T₂', condition: 'constant P, n'),
    FormulaEntry('Gay-Lussac\'s law', 'P₁/T₁ = P₂/T₂', condition: 'constant V, n'),
    FormulaEntry('Combined gas law', 'P₁V₁/T₁ = P₂V₂/T₂', condition: 'fixed n'),
    FormulaEntry('Universal gas constant', 'R = 8.314 J/(mol·K)'),
    FormulaEntry('Moles from mass', 'n = m/M', condition: 'M = molar mass'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'At constant temperature, if the volume of a gas is reduced to one-third, its pressure becomes:',
      options: ['One-third', 'Three times', 'Same', 'Nine times'],
      correctIndex: 1,
      solution: 'Boyle\'s law: PV = constant. Reducing V to V/3 requires P to become 3P to keep the product the same.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The ideal gas law PV = nRT requires temperature to be measured in:',
      options: ['Celsius', 'Fahrenheit', 'Kelvin (absolute)', 'Any scale — it doesn\'t matter'],
      correctIndex: 2,
      solution: 'The proportionalities in gas laws hold only when T is absolute (Kelvin), since they are referenced from absolute zero.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A gas at constant pressure is heated from 27°C to 127°C. Its volume increases by a factor of:',
      options: ['127/27', '400/300', '4.7', '2'],
      correctIndex: 1,
      solution: 'Convert to Kelvin: T₁=300K, T₂=400K. Charles\'s law: V₂/V₁ = T₂/T₁ = 400/300 ≈ 1.33.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A rigid sealed container of gas is heated, raising its absolute temperature by 50%. Assuming ideal gas behavior, the pressure:',
      options: ['Increases by 50%', 'Decreases by 50%', 'Stays the same', 'Increases by 100%'],
      correctIndex: 0,
      solution: 'Fixed volume → Gay-Lussac\'s law: P ∝ T. A 50% increase in T gives a 50% increase in P.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: '1 mole of an ideal gas at 300 K occupies 24.6 L at 1 atm pressure. Which law/equation directly confirms this from PV=nRT?',
      options: ['Boyle\'s law alone', 'Charles\'s law alone', 'The full ideal gas law with n=1, T=300K', 'Gay-Lussac\'s law alone'],
      correctIndex: 2,
      solution: 'This is simply plugging n=1, T=300K into PV=nRT to solve for V — a direct application of the full equation, not a special-case law.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A gas occupies 4 L at 2 atm and 300 K. It is compressed to 2 L and heated to 450 K. The new pressure is:',
      options: ['3 atm', '4 atm', '6 atm', '1.5 atm'],
      correctIndex: 2,
      solution:
          'Combined gas law: P₁V₁/T₁ = P₂V₂/T₂ → (2×4)/300 = (P₂×2)/450 → 8/300 = 2P₂/450 → P₂ = 8×450/(300×2) = 6 atm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: '2 moles of an ideal gas at temperature T occupy volume V at pressure P. If the gas is replaced by 4 moles at the same T and V, the new pressure is:',
      options: ['P/2', 'P', '2P', '4P'],
      correctIndex: 2,
      solution: 'PV = nRT → P = nRT/V ∝ n at fixed T, V. Doubling n (2 to 4 moles) doubles P.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A vessel contains a mixture of 2 moles of gas A and 3 moles of gas B at total pressure P. The partial pressure of gas A is:',
      options: ['P/5', '2P/5', '3P/5', 'P'],
      correctIndex: 1,
      solution:
          'By Dalton\'s law (an extension of the ideal gas law to mixtures), each gas contributes pressure proportional to its mole fraction. Mole fraction of A = 2/(2+3) = 2/5, so partial pressure of A = 2P/5.',
    ),
  ],
  revision: [
    'Boyle\'s law: PV = constant at fixed T. Charles\'s law: V/T = constant at fixed P. Gay-Lussac\'s: P/T = constant at fixed V.',
    'All three combine into PV = nRT, the ideal gas law, with R = 8.314 J/(mol·K).',
    'Always use ABSOLUTE temperature (Kelvin) in gas law calculations.',
    'Combined gas law P₁V₁/T₁ = P₂V₂/T₂ handles two-state problems without needing n or R.',
    'Ideal gas assumes no intermolecular forces and negligible molecular volume.',
    'Real gases deviate from ideal behavior at high pressure (molecular volume matters) or low temperature (attractive forces matter).',
  ],
  sandboxBuilder: (_) => const GasLawsSimulator(),
);
