import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct rule of notice-writing format for each prompt.
class NoticeWritingSimulationWidget extends StatelessWidget {
  const NoticeWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A notice must always be ___.', correctWord: 'enclosed in a box', options: ['enclosed in a box', 'written in a paragraph without a border'], note: 'A box clearly separates the notice from surrounding text on a noticeboard.'),
    CompletionExample(sentenceWithBlank: 'A notice should be written in ___ language.', correctWord: 'formal, impersonal', options: ['formal, impersonal', 'casual, personal'], note: 'Notices are official announcements, so they avoid a personal tone.'),
    CompletionExample(sentenceWithBlank: 'A notice is usually restricted to about ___.', correctWord: '50 words', options: ['50 words', '500 words'], note: 'Notices must be brief so they can be read quickly on a board.'),
    CompletionExample(sentenceWithBlank: 'The word "NOTICE" is typically written ___.', correctWord: 'at the top, centred and underlined', options: ['at the top, centred and underlined', 'at the very end'], note: 'This makes the notice instantly recognisable at a glance.'),
    CompletionExample(sentenceWithBlank: 'The name and designation of the issuing authority appear ___.', correctWord: 'at the bottom right', options: ['at the bottom right', 'nowhere'], note: 'This tells readers who is responsible for the notice.'),
    CompletionExample(sentenceWithBlank: 'A notice should avoid using ___ in its body.', correctWord: 'the pronoun "I" (unless issued personally)', options: ['the pronoun "I" (unless issued personally)', 'dates'], note: 'Notices are impersonal, official communications, not personal statements.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Notice Writing',
      icon: Icons.announcement,
      accent: Colors.orange,
      description: 'Choose the rule that correctly completes each notice-writing guideline.',
      examples: _examples,
    );
  }
}
