import '../../models/lesson.dart';
import '../../simulators/heat_transfer_sim.dart';
import '../../theme/tokens.dart';

/// Heat Transfer — conduction, convection and radiation, and how fast heat moves.
final Lesson heatTransferLesson = Lesson(
  topicId: 'heat-transfer',
  title: 'Heat Transfer',
  accentColor: Palette.chThermal,
  bigQuestion:
      'Touch a metal spoon and a wooden spoon that have both been sitting in the same room all day — the metal one feels distinctly colder, even though a thermometer shows they are at EXACTLY the same temperature. If they\'re the same temperature, why does one feel colder?',
  whyItMatters:
      'Heat transfer explains everything from why your house loses warmth in winter to why a thermos keeps coffee hot to how the Sun warms the Earth across empty space. NEET and JEE test all three modes — conduction (Fourier\'s law), convection, and radiation (Stefan-Boltzmann) — often in the same problem set, and thermal resistance combinations are a favourite numerical trick borrowed straight from circuit theory.',
  prediction: const PredictionPrompt(
    scenario:
        'A metal rod and a wooden rod of the SAME length and cross-section both connect a hot reservoir to a cold reservoir at the same two temperatures. Which one conducts heat faster?',
    options: [
      'The wooden rod — wood insulates heat sources better',
      'The metal rod — its high thermal conductivity lets heat flow through much faster',
      'Both conduct heat at exactly the same rate — length and area are equal',
      'Neither conducts any heat unless they are touching a flame',
    ],
    correctIndex: 1,
    reveal:
        'Fourier\'s law dQ/dt = kAΔT/L shows the rate depends directly on thermal conductivity k — and metals have k values roughly 100-1000× larger than wood. In the lab, switch the rod material from wood to copper and watch the heat-flow rate (and how fast the far end heats up) shoot up dramatically for the same ΔT, A and L.',
  ),
  experiments: [
    'Switch material from wood to copper and watch the conduction rate increase dramatically',
    'Increase the rod length L and see the heat flow rate drop proportionally',
    'Increase cross-sectional area A and see the heat flow rate rise proportionally',
    'Increase the temperature difference ΔT between the ends and watch flow rate rise linearly',
    'Compare radiative heat loss at different surface temperatures — notice the very steep T⁴ rise',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Heat always flows spontaneously from a hotter body to a colder one, and it does so through three distinct mechanisms. CONDUCTION is heat transfer through direct molecular contact within a solid (or between touching solids) — fast-vibrating molecules jostle their slower neighbours. CONVECTION is heat carried by the bulk movement of a fluid (liquid or gas) — hot fluid rises, cool fluid sinks, creating circulation currents. RADIATION is heat transfer via electromagnetic waves and needs no medium at all — it is the only mode that works through a vacuum.',
      title: 'Three modes of heat transfer',
    ),
    ContentBlock.formula('dQ/dt = kA(ΔT)/L', title: 'FOURIER\'S LAW OF CONDUCTION'),
    ContentBlock.bullets([
      'k = thermal conductivity, a material property (high for metals, low for insulators like wood, air, wool)',
      'A = cross-sectional area through which heat flows',
      'ΔT = temperature difference between the two ends/faces',
      'L = thickness/length of the conducting path',
      'Rate of heat flow ∝ A·ΔT, and ∝ 1/L — thick insulation and small area both slow conduction',
    ]),
    ContentBlock.paragraph(
      'Why does a metal spoon feel colder than a wooden one at the same temperature? Your skin senses the RATE at which heat leaves your hand, not the object\'s temperature directly. Metal\'s high k pulls heat out of your fingers much faster than wood does, so it feels colder even though a thermometer reads identical temperatures for both. This is a classic case of confusing temperature (a state) with heat flow rate (a process).',
      title: 'Why metal feels colder than wood',
    ),
    ContentBlock.realLife(
      'Double-glazed windows trap a layer of low-conductivity air (or gas) between two panes of glass specifically to slow conduction; a thermos flask uses a vacuum jacket (kills conduction and convection entirely) plus a silvered surface (reflects radiation) to keep drinks hot or cold for hours; the entire idea of "insulation" in buildings is about maximizing thermal resistance to slow conductive heat loss.',
    ),
    ContentBlock.formula('E = σT⁴', title: 'STEFAN–BOLTZMANN LAW (RADIATION)'),
    ContentBlock.paragraph(
      'Every object above absolute zero radiates electromagnetic energy, and the Stefan-Boltzmann law says the power radiated per unit area grows as the FOURTH POWER of absolute temperature. This T⁴ dependence is extremely steep — doubling an object\'s absolute temperature increases its radiated power by a factor of 16. Radiation is the only heat-transfer mode that works across a vacuum, which is how the Sun\'s heat crosses 150 million km of empty space to reach Earth.',
      title: 'Radiation grows explosively with temperature',
    ),
    ContentBlock.mistake(
      'Believing conduction, convection and radiation are mutually exclusive — in reality, most real-world heat loss (like a hot cup of tea cooling) happens through all three at once. Exam problems often isolate just one mode for simplicity, but always check which mode(s) the question is actually describing.',
    ),
    ContentBlock.mistake(
      'Forgetting that Stefan-Boltzmann requires ABSOLUTE temperature (Kelvin), not Celsius. Since the law involves T⁴, plugging in Celsius values gives wildly wrong answers — always convert to Kelvin first (K = °C + 273) before applying E = σT⁴.',
    ),
    ContentBlock.example(
      'A copper rod (k = 400 W/m·K) of length 2 m and cross-section 0.01 m² connects a hot end at 100°C to a cold end at 20°C. Find the rate of heat conduction.\n\ndQ/dt = kAΔT/L = 400 × 0.01 × (100−20) / 2\n= 400 × 0.01 × 80 / 2\n= 320/2 = 160 W.',
    ),
    ContentBlock.jeeTip(
      'Thermal resistance R_th = L/(kA) behaves exactly like electrical resistance: rods in SERIES add resistances directly (R_total = R₁+R₂+…), while rods in PARALLEL combine as 1/R_total = 1/R₁+1/R₂+…. The heat-flow rate is then dQ/dt = ΔT/R_th, a direct analogue of Ohm\'s law I = V/R. This lets you reuse all your circuit-solving intuition for conduction problems.',
    ),
    ContentBlock.neetNote(
      'NEET often tests the qualitative ranking of conductivities: silver/copper (excellent conductors) > aluminium/iron > water > wood/glass > air/vacuum (excellent insulators). Also remember Newton\'s law of cooling as a related idea: the rate of cooling of a body is proportional to the temperature difference between the body and its surroundings, for small ΔT — this underlies many convection-adjacent numerical problems.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Consider a slab conducting heat under steady state',
      math: 'Heat flows from hot face (T_h) to cold face (T_c) through thickness L, area A',
      note: 'Steady state means the temperature profile inside the slab does not change with time.',
    ),
    DerivationStep(
      title: 'State the experimental proportionalities',
      math: 'dQ/dt ∝ A,   dQ/dt ∝ (T_h − T_c),   dQ/dt ∝ 1/L',
      note: 'More area lets more heat pass; bigger temperature gap drives faster flow; thicker material impedes flow.',
    ),
    DerivationStep(
      title: 'Combine into one relation with a proportionality constant',
      math: 'dQ/dt = k·A·(T_h − T_c)/L',
      note: 'k is the thermal conductivity, a property unique to each material.',
    ),
    DerivationStep(
      title: 'Define thermal resistance by analogy with Ohm\'s law',
      math: 'dQ/dt = ΔT / R_th,   R_th = L/(kA)',
      note: 'Just as V = IR relates voltage/current/resistance, ΔT = (dQ/dt)·R_th relates temperature drop to heat current and thermal resistance.',
    ),
    DerivationStep(
      title: 'Extend to slabs in series (same heat current through each)',
      math: 'R_total = R₁ + R₂ + R₃ + …',
      note: 'Just like resistors in series — each layer adds its own resistance to the total.',
    ),
  ],
  formulas: const [
    FormulaEntry('Fourier\'s law of conduction', 'dQ/dt = kA·ΔT/L'),
    FormulaEntry('Thermal resistance', 'R_th = L/(kA)'),
    FormulaEntry('Heat current (Ohm\'s law analogue)', 'dQ/dt = ΔT/R_th'),
    FormulaEntry('Series thermal resistance', 'R_total = R₁ + R₂ + …'),
    FormulaEntry('Parallel thermal resistance', '1/R_total = 1/R₁ + 1/R₂ + …'),
    FormulaEntry('Stefan–Boltzmann law', 'E = σT⁴', condition: 'T in Kelvin, σ = 5.67×10⁻⁸ W/m²K⁴'),
    FormulaEntry('Newton\'s law of cooling', 'dT/dt ∝ (T − T_surroundings)', condition: 'small ΔT'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Heat transfer through a vacuum is only possible via:',
      options: ['Conduction', 'Convection', 'Radiation', 'None of these'],
      correctIndex: 2,
      solution: 'Radiation is the only mode that requires no medium — it travels as electromagnetic waves, which propagate through vacuum.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'In Fourier\'s law dQ/dt = kAΔT/L, doubling the thickness L (all else constant) will:',
      options: ['Double the heat flow rate', 'Halve the heat flow rate', 'Leave it unchanged', 'Quadruple it'],
      correctIndex: 1,
      solution: 'Heat flow rate ∝ 1/L, so doubling L halves the rate of conduction.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A metal object and a wooden object are both at room temperature. The metal feels colder to touch because:',
      options: [
        'Metal is actually at a lower temperature',
        'Metal has higher thermal conductivity and draws heat from the hand faster',
        'Wood absorbs heat from the hand',
        'Metal has a negative specific heat',
      ],
      correctIndex: 1,
      solution: 'Both are at the same temperature, but metal\'s much higher k conducts heat away from your skin faster, giving a colder sensation.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If the absolute temperature of a black body is doubled, the power radiated per unit area becomes:',
      options: ['2 times', '4 times', '8 times', '16 times'],
      correctIndex: 3,
      solution: 'E = σT⁴. Doubling T multiplies E by 2⁴ = 16.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A rod conducts heat at rate P when its ends are at temperatures T₁ and T₂. If both the length and cross-sectional area are doubled (ΔT unchanged), the new rate is:',
      options: ['P/2', 'P', '2P', '4P'],
      correctIndex: 1,
      solution: 'Rate ∝ A/L. Doubling both A and L leaves the ratio A/L (and hence the rate) unchanged.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two rods of the same length and area but thermal conductivities k₁ and k₂ are joined end-to-end (in series) between temperatures T_h and T_c. The equivalent conductivity is:',
      options: ['(k₁+k₂)/2', '2k₁k₂/(k₁+k₂)', 'k₁+k₂', '√(k₁k₂)'],
      correctIndex: 1,
      solution:
          'Series thermal resistances add: R_total = L/(k₁A) + L/(k₂A) = (2L)/(k_eq·A). Solving: k_eq = 2k₁k₂/(k₁+k₂), the harmonic-mean-like series combination.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A copper rod (k = 400 W/m·K), length 1 m, area 2×10⁻⁴ m², has its ends maintained at 100°C and 0°C. The rate of heat flow is:',
      options: ['4 W', '8 W', '40 W', '80 W'],
      correctIndex: 1,
      solution: 'dQ/dt = kAΔT/L = 400 × 2×10⁻⁴ × 100 / 1 = 8 W.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two identical rods conducting heat are connected in PARALLEL between the same two temperatures, instead of one rod alone. The combined heat flow rate compared to a single rod\'s rate P is:',
      options: ['P/2', 'P', '2P', '4P'],
      correctIndex: 2,
      solution: 'Parallel paths each carry rate P independently (same ΔT, same k, A, L per rod), so total flow = P + P = 2P.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Which of the following best explains why a thermos flask keeps liquids hot for a long time?',
      options: [
        'It uses a material with very high thermal conductivity',
        'It has a vacuum jacket (blocks conduction/convection) and silvered walls (reflect radiation)',
        'It actively cools the outside air',
        'It relies purely on convection to retain heat',
      ],
      correctIndex: 1,
      solution: 'A thermos minimizes ALL three heat-loss modes: vacuum stops conduction and convection, and a silvered (reflective) surface minimizes radiative loss.',
    ),
  ],
  revision: [
    'Three modes: conduction (contact), convection (fluid bulk motion), radiation (EM waves, works in vacuum).',
    'Fourier\'s law: dQ/dt = kAΔT/L — rate ∝ area and ΔT, inversely ∝ thickness.',
    'Metal feels colder than wood at the same temperature because it conducts heat away from skin faster.',
    'Thermal resistance R_th = L/(kA) behaves like electrical resistance: series adds, parallel combines reciprocally.',
    'Stefan-Boltzmann: E = σT⁴ (T in Kelvin) — radiated power grows steeply with temperature.',
    'Insulation (double glazing, thermos vacuum jackets) works by maximizing thermal resistance / blocking modes.',
  ],
  sandboxBuilder: (_) => const HeatTransferSimulator(),
);
