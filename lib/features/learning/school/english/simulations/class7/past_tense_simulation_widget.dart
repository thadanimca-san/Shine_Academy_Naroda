import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correct past-tense verb form to complete each sentence.
class PastTenseSimulationWidget extends StatelessWidget {
  const PastTenseSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'She ___ to the market yesterday.', correctWord: 'went', options: ['go', 'went', 'gone'], note: '"Went" is the simple past form of the irregular verb "go".'),
    CompletionExample(sentenceWithBlank: 'While I ___ dinner, the phone rang.', correctWord: 'was cooking', options: ['cooked', 'was cooking', 'have cooked'], note: 'An ongoing past action interrupted by another uses past continuous.'),
    CompletionExample(sentenceWithBlank: 'By the time we arrived, the movie ___ already started.', correctWord: 'had', options: ['had', 'has', 'was'], note: 'An action completed before another past action uses the past perfect: had + past participle.'),
    CompletionExample(sentenceWithBlank: 'He ___ his homework last night.', correctWord: 'finished', options: ['finish', 'finishes', 'finished'], note: 'Regular verbs form the simple past by adding -ed.'),
    CompletionExample(sentenceWithBlank: 'They ___ playing when it started to rain.', correctWord: 'were', options: ['was', 'were', 'are'], note: '"They" (plural) uses "were" in the past continuous tense.'),
    CompletionExample(sentenceWithBlank: 'I ___ not see you at the party.', correctWord: 'did', options: ['did', 'does', 'was'], note: 'Negative simple past sentences use "did not" for all subjects.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Complete with the Past Tense',
      icon: Icons.history,
      accent: Colors.brown,
      description: 'Pick the verb form that correctly completes each sentence.',
      examples: _examples,
    );
  }
}
