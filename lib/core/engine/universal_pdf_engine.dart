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
    void Function(int, int)? onProgress,
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    // CRITICAL: load fonts into the global dart:ui registry BEFORE any capture.
    await _ensureFontsRegistered();

    final pdf = pw.Document();
    final screenshotController = ScreenshotController();

    // Split widgets into chunks to avoid exceeding maximum texture size bounds
    // (a single long Column of 100 blocks easily exceeds 8192 pixels).

    
    final List<Uint8List> capturedImages = [];
    // Increase chunk size to 30 lines. Since widgets are mostly individual lines,
    // 30 lines roughly equates to 1 page. This drastically reduces JNI calls and speeds up generation.
    const int chunkSize = 1; 
    
    for (int i = 0; i < widgets.length; i += chunkSize) {
      if (onProgress != null) {
        onProgress(i, widgets.length);
      }
      int end = (i + chunkSize < widgets.length) ? i + chunkSize : widgets.length;
      final chunk = widgets.sublist(i, end);
      
      final combinedChunk = Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: chunk,
      );

      final img = await screenshotController.captureFromWidget(
        _wrapInTheme(combinedChunk),
        delay: const Duration(milliseconds: 100),
        pixelRatio: 1.2, // Reduce from 2.0 to 1.5 to save memory and prevent OOM
      );
      capturedImages.add(img);
    }
    if (onProgress != null) {
      onProgress(widgets.length, widgets.length);
    }

    ByteData? logoData;
    try {
      logoData = await rootBundle.load('assets/branding/logo.jpg');
    } catch (e) {
      debugPrint("Watermark Warning: $e");
    }
    
    pdf.addPage(
      pw.MultiPage(
        pageTheme: pw.PageTheme(
          pageFormat: PdfPageFormat.a4,
          margin: const pw.EdgeInsets.all(32),
          buildBackground: (pw.Context context) {
            if (logoData == null) return pw.SizedBox();
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoData.buffer.asUint8List()), width: 300),
              ),
            );
          },
        ),
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

  
  /// Generates a PDF natively using the pdf package without screenshot capture.
  /// This is MUCH faster and 100% reliable for text-heavy PDFs.
  
  static Future<void> generateNativePdfTextOnly({
    required String title,
    required List<pw.Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    // Load base font for English/Latin
    final englishData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final baseTtf = pw.Font.ttf(englishData);

    // Fallback font for Gujarati
    final gujaratiData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujFallbackTtf = pw.Font.ttf(gujaratiData);
    
    // Fallback font for Hindi
    final hindiData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hinFallbackTtf = pw.Font.ttf(hindiData);

    // Fallback font for Math Symbols
    final mathData = await rootBundle.load('assets/fonts/NotoSansMath-Regular.ttf');
    final mathFallbackTtf = pw.Font.ttf(mathData);

    final pdf = pw.Document(
      theme: pw.ThemeData.withFont(
        base: baseTtf,
        fontFallback: [mathFallbackTtf, gujFallbackTtf, hinFallbackTtf],
      ),
    );

    ByteData? logoData;
    try {
      logoData = await rootBundle.load('assets/branding/logo.jpg');
    } catch (e) {
      debugPrint("Watermark Warning: $e");
    }
    
    pdf.addPage(
      pw.MultiPage(
        pageTheme: pw.PageTheme(
          pageFormat: PdfPageFormat.a4,
          margin: const pw.EdgeInsets.all(32),
          buildBackground: (pw.Context context) {
            if (logoData == null) return pw.SizedBox();
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoData.buffer.asUint8List()), width: 300),
              ),
            );
          },
        ),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
        build: (pw.Context ctx) {
          return widgets;
        },
      ),
    );

    final bytes = await pdf.save();
    final dir = await getTemporaryDirectory();
    final prefix = isAnswerKey ? 'Answer_Key_' : 'Question_Paper_';
    final safeTitle = title.replaceAll(RegExp(r'[^a-zA-Z0-9_\-]'), '_');
    final file = File('${dir.path}/$prefix$safeTitle.pdf');
    await file.writeAsBytes(bytes);
    await OpenFilex.open(file.path);
  }


  static Future<void> generatePdfFromWidgets({
    required String title,
    required List<Widget> widgets,
    bool isAnswerKey = false,
    void Function(int, int)? onProgress,
  }) async {
    final bytes = await generatePdfBytesFromWidgets(
      title: title,
      widgets: widgets,
      isAnswerKey: isAnswerKey,
      onProgress: onProgress,
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
    return MediaQuery(
      data: const MediaQueryData(size: Size(794, 2000)),
      child: Directionality(
        textDirection: TextDirection.ltr,
        child: Theme(
          data: ThemeData(
            fontFamilyFallback: const ['NotoSansGujarati', 'NotoSansDevanagari'],
            colorSchemeSeed: Colors.indigo,
            useMaterial3: true,
          ),
          child: Material(
            color: Colors.white,
            child: Container(
              width: 794, // A4 width in pixels at 96 DPI
              color: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
              child: child,
            ),
          ),
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
