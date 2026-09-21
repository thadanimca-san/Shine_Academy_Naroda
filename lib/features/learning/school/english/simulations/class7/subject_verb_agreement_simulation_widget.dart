import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the verb form that correctly agrees with the subject in number.
class SubjectVerbAgreementSimulationWidget extends StatelessWidget {
  const SubjectVerbAgreementSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She ___ to school every day.', correctWord: 'walks', options: ['walk', 'walks'], note: '"She" is singular, so the verb takes -s.'),
    CompletionExample(sentenceWithBlank: 'The boys ___ football on Sundays.', correctWord: 'play', options: ['play', 'plays'], note: '"The boys" is plural, so the verb has no -s.'),
    CompletionExample(sentenceWithBlank: 'The team ___ practising for the finals.', correctWord: 'is', options: ['is', 'are'], note: '"Team" acts as a single unit, so it takes a singular verb.'),
    CompletionExample(sentenceWithBlank: 'Everyone ___ invited to the party.', correctWord: 'is', options: ['is', 'are'], note: 'Indefinite pronouns like "everyone" take a singular verb.'),
    CompletionExample(sentenceWithBlank: 'Neither of the answers ___ correct.', correctWord: 'is', options: ['is', 'are'], note: '"Neither" is treated as singular.'),
    CompletionExample(sentenceWithBlank: 'The scissors ___ on the table.', correctWord: 'are', options: ['is', 'are'], note: '"Scissors" is always treated as plural.'),
    CompletionExample(sentenceWithBlank: 'Mathematics ___ my favourite subject.', correctWord: 'is', options: ['is', 'are'], note: 'Subject names ending in -s, like "Mathematics", take a singular verb.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Subject-Verb Agreement',
      icon: Icons.check_circle_outline,
      accent: Colors.teal,
      description: 'Pick the verb form that correctly agrees with the subject.',
      examples: _examples,
    );
  }
}
