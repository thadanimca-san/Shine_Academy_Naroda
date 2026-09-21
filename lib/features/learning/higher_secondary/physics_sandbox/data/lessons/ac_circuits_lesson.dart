import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../simulators/ac_circuits_sandbox.dart';

/// AC Circuits (RLC series, impedance, resonance) — the AC half of electricity.
final Lesson acCircuitsLesson = Lesson(
  topicId: 'ac-circuits',
  title: 'AC Circuits: RLC & Resonance',
  bigQuestion:
      'A resistor, inductor, and capacitor each respond differently to an alternating voltage — one behaves the same as in DC, one hates fast changes, one loves them. Wire all three in series and drive them at just the right frequency, and something remarkable happens: they cancel each other out completely.',
  whyItMatters:
      'AC circuits power literally everything plugged into a wall socket. The resonance condition XL = XC, giving ω₀ = 1/√LC, is one of the highest-yield single formulas in the entire JEE/NEET physics syllabus — it appears in radio tuning, filter circuits, and dozens of numerical problems every year. Understanding WHY inductors and capacitors behave oppositely with frequency is the conceptual key that unlocks the whole chapter.',
  prediction: const PredictionPrompt(
    scenario:
        'In a series RLC circuit driven at frequency ω, you slowly increase ω starting from a very low value. As ω rises toward ω₀ = 1/√LC, the circuit\'s impedance Z:',
    options: [
      'Keeps rising steadily the whole time',
      'Falls to a minimum right at ω₀, then rises again',
      'Stays constant no matter what ω is',
      'Rises to a maximum right at ω₀',
    ],
    correctIndex: 1,
    reveal:
        'At ω₀, XL and XC become equal and cancel in Z = √(R²+(XL−XC)²), leaving Z = R — the minimum possible impedance. Drag the frequency slider in the lab until Xₗ and X꜀ meet: the impedance meter dips to its lowest value exactly there, and the phase angle collapses to zero. This is resonance — the circuit conducts more current at ω₀ than at any other frequency.',
  ),
  experiments: [
    'Drag ω slowly upward and watch Xₗ = ωL rise steadily while X꜀ = 1/ωC falls',
    'Find the frequency where the two reactance bars in the diagram become equal — that is ω₀',
    'At that point, watch Z drop to its minimum (Z = R) and the phase angle φ collapse toward 0°',
    'Increase R and notice the minimum impedance (at resonance) rises, but ω₀ itself does NOT change — resonance depends only on L and C',
    'Push ω far above or below ω₀ and watch the voltage phasor swing away from the current phasor — the phase angle grows',
  ],
  concept: const [
    ContentBlock.paragraph(
      'An AC source supplies a voltage that oscillates sinusoidally: v = V₀ sinωt, where V₀ is the peak voltage and ω = 2πf is the angular frequency. Unlike DC, both current and voltage constantly change direction, and different circuit elements respond to that change in very different ways.',
      title: 'AC basics',
    ),
    ContentBlock.formula('v = V₀ sin ωt,   i = I₀ sin(ωt − φ)', title: 'AC VOLTAGE AND CURRENT'),
    ContentBlock.paragraph(
      'A resistor behaves exactly as in DC: v = iR at every instant, and current is always in phase with voltage. But an inductor opposes any CHANGE in current (self-induced back-EMF ε = −L di/dt) — the faster the current tries to change, the harder the inductor fights back. At high frequency, current is forced to change rapidly, so the inductor "resists" more. Its effective AC resistance, called reactance, therefore GROWS with frequency.',
      title: 'Why an inductor\'s reactance grows with frequency',
    ),
    ContentBlock.formula('X_L = ωL', title: 'INDUCTIVE REACTANCE'),
    ContentBlock.paragraph(
      'A capacitor works the opposite way. At LOW frequency, the capacitor has time to fully charge up each half-cycle, building a large opposing voltage that blocks current — high reactance. At HIGH frequency, the voltage reverses before the capacitor can charge much at all, so it never builds up much opposition — current flows more easily, meaning LOW reactance. In the limit of DC (ω→0), a capacitor blocks current completely (X_C → ∞); in the limit of very high frequency, it behaves almost like a wire (X_C → 0).',
      title: 'Why a capacitor\'s reactance shrinks with frequency',
    ),
    ContentBlock.formula('X_C = 1/(ωC)', title: 'CAPACITIVE REACTANCE'),
    ContentBlock.paragraph(
      'In a series RLC circuit, R, XL and XC combine like a Pythagorean sum, not a simple algebraic sum, because voltage across R is in phase with current, voltage across L LEADS current by 90°, and voltage across C LAGS current by 90° — so XL and XC point in opposite directions and partially cancel, while R sits at right angles to both.',
      title: 'Impedance: combining R, XL and XC',
    ),
    ContentBlock.formula('Z = √(R² + (X_L − X_C)²)', title: 'IMPEDANCE OF SERIES RLC CIRCUIT'),
    ContentBlock.paragraph(
      'Since impedance depends on (XL−XC), there exists one special frequency where they are exactly equal and cancel completely, leaving only R. At that frequency, called resonance, impedance is at its ABSOLUTE MINIMUM (Z = R) and current is at its ABSOLUTE MAXIMUM for a given driving voltage.',
      title: 'Resonance: when reactances cancel',
    ),
    ContentBlock.formula('X_L = X_C  ⟹  ω₀ = 1/√(LC),   Z_min = R', title: 'RESONANCE CONDITION (extremely high-yield)'),
    ContentBlock.paragraph(
      'The phase angle φ between voltage and current is given by tanφ = (XL−XC)/R. When XL > XC, voltage leads current (net "inductive" circuit); when XC > XL, current leads voltage (net "capacitive" circuit); at resonance φ = 0, voltage and current are perfectly in phase — the circuit behaves as if it were purely resistive.',
      title: 'Phase angle and power factor',
    ),
    ContentBlock.formula('cosφ = R/Z   (power factor),   P_avg = V_rms · I_rms · cosφ', title: 'AVERAGE POWER IN AN AC CIRCUIT'),
    ContentBlock.bullets([
      'Power factor cosφ measures how much of the apparent power (V_rms×I_rms) is actually delivered as real, usable power',
      'A pure resistor has cosφ = 1 (all power consumed); a pure L or C has cosφ = 0 (zero average power — energy sloshes back and forth but none is dissipated)',
      'At resonance, cosφ = 1 since φ = 0 — maximum power transfer occurs at resonance',
    ]),
    ContentBlock.realLife(
      'Radio and TV tuners are RLC circuits: turning the dial changes C (or L), shifting ω₀ = 1/√LC to match the frequency of the desired broadcast station, which then produces a huge resonant current while all other frequencies are suppressed. Power factor correction (adding capacitors) is used in industrial electrical systems to bring cosφ closer to 1, reducing wasted current for the same delivered power.',
    ),
    ContentBlock.mistake(
      'Adding R, XL and XC as plain numbers to get impedance. They must be combined as Z = √(R²+(XL−XC)²) because voltage across L and voltage across C are 90° out of phase with the current in OPPOSITE senses — they partially cancel rather than add.',
    ),
    ContentBlock.mistake(
      'Believing resonance depends on R. It does not — ω₀ = 1/√LC involves only L and C. Changing R changes how SHARP the resonance peak is (and how large the minimum impedance is, since Z_min = R), but never shifts where ω₀ occurs.',
    ),
    ContentBlock.example(
      'A series RLC circuit has R = 30 Ω, XL = 40 Ω, XC = 10 Ω. Find the impedance and phase angle.\n\nZ = √(R²+(XL−XC)²) = √(30²+(40−10)²) = √(900+900) = √1800 ≈ 42.4 Ω.\n\ntanφ = (XL−XC)/R = 30/30 = 1 ⟹ φ = 45°.\n\nSince XL > XC, voltage leads current by 45° — the circuit is net inductive.',
    ),
    ContentBlock.jeeTip(
      'At resonance, remember three facts simultaneously: (1) XL = XC, (2) Z = R (minimum), (3) current I₀ = V₀/R is MAXIMUM. JEE loves combining this with the Q-factor (sharpness of resonance) — a high L/C ratio with small R gives a sharp, narrow resonance peak.',
    ),
    ContentBlock.jeeTip(
      'A quick sanity check for reactance direction: as ω → 0 (DC), XC → ∞ (capacitor blocks DC completely — a classic DC-blocking application) while XL → 0 (inductor is just a wire in steady DC). As ω → ∞, the reverse: XC → 0, XL → ∞.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests pure-element circuits as special cases: pure resistor (P = VI, φ=0), pure inductor (P_avg = 0, current lags voltage by 90°), pure capacitor (P_avg = 0, current leads voltage by 90°). Only resistance ever dissipates real average power in an AC circuit — reactance alone dissipates nothing.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Instantaneous voltages across R, L, C in series',
      math: 'v_R = iR,  v_L = L di/dt,  v_C = q/C',
      note: 'Same current i flows through all three (series circuit); each element responds differently.',
    ),
    DerivationStep(
      title: 'Phase relationships for i = I₀ sin ωt',
      math: 'v_R in phase with i\nv_L leads i by 90°\nv_C lags i by 90°',
      note: 'This follows from differentiating/integrating the sinusoidal current.',
    ),
    DerivationStep(
      title: 'Add the three voltages as phasors (not plain numbers)',
      math: 'V₀² = V_R0² + (V_L0 − V_C0)²',
      note: 'V_L and V_C point in opposite directions on the phasor diagram (180° apart), so they subtract; V_R is perpendicular to both.',
    ),
    DerivationStep(
      title: 'Divide through by I₀ to get impedance',
      math: 'Z = V₀/I₀ = √(R² + (X_L − X_C)²)',
      note: 'X_L = V_L0/I₀ = ωL and X_C = V_C0/I₀ = 1/ωC by definition of reactance.',
    ),
    DerivationStep(
      title: 'Minimise Z with respect to ω',
      math: 'Z is minimum when X_L = X_C  ⟹  ωL = 1/(ωC)  ⟹  ω₀ = 1/√(LC)',
      note: 'At this ω₀, Z_min = R and current is maximum — the resonance condition.',
    ),
  ],
  formulas: const [
    FormulaEntry('AC voltage/current', 'v = V₀sinωt,  i = I₀sin(ωt−φ)'),
    FormulaEntry('Inductive reactance', 'X_L = ωL'),
    FormulaEntry('Capacitive reactance', 'X_C = 1/(ωC)'),
    FormulaEntry('Impedance (series RLC)', 'Z = √(R²+(X_L−X_C)²)'),
    FormulaEntry('Resonance frequency', 'ω₀ = 1/√(LC)', condition: 'Z minimum = R, current maximum'),
    FormulaEntry('Phase angle', 'tanφ = (X_L−X_C)/R'),
    FormulaEntry('Power factor', 'cosφ = R/Z'),
    FormulaEntry('Average AC power', 'P_avg = V_rms·I_rms·cosφ'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'As the frequency of an AC source increases, the reactance of an inductor:',
      options: ['Decreases', 'Increases', 'Stays constant', 'Becomes zero'],
      correctIndex: 1,
      solution: 'X_L = ωL. Since reactance is directly proportional to ω, it increases as frequency rises — the inductor opposes rapidly changing current more strongly.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'As the frequency of an AC source increases, the reactance of a capacitor:',
      options: ['Increases', 'Decreases', 'Stays constant', 'Becomes infinite'],
      correctIndex: 1,
      solution: 'X_C = 1/(ωC). Reactance is inversely proportional to ω, so it decreases as frequency rises — the capacitor has less time to build an opposing charge each cycle.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'In a series RLC circuit, R = 30 Ω, XL = 40 Ω, XC = 10 Ω. The impedance of the circuit is:',
      options: ['30 Ω', '42.4 Ω', '50 Ω', '70 Ω'],
      correctIndex: 1,
      solution: 'Z = √(R²+(XL−XC)²) = √(30²+30²) = √1800 ≈ 42.4 Ω.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A series RLC circuit has L = 1 H and C = 1 µF. The resonant angular frequency ω₀ is:',
      options: ['100 rad/s', '1000 rad/s', '10⁴ rad/s', '10 rad/s'],
      correctIndex: 1,
      solution: 'ω₀ = 1/√(LC) = 1/√(1×10⁻⁶) = 1/(10⁻³) = 1000 rad/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'At resonance in a series RLC circuit, the impedance equals:',
      options: ['Zero', 'R', 'XL + XC', '√(XL·XC)'],
      correctIndex: 1,
      solution: 'At resonance XL = XC, so they cancel in Z = √(R²+(XL−XC)²), leaving Z = R — the minimum possible impedance.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A series RLC circuit has R = 15 Ω and is driven exactly at its resonant frequency with V_rms = 30 V. The rms current is:',
      options: ['0.5 A', '1 A', '2 A', '15 A'],
      correctIndex: 2,
      solution: 'At resonance Z = R = 15 Ω. I_rms = V_rms/Z = 30/15 = 2 A.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'In a series RLC circuit driven below resonance (ω < ω₀), the circuit behaves predominantly:',
      options: [
        'Inductive — voltage leads current',
        'Capacitive — current leads voltage',
        'Purely resistive',
        'It depends only on R',
      ],
      correctIndex: 1,
      solution: 'Below ω₀, XC = 1/(ωC) is large (low ω) while XL = ωL is small, so XC > XL. The circuit is net capacitive, and current leads voltage (tanφ = (XL−XC)/R is negative).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'An AC circuit has V_rms = 200 V, I_rms = 2 A, and power factor cosφ = 0.6. The average power consumed is:',
      options: ['400 W', '240 W', '120 W', '600 W'],
      correctIndex: 1,
      solution: 'P_avg = V_rms·I_rms·cosφ = 200×2×0.6 = 240 W.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'In a purely inductive AC circuit (R = 0, C absent), the average power dissipated is:',
      options: ['Maximum', 'Zero', 'Equal to V_rms·I_rms', 'Depends on frequency'],
      correctIndex: 1,
      solution: 'In a pure inductor, current lags voltage by exactly 90° (φ=90°), so cosφ = 0 and P_avg = V_rms·I_rms·cosφ = 0 — energy oscillates in and out but none is permanently dissipated.',
    ),
  ],
  revision: [
    'v = V₀sinωt; resistor: in phase; inductor: current lags voltage by 90°; capacitor: current leads voltage by 90°.',
    'X_L = ωL grows with frequency; X_C = 1/ωC shrinks with frequency.',
    'Impedance: Z = √(R²+(X_L−X_C)²) — combine as a phasor sum, never add plainly.',
    'Resonance: X_L = X_C ⟹ ω₀ = 1/√(LC); at resonance Z = R (minimum) and current is maximum.',
    'Resonance frequency depends only on L and C — never on R.',
    'Power factor cosφ = R/Z; P_avg = V_rms·I_rms·cosφ. Pure L or C dissipates zero average power.',
  ],
  sandboxBuilder: (_) => const AcCircuitsSandbox(),
  accentColor: const Color(0xFF6D28D9),
);
