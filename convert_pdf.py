import re

path = 'lib/features/learning/learning_engine/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update imports
code = re.sub(r"import 'package:flutter/material.dart'.*?;", "import 'package:flutter/material.dart' show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator, debugPrint;\nimport 'package:pdf/pdf.dart';\nimport 'package:pdf/widgets.dart' as pw;", code, count=1)

# 2. Update method signatures
code = code.replace("List<Widget> flutterWidgets = [];", "List<pw.Widget> flutterWidgets = [];")
code = code.replace("static Future<List<Widget>> _buildFlutterWidgets", "static Future<List<pw.Widget>> _buildNativeWidgets")
code = code.replace("flutterWidgets.addAll(await _buildFlutterWidgets(block));", "flutterWidgets.addAll(await _buildNativeWidgets(block));")
code = code.replace("List<Widget> widgets = [];", "List<pw.Widget> widgets = [];")
code = code.replace("return widgets;", "return widgets;")
code = code.replace("static Future<Widget?> _buildFlutterImage", "static Future<pw.Widget?> _buildNativeImage")
code = code.replace("final imageWidget = await _buildFlutterImage(payload);", "final imageWidget = await _buildNativeImage(payload);")
code = code.replace("final defImageWidget = await _buildFlutterImage(payload);", "final defImageWidget = await _buildNativeImage(payload);")

# 3. Replace UniversalPdfEngine call
old_engine_call = """
      final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
        title: title,
        widgets: flutterWidgets,
        isAnswerKey: false,
        onProgress: (current, total) {
           progressNotifier.value = (validBlocks.length) + current;
        }
      );
"""
new_engine_call = """
      await UniversalPdfEngine.generateNativePdfTextOnly(
        title: title,
        widgets: flutterWidgets,
        isAnswerKey: false,
      );
      
      if (dialogCtx != null && dialogCtx!.mounted) {
        Navigator.of(dialogCtx!).pop();
        dialogCtx = null;
      }
      return; // generateNativePdfTextOnly opens the file internally
"""
code = code.replace(old_engine_call.strip(), new_engine_call.strip())

# Remove the old openPdfBytes since generateNativePdfTextOnly opens it
code = re.sub(r"await PdfViewerUtil\.openPdfBytes.*?;\n", "", code)

# 4. Replace widget names with pw.* (Careful not to replace the loading dialog widgets)
code = re.sub(r"(?<!pw\.)Text\('QUESTION'", "pw.Text('QUESTION'", code)
code = re.sub(r"(?<!pw\.)Text\('SOLUTION / ANSWER'", "pw.Text('SOLUTION / ANSWER'", code)
code = re.sub(r"(?<!pw\.)Text\(label", "pw.Text(label", code)
code = re.sub(r"(?<!pw\.)Text\(title", "pw.Text(title", code)
code = re.sub(r"(?<!pw\.)Text\('• '", "pw.Text('• '", code)
code = re.sub(r"(?<!pw\.)Text\(caption", "pw.Text(caption", code)

code = re.sub(r"TtsInteractiveText\(text:\s*([^,]+),\s*style:", r"pw.Text(\1, style:", code)
code = re.sub(r"TtsInteractiveText\(text:\s*([^,]+)\)", r"pw.Text(\1)", code)

# 5. _buildParagraphs
code = code.replace("static List<Widget> _buildParagraphs(String text, {Color? textColor}) {", "static List<pw.Widget> _buildParagraphs(String text, {PdfColor? textColor}) {")
code = code.replace("List<Widget> widgets = [];", "List<pw.Widget> widgets = [];")

# We must replace Color with PdfColor
code = code.replace("Color? textColor", "PdfColor? textColor")
code = code.replace("Colors.grey", "PdfColors.grey")
code = code.replace("Colors.green", "PdfColors.green")
code = code.replace("Colors.black87", "PdfColors.grey900")
code = code.replace("Color(0xFF0D47A1)", "PdfColor.fromInt(0xFF0D47A1)")
code = code.replace("Colors.purple[900]!", "PdfColors.purple900")
code = code.replace("Colors.amber[900]!", "PdfColors.amber900")


# Replace Flutter layout widgets with pw. equivalents inside the switch and helpers
replacements = [
    (r"(?<!pw\.)SizedBox\(", "pw.SizedBox("),
    (r"(?<!pw\.)Padding\(", "pw.Padding("),
    (r"(?<!pw\.)Row\(", "pw.Row("),
    (r"(?<!pw\.)Column\(", "pw.Column("),
    (r"(?<!pw\.)Expanded\(", "pw.Expanded("),
    (r"(?<!pw\.)Center\(", "pw.Center("),
    (r"(?<!pw\.)TextStyle\(", "pw.TextStyle("),
    (r"(?<!pw\.)EdgeInsets\.", "pw.EdgeInsets."),
    (r"(?<!pw\.)FontWeight\.", "pw.FontWeight."),
    (r"(?<!pw\.)CrossAxisAlignment\.", "pw.CrossAxisAlignment."),
    (r"(?<!pw\.)MainAxisSize\.", "pw.MainAxisSize."),
    (r"(?<!pw\.)FontStyle\.", "pw.FontStyle."),
]

# Only apply layout replacements AFTER line 250 (so we don't break the loading dialog which uses real Flutter widgets)
lines = code.split('\n')
for i in range(200, len(lines)):
    for old, new in replacements:
        lines[i] = re.sub(old, new, lines[i])
        
code = '\n'.join(lines)

# Fix Image.memory
code = code.replace("pw.Image.memory(imageBytes, height: 200, fit: BoxFit.contain)", "pw.Image(pw.MemoryImage(imageBytes), height: 200, fit: pw.BoxFit.contain)")

# Fix SVG
code = code.replace("import 'package:flutter_svg/flutter_svg.dart';", "")
code = code.replace("import 'package:flutter_html/flutter_html.dart';", "")

code = code.replace("SvgPicture.string(", "pw.SvgImage(svg: ")
code = code.replace("height: 200,", "height: 200,")
code = code.replace("return pw.Center(child: pw.SvgImage(svg: svgString, height: 200));", "return [pw.Center(child: pw.SvgImage(svg: svgString, height: 200)), pw.SizedBox(height: 16)];")

# Wait, SVG block returns List<Widget> not Widget, so we need to wrap it. 
# It already says `return [pw.Center(child: pw.SvgPicture.string(...))]` ?
# Let's write the result back.
with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Conversion complete")
