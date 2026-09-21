import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly completes the reported version of a
/// mixed set of statements, questions, commands, and exclamations.
class ReportedSpeechBoardSimulationWidget extends StatelessWidget {
  const ReportedSpeechBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He said, "I can finish this today." → He said that he ___ finish it that day.', correctWord: 'could', options: ['could', 'can'], note: '"Can" backshifts to "could" in reported speech.'),
    CompletionExample(sentenceWithBlank: 'The manager said, "You must submit the report today." → The manager said that I ___ submit the report that day.', correctWord: 'had to', options: ['had to', 'must'], note: '"Must" (obligation) backshifts to "had to" in reported speech.'),
    CompletionExample(sentenceWithBlank: 'He asked, "Did you complete the assignment?" → He asked me ___ I had completed the assignment.', correctWord: 'if', options: ['if', 'that'], note: 'Yes/no questions are reported using "if" or "whether".'),
    CompletionExample(sentenceWithBlank: 'The teacher said, "Keep quiet, boys." → The teacher ordered the boys ___ quiet.', correctWord: 'to keep', options: ['to keep', 'keep'], note: 'Commands are reported using "to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'She said to him, "Please help me." → She requested him ___ help her.', correctWord: 'to', options: ['to', 'that he'], note: 'Polite requests are reported using "to" + base verb after "requested".'),
    CompletionExample(sentenceWithBlank: 'They said, "We will visit tomorrow." → They said that they ___ visit the next day.', correctWord: 'would', options: ['would', 'will'], note: '"Will" backshifts to "would" in reported speech.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Reported Speech (Board Level, Mixed)',
      icon: Icons.record_voice_over,
      accent: Colors.purple,
      description: 'Choose the word that correctly completes the reported sentence.',
      examples: _examples,
    );
  }
}
