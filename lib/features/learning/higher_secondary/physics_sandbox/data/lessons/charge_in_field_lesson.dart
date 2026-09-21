import '../../models/lesson.dart';
import '../../simulators/charge_in_field_sandbox.dart';
import '../../theme/tokens.dart';

/// Motion in a Magnetic Field — the magnetic force that steers without speeding up.
final Lesson chargeInFieldLesson = Lesson(
  topicId: 'charge-in-field',
  title: 'Motion in a Magnetic Field',
  accentColor: Palette.chElectroMag,
  bigQuestion:
      'A charged particle enters a magnetic field and curves into a perfect circle, going around and around seemingly forever without ever slowing down or speeding up. What kind of force can constantly push on something, changing its direction endlessly, yet never once change how fast it\'s going?',
  whyItMatters:
      'The magnetic force on a moving charge is the working principle behind particle accelerators, mass spectrometers, cyclotrons, and the aurora borealis. It is also one of the cleanest examples in all of physics of a force that is always perpendicular to velocity — a geometric idea tested heavily in both NEET and JEE, and one that unlocks circular-motion problems across the electromagnetism syllabus.',
  prediction: const PredictionPrompt(
    scenario:
        'A charged particle moves into a uniform magnetic field, entering exactly perpendicular to the field lines. The magnetic force on it is F = qv×B. What happens to the particle\'s SPEED as it moves through the field?',
    options: [
      'Speed increases steadily as the force accelerates it',
      'Speed decreases steadily as the force decelerates it',
      'Speed stays exactly constant — only the direction of motion changes',
      'Speed oscillates back and forth',
    ],
    correctIndex: 2,
    reveal:
        'The magnetic force qv×B is always perpendicular to velocity v, so it can never do any work on the particle (W = F·d, and F⊥v means no component of force along the motion). With no work done, kinetic energy — and hence speed — never changes; only the DIRECTION of motion curves, tracing a circle. In the lab, watch the speed readout stay pinned constant while the particle loops in a perfect circle.',
  ),
  experiments: [
    'Send a charge in perpendicular to B and watch it trace a perfect circle at constant speed',
    'Increase the magnetic field strength B and watch the circle radius shrink (r = mv/qB)',
    'Increase the particle\'s speed v and watch the radius grow proportionally',
    'Send the charge in at an angle to B (not perpendicular) and watch it trace a helix instead of a circle',
    'Flip the sign of the charge and watch the curving direction reverse',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A moving charge in a magnetic field experiences a force given by F = qv×B, the magnetic (Lorentz) force. Because this is a CROSS product, the force is always perpendicular to BOTH the velocity v and the field B — it can never point along the direction of motion. A force perpendicular to velocity does no work, which is the single most important consequence of this force law.',
      title: 'The magnetic force law',
    ),
    ContentBlock.formula('F = qv×B,   |F| = qvB sinθ', title: 'MAGNETIC FORCE ON A MOVING CHARGE'),
    ContentBlock.bullets([
      'θ = angle between velocity v and field B',
      'Force is maximum when v is perpendicular to B (θ = 90°)',
      'Force is zero when v is parallel (or antiparallel) to B (θ = 0° or 180°) — the charge moves in a straight line',
      'Direction found by the right-hand rule (for positive charge): point fingers along v, curl toward B, thumb gives F',
    ]),
    ContentBlock.paragraph(
      'Since F is always perpendicular to v, F does zero work: W = ∫F·ds = 0, because F and the displacement direction (along v) are always at 90°. By the work-energy theorem, zero work means zero change in kinetic energy — so SPEED never changes, no matter how long the particle stays in the field. Only the DIRECTION of velocity is continuously altered.',
      title: 'Why speed never changes',
    ),
    ContentBlock.formula('r = mv/(qB)', title: 'RADIUS OF CIRCULAR MOTION'),
    ContentBlock.paragraph(
      'When a charged particle enters a uniform field EXACTLY perpendicular to B, the magnetic force acts as a constant-magnitude centripetal force, curving the particle into a perfect circle. Setting the magnetic force equal to the required centripetal force (qvB = mv²/r) and solving for r gives r = mv/(qB) — larger momentum needs a bigger circle, and a stronger field pulls the circle tighter.',
      title: 'Circular motion — perpendicular entry',
    ),
    ContentBlock.paragraph(
      'If the particle enters at some ANGLE to B (neither parallel nor perpendicular), split v into two components: v_perp (perpendicular to B, causing circular motion) and v_parallel (along B, unaffected by the magnetic force since sinθ=0 for that component). The result is a HELIX — circular motion in the plane perpendicular to B, combined with steady straight-line drift along B. This is the principle behind the cyclotron and how charged particles spiral along Earth\'s magnetic field lines toward the poles, creating the aurora.',
      title: 'Helical motion — angled entry',
    ),
    ContentBlock.realLife(
      'A cyclotron accelerates charged particles in an expanding spiral, using a magnetic field to keep them curving in circular arcs while an alternating electric field speeds them up at each half-turn — the whole idea depends on the magnetic force never doing work itself, leaving the electric field to do all the accelerating. The aurora borealis (northern lights) happens because charged particles from the Sun spiral in helices along Earth\'s magnetic field lines, funnelled toward the poles where they collide with atmospheric atoms and produce light.',
    ),
    ContentBlock.mistake(
      'Believing the magnetic force changes a particle\'s speed or kinetic energy. Because F⊥v always, magnetic forces do ZERO work — this is one of the most conceptually tested facts in the chapter. Any speed change in a real device (like a cyclotron) must come from an ELECTRIC field, not the magnetic field.',
    ),
    ContentBlock.mistake(
      'Forgetting the sinθ factor in F = qvB sinθ, and assuming the force is always qvB regardless of the angle between v and B. If the particle moves exactly along the field lines (θ=0°), the magnetic force is zero and the particle travels in a straight line, unaffected.',
    ),
    ContentBlock.example(
      'A proton (q = 1.6×10⁻¹⁹ C, m = 1.67×10⁻²⁷ kg) moves at 2×10⁶ m/s perpendicular to a magnetic field of 0.5 T. Find the radius of its circular path.\n\nr = mv/(qB) = (1.67×10⁻²⁷ × 2×10⁶) / (1.6×10⁻¹⁹ × 0.5)\n= 3.34×10⁻²¹ / 8×10⁻²⁰\n≈ 0.0418 m ≈ 4.2 cm.',
    ),
    ContentBlock.jeeTip(
      'The period of circular motion T = 2πm/(qB) is INDEPENDENT of speed v — faster particles trace bigger circles but take the same time per revolution. This is the key principle that makes a cyclotron work at a FIXED driving frequency, even as particles speed up and spiral outward with increasing radius.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests the direction of curving using the right-hand rule (for positive charges) or left-hand rule (for negative charges, or equivalently reverse the right-hand result). Also remember: crossed electric and magnetic fields (velocity selector) let a charge pass undeflected only when qE = qvB, i.e. v = E/B — a classic combined-field application.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write the magnetic force for perpendicular entry (θ=90°)',
      math: 'F = qvB',
      note: 'Maximum force magnitude, constant since v and B magnitudes stay fixed (speed doesn\'t change).',
    ),
    DerivationStep(
      title: 'Recognise this force is always perpendicular to velocity',
      math: 'F ⊥ v at every instant  →  F acts as a centripetal force',
      note: 'A force of constant magnitude always perpendicular to velocity produces uniform circular motion.',
    ),
    DerivationStep(
      title: 'Equate magnetic force to the required centripetal force',
      math: 'qvB = mv²/r',
    ),
    DerivationStep(
      title: 'Solve for the radius of the circular path',
      math: 'r = mv/(qB)',
    ),
    DerivationStep(
      title: 'Find the period of revolution',
      math: 'T = 2πr/v = 2π[mv/(qB)]/v = 2πm/(qB)',
      note: 'Notice v cancels — the period does not depend on speed, only on mass, charge, and field strength.',
    ),
  ],
  formulas: const [
    FormulaEntry('Magnetic force', 'F = qv×B,  |F| = qvB sinθ'),
    FormulaEntry('Radius of circular path', 'r = mv/(qB)', condition: 'v ⊥ B'),
    FormulaEntry('Period of revolution', 'T = 2πm/(qB)', condition: 'independent of v'),
    FormulaEntry('Cyclotron frequency', 'f = qB/(2πm)'),
    FormulaEntry('Velocity selector condition', 'v = E/B', condition: 'undeflected path'),
    FormulaEntry('Work done by magnetic force', 'W = 0', condition: 'always, since F ⊥ v'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The magnetic force on a moving charge does:',
      options: ['Positive work always', 'Negative work always', 'Zero work always', 'Work depending on B'],
      correctIndex: 2,
      solution: 'F = qv×B is always perpendicular to v, so it does zero work regardless of path or field strength.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A charged particle moving parallel to a magnetic field experiences a magnetic force of:',
      options: ['Maximum magnitude', 'Zero', 'qvB', 'Depends on charge sign'],
      correctIndex: 1,
      solution: 'F = qvB sinθ. For θ = 0° (parallel), sinθ = 0, so the force is zero.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A charged particle enters a uniform magnetic field perpendicular to it. Its path is:',
      options: ['A straight line', 'A parabola', 'A circle', 'A helix'],
      correctIndex: 2,
      solution: 'Perpendicular entry gives a constant-magnitude centripetal force, producing uniform circular motion.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If the speed of a charged particle moving in a circle inside a magnetic field is doubled (B unchanged), the radius of its path:',
      options: ['Doubles', 'Halves', 'Stays the same', 'Quadruples'],
      correctIndex: 0,
      solution: 'r = mv/(qB) ∝ v. Doubling v doubles r.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The period of revolution of a charged particle in a magnetic field, moving in a circle, depends on:',
      options: ['Speed of the particle', 'Radius of the circle', 'Charge, mass, and field strength only', 'Kinetic energy'],
      correctIndex: 2,
      solution: 'T = 2πm/(qB) — v cancels out entirely, so period depends only on m, q, and B.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'An electron (q = 1.6×10⁻¹⁹ C, m = 9.1×10⁻³¹ kg) moves at 10⁶ m/s perpendicular to a field of 0.02 T. Its radius of circular motion is approximately:',
      options: ['0.28 mm', '2.8 mm', '28 mm', '0.028 mm'],
      correctIndex: 0,
      solution:
          'r = mv/(qB) = (9.1×10⁻³¹ × 10⁶)/(1.6×10⁻¹⁹ × 0.02) = 9.1×10⁻²⁵ / 3.2×10⁻²¹ ≈ 2.84×10⁻⁴ m ≈ 0.28 mm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A charged particle enters a magnetic field at an angle of 45° to the field lines. Its resulting trajectory is:',
      options: ['A straight line', 'A perfect circle', 'A helix with varying pitch', 'A helix with uniform pitch'],
      correctIndex: 3,
      solution:
          'The velocity component along B is unaffected (constant), and the perpendicular component causes uniform circular motion — combined, this produces a helix with CONSTANT (uniform) pitch, since both components are individually constant.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'In a velocity selector, a charged particle passes undeflected through crossed electric field E and magnetic field B. The particle\'s speed is:',
      options: ['E×B', 'E/B', 'B/E', 'E+B'],
      correctIndex: 1,
      solution: 'Undeflected motion requires electric force = magnetic force: qE = qvB → v = E/B.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Two particles, a proton and an electron, enter the same magnetic field with equal speed and perpendicular to B. Compared to the electron\'s circular radius, the proton\'s radius is:',
      options: [
        'Much smaller (proton is more massive but this doesn\'t matter)',
        'Much larger, since r ∝ mass and the proton is far more massive',
        'Exactly equal',
        'Zero, since protons don\'t curve',
      ],
      correctIndex: 1,
      solution: 'r = mv/(qB). Same v, B, and |q|, but proton mass is about 1836× the electron mass, so r_proton ≫ r_electron.',
    ),
  ],
  revision: [
    'F = qv×B is always perpendicular to velocity, so magnetic force does ZERO work — speed never changes.',
    'Perpendicular entry (v⊥B) produces perfect circular motion with radius r = mv/(qB).',
    'Angled entry produces a helix: circular motion perpendicular to B, plus steady drift along B.',
    'Period T = 2πm/(qB) is INDEPENDENT of speed — the basis of cyclotron operation.',
    'F = qvB sinθ is maximum at θ=90°, zero at θ=0° (motion parallel to B is a straight line).',
    'Velocity selector: undeflected motion requires v = E/B (electric and magnetic forces balance).',
  ],
  sandboxBuilder: (_) => const ChargeInFieldSandbox(),
);
