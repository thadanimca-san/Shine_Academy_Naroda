import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the meaning that correctly matches each board-level idiom or
/// phrasal verb.
class IdiomsPhrasalVerbsBoardSimulationWidget extends StatelessWidget {
  const IdiomsPhrasalVerbsBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'To "hit the books" means to ___.', correctWord: 'study hard', options: ['study hard', 'relax'], note: 'This idiom describes studying with focus and effort.'),
    CompletionExample(sentenceWithBlank: 'To "beat around the bush" means to ___.', correctWord: 'avoid the main point', options: ['avoid the main point', 'speak directly'], note: 'This idiom describes avoiding a direct answer or topic.'),
    CompletionExample(sentenceWithBlank: 'To "keep an eye on" something means to ___.', correctWord: 'watch it carefully', options: ['watch it carefully', 'ignore it'], note: 'This phrase means to monitor or supervise something closely.'),
    CompletionExample(sentenceWithBlank: 'To "come across" something means to ___.', correctWord: 'find it by chance', options: ['find it by chance', 'search for it deliberately'], note: '"Come across" implies an unplanned discovery.'),
    CompletionExample(sentenceWithBlank: '"Once in a blue moon" means ___.', correctWord: 'very rarely', options: ['very rarely', 'very often'], note: 'This idiom describes something that happens very infrequently.'),
    CompletionExample(sentenceWithBlank: 'To "break the ice" means to ___.', correctWord: 'ease tension in a social situation', options: ['ease tension in a social situation', 'cause a conflict'], note: 'This idiom describes making people feel more comfortable at the start of an interaction.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Idioms and Phrasal Verbs (Board Level)',
      icon: Icons.chat_bubble,
      accent: Colors.cyan,
      description: 'Choose the correct meaning of each idiom or phrasal verb.',
      examples: _examples,
    );
  }
}
