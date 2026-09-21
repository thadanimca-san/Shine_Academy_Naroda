import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the modal verb that correctly completes each sentence.
class ModalsAdvancedSimulationWidget extends StatelessWidget {
  const ModalsAdvancedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'You ___ wear a helmet while riding — it is the law.', correctWord: 'must', options: ['must', 'need not'], note: '"Must" expresses strong obligation.'),
    CompletionExample(sentenceWithBlank: 'You ___ come if you are busy; it is not compulsory.', correctWord: 'need not', options: ['need not', 'must not'], note: '"Need not" expresses absence of obligation, unlike "must not" (prohibition).'),
    CompletionExample(sentenceWithBlank: 'She ___ studied harder; she failed the exam.', correctWord: 'should have', options: ['should have', 'must have'], note: '"Should have" expresses a past missed obligation or regret.'),
    CompletionExample(sentenceWithBlank: 'He is not in his office; he ___ gone home.', correctWord: 'must have', options: ['must have', 'should have'], note: '"Must have" expresses a confident deduction about the past.'),
    CompletionExample(sentenceWithBlank: 'It ___ rain later, though the forecast is unclear.', correctWord: 'might', options: ['might', 'must'], note: '"Might" expresses a weaker possibility than "must".'),
    CompletionExample(sentenceWithBlank: 'You ___ smoke in this hospital — it is strictly prohibited.', correctWord: 'must not', options: ['must not', 'need not'], note: '"Must not" expresses prohibition.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Modals (Advanced Usage)',
      icon: Icons.gavel,
      accent: Colors.deepPurple,
      description: 'Choose the modal verb that correctly completes the sentence.',
      examples: _examples,
    );
  }
}
