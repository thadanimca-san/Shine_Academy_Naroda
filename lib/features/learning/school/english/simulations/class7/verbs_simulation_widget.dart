import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted verb as transitive (needs an object) or
/// intransitive (complete on its own).
class VerbsSimulationWidget extends StatelessWidget {
  const VerbsSimulationWidget({super.key});

  static const _options = ['Transitive Verb', 'Intransitive Verb'];

  static const _examples = [
    ClassifyExample(sentence: 'She sings a beautiful song.', highlight: 'sings', correctType: 'Transitive Verb'),
    ClassifyExample(sentence: 'The baby sleeps peacefully.', highlight: 'sleeps', correctType: 'Intransitive Verb'),
    ClassifyExample(sentence: 'He kicked the ball hard.', highlight: 'kicked', correctType: 'Transitive Verb'),
    ClassifyExample(sentence: 'The sun rises in the east.', highlight: 'rises', correctType: 'Intransitive Verb'),
    ClassifyExample(sentence: 'They built a sandcastle.', highlight: 'built', correctType: 'Transitive Verb'),
    ClassifyExample(sentence: 'The children laughed loudly.', highlight: 'laughed', correctType: 'Intransitive Verb'),
    ClassifyExample(sentence: 'She read the newspaper.', highlight: 'read', correctType: 'Transitive Verb'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Transitive or Intransitive?',
      icon: Icons.directions_run,
      accent: Colors.deepOrange,
      description: 'Does the highlighted verb need an object to complete its meaning? Tap the correct type.',
      examples: _examples,
      options: _options,
    );
  }
}
