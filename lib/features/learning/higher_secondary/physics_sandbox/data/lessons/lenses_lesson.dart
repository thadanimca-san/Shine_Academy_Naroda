import '../../models/lesson.dart';
import '../../simulators/lenses_sandbox.dart';
import '../../theme/tokens.dart';

/// Lenses — the thin lens formula, sign convention, and image nature.
final Lesson lensesLesson = Lesson(
  topicId: 'lenses',
  title: 'Lenses',
  accentColor: Palette.chOptics,
  bigQuestion:
      'A magnifying glass held close to a coin makes it look bigger — but hold that exact same glass at arm\'s length and project the coin\'s image onto a wall, and it comes out upside down and shrunk. Same lens, same coin — so what single number decides whether a lens magnifies or flips your image?',
  whyItMatters:
      'Lenses are the single most exam-dense topic in optics: the thin lens formula, magnification, lens maker\'s formula, and power all recur constantly in NEET and JEE, both as direct numericals and buried inside optical-instrument problems (microscopes, telescopes, the human eye). Nail the sign convention here and every later topic — prism, dispersion, instruments — becomes far easier, since they all reuse this same bookkeeping.',
  prediction: const PredictionPrompt(
    scenario:
        'An object sits well within the focal length of a converging (convex) lens — closer to the lens than F. As you slowly drag it farther away, past F, what happens to the image?',
    options: [
      'It stays virtual and upright the whole time',
      'It switches from virtual+upright+magnified to real+inverted once the object passes F',
      'It disappears completely once past the focal point',
      'It becomes virtual and inverted',
    ],
    correctIndex: 1,
    reveal:
        'Inside the focal length, a converging lens acts as a simple magnifying glass — virtual, upright, magnified image on the SAME side as the object. Once the object crosses F, the image flips to real and inverted, forming on the far side of the lens. In the lab, drag the object distance slider from small values (inside F) to large values (beyond F) and watch the image arrow flip from upright-and-purple (virtual) to inverted-and-blue (real).',
  ),
  experiments: [
    'Place the object inside the focal length of a converging lens and observe a virtual, magnified, upright image on the same side',
    'Move the object beyond the focal length and watch the image become real and inverted on the far side',
    'Compare a diverging lens at any object distance — the image stays virtual, upright, and diminished',
    'Drag the object to exactly 2F and confirm the image forms at 2F too, same size, inverted',
    'Watch the image distance readout follow 1/v − 1/u = 1/f as you change object distance',
    'Shrink the focal length while keeping the object distance fixed and see the image swing rapidly closer to the lens',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A lens is a transparent medium bounded by two curved (usually spherical) surfaces that refracts light twice — once entering, once leaving — to converge or diverge a beam. A converging (convex) lens is thicker at the middle and bends parallel rays inward to a real focus; a diverging (concave) lens is thinner at the middle and spreads parallel rays outward, so they only APPEAR to come from a virtual focus.',
      title: 'What a lens does',
    ),
    ContentBlock.bullets([
      'Cartesian sign convention: all distances measured from the optical centre of the lens',
      'Distances measured in the direction of incident light (usually left to right) are POSITIVE; against it are NEGATIVE',
      'Heights measured upward (above principal axis) are POSITIVE; downward are NEGATIVE',
      'For a converging lens, f is POSITIVE; for a diverging lens, f is NEGATIVE',
    ], title: 'Sign convention — get this right first'),
    ContentBlock.formula('1/v − 1/u = 1/f', title: 'THE THIN LENS FORMULA'),
    ContentBlock.paragraph(
      'u = object distance, v = image distance, f = focal length, all measured from the lens\'s optical centre using the sign convention above. Note the MINUS sign between 1/v and 1/u — this is the single biggest difference from the mirror formula (which uses a plus). The formula works for BOTH converging and diverging lenses, and for real or virtual images, as long as signs are applied consistently.',
      title: 'One formula, both lens types',
    ),
    ContentBlock.formula('m = v/u = h_image/h_object', title: 'MAGNIFICATION'),
    ContentBlock.bullets([
      'Positive m: image is upright (erect) relative to the object',
      'Negative m: image is inverted',
      '|m| > 1: image is magnified (larger than object); |m| < 1: image is diminished',
    ]),
    ContentBlock.bullets([
      'Object beyond 2F: real, inverted, diminished, between F and 2F on the far side',
      'Object at 2F: real, inverted, same size, at 2F on the far side',
      'Object between F and 2F: real, inverted, magnified, beyond 2F on the far side',
      'Object at F: image at infinity',
      'Object between F and the lens: virtual, upright, magnified, same side as the object',
    ], title: 'Converging lens image nature (by object position)'),
    ContentBlock.paragraph(
      'A diverging lens ALWAYS produces a virtual, upright, diminished image no matter where the object sits — the rays entering it spread out further, so they can never actually converge to a real image on the far side. This is why a diverging lens by itself is never used as a magnifier or a projector lens; it is used to CORRECT vision (myopia) or to spread a beam.',
      title: 'Why diverging lenses are always predictable',
    ),
    ContentBlock.formula('1/f = (n − 1)(1/R₁ − 1/R₂)', title: 'LENS MAKER\'S FORMULA'),
    ContentBlock.paragraph(
      'The lens maker\'s formula connects a lens\'s focal length to the physical geometry that produced it: n is the refractive index of the lens material relative to the surrounding medium, and R₁, R₂ are the (signed) radii of curvature of the first and second surfaces the light meets. It shows WHY a more curved lens (smaller R) or a higher-n glass gives a shorter, more powerful focal length — this is the formula opticians effectively use when grinding a lens to a prescription.',
      title: 'Where focal length comes from',
    ),
    ContentBlock.formula('P = 1/f  (f in metres, P in dioptres D)', title: 'POWER OF A LENS'),
    ContentBlock.paragraph(
      'Power measures how strongly a lens converges or diverges light — the shorter the focal length, the more powerful the lens. A converging lens has positive power, a diverging lens negative power, and the unit is the dioptre (D), used directly on spectacle prescriptions (e.g. "+2.5 D" or "−1.5 D"). When several thin lenses are held in contact, their powers simply ADD: P_net = P₁ + P₂ + …, which is why combining lenses is done in terms of power rather than focal length.',
      title: 'Power and combinations',
    ),
    ContentBlock.realLife(
      'Spectacles use converging lenses (positive power) to correct hypermetropia (far-sightedness) and diverging lenses (negative power) to correct myopia (near-sightedness); prescriptions are written directly in dioptres. Cameras, projectors, and the human eye\'s own lens all use converging lenses to form real images on a sensor, screen, or retina.',
    ),
    ContentBlock.mistake(
      'Using the mirror formula\'s plus sign (1/v + 1/u = 1/f) for a lens by mistake. The LENS formula has a MINUS: 1/v − 1/u = 1/f. Mixing the two up is the single most common lens-chapter error — always double check which formula you\'re using before substituting.',
    ),
    ContentBlock.mistake(
      'Assuming a converging lens always magnifies. It only magnifies when the object is WITHIN the focal length (virtual image, like a magnifying glass) or between F and 2F (real, magnified). For an object beyond 2F, the image is actually SMALLER than the object, not bigger.',
    ),
    ContentBlock.example(
      'An object is placed 30 cm in front of a converging lens of focal length 10 cm. Find the image position and magnification.\n\nSign convention: u = −30 cm, f = +10 cm.\n1/v = 1/f + 1/u = 1/10 + 1/(−30) = 3/30 − 1/30 = 2/30 = 1/15.\nv = +15 cm (positive → real image, 15 cm on the far side of the lens).\nm = v/u = 15/(−30) = −0.5 (inverted, diminished to half size).',
    ),
    ContentBlock.jeeTip(
      'For quick ray-diagram sketching, remember the three standard rays from an off-axis point: (1) a ray parallel to the principal axis refracts through the far focus F (converging) or appears to come from the near focus F (diverging); (2) a ray through the optical centre goes straight through, undeviated; (3) a ray through the near focus (converging) or aimed at the far focus (diverging) emerges parallel to the axis. Any two of these three rays are enough to locate the image.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the exact object position range for a converging lens to produce a specific image type: object beyond 2F gives a diminished real image, object between F and 2F gives a magnified real image, object at 2F gives a same-size real image, object between F and the lens gives a magnified VIRTUAL image. Memorising this progression (mirroring the concave-mirror table, but with 2F in place of C) is high-value.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up refraction at the first surface of the lens',
      math: 'n₁/(−u) + n₂/v₁ = (n₂ − n₁)/R₁',
      note: 'Using the single-spherical-surface refraction formula on surface 1, image at v₁ (virtual object for the next surface).',
    ),
    DerivationStep(
      title: 'Apply the same formula at the second surface',
      math: 'n₂/(−v₁) + n₁/v = (n₁ − n₂)/R₂',
      note: 'The image from surface 1 acts as the object for surface 2; the lens is assumed thin so both surfaces share the same optical centre.',
    ),
    DerivationStep(
      title: 'Add the two surface equations',
      math: 'n₁/v − n₁/u = (n₂ − n₁)(1/R₁ − 1/R₂)',
      note: 'The intermediate v₁ terms cancel, leaving a single relation between object distance u and final image distance v.',
    ),
    DerivationStep(
      title: 'Divide through by n₁ and define n = n₂/n₁',
      math: '1/v − 1/u = (n − 1)(1/R₁ − 1/R₂)',
    ),
    DerivationStep(
      title: 'Identify the right-hand side as 1/f (lens maker\'s formula)',
      math: '1/f = (n − 1)(1/R₁ − 1/R₂)   →   1/v − 1/u = 1/f',
      note: 'This is the thin lens formula — the same 1/f appears no matter where the object is, since f depends only on the lens\'s shape and material.',
    ),
  ],
  formulas: const [
    FormulaEntry('Thin lens formula', '1/v − 1/u = 1/f'),
    FormulaEntry('Magnification', 'm = v/u = h_i/h_o'),
    FormulaEntry('Lens maker\'s formula', '1/f = (n − 1)(1/R₁ − 1/R₂)'),
    FormulaEntry('Power of a lens', 'P = 1/f', condition: 'f in metres, P in dioptres (D)'),
    FormulaEntry('Combined power (lenses in contact)', 'P_net = P₁ + P₂ + …'),
    FormulaEntry('Converging lens focal length', 'f > 0', condition: 'Cartesian convention'),
    FormulaEntry('Diverging lens focal length', 'f < 0', condition: 'Cartesian convention'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A diverging lens always forms an image that is:',
      options: ['Real and inverted', 'Virtual, upright, and diminished', 'Real and magnified', 'Virtual and inverted'],
      correctIndex: 1,
      solution: 'Regardless of object position, a diverging lens always produces a virtual, upright, diminished image.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In the Cartesian sign convention, the focal length of a converging lens is taken as:',
      options: ['Positive', 'Negative', 'Zero', 'Either, depending on the object'],
      correctIndex: 0,
      solution: 'A converging lens brings parallel rays to a real focus on the far side, so by convention f is positive.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An object is placed at 2F of a converging lens. The image formed is:',
      options: [
        'Virtual, upright, magnified',
        'Real, inverted, same size, at 2F on the far side',
        'Real, inverted, diminished',
        'At infinity',
      ],
      correctIndex: 1,
      solution: 'At u = −2f, the lens formula gives v = +2f as well — image forms at 2F on the far side, same size, real and inverted.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A converging lens has focal length 15 cm. An object is placed 10 cm from the lens (within F). The image is:',
      options: ['Real and diminished', 'Virtual and magnified', 'Real and same size', 'Virtual and diminished'],
      correctIndex: 1,
      solution: 'An object within the focal length of a converging lens always gives a virtual, upright, magnified image — the magnifying-glass case.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'An object is placed 20 cm from a converging lens of focal length 10 cm. Find the image distance.',
      options: ['20 cm', '−20 cm', '10 cm', '6.7 cm'],
      correctIndex: 0,
      solution:
          'u = −20, f = +10. 1/v = 1/f + 1/u = 1/10 + (−1/20) = 1/20. v = +20 cm (real image, on the far side, at 2f since the object was at 2f).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'For the previous problem (object at 20 cm, f = 10 cm converging lens), the magnification is:',
      options: ['−1', '+1', '−2', '+0.5'],
      correctIndex: 0,
      solution: 'm = v/u = 20/(−20) = −1. Same size, inverted — consistent with the object being exactly at 2F.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'An object is placed 5 cm from a converging lens of focal length 15 cm. The image distance and nature are:',
      options: [
        'v = −7.5 cm, virtual, magnified',
        'v = +7.5 cm, real, magnified',
        'v = −7.5 cm, virtual, diminished',
        'v = +15 cm, real, same size',
      ],
      correctIndex: 0,
      solution:
          'u = −5, f = +15. 1/v = 1/f + 1/u = 1/15 + (−1/5) = 1/15 − 3/15 = −2/15. v = −7.5 cm (negative → virtual, same side as object). m = v/u = −7.5/(−5) = 1.5 (magnified, upright).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A diverging lens of focal length 20 cm has an object placed 30 cm in front of it. The image distance is:',
      options: ['−12 cm', '+12 cm', '−50 cm', '+50 cm'],
      correctIndex: 0,
      solution:
          'u = −30, f = −20 (diverging). 1/v = 1/f + 1/u = −1/20 + (−1/30) = −3/60 − 2/60 = −5/60 = −1/12. v = −12 cm (virtual, same side as the object, as expected for a diverging lens).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Two thin converging lenses of power +2 D and +3 D are placed in contact. The combined power and focal length are:',
      options: ['+5 D, 20 cm', '+1 D, 100 cm', '+6 D, 16.7 cm', '+5 D, 50 cm'],
      correctIndex: 0,
      solution: 'P_net = P₁ + P₂ = 2 + 3 = 5 D. f = 1/P = 1/5 m = 0.20 m = 20 cm.',
    ),
  ],
  revision: [
    '1/v − 1/u = 1/f — the MINUS sign distinguishes the lens formula from the mirror formula (which has a plus).',
    'Cartesian convention: converging lens has f > 0, diverging lens has f < 0.',
    'Magnification m = v/u: negative means inverted, positive means upright; |m| > 1 means magnified.',
    'Diverging lens: always virtual, upright, diminished, regardless of object position.',
    'Converging lens: image nature depends on object position relative to F and 2F.',
    'Object within F on a converging lens → virtual, upright, magnified (magnifying-glass case).',
    'Lens maker\'s formula: 1/f = (n − 1)(1/R₁ − 1/R₂); power P = 1/f (dioptres, f in metres).',
    'Lenses in contact: powers add, P_net = P₁ + P₂ + …',
  ],
  sandboxBuilder: (_) => const LensesSandbox(),
);
