import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing a classified advertisement.
class AdvertisementWritingSimulationWidget extends StatelessWidget {
  const AdvertisementWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'Classified advertisements are written in a ___ style.', correctWord: 'compressed, telegraphic', options: ['compressed, telegraphic', 'long, descriptive'], note: 'Newspaper column space is limited and charged by the word.'),
    CompletionExample(sentenceWithBlank: 'An advertisement for a flat should always include the ___.', correctWord: 'location, size, and contact details', options: ['location, size, and contact details', "owner's life story"], note: 'These are the details a prospective tenant/buyer actually needs.'),
    CompletionExample(sentenceWithBlank: 'A "Situations Vacant" advertisement should specify the ___.', correctWord: 'job role and required qualifications', options: ['job role and required qualifications', "hobbies of the employer"], note: 'Applicants need to know the role and whether they qualify.'),
    CompletionExample(sentenceWithBlank: 'Classified ads commonly ___.', correctWord: 'omit articles like "a/the" to save space', options: ['omit articles like "a/the" to save space', 'use full grammatical sentences throughout'], note: 'This telegraphic style is an accepted convention for classified ads.'),
    CompletionExample(sentenceWithBlank: 'Every classified advertisement must end with ___.', correctWord: 'contact information', options: ['contact information', 'a signature'], note: 'Without contact details, the ad cannot achieve its purpose.'),
    CompletionExample(sentenceWithBlank: 'The main goal of a classified ad is to convey maximum information in ___.', correctWord: 'the fewest possible words', options: ['the fewest possible words', 'as many words as possible'], note: 'Classified ads are charged per word, so brevity matters.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Classified Advertisement Writing',
      icon: Icons.campaign,
      accent: Colors.pink,
      description: 'Choose the correct convention for a classified advertisement.',
      examples: _examples,
    );
  }
}
