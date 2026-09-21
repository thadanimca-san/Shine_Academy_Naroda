import '../../models/lesson.dart';
import '../../simulators/motion_1d_sandbox.dart';
import '../../theme/tokens.dart';

/// Motion in a Straight Line — the three equations of motion, discovered by driving.
final Lesson motion1dLesson = Lesson(
  topicId: 'motion-1d',
  title: 'Motion in a Straight Line',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A car speeds up from rest at a steady rate. In the 1st second it covers 1 m. How far does it travel in the 3rd second alone — 1 m again, 3 m, or 5 m?',
  whyItMatters:
      'Kinematics in one dimension is the alphabet of mechanics — every later chapter (projectiles, Newton\'s laws, energy, gravitation) is written in it. The three equations of motion appear in NEET and JEE every single year, usually disguised inside another topic. Master u, v, a, s, t here and half the mechanics paper opens up.',
  prediction: const PredictionPrompt(
    scenario:
        'A car starts from rest with constant acceleration. Compare the distance covered in the 1st second with the distance covered in the 3rd second (from t=2s to t=3s):',
    options: [
      'Both are equal — acceleration is constant',
      'The 3rd second covers 3× the distance',
      'The 3rd second covers 5× the distance',
      'The 3rd second covers 9× the distance',
    ],
    correctIndex: 2,
    reveal:
        'Distances in successive seconds follow the odd-number pattern 1 : 3 : 5 : 7… (Galileo\'s law of odd numbers). From s = ½at², total distance after 1s, 2s, 3s is 1, 4, 9 units — so each new second adds 3, then 5 units. In the lab, set u = 0, start the clock, and watch the position readout at t = 1, 2, 3 s: 1×, 4×, 9× — the gaps are the odd numbers.',
  ),
  experiments: [
    'Set u = 0, a = 2 and read s at t = 1, 2, 3 s — confirm the 1 : 4 : 9 pattern',
    'Set a = 0 — the car cruises at constant v and s grows in a straight line',
    'Give u = 10, a = −4 (brakes): watch v hit zero, then the car reverse',
    'While running, drag a to a new value — the car responds instantly',
  ],
  concept: const [
    ContentBlock.paragraph(
      'To describe motion along a line you need just five quantities: initial velocity u, final velocity v, acceleration a, displacement s and time t. Velocity is how fast position changes; acceleration is how fast velocity changes. When a is constant, the whole motion becomes predictable by algebra — that is what "uniformly accelerated motion" means.',
      title: 'Five symbols describe everything',
    ),
    ContentBlock.formula('v = u + at,   s = ut + ½at²,   v² = u² + 2as',
        title: 'THE THREE EQUATIONS OF MOTION'),
    ContentBlock.bullets([
      'Each equation is missing exactly one variable: the 1st has no s, the 2nd no v, the 3rd no t',
      'Pick the equation whose missing variable you neither know nor want',
      'All three assume CONSTANT acceleration — never use them when a changes',
      'Signs carry direction: choose one direction as +, and keep it for u, v, a and s',
    ]),
    ContentBlock.paragraph(
      'Distance is the total path length (always positive); displacement is the straight-line change in position (can be negative or zero). A car that drives 100 m forward and 100 m back has distance 200 m but displacement zero. Average speed = distance/time; average velocity = displacement/time — they differ the moment the motion turns around.',
      title: 'Distance vs displacement',
    ),
    ContentBlock.realLife(
      'Braking distance follows v² = u² + 2as with negative a. Double your highway speed and the braking distance becomes FOUR times longer — this single equation is why speed limits exist and why tailgating at 100 km/h is so dangerous.',
    ),
    ContentBlock.mistake(
      'Using the equations of motion when acceleration is not constant — for example while a parachute opens, or when a is given as a function of time. The three equations are valid ONLY for constant a; otherwise you must integrate (JEE) or use graphs.',
    ),
    ContentBlock.mistake(
      'Sign confusion in retardation problems. If you take the direction of motion as positive, braking means a is NEGATIVE. Students who plug a = +5 instead of −5 into v = u + at get a car that speeds up while braking.',
    ),
    ContentBlock.example(
      'A car moving at 20 m/s brakes uniformly and stops in 40 m. Find the retardation.\n\nUse v² = u² + 2as (no time given, none wanted):\n0 = (20)² + 2·a·40\n0 = 400 + 80a\na = −5 m/s².\n\nThe magnitude of retardation is 5 m/s²; the minus sign says it opposes the motion.',
    ),
    ContentBlock.jeeTip(
      'Graphs are half of JEE kinematics: slope of the x–t graph is velocity, slope of the v–t graph is acceleration, and AREA under the v–t graph is displacement. Many "hard" problems collapse to reading a slope or computing a triangle\'s area. Also remember s_nth = u + (a/2)(2n−1) for distance in the nth second.',
    ),
    ContentBlock.neetNote(
      'NEET loves the odd-number ratio for a body starting from rest: distances in successive seconds are 1 : 3 : 5 : 7…, and total distances after equal times are 1 : 4 : 9 : 16…. Also memorise: for a body dropped from rest, v = gt and h = ½gt² with g ≈ 10 m/s² in most NEET numericals.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the definition of acceleration',
      math: 'a = dv/dt  →  dv = a·dt',
      note: 'Constant a lets us integrate both sides directly.',
    ),
    DerivationStep(
      title: 'Integrate velocity from u to v, time from 0 to t',
      math: '∫ᵤᵛ dv = a·∫₀ᵗ dt  →  v − u = at',
      note: 'This is the first equation: v = u + at.',
    ),
    DerivationStep(
      title: 'Use the definition of velocity',
      math: 'v = ds/dt  →  ds = (u + at)·dt',
    ),
    DerivationStep(
      title: 'Integrate displacement from 0 to s',
      math: 's = ut + ½at²',
      note: 'The second equation — position as a function of time.',
    ),
    DerivationStep(
      title: 'Eliminate t using v·dv = a·ds',
      math: '∫ᵤᵛ v·dv = a·∫₀ˢ ds  →  ½(v² − u²) = as',
      note: 'Rearranged: v² = u² + 2as — the third equation, perfect when time is unknown.',
    ),
  ],
  formulas: const [
    FormulaEntry('First equation', 'v = u + at'),
    FormulaEntry('Second equation', 's = ut + ½at²'),
    FormulaEntry('Third equation', 'v² = u² + 2as'),
    FormulaEntry('Distance in nth second', 's_nth = u + (a/2)(2n−1)'),
    FormulaEntry('Average velocity', 'v_avg = (u + v)/2', condition: 'constant a only'),
    FormulaEntry('Free fall', 'v = gt,  h = ½gt²', condition: 'dropped from rest, g ≈ 9.8 m/s²'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A body starts from rest with uniform acceleration 2 m/s². Its velocity after 5 s is:',
      options: ['5 m/s', '10 m/s', '20 m/s', '2.5 m/s'],
      correctIndex: 1,
      solution: 'v = u + at = 0 + 2×5 = 10 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A car covers distances in the ratio 1 : 3 : 5 in successive seconds. Its motion is:',
      options: [
        'Uniform velocity',
        'Uniform acceleration starting from rest',
        'Increasing acceleration',
        'Retarded motion',
      ],
      correctIndex: 1,
      solution:
          'The odd-number ratio 1 : 3 : 5 : 7… is the signature of constant acceleration from rest (Galileo\'s law). It follows from s = ½at².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A bus moving at 72 km/h is brought to rest in 10 s. The retardation is:',
      options: ['7.2 m/s²', '2 m/s²', '3.6 m/s²', '20 m/s²'],
      correctIndex: 1,
      solution:
          'Convert: 72 km/h = 72×(5/18) = 20 m/s. Then a = (v−u)/t = (0−20)/10 = −2 m/s². Retardation = 2 m/s².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A stone is dropped from a tower and falls freely. The distance it covers in the 3rd second (g = 10 m/s²) is:',
      options: ['45 m', '25 m', '15 m', '30 m'],
      correctIndex: 1,
      solution:
          's_nth = u + (g/2)(2n−1) = 0 + 5×(6−1) = 25 m. The nth-second formula saves you two full calculations.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A car at 20 m/s doubles its speed to 40 m/s. If its braking distance from 20 m/s was d, from 40 m/s it will be:',
      options: ['d', '2d', '4d', '√2·d'],
      correctIndex: 2,
      solution:
          'v² = u² + 2as → stopping distance s = u²/(2|a|) ∝ u². Doubling u quadruples the braking distance. This is the exam\'s favourite safety question.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The v–t graph of a particle is a straight line from (0, 10 m/s) to (5 s, 0). Displacement in these 5 s is:',
      options: ['50 m', '25 m', '10 m', '12.5 m'],
      correctIndex: 1,
      solution:
          'Displacement = area under the v–t graph = area of triangle = ½ × 5 × 10 = 25 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A particle\'s position is x = t³ − 6t² + 9t (metres). Its velocity is zero at:',
      options: ['t = 1 s and t = 3 s', 't = 0 only', 't = 2 s only', 't = 3 s only'],
      correctIndex: 0,
      solution:
          'v = dx/dt = 3t² − 12t + 9 = 3(t² − 4t + 3) = 3(t−1)(t−3). So v = 0 at t = 1 s and t = 3 s. Non-constant a → equations of motion don\'t apply; calculus does.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A body starting from rest travels distance x₁ in the first 2 s and x₂ in the next 2 s under constant acceleration. Then x₂ equals:',
      options: ['x₁', '2x₁', '3x₁', '4x₁'],
      correctIndex: 2,
      solution:
          'From rest: distance in first 2s ∝ 2² = 4 units; distance in 4 s ∝ 16 units, so next 2 s covers 12 units. Ratio x₂/x₁ = 12/4 = 3, i.e. x₂ = 3x₁.',
    ),
  ],
  revision: [
    'v = u + at, s = ut + ½at², v² = u² + 2as — valid ONLY for constant a.',
    'Pick the equation missing the variable you don\'t know and don\'t need.',
    'Slope of x–t = velocity; slope of v–t = acceleration; area under v–t = displacement.',
    'From rest: successive-second distances go 1 : 3 : 5 : 7…, totals go 1 : 4 : 9 : 16….',
    'Stopping distance ∝ u² — double the speed, quadruple the distance.',
    's_nth = u + (a/2)(2n−1) for distance covered in the nth second.',
  ],
  sandboxBuilder: (_) => const Motion1DSandbox(),
);
