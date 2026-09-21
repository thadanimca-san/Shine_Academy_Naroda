import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ChapterDetailScreen extends StatefulWidget {
  final String assetPath;

  const ChapterDetailScreen({
    Key? key,
    this.assetPath = 'app_core/chapters/ncert_class10_science_ch1_chemical_reactions.json',
  }) : super(key: key);

  @override
  _ChapterDetailScreenState createState() => _ChapterDetailScreenState();
}

class _ChapterDetailScreenState extends State<ChapterDetailScreen> {
  Map<String, dynamic>? chapterData;
  bool isLoading = true;
  String errorMessage = '';
  String currentLanguage = 'en'; // 'en' or 'gu'

  @override
  void initState() {
    super.initState();
    loadChapterData();
  }

  Future<void> loadChapterData() async {
    setState(() {
      isLoading = true;
      errorMessage = '';
    });
    
    String targetPath = widget.assetPath;
    if (currentLanguage == 'gu') {
      targetPath = targetPath.replaceAll('.json', '_gu.json');
    }
    
    try {
      String jsonStr = await rootBundle.loadString(targetPath);
      final decoded = json.decode(jsonStr);
      
      Map<String, dynamic> normalized;
      if (decoded is List) {
        normalized = {
          'metadata': {'title': 'Chapter'},
          'content': decoded,
          'blocks': decoded,
        };
      } else {
        normalized = decoded as Map<String, dynamic>;
      }

      setState(() {
        chapterData = normalized;
        isLoading = false;
      });
    } catch (e) {
      debugPrint('Error loading chapter file: $e');
      if (currentLanguage == 'gu') {
        // Fallback to English if Gujarati is not found
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(TrilingualService.instance.getUIText('Gujarati version is not available for this chapter yet.'))),
        );
        setState(() {
          currentLanguage = 'en';
        });
        loadChapterData();
        return;
      }
      setState(() {
        isLoading = false;
        errorMessage = e.toString();
      });
    }
  }

  Widget _buildTheoryTab(Map<String, dynamic> data) {
    final intro = data['introduction'] ?? {};
    final defs = data['key_definitions'] as List? ?? [];

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        if (intro.isNotEmpty) ...[
          Text(
            intro['heading'] ?? 'Introduction',
            style: GoogleFonts.poppins(fontSize: 22, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
          ),
          const SizedBox(height: 12),
          Text(
            intro['details_en'] ?? '',
            style: GoogleFonts.inter(fontSize: 16, height: 1.6, color: AppColors.textPrimary),
          ),
          const Divider(height: 40, thickness: 1),
        ],
        Text(TrilingualService.instance.getUIText("Key Definitions"),
          style: GoogleFonts.poppins(fontSize: 20, fontWeight: FontWeight.bold, color: AppColors.primary),
        ),
        const SizedBox(height: 16),
        ...defs.map((def) => Card(
              margin: const EdgeInsets.only(bottom: 16),
              elevation: 2,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      def['term'] ?? '',
                      style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 16, color: AppColors.accent),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      def['explanation_en'] ?? '',
                      style: GoogleFonts.inter(fontSize: 15, height: 1.5, color: AppColors.textSecondary),
                    ),
                  ],
                ),
              ),
            )),
      ],
    );
  }

  Widget _buildExamplesTab(Map<String, dynamic> data) {
    final examples = data['practical_examples'] as List? ?? [];
    if (examples.isEmpty) {
      return Center(child: Text(TrilingualService.instance.getUIText("No examples available.")));
    }

    return ListView(
      padding: const EdgeInsets.all(16),
      children: examples.map((ex) => Card(
            margin: const EdgeInsets.only(bottom: 16),
            elevation: 3,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            child: Theme(
              data: Theme.of(context).copyWith(dividerColor: Colors.transparent),
              child: ExpansionTile(
                initiallyExpanded: ex['example_no'] == 1,
                title: Text(
                  "Example ${ex['example_no']}: ${ex['title']}",
                  style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 16, color: AppColors.primaryDark),
                ),
                children: [
                  Container(
                    width: double.infinity,
                    decoration: BoxDecoration(
                      color: AppColors.surface,
                      borderRadius: const BorderRadius.only(bottomLeft: Radius.circular(16), bottomRight: Radius.circular(16)),
                    ),
                    padding: const EdgeInsets.all(16.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText("Problem:"),
                          style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 14, color: Colors.grey[700]),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          ex['problem'] ?? '',
                          style: GoogleFonts.inter(fontSize: 15, height: 1.5),
                        ),
                        const SizedBox(height: 16),
                        Text(TrilingualService.instance.getUIText("Solution:"),
                          style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 14, color: Colors.green[700]),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          ex['solution'] ?? '',
                          style: GoogleFonts.inter(fontSize: 15, height: 1.5),
                        ),
                      ],
                    ),
                  )
                ],
              ),
            ),
          )).toList(),
    );
  }

  Widget _buildExercisesTab(Map<String, dynamic> data) {
    final exercises = data['exercises'] as List? ?? [];
    if (exercises.isEmpty) {
      return Center(child: Text(TrilingualService.instance.getUIText("No exercises available.")));
    }

    return ListView(
      padding: const EdgeInsets.all(16),
      children: exercises.map((q) => Card(
            margin: const EdgeInsets.only(bottom: 16),
            elevation: 2,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      CircleAvatar(
                        radius: 14,
                        backgroundColor: AppColors.primary,
                        child: Text(
                          "${q['q_no']}",
                          style: GoogleFonts.inter(color: Colors.white, fontSize: 12, fontWeight: FontWeight.bold),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          q['question'] ?? '',
                          style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w600, height: 1.4),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  if (q['options'] != null)
                    ...List<String>.from(q['options']).map((opt) => Padding(
                          padding: const EdgeInsets.only(bottom: 8.0, left: 40),
                          child: Container(
                            width: double.infinity,
                            padding: const EdgeInsets.all(12),
                            decoration: BoxDecoration(
                              color: Colors.grey[100],
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: Colors.grey[300]!),
                            ),
                            child: Text(
                              opt,
                              style: GoogleFonts.inter(fontSize: 14),
                            ),
                          ),
                        )),
                ],
              ),
            ),
          )).toList(),
    );
  }

  Widget _buildPyqTab(Map<String, dynamic> data) {
    final pyqs = data['previous_years_questions'] as List? ?? [];
    if (pyqs.isEmpty) {
      return Center(child: Text(TrilingualService.instance.getUIText("No PYQs available.")));
    }

    return ListView(
      padding: const EdgeInsets.all(16),
      children: pyqs.map((pyq) => Card(
            margin: const EdgeInsets.only(bottom: 16),
            elevation: 3,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: BorderSide(color: AppColors.accent.withValues(alpha: 0.3), width: 1),
            ),
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Chip(
                        backgroundColor: AppColors.accent.withValues(alpha: 0.1),
                        label: Text(
                          "Year: ${pyq['year']}",
                          style: GoogleFonts.poppins(color: AppColors.accent, fontWeight: FontWeight.bold, fontSize: 12),
                        ),
                      ),
                      Text(
                        pyq['question_type'] ?? '',
                        style: GoogleFonts.inter(color: Colors.grey[600], fontSize: 12, fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text(
                    pyq['question'] ?? '',
                    style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 15, height: 1.5),
                  ),
                  const Divider(height: 24),
                  Text(TrilingualService.instance.getUIText("Solution:"),
                    style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 13, color: Colors.green[700]),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    pyq['solution'] ?? '',
                    style: GoogleFonts.inter(fontSize: 14, height: 1.5, color: Colors.grey[800]),
                  ),
                ],
              ),
            ),
          )).toList(),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    if (chapterData == null) {
      return Scaffold(
        appBar: AppBar(title: Text(TrilingualService.instance.getUIText("Error"))),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text("Failed to load chapter content.\n\nError details:\n$errorMessage", 
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.red, fontSize: 14),
            ),
          ),
        ),
      );
    }

    return DefaultTabController(
      length: 4,
      child: Scaffold(
        backgroundColor: AppColors.background,
        appBar: BrandAppBar(
          title: chapterData!['chapter_name_en'] ?? chapterData!['title'] ?? 'Chapter Details',
          actions: [
            Padding(
              padding: const EdgeInsets.only(right: 8.0),
              child: Row(
                children: [
                  Text(TrilingualService.instance.getUIText('EN'), style: TextStyle(fontWeight: currentLanguage == 'en' ? FontWeight.bold : FontWeight.normal, color: currentLanguage == 'en' ? Colors.white : Colors.white54)),
                  Switch(
                    value: currentLanguage == 'gu',
                    onChanged: (val) {
                      setState(() {
                        currentLanguage = val ? 'gu' : 'en';
                      });
                      loadChapterData();
                    },
                    activeThumbColor: Colors.white,
                    activeTrackColor: Colors.white38,
                    inactiveThumbColor: Colors.white,
                    inactiveTrackColor: Colors.white38,
                  ),
                  Text(TrilingualService.instance.getUIText('GU'), style: TextStyle(fontWeight: currentLanguage == 'gu' ? FontWeight.bold : FontWeight.normal, color: currentLanguage == 'gu' ? Colors.white : Colors.white54)),
                  const SizedBox(width: 8),
                ],
              ),
            ),
          ],
          bottom: TabBar(
            isScrollable: true,
            indicatorColor: Colors.white,
            indicatorWeight: 3,
            labelColor: Colors.white,
            unselectedLabelColor: Colors.white70,
            labelStyle: GoogleFonts.poppins(fontWeight: FontWeight.bold),
            unselectedLabelStyle: GoogleFonts.poppins(fontWeight: FontWeight.normal),
            tabs: const [
              Tab(text: "Theory & Concepts"),
              Tab(text: "Examples"),
              Tab(text: "Exercises"),
              Tab(text: "Board PYQs"),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            _buildTheoryTab(chapterData!),
            _buildExamplesTab(chapterData!),
            _buildExercisesTab(chapterData!),
            _buildPyqTab(chapterData!),
          ],
        ),
      ),
    );
  }
}