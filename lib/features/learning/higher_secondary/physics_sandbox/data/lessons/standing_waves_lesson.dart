import '../../models/lesson.dart';
import '../../simulators/standing_waves_sim.dart';
import '../../theme/tokens.dart';

/// Standing Waves — superposition, nodes/antinodes, and resonant harmonics.
final Lesson standingWavesLesson = Lesson(
  topicId: 'standing-waves',
  title: 'Standing Waves',
  accentColor: Palette.chWaves,
  bigQuestion:
      'Pluck a guitar string and a pattern of loops appears frozen in place — some points on the string never move at all, while points between them swing wildly. Nothing seems to be travelling anywhere, yet it started from two ordinary travelling waves. How can two moving waves add up to a pattern that doesn\'t move?',
  whyItMatters:
      'Standing waves are how every stringed and wind instrument makes music, how microwave ovens create hot and cold spots, and how quantum wavefunctions in a box are shaped. They are also one of the most reliably tested topics in both NEET and JEE — the harmonic formulas for strings and pipes appear almost every year. Understanding superposition here also sets up interference and diffraction in optics.',
  prediction: const PredictionPrompt(
    scenario:
        'A string fixed at both ends is vibrating in its fundamental (1st harmonic) mode. If you now drive it at exactly TWICE the fundamental frequency (2nd harmonic), how many stationary points (nodes, excluding the two fixed ends) appear along the string?',
    options: [
      'Still zero extra nodes — same as before',
      'One extra node appears at the exact centre',
      'Two extra nodes appear',
      'The string stops vibrating entirely',
    ],
    correctIndex: 1,
    reveal:
        'The nth harmonic on a string fixed at both ends fits n half-wavelengths between the ends, creating (n−1) nodes strictly between the fixed ends. The fundamental (n=1) has zero internal nodes; the 2nd harmonic (n=2) has exactly one, right at the midpoint. In the lab, switch harmonic mode from 1 to 2 and watch a new stationary point freeze into existence at the centre.',
  ),
  experiments: [
    'Set harmonic n = 1 (fundamental) and count nodes — only the two fixed ends',
    'Step up to n = 2, 3, 4 and watch new nodes appear evenly spaced',
    'Compare a string (both ends fixed, all harmonics) with a pipe closed at one end (only odd harmonics)',
    'Adjust the driving frequency slowly through resonance and watch amplitude peak sharply at each harmonic',
    'Freeze the animation at an antinode and a node — compare the local amplitude',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A standing wave is what results when two IDENTICAL waves (same amplitude, wavelength, frequency) travel through the same medium in OPPOSITE directions and superpose. This happens naturally when a wave reflects off a fixed or free boundary and interferes with itself. The result is a pattern that oscillates in place — the envelope of the pattern does not travel, even though it is built from two waves that individually do.',
      title: 'Two travelling waves make one standing wave',
    ),
    ContentBlock.formula('y₁ = A sin(kx − ωt),  y₂ = A sin(kx + ωt)  →  y = y₁+y₂ = 2A sin(kx) cos(ωt)',
        title: 'SUPERPOSITION OF OPPOSITE WAVES'),
    ContentBlock.paragraph(
      'The result y = 2A sin(kx) cos(ωt) separates into a SPATIAL part sin(kx) that fixes where each point sits, and a TEMPORAL part cos(ωt) that makes every point oscillate together, in phase, with amplitude that depends only on position (2A sin(kx)). At points where sin(kx) = 0, the amplitude is always zero — these are NODES. At points where sin(kx) = ±1, the amplitude is maximum (2A) — these are ANTINODES.',
      title: 'Nodes and antinodes',
    ),
    ContentBlock.bullets([
      'Nodes: points of ZERO displacement at all times — destructive interference is total here',
      'Antinodes: points of MAXIMUM displacement amplitude — constructive interference is total here',
      'Adjacent nodes (or adjacent antinodes) are separated by exactly λ/2',
      'A node and its neighbouring antinode are separated by λ/4',
    ]),
    ContentBlock.formula('fₙ = nv/(2L),   n = 1, 2, 3, …', title: 'HARMONICS — STRING FIXED AT BOTH ENDS'),
    ContentBlock.paragraph(
      'Both ends of a string tied down must be nodes (they cannot move). The allowed standing-wave patterns must fit a whole number of half-wavelengths between the two fixed ends: L = nλ/2, so λₙ = 2L/n and fₙ = v/λₙ = nv/(2L). ALL integers n = 1, 2, 3… are allowed — this is why a string produces the full harmonic series (fundamental plus all its integer multiples).',
      title: 'Why strings allow every harmonic',
    ),
    ContentBlock.formula('fₙ = nv/(4L),   n = 1, 3, 5, … (odd only)', title: 'PIPE CLOSED AT ONE END'),
    ContentBlock.paragraph(
      'A pipe closed at one end must have a node (no air motion) at the closed end but an antinode (maximum air motion) at the open end. Fitting a node-to-antinode distance of λ/4 means L = nλ/4 with n odd only — only 1st, 3rd, 5th... harmonics can exist. This is why a closed pipe (like a clarinet, roughly) sounds noticeably different in tone/timbre from an open pipe or string, which produce every harmonic.',
      title: 'Why closed pipes skip even harmonics',
    ),
    ContentBlock.realLife(
      'Every musical instrument is a standing-wave generator: a guitar string is fixed at both ends (all harmonics, rich buzzy tone), an open flute is open at both ends (also all harmonics), and instruments like a clarinet are effectively closed at the mouthpiece end (odd harmonics only, giving its distinctive hollow, woody tone). Microwave ovens set up standing electromagnetic waves too, which is why food can have unevenly heated "hot spots" at the antinodes — turntables exist specifically to average this out.',
    ),
    ContentBlock.mistake(
      'Assuming a standing wave means "nothing is moving." Every point EXCEPT the nodes is oscillating, and points at the antinodes move with the LARGEST amplitude of the entire pattern. What is stationary is the overall spatial PATTERN of nodes and antinodes, not the medium\'s particles themselves (except exactly at the nodes).',
    ),
    ContentBlock.mistake(
      'Forgetting that a pipe closed at one end only supports ODD harmonics, and mistakenly using fₙ = nv/(2L) (the open/string formula) instead of fₙ = nv/(4L) with only odd n. Mixing these two cases up is one of the most common wave-topic errors in exams.',
    ),
    ContentBlock.example(
      'A string of length 0.6 m is fixed at both ends and vibrates in its 3rd harmonic. If wave speed on the string is 200 m/s, find the frequency and sketch the node pattern.\n\nfₙ = nv/(2L) = 3×200/(2×0.6) = 600/1.2 = 500 Hz.\n\nThe 3rd harmonic (n=3) fits 3 half-wavelengths, giving nodes at both ends plus 2 additional internal nodes (at L/3 and 2L/3), and 3 antinodes total.',
    ),
    ContentBlock.jeeTip(
      'For resonance-tube experiments (a pipe with one end closed, dipped in water, air column length adjustable), successive resonance lengths differ by λ/2 — measuring the gap between two consecutive resonant lengths directly gives you λ/2 without needing to know the exact closed-end correction. This trick eliminates the "end correction" error entirely.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks to identify the harmonic number from a diagram showing loops (antinodes) — count the number of complete loops to get n directly for a string, since the nth harmonic has exactly n loops (antinodes) and n+1 nodes total (including both ends). Also remember: the fundamental frequency of a closed pipe is HALF that of an open pipe of the same length, since fₙ=₁ = v/4L vs v/2L.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Superpose two identical counter-propagating waves',
      math: 'y = A sin(kx−ωt) + A sin(kx+ωt)',
    ),
    DerivationStep(
      title: 'Apply the sine addition identity',
      math: 'sin(A−B) + sin(A+B) = 2 sinA cosB',
      note: 'With A = kx, B = ωt.',
    ),
    DerivationStep(
      title: 'Obtain the standing wave form',
      math: 'y(x,t) = [2A sin(kx)]·cos(ωt)',
      note: 'Position-dependent amplitude 2A sin(kx), multiplied by a universal time oscillation cos(ωt).',
    ),
    DerivationStep(
      title: 'Apply the boundary condition for a string fixed at both ends',
      math: 'y(0,t) = 0 and y(L,t) = 0 for all t  →  sin(kL) = 0  →  kL = nπ',
    ),
    DerivationStep(
      title: 'Solve for allowed wavelengths and frequencies',
      math: 'k = nπ/L = 2π/λ  →  λₙ = 2L/n  →  fₙ = v/λₙ = nv/(2L)',
      note: 'Every integer n is allowed — the full harmonic series.',
    ),
  ],
  formulas: const [
    FormulaEntry('Standing wave', 'y(x,t) = 2A sin(kx)·cos(ωt)'),
    FormulaEntry('Node spacing', 'Δx = λ/2', condition: 'between adjacent nodes'),
    FormulaEntry('String fixed both ends', 'fₙ = nv/(2L),  n = 1,2,3,…'),
    FormulaEntry('Pipe open both ends', 'fₙ = nv/(2L),  n = 1,2,3,…'),
    FormulaEntry('Pipe closed one end', 'fₙ = nv/(4L),  n = 1,3,5,… (odd only)'),
    FormulaEntry('Fundamental frequency', 'f₁ = v/(2L) [string/open] or v/(4L) [closed pipe]'),
    FormulaEntry('Resonance length gap', 'ΔL = λ/2', condition: 'between successive resonances in a closed pipe'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'At a node in a standing wave, the displacement is:',
      options: ['Always maximum', 'Always zero', 'Equal to the amplitude A', 'Varies randomly'],
      correctIndex: 1,
      solution: 'By definition, a node is a point of total destructive interference — displacement is zero at all times.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The distance between two adjacent nodes in a standing wave is:',
      options: ['λ', 'λ/2', 'λ/4', '2λ'],
      correctIndex: 1,
      solution: 'Adjacent nodes (or adjacent antinodes) are always separated by exactly half a wavelength.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A string fixed at both ends vibrates in its 2nd harmonic. The number of nodes (including the two ends) is:',
      options: ['1', '2', '3', '4'],
      correctIndex: 2,
      solution: 'The nth harmonic has (n+1) nodes total including endpoints. For n=2: 2+1 = 3 nodes (both ends plus one at the centre).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A pipe closed at one end can resonate at which of these harmonic numbers?',
      options: ['1, 2, 3, 4', '1, 3, 5, 7', '2, 4, 6, 8', 'Only 1'],
      correctIndex: 1,
      solution: 'A pipe closed at one end supports only odd harmonics: fₙ = nv/(4L) for n = 1, 3, 5, …',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A string of length 1 m fixed at both ends has wave speed 100 m/s. Its fundamental frequency is:',
      options: ['25 Hz', '50 Hz', '100 Hz', '200 Hz'],
      correctIndex: 1,
      solution: 'f₁ = v/(2L) = 100/(2×1) = 50 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'An open pipe and a closed pipe of the same length L have fundamental frequencies f_open and f_closed. Their ratio f_open : f_closed is:',
      options: ['1:1', '2:1', '1:2', '4:1'],
      correctIndex: 1,
      solution: 'f_open = v/(2L), f_closed = v/(4L). Ratio = (v/2L)/(v/4L) = 2:1 — the open pipe\'s fundamental is twice the closed pipe\'s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A string vibrating in its 4th harmonic has length 2 m. The wavelength of the standing wave is:',
      options: ['0.5 m', '1 m', '2 m', '4 m'],
      correctIndex: 1,
      solution: 'λₙ = 2L/n = 2×2/4 = 1 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A closed-pipe resonance tube shows successive resonances at air column lengths 17 cm and 51 cm. The wavelength of sound used is:',
      options: ['17 cm', '34 cm', '68 cm', '102 cm'],
      correctIndex: 2,
      solution: 'Successive resonances in a closed pipe differ by λ/2. ΔL = 51−17 = 34 cm = λ/2, so λ = 68 cm.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A standing wave is formed as y = 4 sin(0.5x) cos(200t) (SI-like units, x in metres). The distance between a node and its adjacent antinode is:',
      options: ['π m', 'π/2 m', 'π/4 m', '2π m'],
      correctIndex: 0,
      solution:
          'k = 0.5 → λ = 2π/k = 4π m. Node-to-antinode distance = λ/4 = 4π/4 = π m.',
    ),
  ],
  revision: [
    'Standing wave = superposition of two identical waves travelling in opposite directions.',
    'y = 2A sin(kx)·cos(ωt): amplitude depends on position, all points oscillate in phase together.',
    'Nodes (zero amplitude) and antinodes (maximum amplitude) alternate, spaced λ/4 apart.',
    'String fixed both ends: fₙ = nv/(2L), ALL integers n allowed — full harmonic series.',
    'Pipe closed one end: fₙ = nv/(4L), only ODD n allowed.',
    'Successive resonance lengths in a closed pipe differ by exactly λ/2 — a clean way to measure λ.',
    'Closed pipe fundamental is half the open pipe/string fundamental for the same length.',
  ],
  sandboxBuilder: (_) => const StandingWavesSimulator(),
);
