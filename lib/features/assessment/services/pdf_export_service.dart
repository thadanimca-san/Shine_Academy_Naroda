import 'package:flutter/material.dart' show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';

class PdfExportService {
  static Future<void> generateAndPreviewQuestionPaper(BuildContext context, String title, List<AssessmentQuestion> questions, {String? schoolName, String? examTitle, String? timeAllowed}) async {
    final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: false, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);
    _showProgress(context, "Generating PDF natively...");
    try {
      await Future.delayed(const Duration(milliseconds: 100));
      await UniversalPdfEngine.generateNativePdfTextOnly(
        title: title,
        widgets: widgets,
        isAnswerKey: false,
      );
    } finally {
      if (context.mounted) Navigator.of(context, rootNavigator: true).pop();
    }
  }

  static Future<void> generateAndPreviewAnswerKey(BuildContext context, String title, List<AssessmentQuestion> questions, {String? schoolName, String? examTitle, String? timeAllowed}) async {
    final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: true, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);
    _showProgress(context, "Generating PDF natively...");
    try {
      await Future.delayed(const Duration(milliseconds: 100));
      await UniversalPdfEngine.generateNativePdfTextOnly(
        title: title,
        widgets: widgets,
        isAnswerKey: true,
      );
    } finally {
      if (context.mounted) Navigator.of(context, rootNavigator: true).pop();
    }
  }

  static List<pw.Widget> _buildGroupedQuestionsWidgets(List<AssessmentQuestion> questions, {required bool showAnswers, String? schoolName, String? examTitle, String? timeAllowed}) {
    List<pw.Widget> widgets = [];
    
    
    if (schoolName != null && schoolName.isNotEmpty) {
      widgets.add(pw.Center(child: pw.Text(schoolName, style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold))));
      widgets.add(pw.SizedBox(height: 4));
    }
    if (examTitle != null && examTitle.isNotEmpty) {
      widgets.add(pw.Center(child: pw.Text(examTitle, style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold))));
      widgets.add(pw.SizedBox(height: 8));
    }
    
    if ((timeAllowed != null && timeAllowed.isNotEmpty) || (schoolName != null && schoolName.isNotEmpty)) {
       int totalMarks = questions.fold(0, (sum, q) => q.type == 'section_header' ? sum : sum + q.marks);
       widgets.add(
         pw.Row(
           mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
           children: [
             if (timeAllowed != null && timeAllowed.isNotEmpty) 
                pw.Text('Time: $timeAllowed', style: pw.TextStyle(fontWeight: pw.FontWeight.bold))
             else pw.SizedBox(),
             pw.Text('Total Marks: $totalMarks', style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
           ]
         )
       );
       widgets.add(pw.Divider());
    }

    widgets.add(pw.SizedBox(height: 10));
    widgets.add(_buildInstructions());
    widgets.add(pw.SizedBox(height: 20));

    // Check if the paper is pre-structured with section headers (Board Pattern)
    bool isStructured = questions.any((q) => q.type == 'section_header');

    if (isStructured) {
      int globalQNum = 1;
      for (var q in questions) {
        if (q.type == 'section_header') {
          widgets.add(pw.SizedBox(height: 12));
          widgets.add(pw.Center(child: pw.Text(_getLocalizedQuestion(q), style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold))));
          widgets.add(pw.SizedBox(height: 12));
        } else {
          widgets.add(_buildSingleQuestion(q, globalQNum, q.marks, showAnswers: showAnswers));
          globalQNum++;
        }
      }
    } else {
      // Standard Custom: Group manually
      final objectiveQs = questions.where((q) => q.type == 'quiz' || q.type == 'true_false' || q.type == 'fill_blank').toList();
      final subjectiveQs = questions.where((q) => q.type != 'quiz' && q.type != 'true_false' && q.type != 'fill_blank' && q.type != 'section_header').toList();

      int globalQNum = 1;

      if (objectiveQs.isNotEmpty) {
        widgets.add(pw.Center(child: pw.Text(TrilingualService.instance.getUIText('SECTION A (Objective Type)'), style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold))));
        widgets.add(pw.SizedBox(height: 12));
        
        for (var q in objectiveQs) {
          widgets.add(_buildSingleQuestion(q, globalQNum, q.marks, showAnswers: showAnswers));
          globalQNum++;
        }
        widgets.add(pw.SizedBox(height: 20));
      }

      if (subjectiveQs.isNotEmpty) {
        widgets.add(pw.Center(child: pw.Text(TrilingualService.instance.getUIText('SECTION B (Descriptive Type)'), style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold))));
        widgets.add(pw.SizedBox(height: 12));
        
        for (var q in subjectiveQs) {
          widgets.add(_buildSingleQuestion(q, globalQNum, q.marks, showAnswers: showAnswers));
          globalQNum++;
        }
      }
    }

    return widgets;
  }

  static pw.Widget _buildInstructions() {
    return pw.Container(
      padding: const pw.EdgeInsets.all(8),
      decoration: pw.BoxDecoration(
        border: pw.Border.all(color: PdfColors.black, width: 1),
      ),
      child: pw.Column(
        crossAxisAlignment: pw.CrossAxisAlignment.start,
        children: [
          pw.Text(TrilingualService.instance.getUIText('General Instructions:'), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
          pw.SizedBox(height: 4),
          pw.Text(TrilingualService.instance.getUIText('1. All questions are compulsory. There are no internal choices.'), style: const pw.TextStyle(fontSize: 14)),
          pw.Text(TrilingualService.instance.getUIText('2. The paper is divided into Section A (Objective) and Section B (Subjective).'), style: const pw.TextStyle(fontSize: 14)),
          pw.Text(TrilingualService.instance.getUIText('3. Figures to the right indicate marks allocated to the question.'), style: const pw.TextStyle(fontSize: 14)),
          pw.Text(TrilingualService.instance.getUIText('4. Write your answers neatly in the provided answer supplement.'), style: const pw.TextStyle(fontSize: 14)),
        ],
      ),
    );
  }

  static String _getLocalizedQuestion(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    String text = q.question;
    if (lang == 'hi' && q.questionHi != null && q.questionHi!.isNotEmpty) text = q.questionHi!;
    if (lang == 'gu' && q.questionGu != null && q.questionGu!.isNotEmpty) text = q.questionGu!;
    return _cleanLatexText(text);
  }

  static String? _getLocalizedExplanation(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    String? text = q.explanationEn;
    if (lang == 'hi' && q.explanationHi != null && q.explanationHi!.isNotEmpty) text = q.explanationHi!;
    if (lang == 'gu' && q.explanationGu != null && q.explanationGu!.isNotEmpty) text = q.explanationGu!;
    return text != null ? _cleanLatexText(text) : null;
  }

  static List<String> _getLocalizedOptions(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    List<String> opts = q.options;
    if (lang == 'hi' && q.optionsHi != null && q.optionsHi!.isNotEmpty) opts = q.optionsHi!;
    if (lang == 'gu' && q.optionsGu != null && q.optionsGu!.isNotEmpty) opts = q.optionsGu!;
    return opts.map((o) => _cleanLatexText(o)).toList();
  }

  static String _cleanLatexText(String text) {
    String clean = text
        .replaceAll(r'\triangle', '△')
        .replaceAll(r'\angle', '∠')
        .replaceAll(r'\circ', '°')
        .replaceAll(r'\sim', '~')
        .replaceAll(r'\cong', '≅')
        .replaceAll(r'\pi', 'π')
        .replaceAll(r'\theta', 'θ')
        .replaceAll(r'\alpha', 'α')
        .replaceAll(r'\beta', 'β')
        .replaceAll(r'\sqrt', '√')
        .replaceAll(r'\times', '×')
        .replaceAll(r'\div', '÷')
        .replaceAll(r'\pm', '±')
        .replaceAll(r'\neq', '≠')
        .replaceAll(r'\leq', '≤')
        .replaceAll(r'\geq', '≥')
        .replaceAll(r'\infty', '∞')
        .replaceAll(r'\rightarrow', '→')
        .replaceAll(r'\Rightarrow', '⇒');

    // Remove $ signs used for inline math
    clean = clean.replaceAll(r'$', '');
    
    return clean;
  }

  static pw.Widget _buildSingleQuestion(AssessmentQuestion q, int qNum, int marks, {required bool showAnswers}) {
    final localizedQ = _getLocalizedQuestion(q);
    final localizedOpts = _getLocalizedOptions(q);

    return pw.Padding(
      padding: const pw.EdgeInsets.only(bottom: 12),
      child: pw.Column(
        crossAxisAlignment: pw.CrossAxisAlignment.start,
        children: [
          pw.Row(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Expanded(
                child: pw.Text('Q$qNum. $localizedQ', style: pw.TextStyle(fontSize: 15, fontWeight: pw.FontWeight.bold)),
              ),
              pw.Text('[$marks]', style: const pw.TextStyle(fontSize: 14)),
            ]
          ),
          pw.SizedBox(height: 6),
          if (q.type == 'quiz')
            pw.Padding(
              padding: const pw.EdgeInsets.only(left: 20),
              child: pw.Wrap(
                spacing: 20,
                runSpacing: 6,
                children: List.generate(
                  localizedOpts.length,
                  (j) => pw.Text(
                    '(${String.fromCharCode(97 + j)}) ${localizedOpts[j]}',
                    style: const pw.TextStyle(fontSize: 14),
                  ),
                ),
              ),
            )
          else if (q.type == 'true_false')
            pw.Padding(
              padding: const pw.EdgeInsets.only(left: 20),
              child: pw.Text(TrilingualService.instance.getUIText('(True / False)'), style: pw.TextStyle(fontSize: 14, fontStyle: pw.FontStyle.italic)),
            ),
          
          if (showAnswers) ...[
            pw.Padding(
              padding: const pw.EdgeInsets.only(left: 20, top: 6),
              child: pw.Text(
                'Ans: ${_getAnswerText(q, localizedOpts)}',
                style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold, color: PdfColors.green),
              ),
            ),
            if (_getLocalizedExplanation(q) != null && _getLocalizedExplanation(q)!.isNotEmpty)
              pw.Padding(
                padding: const pw.EdgeInsets.only(left: 20, top: 2),
                child: pw.Text(
                  'Solution: ${_getLocalizedExplanation(q)}',
                  style: pw.TextStyle(fontSize: 14, fontStyle: pw.FontStyle.italic, color: PdfColors.grey700),
                ),
              ),
          ]
        ],
      ),
    );
  }

  static String _getAnswerText(AssessmentQuestion q, List<String> localizedOpts) {
    if (q.type == 'quiz') {
       int idx = q.correctIndexOrAnswer is int ? q.correctIndexOrAnswer : 0;
       if (idx >= 0 && idx < localizedOpts.length) {
         return '(${String.fromCharCode(97 + idx)}) ${_cleanLatexText(localizedOpts[idx])}';
       }
       return 'Error';
    }
    return _cleanLatexText(q.correctIndexOrAnswer.toString());
  }

  static void _showProgress(BuildContext context, String message) {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          content: Row(
            children: [
              const CircularProgressIndicator(),
              const SizedBox(width: 20),
              Text(message),
            ],
          ),
        );
      },
    );
  }
}
