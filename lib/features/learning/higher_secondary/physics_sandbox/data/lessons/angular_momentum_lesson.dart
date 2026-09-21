import '../../models/lesson.dart';
import '../../simulators/angular_momentum_sandbox.dart';
import '../../theme/tokens.dart';

/// Angular Momentum — the rotational analogue of momentum, and why skaters speed up.
final Lesson angularMomentumLesson = Lesson(
  topicId: 'angular-momentum',
  title: 'Angular Momentum',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A figure skater spins slowly with arms stretched wide, then suddenly pulls her arms in — and without pushing off anything or getting any new force from outside, she spins dramatically faster. Where does that extra rotation speed come from?',
  whyItMatters:
      'Angular momentum is to rotation what ordinary momentum is to straight-line motion — and just like linear momentum, it is conserved whenever no external torque acts. This single idea explains the skater/diver spin-up effect, why planets sweep out equal areas in equal times (Kepler\'s second law), and why a spinning top resists toppling. JEE and NEET both treat conservation of angular momentum as a go-to shortcut for problems that would otherwise need messy torque integration.',
  prediction: const PredictionPrompt(
    scenario:
        'A figure skater spins with arms stretched out, then pulls her arms in close to her body while continuing to spin freely (no external torque from the ice, which is essentially frictionless). What happens to her spin rate?',
    options: [
      'It stays exactly the same — pulling in arms doesn\'t affect spin',
      'It decreases, because she is now a smaller, lighter-looking shape',
      'It increases, because her moment of inertia decreases while angular momentum stays fixed',
      'It becomes zero, because she loses all her rotational energy',
    ],
    correctIndex: 2,
    reveal:
        'With no external torque acting (ice friction is negligible), angular momentum L = Iω is conserved. Pulling the arms in reduces the moment of inertia I (mass now sits closer to the rotation axis), so ω must increase to keep L fixed. In the lab, drag the "arms in ↔ out" slider toward IN and watch the spin visibly speed up — exactly the skater effect, governed by nothing more than L = Iω = constant.',
  ),
  experiments: [
    'Drag arms fully IN and watch ω shoot up as I drops',
    'Drag arms fully OUT and watch the spin slow down dramatically',
    'Increase body mass at a fixed arm position and see I rise, ω fall — same L, more mass needs slower spin',
    'Raise the angular momentum slider (a stronger initial push) and see the whole spin speed up uniformly, at any arm position',
    'Note that L itself, the meter you cannot change by moving the arms, never budges as arms go in and out — only I and ω trade off against each other',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Angular momentum measures "how much rotation" a body has, combining how much mass is rotating, how that mass is distributed relative to the axis (moment of inertia), and how fast it spins. It is the rotational counterpart of ordinary (linear) momentum p = mv, with moment of inertia I playing the role of mass and angular velocity ω playing the role of velocity.',
      title: 'What angular momentum measures',
    ),
    ContentBlock.formula('L = Iω    (for rotation about a fixed axis)', title: 'ANGULAR MOMENTUM — ROTATION FORM'),
    ContentBlock.formula('L = r × p = r × mv    (for a single particle, about any chosen point)', title: 'ANGULAR MOMENTUM — VECTOR FORM'),
    ContentBlock.bullets([
      'L = Iω applies cleanly to a rigid body spinning about a fixed axis',
      'L = r×p is the more general definition, useful for a single particle (like a planet) whose "rotation" is really just its position and momentum relative to a chosen origin',
      'Both definitions agree for a particle moving in a circle: L = mvr = m(ωr)r = mr²ω = Iω, since I = mr² for a point mass',
      'Angular momentum is a vector, with direction given by the right-hand rule along the rotation axis',
    ]),
    ContentBlock.paragraph(
      'Just as linear momentum is conserved when no external force acts, angular momentum is conserved when no external TORQUE acts on a system. Internal torques (like a skater\'s own muscles pulling her arms inward) can freely redistribute mass and change I, but they cannot change L itself — so ω must adjust to compensate.',
      title: 'Conservation of angular momentum',
    ),
    ContentBlock.formula('If τ_ext = 0:   I₁ω₁ = I₂ω₂   (L stays constant)', title: 'CONSERVATION LAW'),
    ContentBlock.paragraph(
      'Torque is to angular momentum exactly what force is to linear momentum: the rate of change of angular momentum. This parallel is one of the cleanest analogies in all of mechanics, and it lets you transfer everything you know about F = dp/dt directly into rotational problems.',
      title: 'Torque as the rate of change of angular momentum',
    ),
    ContentBlock.formula('τ = dL/dt    (exact rotational analogue of F = dp/dt)', title: 'TORQUE — ANGULAR MOMENTUM RELATION'),
    ContentBlock.realLife(
      'A diver leaping off a board tucks into a ball mid-air to spin fast for multiple somersaults, then stretches back out just before entering the water to slow the spin to nearly zero for a clean, vertical splash. A spinning bicycle wheel resists being tipped over (gyroscopic stability) because changing the direction of its angular momentum vector requires an external torque. Even the graceful, slow-motion spin of a falling cat (which twists itself in mid-air to always land on its feet) conserves total angular momentum at zero throughout the fall.',
    ),
    ContentBlock.mistake(
      'Assuming energy is also conserved when a skater pulls her arms in. It is NOT — kinetic energy actually INCREASES (½Iω² grows because ω grows faster than I shrinks), and that extra energy comes from the real muscular work done pulling the arms inward against the outward-feeling centrifugal tendency. Only angular MOMENTUM is conserved here, not kinetic energy.',
    ),
    ContentBlock.mistake(
      'Forgetting that L = Iω requires a well-defined rotation axis and rigid-body assumption; for irregular, non-rigid or multi-part systems, always fall back on L = Σ(r×p) summed over all the mass elements, or use the more general conservation statement I₁ω₁ = I₂ω₂ only when I is measured consistently about the SAME axis before and after.',
    ),
    ContentBlock.example(
      'A student on a frictionless rotating stool holds two 2 kg weights at arm\'s length, 0.8 m from the rotation axis, spinning at 2 rad/s. She then pulls the weights in to 0.4 m from the axis (ignore her own body\'s moment of inertia change). Find her new angular speed.\n\nI₁ = 2 × (0.8)² × 2 (two weights) = 2 × 0.64 × 2 = 2.56 kg·m²\nI₂ = 2 × (0.4)² × 2 = 2 × 0.16 × 2 = 0.64 kg·m²\nConservation: I₁ω₁ = I₂ω₂ ⟹ 2.56 × 2 = 0.64 × ω₂ ⟹ ω₂ = 5.12/0.64 = 8 rad/s.\n\nHalving the radius quadrupled her spin rate (since I ∝ r²) — exactly the skater effect.',
    ),
    ContentBlock.jeeTip(
      'For problems combining a spinning disc/platform with a person or object walking onto it (or falling onto a rotating system), always conserve angular momentum about the FIXED rotation axis of the system, using I_total = I_platform + I_person(at their new radius), not linear momentum — the person\'s own path onto the platform is often irrelevant once they are aboard and rotating with it.',
    ),
    ContentBlock.neetNote(
      'NEET occasionally connects this topic to planetary motion: a planet in an elliptical orbit sweeps out equal areas in equal times (Kepler\'s second law) precisely BECAUSE gravity, always pointing along the line to the sun, produces zero torque about the sun — so the planet\'s angular momentum about the sun is conserved throughout its orbit. This is covered in more depth in the Planetary Motion topic; here, just recognise it as one more example of τ_ext = 0 ⟹ L = constant.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define angular momentum of a particle about a point',
      math: 'L = r × p = r × mv',
      note: 'For circular motion, r ⊥ v, so |L| = mvr = m(ωr)r = mr²ω.',
    ),
    DerivationStep(
      title: 'Generalise to a rigid body (sum over all mass elements)',
      math: 'L = Σmᵢrᵢ²ω = (Σmᵢrᵢ²)ω = Iω',
      note: 'I = Σmᵢrᵢ² is the moment of inertia — all mass elements share the same ω for a rigid body.',
    ),
    DerivationStep(
      title: 'Differentiate L with respect to time',
      math: 'dL/dt = d(Iω)/dt',
      note: 'If I is fixed (rigid body, fixed axis), this becomes I(dω/dt) = Iα.',
    ),
    DerivationStep(
      title: 'Relate to torque via the rotational equation of motion',
      math: 'τ_net = Iα = dL/dt',
      note: 'This mirrors F_net = ma = dp/dt exactly — torque plays the role of force, angular momentum the role of momentum.',
    ),
    DerivationStep(
      title: 'Set τ_ext = 0 to get the conservation law',
      math: 'dL/dt = 0  ⟹  L = constant  ⟹  I₁ω₁ = I₂ω₂',
      note: 'This is the mathematical basis for the skater/diver spin-up-spin-down effect.',
    ),
  ],
  formulas: const [
    FormulaEntry('Angular momentum (rigid body, fixed axis)', 'L = Iω'),
    FormulaEntry('Angular momentum (particle, vector form)', 'L = r × p = r × mv'),
    FormulaEntry('Torque–angular momentum relation', 'τ = dL/dt'),
    FormulaEntry('Conservation of angular momentum', 'τ_ext = 0  ⟹  I₁ω₁ = I₂ω₂'),
    FormulaEntry('Kinetic energy of rotation', 'KE = ½Iω² = L²/(2I)'),
    FormulaEntry('Kepler\'s second law (angular momentum link)', 'Gravity produces zero torque about the sun ⟹ L conserved ⟹ equal areas in equal times'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Angular momentum is the rotational analogue of:',
      options: ['Force', 'Linear momentum', 'Kinetic energy', 'Work'],
      correctIndex: 1,
      solution: 'L = Iω is the rotational counterpart of p = mv, with I replacing m and ω replacing v.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A figure skater pulls her arms in while spinning freely on ice. Her angular speed:',
      options: ['Decreases', 'Stays the same', 'Increases', 'Becomes zero'],
      correctIndex: 2,
      solution: 'No external torque acts (ice is essentially frictionless), so L = Iω is conserved. Pulling arms in reduces I, so ω must increase.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Angular momentum is conserved for a system whenever:',
      options: [
        'No external force acts on it',
        'No external torque acts on it',
        'Its kinetic energy is constant',
        'Its moment of inertia is constant',
      ],
      correctIndex: 1,
      solution: 'From τ_ext = dL/dt, zero external torque directly implies L stays constant — this is the precise condition, distinct from the condition for linear momentum conservation (zero external force).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A disc of moment of inertia 4 kg·m² spins at 6 rad/s. It is coupled to an identical stationary disc (also 4 kg·m²) on the same axis, and they end up rotating together. The final common angular speed is:',
      options: ['2 rad/s', '3 rad/s', '4 rad/s', '6 rad/s'],
      correctIndex: 1,
      solution: 'Conservation of angular momentum: I₁ω₁ = (I₁+I₂)ω_f ⟹ 4×6 = 8×ω_f ⟹ ω_f = 24/8 = 3 rad/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'When a spinning skater pulls her arms inward, her rotational kinetic energy:',
      options: [
        'Stays the same, since angular momentum is conserved',
        'Decreases, since I decreases',
        'Increases, at the expense of muscular work done pulling the arms in',
        'Becomes exactly zero',
      ],
      correctIndex: 2,
      solution: 'KE = L²/(2I). Since L is fixed and I decreases, KE must increase. The extra energy comes from real work done by her muscles against the outward tendency of the masses — energy conservation still holds for the whole process, just not for rotational KE alone.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The relation between torque and angular momentum is:',
      options: ['τ = L/t', 'τ = dL/dt', 'τ = Lω', 'τ = L/I'],
      correctIndex: 1,
      solution: 'τ_net = dL/dt is the exact rotational analogue of F_net = dp/dt.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A student of moment of inertia 2.5 kg·m² sits on a frictionless rotating stool spinning at 3 rad/s while holding two 1.5 kg masses at 1.0 m from the axis. She pulls the masses in to 0.5 m. Her new angular speed is closest to (treat her own I as unchanged):',
      options: ['5.1 rad/s', '6 rad/s', '9 rad/s', '12 rad/s'],
      correctIndex: 0,
      solution: 'I₁ = 2.5 + 2(1.5)(1.0)² = 2.5+3 = 5.5 kg·m². I₂ = 2.5 + 2(1.5)(0.5)² = 2.5+0.75 = 3.25 kg·m². Conservation: I₁ω₁ = I₂ω₂ ⟹ 5.5×3 = 3.25×ω₂ ⟹ ω₂ = 16.5/3.25 ≈ 5.08 rad/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A planet moves in an elliptical orbit around the sun. Compared to its angular momentum at aphelion (farthest point), its angular momentum at perihelion (closest point) is:',
      options: ['Larger', 'Smaller', 'Exactly equal', 'Cannot be determined'],
      correctIndex: 2,
      solution: 'Gravity always points along the line joining planet and sun, producing zero torque about the sun at every point of the orbit. Hence angular momentum L = mvr sinθ (with θ=90° at both apsides) is exactly conserved throughout the orbit — this is the physical basis of Kepler\'s second law (equal areas in equal times).',
    ),
  ],
  revision: [
    'Angular momentum L = Iω (rigid body) or L = r×p (general particle form) — the rotational analogue of linear momentum p = mv.',
    'Torque is the rate of change of angular momentum: τ = dL/dt, exactly parallel to F = dp/dt.',
    'Conservation law: if net external torque = 0, then L = Iω stays constant, so I₁ω₁ = I₂ω₂.',
    'Skater/diver effect: pulling mass closer to the axis reduces I, forcing ω to increase to conserve L — kinetic energy actually increases, paid for by real muscular work.',
    'L = r×p is a vector via the right-hand rule; for a rigid body about a fixed axis it reduces cleanly to the scalar L=Iω.',
    'Kepler\'s second law (equal areas in equal times) is angular momentum conservation in disguise — gravity\'s zero torque about the sun keeps a planet\'s L constant throughout its orbit.',
    'Do not confuse conservation of angular momentum with conservation of kinetic energy — only L is guaranteed constant when torque is zero; KE can change.',
  ],
  sandboxBuilder: (_) => const AngularMomentumSandbox(),
);
