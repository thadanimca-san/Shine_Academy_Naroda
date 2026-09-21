import 'package:flutter/material.dart';

import '../data/chapters.dart';
import '../theme/app_theme.dart';
import 'chapter_reader_screen.dart';

import '../models/chapter.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

class ChapterListScreen extends StatelessWidget {
  final List<Chapter>? chapters;
  const ChapterListScreen({super.key, this.chapters});

  @override
  Widget build(BuildContext context) {
    final Map<String, List<Chapter>> displayChapters = chapters != null 
        ? {'Your Class': chapters!} 
        : chaptersByGrade;

    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Chapters')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            margin: const EdgeInsets.only(bottom: 16),
            decoration: BoxDecoration(
              color: AppColors.paperRaised,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppColors.rule),
            ),
            child:  Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(TrilingualService.instance.getUIText('⚠️'), style: TextStyle(fontSize: 16)),
                SizedBox(width: 8),
                Expanded(
                  child: Text(TrilingualService.instance.getUIText('Draft chapters written to match typical GSEB/CBSE Class 7–10 style and difficulty — ''not copied from the real textbooks. Needs a teacher pass before treating as final.'),
                    style: TextStyle(fontSize: 12, color: AppColors.inkSoft),
                  ),
                ),
              ],
            ),
          ),
          for (final entry in displayChapters.entries) ...[
            Padding(
              padding: const EdgeInsets.only(bottom: 10, top: 4),
              child: Text(
                '${entry.key} · ${entry.value.length} chapters',
                style: Theme.of(context).textTheme.titleMedium,
              ),
            ),
            ...entry.value.map(
              (chapter) => Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: Card(
                  child: ListTile(
                    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                    leading: CircleAvatar(
                      backgroundColor: AppColors.saffronTint,
                      child: Text(chapter.emoji, style: TextStyle(fontSize: 18)),
                    ),
                    title: Text(chapter.title, style: Theme.of(context).textTheme.titleMedium),
                    subtitle: Text('${chapter.glosses.length} words glossed in Hindi'),
                    trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                    onTap: () => Navigator.of(context).push(
                      MaterialPageRoute(builder: (_) => ChapterReaderScreen(chapter: chapter)),
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
