import '../../models/lesson.dart';
import '../../simulators/vectors_sandbox.dart';
import '../../theme/tokens.dart';

/// Vectors — the arithmetic of directions.
final Lesson vectorsLesson = Lesson(
  topicId: 'vectors',
  title: 'Vectors',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'You pull a box with 3 N and your friend pulls with 4 N. The box feels… 7 N? 1 N? 5 N? All three answers can be right — what decides?',
  whyItMatters:
      'Forces, velocities, fields — most of physics is vectors, and every chapter silently assumes you can add, subtract and resolve them. The parallelogram law and components are not one exam topic; they are the grammar used by ALL topics. Ten minutes of real fluency here pays off in every mechanics and electricity problem you ever solve.',
  prediction: const PredictionPrompt(
    scenario:
        'Two vectors of magnitudes 3 and 4 are added. Which of these CANNOT be the magnitude of their resultant?',
    options: ['7', '5', '1', '8'],
    correctIndex: 3,
    reveal:
        'The resultant of two vectors lies between |A − B| = 1 (opposite directions) and A + B = 7 (same direction). 5 happens at 90°. But 8 > 7 is impossible — no angle can make two vectors add beyond the sum of their magnitudes. Sweep B\'s direction in the lab and watch |R| slide between 1 and 7.',
  ),
  experiments: [
    'Set A = 3, B = 4, angle between them 0° — resultant is 7 (simple addition)',
    'Rotate B to 180° apart — resultant collapses to 1 (subtraction)',
    'Put them at 90° — resultant is exactly 5 (the 3-4-5 triangle!)',
    'Press Animate tip-to-tail and watch B start where A ends — that IS vector addition',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A scalar has only size (mass, time, speed). A vector has size AND direction (displacement, velocity, force). Two vectors are equal only when both magnitude and direction match. Adding vectors respects direction — which is why 3 + 4 can equal anything from 1 to 7.',
      title: 'Scalars vs vectors',
    ),
    ContentBlock.formula('|R|² = A² + B² + 2AB·cosθ', title: 'PARALLELOGRAM LAW'),
    ContentBlock.bullets([
      'θ = 0° → R = A + B (maximum);  θ = 180° → R = |A − B| (minimum)',
      'θ = 90° → R = √(A² + B²) — Pythagoras',
      'Direction of R: tanα = B·sinθ / (A + B·cosθ) from vector A',
      'Tip-to-tail picture: draw B starting from A\'s head; R runs start → finish',
    ]),
    ContentBlock.paragraph(
      'The power move is resolving: any vector splits into perpendicular components Aₓ = A·cosθ and A_y = A·sinθ. Components of different vectors along the same axis are ordinary numbers — add them like arithmetic, then rebuild the resultant with Pythagoras. This is how multi-force problems become one-line calculations.',
      title: 'Components: turning geometry into arithmetic',
    ),
    ContentBlock.realLife(
      'A plane aims north while the jet stream pushes east — its actual path is the vector sum, which is why pilots "crab" into the wind. Tug-of-war teams, cranes with slanted cables, and even your phone\'s tilt sensor (resolving gravity along axes) all run on vector addition.',
    ),
    ContentBlock.mistake(
      'Adding magnitudes while ignoring direction. Forces of 6 N and 8 N give 14 N ONLY if parallel. At 90° they give 10 N; opposite, 2 N. Never add vector magnitudes until you\'ve checked the angle.',
    ),
    ContentBlock.mistake(
      'Confusing the angle in the formula. The θ in R² = A² + B² + 2AB·cosθ is the angle BETWEEN the two vectors when drawn tail-to-tail — not the angle either makes with the x-axis.',
    ),
    ContentBlock.example(
      'Two forces 6 N and 8 N act at 90°. Find the resultant.\n\nR = √(6² + 8² + 2·6·8·cos90°) = √(36 + 64 + 0) = √100 = 10 N.\n\nDirection from the 6 N force: tanα = 8·sin90°/(6 + 8·cos90°) = 8/6 → α ≈ 53°.',
    ),
    ContentBlock.jeeTip(
      'If |A + B| = |A − B|, the vectors are perpendicular (square both sides and the cross terms force cosθ = 0). And remember the unit-vector algebra: î·î = 1, î·ĵ = 0, î×ĵ = k̂. Dot product → projection/work; cross product → area/torque. JEE hides vector identities inside mechanics problems.',
    ),
    ContentBlock.neetNote(
      'NEET repeats three specials: equal magnitudes at 120° give a resultant equal to either one; equal magnitudes at 90° give √2 times one; and three equal vectors at 120° to each other cancel to zero. Recognising these instantly saves a full minute each.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Place the two vectors tail-to-tail at angle θ',
      math: 'A along x-axis;  B at angle θ',
    ),
    DerivationStep(
      title: 'Resolve B into components',
      math: 'Bₓ = B·cosθ,   B_y = B·sinθ',
    ),
    DerivationStep(
      title: 'Add components axis by axis',
      math: 'Rₓ = A + B·cosθ,   R_y = B·sinθ',
    ),
    DerivationStep(
      title: 'Apply Pythagoras to the components',
      math: 'R² = (A + B·cosθ)² + (B·sinθ)²\n   = A² + B²(cos²θ+sin²θ) + 2AB·cosθ\n   = A² + B² + 2AB·cosθ',
      note: 'The parallelogram law is just Pythagoras after resolving.',
    ),
    DerivationStep(
      title: 'Direction of the resultant',
      math: 'tanα = R_y/Rₓ = B·sinθ / (A + B·cosθ)',
      note: 'α is measured from vector A.',
    ),
  ],
  formulas: const [
    FormulaEntry('Resultant magnitude', 'R = √(A² + B² + 2AB·cosθ)'),
    FormulaEntry('Resultant direction', 'tanα = B·sinθ/(A + B·cosθ)'),
    FormulaEntry('Components', 'Aₓ = A·cosθ,  A_y = A·sinθ'),
    FormulaEntry('Rebuild from components', 'A = √(Aₓ² + A_y²),  tanθ = A_y/Aₓ'),
    FormulaEntry('Dot product', 'A·B = AB·cosθ', condition: 'scalar; zero when perpendicular'),
    FormulaEntry('Cross product', '|A×B| = AB·sinθ', condition: 'vector; zero when parallel'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Which of the following is a vector quantity?',
      options: ['Speed', 'Work', 'Displacement', 'Mass'],
      correctIndex: 2,
      solution:
          'Displacement has magnitude and direction. Speed and mass are scalars; work (force·displacement dot product) is also a scalar.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The resultant of two vectors of magnitudes 3 and 4 acting at 90° is:',
      options: ['7', '5', '1', '12'],
      correctIndex: 1,
      solution: 'R = √(3² + 4²) = √25 = 5. The classic 3-4-5 right triangle.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two equal forces F act at 120° to each other. Their resultant has magnitude:',
      options: ['2F', 'F√2', 'F', 'F/2'],
      correctIndex: 2,
      solution:
          'R = √(F² + F² + 2F²·cos120°) = √(2F² − F²) = F. Equal vectors at 120° → resultant equals either vector.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If |A + B| = |A − B|, the angle between A and B is:',
      options: ['0°', '45°', '60°', '90°'],
      correctIndex: 3,
      solution:
          'Squaring both: A² + B² + 2AB·cosθ = A² + B² − 2AB·cosθ → 4AB·cosθ = 0 → θ = 90°.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A force of 10 N acts at 60° to the horizontal. Its horizontal component is:',
      options: ['10 N', '5 N', '8.66 N', '7.07 N'],
      correctIndex: 1,
      solution: 'Fₓ = F·cos60° = 10 × 0.5 = 5 N. (The vertical part is 10·sin60° ≈ 8.66 N.)',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The resultant of A and B is perpendicular to A, and |R| = A. The angle between A and B is:',
      options: ['120°', '135°', '150°', '90°'],
      correctIndex: 1,
      solution:
          'R ⊥ A means A + B·cosθ = 0, and R = B·sinθ = A. So B·cosθ = −A and B·sinθ = A → tanθ = −1 → θ = 135°.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Vectors A = 2î + 3ĵ and B = 4î − ĵ. The magnitude of A + B is:',
      options: ['√40', '√38', '6', '√52'],
      correctIndex: 0,
      solution: 'A + B = 6î + 2ĵ; |A+B| = √(36 + 4) = √40 = 2√10.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'If A·B = 0 and A×B = 0, and neither vector is null, then:',
      options: [
        'They are perpendicular',
        'They are parallel',
        'This is impossible',
        'They are equal',
      ],
      correctIndex: 2,
      solution:
          'A·B = 0 needs θ = 90°; |A×B| = 0 needs θ = 0° or 180°. No angle satisfies both with nonzero magnitudes — impossible.',
    ),
  ],
  revision: [
    'R² = A² + B² + 2AB·cosθ; resultant ranges from |A−B| to A+B.',
    'Resolve everything: Aₓ = A·cosθ, A_y = A·sinθ; add components like numbers.',
    'Equal vectors: at 90° → √2·A; at 120° → A; three at 120° → zero.',
    '|A+B| = |A−B| ⟺ A ⊥ B.',
    'Dot product AB·cosθ (scalar, work); cross product AB·sinθ (vector, torque).',
    'Tip-to-tail: draw B from A\'s head; the resultant closes the triangle.',
  ],
  sandboxBuilder: (_) => const VectorsSandbox(),
);
