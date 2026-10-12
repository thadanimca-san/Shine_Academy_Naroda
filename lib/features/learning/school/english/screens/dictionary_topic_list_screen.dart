import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../data/dictionary_topics.dart';
import '../models/dictionary_word.dart';
import '../theme/app_theme.dart';
import 'dictionary_search_screen.dart';
import 'dictionary_words_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../../../../../shared/widgets/activation_gate.dart';

/// Grade picker for the Picture Dictionary. With 17 themes per grade across
/// Class 7-10 (academic vocabulary plus Science and Social Studies), a flat
/// list would be too long to scan, so grade is chosen first, then its
/// themes are shown. A global search (all grades, all themes, one box) is
/// offered up front for anyone who just wants a word.
class DictionaryGradeListScreen extends StatelessWidget {
  const DictionaryGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final isSkillup = (appFlavor == 'skillup');
    final grades = dictionaryTopicsByGrade.keys.toList();
    final totalWords = allDictionaryTopics.fold(0, (sum, t) => sum + (t.words.isNotEmpty ? t.words.length : (t.wordIds?.length ?? 0)));

    final Map<String, Map<String, String>> skillupLevelMap = {
      'Class 3': {
        'title': 'Level 1: Daily Life & Home Essentials (दैनिक जीवन)',
        'subtitle': 'Animals, Food, Body, Clothes, Home & Family',
        'emoji': '🏡',
      },
      'Class 4': {
        'title': 'Level 2: Living World, Nature & Travel (प्रकृति व यात्रा)',
        'subtitle': 'Nature, Weather, Transport, Garden, Colors & Shapes',
        'emoji': '🌿',
      },
      'Class 5': {
        'title': 'Level 3: Workplaces, Society & Sports (कामकाज व समाज)',
        'subtitle': 'Occupations, Feelings, Sports, Society & Living',
        'emoji': '🏙️',
      },
      'Class 6': {
        'title': 'Level 4: Science, Inventions & World Wonders (विज्ञान व दुनिया)',
        'subtitle': 'Science, Tools, Glacier, Ecosystem & Technology',
        'emoji': '🔬',
      },
      'Class 7': {
        'title': 'Level 5: Academic Words & Context (शैक्षणिक शब्दावली)',
        'subtitle': 'Essential academic concepts & social terms',
        'emoji': '📚',
      },
      'Class 8': {
        'title': 'Level 6: Idioms & Spoken Phrasal Verbs (मुहावरे व वाक्यांश)',
        'subtitle': 'Common spoken idioms, expressions & daily phrases',
        'emoji': '💬',
      },
      'Class 9': {
        'title': 'Level 7: Synonyms & Antonyms (समानार्थी व विलोम शब्द)',
        'subtitle': 'Word precision, vocabulary expansion & pairs',
        'emoji': '🎯',
      },
      'Class 10': {
        'title': 'Level 8: Professional & Elite Fluency (व्यावसायिक शब्दावली)',
        'subtitle': 'Advanced communication & leadership vocabulary',
        'emoji': '👑',
      },
    };

    return Scaffold(
      appBar: BrandAppBar(
        title: TrilingualService.instance.getUIText('Visual Picture Dictionary'),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
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
                        Text(
                          TrilingualService.instance.getUIText('Search all visual words (Instant)'),
                          style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.tealDeep),
                        ),
                        Text(
                          'Instant visual search across $totalWords words (ant, glacier, butterfly...)',
                          style: TextStyle(fontSize: 12, color: AppColors.inkSoft),
                        ),
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

            final String displayTitle = (isSkillup && skillupLevelMap.containsKey(grade))
                ? skillupLevelMap[grade]!['title']!
                : grade;
            final String displaySubtitle = (isSkillup && skillupLevelMap.containsKey(grade))
                ? '${topics.length} themes · $wordCount words (${skillupLevelMap[grade]!['subtitle']!})'
                : '${topics.length} themes · $wordCount words';
            final String displayEmoji = (isSkillup && skillupLevelMap.containsKey(grade))
                ? skillupLevelMap[grade]!['emoji']!
                : '📖';

            final card = Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Card(
                child: ListTile(
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  leading: CircleAvatar(
                    backgroundColor: AppColors.saffronTint,
                    child: Text(displayEmoji, style: const TextStyle(fontSize: 20)),
                  ),
                  title: Text(
                    TrilingualService.instance.getUIText(displayTitle),
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                  subtitle: Text(displaySubtitle),
                  trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => DictionaryTopicListScreen(
                        grade: isSkillup ? displayTitle : grade,
                        topics: topics,
                      ),
                    ),
                  ),
                ),
              ),
            );

            if (!isSkillup) return card;

            return ActivationGate(
              isFree: false,
              child: card,
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
