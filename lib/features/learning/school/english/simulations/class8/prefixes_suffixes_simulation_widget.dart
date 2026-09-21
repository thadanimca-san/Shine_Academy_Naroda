import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correctly formed word using a prefix or suffix.
class PrefixesSuffixesSimulationWidget extends StatelessWidget {
  const PrefixesSuffixesSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'What he did was completely ___.', correctWord: 'unfair', options: ['unfair', 'disfair', 'infair'], note: 'The prefix "un-" is used with "fair" to mean "not fair".'),
    CompletionExample(sentenceWithBlank: 'She showed great ___ during the crisis.', correctWord: 'kindness', options: ['kindness', 'kindful', 'kindity'], note: 'The suffix "-ness" turns the adjective "kind" into a noun.'),
    CompletionExample(sentenceWithBlank: 'His answer was completely ___.', correctWord: 'incorrect', options: ['incorrect', 'uncorrect', 'discorrect'], note: 'The prefix "in-" is used with "correct" to mean "not correct".'),
    CompletionExample(sentenceWithBlank: 'The magician made the coin ___.', correctWord: 'disappear', options: ['disappear', 'unappear', 'misappear'], note: 'The prefix "dis-" is used with "appear" to mean the opposite.'),
    CompletionExample(sentenceWithBlank: 'It is important to act ___ in an emergency.', correctWord: 'responsibly', options: ['responsibly', 'responsibness', 'responsibful'], note: 'The suffix "-ly" turns the adjective "responsible" into an adverb.'),
    CompletionExample(sentenceWithBlank: 'His behaviour in class was quite ___.', correctWord: 'childish', options: ['childish', 'childful', 'childness'], note: 'The suffix "-ish" gives the meaning "somewhat like".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Prefixes and Suffixes',
      icon: Icons.text_fields,
      accent: Colors.orange,
      description: 'Pick the correctly formed word using a prefix or suffix.',
      examples: _examples,
    );
  }
}
