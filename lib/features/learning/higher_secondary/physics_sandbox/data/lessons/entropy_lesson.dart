import '../../models/lesson.dart';
import '../../simulators/entropy_sandbox.dart';
import '../../theme/tokens.dart';

/// Entropy & the Second Law — why time has a direction, and why some things never un-happen.
final Lesson entropyLesson = Lesson(
  topicId: 'entropy',
  title: 'Entropy & the Second Law',
  accentColor: Palette.chThermal,
  bigQuestion:
      'Drop an ice cube into hot tea and it melts, the tea cools a little, and everything settles to a lukewarm equilibrium — completely ordinary. But you have NEVER once seen the reverse happen: lukewarm tea spontaneously separating itself back into a floating ice cube and hotter tea. Every law of mechanics you\'ve learned works perfectly well run backward in time — so why does this one thing never run backward?',
  whyItMatters:
      'The second law of thermodynamics — and the concept of entropy that quantifies it — is the deepest, most conceptually rich idea in the entire thermodynamics syllabus. It sets the ultimate limit on every engine (already seen in the Carnot efficiency result), explains why perpetual motion machines are fundamentally impossible (not just badly engineered), and answers a question physics rarely touches elsewhere: why does time seem to flow in only one direction?',
  prediction: const PredictionPrompt(
    scenario:
        'A rigid, insulated box is divided by a thin partition: gas fills the left half, the right half is a perfect vacuum. The partition is suddenly removed. What happens next?',
    options: [
      'Nothing — gas stays in the left half since there\'s no force pushing it right',
      'The gas spontaneously expands to fill the whole box, and never spontaneously returns to the left half alone',
      'The gas expands to fill the box, then spontaneously returns to the left half after some time',
      'Half the gas moves right, then oscillates back and forth forever, evenly split',
    ],
    correctIndex: 1,
    reveal:
        'This is FREE EXPANSION — an irreversible process. Random molecular motion carries gas into the empty half almost immediately, and while in principle every molecule COULD by pure chance wander back into the left half at the same instant, the odds against that are so astronomically small (think 1 in 2^(10^23)) that it is treated as physically impossible. In the lab, hit "Remove partition" and watch the gas spread out and the entropy graph climb and plateau — then hit "Watch it reverse?" and see that it simply never happens.',
  ),
  experiments: [
    'Hit "Remove partition" and watch the gas rush to fill the whole box while the entropy graph climbs',
    'Watch the entropy graph plateau once the gas is fully mixed — entropy stops rising once equilibrium is reached',
    'Hit "Watch it reverse?" and observe that the gas never spontaneously re-crowds into one half, however long you watch',
    'Reset and repeat — note the entropy graph always climbs the same way, never spontaneously falling',
    'Think about a hot cup of tea next to a cold room: heat only ever flows tea→room, never room→tea on its own, exactly mirroring the free-expansion behaviour here',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The FIRST law of thermodynamics (energy conservation) permits an enormous range of processes that we simply never observe — for example, heat flowing spontaneously from a cold object to a hot one would not violate energy conservation at all, yet it never happens. The SECOND law is what rules out such processes. It can be stated in several completely equivalent ways: (1) heat flows spontaneously only from a hotter body to a colder one, never the reverse, without external work; (2) no cyclic engine can convert heat completely into work (Kelvin-Planck statement); (3) the entropy of an isolated system never decreases over time.',
      title: 'The second law: several equivalent statements',
    ),
    ContentBlock.bullets([
      'Clausius statement: heat cannot flow spontaneously from a colder body to a hotter body',
      'Kelvin-Planck statement: no engine operating in a cycle can convert ALL absorbed heat into work (some must be rejected)',
      'Entropy statement: the total entropy of an isolated system can only increase or, in an idealized reversible process, stay the same — it never decreases',
    ]),
    ContentBlock.formula('ΔS_isolated system ≥ 0', title: 'ENTROPY STATEMENT OF THE SECOND LAW'),
    ContentBlock.paragraph(
      'ENTROPY (S) is a thermodynamic quantity that measures the degree of disorder, randomness, or — more precisely — the number of ways a system\'s microscopic state can be arranged while looking the same macroscopically. A gas confined to half a box has fewer possible molecular arrangements (lower entropy) than the same gas spread through the whole box (vastly more possible arrangements, higher entropy). Processes tend to move toward the macroscopic state reachable by the largest number of microscopic arrangements — simply because that state is overwhelmingly the most probable one.',
      title: 'What entropy actually measures',
    ),
    ContentBlock.formula('ΔS = Q/T   (for a reversible process at constant temperature T)',
        title: 'ENTROPY CHANGE (BASIC FORMULA)'),
    ContentBlock.paragraph(
      'At the exam level, entropy change for a reversible process exchanging heat Q at a fixed absolute temperature T is simply ΔS = Q/T. If heat is absorbed (Q positive), entropy increases; if heat is rejected (Q negative), entropy of that particular system decreases — but the SURROUNDINGS that received the heat gain at least as much entropy, so the total (system + surroundings) never decreases, consistent with the second law.',
      title: 'Computing entropy change (exam level)',
    ),
    ContentBlock.paragraph(
      'Entropy can also be thought of as a measure of energy that has become "unavailable" to do useful work. Even though total energy is always conserved (first law), as entropy rises, a larger fraction of that energy becomes spread out, disordered, and thermodynamically unable to be harnessed for useful work — this is exactly why no engine can be 100% efficient (recall η_Carnot = 1 − Tc/Th from the Heat Engines lesson: some heat MUST be rejected to the cold reservoir, carrying away entropy, or the second law would be violated).',
      title: 'Entropy as "unavailable" energy',
    ),
    ContentBlock.realLife(
      'The one-way flow of entropy is often called the "arrow of time" — it is one of the very few places in fundamental physics where the future is distinguishable from the past. Shuffle a sorted deck of cards and it becomes disordered; you never see a shuffled deck spontaneously sort itself. Perfume spreads through a room and never spontaneously re-collects into the bottle. Every one of these is entropy increasing, and it is why we can look at a video and tell, just from the direction disorder is changing, whether it is playing forward or in reverse.',
    ),
    ContentBlock.mistake(
      'Believing entropy can NEVER decrease anywhere, ever. The correct statement is about an ISOLATED system (or the universe as a whole): entropy of a sub-part CAN decrease (e.g. a refrigerator lowers the entropy of the food inside), but only at the cost of increasing the entropy of its surroundings by an equal or greater amount — the total never decreases.',
    ),
    ContentBlock.mistake(
      'Assuming a "perpetual motion machine of the second kind" (one that extracts heat from a single reservoir and converts it completely into work, with no cold reservoir at all) is merely impractical. It is not a matter of poor engineering — it is FORBIDDEN outright by the second law (Kelvin-Planck statement), no matter how perfect the machine\'s design.',
    ),
    ContentBlock.example(
      '2000 J of heat flows out of a hot reservoir at 500 K into a cold reservoir at 250 K. Find the total change in entropy of the two reservoirs combined.\n\nHot reservoir loses heat: ΔS_hot = −Q/T_hot = −2000/500 = −4 J/K.\nCold reservoir gains the same heat: ΔS_cold = +Q/T_cold = +2000/250 = +8 J/K.\nTotal ΔS = −4 + 8 = +4 J/K.\n\nTotal entropy INCREASES, consistent with the second law — even though the hot reservoir\'s own entropy fell, the cold reservoir\'s entropy rose by more, since it received the same heat at a lower temperature.',
    ),
    ContentBlock.jeeTip(
      'The example above generalizes into a fast heuristic: whenever heat flows from a hotter to a colder body, total entropy ALWAYS increases, because the same Q divided by a smaller T (cold reservoir gaining) outweighs Q divided by a larger T (hot reservoir losing). This is exactly why heat never flows spontaneously the other way — that would require total entropy to decrease, which the second law forbids.',
    ),
    ContentBlock.neetNote(
      'NEET often frames the second law as: "It is impossible to construct a heat engine working in a cycle that converts all the heat absorbed into work" (Kelvin-Planck) or asks directly which processes are irreversible. Free expansion of a gas into vacuum, and heat flow across a finite temperature difference, are the two classic irreversible processes to remember for exam recall.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define entropy change for a reversible, isothermal heat exchange',
      math: 'dS = dQ_rev / T',
      note: 'This is the operational definition of entropy at the level needed for JEE/NEET — a state-function generalization of "heat added per unit temperature."',
    ),
    DerivationStep(
      title: 'Apply to heat flowing from a hot to a cold reservoir',
      math: 'ΔS_hot = −Q/T_hot   (heat leaves)\nΔS_cold = +Q/T_cold   (same heat Q arrives)',
    ),
    DerivationStep(
      title: 'Add the two changes to get the total entropy change',
      math: 'ΔS_total = Q(1/T_cold − 1/T_hot)',
      note: 'Since T_hot > T_cold, the term (1/T_cold − 1/T_hot) is always positive.',
    ),
    DerivationStep(
      title: 'Conclude that spontaneous heat flow always increases total entropy',
      math: 'ΔS_total > 0   whenever T_hot > T_cold',
      note: 'This is exactly why heat only ever flows hot→cold spontaneously — the reverse direction would require ΔS_total < 0, forbidden by the second law.',
    ),
  ],
  formulas: const [
    FormulaEntry('Entropy change (reversible, constant T)', 'ΔS = Q/T'),
    FormulaEntry('Second law (isolated system)', 'ΔS_isolated ≥ 0'),
    FormulaEntry('Entropy change, heat hot→cold', 'ΔS_total = Q(1/Tc − 1/Th) > 0', condition: 'Th > Tc'),
    FormulaEntry('Carnot efficiency (cross-reference)', 'η_Carnot = 1 − Tc/Th', condition: 'see Heat Engines lesson'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The second law of thermodynamics states that heat flows spontaneously:',
      options: ['From cold to hot always', 'From hot to cold, never the reverse without external work', 'In either direction equally', 'Only in a vacuum'],
      correctIndex: 1,
      solution: 'The Clausius statement of the second law: heat never flows spontaneously from a colder to a hotter body.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Entropy of an isolated system, over time:',
      options: ['Always decreases', 'Always stays exactly constant', 'Never decreases (increases or stays same)', 'Oscillates randomly'],
      correctIndex: 2,
      solution: 'ΔS_isolated ≥ 0 — entropy of an isolated system never decreases; it increases for irreversible processes and stays constant only in the idealized reversible limit.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A "perpetual motion machine of the second kind" is impossible because it would:',
      options: [
        'Violate energy conservation (first law)',
        'Convert heat completely into work from a single reservoir, violating the second law',
        'Require an infinite amount of fuel',
        'Only work at absolute zero',
      ],
      correctIndex: 1,
      solution: 'Such a machine would extract heat from one reservoir and convert it entirely to work with no waste heat — forbidden by the Kelvin-Planck statement of the second law, even though it wouldn\'t violate energy conservation.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: '600 J of heat flows from a reservoir at 400 K to one at 200 K. The total change in entropy of the two reservoirs is:',
      options: ['0 J/K', '1.5 J/K', '−1.5 J/K', '3.0 J/K'],
      correctIndex: 1,
      solution: 'ΔS = −Q/T_hot + Q/T_cold = −600/400 + 600/200 = −1.5 + 3.0 = 1.5 J/K.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A gas undergoes FREE EXPANSION into a vacuum (no heat exchange, no work done, ΔU=0 for ideal gas). This process is:',
      options: ['Reversible, with ΔS=0', 'Irreversible, with ΔS>0', 'Irreversible, with ΔS<0', 'Reversible, with ΔS>0'],
      correctIndex: 1,
      solution: 'Free expansion is a classic irreversible process — the gas never spontaneously returns to its original confined volume, so entropy strictly increases, even though ΔU=0 and no external heat or work crossed the boundary.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Ice melts in a glass of water at 0°C, absorbing 1200 J of latent heat from the surrounding water at the same temperature (273 K). The entropy change of the ice (as it melts) is approximately:',
      options: ['4.4 J/K', '0 J/K', '−4.4 J/K', '1200 J/K'],
      correctIndex: 0,
      solution: 'ΔS = Q/T = 1200/273 ≈ 4.4 J/K. The melting ice absorbs heat reversibly at constant T, so entropy increases by Q/T.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A Carnot engine operates between 600 K and 300 K. Compared to a real (irreversible) engine operating between the same two reservoirs, the Carnot engine\'s efficiency is:',
      options: [
        'Lower than the real engine\'s',
        'Equal to the real engine\'s, always',
        'Higher than or equal to the real engine\'s — the theoretical maximum',
        'Unrelated to the real engine\'s efficiency',
      ],
      correctIndex: 2,
      solution: 'The Carnot efficiency η=1−Tc/Th is the theoretical ceiling set by the second law; any real (irreversible) engine between the same reservoirs is always less efficient, per the Heat Engines lesson.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Which of these processes is REVERSIBLE (in the idealized thermodynamic sense)?',
      options: [
        'Free expansion of a gas into vacuum',
        'Heat flowing across a finite temperature difference',
        'A quasi-static isothermal expansion against an infinitesimally smaller external pressure',
        'Friction converting kinetic energy to heat',
      ],
      correctIndex: 2,
      solution: 'A reversible process proceeds through a continuous sequence of equilibrium states with no finite unbalanced forces — a quasi-static process against a pressure differing infinitesimally from the gas pressure approximates this ideal. The other three are classic irreversible processes.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'The "arrow of time" in physics is most closely associated with:',
      options: ['Newton\'s laws of motion', 'The increase of entropy in isolated systems', 'Conservation of momentum', 'The constancy of the speed of light'],
      correctIndex: 1,
      solution: 'Entropy increase (the second law) is one of the few physical laws that distinguishes past from future — most mechanical laws are time-symmetric, but entropy consistently increases going forward in time.',
    ),
  ],
  revision: [
    'Second law (equivalent statements): heat flows hot→cold spontaneously; no engine converts all heat to work (Kelvin-Planck); entropy of an isolated system never decreases.',
    'Entropy S measures disorder / the number of equivalent microscopic arrangements; systems evolve toward the most probable (highest-entropy) macrostate.',
    'ΔS = Q/T for a reversible process at constant temperature T — the basic exam-level formula.',
    'Heat flowing hot→cold always gives ΔS_total > 0; the reverse direction would require ΔS_total < 0, forbidden by the second law.',
    'Free expansion into vacuum and heat flow across a finite ΔT are the two classic irreversible processes.',
    'Perpetual motion machines of the second kind are impossible — not an engineering failure, but a direct violation of the second law.',
    'Entropy increase is often called the "arrow of time" — nearly the only physical law that distinguishes forward from backward in time.',
    'Cross-reference: Carnot efficiency η=1−Tc/Th (Heat Engines lesson) is itself a direct consequence of the second law and entropy never decreasing.',
  ],
  sandboxBuilder: (_) => const EntropySandbox(),
);
