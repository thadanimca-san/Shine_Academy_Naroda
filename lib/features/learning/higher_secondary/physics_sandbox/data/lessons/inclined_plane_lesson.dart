import '../../models/lesson.dart';
import '../../simulators/inclined_plane_sim.dart';
import '../../theme/tokens.dart';

/// The Inclined Plane — resolving gravity into components, and the role of friction.
final Lesson inclinedPlaneLesson = Lesson(
  topicId: 'inclined-plane',
  title: 'Inclined Plane',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A block sits happily on a gentle ramp, but the same block placed on a steep ramp slides down immediately. What exactly changes about gravity\'s "grip" on the block as the ramp gets steeper — and is there a precise angle where it switches from staying put to sliding?',
  whyItMatters:
      'The inclined plane is the single most-tested setup in mechanics, because it forces you to resolve a vector (gravity) into two perpendicular components — a skill every later chapter (circular motion, projectile motion, banked curves) depends on. Nearly every JEE/NEET pulley, friction and Newton\'s-law question hides an incline inside it somewhere.',
  prediction: const PredictionPrompt(
    scenario:
        'A block rests on a frictionless incline that starts flat (0°) and is slowly tilted up toward vertical (90°). How does the block\'s acceleration down the slope change as the angle increases?',
    options: [
      'It stays constant at g regardless of angle',
      'It increases from 0 (at 0°) up to g (at 90°), following a sin θ pattern',
      'It decreases as the angle increases',
      'It jumps straight to g the moment the incline is tilted at all',
    ],
    correctIndex: 1,
    reveal:
        'On a frictionless incline, a = g sinθ. At θ = 0° (flat ground) a = 0; at θ = 90° (a vertical wall / free fall) a = g — the full acceleration of gravity. In the lab, drag the angle slider from 0° to 90° with friction off and watch the acceleration readout trace exactly g sinθ, smoothly connecting "no sliding" to "free fall."',
  ),
  experiments: [
    'Set friction to zero and increase the angle from 0° to 90° — watch a = g sinθ smoothly rise from 0 to g',
    'Turn friction on and find the angle at which the block just barely starts to slide — the angle of repose',
    'Set the angle below the angle of repose with friction on — confirm the block stays perfectly still',
    'Compare the normal force reading as you tilt the incline — watch N = mg cosθ shrink as θ grows',
    'Give the block an initial push UP a rough incline and watch it decelerate faster than it would sliding down',
  ],
  concept: const [
    ContentBlock.paragraph(
      'On an inclined plane, gravity mg still points straight down, but the natural directions to work in are ALONG the incline and PERPENDICULAR to it — because those are the directions in which the block can (or cannot) accelerate. Resolving mg into these two components is the single most important skill for solving incline problems.',
      title: 'Resolving gravity along the incline',
    ),
    ContentBlock.formula('Along incline: mg sinθ.     Perpendicular to incline: mg cosθ.',
        title: 'COMPONENTS OF WEIGHT ON AN INCLINE'),
    ContentBlock.bullets([
      'mg sinθ pulls the block DOWN the slope — this is the component that can cause sliding',
      'mg cosθ presses the block INTO the surface — this determines the normal force N',
      'Perpendicular to the incline, there is no acceleration (block stays on the surface): N = mg cosθ',
      'Along the incline, Newton\'s second law gives the block\'s acceleration down the slope',
    ]),
    ContentBlock.paragraph(
      'On a FRICTIONLESS incline, the only force along the slope is mg sinθ, so by Newton\'s second law the block always accelerates down at a = g sinθ — regardless of its mass, exactly like free fall does not depend on mass. This surprising angle-only dependence (no mass, no size) is a favourite exam observation.',
      title: 'Frictionless incline: a = g sinθ',
    ),
    ContentBlock.formula('a = g sinθ   (frictionless)', title: 'ACCELERATION, NO FRICTION'),
    ContentBlock.paragraph(
      'On a ROUGH incline, friction acts along the surface, opposing relative sliding. If the block is not yet moving, static friction adjusts to balance mg sinθ as long as it can — the block stays still whenever mg sinθ ≤ μs·mg cosθ, i.e., whenever tanθ ≤ μs. Beyond that angle, the block slides down with reduced acceleration a = g(sinθ − μk cosθ), because kinetic friction now opposes the motion.',
      title: 'Rough incline: the tug-of-war with friction',
    ),
    ContentBlock.formula('Stays still: tanθ ≤ μs.     Slides: a = g(sinθ − μk cosθ)  for tanθ > μs',
        title: 'CONDITION FOR SLIDING'),
    ContentBlock.realLife(
      'Ramps for wheelchairs and hand-trucks are deliberately kept at a shallow angle so that tanθ stays well below μs for the wheels — a wheelchair ramp steeper than about 5° starts to require real force to hold a chair stationary, which is exactly why building codes cap ramp angles so low.',
    ),
    ContentBlock.mistake(
      'Resolving mg along the HORIZONTAL and VERTICAL directions instead of along and perpendicular to the incline. This is not wrong in principle, but it makes the normal force direction messy and doubles the algebra. Always choose axes along and perpendicular to the incline surface for ramp problems — it makes N purely perpendicular and simplifies everything.',
    ),
    ContentBlock.mistake(
      'Using a = g sinθ even when friction is present, or forgetting to check tanθ vs μs before assuming the block moves at all. Many students jump straight to a = g(sinθ − μk cosθ) without first verifying that the block actually overcomes static friction; if tanθ ≤ μs, the correct acceleration is ZERO, not a small positive number.',
    ),
    ContentBlock.example(
      'A 4 kg block sits on a 30° rough incline with μs = 0.5, μk = 0.4 (g = 10 m/s²). Does it slide, and if so, with what acceleration?\n\nCheck: tanθ = tan30° ≈ 0.577. Since tanθ (0.577) > μs (0.5), the block DOES slide.\n\na = g(sinθ − μk cosθ) = 10×(0.5 − 0.4×0.866) = 10×(0.5 − 0.346) = 10×0.154 ≈ 1.54 m/s², directed down the incline.',
    ),
    ContentBlock.jeeTip(
      'For a block being pushed or pulled UP a rough incline, BOTH gravity\'s component (mg sinθ) and kinetic friction (μk mg cosθ) oppose the motion — they add together, giving deceleration a = g(sinθ + μk cosθ). This is why sliding up is always "harder" (more deceleration) than sliding down is "easy" — a very common JEE trap for students who reuse the down-the-incline formula for up-the-incline motion.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the acceleration or the minimum force to keep a block stationary/moving on an incline. Remember two clean special cases: frictionless incline gives a = g sinθ (independent of mass); and the angle of repose formula tanθ = μs (from the friction chapter) tells you exactly when an incline problem "switches on" sliding.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up axes along and perpendicular to the incline',
      math: 'x: along incline (positive down-slope).   y: perpendicular to incline.',
      note: 'This choice makes the normal force purely along y and simplifies the equations.',
    ),
    DerivationStep(
      title: 'Resolve the weight mg into these axes',
      math: 'Along incline: mg sinθ.   Perpendicular: mg cosθ.',
      note: 'θ is the incline angle from the horizontal; a quick sketch confirms these components via similar triangles.',
    ),
    DerivationStep(
      title: 'Apply Newton\'s second law perpendicular to the incline (no acceleration there)',
      math: 'N − mg cosθ = 0  ⟹  N = mg cosθ',
    ),
    DerivationStep(
      title: 'Apply Newton\'s second law along the incline (frictionless case)',
      math: 'mg sinθ = ma',
      note: 'Only mg sinθ acts along the slope when there is no friction.',
    ),
    DerivationStep(
      title: 'Solve for acceleration',
      math: 'a = g sinθ',
      note: 'Adding kinetic friction subtracts μk·N = μk·mg cosθ from the along-incline force: a = g(sinθ − μk cosθ).',
    ),
  ],
  formulas: const [
    FormulaEntry('Weight component along incline', 'mg sinθ'),
    FormulaEntry('Weight component perpendicular to incline', 'mg cosθ'),
    FormulaEntry('Normal force on incline', 'N = mg cosθ'),
    FormulaEntry('Acceleration, frictionless incline', 'a = g sinθ'),
    FormulaEntry('Acceleration sliding down, with friction', 'a = g(sinθ − μk cosθ)', condition: 'tanθ > μs'),
    FormulaEntry('Deceleration sliding up, with friction', 'a = g(sinθ + μk cosθ)'),
    FormulaEntry('Condition to remain stationary', 'tanθ ≤ μs'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'On a frictionless incline of angle θ, the acceleration of a block sliding down is:',
      options: ['g', 'g sinθ', 'g cosθ', 'g tanθ'],
      correctIndex: 1,
      solution: 'With no friction, only mg sinθ acts along the incline, giving a = g sinθ.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The normal force on a block of mass m resting on an incline of angle θ is:',
      options: ['mg', 'mg sinθ', 'mg cosθ', 'mg tanθ'],
      correctIndex: 2,
      solution: 'Perpendicular equilibrium gives N = mg cosθ.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A block on a frictionless 30° incline (g = 10 m/s²) has acceleration:',
      options: ['10 m/s²', '5 m/s²', '8.66 m/s²', '2.5 m/s²'],
      correctIndex: 1,
      solution: 'a = g sinθ = 10 × sin30° = 10 × 0.5 = 5 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A block remains stationary on a rough incline of angle θ as long as:',
      options: ['tanθ ≥ μs', 'tanθ ≤ μs', 'sinθ ≤ μk', 'cosθ ≤ μs'],
      correctIndex: 1,
      solution: 'The block stays put whenever gravity\'s along-incline pull does not exceed the maximum static friction: tanθ ≤ μs.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Two blocks of different masses, both released from rest on the SAME frictionless incline, reach the bottom:',
      options: [
        'The heavier one first, since it has more force',
        'The lighter one first, since it has less inertia',
        'At the same time, since a = g sinθ is independent of mass',
        'It depends on their shapes',
      ],
      correctIndex: 2,
      solution: 'a = g sinθ has no mass dependence — just like free fall, all masses accelerate identically on a frictionless incline, so both arrive together.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A 2 kg block on a 37° rough incline has μk = 0.25 (g = 10 m/s², sin37° = 0.6, cos37° = 0.8). Its acceleration while sliding down is:',
      options: ['4 m/s²', '6 m/s²', '2 m/s²', '8 m/s²'],
      correctIndex: 0,
      solution: 'a = g(sinθ − μk cosθ) = 10×(0.6 − 0.25×0.8) = 10×(0.6 − 0.2) = 4 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A block is projected UP a rough incline of angle 30° with μk = 0.2 (g = 10 m/s²). Its deceleration while moving up is:',
      options: ['3.27 m/s²', '5 m/s²', '6.73 m/s²', '5.87 m/s²'],
      correctIndex: 2,
      solution: 'Moving up, both gravity and friction oppose the motion: a = g(sinθ + μk cosθ) = 10×(sin30° + 0.2×cos30°) = 10×(0.5 + 0.2×0.866) = 10×(0.5 + 0.173) = 6.73 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A block of mass m is held stationary on a rough incline of angle θ (with tanθ > μs) by a horizontal force F pushing it into the incline from outside (i.e., a force additional to gravity, directed horizontally). Which statement about the normal force is correct?',
      options: [
        'N = mg cosθ always, regardless of F',
        'N depends on both mg cosθ and a component of F, since F is not purely along the incline',
        'N = mg regardless of angle',
        'F has no effect on N since it is horizontal',
      ],
      correctIndex: 1,
      solution:
          'A horizontal force has components both along AND perpendicular to the incline (since the incline surface is tilted relative to horizontal). Its perpendicular component adds to or subtracts from mg cosθ in determining N — so N is NOT simply mg cosθ once an extra horizontal force is introduced.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'As the angle of a frictionless incline increases from 0° to 90°, the normal force on a block of fixed mass:',
      options: ['Increases from 0 to mg', 'Decreases from mg to 0', 'Stays constant at mg', 'Increases from mg to 2mg'],
      correctIndex: 1,
      solution: 'N = mg cosθ decreases from mg (at θ = 0°, flat) to 0 (at θ = 90°, vertical wall) as the angle increases.',
    ),
  ],
  revision: [
    'Resolve weight along the incline (mg sinθ, causes sliding) and perpendicular to it (mg cosθ, determines N).',
    'Perpendicular to the incline there is no acceleration: N = mg cosθ.',
    'Frictionless incline: a = g sinθ — independent of mass, just like free fall.',
    'Block stays stationary on a rough incline whenever tanθ ≤ μs.',
    'Sliding DOWN with friction: a = g(sinθ − μk cosθ). Sliding UP (decelerating): a = g(sinθ + μk cosθ) — friction and gravity both oppose upward motion.',
    'Always verify whether the block actually moves (compare tanθ to μs) before computing an acceleration.',
    'N = mg cosθ shrinks as the incline steepens, reaching zero at a vertical (90°) surface.',
  ],
  sandboxBuilder: (_) => const InclinedPlaneSimulator(),
);
