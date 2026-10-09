import re
import glob

files = glob.glob('lib/features/**/*.dart', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # PdfGeneratorService.generateAndOpenQuestionPaper(selectedChapters)
    # -> PdfGeneratorService.generateAndOpenQuestionPaper(context, selectedChapters)
    new_content = re.sub(r'PdfGeneratorService\.generateAndOpenQuestionPaper\(\s*selectedChapters\s*,?\s*\)', r'PdfGeneratorService.generateAndOpenQuestionPaper(context, selectedChapters)', content)
    if new_content != content:
        content = new_content
        modified = True

    new_content = re.sub(r'PdfGeneratorService\.generateAndOpenAnswerKey\(\s*selectedChapters\s*,?\s*\)', r'PdfGeneratorService.generateAndOpenAnswerKey(context, selectedChapters)', content)
    if new_content != content:
        content = new_content
        modified = True

    new_content = re.sub(r'_generate\(PdfGeneratorService\.generateQuestionPaperPDF\)', r'_generate((ch, [_]) => PdfGeneratorService.generateQuestionPaperPDF(context, ch))', content)
    if new_content != content:
        content = new_content
        modified = True

    new_content = re.sub(r'_generate\(PdfGeneratorService\.generateAnswerKeyPDF\)', r'_generate((ch, [_]) => PdfGeneratorService.generateAnswerKeyPDF(context, ch))', content)
    if new_content != content:
        content = new_content
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {file}")

