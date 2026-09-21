import 'dart:math';
import 'package:flutter/material.dart';
import 'sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// One fill-in-the-blank sentence (blank shown as ___) with several word
/// options, one of which correctly completes it.
class CompletionExample {
  final String sentenceWithBlank; // use "___" as the blank marker
  final String correctWord;
  final List<String> options;
  final String? note;

  const CompletionExample({required this.sentenceWithBlank, required this.correctWord, required this.options, this.note});
}

/// A reusable "choose the word that correctly completes the sentence"
/// drill: shows the sentence with a blank, lets the student pick from a
/// few word options, and reveals whether the choice is correct with a
/// short explanatory note.
class ChooseCompletionWidget extends StatefulWidget {
  final String title;
  final IconData icon;
  final Color accent;
  final String description;
  final List<CompletionExample> examples;

  const ChooseCompletionWidget({
    super.key,
    required this.title,
    required this.icon,
    required this.accent,
    required this.description,
    required this.examples,
  });

  @override
  State<ChooseCompletionWidget> createState() => _ChooseCompletionWidgetState();
}

class _ChooseCompletionWidgetState extends State<ChooseCompletionWidget> {
  int _index = 0;
  String? _guess;

  @override
  Widget build(BuildContext context) {
    final example = widget.examples[_index];
    final isCorrect = _guess == example.correctWord;
    final parts = example.sentenceWithBlank.split('___');
    // Shuffle with a seed stable per sentence, so the correct answer isn't
    // always in the same position — a student could otherwise learn to
    // "always pick the first option" without knowing any real content.
    final shuffledOptions = [...example.options]..shuffle(Random(example.sentenceWithBlank.hashCode));

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
                children: [
                  TextSpan(text: parts.first),
                  TextSpan(
                    text: _guess ?? '______',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: _guess == null ? widget.accent : (isCorrect ? Colors.green.shade700 : Colors.red.shade700),
                      decoration: TextDecoration.underline,
                    ),
                  ),
                  if (parts.length > 1) TextSpan(text: parts.sublist(1).join('___')),
                ],
              ),
            ),
          ),
          const SizedBox(height: 14),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: shuffledOptions.map((opt) {
              final isSelected = _guess == opt;
              Color? bg;
              Color? fg;
              if (_guess != null) {
                if (opt == example.correctWord) {
                  bg = Colors.green.shade600;
                  fg = Colors.white;
                } else if (isSelected) {
                  bg = Colors.red.shade600;
                  fg = Colors.white;
                }
              }
              return ChoiceChip(
                label: Text(opt, style: TextStyle(fontSize: 13, color: fg ?? (isSelected ? Colors.white : Colors.black87))),
                selected: isSelected,
                selectedColor: widget.accent,
                backgroundColor: bg ?? widget.accent.withValues(alpha: 0.08),
                onSelected: _guess == null ? (_) => setState(() => _guess = opt) : null,
              );
            }).toList(),
          ),
          if (_guess != null && example.note != null) ...[
            const SizedBox(height: 10),
            Text(example.note!, style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
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
                label: Text(TrilingualService.instance.getUIText('Next')),
                style: ElevatedButton.styleFrom(backgroundColor: widget.accent, foregroundColor: Colors.white),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
