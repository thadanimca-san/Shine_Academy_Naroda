import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Identify whether the highlighted clause is a noun, adjective, or
/// adverb clause.
class ClausesAdvancedSimulationWidget extends StatelessWidget {
  const ClausesAdvancedSimulationWidget({super.key});

  static const _examples = [
    ClassifyExample(sentence: 'I know that he is innocent.', highlight: 'that he is innocent', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'The house which stands on the hill is old.', highlight: 'which stands on the hill', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'He will succeed if he works hard.', highlight: 'if he works hard', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'She spoke as if she knew everything.', highlight: 'as if she knew everything', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'Whoever comes first will win the prize.', highlight: 'Whoever comes first', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'This is the reason why he resigned.', highlight: 'why he resigned', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'Although it was raining, they went out.', highlight: 'Although it was raining', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'He saved money so that he could buy a car.', highlight: 'so that he could buy a car', correctType: 'Adverb Clause'),
  ];

  static const _options = ['Noun Clause', 'Adjective Clause', 'Adverb Clause'];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Clauses (Advanced Practice)',
      icon: Icons.account_tree,
      accent: Colors.brown,
      description: 'Identify the kind of the highlighted clause.',
      examples: _examples,
      options: _options,
    );
  }
}
