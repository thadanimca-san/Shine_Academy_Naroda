import 'package:flutter/material.dart';

import '../../../../../foundation/theme/brand_app_bar.dart';
import '../data/chapters.dart';
import '../data/figures_of_speech.dart';
import '../data/practice_topics.dart';
import '../data/reading_topics.dart';
import '../data/writing_topics.dart';
import '../theme/app_theme.dart';
import 'chapter_list_screen.dart';
import 'figures_of_speech_screen.dart';
import 'practice_session_screen.dart';
import 'reading_list_screen.dart';
import 'writing_list_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PracticeTopicListScreen extends StatelessWidget {
  const PracticeTopicListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final totalReadingPassages =
        readingLibraryByGrade.values.fold<int>(0, (sum, lib) => sum + lib.passages.length);

    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Practice')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Text(TrilingualService.instance.getUIText('Reading'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('📖'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(TrilingualService.instance.getUIText('Reading Passages')),
              subtitle: Text('Class 7–10 · $totalReadingPassages illustrated passages'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const ReadingGradeListScreen()),
              ),
            ),
          ),
          const SizedBox(height: 24),
          Text(TrilingualService.instance.getUIText('Writing'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('✍️'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(TrilingualService.instance.getUIText('Picture Writing')),
              subtitle: Text(
                '${writingLibraryByGrade.keys.length} grade${writingLibraryByGrade.keys.length == 1 ? '' : 's'} · '
                '${writingLibraryByGrade.values.fold<int>(0, (sum, lib) => sum + lib.prompts.length)} picture prompts',
              ),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const WritingGradeListScreen()),
              ),
            ),
          ),
          const SizedBox(height: 24),
          Text(TrilingualService.instance.getUIText('Chapters'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.tealTint,
                child: Text(TrilingualService.instance.getUIText('📘'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(TrilingualService.instance.getUIText('Textbook Chapters')),
              subtitle: Text('Class 7–10 · ${allChapters.length} chapters · Hindi summary + word meanings'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const ChapterListScreen()),
              ),
            ),
          ),
          const SizedBox(height: 24),
          Text(TrilingualService.instance.getUIText('Figures of Speech'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('🎭'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(TrilingualService.instance.getUIText('Simile, Metaphor & more')),
              subtitle: Text(
                '${figuresOfSpeech.length} figures of speech · '
                '${figuresOfSpeech.fold<int>(0, (sum, f) => sum + f.examples.length)} examples',
              ),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => const FiguresOfSpeechListScreen()),
              ),
            ),
          ),
          const SizedBox(height: 24),
          for (final entry in practiceTopicsByGrade.entries) ...[
            Padding(
              padding: const EdgeInsets.only(bottom: 10, top: 4),
              child: Text('${entry.key} Grammar', style: Theme.of(context).textTheme.titleMedium),
            ),
            ...entry.value.map(
              (topic) => Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: Card(
                  child: ListTile(
                    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    leading: CircleAvatar(
                      backgroundColor: AppColors.tealTint,
                      child: Text(TrilingualService.instance.getUIText('✏️'), style: TextStyle(fontSize: 18)),
                    ),
                    title: Text(topic.title, style: Theme.of(context).textTheme.titleMedium),
                    subtitle: Text('${topic.bank.length} questions in bank'),
                    trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(builder: (_) => PracticeSessionScreen(topic: topic)),
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 12),
          ],
        ],
      ),
    );
  }
}
