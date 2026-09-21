import '../../models/lesson.dart';
import '../../simulators/logic_gates_sandbox.dart';
import '../../theme/tokens.dart';

/// Logic Gates — binary logic, truth tables, and the universal building blocks of computing.
final Lesson logicGatesLesson = Lesson(
  topicId: 'logic-gates',
  title: 'Logic Gates',
  accentColor: Palette.chModern,
  bigQuestion:
      'Every app, video, and webpage on your phone ultimately boils down to billions of tiny switches flipping between just two states — ON and OFF. How can something as complex as a video game or a search engine be built entirely out of a handful of simple yes/no decision circuits repeated over and over?',
  whyItMatters:
      'Logic gates are the literal building blocks of every digital device ever made — computers, phones, calculators, traffic lights. NEET and JEE test truth tables and Boolean expressions directly, and this topic bridges physics (transistor-based electronic switches) into the world of computer engineering, making it one of the most conceptually rewarding topics in modern physics.',
  prediction: const PredictionPrompt(
    scenario:
        'You have only NAND gates available (no AND, OR, or NOT gates in stock). Can you still build a circuit that performs a NOT operation (inverts a single input)?',
    options: [
      'No — NOT requires a fundamentally different physical mechanism',
      'Yes — connecting BOTH inputs of a NAND gate to the same signal produces a NOT gate',
      'Yes, but only using at least three NAND gates',
      'No — NAND can only ever produce AND-like behavior',
    ],
    correctIndex: 1,
    reveal:
        'A NAND gate with both inputs tied to the same signal outputs NOT(A AND A) = NOT(A) — instant inverter with a single gate! This is the core idea behind NAND being a "universal gate": ANY logic function, including AND, OR, and NOT, can be built using NAND gates alone. In the lab, wire a single NAND gate with both inputs connected to the same source and watch its output table match a NOT gate exactly.',
  ),
  experiments: [
    'Build an AND gate and toggle both inputs to verify the truth table',
    'Build an OR gate and confirm the output is 1 whenever at least one input is 1',
    'Tie both inputs of a NAND gate together and verify it behaves exactly like a NOT gate',
    'Chain multiple NAND gates together to build an AND gate (NAND followed by NOT)',
    'Build an XOR gate and observe it outputs 1 only when the inputs DIFFER',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Digital electronics represents information using just two discrete voltage levels: HIGH (logic 1, typically several volts) and LOW (logic 0, typically near zero volts) — this binary representation is far more robust to noise than trying to represent continuous (analog) values, which is why virtually all modern computing is digital. A logic gate is a physical circuit (built from transistors/diodes) that takes one or more binary inputs and produces a single binary output according to a fixed rule.',
      title: 'Binary logic: the language of digital circuits',
    ),
    ContentBlock.bullets([
      'AND: output is 1 only if ALL inputs are 1 (A·B)',
      'OR: output is 1 if AT LEAST ONE input is 1 (A+B)',
      'NOT: output is the inverse of the single input (Ā)',
      'NAND: NOT(AND) — output is 0 only if all inputs are 1',
      'NOR: NOT(OR) — output is 1 only if all inputs are 0',
      'XOR: output is 1 only if the inputs are DIFFERENT (exclusive OR)',
    ], title: 'The six basic gates'),
    ContentBlock.formula('AND: Y=1 only for A=1,B=1     OR: Y=1 for A=1 or B=1 or both',
        title: 'AND / OR TRUTH TABLES (SUMMARY)'),
    ContentBlock.paragraph(
      'A truth table lists every possible combination of inputs and the corresponding output — it is the complete, unambiguous definition of what a gate does. For a 2-input gate there are 2² = 4 possible input combinations (00, 01, 10, 11); for n inputs there are 2ⁿ combinations. Truth tables are the standard way exam questions specify or test understanding of gate behaviour.',
      title: 'Truth tables define gates completely',
    ),
    ContentBlock.paragraph(
      'NAND and NOR are called UNIVERSAL GATES because either one, used alone (with appropriate wiring), can construct ANY other logic gate — AND, OR, NOT, XOR, everything. This is a profound practical result: manufacturers can mass-produce a single gate type and wire it in different combinations to build arbitrarily complex digital circuits, rather than needing to fabricate many different gate types.',
      title: 'NAND and NOR: the universal building blocks',
    ),
    ContentBlock.bullets([
      'NOT from NAND: tie both inputs together — NAND(A,A) = NOT(A)',
      'AND from NAND: a NAND gate followed by a NOT gate (itself built from NAND) — NOT(NAND(A,B)) = AND(A,B)',
      'OR from NAND: invert both inputs first, then NAND them (De Morgan\'s law in action)',
    ], title: 'Building other gates from NAND'),
    ContentBlock.paragraph(
      'Boolean algebra is the mathematical system underlying logic gates, using the operators AND (·), OR (+), and NOT (overbar). Laws like De Morgan\'s theorems — NOT(A·B) = Ā+B̄ and NOT(A+B) = Ā·B̄ — let you convert between AND-based and OR-based expressions, which is exactly what makes universal gates like NAND capable of replicating both AND and OR behaviour.',
      title: 'Boolean algebra basics',
    ),
    ContentBlock.realLife(
      'Every digital device — your phone\'s processor, a pocket calculator, a digital clock, a car\'s engine control unit — is built from billions of transistors arranged into logic gates, which combine into larger circuits (adders, memory cells, processors). Modern CPUs contain billions of transistors implementing NAND/NOR-based logic at nanometre scale, and the entire architecture of modern computing rests on the simple truth tables covered in this lesson.',
    ),
    ContentBlock.mistake(
      'Confusing OR and XOR. OR outputs 1 when EITHER or BOTH inputs are 1 (inclusive or) — so for inputs (1,1), OR gives 1. XOR outputs 1 only when the inputs DIFFER — so for inputs (1,1), XOR gives 0. This single differing case (both inputs = 1) is exactly what separates the two gates.',
    ),
    ContentBlock.mistake(
      'Mixing up NAND and NOR truth tables. NAND is 0 only when ALL inputs are 1 (otherwise 1) — the inverse of AND. NOR is 1 only when ALL inputs are 0 (otherwise 0) — the inverse of OR. Writing out the base gate\'s truth table first, then inverting every output, is a reliable way to avoid errors.',
    ),
    ContentBlock.example(
      'Verify that a NAND gate with both inputs tied together behaves as a NOT gate.\n\nNAND truth table: NAND(0,0)=1, NAND(0,1)=1, NAND(1,0)=1, NAND(1,1)=0.\nTying inputs together means A=B always, so we only use the (0,0) and (1,1) rows:\nNAND(0,0) = 1 = NOT(0) ✓\nNAND(1,1) = 0 = NOT(1) ✓\n\nBoth cases match NOT exactly — confirming the universal-gate construction.',
    ),
    ContentBlock.jeeTip(
      'When asked to identify a gate from its output expression, convert to standard Boolean form and compare: Y = A·B is AND, Y = A+B is OR, Y = NOT(A·B) is NAND, Y = A⊕B (or ĀB+AB̄) is XOR. Practice converting between truth table, Boolean expression, and gate symbol quickly — all three representations are used interchangeably across exam questions.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks to identify a gate purely from a given truth table, or asks which single input combination distinguishes two similar gates (e.g., AND vs NAND differ ONLY in the all-1s row; OR vs NOR differ ONLY in the all-0s row). Memorising these single "signature" rows is a fast way to identify a gate under exam time pressure.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define the AND operation from its truth table',
      math: 'Y = A·B: Y=1 only when both A=1 AND B=1',
      note: 'All other combinations (0,0), (0,1), (1,0) give Y=0.',
    ),
    DerivationStep(
      title: 'Define NAND as the complement of AND',
      math: 'Y_NAND = NOT(A·B) = (A·B)‾',
      note: 'Simply invert every output row of the AND truth table.',
    ),
    DerivationStep(
      title: 'Show NAND produces NOT when inputs are tied together',
      math: 'Set B = A: Y = NOT(A·A) = NOT(A)',
      note: 'A·A = A in Boolean algebra (idempotent law), so NAND(A,A) = NOT(A).',
    ),
    DerivationStep(
      title: 'Build AND from two NAND gates',
      math: 'Y = NOT(NOT(A·B)) = NOT(NAND(A,B)) = A·B',
      note: 'Feed a NAND gate\'s output into a NOT gate (itself built from a NAND with tied inputs) to recover AND.',
    ),
    DerivationStep(
      title: 'Build OR from NAND using De Morgan\'s theorem',
      math: 'A+B = NOT(Ā·B̄) = NAND(NOT(A), NOT(B))',
      note: 'Invert both inputs first (each via a NAND-based NOT), then NAND the results — this yields OR, completing the proof that NAND alone is universal.',
    ),
  ],
  formulas: const [
    FormulaEntry('AND', 'Y = A·B'),
    FormulaEntry('OR', 'Y = A+B'),
    FormulaEntry('NOT', 'Y = Ā'),
    FormulaEntry('NAND', 'Y = (A·B)‾'),
    FormulaEntry('NOR', 'Y = (A+B)‾'),
    FormulaEntry('XOR', 'Y = AB̄ + ĀB'),
    FormulaEntry('De Morgan\'s theorems', '(A·B)‾ = Ā+B̄,   (A+B)‾ = Ā·B̄'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'An AND gate with inputs A=1, B=0 gives output:',
      options: ['1', '0', 'Undefined', 'Depends on gate type'],
      correctIndex: 1,
      solution: 'AND requires BOTH inputs to be 1. Since B=0, the output is 0.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Which of these gates is called a "universal gate" because it alone can build all other gates?',
      options: ['AND', 'OR', 'NAND', 'XOR'],
      correctIndex: 2,
      solution: 'NAND (and also NOR) is universal — any logic function can be constructed using NAND gates alone.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An OR gate with inputs A=1, B=1 gives output:',
      options: ['0', '1', 'Undefined', '2'],
      correctIndex: 1,
      solution: 'OR outputs 1 if at least one input is 1 — with both inputs 1, the output is still 1 (inclusive OR).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'An XOR gate with inputs A=1, B=1 gives output:',
      options: ['1', '0', 'Undefined', 'Depends on order'],
      correctIndex: 1,
      solution: 'XOR outputs 1 only when the inputs DIFFER. Since both inputs are 1 (same), XOR gives 0 — this is what distinguishes XOR from OR.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A NAND gate with both inputs A=0, B=0 gives output:',
      options: ['0', '1', 'Undefined', 'Depends on the circuit'],
      correctIndex: 1,
      solution: 'NAND = NOT(AND). AND(0,0)=0, so NAND(0,0) = NOT(0) = 1.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'To build a NOT gate using only a NAND gate, you should:',
      options: [
        'Connect one input to ground permanently',
        'Tie both inputs of the NAND gate together to the same signal',
        'Use two separate NAND gates with different inputs',
        'It cannot be done with NAND alone',
      ],
      correctIndex: 1,
      solution: 'NAND(A,A) = NOT(A·A) = NOT(A), since A·A=A. Tying both inputs to the same signal converts NAND directly into NOT.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Which Boolean expression correctly describes a NOR gate\'s output?',
      options: ['Y = A·B', 'Y = A+B', 'Y = NOT(A+B)', 'Y = NOT(A·B)'],
      correctIndex: 2,
      solution: 'NOR is literally "NOT OR" — Y = NOT(A+B), which is 1 only when both A and B are 0.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Using De Morgan\'s theorem, NOT(A·B) is equivalent to:',
      options: ['Ā·B̄', 'Ā+B̄', 'A+B', 'A·B'],
      correctIndex: 1,
      solution: 'De Morgan\'s first theorem: NOT(A·B) = Ā + B̄ (complement of AND equals OR of complements).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A circuit has two NAND gates: the first takes inputs A and B and produces output X = NAND(A,B); the second takes X as BOTH its inputs to produce Y = NAND(X,X). The overall circuit Y in terms of A and B is equivalent to:',
      options: ['NOT(A+B)', 'A·B (AND gate)', 'A+B (OR gate)', 'NOT(A·B) (NAND gate)'],
      correctIndex: 1,
      solution:
          'X = NOT(A·B). Then Y = NAND(X,X) = NOT(X) = NOT(NOT(A·B)) = A·B. Two cascaded NAND gates (second one wired as a NOT) reconstruct an AND gate.',
    ),
  ],
  revision: [
    'Digital logic uses two states: HIGH (1) and LOW (0) — robust against noise compared to analog signals.',
    'AND: all inputs 1 → output 1. OR: any input 1 → output 1. NOT: inverts the single input.',
    'NAND = NOT(AND); NOR = NOT(OR); XOR = 1 only when inputs differ.',
    'NAND and NOR are UNIVERSAL gates — either alone can build all other gate types.',
    'NAND with tied inputs = NOT gate; this is the key building block for all NAND-only circuits.',
    'De Morgan\'s theorems: NOT(A·B)=Ā+B̄ and NOT(A+B)=Ā·B̄ connect AND-based and OR-based logic.',
    'AND/NAND and OR/NOR pairs differ in exactly one row of their truth table (all-1s or all-0s respectively).',
  ],
  sandboxBuilder: (_) => const LogicGatesSandbox(),
);
