import 'package:flutter/material.dart';

import '../data/dictionary_topics.dart';
import '../models/dictionary_word.dart';
import '../theme/app_theme.dart';
import 'dictionary_search_screen.dart';
import 'dictionary_words_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Grade picker for the Picture Dictionary. With 17 themes per grade across
/// Class 7-10 (academic vocabulary plus Science and Social Studies), a flat
/// list would be too long to scan, so grade is chosen first, then its
/// themes are shown. A global search (all grades, all themes, one box) is
/// offered up front for anyone who just wants a word.
class DictionaryGradeListScreen extends StatelessWidget {
  const DictionaryGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = dictionaryTopicsByGrade.keys.toList();
    final totalWords = allDictionaryTopics.fold(0, (sum, t) => sum + (t.words.isNotEmpty ? t.words.length : (t.wordIds?.length ?? 0)));
    return Scaffold(
      appBar: BrandAppBar(
        title: TrilingualService.instance.getUIText('Picture Dictionary'),
        actions: [
          IconButton(
            icon: Icon(Icons.search),
            tooltip: 'Search all words',
            onPressed: () => Navigator.of(context).push(
              MaterialPageRoute(builder: (_) => const DictionarySearchScreen()),
            ),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          InkWell(
            borderRadius: BorderRadius.circular(12),
            onTap: () => Navigator.of(context).push(
              MaterialPageRoute(builder: (_) => const DictionarySearchScreen()),
            ),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              margin: const EdgeInsets.only(bottom: 16),
              decoration: BoxDecoration(
                color: AppColors.tealTint,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppColors.rule),
              ),
              child: Row(
                children: [
                  Icon(Icons.search, color: AppColors.tealDeep),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText('Search all words'), style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.tealDeep)),
                        Text('Across every grade and theme · $totalWords words',
                            style: TextStyle(fontSize: 12, color: AppColors.inkSoft)),
                      ],
                    ),
                  ),
                  Icon(Icons.chevron_right, color: AppColors.inkFaint),
                ],
              ),
            ),
          ),
          ...grades.map((grade) {
            final topics = dictionaryTopicsByGrade[grade]!;
            final wordCount = topics.fold(0, (sum, t) => sum + (t.words.isNotEmpty ? t.words.length : (t.wordIds?.length ?? 0)));
            return Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Card(
                child: ListTile(
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  leading: CircleAvatar(
                    backgroundColor: AppColors.saffronTint,
                    child: Text(TrilingualService.instance.getUIText('📖'), style: TextStyle(fontSize: 20)),
                  ),
                  title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
                  subtitle: Text('${topics.length} themes · $wordCount words'),
                  trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => DictionaryTopicListScreen(grade: grade, topics: topics)),
                  ),
                ),
              ),
            );
          }),
        ],
      ),
    );
  }
}

class DictionaryTopicListScreen extends StatelessWidget {
  final String grade;
  final List<DictionaryTopic> topics;

  const DictionaryTopicListScreen({super.key, required this.grade, required this.topics});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(title: '$grade Dictionary'),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: topics.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final topic = topics[index];
          final topicEmoji = topic.words.map((w) => w.emoji).firstWhere((e) => e != null, orElse: () => null);
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: topicEmoji != null
                    ? Text(topicEmoji, style: TextStyle(fontSize: 20))
                    : Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 18),
              ),
              title: Text(topic.title, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text('${topic.grade} · ${topic.words.isNotEmpty ? topic.words.length : (topic.wordIds?.length ?? 0)} words'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => DictionaryWordsScreen(topic: topic)),
              ),
            ),
          );
        },
      ),
    );
  }
}
