import '../../models/lesson.dart';
import '../../simulators/nuclear_physics_sandbox.dart';
import '../../theme/tokens.dart';

/// Nuclear Physics — mass defect, binding energy, and why both splitting
/// heavy nuclei and fusing light nuclei release energy.
final Lesson nuclearPhysicsLesson = Lesson(
  topicId: 'nuclear-physics',
  title: 'Nuclear Physics: Binding Energy',
  accentColor: Palette.chModern,
  bigQuestion:
      'Weigh the protons and neutrons that make up a helium nucleus separately, then weigh the assembled nucleus — the assembled nucleus weighs LESS than its parts. Where did the missing mass go, and how can splitting a uranium nucleus AND fusing two hydrogen nuclei both release enormous energy, if they are opposite processes?',
  whyItMatters:
      'Binding energy explains where nuclear energy — from reactors to the Sun to weapons — actually comes from, and it is one of the most numerically-tested topics in NEET/JEE: mass defect calculations, the u-to-MeV conversion, and reading the binding-energy curve appear constantly. It also sets up radioactivity, fission, and fusion, which build directly on this one idea.',
  prediction: const PredictionPrompt(
    scenario:
        'You have two ways to release nuclear energy: SPLIT a heavy nucleus like uranium-235 (fission), or FUSE two light nuclei like hydrogen isotopes (fusion). Which of these processes can release energy?',
    options: [
      'Only fission releases energy; fusion always absorbs energy',
      'Only fusion releases energy; fission always absorbs energy',
      'Both can release energy, because both move the nucleons toward the binding-energy peak near iron (A≈56)',
      'Neither releases energy — nuclear reactions always conserve mass exactly',
    ],
    correctIndex: 2,
    reveal:
        'Both release energy. In the lab, drag A up past 140 (heavy end) and note the BE/nucleon marker sits below the peak — splitting such a nucleus into two medium nuclei moves both fragments UP toward the peak, releasing energy. Now drag A down below 20 (light end) — fusing two such light nuclei into one medium nucleus ALSO moves the product up toward the peak. Both processes are really the same story: nucleons rearranging into a MORE tightly bound (higher BE/nucleon) configuration, converting mass into energy via E=Δmc².',
  ),
  experiments: [
    'Set A=4, Z=2 (helium) and read the mass defect and total binding energy',
    'Drag A up toward 235 (heavy nucleus) and watch BE/nucleon marker sit below the peak, on the left-of-peak-but-far-side',
    'Drag A down toward 4-20 (light nucleus) and see the marker sit below the peak on the other side',
    'Set A≈56 (iron region) and confirm the marker sits AT the peak — the most stable, tightly-bound nuclei in nature',
    'Compare total binding energy (grows with A) against binding energy PER NUCLEON (peaks near A=56) — these tell different stories',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The nucleus is made of NUCLEONS: protons (charge +e) and neutrons (no charge), bound together by the strong nuclear force. A nucleus is written as ᴬZX, where Z is the ATOMIC NUMBER (number of protons, which fixes the element) and A is the MASS NUMBER (total nucleons, protons + neutrons). The number of neutrons is N = A − Z.',
      title: 'Nuclear composition',
    ),
    ContentBlock.bullets([
      'Isotopes: same Z, different A (same element, different neutron count) — e.g. ¹H, ²H (deuterium), ³H (tritium)',
      'Isobars: same A, different Z (different elements, same total nucleon count) — e.g. ¹⁴C and ¹⁴N',
      'Isotones: same N (neutron count), different Z and A — e.g. ¹⁴C and ¹⁶O both have 8 neutrons',
    ], title: 'Isotopes, isobars, isotones'),
    ContentBlock.paragraph(
      'Here is the surprising experimental fact: if you carefully weigh a nucleus, it is always LIGHTER than the sum of the masses of its separate, free protons and neutrons. This missing mass is called the MASS DEFECT, Δm. By Einstein\'s mass-energy equivalence, this missing mass was converted into energy that was released when the nucleons bound together — this is the nucleus\'s BINDING ENERGY, the energy you would need to supply to pull the nucleus apart again into free nucleons.',
      title: 'Mass defect — where the missing mass goes',
    ),
    ContentBlock.formula('Δm = [Z·mₚ + (A−Z)·mₙ] − M_nucleus', title: 'MASS DEFECT'),
    ContentBlock.formula('BE = Δm·c²', title: 'BINDING ENERGY (EINSTEIN\'S MASS-ENERGY EQUIVALENCE)'),
    ContentBlock.paragraph(
      'In nuclear physics, masses are almost always given in ATOMIC MASS UNITS (u), where 1 u = 1/12 the mass of a carbon-12 atom. Converting mass defect directly into energy using c² in SI units is clumsy, so a single conversion factor is memorised and used constantly.',
      title: 'The essential conversion: u to MeV',
    ),
    ContentBlock.formula('1 u = 931.5 MeV/c²   (so BE(MeV) = Δm(u) × 931.5)',
        title: 'MASS-ENERGY CONVERSION (MEMORISE THIS)'),
    ContentBlock.paragraph(
      'Total binding energy grows with the number of nucleons, so it is not a fair way to compare stability across different nuclei. Instead, physicists use BINDING ENERGY PER NUCLEON (BE/A) — the average energy holding each nucleon in place. Plotted against mass number A, this quantity rises steeply for light nuclei, peaks around A≈56 (iron and nearby nuclei, the most tightly-bound, most stable nuclei in existence), then decreases slowly for heavier nuclei.',
      title: 'Binding energy PER NUCLEON — the real measure of stability',
    ),
    ContentBlock.bullets([
      'Rises steeply for light nuclei (He, Li, ... ) — each added nucleon strengthens binding a lot',
      'Peaks near A≈56 (iron, nickel region) at about 8.7-8.8 MeV/nucleon — the most stable nuclei',
      'Falls slowly for heavy nuclei (toward uranium, A≈235) — the extra protons\' mutual Coulomb repulsion starts to outweigh the short-range nuclear attraction',
    ]),
    ContentBlock.paragraph(
      'Because the curve peaks at A≈56, ANY process that moves nucleons toward that peak releases energy — regardless of which direction you approach it from. Splitting a heavy nucleus (FISSION) into two medium nuclei moves both fragments up the curve to higher BE/nucleon. Combining two light nuclei (FUSION) into one medium nucleus also moves the product up the curve. Both convert a little mass into a lot of energy via E=Δmc².',
      title: 'Why fission AND fusion both release energy',
    ),
    ContentBlock.bullets([
      'Fission: heavy nucleus (e.g. U-235, low BE/nucleon ≈7.6 MeV) splits into two medium nuclei (higher BE/nucleon ≈8.5 MeV) — energy released per fission ≈ 200 MeV',
      'Fusion: light nuclei (e.g. two H isotopes, low BE/nucleon) combine into helium (much higher BE/nucleon ≈7.1 MeV) — energy released per fusion ≈ tens of MeV, but per unit mass fusion releases even MORE energy than fission',
    ], title: 'Fission vs fusion energetics'),
    ContentBlock.paragraph(
      'The force holding nucleons together — the STRONG NUCLEAR FORCE — has a few defining properties that explain the shape of the binding curve and much of nuclear behaviour.',
      title: 'Properties of the nuclear force',
    ),
    ContentBlock.bullets([
      'Short-range: acts only over nuclear distances (~1-3 fm), essentially zero beyond that — unlike gravity or Coulomb force which fall off gradually',
      'Very strong: about 100× stronger than the electromagnetic force at nuclear distances — otherwise Coulomb repulsion between protons would blow the nucleus apart',
      'Charge-independent: acts the same way between proton-proton, neutron-neutron, and proton-neutron pairs',
      'Saturating: each nucleon binds only with its immediate neighbours, not with every other nucleon — this is WHY total binding energy grows roughly proportional to A rather than A², and why BE/nucleon levels off instead of rising forever',
    ]),
    ContentBlock.realLife(
      'Nuclear power reactors run on controlled FISSION of uranium-235 (or plutonium), releasing heat that boils water to spin turbines. The Sun and all stars are powered by FUSION, converting hydrogen into helium in their cores at extreme temperature and pressure — this is the same reaction humans are still struggling to harness commercially on Earth (fusion power).',
    ),
    ContentBlock.mistake(
      'Confusing total binding energy with binding energy per nucleon. A uranium nucleus has a much LARGER total binding energy than a helium nucleus simply because it has far more nucleons — but its binding energy PER NUCLEON is actually smaller (less stable per nucleon) than helium\'s. Stability comparisons must always use BE/nucleon, never the total.',
    ),
    ContentBlock.mistake(
      'Forgetting to use ATOMIC masses consistently. Standard tables give atomic masses (nucleus + electrons), not bare nuclear masses. As long as you consistently use Z hydrogen ATOM masses (not bare proton masses) on one side and the atomic mass of the nucleus on the other, the electron masses cancel out correctly and you get the right mass defect.',
    ),
    ContentBlock.example(
      'Find the binding energy per nucleon of helium-4 (mass = 4.002603 u), given mₚ(H atom) = 1.007825 u, mₙ = 1.008665 u, and 1u = 931.5 MeV.\n\nΔm = [2(1.007825) + 2(1.008665)] − 4.002603\n= [2.01565 + 2.01733] − 4.002603\n= 4.032980 − 4.002603 = 0.030377 u.\n\nBE = 0.030377 × 931.5 ≈ 28.3 MeV (total binding energy).\n\nBE per nucleon = 28.3/4 ≈ 7.07 MeV/nucleon.',
    ),
    ContentBlock.jeeTip(
      'When comparing "which nucleus is more stable," always compare BE/nucleon values directly from the given data or the curve — do NOT try to compare total binding energies of nuclei with different A. A common trap answer relies on students comparing raw totals.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the numeric conversion 1u = 931.5 MeV directly, along with the shape of the BE/nucleon curve (peak at Fe, A≈56) and the qualitative fission-vs-fusion energy release explanation. Also remember: the nuclear force is charge-independent and short-range — a frequently asked direct-recall fact.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Add up the masses of separate, free nucleons',
      math: 'M_free = Z·mₚ + (A−Z)·mₙ',
      note: 'This is the mass BEFORE the nucleons come together to form a nucleus.',
    ),
    DerivationStep(
      title: 'Compare to the actual measured mass of the assembled nucleus',
      math: 'Δm = M_free − M_nucleus',
      note: 'Experimentally, M_nucleus is always found to be smaller: Δm > 0.',
    ),
    DerivationStep(
      title: 'Convert the missing mass into energy',
      math: 'BE = Δm·c²',
      note: 'This is the energy that was released when the nucleus formed (equivalently, the energy needed to break it apart again).',
    ),
    DerivationStep(
      title: 'Use the practical unit conversion',
      math: 'BE (MeV) = Δm (u) × 931.5',
      note: '1u = 931.5 MeV/c² avoids working directly in kilograms and joules.',
    ),
    DerivationStep(
      title: 'Normalise by nucleon count for a fair stability comparison',
      math: 'BE per nucleon = BE / A',
      note: 'This is the quantity that peaks near A≈56 and determines whether fission or fusion of a given nucleus releases energy.',
    ),
  ],
  formulas: const [
    FormulaEntry('Mass defect', 'Δm = [Z·mₚ + (A−Z)·mₙ] − M_nucleus'),
    FormulaEntry('Binding energy', 'BE = Δm·c²'),
    FormulaEntry('Mass-energy conversion', '1 u = 931.5 MeV/c²'),
    FormulaEntry('Binding energy per nucleon', 'BE/A', condition: 'peaks near A ≈ 56 (iron)'),
    FormulaEntry('Neutron number', 'N = A − Z'),
    FormulaEntry('Typical energy released per fission (U-235)', '≈ 200 MeV'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The mass defect of a nucleus represents:',
      options: [
        'An error in measurement',
        'The mass converted to binding energy when nucleons combine',
        'The mass of the electrons in the atom',
        'The mass lost during radioactive decay only',
      ],
      correctIndex: 1,
      solution: 'Mass defect Δm is the difference between the sum of masses of free nucleons and the actual nucleus mass — this "missing" mass was converted to binding energy, BE = Δm·c².',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The conversion factor between atomic mass units and energy is:',
      options: ['1 u = 931.5 eV', '1 u = 931.5 MeV', '1 u = 9.315 MeV', '1 u = 1.6×10⁻¹⁹ MeV'],
      correctIndex: 1,
      solution: '1 u = 931.5 MeV/c², a standard conversion used throughout nuclear physics numericals.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'The binding energy per nucleon curve, plotted against mass number A, has its maximum near:',
      options: ['A ≈ 4 (helium)', 'A ≈ 56 (iron)', 'A ≈ 120 (tin)', 'A ≈ 235 (uranium)'],
      correctIndex: 1,
      solution: 'The BE/nucleon curve peaks near A ≈ 56, around iron and nickel — the most tightly bound, most stable nuclei.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Both nuclear fission (of heavy nuclei) and nuclear fusion (of light nuclei) release energy because:',
      options: [
        'Both processes increase the total number of nucleons',
        'Both move the resulting nuclei toward the peak of the binding-energy-per-nucleon curve',
        'Fission and fusion are actually identical processes',
        'Mass is created in both processes',
      ],
      correctIndex: 1,
      solution: 'Whether nucleons are approaching the peak (A≈56) from the heavy side (fission) or the light side (fusion), the products end up MORE tightly bound, releasing the difference in binding energy as usable energy.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A nucleus has mass defect Δm = 0.5 u. Its total binding energy is approximately:',
      options: ['465.75 MeV', '9.315 MeV', '931.5 MeV', '46.575 MeV'],
      correctIndex: 0,
      solution: 'BE = Δm × 931.5 = 0.5 × 931.5 = 465.75 MeV.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'Given mₚ = 1.007825 u (H atom), mₙ = 1.008665 u, and M(He-4) = 4.002603 u, the mass defect of helium-4 is closest to:',
      options: ['0.0304 u', '0.304 u', '0.00304 u', '3.04 u'],
      correctIndex: 0,
      solution: 'Δm = [2(1.007825)+2(1.008665)] − 4.002603 = 4.032980 − 4.002603 = 0.030377 u ≈ 0.0304 u.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Which property of the nuclear force explains why binding energy per nucleon does NOT keep increasing indefinitely with A, but instead saturates and falls for heavy nuclei?',
      options: [
        'The nuclear force is long-range like gravity',
        'The nuclear force saturates — each nucleon binds only with nearby neighbours, not all others',
        'The nuclear force becomes repulsive for A > 1',
        'Neutrons stop existing above A = 56',
      ],
      correctIndex: 1,
      solution: 'The short-range, saturating nature of the nuclear force means each nucleon interacts strongly with only its immediate neighbours; for heavy nuclei, growing Coulomb repulsion between the increasing number of protons is no longer fully compensated, lowering BE/nucleon.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'If the binding energy per nucleon of uranium-235 is about 7.6 MeV and that of its two fission fragments averages about 8.5 MeV, the approximate energy released per fission event (A=235) is closest to:',
      options: ['20 MeV', '200 MeV', '2 MeV', '2000 MeV'],
      correctIndex: 1,
      solution: 'Energy released ≈ A × (BE/nucleon after − BE/nucleon before) = 235 × (8.5 − 7.6) MeV ≈ 235 × 0.9 ≈ 211 MeV — consistent with the well-known ≈200 MeV per U-235 fission.',
    ),
  ],
  revision: [
    'Nucleus = Z protons + (A−Z) neutrons; isotopes share Z, isobars share A, isotones share N.',
    'Mass defect Δm = [Zmₚ + (A−Z)mₙ] − M_nucleus is always positive — mass converted to binding energy.',
    'BE = Δm·c²; practical conversion: 1u = 931.5 MeV.',
    'Binding energy PER NUCLEON (not total BE) measures stability; the curve peaks near A≈56 (iron).',
    'Fission (heavy→medium) and fusion (light→medium) BOTH release energy by moving nuclei toward that peak.',
    'Nuclear force: short-range, very strong, charge-independent, and saturating.',
    'Real-world: nuclear reactors use controlled fission; the Sun and stars are powered by fusion.',
  ],
  sandboxBuilder: (_) => const NuclearPhysicsSandbox(),
);
