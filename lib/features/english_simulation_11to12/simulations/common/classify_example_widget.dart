import 'package:flutter/material.dart';
import 'sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// One example sentence with a highlighted word/phrase and its correct
/// classification out of a shared set of category options.
class ClassifyExample {
  final String sentence;
  final String highlight;
  final String correctType;

  const ClassifyExample({required this.sentence, required this.highlight, required this.correctType});
}

/// A reusable "read the sentence, classify the highlighted word" grammar
/// drill: shows one example at a time with multiple-choice category
/// chips, checks the answer, then lets the student move to the next one.
/// Used across many grammar topics (nouns, verbs, adverbs, sentence
/// kinds, etc.) so each chapter only needs to supply its example list.
class ClassifyExampleWidget extends StatefulWidget {
  final String title;
  final IconData icon;
  final Color accent;
  final String description;
  final List<ClassifyExample> examples;
  final List<String> options;

  const ClassifyExampleWidget({
    super.key,
    required this.title,
    required this.icon,
    required this.accent,
    required this.description,
    required this.examples,
    required this.options,
  });

  @override
  State<ClassifyExampleWidget> createState() => _ClassifyExampleWidgetState();
}

class _ClassifyExampleWidgetState extends State<ClassifyExampleWidget> {
  int _index = 0;
  String? _guess;

  @override
  Widget build(BuildContext context) {
    final example = widget.examples[_index];
    final isCorrect = _guess == example.correctType;

    return SimFrame(
      title: widget.title,
      icon: widget.icon,
      accent: widget.accent,
      description: widget.description,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: widget.accent.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(10)),
            child: RichText(
              text: TextSpan(
                style: TextStyle(fontSize: 16, color: Theme.of(context).colorScheme.onSurface),
                children: _highlightedSpans(example.sentence, example.highlight, widget.accent),
              ),
            ),
          ),
          const SizedBox(height: 14),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: widget.options.map((t) {
              final isSelected = _guess == t;
              Color? bg;
              Color? fg;
              if (_guess != null) {
                if (t == example.correctType) {
                  bg = Colors.green.shade600;
                  fg = Colors.white;
                } else if (isSelected) {
                  bg = Colors.red.shade600;
                  fg = Colors.white;
                }
              }
              return ChoiceChip(
                label: Text(t, style: TextStyle(fontSize: 12, color: fg ?? (isSelected ? Colors.white : Colors.black87))),
                selected: isSelected,
                selectedColor: widget.accent,
                backgroundColor: bg ?? widget.accent.withValues(alpha: 0.08),
                onSelected: _guess == null ? (_) => setState(() => _guess = t) : null,
              );
            }).toList(),
          ),
          if (_guess != null) ...[
            const SizedBox(height: 10),
            Text(
              isCorrect ? 'Correct!' : 'Not quite — the answer is ${example.correctType}.',
              style: TextStyle(color: isCorrect ? Colors.green.shade700 : Colors.red.shade700, fontWeight: FontWeight.w600),
            ),
          ],
          const SizedBox(height: 14),
          Row(
            children: [
              Text('${_index + 1} / ${widget.examples.length}', style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
              const Spacer(),
              ElevatedButton.icon(
                onPressed: () => setState(() {
                  _index = (_index + 1) % widget.examples.length;
                  _guess = null;
                }),
                icon: Icon(Icons.arrow_forward),
                label: Text(TrilingualService.instance.getUIText('Next Example')),
                style: ElevatedButton.styleFrom(backgroundColor: widget.accent, foregroundColor: Colors.white),
              ),
            ],
          ),
        ],
      ),
    );
  }

  List<TextSpan> _highlightedSpans(String sentence, String highlight, Color color) {
    final idx = sentence.indexOf(highlight);
    if (idx < 0) return [TextSpan(text: sentence)];
    return [
      TextSpan(text: sentence.substring(0, idx)),
      TextSpan(text: highlight, style: TextStyle(fontWeight: FontWeight.bold, color: color, decoration: TextDecoration.underline)),
      TextSpan(text: sentence.substring(idx + highlight.length)),
    ];
  }
}
