import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the word that correctly fixes the error or fills the omission
/// in each sentence.
class EditingOmissionAdvancedSimulationWidget extends StatelessWidget {
  const EditingOmissionAdvancedSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'He ___ like coffee.', correctWord: "doesn't", options: ["doesn't", "don't"], note: 'Third-person singular subjects take "doesn\'t" in the negative present simple.'),
    CompletionExample(sentenceWithBlank: 'She is interested ___ learning new languages.', correctWord: 'in', options: ['in', 'at'], note: '"Interested in" is the fixed preposition pairing.'),
    CompletionExample(sentenceWithBlank: 'Each of the students ___ submitted their project.', correctWord: 'has', options: ['has', 'have'], note: '"Each" takes a singular verb even when followed by a plural-looking phrase.'),
    CompletionExample(sentenceWithBlank: 'This is the ___ solution.', correctWord: 'best', options: ['best', 'most best'], note: '"Best" is already superlative; "most best" is a double superlative error.'),
    CompletionExample(sentenceWithBlank: 'Neither Ravi nor Sunil ___ present.', correctWord: 'was', options: ['was', 'were'], note: 'With "neither...nor", the verb agrees with the nearer subject, which is singular here.'),
    CompletionExample(sentenceWithBlank: 'The ___ in this room is old.', correctWord: 'furniture', options: ['furniture', 'furnitures'], note: '"Furniture" is an uncountable noun and has no plural form.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Editing and Omission (Advanced Practice)',
      icon: Icons.fact_check,
      accent: Colors.deepOrange,
      description: 'Choose the word that correctly fixes the error or fills the gap.',
      examples: _examples,
    );
  }
}
