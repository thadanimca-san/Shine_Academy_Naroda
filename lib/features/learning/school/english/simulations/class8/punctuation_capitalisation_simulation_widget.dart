import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correctly punctuated/capitalised version of each sentence
/// fragment (more advanced usage than the Class 7 basic punctuation drill).
class PunctuationCapitalisationSimulationWidget extends StatelessWidget {
  const PunctuationCapitalisationSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'My favourite subjects are ___ Maths, Science and English.', correctWord: 'Maths,', options: ['Maths,', 'maths,', 'Maths'], note: 'Proper nouns/subject names like "Maths" are capitalised.'),
    CompletionExample(sentenceWithBlank: 'She asked, ___ "Where are you going?"', correctWord: 'She said,', options: ['She said,', 'She said', 'she said,'], note: 'A comma is used before an opening quotation mark in direct speech.'),
    CompletionExample(sentenceWithBlank: 'I bought apples, bananas___ and oranges.', correctWord: 'apples, bananas,', options: ['apples, bananas,', 'apples bananas', 'apples, bananas'], note: 'Commas separate items in a list, including before "and" (Oxford comma style).'),
    CompletionExample(sentenceWithBlank: 'Wow___ what a beautiful sunset!', correctWord: 'Wow!', options: ['Wow!', 'Wow,', 'Wow.'], note: 'An exclamation mark follows an interjection expressing strong feeling.'),
    CompletionExample(sentenceWithBlank: 'The teacher said ___ "well done" to the class.', correctWord: '"well done"', options: ['"well done"', 'well done', "'well done'"], note: 'Double quotation marks enclose a direct quotation.'),
    CompletionExample(sentenceWithBlank: 'I live in ___ mumbai.', correctWord: 'Mumbai', options: ['Mumbai', 'mumbai', 'MUMBAI'], note: 'Place names are proper nouns and must be capitalised.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Punctuation and Capitalisation',
      icon: Icons.format_quote,
      accent: Colors.blue,
      description: 'Choose the correctly punctuated or capitalised form.',
      examples: _examples,
    );
  }
}
