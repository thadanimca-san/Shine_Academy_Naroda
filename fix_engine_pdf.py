import re

path = 'lib/features/learning/learning_engine/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace PdfGoogleFonts with local fonts
new_fonts = '''
    final baseData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final fontBase = pw.Font.ttf(baseData);
    final boldData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    final fontBold = pw.Font.ttf(boldData);
    
    final gujData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujFont = pw.Font.ttf(gujData);
    final hinData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hinFont = pw.Font.ttf(hinData);

    final fontTheme = pw.ThemeData.withFont(
      base: fontBase, 
      bold: fontBold,
      fontFallback: [gujFont, hinFont]
    );
'''

# Find instances of:
# final fontBase = await PdfGoogleFonts.notoSansRegular();
# final fontBold = await PdfGoogleFonts.notoSansBold();
# final fontTheme = pw.ThemeData.withFont(base: fontBase, bold: fontBold);

pattern = r'    final fontBase = await PdfGoogleFonts\.notoSansRegular\(\);\n\s*final fontBold = await PdfGoogleFonts\.notoSansBold\(\);\n\s*final fontTheme = pw\.ThemeData\.withFont\(base: fontBase, bold: fontBold\);'
content = re.sub(pattern, new_fonts.strip(), content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed fonts in learning_engine pdf service")
