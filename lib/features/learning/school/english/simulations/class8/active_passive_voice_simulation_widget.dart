import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correctly transformed passive-voice verb form for each sentence.
class ActivePassiveVoiceSimulationWidget extends StatelessWidget {
  const ActivePassiveVoiceSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'The cake ___ by my mother.', correctWord: 'was baked', options: ['was baked', 'baked', 'bakes'], note: 'Passive: object of the active sentence becomes the subject.'),
    CompletionExample(sentenceWithBlank: 'The letter ___ tomorrow.', correctWord: 'will be posted', options: ['will be posted', 'will post', 'posted'], note: 'Future passive: "will be + past participle".'),
    CompletionExample(sentenceWithBlank: 'English ___ in many countries.', correctWord: 'is spoken', options: ['is spoken', 'speaks', 'spoke'], note: 'Present simple passive: "is/are + past participle".'),
    CompletionExample(sentenceWithBlank: 'The window ___ by the boy yesterday.', correctWord: 'was broken', options: ['was broken', 'broke', 'is broken'], note: 'Past simple passive: "was/were + past participle".'),
    CompletionExample(sentenceWithBlank: 'The homework ___ by the students already.', correctWord: 'has been done', options: ['has been done', 'has done', 'did'], note: 'Present perfect passive: "has/have been + past participle".'),
    CompletionExample(sentenceWithBlank: 'The project ___ by the team right now.', correctWord: 'is being completed', options: ['is being completed', 'completes', 'was completed'], note: 'Present continuous passive: "is/are being + past participle".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Active to Passive Voice',
      icon: Icons.swap_horiz,
      accent: Colors.indigo,
      description: 'Pick the correctly transformed passive-voice form of the verb.',
      examples: _examples,
    );
  }
}
