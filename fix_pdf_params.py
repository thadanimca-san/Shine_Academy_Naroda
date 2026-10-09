import re

path = 'lib/features/assessment/services/pdf_export_service.dart'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update generateAndPreviewQuestionPaper signature
old_sig_q = 'static Future<void> generateAndPreviewQuestionPaper(BuildContext context, String title, List<AssessmentQuestion> questions) async {'
new_sig_q = 'static Future<void> generateAndPreviewQuestionPaper(BuildContext context, String title, List<AssessmentQuestion> questions, {String? schoolName, String? examTitle, String? timeAllowed}) async {'
content = content.replace(old_sig_q, new_sig_q)

# Update generateAndPreviewAnswerKey signature
old_sig_a = 'static Future<void> generateAndPreviewAnswerKey(BuildContext context, String title, List<AssessmentQuestion> questions) async {'
new_sig_a = 'static Future<void> generateAndPreviewAnswerKey(BuildContext context, String title, List<AssessmentQuestion> questions, {String? schoolName, String? examTitle, String? timeAllowed}) async {'
content = content.replace(old_sig_a, new_sig_a)

# Update _buildGroupedQuestionsWidgets signature to pass the params down
old_build_sig = 'static List<pw.Widget> _buildGroupedQuestionsWidgets(List<AssessmentQuestion> questions, {required bool showAnswers}) {'
new_build_sig = 'static List<pw.Widget> _buildGroupedQuestionsWidgets(List<AssessmentQuestion> questions, {required bool showAnswers, String? schoolName, String? examTitle, String? timeAllowed}) {'
content = content.replace(old_build_sig, new_build_sig)

# Update the calls to _buildGroupedQuestionsWidgets
content = content.replace(
    'final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: false);',
    'final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: false, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);'
)
content = content.replace(
    'final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: true);',
    'final widgets = _buildGroupedQuestionsWidgets(questions, showAnswers: true, schoolName: schoolName, examTitle: examTitle, timeAllowed: timeAllowed);'
)

# Now, actually render the school/exam title block inside _buildGroupedQuestionsWidgets
injection = """
    if (schoolName != null && schoolName.isNotEmpty) {
      widgets.add(pw.Center(child: pw.Text(schoolName, style: pw.TextStyle(fontSize: 18, fontWeight: pw.FontWeight.bold))));
      widgets.add(pw.SizedBox(height: 4));
    }
    if (examTitle != null && examTitle.isNotEmpty) {
      widgets.add(pw.Center(child: pw.Text(examTitle, style: pw.TextStyle(fontSize: 16, fontWeight: pw.FontWeight.bold))));
      widgets.add(pw.SizedBox(height: 8));
    }
    
    if ((timeAllowed != null && timeAllowed.isNotEmpty) || (schoolName != null && schoolName.isNotEmpty)) {
       int totalMarks = questions.fold(0, (sum, q) => q.type == 'section_header' ? sum : sum + q.marks);
       widgets.add(
         pw.Row(
           mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
           children: [
             if (timeAllowed != null && timeAllowed.isNotEmpty) 
                pw.Text('Time: $timeAllowed', style: pw.TextStyle(fontWeight: pw.FontWeight.bold))
             else pw.SizedBox(),
             pw.Text('Total Marks: $totalMarks', style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
           ]
         )
       );
       widgets.add(pw.Divider());
    }

    widgets.add(pw.SizedBox(height: 10));
"""

content = content.replace('widgets.add(pw.SizedBox(height: 10));\n    widgets.add(_buildInstructions());', injection + '    widgets.add(_buildInstructions());')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated pdf export service signatures")
