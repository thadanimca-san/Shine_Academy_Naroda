import os

# Data structure for missing lessons
lessons = [
    {
        "filename": "elasticity_lesson.dart",
        "var_name": "elasticityLesson",
        "topic_id": "elasticity",
        "title": "Elasticity & Hooke's Law",
        "unit": "Properties of Matter",
        "tagline": "Stress, strain, and why things bounce back",
        "icon": "Icons.compress",
        "accentColor": "Palette.chMechanics",
        "bigQuestion": "Why does steel bounce back better than rubber?",
        "whyItMatters": "Elasticity governs everything from building bridges that don't snap in the wind to the shock absorbers in your car. Hooke's Law is the gateway to understanding how solids deform and recover.",
        "prediction_scenario": "If you double the length of a wire and apply the same force, the extension will:",
        "prediction_options": ["Remain the same", "Double", "Halve", "Quadruple"],
        "prediction_correct": 1,
        "prediction_reveal": "Double. Extension ΔL = (F L) / (A Y). If length L doubles, ΔL doubles.",
        "experiments": [
            "Stretch a wire and observe the stress-strain curve.",
            "Find the yield point where it stops bouncing back.",
            "Compare Young's Modulus of steel vs rubber."
        ]
    },
    {
        "filename": "fluid_mechanics_lesson.dart",
        "var_name": "fluidMechanicsLesson",
        "topic_id": "fluid-mechanics",
        "title": "Fluid Mechanics",
        "unit": "Properties of Matter",
        "tagline": "Archimedes, Bernoulli, and the flow of liquids",
        "icon": "Icons.water",
        "accentColor": "Palette.chMechanics",
        "bigQuestion": "How does a 300-ton airplane stay in the sky?",
        "whyItMatters": "Fluid mechanics explains how planes fly, why ships float, and how blood flows in your veins.",
        "prediction_scenario": "If water flows from a wide pipe into a narrow pipe, its speed:",
        "prediction_options": ["Decreases", "Stays the same", "Increases", "Becomes zero"],
        "prediction_correct": 2,
        "prediction_reveal": "Increases. By the Equation of Continuity (A1V1 = A2V2), a smaller area means a higher velocity.",
        "experiments": [
            "Change pipe diameter and watch velocity increase.",
            "Observe pressure drop (Bernoulli's principle)."
        ]
    },
    {
        "filename": "surface_tension_lesson.dart",
        "var_name": "surfaceTensionLesson",
        "topic_id": "surface-tension",
        "title": "Surface Tension",
        "unit": "Properties of Matter",
        "tagline": "Why water drops are round and bugs can walk on water",
        "icon": "Icons.bubble_chart",
        "accentColor": "Palette.chMechanics",
        "bigQuestion": "Why does water rise in a narrow capillary tube but mercury falls?",
        "whyItMatters": "Surface tension is why trees can pull water hundreds of feet into the air without a pump.",
        "prediction_scenario": "If you add soap to water, its surface tension:",
        "prediction_options": ["Increases", "Decreases", "Stays the same", "Becomes zero"],
        "prediction_correct": 1,
        "prediction_reveal": "Decreases. Soap molecules disrupt the cohesive forces between water molecules.",
        "experiments": [
            "Change capillary tube radius and watch the ascent height change.",
            "Measure excess pressure inside a soap bubble."
        ]
    },
    {
        "filename": "em_waves_lesson.dart",
        "var_name": "emWavesLesson",
        "topic_id": "em-waves",
        "title": "Electromagnetic Waves",
        "unit": "Electricity & Magnetism",
        "tagline": "Displacement current and the EM spectrum",
        "icon": "Icons.wifi_tethering",
        "accentColor": "const Color(0xFF0284C7)",
        "bigQuestion": "How does light travel through a vacuum where there is nothing to wave?",
        "whyItMatters": "EM waves are the basis of all modern communication—from your Wi-Fi to X-rays in a hospital.",
        "prediction_scenario": "Which of these EM waves has the highest frequency?",
        "prediction_options": ["Microwaves", "Infrared", "Ultraviolet", "X-Rays"],
        "prediction_correct": 3,
        "prediction_reveal": "X-Rays. The spectrum order from low to high frequency is Radio, Micro, IR, Visible, UV, X-Ray, Gamma.",
        "experiments": [
            "Explore the EM spectrum and wavelength-frequency relationship.",
            "Calculate displacement current between capacitor plates."
        ]
    },
    {
        "filename": "measuring_instruments_lesson.dart",
        "var_name": "measuringInstrumentsLesson",
        "topic_id": "measuring-instruments",
        "title": "Measuring Instruments",
        "unit": "Mechanics",
        "tagline": "Vernier calipers and screw gauges",
        "icon": "Icons.architecture",
        "accentColor": "Palette.chMechanics",
        "bigQuestion": "How do you measure the thickness of a human hair?",
        "whyItMatters": "Physics is an experimental science. Without precise measurements and error analysis, theories cannot be tested.",
        "prediction_scenario": "If the zero of the vernier scale is to the right of the main scale zero, the zero error is:",
        "prediction_options": ["Positive", "Negative", "Zero", "Infinite"],
        "prediction_correct": 0,
        "prediction_reveal": "Positive. It means the instrument reads more than the actual value, so you must subtract the error.",
        "experiments": [
            "Slide the vernier caliper and read the main and vernier scales.",
            "Rotate the screw gauge and calculate the pitch and least count."
        ]
    },
    {
        "filename": "magnetism_matter_lesson.dart",
        "var_name": "magnetismMatterLesson",
        "topic_id": "magnetism-matter",
        "title": "Magnetism & Matter",
        "unit": "Electricity & Magnetism",
        "tagline": "Earth's magnetism and magnetic materials",
        "icon": "Icons.public",
        "accentColor": "Palette.chMechanics",
        "bigQuestion": "Why does a compass needle dip downwards as you get closer to the poles?",
        "whyItMatters": "Without Earth's magnetic field, solar wind would strip away our atmosphere. Understanding magnetic materials is also the basis of all computer hard drives and motors.",
        "prediction_scenario": "If you heat a strong permanent magnet (ferromagnetic) past its Curie temperature, it becomes:",
        "prediction_options": ["Diamagnetic", "Paramagnetic", "Superconducting", "Non-magnetic permanently"],
        "prediction_correct": 1,
        "prediction_reveal": "Paramagnetic. Thermal agitation destroys the alignment of magnetic domains.",
        "experiments": [
            "Measure Earth's magnetic dip angle at different latitudes.",
            "Heat a magnet and watch it lose its strength."
        ]
    }
]

