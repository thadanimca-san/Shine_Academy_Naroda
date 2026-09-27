import os
import re

files_to_update = [
    'lib/core/services/pdf_generator_service.dart',
    'lib/features/english_simulation_11to12/services/pdf_generator_service.dart',
    'lib/features/learning/learning_engine/services/pdf_export_service.dart',
    'lib/features/learning/school/sci_simulation/services/pdf_generator_service.dart',
    'lib/features/learning/school/english/services/pdf_generator_service.dart',
    'lib/features/learning/school/maths_simulation/services/pdf_generator_service.dart',
    'lib/features/learning/higher_secondary/english_simulation/services/pdf_generator_service.dart'
]

pattern = re.compile(r'Printing\.sharePdf\(\s*bytes:\s*(.*?),\s*filename:\s*(.*?)\s*\)', re.DOTALL)

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace the pattern
    new_content = pattern.sub(r'Printing.layoutPdf(\n      onLayout: (PdfPageFormat format) async => \1,\n      name: \2\n    )', content)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
