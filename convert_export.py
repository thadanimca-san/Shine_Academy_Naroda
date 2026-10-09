import re

path = 'lib/features/assessment/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace flutter imports
content = content.replace("import 'package:flutter/material.dart';", "import 'package:flutter/material.dart' show BuildContext, showDialog, AlertDialog, CircularProgressIndicator, Row, Text, SizedBox, Navigator;\nimport 'package:pdf/pdf.dart';\nimport 'package:pdf/widgets.dart' as pw;")
content = content.replace("import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';", "")

content = content.replace('List<Widget>', 'List<pw.Widget>')
content = content.replace('static Widget', 'static pw.Widget')
content = content.replace('Widget>', 'pw.Widget>')
content = content.replace('Widget _build', 'pw.Widget _build')

# Now replace widgets
content = content.replace('const SizedBox', 'pw.SizedBox')
content = content.replace('SizedBox(', 'pw.SizedBox(')
content = content.replace('Center(', 'pw.Center(')
content = content.replace('Padding(', 'pw.Padding(')
content = content.replace('Row(', 'pw.Row(')
content = content.replace('Column(', 'pw.Column(')
content = content.replace('Expanded(', 'pw.Expanded(')
content = content.replace('Container(', 'pw.Container(')
content = content.replace('Wrap(', 'pw.Wrap(')
content = content.replace('TtsInteractiveText(', 'pw.Text(')

# Styles and enums
content = content.replace('TextStyle', 'pw.TextStyle')
content = content.replace('FontWeight.bold', 'pw.FontWeight.bold')
content = content.replace('FontWeight.normal', 'pw.FontWeight.normal')
content = content.replace('FontStyle.italic', 'pw.FontStyle.italic')
content = content.replace('CrossAxisAlignment.start', 'pw.CrossAxisAlignment.start')
content = content.replace('EdgeInsets.', 'pw.EdgeInsets.')
content = content.replace('Colors.black', 'PdfColors.black')
content = content.replace('Colors.green', 'PdfColors.green')
content = content.replace('Colors.black54', 'PdfColors.grey700')
content = content.replace('BoxDecoration(', 'pw.BoxDecoration(')
content = content.replace('Border.all(', 'pw.Border.all(')

# generatePdfFromWidgets -> generateNativePdfTextOnly
content = content.replace('UniversalPdfEngine.generatePdfFromWidgets', 'UniversalPdfEngine.generateNativePdfTextOnly')

# Add context to signatures
content = content.replace('generateQuestionPaper(String title,', 'generateQuestionPaper(BuildContext context, String title,')
content = content.replace('generateAnswerKey(String title,', 'generateAnswerKey(BuildContext context, String title,')

# Add progress dialog
progress_code = '''
    _showProgress(context, "Generating PDF natively...");
    try {
      await Future.delayed(const Duration(milliseconds: 100));
'''
end_try_code = '''
    } finally {
      if (context.mounted) Navigator.of(context, rootNavigator: true).pop();
    }
'''

content = re.sub(r'await UniversalPdfEngine\.generateNativePdfTextOnly\((.*?)\);', progress_code + r'await UniversalPdfEngine.generateNativePdfTextOnly(\1);' + end_try_code, content, flags=re.DOTALL)

# Add _showProgress
show_progress_fn = '''
  static void _showProgress(BuildContext context, String message) {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          content: Row(
            children: [
              const CircularProgressIndicator(),
              const SizedBox(width: 20),
              Text(message),
            ],
          ),
        );
      },
    );
  }
}
'''
content = content.replace('}\n\n  static String _getAnswerText', '  static String _getAnswerText')
content = re.sub(r'\}\s*$', show_progress_fn, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Converted pdf_export_service")
