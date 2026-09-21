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
      buildBackground: (pw.Context context) {
        return pw.FullPage(
          ignoreMargins: true,
          child: pw.Center(
            child: pw.Opacity(
              opacity: 0.15, // Light opacity for a watermark
              child: pw.SizedBox(
                width: 200, // Visiting card size
                child: pw.Image(watermarkImage, fit: pw.BoxFit.contain),
              ),
            ),
          ),
        );
      },
    );
  }
}
