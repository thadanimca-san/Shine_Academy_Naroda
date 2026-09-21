import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the response that grammatically and contextually completes
/// each side of a short dialogue.
class DialogueCompletionSimulationWidget extends StatelessWidget {
  const DialogueCompletionSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A: "Would you like some tea?" B: "Yes, I ___ love some."', correctWord: 'would', options: ['would', 'will'], note: '"Would" matches the polite, hypothetical tone of the question.'),
    CompletionExample(sentenceWithBlank: 'A: "Have you finished your homework?" B: "Yes, I ___ finished it."', correctWord: 'have', options: ['have', 'has'], note: 'The subject "I" takes "have" in the present perfect.'),
    CompletionExample(sentenceWithBlank: 'A: "Where were you yesterday?" B: "I ___ at the library."', correctWord: 'was', options: ['was', 'am'], note: 'Yesterday is in the past, so the past tense "was" is required.'),
    CompletionExample(sentenceWithBlank: 'A: "How long have you lived here?" B: "I have lived here ___ ten years."', correctWord: 'for', options: ['for', 'since'], note: '"For" is used with a duration of time, not a starting point.'),
    CompletionExample(sentenceWithBlank: 'A: "Why didn\'t you call me?" B: "I ___ my phone at home."', correctWord: 'had forgotten', options: ['had forgotten', 'forget'], note: 'The forgetting happened before the not-calling, so the past perfect is used.'),
    CompletionExample(sentenceWithBlank: 'A: "Shall we meet at six?" B: "That ___ perfect for me."', correctWord: 'sounds', options: ['sounds', 'sound'], note: '"That" is singular, so it takes the singular verb "sounds".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Dialogue Completion',
      icon: Icons.forum,
      accent: Colors.blue,
      description: 'Choose the word that correctly completes B\'s response.',
      examples: _examples,
    );
  }
}