def generate_lesson_file(lesson):
    content = f'''import '../../models/lesson.dart';
import '../../theme/tokens.dart';
import 'package:flutter/material.dart';

final Lesson {lesson['var_name']} = Lesson(
  topicId: '{lesson['topic_id']}',
  title: '{lesson['title']}',
  accentColor: {lesson['accentColor']},
  bigQuestion: "{lesson['bigQuestion']}",
  whyItMatters: "{lesson['whyItMatters']}",
  prediction: const PredictionPrompt(
    scenario: "{lesson['prediction_scenario']}",
    options: {lesson['prediction_options']},
    correctIndex: {lesson['prediction_correct']},
    reveal: "{lesson['prediction_reveal']}",
  ),
  experiments: {lesson['experiments']},
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for {lesson['title']} will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for {lesson['title']}',
    'Important point 2 for {lesson['title']}',
  ],
  sandboxBuilder: null,
);
'''
    os.makedirs('lib/features/learning/higher_secondary/physics_sandbox/data/lessons', exist_ok=True)
    with open(f"lib/features/learning/higher_secondary/physics_sandbox/data/lessons/{lesson['filename']}", "w") as f:
        f.write(content)

def update_syllabus():
    syllabus_path = 'lib/features/learning/higher_secondary/physics_sandbox/data/syllabus_data.dart'
    with open(syllabus_path, 'r') as f:
        content = f.read()

    # 1. Add imports
    imports = "\\n".join([f"import 'lessons/{lesson['filename']}';" for lesson in lessons])
    if "import 'lessons/elasticity_lesson.dart';" not in content:
        content = content.replace('// ── Lesson data ──────────────────────────────────────────────────────────────',
                                  f'// ── Lesson data ──────────────────────────────────────────────────────────────\\n{imports}')

    # 2. Add to syllabus structure
    properties_of_matter_chapter = """  Chapter(
    id: 'properties-of-matter',
    title: 'Properties of Bulk Matter',
    unit: 'Properties of Matter',
    icon: Icons.water,
    tint: const Color(0xFF0EA5E9),
    topics: [
      Topic(
        id: 'elasticity',
        title: 'Elasticity & Hooke\\'s Law',
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
"""
    if "id: 'properties-of-matter'" not in content:
        content = content.replace("  // ─────────────────────── THERMAL PHYSICS ────────────────────────",
                                  f"{properties_of_matter_chapter}\\n  // ─────────────────────── THERMAL PHYSICS ────────────────────────")

    measuring_topic = """      Topic(
        id: 'measuring-instruments',
        title: 'Measuring Instruments',
        tagline: 'Vernier calipers and screw gauges',
        icon: Icons.architecture,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: measuringInstrumentsLesson),
      ),
"""
    if "id: 'measuring-instruments'" not in content:
        content = content.replace("builder: (_) => LessonScreen(lesson: vectorsLesson),\\n      ),",
                                  f"builder: (_) => LessonScreen(lesson: vectorsLesson),\\n      ),\\n{measuring_topic}")

    em_waves_topic = """      Topic(
        id: 'magnetism-matter',
        title: 'Magnetism & Matter',
        tagline: 'Earth\\'s magnetism and magnetic materials',
        icon: Icons.public,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: magnetismMatterLesson),
      ),
      Topic(
        id: 'em-waves',
        title: 'Electromagnetic Waves',
        tagline: 'Displacement current and the EM spectrum',
        icon: Icons.wifi_tethering,
        status: TopicStatus.available,
        builder: (_) => LessonScreen(lesson: emWavesLesson),
      ),
"""
    if "id: 'em-waves'" not in content:
        content = content.replace("builder: (_) => LessonScreen(lesson: transformersLesson),\\n      ),",
                                  f"builder: (_) => LessonScreen(lesson: transformersLesson),\\n      ),\\n{em_waves_topic}")

    with open(syllabus_path, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    print("Generating missing physics lessons...")
    for lesson in lessons:
        generate_lesson_file(lesson)
        print(f"Created {lesson['filename']}")
    update_syllabus()
    print("Updated syllabus_data.dart with new chapters and topics.")
    print("All done! Run `flutter run` to see the new topics in the Sandbox.")
