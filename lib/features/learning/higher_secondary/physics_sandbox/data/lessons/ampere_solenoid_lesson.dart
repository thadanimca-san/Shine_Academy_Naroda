import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../simulators/ampere_solenoid_sandbox.dart';

/// Ampere's Circuital Law & the Solenoid — symmetry shortcuts for B-fields.
final Lesson ampereSolenoidLesson = Lesson(
  topicId: 'ampere-solenoid',
  title: 'Ampere\'s Law & the Solenoid',
  bigQuestion:
      'Integrating Biot–Savart over every turn of a coil sounds like a nightmare of calculus. Yet the field inside a long solenoid turns out to be a shockingly simple, exactly uniform B = μ₀nI. How does symmetry let us skip the hard integral entirely?',
  whyItMatters:
      'Ampere\'s circuital law is the magnetic twin of Gauss\'s law — both let you find fields instantly IF the source has enough symmetry, by choosing a clever imaginary loop instead of grinding through Biot–Savart. The solenoid result B = μ₀nI is one of the most quoted formulas in the magnetism chapter, and it is the working principle behind every electromagnet, MRI magnet, and relay coil.',
  prediction: const PredictionPrompt(
    scenario:
        'A long solenoid carries current I with n turns per metre. You double the number of turns per metre (pack them twice as densely) but keep I the same. The field inside becomes:',
    options: [
      'The same (only current matters)',
      'Twice as large (B ∝ n)',
      'Four times as large (B ∝ n²)',
      'Half as large (more turns means more resistance)',
    ],
    correctIndex: 1,
    reveal:
        'B = μ₀nI is directly proportional to n, the number of turns per unit length. In the lab, drag the turn-density slider up and watch B exactly double when n doubles — and notice the field stays essentially uniform inside no matter what the coil radius is.',
  ),
  experiments: [
    'Raise the turn density n and watch the parallel field lines inside get labeled with a bigger B reading, while the sparse field outside barely changes',
    'Double the current I and confirm B doubles (B ∝ I, same as n)',
    'Notice the field lines inside are parallel and evenly spaced — just like a bar magnet\'s field between its poles',
    'Observe that outside the solenoid the field is drawn very faint — for a long, tightly wound coil it is essentially zero there',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Ampere\'s circuital law is a shortcut for finding magnetic fields when the current distribution has enough symmetry — exactly the role Gauss\'s law plays for electric fields with charge symmetry. Instead of summing Biot–Savart contributions element by element, you choose an imaginary closed loop (an "Amperian loop") that matches the symmetry of the problem, and the law hands you B directly.',
      title: 'The magnetic twin of Gauss\'s law',
    ),
    ContentBlock.formula('∮ B·dl = μ₀ I_enclosed', title: 'AMPERE\'S CIRCUITAL LAW'),
    ContentBlock.bullets([
      'The line integral of B around ANY closed loop equals μ₀ times the current enclosed by that loop',
      'Only the ENCLOSED current matters — currents outside the loop contribute nothing to the integral',
      'Just like Gauss\'s law, this is exact always, but only USEFUL for finding B directly when symmetry lets you pull B outside the integral',
    ]),
    ContentBlock.paragraph(
      'To find the field inside a long solenoid, draw a rectangular Amperian loop: one long side buried deep inside the solenoid (where the field is uniform, parallel to the axis), the opposite long side far outside (where B ≈ 0), and two short sides perpendicular to B (contributing zero to the integral since B·dl = 0 there when B is parallel to the axis).',
      title: 'The rectangular loop trick for a solenoid',
    ),
    ContentBlock.formula('B = μ₀ n I', title: 'FIELD INSIDE A LONG SOLENOID (n = turns per unit length)'),
    ContentBlock.bullets([
      'B is essentially UNIFORM throughout the interior — same magnitude, same direction, independent of position on the axis (as long as you\'re far from the ends) and independent of the solenoid\'s radius',
      'B is essentially ZERO outside a long, tightly-wound solenoid',
      'Direction inside: right-hand rule — curl fingers along the direction of current flow in the turns, thumb points along B',
    ]),
    ContentBlock.paragraph(
      'This uniform interior field is exactly what a bar magnet\'s field looks like between well-separated poles — which is why a current-carrying solenoid behaves just like a bar magnet, with a north pole at one end and a south pole at the other, for as long as current flows.',
      title: 'A solenoid behaves like a bar magnet',
    ),
    ContentBlock.paragraph(
      'A toroid is a solenoid bent into a doughnut shape, so its own field lines never have to "leave" and re-enter — no end effects at all. Applying Ampere\'s law to a circular loop of radius r running through the toroid\'s core (enclosing N turns total) gives a clean standard result.',
      title: 'The toroid: a solenoid with no ends',
    ),
    ContentBlock.formula('B = μ₀NI / 2πr', title: 'FIELD INSIDE A TOROID (N = total turns, r = loop radius through the core)'),
    ContentBlock.realLife(
      'Electromagnets are solenoids wound around an iron core, and they are everywhere: scrapyard cranes that lift and drop entire cars by switching current on/off, MRI machines (superconducting solenoids producing enormous, extremely uniform fields for imaging), relay switches in cars and appliances, and the electromagnetic locks on many doors.',
    ),
    ContentBlock.mistake(
      'Assuming Ampere\'s law by itself always lets you SOLVE for B. The law is always true, but it only becomes a useful shortcut when the geometry is symmetric enough (straight wire, solenoid, toroid) that you can argue B is constant along your chosen loop and pull it out of the integral. For an irregular current distribution, you\'re back to Biot–Savart.',
    ),
    ContentBlock.mistake(
      'Forgetting that only the ENCLOSED current counts. If your Amperian loop only threads through 3 of a solenoid\'s 500 turns, then I_enclosed in the law is the current in just those 3 turns worth of wire (or, in the rectangular-loop derivation, it is naturally expressed as nI per unit length threading the loop) — not the total current in the entire coil.',
    ),
    ContentBlock.example(
      'A solenoid is 50 cm long, has 1000 turns, and carries 2 A. Find the field inside.\n\nn = 1000/0.5 = 2000 turns/m.\n\nB = μ₀nI = (4π×10⁻⁷)(2000)(2)\n= (1.2566×10⁻⁶)(4000)\n= 5.03×10⁻³ T ≈ 5 mT.\n\nNotice the radius of the solenoid never entered the calculation — only n (turns per length) and I matter for the interior field.',
    ),
    ContentBlock.jeeTip(
      'JEE often gives "N turns over length L" rather than n directly — always compute n = N/L first before plugging into B = μ₀nI. Also remember the toroid result B = μ₀NI/2πr uses TOTAL turns N (not turns per length), since r changes around the ring while N is one fixed number for the whole coil.',
    ),
    ContentBlock.jeeTip(
      'A classic combined problem: a solenoid with a soft iron core has its field boosted by the core\'s relative permeability μr, giving B = μ₀μr n I. This is how real electromagnets achieve fields far stronger than an air-core coil could produce with the same current.',
    ),
    ContentBlock.neetNote(
      'NEET tests the qualitative solenoid facts hardest: field is uniform and strong INSIDE, negligible OUTSIDE, and behaves exactly like a bar magnet. Also expect direct plug-and-chug on B = μ₀nI and the toroid formula B = μ₀NI/2πr — know which N/n definition each formula uses.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State Ampere\'s law and choose the Amperian loop',
      math: '∮ B·dl = μ₀ I_enclosed',
      note: 'Choose a rectangle: side "ab" of length L deep inside the solenoid (parallel to axis), side "cd" of length L far outside, and two short perpendicular sides bc, da.',
    ),
    DerivationStep(
      title: 'Evaluate each side of the rectangle',
      math: '∫_ab B·dl = B·L   (B parallel to dl, uniform inside)\n∫_cd B·dl = 0   (B ≈ 0 outside)\n∫_bc B·dl = ∫_da B·dl = 0   (B ⟂ dl on these sides)',
    ),
    DerivationStep(
      title: 'Total the enclosed current',
      math: 'I_enclosed = (n·L)·I',
      note: 'The rectangle threads through n·L turns, each carrying current I.',
    ),
    DerivationStep(
      title: 'Apply Ampere\'s law and solve for B',
      math: 'B·L = μ₀ (nL) I  ⟹  B = μ₀ n I',
      note: 'The length L cancels — the result is independent of how long a segment you chose, confirming B is truly uniform inside.',
    ),
  ],
  formulas: const [
    FormulaEntry('Ampere\'s circuital law', '∮ B·dl = μ₀ I_enclosed'),
    FormulaEntry('Field inside long solenoid', 'B = μ₀nI', condition: 'n = turns per unit length'),
    FormulaEntry('Field inside toroid', 'B = μ₀NI/2πr', condition: 'N = total turns, r = radius of Amperian loop'),
    FormulaEntry('Field just outside a long solenoid', 'B ≈ 0'),
    FormulaEntry('Solenoid with iron core', 'B = μ₀μᵣnI', condition: 'μᵣ = relative permeability of core'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Ampere\'s circuital law relates the line integral of B around a closed loop to:',
      options: [
        'The total charge enclosed',
        'The current enclosed by the loop',
        'The area of the loop',
        'The potential difference across the loop',
      ],
      correctIndex: 1,
      solution: '∮B·dl = μ₀I_enclosed — only the current threading through the loop determines the circulation of B.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Inside a long current-carrying solenoid, the magnetic field is:',
      options: [
        'Zero',
        'Maximum near the ends and zero at the centre',
        'Uniform and parallel to the axis',
        'Radially outward',
      ],
      correctIndex: 2,
      solution: 'For an ideal long solenoid, the field inside is essentially uniform in magnitude and direction, parallel to the axis — just like the field between the poles of a bar magnet.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A solenoid has 2000 turns over a length of 1 m and carries a current of 5 A. The magnetic field inside is:',
      options: ['6.28×10⁻³ T', '1.26×10⁻² T', '2.5×10⁻³ T', '3.14×10⁻³ T'],
      correctIndex: 1,
      solution: 'n = 2000/1 = 2000 turns/m. B = μ₀nI = (4π×10⁻⁷)(2000)(5) = (1.2566×10⁻⁶)(10000) = 1.2566×10⁻² T ≈ 1.26×10⁻² T.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A toroid has 500 turns and carries 2 A. At a point inside the core at radius 10 cm from the toroid\'s centre, the field is:',
      options: ['1×10⁻³ T', '2×10⁻³ T', '4×10⁻³ T', '5×10⁻⁴ T'],
      correctIndex: 1,
      solution: 'B = μ₀NI/2πr = (4π×10⁻⁷)(500)(2)/(2π×0.10) = (μ₀/2π)(500×2/0.10) = (2×10⁻⁷)(10000) = 2×10⁻³ T.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'If the current in a long solenoid is doubled and the number of turns per unit length is halved, the field inside:',
      options: ['Doubles', 'Halves', 'Stays the same', 'Becomes four times as large'],
      correctIndex: 2,
      solution: 'B = μ₀nI. Doubling I and halving n multiply B by (2)×(1/2) = 1 — the field is unchanged.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The magnetic field just outside a long, tightly-wound solenoid carrying steady current is approximately:',
      options: ['Equal to the field inside', 'Twice the field inside', 'Zero', 'Infinite'],
      correctIndex: 2,
      solution: 'For an ideal long solenoid, the field outside is negligible — nearly all the field is confined inside, unlike a single wire\'s field which extends everywhere.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A rectangular Amperian loop is drawn with one long side deep inside a solenoid and the opposite long side deep outside. Why do the two short (perpendicular) sides contribute zero to ∮B·dl?',
      options: [
        'Because B is zero everywhere on those sides',
        'Because B is perpendicular to dl along those sides, making B·dl = 0',
        'Because those sides have zero length',
        'Because current does not flow through those sides',
      ],
      correctIndex: 1,
      solution: 'Inside the solenoid B is parallel to the axis; on the short sides (perpendicular to the axis), dl is perpendicular to B, so B·dl = 0 pointwise along the entire short side, even though B itself is not zero there.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A solenoid with an iron core (relative permeability μᵣ = 500) has n = 1000 turns/m and carries 1 A. The field inside compared to an identical air-core solenoid is:',
      options: ['The same', '500 times larger', '500 times smaller', 'Independent of the core material'],
      correctIndex: 1,
      solution: 'B = μ₀μᵣnI. The iron core multiplies the field by its relative permeability μᵣ = 500 compared to the air-core value μ₀nI — this is exactly why electromagnets use iron cores.',
    ),
  ],
  revision: [
    'Ampere\'s law: ∮B·dl = μ₀I_enclosed — the magnetic twin of Gauss\'s law, useful when symmetry lets B come out of the integral.',
    'Long solenoid: B = μ₀nI inside (uniform, along the axis), B ≈ 0 outside.',
    'Toroid: B = μ₀NI/2πr, using TOTAL turns N (unlike solenoid\'s per-length n).',
    'A current-carrying solenoid behaves like a bar magnet: N pole at one end, S pole at the other.',
    'Iron cores boost the field: B = μ₀μᵣnI — the working principle of every electromagnet.',
    'Real-life: cranes, MRI magnets, relays, and electromagnetic locks are all long solenoids.',
  ],
  sandboxBuilder: (_) => const AmpereSolenoidSandbox(),
  accentColor: const Color(0xFF6D28D9),
);
