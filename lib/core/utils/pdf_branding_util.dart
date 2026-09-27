import 'dart:typed_data';
import 'package:flutter/services.dart' show rootBundle;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;

class PdfBrandingUtil {
  PdfBrandingUtil._();

  /// Loads the Shine Academy logo and returns a PageTheme with it set as a watermark.
  /// Pass in the default pageFormat you are using.
  static Future<pw.PageTheme> getPageTheme({
    PdfPageFormat pageFormat = PdfPageFormat.a4,
    pw.ThemeData? theme,
    String? studentName,
  }) async {
    // Load the logo bytes from the assets directory
    final ByteData bytes = await rootBundle.load('assets/shineacademynarodalogo.jpg');
    final pw.MemoryImage watermarkImage = pw.MemoryImage(bytes.buffer.asUint8List());

    // Load fonts for Hindi, Gujarati, and Math symbols
    final gujaratiFontData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final hindiFontData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final mathFontData = await rootBundle.load('assets/fonts/NotoSansMath-Regular.ttf');
    final dejavuFontData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final dejavuFontBoldData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    
    final gujaratiFont = pw.Font.ttf(gujaratiFontData);
    final hindiFont = pw.Font.ttf(hindiFontData);
    final mathFont = pw.Font.ttf(mathFontData);
    final dejavuFont = pw.Font.ttf(dejavuFontData);
    final dejavuFontBold = pw.Font.ttf(dejavuFontBoldData);

    final finalTheme = theme ?? pw.ThemeData.withFont(
      base: dejavuFont,
      bold: dejavuFontBold,
      italic: pw.Font.helveticaOblique(),
      boldItalic: pw.Font.helveticaBoldOblique(),
    );

    // Apply fallbacks
    final themedWithFallback = finalTheme.copyWith(
      defaultTextStyle: finalTheme.defaultTextStyle.copyWith(
        fontFallback: [mathFont, gujaratiFont, hindiFont],
      ),
    );

    return pw.PageTheme(
      pageFormat: pageFormat,
      theme: themedWithFallback,
      margin: const pw.EdgeInsets.fromLTRB(32, 32, 32, 44),
      buildBackground: (pw.Context context) {
        final watermarkText = studentName != null && studentName.isNotEmpty
            ? "SHINE ACADEMY NARODA - CONFIDENTIAL - FOR $studentName ONLY"
            : "SHINE ACADEMY NARODA - CONFIDENTIAL STUDY MATERIAL";

        return pw.FullPage(
          ignoreMargins: true,
          child: pw.Stack(
            children: [
              // 1. Center faint Logo
              pw.Center(
                child: pw.Opacity(
                  opacity: 0.15,
                  child: pw.SizedBox(
                    width: 200,
                    child: pw.Image(watermarkImage, fit: pw.BoxFit.contain),
                  ),
                ),
              ),
              // 2. Aggressive Diagonal Text Watermark overlaying the whole page
              pw.Opacity(
                opacity: 0.08,
                child: pw.Watermark(
                  child: pw.Transform.rotateBox(
                    angle: 0.785398, // roughly 45 degrees
                    child: pw.Column(
                      mainAxisAlignment: pw.MainAxisAlignment.center,
                      children: List.generate(
                        10,
                        (index) => pw.Padding(
                          padding: const pw.EdgeInsets.symmetric(vertical: 40),
                          child: pw.Text(
                            watermarkText.toUpperCase(),
                            style: pw.TextStyle(
                              fontSize: 24,
                              fontWeight: pw.FontWeight.bold,
                              color: PdfColors.grey700,
                            ),
                            textAlign: pw.TextAlign.center,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
              // 3. Footer Legal Text
              pw.Positioned(
                bottom: 10,
                left: 0,
                right: 0,
                child: pw.Center(
                  child: pw.Text(
                    "Strictly for personal use. Unauthorized reproduction or commercial use is prohibited. Property of Shine Academy Naroda.",
                    style: pw.TextStyle(fontSize: 8, color: PdfColors.grey500),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
