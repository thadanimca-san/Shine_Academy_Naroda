import '../../models/lesson.dart';
import '../../simulators/polarization_sandbox.dart';
import '../../theme/tokens.dart';

/// Polarization — polarizers, Malus's law, Brewster's angle, and real-life uses.
final Lesson polarizationLesson = Lesson(
  topicId: 'polarization',
  title: 'Polarization',
  accentColor: Palette.chOptics,
  bigQuestion:
      'Take two pairs of polarized sunglasses, hold one behind the other, and slowly rotate one of them. At most angles some light gets through — but at exactly 90°, the pair of lenses go completely BLACK, blocking essentially all light. Neither lens absorbs much light on its own — so where does the light actually go when the two are crossed?',
  whyItMatters:
      'Polarization is the single cleanest piece of evidence that light is a TRANSVERSE wave — a fact NEET tests directly and often by contrast with sound (a longitudinal wave, which cannot be polarized at all). Malus\'s law is a short, self-contained, numerically friendly formula that appears constantly in both exams, and Brewster\'s angle links polarization back to reflection and refraction from earlier topics.',
  prediction: const PredictionPrompt(
    scenario:
        'Unpolarized light passes through a polarizer, then through a second polarizer (the "analyzer") whose transmission axis is rotated by an angle θ relative to the first. As θ is increased from 0° to 90°, the intensity of light reaching the screen:',
    options: [
      'Stays constant — polarizers only block light at 90°, nothing in between',
      'Decreases smoothly, following I = I0 cos²θ, reaching exactly zero at θ = 90°',
      'Decreases linearly with θ',
      'Increases as θ increases',
    ],
    correctIndex: 1,
    reveal:
        'The intensity follows Malus\'s law, I = I0 cos²θ — a smooth curve, not a sudden on/off switch, and it reaches EXACTLY zero only at θ = 90° (crossed polarizers). In the lab, drag θ from 0° to 90° and watch the transmitted intensity readout fall smoothly along the cos²θ curve, going completely dark only at the very end.',
  ),
  experiments: [
    'Set θ = 0° (axes aligned) and confirm all the polarized light passes through (I/I0 = 1)',
    'Set θ = 90° (crossed polarizers) and watch the transmitted intensity readout drop to zero',
    'Set θ = 45° and check that I/I0 = cos²45° = 0.5, exactly half the maximum',
    'Sweep θ slowly and watch the intensity fall along the smooth cos²θ curve, not a straight line',
    'Notice the beam between the two filters is always polarized along the FIRST filter\'s axis, regardless of θ',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Ordinary light sources (the sun, a bulb) emit unpolarized light — countless waves whose electric field vibrates in every possible direction perpendicular to the direction of travel, with no preferred plane. Polarized light, in contrast, has its electric field vibrating in just ONE fixed plane. Only transverse waves (where the vibration is perpendicular to the direction of travel) can be polarized — a longitudinal wave, like sound, vibrates ALONG its direction of travel and has no perpendicular plane to restrict, so it simply cannot be polarized.',
      title: 'Unpolarized vs. polarized light',
    ),
    ContentBlock.neetNote(
      'The fact that light CAN be polarized (while sound cannot) is one of the most direct experimental proofs that light is a TRANSVERSE wave — a favourite standalone NEET fact, often tested as a pure conceptual question with no numbers involved.',
    ),
    ContentBlock.paragraph(
      'A polarizer is a filter (commonly made of a material called Polaroid) that only transmits the component of the electric field along its own transmission axis, blocking the perpendicular component. Passing unpolarized light through a single polarizer produces light polarized along that polarizer\'s axis, at exactly half the original intensity (since, on average, half the field component along any given direction survives).',
      title: 'The polarizer',
    ),
    ContentBlock.paragraph(
      'A second polarizer placed after the first is called the analyzer — its job is to test (analyze) the polarization state of the light coming from the first polarizer. If the analyzer\'s transmission axis is rotated by angle θ relative to the polarizer\'s axis, only the COMPONENT of the already-polarized electric field along the analyzer\'s axis gets through.',
      title: 'The analyzer',
    ),
    ContentBlock.formula('I = I0 cos²θ', title: 'MALUS\'S LAW'),
    ContentBlock.paragraph(
      'I0 is the intensity of the (already polarized) light arriving at the analyzer, θ is the angle between the polarizer\'s and analyzer\'s transmission axes, and I is the intensity that emerges. At θ = 0° (axes aligned), I = I0 — full transmission. At θ = 90° (crossed polarizers), I = 0 — complete blocking. At θ = 45°, exactly half the intensity survives (cos²45° = 0.5).',
      title: 'Malus\'s law explained',
    ),
    ContentBlock.paragraph(
      'Ordinary reflection can also polarize light, even from a completely everyday surface like water, glass, or a road. At one particular angle of incidence — called Brewster\'s angle θB — the reflected ray becomes COMPLETELY (100%) polarized, with its electric field vibrating perpendicular to the plane of incidence. This special condition occurs exactly when the reflected ray and the refracted ray are perpendicular to each other.',
      title: 'Polarization by reflection: Brewster\'s angle',
    ),
    ContentBlock.formula('tanθB = n', title: 'BREWSTER\'S ANGLE'),
    ContentBlock.paragraph(
      'n is the refractive index of the reflecting medium (relative to the medium the light travels in, usually air). At this angle, the reflected and refracted rays are perpendicular, i.e. θB + θr = 90°, which combined with Snell\'s law gives the simple relation tanθB = n.',
      title: 'Where tanθB = n comes from',
    ),
    ContentBlock.realLife(
      'Polarized sunglasses block the strongly horizontally-polarized glare that reflects off horizontal surfaces like water, snow, or roads (light reflecting near Brewster\'s angle off these surfaces is heavily polarized), letting through the less intense unpolarized light directly from objects and cutting glare dramatically. LCD screens use polarizing filters combined with liquid crystals that rotate the plane of polarization to control pixel brightness. 3D cinema glasses use polarization (or its circular variant) to send a DIFFERENT image to each eye — each lens is a polarizer oriented to pass only the light meant for that eye.',
    ),
    ContentBlock.mistake(
      'Believing sound waves can also be polarized, "just like light." Sound is a LONGITUDINAL wave — its vibration is along the direction of propagation, so there is no perpendicular plane to restrict, and polarization is simply impossible for sound. This distinguishes transverse waves (light, which CAN be polarized) from longitudinal waves (sound, which CANNOT).',
    ),
    ContentBlock.mistake(
      'Assuming crossed polarizers (θ = 90°) block ALL light gradually and evenly as θ increases from 0° in a straight-line fashion. The relationship is cos²θ, a curve — the intensity actually falls off SLOWLY near θ = 0° and drops steeply as θ approaches 90°, not at a constant rate.',
    ),
    ContentBlock.example(
      'Unpolarized light of intensity I0 passes through a polarizer (emerging at I0/2), then through an analyzer whose axis is at 60° to the polarizer\'s axis. Find the final intensity.\n\nAfter the polarizer: I1 = I0/2.\nMalus\'s law at the analyzer: I2 = I1 cos²(60°) = (I0/2)(0.5)² = (I0/2)(0.25) = I0/8.\n\nSo only one-eighth of the original unpolarized intensity survives both filters.',
    ),
    ContentBlock.jeeTip(
      'When a problem involves UNPOLARIZED light hitting the FIRST polarizer, always halve the intensity at that first stage (I1 = I0/2) before applying Malus\'s law for any SUBSEQUENT polarizers — Malus\'s law (I = I0cos²θ) applies only when the incoming light is already polarized, which is the case starting from the second filter onward.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the number of polarizers/analyzers needed to achieve a certain fractional intensity, or direct numerical evaluations of cos²θ at standard angles (0°, 30°, 45°, 60°, 90°) — memorising cos²30° = 3/4, cos²45° = 1/2, cos²60° = 1/4 speeds up these questions considerably.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Represent the polarized electric field arriving at the analyzer',
      math: 'E0 = amplitude of the light emerging from the first polarizer, oscillating along ITS transmission axis',
    ),
    DerivationStep(
      title: 'Resolve E0 into components along and perpendicular to the analyzer\'s axis',
      math: 'Component along analyzer axis = E0 cosθ;  component perpendicular = E0 sinθ',
      note: 'θ is the angle between the polarizer\'s and analyzer\'s transmission axes.',
    ),
    DerivationStep(
      title: 'Only the parallel component is transmitted',
      math: 'The analyzer blocks the perpendicular component entirely and transmits only E = E0 cosθ',
    ),
    DerivationStep(
      title: 'Convert amplitude to intensity (intensity ∝ amplitude²)',
      math: 'I ∝ E² = E0² cos²θ = I0 cos²θ',
      note: 'Malus\'s law — I0 here is the intensity of the ALREADY POLARIZED light reaching the analyzer, not the original unpolarized source intensity.',
    ),
  ],
  formulas: const [
    FormulaEntry('Malus\'s law', 'I = I0 cos²θ'),
    FormulaEntry('Intensity after first polarizer (from unpolarized light)', 'I1 = I0(unpolarized)/2'),
    FormulaEntry('Brewster\'s angle', 'tanθB = n'),
    FormulaEntry('Brewster condition (geometric)', 'θB + θrefraction = 90°'),
    FormulaEntry('Standard values', 'cos²30° = 3/4,  cos²45° = 1/2,  cos²60° = 1/4'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Which of the following waves CANNOT be polarized?',
      options: ['Light waves', 'Radio waves', 'Sound waves (in air)', 'Microwaves'],
      correctIndex: 2,
      solution: 'Sound in air is a LONGITUDINAL wave; polarization requires a transverse wave, so sound cannot be polarized. Light, radio, and microwaves are all transverse electromagnetic waves and CAN be polarized.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two polarizers are crossed (their transmission axes at 90° to each other). The intensity of light transmitted through both is:',
      options: ['I0', 'I0/2', 'Zero', 'I0/4'],
      correctIndex: 2,
      solution: 'By Malus\'s law, I = I0cos²(90°) = I0 × 0 = 0. Crossed polarizers block all the light.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Polarized light of intensity I0 is incident on an analyzer whose axis makes a 45° angle with the polarization direction. The transmitted intensity is:',
      options: ['I0', 'I0/2', 'I0/4', 'Zero'],
      correctIndex: 1,
      solution: 'I = I0cos²(45°) = I0 × (1/√2)² = I0 × 0.5 = I0/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Unpolarized light of intensity I0 passes through a single polarizer. The intensity emerging is:',
      options: ['I0', 'I0/2', 'I0/4', 'Zero'],
      correctIndex: 1,
      solution: 'A single polarizer transmits exactly half the intensity of unpolarized light, regardless of its axis orientation (by symmetry, averaging over all incoming vibration directions).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Unpolarized light of intensity I0 passes through a polarizer, then an analyzer at 60° to the polarizer\'s axis. The final transmitted intensity is:',
      options: ['I0/8', 'I0/4', 'I0/2', 'I0×0.75'],
      correctIndex: 0,
      solution: 'After the polarizer: I1 = I0/2. After the analyzer: I2 = I1cos²(60°) = (I0/2)(0.25) = I0/8.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Light reflecting off a glass surface (n = 1.5) is completely polarized when the angle of incidence equals Brewster\'s angle. This angle is approximately:',
      options: ['33.7°', '48.6°', '56.3°', '61.9°'],
      correctIndex: 2,
      solution: 'tanθB = n = 1.5 → θB = tan⁻¹(1.5) ≈ 56.3°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'At Brewster\'s angle, the angle between the reflected ray and the refracted ray is:',
      options: ['0°', '45°', '90°', '180°'],
      correctIndex: 2,
      solution: 'Brewster\'s angle is defined precisely by the condition that the reflected and refracted rays are perpendicular to each other (θB + θrefraction = 90°).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Three polarizers are stacked: the first and third are crossed (90° apart), with a THIRD polarizer inserted between them at 45° to both. Unpolarized light of intensity I0 is incident. The final transmitted intensity is:',
      options: ['Zero (still crossed, no change)', 'I0/8', 'I0/4', 'I0/2'],
      correctIndex: 1,
      solution: 'After polarizer 1: I0/2. After the middle polarizer (45° from polarizer 1): (I0/2)cos²45° = I0/4. After polarizer 3 (45° from the middle one): (I0/4)cos²45° = I0/8. Inserting the middle polarizer actually lets SOME light through, unlike the fully crossed pair alone!',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Polarized sunglasses reduce glare from a wet road primarily because:',
      options: [
        'They absorb all colours of light equally',
        'Reflected glare off horizontal surfaces is strongly polarized (horizontally), and the sunglasses\' polarizing axis blocks that component',
        'They magnify the image of the road',
        'They convert visible light into infrared',
      ],
      correctIndex: 1,
      solution: 'Reflected light off horizontal surfaces near Brewster\'s angle is heavily polarized in the horizontal direction; polarized sunglasses are oriented to block this component, cutting glare while letting other light through.',
    ),
  ],
  revision: [
    'Unpolarized light vibrates in all directions perpendicular to its motion; polarized light vibrates in just one plane.',
    'Only TRANSVERSE waves can be polarized — sound (longitudinal) cannot, proving light is transverse.',
    'A single polarizer transmits half the intensity of unpolarized light and polarizes it along its own axis.',
    'Malus\'s law: I = I0cos²θ, applied to ALREADY polarized light hitting a second filter (the analyzer).',
    'θ = 0° → full transmission; θ = 90° (crossed) → zero transmission; θ = 45° → half transmission.',
    'Brewster\'s angle: tanθB = n; reflected ray is completely polarized when reflected and refracted rays are perpendicular.',
    'Real-life uses: polarized sunglasses (glare reduction), LCD screens, 3D cinema glasses.',
  ],
  sandboxBuilder: (_) => const PolarizationSandbox(),
);
