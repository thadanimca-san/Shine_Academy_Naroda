import 'package:flutter/material.dart';

import '../services/progress_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Shows the student's practice accuracy per topic, so they can see at a
/// glance which topics need more revision instead of having to guess.
class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('My Progress'))),
      body: FutureBuilder<Map<String, TopicProgress>>(
        future: ProgressService.getAllProgress(),
        builder: (context, snapshot) {
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final progress = snapshot.data!;
          final topicKeys = ProgressService.topicLabels.keys.toList();

          final practicedKeys = topicKeys.where(progress.containsKey).toList();
          final unpracticedKeys = topicKeys.where((k) => !progress.containsKey(k)).toList();

          return ListView(
            padding: const EdgeInsets.all(16),
            children: [
              if (progress.isEmpty)
                Padding(
                  padding: EdgeInsets.only(top: 24, bottom: 8),
                  child: Text(TrilingualService.instance.getUIText('No practice attempts yet. Pick a topic below and start practicing — your accuracy will show up here.'),
                    style: TextStyle(fontSize: 14),
                  ),
                ),
              for (final key in practicedKeys) _buildTopicCard(progress[key]!),
              if (unpracticedKeys.isNotEmpty) ...[
                const SizedBox(height: 8),
                Text(TrilingualService.instance.getUIText('Not yet practiced'), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.grey.shade700)),
                const SizedBox(height: 6),
                for (final key in unpracticedKeys)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 2),
                    child: Text('• ${ProgressService.topicLabels[key]}', style: TextStyle(color: Colors.grey.shade600)),
                  ),
              ],
            ],
          );
        },
      ),
    );
  }

  Widget _buildTopicCard(TopicProgress p) {
    final label = ProgressService.topicLabels[p.topicKey] ?? p.topicKey;
    final accuracyPercent = (p.accuracy * 100).round();
    final isWeak = p.attempted >= 3 && p.accuracy < 0.6;
    final color = isWeak ? Colors.red : (p.accuracy >= 0.8 ? Colors.green : Colors.orange);

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(child: Text(label, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15))),
                if (isWeak) Icon(Icons.warning_amber, color: Colors.red, size: 20),
              ],
            ),
            const SizedBox(height: 6),
            LinearProgressIndicator(value: p.accuracy, color: color, backgroundColor: color.withValues(alpha: 0.15)),
            const SizedBox(height: 6),
            Text('$accuracyPercent% accuracy — ${p.correct}/${p.attempted} correct',
                style: TextStyle(color: color, fontWeight: FontWeight.bold)),
            if (isWeak)
              Padding(
                padding: EdgeInsets.only(top: 4),
                child: Text(TrilingualService.instance.getUIText('Needs more practice'), style: TextStyle(color: Colors.red, fontStyle: FontStyle.italic)),
              ),
          ],
        ),
      ),
    );
  }
}
