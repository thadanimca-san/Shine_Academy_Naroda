import 'package:flutter/material.dart';

import '../../../../../foundation/theme/brand_app_bar.dart';
import '../data/reading_topics.dart';
import '../models/practice_question.dart';
import '../models/reading_passage.dart';
import '../theme/app_theme.dart';
import 'reading_passage_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Grade picker for Reading. Each grade has its own small library of
/// illustrated passages, so grade is chosen first, then its passages.
class ReadingGradeListScreen extends StatelessWidget {
  const ReadingGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = readingLibraryByGrade.keys.toList();
    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Reading')),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: grades.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final grade = grades[index];
          final library = readingLibraryByGrade[grade]!;
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('📖'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text('${library.passages.length} illustrated passages'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => ReadingPassageListScreen(library: library)),
              ),
            ),
          );
        },
      ),
    );
  }
}

class ReadingPassageListScreen extends StatelessWidget {
  final ReadingLibrary library;

  const ReadingPassageListScreen({super.key, required this.library});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(title: '${library.grade} Reading'),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: library.passages.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final passage = library.passages[index];
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(passage.emoji, style: TextStyle(fontSize: 18)),
              ),
              title: Text(passage.title, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text(
                '${passage.questions.length} questions · ${_difficultyLabel(passage.difficulty)}',
              ),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => ReadingPassageScreen(passage: passage)),
              ),
            ),
          );
        },
      ),
    );
  }

  String _difficultyLabel(Difficulty d) => switch (d) {
        Difficulty.easy => 'Easy',
        Difficulty.medium => 'Medium',
        Difficulty.hard => 'Hard',
      };
}
