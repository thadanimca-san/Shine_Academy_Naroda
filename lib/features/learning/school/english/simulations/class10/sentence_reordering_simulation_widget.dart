import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct word to complete a jumbled sentence once it has
/// been reordered.
class SentenceReorderingSimulationWidget extends StatelessWidget {
  const SentenceReorderingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Jumbled: "playground / children / the / in / are / playing" begins with ___.', correctWord: 'The', options: ['The', 'Children'], note: 'A capitalised word in a jumbled set is usually the first word.'),
    CompletionExample(sentenceWithBlank: '"quickly / she / ran / home" correctly orders as "She ran home ___".', correctWord: 'quickly', options: ['quickly', 'she'], note: 'Adverbs of manner typically come after the verb and object.'),
    CompletionExample(sentenceWithBlank: 'A jumbled interrogative sentence usually begins with a ___.', correctWord: 'wh-word or auxiliary', options: ['wh-word or auxiliary', 'adjective'], note: 'Questions begin with a wh-word (what, where) or an auxiliary verb (do, is).'),
    CompletionExample(sentenceWithBlank: 'In a simple declarative sentence, the ___ usually comes first.', correctWord: 'subject', options: ['subject', 'object'], note: 'Standard English word order is Subject–Verb–Object.'),
    CompletionExample(sentenceWithBlank: '"fast / cheetah / runs / the / very" correctly orders as "The cheetah runs very ___".', correctWord: 'fast', options: ['fast', 'cheetah'], note: 'The adverb "fast" describes how the cheetah runs and comes last.'),
    CompletionExample(sentenceWithBlank: 'In "must / homework / you / finish / your", the modal verb "must" comes ___.', correctWord: 'after the subject', options: ['after the subject', 'before the subject'], note: 'Modals follow the subject and precede the main verb: "You must finish".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Sentence Reordering (Jumbled Words)',
      icon: Icons.reorder,
      accent: Colors.teal,
      description: 'Choose the word that correctly completes the reordered sentence.',
      examples: _examples,
    );
  }
}
