import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/meter_bridge_sandbox.dart';

/// Meter Bridge & Potentiometer — precision measurement using a balance
/// point instead of a deflection-based meter.
final Lesson meterBridgeLesson = Lesson(
  topicId: 'meter-bridge',
  title: 'Meter Bridge & Potentiometer',
  bigQuestion:
      'An ordinary ohmmeter draws current from the very component it is measuring, subtly disturbing the answer. Is there a way to measure resistance — or even a battery\'s EMF — so precisely that at the moment of measurement, no current flows through the measuring device at all?',
  whyItMatters:
      'The meter bridge and the potentiometer are the two classic "null method" instruments of the NEET/JEE circuits syllabus — both find an answer by adjusting something until a galvanometer reads exactly zero, at which point the measurement is free of the errors that plague ordinary current-drawing meters. These appear constantly in practical-based NEET questions and are a JEE favourite for testing careful proportional reasoning.',
  prediction: const PredictionPrompt(
    scenario:
        'In a meter bridge, the known resistance S is fixed and you slide the jockey to find the balance point. If you now DOUBLE the known resistance S (keeping the same unknown R), where will the new balance point l move?',
    options: [
      'It stays exactly the same, since only R matters',
      'It moves toward the R-side end (l decreases)',
      'It moves toward the S-side end (l increases)',
      'The bridge can no longer be balanced',
    ],
    correctIndex: 1,
    reveal:
        'The balance condition is R/S = l/(100−l), with l measured from the R-side end. If S doubles while R stays fixed, the ratio R/S is halved — and since l/(100−l) grows as l grows, a SMALLER ratio means a SMALLER l. So the balance point shifts toward the R-side end (l decreases) to keep the ratio consistent. In the lab, raise the S slider and watch the jockey\'s balance position creep toward the left (R) end — trace it against the formula to confirm.',
  ),
  experiments: [
    'Slide the jockey until the galvanometer reads exactly BALANCED (zero) and read off R',
    'Change the known resistance S and re-find the new balance point',
    'Verify R/S = l/(100−l) numerically at two different balance settings',
    'Move the jockey to exactly 50 cm and see what value of S makes it balance there (should equal R)',
    'Push S to its extreme values and watch the balance point crowd toward one end of the wire',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A Wheatstone bridge is a network of four resistances (P, Q, R, S) arranged in a diamond, with a galvanometer connected across one diagonal and a battery across the other. When the bridge is BALANCED — meaning no current flows through the galvanometer — a simple ratio condition holds between the four resistances, regardless of the EMF of the battery or the exact resistance of the galvanometer.',
      title: 'The Wheatstone bridge principle',
    ),
    ContentBlock.formula('P/Q = R/S   (balance condition, no current through the galvanometer)',
        title: 'WHEATSTONE BRIDGE BALANCE'),
    ContentBlock.paragraph(
      'A meter bridge is a practical, compact realisation of the Wheatstone bridge using a single metre of uniform resistance wire in place of two of the four arms. The wire is stretched along a scale, and a sliding contact (jockey) divides it into two lengths, l and (100−l) cm. Since the wire has uniform cross-section and material, its resistance per unit length is constant, so the two wire-segments\' resistances are directly proportional to their lengths — turning the general Wheatstone ratio into a simple length ratio.',
      title: 'The meter bridge: Wheatstone bridge on a wire',
    ),
    ContentBlock.formula('R/S = l/(100 − l)   (meter bridge balance, from the balance length l)',
        title: 'METER BRIDGE FORMULA'),
    ContentBlock.bullets([
      'R is the unknown resistance (connected in one gap), S is a known resistance box (connected in the other gap)',
      'l is measured from the end nearer R to the jockey\'s balance position',
      'At balance, the galvanometer shows zero deflection — no current flows through it',
      'Because no current flows through the galvanometer at balance, the galvanometer\'s own resistance does not affect the measurement at all',
    ]),
    ContentBlock.paragraph(
      'A potentiometer takes the null-method idea further, comparing potential differences (or EMFs) rather than resistances. A long uniform wire carries a steady "driver" current, creating a uniform potential drop per unit length along it. An unknown EMF (or potential difference) is balanced against a length of this wire by sliding a contact until a galvanometer in that branch shows zero deflection — at that exact balance length, the unknown EMF exactly equals the potential drop across that length of wire.',
      title: 'The potentiometer principle',
    ),
    ContentBlock.formula('ε₁/ε₂ = l₁/l₂   (comparing two EMFs via their balance lengths)',
        title: 'POTENTIOMETER — COMPARING EMFs'),
    ContentBlock.paragraph(
      'The potentiometer\'s crucial advantage over an ordinary voltmeter: AT THE BALANCE POINT, it draws ZERO current from the source being measured (the galvanometer reads zero exactly because no current flows through that branch). A voltmeter, by contrast, always draws some current to deflect its needle, which slightly loads the circuit and gives a reading marginally lower than the true EMF. This is why the potentiometer is the preferred instrument for measuring EMF precisely, especially for comparing cells or measuring internal resistance.',
      title: 'Why the potentiometer beats a voltmeter',
    ),
    ContentBlock.realLife(
      'Precision resistance measurement in physics and electronics labs still uses bridge circuits (modern digital multimeters use similar null-balancing principles internally for high-accuracy modes) because they eliminate the systematic error that current-drawing meters introduce. Historically, potentiometers were the gold-standard method for calibrating standard cells and measuring small EMFs before high-impedance digital voltmeters became cheap and widespread.',
    ),
    ContentBlock.mistake(
      'Forgetting END CORRECTIONS in a meter bridge. The metre wire\'s ends are soldered into metal strips (with their own small resistance and contact resistance) that are not part of the ideal 100 cm scale — this introduces a small systematic error, especially when the balance point falls very close to either end (below ~10 cm or above ~90 cm). Best practice is to choose S so the balance point falls near the middle of the wire (between 30 and 70 cm), where end-correction errors are smallest.',
    ),
    ContentBlock.example(
      'In a meter bridge, the balance point is found at l = 40 cm from the end connected to the unknown resistance R, with S = 15 Ω in the other gap. Find R.\n\nR/S = l/(100−l) = 40/60 = 2/3.\n\nR = S × (2/3) = 15 × 2/3 = 10 Ω.',
    ),
    ContentBlock.jeeTip(
      'A classic "trick" question: if the balance point is measured from the S-side instead of the R-side, the ratio flips — R/S = (100−l)/l, not l/(100−l). Always double-check which end the problem measures l from before applying the formula; misreading this is the single most common error in meter-bridge numericals.',
    ),
    ContentBlock.jeeTip(
      'A very useful check: interchanging R and S (swapping the resistance box and unknown resistance to opposite gaps) should move the balance point to (100−l), the mirror position — since the ratio simply inverts. This "swap test" is sometimes used experimentally to average out small errors from unequal wire cross-section.',
    ),
    ContentBlock.neetNote(
      'NEET practical-based questions often ask: why is the galvanometer connected to the middle (jockey) branch rather than in series with the battery? Because it is only used to DETECT the null condition, not to carry current continuously — protecting the (often delicate) galvanometer coil from sustained current. Also expect: the potentiometer\'s balance length is directly proportional to the EMF being measured, assuming the driver current is held constant throughout the comparison.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Balance condition for a general Wheatstone bridge',
      math: 'At balance, no current flows through the galvanometer branch.\n⟹ P/Q = R/S',
      note: 'This follows from applying KVL to both loops of the bridge with zero galvanometer current — see the Kirchhoff\'s Laws lesson for the general method.',
    ),
    DerivationStep(
      title: 'Adapt to the meter bridge: wire segments replace two arms',
      math: 'Left wire segment (length l) plays the role of arm P\nRight wire segment (length 100−l) plays the role of arm Q',
      note: 'Both segments are the same uniform wire, so resistance ∝ length.',
    ),
    DerivationStep(
      title: 'Resistance is proportional to length for uniform wire',
      math: 'P = (resistance/length) × l,   Q = (resistance/length) × (100−l)\n⟹ P/Q = l/(100−l)',
    ),
    DerivationStep(
      title: 'Substitute into the Wheatstone balance condition',
      math: 'R/S = P/Q = l/(100−l)',
      note: 'The proportionality constant (resistance per unit length) cancels out entirely — only the LENGTH RATIO survives.',
    ),
    DerivationStep(
      title: 'Potentiometer: potential drop per unit length is constant',
      math: 'V/L = constant (driver current × resistance per length)\nε = (V/L) × l_balance  ⟹  ε₁/ε₂ = l₁/l₂',
      note: 'Comparing two EMFs against the same wire (same driver current) cancels the constant, leaving a pure length ratio.',
    ),
  ],
  formulas: const [
    FormulaEntry('Wheatstone bridge balance', 'P/Q = R/S'),
    FormulaEntry('Meter bridge balance', 'R/S = l/(100−l)'),
    FormulaEntry('Potentiometer EMF comparison', 'ε₁/ε₂ = l₁/l₂'),
    FormulaEntry('Potential gradient (potentiometer)', 'k = V/L  (volts per unit length)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A Wheatstone bridge is balanced when:',
      options: [
        'The current through the galvanometer is maximum',
        'The current through the galvanometer is zero',
        'All four resistances are equal',
        'The battery current is zero',
      ],
      correctIndex: 1,
      solution: 'Balance is defined precisely as the condition where no current flows through the galvanometer branch, giving P/Q = R/S.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'In a meter bridge experiment, the balance point should ideally be obtained near the middle of the wire because:',
      options: [
        'The wire is thicker there',
        'End-correction errors are minimised near the middle of the scale',
        'The galvanometer is most sensitive there',
        'The battery delivers maximum current there',
      ],
      correctIndex: 1,
      solution: 'Balance points very close to either end are more affected by end-corrections (resistance of the connecting strips/contacts), so choosing S to bring the balance point near the middle (30–70 cm) minimises this systematic error.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In a meter bridge, balance is obtained at l = 60 cm from the unknown-resistance end, with a known resistance S = 12 Ω. The unknown resistance R is:',
      options: ['8 Ω', '12 Ω', '18 Ω', '20 Ω'],
      correctIndex: 2,
      solution: 'R/S = l/(100−l) = 60/40 = 1.5. R = 1.5 × 12 = 18 Ω.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'If the unknown resistance R and known resistance S in a meter bridge are interchanged (swapped to opposite gaps), the new balance point (measured from the same end as before) becomes:',
      options: ['The same as before', '(100 − l), the mirror position', '50 cm always', '2l'],
      correctIndex: 1,
      solution: 'Swapping R and S inverts the ratio: new balance length l\' satisfies S/R = l\'/(100−l\'), which is the reciprocal relation — solving shows l\' = 100 − l, the mirror image of the original balance point.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A potentiometer is preferred over a voltmeter for measuring EMF because:',
      options: [
        'It is cheaper to build',
        'At balance, it draws zero current from the cell being measured, giving the TRUE EMF',
        'It gives a digital readout',
        'It works without a battery',
      ],
      correctIndex: 1,
      solution: 'At the balance point, no current flows through the galvanometer/cell branch, so the potentiometer measures the true EMF without loading the source — unlike a voltmeter, which always draws some current and reads slightly low.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two cells of EMF ε₁ and ε₂ give balance points at 60 cm and 40 cm respectively on a potentiometer wire (same driver current throughout). The ratio ε₁/ε₂ is:',
      options: ['1.5', '0.67', '2.0', '1.0'],
      correctIndex: 0,
      solution: 'ε₁/ε₂ = l₁/l₂ = 60/40 = 1.5.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In a meter bridge, if the balance length l is measured from the wrong end (from the S side instead of the R side), and the correct formula R/S = l/(100−l) is applied anyway, the calculated R will be:',
      options: [
        'Correct, since the formula doesn\'t depend on which end',
        'The reciprocal ratio of the true value (effectively giving S/R × S instead of R)',
        'Exactly double the true value',
        'Exactly half the true value',
      ],
      correctIndex: 1,
      solution: 'Measuring l from the wrong end swaps the roles of l and (100−l) in the ratio, effectively computing S²/R instead of R — a systematic ratio-inversion error. Always confirm which end the balance length is measured from before applying the formula.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The galvanometer in a meter bridge or potentiometer setup is used to:',
      options: [
        'Continuously measure the current flowing through the circuit',
        'Detect the null (zero-current) condition at balance',
        'Supply EMF to the circuit',
        'Measure the resistance of the wire directly',
      ],
      correctIndex: 1,
      solution: 'The galvanometer here is purely a null detector — its job is to show zero deflection at balance, not to continuously measure current, which protects it and avoids errors from its own resistance.',
    ),
  ],
  revision: [
    'Wheatstone bridge balance: P/Q = R/S when the galvanometer carries zero current.',
    'Meter bridge: R/S = l/(100−l), with l the balance length from the R-side end — a practical Wheatstone bridge using a uniform wire.',
    'Potentiometer: ε₁/ε₂ = l₁/l₂ compares EMFs via balance lengths, with a constant driver current.',
    'The potentiometer draws ZERO current at balance, giving the true EMF — superior to a voltmeter, which always loads the circuit.',
    'End corrections matter near the wire\'s ends; aim for a balance point between 30–70 cm for accuracy.',
    'Swapping R and S mirrors the balance point to (100−l) — a useful experimental cross-check.',
  ],
  sandboxBuilder: (_) => const MeterBridgeSandbox(),
  accentColor: Palette.chElectroMag,
);
