import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correctly spelled homophone that fits the sentence's meaning.
class HomophonesHomonymsSimulationWidget extends StatelessWidget {
  const HomophonesHomonymsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Please ___ the ball to me.', correctWord: 'throw', options: ['throw', 'though', 'through'], note: '"Throw" means to toss; it sounds like "though" and "through" but differs in meaning.'),
    CompletionExample(sentenceWithBlank: 'I need to buy a new ___ of shoes.', correctWord: 'pair', options: ['pair', 'pear', 'pare'], note: '"Pair" means a set of two; "pear" is a fruit.'),
    CompletionExample(sentenceWithBlank: 'The knight rode his ___ into battle.', correctWord: 'horse', options: ['horse', 'hoarse'], note: '"Horse" is the animal; "hoarse" describes a rough voice.'),
    CompletionExample(sentenceWithBlank: 'Please ___ the letter to the correct address.', correctWord: 'mail', options: ['mail', 'male'], note: '"Mail" refers to post; "male" refers to gender.'),
    CompletionExample(sentenceWithBlank: 'The gardener will ___ the plants tomorrow.', correctWord: 'water', options: ['water', 'wader'], note: '"Water" is both the noun and verb here.'),
    CompletionExample(sentenceWithBlank: 'They sailed across the calm ___.', correctWord: 'sea', options: ['sea', 'see'], note: '"Sea" is the body of water; "see" means to view.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Homophones and Homonyms',
      icon: Icons.spellcheck,
      accent: Colors.lime,
      description: 'Choose the word that fits the sentence — watch out for similar-sounding traps!',
      examples: _examples,
    );
  }
}
