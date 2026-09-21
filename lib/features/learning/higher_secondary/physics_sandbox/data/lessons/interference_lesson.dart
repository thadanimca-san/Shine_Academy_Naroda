import '../../models/lesson.dart';
import '../../simulators/interference_sandbox.dart';

/// Interference — where two waves add up to darkness.
final Lesson interferenceLesson = Lesson(
  topicId: 'interference',
  title: 'Interference',
  bigQuestion:
      'Shine two identical beams of light on a wall and, in places, you get DARKNESS. How can adding light to light produce black bands?',
  whyItMatters:
      'Interference is the single most direct proof that light is a wave. The same principle explains the colours in soap films and oil slicks, how anti-reflection coatings work, and how we measure distances to a fraction of a wavelength. For JEE and NEET, Young\'s double-slit experiment is a guaranteed question — one formula, β = λD/d, unlocks the whole chapter.',
  prediction: const PredictionPrompt(
    scenario:
        'In a double-slit experiment the fringes on the screen are too close together to count. You want to spread them apart. Which single change spreads them the MOST?',
    options: [
      'Move the two slits closer together (smaller d)',
      'Move the two slits farther apart (larger d)',
      'Use blue light instead of red',
      'Move the screen closer to the slits',
    ],
    correctIndex: 0,
    reveal:
        'Fringe width β = λD/d. To widen fringes you shrink d, grow D, or use a longer wavelength (red). In the lab, drag d from 600 µm down to 100 µm and watch β grow six-fold. Bringing the screen closer (smaller D) or switching to blue (shorter λ) does the opposite.',
  ),
  experiments: [
    'Halve d and confirm the fringe spacing β exactly doubles',
    'Slide λ from violet (400 nm) to red (700 nm) — fringes widen and recolour',
    'Increase D and watch the whole pattern fan out',
    'Read the live β value and check it against β = λD/d yourself',
    'Notice the intensity curve peaks are all equal height — a signature of TWO slits',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Two waves meeting at a point simply add — crest on crest builds a bigger crest, crest on trough cancels. This is the superposition principle. When the two sources are coherent (same frequency, fixed phase relationship), the pattern of adding and cancelling stays put on the screen, and we see it as bright and dark fringes.',
      title: 'Superposition: waves add, they don\'t collide',
    ),
    ContentBlock.paragraph(
      'Everything depends on path difference — how much farther one wave has travelled than the other by the time they meet. If one wave is a whole number of wavelengths behind, the two arrive in step and reinforce: constructive interference. If it is behind by half a wavelength (or any odd half-integer), they arrive exactly out of step and cancel: destructive interference.',
      title: 'Path difference decides bright or dark',
    ),
    ContentBlock.formula(
        'Constructive (bright):  Δx = nλ\nDestructive (dark):  Δx = (n + ½)λ',
        title: 'CONDITIONS FOR FRINGES'),
    ContentBlock.paragraph(
      'In Young\'s experiment, two slits separated by d act as coherent sources. At a point on the screen a distance y from the centre, the path difference is Δx = d·sinθ ≈ dy/D for small angles. Setting this equal to nλ gives the position of the nth bright fringe, and the gap between neighbouring fringes is the fringe width β.',
      title: 'Young\'s double slit',
    ),
    ContentBlock.formula('β = λD/d', title: 'FRINGE WIDTH'),
    ContentBlock.realLife(
      'The rainbow sheen on a soap bubble or a puddle with a drop of oil is interference. Light reflecting off the top and bottom of a thin film travels slightly different distances; whichever wavelength interferes constructively is the colour you see, and it shifts as the film thickness (or your viewing angle) changes. Anti-reflection coatings on camera lenses use exactly this to CANCEL unwanted reflections.',
    ),
    ContentBlock.mistake(
      'Students think interference "creates" or "destroys" energy. It does neither. The energy that vanishes from the dark fringes reappears in the bright ones — the bright fringes are brighter than either beam alone. Total energy is perfectly conserved; interference only REDISTRIBUTES it.',
    ),
    ContentBlock.mistake(
      'Forgetting coherence. Two separate bulbs never produce a stable interference pattern because their phase relationship jitters randomly millions of times a second. That is why Young used ONE source split into two slits — the whole point of the single slit before the double slit is to make the two beams coherent.',
    ),
    ContentBlock.jeeTip(
      'When the whole apparatus is dipped in a medium of refractive index µ, the wavelength shrinks to λ/µ, so β shrinks to β/µ. JEE loves this: "fringe width in water" just means divide by µ. Similarly, covering one slit with a thin sheet shifts the entire pattern — path difference gains (µ−1)t.',
    ),
    ContentBlock.jeeTip(
      'Fringe width is independent of the fringe order n — every fringe has the same width β. So the distance from the central maximum to the nth bright fringe is simply nβ. Use this to convert "distance between 5th and 2nd fringe" into 3β in one step.',
    ),
    ContentBlock.neetNote(
      'NEET focuses on the conditions and the formula, not heavy derivation. Remember: bright fringe when path difference = nλ, dark when (n+½)λ; fringe width β = λD/d; intensity at a bright fringe with equal sources is 4I₀ (not 2I₀), because amplitudes add and intensity ∝ amplitude².',
    ),
    ContentBlock.example(
      'In a double-slit experiment, d = 0.2 mm, D = 1.0 m, λ = 600 nm. Find the fringe width and the distance to the 3rd bright fringe.\n\nβ = λD/d = (600×10⁻⁹ × 1.0)/(0.2×10⁻³) = 3.0×10⁻³ m = 3.0 mm.\n\n3rd bright fringe is at y₃ = 3β = 9.0 mm from the centre. Notice we never needed the actual intensities — the geometry alone fixes the positions.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Set up the geometry',
      math: 'Slits S₁, S₂ separated by d.\nScreen at distance D (D ≫ d).\nPoint P at height y above centre.',
      note: 'Two coherent sources; we track the extra path S₂P − S₁P.',
    ),
    DerivationStep(
      title: 'Find the path difference',
      math: 'Δx = S₂P − S₁P = d·sinθ ≈ d·tanθ = d·y/D',
      note: 'For small θ, sinθ ≈ tanθ ≈ y/D. This approximation is the heart of the derivation.',
    ),
    DerivationStep(
      title: 'Apply the bright-fringe condition',
      math: 'Δx = nλ\n→ d·yₙ/D = nλ\n→ yₙ = nλD/d',
      note: 'Position of the nth bright fringe from the centre.',
    ),
    DerivationStep(
      title: 'Subtract successive fringes for the width',
      math: 'β = yₙ₊₁ − yₙ = (n+1)λD/d − nλD/d\nβ = λD/d',
      note: 'The n cancels — every fringe is equally spaced.',
    ),
    DerivationStep(
      title: 'Intensity across the screen',
      math: 'I = I₀·cos²(Δφ/2),  Δφ = 2πΔx/λ\nI = 4I₀·cos²(πdy/λD)',
      note: 'Maxima reach 4I₀ (two equal sources), minima reach 0. This drives the curve in the lab.',
    ),
  ],
  formulas: const [
    FormulaEntry('Path difference (double slit)', 'Δx = d·sinθ ≈ dy/D'),
    FormulaEntry('Bright fringe', 'Δx = nλ,  yₙ = nλD/d'),
    FormulaEntry('Dark fringe', 'Δx = (n + ½)λ'),
    FormulaEntry('Fringe width', 'β = λD/d'),
    FormulaEntry('Fringe width in a medium', 'β\' = β/µ', condition: 'apparatus in medium of index µ'),
    FormulaEntry('Intensity', 'I = 4I₀cos²(πdy/λD)', condition: 'equal-amplitude sources'),
    FormulaEntry('Resultant intensity (general)', 'I = I₁ + I₂ + 2√(I₁I₂)cosφ'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In Young\'s double-slit experiment, the fringe width β is doubled if:',
      options: [
        'The slit separation d is doubled',
        'The slit separation d is halved',
        'The wavelength λ is halved',
        'The screen distance D is halved',
      ],
      correctIndex: 1,
      solution:
          'β = λD/d. β is inversely proportional to d, so halving d doubles β. Doubling d or halving λ or D would each HALVE β.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Two waves interfere destructively when their path difference is:',
      options: ['nλ', '(n + ½)λ', '2nλ', 'λ/4'],
      correctIndex: 1,
      solution:
          'Destructive interference (dark fringe) requires the waves to arrive exactly out of step, i.e. path difference = an odd multiple of half a wavelength = (n + ½)λ. A whole number of wavelengths (nλ) gives a bright fringe.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'In a double-slit setup, d = 0.5 mm, D = 1 m, λ = 500 nm. The fringe width is:',
      options: ['0.5 mm', '1.0 mm', '2.0 mm', '5.0 mm'],
      correctIndex: 1,
      solution:
          'β = λD/d = (500×10⁻⁹ × 1)/(0.5×10⁻³) = 10⁻³ m = 1.0 mm.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'The intensity at a bright fringe due to two coherent sources each of intensity I₀ is:',
      options: ['I₀', '2I₀', '4I₀', '√2 I₀'],
      correctIndex: 2,
      solution:
          'Amplitudes add: A = A₀ + A₀ = 2A₀. Intensity ∝ amplitude², so I = (2A₀)² ∝ 4I₀. This is why the bright fringe is brighter than the simple sum 2I₀ — the "extra" energy comes from the dark fringes.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A double-slit apparatus giving fringe width β in air is fully immersed in water (µ = 4/3). The new fringe width is:',
      options: ['4β/3', '3β/4', 'β', '16β/9'],
      correctIndex: 1,
      solution:
          'In water, wavelength becomes λ/µ, so β\' = β/µ = β/(4/3) = 3β/4. Fringes bunch together in a denser medium.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'In a double-slit experiment the distance between the 4th and 1st bright fringes is 7.5 mm. The fringe width is:',
      options: ['1.5 mm', '2.0 mm', '2.5 mm', '7.5 mm'],
      correctIndex: 2,
      solution:
          'The 4th and 1st bright fringes are separated by (4−1) = 3 fringe widths. So 3β = 7.5 mm → β = 2.5 mm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A thin sheet of thickness t and refractive index µ is placed over one slit. The central fringe shifts by a number of fringes equal to:',
      options: ['(µ−1)t/λ', 'µt/λ', '(µ−1)t/D', 't/λ'],
      correctIndex: 0,
      solution:
          'The sheet adds an extra optical path (µ−1)t to that beam. The number of fringes shifted = extra path / λ = (µ−1)t/λ. The pattern moves toward the covered slit.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.advanced,
      question:
          'Two coherent sources have intensities in the ratio 4:1. The ratio of maximum to minimum intensity in the pattern is:',
      options: ['5:3', '9:1', '4:1', '25:9'],
      correctIndex: 1,
      solution:
          'Amplitudes ∝ √I, so A₁:A₂ = 2:1. I_max ∝ (A₁+A₂)² = 9, I_min ∝ (A₁−A₂)² = 1. Ratio = 9:1.',
    ),
  ],
  revision: [
    'Superposition: coherent waves add; path difference nλ → bright, (n+½)λ → dark.',
    'Fringe width β = λD/d — same for every fringe, so nth bright fringe sits at nβ.',
    'Immersing in a medium µ shrinks λ and β by a factor µ.',
    'Equal sources give bright-fringe intensity 4I₀, dark-fringe intensity 0.',
    'Coherence is essential — two independent bulbs give no stable pattern.',
    'Interference conserves energy: it redistributes light, never destroys it.',
  ],
  sandboxBuilder: (_) => const InterferenceSandbox(),
);
