import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct preposition of time/manner/agent for each sentence
/// (more advanced usage than the Class 7 spatial prepositions drill).
class Class8PrepositionsSimulationWidget extends StatelessWidget {
  const Class8PrepositionsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'The letter was written ___ a fountain pen.', correctWord: 'with', options: ['with', 'by', 'on'], note: '"With" shows the instrument used.'),
    CompletionExample(sentenceWithBlank: 'The novel was written ___ a famous author.', correctWord: 'by', options: ['by', 'with', 'from'], note: '"By" shows the agent (doer) of a passive action.'),
    CompletionExample(sentenceWithBlank: 'We will meet ___ Monday morning.', correctWord: 'on', options: ['on', 'in', 'at'], note: '"On" is used with specific days.'),
    CompletionExample(sentenceWithBlank: 'She has been studying ___ two hours.', correctWord: 'for', options: ['for', 'since', 'during'], note: '"For" is used with a duration of time.'),
    CompletionExample(sentenceWithBlank: 'He has lived here ___ 2015.', correctWord: 'since', options: ['since', 'for', 'from'], note: '"Since" is used with a starting point in time.'),
    CompletionExample(sentenceWithBlank: 'They are worried ___ the exam results.', correctWord: 'about', options: ['about', 'of', 'for'], note: '"Worried about" is a fixed preposition pairing.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Prepositions of Time, Agent and Manner',
      icon: Icons.schedule,
      accent: Colors.cyan,
      description: 'Pick the preposition that correctly completes each sentence.',
      examples: _examples,
    );
  }
}
