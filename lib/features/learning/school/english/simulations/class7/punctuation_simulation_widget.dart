import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the punctuation mark that correctly ends (or completes) each
/// sentence.
class PunctuationSimulationWidget extends StatelessWidget {
  const PunctuationSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'What time is it___', correctWord: '?', options: ['.', '?', '!'], note: 'A question ends with a question mark.'),
    CompletionExample(sentenceWithBlank: 'What a beautiful sunset___', correctWord: '!', options: ['.', '!', '?'], note: 'Strong feeling or surprise ends with an exclamation mark.'),
    CompletionExample(sentenceWithBlank: 'I live in Delhi___', correctWord: '.', options: ['.', '?', '!'], note: 'A plain statement ends with a full stop.'),
    CompletionExample(sentenceWithBlank: "I bought apples, bananas___ and grapes.", correctWord: ',', options: [',', '.', ';'], note: 'A comma separates items in a list.'),
    CompletionExample(sentenceWithBlank: "That is Raj___s book.", correctWord: "'", options: ["'", ',', '.'], note: 'An apostrophe before "s" shows possession.'),
    CompletionExample(sentenceWithBlank: "She said___ I will come tomorrow.", correctWord: ',', options: [',', '.', '!'], note: 'A comma is often used before a quotation.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Choose the Correct Punctuation',
      icon: Icons.format_quote,
      accent: Colors.red,
      description: 'Pick the punctuation mark that correctly completes each sentence.',
      examples: _examples,
    );
  }
}
