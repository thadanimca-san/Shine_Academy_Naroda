import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/utils/pdf_viewer_util.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/foundation/theme/app_typography.dart';
import '../widgets/paper_question_tile.dart';

/// Question paper and answer key PDFs.
///
/// Pages are drawn with the same Flutter widgets as the on-screen paper and
/// captured as images, so LaTeX formulas and Gujarati/Hindi text print exactly
/// as on screen, text cannot be copied out, and every page carries the shared
/// Shine Academy watermark.
class PdfExportService {
  static Future<void> generateAndPreviewQuestionPaper(BuildContext context, String title, List<AssessmentQuestion> questions,
      {String? schoolName, String? examTitle, String? timeAllowed, List<String>? instructions}) {
    return _export(context, title, questions,
        showAnswers: false, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed, instructions: instructions);
  }

  static Future<void> generateAndPreviewAnswerKey(BuildContext context, String title, List<AssessmentQuestion> questions,
      {String? schoolName, String? examTitle, String? timeAllowed, List<String>? instructions}) {
    return _export(context, title, questions,
        showAnswers: true, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed, instructions: instructions);
  }

  static Future<void> _export(BuildContext context, String title, List<AssessmentQuestion> questions,
      {required bool showAnswers, String? schoolName, String? examTitle, String? timeAllowed, List<String>? instructions}) async {
    // Callers often pass the context of a details dialog that closes right
    // away, so keep the navigator now: the progress dialog must always close.
    final navigator = Navigator.of(context, rootNavigator: true);
    final progress = ValueNotifier<String>(TrilingualService.instance.getUIText('Preparing pages...'));
    var progressOpen = true;
    void closeProgress() {
      if (progressOpen && navigator.mounted) navigator.pop();
      progressOpen = false;
    }

    _showProgress(navigator.context, progress);
    try {
      final items = _withSectionsIfMissing(questions);
      final widgets = <Widget>[
        _PaperHeader(
          schoolName: schoolName,
          examTitle: examTitle,
          timeAllowed: timeAllowed,
          totalMarks: items.where((q) => q.type != 'section_header').fold(0, (sum, q) => sum + q.marks),
          instructions: instructions ?? _defaultInstructions,
        ),
        ...buildPaperTiles(items, showAnswers: showAnswers, isPdfMode: true),
      ];
      final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
        title: title,
        widgets: widgets,
        isAnswerKey: showAnswers,
        onProgress: (done, total) => progress.value = '${TrilingualService.instance.getUIText('Drawing page items')} $done / $total',
      );
      closeProgress();
      final prefix = showAnswers ? 'Answer_Key_' : 'Question_Paper_';
      await PdfViewerUtil.openPdfBytes(bytes, '$prefix${title.replaceAll(RegExp(r'[^a-zA-Z0-9_\-]'), '_')}.pdf');
    } finally {
      closeProgress();
      progress.dispose();
    }
  }

  static const List<String> _defaultInstructions = [
    'All questions are compulsory.',
    'Figures to the right indicate the marks for each question.',
    'Write your answers neatly in the answer sheet.',
  ];

  /// Custom papers without section headers are grouped into objective and
  /// written sections, as printed papers expect.
  static List<AssessmentQuestion> _withSectionsIfMissing(List<AssessmentQuestion> questions) {
    if (questions.any((q) => q.type == 'section_header')) return questions;
    bool isObjective(AssessmentQuestion q) => q.type == 'quiz' || q.type == 'true_false' || q.type == 'fill_blank';
    AssessmentQuestion header(String text) => AssessmentQuestion(
        moduleId: 'header', type: 'section_header', question: TrilingualService.instance.getUIText(text),
        options: const [], correctIndexOrAnswer: '', marks: 0);

    final objective = questions.where(isObjective).toList();
    final written = questions.where((q) => !isObjective(q)).toList();
    return [
      if (objective.isNotEmpty) ...[header('SECTION A (Objective Type)'), ...objective],
      if (written.isNotEmpty) ...[header('SECTION B (Descriptive Type)'), ...written],
    ];
  }

  static void _showProgress(BuildContext context, ValueNotifier<String> message) {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) => AlertDialog(
        content: Row(
          children: [
            const CircularProgressIndicator(),
            const SizedBox(width: 20),
            Expanded(child: ValueListenableBuilder<String>(valueListenable: message, builder: (_, text, __) => Text(text))),
          ],
        ),
      ),
    );
  }
}

class _PaperHeader extends StatelessWidget {
  final String? schoolName;
  final String? examTitle;
  final String? timeAllowed;
  final int totalMarks;
  final List<String> instructions;

  const _PaperHeader({
    required this.schoolName,
    required this.examTitle,
    required this.timeAllowed,
    required this.totalMarks,
    required this.instructions,
  });

  @override
  Widget build(BuildContext context) {
    final onSurface = Theme.of(context).colorScheme.onSurface;
    final bold = AppTypography.body(context, color: onSurface, fontWeight: FontWeight.bold);
    final small = AppTypography.bodySmall(context, color: onSurface);
    final ui = TrilingualService.instance.getUIText;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (schoolName?.isNotEmpty ?? false)
          Text(schoolName!, textAlign: TextAlign.center, style: AppTypography.h3(context, color: onSurface)),
        if (examTitle?.isNotEmpty ?? false) Text(examTitle!, textAlign: TextAlign.center, style: bold),
        const SizedBox(height: 8),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text((timeAllowed?.isNotEmpty ?? false) ? '${ui('Time')}: $timeAllowed' : '', style: bold),
            Text('${ui('Maximum Marks')}: $totalMarks', style: bold),
          ],
        ),
        const Divider(thickness: 1.5),
        Container(
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(border: Border.all(color: onSurface)),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(ui('General Instructions:'), style: bold),
              for (var i = 0; i < instructions.length; i++) Text('${i + 1}. ${ui(instructions[i])}', style: small),
            ],
          ),
        ),
        const SizedBox(height: 12),
      ],
    );
  }
}
