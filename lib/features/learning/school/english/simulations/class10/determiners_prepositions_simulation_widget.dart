import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the determiner or preposition that correctly completes each
/// board-style sentence.
class DeterminersPrepositionsSimulationWidget extends StatelessWidget {
  const DeterminersPrepositionsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She is good ___ solving puzzles.', correctWord: 'at', options: ['at', 'in'], note: '"Good at" is the fixed collocation for skill in an activity.'),
    CompletionExample(sentenceWithBlank: 'The success of the plan depends ___ everyone\'s cooperation.', correctWord: 'on', options: ['on', 'of'], note: '"Depend on" is a fixed verb-preposition pairing.'),
    CompletionExample(sentenceWithBlank: 'She has ___ little experience in this field, so she can manage on her own.', correctWord: 'a', options: ['a', 'no'], note: '"A little" means some (positive), unlike "little" alone which means almost none.'),
    CompletionExample(sentenceWithBlank: 'He lives ___ Mumbai.', correctWord: 'in', options: ['in', 'at'], note: '"In" is used with cities and large areas.'),
    CompletionExample(sentenceWithBlank: 'The cat jumped ___ the box.', correctWord: 'into', options: ['into', 'to'], note: '"Into" shows movement toward the inside of something.'),
    CompletionExample(sentenceWithBlank: 'There is ___ milk left in the bottle.', correctWord: 'little', options: ['little', 'few'], note: '"Little" is used with uncountable nouns like "milk"; "few" is used with countable nouns.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Determiners and Prepositions: Combined Practice',
      icon: Icons.rule,
      accent: Colors.lightBlue,
      description: 'Choose the determiner or preposition that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
