import '../../models/lesson.dart';
import '../../simulators/relative_motion_sandbox.dart';
import '../../theme/tokens.dart';

/// Relative Motion — velocity depends on who is watching.
final Lesson relativeMotionLesson = Lesson(
  topicId: 'relative-motion',
  title: 'Relative Motion',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'You\'re in a train at 60 km/h and the train beside you crawls at 50 km/h in the same direction. Why does it seem to drift backward at walking pace — and who is actually "right" about its speed?',
  whyItMatters:
      'There is no such thing as "the" velocity of an object — only velocity relative to an observer. This one idea solves train-overtaking problems, river-boat crossings, rain-and-umbrella questions, and later becomes the foundation of pseudo-forces and even relativity. NEET and JEE both plant one relative-velocity question in almost every paper.',
  prediction: const PredictionPrompt(
    scenario:
        'Car A moves at 12 m/s and car B at 6 m/s in the same direction. To a passenger riding in car B, car A appears to move at:',
    options: [
      '18 m/s forward',
      '6 m/s forward',
      '12 m/s forward',
      '6 m/s backward',
    ],
    correctIndex: 1,
    reveal:
        'v(A rel B) = v_A − v_B = 12 − 6 = 6 m/s forward. Same direction → speeds SUBTRACT. In the lab, tap "Ride car B": car B freezes and car A pulls ahead at exactly 6 m/s. Now flip B\'s velocity to −6 m/s (opposite direction) and watch A close in at 18 m/s.',
  ),
  experiments: [
    'Set v_A = 12, v_B = 6 and tap "Ride car B" — A creeps forward at 6 m/s',
    'Make the velocities equal — in either car\'s frame, the other car freezes',
    'Set v_B negative (opposite direction) — the closing speed becomes v_A + |v_B|',
    'Tap "Ride car A" — the milestones (the ground itself!) stream backward at v_A',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Every velocity is measured from some frame of reference — the ground, a car, a boat. The velocity of A as seen from B is the vector difference v(AB) = v_A − v_B. In one dimension this reduces to simple arithmetic with signs: same direction → subtract, opposite directions → add.',
      title: 'Velocity is a comparison, not a property',
    ),
    ContentBlock.formula('v(AB) = v_A − v_B     (velocity of A relative to B)',
        title: 'RELATIVE VELOCITY'),
    ContentBlock.bullets([
      'Same direction: relative speed = |v_A − v_B| (overtaking is slow)',
      'Opposite directions: relative speed = v_A + v_B (head-on approach is fast)',
      'v(AB) = −v(BA): each sees the other with equal and opposite velocity',
      'In your own frame, YOU are always at rest — the world moves instead',
    ]),
    ContentBlock.paragraph(
      'In two dimensions the same formula holds with vectors: subtract components. Classic setups — a boat crossing a river (add the current\'s velocity), rain falling on a moving cyclist (tilt of the umbrella follows the relative velocity of rain), two ships on crossing courses (closest approach).',
      title: 'The 2D version: subtract vectors',
    ),
    ContentBlock.realLife(
      'Sitting in a station, your train "moves" — then you realise the neighbouring train is pulling out and yours is still. Your brain measured only relative velocity; without an outside reference it cannot tell who is moving. Pilots do the same math daily: an aircraft\'s ground speed is airspeed plus wind velocity, as vectors.',
    ),
    ContentBlock.mistake(
      'Adding speeds when cars move the same way. Two trains at 60 and 50 km/h in the same direction close at 10 km/h, not 110. The 110 figure is for OPPOSITE directions. Draw arrows before you compute.',
    ),
    ContentBlock.mistake(
      'Dropping signs in 1D. Choose one direction as positive and write every velocity with a sign FIRST. v(AB) = v_A − v_B then works automatically — including the case where the answer comes out negative (A falls behind).',
    ),
    ContentBlock.example(
      'A 100 m long train at 20 m/s overtakes a 50 m train at 10 m/s moving the same way. Time to fully overtake?\n\nRelative speed = 20 − 10 = 10 m/s.\nDistance to clear = sum of lengths = 150 m.\nt = 150/10 = 15 s.\n\nIn the slow train\'s frame the fast train simply travels 150 m at 10 m/s.',
    ),
    ContentBlock.jeeTip(
      'River-boat: to cross by the SHORTEST PATH, aim upstream so the upstream component of your velocity cancels the current (sinθ = u/v). To cross in SHORTEST TIME, point straight across — the current drifts you downstream but the crossing time is just width/v. JEE alternates between these two; read which one is asked.',
    ),
    ContentBlock.neetNote(
      'Rain problems: if rain falls vertically at v_r and you run at v_m, the rain hits you at tanθ = v_m/v_r from the vertical — tilt the umbrella FORWARD by that angle. And remember the train-overtake rule: relative speed uses the difference, total length uses the sum.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write positions in the ground frame',
      math: 'x_A(t) = x_A₀ + v_A·t\nx_B(t) = x_B₀ + v_B·t',
    ),
    DerivationStep(
      title: 'Position of A as measured from B',
      math: 'x(AB) = x_A − x_B = (x_A₀ − x_B₀) + (v_A − v_B)·t',
      note: 'B treats itself as the origin.',
    ),
    DerivationStep(
      title: 'Differentiate to get relative velocity',
      math: 'v(AB) = d(x_AB)/dt = v_A − v_B',
      note: 'The separation changes at the difference of the velocities.',
    ),
    DerivationStep(
      title: 'Generalise to vectors (2D/3D)',
      math: '→v(AB) = →v_A − →v_B',
      note: 'Subtract component-wise; magnitude via |v(AB)|² = v_A² + v_B² − 2v_Av_B·cosθ.',
    ),
  ],
  formulas: const [
    FormulaEntry('Relative velocity', 'v(AB) = v_A − v_B'),
    FormulaEntry('Same direction', 'relative speed = |v_A − v_B|'),
    FormulaEntry('Opposite directions', 'relative speed = v_A + v_B'),
    FormulaEntry('Overtake time (trains)', 't = (L₁ + L₂)/relative speed'),
    FormulaEntry('River crossing (min time)', 't = d/v', condition: 'point straight across; drift = u·d/v'),
    FormulaEntry('Rain tilt', 'tanθ = v_man/v_rain', condition: 'umbrella tilted forward from vertical'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two cars move at 40 km/h and 60 km/h in the same direction. The velocity of the faster car relative to the slower one is:',
      options: ['100 km/h', '60 km/h', '20 km/h', '40 km/h'],
      correctIndex: 2,
      solution: 'Same direction → subtract: 60 − 40 = 20 km/h.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two trains approach each other at 30 m/s and 20 m/s. Their relative speed of approach is:',
      options: ['10 m/s', '25 m/s', '50 m/s', '600 m/s'],
      correctIndex: 2,
      solution: 'Opposite directions → add: 30 + 20 = 50 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A 150 m train at 25 m/s overtakes a 100 m train at 15 m/s in the same direction. Time taken to overtake completely:',
      options: ['10 s', '25 s', '15 s', '6.25 s'],
      correctIndex: 1,
      solution:
          'Relative speed = 25 − 15 = 10 m/s; distance = 150 + 100 = 250 m; t = 250/10 = 25 s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Rain falls vertically at 10 m/s. A man runs at 10 m/s. To keep dry he must tilt his umbrella from the vertical by:',
      options: ['30°', '45°', '60°', '90°'],
      correctIndex: 1,
      solution:
          'tanθ = v_man/v_rain = 10/10 = 1 → θ = 45°, tilted forward in the direction of running.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A boat can move at 5 m/s in still water. It crosses a 100 m river flowing at 3 m/s by the shortest path. Its crossing time is:',
      options: ['20 s', '25 s', '33.3 s', '12.5 s'],
      correctIndex: 1,
      solution:
          'Shortest path → aim upstream so the effective across-river speed = √(5² − 3²) = 4 m/s. t = 100/4 = 25 s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The same boat instead crosses in the shortest TIME. How far downstream does it land?',
      options: ['60 m', '75 m', '100 m', '45 m'],
      correctIndex: 0,
      solution:
          'Shortest time → point straight across: t = 100/5 = 20 s. Drift = current × time = 3 × 20 = 60 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'To a man walking east at 4 km/h, the wind appears to blow from the north. Walking at 8 km/h it appears from the north-east. The true wind speed is:',
      options: ['4 km/h', '4√2 km/h', '8 km/h', '4√5 km/h'],
      correctIndex: 1,
      solution:
          'Apparent wind = true wind − man\'s velocity. Take east as +x. Case 1 (man at 4): apparent is due south → x-component zero → wₓ − 4 = 0 → wₓ = 4. Case 2 (man at 8): apparent from north-east → its components are equal: wₓ − 8 = w_y → w_y = −4. True wind = (4, −4), speed = √(4² + 4²) = 4√2 km/h, blowing from the north-west.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A passenger in car B (moving at 6 m/s) watches car A (12 m/s, same direction). In B\'s frame, the ground milestones move:',
      options: [
        'Forward at 6 m/s',
        'Backward at 6 m/s',
        'Backward at 12 m/s',
        'They stay still',
      ],
      correctIndex: 1,
      solution:
          'v(ground rel B) = 0 − 6 = −6 m/s: the ground streams backward at B\'s own speed. Exactly what the "Ride car B" camera shows in the lab.',
    ),
  ],
  revision: [
    'v(AB) = v_A − v_B — always subtract the observer\'s velocity.',
    'Same direction: speeds subtract. Opposite: speeds add.',
    'Overtaking time = (sum of lengths)/(difference of speeds).',
    'River: shortest time → aim straight (drift happens); shortest path → aim upstream (slower crossing).',
    'Rain: tilt umbrella forward by tanθ = v_man/v_rain.',
    'In your own frame you are at rest; the world moves with −(your velocity).',
  ],
  sandboxBuilder: (_) => const RelativeMotionSandbox(),
);
