import 'package:flutter/material.dart';
import 'package:printing/printing.dart';

import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/question_paper.dart';
import '../services/question_paper_pdf.dart';
import '../theme/app_theme.dart';
import 'package:shine_academy_naroda/features/assessment/exam_engine_screen.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Shows the assembled paper (formatted like a real exam paper) and its
/// answer key on-screen, with buttons to export either as a watermarked PDF
/// for printing.
class QuestionPaperPreviewScreen extends StatefulWidget {
  final QuestionPaper paper;

  const QuestionPaperPreviewScreen({super.key, required this.paper});

  @override
  State<QuestionPaperPreviewScreen> createState() => _QuestionPaperPreviewScreenState();
}

class _QuestionPaperPreviewScreenState extends State<QuestionPaperPreviewScreen> with SingleTickerProviderStateMixin {
  late final TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  List<AssessmentQuestion> _mapToAssessmentQuestions() {
    final List<AssessmentQuestion> allQs = [];
    for (final section in widget.paper.sections) {
      for (final q in section.questions) {
        String prompt = q.prompt;
        if (section.passageText != null && section.passageText!.isNotEmpty) {
          prompt = "Passage:\n${section.passageText}\n\nQuestion:\n$prompt";
        }
        allQs.add(AssessmentQuestion(
          moduleId: 'custom',
          type: 'quiz',
          question: prompt,
          questionHi: q.promptHi,
          options: q.options,
          optionsHi: q.optionsHi,
          correctIndexOrAnswer: q.correctIndex,
          explanationEn: q.explanation,
          explanationHi: q.explanationHi,
          section: section.heading,
          marks: section.marksPerQuestion,
        ));
      }
    }
    return allQs;
  }

