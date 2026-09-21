import 'dart:io';
import 'dart:typed_data';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import '../../../core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PdfExportService {
  /// Generates and previews the Question Paper PDF
  static Future<void> generateAndPreviewQuestionPaper(String title, List<AssessmentQuestion> questions, {String schoolName = 'Shine Academy Naroda', String examTitle = 'TERM EXAMINATION', String timeAllowed = '1 Hr 30 Min'}) async {
    final pdf = await _buildQuestionPaperPdf(questions, title: title, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);
    final bytes = await pdf.save();
    final flattenedBytes = await _flattenPdfBytes(bytes);
    
    final dir = await getTemporaryDirectory();
    final file = File('${dir.path}/Question_Paper_${title.replaceAll(' ', '_')}.pdf');
    await file.writeAsBytes(flattenedBytes);
    await OpenFilex.open(file.path);
  }

  /// Generates and previews the Answer Key PDF
  static Future<void> generateAndPreviewAnswerKey(String title, List<AssessmentQuestion> questions, {String schoolName = 'Shine Academy Naroda', String examTitle = 'TERM EXAMINATION', String timeAllowed = '1 Hr 30 Min'}) async {
    final pdf = await _buildAnswerKeyPdf(questions, title: title, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);
    final bytes = await pdf.save();
    final flattenedBytes = await _flattenPdfBytes(bytes);
    
    final dir = await getTemporaryDirectory();
    final file = File('${dir.path}/Answer_Key_${title.replaceAll(' ', '_')}.pdf');
    await file.writeAsBytes(flattenedBytes);
    await OpenFilex.open(file.path);
  }

  /// Flattens a PDF into an image-based PDF for maximum security
  static Future<Uint8List> _flattenPdfBytes(Uint8List originalBytes) async {
    final newPdf = pw.Document();
    
    // Rasterize at 200 DPI for good balance between quality and file size
    final rasters = Printing.raster(originalBytes, dpi: 200.0);
    
    await for (final raster in rasters) {
      final pngBytes = await raster.toPng();
      final memoryImage = pw.MemoryImage(pngBytes);
      
      newPdf.addPage(
        pw.Page(
          pageFormat: PdfPageFormat.a4,
          margin: pw.EdgeInsets.zero,
          build: (pw.Context context) {
            return pw.Center(
              child: pw.Image(memoryImage, fit: pw.BoxFit.contain),
            );
          },
        ),
      );
    }
    
    return await newPdf.save();
  }

  static Future<pw.Document> _buildQuestionPaperPdf(List<AssessmentQuestion> questions, {required String title, required String schoolName, required String examTitle, required String timeAllowed}) async {
    final pdf = pw.Document();
    final pageTheme = await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4);

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        header: (pw.Context context) => _buildHeader(title, questions, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed, isAnswerKey: false),
        build: (pw.Context context) {
          return [
            pw.SizedBox(height: 10),
            _buildInstructions(),
            pw.SizedBox(height: 20),
            ..._buildGroupedQuestionsList(questions, showAnswers: false),
          ];
        },
      ),
    );

    return pdf;
  }

  static Future<pw.Document> _buildAnswerKeyPdf(List<AssessmentQuestion> questions, {required String title, required String schoolName, required String examTitle, required String timeAllowed}) async {
    final pdf = pw.Document();
    final pageTheme = await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4);

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        header: (pw.Context context) => _buildHeader(title, questions, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed, isAnswerKey: true),
        build: (pw.Context context) {
          return [
            pw.SizedBox(height: 20),
            ..._buildGroupedQuestionsList(questions, showAnswers: true),
          ];
        },
      ),
    );

    return pdf;
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
          pw.Text(TrilingualService.instance.getUIText('General Instructions:'), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)),
          pw.SizedBox(height: 4),
          pw.Text(TrilingualService.instance.getUIText('1. All questions are compulsory. There are no internal choices.'), style: const pw.TextStyle(fontSize: 10)),
          pw.Text(TrilingualService.instance.getUIText('2. The paper is divided into Section A (Objective) and Section B (Subjective).'), style: const pw.TextStyle(fontSize: 10)),
          pw.Text(TrilingualService.instance.getUIText('3. Figures to the right indicate marks allocated to the question.'), style: const pw.TextStyle(fontSize: 10)),
          pw.Text(TrilingualService.instance.getUIText('4. Write your answers neatly in the provided answer supplement.'), style: const pw.TextStyle(fontSize: 10)),
        ],
      ),
    );
  }

  static pw.Widget _buildHeader(String title, List<AssessmentQuestion> questions, {required bool isAnswerKey, required String schoolName, required String examTitle, required String timeAllowed}) {
    // Total marks: Use the marks assigned to each question.
    int totalMarks = 0;
    for (var q in questions) {
      if (q.type != 'section_header') {
        totalMarks += q.marks;
      }
    }

    final today = DateTime.now();
    final dateString = "${today.day.toString().padLeft(2, '0')}/${today.month.toString().padLeft(2, '0')}/${today.year}";
    
    // Attempt to extract standard and subject from title (e.g. "GSEB CLASS7 - Maths")
    String standard = "________";
    String subject = "________";
    if (title.contains('-')) {
      final parts = title.split('-');
      standard = parts[0].trim();
      subject = parts[1].trim();
    } else {
      subject = title;
    }

    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.center,
      children: [
        pw.Text(
          schoolName.toUpperCase(),
          style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold),
        ),
        pw.SizedBox(height: 4),
        pw.Text(
          isAnswerKey ? 'OFFICIAL ANSWER KEY' : examTitle.toUpperCase(),
          style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold),
        ),
        pw.SizedBox(height: 12),
        pw.Row(
          mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
          crossAxisAlignment: pw.CrossAxisAlignment.start,
          children: [
            // Left Column
            pw.Column(
              crossAxisAlignment: pw.CrossAxisAlignment.start,
              children: [
                pw.Text('Standard: $standard', style: pw.TextStyle(fontSize: 11, fontWeight: pw.FontWeight.bold)),
                pw.SizedBox(height: 4),
                pw.Text('Subject: $subject', style: pw.TextStyle(fontSize: 11, fontWeight: pw.FontWeight.bold)),
                pw.SizedBox(height: 4),
                pw.Text('Date: $dateString', style: const pw.TextStyle(fontSize: 11)),
              ]
            ),
            // Right Column
            pw.Column(
              crossAxisAlignment: pw.CrossAxisAlignment.end,
              children: [
                pw.Text('Total Marks: $totalMarks', style: pw.TextStyle(fontSize: 11, fontWeight: pw.FontWeight.bold)),
                pw.SizedBox(height: 4),
                pw.Text('Time Allowed: $timeAllowed', style: const pw.TextStyle(fontSize: 11)),
                pw.SizedBox(height: 4),
                pw.Text(TrilingualService.instance.getUIText('Roll No: __________'), style: const pw.TextStyle(fontSize: 11)),
              ]
            ),
          ],
        ),
        pw.SizedBox(height: 8),
        pw.Divider(thickness: 1.5),
      ],
    );
  }

  static String _getLocalizedQuestion(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && q.questionHi != null && q.questionHi!.isNotEmpty) return q.questionHi!;
    if (lang == 'gu' && q.questionGu != null && q.questionGu!.isNotEmpty) return q.questionGu!;
    return q.question;
  }

  static String? _getLocalizedExplanation(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && q.explanationHi != null && q.explanationHi!.isNotEmpty) return q.explanationHi!;
    if (lang == 'gu' && q.explanationGu != null && q.explanationGu!.isNotEmpty) return q.explanationGu!;
    return q.explanationEn;
  }

  static List<String> _getLocalizedOptions(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && q.optionsHi != null && q.optionsHi!.isNotEmpty) return q.optionsHi!;
    if (lang == 'gu' && q.optionsGu != null && q.optionsGu!.isNotEmpty) return q.optionsGu!;
    return q.options;
  }

  static List<pw.Widget> _buildGroupedQuestionsList(List<AssessmentQuestion> questions, {required bool showAnswers}) {
    List<pw.Widget> widgets = [];
    
    // Check if the paper is pre-structured with section headers (Board Pattern)
    bool isStructured = questions.any((q) => q.type == 'section_header');

    if (isStructured) {
      int globalQNum = 1;
      for (var q in questions) {
        if (q.type == 'section_header') {
          widgets.add(pw.SizedBox(height: 12));
          widgets.add(pw.Center(child: pw.Text(_getLocalizedQuestion(q), style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold))));
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
        widgets.add(pw.Center(child: pw.Text(TrilingualService.instance.getUIText('SECTION A (Objective Type)'), style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold))));
        widgets.add(pw.SizedBox(height: 12));
        
        for (var q in objectiveQs) {
          widgets.add(_buildSingleQuestion(q, globalQNum, q.marks, showAnswers: showAnswers));
          globalQNum++;
        }
        widgets.add(pw.SizedBox(height: 20));
      }

      if (subjectiveQs.isNotEmpty) {
        widgets.add(pw.Center(child: pw.Text(TrilingualService.instance.getUIText('SECTION B (Descriptive Type)'), style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold))));
        widgets.add(pw.SizedBox(height: 12));
        
        for (var q in subjectiveQs) {
          widgets.add(_buildSingleQuestion(q, globalQNum, q.marks, showAnswers: showAnswers));
          globalQNum++;
        }
      }
    }

    return widgets;
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
                child: pw.Text('Q$qNum. $localizedQ', style: pw.TextStyle(fontSize: 11, fontWeight: pw.FontWeight.bold)),
              ),
              pw.Text('[$marks]', style: const pw.TextStyle(fontSize: 10)), // Marks on the right
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
                    style: const pw.TextStyle(fontSize: 10),
                  ),
                ),
              ),
            )
          else if (q.type == 'true_false')
            pw.Padding(
              padding: const pw.EdgeInsets.only(left: 20),
              child: pw.Text(TrilingualService.instance.getUIText('(True / False)'), style: const pw.TextStyle(fontSize: 10, fontStyle: pw.FontStyle.italic)),
            ),
          
          if (showAnswers) ...[
            pw.Padding(
              padding: const pw.EdgeInsets.only(left: 20, top: 6),
              child: pw.Text(
                'Ans: ${_getAnswerText(q, localizedOpts)}',
                style: pw.TextStyle(fontSize: 10, fontWeight: pw.FontWeight.bold, color: PdfColors.green800),
              ),
            ),
            if (_getLocalizedExplanation(q) != null && _getLocalizedExplanation(q)!.isNotEmpty)
              pw.Padding(
                padding: const pw.EdgeInsets.only(left: 20, top: 2),
                child: pw.Text(
                  'Solution: ${_getLocalizedExplanation(q)}',
                  style: pw.TextStyle(fontSize: 10, fontStyle: pw.FontStyle.italic, color: PdfColors.grey700),
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
         return '(${String.fromCharCode(97 + idx)}) ${localizedOpts[idx]}';
       }
       return 'Error';
    }
    return q.correctIndexOrAnswer.toString();
  }

  // _buildCompactAnswerKey was replaced by inline answers in _buildGroupedQuestionsList
}
