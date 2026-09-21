import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct reporting word/order when a direct question is
/// transformed into reported speech.
class ReportedSpeechQuestionsSimulationWidget extends StatelessWidget {
  const ReportedSpeechQuestionsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She said, "Where do you live?" → She asked me where I ___.', correctWord: 'lived', options: ['lived', 'did live'], note: 'Reported questions use statement word order, not the auxiliary "did".'),
    CompletionExample(sentenceWithBlank: 'He said, "Are you coming?" → He asked ___ I was coming.', correctWord: 'if', options: ['if', 'that'], note: 'Yes/No questions are reported with "if" or "whether".'),
    CompletionExample(sentenceWithBlank: 'She said, "Do you like tea?" → She asked me ___ I liked tea.', correctWord: 'whether', options: ['whether', 'what'], note: 'Yes/No questions can also use "whether".'),
    CompletionExample(sentenceWithBlank: 'He said, "Can you help me?" → He asked me ___ I could help him.', correctWord: 'if', options: ['if', 'what'], note: 'A yes/no question with a modal still uses "if"/"whether".'),
    CompletionExample(sentenceWithBlank: 'She said, "When will you leave?" → She asked me when I ___.', correctWord: 'would leave', options: ['would leave', 'will leave'], note: '"Will" shifts back to "would" as usual.'),
    CompletionExample(sentenceWithBlank: 'The teacher said, "Have you done your homework?" → The teacher asked ___ I had done my homework.', correctWord: 'if', options: ['if', 'that'], note: 'Yes/No questions always use "if"/"whether", never "that".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Reporting Questions Correctly',
      icon: Icons.question_answer,
      accent: Colors.indigo,
      description: 'Choose the correct word to report each question.',
      examples: _examples,
    );
  }
}
