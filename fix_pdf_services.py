import os
import glob
import re

files = glob.glob('lib/features/**/services/pdf_generator_service.dart', recursive=True)

new_generate_pdf = '''
  static Future<void> _generatePdf(BuildContext context, List<ChapterModel> chapters, {required bool isAnswerKey}) async {
    final subjectLabel = chapters.isNotEmpty ? '${chapters.first.subject} (Class ${chapters.first.standard})' : 'Assessment';
    
    List<pw.Widget> content = [
      pw.Center(child: pw.Text(
          isAnswerKey ? '$subjectLabel - Answer Key' : '$subjectLabel - Question Paper',
          style: pw.TextStyle(
            fontSize: 20,
            fontWeight: pw.FontWeight.bold,
            color: isAnswerKey ? PdfColors.green800 : PdfColors.blue800,
          ),
        ),
      ),
      pw.SizedBox(height: 10),
      pw.Text(
        isAnswerKey
            ? 'Complete solutions and answer keys corresponding to the assessment questions.'
            : 'Instructions: Fill in the blanks with appropriate scientific terms.',
        style: const pw.TextStyle(fontSize: 12),
      ),
      pw.SizedBox(height: 20),
    ];

    int questionNumber = 1;
    for (var chapter in chapters) {
      content.add(
        pw.Padding(
          padding: const pw.EdgeInsets.only(top: 12, bottom: 6),
          child: pw.Text(
            'Chapter: ${chapter.chapterName} (${chapter.subject})',
            style: pw.TextStyle(
              fontSize: 14,
              fontWeight: pw.FontWeight.bold,
              color: PdfColors.grey800,
            ),
          ),
        ),
      );

      for (var item in chapter.fillInTheBlanks) {
        String formattedQuestion = item.question
            .replaceAll('[', '(')
            .replaceAll(']', ')')
            .replaceAll(RegExp(r'\\$'), ''); // Strip math $

        content.add(
          pw.Padding(
            padding: const pw.EdgeInsets.symmetric(vertical: 6),
            child: pw.Column(
              crossAxisAlignment: pw.CrossAxisAlignment.start,
              children: [
                pw.Text(
                  '$questionNumber. $formattedQuestion',
                  style: const pw.TextStyle(fontSize: 12),
                ),
                if (isAnswerKey) ...[
                  pw.SizedBox(height: 2),
                  pw.Text(
                    '   Answer: ${item.answer.replaceAll(RegExp(r'\\$'), '')}',
                    style: pw.TextStyle(
                      fontSize: 12,
                      fontWeight: pw.FontWeight.bold,
                      color: PdfColors.green900,
                    ),
                  ),
                ],
              ],
            ),
          ),
        );
        questionNumber++;
      }

      for (var problem in chapter.numericalProblems) {
        content.add(
          pw.Padding(
            padding: const pw.EdgeInsets.symmetric(vertical: 6),
            child: pw.Column(
              crossAxisAlignment: pw.CrossAxisAlignment.start,
              children: [
                pw.Text(
                  '$questionNumber. ${problem.question.replaceAll(RegExp(r'\\$'), '')}',
                  style: const pw.TextStyle(fontSize: 12),
                ),
                if (problem.given.isNotEmpty)
                  pw.Text(
                    '   Given: ${problem.given.join(', ').replaceAll(RegExp(r'\\$'), '')}',
                    style: pw.TextStyle(fontSize: 11, fontStyle: pw.FontStyle.italic, color: PdfColors.grey700),
                  ),
                if (isAnswerKey) ...[
                  pw.SizedBox(height: 2),
                  for (var i = 0; i < problem.solutionSteps.length; i++)
                    pw.Text(
                      '   ${i + 1}. ${problem.solutionSteps[i].replaceAll(RegExp(r'\\$'), '')}',
                      style: const pw.TextStyle(fontSize: 11),
                    ),
                  pw.Text(
                    '   Final Answer: ${problem.formattedAnswer.replaceAll(RegExp(r'\\$'), '')}',
                    style: pw.TextStyle(fontSize: 12, fontWeight: pw.FontWeight.bold, color: PdfColors.green900),
                  ),
                ],
              ],
            ),
          ),
        );
        questionNumber++;
      }
    }

    // Show progress dialog
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return const AlertDialog(
          content: Row(
            children: [
              CircularProgressIndicator(),
              SizedBox(width: 20),
              Text("Generating PDF natively... Please wait"),
            ],
          ),
        );
      },
    );

    try {
      await Future.delayed(const Duration(milliseconds: 100));
      await UniversalPdfEngine.generateNativePdfTextOnly(
        title: '$subjectLabel - ${isAnswerKey ? 'Answer Key' : 'Question Paper'}',
        widgets: content,
        isAnswerKey: isAnswerKey,
      );
    } finally {
      if (context.mounted) {
        Navigator.of(context, rootNavigator: true).pop();
      }
    }
  }
}
'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of _generatePdf
    start_idx = content.find('static Future<void> _generatePdf')
    if start_idx != -1:
        # Keep everything before start_idx
        content = content[:start_idx] + new_generate_pdf
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Fixed PdfGeneratorService files")
