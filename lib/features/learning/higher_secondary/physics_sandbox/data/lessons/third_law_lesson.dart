import '../../models/lesson.dart';
import '../../simulators/third_law_sim.dart';
import '../../theme/tokens.dart';

/// Newton's Third Law — action-reaction pairs, and why they never cancel for one body.
final Lesson newtonThirdLawLesson = Lesson(
  topicId: 'newton-third-law',
  title: 'Newton\'s Third Law',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'When you push against a wall, the wall pushes back on you with an equal force — but if the two forces are always exactly equal and opposite, how does anything ever accelerate? Shouldn\'t everything just cancel out to zero?',
  whyItMatters:
      'This is the single most misunderstood law in all of mechanics, and JEE/NEET both love to exploit that confusion. Understanding that action-reaction pairs act on DIFFERENT bodies (so they never cancel for either body alone) unlocks rocket propulsion, walking, recoil, and every "why doesn\'t it move" trick question in the syllabus.',
  prediction: const PredictionPrompt(
    scenario:
        'A person stands on frictionless ice and pushes hard against a wall. The wall pushes back on the person with an equal and opposite force. What happens to the person?',
    options: [
      'Nothing — the forces cancel and the person stays still',
      'The person accelerates away from the wall',
      'The person accelerates toward the wall',
      'It depends on how hard the wall pushes back',
    ],
    correctIndex: 1,
    reveal:
        'The action (person pushes wall) and reaction (wall pushes person) act on TWO DIFFERENT bodies, so they never cancel for either one. Only the reaction force — the wall pushing the person — acts on the person, and it pushes them backward, away from the wall. In the lab, push the movable block against the fixed wall and watch it recoil; the wall never moves because it\'s fixed to the Earth, but the block clearly accelerates.',
  ),
  experiments: [
    'Push the free block against the wall and watch it recoil away — the reaction force is real and unbalanced ON the block',
    'Compare a light block and heavy block pushing off each other — lighter one flies off faster (same force, less mass)',
    'Fire the "rocket" object and watch exhaust go one way, rocket the other — measure both momenta',
    'Try to find a force in the sim that acts on the SAME body as its pair — you can\'t, because they never do',
    'Turn on the force-pair vector overlay and confirm the two arrows are equal length, opposite direction, on different objects',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Newton\'s third law states: for every action there is an equal and opposite reaction. More precisely — if body A exerts a force on body B, then body B simultaneously exerts a force of the same magnitude, in the opposite direction, on body A. These two forces are called an action-reaction pair, and they always act on two DIFFERENT objects, never on the same one.',
      title: 'Forces always come in pairs',
    ),
    ContentBlock.formula('F_AB = −F_BA', title: 'NEWTON\'S THIRD LAW'),
    ContentBlock.bullets([
      'The two forces in a pair are equal in magnitude and opposite in direction',
      'They act on DIFFERENT bodies — A on B, and B on A',
      'They act simultaneously — neither force is the "cause" that happens first',
      'They are of the SAME TYPE (both contact forces, or both gravitational, etc.) but never the same force counted twice',
    ]),
    ContentBlock.paragraph(
      'Because the two forces of a pair act on different bodies, they can never cancel each other out for a single object\'s equation of motion. To decide whether a body accelerates, you only ever add up the forces acting ON that body — never mix in the reaction forces that body exerts on something else. This is why pushing a wall accelerates you even though "the forces are equal and opposite": the wall\'s push is entirely yours to keep.',
      title: 'Why action-reaction pairs never produce equilibrium for one body',
    ),
    ContentBlock.realLife(
      'A rocket in the vacuum of space has nothing to "push off" except its own exhaust gas. The rocket pushes hot gas backward (action); the gas pushes the rocket forward with equal force (reaction). Since the reaction acts on the rocket alone, the rocket accelerates forward — no air or ground is needed, which is exactly why rockets work in space.',
    ),
    ContentBlock.realLife(
      'Walking works the same way: your foot pushes backward on the ground (action); the ground pushes forward on your foot (reaction), and that reaction is what propels YOU forward. This is also why walking is impossible on frictionless ice — without friction, your foot can\'t exert a backward push on the ground, so there\'s no forward reaction to receive.',
    ),
    ContentBlock.mistake(
      'Thinking that action and reaction forces act on the SAME body and therefore cancel out, preventing any motion. This is the most common misconception in mechanics. If they acted on the same object, nothing could ever accelerate by pushing off anything — walking, swimming, and rockets would all be impossible. They act on different bodies and never cancel for either one.',
    ),
    ContentBlock.mistake(
      'Confusing an action-reaction pair with a pair of BALANCED forces on one object (like weight and normal reaction on a book on a table). Weight and normal force both act on the SAME book, are of DIFFERENT physical origin (gravity vs. contact), and only happen to be equal because the book is in equilibrium — they are not a third-law pair, which must be same-type, different-body, and equal by law, not by coincidence.',
    ),
    ContentBlock.example(
      'A 5 kg gun fires a 0.02 kg bullet at 400 m/s. Find the recoil speed of the gun.\n\nAction: gun pushes bullet forward. Reaction: bullet pushes gun backward with equal force, for equal time — so the IMPULSE on each is equal and opposite, giving equal and opposite momentum change.\n\nm_bullet·v_bullet = m_gun·v_recoil\n0.02 × 400 = 5 × v_recoil\nv_recoil = 8/5 = 1.6 m/s, directed opposite to the bullet.',
    ),
    ContentBlock.jeeTip(
      'The third law, applied over the SAME time interval, gives conservation of momentum for an isolated system: since F_AB = −F_BA at every instant, integrating over time gives J_AB = −J_BA, i.e., Δp_A = −Δp_B, so total momentum p_A + p_B stays constant. Whenever a JEE problem features an internal collision, explosion, or recoil with no external force, momentum conservation is really the third law in disguise.',
    ),
    ContentBlock.neetNote(
      'NEET likes direct identification questions: "Which pair is a third-law pair?" Always check three things — same TYPE of force, acting on DIFFERENT bodies, and equal/opposite by definition (not by circumstance). Weight-and-normal-reaction on one block is NOT a third-law pair; weight-of-Earth-on-block and weight-of-block-on-Earth IS.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Consider an isolated system of two bodies A and B',
      math: 'F_ext = 0  (no external force on the pair)',
      note: 'Only the mutual force between A and B acts within the system.',
    ),
    DerivationStep(
      title: 'Apply the third law to the mutual forces',
      math: 'F_AB = −F_BA',
      note: 'The force A exerts on B is equal and opposite to the force B exerts on A.',
    ),
    DerivationStep(
      title: 'Relate each force to the rate of change of momentum',
      math: 'F_BA = dp_A/dt,   F_AB = dp_B/dt',
      note: 'By the second law, the force ON A changes A\'s momentum, and likewise for B.',
    ),
    DerivationStep(
      title: 'Substitute into the third law equation',
      math: 'dp_B/dt = −dp_A/dt  ⟹  d(p_A + p_B)/dt = 0',
    ),
    DerivationStep(
      title: 'Integrate to get conservation of momentum',
      math: 'p_A + p_B = constant',
      note: 'This is why an internal explosion (like a gun firing) conserves total momentum — the third law guarantees it.',
    ),
  ],
  formulas: const [
    FormulaEntry('Third law', 'F_AB = −F_BA'),
    FormulaEntry('Equal and opposite impulse', 'J_AB = −J_BA'),
    FormulaEntry('Momentum conservation (isolated pair)', 'p_A + p_B = constant'),
    FormulaEntry('Recoil condition', 'm₁v₁ = m₂v₂  (equal and opposite momenta from rest)'),
    FormulaEntry('Rocket thrust', 'F = u·(dm/dt)', condition: 'u = exhaust speed relative to rocket'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Newton\'s third law states that action and reaction forces:',
      options: [
        'Act on the same body and cancel out',
        'Act on different bodies and are equal and opposite',
        'Act on different bodies but are not necessarily equal',
        'Act only in collisions',
      ],
      correctIndex: 1,
      solution: 'Action and reaction are equal in magnitude, opposite in direction, and always act on two different bodies.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A book rests on a table. The normal reaction from the table on the book forms a third-law pair with:',
      options: [
        'The weight of the book',
        'The force the book exerts on the table',
        'The friction on the book',
        'Nothing — it has no pair',
      ],
      correctIndex: 1,
      solution:
          'The third-law pair of "table pushes book up" is "book pushes table down" — same type of force (contact/normal), acting on different bodies. Weight and normal reaction, though equal here, act on the SAME book and are not a third-law pair.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A swimmer pushes water backward to move forward. This is best explained by:',
      options: [
        'Newton\'s first law',
        'Newton\'s second law',
        'Newton\'s third law',
        'Law of conservation of energy',
      ],
      correctIndex: 2,
      solution:
          'The swimmer\'s hand pushes water backward (action); the water pushes the swimmer forward (reaction) — a direct application of the third law.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A gun of mass 4 kg fires a bullet of mass 0.05 kg with a muzzle velocity of 200 m/s. The recoil velocity of the gun is:',
      options: ['1 m/s', '2.5 m/s', '4 m/s', '0.4 m/s'],
      correctIndex: 1,
      solution:
          'Momentum conservation: 0 = m_bullet·v_bullet + m_gun·v_recoil (opposite signs). 0.05×200 = 4×v_recoil → v_recoil = 10/4 = 2.5 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Why can a rocket accelerate in the vacuum of space, where there is nothing to push against?',
      options: [
        'It pushes against the vacuum itself',
        'It pushes exhaust gas backward, and the gas pushes the rocket forward by the third law',
        'It uses air resistance from the atmosphere left behind',
        'It cannot accelerate in a true vacuum',
      ],
      correctIndex: 1,
      solution:
          'The rocket only needs to push its own exhaust gas; by the third law the gas pushes back on the rocket with equal force. No external medium (air or ground) is required.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two ice skaters, masses 40 kg and 60 kg, stand at rest facing each other and push off. The 40 kg skater moves at 3 m/s. The 60 kg skater\'s speed is:',
      options: ['1 m/s', '2 m/s', '3 m/s', '4.5 m/s'],
      correctIndex: 1,
      solution:
          'Momentum conservation (system starts at rest, so total momentum stays zero): 40×3 = 60×v → v = 120/60 = 2 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A man of mass 60 kg is standing on a stationary boat of mass 140 kg on frictionless water. He walks 4 m toward the front of the boat. If there is no external horizontal force, the boat moves:',
      options: [
        'Not at all',
        '4 m in the same direction as the man',
        'Some distance opposite to the man\'s motion, so the centre of mass stays fixed',
        '4 m in the direction opposite to the man',
      ],
      correctIndex: 2,
      solution:
          'The man pushes the boat backward (action) while the boat pushes him forward (reaction) — an internal third-law pair, so total momentum (and centre of mass) stays fixed. The boat recoils backward by an amount that keeps the system\'s centre of mass stationary: distance = (60/200)×4 = 1.2 m opposite to the man.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A block A is placed on block B, which rests on the ground. Consider the pair "weight of A" and "normal force of B on A." This pair is:',
      options: [
        'A third-law pair, since they are equal and opposite',
        'Not a third-law pair — both act on the same body A, and are different types of force',
        'A third-law pair only if A is in equilibrium',
        'A third-law pair because B supports A',
      ],
      correctIndex: 1,
      solution:
          'Both forces act on the SAME body (A), and are of different physical origin (gravitational vs. contact). A genuine third-law pair must act on two different bodies and be of the same type — this pair fails both tests, even though the magnitudes happen to match in equilibrium.',
    ),
  ],
  revision: [
    'For every action there is an equal and opposite reaction — acting on a DIFFERENT body, never the same one.',
    'Action-reaction pairs never cancel for a single object; only forces ON that object determine its motion.',
    'Weight and normal reaction on the same block are equal by equilibrium, NOT a third-law pair (different force types, same body).',
    'Rockets, swimming, and walking all work by pushing something else backward to receive a forward reaction.',
    'The third law, applied over time, is the reason total momentum is conserved in an isolated system.',
    'To identify a genuine third-law pair: same type of force, opposite bodies, equal and opposite by definition.',
  ],
  sandboxBuilder: (_) => const ThirdLawSimulator(),
);
