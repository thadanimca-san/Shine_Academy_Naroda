import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted conjunction as coordinating, subordinating or
/// correlative (more advanced than the Class 7 basic and/but/or drill).
class Class8ConjunctionsSimulationWidget extends StatelessWidget {
  const Class8ConjunctionsSimulationWidget({super.key});

  static const _options = ['Coordinating', 'Subordinating', 'Correlative'];

  static const _examples = [
    ClassifyExample(sentence: 'I stayed home because it was raining.', highlight: 'because', correctType: 'Subordinating'),
    ClassifyExample(sentence: 'She is both talented and hardworking.', highlight: 'both...and', correctType: 'Correlative'),
    ClassifyExample(sentence: 'He was tired, yet he kept working.', highlight: 'yet', correctType: 'Coordinating'),
    ClassifyExample(sentence: 'Neither the teacher nor the students were late.', highlight: 'neither...nor', correctType: 'Correlative'),
    ClassifyExample(sentence: 'Although it was late, we continued the meeting.', highlight: 'Although', correctType: 'Subordinating'),
    ClassifyExample(sentence: 'You can have tea or coffee.', highlight: 'or', correctType: 'Coordinating'),
    ClassifyExample(sentence: 'Whether you agree or not, we must proceed.', highlight: 'Whether...or', correctType: 'Correlative'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Kinds of Conjunctions',
      icon: Icons.link,
      accent: Colors.pink,
      description: 'Tap the type that matches the highlighted conjunction.',
      examples: _examples,
      options: _options,
    );
  }
}
