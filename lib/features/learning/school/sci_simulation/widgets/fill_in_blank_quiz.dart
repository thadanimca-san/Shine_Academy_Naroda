import 'dart:math';
import 'package:flutter/material.dart';
import '../models/chapter_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Returns [options] in a shuffled order that's stable for a given
/// [seedKey] (e.g. the question id) — so the correct answer isn't always
/// in the same position (a student could otherwise learn "always pick the
/// first option" without knowing any of the actual content), while the
/// order still doesn't jump around between rebuilds of the same question.
List<String> stableShuffledOptions(String seedKey, List<String> options) {
  final shuffled = [...options];
  shuffled.shuffle(Random(seedKey.hashCode));
  return shuffled;
}

/// Splits a question like "The SI unit is [ m/s / m/s² ]." into the
/// surrounding text and the list of choice options found inside the brackets.
class _ParsedQuestion {
  final String before;
  final String after;
  final List<String> options;

  _ParsedQuestion({required this.before, required this.after, required this.options});
}

_ParsedQuestion _parseQuestion(String question) {
  final match = RegExp(r'\[(.*?)\]').firstMatch(question);
  if (match == null) {
    return _ParsedQuestion(before: question, after: '', options: const []);
  }
  final before = question.substring(0, match.start);
  final after = question.substring(match.end);
  final options = match
      .group(1)!
      .split('/')
      .map((s) => s.trim())
      .where((s) => s.isNotEmpty)
      .toList();
  return _ParsedQuestion(before: before, after: after, options: options);
}

/// An interactive fill-in-the-blanks quiz for a single chapter.
/// Students pick one of the two bracketed options per question, then tap
/// "Check Answers" to see per-question correctness and an overall score.
class FillInBlankQuiz extends StatefulWidget {
  final List<QuestionItem> questions;

  const FillInBlankQuiz({super.key, required this.questions});

  @override
  State<FillInBlankQuiz> createState() => _FillInBlankQuizState();
}

class _FillInBlankQuizState extends State<FillInBlankQuiz> {
  final Map<String, String> _selected = {};
  bool _checked = false;

  int get _score => widget.questions
      .where((q) => _selected[q.id]?.trim().toLowerCase() == q.answer.trim().toLowerCase())
      .length;

  void _reset() {
    setState(() {
      _selected.clear();
      _checked = false;
    });
  }

  int get _answeredCount => _selected.length;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (_checked)
          Card(
            color: _score == widget.questions.length ? Colors.green[50] : Colors.orange[50],
            margin: const EdgeInsets.only(bottom: 12),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Row(
                children: [
                  Icon(
                    _score == widget.questions.length ? Icons.emoji_events : Icons.bar_chart,
                    color: _score == widget.questions.length ? Colors.green[800] : Colors.orange[800],
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      'Score: $_score / ${widget.questions.length}',
                      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                    ),
                  ),
                  TextButton.icon(
                    onPressed: _reset,
                    icon: Icon(Icons.refresh),
                    label: Text(TrilingualService.instance.getUIText('Retry')),
                  ),
                ],
              ),
            ),
          ),
        ...widget.questions.asMap().entries.map((entry) {
          final index = entry.key + 1;
          final item = entry.value;
          final parsed = _parseQuestion(item.question);
          final chosen = _selected[item.id];
          final isCorrect = chosen != null &&
              chosen.trim().toLowerCase() == item.answer.trim().toLowerCase();

          return Card(
            margin: const EdgeInsets.only(bottom: 8.0),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  RichText(
                    text: TextSpan(
                      style: DefaultTextStyle.of(context).style,
                      children: [
                        TextSpan(text: '$index. ', style: TextStyle(fontWeight: FontWeight.bold)),
                        TextSpan(text: parsed.before),
                        TextSpan(
                          text: chosen ?? '______',
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            color: !_checked
                                ? Colors.blue[800]
                                : (isCorrect ? Colors.green[700] : Colors.red[700]),
                            decoration: TextDecoration.underline,
                          ),
                        ),
                        TextSpan(text: parsed.after),
                      ],
                    ),
                  ),
                  const SizedBox(height: 10),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: stableShuffledOptions(item.id, parsed.options).map((option) {
                      final isChosen = chosen == option;
                      Color? bgColor;
                      Color? fgColor;
                      if (_checked && isChosen) {
                        bgColor = isCorrect ? Colors.green[600] : Colors.red[600];
                        fgColor = Colors.white;
                      } else if (_checked && option.trim().toLowerCase() == item.answer.trim().toLowerCase()) {
                        bgColor = Colors.green[100];
                      } else if (isChosen) {
                        bgColor = Colors.blue[700];
                        fgColor = Colors.white;
                      }
                      return ChoiceChip(
                        label: Text(option),
                        selected: isChosen,
                        onSelected: _checked
                            ? null
                            : (_) {
                                setState(() {
                                  _selected[item.id] = option;
                                });
                              },
                        selectedColor: Colors.blue[700],
                        backgroundColor: bgColor,
                        labelStyle: TextStyle(
                          color: fgColor ?? (isChosen ? Colors.white : Colors.black87),
                          fontWeight: FontWeight.w500,
                        ),
                      );
                    }).toList(),
                  ),
                  if (_checked && !isCorrect) ...[
                    const SizedBox(height: 6),
                    Text(
                      'Correct answer: ${item.answer}',
                      style: TextStyle(color: Colors.green[800], fontStyle: FontStyle.italic, fontSize: 13),
                    ),
                  ],
                ],
              ),
            ),
          );
        }),
        const SizedBox(height: 8),
        SizedBox(
          width: double.infinity,
          child: ElevatedButton.icon(
            onPressed: _checked ? null : () => setState(() => _checked = true),
            icon: Icon(Icons.check_circle_outline),
            label: Text(_checked
                ? 'Checked'
                : 'Check Answers ($_answeredCount/${widget.questions.length} answered)'),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.blue[800],
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 14),
            ),
          ),
        ),
      ],
    );
  }
}
