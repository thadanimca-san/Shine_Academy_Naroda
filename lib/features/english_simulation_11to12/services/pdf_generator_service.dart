import 'package:flutter/services.dart' show rootBundle;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import '../models/chapter_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PdfGeneratorService {
  // --- Multi-chapter methods ---
  static Future<void> generateAndOpenQuestionPaper(List<ChapterModel> chapters) async {
    await _generatePdf(chapters, isAnswerKey: false);
  }

  static Future<void> generateAndOpenAnswerKey(List<ChapterModel> chapters) async {
    await _generatePdf(chapters, isAnswerKey: true);
  }

  // --- Single-chapter aliases ---
  static Future<void> generateQuestionPaperPDF(ChapterModel chapter, [dynamic extra]) async {
    await _generatePdf([chapter], isAnswerKey: false);
  }

  static Future<void> generateAnswerKeyPDF(ChapterModel chapter, [dynamic extra]) async {
    await _generatePdf([chapter], isAnswerKey: true);
  }

  // --- Core shared generator logic ---
  static Future<void> _generatePdf(List<ChapterModel> chapters, {required bool isAnswerKey}) async {
    // Use a Unicode-capable font so special characters used across the
    // question bank (², ³, ⁵, ×, ·, →, °, λ, subscripts, etc.) render
    // correctly instead of showing up as missing-glyph boxes with the
    // package's default Helvetica-based fonts.
    final regularFontData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final boldFontData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    final regularFont = pw.Font.ttf(regularFontData);
    final boldFont = pw.Font.ttf(boldFontData);

    final pdf = pw.Document(
      theme: pw.ThemeData.withFont(base: regularFont, bold: boldFont),
    );

    final subjectLabel = chapters.isNotEmpty ? '${chapters.first.subject} (Class ${chapters.first.standard})' : 'Assessment';

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.fromLTRB(32, 32, 32, 44),
        footer: (pw.Context context) => pw.Column(
          children: [
            pw.Divider(color: PdfColors.grey300, thickness: 0.5),
            pw.Row(
              mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
              children: [
                pw.UrlLink(
                  destination: 'https://www.youtube.com/@Kashish_Thadani',
                  child: pw.Text(TrilingualService.instance.getUIText('Learn with Videos - Joy of Learning with Kashish - youtube.com/@Kashish_Thadani'),
                    style: pw.TextStyle(fontSize: 9, color: PdfColors.red800, decoration: pw.TextDecoration.underline),
                  ),
                ),
                pw.Text(
                  'Page ${context.pageNumber} of ${context.pagesCount}',
                  style: const pw.TextStyle(fontSize: 9, color: PdfColors.grey600),
                ),
              ],
            ),
          ],
        ),
        build: (pw.Context context) {
          List<pw.Widget> content = [
            pw.Header(
              level: 0,
              child: pw.Text(
                isAnswerKey ? '$subjectLabel - Answer Key' : '$subjectLabel - Question Paper',
                style: pw.TextStyle(
                  fontSize: 20,
                  fontWeight: pw.FontWeight.bold,
                  color: isAnswerKey ? PdfColors.green800 : PdfColors.blue800,
                ),
              ),
            ),
            pw.SizedBox(height: 10),
            pw.Text(
              isAnswerKey
                  ? 'Complete solutions and answer keys corresponding to the assessment questions.'
                  : 'Instructions: Fill in the blanks with the appropriate term.',
              style: const pw.TextStyle(fontSize: 12),
            ),
            pw.SizedBox(height: 20),
          ];

          int questionNumber = 1;
          for (var chapter in chapters) {
            content.add(
              pw.Padding(
                padding: const pw.EdgeInsets.only(top: 12, bottom: 6),
                child: pw.Text(
                  'Chapter: ${chapter.chapterName} (${chapter.subject})',
                  style: pw.TextStyle(
                    fontSize: 14,
                    fontWeight: pw.FontWeight.bold,
                    color: PdfColors.grey800,
                  ),
                ),
              ),
            );

            for (var item in chapter.fillInTheBlanks) {
              // Replace any square brackets [...] with round brackets (...) in the question text
              String formattedQuestion = item.question
                  .replaceAll('[', '(')
                  .replaceAll(']', ')');

              content.add(
                pw.Padding(
                  padding: const pw.EdgeInsets.symmetric(vertical: 6),
                  child: pw.Column(
                    crossAxisAlignment: pw.CrossAxisAlignment.start,
                    children: [
                      pw.Text(
                        '$questionNumber. $formattedQuestion',
                        style: const pw.TextStyle(fontSize: 12),
                      ),
                      if (isAnswerKey) ...[
                        pw.SizedBox(height: 2),
                        pw.Text(
                          '   Answer: ${item.answer}',
                          style: pw.TextStyle(
                            fontSize: 12,
                            fontWeight: pw.FontWeight.bold,
                            color: PdfColors.green900,
                          ),
                        ),
                      ],
                    ],
                  ),
                ),
              );
              questionNumber++;
            }

            for (var problem in chapter.numericalProblems) {
              content.add(
                pw.Padding(
                  padding: const pw.EdgeInsets.symmetric(vertical: 6),
                  child: pw.Column(
                    crossAxisAlignment: pw.CrossAxisAlignment.start,
                    children: [
                      pw.Text(
                        '$questionNumber. ${problem.question}',
                        style: const pw.TextStyle(fontSize: 12),
                      ),
                      if (problem.given.isNotEmpty)
                        pw.Text(
                          '   Given: ${problem.given.join(', ')}',
                          style: pw.TextStyle(fontSize: 11, fontStyle: pw.FontStyle.italic, color: PdfColors.grey700),
                        ),
                      if (isAnswerKey) ...[
                        pw.SizedBox(height: 2),
                        for (var i = 0; i < problem.solutionSteps.length; i++)
                          pw.Text(
                            '   ${i + 1}. ${problem.solutionSteps[i]}',
                            style: const pw.TextStyle(fontSize: 11),
                          ),
                        pw.Text(
                          '   Final Answer: ${problem.formattedAnswer}',
                          style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold, color: PdfColors.green900),
                        ),
                      ],
                    ],
                  ),
                ),
              );
              questionNumber++;
            }
          }

          return content;
        },
      ),
    );

    // Save PDF bytes and open directly with the system's default PDF reader
    final bytes = await pdf.save();
    await Printing.sharePdf(
      bytes: bytes,
      filename: isAnswerKey ? 'Class9_Answer_Key.pdf' : 'Class9_Question_Paper.pdf',
    );
  }
}