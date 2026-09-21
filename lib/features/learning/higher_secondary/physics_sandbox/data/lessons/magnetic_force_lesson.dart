import '../../models/lesson.dart';
import '../../simulators/magnetic_force_sandbox.dart';

/// Magnetic Field & Lorentz Force — the entry point to magnetism.
final Lesson magneticForceLesson = Lesson(
  topicId: 'magnetic-force',
  title: 'Magnetic Field & Lorentz Force',
  bigQuestion:
      'A magnet does nothing to a charge sitting still — but the instant that charge starts moving, the magnet grabs it and pushes it sideways. How can a force depend on whether you happen to be moving?',
  whyItMatters:
      'The magnetic force is the strangest force in your syllabus: it is always perpendicular to the motion, so it never speeds a particle up — it only bends its path. That single rule runs cyclotrons, mass spectrometers, TV tubes and every electric motor on Earth. Master F = qv×B and half of the magnetism chapter becomes bookkeeping.',
  prediction: const PredictionPrompt(
    scenario:
        'A positive charge is fired straight ALONG the magnetic field lines (θ = 0° between v and B). What magnetic force does it feel?',
    options: [
      'A large force, since the field is strong',
      'A force along the direction of motion',
      'Zero force',
      'A force opposite to the motion',
    ],
    correctIndex: 2,
    reveal:
        'Because F = qvB·sinθ and sin 0° = 0, a charge moving parallel to B feels NO magnetic force at all. Set θ = 0° (or 180°) in the lab and watch F collapse to zero. The force is largest at θ = 90°, when v is perpendicular to B.',
  ),
  experiments: [
    'Set θ = 90° for maximum force, then drag θ to 0° and watch F vanish',
    'Flip the charge q from + to − and watch the force dot become a cross (direction reverses)',
    'Double the speed v — the force doubles (F ∝ v)',
    'Double the field B — the force doubles too (F ∝ B)',
    'Try q = 0: no charge, no force, no matter how fast it moves',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A magnetic field B is the region around a magnet or a current where a moving charge feels a push. The key word is MOVING. A stationary charge in a magnetic field feels nothing — unlike an electric field, which pushes charges whether they move or not. The magnetic force needs velocity to exist.',
      title: 'The magnetic force only acts on moving charge',
    ),
    ContentBlock.formula('F = q·v × B      |F| = q·v·B·sinθ', title: 'THE MAGNETIC (LORENTZ) FORCE'),
    ContentBlock.paragraph(
      'Read this vector equation carefully. The cross product means F is perpendicular to BOTH v and B at once. θ is the angle between v and B. When they are parallel (θ = 0) the force is zero; when they are perpendicular (θ = 90°) the force is maximum, qvB. The unit of B is the tesla (T): one tesla makes a 1 C charge moving at 1 m/s feel 1 N.',
    ),
    ContentBlock.bullets([
      'Direction of F: right-hand rule — fingers point along v, curl toward B, thumb gives v×B (for +q).',
      'For a negative charge, the force is opposite to v×B.',
      'F ⟂ v always, so the magnetic force does NO work and never changes the speed.',
    ]),
    ContentBlock.paragraph(
      'That last point is the whole personality of this force. Because F is always perpendicular to the velocity, it can only turn the particle, never speed it up or slow it down. Kinetic energy stays constant; only the direction of motion changes. This is why charges spiral instead of accelerating in straight lines.',
      title: 'Why the magnetic force does no work',
    ),
    ContentBlock.realLife(
      'The Northern Lights are F = qv×B in the sky. Charged particles streaming from the Sun hit Earth\'s magnetic field, get bent into spirals, and funnel toward the poles where they crash into the atmosphere and glow. The same force steers the electron beam in old CRT televisions and confines plasma in fusion reactors.',
    ),
    ContentBlock.paragraph(
      'When both an electric field E and a magnetic field B are present, the total force is the full Lorentz force: F = qE + qv×B. The electric part acts even at rest and can do work; the magnetic part needs motion and cannot. A "velocity selector" balances the two so only charges of one particular speed pass straight through.',
      title: 'The complete Lorentz force',
    ),
    ContentBlock.formula('F = q·E + q·v × B', title: 'FULL LORENTZ FORCE'),
    ContentBlock.mistake(
      'Students forget the sinθ and write F = qvB always. That is only true at θ = 90°. If the charge moves at 30° to the field, the force is qvB·sin30° = ½qvB. Always check the angle between v and B, not between v and something else.',
    ),
    ContentBlock.mistake(
      'A very common slip: claiming the magnetic force speeds up the particle. It cannot. F ⟂ v means power P = F·v = 0. The particle\'s speed (and kinetic energy) is frozen; only its direction turns. If a problem shows a charge gaining speed, an electric field must be involved.',
    ),
    ContentBlock.example(
      'A proton (q = 1.6×10⁻¹⁹ C) moves at v = 2×10⁶ m/s at 30° to a field B = 0.5 T. Find the force.\n\nF = qvB·sinθ = (1.6×10⁻¹⁹)(2×10⁶)(0.5)(sin30°)\n= (1.6×10⁻¹⁹)(2×10⁶)(0.5)(0.5)\n= 8×10⁻¹⁴ N.\n\nDirection: perpendicular to the plane of v and B, given by the right-hand rule. Notice how tiny the number is — magnetic forces on single particles are minute, yet they bend the path completely because there is nothing else acting.',
    ),
    ContentBlock.jeeTip(
      'For a current-carrying wire the force is F = I·L×B, magnitude BIL·sinθ. It is the same qv×B summed over all the moving electrons (I = nqvA). JEE mixes single-charge and wire versions in one problem — know that they are the same physics.',
    ),
    ContentBlock.jeeTip(
      'In a velocity selector, qE = qvB gives the pass-through speed v = E/B, independent of charge and mass. This one line is a favourite JEE plug-in for mass spectrometer problems.',
    ),
    ContentBlock.neetNote(
      'NEET loves the conceptual trio: (1) magnetic force does no work, (2) it is zero when v ∥ B, (3) it is maximum when v ⟂ B. Also remember the unit conversions: 1 T = 10⁴ gauss, and the tesla in base units is kg·s⁻²·A⁻¹.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define the field through the force it produces',
      math: 'F = q·v × B',
      note: 'B is defined operationally: it is whatever vector makes this cross-product give the observed force on a test charge.',
    ),
    DerivationStep(
      title: 'Take the magnitude of the cross product',
      math: '|v × B| = v·B·sinθ\n|F| = q·v·B·sinθ',
      note: 'θ is the angle between v and B. This is where sinθ enters.',
    ),
    DerivationStep(
      title: 'Show the force does no work',
      math: 'P = F · v = q(v × B) · v = 0',
      note: 'v×B is perpendicular to v, so its dot product with v is zero. No work → speed constant.',
    ),
    DerivationStep(
      title: 'Build the wire force from single charges',
      math: 'I = n·q·v·A\nF = (n·A·L)·q·(v × B) = I·L × B',
      note: 'Summing qv×B over all n carriers in length L reproduces the current-in-a-wire law F = IL×B.',
    ),
    DerivationStep(
      title: 'Add the electric part for the full Lorentz force',
      math: 'F = q·E + q·v × B',
      note: 'Setting qE = qvB gives the velocity selector condition v = E/B.',
    ),
  ],
  formulas: const [
    FormulaEntry('Magnetic force on a charge', 'F = qvB·sinθ', condition: 'θ = angle between v and B'),
    FormulaEntry('Vector form', 'F = q·v × B'),
    FormulaEntry('Full Lorentz force', 'F = qE + q·v × B'),
    FormulaEntry('Force on a current wire', 'F = I·L × B,  |F| = BIL·sinθ'),
    FormulaEntry('Velocity selector', 'v = E/B', condition: 'when qE = qvB balance'),
    FormulaEntry('Work done by magnetic force', 'W = 0', condition: 'F ⟂ v always'),
    FormulaEntry('Tesla in base units', '1 T = 1 N·s·C⁻¹·m⁻¹ = 10⁴ gauss'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The magnetic force on a charged particle is zero when the particle moves:',
      options: [
        'Perpendicular to the field',
        'Parallel or antiparallel to the field',
        'In a circle',
        'At 45° to the field',
      ],
      correctIndex: 1,
      solution:
          'F = qvB·sinθ. When v is parallel (θ = 0°) or antiparallel (θ = 180°) to B, sinθ = 0, so the force vanishes. The force is maximum at θ = 90°.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The work done by a magnetic force on a moving charge is:',
      options: ['Always positive', 'Always negative', 'Always zero', 'Equal to qvB'],
      correctIndex: 2,
      solution:
          'The magnetic force is always perpendicular to the velocity, so F·v = 0 and the power delivered is zero. The magnetic force changes direction but never speed, hence does no work.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A charge of 2 µC moves at 5×10⁵ m/s perpendicular to a field of 0.4 T. The force on it is:',
      options: ['0.2 N', '0.4 N', '0.04 N', '4 N'],
      correctIndex: 1,
      solution:
          'F = qvB·sin90° = (2×10⁻⁶)(5×10⁵)(0.4)(1) = (2×10⁻⁶)(2×10⁵) = 0.4 N. Keep the powers of ten organised: 2×5 = 10, and 10⁻⁶×10⁵ = 10⁻¹, giving 10×0.1×0.4 = 0.4 N.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A wire of length 0.5 m carrying 4 A lies perpendicular to a 0.3 T field. The force on it is:',
      options: ['0.3 N', '0.6 N', '0.12 N', '1.2 N'],
      correctIndex: 1,
      solution:
          'F = BIL·sinθ = (0.3)(4)(0.5)(1) = 0.6 N. This is qv×B summed over every electron in the wire.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'In a velocity selector, E = 3×10⁴ V/m and B = 0.6 T are crossed. The speed of particles passing undeflected is:',
      options: ['5×10⁴ m/s', '1.8×10⁴ m/s', '5×10³ m/s', '2×10⁵ m/s'],
      correctIndex: 0,
      solution:
          'Undeflected means the electric and magnetic forces balance: qE = qvB, so v = E/B = 3×10⁴ / 0.6 = 5×10⁴ m/s. Note it is independent of the charge and mass.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A proton and an electron move with the same velocity into the same magnetic field. Compared to the proton, the force on the electron is:',
      options: [
        'Larger in magnitude',
        'Equal in magnitude, opposite in direction',
        'Zero',
        'Smaller in magnitude',
      ],
      correctIndex: 1,
      solution:
          'The magnitude qvB depends on the charge magnitude, which is equal (1.6×10⁻¹⁹ C) for both. The sign is opposite, so the forces are equal in magnitude but point in opposite directions. Mass does not enter the force formula.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A charge q moves with v = (2î + 3ĵ)×10⁵ m/s in a field B = 0.1 k̂ T. The magnetic force is proportional to:',
      options: ['(3î − 2ĵ)', '(2î + 3ĵ)', '(3î + 2ĵ)', 'k̂'],
      correctIndex: 0,
      solution:
          'v × B = (2î + 3ĵ)×10⁵ × 0.1k̂. Using î×k̂ = −ĵ and ĵ×k̂ = î: (2×10⁵)(0.1)(î×k̂) + (3×10⁵)(0.1)(ĵ×k̂) = (2×10⁴)(−ĵ) + (3×10⁴)(î) = 10⁴(3î − 2ĵ). So F ∝ (3î − 2ĵ) — perpendicular to v, as expected.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A charge enters a region with both E and B along the same direction, moving parallel to them. Its path is:',
      options: [
        'A circle',
        'A straight line, but it speeds up or slows down',
        'A helix',
        'Unchanged in speed and direction',
      ],
      correctIndex: 1,
      solution:
          'v is parallel to B, so v×B = 0 and the magnetic force is zero. Only the electric force qE acts, along the line of motion — the charge accelerates or decelerates in a straight line. No bending occurs because the magnetic part is switched off by the parallel geometry.',
    ),
  ],
  revision: [
    'Magnetic force acts only on MOVING charge: F = qv×B, magnitude qvB·sinθ.',
    'Force is zero when v ∥ B (θ = 0/180°) and maximum when v ⟂ B (θ = 90°).',
    'F is always perpendicular to v, so it does NO work — speed is constant, only direction turns.',
    'Current wire version: F = IL×B, magnitude BIL·sinθ — the same physics summed over carriers.',
    'Full Lorentz force F = qE + qv×B; velocity selector gives v = E/B.',
    'Unit: tesla, 1 T = 10⁴ gauss. The sign of q flips the force direction.',
  ],
  sandboxBuilder: (_) => const MagneticForceSandbox(),
);
