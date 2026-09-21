import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing an article.
class ArticleWritingSimulationWidget extends StatelessWidget {
  const ArticleWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'An article should begin with a ___ that grabs the reader\'s attention.', correctWord: 'catchy title', options: ['catchy title', 'list of statistics'], note: 'A strong title draws the reader in before they even start reading.'),
    CompletionExample(sentenceWithBlank: 'The introduction of an article should ___.', correctWord: 'state the topic and hook the reader', options: ['state the topic and hook the reader', 'list the conclusion first'], note: 'The opening should orient the reader and spark their interest.'),
    CompletionExample(sentenceWithBlank: 'Compared to a report, an article is written in a more ___ tone.', correctWord: 'personal, persuasive', options: ['personal, persuasive', 'strictly factual'], note: 'Articles often reflect the writer\'s own views and voice.'),
    CompletionExample(sentenceWithBlank: 'An article should be organised into ___.', correctWord: 'clear paragraphs with logical flow', options: ['clear paragraphs with logical flow', 'one unbroken block of text'], note: 'Clear paragraphing helps the reader follow the argument.'),
    CompletionExample(sentenceWithBlank: 'An article on a social issue should ideally end with ___.', correctWord: 'a call to action or reflection', options: ['a call to action or reflection', 'an unrelated joke'], note: 'A strong ending leaves the reader with something to think about or do.'),
    CompletionExample(sentenceWithBlank: 'Unlike a formal letter, an article does not require a ___.', correctWord: 'salutation and complimentary close', options: ['salutation and complimentary close', 'title'], note: 'Articles are addressed to a general readership, not one recipient.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Article Writing',
      icon: Icons.article,
      accent: Colors.indigo,
      description: 'Choose the correct convention for article writing.',
      examples: _examples,
    );
  }
}
