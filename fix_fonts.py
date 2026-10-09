import re

file_path = 'lib/core/engine/universal_pdf_engine.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_font_loader = '''
    // Base font for standard English
    final englishData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final baseTtf = pw.Font.ttf(englishData);

    // Fallback font for Gujarati
    final gujaratiData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujTtf = pw.Font.ttf(gujaratiData);
    
    // Fallback font for Hindi
    final hindiData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hindiTtf = pw.Font.ttf(hindiData);

    final pdf = pw.Document(
      theme: pw.ThemeData.withFont(
        base: baseTtf,
        fontFallback: [gujTtf, hindiTtf],
      ),
    );
'''

# Find the old font loader section and replace it
# The old one was:
#     final gujaratiData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
#     final ttf = pw.Font.ttf(gujaratiData);
#     
#     // Fallback font for Hindi
#     final hindiData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
#     final fallbackTtf = pw.Font.ttf(hindiData);
# 
#     final pdf = pw.Document(
#       theme: pw.ThemeData.withFont(
#         base: ttf,
#         fontFallback: [fallbackTtf],
#       ),
#     );

content = re.sub(r'    final gujaratiData =.*?\}\),\n    \);', new_font_loader.strip(), content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed UniversalPdfEngine fonts")
