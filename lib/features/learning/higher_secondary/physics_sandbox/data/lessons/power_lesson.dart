import '../../models/lesson.dart';
import '../../simulators/power_sandbox.dart';
import '../../theme/tokens.dart';

/// Power — the rate at which work gets done, and why engines are rated in kW, not just N.
final Lesson powerLesson = Lesson(
  topicId: 'power',
  title: 'Power',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'A small motorbike and a truck can both, eventually, drag the same heavy load up the same hill. So why does only the truck get an engine rated in hundreds of horsepower — if the FORCE needed is the same, what is the extra power actually paying for?',
  whyItMatters:
      'Power is the bridge between "how much work gets done" and "how fast." It is a deceptively short topic — one formula, P=Fv — but it appears constantly disguised inside pulley problems, incline problems, pump/motor problems, and real-world engineering questions about efficiency. JEE loves multi-step problems where you must first find force from Newton\'s laws, THEN multiply by velocity to get power; NEET loves direct-recall unit conversions (horsepower, kilowatt-hour).',
  prediction: const PredictionPrompt(
    scenario:
        'A car climbs a slope at a CONSTANT speed v, so its net force is zero (drive force exactly balances gravity + friction). If you double the speed v while keeping the same slope and friction, the engine\'s power output:',
    options: [
      'Stays exactly the same, since the force needed hasn\'t changed',
      'Doubles, since P = Fv and F is unchanged',
      'Quadruples, since power depends on v²',
      'Drops to half, since less time is spent on the slope',
    ],
    correctIndex: 1,
    reveal:
        'Because the car moves at constant speed, the required drive force F = mg sinθ + f does NOT depend on v at all — only on mass, slope and friction. But power P = Fv is directly proportional to v, so doubling the speed exactly doubles the power needed, even though the force stays fixed. In the lab, push the speed slider up and watch the drive-force meter stay put while the power meter climbs in lock-step.',
  ),
  experiments: [
    'Raise the speed slider and watch power rise in direct proportion, while the drive-force meter barely moves',
    'Increase the slope angle and see the drive force jump (more of gravity opposes the climb) — power rises too',
    'Set friction to its maximum and note power increases even on a flat road (θ=0) just to overcome resistance',
    'Increase mass and see the drive force needed for the same slope grow directly with m',
    'Compare average power (accumulated work / time) to instantaneous power at steady speed — they converge once climbing settles into a steady state',
  ],
  concept: const [
    ContentBlock.paragraph(
      'Power is the rate at which work is done, or equivalently the rate at which energy is transferred. Two machines can do the exact same amount of work, but the one that finishes faster has delivered more power. Average power over a time interval is simply total work divided by total time; instantaneous power is the power at one particular moment.',
      title: 'Power: work per unit time',
    ),
    ContentBlock.formula('P_avg = W/t          P_inst = dW/dt = F·v·cosθ', title: 'AVERAGE AND INSTANTANEOUS POWER'),
    ContentBlock.bullets([
      'θ is the angle between the force F and the velocity v',
      'If F acts exactly along the direction of motion, P = Fv (cosθ = 1)',
      'If F is perpendicular to velocity (like the centripetal force in circular motion), it does zero work and delivers zero power',
      'Power is a scalar — it has no direction, even though it is built from two vectors',
    ]),
    ContentBlock.paragraph(
      'A vehicle climbing a slope at CONSTANT speed has zero net force (Newton\'s first law: no acceleration means no net force). The engine\'s drive force must therefore exactly balance the two forces opposing motion: the component of gravity along the slope, and friction/air resistance.',
      title: 'Power on an incline — the classic vehicle problem',
    ),
    ContentBlock.formula('F_drive = mg sinθ + f          P = F_drive · v = (mg sinθ + f)·v', title: 'POWER CLIMBING A SLOPE'),
    ContentBlock.paragraph(
      'The SI unit of power is the watt (W = J/s = kg·m²/s³). For everyday engines the kilowatt (kW = 1000 W) is more convenient, and older or informal ratings still use horsepower, where 1 hp ≈ 746 W. A "kilowatt-hour" (kWh), despite its name, is a unit of ENERGY, not power — it is the energy delivered by a 1 kW device running for 1 hour (3.6×10⁶ J), and it is exactly what your electricity bill charges for.',
      title: 'Units: watt, kilowatt, horsepower, kilowatt-hour',
    ),
    ContentBlock.realLife(
      'This is exactly why vehicle engines are rated in kW/horsepower rather than just newtons of force: force alone tells you how heavy a load you can move, but power tells you how FAST you can move it. A small vehicle can drag an enormous crate given enough time (force is what matters for that), but only a high-power engine can drag it up a hill quickly — power is what buys you speed against resistance.',
    ),
    ContentBlock.paragraph(
      'Real machines never convert 100% of input power into useful output — some is always lost to friction, heat, or vibration. Efficiency compares what you get out to what you put in.',
      title: 'Efficiency: not all power is useful',
    ),
    ContentBlock.formula('η = P_output / P_input × 100%', title: 'EFFICIENCY'),
    ContentBlock.realLife(
      'An incandescent bulb converts only about 2-3% of its electrical input power into visible light (the rest becomes heat) — an LED bulb reaches far higher efficiency, which is why it needs much less input power for the same brightness. Electric motors typically reach 80-90% efficiency, while a car engine burning petrol wastes most of its input power as heat, rarely exceeding 30-40% efficiency.',
    ),
    ContentBlock.mistake(
      'Assuming that because a machine can exert a huge force, it must also be "powerful." A hand-cranked hydraulic jack can lift a car (huge force) but takes minutes to do it (tiny power); a small motor spinning a fan blade quickly can deliver more power despite exerting far less force. Power depends on BOTH force and speed together.',
    ),
    ContentBlock.mistake(
      'Forgetting the cosθ factor when force and velocity are not aligned. If a force is applied at an angle to the direction of motion, only the component of force ALONG the velocity contributes to power — the perpendicular component contributes nothing.',
    ),
    ContentBlock.example(
      'A car of mass 1200 kg climbs a slope of 5° at a constant speed of 15 m/s. Friction and air resistance together total 300 N. Find the power delivered by the engine (g = 10 m/s²).\n\nF_drive = mg sinθ + f = 1200×10×sin5° + 300 ≈ 1200×10×0.0872 + 300 ≈ 1046.4 + 300 = 1346.4 N\nP = F_drive × v = 1346.4 × 15 ≈ 20196 W ≈ 20.2 kW (about 27 hp).',
    ),
    ContentBlock.jeeTip(
      'When a body accelerates (not constant speed), the instantaneous power still equals Fv, but F now includes the ma term too — remember to find the NET force from Newton\'s second law first (including any acceleration), THEN multiply by the instantaneous velocity, which itself may be changing.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests direct unit-conversion recall: 1 hp = 746 W, 1 kWh = 3.6×10⁶ J. Also remember the alternate power formula for rotational systems, P = τω (torque times angular velocity) — the rotational analogue of P = Fv, useful for motors and turbines.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Start from the definition of work done by a force',
      math: 'dW = F·dx = F cosθ · dx',
      note: 'θ is the angle between the constant force F and the small displacement dx.',
    ),
    DerivationStep(
      title: 'Divide both sides by the time interval dt',
      math: 'dW/dt = F cosθ · (dx/dt)',
    ),
    DerivationStep(
      title: 'Recognise dx/dt as the instantaneous speed',
      math: 'P = F cosθ · v = F·v·cosθ',
      note: 'When F is entirely along the direction of motion, this simplifies to P = Fv.',
    ),
    DerivationStep(
      title: 'Apply to a vehicle at constant speed on a slope',
      math: 'Net force = 0 ⟹ F_drive = mg sinθ + f',
      note: 'From Newton\'s first law: zero acceleration means the drive force exactly cancels gravity\'s slope-component and resistive forces.',
    ),
    DerivationStep(
      title: 'Multiply by speed to get the engine\'s power output',
      math: 'P = (mg sinθ + f)·v',
      note: 'This is the power the engine must continuously deliver to maintain that constant climbing speed.',
    ),
  ],
  formulas: const [
    FormulaEntry('Average power', 'P_avg = W/t'),
    FormulaEntry('Instantaneous power', 'P = F·v·cosθ'),
    FormulaEntry('Power (force along motion)', 'P = Fv'),
    FormulaEntry('Vehicle climbing a slope at constant speed', 'P = (mg sinθ + f)·v'),
    FormulaEntry('Rotational power', 'P = τ·ω', condition: 'rotational analogue of P = Fv'),
    FormulaEntry('Efficiency', 'η = P_output/P_input × 100%'),
    FormulaEntry('Unit conversions', '1 hp ≈ 746 W,   1 kWh = 3.6×10⁶ J'),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question: 'The SI unit of power is:',
      options: ['Joule', 'Newton', 'Watt', 'Joule-second'],
      correctIndex: 2,
      solution: 'Power = work/time = joule/second = watt (W).',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.basic,
      question: 'A "kilowatt-hour" is a unit of:',
      options: ['Power', 'Force', 'Energy', 'Momentum'],
      correctIndex: 2,
      solution: 'Despite the name including "power" (kilowatt), a kilowatt-HOUR is power × time = energy: 1 kWh = 1000 W × 3600 s = 3.6×10⁶ J.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A crane lifts a 500 kg load at a constant speed of 2 m/s. The power delivered by the crane\'s motor is (g=10 m/s²):',
      options: ['1000 W', '5000 W', '10000 W', '2500 W'],
      correctIndex: 2,
      solution: 'At constant speed, lifting force = weight = mg = 500×10 = 5000 N. P = Fv = 5000×2 = 10000 W.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question: 'A force of 20 N acts on a body at an angle of 60° to its direction of motion, which proceeds at 5 m/s. The power delivered by this force is:',
      options: ['100 W', '86.6 W', '50 W', '10 W'],
      correctIndex: 2,
      solution: 'P = Fv cosθ = 20 × 5 × cos60° = 100 × 0.5 = 50 W.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question: 'A car climbs a slope at constant speed. If the speed is doubled (same slope, same friction), the power required:',
      options: ['Stays the same', 'Doubles', 'Quadruples', 'Halves'],
      correctIndex: 1,
      solution: 'At constant speed the drive force F = mg sinθ + f is independent of v. Since P = Fv, doubling v with F unchanged exactly doubles P.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question: 'An engine rated at 74.6 kW is approximately equal to how many horsepower?',
      options: ['10 hp', '74.6 hp', '100 hp', '746 hp'],
      correctIndex: 2,
      solution: '1 hp ≈ 746 W, so 74.6 kW = 74600 W ÷ 746 W/hp = 100 hp.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A body of mass m, starting from rest, is acted on by a constant force F along a frictionless surface. The instantaneous power delivered by F as a function of time t is:',
      options: ['P = F²t/m', 'P = Fmt', 'P = F²t²/m', 'P = Ft/m²'],
      correctIndex: 0,
      solution: 'a = F/m (constant), so v = at = Ft/m. Instantaneous power P = Fv = F×(Ft/m) = F²t/m — power grows linearly with time under constant force from rest.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question: 'A pump lifts water from a well 10 m deep and delivers it at 2 m/s through a pipe, pumping 50 kg of water every second. Total power delivered by the pump is closest to (g=10 m/s², ignore pipe friction):',
      options: ['5000 W', '5100 W', '5600 W', '6000 W'],
      correctIndex: 1,
      solution: 'Power = rate of gain of PE + rate of gain of KE. PE rate = (dm/dt)·g·h = 50×10×10 = 5000 W. KE rate = ½(dm/dt)v² = ½×50×2² = 100 W. Total ≈ 5100 W.',
    ),
  ],
  revision: [
    'Power = rate of doing work: P_avg = W/t, P_inst = Fv cosθ, reducing to P = Fv when force and velocity are aligned.',
    'A vehicle climbing at constant speed has zero net force: F_drive = mg sinθ + f, so P = (mg sinθ + f)v.',
    'At constant climbing speed, power is directly proportional to speed even though the drive force itself does not change with v.',
    'Units: 1 watt = 1 J/s; 1 hp ≈ 746 W; 1 kWh = 3.6×10⁶ J (a kWh is ENERGY, not power).',
    'Engines are rated in power, not force, because power tells you how fast work can be done against resistance — force alone only tells you what load can be moved.',
    'Efficiency η = P_output/P_input; real machines always lose some power to heat and friction, so η < 100%.',
    'Rotational analogue: P = τω, exactly parallel to P = Fv for translational motion.',
  ],
  sandboxBuilder: (_) => const PowerSandbox(),
);
