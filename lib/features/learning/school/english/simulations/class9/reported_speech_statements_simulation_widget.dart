import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correctly backshifted verb/pronoun/time form when a direct
/// statement is transformed into reported speech.
class ReportedSpeechStatementsSimulationWidget extends StatelessWidget {
  const ReportedSpeechStatementsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She said, "I am happy." → She said that she ___ happy.', correctWord: 'was', options: ['was', 'is'], note: 'Present tense shifts one step back to past tense.'),
    CompletionExample(sentenceWithBlank: 'He said, "I will help you." → He said that he ___ help me.', correctWord: 'would', options: ['would', 'will'], note: '"Will" shifts back to "would".'),
    CompletionExample(sentenceWithBlank: 'They said, "We went to the market yesterday." → They said that they ___ to the market the day before.', correctWord: 'had gone', options: ['had gone', 'went'], note: 'Simple past shifts to past perfect.'),
    CompletionExample(sentenceWithBlank: 'The teacher said, "The Earth revolves around the Sun." → The teacher said that the Earth ___ around the Sun.', correctWord: 'revolves', options: ['revolves', 'revolved'], note: 'Universal truths keep the present tense.'),
    CompletionExample(sentenceWithBlank: 'She said, "This is my pen." → She said that ___ was her pen.', correctWord: 'that', options: ['that', 'this'], note: '"This" changes to "that" in reported speech.'),
    CompletionExample(sentenceWithBlank: 'They said, "We are leaving now." → They said that they were leaving ___.', correctWord: 'then', options: ['then', 'now'], note: '"Now" changes to "then".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Reporting Statements Correctly',
      icon: Icons.record_voice_over,
      accent: Colors.brown,
      description: 'Choose the correctly transformed word for reported statements.',
      examples: _examples,
    );
  }
}
