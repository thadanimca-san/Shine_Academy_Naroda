import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the tense form that correctly completes each sentence.
class TensesIntegratedSimulationWidget extends StatelessWidget {
  const TensesIntegratedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'By the time we arrived, the movie ___.', correctWord: 'had already started', options: ['had already started', 'already started'], note: 'The past perfect shows an action completed before another past action.'),
    CompletionExample(sentenceWithBlank: 'She ___ in Delhi for ten years and still does.', correctWord: 'has lived', options: ['has lived', 'lived'], note: 'The present perfect connects a past action to the present.'),
    CompletionExample(sentenceWithBlank: 'By next year, he ___ his degree.', correctWord: 'will have completed', options: ['will have completed', 'completes'], note: 'The future perfect describes an action finished before a future point.'),
    CompletionExample(sentenceWithBlank: 'While she ___, the phone rang.', correctWord: 'was cooking', options: ['was cooking', 'cooked'], note: 'The past continuous sets the ongoing background action interrupted by another.'),
    CompletionExample(sentenceWithBlank: 'He ___ his homework before he went out to play.', correctWord: 'had finished', options: ['had finished', 'finished'], note: 'The past perfect shows the homework was finished before going out.'),
    CompletionExample(sentenceWithBlank: 'Look! It ___ heavily outside.', correctWord: 'is raining', options: ['is raining', 'rains'], note: 'The present continuous describes an action happening right now.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Tenses (Integrated Practice)',
      icon: Icons.schedule,
      accent: Colors.blueGrey,
      description: 'Choose the tense form that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
