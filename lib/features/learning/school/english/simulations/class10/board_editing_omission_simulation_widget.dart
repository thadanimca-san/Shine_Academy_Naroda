import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly fixes the error or fills the omission
/// in each board-level exam-style sentence.
class BoardEditingOmissionSimulationWidget extends StatelessWidget {
  const BoardEditingOmissionSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She always ___ the truth.', correctWord: 'speaks', options: ['speaks', 'speak'], note: 'Third-person singular subjects take the "-s" verb form in the present simple.'),
    CompletionExample(sentenceWithBlank: 'He is ___ best player in the team.', correctWord: 'the', options: ['the', 'a'], note: 'Superlatives ("best") require the definite article "the".'),
    CompletionExample(sentenceWithBlank: 'There ___ many problems.', correctWord: 'are', options: ['are', 'is'], note: '"Problems" is plural, so the plural verb "are" is needed.'),
    CompletionExample(sentenceWithBlank: 'She is senior ___ me.', correctWord: 'to', options: ['to', 'than'], note: '"Senior" is a Latin comparative and pairs with "to", not "than".'),
    CompletionExample(sentenceWithBlank: 'Neither of the answers ___ correct.', correctWord: 'was', options: ['was', 'were'], note: '"Neither" takes a singular verb even before a plural-looking phrase.'),
    CompletionExample(sentenceWithBlank: 'He apologised ___ his mistake.', correctWord: 'for', options: ['for', 'of'], note: '"Apologise" is followed by the fixed preposition "for".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Editing and Omission (Board Level)',
      icon: Icons.fact_check,
      accent: Colors.deepOrange,
      description: 'Choose the word that correctly fixes the error or fills the gap.',
      examples: _examples,
    );
  }
}
