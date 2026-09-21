import '../../models/lesson.dart';
import '../../simulators/prism_dispersion_sandbox.dart';
import '../../theme/tokens.dart';

/// Prism & Dispersion — deviation through a prism and the splitting of white light.
final Lesson prismDispersionLesson = Lesson(
  topicId: 'prism-dispersion',
  title: 'Prism & Dispersion',
  accentColor: Palette.chOptics,
  bigQuestion:
      'Shine a beam of ordinary white sunlight through a triangular glass prism and a full rainbow spreads out on the far wall — red, orange, yellow, green, blue, violet, in order, every time. The prism didn\'t ADD any colour to the light. So where was the rainbow hiding inside "white" light all along?',
  whyItMatters:
      'The prism is the classic device that reveals white light is actually a mixture of colours, each bending by a slightly different amount — a direct, visual proof of how refractive index depends on wavelength. Prism-deviation numericals (especially the minimum-deviation formula) are a NEET/JEE staple, and dispersion is the conceptual seed for rainbows, chromatic aberration in lenses, and spectrometers.',
  prediction: const PredictionPrompt(
    scenario:
        'White light enters a glass prism and splits into a spectrum on the far side. Compared to red light, violet light:',
    options: [
      'Bends by exactly the same amount as red light (only the entry angle matters)',
      'Bends LESS than red light, since violet has more energy and less needs deflecting',
      'Bends MORE than red light, because glass has a slightly higher refractive index for violet than for red',
      'Does not bend at all — only red and yellow refract in glass',
    ],
    correctIndex: 2,
    reveal:
        'Refractive index is not quite constant — it depends weakly on wavelength, and for ordinary (normal) dispersion, shorter wavelengths (violet) experience a HIGHER refractive index than longer wavelengths (red). A higher n means more bending at each face, so violet emerges deviated the most and red the least. In the lab, switch to "white light (dispersion)" and watch the six rays fan out, violet swinging farthest from the original direction.',
  ),
  experiments: [
    'With a single colour, sweep the angle of incidence i1 and watch how the deviation δ changes — find the minimum',
    'Read off r1 and r2 and confirm r1 + r2 always equals the prism angle A',
    'Switch on dispersion and watch the six colour rays emerge fanned out, violet bending most, red least',
    'Increase the prism angle A and see the whole spectrum fan out wider',
    'Push the angle of incidence to an extreme and find where total internal reflection kills the emergent ray at the second face',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A prism is a transparent block with two flat refracting faces meeting at an angle A (the "angle of the prism" or apex angle). A ray of light refracts TWICE — once entering the first face, once leaving the second — and the two refractions together bend the ray toward the base of the prism, away from its original direction.',
      title: 'Two refractions, one prism',
    ),
    ContentBlock.formula('r1 + r2 = A', title: 'GEOMETRY OF THE PRISM'),
    ContentBlock.formula('δ = (i1 + i2) − A', title: 'ANGLE OF DEVIATION'),
    ContentBlock.paragraph(
      'i1 is the angle of incidence at the first face, r1 the angle of refraction there; r2 is the angle of incidence (inside the glass) at the second face, and i2 the angle of emergence there. The prism\'s geometry forces r1 + r2 = A always. The total deviation δ — the angle between the original and final directions of the ray — is (i1 + i2) − A.',
      title: 'Tracking the ray through both faces',
    ),
    ContentBlock.paragraph(
      'As i1 is varied, δ first decreases, reaches a single minimum value δm, then increases again. At exactly this minimum, the ray passes through the prism symmetrically: i1 = i2 and r1 = r2 = A/2. This special, easily reproducible condition gives the cleanest way to measure a prism\'s refractive index in the lab.',
      title: 'Minimum deviation — the symmetric ray path',
    ),
    ContentBlock.formula('n = sin((A + δm)/2) / sin(A/2)', title: 'PRISM FORMULA (AT MINIMUM DEVIATION)'),
    ContentBlock.paragraph(
      'Refractive index is not truly a single fixed number for a material — it depends slightly on the wavelength of light, a phenomenon called dispersion. For ordinary transparent materials (normal dispersion), shorter wavelengths (violet, blue) experience a HIGHER refractive index than longer wavelengths (red, orange), so n_violet > n_red. This is why violet refracts (bends) more than red at every interface.',
      title: 'Why refractive index depends on colour',
    ),
    ContentBlock.bullets([
      'Each colour has its own refractive index and hence its own r1, r2, and δ',
      'Violet has the highest n → bends the most → largest deviation',
      'Red has the lowest n → bends the least → smallest deviation',
      'The angular spread between the extreme colours (violet and red) is called the ANGULAR DISPERSION',
    ], title: 'Dispersion inside the prism'),
    ContentBlock.paragraph(
      'Angular dispersion (δ_violet − δ_red) is a DIFFERENT quantity from the deviation δ of any single colour — deviation tells you how far one wavelength bent from its original path, while angular dispersion tells you how widely the different colours have been spread APART from each other. A prism with strong dispersion but modest average deviation is what a good spectrometer prism needs.',
      title: 'Deviation vs. angular dispersion — do not confuse them',
    ),
    ContentBlock.realLife(
      'A rainbow forms inside raindrops through the SAME three ingredients as a prism experiment: light refracts entering the drop (splitting into colours via dispersion), totally internally reflects once off the back of the drop, then refracts again on the way out — sending each colour to your eye from a slightly different angle, painting the familiar arc with red on the outside and violet on the inside (for a primary rainbow).',
    ),
    ContentBlock.mistake(
      'Confusing angular dispersion with the deviation δ of a single colour. δ is how far ONE wavelength deviates from its original direction; angular dispersion is the ANGLE BETWEEN two different colours\' emergent rays. A prism can have a large δ for yellow light yet a small angular dispersion (poor colour-splitting power), or vice versa.',
    ),
    ContentBlock.mistake(
      'Assuming the minimum-deviation condition (i1 = i2, r1 = r2 = A/2) holds for EVERY angle of incidence. It is a special, symmetric configuration that occurs at exactly one value of i1 for a given prism and wavelength — not the general case.',
    ),
    ContentBlock.example(
      'A prism of angle 60° gives a minimum deviation of 30° for a certain wavelength. Find the refractive index.\n\nn = sin((A + δm)/2) / sin(A/2) = sin((60° + 30°)/2) / sin(30°) = sin(45°) / sin(30°)\n= 0.7071 / 0.5 = 1.414 ≈ √2.',
    ),
    ContentBlock.jeeTip(
      'For a thin prism (small angle A) with small angles of incidence, the deviation simplifies to δ ≈ (n − 1)A — independent of i1. This small-angle approximation is frequently used in combination problems (e.g. achromatic prism combinations) to avoid heavy trigonometry.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests the ordering of colours by deviation and wavelength: violet has the shortest wavelength, highest frequency, highest refractive index, and bends MOST; red has the longest wavelength, lowest frequency, lowest refractive index, and bends LEAST. This ordering is the same reason the sky is blue (Rayleigh scattering favours short wavelengths) — a frequently paired NEET fact.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the ray path through the prism',
      math: 'Incidence i1 at face 1 → refraction r1; travels inside; incidence r2 at face 2 → emergence i2',
      note: 'The prism\'s two faces meet at apex angle A.',
    ),
    DerivationStep(
      title: 'Use the geometry of the triangle formed by the ray and the two normals',
      math: 'r1 + r2 = A',
      note: 'Follows directly from the angle sum in the quadrilateral formed by the two normals and the two prism faces.',
    ),
    DerivationStep(
      title: 'Add up the total bending at each face',
      math: 'Deviation at face 1 = i1 − r1;  deviation at face 2 = i2 − r2\nTotal: δ = (i1 − r1) + (i2 − r2) = (i1 + i2) − (r1 + r2)',
    ),
    DerivationStep(
      title: 'Substitute r1 + r2 = A',
      math: 'δ = (i1 + i2) − A',
      note: 'The angle-of-deviation formula.',
    ),
    DerivationStep(
      title: 'Apply the symmetric condition at minimum deviation',
      math: 'At δ = δm: i1 = i2 = i,  r1 = r2 = A/2,  and i = (A + δm)/2',
      note: 'By Snell\'s law at face 1: n = sin i / sin r1 = sin((A+δm)/2) / sin(A/2) — the prism formula.',
    ),
  ],
  formulas: const [
    FormulaEntry('Prism geometry', 'r1 + r2 = A'),
    FormulaEntry('Angle of deviation', 'δ = (i1 + i2) − A'),
    FormulaEntry('Prism formula (minimum deviation)', 'n = sin((A + δm)/2) / sin(A/2)'),
    FormulaEntry('Thin-prism approximation', 'δ ≈ (n − 1)A', condition: 'small A, small i1'),
    FormulaEntry('Minimum deviation symmetric condition', 'i1 = i2,  r1 = r2 = A/2'),
    FormulaEntry('Angular dispersion', 'θ = δ_violet − δ_red'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Inside a glass prism, which colour of visible light bends the MOST?',
      options: ['Red', 'Green', 'Violet', 'Yellow'],
      correctIndex: 2,
      solution: 'Violet has the highest refractive index in glass (shortest wavelength), so it refracts (bends) the most at each face.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The relation connecting the prism angle A and the two internal refraction angles r1, r2 is:',
      options: ['r1 − r2 = A', 'r1 + r2 = A', 'r1 × r2 = A', 'r1 + r2 = 2A'],
      correctIndex: 1,
      solution: 'From the geometry of the prism triangle, r1 + r2 = A always, regardless of the angle of incidence.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A prism of angle 60° is made of glass of refractive index √2. The angle of minimum deviation is:',
      options: ['30°', '45°', '60°', '20°'],
      correctIndex: 0,
      solution: 'n = sin((A+δm)/2)/sin(A/2) → √2 = sin((60+δm)/2)/sin30° = sin((60+δm)/2)/0.5 → sin((60+δm)/2) = √2×0.5 = 0.7071 → (60+δm)/2 = 45° → δm = 30°.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'At the position of minimum deviation in a prism, the relationship between the angle of incidence i1 and the angle of emergence i2 is:',
      options: ['i1 = 2i2', 'i1 = i2', 'i1 + i2 = 90°', 'i2 = 0'],
      correctIndex: 1,
      solution: 'At minimum deviation the ray path is symmetric inside the prism: i1 = i2 and r1 = r2 = A/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'For a thin prism of angle 5° and refractive index 1.6, the deviation (small-angle approximation) is approximately:',
      options: ['3°', '6°', '8°', '1.5°'],
      correctIndex: 0,
      solution: 'δ ≈ (n − 1)A = (1.6 − 1) × 5° = 0.6 × 5° = 3°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A ray enters a 60° prism at i1 = 50° and refracts at r1 = 30°. If it emerges at i2 = 40°, the deviation δ is:',
      options: ['30°', '60°', '20°', '90°'],
      correctIndex: 0,
      solution: 'r2 = A − r1 = 60° − 30° = 30°. δ = (i1 + i2) − A = (50 + 40) − 60 = 30°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Angular dispersion produced by a prism refers to:',
      options: [
        'The deviation of a single colour from its original path',
        'The angle between the emergent rays of two different colours (e.g. violet and red)',
        'The prism\'s apex angle',
        'The angle of minimum deviation for yellow light',
      ],
      correctIndex: 1,
      solution: 'Angular dispersion = δ_violet − δ_red, the SPREAD between colours — a distinct quantity from the deviation of any one colour.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A rainbow forms in the sky due to which sequence of processes inside raindrops?',
      options: [
        'Only refraction, no reflection',
        'Refraction, then total internal reflection off the back of the drop, then refraction again on exit',
        'Only diffraction of sunlight',
        'Polarization of sunlight by the water surface',
      ],
      correctIndex: 1,
      solution: 'Sunlight refracts entering the raindrop (dispersing into colours), reflects internally once off the back surface, then refracts again exiting — sending separated colours to the observer\'s eye at slightly different angles.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'If the angle of incidence in a prism experiment is gradually increased from a small value, the angle of deviation δ generally:',
      options: [
        'Increases continuously throughout',
        'Decreases continuously throughout',
        'First decreases to a minimum value, then increases',
        'Remains constant',
      ],
      correctIndex: 2,
      solution: 'δ vs i1 is a U-shaped curve: it falls to a single minimum (δm, at the symmetric ray path) and then rises again as i1 increases further.',
    ),
  ],
  revision: [
    'Two refractions per prism: r1 + r2 = A (geometry); δ = (i1 + i2) − A (deviation).',
    'At minimum deviation: i1 = i2, r1 = r2 = A/2, and n = sin((A+δm)/2)/sin(A/2).',
    'Thin-prism approximation: δ ≈ (n − 1)A for small A and small i1.',
    'Refractive index depends on wavelength (dispersion): n_violet > n_red, so violet bends most, red least.',
    'Angular dispersion (spread between colours) is a DIFFERENT quantity from the deviation of one colour.',
    'Rainbow = refraction + total internal reflection + refraction again, inside raindrops.',
    'Total internal reflection can occur at the second face of a prism if r2 exceeds the critical angle — no ray emerges.',
  ],
  sandboxBuilder: (_) => const PrismDispersionSandbox(),
);
