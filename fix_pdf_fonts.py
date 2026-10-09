import re

path = 'lib/core/engine/universal_pdf_engine.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: _wrapInTheme in generatePdfFromWidgets
old_theme = """
      theme: ThemeData(
        fontFamily: 'NotoSansGujarati',
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
      ),
"""
new_theme = """
      theme: ThemeData(
        fontFamilyFallback: const ['NotoSansGujarati', 'NotoSansDevanagari'],
        colorSchemeSeed: Colors.indigo,
        useMaterial3: true,
      ),
"""
content = content.replace(old_theme.strip(), new_theme.strip())

# Fix 2: generateNativePdfTextOnly
old_native = """
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
"""
new_native = """
    // Load base font for English/Latin
    final englishData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final baseTtf = pw.Font.ttf(englishData);

    // Fallback font for Gujarati
    final gujaratiData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujFallbackTtf = pw.Font.ttf(gujaratiData);
    
    // Fallback font for Hindi
    final hindiData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hinFallbackTtf = pw.Font.ttf(hindiData);

    final pdf = pw.Document(
      theme: pw.ThemeData.withFont(
        base: baseTtf,
        fontFallback: [gujFallbackTtf, hinFallbackTtf],
      ),
    );
"""
content = content.replace(old_native.strip(), new_native.strip())

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed UniversalPdfEngine fonts")
