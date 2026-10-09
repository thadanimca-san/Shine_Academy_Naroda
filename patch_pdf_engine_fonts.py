import os

engine_file = 'lib/core/engine/universal_pdf_engine.dart'
with open(engine_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_method = '''
  static Future<void> generateNativePdfTextOnly({
    required String title,
    required List<pw.Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    // Load font to support Gujarati and Hindi natively in pdf package
    final gujaratiData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final ttf = pw.Font.ttf(gujaratiData);
    
    // Fallback font for Hindi
    final hindiData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final fallbackTtf = pw.Font.ttf(hindiData);

    final pdf = pw.Document(
      theme: pw.ThemeData.withFont(
        base: ttf,
        fontFallback: [fallbackTtf],
      ),
    );

    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
        build: (pw.Context ctx) {
          return widgets;
        },
      ),
    );

    final bytes = await pdf.save();
    final dir = await getTemporaryDirectory();
    final prefix = isAnswerKey ? 'Answer_Key_' : 'Question_Paper_';
    final safeTitle = title.replaceAll(RegExp(r'[^a-zA-Z0-9_\\-]'), '_');
    final file = File('${dir.path}/$prefix$safeTitle.pdf');
    await file.writeAsBytes(bytes);
    await OpenFilex.open(file.path);
  }
'''

import re
content = re.sub(r'static Future<void> generateNativePdfTextOnly\(\{.*?\n  \}', new_method, content, flags=re.DOTALL)

with open(engine_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated generateNativePdfTextOnly with fonts")
