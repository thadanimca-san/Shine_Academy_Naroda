import '../../models/lesson.dart';
import '../../simulators/units_dimensions_sandbox.dart';
import '../../theme/tokens.dart';

/// Units & Dimensions — physics' built-in error detector.
final Lesson unitsDimensionsLesson = Lesson(
  topicId: 'units-dimensions',
  title: 'Units & Dimensions',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Without solving anything, how can you tell in five seconds that the formula T = 2π√(g/L) for a pendulum MUST be wrong?',
  whyItMatters:
      'Dimensional analysis is the cheapest superpower in the exam hall: it catches wrong formulas, recovers half-forgotten ones, and converts units without memorising conversion tables. NEET and JEE both open their papers with a units-and-dimensions question more often than any other topic. It is also the last line of defence against silly errors in every numerical you will ever solve.',
  prediction: const PredictionPrompt(
    scenario:
        'The pendulum period formula is either T = 2π√(L/g) or T = 2π√(g/L). Without any experiment, dimensional analysis says:',
    options: [
      'Both are dimensionally fine — only experiment can decide',
      'Only √(L/g) gives dimensions of time',
      'Only √(g/L) gives dimensions of time',
      'Dimensions can\'t be applied to square roots',
    ],
    correctIndex: 1,
    reveal:
        '√(L/g) has dimensions √(L / (L·T⁻²)) = √(T²) = T — time. Correct. √(g/L) gives 1/T, a frequency, so equating it to a period is dimensional nonsense. In the lab, build [T¹] on the balance and try matching it against different combinations — only consistent ones balance.',
  ),
  experiments: [
    'Pick Force as the target and build M¹L¹T⁻² — watch the balance level off',
    'Try to make Energy with the dimensions of Force — the beam refuses; they differ by one L',
    'Build Pressure (M L⁻¹ T⁻²) and compare with Energy per volume — identical! Same dimensions, different quantities',
    'Press "Weigh the pans" after each build for the verdict',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Every mechanical quantity can be written as a product of powers of three base dimensions: mass [M], length [L] and time [T]. Velocity is L T⁻¹, force is M L T⁻², energy is M L² T⁻². The recipe of powers is the quantity\'s "dimensional formula" — its fingerprint.',
      title: 'Three letters describe all of mechanics',
    ),
    ContentBlock.formula('[Force] = M L T⁻²,  [Energy] = M L² T⁻²,  [Power] = M L² T⁻³',
        title: 'DIMENSIONAL FORMULAS TO KNOW COLD'),
    ContentBlock.bullets([
      'Principle of homogeneity: every term ADDED or EQUATED must have identical dimensions',
      'Arguments of sin, cos, log, exp must be dimensionless',
      'Dimensionless quantities: pure numbers, angles, strain, relative density, coefficients like μ',
      'Same dimensions ≠ same quantity: torque and energy are both M L² T⁻²',
    ]),
    ContentBlock.paragraph(
      'Three uses appear in exams: (1) CHECK a formula — if dimensions of both sides differ, it is wrong, no exceptions. (2) DERIVE a formula up to a constant — assume the answer is a product of powers of the relevant variables and match dimensions. (3) CONVERT units — a quantity n₁u₁ = n₂u₂ lets you carry a value between unit systems.',
      title: 'What dimensional analysis can do',
    ),
    ContentBlock.realLife(
      'In 1999 NASA lost the \$125-million Mars Climate Orbiter because one team used newton-seconds and another pound-seconds — a pure units failure. Every engineering discipline runs dimensional checks for exactly this reason; you are learning the same habit.',
    ),
    ContentBlock.mistake(
      'Believing a dimensionally correct formula must be right. Dimensions cannot see pure numbers: T = 2π√(L/g) and T = 5√(L/g) look identical to dimensional analysis. Correct dimensions are NECESSARY, never sufficient.',
    ),
    ContentBlock.mistake(
      'Adding quantities with different dimensions "because the numbers work out". You can never add a velocity to an acceleration, even if both equal 9.8 numerically. If an equation has v + at², it is wrong before you compute anything.',
    ),
    ContentBlock.example(
      'The centripetal force on a body depends on mass m, speed v and radius r. Derive F up to a constant.\n\nAssume F = k·mᵃvᵇrᶜ.\nM¹L¹T⁻² = Mᵃ·(LT⁻¹)ᵇ·Lᶜ = Mᵃ Lᵇ⁺ᶜ T⁻ᵇ\n\nMatch: a = 1;  −b = −2 → b = 2;  b + c = 1 → c = −1.\n\nSo F = k·mv²/r — the correct form, with k = 1 from experiment.',
    ),
    ContentBlock.jeeTip(
      'JEE loves dimensions of unusual combinations: [ε₀], [μ₀], [√(1/μ₀ε₀)] = velocity, [E/B] = velocity, [h] = M L² T⁻¹ (same as angular momentum), [pressure × volume] = energy. Also: in any equation like x = a·e^(−bt), b must have dimensions T⁻¹ so the exponent stays dimensionless.',
    ),
    ContentBlock.neetNote(
      'NEET favourites: pairs with SAME dimensions — (work, torque), (angular momentum, Planck\'s constant), (pressure, energy density), (impulse, momentum), (light year, wavelength — both lengths!). Also significant figures and error rules: percentage errors ADD when quantities multiply, and multiply by the power for exponents.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the homogeneity principle',
      math: '[LHS] = [RHS]  (term by term)',
      note: 'Physics equations relate quantities, so their dimensional recipes must match.',
    ),
    DerivationStep(
      title: 'Worked check: v² = u² + 2as',
      math: '[v²] = L²T⁻²;  [u²] = L²T⁻²;  [2as] = (LT⁻²)(L) = L²T⁻²',
      note: 'All three terms match — the equation is dimensionally sound.',
    ),
    DerivationStep(
      title: 'Deriving by power matching',
      math: 'Assume Q = k·xᵃyᵇzᶜ → write both sides in M, L, T → equate powers',
      note: 'Three equations (for M, L, T) determine up to three unknown exponents.',
    ),
    DerivationStep(
      title: 'Unit conversion rule',
      math: 'n₂ = n₁ · [M₁/M₂]ᵃ · [L₁/L₂]ᵇ · [T₁/T₂]ᶜ',
      note: 'Convert 1 N to dynes: a=1,b=1,c=−2 → 1 N = (1000 g/1 g)(100 cm/1 cm)(1)⁻² = 10⁵ dyne.',
    ),
  ],
  formulas: const [
    FormulaEntry('Velocity / acceleration', '[v] = LT⁻¹,  [a] = LT⁻²'),
    FormulaEntry('Force / energy / power', 'MLT⁻²,  ML²T⁻²,  ML²T⁻³'),
    FormulaEntry('Pressure / density', 'ML⁻¹T⁻²,  ML⁻³'),
    FormulaEntry('Momentum / impulse', 'MLT⁻¹ (identical pair)'),
    FormulaEntry('Angular momentum / Planck h', 'ML²T⁻¹ (identical pair)'),
    FormulaEntry('Unit conversion', 'n₁u₁ = n₂u₂'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The dimensional formula of force is:',
      options: ['MLT⁻¹', 'MLT⁻²', 'ML²T⁻²', 'ML⁻¹T⁻²'],
      correctIndex: 1,
      solution: 'F = ma → [M]·[LT⁻²] = MLT⁻².',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Which pair has the SAME dimensional formula?',
      options: [
        'Force and work',
        'Work and torque',
        'Power and pressure',
        'Momentum and energy',
      ],
      correctIndex: 1,
      solution:
          'Work = force × distance and torque = force × lever arm are both ML²T⁻². (They differ physically — one is a scalar, one a vector.)',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In x = a·sin(bt), where x is length and t is time, the dimensions of b are:',
      options: ['T', 'T⁻¹', 'LT⁻¹', 'dimensionless'],
      correctIndex: 1,
      solution:
          'The argument of sine must be dimensionless: [bt] = 1 → [b] = T⁻¹. (And [a] = L, since it carries x\'s dimension.)',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: '1 newton expressed in dynes is:',
      options: ['10³', '10⁴', '10⁵', '10⁷'],
      correctIndex: 2,
      solution:
          'N = kg·m/s², dyne = g·cm/s². Factor = 1000 (g) × 100 (cm) = 10⁵. So 1 N = 10⁵ dyne.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The velocity v of a particle depends on time as v = At² + Bt. The dimensions of B are:',
      options: ['LT⁻¹', 'LT⁻²', 'LT⁻³', 'L'],
      correctIndex: 1,
      solution:
          'Each term must be a velocity: [Bt] = LT⁻¹ → [B] = LT⁻². (Similarly [A] = LT⁻³.)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'If energy E, velocity v and time T are chosen as fundamental quantities, the dimensions of surface tension are:',
      options: ['Ev⁻²T⁻²', 'Ev⁻¹T⁻²', 'E²v⁻¹T⁻²', 'Ev⁻²T⁻¹'],
      correctIndex: 0,
      solution:
          'Surface tension σ = force/length = MT⁻². Write M = E v⁻², L = vT: σ = (Ev⁻²)·T⁻² = Ev⁻²T⁻². Express old base dimensions in terms of the new trio and substitute.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'The period of a drop\'s oscillation may depend on surface tension S, radius r and density ρ. By dimensions, T is proportional to:',
      options: ['√(ρr³/S)', '√(S/ρr³)', 'ρr³/S', '√(ρr/S)'],
      correctIndex: 0,
      solution:
          'Assume T = k·Sᵃrᵇρᶜ. [S] = MT⁻², [r] = L, [ρ] = ML⁻³. Matching M: a + c = 0; L: b − 3c = 0; T: −2a = 1 → a = −½, c = ½, b = 3/2. T = k√(ρr³/S) — the classic Rayleigh drop formula.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A formula passes the dimensional check. We can conclude:',
      options: [
        'It is definitely correct',
        'It may be correct — numerical constants are invisible to dimensions',
        'It is definitely wrong',
        'Its constants are all 1',
      ],
      correctIndex: 1,
      solution:
          'Dimensional consistency is necessary but not sufficient. Factors like ½, 2π, or even wrong dimensionless combinations slip through unseen.',
    ),
  ],
  revision: [
    'Homogeneity: every added/equated term must carry identical dimensions.',
    'sin, cos, log, exp arguments are always dimensionless.',
    'Same-dimension pairs: work↔torque, impulse↔momentum, h↔angular momentum, pressure↔energy density.',
    'Derive formulas: assume products of powers, match M, L, T exponents.',
    'Convert units with n₁u₁ = n₂u₂ (1 N = 10⁵ dyne, 1 J = 10⁷ erg).',
    'Dimensional check catches wrong formulas but cannot bless right ones.',
  ],
  sandboxBuilder: (_) => const UnitsDimensionsSandbox(),
);
