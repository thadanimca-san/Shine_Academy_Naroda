import '../../models/lesson.dart';
import '../../simulators/communication_systems_sandbox.dart';
import '../../theme/tokens.dart';

/// Communication Systems — modulation, AM basics, and wave propagation modes.
final Lesson communicationSystemsLesson = Lesson(
  topicId: 'communication-systems',
  title: 'Communication Systems',
  accentColor: Palette.chModern,
  bigQuestion:
      'Your voice, as sound, is a low-frequency signal — yet radio stations broadcast it using waves oscillating millions of times faster than your vocal cords ever could. Why not just transmit your voice signal directly through the air at its own natural frequency?',
  whyItMatters:
      'Every wireless technology you use daily — radio, TV, mobile phones, WiFi — works because of modulation, the core idea in this lesson. NEET and JEE test modulation index numericals, propagation-mode classification, and the AM/FM comparison regularly, and this topic conceptually completes the physics syllabus by connecting waves and electronics to real communication technology.',
  prediction: const PredictionPrompt(
    scenario:
        'Sound signals (the human voice) span roughly 20 Hz - 20 kHz. If you tried to transmit such a low-frequency signal directly through an antenna without any modulation, what practical problem would you run into?',
    options: [
      'The signal would travel too fast to be received',
      'The required antenna size would be impractically huge, since antenna length must be comparable to the wavelength',
      'The signal would automatically convert itself to light',
      'There is no problem; direct transmission works fine and modulation is unnecessary',
    ],
    correctIndex: 1,
    reveal:
        'An efficient antenna needs a size comparable to the wavelength of the signal it radiates. For a 20 kHz baseband signal, the wavelength is about 15 km — an obviously impossible antenna to build. In the lab, notice the carrier wave oscillates FAR faster than the message signal; only after modulation does the antenna need to handle just the (much shorter) carrier wavelength, which is practical to build.',
  ),
  experiments: [
    'Set modulation index m=0 and see the "modulated" wave collapse to a plain, unvarying carrier — no information is being carried',
    'Raise m from 0 toward 1 and watch the envelope (dotted outline) increasingly hug the shape of the message signal',
    'Push m above 1 and observe the envelope clip/distort — over-modulation, which garbles the recovered signal',
    'Increase the message frequency f_m and watch the bandwidth reading (2f_m) grow accordingly',
    'Increase the carrier frequency f_c (keeping the message the same) and note the envelope shape is unaffected — only the "fill" oscillation gets faster',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Every communication system, whatever the technology, shares the same basic building blocks. A TRANSMITTER converts the information (message) into a form suitable for sending — usually by modulating it onto a carrier wave. A CHANNEL (wire, optical fibre, or free space) carries the signal from transmitter to receiver, and inevitably introduces some NOISE (unwanted random disturbance) and attenuation (signal weakening) along the way. A RECEIVER at the far end extracts the original message back out of the received (noisy, weakened) signal.',
      title: 'Elements of a communication system',
    ),
    ContentBlock.bullets([
      'Transmitter: converts message into a transmittable signal (modulation)',
      'Channel: the medium carrying the signal (wire, fibre, or free space) — introduces noise and attenuation',
      'Receiver: recovers the original message from the received signal (demodulation)',
      'Noise: any unwanted, random signal that degrades the transmitted information',
    ]),
    ContentBlock.paragraph(
      'Baseband signals (like a raw voice or music signal, roughly 20 Hz-20 kHz) cannot be transmitted directly through free space for two big practical reasons: first, efficient antennas need a size comparable to the wavelength of the signal (λ=c/f), and low frequencies mean impractically enormous wavelengths and antennas; second, many different transmitters would all clash in the same low-frequency band with no way to separate them. MODULATION solves both: the baseband (message) signal is superimposed onto a high-frequency CARRIER wave, so it inherits the carrier\'s short wavelength (small antenna) and can be shifted to its own frequency slot (multiple stations without interference).',
      title: 'Why modulation is necessary',
    ),
    ContentBlock.formula('λ = c/f  ⟹  low f needs impractically large antenna', title: 'ANTENNA SIZE CONSTRAINT'),
    ContentBlock.paragraph(
      'In AMPLITUDE MODULATION (AM), the AMPLITUDE of the high-frequency carrier wave is varied in step with the message signal, while the carrier\'s frequency and phase stay constant. The result is a wave whose outer "envelope" traces the shape of the original message. The depth of this variation is captured by the modulation index.',
      title: 'Amplitude modulation (AM)',
    ),
    ContentBlock.formula('m = Aₘ / A_c', title: 'MODULATION INDEX (Aₘ = message amplitude, A_c = carrier amplitude)'),
    ContentBlock.bullets([
      'm < 1 (under-modulation): envelope follows the message faithfully, cleanly recoverable',
      'm = 1: maximum modulation depth without distortion — carrier amplitude swings from 0 to 2A_c',
      'm > 1 (over-modulation): the envelope clips/distorts, and the original message CANNOT be recovered cleanly at the receiver',
    ], title: 'Reading the modulation index'),
    ContentBlock.paragraph(
      'An AM signal, when analysed in frequency, is found to contain three components: the original carrier frequency f_c, plus two new "sideband" frequencies at f_c+f_m and f_c−f_m (where f_m is the message frequency). This means the total frequency range (bandwidth) occupied by an AM signal is twice the highest message frequency.',
      title: 'Bandwidth of an AM signal',
    ),
    ContentBlock.formula('Bandwidth = 2 f_m', title: 'AM BANDWIDTH'),
    ContentBlock.paragraph(
      'FREQUENCY MODULATION (FM) is an alternative scheme where instead of varying the carrier\'s amplitude, its FREQUENCY is varied in step with the message (amplitude stays constant). FM signals are much more resistant to noise, because most noise adds unwanted amplitude variations, which an FM receiver — tuned only to frequency changes — simply ignores. This is why FM radio sounds clearer than AM radio, especially near electrical interference, though FM needs a larger bandwidth than AM.',
      title: 'Frequency modulation (FM) — a noise-resistant alternative',
    ),
    ContentBlock.paragraph(
      'Once a signal leaves the transmitting antenna, it can reach the receiver by different propagation paths depending on its frequency. Choosing the right frequency band for a given application depends heavily on which propagation mode is available.',
      title: 'Modes of wave propagation',
    ),
    ContentBlock.bullets([
      'Ground wave propagation: signal travels along the Earth\'s surface, works best for LOW frequencies (up to ~2 MHz, e.g., AM radio); range limited by ground absorption',
      'Sky wave propagation: signal is reflected back to Earth by the ionosphere, works for frequencies roughly 2-30 MHz (short-wave radio); allows long-distance communication by bouncing off the ionosphere',
      'Space wave propagation: signal travels in a (nearly) straight line directly from transmitter to receiver (or via satellite), used for frequencies above ~30 MHz (FM radio, TV, mobile, satellite); limited by line-of-sight, so needs tall antennas or satellites for long range',
    ], title: 'Ground wave, sky wave, space wave — a high-yield table'),
    ContentBlock.realLife(
      'AM radio stations use ground/sky wave propagation at lower frequencies, giving them huge range (hundreds of km) but lower audio fidelity and susceptibility to noise. FM radio and TV use space wave (line-of-sight) propagation at higher frequencies, giving clearer sound/picture but shorter range, needing repeater towers. Mobile phones use space wave propagation via a dense network of cell towers, each covering a small area, with signals handed off from tower to tower as you move.',
    ),
    ContentBlock.mistake(
      'Confusing which parameter is varied in AM vs FM. In AM, amplitude varies and frequency stays constant. In FM, frequency varies and amplitude stays constant. Mixing these up is one of the most common mistakes on this topic.',
    ),
    ContentBlock.mistake(
      'Forgetting that AM bandwidth is 2f_m, not f_m. Students often forget the sidebands appear on BOTH sides of the carrier (f_c+f_m and f_c−f_m), doubling the required bandwidth compared to the message frequency alone.',
    ),
    ContentBlock.example(
      'A carrier wave of amplitude 10 V is amplitude modulated by a message signal of amplitude 4 V. Find the modulation index and describe whether the signal is properly modulated.\n\nm = Aₘ/A_c = 4/10 = 0.4.\n\nSince m = 0.4 < 1, this is a valid under-modulated signal that can be cleanly demodulated at the receiver.',
    ),
    ContentBlock.jeeTip(
      'For "maximum and minimum amplitude of the modulated wave" problems: A_max = A_c(1+m) and A_min = A_c(1−m). You can also back out m from measured amplitudes: m = (A_max − A_min)/(A_max + A_min) — a very common numerical shortcut.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks direct-recall questions on the propagation-mode frequency table (ground wave: low f, up to ~2 MHz; sky wave: ~2-30 MHz via ionospheric reflection; space wave: >30 MHz, line-of-sight) and the basic block diagram of a communication system (transmitter–channel–receiver, with noise entering at the channel).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write the carrier and message as simple sinusoids',
      math: 'c(t) = A_c sin(ω_c t),   m(t) = Aₘ sin(ω_m t)',
      note: 'ω_c ≫ ω_m: the carrier oscillates far faster than the message.',
    ),
    DerivationStep(
      title: 'In AM, let the carrier\'s amplitude vary with the message',
      math: 's(t) = [A_c + Aₘ sin(ω_m t)] sin(ω_c t)',
      note: 'The bracket is the instantaneous envelope amplitude, tracing the message shape.',
    ),
    DerivationStep(
      title: 'Introduce the modulation index',
      math: 's(t) = A_c[1 + m·sin(ω_m t)]·sin(ω_c t),   m = Aₘ/A_c',
    ),
    DerivationStep(
      title: 'Expand using a product-to-sum identity',
      math: 's(t) = A_c sin(ω_c t) + (mA_c/2)[cos((ω_c−ω_m)t) − cos((ω_c+ω_m)t)]',
      note: 'This reveals three frequency components: the carrier f_c, and two sidebands at f_c−f_m and f_c+f_m.',
    ),
    DerivationStep(
      title: 'Read off the bandwidth',
      math: 'Bandwidth = (f_c+f_m) − (f_c−f_m) = 2f_m',
      note: 'The AM signal occupies a band twice as wide as the highest message frequency.',
    ),
  ],
  formulas: const [
    FormulaEntry('Modulation index', 'm = Aₘ/A_c'),
    FormulaEntry('Max/min amplitude of AM wave', 'A_max = A_c(1+m),  A_min = A_c(1−m)'),
    FormulaEntry('Modulation index from amplitudes', 'm = (A_max−A_min)/(A_max+A_min)'),
    FormulaEntry('AM bandwidth', 'BW = 2f_m'),
    FormulaEntry('Wavelength-antenna relation', 'λ = c/f'),
    FormulaEntry('Ground wave range', 'up to ~2 MHz'),
    FormulaEntry('Sky wave range', '~2-30 MHz (ionospheric reflection)'),
    FormulaEntry('Space wave range', '>30 MHz (line-of-sight / satellite)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The three basic elements of any communication system are:',
      options: [
        'Transmitter, amplifier, speaker',
        'Transmitter, channel, receiver',
        'Antenna, battery, receiver',
        'Modulator, demodulator, noise',
      ],
      correctIndex: 1,
      solution: 'Every communication system consists of a transmitter (encodes the message), a channel (carries the signal, introducing noise), and a receiver (recovers the message).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Modulation is necessary mainly because:',
      options: [
        'Baseband signals travel too fast without it',
        'Direct transmission of low-frequency signals would need impractically large antennas',
        'It converts sound into light',
        'It is required by law',
      ],
      correctIndex: 1,
      solution: 'Efficient antennas need a size comparable to the signal wavelength; low-frequency baseband signals have wavelengths of kilometres, making direct transmission impractical. Superimposing them on a high-frequency carrier solves this.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A carrier of amplitude 20 V is modulated by a signal of amplitude 5 V. The modulation index is:',
      options: ['0.20', '0.25', '4', '0.5'],
      correctIndex: 1,
      solution: 'm = Aₘ/A_c = 5/20 = 0.25.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'An AM wave has A_max = 12 V and A_min = 4 V. The modulation index is:',
      options: ['0.5', '0.6', '0.33', '0.75'],
      correctIndex: 0,
      solution: 'm = (A_max−A_min)/(A_max+A_min) = (12−4)/(12+4) = 8/16 = 0.5.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'An AM signal carries a message of maximum frequency 5 kHz. Its bandwidth is:',
      options: ['5 kHz', '2.5 kHz', '10 kHz', '20 kHz'],
      correctIndex: 2,
      solution: 'AM bandwidth = 2f_m = 2 × 5 kHz = 10 kHz.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Compared to AM, FM (frequency modulation) is generally preferred for high-fidelity broadcast because:',
      options: [
        'FM needs less bandwidth than AM',
        'FM is more resistant to noise, since amplitude-based noise does not affect a frequency-encoded signal',
        'FM signals travel faster than AM signals',
        'FM does not require a carrier wave',
      ],
      correctIndex: 1,
      solution: 'Most noise adds unwanted amplitude fluctuations; since FM encodes information in frequency (not amplitude) variations, an FM receiver is far less affected by such noise, giving clearer reception.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Which propagation mode allows AM radio signals (below ~2 MHz) to travel long distances along the Earth\'s surface?',
      options: ['Sky wave propagation', 'Space wave propagation', 'Ground wave propagation', 'Satellite propagation'],
      correctIndex: 2,
      solution: 'Ground wave propagation, effective at low frequencies (up to ~2 MHz), lets the signal follow the Earth\'s curvature along the surface.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'FM/TV broadcasts (frequencies above ~30 MHz) mainly rely on which propagation mode, and why is their range limited?',
      options: [
        'Sky wave; limited because the ionosphere absorbs these frequencies',
        'Space wave; limited to roughly line-of-sight distance since these frequencies pass through the ionosphere without reflecting',
        'Ground wave; limited by ground conductivity',
        'All three modes equally, no real limitation',
      ],
      correctIndex: 1,
      solution: 'Above ~30 MHz, waves penetrate the ionosphere instead of reflecting off it, so they must travel via space wave (line-of-sight or satellite relay), limiting range to roughly the horizon distance unless towers/satellites are used.',
    ),
  ],
  revision: [
    'A communication system = transmitter + channel (with noise) + receiver.',
    'Modulation is needed because baseband signals would need impractically large antennas (λ=c/f) and would clash without frequency separation.',
    'AM: carrier amplitude varies with the message; modulation index m=Aₘ/A_c; m<1 clean, m>1 over-modulated/distorted.',
    'AM bandwidth = 2f_m (two sidebands at f_c±f_m around the carrier).',
    'FM: carrier frequency varies with the message; more noise-resistant than AM but needs more bandwidth.',
    'Ground wave (~≤2 MHz), sky wave (~2-30 MHz, ionosphere reflection), space wave (~>30 MHz, line-of-sight/satellite) — memorise the frequency ranges.',
    'Real life: AM radio uses ground/sky waves for long range; FM/TV/mobile use space waves for higher fidelity but shorter direct range.',
  ],
  sandboxBuilder: (_) => const CommunicationSystemsSandbox(),
);
