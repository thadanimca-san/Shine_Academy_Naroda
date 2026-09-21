import '../../models/lesson.dart';
import '../../simulators/rolling_motion_sim.dart';
import '../../theme/tokens.dart';

/// Rolling Motion — why a solid ball always beats a hoop down the same slope.
final Lesson rollingMotionLesson = Lesson(
  topicId: 'rolling-motion',
  title: 'Rolling Motion',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A solid ball, a hollow ball, a solid disc and a ring — all the same mass and radius — are released from rest at the top of the same ramp. They all feel the same gravity and the same slope. Do they reach the bottom together?',
  whyItMatters:
      'Rolling without slipping is where translational and rotational mechanics finally meet — a wheel, a ball, a cylinder all move by doing both at once. The incline race is one of the most-tested setups in JEE and NEET because it forces you to combine energy conservation with moment of inertia in one clean calculation. Understand this and you can predict the winner of ANY rolling race without touching a stopwatch.',
  prediction: const PredictionPrompt(
    scenario:
        'A solid sphere, a hollow sphere, a solid disc and a ring — identical mass and radius — are released from rest together at the top of a frictionless-looking but actually rolling-without-slipping incline. Which reaches the bottom first?',
    options: [
      'They all arrive together — same mass, same height, same gravity',
      'The ring, because it has the largest radius of gyration',
      'The solid sphere, because it has the smallest moment of inertia',
      'The hollow sphere, because a shell distributes mass evenly',
    ],
    correctIndex: 2,
    reveal:
        'The solid sphere wins every time. Its acceleration down the incline is a = g sinθ/(1 + k), where k = I/MR² is smallest for a solid sphere (k = 2/5) — so 1+k is smallest and a is largest. The order is always: solid sphere > solid disc > hollow sphere > ring, exactly by increasing k. In the lab, release all four shapes together on the same incline and watch the solid sphere pull ahead immediately, with the ring trailing last.',
  ),
  experiments: [
    'Release a solid sphere and a ring together on the same incline — watch the sphere win decisively',
    'Race the solid disc against the hollow sphere — the disc (k=½) narrowly loses to the sphere\'s siblings but beats the ring',
    'Increase the incline angle and see all objects accelerate faster, but the FINISH ORDER never changes',
    'Toggle "frictionless" (sliding, not rolling) and watch all shapes tie — without friction there is no rolling, only sliding',
    'Check the velocity readout at the bottom: v = ωR always holds while rolling without slipping',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A wheel rolling on a road is not just spinning, and not just translating — it is doing both simultaneously, and the two motions are locked together by one geometric condition. "Rolling without slipping" means the point of the wheel touching the ground is instantaneously at rest relative to the ground — no skidding, no sliding.',
      title: 'Two motions, one condition',
    ),
    ContentBlock.formula('v = ωR   (rolling without slipping)', title: 'THE ROLLING CONDITION'),
    ContentBlock.bullets([
      'v is the velocity of the CENTRE of the rolling body',
      'ω is the angular velocity about that same centre',
      'R is the radius of the rolling body',
      'This single equation links translation (v) and rotation (ω) — know one, you know the other',
    ]),
    ContentBlock.paragraph(
      'Because rolling combines translation and rotation, the total kinetic energy has two separate terms: translational KE from the centre of mass moving, and rotational KE from spinning about the centre of mass. Neither term alone tells the full story — you always need both.',
      title: 'Total kinetic energy of a rolling body',
    ),
    ContentBlock.formula('KE_total = ½Mv² + ½Iω²', title: 'ROLLING KINETIC ENERGY'),
    ContentBlock.paragraph(
      'Using v = ωR and writing I = kMR² (k is the shape factor: ½ for a disc, 2/5 for a solid sphere, 1 for a ring), the rotational term becomes ½(kMR²)(v/R)² = ½kMv². So KE_total = ½Mv²(1 + k) — a shape with a larger k stores more energy in spin for the same speed v, leaving less energy available to have gotten it moving fast in the first place.',
      title: 'Rewriting energy with the shape factor k',
    ),
    ContentBlock.realLife(
      'Sports balls exploit this: a solid cricket/golf ball (k=2/5) accelerates and decelerates faster than a hollow ball of the same mass and size would. Train wheels and heavy flywheels are deliberately built with larger k (mass toward the rim) specifically because that stores MORE rotational energy for a given speed — useful for smoothing momentum, bad for quick acceleration.',
    ),
    ContentBlock.mistake(
      'Using KE = ½Mv² alone for a rolling object, ignoring the rotational term. This is the single most common rolling-motion error and it always gives too small (or wrong) an answer. A rolling body\'s kinetic energy is NEVER purely translational.',
    ),
    ContentBlock.mistake(
      'Applying friction backwards or forgetting it entirely. Static friction is what CAUSES the torque that produces rolling as an object accelerates down an incline — without friction, an object on a frictionless slope only slides, never rolls. But once rolling without slipping is established, this friction does NO work (the contact point has zero velocity), so energy conservation still applies cleanly.',
    ),
    ContentBlock.example(
      'A solid sphere (k = 2/5) rolls from rest down an incline of height h = 1.4 m without slipping. Find its speed at the bottom (g = 10 m/s²).\n\nEnergy conservation: Mgh = ½Mv²(1+k)\ngh = ½v²(1 + 2/5) = ½v²(7/5)\nv² = 2gh × 5/7 = (2×10×1.4×5)/7 = 140/7 = 20\nv = √20 ≈ 4.47 m/s.\n\nCompare to a frictionless slide (no rotation): v = √(2gh) = √28 ≈ 5.29 m/s — rolling is always slower because some energy goes into spin.',
    ),
    ContentBlock.jeeTip(
      'For acceleration down an incline, derive once and reuse: a = g sinθ/(1+k). Since k is smallest for a solid sphere and largest for a ring, acceleration ranking is ALWAYS solid sphere > solid cylinder/disc > hollow sphere > hollow cylinder/ring, regardless of mass, radius, or incline angle — a pure race, decided entirely by shape.',
    ),
    ContentBlock.neetNote(
      'NEET often asks for the fraction of kinetic energy that is rotational: KE_rot/KE_total = k/(1+k). For a solid sphere this is (2/5)/(7/5) = 2/7; for a ring it is 1/2. Memorise these two — they appear repeatedly as direct-recall questions.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up energy conservation on the incline',
      math: 'Mgh = KE_translation + KE_rotation = ½Mv² + ½Iω²',
      note: 'Starting from rest, all lost PE converts to KE (rolling friction does no work at the contact point).',
    ),
    DerivationStep(
      title: 'Use the rolling condition to eliminate ω',
      math: 'ω = v/R  →  ½Iω² = ½I(v/R)²',
    ),
    DerivationStep(
      title: 'Write I in terms of the shape factor k',
      math: 'I = kMR²  →  ½Iω² = ½kMR²(v/R)² = ½kMv²',
      note: 'k = ½ for a disc, 2/5 for a solid sphere, 1 for a ring, 2/3 for a hollow sphere.',
    ),
    DerivationStep(
      title: 'Combine both KE terms',
      math: 'Mgh = ½Mv² + ½kMv² = ½Mv²(1+k)',
      note: 'Cancel M: gh = ½v²(1+k)  →  v² = 2gh/(1+k).',
    ),
    DerivationStep(
      title: 'Relate to acceleration using kinematics on the incline',
      math: 'h = L sinθ,  v² = 2aL  →  a = g sinθ/(1+k)',
      note: 'The key result: smaller k → larger a → wins the race, independent of M and R.',
    ),
  ],
  formulas: const [
    FormulaEntry('Rolling without slipping', 'v = ωR'),
    FormulaEntry('Total rolling KE', 'KE = ½Mv² + ½Iω² = ½Mv²(1+k)', condition: 'I = kMR²'),
    FormulaEntry('Speed at bottom of incline', 'v² = 2gh/(1+k)'),
    FormulaEntry('Acceleration down incline', 'a = g sinθ/(1+k)'),
    FormulaEntry('Fraction of KE that is rotational', 'KE_rot/KE_total = k/(1+k)'),
    FormulaEntry('Shape factors', 'ring/hoop: k=1, disc: k=½, solid sphere: k=2/5, hollow sphere: k=2/3'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For a rolling body, the condition "rolling without slipping" means:',
      options: [
        'The centre of mass is at rest',
        'The point of contact with the ground is instantaneously at rest',
        'The angular velocity is zero',
        'There is no friction at all',
      ],
      correctIndex: 1,
      solution: 'Rolling without slipping means the contact point has zero velocity relative to the ground at each instant — that is exactly what v = ωR guarantees.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A ring and a solid sphere of equal mass and radius roll down the same incline from rest. Which reaches the bottom first?',
      options: ['The ring', 'The solid sphere', 'Both together', 'Cannot be determined'],
      correctIndex: 1,
      solution: 'a = g sinθ/(1+k). The solid sphere has k=2/5 (smaller than the ring\'s k=1), so it has larger acceleration and wins.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A solid cylinder (k = ½) rolls down an incline of height 2 m without slipping. Its speed at the bottom is (g = 10 m/s²):',
      options: ['4√2 m/s', '2√(20/3) m/s', '√(80/3) m/s', '20/3 m/s'],
      correctIndex: 2,
      solution: 'v² = 2gh/(1+k) = 2×10×2/(1.5) = 40/1.5 = 80/3, so v = √(80/3) m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'For a solid sphere rolling without slipping, the fraction of its total kinetic energy that is rotational is:',
      options: ['1/2', '2/7', '2/5', '5/7'],
      correctIndex: 1,
      solution: 'KE_rot/KE_total = k/(1+k) = (2/5)/(7/5) = 2/7.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A hollow sphere and a solid sphere, same mass and radius, are released together on an incline. The solid sphere reaches the bottom first because:',
      options: [
        'It has greater mass',
        'It has a smaller moment of inertia, so more of the released PE goes into translational KE',
        'It experiences less gravity',
        'The hollow sphere experiences more air resistance',
      ],
      correctIndex: 1,
      solution: 'Both have the same mass, so PE loss is the same. The solid sphere\'s smaller k (2/5 vs 2/3) means less energy is "used up" spinning it, so more converts into translational speed v.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A ring rolls down an incline of angle θ without slipping. Its acceleration is:',
      options: ['g sinθ', 'g sinθ/2', 'g sinθ/3', '2g sinθ/3'],
      correctIndex: 1,
      solution: 'a = g sinθ/(1+k). For a ring k=1, so a = g sinθ/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A solid sphere and a solid disc, both released from rest at the same height on identical inclines, have a ratio of their speeds at the bottom v_sphere : v_disc equal to:',
      options: ['√(15/14)', '√(14/15)', '1 : 1', '5 : 7'],
      correctIndex: 0,
      solution:
          'v² = 2gh/(1+k). Sphere: v_s² ∝ 1/(1+2/5) = 5/7. Disc: v_d² ∝ 1/(1+1/2) = 2/3. Ratio v_s²/v_d² = (5/7)/(2/3) = 15/14, so v_s/v_d = √(15/14).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A uniform solid cylinder rolls without slipping down an incline of angle 30° and length 2 m, starting from rest (g = 10 m/s²). The time taken to reach the bottom is:',
      options: ['0.87 s', '1.1 s', '1.55 s', '2.0 s'],
      correctIndex: 1,
      solution:
          'a = g sinθ/(1+k) = 10×0.5/(1.5) = 10/3 m/s². Using L = ½at²: 2 = ½×(10/3)×t² → t² = 4×3/10 = 1.2 → t ≈ 1.095 ≈ 1.1 s.',
    ),
  ],
  revision: [
    'Rolling without slipping: v = ωR — the contact point is instantaneously at rest.',
    'Total rolling KE = ½Mv² + ½Iω² = ½Mv²(1+k), where I = kMR².',
    'Down an incline: a = g sinθ/(1+k) and v² = 2gh/(1+k) — smaller k wins the race.',
    'Race order (fastest to slowest): solid sphere > solid disc/cylinder > hollow sphere > ring/hoop.',
    'Static friction causes rolling but does zero work once rolling is established — energy conservation still holds.',
    'Fraction of KE that is rotational = k/(1+k); for a solid sphere this is 2/7, for a ring it is 1/2.',
    'The winner of any rolling race depends only on shape (k) — never on mass or radius.',
  ],
  sandboxBuilder: (_) => const RollingMotionSimulator(),
);
