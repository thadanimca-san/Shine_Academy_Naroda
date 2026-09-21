import '../../models/lesson.dart';
import '../../simulators/second_law_sim.dart';
import '../../theme/tokens.dart';

/// Newton's Second Law — F = ma, built from momentum and impulse.
final Lesson newtonSecondLawLesson = Lesson(
  topicId: 'newton-second-law',
  title: 'Newton\'s Second Law',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Push a shopping cart and an empty cart moves off briskly. Push a fully loaded cart with the exact same force and it barely creeps. Why does the SAME force produce such different accelerations — and is there an exact formula connecting force, mass and acceleration?',
  whyItMatters:
      'F = ma is the single most-used equation in all of JEE/NEET mechanics — every block, pulley, incline and circular-motion problem is really just this law applied carefully with a free-body diagram. Understanding that it actually comes from F = dp/dt (not just "memorised as ma") is what lets you solve variable-mass problems (rockets, raindrops, conveyor belts) that trip up students who only know the shortcut.',
  prediction: const PredictionPrompt(
    scenario:
        'A constant force F is applied to a cart of mass m, giving it acceleration a. You now DOUBLE the mass on the cart (keeping F the same). The new acceleration is:',
    options: [
      'Still a (mass doesn\'t affect acceleration)',
      '2a (more mass means it accelerates faster)',
      'a/2 (acceleration is inversely proportional to mass)',
      'a/4 (mass affects it quadratically)',
    ],
    correctIndex: 2,
    reveal:
        'a = F/m, so acceleration is inversely proportional to mass — doubling m halves a for the same force. In the lab, set a fixed applied force, double the mass slider, and watch the acceleration readout drop to exactly half. This inverse relationship is why a loaded truck needs a far longer distance to reach the same speed as an empty one under the same engine force.',
  ),
  experiments: [
    'Fix the force and double the mass — confirm acceleration halves',
    'Fix the mass and double the force — confirm acceleration doubles',
    'Set force to zero — the object moves at constant velocity (first law as a special case)',
    'Apply a force for a short burst and read the impulse = area under the F–t graph',
    'Try a very large mass with a small force and watch how sluggish the response becomes',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Newton\'s second law connects force to the RATE OF CHANGE of momentum, not directly to acceleration. Momentum p = mv captures "how much motion" an object has. The law says: the net force on a body equals how fast its momentum is changing, and the change happens in the direction of the force.',
      title: 'Force is the rate of change of momentum',
    ),
    ContentBlock.formula('F_net = dp/dt,   p = mv', title: 'NEWTON\'S SECOND LAW (GENERAL FORM)'),
    ContentBlock.paragraph(
      'When mass is constant, dp/dt = m(dv/dt) = ma, which gives the familiar F = ma. But the general form F = dp/dt is more powerful — it still works when mass itself is changing, such as a rocket burning fuel or rain accumulating in an open cart. Always start from F = dp/dt if mass is not constant.',
      title: 'F = ma is a special case',
    ),
    ContentBlock.formula('F = ma   (only valid when m is constant)', title: 'CONSTANT-MASS FORM'),
    ContentBlock.bullets([
      'a ∝ F at fixed mass — double the force, double the acceleration',
      'a ∝ 1/m at fixed force — double the mass, halve the acceleration',
      'F and a always point in the SAME direction',
      'This is a vector law: apply it separately along each independent direction (e.g., x and y)',
    ]),
    ContentBlock.paragraph(
      'Impulse J is the effect of a force acting over time: J = ∫F dt = Δp. A large force for a short time can produce the same change in momentum as a small force for a long time — this is why airbags and cricket "giving with the ball" work: stretching the time of contact reduces the peak force for the same change in momentum.',
      title: 'Impulse: force applied over time',
    ),
    ContentBlock.formula('J = ∫F dt = Δp = m(v − u)', title: 'IMPULSE-MOMENTUM THEOREM'),
    ContentBlock.realLife(
      'Catching a fast cricket ball hurts less if you pull your hands back as you catch it. By extending the time of contact Δt for the same Δp, the average force F = Δp/Δt on your hand drops sharply. Airbags and crumple zones in cars use the exact same idea to reduce injury force during a collision.',
    ),
    ContentBlock.mistake(
      'Confusing mass and weight. Mass (kg) is the amount of matter and is constant everywhere; weight (N) = mg is the gravitational FORCE on that mass and changes with location (less on the Moon, zero in free-fall). "How much does it weigh?" and "what is its mass?" are different questions — never divide or multiply them incorrectly.',
    ),
    ContentBlock.mistake(
      'Applying F = ma directly to a system with changing mass (like a rocket or a leaking sand cart). You must use F_ext = dp/dt = m(dv/dt) + v(dm/dt), which has an EXTRA term from the changing mass. Plugging straight into F = ma silently drops that term and gives a wrong answer.',
    ),
    ContentBlock.example(
      'A 0.5 kg ball moving at 20 m/s is caught and brought to rest in 0.1 s. Find the average force exerted by the hand.\n\nΔp = m(v − u) = 0.5 × (0 − 20) = −10 kg·m/s.\nF_avg = Δp/Δt = −10 / 0.1 = −100 N.\n\nThe magnitude is 100 N, directed opposite to the ball\'s motion — the hand decelerates the ball.',
    ),
    ContentBlock.jeeTip(
      'Apparent weight in a lift: if a person of mass m stands on a weighing scale in a lift accelerating upward at a, the scale reads N = m(g + a) — MORE than actual weight. Accelerating downward gives N = m(g − a) — LESS than actual weight. In free fall (a = g downward), N = 0: true weightlessness. Always draw the free-body diagram and apply F_net = ma along the direction of acceleration.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the SI unit chain: force in newtons (1 N = 1 kg·m/s²), and the fact that 1 kgf (kilogram-force) = 9.8 N. Also remember: the second law only gives the NET force; if multiple forces act, first find their vector sum, then set that equal to ma.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define momentum',
      math: 'p = mv',
      note: 'Momentum is a vector, combining mass and velocity into one "quantity of motion."',
    ),
    DerivationStep(
      title: 'State the general second law',
      math: 'F_net = dp/dt',
      note: 'This is how Newton actually phrased it — force causes momentum to change.',
    ),
    DerivationStep(
      title: 'Expand the derivative using the product rule',
      math: 'F_net = d(mv)/dt = m(dv/dt) + v(dm/dt)',
    ),
    DerivationStep(
      title: 'Apply the constant-mass condition',
      math: 'dm/dt = 0  (mass constant)  ⟹  F_net = m(dv/dt)',
      note: 'The second term vanishes only because mass is not changing.',
    ),
    DerivationStep(
      title: 'Recognise dv/dt as acceleration',
      math: 'F_net = ma',
      note: 'The familiar form — valid ONLY when mass stays constant during the motion.',
    ),
  ],
  formulas: const [
    FormulaEntry('General second law', 'F_net = dp/dt'),
    FormulaEntry('Constant-mass form', 'F_net = ma'),
    FormulaEntry('Variable-mass form', 'F_ext = m(dv/dt) + v(dm/dt)'),
    FormulaEntry('Impulse-momentum theorem', 'J = ∫F dt = Δp = m(v − u)'),
    FormulaEntry('Weight', 'W = mg'),
    FormulaEntry('Apparent weight, lift accelerating up', 'N = m(g + a)'),
    FormulaEntry('Apparent weight, lift accelerating down', 'N = m(g − a)'),
    FormulaEntry('Weightlessness condition', 'N = 0  when a = g (free fall)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A net force of 10 N acts on a 2 kg mass. Its acceleration is:',
      options: ['2 m/s²', '5 m/s²', '10 m/s²', '20 m/s²'],
      correctIndex: 1,
      solution: 'a = F/m = 10/2 = 5 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The SI unit of force, the newton, is equivalent to:',
      options: ['1 kg·m/s', '1 kg·m/s²', '1 kg/m·s²', '1 kg·m²/s²'],
      correctIndex: 1,
      solution: 'From F = ma, [N] = [kg][m/s²] = kg·m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A person of mass 60 kg stands on a weighing scale inside a lift accelerating upward at 2 m/s² (g = 10 m/s²). The scale reading is:',
      options: ['600 N', '480 N', '720 N', '60 N'],
      correctIndex: 2,
      solution: 'N = m(g + a) = 60 × (10 + 2) = 720 N — more than the actual weight of 600 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A ball of mass 0.15 kg hits a wall with speed 12 m/s and rebounds with the same speed. If contact lasts 0.01 s, the average force on the wall is:',
      options: ['180 N', '360 N', '18 N', '3.6 N'],
      correctIndex: 1,
      solution:
          'Δp = m(v−u) = 0.15×(−12 − 12) = 0.15×(−24) = −3.6 kg·m/s. |F| = |Δp|/Δt = 3.6/0.01 = 360 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Why do cricketers pull their hands backward while catching a fast ball?',
      options: [
        'To increase the impulse on the ball',
        'To increase the time of contact and thus reduce the average force on the hand',
        'To decrease the change in momentum of the ball',
        'To increase the force needed to stop the ball',
      ],
      correctIndex: 1,
      solution:
          'Δp is fixed by the ball\'s speed; pulling the hands back increases Δt, so F_avg = Δp/Δt decreases — the same impulse is delivered with a gentler peak force.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A lift is falling freely (cable snapped). The apparent weight of a passenger inside is:',
      options: ['mg', '2mg', 'Zero', 'mg/2'],
      correctIndex: 2,
      solution:
          'Free fall means a = g downward, so N = m(g − a) = m(g − g) = 0. This is true weightlessness, not absence of gravity.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Sand drops vertically at rate dm/dt onto a conveyor belt moving horizontally at constant velocity v. The extra force needed to keep the belt moving at constant v is:',
      options: ['Zero, since v is constant', 'v·(dm/dt)', '(v²/2)·(dm/dt)', 'g·(dm/dt)'],
      correctIndex: 1,
      solution:
          'Belt velocity is constant (dv/dt = 0), but mass increases, so F = m(dv/dt) + v(dm/dt) = 0 + v(dm/dt) = v·(dm/dt). Even at constant velocity, extra force is needed because momentum is still increasing due to added mass.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A rocket ejects gas at a relative speed u and burns fuel at rate dm/dt (mass decreasing). Ignoring gravity, the thrust force on the rocket is:',
      options: ['u·(dm/dt)', '−u·(dm/dt)', 'u²·(dm/dt)', 'm·u'],
      correctIndex: 0,
      solution:
          'Thrust magnitude = u × |dm/dt|, directed opposite to the ejected gas. This comes from applying F = dp/dt to the rocket-plus-ejected-gas system and is the standard "rocket equation" force term.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'On the Moon, where g is about 1/6th of Earth\'s, an astronaut\'s:',
      options: [
        'Mass and weight both reduce to 1/6th',
        'Mass stays the same, weight reduces to 1/6th',
        'Mass reduces to 1/6th, weight stays the same',
        'Both mass and weight stay the same',
      ],
      correctIndex: 1,
      solution:
          'Mass is an intrinsic property of matter and does not depend on gravity. Weight = mg depends on local g, so it becomes about 1/6th on the Moon while mass is unchanged.',
    ),
  ],
  revision: [
    'F_net = dp/dt is the true, general form of the second law; F = ma applies only when mass is constant.',
    'Acceleration is proportional to net force and inversely proportional to mass.',
    'Impulse J = ∫F dt = Δp — a large force for a short time can equal a small force for a long time.',
    'Mass is constant everywhere; weight = mg changes with location and with acceleration of the frame.',
    'Apparent weight in a lift: N = m(g + a) accelerating up, N = m(g − a) accelerating down, N = 0 in free fall.',
    'Variable-mass systems (rockets, sand on a belt) need the extra v(dm/dt) term — never just F = ma.',
    'Force and acceleration are always in the same direction — resolve into components along independent axes.',
  ],
  sandboxBuilder: (_) => const SecondLawSimulator(),
);
