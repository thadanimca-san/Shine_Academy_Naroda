import '../../models/lesson.dart';
import '../../simulators/rotational_motion_sim.dart';
import '../../theme/tokens.dart';

/// Rotational Kinematics — the angular twins of displacement, velocity, and acceleration.
final Lesson rotationalKinematicsLesson = Lesson(
  topicId: 'rotational-dynamics',
  title: 'Rotational Kinematics',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A spinning ceiling fan has every single point on its blades completing one full circle in exactly the same time. Yet a point near the tip is clearly moving faster through the air than a point near the hub. How can two points on the SAME rigid blade have different speeds but the same "amount of turning"?',
  whyItMatters:
      'Rotational kinematics is linear kinematics wearing a different costume — every formula you already know (v = u + at, s = ut + ½at², v² = u² + 2as) has an exact angular twin, just with θ, ω, α replacing s, v, a. This mapping is one of the highest-leverage shortcuts in the entire mechanics syllabus, letting you solve spinning-wheel, flywheel, and rotating-disc problems in JEE and NEET almost by pattern-matching rather than deriving from scratch.',
  prediction: const PredictionPrompt(
    scenario:
        'A rigid disc spins about its center. Compare the LINEAR speed of a point at the rim (radius R) with a point halfway to the center (radius R/2), both on the same spinning disc:',
    options: [
      'Both points move at the same linear speed — it\'s one rigid disc',
      'The rim point moves twice as fast as the halfway point',
      'The rim point moves four times as fast',
      'The halfway point moves faster because it turns "tighter"',
    ],
    correctIndex: 1,
    reveal:
        'Every point on a rigid body shares the same angular velocity ω, but linear speed v = ωr grows with radius. Double the radius, double the linear speed, even though both points complete a revolution in the exact same time. In the lab, mark two radii on the spinning disc and read off their linear-speed indicators — the ratio always matches the ratio of their radii exactly.',
  ),
  experiments: [
    'Spin the disc at constant ω and compare the speed readout at different radii — confirm v = ωr',
    'Apply angular acceleration and watch ω grow linearly with time, matching ω = ω₀ + αt',
    'Read the angle turned at increasing times and confirm the θ = ω₀t + ½αt² pattern',
    'Increase ω and watch the centripetal-acceleration arrow at the rim grow with ω²',
    'Stop the angular acceleration and watch ω stay constant while θ keeps growing linearly',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Rotational motion has its own set of describing quantities that mirror straight-line motion exactly. Angular displacement θ (in radians) replaces linear displacement s. Angular velocity ω replaces linear velocity v. Angular acceleration α replaces linear acceleration a. Every rigid body rotating about a fixed axis has ONE value of θ, ω, α that applies to the whole body — unlike linear speed, which differs point to point.',
      title: 'θ, ω, α — the angular alphabet',
    ),
    ContentBlock.formula(
      'ω = dθ/dt,   α = dω/dt',
      title: 'ANGULAR VELOCITY AND ACCELERATION',
    ),
    ContentBlock.paragraph(
      'A point at radius r from the rotation axis has a linear (tangential) speed and a linear (tangential) acceleration that are simply the angular quantities scaled by r. This is the bridge between "how fast is it turning" (ω, α — same for the whole body) and "how fast is this specific point moving" (v, a_t — different at different radii).',
      title: 'Connecting angular and linear quantities',
    ),
    ContentBlock.formula(
      'v = ω·r,   a_t = α·r',
      title: 'LINEAR-ANGULAR BRIDGE (tangential)',
    ),
    ContentBlock.bullets([
      'Every point of a rigid body shares the SAME ω and α, regardless of its distance from the axis',
      'Linear (tangential) speed v = ωr grows with radius — points farther out move faster',
      'Radians, not degrees, must be used in all these formulas: 1 revolution = 2π rad = 360°',
      'A point moving in a circle also has a RADIAL (centripetal) acceleration, even at constant ω',
    ]),
    ContentBlock.formula(
      'ω = ω₀ + αt,   θ = ω₀t + ½αt²,   ω² = ω₀² + 2αθ',
      title: 'THE THREE ROTATIONAL EQUATIONS OF MOTION',
    ),
    ContentBlock.realLife(
      'On a rotating merry-go-round, a child sitting near the edge feels a much stronger outward pull and moves noticeably faster through the air than a child sitting near the center — same ω for both, but v = ωr means the outer child has a larger r and therefore a larger v and larger centripetal acceleration a_c = ω²r.',
    ),
    ContentBlock.mistake(
      'Using degrees instead of radians in the rotational kinematics equations. θ = ω₀t + ½αt² and v = ωr are only correct when θ and ω are in RADIANS (and rad/s). Plugging in degrees will silently give wildly wrong answers, since 1 rad ≈ 57.3°.',
    ),
    ContentBlock.mistake(
      'Forgetting that even at CONSTANT angular velocity (α = 0), a point moving in a circle still has acceleration — the centripetal acceleration a_c = ω²r = v²/r, directed toward the center. "Constant ω" means zero TANGENTIAL acceleration, not zero acceleration overall.',
    ),
    ContentBlock.example(
      'A wheel starts from rest and reaches an angular velocity of 20 rad/s in 4 s under constant angular acceleration. Find (a) α, and (b) the angle turned in that time.\n\n(a) α = (ω − ω₀)/t = (20 − 0)/4 = 5 rad/s²\n\n(b) θ = ω₀t + ½αt² = 0 + ½×5×4² = ½×5×16 = 40 rad.',
    ),
    ContentBlock.jeeTip(
      'The mapping s↔θ, v↔ω, a↔α, u↔ω₀ lets you convert ANY linear kinematics result instantly into a rotational one, including the "distance/angle in the nth interval" formula: θ_nth = ω₀ + (α/2)(2n−1), the direct analog of s_nth = u + (a/2)(2n−1) — a favourite JEE shortcut for flywheel problems.',
    ),
    ContentBlock.jeeTip(
      'The TOTAL linear acceleration of a point on a spinning-up rigid body has TWO perpendicular components: tangential a_t = αr (from angular acceleration, along the direction of motion) and centripetal a_c = ω²r (from the turning itself, toward the center). The resultant magnitude is √(a_t² + a_c²) — a very common "resolve into components" JEE question.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the linear speed of a point on the rim of a rotating object given its RPM (revolutions per minute). Convert first: ω = 2πN/60 (N in rpm gives ω in rad/s), then use v = ωr. Also remember: centripetal acceleration can be written two equivalent ways, a_c = ω²r or a_c = v²/r — pick whichever quantity (ω or v) you already know.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the definition of angular acceleration',
      math: 'α = dω/dt  →  dω = α·dt',
      note:
          'For constant α, this integrates directly — exactly parallel to a = dv/dt in linear motion.',
    ),
    DerivationStep(
      title: 'Integrate angular velocity from ω₀ to ω, time from 0 to t',
      math: '∫_{ω₀}^{ω} dω = α∫₀ᵗ dt  →  ω − ω₀ = αt',
      note: 'First rotational equation: ω = ω₀ + αt.',
    ),
    DerivationStep(
      title: 'Use the definition of angular velocity',
      math: 'ω = dθ/dt  →  dθ = (ω₀ + αt)·dt',
    ),
    DerivationStep(
      title: 'Integrate angular displacement from 0 to θ',
      math: 'θ = ω₀t + ½αt²',
      note: 'Second rotational equation — the direct analog of s = ut + ½at².',
    ),
    DerivationStep(
      title: 'Eliminate t using ω·dω = α·dθ',
      math: '∫_{ω₀}^{ω} ω dω = α∫₀^θ dθ  →  ½(ω² − ω₀²) = αθ',
      note:
          'Rearranged: ω² = ω₀² + 2αθ — the third rotational equation, useful when time is unknown.',
    ),
  ],
  formulas: const [
    FormulaEntry('First rotational equation', 'ω = ω₀ + αt'),
    FormulaEntry('Second rotational equation', 'θ = ω₀t + ½αt²'),
    FormulaEntry('Third rotational equation', 'ω² = ω₀² + 2αθ'),
    FormulaEntry('Linear-angular bridge', 'v = ωr,   a_t = αr'),
    FormulaEntry('Centripetal acceleration', 'a_c = ω²r = v²/r'),
    FormulaEntry(
      'Angular velocity from RPM',
      'ω = 2πN/60',
      condition: 'N in revolutions per minute',
    ),
    FormulaEntry('Angle in nth second', 'θ_nth = ω₀ + (α/2)(2n−1)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A wheel rotating at 5 rad/s speeds up to 15 rad/s in 5 s under constant angular acceleration. The value of α is:',
      options: ['1 rad/s²', '2 rad/s²', '3 rad/s²', '4 rad/s²'],
      correctIndex: 1,
      solution: 'α = (ω − ω₀)/t = (15 − 5)/5 = 2 rad/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A rigid disc rotates about its center. Which of the following is the SAME for every point on the disc?',
      options: [
        'Linear speed',
        'Linear acceleration',
        'Angular velocity',
        'Centripetal acceleration',
      ],
      correctIndex: 2,
      solution:
          'Every point on a rigid body shares the same ω (and α), since the whole body turns through the same angle in the same time. Linear speed, acceleration, and centripetal acceleration all depend on r, which differs point to point.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A fan blade rotates at ω = 10 rad/s. The linear speed of a point 0.5 m from the axis is:',
      options: ['2.5 m/s', '5 m/s', '10 m/s', '20 m/s'],
      correctIndex: 1,
      solution: 'v = ωr = 10×0.5 = 5 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A wheel of radius 0.2 m rotates at a constant 100 rad/s. The centripetal acceleration of a point on its rim is:',
      options: ['200 m/s²', '2000 m/s²', '20 m/s²', '400 m/s²'],
      correctIndex: 1,
      solution: 'a_c = ω²r = (100)²×0.2 = 10000×0.2 = 2000 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A grinding wheel starts from rest and reaches 300 rpm in 10 s with constant angular acceleration. The angular acceleration is:',
      options: ['π rad/s²', '2π rad/s²', '3π rad/s²', 'π/2 rad/s²'],
      correctIndex: 0,
      solution:
          'ω = 2πN/60 = 2π×300/60 = 10π rad/s. α = (ω − 0)/t = 10π/10 = π rad/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A point on a rotating rigid body has tangential acceleration 2 m/s² and centripetal acceleration 6 m/s² at some instant. The magnitude of its total linear acceleration is:',
      options: ['8 m/s²', '4 m/s²', '√40 m/s²', '2√10 m/s²'],
      correctIndex: 2,
      solution:
          'The two components are perpendicular: a_total = √(a_t² + a_c²) = √(2² + 6²) = √(4+36) = √40 ≈ 6.32 m/s² (equivalently 2√10).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A flywheel rotating at ω₀ = 20 rad/s is brought to rest by a constant angular retardation in 40 revolutions. The angular retardation is (use ω² = ω₀² + 2αθ, θ in radians):',
      options: ['0.8 rad/s²', '1.6 rad/s²', '4 rad/s²', '8 rad/s²'],
      correctIndex: 0,
      solution:
          'θ = 40×2π = 80π rad. 0 = 20² − 2α(80π) → α = 400/(160π) = 2.5/π ≈ 0.796 ≈ 0.8 rad/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A wheel starts from rest with constant angular acceleration. Since θ = ½αt² measures angle from rest, how does the TIME taken to complete each successive revolution (1st, 2nd, 3rd, …) behave, compared to the previous one?',
      options: [
        'Each successive revolution takes LESS time than the one before, following a √n − √(n−1) pattern',
        'Every revolution takes exactly the same time, since it starts from rest',
        'Each successive revolution takes MORE time, growing linearly with revolution number',
        'The times follow the same 1:3:5:7 odd-number ratio as linear distance in successive seconds',
      ],
      correctIndex: 0,
      solution:
          'Since θ = ½αt² (from rest), the time to complete n revolutions is t_n ∝ √n. The time for the nth revolution alone is t_n − t_{n−1} ∝ √n − √(n−1), a gap that SHRINKS as n grows — the mirror image of the linear "odd number" rule, which describes distance covered per fixed time interval, not time taken per fixed distance/revolution.',
    ),
  ],
  revision: [
    'θ, ω, α mirror s, v, a exactly — the entire linear kinematics toolkit has a rotational twin.',
    'ω = ω₀ + αt,  θ = ω₀t + ½αt²,  ω² = ω₀² + 2αθ — valid only for constant α, and only in RADIANS.',
    'Every point of a rigid body shares the same ω and α; linear v = ωr and a_t = αr depend on radius.',
    'Centripetal acceleration a_c = ω²r = v²/r exists even at constant ω — it changes direction, not speed.',
    'Total linear acceleration of a point = vector sum of tangential (αr) and centripetal (ω²r) components.',
    'Convert RPM to rad/s with ω = 2πN/60 before using any kinematics formula.',
    'θ_nth = ω₀ + (α/2)(2n−1) is the rotational analog of the "distance in nth second" formula.',
  ],
  sandboxBuilder: (_) => const RotationalMotionSimulator(),
);
