import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly fixes the error or fills the omission
/// in each board-style sentence.
class EditingOmissionBoardSimulationWidget extends StatelessWidget {
  const EditingOmissionBoardSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He has ___ to the market.', correctWord: 'gone', options: ['gone', 'went'], note: 'The present perfect requires the past participle "gone", not "went".'),
    CompletionExample(sentenceWithBlank: 'She is responsible ___ the mistake.', correctWord: 'for', options: ['for', 'of'], note: '"Responsible for" is the fixed preposition pairing.'),
    CompletionExample(sentenceWithBlank: 'One of the boys ___ late.', correctWord: 'was', options: ['was', 'were'], note: '"One" is singular, so it takes the singular verb "was".'),
    CompletionExample(sentenceWithBlank: 'This is a ___ idea.', correctWord: 'unique', options: ['unique', 'most unique'], note: '"Unique" is an absolute adjective and cannot be compared with "most".'),
    CompletionExample(sentenceWithBlank: 'The news ___ shocking.', correctWord: 'was', options: ['was', 'were'], note: '"News" is treated as a singular uncountable noun.'),
    CompletionExample(sentenceWithBlank: 'She has been suffering from fever ___ three days.', correctWord: 'for', options: ['for', 'since'], note: '"For" is used with a duration of time, not a starting point.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Editing and Omission (Board Level)',
      icon: Icons.fact_check,
      accent: Colors.deepOrange,
      description: 'Choose the word that correctly fixes the error or fills the gap.',
      examples: _examples,
    );
  }
}
