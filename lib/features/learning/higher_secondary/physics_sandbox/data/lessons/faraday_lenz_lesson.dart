import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../simulators/faraday_lenz_sandbox.dart';

/// Faraday's Law & Lenz's Law — electromagnetic induction.
final Lesson faradayLenzLesson = Lesson(
  topicId: 'faraday-lenz',
  title: 'Faraday\'s Law & Lenz\'s Law',
  bigQuestion:
      'A coil of wire, sitting perfectly still, has no battery and no obvious power source. Yet the instant you plunge a magnet into it, current flows. Where does that electricity come from, and what decides which way it flows?',
  whyItMatters:
      'Electromagnetic induction is how essentially all the world\'s electricity is generated — every power-station turbine is just a coil spinning in a magnetic field, obeying the exact law you are about to learn. Faraday\'s law (how much EMF) and Lenz\'s law (which direction) together explain generators, transformers, induction cooktops, eddy-current brakes, and the humble dynamo. It is arguably the single most economically important idea in this entire syllabus.',
  prediction: const PredictionPrompt(
    scenario:
        'A bar magnet moves toward a coil at a certain speed, inducing an EMF ε. You now move the SAME magnet toward the SAME coil at DOUBLE the speed. The induced EMF becomes:',
    options: [
      'The same ε (only the magnet\'s strength matters)',
      'Twice as large (2ε)',
      'Four times as large (4ε)',
      'Half as large, since it interacts for less time',
    ],
    correctIndex: 1,
    reveal:
        'EMF is the RATE of change of flux, ε = -dΦ/dt. Moving the magnet twice as fast changes the flux twice as quickly, so the EMF doubles. In the lab, drag the speed slider up and watch the meter reading double for a doubled speed — even though the magnet\'s strength (and hence peak flux) never changed.',
  ),
  experiments: [
    'Push the magnet toward the coil and note which way the galvanometer needle swings',
    'Pull the magnet away and watch the needle swing the OPPOSITE way — the induced current reverses',
    'Raise the speed slider and watch the EMF reading grow, even though nothing about the magnet itself changed',
    'Slow the magnet down until it barely moves — the EMF nearly vanishes even though flux through the coil is still large',
    'Notice EMF is biggest exactly as the magnet passes closest to the coil, where flux is changing fastest — not where flux itself is biggest',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Magnetic flux Φ measures how much magnetic field "passes through" a loop of area A. If the field B makes angle θ with the normal to the loop, only the component of B perpendicular to the loop contributes.',
      title: 'Magnetic flux',
    ),
    ContentBlock.formula('Φ = B·A·cosθ', title: 'MAGNETIC FLUX (unit: weber, Wb)'),
    ContentBlock.paragraph(
      'Faraday discovered that a changing flux through a coil induces an EMF (a voltage that can drive current) in that coil — no battery needed. The faster the flux changes, the bigger the EMF. For a coil of N turns, each turn contributes, so the EMFs add.',
      title: 'Faraday\'s law of electromagnetic induction',
    ),
    ContentBlock.formula('ε = -N · dΦ/dt', title: 'FARADAY\'S LAW'),
    ContentBlock.bullets([
      'EMF depends on the RATE of change of flux, not the flux itself — a huge steady flux induces nothing',
      'Flux can change three ways: changing B (field strength), changing A (loop area), or changing θ (orientation) — or any combination',
      'N turns multiply the effect: stacking more loops of wire in the same changing field gives proportionally more EMF',
    ]),
    ContentBlock.paragraph(
      'Lenz\'s law fixes the direction: the induced current always flows in the direction that OPPOSES the change producing it — not the flux itself, but the CHANGE in flux. If flux is increasing, the induced current creates its own field to oppose the increase; if flux is decreasing, the induced current tries to maintain it. This opposition is exactly what the minus sign in Faraday\'s law encodes.',
      title: 'Lenz\'s law: direction of the induced current',
    ),
    ContentBlock.paragraph(
      'The minus sign is not a mathematical decoration — it is energy conservation in disguise. If the induced current instead REINFORCED the change (a violation of Lenz\'s law), flux would spiral faster and faster, generating ever-more energy from nothing. Because the induced current opposes the change, you must do mechanical work to push a magnet into a coil against the induced repulsion — and that work is exactly what becomes the electrical energy delivered by the induced current.',
      title: 'The minus sign IS energy conservation',
    ),
    ContentBlock.paragraph(
      'When a straight conducting rod of length L slides with speed v perpendicular to a field B (sweeping out area and hence changing flux), the induced EMF has a clean direct formula — this is called motional EMF, and it is just Faraday\'s law applied to a growing-area loop.',
      title: 'Motional EMF: a special case',
    ),
    ContentBlock.formula('ε = B·L·v', title: 'MOTIONAL EMF (rod of length L moving at speed v ⟂ to B)'),
    ContentBlock.realLife(
      'Induction cooktops pass a rapidly alternating current through a coil beneath the glass surface; the changing flux induces swirling "eddy currents" directly in the base of a ferromagnetic pot, and I²R heating in the pot itself cooks the food — the cooktop surface itself never gets hot. Electric generators in every power station are coils forced to rotate in a magnetic field, continuously changing flux to produce EMF. Eddy-current braking in trains and roller-coasters uses induced currents in a moving conductor to oppose its own motion, providing smooth, contact-free braking (a direct consequence of Lenz\'s law).',
    ),
    ContentBlock.mistake(
      'Saying the induced current opposes the FLUX. It does not — it opposes the CHANGE in flux. If flux through a coil is large but constant, there is zero induced EMF and zero induced current, no matter how strong that steady flux is. Only a changing flux induces anything.',
    ),
    ContentBlock.mistake(
      'Forgetting the N (number of turns) in ε = -NdΦ/dt. A single loop and a 500-turn coil in the identical changing field produce very different EMFs — the 500-turn coil gives 500 times more EMF for the same dΦ/dt per turn.',
    ),
    ContentBlock.example(
      'A single-turn coil of area 0.02 m² sits in a field that increases uniformly from 0.2 T to 0.6 T in 0.4 s, with the field perpendicular to the coil. Find the induced EMF.\n\nΔΦ = ΔB·A = (0.6−0.2)(0.02) = 0.4×0.02 = 0.008 Wb.\n\nε = N·ΔΦ/Δt = 1 × 0.008/0.4 = 0.02 V = 20 mV.\n\nThe minus sign only tells you the DIRECTION opposes the increase — for magnitude, just report 20 mV.',
    ),
    ContentBlock.jeeTip(
      'Eddy currents dissipate energy as heat (I²R losses) in bulk conductors — this is exploited in induction heating/braking but is a NUISANCE in transformer cores and motor housings, where it wastes energy. Laminating the iron core (thin sheets insulated from each other) breaks up the eddy-current loops and cuts this loss dramatically — a favourite JEE conceptual question.',
    ),
    ContentBlock.jeeTip(
      'For a rod rotating about one end in a field B (like a spoke), the "motional EMF" formula generalises to ε = ½BωL², derived by integrating εrod = Bvdr = Bωr·dr from 0 to L. Recognise this as just Faraday\'s law applied to the changing swept area.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks to identify which of the three flux-change methods (changing B, changing A, changing θ) applies in a given scenario — e.g., an AC generator changes θ (a coil rotating in a fixed field), while a sliding rod changes A. Also remember: Φ is measured in weber (Wb), and 1 Wb = 1 T·m².',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define flux through a loop',
      math: 'Φ = B·A·cosθ',
      note: 'θ is the angle between B and the area vector (normal to the loop).',
    ),
    DerivationStep(
      title: 'State Faraday\'s law for the rate of change',
      math: 'ε = -N dΦ/dt',
      note: 'The minus sign (Lenz\'s law) fixes the direction; magnitude uses |dΦ/dt|.',
    ),
    DerivationStep(
      title: 'Specialise to a rod sweeping area at speed v',
      math: 'dΦ/dt = B·(dA/dt) = B·L·v   (dA/dt = L·v for a rod of length L)',
      note: 'The rod sweeps out a strip of area L·v every second, perpendicular to B.',
    ),
    DerivationStep(
      title: 'Read off the motional EMF',
      math: 'ε = B·L·v',
      note: 'Same physics as Faraday\'s law, just applied to a growing-area geometry instead of a changing field.',
    ),
    DerivationStep(
      title: 'Confirm energy conservation via the opposing force',
      math: 'F_opposing = BIL,  Power_mechanical = F·v = BILv = εI = Power_electrical',
      note: 'The work you do pushing against the induced opposing force exactly equals the electrical power delivered — no energy is created or destroyed.',
    ),
  ],
  formulas: const [
    FormulaEntry('Magnetic flux', 'Φ = B·A·cosθ'),
    FormulaEntry('Faraday\'s law', 'ε = -N·dΦ/dt'),
    FormulaEntry('Motional EMF', 'ε = BLv', condition: 'rod of length L, speed v ⟂ B'),
    FormulaEntry('Rotating rod EMF', 'ε = ½BωL²', condition: 'rod rotating about one end'),
    FormulaEntry('Unit of flux', '1 Wb = 1 T·m²'),
    FormulaEntry('Induced current', 'I = ε/R', condition: 'R = resistance of the circuit'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'An induced EMF is produced in a coil when:',
      options: [
        'A steady magnetic field passes through it',
        'The magnetic flux through it changes with time',
        'The coil carries a steady current',
        'The coil is placed in a vacuum',
      ],
      correctIndex: 1,
      solution: 'Faraday\'s law: ε = -NdΦ/dt. EMF requires a CHANGING flux — a constant flux, however large, induces nothing.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Lenz\'s law is a consequence of the conservation of:',
      options: ['Charge', 'Momentum', 'Energy', 'Magnetic flux'],
      correctIndex: 2,
      solution: 'The induced current opposes the change producing it; if it did not, energy could be created from nothing. The minus sign in Faraday\'s law encodes energy conservation.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A coil of 200 turns and area 0.01 m² experiences a field changing from 0 to 0.5 T in 0.2 s, perpendicular to the coil. The induced EMF is:',
      options: ['1 V', '2.5 V', '5 V', '10 V'],
      correctIndex: 2,
      solution: 'ΔΦ = ΔB×A = 0.5×0.01 = 0.005 Wb. ε = N·ΔΦ/Δt = 200×0.005/0.2 = 1/0.2 = 5 V.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A rod of length 1 m moves at 4 m/s perpendicular to a field of 0.5 T, with both v and the rod perpendicular to B. The motional EMF induced is:',
      options: ['0.5 V', '1 V', '2 V', '4 V'],
      correctIndex: 2,
      solution: 'ε = BLv = 0.5×1×4 = 2 V.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A bar magnet is dropped, north pole first, through a horizontal coil connected to a resistor. Compared to free fall with no coil, the magnet\'s fall through the coil is:',
      options: [
        'Unaffected — magnetism does not resist gravity',
        'Slowed down, because the induced current opposes the magnet\'s motion (Lenz\'s law)',
        'Sped up, because the induced current pulls the magnet through faster',
        'Stopped completely and held in place',
      ],
      correctIndex: 1,
      solution: 'By Lenz\'s law, the induced current creates a field opposing the change in flux, which manifests as a retarding force on the magnet — this is exactly the principle of eddy-current/electromagnetic braking, and it slows (but does not stop) the fall.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Laminating the iron core of a transformer (using thin insulated sheets instead of a solid block) primarily reduces:',
      options: ['Hysteresis loss only', 'Eddy current losses', 'Copper (I²R) loss in the windings', 'Flux leakage'],
      correctIndex: 1,
      solution: 'Lamination breaks the core into thin, mutually insulated sheets, restricting the loops available for eddy currents to circulate in, which cuts the resistive heating loss caused by those induced eddy currents.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A square loop of side 0.2 m and resistance 2 Ω is pulled out of a uniform field of 0.8 T at a constant speed of 3 m/s, with one side always inside the field. The induced current is:',
      options: ['0.12 A', '0.24 A', '0.48 A', '0.6 A'],
      correctIndex: 1,
      solution: 'ε = BLv = 0.8×0.2×3 = 0.48 V. I = ε/R = 0.48/2 = 0.24 A.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A conducting rod of length L rotates with angular speed ω about one end (the pivot), in a field B perpendicular to the plane of rotation. The EMF induced between the pivot and the free end is:',
      options: ['BωL', '½BωL²', 'BωL²', '¼BωL²'],
      correctIndex: 1,
      solution: 'Each element dr at radius r moves at speed v = ωr, contributing dε = B(ωr)dr. Integrating from r=0 (pivot) to r=L (free end): ε = Bω∫₀ᴸ r dr = Bω(L²/2) = ½BωL².',
    ),
  ],
  revision: [
    'Flux: Φ = BA cosθ, measured in weber (Wb).',
    'Faraday\'s law: ε = -NdΦ/dt — EMF depends on the RATE of change of flux, not flux itself.',
    'Lenz\'s law: induced current opposes the CHANGE in flux (not the flux) — this is energy conservation.',
    'Three ways to change flux: changing B, changing A, changing θ — motional EMF (ε=BLv) is the changing-A case.',
    'Real life: generators (changing θ), induction cooktops and eddy-current brakes (induced eddy currents), transformers (changing B).',
    'Laminated cores reduce eddy-current losses; this is a standard JEE/NEET conceptual point.',
  ],
  sandboxBuilder: (_) => const FaradayLenzSandbox(),
  accentColor: const Color(0xFF6D28D9),
);
