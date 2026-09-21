import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correct present-tense verb form to complete each sentence.
class PresentTenseSimulationWidget extends StatelessWidget {
  const PresentTenseSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She ___ to school every day.', correctWord: 'walks', options: ['walk', 'walks', 'walking'], note: 'Simple present, third person singular: add -s.'),
    CompletionExample(sentenceWithBlank: 'They ___ football right now.', correctWord: 'are playing', options: ['play', 'are playing', 'played'], note: 'An action happening right now uses the present continuous tense.'),
    CompletionExample(sentenceWithBlank: 'I ___ already finished my homework.', correctWord: 'have', options: ['have', 'has', 'had'], note: 'Present perfect with "I" uses "have" + past participle.'),
    CompletionExample(sentenceWithBlank: 'Water ___ at 100°C.', correctWord: 'boils', options: ['boils', 'is boiling', 'boiled'], note: 'A scientific fact uses the simple present tense.'),
    CompletionExample(sentenceWithBlank: 'He ___ his teeth twice a day.', correctWord: 'brushes', options: ['brush', 'brushes', 'brushing'], note: 'Simple present, third person singular: add -es after "sh".'),
    CompletionExample(sentenceWithBlank: 'Look! It ___ heavily outside.', correctWord: 'is raining', options: ['rains', 'is raining', 'has rained'], note: '"Look!" signals something happening right now — present continuous.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Complete with the Present Tense',
      icon: Icons.today,
      accent: Colors.blue,
      description: 'Pick the verb form that correctly completes each sentence.',
      examples: _examples,
    );
  }
}
