import '../../models/lesson.dart';
import '../../simulators/bohr_model_sandbox.dart';
import '../../theme/tokens.dart';

/// Bohr Model — quantised orbits and the hydrogen spectrum.
final Lesson bohrModelLesson = Lesson(
  topicId: 'bohr-model',
  title: 'Bohr Model of the Atom',
  accentColor: Palette.chModern,
  bigQuestion:
      'If electrons orbit the nucleus like planets orbit the sun, classical physics demands they should continuously radiate energy and spiral into the nucleus in a fraction of a second — atoms should not exist. Yet here you are, made of stable atoms. What rule did Bohr add to save the atom from collapsing?',
  whyItMatters:
      'The Bohr model is the bridge between classical and quantum physics, and it is one of the most heavily tested topics in NEET and JEE modern physics. The formulas for orbit radius, energy levels, and spectral lines appear in numerical problems almost every year, and the hydrogen spectrum (Lyman/Balmer/Paschen) is a guaranteed direct-recall question.',
  prediction: const PredictionPrompt(
    scenario:
        'An electron in a hydrogen atom sits in the n=3 orbit. It can drop down to either n=1 or n=2. Compared to the n=3→n=2 transition, the n=3→n=1 transition photon will be:',
    options: [
      'Lower energy (longer wavelength)',
      'The same energy',
      'Higher energy (shorter wavelength)',
      'No photon is emitted for a bigger jump',
    ],
    correctIndex: 2,
    reveal:
        'Higher energy. In the lab, select n₂=3 and switch n₁ between 2 and 1 — the ΔE meter jumps sharply higher for the drop to n=1 (Lyman series, UV) than for the drop to n=2 (Balmer series, visible light). Bigger jumps in energy level release more energetic — shorter wavelength — photons.',
  ),
  experiments: [
    'Select n₂=2, n₁=1 and trigger the transition — the classic 10.2 eV Lyman-alpha photon, in the UV',
    'Select n₂=3, n₁=2 and trigger it — the Balmer-alpha photon, visible red light (656 nm)',
    'Keep n₁=1 fixed and raise n₂ from 2 to 5 — watch ΔE approach (but never exceed) 13.6 eV, the ionization limit',
    'Switch to absorption mode and watch the electron jump OUTWARD as a photon is absorbed',
    'Compare orbit radii visually — n=2 orbit is 4× the n=1 radius, n=3 is 9× — confirming r ∝ n²',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Rutherford\'s nuclear model (electrons orbiting a tiny dense nucleus) explained scattering experiments beautifully but had a fatal flaw: classical electromagnetism says an accelerating (orbiting) charge must continuously radiate energy, so the electron should spiral inward and crash into the nucleus in about 10⁻¹⁰ seconds. Bohr rescued the model in 1913 by adding quantum postulates on top of the classical picture.',
      title: 'The problem Bohr had to solve',
    ),
    ContentBlock.bullets([
      'Postulate 1 (quantised orbits): electrons move only in certain allowed circular orbits for which the angular momentum is quantised: L = nh/2π, n = 1, 2, 3, ... (n is the principal quantum number)',
      'Postulate 2 (stationary states): while in one of these allowed orbits, the electron does NOT radiate energy, even though it is accelerating — these are called stationary states',
      'Postulate 3 (quantum jumps): the atom emits or absorbs a photon ONLY when an electron jumps between two allowed orbits, and the photon energy exactly equals the energy difference: hν = E_final − E_initial (or |E₂ − E₁| for the magnitude)',
    ], title: 'Bohr\'s three postulates'),
    ContentBlock.formula('L = mvr = nh/2π,   n = 1, 2, 3, ...', title: 'QUANTISED ANGULAR MOMENTUM'),
    ContentBlock.paragraph(
      'Combining this quantisation condition with Coulomb\'s law providing the centripetal force (for hydrogen, one proton and one electron), Bohr derived that only certain orbit radii are allowed, and they grow as the SQUARE of the principal quantum number n.',
      title: 'Allowed orbit radii',
    ),
    ContentBlock.formula('rₙ = n² r₁,   r₁ = 0.529 Å (the Bohr radius)', title: 'ORBIT RADIUS'),
    ContentBlock.paragraph(
      'Each allowed orbit has a definite total energy (kinetic + potential), and because the electron is bound to the nucleus, this energy is negative — zero energy corresponds to a free (ionised) electron at rest infinitely far away. For hydrogen, the energy of the nth level works out to a strikingly simple formula.',
      title: 'Energy levels',
    ),
    ContentBlock.formula('Eₙ = −13.6/n² eV   (hydrogen)', title: 'ENERGY OF THE nTH LEVEL'),
    ContentBlock.bullets([
      'n=1 (ground state): E₁ = −13.6 eV — the most tightly bound, lowest-energy state',
      'n=2: E₂ = −3.4 eV',
      'n=3: E₃ = −1.51 eV',
      'n=∞: E = 0 eV — the electron is just barely free (ionised)',
    ]),
    ContentBlock.formula('ΔE = 13.6 (1/n₁² − 1/n₂²) eV   (n₂ > n₁, energy released on the n₂→n₁ drop)',
        title: 'TRANSITION ENERGY'),
    ContentBlock.paragraph(
      'Since the ground state energy is E₁ = −13.6 eV, exactly 13.6 eV must be supplied to remove the electron completely from a hydrogen atom in its ground state (raising it to n=∞, E=0). This is the IONIZATION ENERGY of hydrogen — one of the most frequently recalled numbers in all of NEET/JEE modern physics.',
      title: 'Ionization energy',
    ),
    ContentBlock.paragraph(
      'Transitions ending on different lower levels form named spectral series, historically discovered separately and named after their discoverers. Each series spans a characteristic region of the electromagnetic spectrum because of how large the corresponding energy gaps are.',
      title: 'Spectral series of hydrogen',
    ),
    ContentBlock.bullets([
      'Lyman series: transitions ending at n=1 — largest energy gaps → ultraviolet (UV)',
      'Balmer series: transitions ending at n=2 — moderate energy gaps → visible light (this is the series you can literally see as coloured lines)',
      'Paschen series: transitions ending at n=3 — smaller gaps → infrared (IR)',
      '(Brackett, n=4, and Pfund, n=5, series continue further into the infrared)',
    ], title: 'Memorise: Lyman=UV, Balmer=visible, Paschen=IR'),
    ContentBlock.realLife(
      'The distinct coloured lines seen in a hydrogen discharge tube (or in starlight passed through a prism) are direct photographic evidence of these discrete energy levels — each spectral line is a fingerprint of a specific n₂→n₁ transition. Astronomers identify elements in distant stars by matching these exact spectral lines.',
    ),
    ContentBlock.mistake(
      'Forgetting the negative sign in Eₙ = −13.6/n² eV. Higher n means a LESS negative (i.e., higher/less bound) energy, closer to zero. Students often compute magnitudes correctly but get confused about which level is "higher energy" — n=3 (E₃=−1.51 eV) has HIGHER energy than n=1 (E₁=−13.6 eV), even though both are negative.',
    ),
    ContentBlock.mistake(
      'Mixing up which transitions emit vs absorb. An electron falling from a higher n to a lower n (n₂→n₁, n₂>n₁) EMITS a photon (releases energy). An electron jumping from a lower n to a higher n only happens by ABSORBING a photon of exactly the right energy — it cannot happen spontaneously.',
    ),
    ContentBlock.example(
      'Find the wavelength of the photon emitted when a hydrogen electron falls from n=3 to n=2 (Balmer-alpha line).\n\nΔE = 13.6(1/2² − 1/3²) = 13.6(1/4 − 1/9) = 13.6 × (5/36) ≈ 1.89 eV.\n\nλ = 1240/ΔE(eV) = 1240/1.89 ≈ 656 nm — the famous red hydrogen-alpha line, visible (Balmer series).',
    ),
    ContentBlock.jeeTip(
      'For "maximum number of spectral lines" problems: if an electron is excited to level n, the total number of possible spectral lines as it (and all electrons in a large sample) cascades down to n=1 is N = n(n−1)/2. For n=4, that\'s 4×3/2 = 6 distinct lines.',
    ),
    ContentBlock.neetNote(
      'The Bohr model works ONLY for hydrogen and hydrogen-LIKE single-electron ions (He⁺, Li²⁺, etc. — one electron orbiting a nucleus of charge +Ze). For these, scale the formulas: rₙ = n²r₁/Z and Eₙ = −13.6Z²/n² eV. It completely fails for multi-electron atoms because it ignores electron-electron repulsion and does not follow from a more fundamental theory (that had to wait for full quantum mechanics).',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Coulomb attraction supplies the centripetal force',
      math: 'k e² / rₙ² = m v² / rₙ',
      note: 'For hydrogen: nuclear charge = +e, orbiting electron charge = −e.',
    ),
    DerivationStep(
      title: 'Apply the quantisation postulate',
      math: 'm vₙ rₙ = n h / 2π',
      note: 'Bohr\'s key new assumption — angular momentum comes only in integer multiples of h/2π.',
    ),
    DerivationStep(
      title: 'Solve the two equations together for radius',
      math: 'rₙ = n² h² ε₀ / (π m e²) = n² r₁,   r₁ = 0.529 Å',
      note: 'Radius grows as the square of the principal quantum number.',
    ),
    DerivationStep(
      title: 'Substitute back to get total energy (KE + PE)',
      math: 'Eₙ = −m e⁴ / (8 ε₀² h² n²) = −13.6/n² eV',
      note: 'The energy is negative because the electron is bound; it becomes less negative (higher) as n increases.',
    ),
    DerivationStep(
      title: 'Photon energy on a transition between two levels',
      math: 'hν = |Eₙ₂ − Eₙ₁| = 13.6(1/n₁² − 1/n₂²) eV',
      note: 'This single formula predicts every spectral line of hydrogen to high precision.',
    ),
  ],
  formulas: const [
    FormulaEntry('Quantised angular momentum', 'L = nh/2π'),
    FormulaEntry('Orbit radius', 'rₙ = n² r₁,  r₁ = 0.529 Å (Bohr radius)'),
    FormulaEntry('Energy of nth level (hydrogen)', 'Eₙ = −13.6/n² eV'),
    FormulaEntry('Transition energy', 'ΔE = 13.6(1/n₁² − 1/n₂²) eV', condition: 'n₂ > n₁'),
    FormulaEntry('Ionization energy of hydrogen (ground state)', '13.6 eV'),
    FormulaEntry('Hydrogen-like ion scaling', 'rₙ = n²r₁/Z,  Eₙ = −13.6Z²/n² eV'),
    FormulaEntry('Max spectral lines from level n cascading to ground', 'N = n(n−1)/2'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'According to Bohr\'s postulate, the angular momentum of an electron in an allowed orbit is:',
      options: ['Continuous, any value allowed', 'Quantised as L = nh/2π', 'Always zero', 'Equal to nh'],
      correctIndex: 1,
      solution: 'Bohr\'s quantisation postulate restricts angular momentum to integer multiples of h/2π: L = nh/2π.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The ionization energy of a hydrogen atom in its ground state is:',
      options: ['3.4 eV', '13.6 eV', '1.51 eV', '10.2 eV'],
      correctIndex: 1,
      solution: 'E₁ = −13.6 eV, so 13.6 eV must be supplied to bring the electron to E=0 (free) — the ionization energy.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A hydrogen electron transitions from n=4 to n=1. This transition belongs to which spectral series and region?',
      options: ['Balmer, visible', 'Lyman, ultraviolet', 'Paschen, infrared', 'Brackett, infrared'],
      correctIndex: 1,
      solution: 'Any transition ending at n=1 belongs to the Lyman series, which lies in the ultraviolet region.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The radius of the second Bohr orbit (n=2) of hydrogen is:',
      options: ['0.529 Å', '1.058 Å', '2.116 Å', '4.232 Å'],
      correctIndex: 2,
      solution: 'rₙ = n²r₁ = 4 × 0.529 Å = 2.116 Å.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The energy of a hydrogen electron in the n=2 state is:',
      options: ['−13.6 eV', '−3.4 eV', '−1.51 eV', '−6.8 eV'],
      correctIndex: 1,
      solution: 'Eₙ = −13.6/n² eV. For n=2: E₂ = −13.6/4 = −3.4 eV.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A hydrogen atom electron drops from n=3 to n=2, emitting a photon. What is the energy of this photon?',
      options: ['1.89 eV', '3.4 eV', '12.09 eV', '0.66 eV'],
      correctIndex: 0,
      solution: 'ΔE = 13.6(1/4 − 1/9) = 13.6 × 5/36 ≈ 1.89 eV — the Balmer-alpha (H-alpha) line.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'An electron in a hydrogen atom is excited to n=4. What is the maximum number of distinct spectral lines that can be emitted as it cascades down to the ground state?',
      options: ['4', '6', '8', '10'],
      correctIndex: 1,
      solution: 'Number of possible lines = n(n−1)/2 = 4×3/2 = 6.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'For a hydrogen-like ion with atomic number Z, the ground state energy is given by:',
      options: ['−13.6 eV', '−13.6 Z eV', '−13.6 Z² eV', '−13.6/Z eV'],
      correctIndex: 2,
      solution: 'For hydrogen-like ions, Eₙ = −13.6 Z²/n² eV. At ground state n=1: E₁ = −13.6 Z² eV.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.advanced,
      question: 'Which of the following is a correct limitation of the Bohr model?',
      options: [
        'It correctly predicts spectra of all multi-electron atoms',
        'It applies well only to hydrogen and other single-electron (hydrogen-like) species',
        'It requires no quantisation assumptions at all',
        'It predicts continuous (non-discrete) energy levels',
      ],
      correctIndex: 1,
      solution: 'The Bohr model ignores electron-electron interactions, so it works accurately only for hydrogen and hydrogen-like single-electron ions, failing for multi-electron atoms.',
    ),
  ],
  revision: [
    'Bohr\'s postulates: quantised angular momentum L=nh/2π; stationary (non-radiating) orbits; photon emitted/absorbed only on a transition, hν = ΔE.',
    'Orbit radius rₙ = n²r₁, with Bohr radius r₁ = 0.529 Å.',
    'Energy Eₙ = −13.6/n² eV for hydrogen; becomes less negative (higher) as n increases.',
    'Transition energy ΔE = 13.6(1/n₁² − 1/n₂²) eV; bigger jumps release more energetic photons.',
    'Lyman series → n=1 (UV), Balmer series → n=2 (visible), Paschen series → n=3 (IR).',
    'Ionization energy of hydrogen ground state = 13.6 eV.',
    'Bohr model works only for hydrogen-like single-electron systems — fails for multi-electron atoms.',
  ],
  sandboxBuilder: (_) => const BohrModelSandbox(),
);
