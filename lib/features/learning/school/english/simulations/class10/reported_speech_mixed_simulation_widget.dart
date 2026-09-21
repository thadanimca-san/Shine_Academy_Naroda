import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly completes the reported version of a
/// statement, question, command, or exclamation.
class ReportedSpeechMixedSimulationWidget extends StatelessWidget {
  const ReportedSpeechMixedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He said, "I am busy right now." → He said that he ___ busy right then.', correctWord: 'was', options: ['was', 'is'], note: 'The present tense backshifts to the past tense in reported speech.'),
    CompletionExample(sentenceWithBlank: 'The officer said, "Stop the car!" → The officer ordered them ___ the car.', correctWord: 'to stop', options: ['to stop', 'stop'], note: 'Commands are reported using "to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'She asked, "Are you free this evening?" → She asked me ___ I was free that evening.', correctWord: 'if', options: ['if', 'that'], note: 'Yes/no questions are reported using "if" or "whether".'),
    CompletionExample(sentenceWithBlank: 'He said, "I will finish it by tomorrow." → He said that he ___ finish it by the next day.', correctWord: 'would', options: ['would', 'will'], note: '"Will" backshifts to "would" in reported speech.'),
    CompletionExample(sentenceWithBlank: 'The teacher said, "Do not run in the corridor." → The teacher ordered us ___ run in the corridor.', correctWord: 'not to', options: ['not to', 'to not'], note: 'Negative commands are reported as "not to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'He said, "Let us go for a walk." → He suggested ___ they go for a walk.', correctWord: 'that', options: ['that', 'to'], note: '"Let us" suggestions are reported with "suggested that".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Reported Speech: Mixed Practice',
      icon: Icons.record_voice_over,
      accent: Colors.purple,
      description: 'Choose the word that correctly completes the reported sentence.',
      examples: _examples,
    );
  }
}
