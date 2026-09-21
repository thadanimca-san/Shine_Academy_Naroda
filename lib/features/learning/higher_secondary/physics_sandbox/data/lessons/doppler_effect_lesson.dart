import '../../models/lesson.dart';
import '../../simulators/doppler_effect_sandbox.dart';
import '../../theme/tokens.dart';

/// Doppler Effect — why a siren's pitch drops the instant it passes you.
final Lesson dopplerEffectLesson = Lesson(
  topicId: 'doppler-effect',
  title: 'Doppler Effect',
  accentColor: Palette.chWaves,
  bigQuestion:
      'An ambulance races toward you, siren blaring at a steady pitch — but the moment it passes and starts moving away, the pitch suddenly seems to DROP, as if the driver changed the siren mid-drive. Nobody touched anything. What changed?',
  whyItMatters:
      'The Doppler effect is one of the most-tested "everyday physics" topics in both JEE and NEET, precisely because it is so tangible — everyone has heard a passing siren or horn. It also quietly underlies radar speed guns, weather radar, and (in a modified form) the redshift that reveals the universe is expanding, so it bridges classical mechanics all the way to astrophysics.',
  prediction: const PredictionPrompt(
    scenario:
        'A source emitting a steady 500 Hz tone moves TOWARD a stationary listener at 20 m/s (speed of sound = 340 m/s). Compared to 500 Hz, the listener hears a frequency that is:',
    options: [
      'Lower than 500 Hz',
      'Exactly 500 Hz (motion doesn\'t change frequency)',
      'Higher than 500 Hz',
      'It depends only on the listener\'s motion, not the source\'s',
    ],
    correctIndex: 2,
    reveal:
        'A source moving toward a stationary listener compresses the wavefronts ahead of it, shortening the effective wavelength and raising the apparent frequency: f\' = f·v/(v − vs) = 500×340/(340−20) ≈ 531 Hz. In the lab, push vₛ positive and watch the wavefront circles crowd together ahead of the source while the apparent-frequency meter climbs above 500 Hz.',
  ),
  experiments: [
    'Set vₛ = +30 m/s (source approaching) and watch wavefronts bunch up ahead of it; note f\' rises',
    'Flip vₛ to −30 m/s (source receding) and watch wavefronts spread out; note f\' falls below f',
    'Keep vₛ = 0 and instead move the observer (vₒ) toward the source; note f\' also rises, but by a different formula path',
    'Set both vₛ and vₒ positive (both approaching each other) and see the largest possible frequency shift',
    'Set vₛ = 0 and vₒ = 0 — confirm f\' = f exactly, no relative motion means no Doppler shift',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The Doppler effect is the apparent change in frequency of a wave, observed when there is RELATIVE motion between the source and the observer/listener. The source keeps emitting at its own fixed frequency f the whole time — what changes is how often wavefronts arrive at the listener, because the listener and source are getting closer together or farther apart while the wave travels between them.',
      title: 'What the Doppler effect actually is',
    ),
    ContentBlock.paragraph(
      'CASE 1 — Source moving toward a stationary observer: each successive wavefront is emitted from a position slightly closer to the observer than the last, so the wavefronts bunch up ahead of the source. The wavelength ahead shrinks, and since v = fλ with v fixed by the medium, the apparent frequency rises.\nCASE 2 — Source moving away: wavefronts stretch out behind it, wavelength grows, apparent frequency falls.',
      title: 'Source in motion (observer stationary)',
    ),
    ContentBlock.formula('f\' = f·v/(v ∓ vₛ)', title: 'SOURCE MOVING (− toward, + away from observer)'),
    ContentBlock.paragraph(
      'CASE 3 — Observer moving toward a stationary source: the observer physically sweeps into wavefronts faster than they would otherwise arrive, so more wavefronts reach the ear per second — apparent frequency rises.\nCASE 4 — Observer moving away: the observer is "running away" from wavefronts, fewer arrive per second, apparent frequency falls.',
      title: 'Observer in motion (source stationary)',
    ),
    ContentBlock.formula('f\' = f·(v ± vₒ)/v', title: 'OBSERVER MOVING (+ toward, − away from source)'),
    ContentBlock.paragraph(
      'When BOTH the source and observer move, the two effects combine into one general formula. The golden rule for signs: use the UPPER sign (+vₒ in numerator, −vₛ in denominator) whenever that motion brings source and observer CLOSER together (raises pitch), and the LOWER sign whenever that motion moves them FARTHER apart (lowers pitch). v is always the speed of sound in the medium, a fixed constant that never gets a sign flip.',
      title: 'The general (combined) Doppler formula',
    ),
    ContentBlock.formula('f\' = f·(v ± vₒ)/(v ∓ vₛ)', title: 'GENERAL DOPPLER FORMULA (SOUND)'),
    ContentBlock.bullets([
      'Numerator (v ± vₒ): use +vₒ if observer approaches source, −vₒ if observer recedes',
      'Denominator (v ∓ vₛ): use −vₛ if source approaches observer, +vₛ if source recedes',
      'If neither moves, or they move at the same velocity in the same direction (no closing speed), f\' = f',
      'The two cases are NOT symmetric in form — vₛ sits in the denominator, vₒ sits in the numerator — because it is the SOURCE\'s motion that physically compresses/stretches the wavelength, while the OBSERVER\'s motion changes only how fast they sweep through existing wavefronts',
    ]),
    ContentBlock.realLife(
      'An ambulance siren sounds noticeably higher-pitched as it approaches and drops the instant it passes — that drop is the switch from "source approaching" (denominator v−vs, higher f\') to "source receding" (denominator v+vs, lower f\'). Police and traffic radar guns bounce microwaves off a moving car and measure the Doppler-shifted return signal to compute the car\'s speed. Doctors use Doppler ultrasound to measure blood-flow speed the same way.',
    ),
    ContentBlock.realLife(
      'Light also shows a Doppler effect: light from galaxies moving away from us is shifted to longer (redder) wavelengths — "redshift" — and this is the key evidence that the universe is expanding. The light-Doppler formula differs slightly from the sound formula (it depends only on relative velocity, since light needs no medium, and requires relativistic corrections at high speed), so don\'t mix the two formulas — but the qualitative idea, "motion shifts the observed frequency," is the same.',
    ),
    ContentBlock.mistake(
      'Mixing up which velocity goes in the numerator vs the denominator. Remember: vₒ (observer) always sits with v in the NUMERATOR; vₛ (source) always sits with v in the DENOMINATOR. Swapping them is the single most common Doppler mistake in exams.',
    ),
    ContentBlock.mistake(
      'Forgetting the sign depends on the DIRECTION of motion relative to the line joining source and observer, not on some fixed rule of "source is always +". Always ask: is this motion closing the gap (pitch should rise) or opening it (pitch should fall), then pick the sign that achieves that.',
    ),
    ContentBlock.example(
      'A car horn emits 400 Hz. The car moves toward a stationary pedestrian at 34 m/s. Speed of sound = 340 m/s. Find the frequency heard.\n\nSource approaching → use v − vₛ in denominator.\nf\' = f·v/(v − vₛ) = 400 × 340/(340 − 34) = 400 × 340/306 ≈ 444.4 Hz.\n\nThe pedestrian hears a noticeably higher pitch than the horn\'s true 400 Hz.',
    ),
    ContentBlock.jeeTip(
      'For problems with a source moving in a circle or reflecting off a wall (like a wall acting as a stationary "observer" that re-emits the sound), treat the wall as a stationary observer to find the frequency it "receives," then treat the wall as a stationary source re-emitting that frequency to whoever hears the echo — apply the Doppler formula twice in sequence.',
    ),
    ContentBlock.neetNote(
      'NEET typically tests the simpler single-motion cases (source-only or observer-only) as direct numericals, plus the conceptual fact that the Doppler effect requires RELATIVE motion along the line joining source and observer — motion purely perpendicular (tangential) to that line produces no first-order Doppler shift.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Source moving toward stationary observer — set up wavefront spacing',
      math: 'True wavelength: λ = v/f\nIn time T = 1/f, source moves a distance vₛT toward the observer',
      note: 'Each new wavefront starts from a point closer to the observer than the previous one.',
    ),
    DerivationStep(
      title: 'Find the compressed wavelength ahead of the source',
      math: 'λ\' = λ − vₛT = (v/f) − (vₛ/f) = (v − vₛ)/f',
      note: 'The wavefronts are squeezed into a shorter length because the source chases its own emitted waves.',
    ),
    DerivationStep(
      title: 'Convert wavelength back to frequency using v = f\'λ\'',
      math: 'f\' = v/λ\' = v / [(v−vₛ)/f] = f·v/(v − vₛ)',
      note: 'This matches the "source approaching" case of the general formula.',
    ),
    DerivationStep(
      title: 'Observer moving toward stationary source — count wavefronts swept per second',
      math: 'Relative speed of wavefronts past the observer = v + vₒ (observer moving into them)',
      note: 'The wavelength λ itself is unchanged (source is stationary); only the rate of encounter changes.',
    ),
    DerivationStep(
      title: 'Frequency heard = relative speed ÷ (unchanged) wavelength',
      math: 'f\' = (v + vₒ)/λ = (v + vₒ)·f/v = f·(v + vₒ)/v',
      note: 'This matches the "observer approaching" case.',
    ),
    DerivationStep(
      title: 'Combine both effects for the general case',
      math: 'f\' = f·(v ± vₒ)/(v ∓ vₛ)',
      note: 'Superposing both mechanisms gives the full formula, with signs chosen by whether each motion closes or opens the gap.',
    ),
  ],
  formulas: const [
    FormulaEntry('General Doppler formula (sound)', 'f\' = f·(v ± vₒ)/(v ∓ vₛ)'),
    FormulaEntry('Source approaching, observer at rest', 'f\' = f·v/(v − vₛ)'),
    FormulaEntry('Source receding, observer at rest', 'f\' = f·v/(v + vₛ)'),
    FormulaEntry('Observer approaching, source at rest', 'f\' = f·(v + vₒ)/v'),
    FormulaEntry('Observer receding, source at rest', 'f\' = f·(v − vₒ)/v'),
    FormulaEntry('Speed of sound in air (approx, 20°C)', 'v ≈ 340 m/s'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A source moves toward a stationary observer. The observer hears a frequency that is:',
      options: ['Lower than the source frequency', 'Higher than the source frequency', 'Exactly equal', 'Zero'],
      correctIndex: 1,
      solution: 'Approaching source compresses wavefronts ahead of it, raising the apparent frequency: f\' = fv/(v−vₛ) > f.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The Doppler effect requires:',
      options: [
        'The source and observer to be at rest',
        'Relative motion between source and observer (along the line joining them)',
        'The medium to be a vacuum',
        'The frequency to exceed 20,000 Hz',
      ],
      correctIndex: 1,
      solution: 'Without relative motion along the line of sight, there is no compression or stretching of wavefronts, hence no frequency shift.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A train sounds a horn of frequency 480 Hz while approaching a stationary platform at 20 m/s. (v = 340 m/s) The frequency heard on the platform is:',
      options: ['452 Hz', '510 Hz', '480 Hz', '400 Hz'],
      correctIndex: 1,
      solution: 'f\' = f·v/(v−vₛ) = 480×340/(340−20) = 480×340/320 = 510 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The same train (480 Hz horn, 20 m/s) has now passed the platform and moves away. The frequency heard is:',
      options: ['452 Hz', '509 Hz', '480 Hz', '520 Hz'],
      correctIndex: 0,
      solution: 'Receding source: f\' = f·v/(v+vₛ) = 480×340/(340+20) = 480×340/360 ≈ 453.3 Hz (≈452 Hz).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A stationary source emits 340 Hz. An observer moves toward it at 34 m/s (v=340 m/s). The frequency heard is:',
      options: ['306 Hz', '374 Hz', '340 Hz', '400 Hz'],
      correctIndex: 1,
      solution: 'Observer approaching: f\' = f(v+vₒ)/v = 340×(340+34)/340 = 374 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A source (400 Hz) moves toward an observer at 20 m/s, while the observer simultaneously moves toward the source at 10 m/s. (v=340 m/s) The apparent frequency is:',
      options: ['422 Hz', '400 Hz', '437.5 Hz', '378 Hz'],
      correctIndex: 2,
      solution:
          'Both motions close the gap: use +vₒ in numerator, −vₛ in denominator.\nf\' = f(v+vₒ)/(v−vₛ) = 400×(340+10)/(340−20) = 400×350/320 = 437.5 Hz.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A source emitting 500 Hz recedes from a stationary observer at 34 m/s while the observer also recedes from the source (moving away) at 17 m/s. (v=340 m/s) The apparent frequency is:',
      options: ['500 Hz', '431.8 Hz', '460.6 Hz', '539.5 Hz'],
      correctIndex: 1,
      solution:
          'Both motions open the gap: use −vₒ in numerator, +vₛ in denominator.\nf\' = f(v−vₒ)/(v+vₛ) = 500×(340−17)/(340+34) = 500×323/374 ≈ 431.8 Hz — lower than 500 Hz, as expected since both motions increase the separation.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A common mistake in Doppler problems is:',
      options: [
        'Using v for the speed of sound in the medium',
        'Placing vₛ in the denominator and vₒ in the numerator',
        'Placing vₒ in the denominator and vₛ in the numerator',
        'Choosing signs based on whether motion opens or closes the gap',
      ],
      correctIndex: 2,
      solution: 'The correct formula always has vₒ (observer speed) in the numerator with v, and vₛ (source speed) in the denominator with v. Swapping these is the classic error.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Redshift of light from a distant galaxy indicates the galaxy is:',
      options: ['Moving toward Earth', 'Moving away from Earth', 'Stationary relative to Earth', 'Getting hotter'],
      correctIndex: 1,
      solution: 'Redshift means the observed wavelength is stretched (longer) compared to emitted — analogous to a receding source lowering apparent frequency, indicating the galaxy is moving away from us.',
    ),
  ],
  revision: [
    'Doppler effect: apparent frequency shifts due to relative motion between source and observer.',
    'General formula: f\' = f(v ± vₒ)/(v ∓ vₛ) — vₒ always in numerator, vₛ always in denominator.',
    'Motion that CLOSES the gap raises f\'; motion that OPENS the gap lowers f\'.',
    'Source approaching: f\' = fv/(v−vₛ). Source receding: f\' = fv/(v+vₛ).',
    'Observer approaching: f\' = f(v+vₒ)/v. Observer receding: f\' = f(v−vₒ)/v.',
    'Real examples: ambulance siren pitch drop, radar speed guns, Doppler ultrasound, astronomical redshift/blueshift.',
    'Light Doppler is analogous but not identical to sound Doppler — no medium needed, relativistic corrections apply.',
  ],
  sandboxBuilder: (_) => const DopplerEffectSandbox(),
);
