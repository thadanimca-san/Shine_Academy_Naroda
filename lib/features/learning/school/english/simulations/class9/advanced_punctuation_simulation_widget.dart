import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify which punctuation mark best fits the highlighted gap in
/// each sentence.
class AdvancedPunctuationSimulationWidget extends StatelessWidget {
  const AdvancedPunctuationSimulationWidget({super.key});

  static const _options = ['Semicolon', 'Colon', 'Apostrophe', 'Hyphen', 'Dash'];

  static const _examples = [
    ClassifyExample(sentence: 'I have finished my homework [;] now I can relax.', highlight: '[;]', correctType: 'Semicolon'),
    ClassifyExample(sentence: 'She bought the following items [:] milk, bread and eggs.', highlight: '[:]', correctType: 'Colon'),
    ClassifyExample(sentence: 'This is Rahul [\'s] book.', highlight: "['s]", correctType: 'Apostrophe'),
    ClassifyExample(sentence: 'My brother [-] in [-] law arrived today.', highlight: '[-]', correctType: 'Hyphen'),
    ClassifyExample(sentence: 'The president [—] along with his cabinet [—] arrived on time.', highlight: '[—]', correctType: 'Dash'),
    ClassifyExample(sentence: 'We need three things [:] courage, patience and hope.', highlight: '[:]', correctType: 'Colon'),
    ClassifyExample(sentence: 'I wanted to go [;] however, it started raining.', highlight: '[;]', correctType: 'Semicolon'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Which Punctuation Mark Fits?',
      icon: Icons.format_quote,
      accent: Colors.blue,
      description: 'Tap the punctuation mark that correctly fills the highlighted gap.',
      examples: _examples,
      options: _options,
    );
  }
}
