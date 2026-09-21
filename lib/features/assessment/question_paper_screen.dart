import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import 'services/pdf_generation_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class QuestionPaperScreen extends StatefulWidget {
  final Map<String, dynamic>? customPaperData;
  const QuestionPaperScreen({super.key, this.customPaperData});

  @override
  State<QuestionPaperScreen> createState() => _QuestionPaperScreenState();
}

class _QuestionPaperScreenState extends State<QuestionPaperScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  final PdfGenerationService _pdfService = PdfGenerationService();
  
  Map<String, dynamic>? _paperData;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _loadPaperData();
  }

  Future<void> _loadPaperData() async {
    if (widget.customPaperData != null) {
      setState(() {
        _paperData = widget.customPaperData;
        _isLoading = false;
      });
      return;
    }

    try {
      final jsonString = await rootBundle.loadString('app_core/assessment/mock_paper.json');
      setState(() {
        _paperData = json.decode(jsonString);
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _downloadPdf() async {
    if (_paperData == null) return;
    
    final title = _paperData!['paper_title'];
    final questions = _paperData!['questions'] as List;

    try {
      if (_tabController.index == 0) {
        await _pdfService.generateQuestionPaperPDF(title, questions);
      } else {
        await _pdfService.generateSolutionsPDF(title, questions);
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error generating PDF: $e'), backgroundColor: Colors.red),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    if (_paperData == null) {
      return Scaffold(body: Center(child: Text(TrilingualService.instance.getUIText("Error loading paper."))));
    }

    final questions = _paperData!['questions'] as List;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        iconTheme: const IconThemeData(color: AppColors.textPrimary),
        title: Text(
          _paperData!['paper_title'],
          style: GoogleFonts.poppins(color: AppColors.textPrimary, fontWeight: FontWeight.bold, fontSize: 18),
        ),
        bottom: TabBar(
          controller: _tabController,
          labelColor: AppColors.primary,
          unselectedLabelColor: Colors.grey,
          indicatorColor: AppColors.primary,
          labelStyle: GoogleFonts.inter(fontWeight: FontWeight.bold),
          tabs: const [
            Tab(text: "Question Paper", icon: Icon(Icons.assignment)),
            Tab(text: "Solutions", icon: Icon(Icons.check_circle_outline)),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildQuestionsList(questions, showSolutions: false),
          _buildQuestionsList(questions, showSolutions: true),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: _downloadPdf,
        backgroundColor: AppColors.primary,
        icon: Icon(Icons.picture_as_pdf, color: Colors.white),
        label: Text(TrilingualService.instance.getUIText("Download PDF"),
          style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.white),
        ),
      ),
    );
  }

  Widget _buildQuestionsList(List questions, {required bool showSolutions}) {
    return ListView.builder(
      padding: const EdgeInsets.all(20),
      itemCount: questions.length,
      itemBuilder: (context, index) {
        final q = questions[index];
        return Card(
          margin: const EdgeInsets.only(bottom: 20),
          elevation: 2,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    CircleAvatar(
                      radius: 16,
                      backgroundColor: AppColors.primary.withValues(alpha: 0.1),
                      child: Text("${q['q_no']}", style: TextStyle(color: AppColors.primary, fontWeight: FontWeight.bold)),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        q['question'],
                        style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w600, height: 1.5),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: Colors.orange.withValues(alpha: 0.1),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text("${q['marks']} Marks", style: GoogleFonts.inter(color: Colors.orange[800], fontWeight: FontWeight.bold, fontSize: 12)),
                    )
                  ],
                ),
                if (showSolutions) ...[
                  const SizedBox(height: 16),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.green.withValues(alpha: 0.05),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: Colors.green.withValues(alpha: 0.2)),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText("Solution:"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.green[800])),
                        const SizedBox(height: 8),
                        Text(
                          q['solution'],
                          style: GoogleFonts.inter(fontSize: 14, color: Theme.of(context).colorScheme.onSurface, height: 1.5),
                        ),
                      ],
                    ),
                  )
                ]
              ],
            ),
          ),
        );
      },
    );
  }
}
