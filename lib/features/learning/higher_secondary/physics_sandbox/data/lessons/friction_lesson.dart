import '../../models/lesson.dart';
import '../../simulators/friction_sim.dart';
import '../../theme/tokens.dart';

/// Friction — static vs kinetic, the angle of repose, and why friction isn't always your enemy.
final Lesson frictionLesson = Lesson(
  topicId: 'friction',
  title: 'Friction',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'You push a heavy box and nothing happens — then you push a little harder and suddenly it slides, and once moving it takes noticeably LESS force to keep it going. Why does friction seem to "give way" only after a threshold, and then get weaker?',
  whyItMatters:
      'Friction problems are everywhere in JEE/NEET mechanics — blocks on inclines, pulleys, circular motion on banked roads, even walking and braking. The key exam trap is that friction is NOT a single fixed force; it is a self-adjusting force up to a maximum, and switches to a different (smaller) value once sliding starts. Get the static-vs-kinetic distinction wrong and half your incline and pulley answers will be wrong too.',
  prediction: const PredictionPrompt(
    scenario:
        'You slowly increase the horizontal force on a heavy crate resting on a rough floor. Which best describes what friction does as you push harder and harder, right up to the moment it starts sliding?',
    options: [
      'Friction stays at a fixed constant value the whole time',
      'Friction increases to exactly match your push, up to a maximum, then drops once sliding begins',
      'Friction decreases steadily as your push increases',
      'Friction is zero until the crate starts moving, then suddenly appears',
    ],
    correctIndex: 1,
    reveal:
        'Static friction is a SELF-ADJUSTING force — it automatically matches the applied force (so the object stays put) up to a maximum value f_s(max) = μs·N. The instant your push exceeds that maximum, the crate breaks loose and kinetic friction takes over, which is slightly SMALLER (μk < μs), so it suddenly feels easier to keep pushing. In the lab, ramp the applied force up slowly and watch the friction readout climb to match it exactly, then drop at the breakaway point.',
  ),
  experiments: [
    'Slowly increase the applied force from zero and watch friction rise to match it exactly, until breakaway',
    'Note the exact force at which the block starts sliding — that\'s f_s(max) = μs·N',
    'Once sliding, read the (now lower) kinetic friction value and confirm μk < μs',
    'Increase the normal force (add weight) and confirm both f_s(max) and f_k scale up proportionally',
    'Tilt the surface until the block just begins to slide — read off the angle of repose and compare tan θ to μs',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Friction is the force that resists relative sliding between two surfaces in contact. It arises from microscopic roughness and molecular adhesion between the surfaces. Crucially, friction comes in two regimes: STATIC friction, which prevents an object from starting to move, and KINETIC (or sliding) friction, which acts once the object is already sliding.',
      title: 'Two regimes of friction',
    ),
    ContentBlock.formula('f_s(max) = μs·N,     f_k = μk·N', title: 'STATIC AND KINETIC FRICTION'),
    ContentBlock.bullets([
      'Static friction is SELF-ADJUSTING: f_s = applied force, up to the maximum μs·N, whenever the object stays at rest',
      'Kinetic friction is essentially CONSTANT once sliding, equal to μk·N, and independent of speed',
      'Both are proportional to the normal force N, NOT to the apparent contact area',
      'μs and μk are dimensionless coefficients that depend only on the pair of surfaces in contact',
    ]),
    ContentBlock.paragraph(
      'Experimentally, the coefficient of static friction is always slightly greater than the coefficient of kinetic friction: μs > μk. This is why it takes a noticeably bigger push to START a heavy object moving than to KEEP it moving — the surfaces "settle into" each other more while at rest, and that extra interlocking is lost the moment sliding begins.',
      title: 'Why μs > μk',
    ),
    ContentBlock.paragraph(
      'The angle of repose is the steepest angle you can tilt a surface before an object resting on it just begins to slide. At that exact angle, gravity\'s component along the incline (mg sinθ) exactly equals the maximum static friction (μs·mg cosθ), giving the elegant result tan θ = μs. Measuring this angle is a common practical method for finding μs.',
      title: 'Angle of repose',
    ),
    ContentBlock.formula('tan θ_repose = μs', title: 'ANGLE OF REPOSE'),
    ContentBlock.realLife(
      'Friction is NOT always the enemy of motion — it is precisely what lets you walk. Your foot pushes backward on the ground and, thanks to friction, does not simply slip; the reaction pushes you forward. Without friction (as on wet ice) your foot slides in place and you can barely move at all. Car tyres, similarly, need friction with the road to accelerate, brake and turn — an icy road removes exactly this and makes all three dangerous.',
    ),
    ContentBlock.mistake(
      'Using μs·N to calculate the friction force on an object that is already moving. Once an object slides, friction switches to the KINETIC value μk·N, which is smaller. Using μs after motion has started overestimates the friction and gives a wrong (too-small) acceleration.',
    ),
    ContentBlock.mistake(
      'Assuming friction always opposes the direction the object is trying to move overall. Friction opposes RELATIVE SLIDING at the point of contact — when walking, your foot is trying to slide backward relative to the ground, so friction on your foot points FORWARD, which is the direction you actually travel. "Friction always opposes motion" is an oversimplification that fails exactly in cases like this.',
    ),
    ContentBlock.example(
      'A 10 kg block rests on a floor with μs = 0.5 and μk = 0.4 (g = 10 m/s²). Find the friction force when a horizontal force of (a) 40 N and (b) 60 N is applied.\n\nN = mg = 100 N, so f_s(max) = 0.5×100 = 50 N and f_k = 0.4×100 = 40 N.\n\n(a) Applied force 40 N < f_s(max) = 50 N → block stays at rest, static friction exactly balances it: f = 40 N.\n(b) Applied force 60 N > f_s(max) = 50 N → block slides, friction is now kinetic: f = f_k = 40 N (not 60 N, and not 50 N).',
    ),
    ContentBlock.jeeTip(
      'On a rough incline, resolve weight into mg sinθ (along the incline) and mg cosθ (perpendicular). Compare mg sinθ to f_s(max) = μs·mg cosθ: if mg sinθ ≤ μs·mg cosθ, i.e., tanθ ≤ μs, the block stays put — static friction adjusts to exactly balance mg sinθ. If tanθ > μs, the block accelerates down the incline with a = g(sinθ − μk cosθ). Always check which regime you\'re in before assuming the block moves.',
    ),
    ContentBlock.neetNote(
      'NEET often asks conceptual friction questions: friction is independent of the apparent area of contact (a brick on its large face and its small face experiences the same friction, for the same weight and surfaces), and rolling friction is much smaller than sliding friction — which is why wheels and ball bearings reduce energy loss so effectively compared to dragging.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the incline at the critical (repose) angle',
      math: 'Block on rough incline, angle θ, on the verge of sliding',
      note: 'At this exact angle, static friction is at its maximum value.',
    ),
    DerivationStep(
      title: 'Resolve weight into components',
      math: 'Along incline: mg sinθ.   Perpendicular: mg cosθ.',
    ),
    DerivationStep(
      title: 'Write the perpendicular equilibrium (no acceleration normal to incline)',
      math: 'N = mg cosθ',
    ),
    DerivationStep(
      title: 'Write the along-incline equilibrium at the verge of sliding',
      math: 'f_s(max) = mg sinθ',
      note: 'Just before sliding, static friction has grown to exactly balance gravity\'s component along the incline.',
    ),
    DerivationStep(
      title: 'Substitute f_s(max) = μs·N and divide',
      math: 'μs·(mg cosθ) = mg sinθ  ⟹  μs = tanθ',
      note: 'The angle of repose satisfies tanθ = μs — independent of the block\'s mass.',
    ),
  ],
  formulas: const [
    FormulaEntry('Maximum static friction', 'f_s(max) = μs·N'),
    FormulaEntry('Kinetic friction', 'f_k = μk·N'),
    FormulaEntry('Relation between coefficients', 'μs > μk'),
    FormulaEntry('Angle of repose', 'tanθ = μs'),
    FormulaEntry('Acceleration down rough incline', 'a = g(sinθ − μk cosθ)', condition: 'tanθ > μs, block already sliding'),
    FormulaEntry('Condition to remain stationary on incline', 'tanθ ≤ μs'),
    FormulaEntry('Normal force on horizontal surface', 'N = mg'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The maximum value of static friction is given by:',
      options: ['μk·N', 'μs·N', 'μs·mg sinθ', 'μs + N'],
      correctIndex: 1,
      solution: 'f_s(max) = μs·N, where N is the normal force between the surfaces.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For a given pair of surfaces, the coefficient of static friction μs compared to the coefficient of kinetic friction μk is generally:',
      options: ['μs < μk', 'μs = μk always', 'μs > μk', 'No fixed relation'],
      correctIndex: 2,
      solution: 'Static friction is generally slightly greater than kinetic friction: μs > μk.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A block of mass 5 kg rests on a floor with μs = 0.4 (g = 10 m/s²). A horizontal force of 15 N is applied. The block:',
      options: [
        'Slides, with friction 20 N',
        'Stays at rest, with static friction 15 N',
        'Stays at rest, with static friction 20 N',
        'Slides, with friction 15 N',
      ],
      correctIndex: 1,
      solution:
          'f_s(max) = μs·mg = 0.4×5×10 = 20 N. Applied force 15 N < 20 N, so the block remains at rest and static friction exactly matches the applied force: 15 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The angle of repose for a surface is 30°. The coefficient of static friction is closest to:',
      options: ['0.87', '0.58', '0.50', '1.73'],
      correctIndex: 1,
      solution: 'μs = tanθ = tan30° = 1/√3 ≈ 0.58.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Friction is independent of:',
      options: ['The normal force', 'The nature of the two surfaces', 'The apparent area of contact', 'None of these — friction depends on all of them'],
      correctIndex: 2,
      solution:
          'Friction depends on N and on μ (which depends on the surface materials), but NOT on the apparent macroscopic contact area — a brick gives the same friction on its large or small face for the same weight.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A block slides down a rough incline of angle 45° with μk = 0.5. Its acceleration (g = 10 m/s²) is:',
      options: ['2.5 m/s²', '3.5 m/s²', '5 m/s²', '7.5 m/s²'],
      correctIndex: 1,
      solution:
          'a = g(sinθ − μk cosθ) = 10×(sin45° − 0.5cos45°) = 10×(0.707 − 0.354) = 10×0.354 ≈ 3.5 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A person walks on a rough horizontal road without slipping. The friction force on the person\'s foot from the ground, at the instant of pushing off, points:',
      options: [
        'Backward, opposing the person\'s forward motion',
        'Forward, in the direction the person moves',
        'Vertically upward only',
        'There is no friction involved in walking',
      ],
      correctIndex: 1,
      solution:
          'The foot pushes backward against the ground (tending to slide backward); by the third law and friction opposing relative sliding, the ground exerts a forward friction force on the foot, which propels the person forward. Friction here enables motion rather than opposing it.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A 2 kg block on a rough horizontal surface (μs = 0.6, μk = 0.5, g = 10 m/s²) is pushed with a steadily increasing horizontal force starting from zero. At the instant the force reaches 13 N, the block:',
      options: [
        'Is still at rest, since 13 N < f_s(max) = 12 N is false — recheck',
        'Has just started sliding, since f_s(max) = 12 N was exceeded',
        'Was already sliding well before 13 N',
        'Never slides regardless of force, since μk < μs',
      ],
      correctIndex: 1,
      solution:
          'f_s(max) = μs·mg = 0.6×2×10 = 12 N. Once the applied force exceeds 12 N (at 13 N), the block breaks loose and starts sliding, after which kinetic friction (μk·mg = 10 N) applies, giving a net force of 13 − 10 = 3 N and acceleration 1.5 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Rolling friction, compared to sliding friction between the same two materials, is generally:',
      options: ['Much larger', 'Much smaller', 'Exactly equal', 'Independent of the materials'],
      correctIndex: 1,
      solution:
          'Rolling friction is significantly smaller than sliding friction for the same surfaces — this is why wheels, ball bearings and rollers are used to reduce energy loss in machines and vehicles.',
    ),
  ],
  revision: [
    'Static friction self-adjusts to match the applied force, up to a maximum f_s(max) = μs·N.',
    'Once sliding begins, friction switches to the smaller, roughly constant kinetic value f_k = μk·N.',
    'μs > μk always — it takes more force to start motion than to sustain it.',
    'Friction depends on N and the surface pair (μ), never on the apparent contact area.',
    'Angle of repose: tanθ = μs — the tilt angle at which an object just begins to slide.',
    'On an incline: stays put if tanθ ≤ μs; slides with a = g(sinθ − μk cosθ) if tanθ > μs.',
    'Friction opposes relative SLIDING at the contact point, not necessarily the object\'s overall direction of travel — walking is powered by friction, not opposed by it.',
  ],
  sandboxBuilder: (_) => const FrictionSimulator(),
);
