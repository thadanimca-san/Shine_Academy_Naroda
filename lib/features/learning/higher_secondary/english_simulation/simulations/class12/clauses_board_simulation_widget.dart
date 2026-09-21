import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Identify whether the highlighted clause is a noun, adjective, or
/// adverb clause in board-style exam sentences.
class ClausesBoardSimulationWidget extends StatelessWidget {
  const ClausesBoardSimulationWidget({super.key});

  static const _examples = [
    ClassifyExample(sentence: 'I wonder whether she will come.', highlight: 'whether she will come', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'The man whose car was stolen filed a report.', highlight: 'whose car was stolen', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'Wherever you go, I will follow.', highlight: 'Wherever you go', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'I do not know where he lives.', highlight: 'where he lives', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'The reason that he gave was unconvincing.', highlight: 'that he gave', correctType: 'Adjective Clause'),
    ClassifyExample(sentence: 'That she is talented is obvious.', highlight: 'That she is talented', correctType: 'Noun Clause'),
    ClassifyExample(sentence: 'He worked hard so that he could succeed.', highlight: 'so that he could succeed', correctType: 'Adverb Clause'),
    ClassifyExample(sentence: 'Although she was tired, she kept working.', highlight: 'Although she was tired', correctType: 'Adverb Clause'),
  ];

  static const _options = ['Noun Clause', 'Adjective Clause', 'Adverb Clause'];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Clauses (Board Level)',
      icon: Icons.account_tree,
      accent: Colors.brown,
      description: 'Identify the kind of the highlighted clause.',
      examples: _examples,
      options: _options,
    );
  }
}
