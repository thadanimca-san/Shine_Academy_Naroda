import 'package:flutter/material.dart';

import '../models/syllabus.dart';
import '../screens/sandbox_screen.dart';
import '../widgets/lesson/lesson_screen.dart';

// ── Lesson data ──────────────────────────────────────────────────────────────
import 'lessons/elasticity_lesson.dart';
import 'lessons/fluid_mechanics_lesson.dart';
import 'lessons/surface_tension_lesson.dart';
import 'lessons/em_waves_lesson.dart';
import 'lessons/measuring_instruments_lesson.dart';
import 'lessons/magnetism_matter_lesson.dart';
import 'lessons/units_dimensions_lesson.dart';
import 'lessons/vectors_lesson.dart';
import 'lessons/motion_1d_lesson.dart';
import 'lessons/motion_2d_lesson.dart';
import 'lessons/relative_motion_lesson.dart';
import 'lessons/collisions_lesson.dart';
import 'lessons/coulombs_law_lesson.dart';
import 'lessons/electric_field_lesson.dart';
import 'lessons/capacitors_lesson.dart';
import 'lessons/magnetic_force_lesson.dart';
import 'lessons/interference_lesson.dart';
import 'lessons/first_law_lesson.dart';
import 'lessons/second_law_lesson.dart';
import 'lessons/third_law_lesson.dart';
import 'lessons/friction_lesson.dart';
import 'lessons/inclined_plane_lesson.dart';
import 'lessons/pulley_lesson.dart';
import 'lessons/energy_lesson.dart';
import 'lessons/work_energy_theorem_lesson.dart';
import 'lessons/pendulum_energy_lesson.dart';
import 'lessons/momentum_impulse_lesson.dart';
import 'lessons/rotational_kinematics_lesson.dart';
import 'lessons/torque_lesson.dart';
import 'lessons/moment_inertia_lesson.dart';
import 'lessons/rolling_motion_lesson.dart';
import 'lessons/gravitation_lesson.dart';
import 'lessons/planetary_orbits_lesson.dart';
import 'lessons/escape_velocity_lesson.dart';
import 'lessons/variation_of_g_lesson.dart';
import 'lessons/shm_lesson.dart';
import 'lessons/shm_duel_lesson.dart';
import 'lessons/wave_basics_lesson.dart';
import 'lessons/standing_waves_lesson.dart';
import 'lessons/heat_transfer_lesson.dart';
import 'lessons/calorimetry_lesson.dart';
import 'lessons/gas_laws_lesson.dart';
import 'lessons/thermo_processes_lesson.dart';
import 'lessons/heat_engines_lesson.dart';
import 'lessons/capacitor_networks_lesson.dart';
import 'lessons/charge_in_field_lesson.dart';
import 'lessons/reflection_mirrors_lesson.dart';
import 'lessons/refraction_lesson.dart';
import 'lessons/semiconductor_diodes_lesson.dart';
import 'lessons/logic_gates_lesson.dart';
import 'lessons/circular_motion_lesson.dart';
import 'lessons/pseudo_forces_lesson.dart';
import 'lessons/power_lesson.dart';
import 'lessons/center_of_mass_lesson.dart';
import 'lessons/angular_momentum_lesson.dart';
import 'lessons/damped_forced_lesson.dart';
import 'lessons/superposition_beats_lesson.dart';
import 'lessons/doppler_effect_lesson.dart';
import 'lessons/sound_waves_lesson.dart';
import 'lessons/thermal_expansion_lesson.dart';
import 'lessons/kinetic_theory_lesson.dart';
import 'lessons/entropy_lesson.dart';
import 'lessons/electric_potential_lesson.dart';
import 'lessons/gauss_law_lesson.dart';
import 'lessons/ohms_law_drift_lesson.dart';
import 'lessons/kirchhoff_laws_lesson.dart';
import 'lessons/heating_effect_lesson.dart';
import 'lessons/meter_bridge_lesson.dart';
import 'lessons/biot_savart_lesson.dart';
import 'lessons/ampere_solenoid_lesson.dart';
import 'lessons/faraday_lenz_lesson.dart';
import 'lessons/ac_circuits_lesson.dart';
import 'lessons/transformers_lesson.dart';
import 'lessons/lenses_lesson.dart';
import 'lessons/prism_dispersion_lesson.dart';
import 'lessons/optical_instruments_lesson.dart';
import 'lessons/diffraction_lesson.dart';
import 'lessons/polarization_lesson.dart';
import 'lessons/photoelectric_effect_lesson.dart';
import 'lessons/bohr_model_lesson.dart';
import 'lessons/nuclear_physics_lesson.dart';
import 'lessons/radioactivity_lesson.dart';
import 'lessons/communication_systems_lesson.dart';

