import '../../models/lesson.dart';
import '../../simulators/oscillations_waves_sim.dart';
import '../../theme/tokens.dart';

/// SHM & Spring–Mass — the restoring force that defines all oscillation.
final Lesson shmLesson = Lesson(
  topicId: 'shm-basics',
  title: 'SHM & Spring–Mass',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A mass on a spring is pulled down and released. It bounces up and down forever (ideally) with a period that never changes — not even as the swings get smaller and smaller. How can the TIME for one bounce stay exactly the same no matter how far you stretched it?',
  whyItMatters:
      'Simple Harmonic Motion is the single most tested motion pattern after straight-line kinematics — it governs springs, pendulums, vibrating atoms, AC circuits, and even the way a guitar string moves. Once you know SHM, you can predict period, velocity, and energy for any system that obeys a linear restoring force, which is most of physics near equilibrium.',
  prediction: const PredictionPrompt(
    scenario:
        'A mass on a spring is pulled to amplitude A and released; its period is T. If you instead pull it to amplitude 2A (same spring, same mass) and release it, the new period is:',
    options: [
      'T/2 — bigger swing means it moves faster overall',
      'T — unchanged, no matter the amplitude',
      '2T — bigger swing takes proportionally longer',
      '4T — period depends on A²',
    ],
    correctIndex: 1,
    reveal:
        'T = 2π√(m/k) contains no A at all — period is independent of amplitude in SHM. A bigger stretch means a bigger restoring force AND a longer path, and the two effects cancel exactly. In the lab, drag the amplitude slider to different values and watch the period readout on the graph stay locked while the peak speed changes.',
  ),
  experiments: [
    'Set amplitude to a small value, then a large one — confirm T stays exactly the same',
    'Double the mass m and watch T grow by √2',
    'Quadruple the spring stiffness k and watch T halve',
    'Pause at the extreme position and read v = 0; pause at the centre and read v = maximum',
    'Watch the KE and PE bars trade off — their sum stays constant through the whole cycle',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Simple Harmonic Motion happens whenever the restoring force is directly proportional to displacement from equilibrium and always points back toward it. Pull a spring-mass system away from equilibrium by x and the spring pulls back with force F = −kx — the minus sign says the force always opposes the displacement. This single rule, F = −kx, is the definition of SHM; everything else follows from it.',
      title: 'The defining condition',
    ),
    ContentBlock.formula('F = −kx  (defines SHM)', title: 'RESTORING FORCE LAW'),
    ContentBlock.formula('x(t) = A cos(ωt + φ),   ω = √(k/m),   T = 2π√(m/k)',
        title: 'POSITION, ANGULAR FREQUENCY, PERIOD'),
    ContentBlock.bullets([
      'A = amplitude, the maximum displacement from equilibrium',
      'ω = angular frequency (rad/s), fixed by k and m only — never by A',
      'φ = phase constant, set by where/how the motion starts',
      'T = 2π/ω is the time for one full cycle; f = 1/T is frequency in Hz',
    ]),
    ContentBlock.paragraph(
      'Differentiating x(t) gives velocity v(t) = −Aω sin(ωt+φ), and differentiating again gives acceleration a(t) = −Aω² cos(ωt+φ) = −ω²x. Notice a = −ω²x is exactly Newton\'s second law form of F = −kx, since ma = −kx gives a = −(k/m)x = −ω²x. Speed is maximum at the centre (x = 0) and zero at the extremes; acceleration is the opposite — zero at the centre, maximum at the extremes.',
      title: 'Velocity and acceleration follow',
    ),
    ContentBlock.formula('E = ½kA² = KE + PE = constant', title: 'ENERGY CONSERVATION IN SHM'),
    ContentBlock.bullets([
      'KE = ½mv² is maximum at the centre, zero at the extremes',
      'PE = ½kx² is zero at the centre, maximum at the extremes',
      'Total mechanical energy E = ½kA² never changes (no friction)',
      'Energy trades between KE and PE twice every cycle',
    ]),
    ContentBlock.realLife(
      'Every quartz watch keeps time using a tiny quartz crystal vibrating in SHM at a precise frequency; a car\'s suspension springs oscillate in (damped) SHM to smooth out bumps; even the electrons in an antenna oscillate harmonically to broadcast radio waves. The mathematics of F = −kx shows up whenever nature nudges something back toward balance.',
    ),
    ContentBlock.mistake(
      'Assuming a bigger amplitude means a longer period, "because it has farther to travel." In SHM the restoring force also grows with displacement, so the system accelerates harder over the larger distance — the two effects cancel and T stays fixed. This cancellation is unique to F ∝ −x; it does NOT happen for other restoring-force laws.',
    ),
    ContentBlock.mistake(
      'Confusing angular frequency ω with the actual rotational speed of anything. In spring-mass SHM nothing is rotating — ω = √(k/m) is simply a rate constant with units rad/s that makes the cosine argument work out. Don\'t look for a spinning wheel; it is purely a mathematical parameter of the oscillation.',
    ),
    ContentBlock.example(
      'A 0.5 kg mass on a spring of k = 200 N/m is pulled 4 cm from equilibrium and released. Find ω, T, and the maximum speed.\n\nω = √(k/m) = √(200/0.5) = √400 = 20 rad/s.\nT = 2π/ω = 2π/20 ≈ 0.314 s.\nMaximum speed occurs at x = 0: v_max = Aω = 0.04 × 20 = 0.8 m/s.',
    ),
    ContentBlock.jeeTip(
      'Whenever a problem gives you F = −kx directly (even disguised as a torque or restoring pressure), you can read off ω = √(k/m) immediately without deriving from scratch — this includes torsional oscillators (ω = √(κ/I)) and any linear-restoring-force system. Recognising the F ∝ −x pattern is often the whole trick.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the energy graph shapes: KE vs x is an inverted parabola (max at x = 0), PE vs x is an upright parabola (max at x = ±A), and their sum is a flat horizontal line. Also remember: at x = A/2, PE is only 1/4 of total energy — don\'t assume it\'s half just because displacement is half (energy depends on x², not x).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Newton\'s second law with the restoring force',
      math: 'ma = −kx  →  m(d²x/dt²) = −kx',
      note: 'This is the equation of motion that defines SHM.',
    ),
    DerivationStep(
      title: 'Rewrite as a standard differential equation',
      math: 'd²x/dt² = −(k/m)x = −ω²x,   ω² = k/m',
    ),
    DerivationStep(
      title: 'Propose the solution and verify',
      math: 'x(t) = A cos(ωt + φ)',
      note: 'Differentiating twice: d²x/dt² = −Aω² cos(ωt+φ) = −ω²x — it satisfies the equation for ANY A and φ.',
    ),
    DerivationStep(
      title: 'Differentiate to get velocity and acceleration',
      math: 'v(t) = −Aω sin(ωt+φ),   a(t) = −Aω² cos(ωt+φ)',
    ),
    DerivationStep(
      title: 'Read off the period',
      math: 'ω = 2π/T  →  T = 2π/ω = 2π√(m/k)',
      note: 'Period depends only on m and k — never on amplitude A.',
    ),
    DerivationStep(
      title: 'Derive the energy conservation relation',
      math: 'E = ½mv² + ½kx² = ½m(Aω sinθ)² + ½k(A cosθ)² = ½kA²',
      note: 'Using mω² = k, the θ-dependent terms cancel exactly, leaving a constant.',
    ),
  ],
  formulas: const [
    FormulaEntry('Restoring force', 'F = −kx'),
    FormulaEntry('Position', 'x(t) = A cos(ωt + φ)'),
    FormulaEntry('Angular frequency', 'ω = √(k/m)'),
    FormulaEntry('Period', 'T = 2π√(m/k)'),
    FormulaEntry('Maximum speed', 'v_max = Aω', condition: 'at x = 0'),
    FormulaEntry('Maximum acceleration', 'a_max = Aω²', condition: 'at x = ±A'),
    FormulaEntry('Total energy', 'E = ½kA² = ½mω²A²'),
    FormulaEntry('KE and PE at displacement x', 'KE = ½k(A²−x²),  PE = ½kx²'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For a body executing SHM, the restoring force is:',
      options: [
        'Constant in magnitude and direction',
        'Proportional to displacement and directed toward equilibrium',
        'Proportional to velocity',
        'Independent of displacement',
      ],
      correctIndex: 1,
      solution: 'SHM is defined by F = −kx: force proportional to displacement, always pointing back to equilibrium.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A mass-spring system has period T. If the amplitude is doubled, the new period is:',
      options: ['T/2', 'T', '2T', '4T'],
      correctIndex: 1,
      solution: 'T = 2π√(m/k) has no dependence on amplitude — period is unchanged.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A 2 kg mass on a spring of force constant 8 N/m oscillates in SHM. Its angular frequency is:',
      options: ['2 rad/s', '4 rad/s', '0.5 rad/s', '16 rad/s'],
      correctIndex: 0,
      solution: 'ω = √(k/m) = √(8/2) = √4 = 2 rad/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In SHM, at the mean (equilibrium) position:',
      options: [
        'Velocity is zero, acceleration is maximum',
        'Velocity is maximum, acceleration is zero',
        'Both velocity and acceleration are maximum',
        'Both velocity and acceleration are zero',
      ],
      correctIndex: 1,
      solution: 'At x = 0, restoring force (and hence acceleration = −ω²x) is zero, while speed is maximum since all energy is kinetic.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A particle in SHM has amplitude A. At what displacement is its kinetic energy equal to its potential energy?',
      options: ['A/4', 'A/2', 'A/√2', 'A'],
      correctIndex: 2,
      solution:
          'KE = PE means ½k(A²−x²) = ½kx² → A² − x² = x² → x² = A²/2 → x = A/√2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'If the spring constant of a spring-mass oscillator is quadrupled while mass stays the same, the new period compared to the original T is:',
      options: ['4T', '2T', 'T/2', 'T/4'],
      correctIndex: 2,
      solution: 'T ∝ 1/√k. Quadrupling k gives new T = T/√4 = T/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A particle executes SHM with amplitude 5 cm and period 4 s. Its maximum speed is:',
      options: ['2.5π cm/s', '5π cm/s', '10π cm/s', '2π cm/s'],
      correctIndex: 0,
      solution:
          'ω = 2π/T = 2π/4 = π/2 rad/s. v_max = Aω = 5 × π/2 = 2.5π cm/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two identical springs of constant k each support the same mass m independently. If instead they are connected in series to support mass m, the new angular frequency compared to the original single-spring ω is:',
      options: ['ω/√2', 'ω√2', 'ω', '2ω'],
      correctIndex: 0,
      solution:
          'Series combination: 1/k_eq = 1/k + 1/k = 2/k → k_eq = k/2. New ω\' = √(k_eq/m) = √(k/2m) = ω/√2.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'The total energy of a particle in SHM is E. When its displacement is half the amplitude, its kinetic energy is:',
      options: ['E/2', 'E/4', '3E/4', 'E'],
      correctIndex: 2,
      solution:
          'PE = ½kx² = ½k(A/2)² = (1/4)(½kA²) = E/4. So KE = E − E/4 = 3E/4.',
    ),
  ],
  revision: [
    'SHM is defined by F = −kx: restoring force proportional to displacement, directed toward equilibrium.',
    'x(t) = A cos(ωt+φ), ω = √(k/m), T = 2π√(m/k) — period never depends on amplitude.',
    'Speed is maximum at the centre (v_max = Aω); acceleration is maximum at the extremes (a_max = Aω²).',
    'Total energy E = ½kA² is conserved — KE and PE continuously trade off.',
    'KE = ½k(A²−x²) and PE = ½kx²; they are equal at x = A/√2.',
    'a = −ω²x is the SHM signature — spotting this form instantly gives you ω.',
  ],
  sandboxBuilder: (_) => const OscillationsWavesSimulator(),
);
