import 'package:flutter/material.dart';

import '../data/question_paper_sources.dart';
import '../services/question_paper_builder.dart';
import '../theme/app_theme.dart';
import 'question_paper_preview_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Where a teacher builds a question paper: pick a grade, pick which
/// grammar topics / reading passages to draw from, and how many questions
/// to pull from each — then generate a formatted paper + answer key.
class QuestionPaperSetupScreen extends StatefulWidget {
  const QuestionPaperSetupScreen({super.key});

  @override
  State<QuestionPaperSetupScreen> createState() => _QuestionPaperSetupScreenState();
}

class _QuestionPaperSetupScreenState extends State<QuestionPaperSetupScreen> {
  String? _grade;
  final Map<String, int> _selectedCounts = {}; // sourceId -> question count

  @override
  Widget build(BuildContext context) {
    final grades = gradesWithPaperContent;
    final grade = _grade ?? (grades.isNotEmpty ? grades.first : null);
    final sources = grade == null ? const <PaperQuestionSource>[] : paperSourcesForGrade(grade);

    final totalSelected = _selectedCounts.values.fold<int>(0, (sum, c) => sum + c);

    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Question Paper Generator')),
      body: grades.isEmpty
          ?  Center(
              child: Padding(
                padding: EdgeInsets.all(24),
                child: Text(TrilingualService.instance.getUIText('No grammar or reading question banks are available yet to build a paper from.'),
                  textAlign: TextAlign.center,
                  style: TextStyle(color: AppColors.inkFaint),
                ),
              ),
            )
          : Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(16, 12, 16, 4),
                  child: Row(
                    children: [
                      Text(TrilingualService.instance.getUIText('Grade'), style: TextStyle(fontWeight: FontWeight.w600)),
                      const SizedBox(width: 12),
                      DropdownButton<String>(
                        value: grade,
                        items: grades
                            .map((g) => DropdownMenuItem(value: g, child: Text(g)))
                            .toList(),
                        onChanged: (v) => setState(() {
                          _grade = v;
                          _selectedCounts.clear();
                        }),
                      ),
                    ],
                  ),
                ),
                if (sources.isEmpty)
                  Expanded(
                    child: Center(
                      child: Text(TrilingualService.instance.getUIText('No content available for this grade yet.'), style: TextStyle(color: AppColors.inkFaint)),
                    ),
                  )
                else
                  Expanded(
                    child: ListView(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                      children: [
                        ..._buildSectionGroup(context, 'Grammar', sources.where((s) => s.sectionKind == 'Grammar').toList()),
                        ..._buildSectionGroup(context, 'Reading', sources.where((s) => s.sectionKind == 'Reading').toList()),
                        ..._buildSectionGroup(
                            context, 'Figures of Speech', sources.where((s) => s.sectionKind == 'Figures of Speech').toList()),
                      ],
                    ),
                  ),
                SafeArea(
                  top: false,
                  child: Padding(
                    padding: const EdgeInsets.all(16),
                    child: SizedBox(
                      width: double.infinity,
                      child: FilledButton(
                        onPressed: totalSelected == 0 || grade == null
                            ? null
                            : () => _generate(context, grade, sources),
                        style: FilledButton.styleFrom(
                          backgroundColor: AppColors.saffron,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                        ),
                        child: Text(totalSelected == 0
                            ? 'Select questions to build a paper'
                            : 'Generate paper — $totalSelected questions'),
                      ),
                    ),
                  ),
                ),
              ],
            ),
    );
  }

  List<Widget> _buildSectionGroup(BuildContext context, String label, List<PaperQuestionSource> sources) {
    if (sources.isEmpty) return const [];
    return [
      Padding(
        padding: const EdgeInsets.only(top: 8, bottom: 8),
        child: Text(label, style: Theme.of(context).textTheme.titleMedium),
      ),
      ...sources.map((source) => _SourceRow(
            source: source,
            count: _selectedCounts[source.id] ?? 0,
            onChanged: (v) => setState(() {
              if (v == 0) {
                _selectedCounts.remove(source.id);
              } else {
                _selectedCounts[source.id] = v;
              }
            }),
          )),
    ];
  }

  void _generate(BuildContext context, String grade, List<PaperQuestionSource> sources) {
    final requests = _selectedCounts.entries
        .map((e) => PaperSectionRequest(
              source: sources.firstWhere((s) => s.id == e.key),
              count: e.value,
            ))
        .toList();

    final paper = buildQuestionPaper(
      grade: grade,
      title: '$grade English - Question Paper',
      requests: requests,
    );

    Navigator.of(context).push(
      MaterialPageRoute(builder: (_) => QuestionPaperPreviewScreen(paper: paper)),
    );
  }
}

class _SourceRow extends StatelessWidget {
  final PaperQuestionSource source;
  final int count;
  final ValueChanged<int> onChanged;

  const _SourceRow({required this.source, required this.count, required this.onChanged});

  @override
  Widget build(BuildContext context) {
    final maxCount = source.questions.length;
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: count > 0 ? AppColors.saffronTint : AppColors.paperRaised,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: AppColors.rule),
      ),
      child: Row(
        children: [
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(source.label, style: TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
                Text('$maxCount questions available', style: TextStyle(fontSize: 11.5, color: AppColors.inkFaint)),
              ],
            ),
          ),
          IconButton(
            icon: Icon(Icons.remove_circle_outline),
            color: AppColors.inkFaint,
            onPressed: count > 0 ? () => onChanged(count - 1) : null,
          ),
          SizedBox(
            width: 24,
            child: Text('$count', textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.w700)),
          ),
          IconButton(
            icon: Icon(Icons.add_circle_outline),
            color: AppColors.saffronDeep,
            onPressed: count < maxCount ? () => onChanged(count + 1) : null,
          ),
        ],
      ),
    );
  }
}
