import '../../models/lesson.dart';
import '../../simulators/sound_waves_sandbox.dart';
import '../../theme/tokens.dart';

/// Sound Waves — longitudinal pressure waves, speed in different media, and the dB scale.
final Lesson soundWavesLesson = Lesson(
  topicId: 'sound-waves',
  title: 'Sound Waves',
  accentColor: Palette.chWaves,
  bigQuestion:
      'Astronauts on the Moon can\'t hear each other shout, even standing right next to each other, and have to talk over radio instead. Sound is "just vibrations" — so why does it need something to vibrate at all?',
  whyItMatters:
      'Sound waves are the most common example of longitudinal waves in the entire syllabus, and questions on wave speed in different media, the decibel scale, and pipe/string harmonics appear across both NEET and JEE year after year. Understanding sound as a genuine pressure wave (not just an abstract "wave on a string") is what makes the loudness/pitch/quality distinctions click.',
  prediction: const PredictionPrompt(
    scenario:
        'A single sound wave of fixed frequency travels first through air, then through water, then through steel. In which medium does it travel FASTEST?',
    options: [
      'Air — gases are "lighter" so sound should zip through easily',
      'Water — a nice middle ground',
      'Steel — the solid',
      'Speed is the same in every medium; only pitch changes',
    ],
    correctIndex: 2,
    reveal:
        'Sound travels fastest in solids, then liquids, then slowest in gases — v_solid > v_liquid > v_gas — because tightly-bonded, closely-packed particles transmit a pressure disturbance to their neighbours almost instantly. In the lab, switch the medium selector from Air (340 m/s) to Steel (5960 m/s) and watch the speed readout jump almost 18-fold, even though the frequency slider hasn\'t moved at all.',
  ),
  experiments: [
    'Switch medium from Air to Water to Steel and watch the speed readout climb sharply each time',
    'Raise the frequency slider and watch the compressions (dark particle bunches) pack closer together — that changes pitch, not loudness',
    'Raise the amplitude slider and watch the pressure graph grow taller and the particles bunch more densely — that changes loudness, not pitch',
    'Compare the particle-column view (top) with the pressure-vs-position graph (bottom) — see how compressions in one match peaks in the other',
    'Note the dB meter rises with amplitude squared, not amplitude itself — doubling amplitude raises intensity level noticeably more than doubling frequency',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Sound is a LONGITUDINAL mechanical wave: the particles of the medium oscillate back and forth ALONG the same direction the wave travels, alternately crowding together (a COMPRESSION, where pressure and density are momentarily higher than normal) and spreading apart (a RAREFACTION, where pressure and density are momentarily lower). The wave itself is really a travelling pattern of pressure excess and pressure deficit, which is why sound is often plotted as a pressure-vs-position graph rather than a simple up-down displacement curve.',
      title: 'Sound: a longitudinal pressure wave',
    ),
    ContentBlock.paragraph(
      'Because sound is a MECHANICAL wave, it needs a material medium (solid, liquid, or gas) whose particles can bump into their neighbours and pass the disturbance along. In a vacuum there are no particles to compress or rarefy, so sound simply cannot propagate — this is why astronauts on the Moon (essentially a vacuum) cannot hear each other directly and must use radio, which is an ELECTROMAGNETIC wave requiring no medium at all.',
      title: 'Why sound cannot travel through a vacuum',
    ),
    ContentBlock.formula('v_solid > v_liquid > v_gas', title: 'SPEED RANKING BY MEDIUM'),
    ContentBlock.paragraph(
      'Wave speed in a medium depends on how stiffly its particles resist being squeezed (elasticity) and how much inertia they carry (density): v = √(elastic modulus / density). Solids have far higher elastic moduli (they resist compression strongly) than gases, more than compensating for their higher density, so sound moves fastest in solids, then liquids, and slowest in gases like air.',
      title: 'What determines the speed',
    ),
    ContentBlock.formula('v_air ≈ 331 + 0.61·T  (T in °C, approx.)', title: 'SPEED OF SOUND IN AIR VS TEMPERATURE'),
    ContentBlock.paragraph(
      'Within a gas, the speed of sound also rises with TEMPERATURE, roughly linearly for everyday ranges: v ≈ 331 + 0.61T where T is in degrees Celsius. Warmer air molecules move faster on average, transmitting the pressure disturbance to neighbours more quickly — so sound genuinely travels a little faster on a hot day than a cold one.',
      title: 'Temperature dependence in air',
    ),
    ContentBlock.paragraph(
      'PITCH is the sensation corresponding to FREQUENCY — a higher frequency sounds like a higher note. LOUDNESS is the sensation corresponding to INTENSITY (and hence amplitude) — a larger amplitude sounds louder. QUALITY (or timbre) is what lets you tell a violin from a flute playing the same note at the same loudness — it comes from the different mix of overtones (harmonics) each instrument produces on top of the fundamental. These three are independent axes: you can raise pitch without changing loudness, and vice versa.',
      title: 'Loudness, pitch, and quality — three separate things',
    ),
    ContentBlock.formula('Intensity level β = 10 log₁₀(I/I₀) dB', title: 'DECIBEL (dB) SCALE'),
    ContentBlock.paragraph(
      'Because the ear can detect an enormous range of intensities (a factor of roughly 10¹² between the faintest audible sound and a painfully loud one), sound level is measured on a LOGARITHMIC decibel (dB) scale rather than linearly. I₀ = 10⁻¹² W/m² is the reference threshold of human hearing. Each 10 dB increase corresponds to the intensity multiplying by 10 — so a 70 dB sound (busy street) carries 10,000 times more intensity than a 30 dB sound (quiet room), even though it "sounds" only moderately louder to our compressed perception.',
      title: 'Why decibels are logarithmic',
    ),
    ContentBlock.realLife(
      'Musical instruments change pitch by changing string tension/length (guitar, violin) or the effective air-column length (flute, organ pipe) — tightening a string or shortening it raises frequency, exactly as fₙ = nv/2L predicts for a string or open pipe (see the Standing Waves lesson for the full harmonic-series derivation). A shorter, tighter string vibrates faster, giving a higher note.',
    ),
    ContentBlock.mistake(
      'Confusing loudness with pitch. Turning up the volume on a speaker increases amplitude/intensity (louder) but does NOT change the frequency (pitch stays the same note). Only changing the source\'s vibration rate changes pitch.',
    ),
    ContentBlock.mistake(
      'Forgetting that sound speed in AIR depends on temperature, and assuming 340 m/s is a universal constant. It is only an approximate value near room temperature; problems that give a temperature expect v = 331 + 0.61T substituted in.',
    ),
    ContentBlock.example(
      'Find the speed of sound in air at 30°C.\n\nv = 331 + 0.61T = 331 + 0.61(30) = 331 + 18.3 = 349.3 m/s.\n\nCompare to 0°C, where v = 331 m/s exactly — the 30° warmer air carries sound about 18 m/s faster.',
    ),
    ContentBlock.jeeTip(
      'For pipe-harmonics numericals, remember (without re-deriving): an OPEN pipe (both ends open) supports all harmonics, fₙ = nv/2L (n=1,2,3,…), just like a string fixed at both ends. A CLOSED pipe (one end closed) supports only ODD harmonics, fₙ = nv/4L (n=1,3,5,…) — so a closed pipe of the same length as an open pipe has a fundamental frequency exactly HALF that of the open pipe, and skips every even harmonic.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks conceptual dB questions: doubling intensity raises level by 10log₁₀2 ≈ 3 dB (NOT by a factor of 2 in dB), while a 10 dB rise means the intensity became 10× larger. Also remember: threshold of hearing = 0 dB (I₀ = 10⁻¹² W/m²), and typical conversation ≈ 60 dB.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Model sound as particles oscillating longitudinally',
      math: 's(x,t) = s₀ sin(kx − ωt)',
      note: 's = particle displacement along the direction of propagation, s₀ = displacement amplitude.',
    ),
    DerivationStep(
      title: 'Relate displacement to pressure variation',
      math: 'Δp(x,t) = Δp₀ cos(kx − ωt),   Δp₀ = (Bulk modulus)·k·s₀',
      note: 'Regions of maximum compression (high Δp) occur where the displacement gradient is steepest — a quarter-cycle out of phase with the displacement wave itself.',
    ),
    DerivationStep(
      title: 'Wave speed from the medium\'s elastic and inertial properties',
      math: 'v = √(B/ρ)   (fluids)     v = √(Y/ρ)   (solids, Young\'s modulus Y)',
      note: 'B = bulk modulus (resistance to compression), ρ = density. Solids have much larger elastic moduli than gases, dominating over any density difference.',
    ),
    DerivationStep(
      title: 'Speed of sound in an ideal gas (Newton-Laplace formula)',
      math: 'v = √(γP/ρ) = √(γRT/M)',
      note: 'γ = Cp/Cv, and using the ideal gas law shows v depends directly on √T — hence the linear-in-T approximation used for air.',
    ),
    DerivationStep(
      title: 'Linear approximation near everyday temperatures',
      math: 'v_air(T) ≈ 331 + 0.61T   (T in °C)',
      note: 'A linearised fit to √T over the everyday temperature range, accurate enough for exam-level numericals.',
    ),
  ],
  formulas: const [
    FormulaEntry('Speed in a solid', 'v = √(Y/ρ)', condition: 'Y = Young\'s modulus'),
    FormulaEntry('Speed in a fluid', 'v = √(B/ρ)', condition: 'B = bulk modulus'),
    FormulaEntry('Speed in a gas (Newton-Laplace)', 'v = √(γP/ρ) = √(γRT/M)'),
    FormulaEntry('Speed in air vs temperature', 'v ≈ 331 + 0.61T', condition: 'T in °C'),
    FormulaEntry('Intensity level', 'β = 10 log₁₀(I/I₀) dB', condition: 'I₀ = 10⁻¹² W/m²'),
    FormulaEntry('Open pipe / string harmonics', 'fₙ = nv/2L', condition: 'n = 1,2,3,… (see standing waves)'),
    FormulaEntry('Closed pipe harmonics', 'fₙ = nv/4L', condition: 'n = 1,3,5,… (odd only)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Sound waves in air are:',
      options: ['Transverse', 'Longitudinal', 'Electromagnetic', 'Torsional'],
      correctIndex: 1,
      solution: 'Sound is a longitudinal mechanical wave — particles oscillate parallel to the direction of propagation, forming compressions and rarefactions.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The speed of sound is generally greatest in:',
      options: ['Gases', 'Liquids', 'Solids', 'Vacuum'],
      correctIndex: 2,
      solution: 'v_solid > v_liquid > v_gas because solids have the highest elastic modulus relative to density among the three.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The speed of sound in air at 20°C is approximately:',
      options: ['331 m/s', '343.2 m/s', '300 m/s', '360 m/s'],
      correctIndex: 1,
      solution: 'v = 331 + 0.61(20) = 331 + 12.2 = 343.2 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Which property of a sound wave determines its LOUDNESS?',
      options: ['Frequency', 'Wavelength', 'Amplitude (intensity)', 'Speed'],
      correctIndex: 2,
      solution: 'Loudness corresponds to intensity, which depends on the square of the amplitude — larger amplitude means louder sound, independent of pitch.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If the intensity of a sound is increased 100 times, the increase in intensity level is:',
      options: ['10 dB', '20 dB', '100 dB', '2 dB'],
      correctIndex: 1,
      solution: 'Δβ = 10 log₁₀(100) = 10 × 2 = 20 dB.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Sound cannot travel through a vacuum because:',
      options: [
        'Vacuum absorbs all sound energy instantly',
        'There are no particles to be compressed and rarefied',
        'The speed of sound becomes infinite in vacuum',
        'Vacuum reflects all sound waves',
      ],
      correctIndex: 1,
      solution: 'Sound is a mechanical wave requiring a material medium; with no particles present, there is nothing to carry the compressions and rarefactions.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A closed organ pipe and an open organ pipe of the SAME length L produce fundamental frequencies f_closed and f_open. Their ratio f_closed : f_open is:',
      options: ['1:1', '1:2', '2:1', '1:4'],
      correctIndex: 1,
      solution: 'f_open = v/2L, f_closed = v/4L, so f_closed/f_open = (v/4L)/(v/2L) = 1/2. Ratio is 1:2 — the closed pipe\'s fundamental is half the open pipe\'s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Two sounds have intensities in the ratio 1000:1. The difference in their intensity levels is:',
      options: ['30 dB', '3 dB', '1000 dB', '10 dB'],
      correctIndex: 0,
      solution: 'Δβ = 10 log₁₀(1000) = 10 × 3 = 30 dB.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The timbre (quality) that lets you distinguish a violin from a flute playing the identical note at identical loudness is due to:',
      options: [
        'Different fundamental frequencies',
        'Different amplitudes',
        'Different mixtures of overtones (harmonics) superposed on the same fundamental',
        'Different speeds of sound in each instrument',
      ],
      correctIndex: 2,
      solution: 'Same note = same fundamental frequency, same loudness = same amplitude of the fundamental; the distinguishing factor is which harmonics are present and in what relative strength — the wave "shape."',
    ),
  ],
  revision: [
    'Sound is a longitudinal pressure wave: particles oscillate along the propagation direction, forming compressions and rarefactions.',
    'v_solid > v_liquid > v_gas — stiffer, more tightly-bonded media carry sound faster.',
    'In air, v ≈ 331 + 0.61T (T in °C) — sound travels faster in warmer air.',
    'Pitch ↔ frequency, loudness ↔ intensity/amplitude, quality (timbre) ↔ harmonic mixture — three independent properties.',
    'Intensity level β = 10 log₁₀(I/I₀) dB — a logarithmic scale; +10 dB means 10× the intensity.',
    'No medium, no sound: sound cannot propagate through vacuum, unlike light/radio (electromagnetic waves).',
    'Open pipe/string: fₙ = nv/2L (all harmonics). Closed pipe: fₙ = nv/4L (odd harmonics only) — see Standing Waves for the full derivation.',
  ],
  sandboxBuilder: (_) => const SoundWavesSandbox(),
);
