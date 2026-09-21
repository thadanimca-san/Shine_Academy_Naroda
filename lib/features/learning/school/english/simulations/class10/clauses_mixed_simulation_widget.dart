import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Identify whether the highlighted clause is a noun, adjective, or
/// adverb clause within a longer, exam-style sentence.
class ClausesMixedSimulationWidget extends StatelessWidget {
  const ClausesMixedSimulationWidget({super.key});

  static const _examples = [
    ClassifyExample(sentence: 'I believe that he is honest.', highlight: 'that he is honest', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'The book that you gave me is wonderful.', highlight: 'that you gave me', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'She left because she was tired.', highlight: 'because she was tired', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'The man who helped us was a stranger.', highlight: 'who helped us', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'I will wait until you arrive.', highlight: 'until you arrive', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'What he said is true.', highlight: 'What he said', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'This is the place where I grew up.', highlight: 'where I grew up', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'I know why she left.', highlight: 'why she left', correctType: 'Noun Clause'),
  ];

  static const _options = ['Noun Clause', 'Adjective Clause', 'Adverb Clause'];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Clauses: Combined Practice',
      icon: Icons.account_tree,
      accent: Colors.brown,
      description: 'Identify the kind of the highlighted clause.',
      examples: _examples,
      options: _options,
    );
  }
}
