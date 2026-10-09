import re

path = 'lib/core/engine/universal_pdf_engine.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the unsafe logo loading in generatePdfBytesFromWidgets
unsafe_load_1 = """
    final ByteData logoData = await rootBundle.load('assets/branding/logo.jpg');
    final Uint8List logoBytes = logoData.buffer.asUint8List();
"""
safe_load = """
    ByteData? logoData;
    try {
      logoData = await rootBundle.load('assets/branding/logo.jpg');
    } catch (e) {
      debugPrint("Watermark Warning: $e");
    }
"""
code = code.replace(unsafe_load_1.strip(), safe_load.strip(), 2) # replace both occurrences

# Replace the unsafe buildBackground
unsafe_bg = """
          buildBackground: (pw.Context context) {
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoBytes), width: 300),
              ),
            );
          },
"""
safe_bg = """
          buildBackground: (pw.Context context) {
            if (logoData == null) return pw.SizedBox();
            return pw.Center(
              child: pw.Opacity(
                opacity: 0.15,
                child: pw.Image(pw.MemoryImage(logoData.buffer.asUint8List()), width: 300),
              ),
            );
          },
"""
code = code.replace(unsafe_bg.strip(), safe_bg.strip(), 2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Safe watermark injected")
