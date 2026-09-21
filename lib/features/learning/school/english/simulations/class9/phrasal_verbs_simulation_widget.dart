import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the phrasal verb whose idiomatic meaning fits the sentence.
class PhrasalVerbsSimulationWidget extends StatelessWidget {
  const PhrasalVerbsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Please ___ my plants while I am away.', correctWord: 'look after', options: ['look after', 'look into'], note: '"Look after" means to take care of.'),
    CompletionExample(sentenceWithBlank: 'The police will ___ the matter thoroughly.', correctWord: 'look into', options: ['look into', 'look after'], note: '"Look into" means to investigate.'),
    CompletionExample(sentenceWithBlank: 'He decided to ___ smoking for good.', correctWord: 'give up', options: ['give up', 'give away'], note: '"Give up" means to quit.'),
    CompletionExample(sentenceWithBlank: 'They had to ___ the meeting due to rain.', correctWord: 'put off', options: ['put off', 'put up with'], note: '"Put off" means to postpone.'),
    CompletionExample(sentenceWithBlank: 'I cannot ___ his rude behaviour any longer.', correctWord: 'put up with', options: ['put up with', 'put off'], note: '"Put up with" means to tolerate.'),
    CompletionExample(sentenceWithBlank: 'The caterpillar will soon ___ a butterfly.', correctWord: 'turn into', options: ['turn into', 'turn off'], note: '"Turn into" means to transform into something else.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Phrasal Verbs in Context',
      icon: Icons.extension,
      accent: Colors.cyan,
      description: 'Choose the phrasal verb whose meaning fits the sentence.',
      examples: _examples,
    );
  }
}
