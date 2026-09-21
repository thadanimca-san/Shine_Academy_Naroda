import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct salutation, closing, or convention for a formal or
/// informal letter.
class LettersFormalInformalSimulationWidget extends StatelessWidget {
  const LettersFormalInformalSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A formal letter to an unknown authority opens with ___.', correctWord: 'Dear Sir/Madam', options: ['Dear Sir/Madam', 'Dear Friend'], note: 'This is the standard neutral formal salutation when the recipient\'s name is unknown.'),
    CompletionExample(sentenceWithBlank: 'A formal letter beginning with "Dear Sir/Madam" should close with ___.', correctWord: 'Yours faithfully', options: ['Yours faithfully', 'Yours sincerely'], note: '"Yours faithfully" pairs with an impersonal salutation.'),
    CompletionExample(sentenceWithBlank: 'A formal letter addressed to a named person should close with ___.', correctWord: 'Yours sincerely', options: ['Yours sincerely', 'Yours faithfully'], note: '"Yours sincerely" pairs with a named salutation like "Dear Mr. Sharma".'),
    CompletionExample(sentenceWithBlank: 'The ___ briefly states the purpose of a formal letter, before the salutation.', correctWord: 'subject line', options: ['subject line', 'postscript'], note: 'The subject line lets the reader instantly know the letter\'s purpose.'),
    CompletionExample(sentenceWithBlank: 'An informal letter to a friend may close with ___.', correctWord: 'Yours affectionately', options: ['Yours affectionately', 'Yours faithfully'], note: 'Informal closings are warmer and more personal.'),
    CompletionExample(sentenceWithBlank: 'A formal letter should maintain a ___ tone throughout.', correctWord: 'respectful, impersonal', options: ['respectful, impersonal', 'casual, personal'], note: 'Formal letters represent official communication and avoid casual language.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Formal and Informal Letters',
      icon: Icons.mail_outline,
      accent: Colors.blue,
      description: 'Choose the correct salutation, closing, or convention.',
      examples: _examples,
    );
  }
}
