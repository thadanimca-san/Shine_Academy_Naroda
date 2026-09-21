import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly fills each gap in a connected,
/// board-style passage combining several grammar points.
class IntegratedGrammarSimulationWidget extends StatelessWidget {
  const IntegratedGrammarSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'India ___ a rich cultural heritage.', correctWord: 'has', options: ['has', 'have'], note: '"India" is singular, so it takes "has".'),
    CompletionExample(sentenceWithBlank: 'It is ___ historical monument built by Shah Jahan.', correctWord: 'an', options: ['an', 'a'], note: '"Historical" begins with a vowel sound, so "an" is used.'),
    CompletionExample(sentenceWithBlank: 'The monument ___ built in the seventeenth century.', correctWord: 'was', options: ['was', 'is'], note: 'The passage describes a past event, so the past tense "was" is needed.'),
    CompletionExample(sentenceWithBlank: 'Tourists ___ advised to carry water bottles in summer.', correctWord: 'are', options: ['are', 'is'], note: '"Tourists" is plural, so it takes "are".'),
    CompletionExample(sentenceWithBlank: 'You ___ book your tickets online to save time.', correctWord: 'should', options: ['should', 'must not'], note: '"Should" gives helpful advice, matching the sentence\'s intent.'),
    CompletionExample(sentenceWithBlank: 'By next year, the museum ___ its renovation.', correctWord: 'will have completed', options: ['will have completed', 'completes'], note: 'An action finished before a future point uses the future perfect tense.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Integrated Grammar (Gap Filling)',
      icon: Icons.integration_instructions,
      accent: Colors.indigo,
      description: 'Choose the word that correctly fills each gap in the passage.',
      examples: _examples,
    );
  }
}
