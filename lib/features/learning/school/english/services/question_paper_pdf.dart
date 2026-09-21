import 'dart:typed_data';

import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';

import '../models/question_paper.dart';

// Watermark is handled centrally by PdfBrandingUtil.getPageTheme().
// It uses assets/shineacademynarodalogo.jpg at 0.15 opacity on every page.

Future<Uint8List> buildQuestionPaperPdf(QuestionPaper paper) async {
  final doc = pw.Document();
  final pageTheme = await PdfBrandingUtil.getPageTheme(
    pageFormat: PdfPageFormat.a4,
  );

  doc.addPage(pw.MultiPage(
    pageTheme: pageTheme,
    build: (context) => [
      _paperHeader(paper),
      pw.SizedBox(height: 16),
      for (final section in paper.sections) _paperSection(section),
    ],
  ));

  return doc.save();
}

Future<Uint8List> buildAnswerKeyPdf(QuestionPaper paper) async {
  final doc = pw.Document();
  final pageTheme = await PdfBrandingUtil.getPageTheme(
    pageFormat: PdfPageFormat.a4,
  );

  doc.addPage(pw.MultiPage(
    pageTheme: pageTheme,
    build: (context) => [
      pw.Center(
        child: pw.Text('${paper.title} - Answer Key', style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold)),
      ),
      pw.SizedBox(height: 16),
      for (final section in paper.sections) _answerKeySection(section),
    ],
  ));

  return doc.save();
}

pw.Widget _paperHeader(QuestionPaper paper) {
  return pw.Column(
    crossAxisAlignment: pw.CrossAxisAlignment.center,
    children: [
      pw.Text(paper.title, style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold)),
      pw.SizedBox(height: 4),
      pw.Text(
        '${paper.grade}  -  Total Marks: ${paper.totalMarks}  -  Questions: ${paper.totalQuestions}',
        style: const pw.TextStyle(fontSize: 11, color: PdfColors.grey700),
      ),
      pw.SizedBox(height: 8),
      pw.Divider(),
    ],
  );
}

pw.Widget _paperSection(PaperSection section) {
  return pw.Padding(
    padding: const pw.EdgeInsets.only(bottom: 16),
    child: pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Row(
          mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
          children: [
            pw.Text(section.heading, style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold)),
            pw.Text('${section.totalMarks} marks', style: const pw.TextStyle(fontSize: 10, color: PdfColors.grey700)),
          ],
        ),
        pw.SizedBox(height: 2),
        pw.Text(section.instructions, style: pw.TextStyle(fontSize: 10, fontStyle: pw.FontStyle.italic, color: PdfColors.grey700)),
        if (section.passageText != null && section.passageText!.isNotEmpty) ...[
          pw.SizedBox(height: 8),
          pw.Container(
            padding: const pw.EdgeInsets.all(10),
            decoration: pw.BoxDecoration(
              color: PdfColors.grey100,
              border: pw.Border.all(color: PdfColors.grey300),
            ),
            child: pw.Text(section.passageText!, style: const pw.TextStyle(fontSize: 11, lineSpacing: 1.5)),
          ),
        ],
        pw.SizedBox(height: 6),
        for (var i = 0; i < section.questions.length; i++) _paperQuestion(i + 1, section.questions[i]),
      ],
    ),
  );
}

pw.Widget _paperQuestion(int number, dynamic question) {
  return pw.Padding(
    padding: const pw.EdgeInsets.only(bottom: 8),
    child: pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Text('$number. ${question.prompt}', style: const pw.TextStyle(fontSize: 11)),
        pw.SizedBox(height: 2),
        for (var i = 0; i < (question.options as List).length; i++)
          pw.Padding(
            padding: const pw.EdgeInsets.only(left: 14, bottom: 1),
            child: pw.Text(
              '(${String.fromCharCode(97 + i)}) ${question.options[i]}',
              style: const pw.TextStyle(fontSize: 10.5, color: PdfColors.grey800),
            ),
          ),
      ],
    ),
  );
}

pw.Widget _answerKeySection(PaperSection section) {
  return pw.Padding(
    padding: const pw.EdgeInsets.only(bottom: 14),
    child: pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Text(section.heading, style: pw.TextStyle(fontSize: 13, fontWeight: pw.FontWeight.bold)),
        pw.SizedBox(height: 4),
        for (var i = 0; i < section.questions.length; i++) _answerKeyQuestion(i + 1, section.questions[i]),
      ],
    ),
  );
}

pw.Widget _answerKeyQuestion(int number, dynamic question) {
  final letter = String.fromCharCode(97 + (question.correctIndex as int));
  return pw.Padding(
    padding: const pw.EdgeInsets.only(bottom: 6),
    child: pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Text('$number. ($letter) ${question.correctAnswer}',
            style: pw.TextStyle(fontSize: 11, fontWeight: pw.FontWeight.bold, color: PdfColors.green800)),
        pw.Text(question.explanation as String, style: const pw.TextStyle(fontSize: 10, color: PdfColors.grey800)),
      ],
    ),
  );
}
