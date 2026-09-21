import '../../models/lesson.dart';
import 'package:flutter/material.dart';

final Lesson emWavesLesson = Lesson(
  topicId: 'em-waves',
  title: 'Electromagnetic Waves',
  accentColor: const Color(0xFF0284C7),
  bigQuestion: "How does light travel through a vacuum where there is nothing to wave?",
  whyItMatters: "EM waves are the basis of all modern communication—from your Wi-Fi to X-rays in a hospital.",
  prediction: const PredictionPrompt(
    scenario: "Which of these EM waves has the highest frequency?",
    options: ['Microwaves', 'Infrared', 'Ultraviolet', 'X-Rays'],
    correctIndex: 3,
    reveal: "X-Rays. The spectrum order from low to high frequency is Radio, Micro, IR, Visible, UV, X-Ray, Gamma.",
  ),
  experiments: ['Explore the EM spectrum and wavelength-frequency relationship.', 'Calculate displacement current between capacitor plates.'],
  concept: const [
    ContentBlock.paragraph(
      'Detailed theory for Electromagnetic Waves will be rendered here. This acts as a placeholder to ensure the app compiles cleanly and the module is ready for full content injection.',
      title: 'Introduction',
    ),
  ],
  derivation: const [],
  formulas: const [],
  questions: const [],
  revision: const [
    'Important point 1 for Electromagnetic Waves',
    'Important point 2 for Electromagnetic Waves',
  ],
  sandboxBuilder: null,
);
