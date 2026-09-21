import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the determiner that correctly completes each board-style
/// sentence.
class DeterminersBoardSimulationWidget extends StatelessWidget {
  const DeterminersBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Is there ___ water left in the tank?', correctWord: 'any', options: ['any', 'some'], note: '"Any" is used in questions and negatives.'),
    CompletionExample(sentenceWithBlank: 'It was ___ interesting film that we watched it twice.', correctWord: 'such an', options: ['such an', 'such a'], note: '"Such an" is used before a singular noun beginning with a vowel sound.'),
    CompletionExample(sentenceWithBlank: '___ of the two roads leads to the station.', correctWord: 'Either', options: ['Either', 'Both'], note: '"Either" refers to one of two, and takes a singular verb.'),
    CompletionExample(sentenceWithBlank: 'She has ___ money to spare after her expenses.', correctWord: 'little', options: ['little', 'few'], note: '"Little" is used with uncountable nouns like "money".'),
    CompletionExample(sentenceWithBlank: 'We need ___ information before we proceed with the plan.', correctWord: 'more', options: ['more', 'many'], note: '"Information" is uncountable, so "more" (not "many") is used.'),
    CompletionExample(sentenceWithBlank: '___ citizen has the right to vote in this country.', correctWord: 'Every', options: ['Every', 'All'], note: '"Every" takes a singular noun and verb.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Determiners (Board Level)',
      icon: Icons.rule,
      accent: Colors.indigo,
      description: 'Choose the determiner that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
