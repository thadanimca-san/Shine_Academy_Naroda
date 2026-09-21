import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class CommonMistakesWidget extends StatelessWidget {
  final Map<String, dynamic> data;
  final String lang;
  const CommonMistakesWidget({super.key, required this.data, this.lang = 'en'});

  @override
  Widget build(BuildContext context) {
    final rawContent = data['content'];
    final content = rawContent is String 
        ? rawContent 
        : (rawContent as Map<String, dynamic>?)?[lang] ?? (rawContent as Map<String, dynamic>?)?['en'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.red[50],
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.red[200]!, width: 2),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(Icons.warning_amber_rounded, color: Colors.red[600], size: 28),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  data['title'] ?? "Common Mistake",
                  style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.red[800]),
                ),
                const SizedBox(height: 4),
                Text(
                  data['content'],
                  style: GoogleFonts.inter(fontSize: 15, color: Theme.of(context).colorScheme.onSurface),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
