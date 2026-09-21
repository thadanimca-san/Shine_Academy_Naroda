import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../simulators/biot_savart_sandbox.dart';

/// Biot–Savart Law — how a current element builds a magnetic field.
final Lesson biotSavartLesson = Lesson(
  topicId: 'biot-savart',
  title: 'Biot–Savart Law',
  bigQuestion:
      'A stationary charge makes an electric field. Slide that same charge along a wire as a current, and it starts making a completely different kind of field — one that circles the wire instead of pointing away from it. What is the rule for building that field, one tiny piece of wire at a time?',
  whyItMatters:
      'The Biot–Savart law is to magnetism what Coulomb\'s law is to electrostatics — the fundamental brick you sum (integrate) to get the field of any current distribution. Every standard result in the magnetism chapter (straight wire, circular loop, solenoid, toroid) is Biot–Savart integrated over a different shape. Learn the source equation once and the rest becomes geometry.',
  prediction: const PredictionPrompt(
    scenario:
        'A long straight wire carries current I. You move the observation point from r = 2 cm to r = 4 cm (twice as far from the wire). The magnetic field there becomes:',
    options: [
      'The same (only current matters)',
      'Half as large (B ∝ 1/r)',
      'One-fourth as large (B ∝ 1/r²)',
      'Twice as large (field spreads out and adds up)',
    ],
    correctIndex: 1,
    reveal:
        'For a long straight wire, B = μ₀I/2πr — the field falls off as 1/r, NOT 1/r² like the electric field of a point charge. In the lab, drag the observation point twice as far from the wire and watch the field reading drop to exactly half. This gentler fall-off (one power of r instead of two) is because the source is an infinite line of current, not a point.',
  ),
  experiments: [
    'Drag the observation point closer to the wire and watch B climb as 1/r',
    'Double the current I and confirm B exactly doubles (B ∝ I)',
    'Reverse the current direction and watch every field circle flip its sense',
    'Move the point to the far side of the wire — the field direction reverses there too, still tangent to the circle',
    'Notice the field lines are closed circles around the wire, with no start or end point anywhere',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Just as Coulomb\'s law gives the electric field due to a point charge, the Biot–Savart law gives the magnetic field due to a tiny current element — a short length dl of wire carrying current I. You can never isolate a current element in practice (currents flow in closed circuits), but you can slice a real wire into many such elements and add up (integrate) their contributions to get the total field.',
      title: 'The magnetic analogue of Coulomb\'s law',
    ),
    ContentBlock.formula('dB = (μ₀/4π) · I·dl×r̂ / r²', title: 'BIOT–SAVART LAW'),
    ContentBlock.bullets([
      'dB ∝ I — double the current, double every contribution',
      'dB ∝ dl — a longer element contributes more field',
      'dB ∝ 1/r² — field from ONE ELEMENT falls off as inverse-square, just like Coulomb\'s law',
      'dB ∝ sinθ — where θ is the angle between dl and r̂ (from the cross product); the element contributes nothing directly along its own length',
      'μ₀ = 4π×10⁻⁷ T·m/A is the permeability of free space, playing the role ε₀ plays in electrostatics',
    ]),
    ContentBlock.paragraph(
      'The direction of dB is given by dl×r̂ — perpendicular to both the current element and the line to the observation point. In practice, students use the right-hand THUMB rule instead of the cross product: point your right thumb along the current, and your curled fingers show the direction the field circles around the wire.',
      title: 'Right-hand thumb rule',
    ),
    ContentBlock.paragraph(
      'Integrating dB over an entire infinite straight wire (summing every element\'s inverse-square contribution, most of which is weakened by the sinθ factor except near the closest point) gives a clean, exact result — the individual 1/r² pieces combine into an overall 1/r law for the whole wire.',
      title: 'Integrating over a whole wire',
    ),
    ContentBlock.formula('B = μ₀I / 2πr', title: 'FIELD OF A LONG STRAIGHT WIRE'),
    ContentBlock.paragraph(
      'For a circular loop of radius R carrying current I, integrating Biot–Savart over the whole ring gives the field exactly at the centre. Every element of the loop is the same distance R from the centre and contributes field along the same axis, so the pieces add directly (no partial cancellation from geometry).',
      title: 'Field at the centre of a circular loop',
    ),
    ContentBlock.formula('B = μ₀I / 2R', title: 'FIELD AT CENTRE OF A CIRCULAR LOOP (radius R)'),
    ContentBlock.realLife(
      'Every current-carrying wire in your charger cable, motor winding, or MRI magnet is a real-world Biot–Savart source. Compass needles deflecting near a wire (Oersted\'s original 1820 discovery), the magnetic field around overhead power lines, and the coils in an electromagnetic crane are all this law at work, summed over millions of current elements.',
    ),
    ContentBlock.mistake(
      'Confusing magnetic field lines with electric field lines. Electric field lines START on positive charges and END on negative charges — they need a source and a sink. Magnetic field lines have neither: they form CLOSED LOOPS that circle the current forever, because there are no magnetic monopoles (no isolated N or S pole has ever been found). Around a straight wire, B-field lines are simply concentric circles with no beginning or end.',
    ),
    ContentBlock.mistake(
      'Forgetting the sinθ factor and assuming every part of a wire contributes equally to the field at a point. An element of wire pointing directly at (or away from) the observation point (θ = 0°) contributes ZERO field there — only the perpendicular component of the geometry matters, exactly as in a cross product.',
    ),
    ContentBlock.example(
      'A long straight wire carries 10 A. Find the magnetic field 5 cm from the wire.\n\nB = μ₀I/2πr = (4π×10⁻⁷)(10) / (2π × 0.05)\n= (2×10⁻⁷ × 10) / 0.05\n= 2×10⁻⁶ / 0.05\n= 4×10⁻⁵ T = 40 µT.\n\n(For comparison, Earth\'s own field is about 50 µT — a modest 10 A wire held a few centimetres from a compass can visibly deflect it, exactly as Oersted saw.)',
    ),
    ContentBlock.jeeTip(
      'Memorise the constant combination μ₀/4π = 10⁻⁷ T·m/A exactly — it appears in every Biot–Savart numeric problem and saves you from recomputing 4π×10⁻⁷/4π under time pressure. Also know μ₀/2π = 2×10⁻⁷ T·m/A directly, since B = μ₀I/2πr is the single most-used formula in this chapter.',
    ),
    ContentBlock.jeeTip(
      'For a finite straight wire (not infinite), the field at a perpendicular distance r involves the angles subtended at the ends: B = (μ₀I/4πr)(sinφ₁+sinφ₂). Setting both angles to 90° (point exactly opposite the middle of an infinite wire) recovers B = μ₀I/2πr as the special case.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the "no magnetic monopole" idea directly: magnetic field lines never start or end in free space, they always close on themselves — a direct consequence of the vector nature of Biot–Savart\'s source (a current LOOP, not an isolated pole). Also remember: B = μ₀I/2R at the CENTRE of a loop, not μ₀I/2πR — a very common substitution slip.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the field of one current element',
      math: 'dB = (μ₀/4π) · I dl×r̂ / r²',
      note: 'The magnetic analogue of dE = kdq/r² for a point charge, but with a cross product instead of a plain radial direction.',
    ),
    DerivationStep(
      title: 'Set up geometry for an infinite straight wire',
      math: 'r = a/sinθ,   l = a·cotθ   (a = perpendicular distance)',
      note: 'Every element dl at angle θ from the perpendicular contributes dB = (μ₀I/4π)(sinθ/r²)dl, all in the same direction (tangent to the circle through the point).',
    ),
    DerivationStep(
      title: 'Integrate θ from 0 to π for an infinite wire',
      math: 'B = ∫dB = (μ₀I/4πa) ∫₀^π sinθ dθ = (μ₀I/4πa)(2)',
    ),
    DerivationStep(
      title: 'Simplify to the standard result',
      math: 'B = μ₀I / 2πa   (write a → r)',
      note: 'Field circles the wire; magnitude falls as 1/r, direction from the right-hand thumb rule.',
    ),
    DerivationStep(
      title: 'Centre of a circular loop (separate case)',
      math: 'Every element: dB = (μ₀I dl)/(4πR²),  all dB parallel to the axis\nB = (μ₀I)/(4πR²) ∮dl = (μ₀I)/(4πR²)(2πR) = μ₀I/2R',
      note: 'All elements are equidistant (R) from the centre and their field contributions add directly, unlike the straight-wire case.',
    ),
  ],
  formulas: const [
    FormulaEntry('Biot–Savart law (element)', 'dB = (μ₀/4π)·I dl×r̂/r²'),
    FormulaEntry('Permeability of free space', 'μ₀ = 4π×10⁻⁷ T·m/A'),
    FormulaEntry('Useful constant', 'μ₀/4π = 10⁻⁷ T·m/A'),
    FormulaEntry('Field of long straight wire', 'B = μ₀I/2πr'),
    FormulaEntry('Field at centre of circular loop', 'B = μ₀I/2R', condition: 'R = loop radius'),
    FormulaEntry('Finite straight wire', 'B = (μ₀I/4πr)(sinφ₁+sinφ₂)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The magnetic field due to a long straight current-carrying wire varies with distance r as:',
      options: ['1/r', '1/r²', 'r', 'constant'],
      correctIndex: 0,
      solution: 'B = μ₀I/2πr, so B ∝ 1/r — one power of r, not two (unlike the electric field of a point charge).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Magnetic field lines around a straight current-carrying wire are:',
      options: [
        'Straight lines radiating outward',
        'Concentric closed circles around the wire',
        'Lines starting at the wire and ending at infinity',
        'Parallel to the wire',
      ],
      correctIndex: 1,
      solution: 'B-field lines around a wire form closed concentric circles with no start or end — a direct signature of the absence of magnetic monopoles.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A long straight wire carries a current of 5 A. The magnetic field at a perpendicular distance of 10 cm is:',
      options: ['5×10⁻⁶ T', '1×10⁻⁵ T', '4×10⁻⁵ T', '5×10⁻⁵ T'],
      correctIndex: 1,
      solution: 'B = μ₀I/2πr = (2×10⁻⁷)(5)/0.10 = 10⁻⁶/0.10 = 1×10⁻⁵ T.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A circular coil of radius 5 cm carries a current of 2 A. The magnetic field at its centre is (μ₀ = 4π×10⁻⁷ T·m/A):',
      options: ['1.26×10⁻⁵ T', '2.51×10⁻⁵ T', '4×10⁻⁵ T', '6.28×10⁻⁵ T'],
      correctIndex: 1,
      solution: 'B = μ₀I/2R. μ₀ = 4π×10⁻⁷ ≈ 1.2566×10⁻⁶ T·m/A. B = (1.2566×10⁻⁶ × 2)/(2×0.05) = (2.513×10⁻⁶)/(0.10) = 2.51×10⁻⁵ T.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The magnetic field at the centre of a circular loop of radius R carrying current I is B₀. If the radius is doubled keeping current the same, the new field is:',
      options: ['B₀/2', '2B₀', 'B₀/4', '4B₀'],
      correctIndex: 0,
      solution: 'B = μ₀I/2R ∝ 1/R. Doubling R halves B, so the new field is B₀/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Which of the following best explains why magnetic field lines never start or end at a point in space?',
      options: [
        'Magnetic fields are always weaker than electric fields',
        'There are no isolated magnetic monopoles',
        'Current elements always point along the wire',
        'The Biot–Savart constant μ₀ is very small',
      ],
      correctIndex: 1,
      solution: 'Electric field lines terminate on charges (electric monopoles exist). Because no isolated N or S pole (magnetic monopole) has ever been observed, magnetic field lines must always close on themselves.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A straight wire carries current I. At a point P at perpendicular distance r, the wire subtends angles of 30° and 60° at P from the two ends (measured from the perpendicular). The field at P is closest to:',
      options: [
        '(μ₀I/4πr)(sin30°+sin60°)',
        '(μ₀I/4πr)(cos30°+cos60°)',
        '(μ₀I/2πr)',
        '(μ₀I/4πr)(tan30°+tan60°)',
      ],
      correctIndex: 0,
      solution: 'For a finite wire, B = (μ₀I/4πr)(sinφ₁+sinφ₂), where φ₁, φ₂ are the angles the ends subtend with the perpendicular from P. Direct substitution gives (μ₀I/4πr)(sin30°+sin60°).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two long straight parallel wires carry currents I and 2I in the same direction, separated by distance d. The point where the net magnetic field is zero lies:',
      options: [
        'Outside the wires, closer to the wire carrying I',
        'Midway between the two wires',
        'Between the wires, closer to the wire carrying I',
        'Between the wires, closer to the wire carrying 2I',
      ],
      correctIndex: 2,
      solution: 'Between two wires carrying current in the SAME direction, the fields oppose each other (one circles clockwise, the other counterclockwise at points in between), so a null point exists between them. Setting μ₀I/2πx = μ₀(2I)/2π(d−x) gives d−x = 2x → x = d/3 from the wire carrying I — closer to the smaller current, just like the Coulomb null-point logic.',
    ),
  ],
  revision: [
    'Biot–Savart: dB = (μ₀/4π)·I dl×r̂/r² — the source law for every magnetic field shape.',
    'Long straight wire: B = μ₀I/2πr — field falls as 1/r, not 1/r².',
    'Centre of circular loop: B = μ₀I/2R.',
    'Direction: right-hand thumb rule — thumb along I, curled fingers show B.',
    'μ₀ = 4π×10⁻⁷ T·m/A; the handy combination μ₀/4π = 10⁻⁷ T·m/A.',
    'Magnetic field lines are always closed loops — no magnetic monopoles exist, unlike electric field lines which start/end on charges.',
  ],
  sandboxBuilder: (_) => const BiotSavartSandbox(),
  accentColor: const Color(0xFF6D28D9),
);
