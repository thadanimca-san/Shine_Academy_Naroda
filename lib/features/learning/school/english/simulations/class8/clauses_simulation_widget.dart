import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted clause by its kind.
class ClausesSimulationWidget extends StatelessWidget {
  const ClausesSimulationWidget({super.key});

  static const _options = ['Main Clause', 'Noun Clause', 'Adjective Clause', 'Adverb Clause'];

  static const _examples = [
    ClassifyExample(sentence: 'I know that he is honest.', highlight: 'that he is honest', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'The man who called is my uncle.', highlight: 'who called', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'She left before the rain started.', highlight: 'before the rain started', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'He finished his homework quickly.', highlight: 'He finished his homework quickly', correctType: 'Main Clause'),
    ClassifyExample(sentence: 'This is the house where I was born.', highlight: 'where I was born', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'Whoever wins the race gets a medal.', highlight: 'Whoever wins the race', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'We stayed indoors because it was raining.', highlight: 'because it was raining', correctType: 'Adverb Clause'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Clause',
      icon: Icons.account_tree,
      accent: Colors.green,
      description: 'Tap the type that matches the highlighted clause.',
      examples: _examples,
      options: _options,
    );
  }
}
