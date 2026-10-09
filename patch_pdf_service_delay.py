import os
import glob

files = glob.glob('lib/features/**/services/pdf_generator_service.dart', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'await Future.delayed(const Duration(milliseconds: 200));' not in content:
        content = content.replace(
            'await UniversalPdfEngine.generatePdfFromWidgets(',
            'await Future.delayed(const Duration(milliseconds: 200));\n      await UniversalPdfEngine.generatePdfFromWidgets('
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Added delay to allow dialog to render")
