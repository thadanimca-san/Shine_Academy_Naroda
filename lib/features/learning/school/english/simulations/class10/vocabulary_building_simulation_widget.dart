import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct synonym, antonym, or word-formed variant for the
/// given word.
class VocabularyBuildingSimulationWidget extends StatelessWidget {
  const VocabularyBuildingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A word similar in meaning to "happy" is ___.', correctWord: 'joyful', options: ['joyful', 'miserable'], note: '"Joyful" and "happy" share a similar positive meaning.'),
    CompletionExample(sentenceWithBlank: 'A word opposite in meaning to "generous" is ___.', correctWord: 'stingy', options: ['stingy', 'kind'], note: '"Stingy" describes someone unwilling to give, the opposite of generous.'),
    CompletionExample(sentenceWithBlank: 'The noun form of the adjective "beautiful" is ___.', correctWord: 'beauty', options: ['beauty', 'beautify'], note: '"Beauty" is the noun; "beautify" is a verb meaning to make beautiful.'),
    CompletionExample(sentenceWithBlank: 'The verb form of the noun "strength" is ___.', correctWord: 'strengthen', options: ['strengthen', 'strong'], note: '"Strengthen" is the verb form; "strong" is the adjective form.'),
    CompletionExample(sentenceWithBlank: 'A word opposite in meaning to "victory" is ___.', correctWord: 'defeat', options: ['defeat', 'triumph'], note: '"Defeat" is the direct opposite of "victory".'),
    CompletionExample(sentenceWithBlank: 'The noun form of the verb "decide" is ___.', correctWord: 'decision', options: ['decision', 'decisive'], note: '"Decision" is the noun; "decisive" is the adjective form.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Vocabulary: Synonyms, Antonyms and Word Formation',
      icon: Icons.menu_book,
      accent: Colors.green,
      description: 'Choose the correct synonym, antonym, or word-formed variant.',
      examples: _examples,
    );
  }
}
