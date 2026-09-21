import '../../models/lesson.dart';
import '../../simulators/collision_lab_sim.dart';

/// Collisions — the first lesson built on the discovery-first shell.
final Lesson collisionsLesson = Lesson(
  topicId: 'collisions',
  title: 'Collisions',
  bigQuestion:
      'A truck and a cycle crash head-on. The forces they exert on each other are exactly equal — so why does the cycle suffer more?',
  whyItMatters:
      'Collisions are where Newton\'s laws show their real power. One idea — momentum conservation — lets you predict the outcome of any crash, explosion or rebound without knowing anything about the messy forces involved. JEE and NEET both love this chapter because a single principle solves a huge variety of problems.',
  prediction: const PredictionPrompt(
    scenario:
        'A heavy cart (4 kg) moving right at 4 m/s hits a light cart (1 kg) at rest, perfectly elastically. What happens to the heavy cart after impact?',
    options: [
      'It stops dead, like in the movies',
      'It keeps moving forward, but slower',
      'It bounces backward',
      'It keeps moving at the same speed',
    ],
    correctIndex: 1,
    reveal:
        'The heavy cart keeps going, just slower (v₁ = (m₁−m₂)/(m₁+m₂) · u₁ = 3/5 × 4 = 2.4 m/s). A moving object only stops dead in an elastic collision when it hits an EQUAL mass — try m₁ = m₂ in the lab and watch the carts swap velocities like billiard balls.',
  ),
  experiments: [
    'Set m₁ = m₂ with e = 1 — watch the velocities swap',
    'Set e = 0 and see the carts stick together',
    'Make m₂ huge — the light cart bounces off like a wall',
    'Watch the COM marker: the collision never disturbs it',
    'Compare the KE bar at e = 1 vs e = 0.5',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Momentum is mass in motion: p = mv. It is a vector — direction matters, and in one dimension that means signs matter. What makes momentum special is that when two objects interact, the momentum one gains is exactly the momentum the other loses. Newton\'s third law guarantees it: equal and opposite forces, acting for the same contact time, produce equal and opposite impulses (FΔt = Δp).',
      title: 'Momentum: the quantity collisions can\'t destroy',
    ),
    ContentBlock.formula('m₁u₁ + m₂u₂  =  m₁v₁ + m₂v₂', title: 'CONSERVATION OF LINEAR MOMENTUM'),
    ContentBlock.paragraph(
      'This single equation holds for EVERY collision — elastic, inelastic, explosive — as long as no external force acts along that direction. Friction from outside? Gravity along the track? If external forces are negligible during the brief impact, momentum before equals momentum after. That is why the equation is your first line in every collision problem.',
    ),
    ContentBlock.realLife(
      'A rocket is a collision problem in reverse: it throws gas backward, so the rocket must gain forward momentum. A gun recoils for the same reason. And the truck-vs-cycle question? Both feel the same force and the same momentum change — but the cycle\'s small mass turns that momentum change into a huge velocity change. Equal Δp, very unequal Δv.',
    ),
    ContentBlock.paragraph(
      'Kinetic energy is different — it is NOT always conserved. During impact, objects deform, heat up and make sound; that energy leaves the "motion" account. We classify collisions by how much KE survives, using the coefficient of restitution e — the ratio of separation speed to approach speed.',
      title: 'Elastic vs inelastic: the fate of kinetic energy',
    ),
    ContentBlock.formula('e = (v₂ − v₁) / (u₁ − u₂)', title: 'COEFFICIENT OF RESTITUTION'),
    ContentBlock.bullets([
      'e = 1 → perfectly elastic: KE fully conserved (ideal billiard balls, gas molecules)',
      '0 < e < 1 → real-world collisions: some KE lost to heat, sound, deformation',
      'e = 0 → perfectly inelastic: objects stick together; maximum possible KE is lost',
    ]),
    ContentBlock.mistake(
      'Students write "kinetic energy is conserved" for every collision. It is conserved ONLY when e = 1. Momentum, on the other hand, is conserved in ALL of them. If a problem says the objects stick together, KE conservation is guaranteed to be FALSE — using it gives a wrong answer instantly.',
    ),
    ContentBlock.mistake(
      'Sign errors kill more collision problems than hard physics does. Choose a positive direction once, give every velocity a sign, and never "drop" a minus because a speed looks positive in the diagram.',
    ),
    ContentBlock.example(
      'Two carts stick together (e = 0): m₁ = 2 kg at 6 m/s hits m₂ = 4 kg at rest.\n\nMomentum: 2×6 + 4×0 = (2+4)×v  →  v = 2 m/s.\n\nKE before = ½×2×36 = 36 J. KE after = ½×6×4 = 12 J.\nLost: 24 J (two-thirds!) — gone into deformation and heat. Notice we never needed the contact force.',
    ),
    ContentBlock.jeeTip(
      'For elastic collisions with equal masses, velocities are simply EXCHANGED. For a light ball hitting a heavy wall elastically, it rebounds with the same speed. Memorize these limits — JEE builds multi-step problems (ball bouncing between walls, chains of collisions) where each step is one of these special cases.',
    ),
    ContentBlock.jeeTip(
      'In a perfectly inelastic collision, the KE lost is ΔKE = ½μ(u₁−u₂)², where μ = m₁m₂/(m₁+m₂) is the reduced mass. This one-liner converts a 5-minute problem into a 30-second one.',
    ),
    ContentBlock.neetNote(
      'NEET repeatedly asks: which quantities are conserved in which collision type? Answer once, remember forever — Momentum: always. Total energy: always. Kinetic energy: only elastic. Also asked: a bullet embedding in a block (perfectly inelastic) followed by a rise h — use momentum for the impact, then energy for the swing. Never energy across the impact.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Newton\'s third law during contact',
      math: 'F₁₂ = −F₂₁\nF₁₂Δt = −F₂₁Δt  →  Δp₁ = −Δp₂',
      note: 'Equal and opposite impulses: whatever momentum cart 1 gains, cart 2 loses.',
    ),
    DerivationStep(
      title: 'Hence total momentum is unchanged',
      math: 'Δp₁ + Δp₂ = 0\nm₁u₁ + m₂u₂ = m₁v₁ + m₂v₂   …(1)',
    ),
    DerivationStep(
      title: 'Add the restitution equation',
      math: 'v₂ − v₁ = e(u₁ − u₂)   …(2)',
      note: 'Definition of e: separation speed = e × approach speed.',
    ),
    DerivationStep(
      title: 'Solve (1) and (2) for the final velocities',
      math:
          'v₁ = [(m₁ − e·m₂)u₁ + (1+e)m₂u₂] / (m₁+m₂)\nv₂ = [(m₂ − e·m₁)u₂ + (1+e)m₁u₁] / (m₁+m₂)',
      note: 'These two lines run the Collision Lab. Every special case below is just a substitution.',
    ),
    DerivationStep(
      title: 'Check the famous limits (e = 1)',
      math:
          'm₁ = m₂:  v₁ = u₂,  v₂ = u₁   (velocities swap)\nm₂ → ∞, u₂ = 0:  v₁ = −u₁   (bounces off a wall)',
      note: 'Verify both in the lab — deriving and then SEEING a limit is how it sticks.',
    ),
  ],
  formulas: const [
    FormulaEntry('Momentum', 'p = m·v'),
    FormulaEntry('Impulse–momentum theorem', 'F·Δt = Δp'),
    FormulaEntry('Conservation of momentum', 'm₁u₁ + m₂u₂ = m₁v₁ + m₂v₂',
        condition: 'No external force along the line of motion'),
    FormulaEntry('Coefficient of restitution', 'e = (v₂ − v₁)/(u₁ − u₂)'),
    FormulaEntry('Perfectly inelastic: common velocity', 'v = (m₁u₁ + m₂u₂)/(m₁ + m₂)',
        condition: 'e = 0, bodies stick together'),
    FormulaEntry('KE lost (perfectly inelastic)', 'ΔKE = ½·[m₁m₂/(m₁+m₂)]·(u₁ − u₂)²'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'In which type of collision is kinetic energy conserved?',
      options: [
        'All collisions',
        'Only perfectly elastic collisions',
        'Only perfectly inelastic collisions',
        'Kinetic energy is never conserved',
      ],
      correctIndex: 1,
      solution:
          'Momentum is conserved in every collision, but kinetic energy survives only when e = 1 (perfectly elastic). In every other case some KE converts to heat, sound and deformation.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A 2 kg body moving at 3 m/s collides with a 1 kg body at rest and they stick together. Their common velocity is:',
      options: ['1 m/s', '1.5 m/s', '2 m/s', '3 m/s'],
      correctIndex: 2,
      solution:
          'Sticking together means perfectly inelastic. Momentum: 2×3 + 1×0 = 3v → v = 6/3 = 2 m/s. (Never use KE conservation here — check: 9 J before, 6 J after; 3 J was lost.)',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A ball dropped from height h rebounds to height h/4. The coefficient of restitution with the floor is:',
      options: ['1/4', '1/2', '1/√2', '3/4'],
      correctIndex: 1,
      solution:
          'Speed just before impact: √(2gh). Speed just after: √(2g·h/4) = ½√(2gh). For collision with the fixed floor, e = separation speed / approach speed = 1/2. In general e = √(h₂/h₁).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'In a perfectly elastic collision between two equal masses, one initially at rest, the moving ball:',
      options: [
        'Continues with half its speed',
        'Rebounds with the same speed',
        'Stops, transferring all its velocity to the other ball',
        'Sticks to the other ball',
      ],
      correctIndex: 2,
      solution:
          'Equal masses + elastic ⇒ velocities are exchanged: the mover stops, the target leaves with the original velocity. This is why a striker in carrom can stop dead. Verify it in the lab with m₁ = m₂, e = 1.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A 4 kg cart at 4 m/s hits a stationary 2 kg cart, e = 0.5. The velocity of the 2 kg cart after collision is:',
      options: ['2 m/s', '3 m/s', '4 m/s', '6 m/s'],
      correctIndex: 2,
      solution:
          'v₂ = (1+e)m₁u₁/(m₁+m₂) = 1.5 × 4 × 4 / 6 = 4 m/s. (And v₁ = [(4 − 0.5×2)×4]/6 = 2 m/s — momentum check: 16 = 4×2 + 2×4 ✓)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'Two carts (m and 2m) approach each other with equal speeds u and collide perfectly inelastically. The fraction of the initial kinetic energy lost is:',
      options: ['1/3', '4/9', '8/9', '1/2'],
      correctIndex: 2,
      solution:
          'Take rightward positive: p = mu − 2mu = −mu, so v = −u/3. KE_i = ½mu² + ½(2m)u² = (3/2)mu². KE_f = ½(3m)(u/3)² = mu²/6. Fraction lost = (3/2 − 1/6)/(3/2) = (4/3)/(3/2) = 8/9. Head-on inelastic collisions destroy almost all the KE.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A bullet of mass m moving at speed v embeds into a block of mass M hanging from a string. The block rises to height h. Which relation is correct?',
      options: [
        '½mv² = (M+m)gh',
        'mv = (M+m)√(2gh)',
        '½(M+m)v² = Mgh',
        'mv = M√(2gh)',
      ],
      correctIndex: 1,
      solution:
          'Two stages, two laws. Impact (perfectly inelastic): momentum only — mv = (M+m)V. Swing: energy only — ½(M+m)V² = (M+m)gh, so V = √(2gh). Combine: mv = (M+m)√(2gh). Using energy across the impact (option A) is the classic trap: KE is lost while embedding.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'During any collision between two carts, the velocity of their center of mass:',
      options: [
        'Suddenly changes at the moment of impact',
        'Becomes zero',
        'Remains constant throughout',
        'Depends on the coefficient of restitution',
      ],
      correctIndex: 2,
      solution:
          'Internal forces cannot move the center of mass. With no external force, v_COM = (m₁u₁+m₂u₂)/(m₁+m₂) stays constant before, during and after impact — for ANY e. Watch the COM marker in the lab sail through the crash undisturbed.',
    ),
  ],
  revision: [
    'Momentum p = mv is conserved in EVERY collision; KE only when e = 1.',
    'e = separation speed ÷ approach speed; ball drop: e = √(h₂/h₁).',
    'Equal masses + elastic → velocities swap. Light vs heavy wall → rebound at same speed.',
    'Perfectly inelastic: v = (m₁u₁+m₂u₂)/(m₁+m₂); KE lost = ½μ(Δu)².',
    'The center of mass never notices the collision — its velocity is constant.',
    'Bullet-block problems: momentum across the impact, energy across the swing.',
  ],
  sandboxBuilder: (_) => const CollisionLabSimulator(),
);
