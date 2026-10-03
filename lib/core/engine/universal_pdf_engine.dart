import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:screenshot/screenshot.dart';
import '../../../core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class UniversalPdfEngine {
  /// Generates a PDF by rendering arbitrary Flutter widgets to images.
  /// This ensures 100% accurate rendering of Gujarati matras, complex text layout, and LaTeX/Math symbols.
  static Future<Uint8List> generatePdfBytesFromWidgets({
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    final pdf = pw.Document();
    final ScreenshotController screenshotController = ScreenshotController();

    List<Uint8List> capturedImages = [];

    // Capture each widget off-screen
    for (var widget in widgets) {
      final img = await screenshotController.captureFromWidget(
        _wrapInTheme(widget),
        delay: const Duration(milliseconds: 300), // Give flutter_math_fork's KaTeX fonts time to load
      );
      capturedImages.add(img);
    }

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        header: (pw.Context context) => _buildBasicHeader(title, isAnswerKey),
        build: (pw.Context context) {
          return capturedImages.map<pw.Widget>((imgBytes) {
            return pw.Padding(
              padding: const pw.EdgeInsets.only(bottom: 12),
              child: pw.Image(pw.MemoryImage(imgBytes)),
            );
          }).toList();
        },
      ),
    );

    return await pdf.save();
  }

  static Future<void> generatePdfFromWidgets({
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    final bytes = await generatePdfBytesFromWidgets(title: title, widgets: widgets, isAnswerKey: isAnswerKey);
    final dir = await getTemporaryDirectory();
    final prefix = isAnswerKey ? 'Answer_Key_' : 'Question_Paper_';
    final safeTitle = title.replaceAll(RegExp(r'[^a-zA-Z0-9_\-]'), '_');
    final file = File('${dir.path}/$prefix$safeTitle.pdf');
    await file.writeAsBytes(bytes);
    await OpenFilex.open(file.path);
  }

  static Widget _wrapInTheme(Widget child) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'NotoSansGujarati', // Fixes off-screen rendering of matras
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
      ),
      home: Scaffold(
        backgroundColor: Colors.white,
        body: Container(
          width: 800, // Fixed width to ensure it scales nicely in A4 PDF
          color: Colors.white,
          padding: const EdgeInsets.symmetric(vertical: 4),
          child: child,
        ),
      ),
    );
  }

  static pw.Widget _buildBasicHeader(String title, bool isAnswerKey) {
    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.center,
      children: [
        pw.Text(
          title,
          style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold),
        ),
        pw.SizedBox(height: 4),
        pw.Text(
          isAnswerKey ? 'Answer Key' : 'Question Paper',
          style: pw.TextStyle(fontSize: 14, fontWeight: pw.FontWeight.bold, color: isAnswerKey ? PdfColors.green800 : PdfColors.blue800),
        ),
        pw.SizedBox(height: 12),
        pw.Divider(thickness: 1.5),
        pw.SizedBox(height: 12),
      ],
    );
  }
}
