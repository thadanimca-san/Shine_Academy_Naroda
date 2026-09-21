import '../../models/lesson.dart';
import '../../simulators/wave_basics_sim.dart';
import '../../theme/tokens.dart';

/// Wave Motion Basics — how v = fλ links speed, frequency and wavelength.
final Lesson waveBasicsLesson = Lesson(
  topicId: 'wave-basics',
  title: 'Wave Motion Basics',
  accentColor: Palette.chWaves,
  bigQuestion:
      'Shake one end of a rope and a wave pulse races down its length — but if you tie a ribbon to the middle of the rope and watch it, the ribbon just bobs up and down, going nowhere. The wave clearly travels, so what exactly is moving?',
  whyItMatters:
      'Waves carry energy without carrying matter — this single idea underlies sound, light, radio, seismic waves, and quantum mechanics itself. The relation v = fλ appears in nearly every wave problem across NEET and JEE, from string vibrations to Doppler shift to optics. Get comfortable separating "what the wave does" from "what the medium\'s particles do" here, and every later wave topic becomes an application of the same idea.',
  prediction: const PredictionPrompt(
    scenario:
        'A wave travels along a stretched string at speed v. If you shake your hand FASTER (higher frequency) while keeping the string\'s tension and mass unchanged, what happens to the wave speed v?',
    options: [
      'v increases — faster shaking means a faster wave',
      'v decreases — higher frequency means smaller, slower waves',
      'v stays exactly the same — only the wavelength changes',
      'v doubles for every doubling of frequency',
    ],
    correctIndex: 2,
    reveal:
        'Wave speed on a string is a property of the MEDIUM (v = √(T/μ), tension and mass per length) — not of how you shake it. Shaking faster only shortens the wavelength (v = fλ, so if v is fixed, λ must shrink as f grows). In the lab, crank up the frequency slider and watch the wave speed readout stay locked while the wavelength visibly compresses.',
  ),
  experiments: [
    'Increase frequency and observe wavelength shrink while wave speed stays constant',
    'Increase the string tension and watch wave speed increase (v = √(T/μ))',
    'Switch to a heavier string (larger μ) and watch wave speed decrease',
    'Track a single colored particle on the string — it only moves up and down, never sideways',
    'Compare a transverse wave (string) against a longitudinal wave (compression pulse) side by side',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A mechanical wave is a disturbance that transports ENERGY through a medium without transporting the medium\'s particles from one place to another. Each particle of the medium oscillates about its own fixed equilibrium position; it is the pattern of disturbance — not the particles themselves — that travels forward. This is why the ribbon tied to the rope just bobs up and down while the pulse itself races past it.',
      title: 'What actually travels in a wave',
    ),
    ContentBlock.bullets([
      'Transverse wave: particles oscillate PERPENDICULAR to the direction of wave travel (e.g. string, light, water surface)',
      'Longitudinal wave: particles oscillate PARALLEL to the direction of wave travel, creating compressions and rarefactions (e.g. sound in air, a slinky pushed and pulled)',
    ], title: 'Transverse vs longitudinal'),
    ContentBlock.formula('y(x,t) = A sin(kx − ωt)', title: 'THE TRAVELLING WAVE EQUATION'),
    ContentBlock.bullets([
      'A = amplitude (maximum particle displacement)',
      'k = 2π/λ, the wave number (spatial analogue of ω)',
      'ω = 2π/T = 2πf, the angular frequency',
      'The minus sign (kx − ωt) means the wave moves in the +x direction; a plus sign (kx + ωt) means −x direction',
    ]),
    ContentBlock.formula('v = fλ', title: 'WAVE SPEED — FREQUENCY — WAVELENGTH'),
    ContentBlock.paragraph(
      'v = fλ is not a law of physics so much as a definition: in one period T, the wave advances exactly one wavelength λ, so speed = distance/time = λ/T = fλ. What makes v = fλ powerful is that v is usually fixed by the medium, so once you change f (by shaking faster, say), λ is forced to change to compensate, and vice versa.',
      title: 'Why v = fλ is really just bookkeeping',
    ),
    ContentBlock.formula('v = √(T/μ)', title: 'SPEED OF A TRANSVERSE WAVE ON A STRING'),
    ContentBlock.paragraph(
      'For a wave on a stretched string, the restoring force comes from tension T, and the inertia resisting that restoring force comes from the mass per unit length μ = mass/length. More tension means a stiffer, faster-responding string (higher v); more mass per length means more inertia to overcome (lower v). This is exactly analogous to how a stiffer spring (larger k) gives a shorter SHM period while more mass gives a longer one.',
      title: 'Why tension and mass control string wave speed',
    ),
    ContentBlock.realLife(
      'Guitar and violin strings use exactly v = √(T/μ): tightening a string (increasing T) raises the wave speed and hence the pitch, while thicker strings (larger μ) sound lower for the same tension — that\'s why bass strings are thick and treble strings are thin. Tuning a guitar is literally adjusting T to control v, and hence frequency, for a fixed string length.',
    ),
    ContentBlock.mistake(
      'Confusing wave speed v (how fast the disturbance pattern travels) with particle speed (how fast an individual bit of the medium is moving up and down). Particle speed varies through the cycle (zero at crests/troughs, maximum at the midline, like SHM) while wave speed v is constant for a given medium. These are DIFFERENT quantities with different formulas.',
    ),
    ContentBlock.mistake(
      'Believing that increasing frequency changes wave speed. In a fixed, unchanged medium, v is constant — changing f always changes λ instead (since v = fλ is fixed). Speed only changes if the medium itself changes (different tension, different density, different material).',
    ),
    ContentBlock.example(
      'A string of mass per length μ = 0.02 kg/m is under tension 50 N. A wave of frequency 100 Hz travels along it. Find the wave speed and wavelength.\n\nv = √(T/μ) = √(50/0.02) = √2500 = 50 m/s.\nλ = v/f = 50/100 = 0.5 m.',
    ),
    ContentBlock.jeeTip(
      'When a problem changes tension or mass, first recompute v = √(T/μ), THEN use v = fλ to find the new wavelength (frequency is usually set by the source and stays fixed as the wave crosses into a new medium — it\'s v and λ that adjust). This source-fixed-frequency rule is exactly analogous to light crossing from air into glass.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests direction-of-travel sign reading: y = A sin(ωt − kx) travels in +x direction, y = A sin(ωt + kx) travels in −x direction. Also remember the particle velocity formula v_particle = ∂y/∂t = −Aω cos(kx−ωt), whose maximum magnitude is Aω — completely different from and generally much smaller than the wave speed v = ω/k.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Isolate a small element of string under tension',
      math: 'Element of length dx, mass dm = μ·dx',
      note: 'Tension T pulls at both ends; curvature of the displaced string creates a net transverse restoring force.',
    ),
    DerivationStep(
      title: 'Write the net transverse force from curvature',
      math: 'F_net = T·(∂²y/∂x²)·dx',
      note: 'For small displacements, the transverse component of tension depends on the string\'s curvature.',
    ),
    DerivationStep(
      title: 'Apply Newton\'s second law to the element',
      math: 'μ·dx·(∂²y/∂t²) = T·(∂²y/∂x²)·dx',
    ),
    DerivationStep(
      title: 'Simplify to the wave equation',
      math: '∂²y/∂t² = (T/μ)·(∂²y/∂x²)',
      note: 'This has the standard wave-equation form ∂²y/∂t² = v²·∂²y/∂x².',
    ),
    DerivationStep(
      title: 'Match coefficients to identify wave speed',
      math: 'v² = T/μ  →  v = √(T/μ)',
      note: 'Tension supplies the restoring force; mass per length supplies the inertia — just like k and m in SHM.',
    ),
    DerivationStep(
      title: 'Connect to frequency and wavelength',
      math: 'In one period T, the wave advances one wavelength λ  →  v = λ/T = fλ',
    ),
  ],
  formulas: const [
    FormulaEntry('Wave speed relation', 'v = fλ'),
    FormulaEntry('Travelling wave', 'y(x,t) = A sin(kx − ωt)'),
    FormulaEntry('Wave number', 'k = 2π/λ'),
    FormulaEntry('Angular frequency', 'ω = 2π/T = 2πf'),
    FormulaEntry('Speed on a string', 'v = √(T/μ)', condition: 'T = tension, μ = mass/length'),
    FormulaEntry('Particle velocity', 'v_particle = ∂y/∂t', condition: 'max magnitude = Aω'),
    FormulaEntry('Particle acceleration', 'a_particle = ∂²y/∂t²'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In a transverse wave, the particles of the medium move:',
      options: ['Parallel to the wave direction', 'Perpendicular to the wave direction', 'In circles', 'They do not move at all'],
      correctIndex: 1,
      solution: 'By definition, transverse waves have particle oscillation perpendicular to the direction of wave propagation.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A wave has frequency 50 Hz and wavelength 4 m. Its speed is:',
      options: ['12.5 m/s', '200 m/s', '54 m/s', '0.08 m/s'],
      correctIndex: 1,
      solution: 'v = fλ = 50 × 4 = 200 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Sound waves in air are an example of:',
      options: ['Transverse waves', 'Longitudinal waves', 'Electromagnetic waves', 'Standing waves only'],
      correctIndex: 1,
      solution: 'Sound propagates via compressions and rarefactions — particle motion is parallel to propagation, so it is longitudinal.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If the tension in a stretched string is quadrupled while mass per unit length stays the same, the wave speed becomes:',
      options: ['2 times', '4 times', 'Half', 'Unchanged'],
      correctIndex: 0,
      solution: 'v = √(T/μ) ∝ √T. Quadrupling T multiplies v by √4 = 2.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A source vibrates at a fixed frequency f, sending a wave onto a string. If the string\'s tension is increased, the wavelength:',
      options: ['Increases', 'Decreases', 'Stays the same', 'Becomes zero'],
      correctIndex: 0,
      solution: 'Higher tension raises v = √(T/μ). Since f (source-driven) is fixed, λ = v/f must increase to match.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A wave is described by y = 0.02 sin(4x − 200t) (SI units). Its speed is:',
      options: ['50 m/s', '200 m/s', '4 m/s', '800 m/s'],
      correctIndex: 0,
      solution: 'Comparing to y = A sin(kx−ωt): k = 4, ω = 200. v = ω/k = 200/4 = 50 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'For the wave y = 0.02 sin(4x − 200t), the maximum particle speed is:',
      options: ['4 m/s', '200 m/s', '0.02 m/s', '8 m/s'],
      correctIndex: 0,
      solution: 'v_particle,max = Aω = 0.02 × 200 = 4 m/s. Note this is very different from the wave speed of 50 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A string of mass 0.4 kg and length 4 m is stretched to tension 100 N. The speed of a transverse wave on it is:',
      options: ['10 m/s', '31.6 m/s', '100 m/s', '250 m/s'],
      correctIndex: 1,
      solution: 'μ = m/L = 0.4/4 = 0.1 kg/m. v = √(T/μ) = √(100/0.1) = √1000 ≈ 31.6 m/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Two strings of the same material and length, but with radii in ratio 1:2, are stretched under the same tension. The ratio of wave speeds (thin : thick) is:',
      options: ['1:1', '2:1', '1:2', '4:1'],
      correctIndex: 1,
      solution:
          'For same material, μ ∝ cross-section area ∝ r². v ∝ 1/√μ ∝ 1/r. Ratio v₁:v₂ = r₂:r₁ = 2:1.',
    ),
  ],
  revision: [
    'A wave transports energy, not matter — each particle oscillates about a fixed point.',
    'Transverse: particle motion ⊥ to propagation. Longitudinal: particle motion ∥ to propagation.',
    'v = fλ links speed, frequency and wavelength — v is fixed by the medium, so changing f changes λ.',
    'On a string, v = √(T/μ) — more tension speeds the wave up, more mass per length slows it down.',
    'Wave speed and particle speed are different quantities; don\'t confuse v = ω/k with v_particle,max = Aω.',
    'y = A sin(kx − ωt) travels in +x; y = A sin(kx + ωt) travels in −x.',
  ],
  sandboxBuilder: (_) => const WaveBasicsSimulator(),
);
