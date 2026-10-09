import re

path = 'lib/core/services/pdf_generator_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_theme = '''
    final baseData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final fontBase = pw.Font.ttf(baseData);
    final boldData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    final fontBold = pw.Font.ttf(boldData);
    
    final gujData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujFont = pw.Font.ttf(gujData);
    final hinData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hinFont = pw.Font.ttf(hinData);

    final pdf = pw.Document(
      title: '$title - Shine Academy',
      author: 'Shine Academy Naroda',
      theme: pw.ThemeData.withFont(
        base: fontBase, 
        bold: fontBold,
        fontFallback: [gujFont, hinFont]
      ),
    );
'''

pattern = r"    final pdf = pw\.Document\(\n      title: '\$title - Shine Academy',\n      author: 'Shine Academy Naroda',\n    \);"
content = re.sub(pattern, new_theme.strip(), content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed fonts in core pdf generator")
