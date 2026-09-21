import '../../models/lesson.dart';
import '../../simulators/collision_lab_sim.dart';
import '../../theme/tokens.dart';

/// Momentum & Impulse — why a longer collision time can mean a much smaller force.
final Lesson momentumImpulseLesson = Lesson(
  topicId: 'momentum-impulse',
  title: 'Momentum & Impulse',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A cricketer catching a fast ball instinctively pulls their hands backward as the ball arrives, instead of holding them rigidly still. Why does that one small motion save their palms from serious pain — when the ball\'s speed loss is exactly the same either way?',
  whyItMatters:
      'Momentum and impulse give you a second, completely independent conservation law from energy — one that survives even violent, energy-losing collisions (crashes, catches, explosions) where mechanical energy is NOT conserved. It is the standard toolkit for every collision problem in NEET and JEE, from recoiling guns to two-body elastic and inelastic collisions, and it explains an enormous range of safety engineering: airbags, crumple zones, catching technique, and padded flooring.',
  prediction: const PredictionPrompt(
    scenario:
        'A ball hits a cricketer\'s hands and stops. Case A: the hands are held rigid, so the ball stops in 0.01 s. Case B: the hands "give" with the ball, so it stops in 0.1 s — ten times longer. The change in momentum is identical in both cases. Compare the average force felt by the hands:',
    options: [
      'The same force in both cases — momentum change is identical',
      'Case A (rigid) feels 10× LESS force than Case B',
      'Case A (rigid) feels 10× MORE force than Case B',
      'Force cannot be compared without knowing the ball\'s mass',
    ],
    correctIndex: 2,
    reveal:
        'Impulse J = FΔt = Δp is fixed by the momentum change alone — but F and Δt trade off against each other. Stretching the stopping time by 10× (giving with the ball) cuts the average force by 10×. In the lab, keep the objects and speeds the same but change the collision duration slider — watch the peak-force readout fall as the contact time grows, even though the momentum-change readout never moves.',
  ),
  experiments: [
    'Collide two carts of equal mass and watch total momentum before = total momentum after',
    'Make one cart much heavier and watch it barely slow down while the light one flies off fast',
    'Switch between elastic and perfectly inelastic collision modes and compare final velocities',
    'Stretch the collision duration (soft bumper) and watch the peak force reading drop',
    'Set opposite-direction velocities and confirm momentum is a signed (vector) quantity in the total',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Momentum is a measure of how hard it is to stop a moving object — it combines how much mass is moving with how fast. A slow-moving truck and a fast-moving bullet can have comparable momentum despite wildly different masses and speeds. Momentum is a VECTOR: it has the same direction as the velocity.',
      title: 'Momentum: quantity of motion',
    ),
    ContentBlock.formula('p = m·v', title: 'LINEAR MOMENTUM'),
    ContentBlock.paragraph(
      'Impulse is what changes an object\'s momentum — it is the product of the force applied and the time for which it acts. When a force varies during a collision, impulse is the area under the force–time graph. Crucially, impulse EQUALS the change in momentum — this connects force-and-time thinking directly to mass-and-velocity thinking.',
      title: 'Impulse: the momentum-changer',
    ),
    ContentBlock.formula(
      'J = F·Δt = Δp = m·v − m·u',
      title: 'IMPULSE-MOMENTUM THEOREM',
    ),
    ContentBlock.bullets([
      'For the SAME impulse (same Δp), a longer contact time Δt means a smaller average force',
      'For the SAME impulse, a shorter contact time means a much larger average force',
      'Impulse and momentum share the same units (kg·m/s = N·s) and are both vectors',
      'In an isolated system (no external force), total momentum is conserved — it doesn\'t change, even during a violent collision',
    ]),
    ContentBlock.realLife(
      'Airbags and crumple zones in cars do NOT reduce the change in momentum during a crash — the car still goes from highway speed to zero. What they do is stretch the stopping time from milliseconds to tenths of a second, which cuts the average force on the occupant by a huge factor, turning what would be lethal into survivable.',
    ),
    ContentBlock.realLife(
      'A boxer "rolling with the punch" moves their head back as the glove lands, extending the contact time and reducing the peak force of impact — exactly the same physics as a cricketer\'s soft hands. Landing mats in gymnastics and high jump work the same way: they extend the stopping time on impact.',
    ),
    ContentBlock.mistake(
      'Treating momentum as a scalar and just adding magnitudes. Momentum conservation must be applied component-by-component (or with correct signs on a line) — two equal masses approaching each other at the same speed have a TOTAL momentum of zero, not double the momentum of one.',
    ),
    ContentBlock.mistake(
      'Confusing "momentum is conserved" with "kinetic energy is conserved." Momentum is conserved in EVERY collision in an isolated system — elastic or not. Kinetic energy is only conserved in elastic collisions; in inelastic collisions (like a ball of clay sticking to a wall) KE is lost to heat and deformation while momentum still balances.',
    ),
    ContentBlock.example(
      'A 0.15 kg cricket ball moving at 20 m/s is caught and brought to rest in 0.1 s. Find the average force exerted by the hands.\n\nΔp = m(v − u) = 0.15×(0 − 20) = −3 kg·m/s\n\nF = Δp/Δt = −3/0.1 = −30 N.\n\nThe magnitude of the force is 30 N (directed opposite to the ball\'s original motion — the hands push back on the ball, and by Newton\'s third law the ball pushes on the hands with 30 N).',
    ),
    ContentBlock.jeeTip(
      'Momentum conservation is the go-to tool whenever a collision or explosion is described but you are NOT told the forces or the time of contact — because p_total(before) = p_total(after) holds regardless of what happens during the brief interaction, even if it involves complicated internal forces you could never analyse directly (e.g. explosive fragmentation, a bullet embedding in a block).',
    ),
    ContentBlock.jeeTip(
      'For 2D collisions (glancing collisions, projectile fragmentation), apply momentum conservation SEPARATELY along the x and y axes — two scalar equations, since momentum is a vector. Do not add magnitudes; resolve into components first.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests recoil problems: a gun of mass M fires a bullet of mass m at velocity v. Since the gun+bullet system starts at rest, total momentum stays zero: Mv_gun + mv_bullet = 0, so the gun recoils with v_gun = −(m/M)v_bullet — heavier gun, smaller recoil speed. Also remember: momentum is always conserved in a collision; kinetic energy is conserved ONLY if the collision is elastic.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Newton\'s second law in its original momentum form',
      math: 'F = dp/dt',
      note:
          'Newton originally defined force as the rate of change of momentum, not F = ma.',
    ),
    DerivationStep(
      title: 'Rearrange and integrate over the duration of the force',
      math: 'F·dt = dp   →   ∫F dt = ∫dp',
      note:
          'The left side, by definition, is the impulse J delivered by the force.',
    ),
    DerivationStep(
      title: 'Evaluate both sides for a collision from time 0 to Δt',
      math: 'J = p_final − p_initial = Δp',
      note: 'For a constant (or average) force, J = F_avg·Δt.',
    ),
    DerivationStep(
      title:
          'Apply Newton\'s third law to a two-body collision (bodies A and B)',
      math: 'F_A on B = −F_B on A   (at every instant of contact)',
    ),
    DerivationStep(
      title: 'Integrate the third-law relation over the same contact time',
      math: 'J_on B = −J_on A   →   Δp_B = −Δp_A   →   Δ(p_A + p_B) = 0',
      note:
          'Total momentum of the isolated two-body system does not change — conservation of momentum follows directly from Newton\'s third law.',
    ),
  ],
  formulas: const [
    FormulaEntry(
      'Linear momentum',
      'p = m·v',
      condition: 'vector, same direction as v',
    ),
    FormulaEntry('Impulse', 'J = F·Δt', condition: 'F constant or average'),
    FormulaEntry('Impulse-momentum theorem', 'J = Δp = m(v − u)'),
    FormulaEntry(
      'Conservation of momentum',
      'p_total(before) = p_total(after)',
      condition: 'isolated system, no external force',
    ),
    FormulaEntry('Recoil velocity', 'v_gun = −(m_bullet/M_gun)·v_bullet'),
    FormulaEntry(
      'Impulse from a varying force',
      'J = ∫F dt',
      condition: 'area under F–t graph',
    ),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A 5 kg object moves at 4 m/s. Its momentum is:',
      options: ['9 kg·m/s', '20 kg·m/s', '1.25 kg·m/s', '80 kg·m/s'],
      correctIndex: 1,
      solution: 'p = mv = 5×4 = 20 kg·m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Why do gymnasts land on soft mats rather than hard floors?',
      options: [
        'To reduce the change in momentum on landing',
        'To increase the stopping time and reduce the force of impact',
        'To increase the momentum change',
        'Mats have no effect on the physics of landing',
      ],
      correctIndex: 1,
      solution:
          'The momentum change (from landing speed to zero) is the same either way. A soft mat increases the stopping TIME, which — since J = FΔt is fixed — reduces the average force.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A bat exerts an average force of 200 N on a 0.2 kg ball for 0.01 s. The change in the ball\'s velocity is:',
      options: ['1 m/s', '5 m/s', '10 m/s', '20 m/s'],
      correctIndex: 2,
      solution: 'J = FΔt = 200×0.01 = 2 kg·m/s. Δv = J/m = 2/0.2 = 10 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A gun of mass 4 kg fires a 40 g bullet with a muzzle velocity of 300 m/s. The recoil velocity of the gun is:',
      options: ['1 m/s', '2 m/s', '3 m/s', '4 m/s'],
      correctIndex: 2,
      solution:
          'Momentum conservation: 0 = Mv_gun + mv_bullet → v_gun = −(m/M)v_bullet = −(0.04/4)×300 = −3 m/s. Magnitude: 3 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A 2 kg mass moving at 3 m/s collides head-on with a stationary 1 kg mass and they stick together. Their common velocity after collision is:',
      options: ['1 m/s', '1.5 m/s', '2 m/s', '3 m/s'],
      correctIndex: 2,
      solution:
          'Momentum conservation: 2×3 + 1×0 = (2+1)×v → 6 = 3v → v = 2 m/s. (This is a perfectly inelastic collision — KE is NOT conserved here, only momentum.)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A ball of mass m hits a wall perpendicularly at speed v and rebounds elastically with the same speed. The impulse delivered to the wall has magnitude:',
      options: ['0', 'mv', '2mv', '½mv'],
      correctIndex: 2,
      solution:
          'Δp of ball = m(−v) − m(v) = −2mv (taking incoming direction as positive). Magnitude of impulse on ball is 2mv; by Newton\'s third law, the wall receives an equal and opposite impulse of magnitude 2mv.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'Two identical balls, each of mass m, moving at speed v toward each other, undergo a head-on ELASTIC collision. Their velocities after collision are:',
      options: [
        'Both continue at v in their original directions (pass through)',
        'Both stop (v = 0)',
        'Both reverse direction, each at speed v',
        'They move together at v/2',
      ],
      correctIndex: 2,
      solution:
          'For an elastic collision between EQUAL masses, the velocities are exactly exchanged. Since each was moving at v toward the other, each ball leaves with speed v in the OPPOSITE (reversed) direction — equivalent to a perfect "bounce back."',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A shell of mass 10 kg explodes in mid-air (momentarily at rest) into two fragments of mass 4 kg and 6 kg. If the 4 kg fragment flies off at 15 m/s, the 6 kg fragment flies off at:',
      options: ['5 m/s', '10 m/s', '15 m/s', '6 m/s'],
      correctIndex: 1,
      solution:
          'Total momentum before explosion = 0. So m₁v₁ + m₂v₂ = 0 → 4×15 + 6×v₂ = 0 → v₂ = −60/6 = −10 m/s. Magnitude 10 m/s, in the opposite direction to the 4 kg piece.',
    ),
  ],
  revision: [
    'Momentum p = mv is a VECTOR — always add with correct signs/directions, never just magnitudes.',
    'Impulse J = FΔt = Δp connects force-and-time to mass-and-velocity change.',
    'Same Δp, longer Δt → smaller average force (airbags, soft hands, landing mats).',
    'Momentum is conserved in EVERY isolated-system collision — elastic or inelastic.',
    'Kinetic energy is conserved ONLY in elastic collisions; inelastic collisions lose KE to heat/deformation.',
    'Recoil problems: total momentum starts at zero, so the two pieces fly off with equal and opposite momenta.',
    'Equal-mass elastic head-on collision: the two objects exactly exchange velocities.',
  ],
  sandboxBuilder: (_) => const CollisionLabSimulator(),
);
