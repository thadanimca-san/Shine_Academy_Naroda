import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the modal verb that best expresses the required meaning
/// (obligation, possibility, ability, prohibition...) in each sentence.
class ModalsSimulationWidget extends StatelessWidget {
  const ModalsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'You ___ submit the form by Friday; it is compulsory.', correctWord: 'must', options: ['must', 'can', 'might'], note: '"Must" expresses strong obligation.'),
    CompletionExample(sentenceWithBlank: 'It ___ rain later; the sky looks cloudy.', correctWord: 'might', options: ['might', 'must', 'can'], note: '"Might" expresses weaker possibility.'),
    CompletionExample(sentenceWithBlank: 'You ___ worry, everything is under control.', correctWord: 'need not', options: ['need not', 'must not', 'cannot'], note: '"Need not" expresses absence of obligation.'),
    CompletionExample(sentenceWithBlank: 'You ___ smoke inside the hospital.', correctWord: 'must not', options: ['must not', 'need not', 'may not'], note: '"Must not" expresses prohibition.'),
    CompletionExample(sentenceWithBlank: 'When I was young, I ___ run very fast.', correctWord: 'could', options: ['could', 'can', 'must'], note: '"Could" expresses past ability.'),
    CompletionExample(sentenceWithBlank: 'Students ___ complete their homework daily.', correctWord: 'ought to', options: ['ought to', 'might', 'need not'], note: '"Ought to" expresses moral duty, like "should".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Choosing the Right Modal',
      icon: Icons.rule,
      accent: Colors.deepPurple,
      description: 'Pick the modal verb that best fits the meaning of each sentence.',
      examples: _examples,
    );
  }
}
