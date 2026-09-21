import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the modal verb that correctly expresses the meaning needed in
/// each sentence (ability, permission, obligation, advice...).
class AuxiliaryModalVerbsSimulationWidget extends StatelessWidget {
  const AuxiliaryModalVerbsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She ___ swim across the river.', correctWord: 'can', options: ['can', 'must', 'should'], note: '"Can" expresses ability.'),
    CompletionExample(sentenceWithBlank: 'You ___ wear a helmet — it\'s the law.', correctWord: 'must', options: ['must', 'may', 'could'], note: '"Must" expresses strong obligation.'),
    CompletionExample(sentenceWithBlank: 'You ___ apologise to her; it would be kind.', correctWord: 'should', options: ['should', 'must', 'can'], note: '"Should" gives advice, softer than "must".'),
    CompletionExample(sentenceWithBlank: '___ I borrow your pen, please?', correctWord: 'May', options: ['May', 'Must', 'Will'], note: '"May" politely asks for permission.'),
    CompletionExample(sentenceWithBlank: 'It ___ rain later, the sky looks cloudy.', correctWord: 'might', options: ['might', 'must', 'shall'], note: '"Might" expresses possibility.'),
    CompletionExample(sentenceWithBlank: 'You ___ not smoke inside the building.', correctWord: 'must', options: ['must', 'can', 'may'], note: '"Must not" expresses prohibition.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Choose the Correct Modal Verb',
      icon: Icons.rule,
      accent: Colors.deepPurple,
      description: 'Pick the modal verb that best fits the meaning of each sentence.',
      examples: _examples,
    );
  }
}
