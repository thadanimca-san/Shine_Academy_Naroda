import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../views/assessment_hub_view.dart';
import 'dictionary_topic_list_screen.dart';
import 'phonetics_screen.dart';
import 'practice_topic_list_screen.dart';
import 'question_paper_setup_screen.dart';
import 'teacher_dashboard_screen.dart';

import 'direct_class_dashboard.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class HomeScreen extends StatelessWidget {
  final int? preSelectedGrade;
  
  const HomeScreen({super.key, this.preSelectedGrade});

  @override
  Widget build(BuildContext context) {
    if (preSelectedGrade != null) {
      return DirectClassDashboard(grade: preSelectedGrade!);
    }
    
    return Scaffold(
      appBar: BrandAppBar(title: 'Shine Academy Naroda'),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 12),
              Text(TrilingualService.instance.getUIText('English Speaking'),
                style: Theme.of(context).textTheme.headlineMedium,
              ),
              Text(TrilingualService.instance.getUIText('Shine Academy Naroda · Class 3–10 English'),
                style: TextStyle(color: AppColors.inkFaint, fontSize: 13),
              ),
              const SizedBox(height: 32),
              Expanded(
                child: GridView.count(
                  crossAxisCount: 2,
                  mainAxisSpacing: 14,
                  crossAxisSpacing: 14,
                  children: [
                    _HomeTile(
                      label: 'Picture\nDictionary',
                      emoji: '📖',
                      color: AppColors.saffronTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const DictionaryGradeListScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Phonetics',
                      emoji: '🔊',
                      color: AppColors.saffronTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const PhoneticsGradeListScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Practice',
                      emoji: '✏️',
                      color: AppColors.tealTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const PracticeTopicListScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Question\nPapers',
                      emoji: '📝',
                      color: AppColors.paperRaised,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const QuestionPaperSetupScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Teacher\nDashboard',
                      emoji: '🧑‍🏫',
                      color: AppColors.tealTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const TeacherDashboardScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Assessment\nHub',
                      emoji: '📚',
                      color: AppColors.paperRaised,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const AssessmentHubView()),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

}

class _HomeTile extends StatelessWidget {
  final String label;
  final String emoji;
  final Color color;
  final VoidCallback onTap;

  const _HomeTile({
    required this.label,
    required this.emoji,
    required this.color,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      borderRadius: BorderRadius.circular(16),
      onTap: onTap,
      child: Container(
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: AppColors.rule),
        ),
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Text(emoji, style: TextStyle(fontSize: 32)),
            const SizedBox(height: 10),
            Text(
              label,
              style: TextStyle(fontWeight: FontWeight.w700, fontSize: 16, color: AppColors.ink),
            ),
          ],
        ),
      ),
    );
  }
}
