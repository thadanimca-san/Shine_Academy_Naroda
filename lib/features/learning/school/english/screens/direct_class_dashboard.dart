import 'package:flutter/material.dart';
import '../models/chapter.dart';
import '../theme/app_theme.dart';
import '../data/dictionary_topics.dart';
import '../data/reading_topics.dart';
import '../data/writing_topics.dart';
import '../data/chapters.dart';
import 'dictionary_topic_list_screen.dart';
import 'reading_list_screen.dart';
import 'writing_list_screen.dart';
import 'chapter_list_screen.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

class DirectClassDashboard extends StatelessWidget {
  final int grade;

  const DirectClassDashboard({super.key, required this.grade});

  @override
  Widget build(BuildContext context) {
    final gradeString = 'Class $grade';
    
    // Fallback safely if data for this grade isn't populated yet
    final dictionaryTopics = dictionaryTopicsByGrade[gradeString] ?? [];
    final readingLibrary = readingLibraryByGrade[gradeString];
    final writingLibrary = writingLibraryByGrade[gradeString];
    
    List<Chapter> grammarChapters = [];
    if (grade == 3) {
      grammarChapters = class3Chapters;
    } else if (grade == 4) {
      grammarChapters = class4Chapters;
    } else if (grade == 5) {
      grammarChapters = class5Chapters;
    } else if (grade == 6) {
      grammarChapters = class6Chapters;
    }

    return Scaffold(
      appBar: BrandAppBar(
        title: 'English Speaking (Class $grade)',
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Text(
            "Spoken English (Class $grade)",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: AppColors.ink),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 16),
          
          if (dictionaryTopics.isNotEmpty)
            _buildActionCard(
              context,
              'Picture Dictionary',
              '📖',
              '${dictionaryTopics.length} themes for Class $grade',
              AppColors.saffronTint,
              () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => DictionaryTopicListScreen(
                    grade: gradeString,
                    topics: dictionaryTopics,
                  ),
                ),
              ),
            ),
            
          if (readingLibrary != null)
            _buildActionCard(
              context,
              'Reading Passages',
              '📚',
              '${readingLibrary.passages.length} illustrated passages',
              AppColors.tealTint,
              () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => ReadingPassageListScreen(library: readingLibrary),
                ),
              ),
            ),
            
          if (grammarChapters.isNotEmpty)
            _buildActionCard(
              context,
              'Grammar & Vocab',
              '✏️',
              '${grammarChapters.length} interactive chapters',
              AppColors.paperRaised,
              () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => ChapterListScreen(chapters: grammarChapters),
                ),
              ),
            ),
            
          if (writingLibrary != null)
            _buildActionCard(
              context,
              'Picture Writing',
              '✍️',
              '${writingLibrary.prompts.length} writing prompts',
              AppColors.saffronTint,
              () => Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => WritingPromptListScreen(library: writingLibrary),
                ),
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildActionCard(BuildContext context, String title, String emoji, String subtitle, Color color, VoidCallback onTap) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        leading: CircleAvatar(
          backgroundColor: color,
          child: Text(emoji, style: TextStyle(fontSize: 18)),
        ),
        title: Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        subtitle: Text(subtitle),
        trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
        onTap: onTap,
      ),
    );
  }
}
