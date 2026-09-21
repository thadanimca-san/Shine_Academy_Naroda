import '../../models/lesson.dart';
import '../../theme/tokens.dart';

final Lesson surfaceTensionLesson = Lesson(
  topicId: 'surface-tension',
  title: 'Surface Tension',
  accentColor: Palette.chMechanics,
  bigQuestion: "Why does water rise in a narrow capillary tube but mercury falls?",
  whyItMatters: "Surface tension is why trees can pull water hundreds of feet into the air without a pump.",
  prediction: const PredictionPrompt(
    scenario: "If you add soap to water, its surface tension:",
    options: ['Increases', 'Decreases', 'Stays the same', 'Becomes zero'],
    correctIndex: 1,
    reveal: "Decreases. Soap molecules disrupt the cohesive forces between water molecules.",
  ),
  experiments: ['Change capillary tube radius and watch the ascent height change.', 'Measure excess pressure inside a soap bubble.'],
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for Surface Tension will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for Surface Tension',
    'Important point 2 for Surface Tension',
  ],
  sandboxBuilder: null,
);