// ── Mechanics simulators (not yet wrapped in a full lesson) ────────────────────
import '../simulators/satellite_motion_sandbox.dart';

/// The complete JEE + NEET physics syllabus map.
///
/// Every topic in the target syllabus is listed here — available ones carry a
/// builder, the rest are visible as "coming soon" so students always see the
/// full journey and can learn in whatever order they choose.
final List<Chapter> syllabus = [
  // ─────────────────────────── MECHANICS ───────────────────────────
  Chapter(
    id: 'foundations',
    title: 'Foundations',
    unit: 'Mechanics',
    icon: Icons.straighten,
    tint: const Color(0xFF6366F1),
    topics: [
      Topic(
        id: 'units-dimensions',
        title: 'Units & Dimensions',
        tagline: 'Why every formula must balance its units',
        icon: Icons.square_foot,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: unitsDimensionsLesson),
      ),
      Topic(
        id: 'vectors',
        title: 'Vectors',
        tagline: 'Add, resolve and multiply arrows like a physicist',
        icon: Icons.call_made,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: vectorsLesson),
      ),
    ],
  ),
  Chapter(
    id: 'kinematics',
    title: 'Kinematics',
    unit: 'Mechanics',
    icon: Icons.speed,
    tint: const Color(0xFF4F46E5),
    topics: [
      Topic(
        id: 'motion-1d',
        title: 'Motion in a Straight Line',
        tagline: 'Position, velocity and acceleration — the language of motion',
        icon: Icons.linear_scale,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: motion1dLesson),
      ),
      Topic(
        id: 'projectile-motion',
        title: 'Projectile Motion',
        tagline: 'Launch, watch the parabola, discover the 45° secret',
        icon: Icons.moving,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: motion2dLesson),
      ),
      Topic(
        id: 'relative-motion',
        title: 'Relative Motion',
        tagline: 'Rivers, rain and moving trains — motion depends on who watches',
        icon: Icons.directions_boat,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: relativeMotionLesson),
      ),
      Topic(
        id: 'circular-motion',
        title: 'Circular Motion',
        tagline: 'Why turning needs a force even at constant speed',
        icon: Icons.rotate_right,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: circularMotionLesson),
      ),
    ],
  ),
  Chapter(
    id: 'laws-of-motion',
    title: 'Laws of Motion',
    unit: 'Mechanics',
    icon: Icons.open_with,
    tint: const Color(0xFF7C3AED),
    topics: [
      Topic(
        id: 'newton-first-law',
        title: "Newton's First Law",
        tagline: 'Inertia — why things keep doing what they were doing',
        icon: Icons.trending_flat,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: newtonFirstLawLesson),
      ),
      Topic(
        id: 'newton-second-law',
        title: "Newton's Second Law",
        tagline: 'F = ma, tested live with your own numbers',
        icon: Icons.unfold_more,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: newtonSecondLawLesson),
      ),
      Topic(
        id: 'newton-third-law',
        title: "Newton's Third Law",
        tagline: 'Every push pushes back — see momentum stay conserved',
        icon: Icons.sync_alt,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: newtonThirdLawLesson),
      ),
      Topic(
        id: 'friction',
        title: 'Friction',
        tagline: 'The force that resists — until the block breaks free',
        icon: Icons.texture,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: frictionLesson),
      ),
      Topic(
        id: 'inclined-plane',
        title: 'Inclined Plane',
        tagline: 'Split gravity into components on a tilting ramp',
        icon: Icons.change_history,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: inclinedPlaneLesson),
      ),
      Topic(
        id: 'pulleys',
        title: 'Pulley Systems',
        tagline: 'Atwood machines — tension, acceleration and clever tricks',
        icon: Icons.layers,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: pulleyLesson),
      ),
      Topic(
        id: 'pseudo-forces',
        title: 'Pseudo Forces',
        tagline: 'Physics inside an accelerating lift or car',
        icon: Icons.elevator,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: pseudoForcesLesson),
      ),
    ],
  ),
  Chapter(
    id: 'work-energy-power',
    title: 'Work, Energy & Power',
    unit: 'Mechanics',
    icon: Icons.bolt,
    tint: const Color(0xFFD97706),
    topics: [
      Topic(
        id: 'energy-transformations',
        title: 'Energy Transformations',
        tagline: 'Watch kinetic and potential energy trade places',
        icon: Icons.swap_vert,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: energyTransformationsLesson),
      ),
      Topic(
        id: 'work-energy-theorem',
        title: 'Work–Energy Theorem',
        tagline: 'Net work done equals the change in kinetic energy',
        icon: Icons.analytics_outlined,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: workEnergyTheoremLesson),
      ),
      Topic(
        id: 'pendulum-energy',
        title: 'Pendulum Energy',
        tagline: 'A swinging bob is an energy conversation with gravity',
        icon: Icons.swap_calls,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: pendulumEnergyLesson),
      ),
      Topic(
        id: 'power',
        title: 'Power',
        tagline: 'How fast is the work being done?',
        icon: Icons.flash_on,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: powerLesson),
      ),
    ],
  ),
  Chapter(
    id: 'momentum-collisions',
    title: 'Momentum & Collisions',
    unit: 'Mechanics',
    icon: Icons.sports_mma,
    tint: const Color(0xFFDB2777),
    topics: [
      Topic(
        id: 'momentum-impulse',
        title: 'Momentum & Impulse',
        tagline: 'Why a cricketer pulls their hands back while catching',
        icon: Icons.sports_cricket,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: momentumImpulseLesson),
      ),
      Topic(
        id: 'collisions',
        title: 'Collisions',
        tagline: 'Elastic vs inelastic — crash carts and conserve momentum',
        icon: Icons.compare_arrows,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: collisionsLesson),
      ),
      Topic(
        id: 'center-of-mass',
        title: 'Center of Mass',
        tagline: 'The one point that moves as if it were the whole body',
        icon: Icons.adjust,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: centerOfMassLesson),
      ),
    ],
  ),
  Chapter(
    id: 'rotational-motion',
    title: 'Rotational Motion',
    unit: 'Mechanics',
    icon: Icons.autorenew,
    tint: const Color(0xFF0891B2),
    topics: [
      Topic(
        id: 'rotational-dynamics',
        title: 'Rotational Kinematics',
        tagline: 'ω and α — the spinning twins of v and a',
        icon: Icons.autorenew,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: rotationalKinematicsLesson),
      ),
      Topic(
        id: 'torque',
        title: 'Torque',
        tagline: 'Why door handles are far from the hinge',
        icon: Icons.build_circle_outlined,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: torqueLesson),
      ),
      Topic(
        id: 'moment-of-inertia',
        title: 'Moment of Inertia',
        tagline: 'Same mass, different shape — different laziness to spin',
        icon: Icons.donut_large,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: momentInertiaLesson),
      ),
      Topic(
        id: 'rolling-motion',
        title: 'Rolling Motion',
        tagline: 'Rolling = spinning + sliding, perfectly synchronized',
        icon: Icons.circle_outlined,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: rollingMotionLesson),
      ),
      Topic(
        id: 'angular-momentum',
        title: 'Angular Momentum',
        tagline: 'Why ice skaters spin faster with arms pulled in',
        icon: Icons.cyclone,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: angularMomentumLesson),
      ),
    ],
  ),
  Chapter(
    id: 'gravitation',
    title: 'Gravitation',
    unit: 'Mechanics',
    icon: Icons.public,
    tint: const Color(0xFF2563EB),
    topics: [
      Topic(
        id: 'universal-gravitation',
        title: 'Universal Gravitation',
        tagline: 'The inverse-square law that runs the universe',
        icon: Icons.public,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: gravitationLesson),
      ),
      Topic(
        id: 'planetary-orbits',
        title: 'Planetary Orbits',
        tagline: "Kepler's laws — ellipses, equal areas, harmonic periods",
        icon: Icons.wb_sunny_outlined,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: planetaryOrbitsLesson),
      ),
      Topic(
        id: 'escape-velocity',
        title: 'Escape Velocity',
        tagline: 'How fast must you throw so it never comes back?',
        icon: Icons.rocket_launch_outlined,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: escapeVelocityLesson),
      ),
      Topic(
        id: 'variation-of-g',
        title: 'Variation of g',
        tagline: 'g changes with height, depth and even latitude',
        icon: Icons.blur_circular,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: variationOfGLesson),
      ),
      Topic(
        id: 'satellite-motion',
        title: 'Satellite Motion',
        tagline: 'Orbital speed, time period and geostationary satellites',
        icon: Icons.satellite_alt,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => const SandboxScreen(title: 'Satellite Motion', child: SatelliteMotionSandbox()),
      ),
    ],
  ),
  Chapter(
    id: 'oscillations',
    title: 'Oscillations (SHM)',
    unit: 'Mechanics',
    icon: Icons.waves,
    tint: const Color(0xFF9333EA),
    topics: [
      Topic(
        id: 'shm-basics',
        title: 'SHM & Spring–Mass',
        tagline: 'The restoring force that makes the world vibrate',
        icon: Icons.vibration,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: shmLesson),
      ),
      Topic(
        id: 'shm-duel',
        title: 'Spring vs Pendulum',
        tagline: 'Two oscillators, one duel — what controls the period?',
        icon: Icons.hourglass_empty,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: shmDuelLesson),
      ),
      Topic(
        id: 'damped-forced',
        title: 'Damping & Resonance',
        tagline: 'Why soldiers break step on bridges',
        icon: Icons.graphic_eq,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: dampedForcedLesson),
      ),
    ],
  ),
  Chapter(
    id: 'waves',
    title: 'Waves',
    unit: 'Mechanics',
    icon: Icons.water,
    tint: const Color(0xFF0D9488),
    topics: [
      Topic(
        id: 'wave-basics',
        title: 'Wave Motion Basics',
        tagline: 'Wavelength, frequency and speed — read a wave like a graph',
        icon: Icons.show_chart,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: waveBasicsLesson),
      ),
      Topic(
        id: 'standing-waves',
        title: 'Standing Waves',
        tagline: 'Nodes, antinodes and harmonics on a vibrating string',
        icon: Icons.waves,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: standingWavesLesson),
      ),
      Topic(
        id: 'superposition-beats',
        title: 'Superposition & Beats',
        tagline: 'When two waves meet: add, cancel, or wobble',
        icon: Icons.stacked_line_chart,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: superpositionBeatsLesson),
      ),
      Topic(
        id: 'doppler-effect',
        title: 'Doppler Effect',
        tagline: 'Why a passing siren drops in pitch',
        icon: Icons.emergency,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: dopplerEffectLesson),
      ),
      Topic(
        id: 'sound-waves',
        title: 'Sound Waves',
        tagline: 'Pressure waves, intensity and organ pipes',
        icon: Icons.volume_up,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: soundWavesLesson),
      ),
    ],
  ),

  Chapter(
    id: 'properties-of-matter',
    title: 'Properties of Bulk Matter',
    unit: 'Properties of Matter',
    icon: Icons.water,
    tint: const Color(0xFF0EA5E9),
    topics: [
      Topic(
        id: 'elasticity',
        title: 'Elasticity & Hooke\'s Law',
        tagline: 'Stress, strain, and why things bounce back',
        icon: Icons.compress,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: elasticityLesson),
      ),
      Topic(
        id: 'fluid-mechanics',
        title: 'Fluid Mechanics',
        tagline: 'Archimedes, Bernoulli, and the flow of liquids',
        icon: Icons.water,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: fluidMechanicsLesson),
      ),
      Topic(
        id: 'surface-tension',
        title: 'Surface Tension',
        tagline: 'Why water drops are round',
        icon: Icons.bubble_chart,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: surfaceTensionLesson),
      ),
    ],
  ),

  // ─────────────────────── THERMAL PHYSICS ────────────────────────
  Chapter(
    id: 'heat-temperature',
    title: 'Heat & Temperature',
    unit: 'Thermal Physics',
    icon: Icons.thermostat,
    tint: const Color(0xFFDC2626),
    topics: [
      Topic(
        id: 'heat-transfer',
        title: 'Heat Transfer',
        tagline: "Conduction, convection, radiation — Fourier's law live",
        icon: Icons.device_thermostat,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: heatTransferLesson),
      ),
      Topic(
        id: 'calorimetry',
        title: 'Calorimetry',
        tagline: 'Mix hot and cold — predict the final temperature',
        icon: Icons.science_outlined,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: calorimetryLesson),
      ),
      Topic(
        id: 'thermal-expansion',
        title: 'Thermal Expansion',
        tagline: 'Why railway tracks leave gaps',
        icon: Icons.open_in_full,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: thermalExpansionLesson),
      ),
    ],
  ),
  Chapter(
    id: 'thermodynamics',
    title: 'Gases & Thermodynamics',
    unit: 'Thermal Physics',
    icon: Icons.local_fire_department,
    tint: const Color(0xFFEA580C),
    topics: [
      Topic(
        id: 'gas-laws',
        title: 'Ideal Gas Laws',
        tagline: 'Boyle, Charles and Gay-Lussac in one piston',
        icon: Icons.blur_on,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: gasLawsLesson),
      ),
      Topic(
        id: 'kinetic-theory',
        title: 'Kinetic Theory',
        tagline: 'Temperature is just molecules in a hurry',
        icon: Icons.scatter_plot,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: kineticTheoryLesson),
      ),
      Topic(
        id: 'thermo-processes',
        title: 'Thermodynamic Processes',
        tagline: 'Isothermal vs adiabatic on a live P-V diagram',
        icon: Icons.show_chart,
        status: TopicStatus.available,
        highYield: true,
        builder: (_) => LessonScreen(lesson: thermoProcessesLesson),
      ),
      Topic(
        id: 'heat-engines',
        title: 'Heat Engines',
        tagline: 'Carnot efficiency — why no engine can be perfect',
        icon: Icons.local_fire_department_outlined,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: heatEnginesLesson),
      ),
      Topic(
        id: 'entropy',
        title: 'Entropy & Second Law',
        tagline: "The universe's one-way street",
        icon: Icons.shuffle,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: entropyLesson),
      ),
    ],
  ),

  // ──────────────────── ELECTRICITY & MAGNETISM ────────────────────
  Chapter(
    id: 'electrostatics',
    title: 'Electrostatics',
    unit: 'Electricity & Magnetism',
    icon: Icons.flash_on,
    tint: const Color(0xFFCA8A04),
    topics: [
      Topic(
        id: 'coulombs-law',
        title: "Charges & Coulomb's Law",
        tagline: 'The electric twin of gravitation — but a trillion times stronger',
        icon: Icons.add_circle_outline,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: coulombsLawLesson),
      ),
      Topic(
        id: 'electric-field',
        title: 'Electric Field',
        tagline: 'Drag charges around and watch field lines bend',
        icon: Icons.grain,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: electricFieldLesson),
      ),
      Topic(
        id: 'electric-potential',
        title: 'Electric Potential',
        tagline: 'Energy landscapes and equipotential contours',
        icon: Icons.terrain,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: electricPotentialLesson),
      ),
      Topic(
        id: 'gauss-law',
        title: "Gauss's Law",
        tagline: 'Count field lines through a closed surface',
        icon: Icons.all_out,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: gaussLawLesson),
      ),
    ],
  ),
  Chapter(
    id: 'capacitance',
    title: 'Capacitance',
    unit: 'Electricity & Magnetism',
    icon: Icons.battery_charging_full,
    tint: const Color(0xFF65A30D),
    topics: [
      Topic(
        id: 'capacitors',
        title: 'Capacitors',
        tagline: 'Store charge, store energy, insert a dielectric',
        icon: Icons.battery_std,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: capacitorsLesson),
      ),
      Topic(
        id: 'capacitor-networks',
        title: 'Series & Parallel',
        tagline: 'Combine capacitors and predict the equivalent',
        icon: Icons.account_tree,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: capacitorNetworksLesson),
      ),
    ],
  ),
  Chapter(
    id: 'current-electricity',
    title: 'Current Electricity',
    unit: 'Electricity & Magnetism',
    icon: Icons.electrical_services,
    tint: const Color(0xFF059669),
    topics: [
      Topic(
        id: 'ohms-law-drift',
        title: "Ohm's Law & Drift Velocity",
        tagline: 'Electrons crawl, current flows — resolve the paradox',
        icon: Icons.trending_up,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: ohmsLawDriftLesson),
      ),
      Topic(
        id: 'kirchhoff-laws',
        title: "Kirchhoff's Laws",
        tagline: 'Junctions and loops — solve any circuit',
        icon: Icons.hub,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: kirchhoffLawsLesson),
      ),
      Topic(
        id: 'heating-effect',
        title: 'Heating Effect',
        tagline: 'Why fuses melt and heaters glow',
        icon: Icons.whatshot,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: heatingEffectLesson),
      ),
      Topic(
        id: 'meter-bridge',
        title: 'Meter Bridge & Potentiometer',
        tagline: 'The classic lab instruments, virtually',
        icon: Icons.straighten,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: meterBridgeLesson),
      ),
    ],
  ),
  Chapter(
    id: 'magnetism',
    title: 'Magnetism',
    unit: 'Electricity & Magnetism',
    icon: Icons.explore,
    tint: const Color(0xFF4338CA),
    topics: [
      Topic(
        id: 'magnetic-force',
        title: 'Magnetic Field & Lorentz Force',
        tagline: 'A force that never does work, yet bends beams',
        icon: Icons.explore,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: magneticForceLesson),
      ),
      Topic(
        id: 'charge-in-field',
        title: 'Motion in a Magnetic Field',
        tagline: 'Circles, helices and the cyclotron',
        icon: Icons.rotate_left,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: chargeInFieldLesson),
      ),
      Topic(
        id: 'biot-savart',
        title: 'Biot–Savart Law',
        tagline: 'Every current element writes its own field',
        icon: Icons.gesture,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: biotSavartLesson),
      ),
      Topic(
        id: 'ampere-solenoid',
        title: "Ampere's Law & Solenoid",
        tagline: 'Wrap a wire, build an electromagnet',
        icon: Icons.settings_ethernet,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: ampereSolenoidLesson),
      ),
    ],
  ),
  Chapter(
    id: 'emi-ac',
    title: 'EMI & AC',
    unit: 'Electricity & Magnetism',
    icon: Icons.electric_bolt,
    tint: const Color(0xFF0284C7),
    topics: [
      Topic(
        id: 'faraday-lenz',
        title: 'Faraday & Lenz Law',
        tagline: 'Move a magnet, make a current — and nature resists',
        icon: Icons.change_circle_outlined,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: faradayLenzLesson),
      ),
      Topic(
        id: 'ac-circuits',
        title: 'AC Circuits',
        tagline: 'Phasors, impedance and resonance in RLC',
        icon: Icons.multiline_chart,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: acCircuitsLesson),
      ),
      Topic(
        id: 'transformers',
        title: 'Transformers',
        tagline: 'How the grid moves power across the country',
        icon: Icons.swap_horizontal_circle,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: transformersLesson),
      ),
    ],
  ),

  // ─────────────────────────── OPTICS ──────────────────────────────
  Chapter(
    id: 'ray-optics',
    title: 'Ray Optics',
    unit: 'Optics',
    icon: Icons.visibility,
    tint: const Color(0xFFC026D3),
    topics: [
      Topic(
        id: 'reflection-mirrors',
        title: 'Reflection & Mirrors',
        tagline: 'Trace rays through concave and convex mirrors',
        icon: Icons.flip,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: reflectionMirrorsLesson),
      ),
      Topic(
        id: 'refraction',
        title: 'Refraction',
        tagline: "Snell's law, apparent depth and total internal reflection",
        icon: Icons.water_drop,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: refractionLesson),
      ),
      Topic(
        id: 'lenses',
        title: 'Lenses',
        tagline: 'Slide the object, watch the image flip and scale',
        icon: Icons.lens_outlined,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: lensesLesson),
      ),
      Topic(
        id: 'prism-dispersion',
        title: 'Prism & Dispersion',
        tagline: 'Split white light into a rainbow',
        icon: Icons.change_history,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: prismDispersionLesson),
      ),
      Topic(
        id: 'optical-instruments',
        title: 'Optical Instruments',
        tagline: 'Microscopes, telescopes and the human eye',
        icon: Icons.biotech,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: opticalInstrumentsLesson),
      ),
    ],
  ),
  Chapter(
    id: 'wave-optics',
    title: 'Wave Optics',
    unit: 'Optics',
    icon: Icons.blur_linear,
    tint: const Color(0xFF7E22CE),
    topics: [
      Topic(
        id: 'interference',
        title: 'Interference',
        tagline: "Young's double slit — light plus light can equal dark",
        icon: Icons.blur_linear,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: interferenceLesson),
      ),
      Topic(
        id: 'diffraction',
        title: 'Diffraction',
        tagline: 'Light bends around edges — see the single-slit pattern',
        icon: Icons.gradient,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: diffractionLesson),
      ),
      Topic(
        id: 'polarization',
        title: 'Polarization',
        tagline: 'Filter light waves by their direction of vibration',
        icon: Icons.line_weight,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: polarizationLesson),
      ),
    ],
  ),

  // ─────────────────────── MODERN PHYSICS ──────────────────────────
  Chapter(
    id: 'modern-physics',
    title: 'Modern Physics',
    unit: 'Modern Physics',
    icon: Icons.science,
    tint: const Color(0xFF0F766E),
    topics: [
      Topic(
        id: 'photoelectric-effect',
        title: 'Photoelectric Effect',
        tagline: 'The experiment that proved light comes in packets',
        icon: Icons.light_mode,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: photoelectricEffectLesson),
      ),
      Topic(
        id: 'bohr-model',
        title: 'Bohr Model',
        tagline: 'Electron orbits, energy levels and spectral lines',
        icon: Icons.track_changes,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: bohrModelLesson),
      ),
      Topic(
        id: 'nuclear-physics',
        title: 'Nuclear Physics',
        tagline: 'Binding energy — why fission and fusion both release energy',
        icon: Icons.hive,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: nuclearPhysicsLesson),
      ),
      Topic(
        id: 'radioactivity',
        title: 'Radioactivity',
        tagline: 'Half-life: predictable decay from random events',
        icon: Icons.timelapse,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: radioactivityLesson),
      ),
    ],
  ),
  Chapter(
    id: 'semiconductors',
    title: 'Semiconductors',
    unit: 'Modern Physics',
    icon: Icons.memory,
    tint: const Color(0xFF334155),
    topics: [
      Topic(
        id: 'semiconductor-diodes',
        title: 'Semiconductors & Diodes',
        tagline: 'p-n junctions — the gate that lets current through one way',
        icon: Icons.memory,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: semiconductorDiodesLesson),
      ),
      Topic(
        id: 'logic-gates',
        title: 'Logic Gates',
        tagline: 'AND, OR, NOT — build circuits that think',
        icon: Icons.account_tree_outlined,
        highYield: true,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: logicGatesLesson),
      ),
      Topic(
        id: 'communication-systems',
        title: 'Communication Systems',
        tagline: 'Modulation — how your voice rides a radio wave',
        icon: Icons.cell_tower,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: communicationSystemsLesson),
      ),
    ],
  ),
];

/// Flat list of every topic across all chapters.
final List<Topic> allTopics = [for (final c in syllabus) ...c.topics];

Topic? topicById(String id) {
  for (final t in allTopics) {
    if (t.id == id) return t;
  }
  return null;
}

Chapter chapterOf(Topic topic) =>
    syllabus.firstWhere((c) => c.topics.any((t) => t.id == topic.id));
