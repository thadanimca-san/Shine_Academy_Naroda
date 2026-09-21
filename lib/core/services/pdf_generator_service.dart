import 'dart:typed_data';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PdfGeneratorService {
  
  static Future<Uint8List> generateBoardPaper({
    required Map<String, dynamic> moduleData,
    required bool includeSolutions,
  }) async {
    final metadata = moduleData['metadata'] ?? {};
    final blocks = (moduleData['content'] ?? moduleData['blocks']) as List? ?? [];
    
    final title = metadata['title'] ?? 'Board Paper';
    final subject = metadata['subject'] ?? 'Subject';
    final totalMarks = metadata['total_marks'] ?? 50;

    final pdf = pw.Document(
      title: '$title - Shine Academy',
      author: 'Shine Academy Naroda',
    );

    // Load watermark image
    final watermarkImageBytes = await rootBundle.load('assets/shineacademynarodalogo.jpg');
    final watermarkImage = pw.MemoryImage(watermarkImageBytes.buffer.asUint8List());

    // Define watermark decoration
    final pageTheme = pw.PageTheme(
      pageFormat: PdfPageFormat.a4,
      margin: const pw.EdgeInsets.all(32),
      buildBackground: (pw.Context context) {
        return pw.FullPage(
          ignoreMargins: false,
          child: pw.Center(
            child: pw.Opacity(
              opacity: 0.15,
              child: pw.SizedBox(
                width: 200, // Visiting card size
                child: pw.Image(watermarkImage, fit: pw.BoxFit.contain),
              ),
            ),
          ),
        );
      },
    );

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        header: (pw.Context context) {
          return pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.center,
            children: [
              pw.Text(TrilingualService.instance.getUIText('SHINE ACADEMY NARODA'), style: pw.TextStyle(fontSize: 24, fontWeight: pw.FontWeight.bold)),
              pw.Text(TrilingualService.instance.getUIText('Board Exam Simulation 2026'), style: pw.TextStyle(fontSize: 16)),
              pw.SizedBox(height: 8),
              pw.Divider(thickness: 2),
              pw.Row(
                mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                children: [
                  pw.Text('Subject: $subject', style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold)),
                  pw.Text('Total Marks: $totalMarks', style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold)),
                ],
              ),
              if (includeSolutions)
                pw.Container(
                  margin: const pw.EdgeInsets.only(top: 4),
                  padding: const pw.EdgeInsets.symmetric(vertical: 4, horizontal: 8),
                  decoration: const pw.BoxDecoration(color: PdfColors.yellow300, borderRadius: pw.BorderRadius.all(pw.Radius.circular(4))),
                  child: pw.Text(TrilingualService.instance.getUIText('SOLUTION & EXAMINER GUIDE'), style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold, color: PdfColors.red900)),
                ),
              pw.Divider(thickness: 2),
              pw.SizedBox(height: 16),
            ]
          );
        },
        footer: (pw.Context context) {
          return pw.Container(
            alignment: pw.Alignment.centerRight,
            margin: const pw.EdgeInsets.only(top: 1.0 * PdfPageFormat.cm),
            child: pw.Text(
              'Page ${context.pageNumber} of ${context.pagesCount}',
              style: pw.Theme.of(context).defaultTextStyle.copyWith(color: PdfColors.grey),
            ),
          );
        },
        build: (pw.Context context) {
          final elements = <pw.Widget>[];
          
          String currentSection = "";

          for (var i = 0; i < blocks.length; i++) {
            final block = blocks[i] as Map<String, dynamic>;
            final section = block['section'] as String?;
            final type = block['type'] as String?;
            final marksVal = block['marks'];
            final question = block['question'] ?? block['body'] ?? block['title'] ?? "";
            
            // Section Headers
            if (section != null && section != currentSection) {
              currentSection = section;
              elements.add(pw.SizedBox(height: 16));
              elements.add(pw.Center(child: pw.Text(currentSection, style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold, decoration: pw.TextDecoration.underline))));
              elements.add(pw.SizedBox(height: 12));
            }

            final qNum = i + 1;
            final marks = marksVal != null ? '[$marksVal Marks]' : '';

            // Question Text
            elements.add(
              pw.Row(
                crossAxisAlignment: pw.CrossAxisAlignment.start,
                children: [
                  pw.Text('Q$qNum. ', style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
                  pw.Expanded(child: pw.Text('$question ')),
                  pw.Text(marks, style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
                ],
              )
            );

            // MCQ Options
            if (type == 'quiz' && block['options'] != null) {
              elements.add(pw.SizedBox(height: 8));
              final letters = ['A', 'B', 'C', 'D'];
              final optionsList = block['options'] as List;
              for (var j = 0; j < optionsList.length; j++) {
                final isCorrect = includeSolutions && (block['correct_index'] == j);
                elements.add(
                  pw.Padding(
                    padding: const pw.EdgeInsets.only(left: 20, bottom: 4),
                    child: pw.Text(
                      '(${letters[j]}) ${optionsList[j]}',
                      style: pw.TextStyle(
                        color: isCorrect ? PdfColors.green800 : PdfColors.black,
                        fontWeight: isCorrect ? pw.FontWeight.bold : pw.FontWeight.normal,
                      )
                    )
                  )
                );
              }
            }
            
            // Solutions
            if (includeSolutions) {
              elements.add(pw.SizedBox(height: 8));
              
              if (block['model_answer'] != null) {
                elements.add(pw.Padding(
                  padding: const pw.EdgeInsets.only(left: 20, bottom: 8),
                  child: pw.Column(
                    crossAxisAlignment: pw.CrossAxisAlignment.start,
                    children: [
                      pw.Text(TrilingualService.instance.getUIText('Model Answer:'), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, color: PdfColors.blue900)),
                      pw.Text(block['model_answer'].toString()),
                    ]
                  )
                ));
              }

              if (block['explanation'] != null) {
                elements.add(pw.Padding(
                  padding: const pw.EdgeInsets.only(left: 20, bottom: 8),
                  child: pw.Column(
                    crossAxisAlignment: pw.CrossAxisAlignment.start,
                    children: [
                      pw.Text(TrilingualService.instance.getUIText('Explanation:'), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, color: PdfColors.blue900)),
                      pw.Text(block['explanation'].toString()),
                    ]
                  )
                ));
              }
              
              if (block['teacher_tip'] != null) {
                elements.add(pw.Padding(
                  padding: const pw.EdgeInsets.only(left: 20, bottom: 8),
                  child: pw.Container(
                    padding: const pw.EdgeInsets.all(8),
                    decoration: pw.BoxDecoration(
                      color: PdfColors.grey100,
                      border: pw.Border.all(color: PdfColors.red900),
                    ),
                    child: pw.Column(
                      crossAxisAlignment: pw.CrossAxisAlignment.start,
                      children: [
                        pw.Text(TrilingualService.instance.getUIText('Examiner Note:'), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, color: PdfColors.red900)),
                        pw.Text(block['teacher_tip'].toString(), style: const pw.TextStyle(color: PdfColors.red900)),
                      ]
                    )
                  )
                ));
              }
            } else if (type != 'quiz') {
               // Leave blank space for student to write if it's not an MCQ paper
               double space = (marksVal is int ? marksVal : 2) * 40.0;
               elements.add(pw.SizedBox(height: space));
            }

            elements.add(pw.SizedBox(height: 12));
          }

          return elements;
        },
      ),
    );

    return await pdf.save();
  }

  static Future<void> downloadPaper(Map<String, dynamic> moduleData, bool includeSolutions) async {
    try {
      final pdfBytes = await generateBoardPaper(
        moduleData: moduleData,
        includeSolutions: includeSolutions,
      );
      
      final suffix = includeSolutions ? 'Solution' : 'Question_Paper';
      final id = moduleData['metadata']?['id'] ?? 'Solved_Paper';
      final filename = '${id}_$suffix.pdf';
      
      await Printing.sharePdf(bytes: pdfBytes, filename: filename);
    } catch (e) {
      debugPrint('Error generating PDF: $e');
    }
  }
}
