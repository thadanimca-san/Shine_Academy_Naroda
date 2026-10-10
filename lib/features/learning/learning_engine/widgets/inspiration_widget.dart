import 'package:flutter/material.dart';

import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_typography.dart';
import '../../../common/widgets/tts_interactive_text.dart';

/// Block `inspiration`: a short true story of a person behind the chapter's
/// ideas, a quote, and where this topic can take the student in life.
///
/// JSON: {"title", "person", "years", "body", "quote", "future"}
class InspirationWidget extends StatelessWidget {
  final Map<String, dynamic> data;
  const InspirationWidget({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    final text = TrilingualService.instance.getLocalizedText;
    final ui = TrilingualService.instance.getUIText;
    final title = text(data, 'title');
    final person = text(data, 'person');
    final years = data['years'] as String? ?? '';
    final quote = text(data, 'quote');
    final future = text(data, 'future');
    final ink = Colors.brown.shade900;

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [Colors.amber.shade50, Colors.orange.shade50]),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.amber.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.auto_awesome, color: Colors.amber.shade800),
              const SizedBox(width: 8),
              Expanded(
                child: Text(title.isEmpty ? ui('A story to inspire you') : title,
                    style: AppTypography.h4(context, color: ink)),
              ),
            ],
          ),
          if (person.isNotEmpty) ...[
            const SizedBox(height: 4),
            Text(years.isEmpty ? person : '$person ($years)',
                style: AppTypography.bodySmall(context, color: Colors.brown.shade700, fontWeight: FontWeight.bold)),
          ],
          const SizedBox(height: 10),
          TtsInteractiveText(text: text(data, 'body'), style: AppTypography.body(context, color: ink)),
          if (quote.isNotEmpty) ...[
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.only(left: 12),
              decoration: BoxDecoration(border: Border(left: BorderSide(color: Colors.amber.shade600, width: 4))),
              child: TtsInteractiveText(
                text: '*$quote*',
                style: AppTypography.body(context, color: Colors.brown.shade800),
              ),
            ),
          ],
          if (future.isNotEmpty) ...[
            const SizedBox(height: 12),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.rocket_launch, color: Colors.deepOrange.shade400),
                const SizedBox(width: 8),
                Expanded(
                  child: TtsInteractiveText(
                    text: '**${ui('Where this can take you')}:** $future',
                    style: AppTypography.body(context, color: ink),
                  ),
                ),
              ],
            ),
          ],
        ],
      ),
    );
  }
}
