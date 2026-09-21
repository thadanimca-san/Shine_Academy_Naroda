import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/solution_model.dart';
import '../services/localization_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Reveals a worked solution's steps one at a time instead of dumping the
/// full answer at once — matches how a teacher actually walks through a
/// solution on the blackboard, and keeps the student engaged with each
/// reasoning step rather than skipping straight to the final answer.
class SolutionRevealWidget extends StatefulWidget {
  final List<SolutionStep> steps;
  final Medium medium;

  const SolutionRevealWidget({super.key, required this.steps, this.medium = Medium.english});

  @override
  State<SolutionRevealWidget> createState() => _SolutionRevealWidgetState();
}

class _SolutionRevealWidgetState extends State<SolutionRevealWidget> {
  int _revealedCount = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (var i = 0; i < _revealedCount; i++) _buildStep(widget.steps[i], i),
        if (_revealedCount < widget.steps.length)
          TextButton.icon(
            onPressed: () => setState(() => _revealedCount++),
            icon: Icon(Icons.expand_more),
            label: Text(_revealedCount == 0 ? 'Show Step 1' : 'Show Next Step'),
          ),
        if (_revealedCount > 0 && _revealedCount < widget.steps.length)
          TextButton(
            onPressed: () => setState(() => _revealedCount = widget.steps.length),
            child: Text(TrilingualService.instance.getUIText('Show All')),
          ),
      ],
    );
  }

  Widget _buildStep(SolutionStep step, int index) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          CircleAvatar(radius: 11, child: Text('${index + 1}', style: TextStyle(fontSize: 11))),
          const SizedBox(width: 8),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(LocalizationService.translatePhrase(step.title, widget.medium), style: TextStyle(fontWeight: FontWeight.bold)),
                Text(LocalizationService.translatePhrase(step.reasoning, widget.medium)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
