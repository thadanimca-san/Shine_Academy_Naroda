import 'package:flutter/material.dart';

import '../models/concept.dart';
import '../theme/app_theme.dart';

/// Shared term-card tile used by both the per-topic glossary browser and
/// the global cross-grade search screen.
class ConceptCard extends StatelessWidget {
  final Concept concept;
  final String? gradeLabel;

  const ConceptCard({super.key, required this.concept, this.gradeLabel});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      borderRadius: BorderRadius.circular(12),
      onTap: () => showModalBottomSheet(
        context: context,
        showDragHandle: true,
        builder: (_) => ConceptDetailSheet(concept: concept),
      ),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: AppColors.paperRaised,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: AppColors.rule),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              children: [
                Container(
                  width: 44,
                  height: 44,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: AppColors.indigoTint,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(concept.emoji, style: TextStyle(fontSize: 22)),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(concept.term,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.ink)),
                      Text(concept.meaningHi,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(color: AppColors.tealDeep, fontSize: 13)),
                    ],
                  ),
                ),
                if (gradeLabel != null)
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
                    decoration: BoxDecoration(
                      color: AppColors.tealTint,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(gradeLabel!, style: TextStyle(fontSize: 10, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                  ),
              ],
            ),
            const SizedBox(height: 8),
            Text(
              concept.meaningEn,
              maxLines: 3,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
            ),
          ],
        ),
      ),
    );
  }
}

class ConceptDetailSheet extends StatelessWidget {
  final Concept concept;

  const ConceptDetailSheet({super.key, required this.concept});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          Center(
            child: Container(
              width: 88,
              height: 88,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: AppColors.indigoTint,
                borderRadius: BorderRadius.circular(16),
              ),
              child: Text(concept.emoji, style: TextStyle(fontSize: 44)),
            ),
          ),
          const SizedBox(height: 16),
          Text(concept.term, style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.ink)),
          Text(
            '${concept.meaningHi}  ·  ${concept.hiTransliteration}',
            style: TextStyle(fontSize: 16, color: AppColors.tealDeep),
          ),
          const SizedBox(height: 12),
          Text(concept.meaningEn, style: TextStyle(fontSize: 15, color: AppColors.inkSoft)),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: AppColors.paperRaised,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text('"${concept.exampleEn}"', style: TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft)),
          ),
        ],
      ),
    );
  }
}
