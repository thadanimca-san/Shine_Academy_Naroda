import 'package:flutter/material.dart';
import '../common/classify_example_widget.dart';

/// Classify each sentence by its purpose: declarative, interrogative,
/// imperative, or exclamatory.
class KindsOfSentencesSimulationWidget extends StatelessWidget {
  const KindsOfSentencesSimulationWidget({super.key});

  static const _options = ['Declarative', 'Interrogative', 'Imperative', 'Exclamatory'];

  static const _examples = [
    ClassifyExample(sentence: 'I live in Delhi.', highlight: 'I live in Delhi.', correctType: 'Declarative'),
    ClassifyExample(sentence: 'Where do you live?', highlight: 'Where do you live?', correctType: 'Interrogative'),
    ClassifyExample(sentence: 'Close the door.', highlight: 'Close the door.', correctType: 'Imperative'),
    ClassifyExample(sentence: 'What a beautiful day it is!', highlight: 'What a beautiful day it is!', correctType: 'Exclamatory'),
    ClassifyExample(sentence: 'Please pass the salt.', highlight: 'Please pass the salt.', correctType: 'Imperative'),
    ClassifyExample(sentence: 'How amazing that trick was!', highlight: 'How amazing that trick was!', correctType: 'Exclamatory'),
    ClassifyExample(sentence: 'Are you coming to the party?', highlight: 'Are you coming to the party?', correctType: 'Interrogative'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ClassifyExampleWidget(
      title: 'Identify the Kind of Sentence',
      icon: Icons.chat_bubble_outline,
      accent: Colors.green,
      description: 'Tap the type that matches the purpose of each sentence.',
      examples: _examples,
      options: _options,
    );
  }
}
