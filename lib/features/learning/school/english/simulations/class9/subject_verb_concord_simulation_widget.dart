import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the verb form that correctly agrees with a tricky subject
/// (collective nouns, indefinite pronouns, subjects joined by or/nor).
class SubjectVerbConcordSimulationWidget extends StatelessWidget {
  const SubjectVerbConcordSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'The team ___ playing very well this season.', correctWord: 'is', options: ['is', 'are'], note: 'A team acting as one unit takes a singular verb.'),
    CompletionExample(sentenceWithBlank: 'Neither the teacher nor the students ___ present.', correctWord: 'were', options: ['were', 'was'], note: 'With "neither...nor", the verb agrees with the nearer subject.'),
    CompletionExample(sentenceWithBlank: 'Everyone ___ submitted their assignment.', correctWord: 'has', options: ['has', 'have'], note: 'Indefinite pronouns like "everyone" take a singular verb.'),
    CompletionExample(sentenceWithBlank: 'The jury ___ divided in their opinions.', correctWord: 'are', options: ['are', 'is'], note: 'Here the jury members act individually, so the verb is plural.'),
    CompletionExample(sentenceWithBlank: 'Mathematics ___ my favourite subject.', correctWord: 'is', options: ['is', 'are'], note: 'Subject names ending in "-s" are treated as singular.'),
    CompletionExample(sentenceWithBlank: 'Each of the boys ___ a bicycle.', correctWord: 'has', options: ['has', 'have'], note: '"Each" takes a singular verb.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Subject-Verb Agreement Challenges',
      icon: Icons.compare_arrows,
      accent: Colors.teal,
      description: 'Pick the verb form that correctly agrees with the subject.',
      examples: _examples,
    );
  }
}
