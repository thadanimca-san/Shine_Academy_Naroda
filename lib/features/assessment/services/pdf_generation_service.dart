import 'package:flutter/services.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PdfGenerationService {
  Future<pw.ImageProvider> _getLogoImage() async {
    final ByteData bytes = await rootBundle.load('assets/shineacademynarodalogo.jpg');
    final Uint8List byteList = bytes.buffer.asUint8List();
    return pw.MemoryImage(byteList);
  }

  Future<void> generateQuestionPaperPDF(String title, List<dynamic> questions) async {
    final pdf = pw.Document();
    final pageTheme = await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4);
    final logoImage = await _getLogoImage();

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        header: (pw.Context context) {
          return pw.Column(
            children: [
              pw.Row(
                mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                children: [
                  pw.Image(logoImage, height: 50),
                  pw.Text(TrilingualService.instance.getUIText('Shine Academy Naroda'), style: pw.TextStyle(fontSize: 24, fontWeight: pw.FontWeight.bold, color: PdfColors.teal800)),
                ],
              ),
              pw.SizedBox(height: 10),
              pw.Divider(),
              pw.SizedBox(height: 10),
              pw.Center(
                child: pw.Text(title, style: pw.TextStyle(fontSize: 20, fontWeight: pw.FontWeight.bold)),
              ),
              pw.SizedBox(height: 20),
            ],
          );
        },
        build: (pw.Context context) {
          return [
            ...questions.map((q) {
              return pw.Container(
                margin: const pw.EdgeInsets.only(bottom: 20),
                child: pw.Row(
                  crossAxisAlignment: pw.CrossAxisAlignment.start,
                  children: [
                    pw.Text('Q${q['q_no']}. ', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
                    pw.Expanded(
                      child: pw.Text(q['question'], style: const pw.TextStyle(fontSize: 14)),
                    ),
                    pw.SizedBox(width: 10),
                    pw.Text('[${q['marks']}]', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
                  ],
                ),
              );
            }),
          ];
        },
      ),
    );

    await Printing.layoutPdf(
      onLayout: (PdfPageFormat format) async => pdf.save(),
      name: 'Question_Paper_${title.replaceAll(' ', '_')}.pdf',
    );
  }

  Future<void> generateSolutionsPDF(String title, List<dynamic> questions) async {
    final pdf = pw.Document();
    final pageTheme = await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4);
    final logoImage = await _getLogoImage();

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        header: (pw.Context context) {
          return pw.Column(
            children: [
              pw.Row(
                mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                children: [
                  pw.Image(logoImage, height: 50),
                  pw.Text(TrilingualService.instance.getUIText('Shine Academy Naroda'), style: pw.TextStyle(fontSize: 24, fontWeight: pw.FontWeight.bold, color: PdfColors.teal800)),
                ],
              ),
              pw.SizedBox(height: 10),
              pw.Divider(),
              pw.SizedBox(height: 10),
              pw.Center(
                child: pw.Text('$title (Solutions)', style: pw.TextStyle(fontSize: 20, fontWeight: pw.FontWeight.bold)),
              ),
              pw.SizedBox(height: 20),
            ],
          );
        },
        build: (pw.Context context) {
          return [
            ...questions.map((q) {
              return pw.Container(
                margin: const pw.EdgeInsets.only(bottom: 20),
                child: pw.Column(
                  crossAxisAlignment: pw.CrossAxisAlignment.start,
                  children: [
                    pw.Row(
                      crossAxisAlignment: pw.CrossAxisAlignment.start,
                      children: [
                        pw.Text('Q${q['q_no']}. ', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
                        pw.Expanded(
                          child: pw.Text(q['question'], style: const pw.TextStyle(fontSize: 14)),
                        ),
                        pw.SizedBox(width: 10),
                        pw.Text('[${q['marks']}]', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
                      ],
                    ),
                    pw.SizedBox(height: 10),
                    pw.Container(
                      padding: const pw.EdgeInsets.all(10),
                      decoration: pw.BoxDecoration(
                        color: PdfColors.grey100,
                        border: pw.Border.all(color: PdfColors.grey300),
                        borderRadius: const pw.BorderRadius.all(pw.Radius.circular(5)),
                      ),
                      child: pw.Text('Answer: \n${q['solution']}', style: const pw.TextStyle(fontSize: 12)),
                    ),
                  ],
                ),
              );
            }),
          ];
        },
      ),
    );

    await Printing.layoutPdf(
      onLayout: (PdfPageFormat format) async => pdf.save(),
      name: 'Solutions_${title.replaceAll(' ', '_')}.pdf',
    );
  }
}
