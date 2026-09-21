import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import 'concept_list_screen.dart';
import 'math_topic_list_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 12),
              Text(TrilingualService.instance.getUIText('maths3to6'), style: Theme.of(context).textTheme.headlineMedium),
              Text(TrilingualService.instance.getUIText('Shine Academy Naroda · Class 3–6 Maths'),
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
                      label: 'Maths Glossary',
                      emoji: '📘',
                      color: AppColors.tealTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const ConceptGradeListScreen()),
                      ),
                    ),
                    _HomeTile(
                      label: 'Practice',
                      emoji: '🔢',
                      color: AppColors.indigoTint,
                      onTap: () => Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => const MathGradeListScreen()),
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
            Text(label, style: TextStyle(fontWeight: FontWeight.w700, fontSize: 16, color: AppColors.ink)),
          ],
        ),
      ),
    );
  }
}
