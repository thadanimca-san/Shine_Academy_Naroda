import '../../models/lesson.dart';
import '../../simulators/moment_inertia_lab_sim.dart';
import '../../theme/tokens.dart';

/// Moment of Inertia — rotational inertia, and why WHERE the mass sits matters as much as HOW MUCH.
final Lesson momentInertiaLesson = Lesson(
  topicId: 'moment-of-inertia',
  title: 'Moment of Inertia',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A solid disc and a ring have exactly the same mass and the same radius. You apply the same twisting force to both. Which one starts spinning faster — or do they spin up identically since their mass is equal?',
  whyItMatters:
      'Every rotating object — a fan, a wheel, a planet, a figure skater pulling in her arms — obeys the rotational version of Newton\'s second law, and moment of inertia I is the "mass" in that law. It is the single idea that separates translational and rotational mechanics, and it feeds directly into rolling motion, angular momentum, and torque — three back-to-back JEE/NEET chapters. Skip this and rolling motion becomes memorised formulas instead of understood physics.',
  prediction: const PredictionPrompt(
    scenario:
        'A solid disc and a ring have equal mass M and equal radius R. The SAME torque is applied to both, starting from rest. After a fixed time, which is spinning faster?',
    options: [
      'Both spin up identically — mass is the same',
      'The disc spins faster — its mass sits closer to the axis on average',
      'The ring spins faster — a bigger radius always wins',
      'It depends only on the torque, not on shape',
    ],
    correctIndex: 1,
    reveal:
        'The disc wins. Its mass is smeared across the whole area, so most of it sits closer to the axis than the ring\'s mass, which is all parked at the rim. Moment of inertia I = ½MR² for the disc but I = MR² for the ring — twice as much for the same M and R. Since angular acceleration α = τ/I, the ring with double the I gets half the α. In the lab, apply equal torque to both shapes and watch the disc\'s angular velocity readout pull ahead immediately.',
  ),
  experiments: [
    'Apply equal torque to the disc and the ring (same M, R) — watch the disc spin up faster',
    'Switch to the solid sphere and compare its spin-up rate to the disc — the sphere wins again',
    'Slide mass outward on the rod (increase the "distribution radius") and watch I climb even though total mass is unchanged',
    'Try the parallel-axis toggle: shift the rotation axis off-centre and watch I jump by Md²',
    'Set torque to zero and confirm nothing spins — I alone does nothing without a torque',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Mass measures how hard it is to change an object\'s straight-line velocity — that\'s inertia. Moment of inertia I measures how hard it is to change an object\'s ANGULAR velocity — it is "rotational inertia." But unlike mass, I is not a fixed property of an object: it depends on which axis you spin it about and how the mass is arranged relative to that axis.',
      title: 'Rotational inertia: mass\'s rotational twin',
    ),
    ContentBlock.formula('I = Σ mᵢrᵢ²   (or ∫ r² dm for a continuous body)', title: 'DEFINITION OF MOMENT OF INERTIA'),
    ContentBlock.paragraph(
      'Here r is each mass element\'s perpendicular distance from the rotation axis — not from any fixed point. Because r is SQUARED, mass far from the axis contributes far more to I than the same mass close to the axis. This is the single most important idea in this chapter: total mass alone tells you almost nothing about I; distribution is everything.',
      title: 'Distance matters more than mass',
    ),
    ContentBlock.bullets([
      'Ring / hoop about its central axis: I = MR² — all mass at radius R',
      'Solid disc / cylinder about its central axis: I = ½MR² — mass spread from 0 to R',
      'Solid sphere about a diameter: I = (2/5)MR²',
      'Hollow sphere (thin shell) about a diameter: I = (2/3)MR²',
      'Thin rod about its centre: I = ML²/12; about one end: I = ML²/3',
    ], title: 'Standard shapes you must memorise'),
    ContentBlock.paragraph(
      'It is common to write I = kMR², where k is a pure number (½ for a disc, 1 for a ring, 2/5 for a sphere) that captures the shape\'s mass distribution independent of actual mass or size. A smaller k means the mass is concentrated nearer the axis, so the object is "rotationally lighter" and easier to spin up or slow down — this k reappears constantly in rolling motion.',
      title: 'The shape factor k',
    ),
    ContentBlock.realLife(
      'Flywheels in engines are deliberately built as rings or thick rims rather than solid discs of the same mass — concentrating mass at the rim maximises I, so the flywheel stores more rotational kinetic energy and smooths out engine pulses better per kilogram of material.',
    ),
    ContentBlock.mistake(
      'Assuming a heavier object always has a larger I. A 1 kg ring of radius 10 cm has I = 0.01 kg·m², while a 2 kg disc of the same radius has I = ½×2×0.01 = 0.01 kg·m² too — identical I despite double the mass, because the disc\'s distribution compensates. Always check BOTH mass and shape/axis.',
    ),
    ContentBlock.mistake(
      'Forgetting that I depends on the axis. The same rod has I = ML²/12 about its centre but I = ML²/3 about its end — four times larger. Never quote a moment of inertia without specifying (or assuming from context) the axis.',
    ),
    ContentBlock.example(
      'Find the moment of inertia of a 2 kg ring of radius 0.5 m about its central axis, and compare it with a disc of the same mass and radius.\n\nRing: I = MR² = 2 × (0.5)² = 0.5 kg·m².\nDisc: I = ½MR² = ½ × 2 × (0.5)² = 0.25 kg·m².\n\nThe ring has exactly double the disc\'s I — consistent with all its mass sitting at the rim instead of being spread inward.',
    ),
    ContentBlock.jeeTip(
      'The PARALLEL AXIS THEOREM lets you shift the axis away from the centre of mass: I = I_cm + Md², where d is the distance between the two parallel axes. It is used constantly for rods pivoted at an end, discs rolling on a rim, and compound bodies. The PERPENDICULAR AXIS THEOREM (planar/2D laminas only) states I_z = I_x + I_y, where x, y are perpendicular axes in the plane of the lamina and z is perpendicular to it — used to find a disc\'s I about a diameter from its I about the central axis.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests direct recall of the standard I formulas and simple parallel-axis shifts — memorise the table above cold. A common NEET question: I of a disc about a diameter (using perpendicular axis: I_diameter = ½ I_central = ¼MR²) versus about a tangent in its own plane (parallel axis: I = ¼MR² + MR² = 5MR²/4).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from Newton\'s second law for one particle in rotation',
      math: 'F = ma_t,  where a_t = rα (tangential acceleration)',
      note: 'Every particle in a rigid body shares the same angular acceleration α.',
    ),
    DerivationStep(
      title: 'Convert force to torque for that particle',
      math: 'τᵢ = Fᵢ·r = (mᵢr α)·r = mᵢr²α',
    ),
    DerivationStep(
      title: 'Sum torques over every particle in the rigid body',
      math: 'τ_net = Σ mᵢrᵢ²α = α·Σ mᵢrᵢ²',
      note: 'α is common to all particles, so it factors out of the sum.',
    ),
    DerivationStep(
      title: 'Define the sum as the moment of inertia',
      math: 'I ≡ Σ mᵢrᵢ²   →   τ = Iα',
      note: 'This is the rotational analogue of F = ma — I plays the role of mass.',
    ),
    DerivationStep(
      title: 'Extend to a continuous body',
      math: 'I = ∫ r² dm',
      note: 'Integrating this over a ring, disc, rod or sphere produces the standard formulas.',
    ),
  ],
  formulas: const [
    FormulaEntry('Definition', 'I = Σ mᵢrᵢ² = ∫ r² dm'),
    FormulaEntry('Rotational Newton\'s law', 'τ = Iα'),
    FormulaEntry('Ring/hoop (central axis)', 'I = MR²'),
    FormulaEntry('Disc/cylinder (central axis)', 'I = ½MR²'),
    FormulaEntry('Solid sphere (diameter)', 'I = (2/5)MR²'),
    FormulaEntry('Hollow sphere (diameter)', 'I = (2/3)MR²'),
    FormulaEntry('Rod (centre / end)', 'I = ML²/12,  I = ML²/3'),
    FormulaEntry('Parallel axis theorem', 'I = I_cm + Md²'),
    FormulaEntry('Perpendicular axis theorem', 'I_z = I_x + I_y', condition: 'planar lamina only'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The moment of inertia of a ring of mass M and radius R about its central axis is:',
      options: ['½MR²', 'MR²', '(2/5)MR²', '(2/3)MR²'],
      correctIndex: 1,
      solution: 'All the ring\'s mass lies at radius R from the axis, so I = MR² directly from the definition.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A disc and a ring have equal mass and radius. The disc\'s moment of inertia compared to the ring\'s is:',
      options: ['Equal', 'Twice as large', 'Half as large', 'Four times as large'],
      correctIndex: 2,
      solution: 'I_disc = ½MR², I_ring = MR². The disc\'s I is exactly half the ring\'s, because its mass is spread inward from the rim.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A thin rod of mass 3 kg and length 2 m rotates about an axis through one end, perpendicular to its length. Its moment of inertia is:',
      options: ['1 kg·m²', '2 kg·m²', '4 kg·m²', '6 kg·m²'],
      correctIndex: 2,
      solution: 'About an end, I = ML²/3 = 3×(2)²/3 = 12/3 = 4 kg·m².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A solid sphere of mass 5 kg and radius 0.2 m has moment of inertia about its diameter equal to:',
      options: ['0.08 kg·m²', '0.2 kg·m²', '0.4 kg·m²', '0.02 kg·m²'],
      correctIndex: 0,
      solution: 'I = (2/5)MR² = 0.4 × 5 × (0.2)² = 0.4 × 5 × 0.04 = 0.08 kg·m².',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A disc of mass M and radius R has I_cm = ½MR² about its central axis. Its moment of inertia about a tangential axis in its own plane is:',
      options: ['½MR²', 'MR²', '(5/4)MR²', '(3/2)MR²'],
      correctIndex: 2,
      solution:
          'First get I about a diameter using the perpendicular axis theorem: I_diameter = ½I_central = ¼MR². The tangential axis in the disc\'s plane is parallel to a diameter, offset by d = R, so by the parallel axis theorem I = ¼MR² + MR² = (5/4)MR².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Two torques of equal magnitude are applied separately, from rest, to a ring and to a solid sphere of the same mass and radius. After the same time interval, the ratio of their angular velocities ω_ring : ω_sphere is:',
      options: ['1 : 1', '2 : 5', '5 : 2', '2 : 3'],
      correctIndex: 1,
      solution:
          'ω = αt = (τ/I)t, so ω ∝ 1/I at fixed τ and t. I_ring = MR², I_sphere = (2/5)MR². Ratio ω_ring:ω_sphere = I_sphere:I_ring = (2/5):1 = 2:5.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A uniform disc of mass M and radius R has a smaller disc of radius R/2 removed from one edge (the small disc\'s edge touches the big disc\'s centre and rim, tangent internally). What tool is essential to find the moment of inertia of the remaining piece about the original centre?',
      options: [
        'Perpendicular axis theorem only',
        'Parallel axis theorem, applied to subtract the removed piece\'s I about the main axis',
        'Direct integration of the remaining shape only',
        'The removed piece can be ignored since it is symmetric',
      ],
      correctIndex: 1,
      solution:
          'Treat the removed disc as negative mass. Its own I about ITS centre is known, but you need its I about the ORIGINAL axis (centre of the big disc), which requires the parallel axis theorem I = I_cm + Md² using the offset between the two centres. Then subtract from the full disc\'s I.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A rod of mass M, length L rotates about an axis perpendicular to it, at a distance L/4 from one end. Its moment of inertia is:',
      options: ['ML²/12', 'ML²/6', '7ML²/48', 'ML²/4'],
      correctIndex: 2,
      solution:
          'Distance from centre to the new axis: d = L/2 − L/4 = L/4. Parallel axis: I = ML²/12 + M(L/4)² = ML²/12 + ML²/16. LCM of 12,16 is 48: ML²/12 = 4ML²/48, ML²/16 = 3ML²/48. Sum = 7ML²/48.',
    ),
  ],
  revision: [
    'I = Σmr² (or ∫r²dm) — rotational inertia depends on mass DISTRIBUTION, not just total mass.',
    'τ = Iα is the rotational analogue of F = ma.',
    'Ring: I = MR². Disc: I = ½MR². Solid sphere: I = (2/5)MR². Hollow sphere: I = (2/3)MR². Rod (centre/end): ML²/12, ML²/3.',
    'Parallel axis theorem: I = I_cm + Md² — shifts the axis away from the centre of mass.',
    'Perpendicular axis theorem (planar bodies only): I_z = I_x + I_y.',
    'Smaller shape factor k in I = kMR² means mass is concentrated near the axis — easier to spin up.',
    'Same mass and radius, different shape → different I → different response to the same torque.',
  ],
  sandboxBuilder: (_) => const MomentInertiaLabSimulator(),
);
