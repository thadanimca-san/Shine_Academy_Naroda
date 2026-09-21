import '../../models/lesson.dart';
import '../../simulators/thermo_processes_sim.dart';
import '../../theme/tokens.dart';

/// Thermodynamic Processes — first law, and isothermal/adiabatic/isobaric/isochoric paths.
final Lesson thermoProcessesLesson = Lesson(
  topicId: 'thermo-processes',
  title: 'Thermodynamic Processes',
  accentColor: Palette.chThermal,
  bigQuestion:
      'A bicycle pump gets noticeably warm when you compress air quickly, even though you never touched a flame or heater — you only pushed the piston. Where does that heat come from if no heat was added from outside?',
  whyItMatters:
      'The first law of thermodynamics — energy conservation applied to heat and work — is the foundation of engines, refrigerators, and weather systems, and P-V diagrams are one of the most visually rich, frequently tested tools in JEE. Distinguishing isothermal from adiabatic processes (and reading area-under-curve as work) shows up constantly in both conceptual and numerical questions.',
  prediction: const PredictionPrompt(
    scenario:
        'A gas is compressed rapidly (no time for heat to escape — adiabatic) versus compressed very slowly while in contact with a constant-temperature bath (isothermal), both to the same final volume from the same start. Which process results in a HIGHER final pressure?',
    options: [
      'Isothermal compression gives the higher final pressure',
      'Adiabatic compression gives the higher final pressure',
      'Both give exactly the same final pressure',
      'Neither — pressure doesn\'t depend on how compression happens',
    ],
    correctIndex: 1,
    reveal:
        'In adiabatic compression, no heat escapes, so ALL the work done on the gas raises its internal energy AND temperature, which pushes pressure up further than isothermal compression (where heat escapes to keep T constant). This is exactly why a bicycle pump gets hot — rapid compression is nearly adiabatic. In the lab, compare the two process curves on the P-V diagram and see the adiabatic curve rise more steeply and end at a higher pressure.',
  ),
  experiments: [
    'Run an isothermal compression and watch the P-V curve trace a smooth hyperbola (PV = constant)',
    'Run an adiabatic compression to the same final volume and see it end at a higher pressure',
    'Run an isobaric (constant pressure) expansion and read the horizontal line on the P-V diagram',
    'Run an isochoric (constant volume) process and see a vertical line — zero work done',
    'Measure the area under each curve to compare work done across process types',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The first law of thermodynamics is simply energy conservation: the heat added to a system either raises its internal energy or is used to do work on the surroundings (or both). ΔU is a STATE function — it depends only on the initial and final states, not on the path taken — while Q and W individually DO depend on the path. This distinction is central to understanding why different processes between the same two states can involve very different amounts of heat and work.',
      title: 'The first law: energy bookkeeping',
    ),
    ContentBlock.formula('ΔU = Q − W', title: 'FIRST LAW OF THERMODYNAMICS'),
    ContentBlock.bullets([
      'ΔU = change in internal energy (depends only on temperature, for an ideal gas)',
      'Q = heat added TO the system (positive if absorbed)',
      'W = work done BY the system (positive if the gas expands and pushes outward)',
    ]),
    ContentBlock.paragraph(
      'ISOTHERMAL: temperature stays constant, so ΔU = 0 (for an ideal gas) and all heat added converts directly to work done: Q = W. The gas follows PV = constant, and W = nRT ln(V₂/V₁). ADIABATIC: no heat exchange with surroundings (Q = 0), so ΔU = −W — all work done comes entirely from internal energy, which is why compressing a gas adiabatically heats it up. The gas follows PV^γ = constant, where γ = Cp/Cv is the ratio of specific heats.',
      title: 'Isothermal vs adiabatic',
    ),
    ContentBlock.formula('PV = constant (isothermal)     PV^γ = constant (adiabatic)',
        title: 'THE TWO SIGNATURE CURVES'),
    ContentBlock.paragraph(
      'ISOBARIC: pressure stays constant, so work is simply W = PΔV, and the P-V diagram shows a horizontal line. ISOCHORIC: volume stays constant, so no work is done at all (W = 0, since W = ∫PdV and dV = 0) — all heat added goes directly into raising internal energy, shown as a vertical line on the P-V diagram.',
      title: 'Isobaric and isochoric processes',
    ),
    ContentBlock.paragraph(
      'On a P-V diagram, the AREA under the curve (between the curve and the V-axis, from V₁ to V₂) equals the work done BY the gas during that process. This is true for ANY process, not just simple ones — it is why P-V diagrams are so useful: work becomes a purely geometric quantity you can read off (or integrate) directly from the graph shape.',
      title: 'Reading work off a P-V diagram',
    ),
    ContentBlock.realLife(
      'A bicycle pump heats up during rapid compression because the process is nearly adiabatic — compression happens too fast for heat to escape, so all the work you do goes into raising the air\'s internal energy (and hence temperature). Refrigerators and air conditioners exploit the reverse: rapid adiabatic EXPANSION of a refrigerant cools it dramatically, which is how the cooling coils get cold.',
    ),
    ContentBlock.mistake(
      'Assuming ΔU = 0 for ALL processes, not just isothermal ones. ΔU = 0 is special to isothermal (constant T) processes for an ideal gas, because internal energy of an ideal gas depends ONLY on temperature. In adiabatic, isobaric, or isochoric processes, temperature generally changes, so ΔU is generally NOT zero.',
    ),
    ContentBlock.mistake(
      'Confusing the adiabatic curve\'s steepness with the isothermal curve\'s. On a P-V diagram, the ADIABATIC curve is always STEEPER than the isothermal curve at any point they cross, because PV^γ falls off faster than PV as V increases (since γ > 1). Students often draw them with the wrong relative steepness, leading to wrong sign errors in work comparisons.',
    ),
    ContentBlock.example(
      '2 moles of an ideal gas at 300 K expand isothermally from 0.01 m³ to 0.02 m³. Find the work done by the gas. (R = 8.314 J/mol·K)\n\nW = nRT ln(V₂/V₁) = 2 × 8.314 × 300 × ln(0.02/0.01)\n= 4988.4 × ln(2)\n= 4988.4 × 0.693\n≈ 3457 J.\n\nSince ΔU = 0 (isothermal), all of this work comes directly from heat absorbed: Q = W ≈ 3457 J.',
    ),
    ContentBlock.jeeTip(
      'For any CYCLIC process (the gas returns to its starting state), ΔU over the full cycle is always zero, since internal energy is a state function. This means Q_net = W_net for a complete cycle — the net heat absorbed exactly equals the net work done, and both equal the enclosed AREA of the loop on the P-V diagram. This is the foundation of every heat-engine efficiency calculation.',
    ),
    ContentBlock.neetNote(
      'NEET often tests the sign convention and simple cases: in isochoric processes W = 0 so Q = ΔU entirely; in adiabatic processes Q = 0 so ΔU = −W. Also remember γ (Cp/Cv) is about 1.67 for monatomic gases, 1.4 for diatomic gases — larger γ means the adiabatic curve is steeper relative to isothermal.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the first law for an infinitesimal process',
      math: 'dU = dQ − dW,   dW = P·dV',
      note: 'Work done BY the gas during a small expansion dV at pressure P.',
    ),
    DerivationStep(
      title: 'Apply to an isothermal process (ideal gas, dU = 0)',
      math: '0 = dQ − P·dV  →  dQ = P·dV = (nRT/V)·dV',
      note: 'Using PV = nRT to express P in terms of V at constant T.',
    ),
    DerivationStep(
      title: 'Integrate to find total work in isothermal expansion',
      math: 'W = ∫ᵥ₁ᵥ² (nRT/V) dV = nRT·ln(V₂/V₁)',
    ),
    DerivationStep(
      title: 'Apply the first law to an adiabatic process (dQ = 0)',
      math: 'dU = −dW  →  nCᵥ·dT = −P·dV',
      note: 'Combined with PV = nRT and eliminating T, this leads to a differential relation between P and V.',
    ),
    DerivationStep(
      title: 'Solve the adiabatic differential relation',
      math: 'dP/P = −γ·dV/V  →  ln P = −γ ln V + constant  →  PV^γ = constant',
      note: 'γ = Cp/Cv is the ratio of specific heats — this is the adiabatic equation of state.',
    ),
  ],
  formulas: const [
    FormulaEntry('First law of thermodynamics', 'ΔU = Q − W'),
    FormulaEntry('Work (general)', 'W = ∫P dV', condition: 'area under P-V curve'),
    FormulaEntry('Isothermal work', 'W = nRT ln(V₂/V₁)', condition: 'ΔU = 0'),
    FormulaEntry('Adiabatic equation of state', 'PV^γ = constant', condition: 'Q = 0'),
    FormulaEntry('Isobaric work', 'W = PΔV', condition: 'constant P'),
    FormulaEntry('Isochoric work', 'W = 0', condition: 'constant V'),
    FormulaEntry('Ratio of specific heats', 'γ = Cp/Cv'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For an isochoric (constant volume) process, the work done by the gas is:',
      options: ['Maximum', 'Zero', 'Equal to Q', 'Negative always'],
      correctIndex: 1,
      solution: 'W = ∫PdV = 0 since dV = 0 throughout — no volume change means no work is done.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In an adiabatic process, the heat exchanged with the surroundings is:',
      options: ['Maximum', 'Zero', 'Equal to work done', 'Equal to ΔU'],
      correctIndex: 1,
      solution: 'Adiabatic is defined by Q = 0 — no heat enters or leaves the system.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'For an isothermal process on an ideal gas, the change in internal energy ΔU is:',
      options: ['Positive', 'Negative', 'Zero', 'Equal to Q'],
      correctIndex: 2,
      solution: 'Internal energy of an ideal gas depends only on temperature. Isothermal means T is constant, so ΔU = 0.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'On a P-V diagram, at a point where an isothermal and an adiabatic curve cross, which is steeper?',
      options: ['Isothermal', 'Adiabatic', 'Both equally steep', 'Depends on the gas mass'],
      correctIndex: 1,
      solution: 'The adiabatic curve (PV^γ = constant, γ>1) is always steeper than the isothermal curve (PV = constant) at any crossing point.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A gas expands at constant pressure 2×10⁵ Pa from volume 0.01 m³ to 0.03 m³. The work done by the gas is:',
      options: ['2000 J', '4000 J', '6000 J', '8000 J'],
      correctIndex: 1,
      solution: 'W = PΔV = 2×10⁵ × (0.03−0.01) = 2×10⁵ × 0.02 = 4000 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A gas undergoes a process where 500 J of heat is added and the gas does 200 J of work on the surroundings. The change in internal energy is:',
      options: ['300 J', '700 J', '-300 J', '200 J'],
      correctIndex: 0,
      solution: 'ΔU = Q − W = 500 − 200 = 300 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: '3 moles of an ideal gas at 400 K expand isothermally to twice their initial volume. The work done by the gas is: (R = 8.314 J/mol·K, ln2 = 0.693)',
      options: ['3457 J', '6915 J', '2305 J', '9974 J'],
      correctIndex: 1,
      solution: 'W = nRT ln(V₂/V₁) = 3 × 8.314 × 400 × ln(2) = 9976.8 × 0.693 ≈ 6915 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A gas undergoes a cyclic process on a P-V diagram, tracing a closed loop that encloses area 500 J. The net work done by the gas over one complete cycle is:',
      options: ['0 J (state function)', '500 J', '−500 J depending on loop direction, magnitude 500 J', '250 J'],
      correctIndex: 2,
      solution:
          'For a cyclic process, ΔU = 0 so Q_net = W_net, and W_net equals the enclosed loop area in magnitude — positive (clockwise) or negative (counterclockwise) depending on the direction traversed. Here the magnitude is 500 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A gas is compressed adiabatically. Its temperature:',
      options: ['Decreases', 'Increases', 'Stays constant', 'First increases then decreases'],
      correctIndex: 1,
      solution: 'Adiabatic: Q=0, so ΔU = −W. Compression means work is done ON the gas (W negative for the gas), so ΔU is positive — internal energy and temperature both rise.',
    ),
  ],
  revision: [
    'First law: ΔU = Q − W. ΔU is a state function (path-independent); Q and W are not.',
    'Isothermal: ΔU=0, Q=W=nRT ln(V₂/V₁), curve follows PV=constant.',
    'Adiabatic: Q=0, ΔU=−W, curve follows PV^γ=constant, steeper than isothermal.',
    'Isobaric: W=PΔV (horizontal line). Isochoric: W=0 (vertical line).',
    'Area under a P-V curve = work done by the gas during that process.',
    'For any complete cycle, ΔU=0, so Q_net = W_net = enclosed loop area.',
    'Rapid compression (like a bicycle pump) is nearly adiabatic — that\'s why it heats up.',
  ],
  sandboxBuilder: (_) => const ThermoProcessesSimulator(),
);
