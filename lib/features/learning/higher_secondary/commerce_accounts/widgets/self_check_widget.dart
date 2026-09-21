import 'package:flutter/material.dart';

import '../services/progress_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// After a student reveals a multi-statement solution (Cash Book, Final
/// Accounts, Partnership, Company Accounts, Cash Flow — topics too
/// free-form for a simple input-and-check), this asks them to honestly
/// mark whether they got it right, and records that into the same
/// progress tracker every other topic feeds. Self-reported accuracy is
/// weaker than an auto-graded check, but far better than these topics
/// contributing nothing to "My Progress" at all.
class SelfCheckWidget extends StatefulWidget {
  final String topicKey;

  const SelfCheckWidget({super.key, required this.topicKey});

  @override
  State<SelfCheckWidget> createState() => _SelfCheckWidgetState();
}

class _SelfCheckWidgetState extends State<SelfCheckWidget> {
  bool? _answeredCorrectly;

  void _record(bool wasCorrect) {
    setState(() => _answeredCorrectly = wasCorrect);
    ProgressService.recordAttempt(topicKey: widget.topicKey, wasCorrect: wasCorrect);
  }

  @override
  Widget build(BuildContext context) {
    if (_answeredCorrectly != null) {
      final good = _answeredCorrectly!;
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 8),
        child: Row(
          children: [
            Icon(good ? Icons.check_circle : Icons.refresh, color: good ? Colors.green : Colors.orange, size: 18),
            const SizedBox(width: 6),
            Text(
              good ? 'Marked as correct — nice work!' : 'Marked for revision — try a fresh question on this topic.',
              style: TextStyle(color: good ? Colors.green.shade800 : Colors.orange.shade800, fontSize: 13),
            ),
          ],
        ),
      );
    }

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText('Did you get this right?'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
          const SizedBox(height: 6),
          Row(
            children: [
              OutlinedButton.icon(
                onPressed: () => _record(true),
                icon: Icon(Icons.check, size: 18),
                label: Text(TrilingualService.instance.getUIText('Yes, correct')),
              ),
              const SizedBox(width: 10),
              OutlinedButton.icon(
                onPressed: () => _record(false),
                icon: Icon(Icons.close, size: 18),
                label: Text(TrilingualService.instance.getUIText('No, I made a mistake')),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
