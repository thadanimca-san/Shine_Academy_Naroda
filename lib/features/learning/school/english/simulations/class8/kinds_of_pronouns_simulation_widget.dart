import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted pronoun by its kind: reflexive, emphatic,
/// reciprocal, relative or indefinite.
class KindsOfPronounsSimulationWidget extends StatelessWidget {
  const KindsOfPronounsSimulationWidget({super.key});

  static const _options = ['Reflexive', 'Emphatic', 'Reciprocal', 'Relative', 'Indefinite'];

  static const _examples = [
    ClassifyExample(sentence: 'He hurt himself while playing.', highlight: 'himself', correctType: 'Reflexive'),
    ClassifyExample(sentence: 'I myself saw the accident happen.', highlight: 'myself', correctType: 'Emphatic'),
    ClassifyExample(sentence: 'The twins always help each other.', highlight: 'each other', correctType: 'Reciprocal'),
    ClassifyExample(sentence: 'The man who called is my uncle.', highlight: 'who', correctType: 'Relative'),
    ClassifyExample(sentence: 'Someone left this umbrella here.', highlight: 'Someone', correctType: 'Indefinite'),
    ClassifyExample(sentence: 'She herself completed the entire project.', highlight: 'herself', correctType: 'Emphatic'),
    ClassifyExample(sentence: 'The students congratulated one another.', highlight: 'one another', correctType: 'Reciprocal'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Kind of Pronoun',
      icon: Icons.person_search,
      accent: Colors.teal,
      description: 'Tap the type that matches the highlighted pronoun.',
      examples: _examples,
      options: _options,
    );
  }
}
