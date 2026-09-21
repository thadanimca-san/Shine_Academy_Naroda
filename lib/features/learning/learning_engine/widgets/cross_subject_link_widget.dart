import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../learning_engine_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/foundation/theme/app_typography.dart';

class CrossSubjectLinkWidget extends StatelessWidget {
  final Map<String, dynamic> block;

  const CrossSubjectLinkWidget({super.key, required this.block});

  @override
  Widget build(BuildContext context) {
    final title = block['title'] ?? 'Review Concept';
    final targetChapterId = block['target_chapter_id'];
    final description = block['description'] ?? 'Tap to review this topic from an earlier class before continuing.';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.deepPurple.shade50, Colors.indigo.shade50],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.deepPurple.shade200, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.deepPurple.withValues(alpha: 0.1),
            blurRadius: 10,
            offset: const Offset(0, 4),
          )
        ],
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: () {
            if (targetChapterId != null) {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => LearningEngineScreen(moduleId: targetChapterId, title: 'Concept Review'),
                ),
              );
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text(TrilingualService.instance.getUIText("Link broken: Missing target chapter ID"))),
              );
            }
          },
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.deepPurple.shade100,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(Icons.link, color: Colors.deepPurple.shade700, size: 28),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Text(TrilingualService.instance.getUIText("PREVIOUS CONCEPT"),
                            style: GoogleFonts.inter(
                              fontSize: 10 * AppTypography.scaleFactor(context),
                              fontWeight: FontWeight.w700,
                              letterSpacing: 1.2,
                              color: Colors.deepPurple.shade600,
                            ),
                          ),
                          const Spacer(),
                          Icon(Icons.arrow_forward_ios, size: 12, color: Colors.deepPurple.shade300),
                        ],
                      ),
                      const SizedBox(height: 4),
                      Text(
                        title,
                        style: GoogleFonts.poppins(
                          fontSize: 16 * AppTypography.scaleFactor(context),
                          fontWeight: FontWeight.bold,
                          color: Theme.of(context).colorScheme.onSurface,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        description,
                        style: GoogleFonts.inter(
                          fontSize: 13 * AppTypography.scaleFactor(context),
                          color: Theme.of(context).colorScheme.onSurfaceVariant,
                          height: 1.4,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
