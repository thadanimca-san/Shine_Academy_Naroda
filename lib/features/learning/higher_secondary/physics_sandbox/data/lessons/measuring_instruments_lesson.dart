import '../../models/lesson.dart';
import '../../theme/tokens.dart';

final Lesson measuringInstrumentsLesson = Lesson(
  topicId: 'measuring-instruments',
  title: 'Measuring Instruments',
  accentColor: Palette.chMechanics,
  bigQuestion: "How do you measure the thickness of a human hair?",
  whyItMatters: "Physics is an experimental science. Without precise measurements and error analysis, theories cannot be tested.",
  prediction: const PredictionPrompt(
    scenario: "If the zero of the vernier scale is to the right of the main scale zero, the zero error is:",
    options: ['Positive', 'Negative', 'Zero', 'Infinite'],
    correctIndex: 0,
    reveal: "Positive. It means the instrument reads more than the actual value, so you must subtract the error.",
  ),
  experiments: ['Slide the vernier caliper and read the main and vernier scales.', 'Rotate the screw gauge and calculate the pitch and least count.'],
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for Measuring Instruments will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for Measuring Instruments',
    'Important point 2 for Measuring Instruments',
  ],
  sandboxBuilder: null,
);
