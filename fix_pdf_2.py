import re

path = 'lib/features/learning/learning_engine/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("PdfPdfColor", "PdfColor")
code = code.replace("PdfPdfColors", "PdfColors")
code = code.replace("getUIpw.Text", "getUIText")
code = code.replace("pw.Image(", "pw.Image(") # this doesn't do much, wait, line 396: Undefined name 'Image'

# Remove const before pw.
for w in ['EdgeInsets', 'SizedBox', 'Padding', 'Text', 'Row', 'Column', 'TextStyle', 'Center', 'Expanded']:
    code = code.replace(f"const pw.{w}", f"pw.{w}")
    code = code.replace(f"const {w}", f"pw.{w}")

code = code.replace("MainAxisSize", "pw.MainAxisSize")
code = code.replace("BoxFit", "pw.BoxFit")
code = code.replace("pw.pw.", "pw.")

# line 178 Undefined method 'Column'
# Let's fix Image.memory just in case it didn't get caught
code = code.replace(" Image.memory(", " pw.Image(pw.MemoryImage(")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Second pass complete")
