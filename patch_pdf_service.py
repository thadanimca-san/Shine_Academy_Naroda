import os
import glob

files = glob.glob('lib/features/**/services/pdf_generator_service.dart', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'generateAndOpenQuestionPaper(BuildContext context, List<ChapterModel> chapters)' not in content:
        # We need to replace the signature of generateAndOpenQuestionPaper and generateAndOpenAnswerKey
        content = content.replace(
            'static Future<void> generateAndOpenQuestionPaper(List<ChapterModel> chapters) async {',
            'static Future<void> generateAndOpenQuestionPaper(BuildContext context, List<ChapterModel> chapters) async {'
        )
        content = content.replace(
            'static Future<void> generateAndOpenAnswerKey(List<ChapterModel> chapters) async {',
            'static Future<void> generateAndOpenAnswerKey(BuildContext context, List<ChapterModel> chapters) async {'
        )
        content = content.replace(
            'static Future<void> generateQuestionPaperPDF(ChapterModel chapter, [dynamic extra]) async {',
            'static Future<void> generateQuestionPaperPDF(BuildContext context, ChapterModel chapter, [dynamic extra]) async {'
        )
        content = content.replace(
            'static Future<void> generateAnswerKeyPDF(ChapterModel chapter, [dynamic extra]) async {',
            'static Future<void> generateAnswerKeyPDF(BuildContext context, ChapterModel chapter, [dynamic extra]) async {'
        )
        content = content.replace(
            'static Future<void> _generatePdf(List<ChapterModel> chapters, {required bool isAnswerKey}) async {',
            'static Future<void> _generatePdf(BuildContext context, List<ChapterModel> chapters, {required bool isAnswerKey}) async {'
        )
        # Fix calls to _generatePdf
        content = content.replace(
            'await _generatePdf(chapters, isAnswerKey: false);',
            'await _generatePdf(context, chapters, isAnswerKey: false);'
        )
        content = content.replace(
            'await _generatePdf(chapters, isAnswerKey: true);',
            'await _generatePdf(context, chapters, isAnswerKey: true);'
        )
        content = content.replace(
            'await _generatePdf([chapter], isAnswerKey: false);',
            'await _generatePdf(context, [chapter], isAnswerKey: false);'
        )
        content = content.replace(
            'await _generatePdf([chapter], isAnswerKey: true);',
            'await _generatePdf(context, [chapter], isAnswerKey: true);'
        )
        
        # Add the progress dialog logic
        if 'showDialog(' not in content:
            content = content.replace(
                'await UniversalPdfEngine.generatePdfFromWidgets(',
                '''
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
              Text("Generating PDF... Please wait"),
            ],
          ),
        );
      },
    );

    try {
      await UniversalPdfEngine.generatePdfFromWidgets(
'''
            )
            content = content.replace(
                'isAnswerKey: isAnswerKey,\n    );',
                '''isAnswerKey: isAnswerKey,
      );
    } finally {
      if (context.mounted) {
        Navigator.of(context, rootNavigator: true).pop();
      }
    }'''
            )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Patched pdf_generator_service.dart files")
