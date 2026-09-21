import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct question tag to complete each sentence.
class QuestionTagsSimulationWidget extends StatelessWidget {
  const QuestionTagsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She is your sister, ___?', correctWord: "isn't she", options: ["isn't she", "is she", "doesn't she"], note: 'Positive statement takes a negative tag.'),
    CompletionExample(sentenceWithBlank: 'You don\'t like coffee, ___?', correctWord: 'do you', options: ['do you', "don't you", 'did you'], note: 'Negative statement takes a positive tag.'),
    CompletionExample(sentenceWithBlank: 'They have finished the work, ___?', correctWord: "haven't they", options: ["haven't they", 'have they', "don't they"], note: '"Have" as an auxiliary is echoed in the tag.'),
    CompletionExample(sentenceWithBlank: 'Let\'s go to the park, ___?', correctWord: "shall we", options: ['shall we', 'will we', "don't we"], note: '"Let\'s" always takes the tag "shall we".'),
    CompletionExample(sentenceWithBlank: 'He can swim well, ___?', correctWord: "can't he", options: ["can't he", 'can he', "couldn't he"], note: 'Modal "can" is echoed negatively in the tag.'),
    CompletionExample(sentenceWithBlank: 'Nobody called, ___?', correctWord: 'did they', options: ['did they', "didn't they", 'do they'], note: '"Nobody" is treated as negative, so the tag is positive.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Question Tags',
      icon: Icons.help_outline,
      accent: Colors.redAccent,
      description: 'Pick the question tag that correctly matches the statement.',
      examples: _examples,
    );
  }
}
