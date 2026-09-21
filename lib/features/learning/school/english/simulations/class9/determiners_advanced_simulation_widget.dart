import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct determiner, distinguishing tricky quantity/number
/// pairs like few/a few, much/many, each/every.
class DeterminersAdvancedSimulationWidget extends StatelessWidget {
  const DeterminersAdvancedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'I have ___ friends, so I never feel lonely.', correctWord: 'a few', options: ['a few', 'few'], note: '"A few" has a positive sense: some, enough.'),
    CompletionExample(sentenceWithBlank: 'She has ___ hope of passing; she has not studied at all.', correctWord: 'little', options: ['little', 'a little'], note: '"Little" has a negative sense: almost none.'),
    CompletionExample(sentenceWithBlank: 'How ___ milk do we need for the recipe?', correctWord: 'much', options: ['much', 'many'], note: '"Much" is used with uncountable nouns like "milk".'),
    CompletionExample(sentenceWithBlank: '___ student was given individual feedback by the teacher.', correctWord: 'Each', options: ['Each', 'Every'], note: '"Each" considers members individually, one at a time.'),
    CompletionExample(sentenceWithBlank: '___ child in the country deserves an education.', correctWord: 'Every', options: ['Every', 'Each'], note: '"Every" considers the group as a whole.'),
    CompletionExample(sentenceWithBlank: 'I do not have ___ money left.', correctWord: 'any', options: ['any', 'some'], note: '"Any" is used in negative sentences.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Tricky Determiner Pairs',
      icon: Icons.checklist,
      accent: Colors.blueGrey,
      description: 'Choose the determiner that correctly fits the meaning of each sentence.',
      examples: _examples,
    );
  }
}
