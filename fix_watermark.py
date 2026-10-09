import re

path = 'lib/core/engine/universal_pdf_engine.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. generatePdfBytesFromWidgets
old_add_page_1 = """
    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
"""
new_add_page_1 = """
    final ByteData logoData = await rootBundle.load('assets/branding/logo.jpg');
    final Uint8List logoBytes = logoData.buffer.asUint8List();
    
    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        pageTheme: pw.PageTheme(
          buildBackground: (pw.Context context) {
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoBytes), width: 300),
              ),
            );
          },
        ),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
"""
code = code.replace(old_add_page_1.strip(), new_add_page_1.strip())

# 2. generateNativePdfTextOnly
old_add_page_2 = """
    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
"""
new_add_page_2 = """
    final ByteData logoData = await rootBundle.load('assets/branding/logo.jpg');
    final Uint8List logoBytes = logoData.buffer.asUint8List();
    
    pdf.addPage(
      pw.MultiPage(
        pageFormat: PdfPageFormat.a4,
        margin: const pw.EdgeInsets.all(32),
        pageTheme: pw.PageTheme(
          buildBackground: (pw.Context context) {
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoBytes), width: 300),
              ),
            );
          },
        ),
        header: (pw.Context ctx) => _buildBasicHeader(title, isAnswerKey),
"""
# Need to use replace carefully because they look identical
code = code.replace(old_add_page_2.strip(), new_add_page_2.strip())

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Watermark injected")
