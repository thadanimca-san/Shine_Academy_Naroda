import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the pronoun that correctly fits the sentence, based on its
/// antecedent and grammatical role.
class PronounsSimulationWidget extends StatelessWidget {
  const PronounsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Priya lost ___ pencil.', correctWord: 'her', options: ['her', 'him', 'their'], note: '"Priya" is female and singular, so the possessive pronoun is "her".'),
    CompletionExample(sentenceWithBlank: 'The boys forgot ___ bags.', correctWord: 'their', options: ['his', 'their', 'its'], note: '"The boys" is plural, so the possessive pronoun is "their".'),
    CompletionExample(sentenceWithBlank: 'This book is ___, not yours.', correctWord: 'mine', options: ['mine', 'my', 'me'], note: '"Mine" stands alone as a possessive pronoun; "my" would need a noun after it.'),
    CompletionExample(sentenceWithBlank: 'He hurt ___ while playing.', correctWord: 'himself', options: ['himself', 'him', 'his'], note: 'A reflexive pronoun is needed because the subject and object are the same person.'),
    CompletionExample(sentenceWithBlank: '___ is the man who helped us?', correctWord: 'Who', options: ['Who', 'Whom', 'Whose'], note: '"Who" is used as the subject of the question.'),
    CompletionExample(sentenceWithBlank: 'The dog wagged ___ tail.', correctWord: 'its', options: ['its', "it's", 'their'], note: '"Its" (no apostrophe) is the possessive form; "it\'s" means "it is".'),
    CompletionExample(sentenceWithBlank: 'The cake, ___ Mom baked, was delicious.', correctWord: 'which', options: ['which', 'who', 'whom'], note: '"Which" is used as a relative pronoun for things, not people.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Choose the Correct Pronoun',
      icon: Icons.person,
      accent: Colors.teal,
      description: 'Pick the pronoun that correctly fits each sentence.',
      examples: _examples,
    );
  }
}
