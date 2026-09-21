import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correct future-tense verb form to complete each sentence.
class FutureTenseSimulationWidget extends StatelessWidget {
  const FutureTenseSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'I ___ visit my grandmother next week.', correctWord: 'am going to', options: ['will', 'am going to', 'was going to'], note: 'A pre-planned intention is often expressed with "going to".'),
    CompletionExample(sentenceWithBlank: "It's heavy — I ___ help you carry it.", correctWord: 'will', options: ['will', 'am going to', 'would'], note: 'A spontaneous decision made at the moment of speaking uses "will".'),
    CompletionExample(sentenceWithBlank: 'At 8pm tomorrow, I ___ studying for the test.', correctWord: 'will be', options: ['will be', 'am', 'was'], note: 'An action in progress at a specific future time uses the future continuous: will be + verb-ing.'),
    CompletionExample(sentenceWithBlank: 'By next year, she ___ graduated.', correctWord: 'will have', options: ['will have', 'has', 'will be'], note: 'An action completed before a future point uses the future perfect: will have + past participle.'),
    CompletionExample(sentenceWithBlank: 'The train ___ at 9 o\'clock tomorrow.', correctWord: 'leaves', options: ['leaves', 'will leave', 'left'], note: 'Fixed schedules and timetables often use the simple present tense for future meaning.'),
    CompletionExample(sentenceWithBlank: 'Look at those clouds — it ___ rain soon.', correctWord: 'is going to', options: ['is going to', 'will', 'was going to'], note: 'A prediction based on present evidence uses "going to".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Complete with the Future Tense',
      icon: Icons.update,
      accent: Colors.indigo,
      description: 'Pick the verb form that correctly completes each sentence.',
      examples: _examples,
    );
  }
}
