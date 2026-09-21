import '../../models/lesson.dart';
import '../../simulators/pseudo_forces_sandbox.dart';
import '../../theme/tokens.dart';

/// Pseudo Forces — the "fake" forces that only exist because YOUR frame is accelerating.
final Lesson pseudoForcesLesson = Lesson(
  topicId: 'pseudo-forces',
  title: 'Pseudo Forces',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A lift accelerates upward and you suddenly feel heavier, pressed into the floor. But no new object touched you, and nothing pulled harder — so what, exactly, is pressing on you?',
  whyItMatters:
      'Every "lift problem," "train problem" and "rotating frame problem" in JEE/NEET hinges on one decision: which reference frame are you working in, and did you remember to add the pseudo-force if it is non-inertial? Get this right and lift/apparent-weight questions, banking problems solved from a car\'s own frame, and centrifugal-force questions all become the same short recipe. Get it wrong and you double-count or miss forces entirely.',
  prediction: const PredictionPrompt(
    scenario:
        'You stand on a weighing scale inside a lift that begins accelerating UPWARD. What happens to the reading on the scale compared to when the lift was at rest?',
    options: [
      'The reading decreases — you feel lighter',
      'The reading stays exactly the same — the lift\'s motion doesn\'t affect weight',
      'The reading increases — you feel heavier',
      'The reading drops to zero — you feel weightless',
    ],
    correctIndex: 2,
    reveal:
        'From the ground frame: N − mg = ma (a is upward, positive), so N = m(g+a) — the scale reads MORE than mg. In the lab, drag the acceleration slider to a positive value and watch the apparent-weight meter climb above your true weight mg. Switch to the "lift frame" view and see the same result explained differently: a downward pseudo-force ma appears (added to real gravity) purely because the lift frame is accelerating upward, and it is this fictitious extra "weight" that presses you into the floor.',
  ),
  experiments: [
    'Set a = +4 m/s² (accelerating upward) and watch the apparent weight rise above mg',
    'Set a = −4 m/s² (accelerating downward) and watch the apparent weight drop below mg',
    'Push a all the way to −9.8 m/s² (free fall) and see the apparent weight hit zero — true weightlessness',
    'Toggle between "ground frame" and "lift frame" at the same acceleration — the apparent weight reading never changes, only the explanation (and the pseudo-force arrow) changes',
    'Increase the mass slider and confirm both N and the pseudo-force scale up in direct proportion to m',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Newton\'s laws, in their simple F=ma form, are valid only in an INERTIAL frame — one that is not accelerating (including not rotating). Inside a frame that IS accelerating (a lift speeding up, a car braking, a merry-go-round spinning), objects at rest relative to that frame appear to violate F=ma unless we invent an extra force to patch the bookkeeping. That invented force is called a pseudo-force (or fictitious force).',
      title: 'Inertial vs non-inertial frames',
    ),
    ContentBlock.formula('F_pseudo = −m·a_frame   (opposite to the frame\'s own acceleration)', title: 'PSEUDO-FORCE FORMULA'),
    ContentBlock.bullets([
      'Magnitude = mass of the object × acceleration of the (non-inertial) frame',
      'Direction is always OPPOSITE to the frame\'s acceleration',
      'It acts on every object described within that frame, in proportion to its mass — just like gravity',
      'It is needed ONLY when you choose to analyse motion from inside the accelerating frame',
    ]),
    ContentBlock.paragraph(
      'A pseudo-force is not caused by any physical interaction — no rope, surface or field produces it. Because of this it has no source object and no Newton\'s-third-law reaction partner, and it does no real work on the universe (energy is not actually being transferred by it) even though it correctly predicts the object\'s acceleration and any real forces (like an increased normal reaction) that arise because of it.',
      title: 'Why it is "fictitious"',
    ),
    ContentBlock.paragraph(
      'For a lift accelerating with acceleration a (taking upward as positive), analysing a person of mass m standing on a scale from the GROUND frame gives N − mg = ma, so N = m(g+a). From the LIFT frame, the person is in equilibrium (at rest relative to the lift), so we must add a downward pseudo-force ma to balance: N − mg − ma = 0, giving the identical N = m(g+a). Both frames agree on what the scale reads — they just explain it differently.',
      title: 'The classic lift (elevator) problem',
    ),
    ContentBlock.formula('N = m(g + a)  [lift accelerating up]     N = m(g − a)  [lift accelerating down]', title: 'APPARENT WEIGHT IN A LIFT'),
    ContentBlock.bullets([
      'Lift accelerating UPWARD (a>0): apparent weight INCREASES, N = m(g+a)',
      'Lift accelerating DOWNWARD (a>0 downward): apparent weight DECREASES, N = m(g−a)',
      'Lift in free fall (a = g downward): N = 0 — total weightlessness, exactly like an astronaut in orbit',
      'Lift moving at CONSTANT velocity (a=0), up or down: apparent weight = mg, completely normal — only acceleration matters, not velocity',
    ]),
    ContentBlock.paragraph(
      'A rotating frame (like a spinning platform, or a car going round a curve as seen by someone sitting inside it) is also non-inertial, since velocity direction is constantly changing. In that frame, an outward pseudo-force called the centrifugal force = mω²r (directed away from the centre) must be added for objects that appear stationary in the rotating frame. This is the ONLY situation in which "centrifugal force" is a legitimate term — see the Circular Motion topic for why it must never be used in the ground/inertial frame.',
      title: 'Centrifugal force: a pseudo-force in a rotating frame',
    ),
    ContentBlock.realLife(
      'That falling-in-your-stomach feeling when an elevator starts moving down, seatbelt pressing you sideways as a car turns fast, being pressed back into your seat as a plane accelerates for takeoff, and true weightlessness felt by astronauts in orbit (they and their spacecraft are both in continuous free fall, so there is no relative acceleration and hence no apparent weight) — all of these are pseudo-force experiences of accelerating frames.',
    ),
    ContentBlock.mistake(
      'Adding a pseudo-force AND analysing from the ground frame at the same time. Pick ONE frame per solution: either work in the ground (inertial) frame using only real forces, or work in the accelerating frame and add exactly one pseudo-force (−ma) per object. Mixing the two double-counts or under-counts the acceleration effect.',
    ),
    ContentBlock.mistake(
      'Believing a pseudo-force has a reaction pair, or that it can do real work on a system as a whole. Since it has no physical source, Newton\'s third law does not apply to it, and any work-energy accounting of the SYSTEM should ultimately be checked in an inertial frame to avoid confusion.',
    ),
    ContentBlock.example(
      'A 50 kg person stands on a scale in a lift accelerating downward at 2 m/s². What does the scale read?\n\nGround frame: N − mg = m(−a), taking up as positive and lift accelerating down means net acceleration is −2 m/s².\nN = mg − ma = 50(9.8) − 50(2) = 490 − 100 = 390 N.\n\nThe scale reads 390 N, noticeably less than the true weight of 490 N — the person feels lighter, though not weightless (since a < g).',
    ),
    ContentBlock.jeeTip(
      'For problems with a block on a wedge that itself accelerates horizontally (a "moving wedge" problem), it is often far faster to jump into the wedge\'s frame, add the horizontal pseudo-force −Ma to every object on it, and then solve a simple statics/dynamics problem — rather than juggling relative accelerations in the ground frame.',
    ),
    ContentBlock.neetNote(
      'NEET loves the direct-recall lift formulas: N=m(g+a) accelerating up, N=m(g−a) accelerating down, and N=0 in free fall. Also remember: at CONSTANT velocity (up or down), apparent weight = true weight mg exactly — this is the most common "trick" distractor option.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write Newton\'s second law in the ground (inertial) frame',
      math: 'N − mg = ma_lift',
      note: 'a_lift is the lift\'s acceleration, positive upward. N is the true, physical normal reaction — this equation is exact and needs no pseudo-force.',
    ),
    DerivationStep(
      title: 'Solve for the scale reading N',
      math: 'N = m(g + a_lift)',
      note: 'This is the ONLY equation you need if you stay in the ground frame.',
    ),
    DerivationStep(
      title: 'Now switch to the lift\'s own (non-inertial) frame',
      math: 'In this frame the person is in equilibrium: ΣF = 0',
      note: 'But if we only include N (up) and mg (down), N − mg = 0 wrongly predicts N = mg always — this frame needs a correction.',
    ),
    DerivationStep(
      title: 'Add the pseudo-force to restore consistency',
      math: 'N − mg − m·a_lift = 0   (pseudo-force = −m·a_lift, i.e. downward when lift accelerates up)',
      note: 'The pseudo-force is defined exactly so that this equation reproduces the correct N.',
    ),
    DerivationStep(
      title: 'Confirm both frames agree',
      math: 'N = m(g + a_lift)   — identical to the ground-frame result',
      note: 'Both frames must always agree on measurable, physical quantities like the scale reading — only the bookkeeping of forces differs.',
    ),
  ],
  formulas: const [
    FormulaEntry('Pseudo-force', 'F_pseudo = −m·a_frame'),
    FormulaEntry('Apparent weight, lift accelerating up', 'N = m(g + a)'),
    FormulaEntry('Apparent weight, lift accelerating down', 'N = m(g − a)'),
    FormulaEntry('Free-fall lift (a = g down)', 'N = 0  (weightlessness)'),
    FormulaEntry('Centrifugal pseudo-force (rotating frame)', 'F_cf = mω²r', condition: 'directed away from centre, valid only in the rotating frame'),
    FormulaEntry('Constant-velocity lift (a = 0)', 'N = mg  (no change from rest)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A pseudo-force is needed when analysing motion from:',
      options: [
        'Any reference frame at all',
        'An inertial (non-accelerating) frame only',
        'A non-inertial (accelerating or rotating) frame',
        'Never — Newton\'s laws always work directly',
      ],
      correctIndex: 2,
      solution: 'Pseudo-forces are bookkeeping devices needed only when you choose to apply F=ma inside a frame that is itself accelerating or rotating (non-inertial).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A lift moves upward at a CONSTANT velocity of 5 m/s. A 60 kg person\'s apparent weight is:',
      options: ['Less than 60g', 'Exactly 60g', 'More than 60g', 'Zero'],
      correctIndex: 1,
      solution: 'Constant velocity means acceleration = 0, so N = m(g+0) = mg — apparent weight equals true weight, regardless of how fast the lift moves.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A 40 kg person stands on a scale in a lift accelerating upward at 2 m/s² (g = 10 m/s²). The scale reads:',
      options: ['320 N', '400 N', '480 N', '600 N'],
      correctIndex: 2,
      solution: 'N = m(g+a) = 40(10+2) = 40×12 = 480 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A lift is in free fall (cable snapped). A person inside experiences apparent weight equal to:',
      options: ['mg', '2mg', 'Zero', 'mg/2'],
      correctIndex: 2,
      solution: 'In free fall a = g downward, so N = m(g−a) = m(g−g) = 0. The person and lift accelerate identically, so there is no relative pressing force — total weightlessness.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Which of the following is TRUE of a pseudo-force?',
      options: [
        'It has an equal-and-opposite reaction force on some other body',
        'It arises from a real physical interaction like tension or gravity',
        'It has no reaction pair and exists only in non-inertial frames',
        'It is the same in every reference frame',
      ],
      correctIndex: 2,
      solution: 'Pseudo-forces are fictitious bookkeeping forces with no physical source, so Newton\'s third law does not apply to them, and they vanish entirely in an inertial frame.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'In the lift frame, a person of mass m appears in equilibrium while the lift accelerates upward at a. The pseudo-force used in this frame is:',
      options: ['ma, upward', 'ma, downward', 'mg, downward', 'Zero — no pseudo-force needed'],
      correctIndex: 1,
      solution: 'F_pseudo = −m·a_frame. Since the lift accelerates upward, the pseudo-force is directed downward, with magnitude ma — added on top of real gravity mg.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A block of mass m rests on a rough horizontal floor inside a truck that suddenly accelerates forward with acceleration a. Analysed in the truck\'s (non-inertial) frame, the block tends to slide backward because of:',
      options: [
        'A real force pushing it backward from the floor',
        'A pseudo-force of magnitude ma acting backward (opposite to the truck\'s forward acceleration)',
        'Gravity acting at an angle',
        'The block\'s own inertia acting as a real force in every frame',
      ],
      correctIndex: 1,
      solution: 'In the truck frame, a backward pseudo-force ma appears (opposite to the truck\'s forward acceleration a). If this exceeds the maximum available static friction, the block slides backward relative to the truck bed — matching what is actually just the block "staying behind" due to inertia as seen from the ground.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A conical pendulum is analysed from the rotating frame attached to the bob itself. In this frame, which forces balance to give equilibrium?',
      options: [
        'Only gravity and tension',
        'Gravity, tension, and an inward centripetal force',
        'Gravity, tension, and an outward centrifugal pseudo-force mω²r',
        'Only the centrifugal force, since gravity is negligible',
      ],
      correctIndex: 2,
      solution: 'In the rotating (bob-attached) frame, the bob is at rest, so real forces (gravity mg down, tension T along the string) must be balanced by the outward centrifugal pseudo-force mω²r for the frame\'s equilibrium equations to hold.',
    ),
  ],
  revision: [
    'Pseudo-forces exist only in non-inertial (accelerating or rotating) frames; they vanish completely in an inertial frame.',
    'F_pseudo = −m·a_frame — magnitude m times the frame\'s acceleration, direction always opposite to it.',
    'Lift problems: N = m(g+a) accelerating up, N = m(g−a) accelerating down, N = mg at constant velocity, N = 0 in free fall.',
    'Centrifugal force (mω²r, outward) is a real, usable pseudo-force ONLY in a rotating frame — never write it as a force acting on the object in the ground frame.',
    'A pseudo-force has no physical source, so it has no Newton\'s-third-law reaction partner and does no real work on the system.',
    'Always pick ONE frame (inertial with only real forces, OR non-inertial with real forces + pseudo-force) and never mix the two in one equation.',
  ],
  sandboxBuilder: (_) => const PseudoForcesSandbox(),
);
