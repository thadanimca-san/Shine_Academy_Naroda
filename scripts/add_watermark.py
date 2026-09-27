import os
import re
import glob

# Find all PDF service files
files = glob.glob('/home/ubuntu/Shine_Academy_Naroda/lib/**/*pdf*service*.dart', recursive=True)

for file_path in files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    if 'pdf_branding_util.dart' not in content:
        # Add import
        content = content.replace("import 'package:pdf/widgets.dart' as pw;", "import 'package:pdf/widgets.dart' as pw;\nimport 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';")
        
    # Replace pw.MultiPage( with the pageTheme injection
    content = content.replace("pw.MultiPage(", "pw.MultiPage(\n        pageTheme: await PdfBrandingUtil.getPageTheme(PdfPageFormat.a4),")
    
    # Remove existing pageFormat to prevent conflicts
    content = re.sub(r'^\s*pageFormat:\s*PdfPageFormat\.[a-zA-Z0-9_]+,\n', '', content, flags=re.MULTILINE)
    
    with open(file_path, 'w') as f:
        f.write(content)

print(f"Updated {len(files)} files.")
