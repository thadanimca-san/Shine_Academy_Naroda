import 'package:flutter/material.dart';

import '../data/math_topics.dart';
import '../models/math_question.dart';
import '../theme/app_theme.dart';
import 'math_session_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Grade picker for Practice, same pattern as the sister English app —
/// grade first, then that grade's topic list.
class MathGradeListScreen extends StatelessWidget {
  const MathGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = mathTopicsByGrade.keys.toList();
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Practice'))),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: grades.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final grade = grades[index];
          final topics = mathTopicsByGrade[grade]!;
          final questionCount = topics.fold<int>(0, (sum, t) => sum + t.bank.length);
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              leading: CircleAvatar(
                backgroundColor: AppColors.indigoTint,
                child: Text(TrilingualService.instance.getUIText('🔢'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text('${topics.length} topics · $questionCount questions'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => MathTopicListScreen(grade: grade, topics: topics)),
              ),
            ),
          );
        },
      ),
    );
  }
}

class MathTopicListScreen extends StatelessWidget {
  final String grade;
  final List<MathTopic> topics;

  const MathTopicListScreen({super.key, required this.grade, required this.topics});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$grade Maths')),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: topics.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final topic = topics[index];
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: AppColors.indigoTint,
                child: Text(TrilingualService.instance.getUIText('✏️'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(topic.title, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text('${topic.bank.length} questions in bank'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => MathSessionScreen(topic: topic)),
              ),
            ),
          );
        },
      ),
    );
  }
}
