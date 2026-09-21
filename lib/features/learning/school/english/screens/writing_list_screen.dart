import 'package:flutter/material.dart';

import '../data/writing_topics.dart';
import '../models/writing_prompt.dart';
import '../theme/app_theme.dart';
import 'writing_prompt_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Grade picker for Writing — picture-description prompts, one library per
/// grade, same pattern as Reading.
class WritingGradeListScreen extends StatelessWidget {
  const WritingGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = writingLibraryByGrade.keys.toList();
    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Writing')),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: grades.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final grade = grades[index];
          final library = writingLibraryByGrade[grade]!;
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('✍️'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text('${library.prompts.length} picture prompts'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => WritingPromptListScreen(library: library)),
              ),
            ),
          );
        },
      ),
    );
  }
}

class WritingPromptListScreen extends StatelessWidget {
  final WritingLibrary library;

  const WritingPromptListScreen({super.key, required this.library});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(title: '${library.grade} Writing'),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: library.prompts.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final prompt = library.prompts[index];
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(prompt.sceneEmoji.characters.first, style: TextStyle(fontSize: 18)),
              ),
              title: Text(prompt.title, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text(_difficultyLabel(prompt.difficulty)),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => WritingPromptScreen(prompt: prompt, grade: library.grade)),
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
