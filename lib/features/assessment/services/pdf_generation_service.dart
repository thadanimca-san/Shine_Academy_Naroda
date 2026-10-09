import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:flutter/material.dart' show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator;
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';


class PdfGenerationService {

  Future<void> generateQuestionPaperPDF(BuildContext context, String title, List<dynamic> questions) async {
    List<pw.Widget> widgets = [];
    
    widgets.add(
      pw.Center(
        child: pw.Text(
          title,
          style: pw.TextStyle(fontSize: 20, fontWeight: pw.FontWeight.bold),
        ),
      ),
    );
    widgets.add(pw.SizedBox(height: 20));

    for (final q in questions) {
      widgets.add(
        pw.Padding(
          padding: const pw.EdgeInsets.only(bottom: 20),
          child: pw.Row(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Text('Q${q['q_no']}. ', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
              pw.Expanded(
                child: pw.Text(q['question'].toString().replaceAll(RegExp(r'\$'), ''), style: const pw.TextStyle(fontSize: 14)),
              ),
              pw.SizedBox(width: 10),
              pw.Text('[${q['marks']}]', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
            ],
          ),
        ),
      );
    }

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

  Future<void> generateSolutionsPDF(BuildContext context, String title, List<dynamic> questions) async {
    List<pw.Widget> widgets = [];

    widgets.add(
      pw.Center(
        child: pw.Text(
          '$title (Solutions)',
          style: pw.TextStyle(fontSize: 20, fontWeight: pw.FontWeight.bold),
        ),
      ),
    );
    widgets.add(pw.SizedBox(height: 20));

    for (final q in questions) {
      widgets.add(
        pw.Padding(
          padding: const pw.EdgeInsets.only(bottom: 20),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Row(
                crossAxisAlignment: pw.CrossAxisAlignment.start,
                children: [
                  pw.Text('Q${q['q_no']}. ', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 14)),
                  pw.Expanded(
                    child: pw.Text(q['question'].toString().replaceAll(RegExp(r'\$'), ''), style: const pw.TextStyle(fontSize: 14)),
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
                child: pw.Text('Answer:\n${q['solution'].toString().replaceAll(RegExp(r'\$'), '')}', style: const pw.TextStyle(fontSize: 12)),
              ),
            ],
          ),
        ),
      );
    }

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
  
  void _showProgress(BuildContext context, String message) {
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

