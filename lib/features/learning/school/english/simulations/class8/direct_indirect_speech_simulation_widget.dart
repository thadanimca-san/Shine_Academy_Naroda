import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correctly transformed reported-speech version of each sentence.
class DirectIndirectSpeechSimulationWidget extends StatelessWidget {
  const DirectIndirectSpeechSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She said, "I am tired." → She said that she ___ tired.', correctWord: 'was', options: ['was', 'is', 'were'], note: 'Present tense "am" shifts to past tense "was" in reported speech.'),
    CompletionExample(sentenceWithBlank: 'He said, "I will come tomorrow." → He said that he ___ come the next day.', correctWord: 'would', options: ['would', 'will', 'shall'], note: '"Will" shifts back to "would".'),
    CompletionExample(sentenceWithBlank: 'They said, "We are playing now." → They said that they ___ playing then.', correctWord: 'were', options: ['were', 'are', 'was'], note: 'Present continuous shifts to past continuous.'),
    CompletionExample(sentenceWithBlank: 'She said, "I saw him yesterday." → She said that she ___ seen him the day before.', correctWord: 'had', options: ['had', 'has', 'have'], note: 'Simple past shifts to past perfect.'),
    CompletionExample(sentenceWithBlank: 'He asked, "Where do you live?" → He asked where I ___.', correctWord: 'lived', options: ['lived', 'live', 'was living'], note: 'In reported questions, tense shifts back and word order becomes statement-like.'),
    CompletionExample(sentenceWithBlank: 'She said, "This is my book." → She said that ___ was her book.', correctWord: 'that', options: ['that', 'this', 'it'], note: '"This" changes to "that" when reporting.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Direct to Indirect Speech',
      icon: Icons.chat_bubble_outline,
      accent: Colors.deepOrange,
      description: 'Choose the correctly transformed word for reported speech.',
      examples: _examples,
    );
  }
}
