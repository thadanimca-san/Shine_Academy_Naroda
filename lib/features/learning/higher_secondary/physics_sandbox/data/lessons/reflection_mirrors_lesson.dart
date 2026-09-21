import '../../models/lesson.dart';
import '../../simulators/reflection_mirrors_sandbox.dart';
import '../../theme/tokens.dart';

/// Reflection & Mirrors — the mirror formula, sign convention, and image nature.
final Lesson reflectionMirrorsLesson = Lesson(
  topicId: 'reflection-mirrors',
  title: 'Reflection & Mirrors',
  accentColor: Palette.chOptics,
  bigQuestion:
      'Stand close to a concave (shaving/makeup) mirror and you see a magnified, upright image of your face. Back away far enough and suddenly the image flips upside down. What is it about your DISTANCE from the mirror that flips the image the way it does?',
  whyItMatters:
      'Mirror optics is built almost entirely on ONE formula (1/v + 1/u = 1/f) and a consistent sign convention — get the sign convention solid and the entire chapter becomes mechanical algebra. NEET and JEE test ray diagrams, image nature (real/virtual, magnified/diminished, erect/inverted) and numerical mirror-formula problems constantly, making this one of the highest-yield topics to master completely.',
  prediction: const PredictionPrompt(
    scenario:
        'An object is placed very close to a concave mirror, well within its focal length. As you slowly move the object farther away, past the focal point, what happens to the image?',
    options: [
      'It stays virtual and upright the whole time',
      'It switches from virtual+upright+magnified to real+inverted at some point',
      'It disappears completely once past the focal point',
      'It becomes virtual and inverted',
    ],
    correctIndex: 1,
    reveal:
        'Inside the focal length, a concave mirror produces a virtual, upright, magnified image (like a shaving mirror); once the object passes the focal point, the image becomes real and inverted. In the lab, drag the object from very close to the mirror out past the focal point and watch the image flip from upright-and-behind-the-mirror to inverted-and-in-front-of-the-mirror.',
  ),
  experiments: [
    'Place the object inside the focal length of a concave mirror and observe a virtual, magnified, upright image',
    'Move the object beyond the focal length and watch the image become real and inverted',
    'Compare a convex mirror at any object distance — the image stays virtual, upright, and diminished',
    'Drag the object to exactly 2f and confirm the image forms at 2f too, same size, inverted',
    'Watch the image distance readout follow 1/v + 1/u = 1/f as you change object distance',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The laws of reflection state that the angle of incidence equals the angle of reflection, and both the incident ray, reflected ray, and the normal at the point of incidence all lie in the same plane. These simple rules, applied point by point along a curved mirror surface, are what let curved mirrors form images — real ones that light rays actually pass through, or virtual ones that only appear to originate from a point.',
      title: 'The laws of reflection',
    ),
    ContentBlock.bullets([
      'New Cartesian sign convention: all distances measured from the pole (centre of the mirror surface)',
      'Distances measured in the direction of incident light are POSITIVE; against it are NEGATIVE',
      'Heights measured upward (above principal axis) are POSITIVE; downward are NEGATIVE',
      'For a concave mirror, focal length f is NEGATIVE; for a convex mirror, f is POSITIVE',
    ], title: 'Sign convention — get this right first'),
    ContentBlock.formula('1/v + 1/u = 1/f', title: 'THE MIRROR FORMULA'),
    ContentBlock.paragraph(
      'u = object distance, v = image distance, f = focal length, all measured from the mirror\'s pole using the sign convention above. This single formula works for BOTH concave and convex mirrors, and for real and virtual images and objects, as long as you consistently apply the correct signs. Solving for v when u and f are known instantly tells you where the image forms — and its sign tells you whether it\'s real (negative, same side as the object) or virtual (positive, "behind" the mirror).',
      title: 'One formula, both mirror types',
    ),
    ContentBlock.formula('m = −v/u = h_image/h_object', title: 'MAGNIFICATION'),
    ContentBlock.bullets([
      'Positive m: image is upright (erect) relative to the object',
      'Negative m: image is inverted',
      '|m| > 1: image is magnified (larger than object); |m| < 1: image is diminished',
    ]),
    ContentBlock.bullets([
      'Object beyond C (centre of curvature): real, inverted, diminished, between F and C',
      'Object at C: real, inverted, same size, at C',
      'Object between C and F: real, inverted, magnified, beyond C',
      'Object at F: image at infinity',
      'Object between F and pole: virtual, upright, magnified, "behind" the mirror',
    ], title: 'Concave mirror image nature (by object position)'),
    ContentBlock.paragraph(
      'A convex mirror ALWAYS produces a virtual, upright, diminished image, regardless of where the object is placed — this makes it ideal for vehicle side mirrors and shop security mirrors, since it gives a wide field of view (though objects appear smaller and closer than they really are, hence the "objects in mirror are closer than they appear" warning). A concave mirror\'s behaviour, by contrast, depends critically on where the object sits relative to F and C.',
      title: 'Why convex mirrors are always predictable',
    ),
    ContentBlock.realLife(
      'Concave mirrors are used in shaving/makeup mirrors (object inside F gives a magnified upright image) and in torches/headlights (object AT the focus sends out a perfectly parallel beam, per the reverse of the ray diagram); convex mirrors are used in vehicle side mirrors and shop anti-theft mirrors for their wide field of view, always giving upright though diminished images.',
    ),
    ContentBlock.mistake(
      'Mixing up the sign convention between concave (f negative) and convex (f positive) mirrors, or forgetting that REAL images have negative v (formed on the same side as the incoming light) while VIRTUAL images have positive v. Get the sign of f wrong at the START and every subsequent calculation in the problem goes wrong.',
    ),
    ContentBlock.mistake(
      'Assuming a concave mirror always magnifies. It only magnifies when the object is WITHIN the focal length (or between F and C for slight magnification) — for objects beyond C, the image is actually SMALLER (diminished) than the object, not bigger.',
    ),
    ContentBlock.example(
      'An object is placed 30 cm in front of a concave mirror of focal length 10 cm. Find the image position and magnification.\n\nSign convention: u = −30 cm, f = −10 cm.\n1/v + 1/u = 1/f → 1/v = 1/f − 1/u = 1/(−10) − 1/(−30) = −1/10 + 1/30 = −3/30 + 1/30 = −2/30 = −1/15.\nv = −15 cm (negative → real image, 15 cm in front of the mirror).\nm = −v/u = −(−15)/(−30) = −15/30 = −0.5 (inverted, diminished to half size).',
    ),
    ContentBlock.jeeTip(
      'For quick ray-diagram sketching, remember the three standard rays from an off-axis point: (1) a ray parallel to the principal axis reflects through F; (2) a ray through F reflects parallel to the axis; (3) a ray through C (or toward C) reflects straight back along itself, since it hits the mirror perpendicular to the surface. Any two of these three rays are enough to locate the image.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the exact object position range for a concave mirror to produce a specific image type: object beyond C gives diminished real image, object between C and F gives magnified real image, object at C gives same-size real image, object between F and pole gives magnified VIRTUAL image. Memorising this progression (with C = 2f) is high-value.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the geometry for a concave mirror',
      math: 'Object at distance u, mirror focal length f, image forms at distance v',
      note: 'Using the New Cartesian sign convention, with the pole as origin.',
    ),
    DerivationStep(
      title: 'Consider two rays from an off-axis object point',
      math: 'Ray 1: parallel to axis, reflects through F. Ray 2: through F, reflects parallel to axis.',
    ),
    DerivationStep(
      title: 'Use similar triangles formed by these rays and the axis',
      math: 'From the geometry of similar triangles at the mirror and at F: relates u, v, and f',
      note: 'Small-angle (paraxial) approximation is used, valid for rays close to the principal axis.',
    ),
    DerivationStep(
      title: 'Combine the two similar-triangle relations algebraically',
      math: '1/v + 1/u = 1/f',
      note: 'The mirror formula — valid for both concave and convex mirrors under the sign convention.',
    ),
    DerivationStep(
      title: 'Derive magnification from the same similar triangles',
      math: 'm = h_image/h_object = −v/u',
      note: 'The negative sign correctly predicts inversion for real images and upright orientation for virtual images.',
    ),
  ],
  formulas: const [
    FormulaEntry('Mirror formula', '1/v + 1/u = 1/f'),
    FormulaEntry('Magnification', 'm = −v/u = h_i/h_o'),
    FormulaEntry('Radius of curvature', 'R = 2f'),
    FormulaEntry('Concave mirror focal length', 'f < 0', condition: 'New Cartesian convention'),
    FormulaEntry('Convex mirror focal length', 'f > 0', condition: 'New Cartesian convention'),
    FormulaEntry('Real image', 'v < 0', condition: 'formed on same side as object'),
    FormulaEntry('Virtual image', 'v > 0', condition: 'formed "behind" the mirror'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A convex mirror always forms an image that is:',
      options: ['Real and inverted', 'Virtual, upright, and diminished', 'Real and magnified', 'Virtual and inverted'],
      correctIndex: 1,
      solution: 'Regardless of object position, a convex mirror always produces a virtual, upright, diminished image.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In the New Cartesian sign convention, the focal length of a concave mirror is taken as:',
      options: ['Positive', 'Negative', 'Zero', 'Either, depending on the object'],
      correctIndex: 1,
      solution: 'Concave mirrors have their focus on the same side as incoming light, so by convention f is negative.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An object is placed at the centre of curvature C of a concave mirror. The image formed is:',
      options: [
        'Virtual, upright, magnified',
        'Real, inverted, same size, at C',
        'Real, inverted, diminished',
        'At infinity',
      ],
      correctIndex: 1,
      solution: 'At C (u = 2f), the mirror formula gives v = 2f as well — image forms at C, same size, real and inverted.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A concave mirror has focal length 15 cm. An object is placed 10 cm from the mirror (within F). The image is:',
      options: ['Real and diminished', 'Virtual and magnified', 'Real and same size', 'Virtual and diminished'],
      correctIndex: 1,
      solution: 'Object within focal length of a concave mirror always gives a virtual, upright, magnified image — the shaving-mirror case.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'An object is placed 20 cm from a concave mirror of focal length 10 cm. Find the image distance.',
      options: ['−20 cm', '−10 cm', '20 cm', '−6.7 cm'],
      correctIndex: 0,
      solution:
          'u = −20, f = −10. 1/v = 1/f − 1/u = −1/10 − (−1/20) = −1/10 + 1/20 = −1/20. v = −20 cm (real image, at C, since object was at C too).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'For the previous problem (object at 20 cm, f = 10 cm concave mirror), the magnification is:',
      options: ['−1', '+1', '−2', '+0.5'],
      correctIndex: 0,
      solution: 'm = −v/u = −(−20)/(−20) = −1. Same size, inverted — consistent with the object being exactly at C.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'An object is placed 5 cm from a concave mirror of focal length 15 cm. The image distance and nature are:',
      options: [
        'v = +7.5 cm, virtual, magnified',
        'v = −7.5 cm, real, magnified',
        'v = +7.5 cm, virtual, diminished',
        'v = −15 cm, real, same size',
      ],
      correctIndex: 0,
      solution:
          'u = −5, f = −15. 1/v = 1/f − 1/u = −1/15 − (−1/5) = −1/15 + 3/15 = 2/15. v = 7.5 cm (positive → virtual). m = −v/u = −7.5/(−5) = 1.5 (magnified, upright).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A convex mirror of focal length 20 cm has an object placed 30 cm in front of it. The image distance is:',
      options: ['+12 cm', '−12 cm', '+50 cm', '−50 cm'],
      correctIndex: 0,
      solution:
          'u = −30, f = +20 (convex). 1/v = 1/f − 1/u = 1/20 − (−1/30) = 1/20 + 1/30 = 3/60+2/60 = 5/60 = 1/12. v = +12 cm (virtual, behind the mirror, as expected for convex).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'As an object approaches a concave mirror from far away toward the focal point, the real image formed:',
      options: [
        'Moves from near F toward the mirror, shrinking',
        'Moves from near F away toward infinity, growing larger',
        'Stays fixed at C',
        'Immediately becomes virtual',
      ],
      correctIndex: 1,
      solution: 'As u decreases from infinity toward f (object approaching focal point from beyond C), the real image moves outward from near F toward infinity, growing progressively larger, until it vanishes (image at infinity) exactly when u = f.',
    ),
  ],
  revision: [
    'Laws of reflection: angle of incidence = angle of reflection; incident ray, reflected ray, normal are coplanar.',
    'New Cartesian convention: distances along incident light are positive; concave f is negative, convex f is positive.',
    'Mirror formula: 1/v + 1/u = 1/f — works for both mirror types with correct signs.',
    'Magnification m = −v/u: negative means inverted, positive means upright; |m|>1 means magnified.',
    'Convex mirror: always virtual, upright, diminished, regardless of object position.',
    'Concave mirror: image nature depends on object position relative to F and C (=2f).',
    'Object within F on a concave mirror → virtual, upright, magnified (shaving mirror case).',
  ],
  sandboxBuilder: (_) => const ReflectionMirrorsSandbox(),
);
