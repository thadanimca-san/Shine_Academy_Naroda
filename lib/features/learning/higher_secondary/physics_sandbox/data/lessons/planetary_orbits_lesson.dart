import '../../models/lesson.dart';
import '../../simulators/planetary_motion_sim.dart';
import '../../theme/tokens.dart';

/// Planetary Orbits — Kepler's three laws, and why farther planets orbit so much slower.
final Lesson planetaryOrbitsLesson = Lesson(
  topicId: 'planetary-orbits',
  title: 'Planetary Orbits',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Mercury completes an orbit around the Sun in just 88 days. Neptune, about 30 times farther out, takes 165 YEARS. Is that slowdown proportional to distance, or is something steeper going on?',
  whyItMatters:
      'Kepler found the pattern in planetary motion decades before Newton explained WHY it happens — and that pattern (T² ∝ r³) is one of the most quoted results in all of mechanics. It connects gravitation to orbital motion, underlies every satellite launched into geostationary orbit, and is a guaranteed numerical in both JEE and NEET. Once you can derive T²∝r³ from F=Gmm/r², you effectively own this entire chapter.',
  prediction: const PredictionPrompt(
    scenario:
        'Planet A orbits the Sun at distance r. Planet B orbits at 4r (four times farther). Compare their orbital periods T_A and T_B:',
    options: [
      'T_B = 4·T_A — period scales directly with distance',
      'T_B = 8·T_A — period scales as r^1.5',
      'T_B = 16·T_A — period scales as r²',
      'T_B = 2·T_A — period scales as √r',
    ],
    correctIndex: 1,
    reveal:
        'Kepler\'s third law says T² ∝ r³, so T ∝ r^1.5 (r to the power 3/2). Going from r to 4r means T scales by 4^1.5 = 8. In the lab, drag a planet out to 4× its orbital radius and watch its period readout climb to 8× — far steeper than the naive "farther means proportionally slower" guess, because gravity is also weaker out there, on top of the longer path length.',
  ),
  experiments: [
    'Set a planet at radius r and note its period, then move it to 4r and confirm the period increases by 8×',
    'Watch the swept-area indicator as a planet moves along an elliptical orbit — equal areas in equal times, even though speed changes',
    'Speed up a planet at perihelion (closest approach) vs aphelion (farthest) — see it move fastest when closest to the Sun',
    'Try a near-circular orbit vs a highly eccentric one at the same average radius — compare period behavior',
    'Drag a satellite to the geostationary radius and watch its period lock to 24 hours, matching Earth\'s rotation',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Before Newton explained gravity, Johannes Kepler found three empirical laws by painstakingly analysing decades of planetary position data. All three describe HOW planets move; none explain WHY — that had to wait for Newton\'s law of gravitation, which derives all three laws from F = Gm₁m₂/r².',
      title: 'Kepler\'s laws — patterns before the reason',
    ),
    ContentBlock.bullets([
      'First law (law of orbits): every planet moves in an ELLIPSE with the Sun at one focus, not a circle',
      'Second law (law of areas): the line joining a planet to the Sun sweeps out EQUAL AREAS in EQUAL TIMES',
      'Third law (law of periods): the square of the orbital period is proportional to the cube of the semi-major axis, T² ∝ r³',
    ], title: 'The three laws'),
    ContentBlock.formula('T² ∝ r³   (Kepler\'s third law)', title: 'THE LAW OF PERIODS'),
    ContentBlock.paragraph(
      'The second law is really a disguised statement of ANGULAR MOMENTUM CONSERVATION. Gravity acts along the line joining planet and Sun (a "central force"), so it produces zero torque about the Sun — angular momentum L = mvr sinθ stays constant throughout the orbit. Near perihelion the planet is close to the Sun (small r) so it must move faster (large v) to keep L constant; near aphelion it is far (large r) and moves slower.',
      title: 'Why the second law is angular momentum in disguise',
    ),
    ContentBlock.paragraph(
      'For orbits, gravity supplies exactly the centripetal force needed to keep the planet on its curved path. Setting the gravitational force equal to the required centripetal force, and using v = 2πr/T for a circular orbit, is the standard route to derive Kepler\'s third law from first principles — done step by step below.',
      title: 'From force to period',
    ),
    ContentBlock.realLife(
      'GPS satellites, weather satellites and communication satellites are all placed at radii chosen specifically using T² ∝ r³. A GEOSTATIONARY satellite is placed at the one radius (~42,164 km from Earth\'s centre) where T works out to exactly 24 hours — matching Earth\'s rotation, so the satellite appears to hang motionless over one point on the equator.',
    ),
    ContentBlock.mistake(
      'Assuming all orbits are circles. Kepler\'s FIRST law explicitly says orbits are ellipses; a circle is just the special case of zero eccentricity. Speed is NOT constant along an elliptical orbit — only the AREAL velocity (area swept per unit time) is constant.',
    ),
    ContentBlock.mistake(
      'Using T² ∝ r³ with r as the distance from the FOCUS at some instant, rather than the semi-major axis (the orbit\'s average radius). For circular orbits these coincide, so most exam numericals are safe, but conceptually the law uses the semi-major axis for elliptical orbits.',
    ),
    ContentBlock.example(
      'Earth orbits the Sun at radius 1 AU with period 1 year. A hypothetical planet orbits at 9 AU. Find its period.\n\nT² ∝ r³  →  (T_planet/T_earth)² = (r_planet/r_earth)³ = 9³ = 729\nT_planet/T_earth = √729 = 27\nT_planet = 27 years.\n\nA factor-of-9 increase in distance produces a factor-of-27 increase in period — the steepness of the r^1.5 scaling.',
    ),
    ContentBlock.jeeTip(
      'Master the standard derivation: equate gravitational force to centripetal force, Gm_sM/r² = m_sv²/r, substitute v = 2πr/T, and simplify to get T² = (4π²/GM)·r³. The constant 4π²/GM depends only on the CENTRAL mass M (e.g., the Sun) — every planet orbiting that same Sun obeys the same proportionality constant, which is exactly why T²/r³ is the same number for all planets in the solar system.',
    ),
    ContentBlock.neetNote(
      'NEET frequently asks for the orbital speed and period of geostationary or low-Earth satellites using v = √(GM/r) and T = 2πr/v = 2π√(r³/GM). Also remember: the total mechanical energy of an orbiting satellite is negative (E = −GMm/2r), signifying it is gravitationally bound to the central body.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Gravity provides the centripetal force for a circular orbit',
      math: 'G·M·m/r² = m·v²/r',
      note: 'M = mass of the central body (e.g. Sun), m = orbiting planet\'s mass, r = orbital radius.',
    ),
    DerivationStep(
      title: 'Cancel m and solve for orbital speed',
      math: 'v² = GM/r   →   v = √(GM/r)',
      note: 'Notice orbital speed depends only on M and r — NOT on the orbiting mass m.',
    ),
    DerivationStep(
      title: 'Express speed using the period of one revolution',
      math: 'v = 2πr/T',
      note: 'Circumference of the orbit divided by time for one full trip.',
    ),
    DerivationStep(
      title: 'Substitute and eliminate v',
      math: '(2πr/T)² = GM/r   →   4π²r²/T² = GM/r',
    ),
    DerivationStep(
      title: 'Rearrange to isolate T²',
      math: 'T² = (4π²/GM)·r³',
      note: 'This is Kepler\'s third law, T² ∝ r³, with the proportionality constant 4π²/GM fixed for all bodies orbiting the same M.',
    ),
  ],
  formulas: const [
    FormulaEntry('Kepler\'s third law', 'T² = (4π²/GM)·r³'),
    FormulaEntry('Orbital speed (circular orbit)', 'v = √(GM/r)'),
    FormulaEntry('Orbital period', 'T = 2π√(r³/GM)'),
    FormulaEntry('Areal velocity (2nd law)', 'dA/dt = L/(2m) = constant'),
    FormulaEntry('Total mechanical energy of orbit', 'E = −GMm/(2r)'),
    FormulaEntry('Gravitational PE in orbit', 'U = −GMm/r'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'Kepler\'s first law states that planetary orbits are:',
      options: ['Perfect circles', 'Ellipses with the Sun at one focus', 'Parabolas', 'Straight lines'],
      correctIndex: 1,
      solution: 'Kepler\'s law of orbits: every planet moves in an ellipse with the Sun at one of the two foci.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'A planet moves faster when it is:',
      options: ['Farthest from the Sun (aphelion)', 'Closest to the Sun (perihelion)', 'At constant speed throughout', 'Only at the semi-major axis point'],
      correctIndex: 1,
      solution: 'By Kepler\'s second law (equal areas in equal times, i.e. conserved angular momentum), a planet moves fastest when closest to the Sun.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'Two planets orbit the Sun with orbital radii in ratio 4:1. The ratio of their orbital periods is:',
      options: ['4:1', '8:1', '2:1', '16:1'],
      correctIndex: 1,
      solution: 'T ∝ r^1.5 (from T²∝r³). Ratio = 4^1.5 = 8. So T ratio = 8:1.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'The orbital speed of a satellite orbiting close to Earth\'s surface (radius R, surface gravity g) is best written as:',
      options: ['√(gR)', '√(2gR)', 'gR', '√(gR²)'],
      correctIndex: 0,
      solution: 'v = √(GM/r). Near the surface r≈R, and GM = gR², so v = √(gR²/R) = √(gR).',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'Kepler\'s second law (equal areas in equal times) is a direct consequence of:',
      options: [
        'Conservation of energy',
        'Conservation of angular momentum, since gravity is a central force',
        'Conservation of linear momentum',
        'Newton\'s third law only',
      ],
      correctIndex: 1,
      solution: 'Gravity acts along the Sun-planet line, producing zero torque about the Sun, so angular momentum L=mvr sinθ is conserved — this constancy IS the equal-areas law.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'A geostationary satellite must have an orbital period of exactly:',
      options: ['1 hour', '12 hours', '24 hours', '365 days'],
      correctIndex: 2,
      solution: 'A geostationary satellite must match Earth\'s rotation period (24 hours) so it appears stationary over a fixed point on the equator.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'The total mechanical energy of a satellite in a circular orbit of radius r around mass M is E = −GMm/2r. Doubling the orbital radius r changes the total energy to:',
      options: ['2E', 'E/2', '4E', 'E/4'],
      correctIndex: 1,
      solution: 'E ∝ 1/r. Doubling r halves the magnitude, so the new energy is E/2 (note E is negative, so the new value −GMm/4r is less negative — the satellite is less tightly bound, i.e. "closer to zero").',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A satellite of mass m orbits at radius r with speed v = √(GM/r). If its orbital radius is quadrupled, its orbital period becomes:',
      options: ['2T', '4T', '8T', '16T'],
      correctIndex: 2,
      solution: 'T ∝ r^1.5. Quadrupling r: factor = 4^1.5 = 8. New period = 8T.',
    ),
  ],
  revision: [
    'Kepler\'s 1st law: orbits are ellipses with the Sun at one focus, not circles.',
    'Kepler\'s 2nd law: equal areas swept in equal times — a disguised statement of angular momentum conservation.',
    'Kepler\'s 3rd law: T² ∝ r³, derived from Gmm/r² = mv²/r combined with v = 2πr/T.',
    'T² = (4π²/GM)r³ — the constant depends only on the central mass M, same for every orbiting body.',
    'Orbital speed v = √(GM/r) does not depend on the orbiting satellite\'s own mass.',
    'A planet moves fastest at perihelion (closest) and slowest at aphelion (farthest).',
    'Geostationary satellites sit at the one radius where T = 24 hours, matching Earth\'s rotation.',
  ],
  sandboxBuilder: (_) => const PlanetaryMotionSimulator(),
);
