import '../../models/lesson.dart';
import '../../simulators/capacitors_sandbox.dart';

/// Capacitors — storing charge and energy in an electric field.
final Lesson capacitorsLesson = Lesson(
  topicId: 'capacitors',
  title: 'Capacitors',
  bigQuestion:
      'A capacitor holds no more "stuff" than an empty gap between two metal plates — so where exactly does its stored energy live, and why does sliding a slab of glass between the plates let it hold more charge for the same battery?',
  whyItMatters:
      'Every camera flash, every touchscreen, every power supply that smooths a wobbly voltage relies on a capacitor. It is the first device where the electric field stops being an abstraction and becomes something you store energy in. JEE and NEET lean on this chapter hard because one geometric formula (C = ε₀εᵣA/d) plus two relations (Q = CV, U = ½CV²) unlock a whole family of problems.',
  prediction: const PredictionPrompt(
    scenario:
        'A parallel-plate capacitor is connected to a battery of fixed voltage V. You slide a glass slab (εᵣ = 4) fully between the plates without disconnecting the battery. What happens to the charge stored on the plates?',
    options: [
      'It stays the same — the battery voltage did not change',
      'It becomes 4 times larger',
      'It becomes 4 times smaller',
      'It drops to zero',
    ],
    correctIndex: 1,
    reveal:
        'With the battery still attached, V is pinned. The dielectric multiplies C by εᵣ = 4, so Q = CV must jump ×4 as well — the battery pushes extra charge onto the plates. Slide the εᵣ slider up in the lab and watch Q climb while the field between the plates actually weakens.',
  ),
  experiments: [
    'Halve the separation d and watch C exactly double',
    'Double the plate area A and watch C double',
    'Slide εᵣ from 1 to 4 with V fixed — Q jumps ×4, energy ×4',
    'Raise the battery V and watch both Q and the field E climb linearly',
    'Find a setting where the field E is smallest for a given voltage — it is the widest gap',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A capacitor is two conductors separated by an insulator. Connect them to a battery and charge piles up: +Q on one plate, −Q on the other. The plates never touch, so the charge just sits there, held in place by its own attraction across the gap. The capacitor stores charge — and, more importantly, stores energy in the electric field that fills the gap.',
      title: 'What a capacitor actually does',
    ),
    ContentBlock.paragraph(
      'Push more charge on and the voltage across the plates rises in exact proportion. That proportionality constant is the capacitance C — literally the "capacity" to hold charge per volt. A big C means the device swallows a lot of charge for only a small rise in voltage.',
    ),
    ContentBlock.formula('C = Q / V        [unit: farad, F = C/V]', title: 'DEFINITION OF CAPACITANCE'),
    ContentBlock.paragraph(
      'Capacitance is set entirely by geometry and the insulator — not by how much charge you happen to put on. For flat parallel plates of area A held a distance d apart, the formula is beautifully simple.',
      title: 'The parallel-plate formula',
    ),
    ContentBlock.formula('C = ε₀·εᵣ·A / d', title: 'PARALLEL-PLATE CAPACITANCE'),
    ContentBlock.bullets([
      'Bigger area A → more room for charge → larger C',
      'Smaller gap d → plates pull harder across the gap → larger C',
      'A dielectric (εᵣ > 1) → weakens the internal field → larger C by factor εᵣ',
      'ε₀ = 8.85 × 10⁻¹² F/m is the permittivity of free space',
    ]),
    ContentBlock.realLife(
      'A camera flash charges a capacitor slowly from a small battery, then dumps all that stored energy into the bulb in a few milliseconds — a huge burst of power the battery alone could never deliver. That is a capacitor\'s superpower: store energy gently, release it violently.',
    ),
    ContentBlock.paragraph(
      'A dielectric is an insulating slab (glass, mica, plastic). Its molecules polarise in the field and set up a weak opposing field, cutting the net field inside to E/εᵣ. Less field for the same charge means less voltage, and since C = Q/V, the capacitance rises by εᵣ. Dielectrics also let plates sit closer without sparking.',
      title: 'Why a dielectric helps',
    ),
    ContentBlock.formula('U = ½QV = ½CV² = Q²/(2C)', title: 'ENERGY STORED'),
    ContentBlock.mistake(
      'Students think "a bigger capacitor stores more energy, always." It depends on what is held fixed. At fixed voltage, U = ½CV² rises with C. But at fixed charge (battery disconnected), U = Q²/2C FALLS as C rises. Always ask: is the battery still connected (V fixed) or removed (Q fixed)? The two cases give opposite answers.',
    ),
    ContentBlock.mistake(
      'Do not confuse the two dielectric scenarios. Battery connected → V fixed, so Q and U rise. Battery disconnected → Q fixed, so V and E fall, and U falls. Mixing these up is the single most common capacitor error in exams.',
    ),
    ContentBlock.example(
      'A parallel-plate capacitor has A = 100 cm² = 0.01 m², d = 1 mm = 10⁻³ m, air gap, connected to 200 V.\n\nC = ε₀A/d = (8.85×10⁻¹²)(0.01)/(10⁻³) = 8.85×10⁻¹¹ F ≈ 88.5 pF.\nQ = CV = 8.85×10⁻¹¹ × 200 = 1.77×10⁻⁸ C = 17.7 nC.\nE = V/d = 200/10⁻³ = 2×10⁵ V/m.\nU = ½CV² = ½ × 8.85×10⁻¹¹ × 200² = 1.77×10⁻⁶ J = 1.77 µJ.',
    ),
    ContentBlock.jeeTip(
      'For the "battery disconnected, then dielectric inserted" case, walk it in order: Q is frozen → C becomes εᵣC → V = Q/C falls by εᵣ → E = V/d falls by εᵣ → U = Q²/2C falls by εᵣ. Every quantity follows once you fix Q. JEE loves testing whether you tracked the right invariant.',
    ),
    ContentBlock.jeeTip(
      'Energy density in the field is u = ½ε₀E². This lets you find the energy without ever computing C — useful when the geometry is nasty. The energy really does live in the field, spread through the gap.',
    ),
    ContentBlock.neetNote(
      'NEET favours the direct-substitution questions: given A, d, εᵣ and V, find C, Q, E or U. Memorise C = ε₀εᵣA/d and the three energy forms. Also remember E = V/d for the uniform field between plates, and E = σ/ε₀ = Q/(ε₀A) in terms of charge.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Field between two charged plates',
      math: 'Each plate: E = σ/(2ε₀)\nBetween the plates the two add: E = σ/ε₀ = Q/(ε₀A)',
      note: 'σ = Q/A is the surface charge density. Outside the plates the fields cancel.',
    ),
    DerivationStep(
      title: 'Voltage across the gap',
      math: 'V = E·d = Q·d/(ε₀A)',
      note: 'The field is uniform, so voltage is simply field × separation.',
    ),
    DerivationStep(
      title: 'Divide to get capacitance',
      math: 'C = Q/V = Q / [Q·d/(ε₀A)] = ε₀A/d',
      note: 'The charge Q cancels — capacitance depends only on geometry, exactly as claimed.',
    ),
    DerivationStep(
      title: 'Insert a dielectric',
      math: 'Field falls to E/εᵣ  →  V falls by εᵣ  →  C = ε₀εᵣA/d',
      note: 'The dielectric multiplies capacitance by its constant εᵣ.',
    ),
    DerivationStep(
      title: 'Energy: integrate charging up',
      math: 'dW = v·dq = (q/C)dq\nU = ∫₀^Q (q/C)dq = Q²/(2C) = ½CV²',
      note: 'The first electron is free; each later one is pushed against those already there.',
    ),
  ],
  formulas: const [
    FormulaEntry('Capacitance (definition)', 'C = Q/V'),
    FormulaEntry('Parallel-plate capacitor', 'C = ε₀·εᵣ·A/d'),
    FormulaEntry('Field between plates', 'E = V/d = σ/ε₀ = Q/(ε₀A)'),
    FormulaEntry('Energy stored', 'U = ½CV² = ½QV = Q²/(2C)'),
    FormulaEntry('Energy density in field', 'u = ½ε₀E²'),
    FormulaEntry('Dielectric effect', 'C → εᵣC,   E → E/εᵣ',
        condition: 'Slab fills the gap'),
    FormulaEntry('Permittivity of free space', 'ε₀ = 8.85 × 10⁻¹² F/m'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The capacitance of a parallel-plate capacitor depends on:',
      options: [
        'The charge placed on the plates',
        'The voltage applied',
        'The plate area, separation and dielectric only',
        'The current flowing through it',
      ],
      correctIndex: 2,
      solution:
          'C = ε₀εᵣA/d is purely geometric. Adding charge raises both Q and V together, leaving C = Q/V unchanged. Capacitance is a property of the device, not of how you use it.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question:
          'If the separation between the plates of a parallel-plate capacitor is halved, its capacitance:',
      options: ['Halves', 'Doubles', 'Stays the same', 'Becomes four times'],
      correctIndex: 1,
      solution:
          'C = ε₀A/d, so C ∝ 1/d. Halving d doubles C. Verify it in the lab: drop d from 4 mm to 2 mm and watch C exactly double.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A 5 µF capacitor is charged to 100 V. The energy stored is:',
      options: ['0.025 J', '0.05 J', '0.25 J', '2.5 J'],
      correctIndex: 0,
      solution:
          'U = ½CV² = ½ × 5×10⁻⁶ × 100² = ½ × 5×10⁻⁶ × 10⁴ = 2.5×10⁻² = 0.025 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A dielectric slab (εᵣ = 3) is inserted into a capacitor kept connected to a battery. Which quantity stays constant?',
      options: ['Charge Q', 'Voltage V', 'Capacitance C', 'Energy U'],
      correctIndex: 1,
      solution:
          'The battery pins V. Then C triples, so Q = CV triples and U = ½CV² triples. Only V is fixed. (If instead the battery were removed, Q would be the fixed quantity.)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'A capacitor is charged to charge Q, then disconnected from the battery. A dielectric εᵣ = 2 is inserted. The stored energy becomes:',
      options: ['4U', '2U', 'U/2', 'U/4'],
      correctIndex: 2,
      solution:
          'Battery disconnected → Q fixed. C doubles, and U = Q²/(2C), so U halves to U/2. The energy "lost" does mechanical work: the slab is pulled in by the field.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'The electric field between the plates of an air capacitor is E. A dielectric εᵣ = 4 is inserted while the charge is kept constant. The new field is:',
      options: ['4E', 'E', 'E/2', 'E/4'],
      correctIndex: 3,
      solution:
          'At constant charge, σ is fixed, and the field inside a dielectric is E₀/εᵣ. So E → E/4. The bound charges on the dielectric surface partly cancel the plate field.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A parallel-plate capacitor has area A and gap d. A metal slab of thickness d/2 is inserted parallel to the plates. The new capacitance is:',
      options: ['ε₀A/d', '2ε₀A/d', 'ε₀A/(2d)', '4ε₀A/d'],
      correctIndex: 1,
      solution:
          'A conducting slab of thickness t reduces the effective gap to (d − t). Here t = d/2, so effective gap = d/2, and C = ε₀A/(d/2) = 2ε₀A/d. A metal slab behaves like shorting out its own thickness.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.advanced,
      question:
          'Two identical capacitors, one with air and one filled with a dielectric εᵣ, are charged to the same voltage V. The ratio of energy stored (dielectric : air) is:',
      options: ['1 : εᵣ', 'εᵣ : 1', '1 : 1', 'εᵣ² : 1'],
      correctIndex: 1,
      solution:
          'At the same V, U = ½CV² and C_dielectric = εᵣ C_air. So U_dielectric : U_air = εᵣ : 1. Same voltage, more capacitance, more stored energy.',
    ),
  ],
  revision: [
    'C = Q/V is the definition; C = ε₀εᵣA/d is the parallel-plate formula — pure geometry.',
    'Field between plates E = V/d = Q/(ε₀A); it is uniform.',
    'Energy U = ½CV² = ½QV = Q²/2C — pick the form matching what is fixed.',
    'Battery CONNECTED → V fixed (Q, U rise with C). Battery REMOVED → Q fixed (V, E, U fall).',
    'A dielectric εᵣ multiplies C by εᵣ and cuts the internal field to E/εᵣ.',
    'A metal slab of thickness t just shrinks the effective gap to (d − t).',
  ],
  sandboxBuilder: (_) => const CapacitorsSandbox(),
);
