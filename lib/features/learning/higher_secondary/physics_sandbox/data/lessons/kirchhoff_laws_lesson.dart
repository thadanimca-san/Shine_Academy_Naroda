import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/kirchhoff_laws_sandbox.dart';

/// Kirchhoff's Laws — the two bookkeeping rules that solve any circuit.
final Lesson kirchhoffLawsLesson = Lesson(
  topicId: 'kirchhoff-laws',
  title: 'Kirchhoff\'s Laws',
  bigQuestion:
      'A circuit with two batteries and three resistors wired into two loops looks like a tangle Ohm\'s law alone cannot untangle — there is no single R and no single V to plug in. Is there a systematic method that ALWAYS works, no matter how complicated the wiring gets?',
  whyItMatters:
      'Ohm\'s law works beautifully for a single loop, but real circuits branch, merge, and loop back on themselves. Kirchhoff\'s two laws are simply conservation of charge and conservation of energy, applied to circuits — and together they are guaranteed to solve ANY circuit, no matter how many loops, batteries, or resistors it contains. Every circuit-analysis technique used in JEE/NEET, and every practical circuit design, is built on these two rules.',
  prediction: const PredictionPrompt(
    scenario:
        'In a two-loop circuit, you make the second battery\'s EMF ε₂ almost exactly equal to what would balance the shared middle branch. What happens to the current flowing through the SHARED (middle) resistor?',
    options: [
      'It stays exactly the same regardless of ε₂',
      'It grows without bound',
      'It shrinks toward zero and can even reverse direction',
      'It becomes exactly equal to ε₂',
    ],
    correctIndex: 2,
    reveal:
        'The shared-branch current is I₁ − I₂ — the difference of the two loop currents. In the lab, slide ε₂ upward: as the two loop currents approach each other, the middle-branch current shrinks toward zero, and pushing ε₂ further makes it flip sign entirely. This is exactly the balance condition used later in the Wheatstone bridge and meter bridge.',
  ),
  experiments: [
    'Set ε₁ = ε₂ with R₁ = R₂ and watch the middle-branch current shrink toward zero by symmetry',
    'Raise R₃ (the shared branch) and see both loop currents adjust to route around the increased resistance',
    'Increase ε₁ alone and watch I₁ rise while I₂ responds only through the shared branch',
    'Set R₃ very small (near 1 Ω) and see the two loops behave almost independently',
    'Verify at any setting that current INTO the top junction equals current OUT of it (KCL)',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Kirchhoff\'s Current Law (KCL), or the junction rule, states that at any junction (node) in a circuit, the total current flowing IN must equal the total current flowing OUT. This is nothing more than conservation of charge — charge cannot pile up or vanish at a point, so whatever current arrives must leave by some path.',
      title: 'Kirchhoff\'s Current Law (junction rule)',
    ),
    ContentBlock.formula('Σ I_in = Σ I_out   (at any junction)', title: 'KCL — JUNCTION RULE'),
    ContentBlock.paragraph(
      'Kirchhoff\'s Voltage Law (KVL), or the loop rule, states that the sum of all potential changes around any closed loop in a circuit is zero. This follows from conservation of energy: if you carry a test charge all the way around a closed loop back to its starting point, its potential energy must return to its original value — there is no net gain or loss.',
      title: 'Kirchhoff\'s Voltage Law (loop rule)',
    ),
    ContentBlock.formula('Σ V = 0   (around any closed loop)', title: 'KVL — LOOP RULE'),
    ContentBlock.bullets([
      'Traversing a resistor in the SAME direction as the assumed current: potential DROPS by IR',
      'Traversing a resistor OPPOSITE to the assumed current: potential RISES by IR',
      'Traversing an EMF source from − to + terminal (inside the cell): potential RISES by ε',
      'Traversing an EMF source from + to − terminal: potential DROPS by ε',
      'Pick a direction (clockwise, say) for every loop current and stay consistent — a negative answer just means the true current flows the other way',
    ]),
    ContentBlock.paragraph(
      'For a circuit with two independent loops, the systematic method is: (1) assign a loop current to each independent loop, all in the same rotational sense (say, clockwise); (2) write one KVL equation per loop, summing IR drops and EMF rises/drops around that loop; (3) any branch shared between two loops carries the DIFFERENCE of the two loop currents; (4) solve the resulting simultaneous equations for the loop currents. This "mesh analysis" automatically satisfies KCL at every junction, since each shared branch\'s current is consistently the difference of two loop currents defined once.',
      title: 'Systematic method for a 2-loop circuit',
    ),
    ContentBlock.realLife(
      'Every piece of consumer electronics — from a phone charger\'s internal circuit to a car\'s wiring harness — is designed using exactly this loop-and-junction bookkeeping, just automated inside circuit-simulation software (SPICE and similar tools). No matter how many thousands of components a circuit has, KCL and KVL applied systematically (usually via matrix methods) are what the software is solving underneath.',
    ),
    ContentBlock.mistake(
      'Mixing up the sign convention when crossing a battery versus crossing a resistor in the SAME loop traversal. A common error is treating every element\'s sign the same way. Fix a rule before you start (e.g. "go clockwise; IR is a drop if current I is assumed clockwise; EMF is a rise if you enter at the − terminal") and apply it consistently to every single element in the loop — do not switch conventions partway through.',
    ),
    ContentBlock.example(
      'A two-loop circuit has ε₁ = 9 V, ε₂ = 2 V, R₁ = 2 Ω (left branch), R₂ = 1 Ω (right branch), R₃ = 1 Ω (shared middle branch). Find both loop currents and the shared-branch current.\n\nLoop equations (I₁, I₂ both clockwise):\nLoop 1: I₁(R₁+R₃) − I₂R₃ = ε₁ → 3I₁ − I₂ = 9\nLoop 2: −I₁R₃ + I₂(R₂+R₃) = ε₂ → −I₁ + 2I₂ = 2\n\nFrom the second equation: I₁ = 2I₂ − 2. Substitute into the first:\n3(2I₂ − 2) − I₂ = 9 → 6I₂ − 6 − I₂ = 9 → 5I₂ = 15 → I₂ = 3 A.\nThen I₁ = 2(3) − 2 = 4 A.\n\nShared-branch current = I₁ − I₂ = 4 − 3 = 1 A, flowing in the direction assumed for loop 1.',
    ),
    ContentBlock.jeeTip(
      'When a branch is shared between two loops, always write its current as the ALGEBRAIC DIFFERENCE of the two loop currents (I₁ − I₂ if both loops are drawn clockwise and the branch is traversed in loop 1\'s clockwise sense but loop 2\'s counter-clockwise sense). Getting this sign right is the single most common place marks are lost in 2-loop KVL problems.',
    ),
    ContentBlock.jeeTip(
      'For circuits with three or more loops, the same method scales up: N independent loops need N loop currents and N simultaneous KVL equations. This is exactly matrix algebra (as used in the sandbox above) — set it up as A·I = ε and solve. You will never need more than KCL + KVL, no matter how large the network.',
    ),
    ContentBlock.neetNote(
      'NEET typically asks for a direct application: given a single loop with one or two EMFs and resistors in series, apply KVL once to find the current, being careful with the sign of each EMF (aiding or opposing). Also expect a conceptual question distinguishing KCL (charge conservation, at a POINT) from KVL (energy conservation, around a LOOP) — do not mix up which law corresponds to which conservation principle.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Assign loop currents',
      math: 'I₁ (left loop, clockwise), I₂ (right loop, clockwise)',
      note: 'The shared middle branch carries I₁ − I₂ (current from loop 1\'s perspective, minus loop 2\'s opposing contribution).',
    ),
    DerivationStep(
      title: 'Apply KVL to loop 1',
      math: 'ε₁ = I₁R₁ + (I₁ − I₂)R₃',
      note: 'Rearranged: I₁(R₁+R₃) − I₂R₃ = ε₁.',
    ),
    DerivationStep(
      title: 'Apply KVL to loop 2',
      math: 'ε₂ = I₂R₂ + (I₂ − I₁)R₃',
      note: 'Rearranged: −I₁R₃ + I₂(R₂+R₃) = ε₂.',
    ),
    DerivationStep(
      title: 'Solve the simultaneous equations',
      math: 'I₁ = [ε₁(R₂+R₃) + ε₂R₃] / [(R₁+R₃)(R₂+R₃) − R₃²]\nI₂ = [ε₂(R₁+R₃) + ε₁R₃] / [(R₁+R₃)(R₂+R₃) − R₃²]',
      note: 'Standard 2×2 linear system solved by substitution or Cramer\'s rule.',
    ),
    DerivationStep(
      title: 'Recover the shared branch current',
      math: 'I_mid = I₁ − I₂',
      note: 'Automatically satisfies KCL at both junctions where the middle branch meets the outer loop.',
    ),
  ],
  formulas: const [
    FormulaEntry('Junction rule (KCL)', 'ΣI_in = ΣI_out'),
    FormulaEntry('Loop rule (KVL)', 'ΣV = 0  (around any closed loop)'),
    FormulaEntry('IR drop sign (same direction as current)', 'ΔV = −IR'),
    FormulaEntry('EMF rise (− to + inside cell)', 'ΔV = +ε'),
    FormulaEntry('Shared-branch current (2-loop mesh)', 'I_shared = I₁ − I₂'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Kirchhoff\'s current law (junction rule) is a direct consequence of:',
      options: ['Conservation of energy', 'Conservation of charge', 'Ohm\'s law', 'Conservation of momentum'],
      correctIndex: 1,
      solution: 'Charge cannot accumulate at a point in steady state, so whatever current flows into a junction must flow out — this is charge conservation, not energy conservation.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Kirchhoff\'s voltage law (loop rule) is a direct consequence of:',
      options: ['Conservation of charge', 'Conservation of energy', 'Newton\'s third law', 'Conservation of mass'],
      correctIndex: 1,
      solution: 'Carrying a charge around a closed loop back to its starting point must return it to the same potential energy — no net work is done over a closed path in an electrostatic-like field, reflecting energy conservation.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In a single loop with EMF 10 V and total resistance 5 Ω, the current in the loop is:',
      options: ['0.5 A', '2 A', '5 A', '50 A'],
      correctIndex: 1,
      solution: 'By KVL, ε = IR ⟹ I = ε/R = 10/5 = 2 A.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A two-loop circuit has loop equations 3I₁ − I₂ = 9 and −I₁ + 2I₂ = 2 (currents in amperes). The value of I₁ is:',
      options: ['2 A', '3 A', '4 A', '5 A'],
      correctIndex: 2,
      solution: 'From the second equation, I₁ = 2I₂ − 2. Substituting into the first: 3(2I₂−2) − I₂ = 9 ⟹ 6I₂ − 6 − I₂ = 9 ⟹ 5I₂ = 15 ⟹ I₂ = 3. Then I₁ = 2(3) − 2 = 4 A.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'At a junction, three wires meet: two carry current INTO the junction (3 A and 5 A), and one carries current OUT. The outgoing current must be:',
      options: ['2 A', '8 A', '15 A', 'Cannot be determined'],
      correctIndex: 1,
      solution: 'By KCL, ΣI_in = ΣI_out ⟹ 3 + 5 = 8 A must leave through the third wire.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'In a two-loop circuit, if the two loop currents I₁ and I₂ (both assumed clockwise) become exactly equal, the current in the shared middle branch is:',
      options: ['I₁ + I₂', 'Zero', '2I₁', 'Cannot be determined without resistance values'],
      correctIndex: 1,
      solution: 'The shared branch current is I₁ − I₂ (the two loop currents flow through it in opposite senses). If I₁ = I₂, this difference is exactly zero — the balance condition used in bridge circuits.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'While applying KVL around a loop, if you traverse a resistor in the direction OPPOSITE to the assumed current flow, the potential change is taken as:',
      options: ['−IR (a drop)', '+IR (a rise)', 'Zero', 'Depends on the EMF in the loop'],
      correctIndex: 1,
      solution: 'Current flows from high to low potential through a resistor. Traversing against the assumed current direction means you move from low to high potential — a RISE of +IR.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The minimum number of independent KVL equations needed to solve a circuit with N independent loops is:',
      options: ['1, regardless of N', 'N', 'N + 1', '2N'],
      correctIndex: 1,
      solution: 'Each independent loop contributes exactly one independent KVL equation; N loop currents require N equations to solve uniquely (mesh analysis).',
    ),
  ],
  revision: [
    'KCL (junction rule): ΣI_in = ΣI_out at any node — conservation of charge.',
    'KVL (loop rule): ΣV = 0 around any closed loop — conservation of energy.',
    'Sign convention: IR is a drop when traversed WITH the current, a rise when traversed AGAINST it; EMF is a rise from − to + inside the cell.',
    'Method for 2-loop circuits: assign loop currents, write one KVL equation per loop, solve simultaneously; shared branch carries I₁ − I₂.',
    'KCL and KVL together are sufficient to solve ANY circuit, however many loops or components it has.',
    'A shared-branch current of zero (I₁ = I₂) is the balance condition seen later in Wheatstone/meter bridges.',
  ],
  sandboxBuilder: (_) => const KirchhoffLawsSandbox(),
  accentColor: Palette.chElectroMag,
);
