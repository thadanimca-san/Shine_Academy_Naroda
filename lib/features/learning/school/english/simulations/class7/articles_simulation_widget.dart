import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Pick a noun and see which article (a/an/the) fits, based on the
/// sound it starts with — including the classic exceptions like "hour"
/// and "university".
class ArticlesSimulationWidget extends StatefulWidget {
  const ArticlesSimulationWidget({super.key});

  @override
  State<ArticlesSimulationWidget> createState() => _ArticlesSimulationWidgetState();
}

class _ArticlesSimulationWidgetState extends State<ArticlesSimulationWidget> {
  static const _nouns = [
    ('cat', 'a', 'starts with the consonant sound /k/'),
    ('apple', 'an', 'starts with the vowel sound /æ/'),
    ('hour', 'an', 'the "h" is silent, so it starts with a vowel sound'),
    ('university', 'a', 'starts with the consonant sound /j/ (\'yoo\'), despite the vowel letter'),
    ('elephant', 'an', 'starts with the vowel sound /e/'),
    ('umbrella', 'an', 'starts with the vowel sound /ʌ/'),
    ('European', 'a', 'starts with the consonant sound /j/ (\'yoo\')'),
    ('orange', 'an', 'starts with the vowel sound /ɒ/'),
    ('table', 'a', 'starts with the consonant sound /t/'),
    ('honest man', 'an', 'the "h" is silent, so it starts with a vowel sound'),
  ];

  int _index = 0;
  String? _guess;

  @override
  Widget build(BuildContext context) {
    final (noun, correct, reason) = _nouns[_index];
    final isCorrect = _guess == correct;

    return SimFrame(
      title: 'A or An?',
      icon: Icons.spellcheck,
      accent: Colors.green.shade700,
      description: 'The choice between "a" and "an" depends on the sound, not the letter, at the start of the next word.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Text('___ $noun', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
              ],
            ),
          ),
          const SizedBox(height: 14),
          Row(
            children: ['a', 'an'].map((opt) {
              final isSelected = _guess == opt;
              Color? bg;
              if (_guess != null) {
                bg = opt == correct ? Colors.green.shade600 : (isSelected ? Colors.red.shade600 : null);
              }
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: ChoiceChip(
                    label: Text(opt, style: TextStyle(fontSize: 14, color: bg != null ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: Colors.green.shade700,
                    backgroundColor: bg ?? Colors.green.shade50,
                    onSelected: _guess == null ? (_) => setState(() => _guess = opt) : null,
                  ),
                ),
              );
            }).toList(),
          ),
          if (_guess != null) ...[
            const SizedBox(height: 10),
            Text(
              (isCorrect ? 'Correct! ' : 'Not quite — it\'s "$correct $noun". ') + reason,
              style: TextStyle(fontSize: 12.5, color: isCorrect ? Colors.green.shade700 : Colors.red.shade700),
            ),
          ],
          const SizedBox(height: 14),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () => setState(() {
                _index = (_index + 1) % _nouns.length;
                _guess = null;
              }),
              icon: Icon(Icons.arrow_forward),
              label: Text(TrilingualService.instance.getUIText('Next Word')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.green.shade700, foregroundColor: Colors.white),
            ),
          ),
        ],
      ),
    );
  }
}
