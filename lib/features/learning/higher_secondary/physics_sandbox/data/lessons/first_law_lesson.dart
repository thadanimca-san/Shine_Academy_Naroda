import '../../models/lesson.dart';
import '../../simulators/first_law_sim.dart';
import '../../theme/tokens.dart';

/// Newton's First Law — inertia, and why "no force" doesn't mean "no motion".
final Lesson newtonFirstLawLesson = Lesson(
  topicId: 'newton-first-law',
  title: 'Newton\'s First Law',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'You give a puck a push on frictionless ice and let go. No one is touching it anymore — so what keeps it moving, and why does it never speed up or curve on its own?',
  whyItMatters:
      'Every dynamics problem before you can even write F = ma starts with this question: is the object in equilibrium, or not? Newton\'s first law defines what "no net force" actually looks like (constant velocity, not rest!) and sets up the entire idea of an inertial frame that the rest of mechanics quietly assumes. Skip this and "pseudo-force" questions in JEE will feel like magic instead of bookkeeping.',
  prediction: const PredictionPrompt(
    scenario:
        'A hockey puck is sliding across frictionless ice at constant velocity. No one is pushing it. What net force is acting on it right now?',
    options: [
      'A large forward force, otherwise it would stop',
      'A small forward force just enough to balance friction',
      'Zero net force',
      'A force that decreases with time as the puck "runs out of push"',
    ],
    correctIndex: 2,
    reveal:
        'Zero net force is required to keep something moving at constant velocity — that IS Newton\'s first law. The everyday feeling that "motion needs a force to continue" comes from friction being present almost everywhere we look. In the lab, drag friction down to zero and give the block a shove: watch it cruise forever at the same speed, needing nothing to sustain it.',
  ),
  experiments: [
    'Set friction to zero, give the block a push, and watch it never slow down',
    'Slowly increase friction and watch the same push now decay to rest',
    'With friction at zero, try to make the block curve or speed up without applying a force — it can\'t be done',
    'Yank the surface sideways under a resting block — watch the block "lag behind" (an inertia demo)',
    'Compare a light block and a heavy block given the same push — the heavier one resists a change in its velocity more',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Newton\'s first law states that a body continues in its state of rest, or of uniform motion in a straight line, unless acted upon by a net external force. Read that carefully: "rest" and "uniform motion" are treated as the SAME natural state. There is nothing special about being at rest — an object cruising at constant velocity is just as free of net force as one sitting still.',
      title: 'The law of inertia',
    ),
    ContentBlock.formula('F_net = 0  ⟺  v = constant (including v = 0)', title: 'NEWTON\'S FIRST LAW'),
    ContentBlock.bullets([
      'Inertia is the tendency of a body to resist any change in its state of motion',
      'Mass is the quantitative MEASURE of inertia — more mass, more resistance to a change in velocity',
      'The law is really a definition: it tells us which reference frames are allowed (inertial frames)',
      '"Uniform motion" means constant speed AND constant direction — a straight line, not a curve',
    ]),
    ContentBlock.paragraph(
      'An inertial frame is one in which the first law actually holds — a free (unforced) body observed from that frame moves at constant velocity. The ground is a good approximation to an inertial frame for everyday problems. A frame that is accelerating (a braking bus, a spinning merry-go-round) is a non-inertial frame: objects inside it appear to accelerate even with no real force acting, which is why we must invent "pseudo-forces" to make Newton\'s laws work there.',
      title: 'Inertial vs non-inertial frames',
    ),
    ContentBlock.realLife(
      'The tablecloth trick: yank a tablecloth out fast enough and the plates barely move. The short yank gives the cloth a large but brief force; the plates\' inertia means they need a much bigger impulse to pick up noticeable speed in that tiny time, so they mostly stay put while the cloth slides out from under them.',
    ),
    ContentBlock.realLife(
      'A seatbelt exists because of inertia. When a car crashes and suddenly decelerates, your body — having no force acting to slow IT down — keeps moving forward at the car\'s original speed until something (ideally the belt, not the windshield) supplies the force to change that.',
    ),
    ContentBlock.mistake(
      'Believing a constant force is needed to keep something moving at constant velocity. This was Aristotle\'s view, and it feels intuitive because friction is everywhere. But zero net force gives constant velocity, not zero velocity — a moving object with no applied force does not stop, it keeps going forever (as it would in deep space).',
    ),
    ContentBlock.mistake(
      'Forgetting that "at rest" is not more natural than "moving at constant velocity." Students often assume a body must eventually come to rest "because that\'s natural." It only comes to rest because a net force (usually friction) acts on it — remove that force and it never would.',
    ),
    ContentBlock.example(
      'A 2 kg block slides on a frictionless surface at 3 m/s. What net force must act on it to keep it moving at 3 m/s for the next 10 s?\n\nBy the first law, zero net force is needed — the block continues at 3 m/s on its own. If any force acted, however small, the velocity would change; the problem is really testing whether you know that "moving" does not require "pushing."',
    ),
    ContentBlock.jeeTip(
      'Whenever a problem says "frame attached to an accelerating lift/car/train," you are being asked to work in a non-inertial frame. Add a pseudo-force = −m·a_frame (opposite to the frame\'s acceleration) to every object in that frame, then apply Newton\'s laws normally. This trick converts a hard problem into a familiar equilibrium one.',
    ),
    ContentBlock.neetNote(
      'NEET often tests the law of inertia through direct scenario questions (why passengers lurch forward when a bus brakes suddenly, why dust is dislodged by beating a carpet). The passenger\'s body keeps moving at the bus\'s original speed while the bus decelerates — that IS inertia, no separate "jerk force" needed in your explanation.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the definition of a free body',
      math: 'A body is "free" if F_net = 0',
      note: 'This is the condition the first law describes.',
    ),
    DerivationStep(
      title: 'Connect force to acceleration (previewing the 2nd law)',
      math: 'F_net = m·a',
      note: 'Even though the 2nd law formalises this, the 1st law is really the special case F_net = 0.',
    ),
    DerivationStep(
      title: 'Set F_net = 0 and solve for acceleration',
      math: '0 = m·a  ⟹  a = 0  (since m ≠ 0)',
    ),
    DerivationStep(
      title: 'Interpret zero acceleration',
      math: 'a = dv/dt = 0  ⟹  v = constant vector',
      note: 'Constant vector means both speed AND direction are unchanging — straight-line, uniform motion.',
    ),
    DerivationStep(
      title: 'State the law',
      math: 'F_net = 0  ⟺  v = constant',
      note: 'This equivalence is Newton\'s first law — it also defines what we mean by an inertial frame.',
    ),
  ],
  formulas: const [
    FormulaEntry('First law condition', 'F_net = 0  ⟺  v = constant'),
    FormulaEntry('Inertia measure', 'm  (larger m → more resistance to Δv)'),
    FormulaEntry('Pseudo-force (non-inertial frame)', 'F_pseudo = −m·a_frame'),
    FormulaEntry('Zero acceleration condition', 'a = dv/dt = 0'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Newton\'s first law is also known as the law of:',
      options: ['Momentum', 'Inertia', 'Action-reaction', 'Gravitation'],
      correctIndex: 1,
      solution:
          'The first law defines inertia — the resistance of a body to a change in its state of motion — and is called the law of inertia.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A body moving at constant velocity in a straight line has:',
      options: [
        'A constant net force acting on it',
        'Zero net force acting on it',
        'A net force proportional to its speed',
        'An increasing net force',
      ],
      correctIndex: 1,
      solution: 'Constant velocity means zero acceleration, and by F = ma, zero net force.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'When a bus suddenly starts moving forward, standing passengers tend to fall backward because:',
      options: [
        'A backward force pushes them',
        'Their feet move with the bus but their upper body, due to inertia, tends to stay at rest',
        'The bus pushes air backward onto them',
        'Friction acts backward on their body',
      ],
      correctIndex: 1,
      solution:
          'The feet (in contact with the floor) are forced forward with the bus, but the rest of the body resists the sudden change in motion due to inertia, so it appears to fall backward relative to the bus.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Which of these is an example of inertia of rest?',
      options: [
        'A person jumping out of a moving bus falls forward',
        'Dust particles fall off a carpet when it is beaten',
        'A cyclist leans while turning',
        'A rocket accelerates upward due to exhaust gases',
      ],
      correctIndex: 1,
      solution:
          'Beating the carpet suddenly moves the fabric; the dust particles, at rest, tend to stay at rest (inertia of rest) and separate from the moving carpet, falling off.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A frame of reference in which Newton\'s first law holds true is called:',
      options: ['A non-inertial frame', 'A rotating frame', 'An inertial frame', 'A rigid frame'],
      correctIndex: 2,
      solution:
          'By definition, an inertial frame is one where an unforced (free) body is observed to move at constant velocity, consistent with the first law.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'In a lift accelerating upward at a, a plumb bob hung from the ceiling appears (to an observer inside the lift) to experience an extra force of magnitude:',
      options: ['mg', 'ma, directed downward', 'ma, directed upward', 'zero, since the bob is in equilibrium'],
      correctIndex: 1,
      solution:
          'The lift is a non-inertial frame accelerating upward at a, so a pseudo-force of magnitude ma acts downward (opposite to the frame\'s acceleration) on every object inside it, including the bob.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A block rests on a frictionless cart that itself accelerates forward at 2 m/s² on a frictionless floor. In the ground (inertial) frame, the horizontal force needed to keep the block stationary RELATIVE TO the cart is provided by:',
      options: [
        'Friction between block and cart',
        'A wall or peg on the cart pushing the block forward',
        'Nothing — the first law says no force is needed',
        'The weight of the block',
      ],
      correctIndex: 1,
      solution:
          'The floor is frictionless, so nothing horizontal acts on the block unless the cart physically pushes it (e.g., a wall). Without that push, the first law says the block continues at constant velocity while the cart accelerates away beneath it — it would NOT stay put on the cart.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A satellite moves in a circular orbit at constant speed. Is it consistent with Newton\'s first law that no force acts on it?',
      options: [
        'Yes, because its speed is constant',
        'No — its velocity (direction) is continuously changing, so a net force (gravity) must act on it',
        'Yes, because it is in space with no friction',
        'No — the first law does not apply to orbital motion',
      ],
      correctIndex: 1,
      solution:
          'The first law concerns velocity, a vector. Even at constant speed, a circular path means the direction — and hence velocity — is always changing, which requires a net centripetal force (gravity here). Uniform circular motion is NOT "no force" motion.',
    ),
  ],
  revision: [
    'A body stays at rest or in uniform straight-line motion unless a net external force acts on it.',
    'Rest and constant-velocity motion are the SAME state as far as force is concerned — both mean F_net = 0.',
    'Inertia is resistance to a change in velocity; mass is its quantitative measure.',
    'An inertial frame is one where a free body genuinely moves at constant velocity.',
    'In a non-inertial (accelerating) frame, add a pseudo-force F = −m·a_frame to make Newton\'s laws work.',
    'Motion never "needs" a force to continue — only a CHANGE in motion needs a force.',
    'Tablecloth trick and seatbelts both exploit inertia: matter resists sudden changes in its velocity.',
  ],
  sandboxBuilder: (_) => const FirstLawSimulator(),
);
