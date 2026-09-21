import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correct plural or gender form to complete each sentence.
class NounsNumberGenderSimulationWidget extends StatelessWidget {
  const NounsNumberGenderSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'The farmer has two ___ pulling the cart.', correctWord: 'oxen', options: ['oxen', 'oxes', 'ox'], note: '"Ox" has the irregular plural "oxen".'),
    CompletionExample(sentenceWithBlank: 'The chef sharpened both ___.', correctWord: 'knives', options: ['knifes', 'knives', 'knife'], note: '"Knife" becomes "knives" in the plural.'),
    CompletionExample(sentenceWithBlank: 'The lioness protected her cubs, while the ___ watched nearby.', correctWord: 'lion', options: ['lion', 'lioness', 'lions'], note: '"Lion" is the masculine form; "lioness" is feminine.'),
    CompletionExample(sentenceWithBlank: 'She is a talented ___ who has won several awards.', correctWord: 'actress', options: ['actor', 'actress', 'actoress'], note: '"Actress" is the feminine form of "actor".'),
    CompletionExample(sentenceWithBlank: 'The shepherd counted all his ___.', correctWord: 'sheep', options: ['sheep', 'sheeps', 'sheepes'], note: '"Sheep" is unchanged in the plural.'),
    CompletionExample(sentenceWithBlank: 'Both of my ___ hurt after the run.', correctWord: 'feet', options: ['foots', 'feet', 'feets'], note: '"Foot" has the irregular plural "feet".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Number and Gender of Nouns',
      icon: Icons.people,
      accent: Colors.indigo,
      description: 'Pick the correct plural or gender form to complete each sentence.',
      examples: _examples,
    );
  }
}
