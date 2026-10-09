import re

path = 'lib/features/learning/learning_engine/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the messy dialog completely
messy_dialog_start = code.find("                  return Column(")
messy_dialog_end = code.find("                  );", messy_dialog_start) + 20

fixed_dialog = """
                  return Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      const CircularProgressIndicator(),
                      const SizedBox(height: 16),
                      Text('${getUIText('Processing component')} $currentBlock'),
                      const SizedBox(height: 8),
                      Text(getUIText('Please wait. High quality rendering takes time...'),
                        style: const TextStyle(fontSize: 12),
                        textAlign: TextAlign.center,
                      ),
                    ],
                  );
"""
if messy_dialog_start != -1:
    code = code[:messy_dialog_start] + fixed_dialog.strip() + "\n" + code[messy_dialog_end:]

# TtsInteractiveText on line 285
code = re.sub(r"Expanded\(child:\s*TtsInteractiveText\(text:\s*([^,]+),\s*style:", r"pw.Expanded(child: pw.Text(\1, style:", code)
code = re.sub(r"Expanded\(child:\s*TtsInteractiveText\(text:\s*([^,]+)\)\)", r"pw.Expanded(child: pw.Text(\1))", code)
code = code.replace("TtsInteractiveText", "pw.Text") # Any remaining

# TtsInteractiveText was replaced with pw.Text, but the argument type errors at 253, 285, 342 are probably because we have:
# widgets.add(pw.Text(...)) where widgets is List<pw.Widget>. This is valid!
# Wait, "The argument type 'Text' can't be assigned to the parameter type 'Widget?'"
# Ah! It says `Text`, not `pw.Text`! 
# So I need to replace ` Text(` with ` pw.Text(` in the _buildNativeWidgets function
code = re.sub(r"(?<!pw\.)Text\(", r"pw.Text(", code)
# Fix the dialog ones that got messed up
code = code.replace("pw.Text('${getUIText", "Text('${getUIText")
code = code.replace("pw.Text(getUIText('Please", "Text(getUIText('Please")

# Fix image height and fit
code = code.replace("pw.Container(height: 200, child: pw.Image(pw.MemoryImage(imageBytes), fit: pw.BoxFit.contain))", "pw.Container(height: 200, child: pw.Image(pw.MemoryImage(imageBytes), fit: pw.BoxFit.contain))")
# Let's fix line 396
code = re.sub(r"pw\.Image\(pw\.MemoryImage\(imageBytes\),\s*height:\s*200,\s*fit:\s*pw\.BoxFit\.contain\)", r"pw.Container(height: 200, child: pw.Image(pw.MemoryImage(imageBytes), fit: pw.BoxFit.contain))", code)

# Let's replace any `const TextStyle` with `pw.TextStyle`
code = code.replace("const TextStyle(", "pw.TextStyle(")
# Re-fix dialog
code = code.replace("style: pw.TextStyle(fontSize: 12),", "style: const TextStyle(fontSize: 12, color: Colors.grey),")
code = code.replace("const pw.TextStyle(", "pw.TextStyle(")
code = code.replace("const pw.pw.TextStyle", "pw.TextStyle")

# Final check for MainAxisSize in the dialog vs pw.MainAxisSize
code = code.replace("mainAxisSize: pw.MainAxisSize.min", "mainAxisSize: MainAxisSize.min")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Fourth pass complete")
