import '../../models/lesson.dart';
import '../../theme/tokens.dart';

final Lesson magnetismMatterLesson = Lesson(
  topicId: 'magnetism-matter',
  title: 'Magnetism & Matter',
  accentColor: Palette.chMechanics,
  bigQuestion: "Why does a compass needle dip downwards as you get closer to the poles?",
  whyItMatters: "Without Earth's magnetic field, solar wind would strip away our atmosphere. Understanding magnetic materials is also the basis of all computer hard drives and motors.",
  prediction: const PredictionPrompt(
    scenario: "If you heat a strong permanent magnet (ferromagnetic) past its Curie temperature, it becomes:",
    options: ['Diamagnetic', 'Paramagnetic', 'Superconducting', 'Non-magnetic permanently'],
    correctIndex: 1,
    reveal: "Paramagnetic. Thermal agitation destroys the alignment of magnetic domains.",
  ),
  experiments: ["Measure Earth's magnetic dip angle at different latitudes.", 'Heat a magnet and watch it lose its strength.'],
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for Magnetism & Matter will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for Magnetism & Matter',
    'Important point 2 for Magnetism & Matter',
  ],
  sandboxBuilder: null,
);
