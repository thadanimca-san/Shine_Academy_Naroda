import '../../models/lesson.dart';
import '../../simulators/shm_duel_sim.dart';
import '../../theme/tokens.dart';

/// Spring vs Pendulum — two different restoring forces, both producing SHM.
final Lesson shmDuelLesson = Lesson(
  topicId: 'shm-duel',
  title: 'Spring vs Pendulum',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Take a spring-mass oscillator and a simple pendulum to the Moon, where gravity is only 1/6th of Earth\'s. One of them keeps ticking at exactly the same rate as on Earth — the other slows down dramatically. Which is which, and why does gravity matter to one but not the other?',
  whyItMatters:
      'Both systems obey the same SHM mathematics, but their PHYSICAL origin is completely different — one restoring force comes from a spring\'s elasticity, the other from gravity\'s pull on a swinging bob. Exam setters love pitting these two against each other precisely because students who memorise formulas without understanding the mechanism get tripped up. This lesson is where "know the formula" turns into "understand the physics."',
  prediction: const PredictionPrompt(
    scenario:
        'A spring-mass system and a simple pendulum, both tuned to the same period T on Earth, are taken to the Moon (g is 1/6th of Earth\'s). What happens to each period?',
    options: [
      'Both periods stay the same T',
      'Both periods increase',
      'The spring\'s period is unchanged; the pendulum\'s period increases',
      'The spring\'s period increases; the pendulum\'s period is unchanged',
    ],
    correctIndex: 2,
    reveal:
        'T = 2π√(m/k) for the spring has no g in it at all — it is exactly the same on the Moon. T = 2π√(L/g) for the pendulum depends directly on g, so with g six times smaller, T grows by √6 ≈ 2.45×. In the lab, use the gravity slider to dial g down and watch the pendulum swing lazily while the spring bounces at its usual rate, completely unaffected.',
  ),
  experiments: [
    'Set both systems to match periods on Earth gravity, then reduce g — watch only the pendulum slow down',
    'Double the pendulum length L and confirm T grows by √2, not by 2',
    'Double the spring mass m and confirm T also grows by √2',
    'Try changing the pendulum\'s bob mass — notice T does NOT change (mass cancels out)',
    'Push the pendulum to a large swing angle and see it drift away from the ideal SHM prediction',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Both the spring-mass system and the simple pendulum swing back and forth, and both — under the right conditions — execute simple harmonic motion. But the force doing the restoring is completely different in origin: the spring\'s restoring force comes from the material\'s elasticity (Hooke\'s law), while the pendulum\'s restoring force comes from a component of gravity pulling the bob back toward the lowest point.',
      title: 'Same math, different physics',
    ),
    ContentBlock.formula('T_spring = 2π√(m/k)     T_pendulum = 2π√(L/g)',
        title: 'THE TWO PERIOD FORMULAS'),
    ContentBlock.bullets([
      'Spring: depends on mass m and stiffness k — NOT on gravity g',
      'Pendulum: depends on length L and gravity g — NOT on the bob\'s mass m',
      'This is the single most exam-tested contrast in oscillations',
    ]),
    ContentBlock.paragraph(
      'For a simple pendulum of length L displaced by a small angle θ, gravity mg has a component mg sinθ tangential to the arc, pulling the bob back toward the vertical. For SMALL angles (θ in radians, roughly under 10°), sinθ ≈ θ, so the restoring force becomes proportional to angular displacement — this is what makes it SHM. At large angles this approximation breaks and the motion is no longer perfectly harmonic (the period actually increases slightly).',
      title: 'Why the pendulum needs the small-angle approximation',
    ),
    ContentBlock.paragraph(
      'Notice the pendulum\'s mass completely cancels out of the period formula — this is Galileo\'s famous observation that a heavy pendulum and a light one of the same length swing in step. It happens because both gravity\'s pull (mg) and inertia (m) scale with mass identically, just as in free fall. The spring has no such cancellation: a heavier mass on the same spring genuinely swings slower, because the spring force doesn\'t know about gravity or inertia the same way.',
      title: 'Why mass matters to one but not the other',
    ),
    ContentBlock.realLife(
      'Grandfather clocks use a pendulum precisely because T = 2π√(L/g) is so predictable — a clockmaker just adjusts the bob\'s height to fine-tune the tick rate, no need to weigh anything precisely. A wristwatch, however, cannot use a pendulum (gravity direction changes as you move your wrist) — instead it uses a balance wheel and hairspring, essentially a rotational spring-mass system, unaffected by orientation or gravity.',
    ),
    ContentBlock.mistake(
      'Assuming heavier pendulum bobs swing slower "because they\'re heavier." The mass cancels completely in T = 2π√(L/g) — only length and gravity matter. Students who reach for "heavier = slower" are importing intuition from the spring case where it sometimes does apply (m appears in T_spring).',
    ),
    ContentBlock.mistake(
      'Applying the small-angle pendulum formula to large swings (like a playground swing pushed high). Beyond about 15-20°, sinθ ≈ θ fails noticeably and the real period is measurably longer than 2π√(L/g) predicts. JEE occasionally probes this qualitative fact even without asking for the correction formula.',
    ),
    ContentBlock.example(
      'A simple pendulum has length 1.0 m on Earth (g = 10 m/s²). Find its period, then find the period on the Moon where g_moon = 1.67 m/s².\n\nEarth: T = 2π√(L/g) = 2π√(1.0/10) = 2π√0.1 ≈ 2π(0.316) ≈ 1.99 s.\nMoon: T\' = 2π√(1.0/1.67) = 2π√0.599 ≈ 2π(0.774) ≈ 4.86 s.\n\nThe period grows because gravity, and hence the restoring force, is weaker — the pendulum takes longer to swing back.',
    ),
    ContentBlock.jeeTip(
      'A classic combined question: "A pendulum clock is taken to a planet where g is different — does it run fast or slow?" Since T ∝ 1/√g, LOWER g means LONGER period means the clock runs SLOW (fewer ticks per real second). Conversely, higher g makes it tick faster. Always check whether the question is about the spring (no g dependence) before applying this logic.',
    ),
    ContentBlock.neetNote(
      'NEET often asks: "A pendulum and a spring both have period T on Earth. Which changes if taken inside a lift accelerating upward?" The effective g increases inside an upward-accelerating lift (g_eff = g + a), so the PENDULUM period shortens (T ∝ 1/√g_eff), while the SPRING period is completely unaffected — it depends only on m and k, never on g.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the pendulum\'s tangential restoring force',
      math: 'F_tangential = −mg sinθ',
      note: 'Gravity component along the arc, opposing increasing θ.',
    ),
    DerivationStep(
      title: 'Apply the small-angle approximation',
      math: 'sinθ ≈ θ (for θ small, in radians)  →  F ≈ −mgθ',
    ),
    DerivationStep(
      title: 'Relate arc displacement to angle',
      math: 's = Lθ  →  θ = s/L  →  F ≈ −(mg/L)·s',
      note: 'This is F = −k_eff·s with an effective spring constant k_eff = mg/L.',
    ),
    DerivationStep(
      title: 'Compare directly to the spring case',
      math: 'Spring: ω_spring = √(k/m)     Pendulum: ω_pendulum = √(k_eff/m) = √(g/L)',
      note: 'Substituting k_eff = mg/L makes the mass cancel — a coincidence of gravity, not general.',
    ),
    DerivationStep(
      title: 'Write both periods from ω = 2π/T',
      math: 'T_spring = 2π√(m/k)     T_pendulum = 2π√(L/g)',
      note: 'Same mathematical form 2π√(inertia-like / stiffness-like), but the roles of mass and gravity are swapped between the two systems.',
    ),
  ],
  formulas: const [
    FormulaEntry('Spring period', 'T = 2π√(m/k)'),
    FormulaEntry('Pendulum period', 'T = 2π√(L/g)'),
    FormulaEntry('Spring angular frequency', 'ω = √(k/m)'),
    FormulaEntry('Pendulum angular frequency', 'ω = √(g/L)'),
    FormulaEntry('Pendulum effective spring constant', 'k_eff = mg/L'),
    FormulaEntry('Frequency', 'f = 1/T'),
    FormulaEntry('Small-angle condition', 'sinθ ≈ θ', condition: 'valid for θ ≲ 10°'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The period of a simple pendulum depends on:',
      options: ['Mass of the bob and length', 'Length and acceleration due to gravity', 'Mass and gravity only', 'Amplitude only'],
      correctIndex: 1,
      solution: 'T = 2π√(L/g) — mass cancels out completely; only L and g matter.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the length of a simple pendulum is quadrupled, its period becomes:',
      options: ['4 times', '2 times', 'Half', 'Unchanged'],
      correctIndex: 1,
      solution: 'T ∝ √L. Quadrupling L multiplies T by √4 = 2.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A pendulum clock keeping correct time on Earth is taken to a place where g is 4% less. The clock will:',
      options: ['Gain time', 'Lose time (run slow)', 'Keep correct time', 'Stop completely'],
      correctIndex: 1,
      solution: 'T ∝ 1/√g. Lower g means longer period, so each swing takes longer — the clock ticks fewer times per real second and runs slow.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A spring-mass system and a simple pendulum are both taken to the Moon. Compared to their periods on Earth:',
      options: [
        'Both periods increase',
        'Both periods stay the same',
        'Only the pendulum\'s period increases; the spring\'s is unchanged',
        'Only the spring\'s period increases; the pendulum\'s is unchanged',
      ],
      correctIndex: 2,
      solution: 'T_spring = 2π√(m/k) has no g — unaffected. T_pendulum = 2π√(L/g) grows as g shrinks.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A simple pendulum has a period of 2 s on Earth (g = 10 m/s²). Its length is approximately:',
      options: ['0.5 m', '1.0 m', '2.0 m', '4.0 m'],
      correctIndex: 1,
      solution:
          'T = 2π√(L/g) → 2 = 2π√(L/10) → √(L/10) = 1/π → L/10 = 1/π² ≈ 0.101 → L ≈ 1.01 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A simple pendulum is set up inside a lift accelerating UPWARD with acceleration a. Its new period compared to the stationary-lift period T is:',
      options: ['Longer than T', 'Shorter than T', 'Exactly T', 'Cannot be determined'],
      correctIndex: 1,
      solution:
          'Effective gravity increases: g_eff = g + a. Since T ∝ 1/√g_eff, a larger g_eff gives a SHORTER period.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two simple pendulums of lengths L and 4L start swinging together (in phase) at t = 0. After how many oscillations of the SHORTER pendulum will they again be in phase?',
      options: ['1', '2', '3', '4'],
      correctIndex: 1,
      solution:
          'T ∝ √L, so T(4L) = 2·T(L). They realign in phase when the shorter one has completed an integer number matching the longer one\'s cycles: 2 oscillations of the short pendulum = 1 oscillation of the long one.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A spring of constant k supports mass m with period T on Earth. If taken to a planet with twice Earth\'s gravity, the new period is:',
      options: ['T/2', 'T', 'T√2', '2T'],
      correctIndex: 1,
      solution: 'T_spring = 2π√(m/k) contains no g whatsoever — the period is exactly T on any planet.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A simple pendulum is swung with a large amplitude (30°) instead of a small one. Compared to the small-angle prediction T = 2π√(L/g), the actual period is:',
      options: ['Exactly equal', 'Slightly less', 'Slightly more', 'Exactly double'],
      correctIndex: 2,
      solution:
          'At large angles sinθ < θ, so the true restoring force is weaker than the small-angle approximation assumes, making the real period slightly LONGER than 2π√(L/g).',
    ),
  ],
  revision: [
    'Spring: T = 2π√(m/k) — depends on mass and stiffness, NEVER on gravity.',
    'Pendulum: T = 2π√(L/g) — depends on length and gravity, NEVER on the bob\'s mass.',
    'Pendulum mass cancels because both gravitational force and inertia scale with m identically.',
    'Small-angle approximation sinθ≈θ is what makes pendulum motion SHM; large swings deviate.',
    'On the Moon (lower g): pendulum period increases; spring period is completely unaffected.',
    'In an accelerating lift, pendulum period changes via g_eff = g ± a; spring period never does.',
  ],
  sandboxBuilder: (_) => const ShmDuelSimulator(),
);
