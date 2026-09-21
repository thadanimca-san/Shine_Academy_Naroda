import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../core/engine/assessment_engine.dart';
import '../../../core/widgets/presentation_builder.dart';
import 'services/pdf_export_service.dart';
import 'exam_engine_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class QuestionPaperViewScreen extends StatefulWidget {
  final List<AssessmentQuestion> questions;
  final String title;

  const QuestionPaperViewScreen({super.key, required this.questions, required this.title});

  @override
  State<QuestionPaperViewScreen> createState() => _QuestionPaperViewScreenState();
}

class _QuestionPaperViewScreenState extends State<QuestionPaperViewScreen> with SingleTickerProviderStateMixin {
  late final TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _showTimerDialog() {
    int selectedMinutes = widget.questions.length * 2; // Default 2 mins per question
    
    showDialog(
      context: context,
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setState) {
            return AlertDialog(
              title: Text(TrilingualService.instance.getUIText('Set Exam Timer'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(TrilingualService.instance.getUIText('How many minutes do you want to set for this exam?')),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      IconButton(
                        icon: const Icon(Icons.remove_circle_outline),
                        onPressed: selectedMinutes > 5 ? () => setState(() => selectedMinutes -= 5) : null,
                      ),
                      Text('$selectedMinutes mins', style: GoogleFonts.inter(fontSize: 20, fontWeight: FontWeight.bold)),
                      IconButton(
                        icon: const Icon(Icons.add_circle_outline),
                        onPressed: selectedMinutes < 180 ? () => setState(() => selectedMinutes += 5) : null,
                      ),
                    ],
                  ),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: Text(TrilingualService.instance.getUIText('Cancel')),
                ),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700], foregroundColor: Colors.white),
                  onPressed: () {
                    Navigator.pop(context);
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ExamEngineScreen(
                          moduleId: 'custom',
                          customQuestions: widget.questions,
                          customTitle: widget.title,
                          customTimeSeconds: selectedMinutes * 60,
                        ),
                      ),
                    );
                  },
                  child: Text(TrilingualService.instance.getUIText('Start Exam')),
                ),
              ],
            );
          }
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(widget.title, style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.blue[900], fontSize: 18)),
        backgroundColor: Colors.white,
        elevation: 1,
        iconTheme: IconThemeData(color: Colors.blue[900]),
        bottom: TabBar(
          controller: _tabController,
          labelColor: Colors.blue[900],
          unselectedLabelColor: Colors.grey[600],
          indicatorColor: Colors.blue[800],
          tabs: const [
            Tab(text: 'Question Paper'),
            Tab(text: 'Answer Key'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _QuestionPaperView(questions: widget.questions),
          _AnswerKeyView(questions: widget.questions),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              SizedBox(
                width: double.infinity,
                child: FilledButton.icon(
                  icon: const Icon(Icons.computer, size: 18),
                  label: Text(TrilingualService.instance.getUIText('Take Test On-Screen'), style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16)),
                  onPressed: () {
                    _showTimerDialog();
                  },
                  style: FilledButton.styleFrom(
                    backgroundColor: Colors.green[700],
                    padding: const EdgeInsets.symmetric(vertical: 16),
                  ),
                ),
              ),
              const SizedBox(height: 12),
              Row(
                children: [
                  Expanded(
                    child: OutlinedButton.icon(
                      icon: const Icon(Icons.picture_as_pdf, size: 18),
                      label: Text(TrilingualService.instance.getUIText('Export paper PDF')),
                      onPressed: () {
                        _showPdfMetadataDialog(false);
                      },
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        side: BorderSide(color: Colors.grey.shade400),
                      ),
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: OutlinedButton.icon(
                      icon: const Icon(Icons.picture_as_pdf, size: 18),
                      label: Text(TrilingualService.instance.getUIText('Export answer key PDF')),
                      onPressed: () {
                        _showPdfMetadataDialog(true);
                      },
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        side: BorderSide(color: Colors.grey.shade400),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showPdfMetadataDialog(bool isAnswerKey) {
    final schoolNameCtrl = TextEditingController(text: 'Shine Academy Naroda');
    final examTitleCtrl = TextEditingController(text: 'TERM EXAMINATION');
    final timeAllowedCtrl = TextEditingController(text: '1 Hr 30 Min');
    
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text(TrilingualService.instance.getUIText('PDF Details'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextFormField(
                  controller: schoolNameCtrl,
                  decoration: InputDecoration(labelText: TrilingualService.instance.getUIText('Institute Name')),
                ),
                TextFormField(
                  controller: examTitleCtrl,
                  decoration: InputDecoration(labelText: TrilingualService.instance.getUIText('Exam Title')),
                ),
                TextFormField(
                  controller: timeAllowedCtrl,
                  decoration: InputDecoration(labelText: TrilingualService.instance.getUIText('Time Allowed')),
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text(TrilingualService.instance.getUIText('Cancel')),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blue[700], foregroundColor: Colors.white),
              onPressed: () async {
                Navigator.pop(context);
                ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Generating PDF...'))));
                if (isAnswerKey) {
                  await PdfExportService.generateAndPreviewAnswerKey(
                    widget.title, 
                    widget.questions, 
                    schoolName: schoolNameCtrl.text,
                    examTitle: examTitleCtrl.text,
                    timeAllowed: timeAllowedCtrl.text,
                  );
                } else {
                  await PdfExportService.generateAndPreviewQuestionPaper(
                    widget.title, 
                    widget.questions, 
                    schoolName: schoolNameCtrl.text,
                    examTitle: examTitleCtrl.text,
                    timeAllowed: timeAllowedCtrl.text,
                  );
                }
              },
              child: Text(TrilingualService.instance.getUIText('Generate')),
            ),
          ],
        );
      }
    );
  }
}

String _getLocalizedQuestion(AssessmentQuestion q) {
  final lang = TrilingualService.instance.activeViewLanguage;
  if (lang == 'hi' && q.questionHi != null && q.questionHi!.isNotEmpty) return q.questionHi!;
  if (lang == 'gu' && q.questionGu != null && q.questionGu!.isNotEmpty) return q.questionGu!;
  return q.question;
}

String? _getLocalizedExplanation(AssessmentQuestion q) {
  final lang = TrilingualService.instance.activeViewLanguage;
  if (lang == 'hi' && q.explanationHi != null && q.explanationHi!.isNotEmpty) return q.explanationHi!;
  if (lang == 'gu' && q.explanationGu != null && q.explanationGu!.isNotEmpty) return q.explanationGu!;
  return q.explanationEn;
}

List<String> _getLocalizedOptions(AssessmentQuestion q) {
  final lang = TrilingualService.instance.activeViewLanguage;
  if (lang == 'hi' && q.optionsHi != null && q.optionsHi!.isNotEmpty) return q.optionsHi!;
  if (lang == 'gu' && q.optionsGu != null && q.optionsGu!.isNotEmpty) return q.optionsGu!;
  return q.options;
}

class _QuestionPaperView extends StatelessWidget {
  final List<AssessmentQuestion> questions;
  const _QuestionPaperView({required this.questions});

  @override
  Widget build(BuildContext context) {
    return PresentationBuilder(
      builder: (context, scaleFactor) {
        int globalQNum = 1;
        return ListView.builder(
          padding: const EdgeInsets.all(24),
          itemCount: questions.length,
          itemBuilder: (context, index) {
            final q = questions[index];
            
            if (q.type == 'section_header') {
              return Padding(
                padding: EdgeInsets.only(top: 24 * scaleFactor, bottom: 16 * scaleFactor),
                child: Text(
                  _getLocalizedQuestion(q),
                  style: GoogleFonts.poppins(fontSize: 18 * scaleFactor, fontWeight: FontWeight.bold, color: Colors.blue[900]),
                  textAlign: TextAlign.center,
                ),
              );
            }

            final currentQNum = globalQNum++;
            final localizedOpts = _getLocalizedOptions(q);

            return Padding(
              padding: EdgeInsets.only(bottom: 24 * scaleFactor),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Q$currentQNum. ", style: GoogleFonts.inter(fontSize: 16 * scaleFactor, fontWeight: FontWeight.w700, color: Colors.blue[900])),
                      Expanded(
                        child: Text(_getLocalizedQuestion(q), style: GoogleFonts.inter(fontSize: 16 * scaleFactor, fontWeight: FontWeight.w600, color: Colors.black87)),
                      ),
                      Text("[${q.marks}]", style: GoogleFonts.inter(fontSize: 14 * scaleFactor, fontWeight: FontWeight.w500, color: Colors.grey[600])),
                    ],
                  ),
                if (q.type == 'quiz')
                  Padding(
                    padding: const EdgeInsets.only(top: 8.0, left: 32.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: List.generate(
                        localizedOpts.length,
                        (j) => Padding(
                          padding: const EdgeInsets.only(bottom: 4.0),
                          child: Text(
                            '${String.fromCharCode(65 + j)}. ${localizedOpts[j]}',
                            style: GoogleFonts.inter(fontSize: 14 * scaleFactor, color: Colors.black87),
                          ),
                        ),
                      ),
                    ),
                  ),
                if (q.type == 'descriptive')
                  Padding(
                    padding: const EdgeInsets.only(top: 8.0, left: 32.0),
                    child: SizedBox(
                      height: 100 * scaleFactor, // Empty space for writing
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }
}

class _AnswerKeyView extends StatelessWidget {
  final List<AssessmentQuestion> questions;
  const _AnswerKeyView({required this.questions});

  @override
  Widget build(BuildContext context) {
    return PresentationBuilder(
      builder: (context, scaleFactor) {
        int globalQNum = 1;
        return ListView.builder(
          padding: const EdgeInsets.all(24),
          itemCount: questions.length,
          itemBuilder: (context, index) {
            final q = questions[index];
            
            if (q.type == 'section_header') {
              return Padding(
                padding: EdgeInsets.only(top: 24 * scaleFactor, bottom: 8 * scaleFactor),
                child: Text(
                  _getLocalizedQuestion(q),
                  style: GoogleFonts.poppins(fontSize: 14 * scaleFactor, fontWeight: FontWeight.bold, color: Colors.grey[600]),
                  textAlign: TextAlign.center,
                ),
              );
            }

            final currentQNum = globalQNum++;
            final localizedOpts = _getLocalizedOptions(q);
            
            // Format answer display
            String answerDisplay = "";
            if (q.type == 'quiz') {
              final correctIdx = q.correctIndexOrAnswer as int;
              answerDisplay = '(${String.fromCharCode(65 + correctIdx)}) ${localizedOpts[correctIdx]}';
            } else {
              answerDisplay = q.correctIndexOrAnswer.toString();
            }

            final explanation = _getLocalizedExplanation(q);

            return Padding(
              padding: EdgeInsets.only(bottom: 24 * scaleFactor),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Q$currentQNum. ", style: GoogleFonts.inter(fontSize: 15 * scaleFactor, fontWeight: FontWeight.w700, color: Colors.grey[700])),
                      Expanded(
                        child: Text(_getLocalizedQuestion(q), style: GoogleFonts.inter(fontSize: 15 * scaleFactor, fontWeight: FontWeight.w600, color: Colors.grey[800])),
                      ),
                    ],
                  ),
                Padding(
                  padding: const EdgeInsets.only(top: 8.0, left: 32.0),
                  child: Text(
                    "Ans: $answerDisplay",
                    style: GoogleFonts.inter(fontSize: 15 * scaleFactor, fontWeight: FontWeight.w700, color: Colors.green[700]),
                  ),
                ),
                if (explanation != null && explanation.isNotEmpty)
                  Padding(
                    padding: const EdgeInsets.only(top: 4.0, left: 32.0),
                    child: Text(
                      "Solution: $explanation",
                      style: GoogleFonts.inter(fontSize: 14 * scaleFactor, fontStyle: FontStyle.italic, color: Colors.grey[700]),
                    ),
                  ),
                ],
              ),
            );
          },
        );
      },
    );
  }
}
