import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the modal verb that correctly completes each board-style
/// sentence.
class ModalsBoardSimulationWidget extends StatelessWidget {
  const ModalsBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'If I had studied harder, I ___ passed the exam.', correctWord: 'would have', options: ['would have', 'would'], note: 'Unreal past conditionals use "would have" + past participle in the main clause.'),
    CompletionExample(sentenceWithBlank: '___ we begin the meeting now?', correctWord: 'Shall', options: ['Shall', 'Will'], note: '"Shall" is used for formal suggestions/offers.'),
    CompletionExample(sentenceWithBlank: 'You ___ finish this report by Friday; it is mandatory.', correctWord: 'have to', options: ['have to', 'may'], note: '"Have to" expresses external obligation.'),
    CompletionExample(sentenceWithBlank: 'He ___ have taken the wrong road; he is very late.', correctWord: 'must', options: ['must', 'can'], note: '"Must have" expresses a confident deduction about the past.'),
    CompletionExample(sentenceWithBlank: 'She ___ have called before visiting; it was rude of her not to.', correctWord: 'should', options: ['should', 'would'], note: '"Should have" expresses a past obligation that was not met.'),
    CompletionExample(sentenceWithBlank: '___ I use your phone for a moment?', correctWord: 'May', options: ['May', 'Must'], note: '"May" is used for polite requests of permission.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Modals (Board Level)',
      icon: Icons.gavel,
      accent: Colors.deepPurple,
      description: 'Choose the modal verb that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
