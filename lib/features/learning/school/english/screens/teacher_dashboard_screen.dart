import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import 'question_paper_setup_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Teacher Dashboard: a simple hub pointing straight at the Question Paper
/// Generator — the one teacher-facing tool that's actually in daily use.
/// No assignment/planning list, no scores, no student data.
class TeacherDashboardScreen extends StatelessWidget {
  const TeacherDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Teacher Dashboard')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            InkWell(
              borderRadius: BorderRadius.circular(14),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const QuestionPaperSetupScreen()),
              ),
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.all(18),
                decoration: BoxDecoration(
                  color: AppColors.tealTint,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: AppColors.rule),
                ),
                child: Row(
                  children: [
                    Container(
                      width: 52,
                      height: 52,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(color: AppColors.paper, borderRadius: BorderRadius.circular(12)),
                      child: Text(TrilingualService.instance.getUIText('📝'), style: TextStyle(fontSize: 26)),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(TrilingualService.instance.getUIText('Question Paper Generator'), style: Theme.of(context).textTheme.titleMedium),
                          const SizedBox(height: 4),
                          Text(TrilingualService.instance.getUIText('Pick a grade and topics, then build a question paper with a matching answer key.'),
                            style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
                          ),
                        ],
                      ),
                    ),
                    Icon(Icons.chevron_right, color: AppColors.inkFaint),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
