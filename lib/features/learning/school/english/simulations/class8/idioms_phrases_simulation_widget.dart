import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the idiom/phrase that correctly completes the sentence's meaning.
class IdiomsPhrasesSimulationWidget extends StatelessWidget {
  const IdiomsPhrasesSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'It is raining heavily; it is ___ outside.', correctWord: 'raining cats and dogs', options: ['raining cats and dogs', 'once in a blue moon', 'a piece of cake'], note: '"Raining cats and dogs" means raining very heavily.'),
    CompletionExample(sentenceWithBlank: 'The exam was so easy, it was ___.', correctWord: 'a piece of cake', options: ['a piece of cake', 'under the weather', 'burning the midnight oil'], note: '"A piece of cake" means something very easy.'),
    CompletionExample(sentenceWithBlank: 'He has been ___ to finish the project on time.', correctWord: 'burning the midnight oil', options: ['burning the midnight oil', 'a piece of cake', 'break the ice'], note: '"Burning the midnight oil" means working late into the night.'),
    CompletionExample(sentenceWithBlank: 'She felt ___ after catching a cold.', correctWord: 'under the weather', options: ['under the weather', 'once in a blue moon', 'raining cats and dogs'], note: '"Under the weather" means feeling slightly unwell.'),
    CompletionExample(sentenceWithBlank: 'We should ___ before starting the meeting.', correctWord: 'break the ice', options: ['break the ice', 'a piece of cake', 'burning the midnight oil'], note: '"Break the ice" means to ease tension at the start of a gathering.'),
    CompletionExample(sentenceWithBlank: 'He visits his grandparents ___.', correctWord: 'once in a blue moon', options: ['once in a blue moon', 'break the ice', 'under the weather'], note: '"Once in a blue moon" means very rarely.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Idioms and Phrases',
      icon: Icons.emoji_objects,
      accent: Colors.deepPurple,
      description: 'Choose the idiom that best matches the meaning of the sentence.',
      examples: _examples,
    );
  }
}
