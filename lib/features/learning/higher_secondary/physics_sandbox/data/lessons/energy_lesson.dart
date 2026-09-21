import '../../models/lesson.dart';
import '../../simulators/energy_sim.dart';
import '../../theme/tokens.dart';

/// Energy Transformations — kinetic, potential, and the constant total that ties them together.
final Lesson energyTransformationsLesson = Lesson(
  topicId: 'energy-transformations',
  title: 'Energy Transformations',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A roller coaster car is hauled to the top of the first hill by a motor, then the motor lets go completely — no engine, no push, for the rest of the ride. How does it still manage to fly through loops and climb smaller hills further down the track?',
  whyItMatters:
      'Energy conservation is the single most powerful shortcut in mechanics — it lets you find speeds and heights without ever touching Newton\'s laws or kinematics equations. Every NEET and JEE paper leans on KE + PE = constant to solve pendulum, roller-coaster, spring, and projectile problems in three lines instead of thirty. It is also the conceptual seed for work, power, and later, energy in electric and atomic systems.',
  prediction: const PredictionPrompt(
    scenario:
        'A ball is released from rest at the top of a frictionless track and slides down to the bottom, height h below the start. Its speed at the bottom depends on:',
    options: [
      'Only its mass — heavier balls arrive faster',
      'Only the height h dropped, not the shape of the track',
      'The exact shape of the track — a steeper path gives a higher final speed',
      'Both the mass and the shape of the track',
    ],
    correctIndex: 1,
    reveal:
        'Speed at the bottom depends ONLY on the height dropped: v = √(2gh), completely independent of mass and of whether the track is straight, curved, or a rollercoaster loop. In the lab, change the track shape or the falling mass and watch the final speed readout stay locked to h — because gravity does the same work mgh regardless of the path, and all of it converts to KE.',
  ),
  experiments: [
    'Drop the object from different heights and watch KE grow while PE shrinks — their sum stays flat',
    'Switch on friction and watch the total energy line slowly droop as heat is generated',
    'Compress the spring different amounts and watch spring PE convert entirely into KE on release',
    'Pause mid-fall and read off KE and PE separately — verify they add up to the starting PE',
    'Try a very steep vs very shallow frictionless ramp of the same height — same final speed either way',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Energy is the capacity to do work, and mechanical energy comes in two everyday forms. Kinetic energy (KE) is the energy of motion — anything moving has it. Potential energy (PE) is stored energy due to position — height in a gravitational field, or compression/stretch in a spring. A system\'s total mechanical energy is the sum of the two.',
      title: 'Two faces of mechanical energy',
    ),
    ContentBlock.formula('KE = ½mv²', title: 'KINETIC ENERGY'),
    ContentBlock.formula(
      'PE_gravity = mgh,   PE_spring = ½kx²',
      title: 'POTENTIAL ENERGY',
    ),
    ContentBlock.paragraph(
      'The law of conservation of energy says energy is never created or destroyed, only converted from one form to another. In a mechanical system with no friction or air resistance, the total mechanical energy (KE + PE) stays exactly constant — as one form shrinks, the other grows by precisely the same amount.',
      title: 'Conservation of mechanical energy',
    ),
    ContentBlock.formula(
      'KE + PE = constant   (no friction/air resistance)',
      title: 'CONSERVATION OF MECHANICAL ENERGY',
    ),
    ContentBlock.bullets([
      'At the highest point of a swing or throw, KE is minimum and PE is maximum',
      'At the lowest point, PE is minimum (often zero) and KE is maximum',
      'Total energy at any two points is equal: KE₁ + PE₁ = KE₂ + PE₂',
      'Friction, air drag, and sound do NOT destroy energy — they convert it to heat, which mechanical-energy bookkeeping does not track',
    ]),
    ContentBlock.realLife(
      'A roller coaster is a pure demonstration of energy conversion: the motor only ever lifts the car up the very first hill, giving it a large store of gravitational PE. Every hill after that is shorter than the first because some energy is always lost to friction and air resistance along the way — the car can never climb back to its starting height.',
    ),
    ContentBlock.realLife(
      'A pendulum bob released from one side swings through the bottom (all KE, zero PE relative to the bottom) and rises to almost the same height on the other side (all PE again) — "almost" because a little energy leaks out to air resistance and pivot friction on every swing, which is why a pendulum eventually stops.',
    ),
    ContentBlock.mistake(
      'Forgetting that PE is measured relative to a chosen reference level. PE = mgh only tells you the CHANGE in potential energy between two heights — you are always free to call any convenient height "h = 0". What matters in every conservation equation is the DIFFERENCE in PE, not its absolute value.',
    ),
    ContentBlock.mistake(
      'Assuming energy conservation still holds once friction, air resistance, or an external push/pull is present. The moment a non-conservative force acts, KE + PE is no longer constant — you must add a "energy lost to friction = work done against friction" term, or switch to the work-energy theorem instead.',
    ),
    ContentBlock.example(
      'A 2 kg ball is dropped from a height of 5 m. Find its speed just before hitting the ground (ignore air resistance, g = 10 m/s²).\n\nEnergy conservation: PE_top = KE_bottom (taking the ground as h = 0)\nmgh = ½mv²\ngh = ½v²\nv² = 2gh = 2×10×5 = 100\nv = 10 m/s.\n\nNotice the mass cancelled out — as always in free fall.',
    ),
    ContentBlock.jeeTip(
      'For a spring-block system, treat spring PE just like gravitational PE in the conservation equation: ½kx₁² + ½mv₁² = ½kx₂² + ½mv₂². A common JEE trap combines gravity AND a spring in one problem (a block sliding down and compressing a spring) — write ONE energy equation with all three terms (initial KE, PE lost in height, PE gained in spring) rather than solving it in stages.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the ratio of KE to PE at a fractional height. If a ball falls from height H, at height h above the ground its PE = mgh and its KE = mg(H−h) — because the energy already converted from PE is exactly mg(H−h). Learn to read off both quantities at any point of the fall without recomputing from scratch.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from work done by gravity as a ball falls height h',
      math: 'W_gravity = F·d = mg·h',
      note:
          'Force of gravity mg acts through displacement h, doing positive work.',
    ),
    DerivationStep(
      title: 'Apply the work-energy theorem',
      math: 'W_net = ΔKE = KE_final − KE_initial',
      note:
          'With no friction, gravity is the only force doing work, so W_gravity = ΔKE.',
    ),
    DerivationStep(
      title: 'Substitute for a ball starting from rest',
      math: 'mgh = ½mv² − 0',
    ),
    DerivationStep(
      title: 'Solve for the final speed',
      math: 'v² = 2gh   →   v = √(2gh)',
      note:
          'PE lost (mgh) has become exactly the KE gained (½mv²) — energy converted, not created.',
    ),
    DerivationStep(
      title: 'Generalise to any two points 1 and 2 on a frictionless path',
      math: '½mv₁² + mgh₁ = ½mv₂² + mgh₂',
      note:
          'This is conservation of mechanical energy — true for any path shape, not just a straight fall.',
    ),
  ],
  formulas: const [
    FormulaEntry('Kinetic energy', 'KE = ½mv²'),
    FormulaEntry(
      'Gravitational PE',
      'PE = mgh',
      condition: 'h measured from a chosen reference',
    ),
    FormulaEntry(
      'Spring PE',
      'PE_spring = ½kx²',
      condition: 'x = compression or extension',
    ),
    FormulaEntry(
      'Conservation of mechanical energy',
      'KE₁ + PE₁ = KE₂ + PE₂',
      condition: 'no friction/drag',
    ),
    FormulaEntry(
      'Speed after falling height h',
      'v = √(2gh)',
      condition: 'released from rest',
    ),
    FormulaEntry('Energy lost to friction', 'ΔE = W_friction = f·d'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A 1 kg object moving at 4 m/s has kinetic energy:',
      options: ['4 J', '8 J', '16 J', '2 J'],
      correctIndex: 1,
      solution: 'KE = ½mv² = ½×1×4² = ½×16 = 8 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A ball is thrown straight up. At the highest point, its:',
      options: [
        'KE is maximum, PE is zero',
        'KE is zero, PE is maximum',
        'Both KE and PE are zero',
        'Both KE and PE are maximum',
      ],
      correctIndex: 1,
      solution:
          'At the highest point, vertical velocity momentarily becomes zero, so KE = 0. All the initial KE has converted to PE, which is at its maximum for that throw.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A body falls freely from a height of 20 m. Its speed just before hitting the ground is (g = 10 m/s²):',
      options: ['10 m/s', '20 m/s', '15 m/s', '5 m/s'],
      correctIndex: 1,
      solution: 'v = √(2gh) = √(2×10×20) = √400 = 20 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A ball falls from height H. At a height h above the ground (h < H), the ratio of its KE to PE is:',
      options: ['h/(H−h)', '(H−h)/h', 'H/h', 'h/H'],
      correctIndex: 1,
      solution:
          'PE at height h = mgh. KE at that point = energy already converted = mg(H−h). Ratio KE/PE = (H−h)/h.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A block compresses a spring of constant k by x from rest, then the spring pushes it back. The block\'s speed when the spring returns to natural length is v. If the compression is doubled to 2x, the new speed is:',
      options: ['v', '2v', '4v', '√2·v'],
      correctIndex: 1,
      solution:
          'Spring PE ½kx² converts entirely to KE ½mv²: v = x√(k/m), so v ∝ x. Doubling x doubles v.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A pendulum bob is released from a height h above its lowest point. If 20% of the mechanical energy is lost to air resistance by the time it reaches the bottom, its speed at the bottom is:',
      options: ['√(2gh)', '√(1.6gh)', '0.8·√(2gh)', '√(0.8·2gh)'],
      correctIndex: 3,
      solution:
          'Only 80% of mgh converts to KE: 0.8mgh = ½mv² → v = √(1.6gh) = √(0.8×2gh). Options (b) and (d) are algebraically the same value — always compute the number, not just the form.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A block slides down a frictionless incline of height h and then compresses a spring (constant k) on a frictionless horizontal surface at the bottom. The maximum compression of the spring is:',
      options: ['√(2mgh/k)', '√(mgh/k)', '2mgh/k', 'mgh/k'],
      correctIndex: 0,
      solution:
          'All PE converts first to KE, then to spring PE at maximum compression (v = 0 momentarily): mgh = ½kx_max² → x_max = √(2mgh/k).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A roller coaster car (frictionless track) must maintain contact at the top of a circular loop of radius r. The minimum height above the loop\'s top from which it must be released, using energy conservation combined with the minimum-speed condition at the top, corresponds to a speed at the top of:',
      options: [
        'v_top = √(gr)',
        'v_top = √(2gr)',
        'v_top = √(5gr)',
        'v_top = gr',
      ],
      correctIndex: 0,
      solution:
          'At minimum speed for contact, gravity alone supplies the centripetal force: mg = mv_top²/r → v_top = √(gr). (Energy conservation is then used separately to find the release height needed to reach this speed.)',
    ),
  ],
  revision: [
    'KE = ½mv² (motion), PE = mgh (height) or ½kx² (spring stretch/compression).',
    'With no friction: KE + PE = constant — energy converts between forms, never lost.',
    'Speed after falling height h: v = √(2gh), independent of mass and of path shape.',
    'PE is always relative to a chosen zero level — only PE differences matter physically.',
    'Friction/air drag remove mechanical energy as heat; total energy (including heat) is still conserved.',
    'At the top of a swing/throw: KE is minimum; at the bottom: KE is maximum.',
    'Spring-and-gravity problems: write one combined energy equation, don\'t solve in separate stages.',
  ],
  sandboxBuilder: (_) => const EnergySimulator(),
);
