import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Pick the correct synonym or antonym for the given word.
class SynonymsAntonymsSimulationWidget extends StatelessWidget {
  const SynonymsAntonymsSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: "Synonym of 'happy' is ___", correctWord: 'joyful', options: ['joyful', 'sad', 'angry'], note: '"Joyful" means the same as "happy".'),
    CompletionExample(sentenceWithBlank: "Antonym of 'happy' is ___", correctWord: 'sad', options: ['joyful', 'sad', 'cheerful'], note: '"Sad" means the opposite of "happy".'),
    CompletionExample(sentenceWithBlank: "Synonym of 'big' is ___", correctWord: 'large', options: ['large', 'tiny', 'small'], note: '"Large" means the same as "big".'),
    CompletionExample(sentenceWithBlank: "Antonym of 'big' is ___", correctWord: 'small', options: ['large', 'small', 'huge'], note: '"Small" means the opposite of "big".'),
    CompletionExample(sentenceWithBlank: "Synonym of 'brave' is ___", correctWord: 'courageous', options: ['courageous', 'cowardly', 'timid'], note: '"Courageous" means the same as "brave".'),
    CompletionExample(sentenceWithBlank: "Antonym of 'brave' is ___", correctWord: 'cowardly', options: ['courageous', 'cowardly', 'bold'], note: '"Cowardly" means the opposite of "brave".'),
    CompletionExample(sentenceWithBlank: "Synonym of 'ancient' is ___", correctWord: 'old', options: ['old', 'modern', 'new'], note: '"Old" means the same as "ancient".'),
    CompletionExample(sentenceWithBlank: "Antonym of 'ancient' is ___", correctWord: 'modern', options: ['old', 'modern', 'aged'], note: '"Modern" means the opposite of "ancient".'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Synonyms & Antonyms',
      icon: Icons.compare_arrows,
      accent: Colors.blueGrey,
      description: 'Pick the word that correctly matches the synonym or antonym asked for.',
      examples: _examples,
    );
  }
}
