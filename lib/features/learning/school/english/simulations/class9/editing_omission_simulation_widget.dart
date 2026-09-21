import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct word to fix the grammatical error or fill the
/// omission in each sentence.
class EditingOmissionSimulationWidget extends StatelessWidget {
  const EditingOmissionSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He ___ to school daily.', correctWord: 'goes', options: ['goes', 'go'], note: 'Third-person singular subjects take "-s/-es" verb forms in the present simple.'),
    CompletionExample(sentenceWithBlank: 'He is fond ___ music.', correctWord: 'of', options: ['of', 'in'], note: '"Fond of" is the correct fixed preposition.'),
    CompletionExample(sentenceWithBlank: 'They ___ playing football.', correctWord: 'were', options: ['were', 'was'], note: '"They" (plural) takes "were", not "was".'),
    CompletionExample(sentenceWithBlank: 'I have been living here ___ 2010.', correctWord: 'since', options: ['since', 'from'], note: '"Since" is used with a specific starting point in time.'),
    CompletionExample(sentenceWithBlank: 'Each of the boys ___ present.', correctWord: 'was', options: ['was', 'were'], note: '"Each" takes a singular verb even when followed by "of the boys".'),
    CompletionExample(sentenceWithBlank: 'He has ___ home.', correctWord: 'gone', options: ['gone', 'went'], note: 'The present perfect uses the past participle "gone", not "went".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Spot and Fix the Error',
      icon: Icons.edit_note,
      accent: Colors.red,
      description: 'Choose the word that correctly fixes the error or fills the gap.',
      examples: _examples,
    );
  }
}
