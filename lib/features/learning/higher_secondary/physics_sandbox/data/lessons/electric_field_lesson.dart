import '../../models/lesson.dart';
import '../../simulators/electric_field_sandbox.dart';

/// Electric Field — turning the force law into a property of space.
final Lesson electricFieldLesson = Lesson(
  topicId: 'electric-field',
  title: 'Electric Field',
  bigQuestion:
      'A charge sitting alone in empty space somehow "knows" to push any other charge that wanders near it — instantly, across the gap, with nothing in between. What is actually filling that space, waiting to act?',
  whyItMatters:
      'The field concept is one of the great leaps in physics. Instead of asking "what force does charge A exert on charge B?", we say charge A fills all of space with an electric field, and any charge B simply responds to the field where it sits. This shift — from action-at-a-distance to a field that lives in space — underpins everything from capacitors to electromagnetic waves to light itself. In exams it is the bridge between Coulomb\'s law and potential, Gauss\'s law and circuits.',
  prediction: const PredictionPrompt(
    scenario:
        'You place a positive and a negative charge of equal size near each other (a dipole). At the exact midpoint between them, which way does the electric field point?',
    options: [
      'It is zero there — the two cancel',
      'From the positive charge toward the negative charge',
      'From the negative charge toward the positive charge',
      'Straight up, perpendicular to the line joining them',
    ],
    correctIndex: 1,
    reveal:
        'At the midpoint both charges push the field the SAME way — away from + and toward −, so they add rather than cancel. In the lab, set q₁ = +q and q₂ = −q and look at the arrows on the line between them: they all point from the plus toward the minus. (For two LIKE charges, that same midpoint is a null point where the field IS zero — try it.)',
  ),
  experiments: [
    'Set q₁ = +q, q₂ = −q (a dipole) and trace how arrows leave + and enter −',
    'Set both charges positive and find the null point where arrows shrink to nothing',
    'Make q₁ much bigger than q₂ — the field near q₁ dominates',
    'Set q₂ = 0 and see the clean radial field of a single point charge',
    'Watch arrow length: it grows near the charges (strong field) and fades far away (1/r²)',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The electric field E at a point is the force per unit positive charge that a tiny test charge would feel there. Divide the Coulomb force by the test charge and the test charge cancels out — what remains is a property of space itself, created by the source charges. Its unit is newtons per coulomb (N/C), equivalently volts per metre (V/m).',
      title: 'Field: force per unit charge',
    ),
    ContentBlock.formula('E = F/q₀   (q₀ = small positive test charge)', title: 'DEFINITION OF ELECTRIC FIELD'),
    ContentBlock.paragraph(
      'For a single point charge Q, put F = kQq₀/r² into the definition and the test charge cancels, leaving the field of a point charge. It points radially outward from a positive charge and radially inward toward a negative one.',
      title: 'Field of a point charge',
    ),
    ContentBlock.formula('E = kQ/r²,   direction: away from +Q, toward −Q', title: 'POINT-CHARGE FIELD'),
    ContentBlock.paragraph(
      'When several charges are present, the total field is the vector sum of the fields each charge would produce alone — the same superposition principle as for forces, but now applied to E. Field lines are a picture of this: they start on positive charges, end on negative charges, never cross, and are denser where the field is stronger.',
      title: 'Superposition and field lines',
    ),
    ContentBlock.bullets([
      'Field lines start on + charges and end on − charges (or go to infinity)',
      'The tangent to a field line gives the field DIRECTION at that point',
      'Closer lines = stronger field; the density of lines encodes magnitude',
      'Two field lines never cross — the field has one definite direction at each point',
      'Field lines meet a conductor surface at 90° (the surface is an equipotential)',
    ]),
    ContentBlock.realLife(
      'A Van de Graaff generator makes your hair stand up because each strand carries the same-sign charge and repels its neighbours, aligning along the field lines leaving your head. Lightning rods are sharpened to concentrate field lines at the tip, where the field grows huge and ionises the air, guiding the strike safely to ground. Microwave ovens, capacitor plates, and CRT screens all steer charges with engineered fields.',
    ),
    ContentBlock.mistake(
      'Confusing the direction of the field with the direction of the force on a charge. E points away from a positive source. The FORCE on a test charge is F = qE — so a NEGATIVE charge feels a force OPPOSITE to E. The field direction is defined by a positive test charge only.',
    ),
    ContentBlock.mistake(
      'Adding field magnitudes like scalars. E is a vector. If two fields at a point are 3 N/C east and 4 N/C north, the resultant is 5 N/C (√(3²+4²)), not 7. Always resolve into components before summing.',
    ),
    ContentBlock.example(
      'A point charge Q = 5 nC sits at the origin. Find the field 10 cm away.\n\nE = kQ/r² = 9×10⁹ × 5×10⁻⁹ / (0.10)²\n= 9×10⁹ × 5×10⁻⁹ / 0.01\n= 45 / 0.01\n= 4500 N/C.\n\nThe field points radially outward (Q is positive). A −2 nC charge placed there would feel F = qE = 2×10⁻⁹ × 4500 = 9×10⁻⁶ N directed back toward Q (opposite to E, since the charge is negative).',
    ),
    ContentBlock.jeeTip(
      'The dipole field is a JEE staple. On the AXIS at distance r (r ≫ a): E_axial = 2kp/r³. On the perpendicular BISECTOR: E_equatorial = kp/r³, and it points OPPOSITE to the dipole moment p. Note the 1/r³ — a dipole\'s field fades faster than a point charge\'s 1/r² because the + and − nearly cancel far away. Here p = q×(2a) is the dipole moment.',
    ),
    ContentBlock.jeeTip(
      'In a uniform field E (like between capacitor plates), a charge feels a CONSTANT force qE — this is exactly like projectile motion under gravity, with a = qE/m. A charge fired sideways into the field traces a parabola. Reuse all your kinematics here.',
    ),
    ContentBlock.neetNote(
      'NEET asks: field of a point charge (E = kQ/r²), field inside a conductor (ZERO — charges rearrange to cancel it), and the dipole in a uniform field, which feels a torque τ = pE·sinθ but NO net force. It rotates to align with the field. Also remember: field lines are imaginary aids, but they are always continuous and never cross.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define field from the force a test charge feels',
      math: 'E = F / q₀',
      note: 'q₀ is vanishingly small so it does not disturb the sources.',
    ),
    DerivationStep(
      title: 'Substitute the Coulomb force of a source Q',
      math: 'F = k·Q·q₀ / r²\nE = F/q₀ = k·Q / r²',
      note: 'The test charge cancels — the field belongs to Q and to space, not to q₀.',
    ),
    DerivationStep(
      title: 'Field on the axis of a dipole (r ≫ a)',
      math: 'E = kq/(r−a)² − kq/(r+a)²\n≈ kq·[4ar]/r⁴ = 2k(q·2a)/r³ = 2kp/r³',
      note: 'p = q·2a is the dipole moment; the near-cancellation gives the 1/r³ falloff.',
    ),
    DerivationStep(
      title: 'Field on the equatorial line (perpendicular bisector)',
      math: 'E = 2·(kq/(r²+a²))·cosθ,  cosθ = a/√(r²+a²)\n≈ kp/r³   (r ≫ a)',
      note: 'Directed opposite to p. Note it is HALF the axial field at the same distance.',
    ),
    DerivationStep(
      title: 'Torque on a dipole in a uniform field',
      math: 'τ = qE·a·sinθ + qE·a·sinθ = (q·2a)E·sinθ = pE·sinθ',
      note: 'The two equal-opposite forces give a couple — pure torque, zero net force. Vectorially τ = p × E.',
    ),
  ],
  formulas: const [
    FormulaEntry('Electric field (definition)', 'E = F/q₀'),
    FormulaEntry('Field of a point charge', 'E = kQ/r²'),
    FormulaEntry('Force on a charge in a field', 'F = qE'),
    FormulaEntry('Dipole field on axis', 'E = 2kp/r³', condition: 'r ≫ a'),
    FormulaEntry('Dipole field on bisector', 'E = kp/r³', condition: 'r ≫ a, opposite to p'),
    FormulaEntry('Torque on a dipole', 'τ = pE·sinθ  (τ = p × E)'),
    FormulaEntry('Dipole moment', 'p = q·(2a)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The electric field at a point due to a point charge Q at distance r is E. What is the field at distance 2r?',
      options: ['E/2', 'E/4', '2E', '4E'],
      correctIndex: 1,
      solution:
          'E ∝ 1/r². Doubling r divides the field by 4, so the new field is E/4.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The electric field inside a charged conductor in electrostatic equilibrium is:',
      options: ['Maximum at the centre', 'Zero everywhere', 'Uniform and non-zero', 'Directed inward'],
      correctIndex: 1,
      solution:
          'Free charges rearrange on the surface until they cancel any interior field. So E = 0 everywhere inside a conductor in equilibrium — a key fact used in shielding.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A charge of 4 nC produces a field of magnitude 3600 N/C at a point. That point is at distance:',
      options: ['0.05 m', '0.10 m', '0.15 m', '0.20 m'],
      correctIndex: 1,
      solution:
          'E = kQ/r² → r² = kQ/E = 9×10⁹ × 4×10⁻⁹ / 3600 = 36/3600 = 0.01 → r = 0.10 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An electric dipole is placed in a uniform electric field. The net force and net torque on it are respectively:',
      options: ['Zero, zero', 'Zero, non-zero (unless aligned)', 'Non-zero, zero', 'Non-zero, non-zero'],
      correctIndex: 1,
      solution:
          'In a UNIFORM field the two equal-opposite forces cancel → net force zero. But they form a couple → torque τ = pEsinθ, which is non-zero unless the dipole is already aligned (θ = 0 or 180°).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'For a dipole, the ratio of the axial field to the equatorial field at the same distance r (r ≫ a) is:',
      options: ['1 : 1', '2 : 1', '1 : 2', '4 : 1'],
      correctIndex: 1,
      solution:
          'E_axial = 2kp/r³ and E_equatorial = kp/r³. The ratio is 2 : 1. The axial field is always twice the equatorial field at equal distance.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two equal positive charges +q are placed at (−a, 0) and (+a, 0). The electric field at a point (0, y) on the y-axis is maximum when y equals:',
      options: ['0', 'a/√2', 'a', 'a√2'],
      correctIndex: 1,
      solution:
          'By symmetry only the y-components survive: E = 2·(kq/(a²+y²))·(y/√(a²+y²)) = 2kqy/(a²+y²)^(3/2). Differentiate and set dE/dy = 0: this gives a² + y² − 3y² = 0 → a² = 2y² → y = a/√2.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'An electron (mass m, charge e) is released from rest in a uniform field E. Its acceleration is:',
      options: ['eE', 'eE/m', 'mE/e', 'E/(em)'],
      correctIndex: 1,
      solution:
          'Force on the electron F = eE (magnitude). By Newton\'s second law a = F/m = eE/m, directed opposite to E because the charge is negative.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Electric field lines:',
      options: [
        'Can cross each other',
        'Start on negative and end on positive charges',
        'Are closer together where the field is stronger',
        'Form closed loops in electrostatics',
      ],
      correctIndex: 2,
      solution:
          'Line density represents field strength, so lines crowd together where E is large. They start on + and end on −, never cross, and (in electrostatics) never form closed loops.',
    ),
  ],
  revision: [
    'E = F/q₀ is force per unit positive charge; unit N/C = V/m.',
    'Point charge: E = kQ/r², pointing away from + and toward −.',
    'Superposition: total E is the VECTOR sum of individual fields.',
    'Field lines start on +, end on −, never cross, crowd where E is strong.',
    'Dipole: E_axial = 2kp/r³, E_equatorial = kp/r³ (both ∝ 1/r³).',
    'In a uniform field a dipole feels torque τ = pEsinθ but zero net force; E inside a conductor is zero.',
  ],
  sandboxBuilder: (_) => const ElectricFieldSandbox(),
);
