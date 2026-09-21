import '../../models/lesson.dart';
import '../../simulators/calorimetry_sim.dart';
import '../../theme/tokens.dart';

/// Calorimetry — heat exchange, specific heat, and latent heat of phase change.
final Lesson calorimetryLesson = Lesson(
  topicId: 'calorimetry',
  title: 'Calorimetry',
  accentColor: Palette.chThermal,
  bigQuestion:
      'Drop an ice cube into a glass of water. The mixture sits there, ice slowly melting, but the thermometer reading barely budges from 0°C — even though the water around it is clearly warmer and losing heat to the ice the whole time. Where is all that heat going, if not into raising the temperature?',
  whyItMatters:
      'Calorimetry is simply energy conservation applied to heat — "heat lost = heat gained" — but it is one of the most numerically rich topics in the NEET/JEE thermal syllabus, mixing specific heat, latent heat, and mixture problems in nearly every paper. It also explains huge real-world effects, from why coastal cities have milder climates to why steam burns are far worse than boiling-water burns.',
  prediction: const PredictionPrompt(
    scenario:
        'An ice-water mixture at 0°C is heated at a constant rate. As heat is added, ALL the ice melts before the temperature starts rising above 0°C. What is happening to the added heat energy while the temperature stays flat at 0°C?',
    options: [
      'The heat is being reflected away and wasted',
      'The heat is going entirely into breaking the ice\'s molecular bonds (latent heat), not raising temperature',
      'The thermometer is broken during melting',
      'No heat is actually being absorbed during this phase',
    ],
    correctIndex: 1,
    reveal:
        'During a phase change, ALL added heat goes into latent heat (Q = mL) — breaking molecular bonds to convert solid to liquid — with NONE of it raising temperature. Only after every last bit of ice has melted does added heat start raising the water\'s temperature again. In the lab, add heat to an ice-water mix and watch the temperature graph go perfectly flat during melting, then start climbing only once the ice fraction hits zero.',
  ),
  experiments: [
    'Add heat to a pure ice-water mixture and watch temperature stay flat at 0°C until all ice melts',
    'Mix hot and cold water of different masses and watch the final equilibrium temperature settle where heat lost = heat gained',
    'Swap the mixing liquid for one with a different specific heat and see the equilibrium temperature shift',
    'Add heat to boiling water and watch temperature stay flat at 100°C during the liquid-to-vapor transition',
    'Compare how much heat is needed to melt ice versus to raise the same mass of water by 1°C',
  ],
  concept: const [
    ContentBlock.paragraph(
      'The principle of calorimetry is simply the law of conservation of energy applied to heat exchange: when two bodies at different temperatures are brought into contact (in an insulated system with no heat lost to surroundings), the heat LOST by the hotter body exactly EQUALS the heat GAINED by the colder body, until both reach a common equilibrium temperature. No heat is created or destroyed — it just moves from hot to cold.',
      title: 'Heat lost = heat gained',
    ),
    ContentBlock.formula('Q = mcΔT', title: 'HEAT FOR A TEMPERATURE CHANGE'),
    ContentBlock.bullets([
      'm = mass of the substance',
      'c = specific heat capacity — heat needed to raise 1 kg by 1°C (or 1 K), a material property',
      'ΔT = change in temperature',
      'Water has an unusually HIGH specific heat (c = 4186 J/kg·K), meaning it resists temperature change strongly',
    ]),
    ContentBlock.formula('Q = mL', title: 'LATENT HEAT FOR A PHASE CHANGE'),
    ContentBlock.paragraph(
      'Latent heat L is the energy needed to change a substance\'s STATE (solid↔liquid or liquid↔gas) WITHOUT any change in temperature. This heat goes entirely into breaking or forming the intermolecular bonds that define the phase — it does not speed up molecular motion, so temperature stays constant throughout the change. This is exactly why an ice-water mixture stays pinned at 0°C: as long as ANY ice remains, added heat keeps melting more ice rather than warming the water.',
      title: 'Why phase changes happen at constant temperature',
    ),
    ContentBlock.bullets([
      'Latent heat of fusion L_f: solid ↔ liquid (e.g. ice to water, L_f ≈ 334,000 J/kg)',
      'Latent heat of vaporization L_v: liquid ↔ gas (e.g. water to steam, L_v ≈ 2,260,000 J/kg — nearly 7× larger than L_f)',
      'Because L_v is so large, a steam burn at 100°C is far worse than a boiling-water burn — steam releases enormous extra energy condensing back to liquid on your skin',
    ]),
    ContentBlock.realLife(
      'Water\'s exceptionally high specific heat capacity is why coastal and island climates are milder than inland/continental ones — the ocean absorbs huge amounts of solar heat with only a small temperature rise during the day, then releases it slowly at night, moderating temperature swings. It is also why water is used as an engine coolant and why a hot-water bottle stays warm for hours: it stores a lot of thermal energy per degree of temperature.',
    ),
    ContentBlock.mistake(
      'Using Q = mcΔT during a phase change. While ice is melting (or water is boiling), temperature does NOT change, so ΔT = 0 for that portion — you must use Q = mL instead. A common calorimetry mistake is applying the wrong formula to the wrong stage of a multi-step heating/cooling problem.',
    ),
    ContentBlock.mistake(
      'Forgetting to account for the calorimeter (container) itself absorbing heat, or forgetting that ice supplied at a temperature BELOW 0°C must first be warmed to 0°C (using Q = m·c_ice·ΔT) before it can even begin melting (Q = mL_f), before the resulting water warms further (Q = m·c_water·ΔT). Multi-stage problems require tracking each stage\'s heat separately.',
    ),
    ContentBlock.example(
      '200 g of water at 80°C is mixed with 100 g of water at 20°C in an insulated container. Find the final equilibrium temperature.\n\nHeat lost by hot water = heat gained by cold water (masses in kg, c cancels since it\'s the same liquid):\n0.2 × (80 − T) = 0.1 × (T − 20)\n16 − 0.2T = 0.1T − 2\n18 = 0.3T\nT = 60°C.',
    ),
    ContentBlock.jeeTip(
      'For multi-stage problems (ice below 0°C warming, melting, then heating as water), break the process into separate stages and compute Q for EACH stage individually: Q₁ = m·c_ice·(0−T_initial), Q₂ = m·L_f, Q₃ = m·c_water·(T_final−0). Sum them for total heat required — never try to shortcut across a phase transition with a single Q = mcΔT.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests "will all the ice melt?" problems: compare the heat AVAILABLE from the hot substance cooling to 0°C against the heat REQUIRED to melt all the ice (mL_f). If available heat is less than required, only some ice melts and the final temperature stays at 0°C; if more, all ice melts and the mixture rises above 0°C — solve stage by stage.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'State the principle of calorimetry for two bodies exchanging heat',
      math: 'Heat lost by hotter body = Heat gained by colder body (isolated system)',
      note: 'This follows directly from conservation of energy — no heat escapes to the surroundings.',
    ),
    DerivationStep(
      title: 'Express heat lost by the hot body (mass m₁, specific heat c₁, from T₁ to T_f)',
      math: 'Q_lost = m₁c₁(T₁ − T_f)',
    ),
    DerivationStep(
      title: 'Express heat gained by the cold body (mass m₂, specific heat c₂, from T₂ to T_f)',
      math: 'Q_gained = m₂c₂(T_f − T₂)',
    ),
    DerivationStep(
      title: 'Set them equal per the calorimetry principle',
      math: 'm₁c₁(T₁ − T_f) = m₂c₂(T_f − T₂)',
    ),
    DerivationStep(
      title: 'Solve for the common equilibrium temperature',
      math: 'T_f = (m₁c₁T₁ + m₂c₂T₂) / (m₁c₁ + m₂c₂)',
      note: 'A weighted average of the two initial temperatures, weighted by each body\'s heat capacity m·c.',
    ),
  ],
  formulas: const [
    FormulaEntry('Heat for temperature change', 'Q = mcΔT'),
    FormulaEntry('Heat for phase change', 'Q = mL'),
    FormulaEntry('Principle of calorimetry', 'Heat lost = Heat gained'),
    FormulaEntry('Equilibrium temperature (mixing)', 'T_f = (m₁c₁T₁ + m₂c₂T₂)/(m₁c₁ + m₂c₂)'),
    FormulaEntry('Latent heat of fusion (ice)', 'L_f ≈ 3.34×10⁵ J/kg'),
    FormulaEntry('Latent heat of vaporization (water)', 'L_v ≈ 2.26×10⁶ J/kg'),
    FormulaEntry('Specific heat of water', 'c_water = 4186 J/(kg·K)'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The heat required to raise the temperature of 1 kg of water by 5°C (c = 4200 J/kg·K) is:',
      options: ['4200 J', '21000 J', '42000 J', '8400 J'],
      correctIndex: 1,
      solution: 'Q = mcΔT = 1 × 4200 × 5 = 21000 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'During melting of ice at 0°C, the temperature of the ice-water mixture:',
      options: ['Rises steadily', 'Falls steadily', 'Remains constant', 'Fluctuates randomly'],
      correctIndex: 2,
      solution: 'All heat added during a phase change goes into latent heat (breaking bonds), not raising temperature — so T stays constant at 0°C until melting completes.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The heat required to convert 10 g of ice at 0°C completely into water at 0°C (L_f = 336 J/g) is:',
      options: ['336 J', '3360 J', '33.6 J', '33600 J'],
      correctIndex: 1,
      solution: 'Q = mL = 10 × 336 = 3360 J.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Why does a burn from steam at 100°C hurt more than a burn from boiling water at 100°C?',
      options: [
        'Steam is actually hotter than boiling water',
        'Steam releases additional latent heat of vaporization when it condenses on skin',
        'Steam has a lower specific heat',
        'There is no real difference',
      ],
      correctIndex: 1,
      solution: 'Steam must first condense to water on the skin, releasing its large latent heat of vaporization (≈2.26×10⁶ J/kg) IN ADDITION to cooling from 100°C — delivering far more total energy than boiling water alone.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: '100 g of water at 90°C is mixed with 100 g of water at 10°C. The equilibrium temperature (equal masses, same c) is:',
      options: ['40°C', '50°C', '60°C', '45°C'],
      correctIndex: 1,
      solution: 'Equal masses and specific heats → equilibrium is the simple average: (90+10)/2 = 50°C.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: '50 g of ice at 0°C is added to 200 g of water at 30°C. (c_water = 4200 J/kg·K, L_f = 336000 J/kg). Will all the ice melt?',
      options: [
        'No, only part of it melts',
        'Yes — heat available exceeds heat required to melt all the ice',
        'Exactly none melts',
        'Cannot be determined',
      ],
      correctIndex: 1,
      solution:
          'Heat available if water cools fully to 0°C: Q = 0.2×4200×30 = 25200 J. Heat required to melt 50 g ice: Q = 0.05×336000 = 16800 J. Since 25200 J > 16800 J, all ice melts (and the mixture ends above 0°C).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'Using the previous scenario (50 g ice at 0°C + 200 g water at 30°C), the final equilibrium temperature is closest to:',
      options: ['0°C', '8°C', '15°C', '22°C'],
      correctIndex: 1,
      solution:
          'After melting ice (uses 16800 J), remaining heat = 25200−16800 = 8400 J warms the combined 250 g of water from 0°C: 8400 = 0.25×4200×ΔT → ΔT = 8°C. Final temperature ≈ 8°C.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.advanced,
      question: 'Why do coastal regions have milder climates than continental interiors at the same latitude?',
      options: [
        'Coastal air has lower density',
        'Water\'s high specific heat absorbs/releases large amounts of heat with small temperature change, moderating nearby air temperature',
        'Oceans reflect all sunlight',
        'Coastal regions receive less sunlight',
      ],
      correctIndex: 1,
      solution: 'Water\'s large c means it changes temperature slowly for a given heat exchange, buffering nearby land from extreme daily/seasonal temperature swings.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A calorimeter of heat capacity 50 J/K contains 100 g of water at 20°C. Hot metal of mass 50 g at 200°C is dropped in, and the mixture settles at 30°C. If c_water = 4.2 J/g·K, the specific heat of the metal is closest to:',
      options: ['0.20 J/g·K', '0.55 J/g·K', '1.4 J/g·K', '2.1 J/g·K'],
      correctIndex: 1,
      solution:
          'Heat gained by water+calorimeter = (100×4.2 + 50)×(30−20) = (420+50)×10 = 4700 J. Heat lost by metal = 50×c×(200−30) = 8500c. Setting equal: 8500c = 4700 → c ≈ 0.55 J/g·K.',
    ),
  ],
  revision: [
    'Principle of calorimetry: heat lost by hotter body = heat gained by colder body (energy conservation).',
    'Q = mcΔT for temperature change; Q = mL for phase change — never mix these up.',
    'During melting/boiling, temperature stays constant — ALL heat goes into breaking/forming bonds.',
    'Latent heat of vaporization is much larger than latent heat of fusion (steam burns hurt more).',
    'Water\'s high specific heat moderates climate near large water bodies.',
    'Multi-stage problems (ice below 0°C → water above 0°C): compute heat for each stage separately, then sum.',
    'Check "will it all melt?" by comparing heat available vs heat required for the full phase change.',
  ],
  sandboxBuilder: (_) => const CalorimetrySimulator(),
);
