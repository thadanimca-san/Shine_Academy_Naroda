import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the determiner that correctly completes each sentence.
class DeterminersAdvancedSimulationWidget extends StatelessWidget {
  const DeterminersAdvancedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She has ___ friends who truly understand her.', correctWord: 'a few', options: ['a few', 'few'], note: '"A few" means some (positive); "few" alone means almost none.'),
    CompletionExample(sentenceWithBlank: '___ student must submit the assignment individually.', correctWord: 'Each', options: ['Each', 'Every'], note: '"Each" emphasises individual members of the group.'),
    CompletionExample(sentenceWithBlank: '___ of the two answers is correct.', correctWord: 'Neither', options: ['Neither', 'Both'], note: '"Neither" refers to not one of the two.'),
    CompletionExample(sentenceWithBlank: '___ the brothers were awarded scholarships.', correctWord: 'Both', options: ['Both', 'Either'], note: '"Both" refers to the two together, taking a plural verb.'),
    CompletionExample(sentenceWithBlank: 'There is ___ traffic on the highway today.', correctWord: 'much', options: ['much', 'many'], note: '"Traffic" is uncountable, so it takes "much".'),
    CompletionExample(sentenceWithBlank: '___ of you can answer this question — it does not matter who.', correctWord: 'Any', options: ['Any', 'Some'], note: '"Any" is used when it does not matter which one, often in such open contexts.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Determiners (Advanced Usage)',
      icon: Icons.rule,
      accent: Colors.indigo,
      description: 'Choose the determiner that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
