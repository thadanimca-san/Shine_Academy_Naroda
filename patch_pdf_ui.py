import os
import glob

files = glob.glob('lib/features/**/*.dart', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if 'PdfGeneratorService.generateAndOpenQuestionPaper(' in content and 'context,' not in content:
        content = content.replace(
            'PdfGeneratorService.generateAndOpenQuestionPaper(\n                              selectedChapters,',
            'PdfGeneratorService.generateAndOpenQuestionPaper(\n                              context, selectedChapters,'
        )
        content = content.replace(
            'PdfGeneratorService.generateAndOpenQuestionPaper(selectedChapters',
            'PdfGeneratorService.generateAndOpenQuestionPaper(context, selectedChapters'
        )
        modified = True
        
    if 'PdfGeneratorService.generateAndOpenAnswerKey(' in content and 'context,' not in content:
        content = content.replace(
            'PdfGeneratorService.generateAndOpenAnswerKey(\n                              selectedChapters,',
            'PdfGeneratorService.generateAndOpenAnswerKey(\n                              context, selectedChapters,'
        )
        content = content.replace(
            'PdfGeneratorService.generateAndOpenAnswerKey(selectedChapters',
            'PdfGeneratorService.generateAndOpenAnswerKey(context, selectedChapters'
        )
        modified = True

    if 'PdfGeneratorService.generateQuestionPaperPDF' in content and 'context,' not in content:
        content = content.replace(
            '_generate(PdfGeneratorService.generateQuestionPaperPDF)',
            '_generate((ch, [_]) => PdfGeneratorService.generateQuestionPaperPDF(context, ch))'
        )
        modified = True

    if 'PdfGeneratorService.generateAnswerKeyPDF' in content and 'context,' not in content:
        content = content.replace(
            '_generate(PdfGeneratorService.generateAnswerKeyPDF)',
            '_generate((ch, [_]) => PdfGeneratorService.generateAnswerKeyPDF(context, ch))'
        )
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")

print("Patched UI files")
