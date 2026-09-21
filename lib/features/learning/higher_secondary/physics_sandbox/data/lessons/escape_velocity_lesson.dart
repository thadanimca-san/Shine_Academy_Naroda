import '../../models/lesson.dart';
import '../../simulators/escape_velocity_sim.dart';
import '../../theme/tokens.dart';

/// Escape Velocity — the speed needed to leave a planet's gravity forever.
final Lesson escapeVelocityLesson = Lesson(
  topicId: 'escape-velocity',
  title: 'Escape Velocity',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Throw a ball straight up and it always falls back. Throw it fast enough, though, and it never comes back at all — it just keeps going, forever slowing but never stopping. Is there really one exact speed where "always falls back" flips to "never comes back"?',
  whyItMatters:
      'Escape velocity is the concept that connects gravitation to rockets, satellites, planetary atmospheres, and even black holes. It is a direct, elegant application of energy conservation — no calculus needed, just KE + PE = 0. It shows up constantly in JEE/NEET, from straightforward Earth-escape numericals to conceptual questions about why the Moon has no air.',
  prediction: const PredictionPrompt(
    scenario:
        'A ball is launched straight up from Earth\'s surface at exactly the escape velocity (11.2 km/s). What happens to its speed as it travels farther and farther from Earth?',
    options: [
      'It stays at exactly 11.2 km/s forever — escape velocity is a constant cruising speed',
      'It slows down continuously and approaches zero speed as it approaches infinite distance, but never turns back',
      'It slows down, stops completely at some finite height, then falls back',
      'It speeds up, since it is escaping Earth\'s pull',
    ],
    correctIndex: 1,
    reveal:
        'At exactly escape velocity, the ball\'s kinetic energy exactly cancels its (negative) gravitational potential energy at every point — total mechanical energy is zero. It keeps slowing due to gravity\'s continued pull, but the pull weakens as 1/r², so the ball asymptotically approaches zero speed only at infinite distance — it never quite stops, and it never turns around. In the lab, launch at exactly v_esc and watch the speed readout creep toward zero as the ball recedes, never reaching negative (falling) velocity.',
  ),
  experiments: [
    'Launch at slightly less than escape velocity — watch the ball slow, stop, and fall back',
    'Launch at exactly escape velocity — watch the speed asymptotically approach zero but the ball never returns',
    'Launch at well above escape velocity — the ball leaves with speed to spare, never even close to stopping',
    'Change the launch ANGLE at fixed escape speed — confirm it still escapes (angle does not matter, only speed)',
    'Switch the central body to a smaller mass or radius (Moon-like) and watch escape velocity readout drop sharply',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Escape velocity is the minimum speed an object needs, launched from a planet\'s surface, to break free of that planet\'s gravity permanently — reaching infinite distance with just barely zero speed left over, never to fall back. It is found purely from energy conservation, treating "escape" as reaching r = ∞ with KE = 0.',
      title: 'The minimum speed to leave forever',
    ),
    ContentBlock.formula('v_esc = √(2GM/R)', title: 'ESCAPE VELOCITY'),
    ContentBlock.bullets([
      'Depends only on the PLANET\'s mass M and radius R — never on the mass of the escaping object',
      'Independent of launch ANGLE — straight up or at any angle, the same speed suffices (ignoring atmosphere/terrain)',
      'For Earth: v_esc ≈ 11.2 km/s ≈ 40,300 km/h',
      'Larger M or smaller R (denser body) → larger escape velocity',
    ]),
    ContentBlock.paragraph(
      'Gravitational potential energy U = −GMm/r is NEGATIVE and increases (becomes less negative) toward zero as r → ∞. "Escaping" means having just enough kinetic energy to make total mechanical energy E = KE + U exactly zero — so the object can coast all the way to infinity, arriving with vanishingly small speed and using up all its KE fighting the negative PE along the way.',
      title: 'Why total energy = 0 is the escape condition',
    ),
    ContentBlock.realLife(
      'The Moon has essentially no atmosphere because its escape velocity is only about 2.4 km/s — far lower than Earth\'s 11.2 km/s. Gas molecules (especially light ones like hydrogen and helium) at typical temperatures move at speeds comparable to or exceeding lunar escape velocity, so they simply leak away into space over geological time, leaving the Moon airless.',
    ),
    ContentBlock.mistake(
      'Assuming heavier objects need a higher escape velocity than lighter ones. Escape velocity is completely independent of the escaping object\'s own mass — both the KE and PE terms are proportional to m, so m cancels out of the energy equation entirely. A feather and a rocket need the identical speed to escape Earth (ignoring air resistance).',
    ),
    ContentBlock.mistake(
      'Thinking escape velocity means the object keeps moving at that constant speed forever, like a cruising speed. In reality the object continuously decelerates due to gravity\'s ever-present (though weakening) pull; escape velocity is only the LAUNCH speed, not a maintained speed.',
    ),
    ContentBlock.example(
      'Find Earth\'s escape velocity given M = 6×10²⁴ kg, R = 6.4×10⁶ m, G = 6.674×10⁻¹¹ N·m²/kg².\n\nv_esc = √(2GM/R)\n= √(2 × 6.674×10⁻¹¹ × 6×10²⁴ / 6.4×10⁶)\n= √(8.01×10¹⁴ / 6.4×10⁶)\n= √(1.25×10⁸)\n≈ 1.12×10⁴ m/s = 11.2 km/s.',
    ),
    ContentBlock.jeeTip(
      'A shortcut worth memorising: v_esc = √2 × v_orbital for a low circular orbit at the same radius, since v_orbital = √(GM/R) and v_esc = √(2GM/R). Also, v_esc = √(2gR) using g = GM/R² — useful when g and R are given instead of G and M directly.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for escape velocity in terms of g and R (v_esc = √(2gR)) and expects the conceptual point that escape velocity does not depend on launch direction or the escaping mass. Also expect qualitative questions linking low escape velocity to a body\'s inability to retain an atmosphere (Moon, Mercury) versus high escape velocity retaining even light gases (Jupiter, Neptune).',
    ),
    ContentBlock.paragraph(
      'Taking the idea to its extreme: if a body is compressed enough that its escape velocity would need to exceed the speed of light c, then nothing — not even light — can escape it. That defines a black hole conceptually, using the SAME formula v_esc = √(2GM/R): setting v_esc = c and solving for R gives the Schwarzschild radius, the boundary of no return.',
      title: 'Taking it further: black holes',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Write total mechanical energy at launch (surface)',
      math: 'E_i = KE_i + U_i = ½mv² + (−GMm/R)',
      note: 'v is the launch speed we want to find; R is the planet\'s radius.',
    ),
    DerivationStep(
      title: 'Write total mechanical energy at infinity (just barely escapes)',
      math: 'E_f = KE_f + U_f = 0 + 0 = 0',
      note: 'At infinite distance, U → 0. "Just escapes" means it arrives with zero leftover speed, so KE_f = 0 too.',
    ),
    DerivationStep(
      title: 'Apply conservation of mechanical energy',
      math: 'E_i = E_f  →  ½mv² − GMm/R = 0',
    ),
    DerivationStep(
      title: 'Cancel the escaping mass m',
      math: '½v² = GM/R',
      note: 'm cancels completely — escape velocity never depends on the mass of the object escaping.',
    ),
    DerivationStep(
      title: 'Solve for v — the escape velocity',
      math: 'v² = 2GM/R  →  v_esc = √(2GM/R)',
      note: 'Equivalently v_esc = √(2gR), using g = GM/R².',
    ),
  ],
  formulas: const [
    FormulaEntry('Escape velocity', 'v_esc = √(2GM/R)'),
    FormulaEntry('Escape velocity (using g)', 'v_esc = √(2gR)'),
    FormulaEntry('Relation to orbital speed', 'v_esc = √2 × v_orbital', condition: 'same radius'),
    FormulaEntry('Earth\'s escape velocity', 'v_esc ≈ 11.2 km/s'),
    FormulaEntry('Moon\'s escape velocity', 'v_esc ≈ 2.4 km/s'),
    FormulaEntry('Total energy at escape', 'E = KE + U = 0'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Escape velocity from a planet\'s surface depends on:',
      options: [
        'The mass of the escaping object only',
        'The mass and radius of the planet only',
        'Both the planet\'s and object\'s mass',
        'The launch angle only',
      ],
      correctIndex: 1,
      solution: 'v_esc = √(2GM/R) depends only on the planet\'s mass M and radius R — the escaping object\'s mass cancels out of the energy equation.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The escape velocity of Earth is approximately:',
      options: ['1.12 km/s', '11.2 km/s', '112 km/s', '2.4 km/s'],
      correctIndex: 1,
      solution: 'v_esc for Earth ≈ 11.2 km/s, a standard value to memorise.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'If Earth\'s mass were doubled while its radius stayed the same, the new escape velocity would be:',
      options: ['11.2 km/s', '11.2√2 km/s', '22.4 km/s', '11.2/√2 km/s'],
      correctIndex: 1,
      solution: 'v_esc ∝ √M. Doubling M multiplies v_esc by √2, giving 11.2√2 ≈ 15.8 km/s.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The Moon has essentially no atmosphere primarily because:',
      options: [
        'It is too far from the Sun',
        'Its low escape velocity lets gas molecules\' thermal speeds exceed it, so gases leak into space',
        'It has no gravity at all',
        'Solar wind blew away its early atmosphere instantly',
      ],
      correctIndex: 1,
      solution: 'The Moon\'s escape velocity (~2.4 km/s) is low enough that a significant fraction of gas molecules, especially light ones, reach or exceed it due to thermal motion, so the atmosphere gradually escapes over time.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A projectile is launched from Earth\'s surface at exactly escape velocity but at 45° to the vertical (instead of straight up). Compared to a vertical launch at the same speed, it:',
      options: [
        'Falls back because it is not launched straight up',
        'Still escapes — escape velocity is independent of launch angle',
        'Escapes only if the angle is less than 30°',
        'Needs a higher speed to escape at an angle',
      ],
      correctIndex: 1,
      solution: 'Escape velocity depends only on total energy (KE + PE), not on the direction of the velocity vector, so any launch angle at v_esc results in escape (ignoring obstacles/atmosphere).',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'The ratio of escape velocity to orbital velocity for a satellite in a low circular orbit around the same planet is:',
      options: ['1 : 1', '√2 : 1', '2 : 1', '1 : √2'],
      correctIndex: 1,
      solution: 'v_esc = √(2GM/R), v_orbital = √(GM/R). Ratio v_esc/v_orbital = √2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A planet has the same mass as Earth but half its radius. The escape velocity from this planet compared to Earth\'s is:',
      options: ['Same', '√2 times Earth\'s', 'Half of Earth\'s', '2 times Earth\'s'],
      correctIndex: 1,
      solution: 'v_esc = √(2GM/R) ∝ 1/√R at fixed M. Halving R multiplies v_esc by √2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'The concept of a black hole\'s "point of no return" (Schwarzschild radius) is obtained by setting v_esc = √(2GM/R) equal to:',
      options: ['Zero', 'The speed of sound', 'The speed of light c', 'The orbital velocity'],
      correctIndex: 2,
      solution: 'Setting v_esc = c and solving for R gives the Schwarzschild radius R_s = 2GM/c² — the radius at which even light cannot escape, defining a black hole conceptually via the same escape-velocity formula.',
    ),
  ],
  revision: [
    'v_esc = √(2GM/R) = √(2gR) — depends only on the planet, never on the escaping object\'s mass.',
    'Escape condition: total mechanical energy KE + U = 0, so the object just reaches infinity with zero speed left.',
    'Escape velocity is independent of launch angle — only the launch SPEED matters.',
    'Earth\'s escape velocity ≈ 11.2 km/s; the Moon\'s is much lower (~2.4 km/s), which is why it has no atmosphere.',
    'v_esc = √2 × v_orbital for a body at the same radius.',
    'Setting v_esc = speed of light gives the (conceptual) Schwarzschild radius of a black hole.',
  ],
  sandboxBuilder: (_) => const EscapeVelocitySimulator(),
);
