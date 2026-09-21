import 'package:flutter/material.dart';
import '../models/chapter_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Interactive numerical/word-problem practice: students type a numeric
/// answer, check it against a tolerance, and can reveal a full step-by-step
/// worked solution independent of whether they attempted it — useful both
/// for self-practice and for a teacher walking through the derivation in class.
class NumericalProblemSet extends StatefulWidget {
  final List<NumericalProblem> problems;

  const NumericalProblemSet({super.key, required this.problems});

  @override
  State<NumericalProblemSet> createState() => _NumericalProblemSetState();
}

class _NumericalProblemSetState extends State<NumericalProblemSet> {
  final Map<String, TextEditingController> _controllers = {};
  final Map<String, bool?> _correctness = {}; // null = not checked yet
  final Set<String> _solutionShown = {};

  TextEditingController _controllerFor(String id) => _controllers.putIfAbsent(id, () => TextEditingController());

  @override
  void dispose() {
    for (final c in _controllers.values) {
      c.dispose();
    }
    super.dispose();
  }

  void _checkAll() {
    setState(() {
      for (final p in widget.problems) {
        final text = _controllerFor(p.id).text.trim();
        if (text.isEmpty) {
          _correctness[p.id] = false;
          continue;
        }
        final parsed = double.tryParse(text);
        if (parsed == null) {
          _correctness[p.id] = false;
          continue;
        }
        final tolerance = (p.numericAnswer.abs() * 0.02).clamp(0.05, double.infinity);
        _correctness[p.id] = (parsed - p.numericAnswer).abs() <= tolerance;
      }
    });
  }

  int get _score => _correctness.values.where((v) => v == true).length;
  bool get _anyChecked => _correctness.isNotEmpty;

  @override
  Widget build(BuildContext context) {
    if (widget.problems.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (_anyChecked)
          Card(
            color: _score == widget.problems.length ? Colors.green[50] : Colors.orange[50],
            margin: const EdgeInsets.only(bottom: 12),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Row(
                children: [
                  Icon(
                    _score == widget.problems.length ? Icons.emoji_events : Icons.bar_chart,
                    color: _score == widget.problems.length ? Colors.green[800] : Colors.orange[800],
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text('Score: $_score / ${widget.problems.length}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                  ),
                  TextButton.icon(
                    onPressed: () => setState(() {
                      _correctness.clear();
                      _solutionShown.clear();
                      for (final c in _controllers.values) {
                        c.clear();
                      }
                    }),
                    icon: Icon(Icons.refresh),
                    label: Text(TrilingualService.instance.getUIText('Retry')),
                  ),
                ],
              ),
            ),
          ),
        ...widget.problems.asMap().entries.map((entry) {
          final index = entry.key + 1;
          final p = entry.value;
          final correctness = _correctness[p.id];
          final showSolution = _solutionShown.contains(p.id);

          return Card(
            margin: const EdgeInsets.only(bottom: 10),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('$index. ${p.question}', style: TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
                  if (p.given.isNotEmpty) ...[
                    const SizedBox(height: 6),
                    Wrap(
                      spacing: 8,
                      runSpacing: 4,
                      children: p.given
                          .map((g) => Chip(
                                label: Text(g, style: TextStyle(fontSize: 11.5)),
                                backgroundColor: Colors.blueGrey.shade50,
                                visualDensity: VisualDensity.compact,
                                padding: EdgeInsets.zero,
                              ))
                          .toList(),
                    ),
                  ],
                  const SizedBox(height: 10),
                  Row(
                    children: [
                      Expanded(
                        child: TextField(
                          controller: _controllerFor(p.id),
                          keyboardType: const TextInputType.numberWithOptions(signed: true, decimal: true),
                          decoration: InputDecoration(
                            isDense: true,
                            labelText: 'Your answer (${p.unit})',
                            border: const OutlineInputBorder(),
                            filled: correctness != null,
                            fillColor: correctness == null ? null : (correctness ? Colors.green.shade50 : Colors.red.shade50),
                            suffixIcon: correctness == null
                                ? null
                                : Icon(correctness ? Icons.check_circle : Icons.cancel, color: correctness ? Colors.green : Colors.red),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      TextButton.icon(
                        onPressed: () => setState(() {
                          if (showSolution) {
                            _solutionShown.remove(p.id);
                          } else {
                            _solutionShown.add(p.id);
                          }
                        }),
                        icon: Icon(showSolution ? Icons.visibility_off : Icons.lightbulb_outline),
                        label: Text(showSolution ? 'Hide Solution' : 'Show Step-by-Step Solution'),
                      ),
                    ],
                  ),
                  if (showSolution) ...[
                    const Divider(),
                    ...p.solutionSteps.asMap().entries.map((s) => Padding(
                          padding: const EdgeInsets.only(bottom: 4),
                          child: Text('${s.key + 1}. ${s.value}', style: TextStyle(fontSize: 13)),
                        )),
                    const SizedBox(height: 4),
                    Text('Final Answer: ${_formatAnswer(p.numericAnswer)} ${p.unit}',
                        style: TextStyle(fontWeight: FontWeight.bold, color: Colors.green.shade800, fontSize: 13)),
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
            onPressed: _checkAll,
            icon: Icon(Icons.check_circle_outline),
            label: Text(TrilingualService.instance.getUIText('Check My Answers')),
            style: ElevatedButton.styleFrom(backgroundColor: Colors.orange[800], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(vertical: 14)),
          ),
        ),
      ],
    );
  }

  String _formatAnswer(double value) {
    if (value == value.roundToDouble()) return value.toStringAsFixed(0);
    return value.toStringAsFixed(2);
  }
}
