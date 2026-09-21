import '../../models/lesson.dart';
import '../../simulators/damped_forced_sandbox.dart';
import '../../theme/tokens.dart';

/// Damping & Resonance — why real oscillations die out, and why they can also explode.
final Lesson dampedForcedLesson = Lesson(
  topicId: 'damped-forced',
  title: 'Damping & Resonance',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Soldiers marching in perfect step across a bridge are ordered to break stride before crossing. A wine glass shatters when a singer hits exactly the right note. A giant suspension bridge once twisted itself apart in steady wind. What single idea connects all three?',
  whyItMatters:
      'Every real oscillator — a pendulum, a car\'s suspension, a building in an earthquake, a radio tuner — eventually loses energy to friction (damping), and every oscillator can be driven by an outside push at just the right frequency to build up a huge response (resonance). JEE and NEET test both halves of this same picture: the qualitative decay regimes (underdamped/critical/overdamped) and the quantitative resonance condition ω_driving ≈ ω_natural. Engineers spend entire careers walking the line between using resonance (radios, MRI machines) and preventing it (bridges, buildings).',
  prediction: const PredictionPrompt(
    scenario:
        'A mass on a spring is pushed by a small periodic driving force. As you slowly increase the DRIVING frequency from very low to very high, passing through the system\'s own natural frequency ω₀ along the way, what happens to the oscillation amplitude?',
    options: [
      'It stays constant throughout — driving frequency doesn\'t affect amplitude',
      'It decreases steadily as driving frequency increases',
      'It rises to a sharp peak right around ω_driving ≈ ω₀, then falls off again',
      'It oscillates unpredictably with no clear pattern',
    ],
    correctIndex: 2,
    reveal:
        'This is resonance: when the driving frequency matches the system\'s own natural frequency, the driving force adds energy in sync with the oscillation on every single cycle, building the amplitude up to a sharp peak — limited only by damping. In the lab, switch to "Driven / resonance" mode and slide the driving frequency toward ω₀; watch the amplitude readout spike sharply, then fall away again on either side. Raise the damping and watch that same peak flatten and broaden — damping is the only thing standing between resonance and a runaway amplitude.',
  ),
  experiments: [
    'In "Free damped" mode, raise the damping slider and watch the oscillation die out faster, hugging the amber decay envelope more tightly',
    'Push damping to its maximum and see the mass barely complete one swing before settling — approaching the overdamped regime',
    'Switch to "Driven / resonance" and slide the driving frequency slowly through ω₀ — watch the amplitude spike sharply near resonance',
    'At resonance, increase damping and watch the sharp peak flatten into a broad, low hump — damping controls how dangerous resonance can get',
    'Change the spring constant k or mass m and see the natural frequency ω₀ = √(k/m) — and hence the resonance peak position — shift accordingly',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A real oscillator (a swinging pendulum, a mass on a spring, a plucked guitar string) never keeps oscillating forever with the same amplitude — friction, air resistance and internal resistance continuously drain its mechanical energy away as heat. This gradual amplitude loss is called damping.',
      title: 'Why real oscillators always lose energy',
    ),
    ContentBlock.formula('m(d²x/dt²) + b(dx/dt) + kx = 0    (damped oscillator equation)', title: 'DAMPED OSCILLATOR EQUATION'),
    ContentBlock.bullets([
      'm = mass, k = spring constant, b = damping coefficient (resistance per unit velocity)',
      'The bx-dot term represents a resistive force proportional to velocity — like air drag or viscous friction',
      'Larger b means the system loses energy faster per oscillation',
    ]),
    ContentBlock.paragraph(
      'Depending on how large the damping is compared to the natural stiffness/mass, three qualitatively different behaviours emerge. UNDERDAMPED: the system still oscillates, but with an amplitude that decays exponentially inside an envelope ±Ae^(−bt/2m) — this is what most real, lightly-damped systems (a swinging pendulum in air, a plucked string) look like. CRITICALLY DAMPED: the system returns to equilibrium in the shortest possible time WITHOUT oscillating at all — this is the ideal design target for shock absorbers and door closers. OVERDAMPED: the system returns to equilibrium slowly, again without oscillating, but more sluggishly than the critical case because the damping is now "too strong."',
      title: 'Three damping regimes',
    ),
    ContentBlock.formula('x(t) = A e^(−bt/2m) cos(ω_d t + φ)    (underdamped case)', title: 'UNDERDAMPED OSCILLATION'),
    ContentBlock.realLife(
      'Car shock absorbers are deliberately engineered close to critical damping: too little damping (underdamped) and the car keeps bouncing after every bump; too much (overdamped) and the suspension feels stiff and slow to settle after a bump, transmitting more jolt to the passengers. Critical damping gives the fastest possible return to a smooth ride with no bounce.',
    ),
    ContentBlock.paragraph(
      'When an external periodic force continuously pushes an oscillator, the system is said to undergo FORCED oscillation. After an initial transient, it settles into a steady-state oscillation at the SAME frequency as the driving force — but with an amplitude that depends sharply on how close the driving frequency is to the system\'s own natural frequency ω₀ = √(k/m).',
      title: 'Forced oscillation',
    ),
    ContentBlock.formula('A(ω) = F₀ / √[(k − mω²)² + (bω)²]    (steady-state amplitude vs driving frequency ω)', title: 'FORCED OSCILLATION AMPLITUDE'),
    ContentBlock.paragraph(
      'RESONANCE occurs when the driving frequency ω is close to the natural frequency ω₀: the denominator above becomes small, so the amplitude becomes large — in the ideal, undamped limit it would grow without bound. Real systems always have SOME damping, which is exactly what keeps the resonance peak finite rather than infinite; less damping gives a taller, narrower resonance peak, while more damping gives a shorter, broader one.',
      title: 'Resonance: when driving frequency matches natural frequency',
    ),
    ContentBlock.realLife(
      'The Tacoma Narrows Bridge (1940) famously twisted itself apart when wind-induced oscillations locked into resonance with one of the bridge\'s own natural torsional modes, building up an amplitude large enough to tear the structure apart — a textbook (if dramatically oversimplified in some retellings) resonance disaster. A trained singer can shatter a wine glass by singing exactly at the glass\'s own natural frequency, driving its walls to oscillate with enough amplitude to fracture. Soldiers are ordered to break step crossing a bridge specifically to avoid accidentally driving the bridge at its natural frequency with their rhythmic footfalls. MRI machines and microwave ovens both deliberately exploit resonance (of nuclear spins, or of water molecules) to work at all.',
    ),
    ContentBlock.mistake(
      'Believing damping is always undesirable. In shock absorbers, door closers, and vibration-control systems, damping (ideally near-critical) is the DESIGN GOAL — it is only "bad" when you specifically want an oscillation to persist, like in a clock pendulum or a musical instrument.',
    ),
    ContentBlock.mistake(
      'Thinking resonance means "the driving force and the natural frequency must be exactly equal, or nothing happens." In reality, the amplitude curve is a smooth, continuous peak — amplitude is elevated over a RANGE of frequencies near ω₀ (a range that narrows as damping decreases), not a single infinitely-sharp point.',
    ),
    ContentBlock.example(
      'A mass of 0.5 kg on a spring of constant k = 50 N/m has a damping coefficient b = 2 kg/s. Find (a) the natural (undamped) angular frequency, and (b) the exponential decay rate of the amplitude envelope.\n\n(a) ω₀ = √(k/m) = √(50/0.5) = √100 = 10 rad/s.\n(b) Decay rate = b/(2m) = 2/(2×0.5) = 2 s⁻¹, so the envelope is Ae^(−2t) — the amplitude falls to about 37% of its starting value (1/e) after 0.5 s.',
    ),
    ContentBlock.jeeTip(
      'For quick qualitative questions, remember the amplitude-decay envelope ±Ae^(−bt/2m) is what actually shrinks — the oscillation FREQUENCY inside that envelope, ω_d = √(ω₀² − (b/2m)²), is always slightly LESS than the undamped natural frequency ω₀ (light damping barely changes it, but the shift is always in the direction of a slightly longer period).',
    ),
    ContentBlock.neetNote(
      'NEET typically asks conceptual, real-life-example questions: identify the Tacoma Narrows bridge / wine glass / soldiers-breaking-step as resonance examples, identify shock absorbers as (near-)critical damping, and recall that damping always removes mechanical energy from an oscillating system (converted to heat via the resistive/frictional force).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write Newton\'s second law for a damped spring-mass system',
      math: 'm(d²x/dt²) = −kx − b(dx/dt)',
      note: 'Restoring force −kx from the spring, resistive (damping) force −b(dx/dt) proportional to velocity, opposing motion.',
    ),
    DerivationStep(
      title: 'Rearrange into standard form',
      math: 'm(d²x/dt²) + b(dx/dt) + kx = 0',
    ),
    DerivationStep(
      title: 'Try a decaying-oscillation solution (underdamped case)',
      math: 'x(t) = A e^(−bt/2m) cos(ω_d t + φ)',
      note: 'This form correctly makes the amplitude Ae^(−bt/2m) shrink exponentially while the cosine keeps oscillating.',
    ),
    DerivationStep(
      title: 'Substitute back to find the damped angular frequency',
      math: 'ω_d = √(ω₀² − (b/2m)²),   where ω₀² = k/m',
      note: 'This is real (oscillation persists) only when (b/2m)² < ω₀² — the underdamped condition. When (b/2m)² ≥ ω₀², the system is critically damped or overdamped and no longer oscillates.',
    ),
    DerivationStep(
      title: 'Add a periodic driving force to get the forced-oscillation amplitude',
      math: 'm(d²x/dt²) + b(dx/dt) + kx = F₀cos(ωt)  ⟹  A(ω) = F₀/√[(k−mω²)² + (bω)²]',
      note: 'The denominator is smallest (amplitude largest) when mω² ≈ k, i.e. ω ≈ ω₀ — the resonance condition.',
    ),
  ],
  formulas: const [
    FormulaEntry('Damped oscillator equation', 'm(d²x/dt²) + b(dx/dt) + kx = 0'),
    FormulaEntry('Underdamped displacement', 'x(t) = A e^(−bt/2m) cos(ω_d t + φ)'),
    FormulaEntry('Damped angular frequency', 'ω_d = √(ω₀² − (b/2m)²)'),
    FormulaEntry('Natural (undamped) frequency', 'ω₀ = √(k/m)'),
    FormulaEntry('Forced oscillation steady amplitude', 'A(ω) = F₀ / √[(k−mω²)² + (bω)²]'),
    FormulaEntry('Resonance condition', 'ω_driving ≈ ω₀  (amplitude maximised, limited by damping)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Real oscillators eventually stop oscillating because of:',
      options: ['Resonance', 'Damping (energy loss to friction/drag)', 'Increasing amplitude', 'Constructive interference'],
      correctIndex: 1,
      solution: 'Damping forces (friction, air drag, viscosity) continuously remove mechanical energy from the oscillator, converting it to heat, so the amplitude decays over time.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Resonance occurs when:',
      options: [
        'The damping coefficient is zero',
        'The driving frequency equals (or is very close to) the natural frequency of the system',
        'The amplitude of oscillation is zero',
        'The mass of the oscillator is very large',
      ],
      correctIndex: 1,
      solution: 'Resonance is the sharp buildup of amplitude when the driving frequency ω matches the system\'s own natural frequency ω₀, since energy is then added in sync with the oscillation every cycle.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A shock absorber in a car is designed to be close to:',
      options: ['Undamped (zero damping)', 'Underdamped', 'Critically damped', 'Resonant'],
      correctIndex: 2,
      solution: 'Critical damping returns the suspension to equilibrium in the shortest time without any oscillation (bouncing), giving the smoothest, most controlled ride after a bump.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The famous collapse of the Tacoma Narrows Bridge is most closely explained by:',
      options: ['Excess damping', 'Resonance between wind-induced oscillation and a natural mode of the bridge', 'Simple material fatigue unrelated to oscillation', 'Overdamping of the bridge structure'],
      correctIndex: 1,
      solution: 'Wind-driven oscillations built up to a large amplitude because they matched (or closely drove) one of the bridge\'s own natural frequencies — a resonance phenomenon, made worse by insufficient damping in that mode.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A mass-spring oscillator has m = 2 kg, k = 8 N/m and damping b = 4 kg/s. Its natural (undamped) angular frequency ω₀ is:',
      options: ['1 rad/s', '2 rad/s', '4 rad/s', '8 rad/s'],
      correctIndex: 1,
      solution: 'ω₀ = √(k/m) = √(8/2) = √4 = 2 rad/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'For the same oscillator (m=2 kg, k=8 N/m, b=4 kg/s), the exponential decay rate of the amplitude envelope (b/2m) is:',
      options: ['0.5 s⁻¹', '1 s⁻¹', '2 s⁻¹', '4 s⁻¹'],
      correctIndex: 1,
      solution: 'Decay rate = b/(2m) = 4/(2×2) = 1 s⁻¹, so the envelope is Ae^(−t).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Soldiers marching in step are told to break stride crossing a bridge because:',
      options: [
        'Marching in step makes the bridge heavier',
        'Their rhythmic footfalls could match the bridge\'s natural frequency, driving a resonant, dangerously large oscillation',
        'It slows down the crossing for safety inspection',
        'It reduces the total force applied to the bridge',
      ],
      correctIndex: 1,
      solution: 'Synchronized footfalls act as a strong periodic driving force. If their frequency happens to match one of the bridge\'s natural vibration modes, resonance can build the oscillation amplitude to dangerous levels — breaking stride randomizes the driving frequency and avoids this.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A damped oscillator has natural frequency ω₀ = 5 rad/s and decay parameter b/(2m) = 3 s⁻¹. The actual (damped) angular frequency of oscillation ω_d is:',
      options: ['√16 = 4 rad/s', '√34 rad/s', '2 rad/s', '8 rad/s'],
      correctIndex: 0,
      solution: 'ω_d = √(ω₀² − (b/2m)²) = √(25 − 9) = √16 = 4 rad/s.',
    ),
  ],
  revision: [
    'All real oscillators lose energy to damping (friction, drag, viscosity), causing amplitude to decay over time.',
    'Underdamped: still oscillates, envelope ±Ae^(−bt/2m) decays exponentially. Critically damped: fastest return to equilibrium with NO oscillation. Overdamped: slow, sluggish return, also without oscillating.',
    'Damped angular frequency ω_d = √(ω₀² − (b/2m)²) is always slightly less than the undamped natural frequency ω₀.',
    'Forced oscillation settles into the driving frequency; steady-state amplitude A(ω) = F₀/√[(k−mω²)²+(bω)²] peaks sharply when ω ≈ ω₀ — this is resonance.',
    'Damping is what keeps the resonance peak finite; less damping gives a taller, narrower peak, more damping gives a shorter, broader one.',
    'Real-life resonance: Tacoma Narrows Bridge collapse, shattering a wine glass with sound, soldiers breaking step on a bridge, MRI machines exploiting nuclear-spin resonance.',
    'Shock absorbers are engineered near CRITICAL damping — the design goal there is fast settling with minimal or no bounce, not zero damping.',
  ],
  sandboxBuilder: (_) => const DampedForcedSandbox(),
);
