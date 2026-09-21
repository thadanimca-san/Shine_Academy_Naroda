import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';

class SubjectListScreen extends StatefulWidget {
  final String curriculumId;
  const SubjectListScreen({super.key, required this.curriculumId});

  @override
  State<SubjectListScreen> createState() => _SubjectListScreenState();
}

class _SubjectListScreenState extends State<SubjectListScreen> {
  Map<String, dynamic>? _curriculumData;
  bool _isLoading = true;
  String _error = '';

  @override
  void initState() {
    super.initState();
    _loadCurriculum();
  }

  Future<void> _loadCurriculum() async {
    try {
      final jsonString = await rootBundle.loadString('app_core/curriculum/${widget.curriculumId}.json');
      setState(() {
        _curriculumData = json.decode(jsonString);
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _error = 'Failed to load curriculum data.';
        _isLoading = false;
      });
    }
  }

  IconData _getIconData(String iconName) {
    switch (iconName) {
      case 'account_balance': return Icons.account_balance;
      case 'bar_chart': return Icons.bar_chart;
      case 'language': return Icons.language;
      case 'business_center': return Icons.business_center;
      case 'trending_up': return Icons.trending_up;
      case 'translate': return Icons.translate;
      case 'g_translate': return Icons.g_translate;
      case 'calculate': return Icons.calculate;
      case 'psychology': return Icons.psychology;
      case 'grid_on': return Icons.grid_on;
      case 'science': return Icons.science;
      case 'menu_book': return Icons.menu_book;
      case 'auto_stories': return Icons.auto_stories;
      default: return Icons.book;
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }
    
    if (_error.isNotEmpty) {
      return Scaffold(
        appBar: const BrandAppBar(title: 'Curriculum'),
        body: Center(child: Text(_error)),
      );
    }

    final title = _curriculumData!['title'] ?? 'Complete Course';
    final subjects = _curriculumData!['subjects'] as List;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(title: title),
      body: ListView.builder(
        padding: const EdgeInsets.all(20),
        itemCount: subjects.length,
        itemBuilder: (context, index) {
          final subject = subjects[index];
          final color = Color(int.parse(subject['color_hex']));
          final iconData = _getIconData(subject['icon']);
          
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 16),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            child: InkWell(
              borderRadius: BorderRadius.circular(12),
              onTap: () {
                final match = RegExp(r'\d+').firstMatch(widget.curriculumId);
                final gradeNum = match != null ? match.group(0) : '9';
                
                if (subject['id'] == 'interactive_science_sim') {
                  context.push('/learning/sci_sim?grade=$gradeNum');
                  return;
                }
                
                if (subject['id'] == 'interactive_grammar') {
                  if (['gseb_class3', 'gseb_class4', 'gseb_class5', 'gseb_class6', 'cbse_class3', 'cbse_class4', 'cbse_class5', 'cbse_class6'].contains(widget.curriculumId)) {
                    context.push('/learning/eng3to6?grade=$gradeNum');
                  } else {
                    context.push('/learning/english_sim?grade=$gradeNum'); // assuming it accepts grade in the future
                  }
                  return;
                }
                // Navigate to chapter list, passing the curriculum ID and subject ID
                context.push('/curriculum/${widget.curriculumId}/${subject['id']}/chapters');
              },
              child: Padding(
                padding: const EdgeInsets.all(20.0),
                child: Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        color: color.withValues(alpha: 0.1),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Icon(iconData, color: color, size: 32),
                    ),
                    const SizedBox(width: 20),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            subject['name'],
                            style: GoogleFonts.poppins(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: AppColors.textPrimary,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            '${(subject['chapters'] as List).length} Chapters',
                            style: GoogleFonts.inter(
                              color: AppColors.textSecondary,
                            ),
                          ),
                        ],
                      ),
                    ),
                    Icon(Icons.arrow_forward_ios, size: 16, color: Colors.grey),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
