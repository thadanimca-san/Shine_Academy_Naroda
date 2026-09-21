import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correctly transformed passive form across a range of tenses,
/// including perfect and modal passives.
class ActivePassiveAllTensesSimulationWidget extends StatelessWidget {
  const ActivePassiveAllTensesSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Active: They build houses. Passive: Houses ___ by them.', correctWord: 'are built', options: ['are built', 'built'], note: 'Present simple passive: "is/are + past participle".'),
    CompletionExample(sentenceWithBlank: 'Active: They are watching a film. Passive: A film ___ by them.', correctWord: 'is being watched', options: ['is being watched', 'was watched'], note: 'Present continuous passive: "is/are being + past participle".'),
    CompletionExample(sentenceWithBlank: 'Active: He has completed the task. Passive: The task ___ by him.', correctWord: 'has been completed', options: ['has been completed', 'was completed'], note: 'Present perfect passive: "has/have been + past participle".'),
    CompletionExample(sentenceWithBlank: 'Active: You must finish this work. Passive: This work ___ by you.', correctWord: 'must be finished', options: ['must be finished', 'is finished'], note: 'Modal passive: modal + "be" + past participle.'),
    CompletionExample(sentenceWithBlank: 'Active: They had sold the shop. Passive: The shop ___ by them.', correctWord: 'had been sold', options: ['had been sold', 'was sold'], note: 'Past perfect passive: "had been + past participle".'),
    CompletionExample(sentenceWithBlank: 'Active: I will have finished the project by then. Passive: The project ___ by then.', correctWord: 'will have been finished', options: ['will have been finished', 'will be finished'], note: 'Future perfect passive: "will have been + past participle".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Passive Voice Across Tenses',
      icon: Icons.swap_horiz,
      accent: Colors.indigo,
      description: 'Choose the correctly transformed passive-voice form of the verb.',
      examples: _examples,
    );
  }
}
