import '../../models/lesson.dart';
import '../../theme/tokens.dart';

final Lesson elasticityLesson = Lesson(
  topicId: 'elasticity',
  title: "Elasticity & Hooke's Law",
  accentColor: Palette.chMechanics,
  bigQuestion: "Why does steel bounce back better than rubber?",
  whyItMatters: "Elasticity governs everything from building bridges that don't snap in the wind to the shock absorbers in your car. Hooke's Law is the gateway to understanding how solids deform and recover.",
  prediction: const PredictionPrompt(
    scenario: "If you double the length of a wire and apply the same force, the extension will:",
    options: ['Remain the same', 'Double', 'Halve', 'Quadruple'],
    correctIndex: 1,
    reveal: "Double. Extension ΔL = (F L) / (A Y). If length L doubles, ΔL doubles.",
  ),
  experiments: ["Stretch a wire and observe the stress-strain curve.", "Find the yield point where it stops bouncing back.", "Compare Young's Modulus of steel vs rubber."],
  concept: const [
    ContentBlock.paragraph(
      "Detailed theory for Elasticity & Hooke's Law will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.",
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    "Important point 1 for Elasticity & Hooke's Law",
    "Important point 2 for Elasticity & Hooke's Law",
  ],
  sandboxBuilder: null,
);
