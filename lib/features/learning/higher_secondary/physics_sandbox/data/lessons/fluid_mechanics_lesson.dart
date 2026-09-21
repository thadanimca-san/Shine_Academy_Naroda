import '../../models/lesson.dart';
import '../../theme/tokens.dart';

final Lesson fluidMechanicsLesson = Lesson(
  topicId: 'fluid-mechanics',
  title: 'Fluid Mechanics',
  accentColor: Palette.chMechanics,
  bigQuestion: "How does a 300-ton airplane stay in the sky?",
  whyItMatters: "Fluid mechanics explains how planes fly, why ships float, and how blood flows in your veins.",
  prediction: const PredictionPrompt(
    scenario: "If water flows from a wide pipe into a narrow pipe, its speed:",
    options: ['Decreases', 'Stays the same', 'Increases', 'Becomes zero'],
    correctIndex: 2,
    reveal: "Increases. By the Equation of Continuity (A1V1 = A2V2), a smaller area means a higher velocity.",
  ),
  experiments: ['Change pipe diameter and watch velocity increase.', "Observe pressure drop (Bernoulli's principle)."],
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for Fluid Mechanics will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for Fluid Mechanics',
    'Important point 2 for Fluid Mechanics',
  ],
  sandboxBuilder: null,
);
