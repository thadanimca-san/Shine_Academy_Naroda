import '../../models/lesson.dart';
import '../../simulators/pendulum_energy_sim.dart';
import '../../theme/tokens.dart';

/// Pendulum Energy — the endless trade between height and speed in a swing.
final Lesson pendulumEnergyLesson = Lesson(
  topicId: 'pendulum-energy',
  title: 'Pendulum Energy',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A playground swing set with a light child and a heavy adult, pulled back to the exact same angle and released together, complete each full swing in almost identical time. But which one is moving faster at the bottom of the arc?',
  whyItMatters:
      'The pendulum is the cleanest real-world demonstration of energy conservation you can hold in your hands — it converts smoothly and repeatedly between kinetic and potential energy every single swing, with almost nothing else going on. It is a favourite NEET/JEE setting for energy-conservation numericals precisely because the geometry (height in terms of angle) adds one clean extra step beyond a simple free fall, and it is the doorway into simple harmonic motion, covered separately.',
  prediction: const PredictionPrompt(
    scenario:
        'A pendulum bob is pulled to one side through angle θ and released from rest. Compare the speed of a light bob and a heavy bob, both released from the SAME angle θ on strings of the SAME length:',
    options: [
      'The heavy bob is faster — more mass means more energy',
      'The light bob is faster — less mass is easier to accelerate',
      'Both reach exactly the same speed at the bottom',
      'It depends on the string material',
    ],
    correctIndex: 2,
    reveal:
        'Speed at the bottom is v = √(2gL(1−cosθ)) — mass cancels out completely, exactly as it does in free fall. In the lab, swap the bob mass and keep the release angle fixed: the speed readout at the bottom stays identical, even though the heavier bob clearly carries more kinetic ENERGY (½mv² scales with mass even though v does not).',
  ),
  experiments: [
    'Release the bob from different angles and watch speed at the bottom grow with the height dropped',
    'Change the bob\'s mass and confirm the speed at the bottom is unchanged (mass cancels)',
    'Pause the swing partway and read off KE and PE — verify they sum to the release-height PE',
    'Change the string length L and observe the period changes, but max speed (for fixed θ) does not',
    'Turn on damping (air resistance) and watch the amplitude shrink swing after swing',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A simple pendulum is a bob on a string swinging under gravity. As it swings, it continuously trades potential energy (height above the lowest point) for kinetic energy (speed), and back again — with the total mechanical energy staying constant if we ignore air resistance and friction at the pivot.',
      title: 'A pendulum is a KE ↔ PE machine',
    ),
    ContentBlock.paragraph(
      'When the string is pulled to an angle θ from the vertical, the bob rises a height h above its lowest point. Using basic geometry, that height is h = L(1 − cosθ), where L is the string length — the bob is L below the pivot at the lowest point, and Lcosθ below the pivot at angle θ, so the difference is the rise.',
      title: 'Height in terms of the swing angle',
    ),
    ContentBlock.formula('h = L(1 − cosθ)', title: 'HEIGHT RISEN AT ANGLE θ'),
    ContentBlock.formula(
      'v = √(2gL(1 − cosθ))',
      title: 'SPEED AT THE BOTTOM OF THE SWING',
    ),
    ContentBlock.bullets([
      'At the extreme angle (turning point), v = 0 and PE is maximum — all energy is potential',
      'At the lowest point of the swing, PE (taken as zero there) is minimum and KE is maximum',
      'Speed at the bottom depends only on L and θ (through h) — never on the mass of the bob',
      'The bob\'s speed at ANY angle φ between 0 and θ: v = √(2gL(cosφ − cosθ))',
    ]),
    ContentBlock.realLife(
      'A wrecking ball is essentially a giant pendulum: it is winched up to a height (given PE), then released to swing down and smash into a wall at the bottom, where all that PE has become KE. Engineers calculate the impact speed using exactly v = √(2gh), the same formula behind the everyday playground swing.',
    ),
    ContentBlock.realLife(
      'The reason a swing set feels like it "settles" over minutes if nobody pumps it is damping — air resistance and friction at the pivot slowly bleed away mechanical energy each cycle, shrinking the amplitude, until the swing eventually hangs still. A frictionless pendulum, if such a thing existed, would swing forever.',
    ),
    ContentBlock.mistake(
      'Using h = L·sinθ instead of h = L(1 − cosθ). The sine gives the HORIZONTAL displacement of the bob from the vertical, not the height it has risen. The vertical rise — the quantity that matters for gravitational PE — always uses (1 − cosθ).',
    ),
    ContentBlock.mistake(
      'Assuming amplitude affects the pendulum\'s period the same way it affects its speed. A larger swing angle does give a higher speed at the bottom (more height dropped), but for SMALL angles the period T = 2π√(L/g) stays essentially independent of amplitude — a subtlety of simple harmonic motion covered in its own lesson.',
    ),
    ContentBlock.example(
      'A pendulum of length 1 m is released from rest at 60° from the vertical. Find its speed at the lowest point (g = 10 m/s²).\n\nh = L(1 − cosθ) = 1×(1 − cos60°) = 1×(1 − 0.5) = 0.5 m\n\nv = √(2gh) = √(2×10×0.5) = √10 ≈ 3.16 m/s.',
    ),
    ContentBlock.jeeTip(
      'For the bob at an intermediate angle φ (between the release angle θ and the bottom), use v² = 2gL(cosφ − cosθ) directly — this single formula (derived from energy conservation between the release point and angle φ) replaces having to redo the whole derivation for every sub-question about tension or speed at an arbitrary point of the swing.',
    ),
    ContentBlock.jeeTip(
      'A classic JEE combination: find the tension in the string at the lowest point. Use energy conservation to get v at the bottom, then apply Newton\'s second law for circular motion: T − mg = mv²/L, so T = mg + mv²/L = mg[1 + 2(1−cosθ)] = mg(3 − 2cosθ).',
    ),
    ContentBlock.neetNote(
      'NEET often asks for the ratio of KE to PE at a given angle during the swing, or the speed at the bottom for a given release angle — always reach first for v² = 2gL(1 − cosθ) rather than trying to use the equations of motion, since the motion along a circular arc is not uniformly accelerated in the way straight-line kinematics assumes.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the geometry of the swing',
      math:
          'Height of bob below pivot at angle θ: L·cosθ\nHeight of bob below pivot at bottom: L',
      note:
          'The bob rises h = L − L·cosθ = L(1 − cosθ) when pulled from the bottom to angle θ.',
    ),
    DerivationStep(
      title:
          'Take the lowest point of the swing as the PE reference (PE = 0 there)',
      math: 'PE at angle θ = mgh = mgL(1 − cosθ)',
      note:
          'At the extreme angle the bob is momentarily at rest, so all its energy there is this PE.',
    ),
    DerivationStep(
      title:
          'Apply conservation of mechanical energy between release and the bottom',
      math: 'KE_bottom + PE_bottom = KE_release + PE_release',
      note:
          'KE_release = 0 (released from rest); PE_bottom = 0 (our reference level).',
    ),
    DerivationStep(
      title: 'Substitute the known terms',
      math: '½mv² + 0 = 0 + mgL(1 − cosθ)',
    ),
    DerivationStep(
      title: 'Solve for the speed at the bottom',
      math: 'v² = 2gL(1 − cosθ)   →   v = √(2gL(1 − cosθ))',
      note:
          'Mass cancels — just like every free-fall speed formula, because both KE and PE are proportional to mass.',
    ),
  ],
  formulas: const [
    FormulaEntry('Height risen at angle θ', 'h = L(1 − cosθ)'),
    FormulaEntry(
      'Speed at the bottom',
      'v = √(2gL(1 − cosθ))',
      condition: 'released from rest at angle θ',
    ),
    FormulaEntry(
      'Speed at intermediate angle φ',
      'v = √(2gL(cosφ − cosθ))',
      condition: '0 ≤ φ ≤ θ',
    ),
    FormulaEntry('Tension at the lowest point', 'T = mg(3 − 2cosθ)'),
    FormulaEntry(
      'Period (small oscillations)',
      'T_period = 2π√(L/g)',
      condition: 'θ small, independent of mass and amplitude',
    ),
    FormulaEntry(
      'Mechanical energy (any point)',
      'E = ½mv² + mgh = mgL(1 − cosθ)',
      condition: 'constant, undamped',
    ),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A pendulum bob is at the extreme point of its swing (maximum angle). At this instant:',
      options: [
        'KE is maximum, PE is zero',
        'KE is zero, PE is maximum',
        'Both KE and PE are zero',
        'KE equals PE',
      ],
      correctIndex: 1,
      solution:
          'At the extreme point the bob is momentarily at rest (v = 0, so KE = 0), and it is at its highest point, so PE is maximum.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'The height risen by a pendulum bob of length L when pulled to angle θ from the vertical is:',
      options: ['L sinθ', 'L(1 − cosθ)', 'L cosθ', 'L(1 + cosθ)'],
      correctIndex: 1,
      solution:
          'h = L − Lcosθ = L(1 − cosθ), the vertical rise above the lowest point.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A pendulum of length 0.8 m is released from rest at 90° to the vertical. Its speed at the lowest point is (g = 10 m/s²):',
      options: ['2 m/s', '4 m/s', '3 m/s', '5 m/s'],
      correctIndex: 1,
      solution:
          'h = L(1 − cos90°) = 0.8×(1 − 0) = 0.8 m. v = √(2gh) = √(2×10×0.8) = √16 = 4 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'Two pendulum bobs of masses m and 2m, released from the same angle on strings of equal length, arrive at the bottom with speeds v₁ and v₂. Then:',
      options: ['v₂ = 2v₁', 'v₂ = √2·v₁', 'v₁ = v₂', 'v₂ = v₁/2'],
      correctIndex: 2,
      solution:
          'v = √(2gL(1−cosθ)) does not contain mass at all — mass cancels in the energy equation, so v₁ = v₂.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A pendulum released from angle θ has speed v at the bottom. To double this speed (same length L), the release angle must satisfy:',
      options: [
        '1 − cosθ_new = 4(1 − cosθ)',
        '1 − cosθ_new = 2(1 − cosθ)',
        'θ_new = 2θ',
        '1 − cosθ_new = √2(1 − cosθ)',
      ],
      correctIndex: 0,
      solution:
          'v² ∝ (1 − cosθ). To get (2v)² = 4v², need (1 − cosθ_new) = 4(1 − cosθ).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A pendulum bob of mass m and string length L is released from angle θ. The tension in the string at the lowest point is:',
      options: ['mg', 'mg(3 − 2cosθ)', 'mg(1 − cosθ)', 'mgcosθ'],
      correctIndex: 1,
      solution:
          'At the bottom, T − mg = mv²/L with v² = 2gL(1−cosθ), giving T = mg + 2mg(1−cosθ) = mg(3 − 2cosθ).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A pendulum of length L is released from angle θ = 60°. Its speed when the string makes 30° with the vertical is:',
      options: [
        '√(2gL(cos30° − cos60°))',
        '√(2gL(cos60° − cos30°))',
        '√(2gLcos30°)',
        '√(gL)',
      ],
      correctIndex: 0,
      solution:
          'Using v² = 2gL(cosφ − cosθ) with φ = 30° (closer to bottom, so cosφ > cosθ): v = √(2gL(cos30° − cos60°)), a positive quantity since cos30° > cos60°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A damped pendulum loses 10% of its mechanical energy on each full swing. If it starts with energy E₀, its energy after 2 complete swings is:',
      options: ['0.90E₀', '0.81E₀', '0.80E₀', '0.99E₀'],
      correctIndex: 1,
      solution:
          'Each swing retains 90% of the previous energy (multiplicative, not additive loss): E₂ = E₀×(0.9)² = 0.81E₀.',
    ),
  ],
  revision: [
    'Height risen at angle θ: h = L(1 − cosθ) — NOT L·sinθ (that\'s horizontal displacement).',
    'Speed at the bottom: v = √(2gL(1 − cosθ)) — mass cancels, just like free fall.',
    'Speed at any intermediate angle φ ≤ θ: v = √(2gL(cosφ − cosθ)).',
    'Tension at the lowest point: T = mg(3 − 2cosθ), always greater than mg.',
    'For small angles the period T = 2π√(L/g) is independent of both mass and amplitude.',
    'Real pendulums lose energy each swing to air resistance and pivot friction (damping) — amplitude shrinks over time even though the period barely changes.',
    'At the extreme point: KE = 0, PE = max. At the lowest point: PE = 0 (by convention), KE = max.',
  ],
  sandboxBuilder: (_) => const PendulumEnergySimulator(),
);
