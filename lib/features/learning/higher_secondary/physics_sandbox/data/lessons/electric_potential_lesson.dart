import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/electric_potential_sandbox.dart';

/// Electric Potential — turning the field into a single number per point.
final Lesson electricPotentialLesson = Lesson(
  topicId: 'electric-potential',
  title: 'Electric Potential',
  bigQuestion:
      'A charged balloon can zap your finger with a spark, yet the electric field around it is invisible and directionless-feeling to describe in words. Is there a single NUMBER — not an arrow — that tells you how "charged up" a point in space really is?',
  whyItMatters:
      'Electric potential is the scalar cousin of the electric field, and it is often far easier to work with. Instead of adding field vectors from every charge (magnitude AND direction), you add potentials from every charge as plain numbers. Potential is also the bridge to energy: once you know V, the potential energy and the work needed to move a charge fall out immediately. Capacitors, circuits, and the entire concept of "voltage" in every battery and wall socket are built on this one idea.',
  prediction: const PredictionPrompt(
    scenario:
        'A positive test charge starts very close to a positive point charge Q and is slowly moved twice as far away. What happens to the potential V at its new location?',
    options: [
      'V stays exactly the same — potential does not depend on distance',
      'V drops to half its original value',
      'V drops to one-quarter of its original value',
      'V becomes negative because the charge moved away',
    ],
    correctIndex: 1,
    reveal:
        'V = kQ/r depends on 1/r — NOT 1/r² like the field. So doubling r simply HALVES V. In the lab, drag the test point outward and watch the ring labels: the potential falls off much more gently than the field would. This 1/r vs 1/r² distinction is one of the most-tested facts in this chapter.',
  ),
  experiments: [
    'Drag the test dot from close-in out to the edge and watch V fall as 1/r, not 1/r²',
    'Flip Q to negative and see every equipotential ring\'s label turn negative',
    'Set Q to a small value and notice how gently V changes with radius compared to a large Q',
    'Watch the energy-landscape bar on the right rise and fall as you move the test point — a physical picture of "height" in the electric hill',
    'Set Q = 0 and confirm every ring reads exactly 0 V, no matter the radius',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Electric potential V at a point is the work done per unit positive charge in bringing a small test charge from infinity (where V is defined as zero) to that point, without any acceleration. Equivalently, for a point charge Q, V = kQ/r — the same Coulomb constant, but now the distance appears to the first power, not squared. Its unit is the volt (V), where 1 V = 1 joule per coulomb.',
      title: 'Potential: energy per unit charge',
    ),
    ContentBlock.formula('V = kQ/r,   k = 1/(4πε₀) = 9×10⁹ N·m²/C²', title: 'POTENTIAL OF A POINT CHARGE'),
    ContentBlock.paragraph(
      'The single biggest advantage of potential over field: V is a SCALAR. To find the total potential at a point due to several charges, you just add the individual potentials as plain numbers — no components, no parallelogram law, signs included. Compare this to the electric field, where superposition demands vector addition (see the Electric Field lesson). This is why problems with many charges are often solved via potential first, then the field is found afterward if needed.',
      title: 'Superposition: scalar addition, not vector',
    ),
    ContentBlock.formula('V_net = ΣVᵢ = kq₁/r₁ + kq₂/r₂ + …', title: 'SUPERPOSITION OF POTENTIAL'),
    ContentBlock.paragraph(
      'Field and potential are two views of the same information, related by E = −dV/dr. The field points in the direction of the STEEPEST DECREASE of potential — from high V to low V. A surface joining points of equal potential is called an equipotential surface, and it is always perpendicular to the field lines passing through it (exactly like contour lines on a map are perpendicular to the direction a ball would roll downhill).',
      title: 'How E and V connect',
    ),
    ContentBlock.formula('E = −dV/dr   (field points from high V to low V)', title: 'FIELD FROM POTENTIAL'),
    ContentBlock.bullets([
      'Equipotential surfaces around a point charge are concentric spheres (circles in 2D)',
      'No work is done moving a charge ALONG an equipotential surface (V does not change)',
      'Field lines and equipotential surfaces always meet at 90°',
      'Equipotentials are closely spaced where the field is strong, widely spaced where it is weak',
    ]),
    ContentBlock.paragraph(
      'Once V is known, the potential energy of a charge pair and the work to move a charge follow immediately. The potential energy of two point charges is U = kq₁q₂/r — this is the energy stored in their configuration, positive for like charges (they would fly apart and release energy) and negative for unlike charges (energy must be supplied to pull them apart). The work done in moving a charge q between two points is simply the charge times the potential difference.',
      title: 'From potential to energy and work',
    ),
    ContentBlock.formula('U = kq₁q₂/r   (potential energy of a charge pair)', title: 'ELECTRIC POTENTIAL ENERGY'),
    ContentBlock.formula('W = q·ΔV = q(V_f − V_i)   (work to move a charge)', title: 'WORK-POTENTIAL RELATION'),
    ContentBlock.realLife(
      'The "voltage" written on every battery (1.5 V, 9 V, 12 V) is a potential DIFFERENCE — it tells you how much energy per coulomb the battery can deliver as charge flows from one terminal to the other. Van de Graaff generators can reach millions of volts of potential yet carry very little charge, which is why a spark from one, though visually dramatic, does not kill you the way a low-voltage but high-current wall socket easily can.',
    ),
    ContentBlock.mistake(
      'Confusing V, U, and E — three different physical quantities that sound similar. V (potential) is a property of a POINT in space due to source charges, defined even with no test charge there. U (potential energy) needs TWO charges — it belongs to a charge placed at that point, U = qV. E (field) is a VECTOR with direction, not a scalar like V. Always ask: "is this a property of a point, or of a charge placed there?"',
    ),
    ContentBlock.mistake(
      'Assuming V is always positive. V = kQ/r takes the SIGN of Q. Around a negative charge, potential is negative everywhere, and it becomes MORE negative (not "smaller in magnitude") as you approach the charge. A test charge is only pulled toward regions of lower potential if it is positive; a negative test charge is pulled toward HIGHER potential.',
    ),
    ContentBlock.example(
      'A charge Q = +2 µC sits alone. Find the potential 30 cm away, and the work needed to bring a +5 nC charge from far away to that point.\n\nV = kQ/r = 9×10⁹ × 2×10⁻⁶ / 0.30 = 18000/0.30 = 60000 V = 6×10⁴ V.\n\nW = qΔV = (5×10⁻⁹)(6×10⁴ − 0) = 3×10⁻⁴ J.\n\nBoth Q and the test charge are positive, so positive work must be done against repulsion to bring the charge in — consistent with W being positive here.',
    ),
    ContentBlock.jeeTip(
      'For a system of charges, total electrostatic potential energy is found by summing U = kq_iq_j/r_ij over every DISTINCT PAIR (not every ordered pair — don\'t double count). For 3 charges there are 3 pairs; for 4 charges there are 6 pairs. This total U is the work needed to assemble the configuration starting from charges at infinity.',
    ),
    ContentBlock.jeeTip(
      'On the equatorial line of a dipole, V = 0 everywhere (the + and − contributions cancel exactly, since both are equidistant) — even though the FIELD there is non-zero (kp/r³, see Electric Field lesson). This is a classic trap: zero potential does NOT imply zero field, and vice versa.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for potential due to a charged conducting sphere: OUTSIDE and ON the surface, V = kQ/r (measuring r from the centre, as if all charge were a point at the centre); INSIDE the sphere, V is CONSTANT and equal to the surface value (even though the field inside is zero) — because no work is needed to move a charge within a region of zero field.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define potential via work done against the field',
      math: 'V = W_∞→P / q₀',
      note: 'Work done per unit positive test charge bringing it from infinity (V = 0) to point P, with no change in kinetic energy.',
    ),
    DerivationStep(
      title: 'Compute the work integral for a point charge Q',
      math: 'V = −∫∞ʳ E·dr = −∫∞ʳ (kQ/x²) dx',
      note: 'Field points radially outward; integrate along the radial direction.',
    ),
    DerivationStep(
      title: 'Evaluate the integral',
      math: 'V = kQ [1/x]∞ʳ = kQ/r',
      note: 'The 1/∞ term vanishes, leaving the familiar 1/r potential.',
    ),
    DerivationStep(
      title: 'Differentiate to recover the field',
      math: 'E = −dV/dr = −d/dr(kQ/r) = kQ/r²',
      note: 'Confirms the E–V relationship is self-consistent: differentiating the 1/r potential recovers the 1/r² field.',
    ),
    DerivationStep(
      title: 'Superpose for multiple charges (scalar sum)',
      math: 'V_net = Σ kqᵢ/rᵢ',
      note: 'Unlike field superposition, no components or angles are needed — just add signed numbers.',
    ),
  ],
  formulas: const [
    FormulaEntry('Potential of a point charge', 'V = kQ/r'),
    FormulaEntry('Superposition of potential', 'V_net = ΣVᵢ  (scalar sum)'),
    FormulaEntry('Field from potential', 'E = −dV/dr'),
    FormulaEntry('Potential energy of a charge pair', 'U = kq₁q₂/r'),
    FormulaEntry('Work done moving a charge', 'W = qΔV'),
    FormulaEntry('Potential inside a charged conducting sphere', 'V = kQ/R  (constant, R = radius)'),
    FormulaEntry('Potential energy of a charge in a field', 'U = qV'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the distance from a point charge is tripled, the electric potential at that point becomes:',
      options: ['3 times', '1/3 of original', '1/9 of original', '9 times'],
      correctIndex: 1,
      solution: 'V ∝ 1/r (not 1/r²). Tripling r divides V by 3, giving one-third of the original potential.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The electric potential inside a uniformly charged hollow conducting sphere (no charge inside):',
      options: [
        'Is zero everywhere inside',
        'Increases linearly toward the centre',
        'Equals the potential at the surface, constant throughout the interior',
        'Cannot be determined without more information',
      ],
      correctIndex: 2,
      solution: 'The field inside a charged conducting sphere is zero, so no work is needed to move a charge inside — V stays constant and equal to the surface value V = kQ/R.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A charge of +4 µC produces a potential of 1.2×10⁵ V at a point. The distance of that point from the charge is:',
      options: ['0.3 m', '0.5 m', '0.03 m', '3 m'],
      correctIndex: 0,
      solution: 'r = kQ/V = (9×10⁹ × 4×10⁻⁶) / 1.2×10⁵ = 3.6×10⁴ / 1.2×10⁵ = 0.3 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two charges +q and −q are placed at (−a,0) and (+a,0). The electric potential at the origin and at a point on the equatorial (perpendicular bisector) line are, respectively:',
      options: [
        'Both zero',
        'Non-zero at origin, zero on equatorial line',
        'Zero at origin, non-zero on equatorial line',
        'Both non-zero and equal',
      ],
      correctIndex: 0,
      solution: 'At the origin, distances to +q and −q are equal (both = a), so V = kq/a − kq/a = 0. On the equatorial line, every point is equidistant from +q and −q, so again V = kq/r − kq/r = 0. Potential is zero everywhere on the perpendicular bisector of a dipole, even though the field there is not.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A charge of 2 nC is moved from a point where V = 400 V to a point where V = 100 V. The work done by the electric force is:',
      options: ['+600 nJ', '−600 nJ', '+800 nJ', '−800 nJ'],
      correctIndex: 0,
      solution: 'Work done BY the electric force = q(V_i − V_f) = 2×10⁻⁹ × (400 − 100) = 2×10⁻⁹ × 300 = 600×10⁻⁹ J = +600 nJ. A positive charge moving from high to low potential has positive work done on it by the field.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Which of the following correctly distinguishes electric potential from electric potential energy?',
      options: [
        'They are the same physical quantity with different names',
        'Potential is a property of a point in space; potential energy belongs to a charge placed there (U = qV)',
        'Potential energy is a vector; potential is a scalar',
        'Potential requires two charges; potential energy requires only one',
      ],
      correctIndex: 1,
      solution: 'V exists at a point due to source charges alone, independent of any test charge. Potential energy U = qV only makes sense once an actual charge q is placed at that point — it takes two entities (the source and the placed charge) to define an energy.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Two point charges +3 µC and +2 µC are 50 cm apart. The electrostatic potential energy of the pair is closest to:',
      options: ['0.108 J', '0.054 J', '0.27 J', '5.4 J'],
      correctIndex: 0,
      solution: 'U = kq₁q₂/r = 9×10⁹ × (3×10⁻⁶)(2×10⁻⁶) / 0.50 = 9×10⁹ × 6×10⁻¹² / 0.50 = 0.054 / 0.50 = 0.108 J. Positive, since both charges are positive — energy must be supplied to assemble them from infinity.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A charge +Q is fixed at the origin. A test charge is brought from r = 2R to r = R along a radial line, then moved along an arc of radius R to another point at the same distance R. The total work done by the electric force over this whole path is:',
      options: [
        'Work done only over the radial segment (arc contributes zero)',
        'Equal work over both segments',
        'Zero over the entire path',
        'Cannot be determined without the arc angle',
      ],
      correctIndex: 0,
      solution: 'Moving along the arc keeps r = R fixed, so it stays on a single equipotential surface — no work is done there (electric force is always radial, perpendicular to the arc\'s direction of motion). All the work is done during the radial segment from 2R to R: W = q(V_R − V_2R).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The potential due to a small electric dipole at a point on its axis, at distance r from its centre (r ≫ length of dipole), is proportional to:',
      options: ['1/r', '1/r²', '1/r³', 'r'],
      correctIndex: 1,
      solution: 'For a dipole, V_axial = kp/r² (potential falls off as 1/r², one power faster than a single point charge\'s 1/r, because the + and − contributions nearly cancel at large r).',
    ),
  ],
  revision: [
    'V = kQ/r for a point charge; V is a SCALAR (unlike E, a vector).',
    'Superposition of potential is simple scalar addition: V_net = ΣVᵢ.',
    'E = −dV/dr: field points from high potential to low potential.',
    'Equipotential surfaces are always perpendicular to field lines; no work is done moving along one.',
    'U = kq₁q₂/r is the potential energy of a charge PAIR; W = qΔV is work to move a single charge.',
    'Inside a charged conducting sphere, V is constant (= surface value) even though E = 0 there.',
    'Zero potential does not imply zero field, and vice versa — check the dipole equatorial line.',
  ],
  sandboxBuilder: (_) => const ElectricPotentialSandbox(),
  accentColor: Palette.chElectroMag,
);
