import re

path = 'lib/features/learning/learning_engine/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Fix ValueListenableBuilder and the dialog Column/Text/TextStyle
code = code.replace("ValueListenableBuilder<int>(", "ValueListenableBuilder<int>(")
# Actually, I'll just add them to the `show` list of flutter/material.dart!
code = code.replace("show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator, debugPrint;", "show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator, debugPrint, ValueListenableBuilder, Column, TextStyle, Colors, TextAlign;")

# TtsInteractiveText on 285
code = re.sub(r"TtsInteractiveText\(text:\s*([^,]+),\s*style:", r"pw.Text(\1, style:", code)
code = re.sub(r"TtsInteractiveText\(text:\s*([^,]+)\)", r"pw.Text(\1)", code)
code = code.replace("Expanded(child: TtsInteractiveText", "pw.Expanded(child: pw.Text")

# Fix Text/TextStyle in dialog to explicitly not be pw.
dialog_code = """
                  return Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      const CircularProgressIndicator(),
                      const SizedBox(height: 16),
                      Text('${getUIText('Processing component')} $currentBlock'),
                      const SizedBox(height: 8),
                      Text(getUIText('Please wait. High quality rendering takes time...'),
                        style: const TextStyle(fontSize: 12, color: Colors.grey),
                        textAlign: TextAlign.center,
                      ),
                    ],
                  );
"""
# Replace the pw. messed up dialog code
messy_dialog = """
                  return pw.Column(
                    mainAxisSize: pw.MainAxisSize.min,
                    children: [
                      const CircularProgressIndicator(),
                      const pw.SizedBox(height: 16),
                      Text('${getUIText('Processing component')} $currentBlock'),
                      const pw.SizedBox(height: 8),
                      Text(getUIText('Please wait. High quality rendering takes time...'),
                        style: const pw.TextStyle(fontSize: 12, color: Colors.grey),
                        textAlign: TextAlign.center,
                      ),
                    ],
                  );
"""
code = code.replace(messy_dialog.strip(), dialog_code.strip())

# Fix pw.Image height/fit issue
code = code.replace("pw.Image(pw.MemoryImage(imageBytes), height: 200, fit: pw.BoxFit.contain)", "pw.Container(height: 200, child: pw.Image(pw.MemoryImage(imageBytes), fit: pw.BoxFit.contain))")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Third pass complete")
