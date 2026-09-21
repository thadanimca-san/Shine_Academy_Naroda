import '../../models/lesson.dart';
import '../../simulators/motion_2d_sandbox.dart';
import '../../theme/tokens.dart';

/// Projectile Motion — two independent motions wearing one trench coat.
final Lesson motion2dLesson = Lesson(
  topicId: 'projectile-motion',
  title: 'Projectile Motion',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A cricketer can throw a ball at one fixed speed. Which angle sends it farthest — and why do 30° and 60° land it in exactly the same spot?',
  whyItMatters:
      'Projectile motion is the first place physics splits one motion into two independent ones — uniform velocity horizontally, free fall vertically. That single idea (independence of perpendicular motions) is reused in charged particles crossing fields, rivers and boats, and inclined-plane launches. Range, maximum height and time of flight are guaranteed marks in both NEET and JEE.',
  prediction: const PredictionPrompt(
    scenario:
        'You launch two identical balls at the same speed, one at 30° and one at 60° to the ground. Ignoring air resistance, which goes farther?',
    options: [
      'The 30° ball — flatter path, more forward speed',
      'The 60° ball — stays in the air longer',
      'Both land at the same range',
      'Impossible to tell without the speed',
    ],
    correctIndex: 2,
    reveal:
        'Range R = u²·sin(2θ)/g, and sin(60°) = sin(120°) — complementary angles (θ and 90°−θ) give identical ranges. The 60° ball flies higher and longer; the 30° ball flies flatter and faster; they land together. Try it: launch at 30°, keep the trail, then launch at 60°.',
  ),
  experiments: [
    'Launch at 30°, then 60° with the same speed — the trails land on the same spot',
    'Sweep the angle and find the maximum range — it is exactly 45°',
    'Double the launch speed and confirm the range becomes 4× (R ∝ u²)',
    'Watch the height readout: h_max peaks when the vertical speed u·sinθ is biggest (steep angles)',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The whole trick of projectile motion: gravity only acts vertically. So the horizontal motion is uniform velocity (uₓ = u·cosθ, never changing), while the vertical motion is uniformly accelerated (u_y = u·sinθ, decelerating at g, then falling). The two motions run on independent clocks-share only time itself. Solve each axis separately and recombine.',
      title: 'One motion, two independent parts',
    ),
    ContentBlock.formula('uₓ = u·cosθ (constant)     u_y = u·sinθ − g·t',
        title: 'COMPONENT VELOCITIES'),
    ContentBlock.bullets([
      'Time of flight T = 2u·sinθ/g — set by the VERTICAL motion alone',
      'Range R = uₓ × T = u²·sin2θ/g — maximum at θ = 45°',
      'Max height H = u²sin²θ/(2g) — where vertical velocity momentarily = 0',
      'At the top: v_y = 0 but vₓ ≠ 0 — the ball is still moving!',
    ]),
    ContentBlock.paragraph(
      'The path is a parabola because x grows linearly with t while y grows with t and t² together. Eliminating t gives y = x·tanθ − gx²/(2u²cos²θ) — the equation of trajectory. JEE sometimes hands you this equation and asks you to read off θ or u from the coefficients.',
      title: 'Why a parabola',
    ),
    ContentBlock.realLife(
      'Basketball arcs, water fountains, long-jump athletes and artillery all obey the same parabola. Real projectiles fall slightly short of theory because of air drag — which is why javelin throwers release below 45°: drag punishes high, slow arcs more than flat, fast ones.',
    ),
    ContentBlock.mistake(
      'Thinking velocity is zero at the top of the flight. Only the VERTICAL component is zero there; the horizontal component u·cosθ survives untouched. Speed at the top = u·cosθ, and that\'s a favourite trick option in both exams.',
    ),
    ContentBlock.mistake(
      'Using the full speed u in a single-axis equation. Every vertical equation must use u·sinθ, every horizontal one u·cosθ. Mixing them is the single most common projectile error.',
    ),
    ContentBlock.example(
      'A ball is thrown at u = 20 m/s, θ = 30°. Find T, H and R (g = 10 m/s²).\n\nT = 2u·sinθ/g = 2×20×0.5/10 = 2 s\nH = u²sin²θ/2g = 400×0.25/20 = 5 m\nR = u²sin2θ/g = 400×sin60°/10 = 400×0.866/10 ≈ 34.6 m',
    ),
    ContentBlock.jeeTip(
      'For projectiles from a height, or up an incline, do NOT hunt for a formula — go back to components: write x(t) and y(t), apply the landing condition, solve for t first. Also useful: at any instant, velocity direction is tanα = v_y/vₓ; the trajectory equation y = x·tanθ(1 − x/R) is a fast form when range is known.',
    ),
    ContentBlock.neetNote(
      'NEET repeats these facts: max range at 45°; equal ranges for θ and 90°−θ; at maximum height only vₓ remains; T depends only on the vertical component. For a horizontal projectile from height h: T = √(2h/g) — independent of launch speed.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Resolve the launch velocity',
      math: 'uₓ = u·cosθ,   u_y = u·sinθ',
      note: 'Gravity will only touch the y-component.',
    ),
    DerivationStep(
      title: 'Write each axis\'s motion',
      math: 'x = u·cosθ·t\ny = u·sinθ·t − ½g·t²',
      note: 'Uniform velocity in x; equations of motion with a = −g in y.',
    ),
    DerivationStep(
      title: 'Time of flight — set y = 0',
      math: '0 = t(u·sinθ − ½g·t)  →  T = 2u·sinθ/g',
      note: 'The projectile lands when the vertical journey closes.',
    ),
    DerivationStep(
      title: 'Range — horizontal distance in time T',
      math: 'R = u·cosθ · T = 2u²·sinθ·cosθ/g = u²·sin2θ/g',
      note: 'sin2θ is maximum (=1) at θ = 45° → R_max = u²/g.',
    ),
    DerivationStep(
      title: 'Maximum height — v_y = 0 at the top',
      math: '0 = (u·sinθ)² − 2gH  →  H = u²·sin²θ/(2g)',
      note: 'Third equation of motion applied vertically.',
    ),
    DerivationStep(
      title: 'Trajectory — eliminate t',
      math: 'y = x·tanθ − g·x²/(2u²cos²θ)',
      note: 'y is quadratic in x → the path is a parabola.',
    ),
  ],
  formulas: const [
    FormulaEntry('Time of flight', 'T = 2u·sinθ/g'),
    FormulaEntry('Range', 'R = u²·sin2θ/g', condition: 'max at θ = 45°'),
    FormulaEntry('Maximum height', 'H = u²·sin²θ/(2g)'),
    FormulaEntry('Trajectory', 'y = x·tanθ − gx²/(2u²cos²θ)'),
    FormulaEntry('Speed at top', 'v = u·cosθ'),
    FormulaEntry('Horizontal projectile', 'T = √(2h/g),  R = u·√(2h/g)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'At the highest point of a projectile\'s flight, which quantity is zero?',
      options: ['Speed', 'Vertical velocity', 'Horizontal velocity', 'Acceleration'],
      correctIndex: 1,
      solution:
          'Only v_y = 0 at the top. The horizontal velocity u·cosθ is unchanged throughout, and acceleration stays g downward the entire flight.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For which pair of launch angles is the range the same (same speed)?',
      options: ['20° and 80°', '30° and 60°', '45° and 90°', '15° and 85°'],
      correctIndex: 1,
      solution:
          'Ranges match when angles are complementary (θ + φ = 90°): sin2(30°) = sin60° = sin120° = sin2(60°). Only 30° + 60° = 90°.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A ball is projected at 40 m/s at 30°. Its time of flight is (g = 10 m/s²):',
      options: ['2 s', '4 s', '6 s', '8 s'],
      correctIndex: 1,
      solution: 'T = 2u·sinθ/g = 2×40×0.5/10 = 4 s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The maximum range of a gun is 100 m. The maximum height reached when fired for maximum range is:',
      options: ['100 m', '50 m', '25 m', '12.5 m'],
      correctIndex: 2,
      solution:
          'R_max = u²/g = 100 m at 45°. At 45°, H = u²sin²45°/2g = (u²/g)×(1/4) = 25 m. H is a quarter of the max range.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A stone is thrown horizontally at 15 m/s from a 20 m tower. It hits the ground after (g = 10 m/s²):',
      options: ['1.5 s', '2 s', '3 s', '4 s'],
      correctIndex: 1,
      solution:
          'Vertical motion is independent free fall: h = ½gt² → 20 = 5t² → t = 2 s. The horizontal speed is irrelevant to the fall time.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A projectile has range R and maximum height H. The launch angle satisfies:',
      options: ['tanθ = 4H/R', 'tanθ = R/4H', 'tanθ = 2H/R', 'tanθ = H/R'],
      correctIndex: 0,
      solution:
          'H/R = [u²sin²θ/2g]/[u²·2sinθcosθ/g] = tanθ/4 → tanθ = 4H/R. A one-line ratio worth memorising for JEE.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'The equation of a projectile\'s path is y = √3·x − 5x². The launch angle is:',
      options: ['30°', '45°', '60°', '75°'],
      correctIndex: 2,
      solution:
          'Compare with y = x·tanθ − gx²/(2u²cos²θ): tanθ = √3 → θ = 60°. The coefficient of x IS tanθ.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two projectiles are fired at the same speed at 45°+α and 45°−α. The ratio of their times of flight is:',
      options: ['1 : 1', 'tan(45°+α) : tan(45°−α)', 'sin(45°+α) : sin(45°−α)', 'cos(45°+α) : cos(45°−α)'],
      correctIndex: 2,
      solution:
          'T ∝ sinθ (T = 2u·sinθ/g). So T₁/T₂ = sin(45°+α)/sin(45°−α). Equal ranges, unequal flight times.',
    ),
  ],
  revision: [
    'Split into components: uₓ = u·cosθ stays constant; u_y = u·sinθ fights gravity.',
    'T = 2u·sinθ/g, H = u²sin²θ/2g, R = u²sin2θ/g (max at 45°).',
    'Complementary angles (θ, 90°−θ) give equal ranges; the steeper one flies longer.',
    'At the top: v_y = 0, speed = u·cosθ, acceleration still g downward.',
    'tanθ = 4H/R links height, range and angle in one line.',
    'Horizontal throw from height h: fall time √(2h/g), independent of speed.',
  ],
  sandboxBuilder: (_) => const Motion2DSandbox(),
);
