import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted adverb clause by the relationship it expresses.
class AdverbClausesSimulationWidget extends StatelessWidget {
  const AdverbClausesSimulationWidget({super.key});

  static const _options = ['Time', 'Reason', 'Condition', 'Contrast'];

  static const _examples = [
    ClassifyExample(sentence: 'Although it was raining, we went out to play.', highlight: 'Although it was raining', correctType: 'Contrast'),
    ClassifyExample(sentence: 'She stayed home because she was unwell.', highlight: 'because she was unwell', correctType: 'Reason'),
    ClassifyExample(sentence: 'We will go for a picnic if it does not rain.', highlight: 'if it does not rain', correctType: 'Condition'),
    ClassifyExample(sentence: 'He left before the meeting ended.', highlight: 'before the meeting ended', correctType: 'Time'),
    ClassifyExample(sentence: 'You will fail unless you study hard.', highlight: 'unless you study hard', correctType: 'Condition'),
    ClassifyExample(sentence: 'Though he is rich, he lives simply.', highlight: 'Though he is rich', correctType: 'Contrast'),
    ClassifyExample(sentence: 'She has been ill since Monday.', highlight: 'since Monday', correctType: 'Time'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'What Does the Adverb Clause Express?',
      icon: Icons.compare_arrows,
      accent: Colors.orange,
      description: 'Tap the relationship the highlighted adverb clause expresses.',
      examples: _examples,
      options: _options,
    );
  }
}
