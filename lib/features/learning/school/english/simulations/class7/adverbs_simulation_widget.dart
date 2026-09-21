import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify the highlighted adverb by the kind of information it adds:
/// manner, time, place, frequency, or degree.
class AdverbsSimulationWidget extends StatelessWidget {
  const AdverbsSimulationWidget({super.key});

  static const _options = ['Manner', 'Time', 'Place', 'Frequency', 'Degree'];

  static const _examples = [
    ClassifyExample(sentence: 'She sings beautifully.', highlight: 'beautifully', correctType: 'Manner'),
    ClassifyExample(sentence: 'We will leave tomorrow.', highlight: 'tomorrow', correctType: 'Time'),
    ClassifyExample(sentence: 'Please sit here.', highlight: 'here', correctType: 'Place'),
    ClassifyExample(sentence: 'He always arrives on time.', highlight: 'always', correctType: 'Frequency'),
    ClassifyExample(sentence: 'The tea is very hot.', highlight: 'very', correctType: 'Degree'),
    ClassifyExample(sentence: 'She quietly closed the door.', highlight: 'quietly', correctType: 'Manner'),
    ClassifyExample(sentence: 'They rarely miss a class.', highlight: 'rarely', correctType: 'Frequency'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Kind of Adverb',
      icon: Icons.speed,
      accent: Colors.pink,
      description: 'Tap the type of adverb the highlighted word represents.',
      examples: _examples,
      options: _options,
    );
  }
}
