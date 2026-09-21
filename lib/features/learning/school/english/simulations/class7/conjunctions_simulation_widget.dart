import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the conjunction that correctly joins each pair of clauses.
class ConjunctionsSimulationWidget extends StatelessWidget {
  const ConjunctionsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'I was tired, ___ I kept working.', correctWord: 'but', options: ['but', 'and', 'because'], note: '"But" shows contrast between the two ideas.'),
    CompletionExample(sentenceWithBlank: 'She stayed home ___ she was sick.', correctWord: 'because', options: ['because', 'or', 'but'], note: '"Because" introduces a reason.'),
    CompletionExample(sentenceWithBlank: '___ it rains, we will cancel the picnic.', correctWord: 'If', options: ['If', 'So', 'And'], note: '"If" introduces a condition.'),
    CompletionExample(sentenceWithBlank: 'He bought bread ___ milk.', correctWord: 'and', options: ['and', 'but', 'or'], note: '"And" simply adds one item to another.'),
    CompletionExample(sentenceWithBlank: 'You can have tea ___ coffee.', correctWord: 'or', options: ['or', 'and', 'because'], note: '"Or" shows a choice between alternatives.'),
    CompletionExample(sentenceWithBlank: 'It was raining, ___ we stayed indoors.', correctWord: 'so', options: ['so', 'but', 'if'], note: '"So" introduces a result.'),
    CompletionExample(sentenceWithBlank: '___ it was cold, she wore a jacket.', correctWord: 'Although', options: ['Although', 'And', 'So'], note: '"Although" introduces a contrast/concession.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Choose the Correct Conjunction',
      icon: Icons.link,
      accent: Colors.deepPurple,
      description: 'Pick the conjunction that best joins the two ideas.',
      examples: _examples,
    );
  }
}
