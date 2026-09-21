import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify how the highlighted noun clause functions in the sentence.
class NounClausesSimulationWidget extends StatelessWidget {
  const NounClausesSimulationWidget({super.key});

  static const _options = ['Subject', 'Object', 'Complement'];

  static const _examples = [
    ClassifyExample(sentence: 'What she said surprised everyone.', highlight: 'What she said', correctType: 'Subject'),
    ClassifyExample(sentence: 'I know that he is honest.', highlight: 'that he is honest', correctType: 'Object'),
    ClassifyExample(sentence: 'The truth is that he lied.', highlight: 'that he lied', correctType: 'Complement'),
    ClassifyExample(sentence: 'Whoever wins the race gets a medal.', highlight: 'Whoever wins the race', correctType: 'Subject'),
    ClassifyExample(sentence: 'She asked me how I solved the puzzle.', highlight: 'how I solved the puzzle', correctType: 'Object'),
    ClassifyExample(sentence: 'My belief is that hard work always pays off.', highlight: 'that hard work always pays off', correctType: 'Complement'),
    ClassifyExample(sentence: 'I do not know whether he will come.', highlight: 'whether he will come', correctType: 'Object'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Function of the Noun Clause',
      icon: Icons.account_tree,
      accent: Colors.purple,
      description: 'Tap how the highlighted noun clause functions in the sentence.',
      examples: _examples,
      options: _options,
    );
  }
}
