import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct infinitive structure when a direct command or
/// request is transformed into reported speech.
class ReportedSpeechCommandsSimulationWidget extends StatelessWidget {
  const ReportedSpeechCommandsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He said, "Sit down." → He ordered me ___ down.', correctWord: 'to sit', options: ['to sit', 'sit'], note: 'Commands are reported with "to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'She said, "Please help me." → She requested me ___ her.', correctWord: 'to help', options: ['to help', 'help'], note: 'Requests are reported with "to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'The teacher said, "Do not talk in class." → The teacher ordered us ___ in class.', correctWord: 'not to talk', options: ['not to talk', 'to not talk'], note: 'Negative commands use "not to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'The doctor said, "Take rest." → The doctor advised me ___ rest.', correctWord: 'to take', options: ['to take', 'take'], note: 'Advice is reported using "advised" + "to" + base verb.'),
    CompletionExample(sentenceWithBlank: 'He said, "Please do not shout." → He requested me ___.', correctWord: 'not to shout', options: ['not to shout', 'to not shout'], note: '"Not to" comes before the base verb, not after "to".'),
    CompletionExample(sentenceWithBlank: 'The captain said, "March forward." → The captain commanded the soldiers ___ forward.', correctWord: 'to march', options: ['to march', 'march'], note: 'Commands are reported with "to" + base verb.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Reporting Commands and Requests',
      icon: Icons.campaign,
      accent: Colors.deepOrange,
      description: 'Choose the correctly reported form of each command or request.',
      examples: _examples,
    );
  }
}
