import '../../models/lesson.dart';
import '../../simulators/diffraction_sandbox.dart';
import '../../theme/tokens.dart';

/// Diffraction — single-slit bending of light and its minima condition.
final Lesson diffractionLesson = Lesson(
  topicId: 'diffraction',
  title: 'Diffraction',
  accentColor: Palette.chOptics,
  bigQuestion:
      'You can hear someone talking around a corner, but you cannot SEE them until you step into their line of sight. Sound bends around obstacles far more easily than light does — yet both are waves. If bending around obstacles ("diffraction") is a universal wave behaviour, why does light seem so stubbornly straight-line while sound curves so easily?',
  whyItMatters:
      'Diffraction is the direct proof that light is a wave, and single-slit diffraction is a NEET/JEE staple that is very easy to confuse with double-slit interference — examiners specifically probe this confusion. Understanding diffraction also explains a very practical limit: no telescope, microscope, or camera lens, however perfectly built, can resolve details finer than what diffraction allows.',
  prediction: const PredictionPrompt(
    scenario:
        'Light passes through a single narrow slit and falls on a screen. As the slit width a is made NARROWER (while wavelength stays fixed), the diffraction pattern on the screen:',
    options: [
      'Stays exactly the same width, since diffraction only depends on wavelength',
      'Gets NARROWER — a narrow slit produces a narrow, tightly focused pattern',
      'Gets WIDER — a narrower slit spreads the light out into a broader pattern',
      'Disappears completely — no light gets through a very narrow slit',
    ],
    correctIndex: 2,
    reveal:
        'The first-minimum condition is a sinθ1 = λ, so sinθ1 = λ/a — a SMALLER slit width a gives a LARGER θ1, spreading the central maximum wider. In the lab, drag the slit width slider down and watch the whole diffraction pattern stretch outward. This is the opposite of what many students expect: making the opening smaller makes the pattern bigger, not smaller.',
  ),
  experiments: [
    'Shrink the slit width a and watch the diffraction pattern spread out wider',
    'Increase the wavelength λ (toward red) and watch the pattern widen too — both a smaller a and a longer λ widen it',
    'Read the first-minimum angle θ1 and confirm it grows as a shrinks',
    'Increase the screen distance D and watch the physical size of the central bright band grow (though the angular width stays fixed)',
    'Compare the width of the bright central band to the faint side bands — the central one is always about twice as wide',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Diffraction is the bending of waves around obstacles and their spreading out after passing through narrow openings — a universal behaviour of ALL waves, not just light. It becomes noticeable whenever the size of the opening or obstacle is comparable to (or smaller than) the wavelength of the wave. Sound waves have wavelengths of centimetres to metres, comparable to doorways and corners, so sound diffracts obviously; visible light has a wavelength of only ~500 nm, far smaller than any ordinary doorway, so light\'s diffraction around everyday objects is far too subtle to notice by eye.',
      title: 'What diffraction is, and why sound bends more than light',
    ),
    ContentBlock.bullets([
      'Diffraction happens because of the SINGLE slit\'s own finite width — every point across that width acts as a source of secondary wavelets (Huygens\' principle) that interfere with EACH OTHER',
      'Interference (as in the double-slit experiment) happens between light from TWO OR MORE separate, coherent sources or slits',
      'A double-slit pattern is actually diffraction (from each slit\'s width) MULTIPLIED by interference (between the two slits) — both effects are present at once in real double-slit setups',
    ], title: 'Diffraction vs interference — the crucial distinction'),
    ContentBlock.formula('a sinθ = nλ  (n = 1, 2, 3, …)', title: 'SINGLE-SLIT DIFFRACTION MINIMA'),
    ContentBlock.paragraph(
      'a is the slit width, θ is the angle from the central axis, λ is the wavelength, and n is an integer (1, 2, 3, …). CRUCIALLY, this condition gives the positions of the DARK FRINGES (minima), not bright fringes — this is the opposite of the double-slit interference formula (d sinθ = nλ), which gives BRIGHT fringes (maxima) for the same-looking equation. Mixing these two up is one of the most common errors in the entire optics syllabus.',
      title: 'The minima condition — and its classic trap',
    ),
    ContentBlock.paragraph(
      'Between the two first-order minima (at n = ±1) lies the CENTRAL MAXIMUM — by far the brightest and widest feature of the pattern. Beyond that, secondary maxima appear between successive minima, but they are both much dimmer and much narrower than the central maximum. In fact, the central maximum is roughly TWICE as wide (in angle) as each secondary maximum.',
      title: 'Central maximum: wide and bright',
    ),
    ContentBlock.formula('Angular width of central maximum = 2λ/a', title: 'CENTRAL MAXIMUM WIDTH'),
    ContentBlock.paragraph(
      'This total angular width (from the −1 minimum to the +1 minimum) is 2λ/a, twice the single-sided angle λ/a. On a screen at distance D, the LINEAR width of the central bright band is approximately 2Dλ/a for small angles.',
      title: 'From angle to a real, measurable width',
    ),
    ContentBlock.bullets([
      'For visible light (λ ~ 500 nm) through everyday-sized openings (doors, windows — metres wide), λ/a is astronomically tiny, so the diffraction spread is unnoticeable',
      'For narrow slits (micrometres wide, comparable to λ), the diffraction spread becomes large and easily observed in the lab',
      'Sound (λ ~ metres) diffracts noticeably around ordinary objects (doorways, corners) because its wavelength is comparable to those obstacle sizes',
    ], title: 'Why we don\'t "see" diffraction around doorways but DO hear around them'),
    ContentBlock.realLife(
      'Diffraction is why you can hear a conversation from around a corner but cannot see the speaker: sound\'s long wavelength diffracts easily around the corner, while light\'s tiny wavelength travels in an almost perfectly straight line past the same corner. It is also why a laser pointer\'s beam through a fine slit or hair visibly fans out into a diffraction pattern, revealing the wave nature of light in a simple classroom demonstration.',
    ),
    ContentBlock.mistake(
      'Treating a sinθ = nλ as a MAXIMA condition, by analogy with the double-slit interference formula d sinθ = nλ. For single-slit diffraction, a sinθ = nλ gives the DARK fringes (minima) — a very easy point to lose marks on if you don\'t pause to check which phenomenon (interference vs. diffraction) the question is actually about.',
    ),
    ContentBlock.mistake(
      'Believing diffraction and interference are entirely separate phenomena that never occur together. In a real double-slit (Young\'s) experiment, each individual slit also diffracts on its own — the overall pattern you see is the double-slit INTERFERENCE fringes multiplied by (modulated by) the single-slit DIFFRACTION envelope from each slit\'s own finite width.',
    ),
    ContentBlock.example(
      'Light of wavelength 600 nm passes through a slit of width 0.30 mm. Find the angular position of the first diffraction minimum.\n\na sinθ = λ → sinθ = λ/a = (600×10⁻⁹) / (0.30×10⁻³) = 2×10⁻³.\nθ ≈ 2×10⁻³ rad (very small angle, so sinθ ≈ θ) ≈ 0.115°.\n\nThe central maximum\'s full angular width is 2θ ≈ 4×10⁻³ rad.',
    ),
    ContentBlock.jeeTip(
      'For small diffraction angles (the usual case, since λ ≪ a in most lab setups), use the small-angle approximation sinθ ≈ tanθ ≈ θ (in radians) to convert directly between the angular minimum position and a LINEAR position on a screen at distance D: y ≈ Dθ = Dλ/a. This shortcut avoids awkward inverse-trig work in most numericals.',
    ),
    ContentBlock.neetNote(
      'NEET commonly asks conceptual comparisons: doubling the slit width a HALVES the diffraction spread (pattern narrows); doubling the wavelength λ DOUBLES the spread (pattern widens). Also remember the direct link to resolving power (see Optical Instruments): a telescope or microscope\'s ability to distinguish two close objects is fundamentally limited by diffraction at its aperture — a bigger aperture (relative to λ) means less diffraction spread and sharper resolution.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Treat the slit as a continuum of Huygens\' secondary sources',
      math: 'Slit width a, divided conceptually into many point sources across its width, all in phase at the slit',
    ),
    DerivationStep(
      title: 'Consider the path difference from the two EDGES of the slit at angle θ',
      math: 'Path difference between the two edge rays = a sinθ',
    ),
    DerivationStep(
      title: 'For the first minimum, split the slit into two halves',
      math: 'If a sinθ = λ, pair up points across the slit that are a/2 apart: each pair has a path difference of λ/2 → destructive interference',
      note: 'Every point in the top half cancels with a corresponding point in the bottom half, so the net amplitude is zero — a minimum.',
    ),
    DerivationStep(
      title: 'Generalise to all minima',
      math: 'a sinθ = nλ,  n = 1, 2, 3, …',
      note: 'For higher n, the slit can be divided into 2n equal parts that cancel pairwise, each time giving a minimum — not a maximum.',
    ),
    DerivationStep(
      title: 'Locate the edges of the central maximum',
      math: 'First minima at θ = ±sin⁻¹(λ/a) → total angular width of central maximum = 2λ/a (for small θ)',
      note: 'This central band is the brightest and widest feature; secondary maxima between higher-order minima are much dimmer and narrower.',
    ),
  ],
  formulas: const [
    FormulaEntry('Single-slit diffraction minima', 'a sinθ = nλ,  n = 1, 2, 3, …'),
    FormulaEntry('Angular width of central maximum', '2λ/a'),
    FormulaEntry('Linear width of central maximum (small angle, screen at D)', '2Dλ/a'),
    FormulaEntry('First-minimum angle (small angle)', 'θ1 ≈ λ/a'),
    FormulaEntry('Double-slit interference maxima (for contrast)', 'd sinθ = nλ', condition: 'a DIFFERENT phenomenon — bright fringes, two slits'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Diffraction of light around ordinary objects (like a doorway) is much less noticeable than diffraction of sound because:',
      options: [
        'Light travels faster than sound',
        'Light\'s wavelength is far smaller than the size of everyday objects, while sound\'s wavelength is comparable',
        'Light does not actually diffract at all',
        'Sound has no wave nature',
      ],
      correctIndex: 1,
      solution: 'Diffraction becomes significant when the wavelength is comparable to the obstacle/opening size. Visible light (~500 nm) is far smaller than doorways, while sound (~cm to m) is comparable, so sound diffracts noticeably and light does not.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The condition a sinθ = nλ for a single slit gives the positions of:',
      options: ['Bright fringes (maxima)', 'Dark fringes (minima)', 'The central maximum only', 'Points of maximum intensity always'],
      correctIndex: 1,
      solution: 'For single-slit diffraction, a sinθ = nλ locates the MINIMA (dark fringes) — a common trap since it resembles the double-slit maxima formula.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Light of wavelength 500 nm passes through a slit of width 0.5 mm. The angle of the first diffraction minimum is approximately:',
      options: ['0.001 rad', '0.01 rad', '0.1 rad', '1 rad'],
      correctIndex: 0,
      solution: 'sinθ = λ/a = (500×10⁻⁹)/(0.5×10⁻³) = 10⁻³ rad. Since this is small, θ ≈ 10⁻³ rad = 0.001 rad.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If the slit width in a single-slit diffraction setup is doubled (wavelength unchanged), the width of the central maximum:',
      options: ['Doubles', 'Halves', 'Stays the same', 'Quadruples'],
      correctIndex: 1,
      solution: 'Central maximum width ∝ λ/a. Doubling a halves this width — a wider slit gives a narrower (more concentrated) diffraction pattern.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A single slit of width 0.2 mm is illuminated by light of wavelength 600 nm, and the pattern is observed on a screen 1 m away. The width of the central maximum is approximately:',
      options: ['3 mm', '6 mm', '1.5 mm', '12 mm'],
      correctIndex: 1,
      solution: 'Width ≈ 2Dλ/a = 2×1×(600×10⁻⁹)/(0.2×10⁻³) = 2×3×10⁻³ = 6×10⁻³ m = 6 mm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The essential physical difference between diffraction and interference is:',
      options: [
        'Diffraction only happens with sound, interference only with light',
        'Diffraction arises from a single slit\'s own finite width (many secondary sources across it); interference arises between two or more separate coherent sources',
        'There is no real difference — they are the same phenomenon',
        'Interference requires white light; diffraction requires monochromatic light',
      ],
      correctIndex: 1,
      solution: 'Diffraction is self-interference of wavelets across ONE opening\'s width; interference (in the Young\'s double-slit sense) is between light from TWO OR MORE distinct coherent sources.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'In a real Young\'s double-slit experiment, the observed fringe pattern is best described as:',
      options: [
        'Pure interference fringes, with no diffraction effects at all',
        'Pure diffraction, with no interference',
        'Double-slit interference fringes modulated (multiplied) by the single-slit diffraction envelope from each slit\'s own width',
        'Random noise with no predictable pattern',
      ],
      correctIndex: 2,
      solution: 'Each slit has finite width and so diffracts on its own; the fine interference fringes from the two slits are enveloped/modulated by this broader single-slit diffraction pattern.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'The resolving power of a microscope or telescope (its ability to distinguish two close objects) is fundamentally limited by:',
      options: [
        'The magnifying power of the eyepiece alone',
        'Diffraction at the objective\'s aperture — a larger aperture (relative to wavelength) gives better resolution',
        'The colour of the light source only, with no dependence on aperture',
        'It has no fundamental physical limit',
      ],
      correctIndex: 1,
      solution: 'Diffraction at the aperture sets a fundamental limit on resolving power; a larger aperture (compared to the wavelength) reduces the diffraction spread and allows finer details to be resolved.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'For a single slit, the SECOND minimum occurs at an angle θ2 satisfying:',
      options: ['a sinθ2 = λ/2', 'a sinθ2 = λ', 'a sinθ2 = 2λ', 'a sinθ2 = 3λ/2'],
      correctIndex: 2,
      solution: 'The general minima condition is a sinθ = nλ. For n = 2 (second minimum), a sinθ2 = 2λ.',
    ),
  ],
  revision: [
    'Diffraction is the bending/spreading of ANY wave through a narrow opening or around an obstacle — significant only when the opening is comparable to the wavelength.',
    'Diffraction = self-interference from ONE slit\'s width; interference = between TWO or more separate coherent sources.',
    'Single-slit MINIMA: a sinθ = nλ (a common trap — this is NOT a maxima condition, unlike the similar-looking double-slit formula).',
    'Central maximum is about TWICE as wide (angularly) as each secondary maximum: width = 2λ/a.',
    'Smaller slit width a, or longer wavelength λ, both WIDEN the diffraction pattern.',
    'Sound diffracts noticeably around everyday objects (λ ~ obstacle size); light usually does not (λ ≪ obstacle size).',
    'Resolving power of microscopes/telescopes is fundamentally limited by diffraction at the aperture — bigger aperture, better resolution.',
  ],
  sandboxBuilder: (_) => const DiffractionSandbox(),
);
