import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import '../../core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class QuestionBankScreen extends StatefulWidget {
  final String moduleId;
  const QuestionBankScreen({super.key, required this.moduleId});

  @override
  State<QuestionBankScreen> createState() => _QuestionBankScreenState();
}

class _QuestionBankScreenState extends State<QuestionBankScreen> {
  List<AssessmentQuestion> _bankData = [];
  bool _isLoading = true;
  String _error = '';
  
  final Set<int> _selectedIndex = {};

  @override
  void initState() {
    super.initState();
    _loadBankData();
  }

  Future<void> _loadBankData() async {
    try {
      final questions = await AssessmentEngine.instance.extractQuestionsForModule(
        widget.moduleId, 
        ['quiz', 'fill_blank', 'true_false', 'short_note']
      );
      setState(() {
        _bankData = questions;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _error = 'Failed to load question bank for this chapter.';
        _isLoading = false;
      });
    }
  }

  void _generatePaper() {
    if (_selectedIndex.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(TrilingualService.instance.getUIText('Please select at least one question.')), backgroundColor: Colors.orange),
      );
      return;
    }

    final selectedQuestions = _selectedIndex.map((idx) => _bankData[idx]).toList();

    // The rest of this logic will need to be adapted or passed directly to QuestionPaperViewScreen
    // Since QuestionPaperViewScreen takes a List<AssessmentQuestion>, we can just push it directly!
    context.push('/assessment/paper_generator', extra: selectedQuestions);
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }
    
    if (_error.isNotEmpty) {
      return Scaffold(
        appBar: const BrandAppBar(title: 'Question Bank'),
        body: Center(child: Text(_error)),
      );
    }

    final title = 'Question Bank';
    final questions = _bankData;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(title: title),
      body: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(16),
            color: Colors.blue.withValues(alpha: 0.1),
            width: double.infinity,
            child: Row(
              children: [
                Icon(Icons.info_outline, color: Colors.blue),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(TrilingualService.instance.getUIText("Select the questions you want to include in your PDF Exam Paper."),
                    style: GoogleFonts.inter(color: Colors.blue[900], fontWeight: FontWeight.w600),
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: questions.length,
              itemBuilder: (context, index) {
                final q = questions[index];
                final isSelected = _selectedIndex.contains(index);

                return Card(
                  margin: const EdgeInsets.only(bottom: 12),
                  elevation: isSelected ? 4 : 1,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                    side: BorderSide(color: isSelected ? AppColors.primary : Colors.transparent, width: 2),
                  ),
                  child: InkWell(
                    borderRadius: BorderRadius.circular(12),
                    onTap: () {
                      setState(() {
                        if (isSelected) {
                          _selectedIndex.remove(index);
                        } else {
                          _selectedIndex.add(index);
                        }
                      });
                    },
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Checkbox(
                            value: isSelected,
                            activeColor: AppColors.primary,
                            onChanged: (val) {
                              setState(() {
                                if (val == true) {
                                  _selectedIndex.add(index);
                                } else {
                                  _selectedIndex.remove(index);
                                }
                              });
                            },
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                      decoration: BoxDecoration(
                                        color: Colors.grey[200],
                                        borderRadius: BorderRadius.circular(8),
                                      ),
                                      child: Text("Marks: ${q.type == 'short_note' ? '5' : '1'}", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                                    ),
                                    const SizedBox(width: 8),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                      decoration: BoxDecoration(
                                        color: Colors.orange[50],
                                        borderRadius: BorderRadius.circular(8),
                                      ),
                                      child: Text(q.type.toUpperCase().replaceAll('_', ' '), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12, color: Colors.orange[900])),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 8),
                                Text(
                                  q.question,
                                  style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w500, color: AppColors.textPrimary),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: _generatePaper,
        backgroundColor: _selectedIndex.isEmpty ? Colors.grey : AppColors.primary,
        icon: Icon(Icons.picture_as_pdf, color: Colors.white),
        label: Text(
          "Generate Exam (${_selectedIndex.length})",
          style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.white),
        ),
      ),
    );
  }
}
