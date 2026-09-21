import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct meaning, synonym, or antonym for each board-level
/// vocabulary item.
class VocabularyBoardSimulationWidget extends StatelessWidget {
  const VocabularyBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A person who works for free is called a ___.', correctWord: 'volunteer', options: ['volunteer', 'mercenary'], note: 'A volunteer offers their services without expecting payment.'),
    CompletionExample(sentenceWithBlank: 'To "shed light on" something means to ___.', correctWord: 'clarify or explain it', options: ['clarify or explain it', 'hide it'], note: 'This idiom describes making something clearer or better understood.'),
    CompletionExample(sentenceWithBlank: 'A word similar in meaning to "candid" is ___.', correctWord: 'frank', options: ['frank', 'secretive'], note: '"Frank" and "candid" both describe open, honest speech.'),
    CompletionExample(sentenceWithBlank: 'To "turn a blind eye to" something means to ___.', correctWord: 'deliberately ignore it', options: ['deliberately ignore it', 'examine it closely'], note: 'This idiom describes consciously choosing not to notice something.'),
    CompletionExample(sentenceWithBlank: 'A word opposite in meaning to "meticulous" is ___.', correctWord: 'careless', options: ['careless', 'thorough'], note: '"Meticulous" means very careful and precise; "careless" is its opposite.'),
    CompletionExample(sentenceWithBlank: 'To "make ends meet" means to ___.', correctWord: 'manage financially with limited money', options: ['manage financially with limited money', 'spend lavishly'], note: 'This idiom describes covering basic expenses within a tight budget.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Vocabulary and Idioms (Board Level)',
      icon: Icons.menu_book,
      accent: Colors.green,
      description: 'Choose the correct meaning of each word or idiom.',
      examples: _examples,
    );
  }
}
