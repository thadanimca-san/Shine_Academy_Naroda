import '../../models/lesson.dart';
import '../../simulators/radioactivity_sandbox.dart';
import '../../theme/tokens.dart';

/// Radioactivity — the statistical decay law, half-life, and decay types.
final Lesson radioactivityLesson = Lesson(
  topicId: 'radioactivity',
  title: 'Radioactivity',
  accentColor: Palette.chModern,
  bigQuestion:
      'Nobody can tell you WHEN a single radioactive atom will decay — it could happen this second or a thousand years from now, and there is no way to know in advance. Yet scientists confidently date fossils to within a few hundred years using radioactivity. How can something be totally unpredictable for one atom, yet perfectly predictable for a trillion of them?',
  whyItMatters:
      'Radioactive decay is a cornerstone of both nuclear physics and NEET/JEE numericals — half-life, decay constant, and activity calculations are tested every single year. It also underlies real technologies you already know: carbon dating, medical imaging tracers, and nuclear power all depend on precisely this statistical decay behaviour.',
  prediction: const PredictionPrompt(
    scenario:
        'You start with N₀ radioactive nuclei. After exactly 3 half-lives have passed, what fraction of the original sample remains undecayed?',
    options: ['1/3', '1/6', '1/8', '1/9'],
    correctIndex: 2,
    reveal:
        'Each half-life halves what remains: after 1 half-life, 1/2 remains; after 2, 1/4; after 3, 1/8. In the lab, set the half-life slider and watch the remaining-N graph — at t=T it sits at N₀/2, at t=2T it\'s at N₀/4, and at t=3T it\'s at N₀/8, exactly matching (1/2)ⁿ for n half-lives.',
  ),
  experiments: [
    'Set a short half-life and watch individual dots decay at unpredictable moments while the population curve still follows a smooth exponential',
    'Read the remaining-N count at t=T, t=2T, and t=3T and confirm the 1/2, 1/4, 1/8 pattern',
    'Increase the half-life slider and watch the whole decay curve stretch out (decays more slowly)',
    'Reset the sample and run it again — the population curve looks the same, but which specific dots decay first is different every time',
    'Compare the "model" N(t) reading against the actual remaining count — they track closely for a reasonably large sample',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Some nuclei are unstable — they spontaneously transform into a different nucleus, releasing particles and/or energy in the process. This is RADIOACTIVE DECAY, discovered by Becquerel and studied extensively by the Curies and Rutherford. Crucially, decay is a RANDOM process: it is impossible to predict when any INDIVIDUAL nucleus will decay. There is no known way to trigger, delay, or predict an individual decay event — it does not depend on temperature, pressure, or chemical environment.',
      title: 'Decay is random for one nucleus...',
    ),
    ContentBlock.paragraph(
      'Even though each nucleus\'s decay moment is unpredictable, EVERY nucleus of a given type has the same fixed PROBABILITY per unit time of decaying — called the decay constant λ. For a large collection of identical nuclei, this fixed probability translates into a smooth, entirely predictable statistical law for how the population as a whole shrinks over time. This is exactly like flipping thousands of coins: you cannot predict any one flip, but you can confidently predict that close to half will land heads.',
      title: '...but statistically predictable for a large sample',
    ),
    ContentBlock.formula('N(t) = N₀ e^(−λt)', title: 'RADIOACTIVE DECAY LAW'),
    ContentBlock.paragraph(
      'The decay constant λ is the probability of decay per unit time for a single nucleus. A more intuitive way to describe decay speed is the HALF-LIFE T½ — the time after which exactly half of any starting sample has decayed. Half-life and decay constant are directly related.',
      title: 'Half-life',
    ),
    ContentBlock.formula('T½ = ln 2 / λ = 0.693 / λ', title: 'HALF-LIFE'),
    ContentBlock.paragraph(
      'After n half-lives have elapsed, the fraction of the original sample still remaining is always (1/2)ⁿ, regardless of how large or small the sample is or what the actual half-life duration is. This works for both whole and fractional numbers of half-lives.',
      title: 'Fraction remaining after n half-lives',
    ),
    ContentBlock.formula('N/N₀ = (1/2)ⁿ,   n = t/T½', title: 'FRACTION REMAINING'),
    ContentBlock.paragraph(
      'Radioactive nuclei decay by one of three characteristic processes, each changing the nucleus differently.',
      title: 'Three types of radioactive decay',
    ),
    ContentBlock.bullets([
      'Alpha (α) decay: nucleus emits a helium nucleus (2 protons + 2 neutrons). Z decreases by 2, A decreases by 4. ᴬZX → ᴬ⁻⁴Z₋₂Y + α',
      'Beta-minus (β⁻) decay: a neutron converts to a proton, emitting an electron (and an antineutrino). Z increases by 1, A stays the same. ᴬZX → ᴬZ₊₁Y + e⁻',
      'Beta-plus (β⁺) decay: a proton converts to a neutron, emitting a positron. Z decreases by 1, A stays the same. (Less commonly tested than β⁻.)',
      'Gamma (γ) decay: the nucleus, left in an excited energy state after α or β decay, emits a high-energy photon. Z and A are BOTH unchanged — only the nucleus\'s internal energy drops',
    ], title: 'Alpha, beta, gamma — what changes in Z and A'),
    ContentBlock.paragraph(
      'The ACTIVITY of a sample is the number of decays occurring per second — this, not N itself, is what a Geiger counter actually measures. Activity is proportional to however many undecayed nuclei remain, so it decays with exactly the same exponential law and half-life as N itself.',
      title: 'Activity',
    ),
    ContentBlock.formula('Activity  A = λN = λN₀e^(−λt) = A₀e^(−λt)', title: 'ACTIVITY'),
    ContentBlock.bullets([
      'SI unit: becquerel (Bq) = 1 decay per second',
      'Older/practical unit: curie (Ci) = 3.7×10¹⁰ decays per second (roughly the activity of 1 gram of radium-226)',
    ]),
    ContentBlock.realLife(
      'Carbon dating exploits this law: living organisms maintain a constant ratio of radioactive ¹⁴C to stable ¹²C while alive (through exchange with the atmosphere), but once they die, ¹⁴C decays with a known half-life (≈5730 years) without being replenished. Measuring how much ¹⁴C remains in an ancient bone or wood sample tells archaeologists how long ago the organism died.',
    ),
    ContentBlock.mistake(
      'Assuming half-life means "half the atoms decay, then decay stops." Decay never stops — after each half-life, half of whatever remains decays in the NEXT half-life too. The sample approaches (but mathematically never quite reaches) zero.',
    ),
    ContentBlock.mistake(
      'Averaging fractions incorrectly across non-whole half-lives. For n=1.5 half-lives, the fraction remaining is (1/2)^1.5 ≈ 0.354, NOT halfway between the n=1 (0.5) and n=2 (0.25) fractions arithmetically — decay is exponential, not linear.',
    ),
    ContentBlock.example(
      'A radioactive sample has a half-life of 20 minutes. Starting with 800 nuclei, how many remain after 1 hour?\n\n1 hour = 60 minutes = 3 half-lives (n=3).\n\nN = N₀(1/2)ⁿ = 800 × (1/2)³ = 800/8 = 100 nuclei remain.',
    ),
    ContentBlock.jeeTip(
      'For decay problems NOT landing on a whole number of half-lives, use N = N₀e^(−λt) directly with λ = 0.693/T½, or take logarithms: ln(N/N₀) = −λt. Many JEE problems intentionally use non-integer half-life multiples to force this approach instead of the shortcut fraction table.',
    ),
    ContentBlock.neetNote(
      'NEET commonly tests decay-scheme bookkeeping: after one α decay followed by two β⁻ decays, find the new (Z, A). Track each step: α changes (Z,A)→(Z−2, A−4); each β⁻ changes (Z,A)→(Z+1, A). Also remember gamma decay changes neither Z nor A — it only releases excess energy as a photon.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the fundamental hazard-rate assumption',
      math: 'dN/dt = −λN',
      note: 'The chance any nucleus decays in a small time dt is λ·dt, independent of the nucleus\'s history — decay has no "memory."',
    ),
    DerivationStep(
      title: 'Separate variables and integrate',
      math: '∫(dN/N) = −λ∫dt   ⟹   ln N = −λt + C',
    ),
    DerivationStep(
      title: 'Apply the initial condition N(0) = N₀',
      math: 'N(t) = N₀ e^(−λt)',
      note: 'This is the exponential decay law.',
    ),
    DerivationStep(
      title: 'Define half-life from N(T½) = N₀/2',
      math: 'N₀/2 = N₀e^(−λT½)   ⟹   ln 2 = λT½   ⟹   T½ = 0.693/λ',
    ),
    DerivationStep(
      title: 'Express activity from the same law',
      math: 'A(t) = λN(t) = λN₀e^(−λt) = A₀e^(−λt)',
      note: 'Activity, the measurable decay rate, follows the same exponential decline as N itself.',
    ),
  ],
  formulas: const [
    FormulaEntry('Decay law', 'N(t) = N₀e^(−λt)'),
    FormulaEntry('Half-life', 'T½ = ln2/λ = 0.693/λ'),
    FormulaEntry('Fraction remaining after n half-lives', 'N/N₀ = (1/2)ⁿ,  n = t/T½'),
    FormulaEntry('Activity', 'A = λN = A₀e^(−λt)'),
    FormulaEntry('Becquerel', '1 Bq = 1 decay/second'),
    FormulaEntry('Curie', '1 Ci = 3.7×10¹⁰ decays/second'),
    FormulaEntry('Alpha decay', 'ᴬZX → ᴬ⁻⁴Z₋₂Y + ⁴₂He'),
    FormulaEntry('Beta-minus decay', 'ᴬZX → ᴬZ₊₁Y + e⁻ (+ antineutrino)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Radioactive decay of an individual nucleus is:',
      options: [
        'Perfectly predictable in timing',
        'Random and unpredictable for any single nucleus',
        'Triggered by external heating',
        'Dependent on chemical bonding',
      ],
      correctIndex: 1,
      solution: 'Individual nuclear decay is a random, spontaneous quantum process — unpredictable in timing and unaffected by chemical or physical environment.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The relationship between half-life T½ and decay constant λ is:',
      options: ['T½ = λ/0.693', 'T½ = 0.693/λ', 'T½ = 0.693λ', 'T½ = 1/λ²'],
      correctIndex: 1,
      solution: 'T½ = ln2/λ = 0.693/λ, derived directly from setting N=N₀/2 in the decay law.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A sample has 1600 nuclei and a half-life of 10 days. How many nuclei remain after 40 days?',
      options: ['800', '400', '100', '200'],
      correctIndex: 2,
      solution: '40 days = 4 half-lives. N = 1600 × (1/2)⁴ = 1600/16 = 100.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In alpha decay, the mass number A and atomic number Z of the daughter nucleus change as:',
      options: [
        'A decreases by 4, Z decreases by 2',
        'A decreases by 2, Z decreases by 4',
        'A unchanged, Z decreases by 2',
        'A decreases by 4, Z unchanged',
      ],
      correctIndex: 0,
      solution: 'An alpha particle is a helium nucleus (2 protons + 2 neutrons), so emitting one reduces A by 4 and Z by 2.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In beta-minus (β⁻) decay, what happens to the atomic number Z and mass number A?',
      options: [
        'Z increases by 1, A unchanged',
        'Z decreases by 1, A unchanged',
        'Z unchanged, A increases by 1',
        'Both Z and A decrease by 1',
      ],
      correctIndex: 0,
      solution: 'In β⁻ decay a neutron converts to a proton (emitting an electron), so Z increases by 1 while total nucleon count A stays the same.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A radioactive sample has activity 800 Bq. If its half-life is 5 minutes, what will its activity be after 15 minutes?',
      options: ['400 Bq', '200 Bq', '100 Bq', '50 Bq'],
      correctIndex: 2,
      solution: '15 minutes = 3 half-lives. Activity follows the same law as N: A = 800 × (1/2)³ = 800/8 = 100 Bq.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A radioactive nucleus decays by emitting one alpha particle followed by two beta-minus particles. If the original nucleus is ²³⁸₉₂U, what is the resulting (A, Z)?',
      options: ['(234, 90)', '(234, 92)', '(230, 88)', '(234, 88)'],
      correctIndex: 1,
      solution: 'Alpha: A=238−4=234, Z=92−2=90. Then two β⁻: Z increases by 1 each time (A unchanged): 90+1+1=92. Final: A=234, Z=92.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'A fossil sample shows that only 25% of its original ¹⁴C remains. If the half-life of ¹⁴C is 5730 years, the approximate age of the fossil is:',
      options: ['2865 years', '5730 years', '11460 years', '17190 years'],
      correctIndex: 2,
      solution: '25% remaining = (1/2)² = 1/4, so n=2 half-lives have elapsed. Age = 2 × 5730 = 11460 years.',
    ),
  ],
  revision: [
    'Individual nuclear decay is random and unpredictable; a large population follows the exact statistical law N=N₀e^(−λt).',
    'Half-life T½ = 0.693/λ; after n half-lives, fraction remaining = (1/2)ⁿ.',
    'Alpha decay: A−4, Z−2 (emits a He nucleus). Beta-minus: A unchanged, Z+1 (neutron→proton+electron). Gamma: A and Z both unchanged (photon emission only).',
    'Activity A = λN, measured in becquerel (1 decay/s) or curie (3.7×10¹⁰ decays/s); it decays with the same half-life as N.',
    'Decay constant λ is fixed for a given nuclide, independent of temperature, pressure, or chemical state.',
    'Carbon dating uses the known ¹⁴C half-life (5730 years) to estimate the age of organic remains.',
  ],
  sandboxBuilder: (_) => const RadioactivitySandbox(),
);
