import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing a speech or debate.
class SpeechWritingSimulationWidget extends StatelessWidget {
  const SpeechWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A speech should open with a ___.', correctWord: 'respectful address to the audience', options: ['respectful address to the audience', 'list of statistics'], note: 'Addressing the audience respectfully is a speech-writing convention.'),
    CompletionExample(sentenceWithBlank: 'A speech must be written to ___.', correctWord: 'sound natural when read aloud', options: ['sound natural when read aloud', 'be skimmed silently'], note: 'A speech is meant to be delivered orally, so it must flow when spoken.'),
    CompletionExample(sentenceWithBlank: 'A debate speech must take a clear ___ on the motion.', correctWord: '"for" or "against" stance', options: ['"for" or "against" stance', 'neutral, undecided stance'], note: 'Debates require a definite position to argue for.'),
    CompletionExample(sentenceWithBlank: 'A strong debate speech should ___.', correctWord: 'anticipate and address counter-arguments', options: ['anticipate and address counter-arguments', 'ignore the opposing side entirely'], note: 'Addressing counter-arguments makes a debate speech more persuasive.'),
    CompletionExample(sentenceWithBlank: 'A speech should end with a ___.', correctWord: 'strong, memorable conclusion', options: ['strong, memorable conclusion', 'abrupt stop with no closing'], note: 'A memorable ending helps the message stay with the audience.'),
    CompletionExample(sentenceWithBlank: 'A good speech opening should include a ___.', correctWord: 'hook to capture attention', options: ['hook to capture attention', 'disclaimer about length'], note: 'A hook draws the audience in from the very first line.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Speech and Debate Writing',
      icon: Icons.record_voice_over,
      accent: Colors.deepPurple,
      description: 'Choose the correct convention for speech/debate writing.',
      examples: _examples,
    );
  }
}
