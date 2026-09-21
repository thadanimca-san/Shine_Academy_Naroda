import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// A noun-type sorter built on the shared classify-example drill: read
/// each sentence and identify what kind of noun is highlighted.
class NounsSimulationWidget extends StatelessWidget {
  const NounsSimulationWidget({super.key});

  static const _options = ['Common Noun', 'Proper Noun', 'Collective Noun', 'Abstract Noun', 'Material Noun'];

  static const _examples = [
    ClassifyExample(sentence: 'Raj lives in Mumbai.', highlight: 'Mumbai', correctType: 'Proper Noun'),
    ClassifyExample(sentence: 'The dog is barking loudly.', highlight: 'dog', correctType: 'Common Noun'),
    ClassifyExample(sentence: 'The whole team celebrated the win.', highlight: 'team', correctType: 'Collective Noun'),
    ClassifyExample(sentence: 'Her honesty impressed everyone.', highlight: 'honesty', correctType: 'Abstract Noun'),
    ClassifyExample(sentence: 'The ring is made of gold.', highlight: 'gold', correctType: 'Material Noun'),
    ClassifyExample(sentence: 'A jury of twelve people decided the case.', highlight: 'jury', correctType: 'Collective Noun'),
    ClassifyExample(sentence: 'Kindness costs nothing.', highlight: 'Kindness', correctType: 'Abstract Noun'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Noun Type',
      icon: Icons.label,
      accent: Colors.indigo,
      description: 'Read the sentence, then tap the correct type for the highlighted noun.',
      examples: _examples,
      options: _options,
    );
  }
}
