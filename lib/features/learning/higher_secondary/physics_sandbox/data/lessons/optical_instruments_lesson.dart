import '../../models/lesson.dart';
import '../../simulators/optical_instruments_sandbox.dart';
import '../../theme/tokens.dart';

/// Optical Instruments — magnifiers, microscopes, telescopes, and the eye.
final Lesson opticalInstrumentsLesson = Lesson(
  topicId: 'optical-instruments',
  title: 'Optical Instruments',
  accentColor: Palette.chOptics,
  bigQuestion:
      'A giant observatory telescope and a simple magnifying glass are both "just a lens" — yet one lets you read tiny print an inch from your eye, and the other reveals galaxies billions of light-years away. What is the ONE design choice that separates a microscope from a telescope, when both are built from the exact same kind of converging lenses?',
  whyItMatters:
      'Optical instruments are where every earlier optics topic (lens formula, magnification, focal length) gets applied to real devices — and NEET/JEE test them directly and often. The core idea (a short-focus objective vs. a long-focus objective, paired with an eyepiece acting as a simple magnifier) recurs in microscopes, telescopes, and even the human eye, making this a highly rewarding, formula-light, concept-heavy topic to master.',
  prediction: const PredictionPrompt(
    scenario:
        'An astronomical telescope is built from two converging lenses: an objective and an eyepiece. To get the HIGHEST magnifying power from a telescope, you should choose:',
    options: [
      'A short focal length objective and a long focal length eyepiece',
      'A long focal length objective and a short focal length eyepiece',
      'Both lenses with equal focal lengths',
      'The focal lengths of the two lenses do not affect magnification',
    ],
    correctIndex: 1,
    reveal:
        'Telescope magnifying power is M = fo/fe — objective focal length divided by eyepiece focal length. To maximise M you want fo as LARGE as possible and fe as SMALL as possible; this is exactly opposite to a microscope, which wants both focal lengths short. In the lab, drag fo up and fe down and watch the magnifying-power readout climb.',
  ),
  experiments: [
    'In telescope mode, increase the objective focal length fo and watch M = fo/fe climb',
    'Decrease the eyepiece focal length fe and watch M climb even faster (small fe matters a lot)',
    'Note the tube length is always fo + fe for a telescope focused for a relaxed (distant) eye',
    'Switch to simple microscope mode and compare M for "relaxed eye" (D/fe) vs "image at near point" (1 + D/fe)',
    'Shrink the magnifier\'s focal length fe and see the magnifying power rise steeply — short-focus lenses magnify more',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A simple microscope is just a single converging lens (a magnifying glass) used to view a small nearby object. Placing the object within the lens\'s focal length produces a virtual, upright, magnified image — the lens lets your eye focus on an object closer than it normally could, so the object subtends a larger angle at your eye than it would unaided.',
      title: 'The simple microscope: one lens, angular magnification',
    ),
    ContentBlock.formula('M = D/f  (relaxed eye, image at infinity)', title: 'SIMPLE MICROSCOPE — RELAXED EYE'),
    ContentBlock.formula('M = 1 + D/f  (image at the near point)', title: 'SIMPLE MICROSCOPE — STRAINED EYE'),
    ContentBlock.paragraph(
      'D = 25 cm is the standard near point distance — the closest an average unaided eye can comfortably focus. Angular magnification compares the angle subtended by the IMAGE (through the lens) to the angle subtended by the object if placed at the near point without any lens. Forming the image at infinity (object exactly at the focus) lets the eye relax; forming it at the near point instead squeezes out slightly more magnification (the "+1") but strains the eye.',
      title: 'Why D = 25 cm matters',
    ),
    ContentBlock.paragraph(
      'A compound microscope stacks two converging lenses: a short-focal-length OBJECTIVE placed very close to a tiny object forms a real, inverted, HIGHLY magnified image just inside the focal length of a second lens, the EYEPIECE — which then acts as a simple magnifier on that already-magnified real image, magnifying it again. The two magnifications multiply, giving compound microscopes far higher power than any single lens could achieve alone.',
      title: 'The compound microscope: magnify twice',
    ),
    ContentBlock.formula('M ≈ (L/fo) × (D/fe)', title: 'COMPOUND MICROSCOPE (APPROXIMATE, RELAXED EYE)'),
    ContentBlock.paragraph(
      'L is the tube length (distance between the objective\'s image and the eyepiece), fo and fe are the objective and eyepiece focal lengths. Both fo and fe are made as SHORT as possible to maximise magnification — completely different from a telescope\'s needs.',
      title: 'Compound microscope: short focal lengths win',
    ),
    ContentBlock.formula('M = fo/fe', title: 'ASTRONOMICAL TELESCOPE (RELAXED EYE)'),
    ContentBlock.paragraph(
      'An astronomical telescope also uses two converging lenses, but the object (a star or planet) is essentially at infinity, so the objective forms a real image at its own focus fo. The eyepiece is then positioned so that this real image sits at ITS focus fe too — so the two focal points coincide, giving a tube length of fo + fe for a relaxed eye. Magnifying power is simply M = fo/fe: to magnify distant objects strongly, you want a LARGE objective focal length and a SHORT eyepiece focal length — again, the opposite of a microscope.',
      title: 'The astronomical telescope: large fo, small fe',
    ),
    ContentBlock.bullets([
      'A large objective APERTURE (diameter, not just focal length) gathers more light, letting the telescope resolve fainter, dimmer objects — this is why research telescopes have huge mirrors/lenses',
      'A large objective focal length gives high magnification when paired with a short eyepiece',
      'Resolving power (ability to distinguish two close objects) is fundamentally limited by diffraction at the objective aperture, not just by magnification',
    ], title: 'Why telescopes want a big objective'),
    ContentBlock.paragraph(
      'The human eye is itself a remarkable optical instrument: the cornea and the eye\'s internal (crystalline) lens together form a real, inverted image on the retina, which the brain interprets right-side up. The lens changes shape (accommodation) via the ciliary muscles to focus on objects at different distances, ranging from the near point (~25 cm) to the far point (infinity, for a normal eye).',
      title: 'The eye as an optical instrument',
    ),
    ContentBlock.bullets([
      'Myopia (near-sightedness): image forms IN FRONT of the retina (eyeball too long, or lens too strong); corrected with a DIVERGING lens',
      'Hypermetropia (far-sightedness): image forms BEHIND the retina (eyeball too short, or lens too weak); corrected with a CONVERGING lens',
      'Presbyopia: age-related loss of accommodation ability (ciliary muscles weaken); corrected with bifocal lenses',
    ], title: 'Common eye defects — high-yield NEET facts'),
    ContentBlock.realLife(
      'Binoculars are essentially a pair of side-by-side telescopes with internal prisms that fold the light path (making them compact) while also flipping the image right-side up, since a simple astronomical telescope alone produces an inverted image. Cameras use a single converging lens system to focus a real image onto film or a digital sensor, mimicking the eye.',
    ),
    ContentBlock.mistake(
      'Mixing up microscope and telescope design rules. A compound microscope wants BOTH focal lengths SHORT (to magnify a tiny nearby object strongly); a telescope wants a LARGE objective focal length and a SHORT eyepiece focal length (to magnify a distant object). Applying the wrong rule is a very common mix-up under exam pressure.',
    ),
    ContentBlock.mistake(
      'Confusing magnifying power with light-gathering power. A telescope\'s magnification depends on fo/fe, but its ability to see FAINT, dim objects depends on the objective\'s APERTURE (diameter), which is an entirely separate design parameter. A telescope can have high magnification but still show a dim, hard-to-see image if its objective is small.',
    ),
    ContentBlock.example(
      'A simple magnifier has focal length 5 cm. Find its magnifying power for (a) relaxed eye, (b) image at the near point (D = 25 cm).\n\n(a) M = D/f = 25/5 = 5×.\n(b) M = 1 + D/f = 1 + 25/5 = 1 + 5 = 6×.\n\nForming the image at the near point gives one extra unit of magnification, at the cost of eye strain.',
    ),
    ContentBlock.jeeTip(
      'For a compound microscope or telescope with the FINAL image at the near point (not at infinity), an extra (1 + fe/D) factor multiplies the eyepiece\'s simple-magnifier formula — this variant appears in JEE numericals asking for "maximum" magnification. Always check whether the question specifies relaxed eye (image at infinity) or image at the near point before choosing the formula.',
    ),
    ContentBlock.neetNote(
      'NEET loves direct eye-defect questions: myopia → diverging (concave) lens; hypermetropia → converging (convex) lens; presbyopia → bifocal lenses combining both. Also remember: the eye\'s near point for a young, normal eye is 25 cm and its far point is infinity — myopia shrinks the far point, hypermetropia pushes the near point beyond 25 cm.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define angular magnification for a simple microscope',
      math: 'M = (angle subtended by image through the lens) / (angle subtended by object at near point D, unaided)',
    ),
    DerivationStep(
      title: 'Relaxed eye: place the object at the lens\'s focus',
      math: 'Object at f → image forms at infinity, viewed with a fully relaxed eye. Angle through lens ≈ h/f; unaided angle at near point ≈ h/D.',
    ),
    DerivationStep(
      title: 'Take the ratio',
      math: 'M = (h/f) / (h/D) = D/f',
      note: 'This is the simple microscope formula for a relaxed eye.',
    ),
    DerivationStep(
      title: 'Image at the near point instead: use the lens formula for magnification',
      math: 'For u such that v = −D (virtual image at near point): 1/v − 1/u = 1/f gives M = 1 + D/f',
      note: 'Slightly larger than D/f, at the cost of the eye having to focus at its near point rather than relax.',
    ),
    DerivationStep(
      title: 'Extend to the astronomical telescope',
      math: 'Distant object → objective forms real image at its focus fo. Eyepiece, acting as a simple magnifier on this image (now effectively "the object" for the eyepiece) at its own focus fe, gives M = fo/fe.',
      note: 'Tube length for relaxed eye = fo + fe, since both focal points coincide at the intermediate image.',
    ),
  ],
  formulas: const [
    FormulaEntry('Simple microscope, relaxed eye', 'M = D/f'),
    FormulaEntry('Simple microscope, image at near point', 'M = 1 + D/f'),
    FormulaEntry('Near point convention', 'D = 25 cm'),
    FormulaEntry('Compound microscope (relaxed eye, approx.)', 'M ≈ (L/fo)(D/fe)'),
    FormulaEntry('Astronomical telescope (relaxed eye)', 'M = fo/fe'),
    FormulaEntry('Telescope tube length (relaxed eye)', 'Length = fo + fe'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The near point distance conventionally used for a normal human eye is:',
      options: ['10 cm', '25 cm', '50 cm', 'Infinity'],
      correctIndex: 1,
      solution: 'By convention, D = 25 cm is used as the standard near point for a normal, unaided eye in all magnification formulas.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Myopia (near-sightedness) is corrected using a:',
      options: ['Converging (convex) lens', 'Diverging (concave) lens', 'Cylindrical lens', 'Bifocal lens only'],
      correctIndex: 1,
      solution: 'In myopia the image forms in front of the retina; a diverging lens spreads the rays out slightly before they enter the eye, pushing the focus back onto the retina.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A simple magnifier of focal length 10 cm is used with the image at infinity (relaxed eye). Its magnifying power is:',
      options: ['1.5×', '2.5×', '10×', '25×'],
      correctIndex: 1,
      solution: 'M = D/f = 25/10 = 2.5×.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The same magnifier (f = 10 cm) is used so the image forms at the near point instead. Its magnifying power becomes:',
      options: ['2.5×', '3.5×', '1.4×', '10×'],
      correctIndex: 1,
      solution: 'M = 1 + D/f = 1 + 25/10 = 1 + 2.5 = 3.5×.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'An astronomical telescope has an objective of focal length 100 cm and an eyepiece of focal length 5 cm. Its magnifying power (relaxed eye) is:',
      options: ['5×', '20×', '95×', '105×'],
      correctIndex: 1,
      solution: 'M = fo/fe = 100/5 = 20×.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'For the telescope above (fo = 100 cm, fe = 5 cm), the length of the tube for a relaxed eye is:',
      options: ['95 cm', '100 cm', '105 cm', '20 cm'],
      correctIndex: 2,
      solution: 'Tube length = fo + fe = 100 + 5 = 105 cm (the objective\'s image forms exactly at the eyepiece\'s focus).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'To increase the magnifying power of an astronomical telescope, you should:',
      options: [
        'Increase fe and decrease fo',
        'Increase fo and decrease fe',
        'Increase both fo and fe equally',
        'Focal lengths do not matter, only the aperture does',
      ],
      correctIndex: 1,
      solution: 'M = fo/fe is maximised by a LARGE objective focal length and a SMALL eyepiece focal length.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Compared to a compound microscope, an astronomical telescope for high magnification generally needs:',
      options: [
        'Both objective and eyepiece with short focal lengths, exactly like a microscope',
        'A long focal length objective (opposite of a microscope\'s short-focus objective) paired with a short focal length eyepiece',
        'No eyepiece at all',
        'An objective with negative focal length',
      ],
      correctIndex: 1,
      solution: 'A microscope\'s objective has a very SHORT focal length (object is close by); a telescope\'s objective has a LONG focal length (object is at infinity) — the two instruments make opposite demands on the objective.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A telescope\'s ability to resolve two closely spaced faint stars (as opposed to simply magnifying them) is primarily limited by:',
      options: [
        'The magnifying power M = fo/fe alone',
        'Diffraction at the objective aperture — resolving power improves with a LARGER aperture',
        'The colour of the starlight',
        'The eyepiece focal length alone',
      ],
      correctIndex: 1,
      solution: 'Resolving power is fundamentally limited by diffraction at the objective\'s aperture; a bigger aperture reduces the diffraction spread and improves resolution, independent of magnifying power.',
    ),
  ],
  revision: [
    'Simple microscope: M = D/f (relaxed eye) or M = 1 + D/f (image at near point); D = 25 cm.',
    'Compound microscope: both objective and eyepiece have SHORT focal lengths; M ≈ (L/fo)(D/fe).',
    'Astronomical telescope: M = fo/fe — LARGE objective focal length, SHORT eyepiece focal length.',
    'Telescope tube length (relaxed eye) = fo + fe.',
    'A larger objective APERTURE improves light-gathering and resolving power, independent of magnification.',
    'Eye: cornea + lens form a real image on the retina; accommodation adjusts focus via the ciliary muscles.',
    'Myopia → diverging lens; hypermetropia → converging lens; presbyopia → bifocal lenses.',
  ],
  sandboxBuilder: (_) => const OpticalInstrumentsSandbox(),
);
