import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing a report.
class ReportWritingSimulationWidget extends StatelessWidget {
  const ReportWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A newspaper report must begin with a ___ that summarises the event.', correctWord: 'headline', options: ['headline', 'salutation'], note: 'A headline lets readers instantly know what the report is about.'),
    CompletionExample(sentenceWithBlank: 'The byline of a report includes the ___.', correctWord: "reporter's name and place", options: ["reporter's name and place", "reader's name"], note: 'The byline credits and locates the person who filed the report.'),
    CompletionExample(sentenceWithBlank: 'Reports are typically written in the ___.', correctWord: 'past tense, third person', options: ['past tense, third person', 'present tense, first person'], note: 'Reports describe events that have already happened, from an outside perspective.'),
    CompletionExample(sentenceWithBlank: 'A report should present the most essential information ___.', correctWord: 'first', options: ['first', 'last'], note: 'This is the "inverted pyramid" style used in journalism.'),
    CompletionExample(sentenceWithBlank: 'Unlike an article, a report avoids ___.', correctWord: "the writer's personal opinions", options: ["the writer's personal opinions", 'factual details'], note: 'A report is meant to be objective and fact-based.'),
    CompletionExample(sentenceWithBlank: 'A report should maintain an ___ tone throughout.', correctWord: 'objective, factual', options: ['objective, factual', 'emotional, persuasive'], note: 'Objectivity keeps the report credible and trustworthy.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Report Writing',
      icon: Icons.description,
      accent: Colors.blueGrey,
      description: 'Choose the correct convention for report writing.',
      examples: _examples,
    );
  }
}
