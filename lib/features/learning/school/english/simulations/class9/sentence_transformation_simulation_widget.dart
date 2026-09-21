import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly completes a sentence transformed into a
/// different form while keeping the original meaning.
class SentenceTransformationSimulationWidget extends StatelessWidget {
  const SentenceTransformationSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He is the tallest boy in class. → He is taller than ___ boy in class.', correctWord: 'any other', options: ['any other', 'all other'], note: 'Superlative-to-comparative transformation uses "any other".'),
    CompletionExample(sentenceWithBlank: 'Despite his illness, he came to work. → ___ he was ill, he came to work.', correctWord: 'Though', options: ['Though', 'Because'], note: '"Though" introduces a contrast, matching "despite".'),
    CompletionExample(sentenceWithBlank: 'Only he can solve this. → No one ___ he can solve this.', correctWord: 'but', options: ['but', 'except of'], note: '"No one but" expresses the same exclusivity as "only".'),
    CompletionExample(sentenceWithBlank: 'It is a difficult task. → ___ a difficult task it is!', correctWord: 'What', options: ['What', 'How'], note: '"What" is used before a noun in exclamatory sentences.'),
    CompletionExample(sentenceWithBlank: 'She sings very sweetly. → ___ sweetly she sings!', correctWord: 'How', options: ['How', 'What'], note: '"How" is used before an adverb/adjective in exclamations.'),
    CompletionExample(sentenceWithBlank: 'He worked hard to succeed. → He worked hard ___ he might succeed.', correctWord: 'so that', options: ['so that', 'because'], note: '"So that" expresses purpose.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Transforming Sentences',
      icon: Icons.transform,
      accent: Colors.deepPurple,
      description: 'Choose the word that correctly completes the transformed sentence.',
      examples: _examples,
    );
  }
}
