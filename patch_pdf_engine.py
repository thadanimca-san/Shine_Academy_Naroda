import os

engine_file = 'lib/core/engine/universal_pdf_engine.dart'
with open(engine_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_method = '''
  /// Generates a PDF natively using the pdf package without screenshot capture.
  /// This is MUCH faster and 100% reliable for text-heavy PDFs.
  static Future<void> generateNativePdfTextOnly({
    required String title,
    required List<pw.Widget> widgets,
    bool isAnswerKey = false,
  }) async {
    final pdf = pw.Document();

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

if 'generateNativePdfTextOnly' not in content:
    content = content.replace('static Future<void> generatePdfFromWidgets', new_method + '\n  static Future<void> generatePdfFromWidgets')
    with open(engine_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added generateNativePdfTextOnly to UniversalPdfEngine")
else:
    print("Already added")
