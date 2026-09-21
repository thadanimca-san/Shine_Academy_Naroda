import '../../models/lesson.dart';
import '../../simulators/gravitation_sim.dart';
import '../../theme/tokens.dart';

/// Universal Gravitation — the force that holds moons, planets and galaxies together.
final Lesson gravitationLesson = Lesson(
  topicId: 'universal-gravitation',
  title: 'Universal Gravitation',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'An apple falls to the ground. The Moon, 384,000 km away, never falls to the ground — it just keeps orbiting. Newton\'s insight was that the SAME force pulls on both. What could possibly be the same about a falling apple and an orbiting Moon?',
  whyItMatters:
      'Universal gravitation is the force that built the solar system, keeps satellites in orbit, and gives every object on Earth its weight. It is structurally almost identical to Coulomb\'s law — same inverse-square form — but always attractive and universal (every mass pulls every other mass, no such thing as "gravitationally neutral"). This chapter is the foundation for orbits, escape velocity, and satellite motion, all guaranteed JEE/NEET topics.',
  prediction: const PredictionPrompt(
    scenario:
        'Two masses attract each other with force F at separation r. You move them to THREE TIMES the distance (3r), keeping both masses the same. The new force is:',
    options: [
      'F/3 — force weakens proportionally with distance',
      'F/9 — force depends on 1/r²',
      '3F — closer masses always pull harder, so farther means the ratio flips',
      'The same F — gravity doesn\'t care about distance, only mass',
    ],
    correctIndex: 1,
    reveal:
        'Gravity follows 1/r² exactly like Coulomb\'s law, so tripling r divides the force by 9. In the lab, drag the separation slider to 3× its starting value and watch the force readout drop to 1/9. This steep inverse-square falloff is why the Sun\'s pull on a distant comet is negligible compared to its pull on Mercury, even though it is the SAME Sun exerting the force.',
  ),
  experiments: [
    'Set two equal masses at a given separation, then triple the distance — confirm the force drops to 1/9',
    'Double one mass and check the force exactly doubles (F ∝ m₁)',
    'Try to make the force repulsive by flipping a mass "sign" — notice you can\'t, gravity only attracts',
    'Compare the pull between two 1 kg masses at 1 m to the pull of Earth on you — see how astronomically weak G makes gravity at human scale',
    'Switch to planetary-scale masses and watch the same 1/r² law scale up to hold planets in orbit',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Newton\'s leap was realising that the force pulling an apple down and the force keeping the Moon in orbit are the same force, obeying the same law, differing only in how far apart the two masses are. Every particle of matter in the universe attracts every other particle — this is why the law is called "universal."',
      title: 'One law, from apples to orbits',
    ),
    ContentBlock.formula('F = G·m₁·m₂ / r²,   G = 6.674×10⁻¹¹ N·m²/kg²', title: 'NEWTON\'S LAW OF UNIVERSAL GRAVITATION'),
    ContentBlock.bullets([
      'F ∝ m₁ and F ∝ m₂ — double either mass, double the force',
      'F ∝ 1/r² — halve the distance, quadruple the force',
      'Direction: always ATTRACTIVE, along the line joining the two masses',
      'Acts between EVERY pair of masses, however small — there is no "gravitationally neutral" object',
    ]),
    ContentBlock.paragraph(
      'This looks like Coulomb\'s law F = kq₁q₂/r² with an important difference: mass has only one "sign" (always positive), so gravity is always attractive — there is no gravitational repulsion. Also, G is a fixed universal constant with no equivalent of a "dielectric medium" weakening it; gravity passes through matter unaffected.',
      title: 'How this compares to Coulomb\'s law',
    ),
    ContentBlock.paragraph(
      'Do not confuse G and g. G (the universal gravitational constant, 6.674×10⁻¹¹ N·m²/kg²) is the SAME everywhere in the universe. g (acceleration due to gravity, ≈9.8 m/s² on Earth) is a LOCAL quantity — it depends on which massive body you are near and how far from its centre you are. g is derived from G, not the other way around.',
      title: 'G vs g — the constant vs the consequence',
    ),
    ContentBlock.realLife(
      'Tides are gravity in action at planetary scale: the Moon pulls harder on the side of Earth nearest it than on the far side, stretching the oceans into two bulges that sweep around the Earth as it rotates, giving two high tides a day. The Sun\'s gravity contributes too — "spring tides" happen when Sun and Moon align and their pulls add up.',
    ),
    ContentBlock.mistake(
      'Confusing G with g, or plugging g into F = Gm₁m₂/r². G is a universal constant (N·m²/kg²); g is an acceleration (m/s²) specific to a location. They are related by g = GM/R² but are never interchangeable.',
    ),
    ContentBlock.mistake(
      'Forgetting that gravitational force is mutual and equal. Earth pulls on you with the same magnitude of force that you pull on Earth (Newton\'s third law) — the reason you fall toward Earth and not the reverse is simply that Earth\'s mass is so much larger, so its acceleration a = F/M_earth is negligibly small compared to yours.',
    ),
    ContentBlock.example(
      'Find the gravitational force between two 50 kg students standing 1 m apart.\n\nF = Gm₁m₂/r² = 6.674×10⁻¹¹ × 50 × 50 / 1²\n= 6.674×10⁻¹¹ × 2500\n≈ 1.67×10⁻⁷ N.\n\nThat is about the weight of a few grains of salt — gravity between everyday objects is far too weak to notice, which is exactly why it took careful laboratory measurement (Cavendish) to confirm the law at all.',
    ),
    ContentBlock.jeeTip(
      'The Cavendish experiment (1798) measured G directly using a torsion balance: two small masses hung on a thin fibre are attracted by two larger fixed masses, twisting the fibre by a tiny, measurable angle. This experiment is historically significant because Newton\'s law predicted the FORM of gravity (1/r²) a century earlier, but the actual size of G — and hence the mass of the Earth itself — was unknown until Cavendish "weighed the Earth."',
    ),
    ContentBlock.neetNote(
      'NEET often tests the relation g = GM/R² directly, and its consequence: on the Moon (mass ≈ M/81, radius ≈ R/3.7 roughly), g is about 1/6th of Earth\'s g. Also remember: gravitational force between point masses obeys superposition just like Coulomb forces — add the force VECTORS from each mass separately.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the two experimental/observational dependences',
      math: 'F ∝ m₁·m₂   (at fixed r)\nF ∝ 1/r²      (at fixed masses)',
      note: 'Inferred by Newton from Kepler\'s planetary data and free-fall experiments.',
    ),
    DerivationStep(
      title: 'Combine into a single proportionality',
      math: 'F ∝ m₁·m₂ / r²',
    ),
    DerivationStep(
      title: 'Insert the universal constant of proportionality',
      math: 'F = G · m₁m₂ / r²,   G = 6.674×10⁻¹¹ N·m²/kg²',
      note: 'G was measured independently by Cavendish; it does not depend on the masses, distance, or medium.',
    ),
    DerivationStep(
      title: 'Apply the law to a mass m at Earth\'s surface',
      math: 'F = G·M_E·m / R_E²',
      note: 'M_E = Earth\'s mass, R_E = Earth\'s radius.',
    ),
    DerivationStep(
      title: 'Equate to F = mg and cancel m',
      math: 'mg = G·M_E·m/R_E²  →  g = G·M_E/R_E²',
      note: 'This is how g emerges as a LOCAL consequence of the universal law — different planets give different g.',
    ),
  ],
  formulas: const [
    FormulaEntry('Newton\'s law of gravitation', 'F = G·m₁m₂/r²'),
    FormulaEntry('Universal gravitational constant', 'G = 6.674×10⁻¹¹ N·m²/kg²'),
    FormulaEntry('Surface gravity from G', 'g = GM/R²'),
    FormulaEntry('Earth\'s mass (from g, R, G)', 'M = gR²/G'),
    FormulaEntry('Gravitational PE (general)', 'U = −Gm₁m₂/r', condition: 'zero reference at infinity'),
    FormulaEntry('Superposition of gravitational force', 'F_net = ΣFᵢ  (vector sum)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'If the distance between two masses is doubled, the gravitational force between them becomes:',
      options: ['Twice as large', 'Half', 'One-fourth', 'Four times'],
      correctIndex: 2,
      solution: 'F ∝ 1/r². Doubling r multiplies r² by 4, so the force falls to 1/4 of its original value.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The gravitational force between two masses is always:',
      options: ['Attractive', 'Repulsive', 'Attractive or repulsive depending on mass sign', 'Zero unless charged'],
      correctIndex: 0,
      solution: 'Unlike electric charge, mass has no negative counterpart, so gravitational force is always attractive.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The value of g at Earth\'s surface is approximately 9.8 m/s², with Earth\'s radius R = 6.4×10⁶ m. Earth\'s mass is approximately (G = 6.674×10⁻¹¹ N·m²/kg²):',
      options: ['6×10²⁴ kg', '6×10²² kg', '6×10²⁶ kg', '6×10²⁰ kg'],
      correctIndex: 0,
      solution: 'M = gR²/G = 9.8×(6.4×10⁶)²/6.674×10⁻¹¹ = 9.8×4.096×10¹³/6.674×10⁻¹¹ ≈ 6.0×10²⁴ kg.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two identical spheres of mass 4 kg each attract with force F at separation r. If each mass is doubled and r is halved, the new force is:',
      options: ['4F', '8F', '16F', '2F'],
      correctIndex: 2,
      solution: 'F ∝ m₁m₂/r². Doubling both masses multiplies F by 4; halving r multiplies F by 4 more (since 1/r² → 4/r²). Total factor = 4×4 = 16.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Why does the Earth accelerate toward you far less than you accelerate toward the Earth, even though the gravitational force is equal and opposite on both?',
      options: [
        'The force on Earth is actually smaller',
        'Earth\'s enormous mass means the same force produces a tiny acceleration (a = F/M)',
        'Earth is not affected by gravity',
        'The distance is different for each body',
      ],
      correctIndex: 1,
      solution: 'By Newton\'s third law the forces are equal in magnitude. But a = F/M, and Earth\'s mass is vastly larger than yours, so its resulting acceleration is negligibly small.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The Cavendish experiment is historically important chiefly because it:',
      options: [
        'First proposed the inverse-square law of gravitation',
        'Measured the value of G, allowing Earth\'s mass to be calculated for the first time',
        'Discovered that gravity is always attractive',
        'Proved Kepler\'s laws',
      ],
      correctIndex: 1,
      solution: 'Newton had already proposed the 1/r² FORM of the law. Cavendish\'s torsion balance measured the numerical value of G, which then let scientists compute Earth\'s mass via M = gR²/G — Earth was effectively "weighed" for the first time.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Three equal point masses m are placed at the corners of an equilateral triangle of side a. The net gravitational force on one mass due to the other two has magnitude:',
      options: ['Gm²/a²', '√3·Gm²/a²', '2Gm²/a²', 'Gm²/(2a²)'],
      correctIndex: 1,
      solution:
          'Each pair exerts force Gm²/a². The two forces on one mass are equal in magnitude and separated by 60° (the triangle\'s interior angle). Resultant = 2×(Gm²/a²)×cos(30°) = 2×(Gm²/a²)×(√3/2) = √3·Gm²/a².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A particle is placed at the midpoint of the line joining two masses M and 4M, separated by distance d. Where along the line (measured from mass M) is the point where the NET gravitational force on a small test mass is zero?',
      options: ['d/3', 'd/2', 'd/5', '2d/3'],
      correctIndex: 0,
      solution:
          'Balance GM/x² = G(4M)/(d−x)². So (d−x)²/x² = 4 → (d−x)/x = 2 → d−x=2x → x=d/3. The null point is nearer the smaller mass M, exactly as in the analogous Coulomb problem.',
    ),
  ],
  revision: [
    'F = G·m₁m₂/r² — always attractive, acts along the line joining the masses, obeys superposition.',
    'F ∝ product of masses, ∝ 1/r². Halve r → 4× force; double a mass → 2× force.',
    'G (6.674×10⁻¹¹ N·m²/kg²) is universal and fixed; g (≈9.8 m/s² on Earth) is local and derived: g = GM/R².',
    'Never confuse G with g — different units, different meaning, related by g = GM/R².',
    'The Cavendish experiment measured G directly, letting scientists compute Earth\'s mass for the first time.',
    'Unlike Coulomb\'s law, gravity has no repulsive case and no medium that weakens it.',
  ],
  sandboxBuilder: (_) => const GravitationSimulator(),
);
