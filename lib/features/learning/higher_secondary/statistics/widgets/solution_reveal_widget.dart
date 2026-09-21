import 'package:flutter/material.dart';

import '../models/central_tendency_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Reveals a worked solution's steps one at a time instead of dumping
/// the full answer at once — matches how a teacher would walk through a
/// solution, and keeps the student engaged with each reasoning step.
class SolutionRevealWidget extends StatefulWidget {
  final String title;
  final List<SolutionStep> steps;
  final String finalAnswer;

  const SolutionRevealWidget({super.key, required this.title, required this.steps, required this.finalAnswer});

  @override
  State<SolutionRevealWidget> createState() => _SolutionRevealWidgetState();
}

class _SolutionRevealWidgetState extends State<SolutionRevealWidget> {
  int _revealedCount = 0;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(widget.title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
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
            if (_revealedCount >= widget.steps.length)
              Padding(
                padding: const EdgeInsets.only(top: 6),
                child: Text('Answer: ${widget.finalAnswer}',
                    style: TextStyle(fontWeight: FontWeight.bold, color: Colors.indigo)),
              ),
          ],
        ),
      ),
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
                Text(step.title, style: TextStyle(fontWeight: FontWeight.bold)),
                Text(step.reasoning),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
