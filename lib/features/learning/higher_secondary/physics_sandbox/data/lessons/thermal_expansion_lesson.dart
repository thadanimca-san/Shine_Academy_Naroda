import '../../models/lesson.dart';
import '../../simulators/thermal_expansion_sandbox.dart';
import '../../theme/tokens.dart';

/// Thermal Expansion — linear, area, and volume expansion, and why railway tracks have gaps.
final Lesson thermalExpansionLesson = Lesson(
  topicId: 'thermal-expansion',
  title: 'Thermal Expansion',
  accentColor: Palette.chThermal,
  bigQuestion:
      'Look closely at an old railway track and you\'ll spot small gaps between consecutive rail segments — put there ON PURPOSE by engineers. Why would anyone deliberately build a gap into a railway track, of all things?',
  whyItMatters:
      'Thermal expansion is one of the most "visible" thermodynamics topics — bridges, railway tracks, thermostats, and even how lakes freeze all trace back to the same handful of small formulas. NEET loves the anomalous expansion of water as a pure-recall conceptual fact, and JEE frequently tests the β=2α, γ=3α approximations derived from binomial expansion.',
  prediction: const PredictionPrompt(
    scenario:
        'A steel rod is heated so its temperature rises by ΔT, and its length increases by ΔL. If you instead used a rod of the SAME material but TWICE the original length, heated through the same ΔT, the new ΔL would be:',
    options: [
      'The same ΔL (only ΔT matters)',
      'Twice as large (ΔL ∝ original length L₀)',
      'Four times as large',
      'Half as large',
    ],
    correctIndex: 1,
    reveal:
        'ΔL = L₀αΔT — the expansion is directly proportional to the ORIGINAL length, so doubling L₀ doubles ΔL for the same ΔT and material. In the lab, drag the temperature slider up and watch the rod visibly stretch — the longer the starting bar, the more absolute length it gains for the same temperature rise, even though the FRACTIONAL expansion (ΔL/L₀) stays identical.',
  ),
  experiments: [
    'Raise ΔT from 0°C to 200°C and watch the rod visibly elongate, more so at higher temperatures',
    'Note the length-change readout grows linearly with ΔT, exactly as ΔL=L₀αΔT predicts',
    'Switch on the bimetallic-strip view and raise ΔT — watch the strip visibly curl toward the steel side',
    'Compare how much the strip bends at low ΔT vs high ΔT — bending increases with temperature too',
    'Imagine (or estimate) what would happen if the rod were clamped rigidly at both ends and couldn\'t expand — that trapped expansion becomes enormous internal stress',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Almost all solids expand when heated: raising the temperature makes atoms vibrate more vigorously about their equilibrium positions, and because the interatomic potential well is slightly asymmetric (easier to push atoms apart than squeeze them together), the AVERAGE atomic spacing increases with temperature. This microscopic effect adds up to a macroscopic, measurable change in length, area, and volume.',
      title: 'Why solids expand when heated',
    ),
    ContentBlock.formula('ΔL = L₀αΔT', title: 'LINEAR EXPANSION'),
    ContentBlock.bullets([
      'L₀ = original length, ΔT = temperature change, α = coefficient of linear expansion (per °C or per K, material-specific)',
      'ΔL is directly proportional to BOTH the original length and the temperature change',
      'α is typically very small (order 10⁻⁵ to 10⁻⁶ per °C) for common metals — expansion is a small effect, but adds up over long structures like railway tracks or bridges',
    ]),
    ContentBlock.paragraph(
      'A 2-D object (a sheet, a plate, a disc) expands in AREA when heated — every linear dimension grows by the same fractional amount, so area, being length×breadth, grows by roughly TWICE that fraction. Similarly, a 3-D solid expands in VOLUME, growing by roughly THREE times the linear fractional expansion, since volume is length×breadth×height.',
      title: 'Area and volume expansion',
    ),
    ContentBlock.formula('ΔA = A₀·β·ΔT ≈ A₀·(2α)·ΔT\nΔV = V₀·γ·ΔT ≈ V₀·(3α)·ΔT',
        title: 'AREA (β≈2α) AND VOLUME (γ≈3α) EXPANSION'),
    ContentBlock.paragraph(
      'These factors of 2 and 3 come directly from the binomial approximation. Consider a cube of side L₀: after heating, each side becomes L₀(1+αΔT). The new volume is L₀³(1+αΔT)³. Expanding (1+αΔT)³ = 1 + 3αΔT + 3(αΔT)² + (αΔT)³ — and since αΔT is a tiny number (typically ~10⁻³ or smaller even for large ΔT), the squared and cubed terms are utterly negligible. Keeping only the first-order term gives V ≈ V₀(1 + 3αΔT), so ΔV ≈ V₀(3α)ΔT — hence γ ≈ 3α. The exact same binomial logic on a square (1+αΔT)² gives β ≈ 2α for area.',
      title: 'Deriving the 2α and 3α approximations',
    ),
    ContentBlock.realLife(
      'Railway tracks are laid with small GAPS between consecutive rail segments specifically so that on hot days, when the rails expand (ΔL = L₀αΔT), they have room to grow without buckling or bending out of shape. Bridges similarly include EXPANSION JOINTS — segmented gaps, often with an interlocking zigzag pattern — that let the structure lengthen and shorten with the seasons without cracking.',
    ),
    ContentBlock.realLife(
      'A BIMETALLIC STRIP bonds two different metals (commonly brass and steel) tightly together along their length. Since the two metals have different α values, one expands more than the other when heated, forcing the whole strip to bend (toward the metal with the SMALLER α, since that side effectively becomes the "inside" of the curve). This bending is used directly as a temperature-triggered switch in old-fashioned thermostats, electric iron temperature control, and fire alarms.',
    ),
    ContentBlock.paragraph(
      'Water shows an ANOMALOUS expansion behaviour: unlike most substances, which simply keep shrinking as they cool, water is DENSEST at 4°C — it actually expands slightly on cooling from 4°C down to 0°C (and expands further, dramatically, on freezing into ice). This means ice (and near-0°C water) is LESS dense than 4°C water and floats on top.',
      title: 'The anomalous expansion of water',
    ),
    ContentBlock.mistake(
      'Assuming water behaves like every other liquid, contracting monotonically as it cools. Between 0°C and 4°C, water actually EXPANDS as it cools further toward 0°C — the density maximum sits at 4°C, not at the freezing point.',
    ),
    ContentBlock.mistake(
      'Forgetting to keep temperature changes in consistent units, or forgetting ΔT is the same whether measured in °C or K (since a 1°C change equals a 1 K change) — but absolute temperatures themselves are NOT interchangeable between the two scales.',
    ),
    ContentBlock.example(
      'A steel rod of length 2 m at 20°C is heated to 120°C. α_steel = 12×10⁻⁶ /°C. Find the new length.\n\nΔT = 120 − 20 = 100°C.\nΔL = L₀αΔT = 2 × 12×10⁻⁶ × 100 = 2400×10⁻⁶ m = 2.4×10⁻³ m = 2.4 mm.\nNew length = 2 m + 0.0024 m = 2.0024 m.',
    ),
    ContentBlock.jeeTip(
      'In problems combining thermal expansion with mechanical stress (a rod clamped rigidly at both ends and then heated), the rod is PREVENTED from expanding, so the "would-be" ΔL is converted entirely into thermal STRESS: stress = Y·α·ΔT (Y = Young\'s modulus). This is a classic JEE crossover question between thermal expansion and elasticity.',
    ),
    ContentBlock.neetNote(
      'NEET loves this exact conceptual fact: because water\'s density is maximum at 4°C, a lake freezes from the TOP down, not the bottom up. As surface water cools below 4°C it becomes LESS dense and stays on top (eventually freezing into a floating ice layer), while the denser 4°C water sinks to the bottom — this insulating ice layer is why fish and aquatic life can survive winter under a frozen lake.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define the linear expansion coefficient',
      math: 'α = (1/L₀)·(ΔL/ΔT)   →   ΔL = L₀αΔT',
      note: 'α is defined as the fractional length change per unit temperature rise — an intrinsic material property.',
    ),
    DerivationStep(
      title: 'Consider a square plate of side L₀ heated by ΔT',
      math: 'New side = L₀(1+αΔT)\nNew area = L₀²(1+αΔT)²',
    ),
    DerivationStep(
      title: 'Binomial-expand, keeping only the first-order term',
      math: '(1+αΔT)² = 1 + 2αΔT + (αΔT)² ≈ 1 + 2αΔT',
      note: 'Since αΔT ≪ 1 for realistic temperature changes, (αΔT)² is negligible.',
    ),
    DerivationStep(
      title: 'Extract the area expansion result',
      math: 'A ≈ A₀(1+2αΔT)  →  ΔA = A₀(2α)ΔT = A₀βΔT,   β ≈ 2α',
    ),
    DerivationStep(
      title: 'Repeat for a cube of side L₀ (volume expansion)',
      math: 'V = L₀³(1+αΔT)³ = L₀³(1+3αΔT+3(αΔT)²+(αΔT)³) ≈ L₀³(1+3αΔT)',
      note: 'Again dropping the negligible higher-order terms.',
    ),
    DerivationStep(
      title: 'Extract the volume expansion result',
      math: 'ΔV = V₀(3α)ΔT = V₀γΔT,   γ ≈ 3α',
      note: 'This 1:2:3 ratio among α, β, γ holds for any isotropic solid, regardless of shape.',
    ),
  ],
  formulas: const [
    FormulaEntry('Linear expansion', 'ΔL = L₀αΔT'),
    FormulaEntry('Area expansion', 'ΔA = A₀βΔT ≈ A₀(2α)ΔT'),
    FormulaEntry('Volume expansion', 'ΔV = V₀γΔT ≈ V₀(3α)ΔT'),
    FormulaEntry('Coefficient ratio', 'α : β : γ ≈ 1 : 2 : 3'),
    FormulaEntry('Thermal stress (rod clamped, prevented from expanding)', 'stress = YαΔT', condition: 'Y = Young\'s modulus'),
    FormulaEntry('Water density anomaly', 'ρ_max at T = 4°C'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The linear expansion of a rod is given by:',
      options: ['ΔL = L₀αΔT', 'ΔL = L₀α/ΔT', 'ΔL = αΔT', 'ΔL = L₀/αΔT'],
      correctIndex: 0,
      solution: 'ΔL = L₀αΔT — expansion is proportional to original length and temperature change, scaled by the material\'s α.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'For an isotropic solid, the volume expansion coefficient γ relates to the linear expansion coefficient α as:',
      options: ['γ = α', 'γ = 2α', 'γ = 3α', 'γ = α/3'],
      correctIndex: 2,
      solution: 'From binomial expansion of (1+αΔT)³, keeping first-order terms, γ ≈ 3α.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Water has its maximum density at:',
      options: ['0°C', '4°C', '100°C', '-4°C'],
      correctIndex: 1,
      solution: 'Water\'s anomalous expansion gives it a density MAXIMUM at 4°C — it expands both on heating above 4°C and on cooling below 4°C toward 0°C.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A lake freezes from the top down (rather than bottom up) primarily because:',
      options: [
        'Ice is a good conductor of heat',
        'Water below 4°C becomes less dense and stays near the surface, eventually freezing there',
        'The lake bottom is always warmer due to geothermal heat',
        'Wind only cools the surface',
      ],
      correctIndex: 1,
      solution: 'Below 4°C, water becomes progressively less dense as it cools further, so it remains near the top; the densest (4°C) water sinks to the bottom, and the surface layer eventually freezes, insulating the water below.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A steel rod 5 m long at 15°C is heated to 65°C. If α_steel = 12×10⁻⁶/°C, find ΔL.',
      options: ['1.5 mm', '3.0 mm', '0.6 mm', '6.0 mm'],
      correctIndex: 1,
      solution: 'ΔT = 50°C. ΔL = L₀αΔT = 5 × 12×10⁻⁶ × 50 = 3000×10⁻⁶ m = 3.0×10⁻³ m = 3.0 mm.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A metal plate of area 2 m² is heated through 100°C. If α = 1.2×10⁻⁵/°C, find the increase in area (using β ≈ 2α).',
      options: ['2.4×10⁻³ m²', '4.8×10⁻³ m²', '1.2×10⁻³ m²', '9.6×10⁻³ m²'],
      correctIndex: 1,
      solution: 'β = 2α = 2.4×10⁻⁵/°C. ΔA = A₀βΔT = 2 × 2.4×10⁻⁵ × 100 = 4.8×10⁻³ m².',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A steel rod is rigidly clamped at both ends so it cannot expand, then heated through ΔT = 50°C. Given α = 12×10⁻⁶/°C and Y = 2×10¹¹ Pa, the thermal stress developed is:',
      options: ['1.2×10⁸ Pa', '6×10⁵ Pa', '1.2×10⁵ Pa', '2.4×10⁸ Pa'],
      correctIndex: 0,
      solution: 'stress = YαΔT = 2×10¹¹ × 12×10⁻⁶ × 50 = 2×10¹¹ × 6×10⁻⁴ = 1.2×10⁸ Pa.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A bimetallic strip made of brass (larger α) and steel (smaller α), bonded together, bends when heated. It curves toward:',
      options: [
        'The brass side (larger α)',
        'The steel side (smaller α)',
        'It does not bend, only stretches',
        'Randomly, depending on strip thickness only',
      ],
      correctIndex: 1,
      solution: 'The metal with the larger α (brass) expands more and effectively forms the outer/longer arc, forcing the strip to curve toward the metal with the smaller α (steel), which forms the inner/shorter arc.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'Railway tracks are laid with small gaps between segments mainly to:',
      options: [
        'Save material cost',
        'Allow thermal expansion in hot weather without buckling',
        'Make the track easier to inspect',
        'Reduce the weight of the track',
      ],
      correctIndex: 1,
      solution: 'The gaps provide room for the rails to expand (ΔL=L₀αΔT) on hot days without buckling or bending out of shape.',
    ),
  ],
  revision: [
    'Linear expansion: ΔL = L₀αΔT. Area: ΔA = A₀βΔT ≈ A₀(2α)ΔT. Volume: ΔV = V₀γΔT ≈ V₀(3α)ΔT.',
    'The 2α and 3α approximations come from binomial-expanding (1+αΔT)² and (1+αΔT)³ and dropping negligible higher-order terms.',
    'Railway track gaps and bridge expansion joints exist to accommodate ΔL=L₀αΔT without structural damage.',
    'Bimetallic strips bend toward the metal with the SMALLER α when heated (used in thermostats, fire alarms).',
    'Water is anomalous: density is MAXIMUM at 4°C, not at 0°C — it expands on cooling from 4°C to 0°C.',
    'This is why lakes freeze top-down: sub-4°C water stays buoyant near the surface, insulating life below with a floating ice layer.',
    'A rod clamped and prevented from expanding develops thermal stress = YαΔT instead of actually changing length.',
  ],
  sandboxBuilder: (_) => const ThermalExpansionSandbox(),
);
