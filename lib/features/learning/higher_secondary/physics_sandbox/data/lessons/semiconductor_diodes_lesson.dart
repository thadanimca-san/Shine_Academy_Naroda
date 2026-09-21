import '../../models/lesson.dart';
import '../../simulators/semiconductor_diodes_sandbox.dart';
import '../../theme/tokens.dart';

/// Semiconductors & Diodes — band gaps, doping, and the p-n junction as a one-way valve.
final Lesson semiconductorDiodesLesson = Lesson(
  topicId: 'semiconductor-diodes',
  title: 'Semiconductors & Diodes',
  accentColor: Palette.chModern,
  bigQuestion:
      'Every phone, computer, and solar panel in the world runs on a material that is neither a good conductor like copper nor a good insulator like rubber — it deliberately sits in between. Why would engineers want a material that\'s bad at BOTH extremes, and how does adding tiny, controlled impurities to it turn it into a one-way valve for electricity?',
  whyItMatters:
      'Semiconductors are the foundation of essentially all modern electronics — every transistor, diode, solar cell, and LED depends on the physics in this lesson. NEET and JEE test band theory, doping types, and diode behaviour extensively, and this topic is the conceptual gateway into all of modern digital electronics, including the logic gates covered next.',
  prediction: const PredictionPrompt(
    scenario:
        'A p-n junction diode is connected to a battery in FORWARD bias (p-side to positive terminal, n-side to negative). What happens to the depletion region and current flow?',
    options: [
      'The depletion region widens and no current flows',
      'The depletion region narrows/vanishes and current flows easily',
      'Nothing changes regardless of bias direction',
      'The diode is destroyed instantly',
    ],
    correctIndex: 1,
    reveal:
        'Forward bias pushes majority carriers (holes from p-side, electrons from n-side) toward the junction, shrinking the depletion region and allowing current to flow readily once the bias exceeds the barrier potential (~0.7V for silicon). In the lab, switch the diode to forward bias and watch the depletion region narrow while current flows; switch to reverse bias and watch the depletion region widen while current is blocked.',
  ),
  experiments: [
    'Apply forward bias and watch the depletion region shrink as current flows',
    'Apply reverse bias and watch the depletion region widen while current is blocked',
    'Increase forward voltage past the barrier potential (~0.7V) and watch current rise sharply',
    'Compare an n-type semiconductor (extra electrons) against a p-type (extra holes) in the doping visualization',
    'Watch electrons and holes drift toward the junction and recombine under forward bias',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Materials are classified by how easily they conduct electricity, which depends on their electronic BAND STRUCTURE. Conductors (like copper) have overlapping valence and conduction bands, so electrons flow freely. Insulators (like rubber) have a large band gap — electrons need a huge amount of energy to jump from the valence band (bound) to the conduction band (free) — so almost no conduction occurs at normal temperatures. Semiconductors (like silicon) have a SMALL band gap, small enough that a modest amount of thermal energy can occasionally push some electrons across, giving them conductivity between the two extremes.',
      title: 'Conductors, insulators, semiconductors — the band gap',
    ),
    ContentBlock.bullets([
      'Conductor: no band gap (bands overlap) — abundant free electrons, excellent conduction',
      'Insulator: large band gap (several eV) — essentially no free electrons at room temperature',
      'Semiconductor: small band gap (~1 eV for silicon) — some electrons cross thermally, giving moderate, TUNABLE conductivity',
    ]),
    ContentBlock.paragraph(
      'A pure (undoped) semiconductor is called INTRINSIC — its conductivity comes only from thermally generated electron-hole pairs, and is quite low and hard to control. Doping deliberately adds a tiny, controlled amount of impurity atoms to create an EXTRINSIC semiconductor with dramatically enhanced, controllable conductivity. Adding a pentavalent impurity (like phosphorus, 5 valence electrons) to silicon (4 valence electrons) creates an N-TYPE semiconductor, with an extra free electron per dopant atom. Adding a trivalent impurity (like boron, 3 valence electrons) creates a P-TYPE semiconductor, with a "hole" (missing electron, acting like a positive charge carrier) per dopant atom.',
      title: 'Intrinsic vs extrinsic — the power of doping',
    ),
    ContentBlock.bullets([
      'N-type: majority carriers are electrons (negative); donor impurities (Group 15, pentavalent)',
      'P-type: majority carriers are holes (positive); acceptor impurities (Group 13, trivalent)',
      'Both types remain electrically NEUTRAL overall — doping adds carriers, not net charge',
    ]),
    ContentBlock.paragraph(
      'When p-type and n-type semiconductors are joined to form a p-n junction, electrons from the n-side diffuse across and combine with holes on the p-side near the boundary, and vice versa — this creates a narrow region depleted of free charge carriers called the DEPLETION REGION, with a built-in electric field that opposes further diffusion. This depletion region is the heart of every diode\'s behaviour.',
      title: 'The p-n junction and depletion region',
    ),
    ContentBlock.bullets([
      'Forward bias (p to +, n to −): opposes the built-in field, shrinks the depletion region, current flows easily once past the barrier voltage (~0.7V Si, ~0.3V Ge)',
      'Reverse bias (p to −, n to +): reinforces the built-in field, widens the depletion region, only a tiny leakage current flows',
    ], title: 'Forward vs reverse bias'),
    ContentBlock.realLife(
      'The diode\'s one-way behaviour makes it perfect as a RECTIFIER — converting alternating current (AC, which reverses direction) into direct current (DC, which flows one way) by blocking the reverse half-cycles. This is exactly what happens inside every phone charger and power adapter: AC from the wall socket is rectified by diodes into the DC that charges your battery. LEDs are also diodes, engineered to emit light when forward-biased as electrons and holes recombine at the junction.',
    ),
    ContentBlock.mistake(
      'Believing doped semiconductors carry a net electric charge because they have "extra" electrons or holes. Both n-type and p-type materials are electrically NEUTRAL overall — the dopant atoms themselves are also neutral (just missing or having an extra electron relative to silicon\'s 4 valence electrons), so no net charge is introduced, only extra CARRIERS of charge.',
    ),
    ContentBlock.mistake(
      'Forgetting the barrier/threshold voltage. A diode does not start conducting the instant forward bias is applied — it needs to exceed the barrier potential (~0.7V for silicon, ~0.3V for germanium) before significant current flows, because that voltage is needed just to overcome the built-in field from the depletion region.',
    ),
    ContentBlock.example(
      'A silicon diode (barrier potential 0.7V) is forward biased with a 5V source in series with a 470Ω resistor. Find the current through the circuit.\n\nVoltage across resistor = 5 − 0.7 = 4.3V (diode drop is fixed once conducting).\nI = V/R = 4.3/470 ≈ 9.1 mA.',
    ),
    ContentBlock.jeeTip(
      'For diode circuit problems, use the simple model: treat a forward-biased diode (once conducting) as a fixed voltage drop (0.7V for Si) in series, and treat a reverse-biased diode as an OPEN circuit (infinite resistance, blocking all current, ignoring tiny leakage). This two-state approximation solves the vast majority of exam circuit problems quickly.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests the qualitative comparison table: conductors have resistivity ~10⁻⁸ Ω·m, semiconductors ~10⁻⁵ to 10⁶ Ω·m, insulators >10¹¹ Ω·m. Also remember that a semiconductor\'s conductivity INCREASES with temperature (more thermally generated carriers) — opposite to metals, whose conductivity DECREASES with temperature (more lattice vibration scattering electrons).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the band-gap model of conduction',
      math: 'Electrons need energy ≥ Eg (band gap) to jump from valence to conduction band',
      note: 'Eg ≈ 1.1 eV for silicon, ≈ 0.7 eV for germanium — small enough for thermal excitation at room temperature.',
    ),
    DerivationStep(
      title: 'Introduce doping to create excess carriers',
      math: 'N-type: pentavalent dopant contributes 1 extra free electron per atom (no matching hole)',
      note: 'P-type: trivalent dopant creates 1 hole per atom (accepts an electron from a neighboring bond).',
    ),
    DerivationStep(
      title: 'Join p-type and n-type to form a junction; diffusion begins',
      math: 'Electrons (n-side) and holes (p-side) diffuse across the junction and recombine near the boundary',
    ),
    DerivationStep(
      title: 'Recombination creates a depletion region with a built-in field',
      math: 'Fixed (immobile) ion cores are left behind: negative ions on p-side, positive ions on n-side',
      note: 'This creates an internal electric field pointing from n to p, opposing further diffusion — equilibrium is reached.',
    ),
    DerivationStep(
      title: 'Apply external bias to shift the equilibrium',
      math: 'Forward bias opposes the built-in field (narrows depletion region, current flows); reverse bias reinforces it (widens depletion region, blocks current)',
      note: 'This asymmetric response to bias direction is exactly what makes a diode a one-way valve for current.',
    ),
  ],
  formulas: const [
    FormulaEntry('Band gap (silicon)', 'Eg ≈ 1.1 eV'),
    FormulaEntry('Band gap (germanium)', 'Eg ≈ 0.7 eV'),
    FormulaEntry('Barrier potential (Si diode)', 'V_barrier ≈ 0.7 V'),
    FormulaEntry('Barrier potential (Ge diode)', 'V_barrier ≈ 0.3 V'),
    FormulaEntry('Forward-bias diode model', 'Diode ≈ fixed 0.7V drop when conducting'),
    FormulaEntry('Reverse-bias diode model', 'Diode ≈ open circuit (infinite resistance)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Semiconductors have a band gap that is:',
      options: ['Zero (bands overlap)', 'Very large (several eV)', 'Small, allowing some thermal excitation', 'Undefined'],
      correctIndex: 2,
      solution: 'Semiconductors have a small band gap (~1 eV) — small enough for thermal energy to occasionally excite electrons across it.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A p-n junction diode conducts easily when:',
      options: ['Reverse biased', 'Forward biased beyond the barrier potential', 'Not biased at all', 'Only at very low temperature'],
      correctIndex: 1,
      solution: 'Forward bias (exceeding the barrier voltage, ~0.7V for Si) narrows the depletion region and allows current to flow readily.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Doping silicon with phosphorus (5 valence electrons) produces:',
      options: ['P-type semiconductor', 'N-type semiconductor', 'An insulator', 'A pure conductor'],
      correctIndex: 1,
      solution: 'Phosphorus, a pentavalent donor, contributes an extra free electron per atom, creating an n-type (electron-majority) semiconductor.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'As temperature increases, the electrical conductivity of a pure semiconductor:',
      options: ['Decreases', 'Increases', 'Stays constant', 'Becomes zero'],
      correctIndex: 1,
      solution: 'Higher temperature generates more electron-hole pairs thermally, increasing the number of charge carriers and hence conductivity — opposite to metals.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In a p-n junction under reverse bias, the depletion region:',
      options: ['Narrows', 'Widens', 'Disappears', 'Stays the same width'],
      correctIndex: 1,
      solution: 'Reverse bias reinforces the built-in field, pulling majority carriers further from the junction and widening the depletion region.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A silicon diode (barrier potential 0.7V) is forward biased by a 3V battery through a 100Ω resistor. The current through the circuit is approximately:',
      options: ['30 mA', '23 mA', '7 mA', '3.7 mA'],
      correctIndex: 1,
      solution: 'V across resistor = 3 − 0.7 = 2.3V. I = V/R = 2.3/100 = 0.023 A = 23 mA.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A half-wave rectifier uses a single diode to convert AC to a pulsating DC. During the half-cycle when the diode is reverse biased, the output voltage across the load is:',
      options: ['Equal to the full input voltage', 'Approximately zero', 'Negative of the input', 'Exactly 0.7V'],
      correctIndex: 1,
      solution: 'A reverse-biased diode blocks current almost completely (acts as an open circuit), so essentially no voltage develops across the load during that half-cycle.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Which statement correctly compares n-type and p-type semiconductors\' overall electric charge?',
      options: [
        'N-type is net negative, p-type is net positive',
        'Both are electrically neutral overall; doping adds charge carriers, not net charge',
        'N-type is net positive, p-type is net negative',
        'Both are net negative due to added electrons',
      ],
      correctIndex: 1,
      solution: 'Dopant atoms are themselves electrically neutral (just different valence electron counts than silicon), so both n-type and p-type materials remain overall neutral — only the number of mobile carriers changes.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'An LED (light-emitting diode) emits light when:',
      options: [
        'Reverse biased, as electrons tunnel through',
        'Forward biased, as electrons and holes recombine at the junction, releasing energy as light',
        'Left unbiased in darkness',
        'Heated externally without any bias',
      ],
      correctIndex: 1,
      solution: 'Forward bias pushes electrons and holes toward the junction where they recombine, releasing their energy difference (roughly equal to the band gap) as emitted photons.',
    ),
  ],
  revision: [
    'Conductors: no band gap. Insulators: large band gap. Semiconductors: small band gap (~1 eV).',
    'Doping creates extrinsic semiconductors: n-type (pentavalent dopant, electron majority), p-type (trivalent dopant, hole majority).',
    'Both n-type and p-type remain electrically neutral overall — doping adds carriers, not charge.',
    'A p-n junction forms a depletion region with a built-in field opposing further diffusion.',
    'Forward bias narrows the depletion region and allows current past the barrier voltage (~0.7V Si).',
    'Reverse bias widens the depletion region and blocks current (diode ≈ open circuit).',
    'Diodes are used as rectifiers (AC→DC) and LEDs (forward-biased recombination emits light).',
  ],
  sandboxBuilder: (_) => const SemiconductorDiodesSandbox(),
);
