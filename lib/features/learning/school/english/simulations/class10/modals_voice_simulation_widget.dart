import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct passive form of a modal-verb sentence.
class ModalsVoiceSimulationWidget extends StatelessWidget {
  const ModalsVoiceSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Active: You must complete this form. Passive: This form ___ by you.', correctWord: 'must be completed', options: ['must be completed', 'must completed'], note: 'The passive modal structure is modal + "be" + past participle.'),
    CompletionExample(sentenceWithBlank: 'Active: We can solve this problem. Passive: This problem ___ by us.', correctWord: 'can be solved', options: ['can be solved', 'can solved'], note: 'The modal "can" does not change form; only "be solved" is added.'),
    CompletionExample(sentenceWithBlank: 'Active: He might have completed the task. Passive: The task ___ by him.', correctWord: 'might have been completed', options: ['might have been completed', 'might be completed'], note: 'A modal perfect ("might have completed") becomes modal + "have been" + past participle.'),
    CompletionExample(sentenceWithBlank: 'Active: You need not worry about this. Passive: This ___ worried about.', correctWord: 'need not be', options: ['need not be', 'need not'], note: 'The modal "need not" is followed by "be" before the past participle.'),
    CompletionExample(sentenceWithBlank: 'Active: You cannot ignore this issue. Passive: This issue ___.', correctWord: 'cannot be ignored', options: ['cannot be ignored', 'cannot ignored'], note: 'Negative modals keep the same structure: modal + "be" + past participle.'),
    CompletionExample(sentenceWithBlank: 'Active: They will have completed the survey by June. Passive: The survey ___ by June.', correctWord: 'will have been completed', options: ['will have been completed', 'will be completed'], note: 'The future perfect passive is "will have been" + past participle.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Modals and Voice: Combined Practice',
      icon: Icons.swap_horiz,
      accent: Colors.deepPurple,
      description: 'Choose the correctly formed passive sentence.',
      examples: _examples,
    );
  }
}