  void _showTimerDialog() {
    int selectedMinutes = widget.paper.totalQuestions * 2;
    
    showDialog(
      context: context,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setState) {
            return AlertDialog(
              title: Text(TrilingualService.instance.getUIText('Set Exam Timer'), style: TextStyle(fontWeight: FontWeight.bold)),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(TrilingualService.instance.getUIText('How many minutes do you want to set for this exam?')),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      IconButton(
                        icon: Icon(Icons.remove_circle_outline),
                        onPressed: selectedMinutes > 5 ? () => setState(() => selectedMinutes -= 5) : null,
                      ),
                      Text('$selectedMinutes mins', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                      IconButton(
                        icon: Icon(Icons.add_circle_outline),
                        onPressed: selectedMinutes < 180 ? () => setState(() => selectedMinutes += 5) : null,
                      ),
                    ],
                  ),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: Text(TrilingualService.instance.getUIText('Cancel')),
                ),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(backgroundColor: AppColors.teal, foregroundColor: Colors.white),
                  onPressed: () {
                    Navigator.pop(context);
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ExamEngineScreen(
                          moduleId: 'custom',
                          customQuestions: _mapToAssessmentQuestions(),
                          customTitle: widget.paper.title,
                          customTimeSeconds: selectedMinutes * 60,
                        ),
                      ),
                    );
                  },
                  child: Text(TrilingualService.instance.getUIText('Start Exam')),
                ),
              ],
            );
          }
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final paper = widget.paper;
    return Scaffold(
      appBar: BrandAppBar(
        title: paper.title,
        bottom: TabBar(
          controller: _tabController,
          labelColor: AppColors.saffronDeep,
          unselectedLabelColor: AppColors.inkFaint,
          indicatorColor: AppColors.saffron,
          tabs: const [
            Tab(text: 'Question Paper'),
            Tab(text: 'Answer Key'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _QuestionPaperView(paper: paper),
          _AnswerKeyView(paper: paper),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  icon: Icon(Icons.computer, size: 18),
                  label: Text(TrilingualService.instance.getUIText('Take Test On-Screen'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                  onPressed: () {
                    _showTimerDialog();
                  },
                  style: FilledButton.styleFrom(
                    backgroundColor: Colors.green[700],
                    padding: const EdgeInsets.symmetric(vertical: 16),
                  ),
                ),
              ),
              const SizedBox(height: 12),
              Row(
                children: [
                  Expanded(
                    child: OutlinedButton.icon(
                      icon: Icon(Icons.picture_as_pdf, size: 18),
                      label: Text(TrilingualService.instance.getUIText('Export paper PDF')),
                      onPressed: () => Printing.layoutPdf(
                        onLayout: (format) => buildQuestionPaperPdf(paper),
                      ),
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        side: const BorderSide(color: AppColors.rule),
                      ),
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: FilledButton.icon(
                      icon: Icon(Icons.picture_as_pdf, size: 18),
                      label: Text(TrilingualService.instance.getUIText('Export answer key PDF')),
                      onPressed: () => Printing.layoutPdf(
                        onLayout: (format) => buildAnswerKeyPdf(paper),
                      ),
                      style: FilledButton.styleFrom(
                        backgroundColor: AppColors.teal,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _QuestionPaperView extends StatelessWidget {
  final QuestionPaper paper;

  const _QuestionPaperView({required this.paper});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        Center(
          child: Column(
            children: [
              Text(paper.title, style: TextStyle(fontSize: 20, fontWeight: FontWeight.w800, color: AppColors.ink)),
              const SizedBox(height: 4),
              Text('${paper.grade} · Total Marks: ${paper.totalMarks} · ${paper.totalQuestions} Questions',
                  style: TextStyle(fontSize: 13, color: AppColors.inkFaint)),
            ],
          ),
        ),
        const Divider(height: 32),
        for (final section in paper.sections) _SectionBlock(section: section),
      ],
    );
  }
}

class _SectionBlock extends StatelessWidget {
  final PaperSection section;

  const _SectionBlock({required this.section});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Expanded(
                child: Text(section.heading, style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15)),
              ),
              Text('${section.totalMarks} marks', style: TextStyle(color: AppColors.inkFaint, fontSize: 12)),
            ],
          ),
          Text(section.instructions, style: TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft, fontSize: 12.5)),
          if (section.passageText != null && section.passageText!.isNotEmpty) ...[
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.blue.withValues(alpha: 0.05),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: Colors.blue.withValues(alpha: 0.2)),
              ),
              child: Text(section.passageText!, style: TextStyle(height: 1.5, color: AppColors.ink)),
            ),
          ],
          const SizedBox(height: 10),
          for (var i = 0; i < section.questions.length; i++) _QuestionBlock(index: i + 1, question: section.questions[i]),
        ],
      ),
    );
  }
}

class _QuestionBlock extends StatelessWidget {
  final int index;
  final dynamic question;

  const _QuestionBlock({required this.index, required this.question});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('$index. ${question.prompt}', style: TextStyle(fontSize: 14, height: 1.4)),
          const SizedBox(height: 4),
          ...List.generate(question.options.length, (i) {
            final letter = String.fromCharCode(97 + i); // a, b, c, d
            return Padding(
              padding: const EdgeInsets.only(left: 16, bottom: 2),
              child: Text('($letter) ${question.options[i]}', style: TextStyle(fontSize: 13.5, color: AppColors.inkSoft)),
            );
          }),
        ],
      ),
    );
  }
}

class _AnswerKeyView extends StatelessWidget {
  final QuestionPaper paper;

  const _AnswerKeyView({required this.paper});

  @override
  Widget build(BuildContext context) {
    var questionNumber = 0;
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        Center(
          child: Text('${paper.title} — Answer Key',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: AppColors.ink)),
        ),
        const Divider(height: 32),
        for (final section in paper.sections) ...[
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Text(section.heading, style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15)),
          ),
          for (final q in section.questions) ...[
            Builder(builder: (context) {
              questionNumber++;
              final letter = String.fromCharCode(97 + q.correctIndex);
              return Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('$questionNumber. ($letter) ${q.correctAnswer}',
                        style: TextStyle(fontWeight: FontWeight.w700, fontSize: 13.5, color: AppColors.success)),
                    Text(q.explanation, style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft)),
                  ],
                ),
              );
            }),
          ],
          const SizedBox(height: 12),
        ],
      ],
    );
  }
}
