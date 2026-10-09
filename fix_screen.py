path = 'lib/features/assessment/question_paper_screen.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('_pdfService.generateQuestionPaperPDF(title, questions);', '_pdfService.generateQuestionPaperPDF(context, title, questions);')
content = content.replace('_pdfService.generateSolutionsPDF(title, questions);', '_pdfService.generateSolutionsPDF(context, title, questions);')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed question_paper_screen")
