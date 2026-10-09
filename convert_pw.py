import os
import re

files_to_convert = [
    "lib/core/services/pdf_generator_service.dart",
    "lib/features/assessment/services/pdf_generation_service.dart",
    "lib/features/learning/learning_engine/services/pdf_export_service.dart",
    "lib/features/learning/higher_secondary/commerce_accounts/services/paper_pdf_service.dart",
    "lib/features/learning/higher_secondary/statistics/services/paper_pdf_service.dart"
]

def process_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r') as f:
        content = f.read()

    # If it's already using UniversalPdfEngine, skip
    if "UniversalPdfEngine" in content and "captureFromWidget" not in content:
        # Wait, if it's already using it, we just need to replace pw.
        pass

    # Replace pw. widgets with standard widgets
    content = re.sub(r'\bpw\.Text\b', 'Text', content)
    content = re.sub(r'\bpw\.TextStyle\b', 'TextStyle', content)
    content = re.sub(r'\bpw\.FontWeight\b', 'FontWeight', content)
    content = re.sub(r'\bpw\.Center\b', 'Center', content)
    content = re.sub(r'\bpw\.Column\b', 'Column', content)
    content = re.sub(r'\bpw\.Row\b', 'Row', content)
    content = re.sub(r'\bpw\.SizedBox\b', 'SizedBox', content)
    content = re.sub(r'\bpw\.Expanded\b', 'Expanded', content)
    content = re.sub(r'\bpw\.Padding\b', 'Padding', content)
    content = re.sub(r'\bpw\.EdgeInsets\b', 'EdgeInsets', content)
    content = re.sub(r'\bpw\.Container\b', 'Container', content)
    content = re.sub(r'\bpw\.BoxDecoration\b', 'BoxDecoration', content)
    content = re.sub(r'\bpw\.Border\b', 'Border', content)
    content = re.sub(r'\bpw\.BorderRadius\b', 'BorderRadius', content)
    content = re.sub(r'\bpw\.Radius\b', 'Radius', content)
    content = re.sub(r'\bpw\.Image\b', 'Image.memory', content)
    content = re.sub(r'\bpw\.CrossAxisAlignment\b', 'CrossAxisAlignment', content)
    content = re.sub(r'\bpw\.MainAxisAlignment\b', 'MainAxisAlignment', content)
    content = re.sub(r'\bpw\.Widget\b', 'Widget', content)
    content = re.sub(r'\bpw\.Document\(\)', '', content)
    content = re.sub(r'\bpw\.Divider\b', 'Divider', content)
    content = re.sub(r'\bpw\.TextAlign\b', 'TextAlign', content)
    content = re.sub(r'\bpw\.FontStyle\b', 'FontStyle', content)
    content = re.sub(r'\bpw\.Bullet\b', 'Text', content) # Approximation
    
    # Replace PdfColors with Colors
    content = re.sub(r'PdfColors\.([a-zA-Z0-9_]+)', r'Colors.\1', content)
    
    # We must add UniversalPdfEngine import
    if "UniversalPdfEngine" not in content:
        content = "import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';\n" + content
    
    if "package:flutter/material.dart" not in content:
        content = "import 'package:flutter/material.dart';\n" + content

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Processed {filepath}")

for f in files_to_convert:
    process_file(f)
