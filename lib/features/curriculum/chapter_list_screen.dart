import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import '../learning/learning_engine/services/pdf_export_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ChapterListScreen extends StatefulWidget {
  final String curriculumId;
  final String subjectId;
  const ChapterListScreen({super.key, required this.curriculumId, required this.subjectId});

  @override
  State<ChapterListScreen> createState() => _ChapterListScreenState();
}

class _ChapterListScreenState extends State<ChapterListScreen> {
  Map<String, dynamic>? _subjectData;
  bool _isLoading = true;
  String _error = '';

  @override
  void initState() {
    super.initState();
    _loadChapters();
  }

  Future<void> _loadChapters() async {
    try {
      final jsonString = await rootBundle.loadString('app_core/curriculum/${widget.curriculumId}.json');
      final curriculum = json.decode(jsonString);
      
      final subjects = curriculum['subjects'] as List;
      final subject = subjects.firstWhere(
        (s) => s['id'] == widget.subjectId, 
        orElse: () => null,
      );

      if (subject == null) {
        throw Exception('Subject not found');
      }

      setState(() {
        _subjectData = subject;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _error = 'Failed to load chapters.';
        _isLoading = false;
      });
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
        appBar: const BrandAppBar(title: 'Chapters'),
        body: Center(child: Text(_error)),
      );
    }

    final subjectName = _subjectData!['name'] ?? _subjectData!['title'] ?? 'Subject';
    final colorString = _subjectData!['color_hex'] ?? _subjectData!['color'] ?? '0xFF2196F3';
    final color = Color(int.parse(colorString.replaceAll('0x', ''), radix: 16));
    final chapters = _subjectData!['chapters'] as List;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(
        title: subjectName,
        actions: [
          IconButton(
            icon: Icon(Icons.picture_as_pdf),
            tooltip: 'Download Subject as PDF',
            onPressed: () async {
              // Note: The UI might freeze slightly while building large PDFs.
              await PdfExportService.generateAndPrintSubject(_subjectData!);
            },
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(20),
        itemCount: chapters.length,
        itemBuilder: (context, index) {
          final chapter = chapters[index];
          final moduleId = chapter['module_id'] ?? chapter['id'];
          final isAvailable = chapter['is_available'] == true || moduleId != null || chapter.containsKey('data_file');
          final chapterNum = chapter['chapter_number'] ?? chapter['chapter_no'] ?? index + 1;
          
          return Card(
            elevation: isAvailable ? 2 : 0,
            color: isAvailable ? Colors.white : Colors.grey.shade100,
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ListTile(
                  contentPadding: const EdgeInsets.only(left: 20, right: 20, top: 12, bottom: 4),
                  leading: CircleAvatar(
                    backgroundColor: isAvailable ? color.withValues(alpha: 0.1) : Colors.grey.shade300,
                    child: Text(
                      '$chapterNum',
                      style: TextStyle(
                        color: isAvailable ? color : Colors.grey,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  title: Text(
                    chapter['title'],
                    style: GoogleFonts.inter(
                      fontWeight: isAvailable ? FontWeight.bold : FontWeight.normal,
                      color: isAvailable ? AppColors.textPrimary : Colors.grey,
                    ),
                  ),
                  subtitle: isAvailable 
                      ? Text(TrilingualService.instance.getUIText('Interactive content ready'), style: TextStyle(color: Colors.green, fontSize: 12))
                      : Text(TrilingualService.instance.getUIText('Coming soon'), style: TextStyle(color: Colors.grey, fontSize: 12)),
                  trailing: !isAvailable ? Icon(Icons.lock_outline, color: Colors.grey) : null,
                ),
                if (isAvailable)
                  Padding(
                    padding: const EdgeInsets.only(left: 20, right: 20, bottom: 12),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        if (moduleId == null || !moduleId.startsWith('sci_sim:'))
                          ElevatedButton.icon(
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Colors.orange,
                              padding: const EdgeInsets.symmetric(horizontal: 12),
                            ),
                            onPressed: () {
                              if (moduleId != null) {
                                context.push('/assessment/engine/$moduleId');
                              }
                            },
                            icon: Icon(Icons.assignment, color: Colors.white, size: 20),
                            label: Text(TrilingualService.instance.getUIText('Practice'), style: TextStyle(color: Colors.white)),
                          ),
                        if (moduleId == null || !moduleId.startsWith('sci_sim:'))
                          const SizedBox(width: 8),
                        ElevatedButton.icon(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: color,
                            padding: const EdgeInsets.symmetric(horizontal: 12),
                          ),
                          onPressed: () {
                            if (moduleId != null) {
                              if (moduleId.startsWith('sci_sim:')) {
                                context.push('/learning/sci_sim_chapter/$moduleId');
                              } else {
                                context.push('/learning/engine/gold/$moduleId');
                              }
                            } else {
                              context.push('/curriculum/${widget.curriculumId}/${widget.subjectId}/chapter/${chapter['chapter_id']}');
                            }
                          },
                          icon: Icon(Icons.play_circle_fill, color: Colors.white),
                          label: Text(TrilingualService.instance.getUIText('Learn'), style: TextStyle(color: Colors.white)),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          );
        },
      ),
    );
  }

}
