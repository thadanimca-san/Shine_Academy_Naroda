import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:screenshot/screenshot.dart';

class UniversalPdfEngine {
  /// Whether we have already loaded fonts into dart:ui's global registry.
  /// The screenshot package creates an isolated render tree (new PipelineOwner /
  /// BuildOwner) that does NOT have access to the fonts declared in pubspec.yaml
  /// (those are loaded into the main engine only).  We must explicitly push the
  /// Gujarati + Devanagari fonts through dart:ui's FontLoader so that they end
  /// up in the GLOBAL registry, which IS shared with every render tree.
  static bool _fontsRegistered = false;

  /// Register fonts into dart:ui's global registry so the off-screen render
  /// tree created by the screenshot package can use them for proper shaping.
  static Future<void> _ensureFontsRegistered() async {
    if (_fontsRegistered) return;
    _fontsRegistered = true;

    // NotoSansGujarati – handles all Gujarati characters and matras correctly
    final gujaratiLoader = FontLoader('NotoSansGujarati');
    gujaratiLoader.addFont(rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf'));
    await gujaratiLoader.load();

    final gujaratiBoldLoader = FontLoader('NotoSansGujarati');
    gujaratiBoldLoader.addFont(rootBundle.load('assets/fonts/NotoSansGujarati-Bold.ttf'));
    await gujaratiBoldLoader.load();

    // NotoSansDevanagari – handles Hindi text
    final hindiLoader = FontLoader('NotoSansDevanagari');
    hindiLoader.addFont(rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf'));
    await hindiLoader.load();
  }

  /// Generates a PDF by rendering Flutter widgets to PNG images then embedding
  /// them in a PDF.  This approach gives 100% accurate Gujarati matra rendering,
  /// correct LaTeX/Math symbol display, and proper Hindi text — things that the
  /// `pdf` package alone cannot provide because it bypasses Flutter's HarfBuzz
  /// shaping engine.
  static Future<Uint8List> generatePdfBytesFromWidgets({
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    // CRITICAL: load fonts into the global dart:ui registry BEFORE any capture.
    await _ensureFontsRegistered();

    final pdf = pw.Document();
    final screenshotController = ScreenshotController();

    // Combine ALL widgets into a single Column and capture ONCE.
    // This reduces JNI calls from N (one per block) to 1.
    final combinedWidget = Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: widgets,
    );

    final img = await screenshotController.captureFromWidget(
      _wrapInTheme(combinedWidget),
      delay: const Duration(milliseconds: 500),
      pixelRatio: 2.0,
    );
    final capturedImages = [img];

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
        build: (pw.Context ctx) {
          return capturedImages.map<pw.Widget>((imgBytes) {
            return pw.Padding(
              padding: const pw.EdgeInsets.only(bottom: 12),
              child: pw.Image(pw.MemoryImage(imgBytes)),
            );
          }).toList();
        },
      ),
    );

    return pdf.save();
  }

  static Future<void> generatePdfFromWidgets({
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    final bytes = await generatePdfBytesFromWidgets(
      title: title,
      widgets: widgets,
      isAnswerKey: isAnswerKey,
    );
    final dir = await getTemporaryDirectory();
    final prefix = isAnswerKey ? 'Answer_Key_' : 'Question_Paper_';
    final safeTitle = title.replaceAll(RegExp(r'[^a-zA-Z0-9_\-]'), '_');
    final file = File('${dir.path}/$prefix$safeTitle.pdf');
    await file.writeAsBytes(bytes);
    await OpenFilex.open(file.path);
  }

  /// Wraps the widget in a full Material app context.
  /// The fontFamily here ensures every Text widget inside the subtree inherits
  /// NotoSansGujarati as the default font.  Combined with the global FontLoader
  /// registration above, this guarantees proper Gujarati shaping.
  static Widget _wrapInTheme(Widget child) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'NotoSansGujarati',
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
      ),
      home: Scaffold(
        backgroundColor: Colors.white,
        body: Container(
          width: 794, // A4 width in pixels at 96 DPI
          color: Colors.white,
          padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
          child: child,
        ),
      ),
    );
  }

  // ── PDF header (rendered by the `pdf` package, not Flutter) ─────────────
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
          style: pw.TextStyle(
            fontSize: 14,
            fontWeight: pw.FontWeight.bold,
            color: isAnswerKey ? PdfColors.green800 : PdfColors.blue800,
          ),
        ),
        pw.SizedBox(height: 12),
        pw.Divider(thickness: 1.5),
        pw.SizedBox(height: 12),
      ],
    );
  }
}
