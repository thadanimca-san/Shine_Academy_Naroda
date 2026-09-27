import os
import re

files_to_update = [
    'lib/core/services/pdf_generator_service.dart',
    'lib/features/english_simulation_11to12/services/pdf_generator_service.dart',
    'lib/features/assessment/services/pdf_generation_service.dart',
    'lib/features/learning/learning_engine/services/pdf_export_service.dart',
    'lib/features/learning/school/sci_simulation/services/pdf_generator_service.dart',
    'lib/features/learning/school/english/services/pdf_generator_service.dart',
    'lib/features/learning/school/maths_simulation/services/pdf_generator_service.dart',
    'lib/features/learning/higher_secondary/english_simulation/services/pdf_generator_service.dart'
]

pattern1 = re.compile(r'await Printing\.layoutPdf\(\s*onLayout: \(PdfPageFormat format\) async => (.*?),\s*name:\s*(.*?)\s*\);', re.DOTALL)
pattern2 = re.compile(r'await Printing\.layoutPdf\(\s*onLayout:\s*\(_\)\s*=>\s*(.*?)\.save\(\)\s*\);', re.DOTALL)

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = content
    
    # 1. Add import if not present
    if "import 'package:shine_academy_naroda/core/utils/pdf_viewer_util.dart';" not in new_content:
        new_content = "import 'package:shine_academy_naroda/core/utils/pdf_viewer_util.dart';\n" + new_content

    # 2. Replace Printing.layoutPdf where onLayout returns bytes or pdf.save()
    
    def repl1(m):
        bytes_val = m.group(1)
        if bytes_val == "pdf.save()":
            bytes_val = "await pdf.save()"
        filename = m.group(2)
        return f"await PdfViewerUtil.openPdfBytes({bytes_val}, {filename});"
        
    new_content = pattern1.sub(repl1, new_content)
    
    def repl2(m):
        pdf_var = m.group(1)
        return f"await PdfViewerUtil.openPdfBytes(await {pdf_var}.save(), 'Document.pdf');"
        
    new_content = pattern2.sub(repl2, new_content)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
