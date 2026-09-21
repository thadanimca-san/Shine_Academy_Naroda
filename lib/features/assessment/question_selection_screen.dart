import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../core/engine/assessment_engine.dart';
import 'question_paper_view_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class QuestionSelectionScreen extends StatefulWidget {
  final List<AssessmentQuestion> allQuestionsPool;
  final List<AssessmentQuestion> initialSelectedQuestions;
  final String title;

  const QuestionSelectionScreen({
    super.key,
    required this.allQuestionsPool,
    required this.initialSelectedQuestions,
    required this.title,
  });

  @override
  State<QuestionSelectionScreen> createState() =>
      _QuestionSelectionScreenState();
}

class _QuestionSelectionScreenState extends State<QuestionSelectionScreen> {
  final Set<int> _selectedIndices = {};
  late List<AssessmentQuestion> _currentQuestions;

  @override
  void initState() {
    super.initState();
    _currentQuestions = List.from(widget.initialSelectedQuestions);
    // Select all by default
    for (int i = 0; i < _currentQuestions.length; i++) {
      _selectedIndices.add(i);
    }
  }

  String _getLocalizedQuestion(AssessmentQuestion q) {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && q.questionHi != null && q.questionHi!.isNotEmpty) return q.questionHi!;
    if (lang == 'gu' && q.questionGu != null && q.questionGu!.isNotEmpty) return q.questionGu!;
    return q.question;
  }

  void _generatePaper() {
    if (_selectedIndices.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            TrilingualService.instance.getUIText(
              'Please select at least one question!',
            ),
          ),
        ),
      );
      return;
    }

    final selectedQuestions = _selectedIndices
        .map((i) => _currentQuestions[i])
        .toList();

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => QuestionPaperViewScreen(
          questions: selectedQuestions,
          title: widget.title,
        ),
      ),
    );
  }

  void _swapQuestion(int index) {
    final currentQ = _currentQuestions[index];

    // Find a question in pool of same type and marks that is NOT in _currentQuestions
    final available = widget.allQuestionsPool
        .where(
          (q) =>
              q.type == currentQ.type &&
              q.marks == currentQ.marks &&
              !_currentQuestions.any(
                (existing) => existing.question == q.question,
              ),
        )
        .toList();

    if (available.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            TrilingualService.instance.getUIText(
              'No more alternative questions available of this type/marks.',
            ),
          ),
        ),
      );
      return;
    }

    available.shuffle();
    setState(() {
      _currentQuestions[index] = available.first;
      // ensure it stays selected
      _selectedIndices.add(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          TrilingualService.instance.getUIText('Select Questions'),
          style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 16),
        ),
        backgroundColor: Colors.white,
        foregroundColor: Colors.blue[900],
        elevation: 1,
        actions: [
          TextButton(
            onPressed: () {
              setState(() {
                if (_selectedIndices.length == _currentQuestions.length) {
                  _selectedIndices.clear();
                } else {
                  _selectedIndices.addAll(
                    List.generate(_currentQuestions.length, (i) => i),
                  );
                }
              });
            },
            child: Text(
              _selectedIndices.length == _currentQuestions.length
                  ? 'Deselect All'
                  : 'Select All',
              style: TextStyle(
                color: Colors.blue[800],
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(16),
            color: Colors.blue[50],
            child: Row(
              children: [
                Icon(Icons.info_outline, color: Colors.blue[800]),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    TrilingualService.instance.getUIText(
                      'Teacher Mode: Swap unsuitable questions or uncheck them before generating the final paper.',
                    ),
                    style: GoogleFonts.inter(color: Colors.blue[900]),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.separated(
              itemCount: _currentQuestions.length,
              separatorBuilder: (context, index) => const Divider(),
              itemBuilder: (context, index) {
                final q = _currentQuestions[index];
                if (q.type == 'section_header') {
                  return Container(
                    padding: const EdgeInsets.symmetric(
                      vertical: 16,
                      horizontal: 24,
                    ),
                    color: Colors.blue[100],
                    child: Text(
                      q.question,
                      style: GoogleFonts.poppins(
                        fontWeight: FontWeight.bold,
                        fontSize: 16,
                        color: Colors.blue[900],
                      ),
                    ),
                  );
                }

                return CheckboxListTile(
                  value: _selectedIndices.contains(index),
                  onChanged: (bool? val) {
                    setState(() {
                      if (val == true) {
                        _selectedIndices.add(index);
                      } else {
                        _selectedIndices.remove(index);
                      }
                    });
                  },
                  title: Text(
                    _getLocalizedQuestion(q),
                    style: GoogleFonts.inter(
                      fontWeight: FontWeight.w600,
                      fontSize: 16,
                    ),
                  ),
                  subtitle: q.type == 'quiz'
                      ? Text(
                          q.options.join(" | "),
                          style: TextStyle(color: Colors.grey),
                        )
                      : Text(
                          'Type: ${q.type}',
                          style: TextStyle(color: Colors.grey),
                        ),
                  secondary: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      CircleAvatar(
                        backgroundColor: Colors.blue[50],
                        foregroundColor: Colors.blue[900],
                        radius: 16,
                        child: Text(
                          '${q.marks}M',
                          style: const TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      IconButton(
                        icon: const Icon(Icons.autorenew),
                        color: Colors.blue[700],
                        tooltip: TrilingualService.instance.getUIText(
                          'Swap Question',
                        ),
                        onPressed: () => _swapQuestion(index),
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: Colors.white,
            boxShadow: [
              BoxShadow(
                color: Theme.of(
                  context,
                ).colorScheme.onSurface.withValues(alpha: 0.1),
                blurRadius: 10,
                offset: const Offset(0, -5),
              ),
            ],
          ),
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.blue[700],
              foregroundColor: Colors.white,
              minimumSize: const Size.fromHeight(50),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
            ),
            onPressed: _generatePaper,
            child: Text(
              '${TrilingualService.instance.getUIText("Confirm & Generate")} (${_selectedIndices.length})',
              style: GoogleFonts.poppins(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
      ),
    );
  }
}
