import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word/phrase that correctly completes the transformed
/// sentence while keeping its original meaning.
class SentenceTransformationSimulationWidget extends StatelessWidget {
  const SentenceTransformationSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He is the tallest boy in the class. → He is taller than ___ boy in the class.', correctWord: 'any other', options: ['any other', 'all other'], note: 'Superlative-to-comparative transformation uses "any other".'),
    CompletionExample(sentenceWithBlank: 'As soon as the bell rang, the students left. → ___ the bell rung than the students left.', correctWord: 'No sooner had the bell rung', options: ['No sooner had the bell rung', 'Hardly had the bell rung'], note: '"No sooner...than" is the correct paired construction.'),
    CompletionExample(sentenceWithBlank: 'It is a very sad story. → ___ a sad story it is!', correctWord: 'What', options: ['What', 'How'], note: '"What" is used before a noun in exclamatory sentences.'),
    CompletionExample(sentenceWithBlank: 'He is too weak to walk. → He is ___ walk.', correctWord: 'so weak that he cannot', options: ['so weak that he cannot', 'such weak that he cannot'], note: '"So + adjective + that" is the correct structure with an adjective.'),
    CompletionExample(sentenceWithBlank: 'Unless you work hard, you will not succeed. → If you ___ hard, you will not succeed.', correctWord: 'do not work', options: ['do not work', 'work'], note: '"Unless" means "if...not", so the transformed clause must be negative.'),
    CompletionExample(sentenceWithBlank: 'Only Sunil can solve this problem. → No one ___ can solve this problem.', correctWord: 'except Sunil', options: ['except Sunil', 'but except Sunil'], note: '"No one except" expresses the same exclusivity as "only".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Transformation of Sentences',
      icon: Icons.transform,
      accent: Colors.teal,
      description: 'Choose the word or phrase that correctly completes the transformed sentence.',
      examples: _examples,
    );
  }
}
