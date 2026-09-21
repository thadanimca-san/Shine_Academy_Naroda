import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct relative pronoun to complete each adjective clause.
class AdjectiveClausesSimulationWidget extends StatelessWidget {
  const AdjectiveClausesSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'The man ___ called yesterday is my uncle.', correctWord: 'who', options: ['who', 'which'], note: '"Who" refers to people.'),
    CompletionExample(sentenceWithBlank: 'This is the book ___ I bought last week.', correctWord: 'that', options: ['that', 'who'], note: '"That" can refer to things.'),
    CompletionExample(sentenceWithBlank: 'The girl ___ bag was stolen informed the police.', correctWord: 'whose', options: ['whose', 'who'], note: '"Whose" shows possession.'),
    CompletionExample(sentenceWithBlank: 'The car, ___ was parked outside, belongs to my father.', correctWord: 'which', options: ['which', 'who'], note: '"Which" refers to things, not people.'),
    CompletionExample(sentenceWithBlank: 'The woman ___ I met yesterday is a doctor.', correctWord: 'whom', options: ['whom', 'which'], note: '"Whom" is used for people as the object of the clause.'),
    CompletionExample(sentenceWithBlank: 'This is the house ___ I was born.', correctWord: 'where', options: ['where', 'which'], note: '"Where" introduces a clause about a place.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Relative Pronouns in Adjective Clauses',
      icon: Icons.link,
      accent: Colors.green,
      description: 'Choose the relative pronoun that correctly completes each adjective clause.',
      examples: _examples,
    );
  }
}
