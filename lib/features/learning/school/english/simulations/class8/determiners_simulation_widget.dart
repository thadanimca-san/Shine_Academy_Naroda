import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted determiner by its kind.
class DeterminersSimulationWidget extends StatelessWidget {
  const DeterminersSimulationWidget({super.key});

  static const _options = ['Article', 'Demonstrative', 'Possessive', 'Quantifier', 'Interrogative'];

  static const _examples = [
    ClassifyExample(sentence: 'I would like a cup of tea.', highlight: 'a', correctType: 'Article'),
    ClassifyExample(sentence: 'This book belongs to me.', highlight: 'This', correctType: 'Demonstrative'),
    ClassifyExample(sentence: 'Her bicycle is parked outside.', highlight: 'Her', correctType: 'Possessive'),
    ClassifyExample(sentence: 'There is very little milk left.', highlight: 'little', correctType: 'Quantifier'),
    ClassifyExample(sentence: 'Which colour do you prefer?', highlight: 'Which', correctType: 'Interrogative'),
    ClassifyExample(sentence: 'Many students passed the exam.', highlight: 'Many', correctType: 'Quantifier'),
    ClassifyExample(sentence: 'Those shoes are too expensive.', highlight: 'Those', correctType: 'Demonstrative'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Determiner',
      icon: Icons.checklist,
      accent: Colors.blueGrey,
      description: 'Tap the type that matches the highlighted determiner.',
      examples: _examples,
      options: _options,
    );
  }
}
