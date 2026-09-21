import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct perfect-tense verb form (present/past/future perfect).
class PerfectTensesSimulationWidget extends StatelessWidget {
  const PerfectTensesSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'I ___ my homework already.', correctWord: 'have finished', options: ['have finished', 'finished', 'will finish'], note: 'Present perfect: action completed with present relevance.'),
    CompletionExample(sentenceWithBlank: 'She ___ to Paris three times.', correctWord: 'has been', options: ['has been', 'was', 'is'], note: 'Present perfect for repeated experience up to now.'),
    CompletionExample(sentenceWithBlank: 'The train ___ before we reached the station.', correctWord: 'had left', options: ['had left', 'has left', 'left'], note: 'Past perfect: earlier of two past actions.'),
    CompletionExample(sentenceWithBlank: 'By next year, I ___ this course.', correctWord: 'will have completed', options: ['will have completed', 'will complete', 'have completed'], note: 'Future perfect: action complete before a future point.'),
    CompletionExample(sentenceWithBlank: 'He ___ already ___ when I called.', correctWord: 'had eaten', options: ['had eaten', 'has eaten', 'ate'], note: 'Past perfect for an action before another past action.'),
    CompletionExample(sentenceWithBlank: 'We ___ here since morning.', correctWord: 'have been waiting', options: ['have been waiting', 'were waiting', 'wait'], note: 'Present perfect continuous for an ongoing action from the past.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Perfect Tense Forms',
      icon: Icons.history,
      accent: Colors.brown,
      description: 'Pick the correct perfect-tense form to complete each sentence.',
      examples: _examples,
    );
  }
}
