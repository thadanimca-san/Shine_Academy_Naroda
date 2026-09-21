import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import '../../simulators/gauss_law_sandbox.dart';

/// Gauss's Law — turning symmetry into a shortcut for the electric field.
final Lesson gaussLawLesson = Lesson(
  topicId: 'gauss-law',
  title: 'Gauss\'s Law',
  bigQuestion:
      'A charge sits somewhere near a closed bag drawn in space, no matter how oddly shaped. Field lines from the charge might poke through the bag\'s wall dozens of times — yet is there one number, counting all those crossings, that only cares whether the charge is inside or outside?',
  whyItMatters:
      'Gauss\'s law is Coulomb\'s law in disguise, restated in a form that makes highly symmetric problems almost trivial. Instead of adding up forces or fields from every bit of a charged sphere, sheet, or wire, you draw one clever imaginary surface and the answer falls out in a few lines. It is also the first of Maxwell\'s four equations — the same law you will meet again, unchanged, when studying electromagnetic waves.',
  prediction: const PredictionPrompt(
    scenario:
        'A charge +Q sits just OUTSIDE a closed spherical surface, very close to its wall. Field lines from the charge clearly pass through the sphere\'s near side. What is the total electric flux through the closed surface?',
    options: [
      'A large positive value, since field lines cross it',
      'Exactly zero',
      'A small positive value, proportional to how close the charge is',
      'Negative, since the charge is outside',
    ],
    correctIndex: 1,
    reveal:
        'Flux depends only on ENCLOSED charge. In the lab, toggle the charge to "outside" and watch: field lines still pierce the sphere, entering on the near side and exiting on the far side — but every line that enters also leaves, so the readout locks to exactly zero no matter how close you place the charge. Move it "inside" and the flux jumps straight to Q/ε₀.',
  ),
  experiments: [
    'Toggle the charge INSIDE and watch flux jump to Q/ε₀ immediately',
    'Toggle the charge OUTSIDE and confirm flux reads exactly 0, even though lines still cross the surface',
    'Increase Q while charge is inside and see flux scale up proportionally, linearly',
    'Increase Q while charge is outside — flux stays locked at 0 regardless of how large Q gets',
    'Notice the entry and exit dots on the surface when the charge is outside — count them and see they always come in pairs',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Electric flux Φ through a surface measures how much electric field "flows" through it — formally, the surface integral of E·dA over every tiny patch of the surface, where dA is a vector pointing outward normal to the patch. For a flat surface in a uniform field, this simplifies to Φ = E·A·cosθ, where θ is the angle between the field and the surface normal. Flux is a scalar and can be positive (field leaving the surface) or negative (field entering).',
      title: 'Electric flux: counting field lines through a surface',
    ),
    ContentBlock.formula('Φ = ∮ E·dA   (surface integral, general case)', title: 'ELECTRIC FLUX'),
    ContentBlock.paragraph(
      'Gauss\'s law states that the total flux through ANY closed surface equals the total charge enclosed by that surface, divided by ε₀. The surface — called a Gaussian surface — is imaginary; you choose its shape purely for mathematical convenience. This is one of the most powerful shortcuts in all of electrostatics.',
      title: 'Gauss\'s law',
    ),
    ContentBlock.formula('Φ = Q_enclosed / ε₀', title: 'GAUSS\'S LAW'),
    ContentBlock.paragraph(
      'Why does the SHAPE and SIZE of the surface not matter, and why do charges OUTSIDE contribute nothing? Picture field lines from a point charge spreading out radially in all directions, like spokes from a hub. Any closed surface enclosing the charge must be crossed by every single one of those lines exactly once, net — the geometry guarantees it regardless of the surface\'s shape, because field lines only start on charges and never end except on charges. A charge sitting outside is different: every field line from it that enters the closed surface on one side must also exit somewhere else (field lines cannot simply stop in empty space), so its net contribution to the flux is exactly zero — entry and exit always cancel in pairs.',
      title: 'Why only enclosed charge counts (the intuitive picture)',
    ),
    ContentBlock.bullets([
      'The Gaussian surface is imaginary — no real material needs to be there',
      'Only ENCLOSED charge appears in Q_enclosed; charges outside contribute zero net flux',
      'The FIELD at the surface can still be affected by outside charges — Gauss\'s law only isolates the FLUX integral, not the field itself, except in symmetric cases',
      'Choosing a surface that matches the symmetry of the charge distribution (sphere for a point charge, cylinder for a line charge, pillbox for a sheet) makes E come straight out of the integral',
    ]),
    ContentBlock.paragraph(
      'The real power of Gauss\'s law is deriving the field of extended charge distributions in just a few lines, by picking a Gaussian surface that matches the symmetry so that E is constant in magnitude over the whole surface (or over the curved parts) and can be pulled outside the integral. Three results appear constantly in JEE/NEET: the field outside a uniformly charged sphere, the field of an infinite charged sheet, and the field of an infinite line charge.',
      title: 'Three classic results',
    ),
    ContentBlock.formula('E = kQ/r²   (uniformly charged sphere, outside, r ≥ R)',
        title: 'FIELD OF A CHARGED SPHERE'),
    ContentBlock.formula('E = σ/(2ε₀)   (infinite charged sheet, σ = surface charge density)',
        title: 'FIELD OF AN INFINITE SHEET'),
    ContentBlock.formula('E = λ/(2πε₀r)   (infinite line charge, λ = linear charge density)',
        title: 'FIELD OF AN INFINITE LINE CHARGE'),
    ContentBlock.realLife(
      'A car acts as a rough Faraday cage in a lightning strike: charge redistributes on the metal body so the field inside stays near zero, protecting the occupants — this is Gauss\'s law at work, since the interior of any closed conductor with no enclosed charge has zero flux and (in electrostatic equilibrium) zero field. The same principle shields sensitive electronics inside grounded metal enclosures.',
    ),
    ContentBlock.mistake(
      'Believing that flux depends on the field produced by charges outside the surface. It does not — the FLUX INTEGRAL isolates only the enclosed charge, always. What outside charges CAN do is distort the field distribution ON the surface (making E stronger in some patches and weaker in others), but when you add up (integrate) the flux over the whole closed surface, all of that redistribution cancels out and only Q_enclosed survives.',
    ),
    ContentBlock.example(
      'A closed spherical surface of radius 20 cm encloses a net charge of +6 nC, along with several other charges positioned outside the sphere. Find the total flux through the sphere.\n\nΦ = Q_enclosed/ε₀ = 6×10⁻⁹ / 8.85×10⁻¹²\n≈ 678 N·m²/C.\n\nThe outside charges are completely irrelevant to this calculation — only the enclosed +6 nC matters, no matter how many other charges surround the sphere or how strong the field is at its surface.',
    ),
    ContentBlock.jeeTip(
      'For an infinite line charge, remember the field falls as 1/r (not 1/r²) — this is a very common JEE trap because students default to inverse-square reasoning. The Gaussian surface here is a coaxial CYLINDER: the curved surface area is 2πrL, and only the charge λL is enclosed, giving E(2πrL) = λL/ε₀ → E = λ/(2πε₀r).',
    ),
    ContentBlock.jeeTip(
      'For an infinite charged sheet, the Gaussian "pillbox" (a small cylinder straddling the sheet) has flux leaving through BOTH flat end-caps (none through the curved side, by symmetry), giving 2EA = σA/ε₀ → E = σ/(2ε₀). Note this field does NOT depend on distance from the sheet — a hallmark of infinite-sheet geometry.',
    ),
    ContentBlock.neetNote(
      'NEET often asks a conceptual flux question: if the enclosed charge is doubled, flux doubles (Φ ∝ Q_enclosed only — NOT on the size or shape of the surface). If the SAME charge is enclosed by a bigger sphere, the flux is UNCHANGED even though the field at the larger surface is weaker — the field drop and the larger area exactly compensate.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the field of a single point charge',
      math: 'E = kQ/r²   (radially outward)',
      note: 'Choose a spherical Gaussian surface of radius r centred on the charge — by symmetry E is the same magnitude everywhere on it, and always parallel to dA.',
    ),
    DerivationStep(
      title: 'Compute the flux through that sphere',
      math: 'Φ = E × (surface area) = (kQ/r²) × 4πr²',
      note: 'The r² cancels exactly — a direct consequence of the inverse-square law.',
    ),
    DerivationStep(
      title: 'Simplify using k = 1/(4πε₀)',
      math: 'Φ = 4πkQ = 4π × Q/(4πε₀) = Q/ε₀',
      note: 'This is why the 4π was tucked into the definition of k back in Coulomb\'s law — it makes this result clean.',
    ),
    DerivationStep(
      title: 'Generalise: any closed surface, any position of the charge inside',
      math: 'Φ = Q/ε₀   (independent of the surface\'s shape or the charge\'s position inside it)',
      note: 'The solid angle subtended by any patch of surface, seen from the charge, is what makes this shape-independent — every field line still gets counted exactly once net.',
    ),
    DerivationStep(
      title: 'Charges outside contribute zero',
      math: 'Φ_outside charge = 0',
      note: 'Every field line entering the closed surface from an external charge must also exit it, since field lines cannot terminate in empty space — entry and exit cancel.',
    ),
  ],
  formulas: const [
    FormulaEntry('Electric flux (general)', 'Φ = ∮ E·dA'),
    FormulaEntry('Flux through a flat surface in uniform field', 'Φ = E·A·cosθ'),
    FormulaEntry('Gauss\'s law', 'Φ = Q_enclosed/ε₀'),
    FormulaEntry('Field of a uniformly charged sphere (outside)', 'E = kQ/r²,  r ≥ R'),
    FormulaEntry('Field of an infinite charged sheet', 'E = σ/(2ε₀)'),
    FormulaEntry('Field of an infinite line charge', 'E = λ/(2πε₀r)'),
    FormulaEntry('Permittivity of free space', 'ε₀ = 8.85×10⁻¹² C²/(N·m²)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A closed surface encloses a net charge of zero, although several individual charges sit both inside and outside it. The total electric flux through the surface is:',
      options: ['Infinite', 'Zero', 'Equal to the largest charge divided by ε₀', 'Cannot be determined'],
      correctIndex: 1,
      solution: 'Flux depends only on the NET enclosed charge. If the enclosed charges sum to zero (regardless of what sits outside), Φ = 0/ε₀ = 0.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'If the charge enclosed by a Gaussian surface is doubled while keeping the surface fixed, the electric flux through the surface:',
      options: ['Stays the same', 'Doubles', 'Quadruples', 'Halves'],
      correctIndex: 1,
      solution: 'Φ = Q_enclosed/ε₀ is directly proportional to the enclosed charge, so doubling Q doubles Φ.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A point charge of 8.85 nC is placed at the centre of a cube. The electric flux through ONE face of the cube is:',
      options: ['1000 N·m²/C', '166.7 N·m²/C', '6000 N·m²/C', '8850 N·m²/C'],
      correctIndex: 1,
      solution: 'Total flux through the cube = Q/ε₀ = 8.85×10⁻⁹/8.85×10⁻¹² = 1000 N·m²/C. By symmetry this splits equally among the 6 faces: 1000/6 ≈ 166.7 N·m²/C per face.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A charge Q is placed at the centre of a sphere of radius R. If the radius is doubled to 2R (same enclosed charge), the flux through the new surface compared to the old is:',
      options: ['Twice as large', 'One-fourth', 'The same', 'Four times as large'],
      correctIndex: 2,
      solution: 'Φ = Q_enclosed/ε₀ does not depend on the surface\'s size at all — as long as the same charge Q is enclosed, the flux is identical for any radius.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The electric field due to an infinite line charge of linear charge density λ at a perpendicular distance r is proportional to:',
      options: ['1/r', '1/r²', 'r', 'Independent of r'],
      correctIndex: 0,
      solution: 'E = λ/(2πε₀r) for an infinite line charge — the field falls as 1/r, one power slower than a point charge\'s 1/r², because of the cylindrical (not spherical) symmetry.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The electric field near an infinite charged conducting sheet with surface charge density σ is E = σ/ε₀ (not σ/2ε₀ as for a non-conducting sheet). This is because:',
      options: [
        'Conductors always have twice the charge density',
        'For a conductor, charge resides only on the outer surface facing outward, so field lines emerge from just one side effectively doubling the pillbox result',
        'The formula for conductors is simply a historical convention',
        'Conductors do not follow Gauss\'s law',
      ],
      correctIndex: 1,
      solution: 'For an isolated charged conducting sheet, the field inside the conductor is zero, so all the flux from the Gaussian pillbox emerges through the outward-facing cap only: EA = σA/ε₀ → E = σ/ε₀. This differs from the non-conducting sheet case, where flux emerges symmetrically through both faces, giving E = σ/(2ε₀) on each side.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A point charge is placed just outside a closed cubical surface, very near one face. The flux through that closed cube is:',
      options: [
        'Large and positive, since the field is strong there',
        'Exactly zero',
        'Equal to Q/ε₀ regardless of position',
        'Negative',
      ],
      correctIndex: 1,
      solution: 'Since the charge is NOT enclosed, every field line entering the cube through the near face must exit somewhere else — net flux through the closed surface is exactly zero, however strong the local field is.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A solid non-conducting sphere of radius R carries a total charge Q uniformly distributed through its volume. The electric field at a distance r < R from the centre is:',
      options: ['kQ/r²', 'kQr/R³', 'kQ/R²', 'Zero'],
      correctIndex: 1,
      solution: 'Using a Gaussian sphere of radius r < R, the enclosed charge is Q_enc = Q(r³/R³) (proportional to enclosed volume, since the charge is uniform). Gauss\'s law gives E(4πr²) = Q(r³/R³)/ε₀ → E = kQr/R³. The field rises linearly with r inside a uniformly charged sphere, reaching kQ/R² at the surface, then falls as kQ/r² outside.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Gauss\'s law is most useful for calculating the electric field when:',
      options: [
        'The charge distribution has no particular symmetry',
        'The charge distribution has spherical, cylindrical, or planar symmetry',
        'Only for point charges in a vacuum',
        'Only when the enclosed charge is zero',
      ],
      correctIndex: 1,
      solution: 'Gauss\'s law becomes a quick calculation tool only when a Gaussian surface can be chosen so that E is constant in magnitude over the surface (or the relevant part of it) — this happens for spherical, cylindrical, or planar symmetry, letting E come outside the flux integral.',
    ),
  ],
  revision: [
    'Φ = ∮E·dA is electric flux; Gauss\'s law: Φ = Q_enclosed/ε₀.',
    'Only ENCLOSED charge matters — surface shape, size, and position of charge inside are all irrelevant.',
    'Charges outside a closed surface contribute exactly zero net flux (entry and exit cancel).',
    'Field of a charged sphere (outside): E = kQ/r²; sheet: E = σ/(2ε₀); line: E = λ/(2πε₀r).',
    'Inside a uniformly charged solid sphere, E grows linearly with r: E = kQr/R³.',
    'Choose the Gaussian surface to match the charge distribution\'s symmetry — that is the entire trick.',
    'External charges can distort the field ON the surface, but never the total flux through it.',
  ],
  sandboxBuilder: (_) => const GaussLawSandbox(),
  accentColor: Palette.chElectroMag,
);
