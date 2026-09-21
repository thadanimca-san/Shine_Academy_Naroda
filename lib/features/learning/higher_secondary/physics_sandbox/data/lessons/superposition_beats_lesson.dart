import '../../models/lesson.dart';
import '../../simulators/superposition_beats_sandbox.dart';
import '../../theme/tokens.dart';

/// Superposition & Beats — waves add algebraically, and close frequencies throb.
final Lesson superpositionBeatsLesson = Lesson(
  topicId: 'superposition-beats',
  title: 'Superposition & Beats',
  accentColor: Palette.chWaves,
  bigQuestion:
      'Pluck two guitar strings tuned almost — but not quite — to the same note, and instead of a steady tone you hear a slow "wah... wah... wah" throb. No one is turning the volume knob. Where does that rhythmic pulsing come from if both strings just keep vibrating steadily?',
  whyItMatters:
      'The principle of superposition is the single idea underneath interference, diffraction, standing waves, and beats — almost every wave-optics and sound topic in JEE/NEET traces back to "just add the displacements." Beats turn this abstract addition into something you can literally hear, and the beat-frequency result f_beat = |f₁ − f₂| is a favourite short, elegant numerical.',
  prediction: const PredictionPrompt(
    scenario:
        'Two tuning forks vibrate at 256 Hz and 260 Hz respectively, sounded together. A listener hears a wobbling loudness. How many times per second does the sound get loud (a "beat")?',
    options: [
      '256 times per second',
      '4 times per second',
      '516 times per second',
      '2 times per second',
    ],
    correctIndex: 1,
    reveal:
        'Beat frequency = |f₁ − f₂| = |260 − 256| = 4 Hz — four loud pulses every second, easily audible. In the lab, set f₁ = 6 Hz and f₂ = 10 Hz and watch the bold "sum" wave envelope swell and shrink 4 times over the same stretch that the individual waves complete many more cycles — the envelope period is always much slower than either wave.',
  ),
  experiments: [
    'Set f₁ = 6 Hz and f₂ = 6.5 Hz — a very slow beat, envelope barely changes across the visible window',
    'Set f₁ = 6 Hz and f₂ = 10 Hz — a fast, obvious throb in the bold sum curve',
    'Make f₁ = f₂ exactly — the envelope flattens out completely: zero beats',
    'Watch how the two individual waves (top two rows) drift in and out of phase with each other',
    'Note that the beat frequency reading always equals |f₁ − f₂|, never f₁ + f₂',
  ],
  concept: const [
    ContentBlock.paragraph(
      'When two or more waves travel through the same region of a medium at the same time, the resultant displacement at every point and instant is simply the ALGEBRAIC SUM of the displacements each wave would have produced alone. This is the principle of superposition — it holds because the wave equation is linear, so waves pass through each other unaffected and simply add where they overlap.',
      title: 'Superposition: waves just add',
    ),
    ContentBlock.formula('y_net(x,t) = y₁(x,t) + y₂(x,t) + …', title: 'PRINCIPLE OF SUPERPOSITION'),
    ContentBlock.paragraph(
      'When two waves of the SAME frequency meet, the result depends on their path difference Δ (or equivalently, phase difference). If Δ = nλ (n = 0, 1, 2, …), the waves arrive crest-to-crest — CONSTRUCTIVE interference — and the resultant amplitude is the sum of the two. If Δ = (n + ½)λ, the waves arrive crest-to-trough — DESTRUCTIVE interference — and the resultant amplitude is the difference (zero if the amplitudes are equal).',
      title: 'Constructive vs destructive interference',
    ),
    ContentBlock.formula(
        'Constructive: path difference = nλ\nDestructive: path difference = (n+½)λ',
        title: 'INTERFERENCE CONDITIONS'),
    ContentBlock.paragraph(
      'BEATS arise from a different situation: two waves of nearly EQUAL but not identical frequencies (f₁ ≈ f₂), overlapping at the same point over time. Because the frequencies are close, the two waves slowly drift in and out of phase with each other — momentarily reinforcing (loud), then a little later cancelling (quiet), then reinforcing again. The listener hears a single tone whose LOUDNESS rises and falls periodically — this rise-and-fall rate is the beat frequency.',
      title: 'Beats: two close tones interfering in time',
    ),
    ContentBlock.formula('f_beat = |f₁ − f₂|', title: 'BEAT FREQUENCY'),
    ContentBlock.bullets([
      'Beats require frequencies CLOSE together — if f₁ and f₂ differ by more than about 15-20 Hz, the ear hears two separate notes, not a throb',
      'The beat frequency is always the DIFFERENCE of the two frequencies, never their sum',
      'The perceived "loud" moments occur f_beat times per second, but the underlying tone still vibrates at roughly the average frequency (f₁+f₂)/2',
    ]),
    ContentBlock.realLife(
      'Piano tuners and guitarists tune by ear using beats: strike a reference tuning fork alongside the string, and if the string is even slightly off-pitch you hear a beating "wah-wah-wah." As you tighten or loosen the string, the beat rate slows down; when the beats vanish entirely (zero beats), the string is in tune. Orchestras use the same trick when tuning to the oboe\'s reference A.',
    ),
    ContentBlock.mistake(
      'Confusing beats with interference fringes. Beats are a variation in loudness over TIME at one fixed point, caused by frequency difference. Interference fringes (like in Young\'s double slit) are a variation in intensity over SPACE at one instant, caused by path difference between waves of the SAME frequency. Different phenomena, similar-sounding math.',
    ),
    ContentBlock.mistake(
      'Writing f_beat = f₁ + f₂ instead of |f₁ − f₂|. The sum of the frequencies is far too fast to perceive as a separate throb — always the ear (or the eye, on the sandbox\'s bold curve) only notices the slow difference frequency.',
    ),
    ContentBlock.example(
      'Two identical sitar strings are struck together. One vibrates at 300 Hz. A beat frequency of 5 Hz is heard. Tightening the second string increases the beat frequency to 8 Hz. What was the second string\'s original frequency?\n\nBeat frequency = |f₁ − f₂| = 5 Hz means f₂ = 295 Hz or 305 Hz.\nTightening a string RAISES its frequency (higher tension → higher pitch). If f₂ started at 305 Hz and rose further, the beat frequency (|300 − f₂|) would still be increasing, matching the observation (5 Hz → 8 Hz).\nIf f₂ had started at 295 Hz, tightening it would raise it toward 300 Hz, which would DECREASE the beat frequency — contradicting the given rise to 8 Hz.\nSo the original frequency was f₂ = 305 Hz.',
    ),
    ContentBlock.jeeTip(
      'The "raise or lower?" trick: when you slightly change one source\'s frequency and the beat rate changes, you can tell which direction the frequency moved. If tightening/loading a string INCREASES the beat frequency, the string\'s frequency was moving AWAY from the reference; if it DECREASES the beat frequency, it was moving TOWARD the reference frequency (and briefly hits zero beats exactly when they match).',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the beats formula as a direct plug-in: f_beat = |f₁ − f₂|, and the fact that beats require frequencies close enough for the ear to track loudness variation (typically under ~10 Hz difference) — larger differences are heard as two distinct notes, not beats.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write the two waves of close frequency at a fixed point',
      math: 'y₁ = A cos(2πf₁t)\ny₂ = A cos(2πf₂t)',
      note: 'Same amplitude A, same location, slightly different frequencies f₁ ≈ f₂.',
    ),
    DerivationStep(
      title: 'Superpose (add) the two displacements',
      math: 'y = y₁ + y₂ = A[cos(2πf₁t) + cos(2πf₂t)]',
    ),
    DerivationStep(
      title: 'Apply the sum-to-product identity',
      math: 'cos A + cos B = 2 cos((A−B)/2) · cos((A+B)/2)',
      note: 'A standard trigonometric identity, with A = 2πf₁t and B = 2πf₂t.',
    ),
    DerivationStep(
      title: 'Substitute and group terms',
      math: 'y = [2A cos(2π·(f₁−f₂)/2 ·t)] · cos(2π·(f₁+f₂)/2 ·t)',
      note: 'This is a fast oscillation at the average frequency (f₁+f₂)/2, whose amplitude is modulated by a slow envelope oscillating at (f₁−f₂)/2.',
    ),
    DerivationStep(
      title: 'Identify the beat frequency from the envelope',
      math: 'Envelope = 2A cos(2π·(f₁−f₂)/2·t)  →  loudness maxima occur twice per envelope cycle',
      note: 'Because |cos| has two peaks per cycle, the LOUDNESS (which depends on |envelope|, not its sign) repeats at twice the envelope frequency.',
    ),
    DerivationStep(
      title: 'Conclude the beat frequency',
      math: 'f_beat = 2 × (f₁−f₂)/2 = |f₁ − f₂|',
      note: 'The number of loud pulses heard per second equals the difference of the two source frequencies.',
    ),
  ],
  formulas: const [
    FormulaEntry('Superposition principle', 'y_net = y₁ + y₂ + …'),
    FormulaEntry('Constructive interference', 'path difference = nλ,  n = 0,1,2,…'),
    FormulaEntry('Destructive interference', 'path difference = (n+½)λ'),
    FormulaEntry('Beat frequency', 'f_beat = |f₁ − f₂|'),
    FormulaEntry('Resultant of two close-frequency waves', 'y = 2A cos(π(f₁−f₂)t) · cos(π(f₁+f₂)t)',
        condition: 'equal amplitudes A'),
    FormulaEntry('Beat period', 'T_beat = 1/f_beat'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Two tuning forks of frequency 512 Hz and 516 Hz are sounded together. The beat frequency is:',
      options: ['4 Hz', '1028 Hz', '514 Hz', '2 Hz'],
      correctIndex: 0,
      solution: 'f_beat = |f₁ − f₂| = |516 − 512| = 4 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Beats are produced by superposing two waves of:',
      options: [
        'The same frequency, different amplitude',
        'Slightly different frequencies',
        'Very different (widely separated) frequencies',
        'The same frequency and same phase',
      ],
      correctIndex: 1,
      solution: 'Beats need two frequencies close to each other so the ear can track the slow loudness variation caused by their difference.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A tuning fork of unknown frequency gives 5 beats/s with a fork of known frequency 250 Hz. When the unknown fork is loaded with wax (which lowers its frequency), the beat frequency decreases. The unknown frequency is:',
      options: ['245 Hz', '255 Hz', '250 Hz', '260 Hz'],
      correctIndex: 1,
      solution:
          'Beat freq 5 Hz means the unknown is 245 or 255 Hz. Loading with wax lowers the frequency. If it were 255 Hz, lowering it moves toward 250 Hz, DECREASING the beat frequency — matches. If it were 245 Hz, lowering it moves further from 250 Hz, which would INCREASE the beat frequency. So the unknown fork is 255 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Two waves y₁ = A cos(2π·300t) and y₂ = A cos(2π·305t) superpose. The envelope of the resultant repeats with period:',
      options: ['1/5 s', '1/10 s', '1/300 s', '1/605 s'],
      correctIndex: 0,
      solution: 'f_beat = |305 − 300| = 5 Hz, so T_beat = 1/f_beat = 1/5 s = 0.2 s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two waves of equal amplitude A and frequencies 400 Hz, 404 Hz superpose. The maximum amplitude the resultant ever reaches is:',
      options: ['A', '2A', '4A', 'A/2'],
      correctIndex: 1,
      solution: 'When the two waves are perfectly in phase (constructive), amplitudes simply add: A + A = 2A. This peak recurs at the beat rate.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Two sources emit waves with a constant path difference of 2.5λ at a certain point. The interference there is:',
      options: ['Constructive', 'Destructive', 'Neither, intensity is average', 'Cannot be determined'],
      correctIndex: 1,
      solution: '2.5λ = (2+½)λ, which matches the destructive condition (n+½)λ with n=2. The waves arrive out of phase and cancel.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A source emits two frequencies 480 Hz and 484 Hz simultaneously. In 8 seconds, how many beats are heard?',
      options: ['16', '32', '4', '8'],
      correctIndex: 1,
      solution: 'f_beat = |484 − 480| = 4 Hz → 4 beats per second. In 8 s: 4 × 8 = 32 beats.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Why can beats normally NOT be heard if the two source frequencies differ by, say, 50 Hz?',
      options: [
        'The formula f_beat = |f₁−f₂| stops applying above 20 Hz difference',
        'The ear cannot follow such rapid loudness fluctuations — it hears two separate tones instead',
        'The waves stop superposing at large frequency differences',
        'Such waves cancel completely and produce silence',
      ],
      correctIndex: 1,
      solution:
          'Superposition and the beat formula still apply mathematically, but human hearing can only perceptually track loudness fluctuations up to roughly 10-15 Hz; faster fluctuations are heard as two distinct pitches rather than a throb.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two coherent sources of equal amplitude produce zero intensity at a point. This point corresponds to a path difference of:',
      options: ['λ', '2λ', 'λ/2', '3λ/2 or (n+½)λ in general'],
      correctIndex: 3,
      solution: 'Zero resultant intensity from equal-amplitude waves requires perfectly destructive interference, i.e. path difference = (n+½)λ — half-integer multiples of λ.',
    ),
  ],
  revision: [
    'Superposition: resultant displacement = algebraic sum of individual wave displacements.',
    'Constructive interference: path difference = nλ. Destructive: path difference = (n+½)λ.',
    'Beats arise from two close (not equal) frequencies overlapping in TIME at one point.',
    'f_beat = |f₁ − f₂| — always the difference, never the sum.',
    'Derivation: cos A + cos B → fast average-frequency oscillation inside a slow envelope; loudness maxima recur at the envelope\'s double-frequency rate = |f₁−f₂|.',
    'Zero beats (steady tone) means the two frequencies are exactly equal — the basis of tuning by ear.',
    'Beats (time variation) and interference fringes (space variation) are related but distinct phenomena.',
  ],
  sandboxBuilder: (_) => const SuperpositionBeatsSandbox(),
);
