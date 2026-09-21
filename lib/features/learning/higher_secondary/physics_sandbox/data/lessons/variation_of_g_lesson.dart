import '../../models/lesson.dart';
import '../../simulators/gravity_variation_sim.dart';
import '../../theme/tokens.dart';

/// Variation of g — why gravity isn't the same everywhere on (or above, or below) Earth.
final Lesson variationOfGLesson = Lesson(
  topicId: 'variation-of-g',
  title: 'Variation of g',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'We treat g = 9.8 m/s² as a fixed number in almost every problem. But is it really the same at the top of Mount Everest, at the bottom of a mine shaft, and at the equator versus the poles? If not, which direction does it change, and why?',
  whyItMatters:
      'g is not a universal constant — it is a LOCAL consequence of gravitation that depends on how far you are from Earth\'s centre and even on Earth\'s own rotation. Understanding how g varies with height, depth, and latitude is essential for satellite and mining engineering, explains why polar expeditions weigh very slightly more, and is one of the most frequently tested conceptual + numerical combinations in NEET and JEE gravitation.',
  prediction: const PredictionPrompt(
    scenario:
        'You have a sensitive weighing scale. You take it to the top of a tall mountain, and separately to the bottom of a deep mine. In which case does g decrease FASTER per kilometre of distance from the surface?',
    options: [
      'They decrease at the same rate — distance from the surface is what matters',
      'g decreases faster going UP (height) than going DOWN (depth) for the same distance',
      'g decreases faster going DOWN (depth) than going UP (height) for the same distance',
      'g does not change with either height or depth, only with latitude',
    ],
    correctIndex: 1,
    reveal:
        'Going up, g_h = g(1 − 2h/R) falls off with a factor of 2 in front of h. Going down, g_d = g(1 − d/R) falls off with just a factor of 1. So for equal small distances, height reduces g about TWICE as fast as depth does. In the lab, move the test mass an equal distance above and below the surface and compare the g readouts — the "above" case drops noticeably more.',
  ),
  experiments: [
    'Raise the test point above the surface and watch g decrease — check it roughly matches g(1−2h/R) for small h',
    'Lower the test point below the surface and watch g decrease more slowly than for the same distance above',
    'Push the depth all the way to Earth\'s centre — watch g go all the way to exactly zero',
    'Switch on Earth\'s rotation and slide the test point from pole to equator — watch g dip slightly at the equator',
    'Compare the equatorial dip caused by centrifugal effect against the (larger) dip caused by Earth\'s equatorial bulge',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The formula g = GM/R² assumes you are measuring g exactly at Earth\'s mean surface, treating Earth as a perfect non-rotating sphere. In reality g changes in three distinct ways: with height above the surface, with depth below the surface, and with latitude (because of Earth\'s rotation and its slightly non-spherical, oblate shape). Each has a different formula and a different physical reason.',
      title: 'g is local, not universal',
    ),
    ContentBlock.formula('g_h = g·(1 − 2h/R)   for h ≪ R', title: 'VARIATION WITH HEIGHT'),
    ContentBlock.paragraph(
      'Above the surface, you are simply farther from Earth\'s centre, so g = GM/(R+h)² decreases because the denominator grows. For h much smaller than R, this can be linearised (binomial approximation) to the simple form above — a good approximation for aircraft and mountain altitudes, but not for satellites, where you must use the full GM/(R+h)² instead.',
      title: 'Above the surface: farther from the centre',
    ),
    ContentBlock.formula('g_d = g·(1 − d/R)   for depth d below the surface', title: 'VARIATION WITH DEPTH'),
    ContentBlock.paragraph(
      'Below the surface, only the mass ENCLOSED within radius (R−d) contributes to gravity at that depth — by a shell theorem, the mass in the shell OUTSIDE your position exerts zero net gravitational pull on you. As you go deeper, less mass is "under" you, so g decreases roughly linearly, reaching EXACTLY ZERO at Earth\'s centre, where you are surrounded symmetrically and pulled equally in all directions.',
      title: 'Below the surface: less mass "pulling from below"',
    ),
    ContentBlock.bullets([
      'g decreases going UP, roughly as g(1 − 2h/R) for small h',
      'g decreases going DOWN, roughly as g(1 − d/R), reaching zero at the centre',
      'For the same small distance, height reduces g about TWICE as fast as depth (factor 2 vs factor 1)',
      'g varies with LATITUDE due to Earth\'s rotation (centrifugal effect) and its equatorial bulge (oblate shape)',
    ]),
    ContentBlock.paragraph(
      'Earth spins, so any point away from the poles moves in a circle and needs centripetal force directed toward Earth\'s axis. Part of the true gravitational pull is "used up" providing this centripetal force, so the NET downward pull you feel (the effective or apparent g) is slightly less than the true gravitational g. This effect is zero at the poles (on the rotation axis itself) and maximum at the equator (farthest from the axis, moving fastest).',
      title: 'Rotation: the centrifugal reduction',
    ),
    ContentBlock.formula('g_eff = g − ω²R·cos²λ   (λ = latitude)', title: 'VARIATION WITH LATITUDE (ROTATION EFFECT)'),
    ContentBlock.realLife(
      'Earth is not a perfect sphere — it bulges slightly at the equator due to its own rotation (equatorial radius is about 21 km more than polar radius). Because g ∝ 1/R², this shape difference ALONE makes g slightly larger at the poles even ignoring rotation. Combined, the two effects mean g_equator ≈ 9.78 m/s² while g_pole ≈ 9.83 m/s² — a small but very real and measurable difference used by geodesists and precision instrument calibrators.',
    ),
    ContentBlock.mistake(
      'Using g_h = g(1−2h/R) for satellite altitudes, where h is comparable to R. This linear approximation is only valid for h ≪ R (mountains, aircraft); for satellites you must use the exact g_h = GM/(R+h)² = g·R²/(R+h)², otherwise the answer is significantly wrong.',
    ),
    ContentBlock.mistake(
      'Forgetting that g becomes exactly zero only at Earth\'s CENTRE, not at some shallow depth. Students sometimes assume g=0 happens quickly with small depth; in fact g decreases only gradually and linearly, reaching zero only when d = R (the very centre).',
    ),
    ContentBlock.example(
      'Find g at a height of 32 km above Earth\'s surface (R = 6400 km, g = 9.8 m/s²) using the approximation for small h.\n\ng_h = g(1 − 2h/R) = 9.8 × (1 − 2×32/6400) = 9.8 × (1 − 0.01) = 9.8 × 0.99 = 9.702 m/s².\n\nA tiny 32 km climb (less than Everest\'s height above sea level by comparison to Earth\'s radius) barely dents g — this is why we treat g as constant for everyday problems.',
    ),
    ContentBlock.jeeTip(
      'For depth AND height problems together, remember the asymmetry: at equal small distances from the surface, g_height drops about twice as fast as g_depth. This is a favourite "which is smaller" conceptual JEE question, and the reason is structural — height moves the ENTIRE mass farther away (inverse-square), while depth only removes a thin outer shell\'s worth of mass from "pulling on you," leaving the closer remaining mass still nearly as effective.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests direct plug-in numericals for both g_h and g_d, plus the conceptual fact g=0 at Earth\'s centre. Also expect a qualitative latitude question: g is minimum at the equator and maximum at the poles, due to both the centrifugal effect (zero at poles, maximum at equator) and Earth\'s equatorial bulge (poles are physically closer to the centre of mass).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from g at radius R, and g at height h above it',
      math: 'g = GM/R²,   g_h = GM/(R+h)²',
    ),
    DerivationStep(
      title: 'Form the ratio and factor out R²',
      math: 'g_h/g = R²/(R+h)² = 1/(1+h/R)²',
    ),
    DerivationStep(
      title: 'Apply the binomial approximation for h ≪ R',
      math: '(1+h/R)⁻² ≈ 1 − 2h/R',
      note: 'Valid when h/R is small, so higher-order terms can be dropped.',
    ),
    DerivationStep(
      title: 'Height result',
      math: 'g_h ≈ g·(1 − 2h/R)',
    ),
    DerivationStep(
      title: 'For depth d, only enclosed mass M\' = M(R−d)³/R³ contributes (uniform density)',
      math: 'g_d = GM\'/(R−d)² = GM(R−d)³/[R³(R−d)²] = GM(R−d)/R³ = g·(R−d)/R',
      note: 'Simplify: g_d = g·(1 − d/R) — exact for uniform density, and it reaches zero precisely at d = R (Earth\'s centre).',
    ),
  ],
  formulas: const [
    FormulaEntry('g at height h (h ≪ R)', 'g_h = g(1 − 2h/R)'),
    FormulaEntry('g at height h (exact)', 'g_h = GM/(R+h)² = gR²/(R+h)²'),
    FormulaEntry('g at depth d', 'g_d = g(1 − d/R)'),
    FormulaEntry('g at Earth\'s centre', 'g_centre = 0'),
    FormulaEntry('g at latitude λ (rotation effect)', 'g_eff = g − ω²R cos²λ'),
    FormulaEntry('g at the poles vs equator', 'g_pole > g_equator', condition: 'rotation + equatorial bulge'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'As you go deeper below Earth\'s surface, the value of g:',
      options: ['Increases steadily', 'Decreases, reaching zero at the centre', 'Stays constant', 'First increases then decreases'],
      correctIndex: 1,
      solution: 'g_d = g(1 − d/R) decreases linearly with depth (uniform density assumption) and becomes exactly zero at d = R, i.e. at Earth\'s centre.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Compared to the poles, the value of g at the equator is:',
      options: ['Larger', 'Smaller', 'Exactly equal', 'Zero'],
      correctIndex: 1,
      solution: 'g is smaller at the equator due to both the centrifugal effect of Earth\'s rotation and the equatorial bulge (larger radius there).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'At what depth below Earth\'s surface does g reduce to half its surface value (assume uniform density, R = 6400 km)?',
      options: ['1600 km', '3200 km', '4800 km', '6400 km'],
      correctIndex: 1,
      solution: 'g_d = g(1−d/R) = g/2 → 1 − d/R = 1/2 → d = R/2 = 3200 km.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'At what height above Earth\'s surface does g reduce to half its surface value, using the approximation g_h = g(1−2h/R)?',
      options: ['R/4', 'R/2', 'R', '2R'],
      correctIndex: 0,
      solution: 'g(1−2h/R) = g/2 → 1 − 2h/R = 1/2 → 2h/R = 1/2 → h = R/4.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'For the same small distance x from Earth\'s surface, comparing g at height x versus g at depth x:',
      options: [
        'g decreases equally in both cases',
        'g decreases about twice as fast going up as going down',
        'g decreases about twice as fast going down as going up',
        'g increases going up and decreases going down',
      ],
      correctIndex: 1,
      solution: 'g_h ≈ g(1−2x/R) vs g_d = g(1−x/R). The height formula has coefficient 2 versus depth\'s coefficient 1, so g falls off faster with height than with an equal depth.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The reduction in effective g at the equator due to Earth\'s rotation alone (ignoring the bulge) is given by:',
      options: ['ω²R', 'ω²R²', 'ωR', 'ω²/R'],
      correctIndex: 0,
      solution: 'g_eff = g − ω²R cos²λ. At the equator λ=0, cos²λ=1, so the reduction is exactly ω²R.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'If Earth stopped rotating entirely, the value of g at the equator would:',
      options: [
        'Decrease further',
        'Increase slightly, since the centrifugal reduction would vanish',
        'Remain exactly the same',
        'Become zero',
      ],
      correctIndex: 1,
      solution: 'The rotation currently REDUCES effective g at the equator via g_eff = g − ω²R cos²λ. With ω=0, that reduction term disappears, so measured g at the equator would increase slightly (approaching the pure gravitational g).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A body weighs W at the poles. Considering only the rotational (centrifugal) effect, at what latitude λ would its apparent weight be exactly midway between its equatorial and polar values?',
      options: ['cos²λ = 1/2', 'cos²λ = 1', 'sin λ = 1/2', 'λ = 0°'],
      correctIndex: 0,
      solution: 'Weight reduction ∝ cos²λ (max at equator λ=0 giving cos²λ=1, zero at poles λ=90° giving cos²λ=0). Halfway reduction requires cos²λ = 1/2, i.e. λ = 45°.',
    ),
  ],
  revision: [
    'g = GM/R² is a LOCAL value, not a universal constant — it changes with height, depth, and latitude.',
    'g decreases with height: g_h ≈ g(1−2h/R) for h≪R; use the exact GM/(R+h)² for large h (satellites).',
    'g decreases with depth: g_d = g(1−d/R), reaching exactly zero at Earth\'s centre.',
    'For equal small distances, height reduces g about twice as fast as depth does.',
    'g varies with latitude: g_eff = g − ω²R cos²λ — minimum at the equator, maximum at the poles.',
    'Earth\'s equatorial bulge (larger radius there) further reduces g at the equator, on top of the rotation effect.',
    'g_pole (≈9.83 m/s²) > g_equator (≈9.78 m/s²) due to BOTH rotation and Earth\'s oblate shape.',
  ],
  sandboxBuilder: (_) => const GravityVariationSimulator(),
);
