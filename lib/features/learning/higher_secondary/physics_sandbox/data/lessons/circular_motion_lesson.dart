import '../../models/lesson.dart';
import '../../simulators/circular_motion_sandbox.dart';
import '../../theme/tokens.dart';

/// Circular Motion — why moving at constant SPEED still means accelerating.
final Lesson circularMotionLesson = Lesson(
  topicId: 'circular-motion',
  title: 'Circular Motion',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A ball on a string whirls around your head at perfectly constant speed. Its speedometer never changes. So why does Newton\'s first law say something MUST be pushing or pulling on it the entire time?',
  whyItMatters:
      'Circular motion is the idea that trips up more JEE/NEET aspirants than almost any other — the instinct to invent an outward "centrifugal force" is so strong that examiners build entire questions around catching it. Once you see clearly that velocity is a vector and a CHANGING DIRECTION is still acceleration, banking, conical pendulums and satellite orbits all become the same one-line calculation: net force toward the centre equals mv²/r.',
  prediction: const PredictionPrompt(
    scenario:
        'A ball whirls on a string in a horizontal circle at constant speed. From the ground (an inertial, non-rotating) frame, what is the net force acting on the ball?',
    options: [
      'Zero — the speed never changes, so there is no net force',
      'A force pointing outward, away from the centre (centrifugal force)',
      'A force pointing inward, toward the centre, supplied by the string tension',
      'Two equal and opposite forces — one in, one out — that cancel',
    ],
    correctIndex: 2,
    reveal:
        'Even though the SPEED is constant, the VELOCITY is not — its direction keeps changing, and any change in velocity is an acceleration. That acceleration points toward the centre (centripetal), and by Newton\'s second law it needs a real, inward net force to cause it — here, string tension. There is no outward force acting on the ball in this ground frame. In the lab, watch the blue arrow: it always points from the ball straight at the centre, at every instant, no matter how fast the ball goes.',
  ),
  experiments: [
    'Increase speed v and watch the force meter jump much faster than v itself — F ∝ v²',
    'Double the radius r at fixed v and see the force reading drop to half — F ∝ 1/r',
    'Increase mass m and confirm the force scales exactly in proportion',
    'Watch the arrow direction across a full revolution — it always points at the pivot, never away from it',
    'Compare the period T at small vs large r for the same v — larger circles take longer to complete even without changing speed',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Velocity is a vector: it has both a magnitude (speed) and a direction. In circular motion at "constant speed," the magnitude never changes but the direction changes every instant — so the velocity vector itself is constantly changing, which by definition means the object is accelerating. This acceleration is called centripetal ("centre-seeking") acceleration, and it always points from the object straight toward the centre of the circle.',
      title: 'Constant speed is NOT constant velocity',
    ),
    ContentBlock.formula('a_c = v²/r = ω²r,   F_c = ma_c = mv²/r = mω²r', title: 'CENTRIPETAL ACCELERATION & FORCE'),
    ContentBlock.bullets([
      'F_c ∝ v² — double the speed, the required force quadruples',
      'F_c ∝ 1/r — a tighter circle at the same speed needs MORE force',
      'F_c ∝ m — twice the mass needs twice the force for the same motion',
      'Direction: always along the radius, pointing INTO the centre, never outward',
    ]),
    ContentBlock.paragraph(
      'The centripetal force is not a new, separate kind of force — it is just the NAME for whichever real force (or combination of forces) happens to be supplying the inward pull. On a whirling ball it is string tension; on a car turning a flat road it is friction between tyres and road; for the Moon orbiting Earth it is gravity; for an electron in a Bohr orbit it is electrostatic attraction to the nucleus.',
      title: 'Centripetal force is a role, not a new force',
    ),
    ContentBlock.mistake(
      'Inventing an outward "centrifugal force" acting ON the object as seen from the ground. In an inertial (non-accelerating, non-rotating) frame there is NO such force on the object — only the real inward force exists. A rider in a car who feels "flung outward" on a turn is actually being flung in a STRAIGHT LINE by inertia while the car curves away beneath them; the door then pushes them inward to make them turn too. The "centrifugal force" you feel is real only as a pseudo-force in the rotating frame of the car itself — see the Pseudo Forces topic for exactly when that is valid to use.',
    ),
    ContentBlock.paragraph(
      'When a road is banked at angle θ, the normal force from the road tilts inward, so it can supply part (or all) of the centripetal force without relying on friction at all. At the "design speed" v, the horizontal component of the normal reaction alone provides exactly mv²/r.',
      title: 'Banking of roads',
    ),
    ContentBlock.formula('tanθ = v²/(rg)   (frictionless banked curve, design speed)', title: 'BANKING ANGLE'),
    ContentBlock.paragraph(
      'This is why highway curves and race tracks are banked — at speeds below the design speed a car tends to slide down the slope (needing friction up the slope to help), and above it the car tends to slide up and out (needing friction down the slope). Banking reduces reliance on tyre friction, which matters hugely in rain or ice.',
    ),
    ContentBlock.paragraph(
      'A conical pendulum is a bob on a string that swings around in a horizontal circle while the string traces a cone. Two forces act on the bob: gravity (mg, down) and tension T (along the string). Resolving tension into a vertical component (balancing gravity) and a horizontal component (supplying the centripetal force) gives a clean, classic pair of equations.',
      title: 'The conical pendulum',
    ),
    ContentBlock.formula('T cosθ = mg,   T sinθ = mv²/r   ⟹   tanθ = v²/(rg)', title: 'CONICAL PENDULUM EQUATIONS'),
    ContentBlock.realLife(
      'A washing machine\'s spin cycle, a Ferris wheel, the way you instinctively lean your bicycle into a turn (tilting your own "banking angle" so gravity and the ground\'s reaction supply the centripetal force), and the way pilots bank an aircraft to turn — all are the exact same equation, tanθ = v²/(rg), showing up in wildly different settings.',
    ),
    ContentBlock.jeeTip(
      'For "motion in a vertical circle" problems (a ball on a string looping vertically), the required centripetal force changes with position because gravity sometimes helps and sometimes opposes it. At the TOP of the loop the minimum speed for the string to stay taut is v_top = √(gr) (tension can drop to zero there, but not below). At the BOTTOM, tension must supply both centripetal force AND support against gravity: T_bottom − mg = mv²/r.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the "which force provides the centripetal force" recognition question directly: friction for a flat-curve car, tension for a whirling ball or conical pendulum, gravity for satellites and planets, the normal reaction (plus friction) for a banked curve. Always ask "what real force is doing the inward pulling here?" before writing any equation.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the velocity vector on a circle',
      math: 'v = ωr,   direction always tangent to the circle',
      note: 'Speed is constant but the tangent direction rotates continuously with angular velocity ω.',
    ),
    DerivationStep(
      title: 'Differentiate the velocity vector',
      math: 'a = dv/dt  → magnitude v²/r, directed toward the centre',
      note: 'This is a standard vector-calculus result: for uniform circular motion, acceleration is purely centripetal (no tangential component).',
    ),
    DerivationStep(
      title: 'Apply Newton\'s second law',
      math: 'F_net = ma = mv²/r,   directed toward the centre',
    ),
    DerivationStep(
      title: 'Rewrite using ω = v/r',
      math: 'F_net = m(ωr)²/r = mω²r',
      note: 'Useful when angular velocity, not speed, is given directly.',
    ),
    DerivationStep(
      title: 'Banking angle from force balance',
      math: 'N sinθ = mv²/r,   N cosθ = mg   ⟹   tanθ = v²/(rg)',
      note: 'Dividing the two equations eliminates both N and m — the banking angle depends only on v, r and g.',
    ),
  ],
  formulas: const [
    FormulaEntry('Centripetal acceleration', 'a_c = v²/r = ω²r'),
    FormulaEntry('Centripetal force', 'F_c = mv²/r = mω²r'),
    FormulaEntry('Period', 'T = 2πr/v = 2π/ω'),
    FormulaEntry('Banking angle (frictionless)', 'tanθ = v²/(rg)'),
    FormulaEntry('Conical pendulum', 'T cosθ = mg,  T sinθ = mv²/r'),
    FormulaEntry('Minimum speed at top of vertical loop', 'v_top = √(gr)', condition: 'string tension → 0'),
    FormulaEntry('Tension at bottom of vertical loop', 'T = mg + mv²/r'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A body moves in a circle at constant speed. Which statement is correct?',
      options: [
        'Its acceleration is zero because speed is constant',
        'Its velocity is constant',
        'It has a nonzero acceleration directed toward the centre',
        'The net force on it is zero',
      ],
      correctIndex: 2,
      solution: 'Constant speed does not mean constant velocity — direction keeps changing. This produces a centripetal acceleration v²/r toward the centre, requiring a nonzero net inward force.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For a ball whirled on a string in a horizontal circle, the centripetal force is supplied by:',
      options: ['Gravity', 'Friction', 'Tension in the string', 'A centrifugal force'],
      correctIndex: 2,
      solution: 'The string tension pulls the ball inward, toward the centre — that IS the centripetal force here. There is no separate centrifugal force acting on the ball in the ground frame.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A car of mass 1000 kg moves at 20 m/s around a flat circular curve of radius 100 m. The minimum friction force needed is:',
      options: ['200 N', '2000 N', '4000 N', '20000 N'],
      correctIndex: 2,
      solution: 'F = mv²/r = 1000 × 20² / 100 = 1000 × 400/100 = 4000 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A road is banked at angle θ for a design speed v with radius r, assuming no friction. If a car goes exactly at this speed v, the frictional force required is:',
      options: ['mg sinθ', 'mv²/r', 'Zero', 'mg cosθ'],
      correctIndex: 2,
      solution: 'At the design speed, tanθ = v²/(rg) is satisfied exactly by the normal reaction alone, so no friction is needed at all.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A conical pendulum bob moves in a horizontal circle of radius r with string length L making angle θ with the vertical. Its speed is:',
      options: ['v = √(gr)', 'v = √(gr tanθ)', 'v = √(gL)', 'v = √(gL sinθ)'],
      correctIndex: 1,
      solution: 'From tanθ = v²/(rg), rearranging gives v² = gr tanθ, so v = √(gr tanθ).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A student says: "When a car turns sharply, I feel pushed outward against the door — so there must be an outward centrifugal force acting on me." From the ground (inertial) frame, the correct explanation is:',
      options: [
        'The student is correct — an outward force acts on them',
        'The student\'s body tends to continue in a straight line (inertia) while the car curves inward beneath/around them; the door then pushes them inward',
        'There is no force at all, real or apparent',
        'Gravity is responsible for the sideways push',
      ],
      correctIndex: 1,
      solution: 'From the ground frame, only real forces exist. The student\'s inertia keeps their body moving in a straight line; the car (and eventually the door) curves around them and provides the inward force. The "outward push" is felt only because the door is pushing IN on the student, not because something is pushing them out.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A ball of mass m is whirled in a vertical circle of radius r using a string. The minimum speed at the topmost point for the string to remain taut is:',
      options: ['√(gr)', '√(2gr)', '√(gr/2)', '2√(gr)'],
      correctIndex: 0,
      solution: 'At the top, gravity alone can supply the centripetal force at minimum tension (T=0): mg = mv²/r ⟹ v = √(gr). Below this speed the string would go slack before reaching the top.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A car takes a banked curve (angle θ, radius r) with friction coefficient μ between tyres and road. The maximum speed before skidding (in terms of tanθ and μ) is given by v²_max/(rg) equal to:',
      options: [
        '(tanθ + μ)/(1 − μ tanθ)',
        '(tanθ − μ)/(1 + μ tanθ)',
        'tanθ · μ',
        '(1 + μ tanθ)/(tanθ − μ)',
      ],
      correctIndex: 0,
      solution: 'At maximum speed the car tends to slide up and out, so friction acts down the slope. Resolving forces along and perpendicular to the incline and eliminating N gives v²_max = rg(tanθ + μ)/(1 − μ tanθ) — a standard JEE result for banked curves with friction.',
    ),
  ],
  revision: [
    'Constant SPEED in a circle is not constant VELOCITY — direction changes continuously, so there is always a centripetal acceleration v²/r toward the centre.',
    'Centripetal force F = mv²/r = mω²r is not a new force — it is the net inward pull of whichever real force is present (tension, friction, gravity, normal reaction).',
    'There is no outward "centrifugal force" acting on the object in an inertial (ground) frame — that force only appears as a pseudo-force in a rotating frame.',
    'Banking: tanθ = v²/(rg) lets the normal reaction supply the centripetal force without relying on friction at the design speed.',
    'Conical pendulum: T cosθ = mg and T sinθ = mv²/r combine to give the same tanθ = v²/(rg).',
    'Vertical circular motion: minimum speed at the top is √(gr) (string tension → 0); at the bottom, tension = mg + mv²/r.',
    'Always ask first: "which real force is providing the centripetal pull here?" before setting up any circular-motion equation.',
  ],
  sandboxBuilder: (_) => const CircularMotionSandbox(),
);
