import '../../models/lesson.dart';
import '../../simulators/coulombs_law_sandbox.dart';

/// Charges & Coulomb's Law — the force law that starts all of electrostatics.
final Lesson coulombsLawLesson = Lesson(
  topicId: 'coulombs-law',
  title: 'Charges & Coulomb\'s Law',
  bigQuestion:
      'Two tiny specks of charge, invisible to the eye, can push each other apart with the force of a small weight — and they never even touch. What decides how hard they push, and why does moving them just a little closer change everything?',
  whyItMatters:
      'Coulomb\'s law is the seed of the entire electricity syllabus. Electric field, potential, capacitance, even the structure of the atom — all grow from this one inverse-square force law. It looks almost identical to gravity, but with a twist gravity never has: charge comes in two signs, so this force can pull OR push. Master this and the rest of electrostatics becomes bookkeeping.',
  prediction: const PredictionPrompt(
    scenario:
        'Two charges sit a distance r apart and repel with force F. You now push them to HALF that distance (r/2), keeping the charges the same. The new force is:',
    options: [
      'The same F (only charge matters)',
      '2F (twice as close, twice the force)',
      '4F (force depends on 1/r²)',
      'F/4 (spreading out weakens it)',
    ],
    correctIndex: 2,
    reveal:
        'Force follows 1/r², so halving r multiplies the force by 4. In the lab, drag the separation slider from 0.30 m down to 0.15 m and watch the force reading jump to four times its value. This steep 1/r² dependence is why atoms hold together so fiercely at short range yet ignore each other far away.',
  ),
  experiments: [
    'Set q₁ = +2 µC, q₂ = +3 µC and halve r — confirm the force becomes 4× larger',
    'Flip q₂ to negative and watch the arrows swap from REPEL to ATTRACT',
    'Set one charge to 0 µC — the force vanishes (no charge, no force)',
    'Double q₁ and note the force exactly doubles (F ∝ q₁)',
    'Drag r to its minimum (0.08 m) and see the force explode — the 1/r² law biting',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Charge is a basic property of matter, like mass — but unlike mass it comes in two flavours we call positive and negative. Rub a glass rod with silk and it loses electrons (becomes positive); rub ebonite with fur and it gains electrons (becomes negative). Like charges repel, unlike charges attract. Charge is measured in coulombs (C), and it is quantised: every charge is a whole-number multiple of the elementary charge e = 1.6×10⁻¹⁹ C.',
      title: 'Charge: the source of the force',
    ),
    ContentBlock.formula('q = n·e,   e = 1.6×10⁻¹⁹ C', title: 'QUANTISATION OF CHARGE'),
    ContentBlock.paragraph(
      'Coulomb measured, in 1785, exactly how the force between two point charges depends on their sizes and separation. The force is proportional to the product of the charges and inversely proportional to the square of the distance between them. It acts along the line joining the two charges.',
      title: 'Coulomb\'s law',
    ),
    ContentBlock.formula('F = k·|q₁·q₂| / r²,   k = 1/(4πε₀) = 9×10⁹ N·m²/C²',
        title: 'COULOMB\'S LAW'),
    ContentBlock.bullets([
      'F ∝ q₁ — double one charge, double the force',
      'F ∝ q₂ — double the other charge, double the force again',
      'F ∝ 1/r² — halve the distance, quadruple the force',
      'Direction: along the line joining the charges (attraction if signs differ, repulsion if same)',
    ]),
    ContentBlock.paragraph(
      'The constant ε₀ = 8.85×10⁻¹² C²/(N·m²) is the permittivity of free space. Inside a material (a "dielectric") the force is weaker — divide by the relative permittivity (dielectric constant) K: F = k·q₁q₂/(K·r²). Water, with K ≈ 80, weakens electric forces so much that salt crystals dissolve in it.',
      title: 'The medium matters',
    ),
    ContentBlock.realLife(
      'Every solid you lean on pushes back because of Coulomb repulsion between the electron clouds of its atoms and yours — you never actually "touch" a table, you feel electrostatic repulsion a fraction of a nanometre away. Static cling, a photocopier grabbing toner, lightning, the way a comb lifts paper bits — all are Coulomb\'s law at human scale.',
    ),
    ContentBlock.mistake(
      'Forgetting to convert units. Charges in problems are usually given in microcoulombs (µC = 10⁻⁶ C) or nanocoulombs (nC = 10⁻⁹ C), and distances in centimetres. Convert to coulombs and metres BEFORE plugging into F = kq₁q₂/r², or your answer will be off by huge powers of ten.',
    ),
    ContentBlock.mistake(
      'Treating the two forces as unequal. By Newton\'s third law the force on q₁ from q₂ is exactly equal and opposite to the force on q₂ from q₁ — even if one charge is a thousand times bigger. A small charge feels the same magnitude of force as the big charge it sits near.',
    ),
    ContentBlock.example(
      'Two charges q₁ = +3 µC and q₂ = −4 µC are 20 cm apart in air. Find the force.\n\nConvert: q₁ = 3×10⁻⁶ C, q₂ = 4×10⁻⁶ C, r = 0.20 m.\n\nF = kq₁q₂/r² = 9×10⁹ × (3×10⁻⁶)(4×10⁻⁶) / (0.20)²\n= 9×10⁹ × 12×10⁻¹² / 0.04\n= 9×10⁹ × 3×10⁻¹⁰\n= 2.7 N.\n\nSigns differ, so the 2.7 N force is attractive — each charge is pulled toward the other.',
    ),
    ContentBlock.jeeTip(
      'When three or more charges act, use the SUPERPOSITION principle: compute the force from each other charge one at a time (ignoring the rest), then add the force VECTORS. Coulomb\'s law gives you magnitudes; geometry (components, the parallelogram law) gives you the resultant. A charge in equilibrium means the vector sum is zero.',
    ),
    ContentBlock.jeeTip(
      'The classic "where is the null point?" problem: for two like charges, the force on a test charge between them balances where kq₁/x² = kq₂/(d−x)². Cancel k, take square roots, and solve x/(d−x) = √(q₁/q₂). The null point lies nearer the smaller charge.',
    ),
    ContentBlock.neetNote(
      'NEET favours the conceptual comparisons: Coulomb force vs gravitational force between the same two particles — the electric force is about 10³⁹ times stronger for two protons. Also remember charge properties: it is conserved (total charge never changes in any process), additive, and quantised. Rubbing does not create charge; it only transfers electrons from one body to the other.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the two experimental dependences',
      math: 'F ∝ q₁·q₂   (at fixed r)\nF ∝ 1/r²      (at fixed charges)',
      note: 'Coulomb established both with his torsion balance.',
    ),
    DerivationStep(
      title: 'Combine into one proportionality',
      math: 'F ∝ q₁·q₂ / r²',
    ),
    DerivationStep(
      title: 'Insert the constant of proportionality',
      math: 'F = k · q₁·q₂ / r²,   k = 1/(4πε₀)',
      note: 'The 4π appears so that Gauss\'s law later comes out clean. k = 9×10⁹ N·m²/C².',
    ),
    DerivationStep(
      title: 'Write it as a vector along the join',
      math: 'F₁₂ = k·q₁q₂/r² · r̂₁₂',
      note: 'r̂ is the unit vector from one charge to the other. Same signs → force is repulsive (along r̂); opposite signs → attractive.',
    ),
    DerivationStep(
      title: 'Superpose for many charges',
      math: 'F_net = Σ k·q·qᵢ/rᵢ² · r̂ᵢ',
      note: 'Total force on one charge = vector sum of the individual Coulomb forces from every other charge.',
    ),
  ],
  formulas: const [
    FormulaEntry('Coulomb\'s law (magnitude)', 'F = k·|q₁q₂|/r²'),
    FormulaEntry('Coulomb constant', 'k = 1/(4πε₀) = 9×10⁹ N·m²/C²'),
    FormulaEntry('Permittivity of free space', 'ε₀ = 8.85×10⁻¹² C²/(N·m²)'),
    FormulaEntry('Force in a medium', 'F = k·q₁q₂/(K·r²)', condition: 'K = dielectric constant of the medium'),
    FormulaEntry('Quantisation of charge', 'q = n·e,  e = 1.6×10⁻¹⁹ C'),
    FormulaEntry('Superposition', 'F_net = ΣFᵢ  (vector sum)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the distance between two point charges is doubled, the electrostatic force between them becomes:',
      options: ['Twice as large', 'Half', 'One-fourth', 'Four times'],
      correctIndex: 2,
      solution:
          'F ∝ 1/r². Doubling r multiplies r² by 4, so the force drops to 1/4 of its original value.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The charge on a body is 1 µC. How many excess electrons does it carry?',
      options: ['6.25×10¹²', '1.6×10¹³', '6.25×10¹⁸', '1.6×10⁻¹³'],
      correctIndex: 0,
      solution:
          'n = q/e = 10⁻⁶ / (1.6×10⁻¹⁹) = 6.25×10¹² electrons. (A negative body has that many EXCESS electrons.)',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Two charges of +2 µC and +2 µC are placed 10 cm apart. The force between them is:',
      options: ['1.8 N', '3.6 N', '0.9 N', '7.2 N'],
      correctIndex: 1,
      solution:
          'F = 9×10⁹ × (2×10⁻⁶)² / (0.10)² = 9×10⁹ × 4×10⁻¹² / 0.01 = 9×10⁹ × 4×10⁻¹⁰ = 3.6 N (repulsive).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two identical charged spheres repel with force F. They are touched together, then returned to their original positions. If the charges were +3q and +q, the new force is:',
      options: ['F', '4F/3', '4F', 'F/3'],
      correctIndex: 1,
      solution:
          'Original: F ∝ (3q)(q) = 3q². On touching, charge shares equally: each becomes (3q+q)/2 = 2q. New force ∝ (2q)(2q) = 4q². Ratio = 4q²/3q² = 4/3, so new force = 4F/3.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A charge is placed at each of two opposite corners of a square. A third charge sits at a third corner. The force analysis requires:',
      options: [
        'Simply adding the two force magnitudes',
        'Subtracting the smaller force from the larger',
        'Adding the forces as vectors using the parallelogram law',
        'Ignoring the farther charge',
      ],
      correctIndex: 2,
      solution:
          'Forces are vectors. The two Coulomb forces on the third charge point in different directions, so you must resolve into components (or use the parallelogram law) to find the resultant. This is the superposition principle.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Charges +q and +4q are fixed a distance d apart. At what distance x from +q (along the line) should a third charge be placed so it feels no net force?',
      options: ['d/3', 'd/2', '2d/3', 'd/5'],
      correctIndex: 0,
      solution:
          'Balance: kq/x² = k(4q)/(d−x)². So (d−x)²/x² = 4 → (d−x)/x = 2 → d−x = 2x → x = d/3. The null point lies nearer the SMALLER charge (+q), as expected.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Two small balls of mass m hang from a common point by silk threads of length L. Each carries charge q and they repel to a separation x (x ≪ L). The equilibrium condition gives x proportional to:',
      options: ['q^(1/3)', 'q^(2/3)', 'q', 'q²'],
      correctIndex: 1,
      solution:
          'At equilibrium, tan θ = F/mg. For small angles tan θ ≈ (x/2)/L, and F = kq²/x². So x/(2L) ≈ kq²/(mg·x²) → x³ ≈ 2Lkq²/(mg) → x ∝ q^(2/3). A standard JEE result worth memorising.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The force between two charges in air is F. When a slab of dielectric constant K fills the space between them (distance unchanged), the force becomes:',
      options: ['KF', 'F/K', 'F/K²', 'K²F'],
      correctIndex: 1,
      solution:
          'In a medium F = kq₁q₂/(K·r²). The medium reduces the force by the factor K, so the new force is F/K.',
    ),
  ],
  revision: [
    'F = k·q₁q₂/r² with k = 9×10⁹; force acts along the line joining the charges.',
    'F ∝ product of charges, ∝ 1/r². Halve r → 4× force; double a charge → 2× force.',
    'Charge is conserved, additive and quantised: q = n·e, e = 1.6×10⁻¹⁹ C.',
    'In a medium of dielectric constant K, force weakens to F/K.',
    'Many charges → superposition: add the Coulomb force VECTORS.',
    'Null point for two like charges lies nearer the smaller charge: x/(d−x) = √(q₁/q₂).',
  ],
  sandboxBuilder: (_) => const CoulombsLawSandbox(),
);
