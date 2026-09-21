import '../../models/lesson.dart';
import '../../simulators/center_of_mass_sandbox.dart';
import '../../theme/tokens.dart';

/// Center of Mass — the single point that behaves as if it carries all the mass.
final Lesson centerOfMassLesson = Lesson(
  topicId: 'center-of-mass',
  title: 'Center of Mass',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A fireworks shell explodes mid-air into dozens of burning fragments flying off in every direction. Each fragment follows its own wild path — yet one particular point keeps sailing along the exact same smooth parabola the shell was already following, as if the explosion never happened. What is that point, and why does it not care about the explosion at all?',
  whyItMatters:
      'Center of mass is the trick that lets you treat a messy, many-part system — a rotating wrench, an exploding shell, a person walking on a boat — as if it were one single particle. Any time internal forces (explosions, collisions, muscles pulling on bones) are involved, COM motion is the one thing that stays simple, governed only by the external force. JEE and NEET repeatedly test this exact idea: internal changes never move the COM.',
  prediction: const PredictionPrompt(
    scenario:
        'A projectile is launched and follows a parabolic path. Mid-flight, an internal explosion splits it into several fragments that fly off in different directions (no external force besides gravity acts during the explosion). What happens to the center of mass of the fragments after the explosion?',
    options: [
      'It flies off in a new, unpredictable direction depending on the explosion',
      'It stops in mid-air since the object broke apart',
      'It continues along the EXACT same parabolic path the original projectile would have followed',
      'It falls straight down immediately',
    ],
    correctIndex: 2,
    reveal:
        'The explosion is an INTERNAL force — it changes how mass is distributed among the fragments, but it cannot change the total momentum of the system, because internal forces always come in equal-and-opposite pairs that cancel. Since gravity (the only external force) is unchanged, the center of mass keeps accelerating at exactly g downward, continuing on the identical parabola. In the lab, watch how repositioning masses (analogous to redistributing mass in an "explosion") never moves the COM outside the range set by the individual masses\' positions — it always responds smoothly and predictably to Σmixi/Σmi.',
  ),
  experiments: [
    'Slide mass 2 far to the right and watch the COM marker move toward it, never past it',
    'Make all three masses equal and space them evenly — the COM lands exactly at the middle position',
    'Increase mass 1 to its maximum while keeping positions fixed — the COM is pulled strongly toward mass 1',
    'Set two masses to the same position (0 separation) and treat them as one combined mass — check the COM formula still gives a sensible answer',
    'Move a mass without changing any other mass — see the COM shifts continuously and smoothly, never jumps',
  ],
  concept: const [
    ContentBlock.paragraph(
      'For a system of discrete point masses, the center of mass (COM) is the single point that represents the average position of mass in the system, weighted by how much mass is at each position. It is defined so that the system\'s total mass, if concentrated at the COM, would produce the exact same overall motion (under external forces) as the real, spread-out system.',
      title: 'What the center of mass IS',
    ),
    ContentBlock.formula('X_cm = Σmᵢxᵢ / Σmᵢ    (1D, discrete masses)', title: 'CENTER OF MASS — 1D'),
    ContentBlock.formula('X_cm = Σmᵢxᵢ/Σmᵢ ,   Y_cm = Σmᵢyᵢ/Σmᵢ    (2D, discrete masses)', title: 'CENTER OF MASS — 2D'),
    ContentBlock.bullets([
      'Each mass "pulls" the COM toward its own position, weighted by how heavy it is',
      'The COM always lies somewhere between the extreme positions of the masses — never outside the range they occupy',
      'If one mass dominates the system, the COM sits very close to that mass',
      'For a CONTINUOUS body, sums become integrals: X_cm = (1/M)∫x dm',
    ]),
    ContentBlock.paragraph(
      'This is the single most powerful fact about center of mass: no matter what happens INSIDE a system — collisions, explosions, people walking around inside a boat, springs stretching and snapping — as long as no NET EXTERNAL force acts, the center of mass moves in a straight line at constant velocity (or stays still). If an external force does act (like gravity on a projectile), the COM accelerates exactly as if all the mass were concentrated there, obeying F_ext = M_total × a_cm, completely ignorant of whatever chaos is happening internally.',
      title: 'The COM only obeys EXTERNAL force',
    ),
    ContentBlock.formula('F_ext = M_total · a_cm    (internal forces never appear in this equation)', title: 'COM MOTION EQUATION'),
    ContentBlock.paragraph(
      'For simple, uniform, symmetric shapes, the COM lies at an easily memorised geometric point — these are standard JEE/NEET facts worth knowing cold: a uniform rod\'s COM is at its midpoint; a uniform triangular lamina\'s COM is at its centroid (the intersection of medians, at 1/3 height from any side); a uniform semicircular ring\'s COM lies on the axis of symmetry at a distance 2R/π from the centre; a uniform semicircular DISC\'s COM lies at 4R/(3π) from the centre.',
      title: 'COM of standard symmetric bodies',
    ),
    ContentBlock.formula(
        'Rod: at the midpoint.   Triangle: at the centroid (1/3 height from base).\nSemicircular ring: 2R/π from centre.   Semicircular disc: 4R/(3π) from centre.',
        title: 'MEMORISE THESE SHAPES'),
    ContentBlock.realLife(
      'Picking up a heavy suitcase in one hand shifts your overall COM sideways — your body instinctively leans the opposite way to keep your combined COM (you + suitcase) above your feet, or you would topple over. Gymnasts, tightrope walkers and even a simple pencil balanced on a finger are all really just games of keeping the COM directly above the point of support.',
    ),
    ContentBlock.mistake(
      'Assuming the COM must lie ON the body itself. For an irregular or hollow shape (like a ring, a horseshoe, or a boomerang), the COM can sit in empty space where there is no material at all — it is a mathematical point defined by the mass DISTRIBUTION, not a physical marker on the object.',
    ),
    ContentBlock.mistake(
      'Believing internal forces (an explosion, a spring release, an internal collision) can change the COM\'s velocity. They cannot — internal forces always occur in equal-and-opposite Newton\'s-third-law pairs across the system, so they cancel out completely when you sum forces over the whole system. Only a genuinely external force (gravity, an outside push) can change how the COM moves.',
    ),
    ContentBlock.example(
      'Point masses of 2 kg, 3 kg and 5 kg are placed at x = 0 m, x = 2 m and x = 6 m respectively on the x-axis. Find the x-coordinate of the center of mass.\n\nX_cm = (2×0 + 3×2 + 5×6) / (2+3+5) = (0 + 6 + 30) / 10 = 36/10 = 3.6 m.\n\nNotice the COM (3.6 m) sits closer to the 5 kg mass at x=6 m than to the lighter masses — exactly as expected, since heavier masses pull the COM toward themselves.',
    ),
    ContentBlock.jeeTip(
      'The classic "two masses on a spring/string on a frictionless surface" problem: if released from rest with no external horizontal force, the COM stays fixed the whole time. Use this to relate the two masses\' displacements directly: m₁x₁ = m₂x₂ (measuring each displacement from its own starting point, since the COM does not move) — this shortcut avoids solving the full dynamics of the spring.',
    ),
    ContentBlock.neetNote(
      'NEET often tests direct-recall COM positions for standard shapes (rod, triangle, semicircular ring/disc) as given above, and the "explosion during projectile motion" concept — always remember: no external force ⟹ COM path is unaffected, only its momentum gets redistributed among the fragments.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define center of mass for a system of particles',
      math: 'X_cm = Σmᵢxᵢ / Σmᵢ = Σmᵢxᵢ / M',
      note: 'M = total mass of the system. This is a mass-weighted average position.',
    ),
    DerivationStep(
      title: 'Differentiate with respect to time to get COM velocity',
      math: 'M·v_cm = Σmᵢvᵢ = P_total',
      note: 'Total momentum of the system equals total mass times COM velocity — a very useful identity.',
    ),
    DerivationStep(
      title: 'Differentiate again to get COM acceleration',
      math: 'M·a_cm = Σmᵢaᵢ = ΣF_i (all forces, internal + external)',
    ),
    DerivationStep(
      title: 'Apply Newton\'s third law to eliminate internal forces',
      math: 'Internal forces occur in pairs Fᵢⱼ = −Fⱼᵢ, so Σ(internal forces) = 0',
      note: 'Every internal push/pull is cancelled by its equal-and-opposite reaction somewhere else in the sum.',
    ),
    DerivationStep(
      title: 'Conclude: only external force governs COM motion',
      math: 'M·a_cm = F_external',
      note: 'This is why explosions, collisions and internal rearrangements never change how the COM itself moves.',
    ),
  ],
  formulas: const [
    FormulaEntry('Center of mass, 1D', 'X_cm = Σmᵢxᵢ/Σmᵢ'),
    FormulaEntry('Center of mass, 2D', 'X_cm = Σmᵢxᵢ/Σmᵢ,  Y_cm = Σmᵢyᵢ/Σmᵢ'),
    FormulaEntry('COM motion equation', 'F_ext = M·a_cm'),
    FormulaEntry('Total momentum via COM', 'P = M·v_cm'),
    FormulaEntry('Uniform rod', 'COM at the midpoint'),
    FormulaEntry('Uniform triangular lamina', 'COM at the centroid, 1/3 height from base'),
    FormulaEntry('Semicircular ring / disc', 'ring: 2R/π from centre;  disc: 4R/(3π) from centre'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Point masses 1 kg and 3 kg are placed at x = 0 m and x = 4 m. The center of mass is at:',
      options: ['1 m', '2 m', '3 m', '4 m'],
      correctIndex: 2,
      solution: 'X_cm = (1×0 + 3×4)/(1+3) = 12/4 = 3 m — closer to the heavier 3 kg mass, as expected.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The center of mass of a uniform triangular lamina lies at:',
      options: ['One of its vertices', 'The midpoint of the longest side', 'The centroid (intersection of medians)', 'The circumcentre'],
      correctIndex: 2,
      solution: 'For a uniform lamina, the COM coincides with the geometric centroid, located 1/3 of the height from any side.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A shell in flight explodes into two fragments under only its own internal explosive force (gravity still acts on both). The center of mass of the fragments, immediately after explosion, will:',
      options: [
        'Change its path completely, in a random new direction',
        'Continue exactly along the original projectile parabola',
        'Come to rest instantly',
        'Move only horizontally from then on',
      ],
      correctIndex: 1,
      solution: 'The explosion is purely internal, so it cannot change the net external force (still just gravity). The COM continues to accelerate at g downward exactly as before, following the same parabola the unexploded shell would have followed.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two blocks of mass 2 kg and 4 kg connected by a spring rest on a frictionless surface. The spring is compressed and released. If the 2 kg block moves 6 cm from its initial position, the 4 kg block moves (in the opposite direction):',
      options: ['12 cm', '6 cm', '3 cm', '24 cm'],
      correctIndex: 2,
      solution: 'No external horizontal force acts, so the COM stays fixed: m₁x₁ = m₂x₂ ⟹ 2×6 = 4×x₂ ⟹ x₂ = 3 cm.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A person of mass 60 kg stands at one end of a stationary 90 kg boat, 6 m long, floating on frictionless water. The person walks to the other end of the boat. How far does the boat move (treating the boat + person system\'s COM as fixed)?',
      options: ['2.4 m', '4 m', '1.6 m', '3 m'],
      correctIndex: 0,
      solution: 'COM of the system stays fixed (no external horizontal force). If person moves 6 m relative to the boat, and boat moves distance d opposite to the person: 60×(6−d) = 90×d ⟹ 360 − 60d = 90d ⟹ 360 = 150d ⟹ d = 2.4 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Three identical point masses m are placed at the corners of an equilateral triangle of side a. The distance of the center of mass from any one vertex is:',
      options: ['a/√3', 'a/2', 'a√3/2', 'a'],
      correctIndex: 0,
      solution: 'For equal masses, COM coincides with the centroid. The centroid-to-vertex distance for an equilateral triangle of side a is a/√3 (since the median length is (√3/2)a, and the centroid divides it 2:1 from the vertex, giving (2/3)(√3/2)a = a/√3).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A uniform semicircular disc of radius R has its center of mass at a distance from the centre O equal to:',
      options: ['2R/π', '4R/(3π)', 'R/2', '3R/(4π)'],
      correctIndex: 1,
      solution: 'The COM of a uniform semicircular DISC (a solid lamina, not just the arc) lies at 4R/(3π) from the centre along the axis of symmetry — a standard result distinct from the semicircular RING\'s 2R/π.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A disc of radius R has a circular hole of radius R/2 cut out, with the hole\'s centre at a distance R/2 from the disc\'s centre (the hole is entirely within the disc, tangent internally). Treating the removed material as "negative mass," the shift of the center of mass from the original centre is:',
      options: ['R/6, away from the hole', 'R/3, toward the hole', 'R/6, toward the hole', 'R/2, away from the hole'],
      correctIndex: 0,
      solution: 'Using negative mass for the hole: full disc mass M (∝R²) at x=0, hole mass M/4 (∝(R/2)²) at x=R/2. X_cm = [M(0) − (M/4)(R/2)] / (M − M/4) = (−MR/8)/(3M/4) = −R/6. The COM shifts by R/6 AWAY from the hole (toward the side with more remaining material).',
    ),
  ],
  revision: [
    'Center of mass: X_cm = Σmᵢxᵢ/Σmᵢ — a mass-weighted average position, always between the extreme mass positions.',
    'Only EXTERNAL force governs COM motion: F_ext = M·a_cm — internal forces (explosions, collisions, springs) always cancel in pairs.',
    'A shell exploding mid-flight still has its COM follow the same parabola, since gravity (external) is unchanged.',
    'Standard shapes: rod → midpoint; triangle → centroid (1/3 height from base); semicircular ring → 2R/π from centre; semicircular disc → 4R/(3π) from centre.',
    'Two masses connected by a spring on a frictionless floor, released from rest: COM stays fixed, so m₁x₁ = m₂x₂ for their displacements.',
    'The COM need not lie on the physical material of the body — for rings, hollow shapes and "hole cut from a disc" problems it can sit in empty space.',
    'Picking up a suitcase or walking on a boat both work by keeping the combined system\'s COM in balance or, absent external force, exactly fixed.',
  ],
  sandboxBuilder: (_) => const CenterOfMassSandbox(),
);
