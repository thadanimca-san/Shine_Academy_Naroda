import '../../models/lesson.dart';
import '../../simulators/torque_workbench_sim.dart';
import '../../theme/tokens.dart';

/// Torque — why WHERE you push matters just as much as how hard.
final Lesson torqueLesson = Lesson(
  topicId: 'torque',
  title: 'Torque',
  accentColor: Palette.chMechanics,
  bigQuestion:
      'Every door handle is placed as far from the hinges as possible, never right next to them. If the same muscular force opens the door either way, why does engineering bother putting the handle way over on the far edge?',
  whyItMatters:
      'Torque is the rotational equivalent of force — it is the missing piece needed to understand anything that turns, tips, balances, or spins: doors, spanners, see-saws, steering wheels, and the equilibrium of every rigid body you\'ll ever analyze in mechanics. JEE and NEET test it constantly through equilibrium problems (Στ = 0), and it is the direct doorway into angular momentum and rotational dynamics beyond this lesson.',
  prediction: const PredictionPrompt(
    scenario:
        'You apply the SAME force F to a wrench, first at a point close to the bolt (small distance r), then at a point far from the bolt (large distance r), always pushing perpendicular to the wrench. Compare the turning effect (torque) in the two cases:',
    options: [
      'Identical torque — force is what matters, not where you push',
      'Torque is larger when pushing closer to the bolt',
      'Torque is larger when pushing farther from the bolt',
      'Torque is zero unless you push exactly at the bolt',
    ],
    correctIndex: 2,
    reveal:
        'Torque τ = r·F·sinθ grows directly with the distance from the pivot (the "lever arm"), so pushing farther out with the same force produces MORE turning effect. In the lab, keep the applied force fixed and drag the application point outward along the wrench — watch the torque readout climb in direct proportion to the distance, exactly why long-handled wrenches make stubborn bolts easy.',
  ),
  experiments: [
    'Apply the same force at increasing distance from the pivot and watch torque grow linearly with r',
    'Change the angle between force and the lever arm and watch torque peak at 90° and vanish at 0°',
    'Apply two opposite forces off-axis (a couple) and observe the net force is zero but net torque is not',
    'Balance the see-saw by adjusting weights and distances until Στ = 0 and it stops rotating',
    'Push directly through the pivot point (r = 0 effectively) and see the torque readout drop to zero',
  ],
  concept: const [
    ContentBlock.paragraph(
      'A force can make an object rotate, and how effectively it does so depends on two things: how hard you push, and how far from the pivot (and at what angle) you push. Torque is the physical quantity that captures both — it is the rotational analog of force, the thing that changes angular velocity the way force changes linear velocity.',
      title: 'Torque: the turning effect of a force',
    ),
    ContentBlock.formula(
      'τ = r × F,   |τ| = rF sinθ',
      title: 'TORQUE (CROSS PRODUCT)',
    ),
    ContentBlock.bullets([
      'r is the position vector from the pivot to the point where the force is applied',
      'θ is the angle between r and F — torque is MAXIMUM when the force is perpendicular to r (θ = 90°)',
      'Torque is ZERO if the force acts along the line through the pivot (θ = 0° or 180°), or if r = 0',
      'Torque is a vector, perpendicular to both r and F, with direction given by the right-hand rule',
    ]),
    ContentBlock.paragraph(
      'The perpendicular distance from the pivot to the LINE OF ACTION of the force is called the lever arm (or moment arm), often written r⊥ = r·sinθ. Torque can equivalently be written as τ = F·r⊥ — force times lever arm. This is often the easier way to compute torque geometrically, without worrying about vector components.',
      title: 'Lever arm — the effective distance',
    ),
    ContentBlock.formula(
      'τ = F · r⊥,   r⊥ = r·sinθ',
      title: 'TORQUE VIA LEVER ARM',
    ),
    ContentBlock.realLife(
      'Door handles sit as far from the hinge as possible precisely to maximize the lever arm r⊥ — the same push force produces far more torque at the far edge than it would near the hinge, which is why pushing a door near its hinges feels so much harder to open even though your force hasn\'t changed.',
    ),
    ContentBlock.realLife(
      'A spanner (wrench) with a long handle lets a mechanic loosen a tight bolt with modest hand force, because torque = force × lever arm — a longer handle means the same force produces more torque. This is also why you\'re told to push perpendicular to the wrench handle, not at an angle: sinθ = 1 gives the maximum possible torque for a given force.',
    ),
    ContentBlock.mistake(
      'Computing torque as simply r×F without checking the angle θ, or assuming maximum distance always means maximum torque. If the force is applied ALONG the lever arm (pulling straight out, or pushing straight in toward the pivot), sinθ = 0 and torque is zero regardless of how far r is — direction matters as much as distance.',
    ),
    ContentBlock.mistake(
      'Forgetting sign conventions when several torques act on one body. Assign a positive direction (say, counter-clockwise) BEFORE summing; a force that would rotate the body clockwise contributes a NEGATIVE torque. Adding all torques as positive magnitudes gives a wrong equilibrium condition.',
    ),
    ContentBlock.example(
      'A force of 20 N is applied at the end of a spanner of length 0.3 m, at an angle of 30° to the spanner. Find the torque about the bolt.\n\nτ = rF sinθ = 0.3×20×sin30° = 0.3×20×0.5 = 3 N·m.\n\nNote the torque is far less than the maximum possible (0.3×20 = 6 N·m at 90°) — pushing at an angle wastes some of the turning effect.',
    ),
    ContentBlock.jeeTip(
      'For a rigid body in rotational equilibrium, BOTH conditions must hold: ΣF = 0 (translational equilibrium) AND Στ = 0 about ANY chosen point (rotational equilibrium). A powerful trick: choose your pivot point to pass through an unknown force\'s line of action — that force then contributes zero torque and drops out of the equation, often solving for the remaining unknown in one step.',
    ),
    ContentBlock.jeeTip(
      'A "couple" is a pair of equal, opposite, parallel forces NOT acting along the same line — their net FORCE is zero (so they cause no translation) but their net TORQUE is NOT zero (τ_couple = F·d, where d is the perpendicular distance between the two lines of action). Steering wheels and screwdrivers are turned by couples. Unlike torque about a point, a couple\'s torque is the same about ANY point.',
    ),
    ContentBlock.neetNote(
      'NEET frequently tests the see-saw / beam-balance style equilibrium problem: for a beam balanced about a pivot with two weights at different distances, set clockwise torque = anticlockwise torque (Στ = 0) directly — W₁r₁ = W₂r₂. Also remember torque has SI unit N·m, dimensionally the same as energy (joules) but conceptually different — never equate them.',
    ),
  ],
  derivation: const [
    DerivationStep(
      title: 'Define torque as the cross product of position and force',
      math: 'τ = r × F',
      note:
          'r is measured FROM the pivot/axis TO the point of application of F.',
    ),
    DerivationStep(
      title:
          'Expand the cross product magnitude using the angle between r and F',
      math: '|τ| = |r||F|sinθ = rF sinθ',
      note:
          'θ is the angle between the vectors r and F when placed tail to tail.',
    ),
    DerivationStep(
      title: 'Regroup the sinθ with r to define the lever arm',
      math: 'τ = F · (r sinθ) = F · r⊥',
      note:
          'r⊥ = r sinθ is the perpendicular distance from the pivot to the force\'s line of action.',
    ),
    DerivationStep(
      title: 'Apply the right-hand rule for direction',
      math:
          'Direction of τ ⟂ to both r and F (out of or into the plane of rotation)',
      note:
          'Curl fingers from r to F; thumb points along τ. This direction is also the axis about which the torque tends to rotate the body.',
    ),
    DerivationStep(
      title: 'State the equilibrium condition for a rigid body',
      math: 'ΣF = 0   AND   Στ = 0 (about any point)',
      note:
          'Both conditions are needed together — zero net force alone permits rotation (as in a couple); zero net torque alone permits sliding.',
    ),
  ],
  formulas: const [
    FormulaEntry('Torque (cross product)', 'τ = r × F,  |τ| = rF sinθ'),
    FormulaEntry(
      'Torque via lever arm',
      'τ = F · r⊥',
      condition: 'r⊥ = r sinθ, perpendicular distance to line of action',
    ),
    FormulaEntry(
      'Maximum torque',
      'τ_max = rF',
      condition: 'θ = 90°, force perpendicular to r',
    ),
    FormulaEntry(
      'Zero torque condition',
      'τ = 0',
      condition: 'θ = 0°/180° or r = 0',
    ),
    FormulaEntry(
      'Torque of a couple',
      'τ_couple = F · d',
      condition:
          'd = perpendicular distance between the two forces\' lines of action',
    ),
    FormulaEntry(
      'Rotational equilibrium',
      'Στ = 0',
      condition: 'about any chosen point, together with ΣF = 0',
    ),
  ],
  questions: const [
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'A force of 10 N is applied perpendicular to a rod at a distance of 0.5 m from the pivot. The torque is:',
      options: ['2 N·m', '5 N·m', '10 N·m', '20 N·m'],
      correctIndex: 1,
      solution: 'τ = rF sinθ = 0.5×10×sin90° = 5 N·m.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.basic,
      question:
          'Torque produced by a force acting exactly along the line joining it to the pivot is:',
      options: ['Maximum', 'Zero', 'Equal to rF', 'Cannot be determined'],
      correctIndex: 1,
      solution:
          'θ = 0° (or 180°), so sinθ = 0 and torque τ = rF sinθ = 0, regardless of the force magnitude.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'A see-saw balances with a 30 kg child sitting 2 m from the pivot and a 20 kg child on the other side. How far from the pivot must the 20 kg child sit for balance?',
      options: ['1.5 m', '2 m', '3 m', '4 m'],
      correctIndex: 2,
      solution: 'Στ = 0: 30×g×2 = 20×g×d → d = 60/20 = 3 m.',
    ),
    PracticeQuestion(
      track: ExamTrack.neet,
      difficulty: Difficulty.exam,
      question:
          'Why is it easier to loosen a tight bolt with a longer spanner?',
      options: [
        'A longer spanner reduces the force needed to overcome friction',
        'Torque = force × lever arm, so a longer handle gives more torque for the same force',
        'A longer spanner changes the direction of the applied force',
        'It has no real effect; it only feels easier',
      ],
      correctIndex: 1,
      solution:
          'τ = F·r⊥ — increasing the lever arm r⊥ while keeping F the same increases the torque delivered to the bolt.',
    ),
    PracticeQuestion(
      track: ExamTrack.both,
      difficulty: Difficulty.exam,
      question:
          'A force of 15 N acts on a wrench of length 0.4 m at an angle of 30° to the handle. The torque produced is:',
      options: ['1.5 N·m', '2 N·m', '3 N·m', '6 N·m'],
      correctIndex: 2,
      solution: 'τ = rF sinθ = 0.4×15×sin30° = 0.4×15×0.5 = 3 N·m.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.exam,
      question:
          'Two equal and opposite forces F act on a rigid body, separated by a perpendicular distance d, forming a couple. The net force and net torque are:',
      options: [
        'Net force = 2F, net torque = 0',
        'Net force = 0, net torque = Fd',
        'Net force = 0, net torque = 0',
        'Net force = F, net torque = Fd/2',
      ],
      correctIndex: 1,
      solution:
          'The two forces are equal and opposite, so they cancel in vector sum: net force = 0. But since they act along different (parallel) lines, they produce a net torque τ = F×d about any point.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A uniform rod of length L and weight W is held horizontal, pivoted at one end, and supported by a vertical string attached at the other end. The tension in the string is:',
      options: ['W', 'W/2', '2W', 'W/4'],
      correctIndex: 1,
      solution:
          'Taking torques about the pivot: weight W acts at the center (L/2 from pivot), tension T acts at the far end (L from pivot). Στ = 0: T·L = W·(L/2) → T = W/2.',
    ),
    PracticeQuestion(
      track: ExamTrack.jee,
      difficulty: Difficulty.advanced,
      question:
          'A ladder of weight W leans against a smooth (frictionless) wall, with its base on a rough floor. Taking torques about the base of the ladder to find the normal force from the wall, which forces contribute ZERO torque about that point?',
      options: [
        'The weight of the ladder',
        'The normal force from the wall',
        'The normal force from the floor AND the friction force from the floor (both act at the pivot point)',
        'None of the forces contribute zero torque',
      ],
      correctIndex: 2,
      solution:
          'Choosing the base of the ladder as the pivot makes r = 0 for any force acting exactly at that point — both the floor\'s normal force and its friction force act there, so they contribute zero torque, leaving an equation relating only the wall\'s normal force and the ladder\'s weight. This is the standard "choose the pivot to eliminate unknowns" trick.',
    ),
  ],
  revision: [
    'τ = r × F, magnitude rF sinθ — torque depends on force, distance from pivot, AND the angle between them.',
    'Maximum torque occurs when force is perpendicular to the lever arm (θ = 90°); zero when force acts along it.',
    'Lever arm r⊥ = r sinθ is the perpendicular distance from the pivot to the force\'s line of action.',
    'Rigid body equilibrium needs BOTH ΣF = 0 and Στ = 0 (about any point) — neither alone is sufficient.',
    'A couple (equal, opposite, non-collinear forces) has zero net force but nonzero, position-independent torque.',
    'Choosing the pivot at an unknown force\'s point of application eliminates it from the torque equation.',
    'Longer lever arms (long wrenches, far door handles) multiply the turning effect of the same applied force.',
  ],
  sandboxBuilder: (_) => const TorqueWorkbenchSimulator(),
);
