import '../../models/lesson.dart';
import '../../simulators/work_energy_theorem_sim.dart';
import '../../theme/tokens.dart';

/// Work-Energy Theorem — connecting force, distance, and the change in a body's kinetic energy.
final Lesson workEnergyTheoremLesson = Lesson(
  topicId: 'work-energy-theorem',
  title: 'Work–Energy Theorem',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'You push a stalled car for 10 m and it barely creeps forward. A friend pushes twice as hard over the same 10 m and it ends up rolling much faster than double your speed. Why does doubling the force do more than just double the final speed?',
  whyItMatters:
      'The work-energy theorem is the bridge between forces (Newton\'s world) and energy (the conservation world) — it is literally F = ma rewritten so distance and speed appear instead of acceleration and time. It lets you solve problems where the force changes with position — springs, varying friction, electric fields — problems the equations of motion cannot touch. It shows up constantly in JEE as "area under an F-x graph" and in NEET as quick numerical work-KE questions.',
  prediction: const PredictionPrompt(
    scenario:
        'A block starts at rest. A constant force F pushes it through a distance d, giving it final kinetic energy K. If the SAME force instead pushes the block through distance 2d, the final kinetic energy is:',
    options: [
      'K (kinetic energy depends only on force, not distance)',
      '2K (double the distance, double the energy)',
      '4K (kinetic energy depends on distance squared)',
      '√2·K',
    ],
    correctIndex: 1,
    reveal:
        'Work = F·d, and the work-energy theorem says that work equals the change in kinetic energy directly — so doubling the distance the force acts over exactly doubles the KE gained, not the speed. (Speed only grows by √2, since KE ∝ v².) In the lab, keep the force fixed and stretch the push distance — watch the KE readout scale linearly with distance while the speed readout grows more slowly.',
  ),
  experiments: [
    'Apply a constant force over increasing distance and watch KE grow in direct proportion to distance',
    'Switch to a spring-like variable force and see the "area under F-x" match the KE gained exactly',
    'Push in the direction of motion, then reverse it — watch KE decrease as work turns negative',
    'Turn on friction and watch part of your work vanish as heat instead of becoming KE',
    'Apply a force perpendicular to motion and confirm it does zero work — KE stays unchanged',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Work is done whenever a force causes displacement in its own direction. For a constant force, work is simply the force component along the motion times the distance moved. Work is a scalar — it has no direction of its own — and it can be positive, negative, or zero depending on the angle between force and displacement.',
      title: 'What "work" means in physics',
    ),
    ContentBlock.formula(
      'W = F·d·cosθ',
      title: 'WORK DONE BY A CONSTANT FORCE',
    ),
    ContentBlock.paragraph(
      'The work-energy theorem states that the total (net) work done on an object by all forces equals the change in its kinetic energy. It is not a new law — it falls straight out of Newton\'s second law — but it is far more convenient whenever you know forces and distances and don\'t care about time.',
      title: 'The work-energy theorem',
    ),
    ContentBlock.formula(
      'W_net = ΔKE = ½mv² − ½mu²',
      title: 'WORK-ENERGY THEOREM',
    ),
    ContentBlock.bullets([
      'θ < 90°: work is positive — the force speeds the object up',
      'θ = 90°: work is zero — the force does nothing to the speed (e.g. gravity on a satellite in circular orbit)',
      'θ > 90°: work is negative — the force slows the object down (e.g. friction, braking, air drag)',
      'When force varies with position, W = ∫F·dx = area under the F–x graph',
    ]),
    ContentBlock.realLife(
      'Friction always does negative work on a moving object because it points opposite to velocity — this is precisely why a sliding box eventually stops: friction keeps removing kinetic energy until KE (and hence v) reaches zero. The work-energy theorem quantifies exactly how far it slides before stopping.',
    ),
    ContentBlock.realLife(
      'A car engine does work against air resistance and rolling friction at highway speed just to maintain a constant KE (zero net change) — this is why cars need continuous fuel even when "not accelerating": the engine\'s positive work exactly cancels the negative work of drag forces.',
    ),
    ContentBlock.mistake(
      'Confusing work done by ONE force with the NET work. The work-energy theorem uses W_net — the work of every force acting, added together (with correct signs) — not just the force you happen to be interested in. If gravity, normal force, and friction all act, sum all three works before equating to ΔKE.',
    ),
    ContentBlock.mistake(
      'Forgetting the cosθ factor, or worse, forgetting that a force perpendicular to displacement does ZERO work. Common trap: the normal force on a block sliding on a horizontal floor does no work at all, because it is always perpendicular to the motion — students sometimes wrongly include it in energy calculations.',
    ),
    ContentBlock.example(
      'A 3 kg block, initially at rest, is pushed by a horizontal force of 12 N across a rough floor (friction force 4 N) for a distance of 5 m. Find its final speed.\n\nW_net = (F_applied − f_friction)·d = (12 − 4)×5 = 40 J\nW_net = ΔKE = ½mv² − 0\n40 = ½×3×v²\nv² = 80/3 = 26.67\nv ≈ 5.16 m/s.',
    ),
    ContentBlock.jeeTip(
      'For a variable force F(x), work is the integral W = ∫F dx, which geometrically is the AREA under the F versus x graph — including sign: area above the x-axis is positive work, area below is negative. This turns many "hard" calculus problems into simple triangle/trapezoid area calculations when F(x) is given as a graph.',
    ),
    ContentBlock.jeeTip(
      'For a spring force F = −kx (Hooke\'s law), the work done BY you to stretch it from 0 to x is W = ∫₀ˣ kx dx = ½kx² — matching spring PE exactly. This is the direct algebraic link between the work-energy theorem and the potential-energy formula used in conservation problems.',
    ),
    ContentBlock.neetNote(
      'NEET often tests the sign of work in one-line conceptual questions: work done by gravity on a ball thrown upward is negative on the way up (force down, displacement up) and positive on the way down. Work done by tension in a swinging pendulum is always zero, since tension is always perpendicular to the bob\'s velocity.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Newton\'s second law',
      math: 'F_net = m·a',
      note:
          'a is the acceleration produced by the net force along the direction of motion.',
    ),
    DerivationStep(
      title: 'Use the kinematic identity v·dv = a·dx',
      math: 'a = v·(dv/dx)',
      note:
          'This comes from a = dv/dt = (dv/dx)(dx/dt) = v·dv/dx — the chain rule in disguise.',
    ),
    DerivationStep(
      title: 'Substitute into Newton\'s second law and separate variables',
      math: 'F_net = m·v·(dv/dx)   →   F_net·dx = m·v·dv',
    ),
    DerivationStep(
      title: 'Integrate both sides from the initial to final state',
      math: '∫ F_net·dx = m·∫ᵤᵛ v·dv = m·[v²/2]ᵤᵛ',
      note: 'The left side is, by definition, the net work done, W_net.',
    ),
    DerivationStep(
      title: 'Evaluate the integral',
      math: 'W_net = ½mv² − ½mu² = ΔKE',
      note:
          'Work-energy theorem: net work always equals the change in kinetic energy, for ANY force pattern — constant or variable.',
    ),
  ],
  formulas: const [
    FormulaEntry('Work by a constant force', 'W = F·d·cosθ'),
    FormulaEntry('Work-energy theorem', 'W_net = ΔKE = ½mv² − ½mu²'),
    FormulaEntry(
      'Work by a variable force',
      'W = ∫F dx',
      condition: 'area under F–x graph',
    ),
    FormulaEntry(
      'Work done stretching a spring',
      'W = ½kx²',
      condition: 'from natural length',
    ),
    FormulaEntry(
      'Work by friction',
      'W_friction = −f·d',
      condition: 'f = friction force, always opposes motion',
    ),
    FormulaEntry('Power (rate of work)', 'P = W/t = F·v·cosθ'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A force of 10 N acts on a block through a displacement of 4 m in the same direction. The work done is:',
      options: ['2.5 J', '14 J', '40 J', '6 J'],
      correctIndex: 2,
      solution: 'W = F·d·cosθ = 10×4×cos0° = 40 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A coolie carries a load horizontally while walking at constant speed. The work done by the coolie on the load is:',
      options: ['Positive', 'Negative', 'Zero', 'Cannot be determined'],
      correctIndex: 2,
      solution:
          'The lifting force (upward) is perpendicular to the horizontal displacement, so θ = 90° and W = F·d·cos90° = 0.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A 2 kg block moving at 3 m/s is acted on by a net force that does 16 J of work on it. Its final speed is:',
      options: ['4 m/s', '5 m/s', '6.5 m/s', '8 m/s'],
      correctIndex: 1,
      solution:
          'W_net = ΔKE: 16 = ½×2×v² − ½×2×3² = v² − 9 → v² = 25 → v = 5 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A body of mass m moving with speed v is stopped by a constant retarding force F over a distance d. Which relation is correct?',
      options: ['F = mv²/d', 'F = mv²/(2d)', 'F = 2mv/d', 'F = mv/d²'],
      correctIndex: 1,
      solution:
          'Work-energy theorem: −F·d = 0 − ½mv² → F·d = ½mv² → F = mv²/(2d).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'The F–x graph for a force acting on a 1 kg object (starting from rest) is a straight line from (0, 0) to (4 m, 4 N). The speed of the object at x = 4 m is:',
      options: ['2 m/s', '4 m/s', '6 m/s', '16 m/s'],
      correctIndex: 1,
      solution:
          'W = area under F-x graph = ½×4×4 = 8 J. W = ΔKE = ½×1×v² → v² = 16 → v = 4 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A spring of constant k = 200 N/m is stretched from x = 0 to x = 0.1 m. The work done in stretching it is:',
      options: ['1 J', '2 J', '10 J', '20 J'],
      correctIndex: 0,
      solution: 'W = ½kx² = ½×200×(0.1)² = ½×200×0.01 = 1 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A block of mass m slides down a rough incline of angle θ and length L, starting from rest. If the coefficient of kinetic friction is μ, the speed at the bottom (using the work-energy theorem) is:',
      options: [
        'v = √(2gL(sinθ − μcosθ))',
        'v = √(2gL sinθ)',
        'v = √(2gLμcosθ)',
        'v = √(2gL(sinθ + μcosθ))',
      ],
      correctIndex: 0,
      solution:
          'W_net = W_gravity + W_friction = mgLsinθ − μmgcosθ·L = mgL(sinθ − μcosθ). Set equal to ½mv² − 0 and solve: v = √(2gL(sinθ − μcosθ)).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A variable force F = (3x² + 2x) N acts on a 1 kg object along the x-axis. The work done as it moves from x = 0 to x = 2 m equals its gain in KE. This work is:',
      options: ['12 J', '16 J', '8 J', '20 J'],
      correctIndex: 0,
      solution:
          'W = ∫₀² (3x² + 2x) dx = [x³ + x²]₀² = (8 + 4) − 0 = 12 J. By the work-energy theorem this equals ΔKE.',
    ),
  ],
  revision: [
    'W = F·d·cosθ for a constant force; sign depends entirely on the angle between F and displacement.',
    'Work-energy theorem: W_net = ΔKE — true for constant OR variable forces.',
    'A force perpendicular to motion (like normal force, or tension in circular motion) does zero work.',
    'For variable forces, W = ∫F dx = area under the F–x graph (respecting sign above/below the axis).',
    'Friction and drag always do negative work on the moving object, converting KE to heat.',
    'Stretching a spring by x does work W = ½kx² — matches spring PE exactly.',
    'Use W_net, the sum of ALL forces\' work — not just one force — when applying the theorem.',
  ],
  sandboxBuilder: (_) => const WorkEnergyTheoremSimulator(),
);
