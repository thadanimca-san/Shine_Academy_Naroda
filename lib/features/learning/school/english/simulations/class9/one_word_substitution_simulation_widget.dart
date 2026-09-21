import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the single word that correctly substitutes the given phrase.
class OneWordSubstitutionSimulationWidget extends StatelessWidget {
  const OneWordSubstitutionSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A person who studies birds is called an ___.', correctWord: 'ornithologist', options: ['ornithologist', 'archaeologist'], note: 'An ornithologist specifically studies birds.'),
    CompletionExample(sentenceWithBlank: 'A person who cannot read or write is called ___.', correctWord: 'illiterate', options: ['illiterate', 'illegal'], note: '"Illiterate" describes someone unable to read or write.'),
    CompletionExample(sentenceWithBlank: 'A person who loves mankind is called a ___.', correctWord: 'philanthropist', options: ['philanthropist', 'patriot'], note: 'A philanthropist works for the welfare of others.'),
    CompletionExample(sentenceWithBlank: 'One who eats too much is called a ___.', correctWord: 'glutton', options: ['glutton', 'gourmet'], note: 'A glutton eats excessively; a gourmet is a connoisseur of food.'),
    CompletionExample(sentenceWithBlank: 'One who studies the stars and planets is called an ___.', correctWord: 'astronomer', options: ['astronomer', 'astrologer'], note: 'An astronomer studies celestial bodies scientifically.'),
    CompletionExample(sentenceWithBlank: 'One who speaks many languages is called a ___.', correctWord: 'polyglot', options: ['polyglot', 'linguist'], note: 'A polyglot can speak several languages fluently.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'One-Word Substitution',
      icon: Icons.short_text,
      accent: Colors.pink,
      description: 'Choose the single word that means the same as the given phrase.',
      examples: _examples,
    );
  }
}
