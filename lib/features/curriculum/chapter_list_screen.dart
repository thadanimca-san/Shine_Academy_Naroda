import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/services/activation_service.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
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
  int _selectedLevel = 0; // 0: All, 1: Level 1, 2: Level 2, 3: Level 3

  int _getChapterLevel(dynamic chapter, int index) {
    if (chapter['level'] is int) return chapter['level'] as int;
    final rawChapterNum = chapter['chapter_number'] ?? chapter['chapter_no'];
    final parsed = int.tryParse(rawChapterNum?.toString().replaceAll(RegExp(r'[^0-9]'), '') ?? '') ?? (index + 1);
    if (parsed <= 20) return 1;
    if (parsed <= 40) return 2;
    return 3;
  }

  String _getLevelBadgeLabel(int level) {
    switch (level) {
      case 1:
        return '🌱 Level 1: Beginner Foundation';
      case 2:
        return '🚀 Level 2: Everyday Fluency';
      case 3:
        return '💼 Level 3: Professional Mastery';
      default:
        return 'Level $level';
    }
  }

  Color _getLevelColor(int level) {
    switch (level) {
      case 1:
        return Colors.green.shade700;
      case 2:
        return Colors.blue.shade700;
      case 3:
        return Colors.purple.shade700;
      default:
        return Colors.blueGrey;
    }
  }

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
    final isActivated = ActivationService.isActivated;
    final bool showLevels = widget.curriculumId.contains('english') || chapters.length >= 20;

    final displayedChapters = _selectedLevel == 0
        ? chapters
        : chapters.where((c) => _getChapterLevel(c, chapters.indexOf(c)) == _selectedLevel).toList();

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(
        title: subjectName,
      ),
      body: Column(
        children: [
          if (showLevels)
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              color: Colors.white,
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: [
                    ChoiceChip(
                      label: Text(
                        '${TrilingualService.instance.getUIText('All')} (${chapters.length})',
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: _selectedLevel == 0 ? Colors.white : Colors.black87,
                        ),
                      ),
                      selected: _selectedLevel == 0,
                      selectedColor: color,
                      onSelected: (_) => setState(() => _selectedLevel = 0),
                    ),
                    const SizedBox(width: 8),
                    ChoiceChip(
                      avatar: const Icon(Icons.eco, size: 16, color: Colors.green),
                      label: Text(
                        TrilingualService.instance.getUIText('Level 1: Beginner (1–20)'),
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: _selectedLevel == 1 ? Colors.white : Colors.green.shade800,
                        ),
                      ),
                      selected: _selectedLevel == 1,
                      selectedColor: Colors.green.shade700,
                      onSelected: (_) => setState(() => _selectedLevel = 1),
                    ),
                    const SizedBox(width: 8),
                    ChoiceChip(
                      avatar: const Icon(Icons.rocket_launch, size: 16, color: Colors.blue),
                      label: Text(
                        TrilingualService.instance.getUIText('Level 2: Intermediate (21–40)'),
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: _selectedLevel == 2 ? Colors.white : Colors.blue.shade800,
                        ),
                      ),
                      selected: _selectedLevel == 2,
                      selectedColor: Colors.blue.shade700,
                      onSelected: (_) => setState(() => _selectedLevel = 2),
                    ),
                    const SizedBox(width: 8),
                    ChoiceChip(
                      avatar: const Icon(Icons.business_center, size: 16, color: Colors.purple),
                      label: Text(
                        TrilingualService.instance.getUIText('Level 3: Professional (41–63)'),
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: _selectedLevel == 3 ? Colors.white : Colors.purple.shade800,
                        ),
                      ),
                      selected: _selectedLevel == 3,
                      selectedColor: Colors.purple.shade700,
                      onSelected: (_) => setState(() => _selectedLevel = 3),
                    ),
                  ],
                ),
              ),
            ),
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(20),
              itemCount: displayedChapters.length,
              itemBuilder: (context, index) {
                final chapter = displayedChapters[index];
                final originalIndex = chapters.indexOf(chapter);
                final chapterLevel = _getChapterLevel(chapter, originalIndex);
                final moduleId = chapter['module_id'] ?? chapter['id'];
                final isAvailable = chapter['is_available'] == true || moduleId != null || chapter.containsKey('data_file');
                final rawChapterNum = chapter['chapter_number'] ?? chapter['chapter_no'];
                final chapterNum = rawChapterNum ?? (originalIndex + 1);
          
          bool isLocked = false;
          if (!isActivated) {
            // Explicit JSON override check:
            final bool? explicitFree = chapter['is_free'] ?? chapter['is_unlocked'] ?? chapter['unlocked'] ?? chapter['free'];
            final bool? explicitLocked = chapter['is_locked'] ?? chapter['locked'];

            if (explicitFree == true) {
              isLocked = false;
            } else if (explicitLocked == true) {
              isLocked = true;
            } else {
              // Default rule before activation: Chapters 1 & 2 are unlocked for every student; Chapters 3+ are locked.
              final parsedNum = int.tryParse(chapterNum.toString()) ?? (index + 1);
              if (parsedNum <= 2 || index <= 1) {
                isLocked = false;
              } else {
                isLocked = true;
              }
            }
          }
          
          final effectiveIsAvailable = isAvailable && !isLocked;

          return Card(
            elevation: isAvailable ? 2 : 0,
            color: isAvailable ? (isLocked ? Colors.orange.shade50 : Colors.white) : Colors.grey.shade100,
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12), side: isLocked ? BorderSide(color: Colors.orange.shade200, width: 1) : BorderSide.none),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ListTile(
                  contentPadding: const EdgeInsets.only(left: 20, right: 20, top: 12, bottom: 4),
                  leading: CircleAvatar(
                    backgroundColor: isAvailable ? (isLocked ? Colors.orange.withValues(alpha: 0.1) : color.withValues(alpha: 0.1)) : Colors.grey.shade300,
                    child: isLocked ? const Icon(Icons.lock, color: Colors.orange) : Text(
                      '$chapterNum',
                      style: TextStyle(
                        color: isAvailable ? color : Colors.grey,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  title: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      if (showLevels)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          margin: const EdgeInsets.only(bottom: 4),
                          decoration: BoxDecoration(
                            color: _getLevelColor(chapterLevel).withValues(alpha: 0.1),
                            borderRadius: BorderRadius.circular(6),
                            border: Border.all(color: _getLevelColor(chapterLevel).withValues(alpha: 0.3)),
                          ),
                          child: Text(
                            TrilingualService.instance.getUIText(_getLevelBadgeLabel(chapterLevel)),
                            style: TextStyle(
                              fontSize: 10,
                              fontWeight: FontWeight.bold,
                              color: _getLevelColor(chapterLevel),
                            ),
                          ),
                        ),
                      Text(
                        chapter['title'],
                        style: GoogleFonts.inter(
                          fontWeight: isAvailable ? FontWeight.bold : FontWeight.normal,
                          color: isAvailable ? AppColors.textPrimary : Colors.grey,
                        ),
                      ),
                    ],
                  ),
                  subtitle: isLocked 
                      ? Text(TrilingualService.instance.getUIText('Premium Content - Requires Activation'), style: TextStyle(color: Colors.orange.shade800, fontSize: 12, fontWeight: FontWeight.bold))
                      : (isAvailable 
                          ? Text(TrilingualService.instance.getUIText('Interactive content ready'), style: TextStyle(color: Colors.green, fontSize: 12))
                          : Text(TrilingualService.instance.getUIText('Coming soon'), style: TextStyle(color: Colors.grey, fontSize: 12))),
                  trailing: !isAvailable ? const Icon(Icons.hourglass_empty, color: Colors.grey) : (isLocked ? const Icon(Icons.lock, color: Colors.orange) : null),
                ),
                if (isLocked && isAvailable)
                  Padding(
                    padding: const EdgeInsets.only(left: 20, right: 20, bottom: 12),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        ElevatedButton.icon(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: Colors.orange,
                            padding: const EdgeInsets.symmetric(horizontal: 16),
                          ),
                          onPressed: () {
                            context.push('/activate');
                          },
                          icon: const Icon(Icons.vpn_key, color: Colors.white, size: 20),
                          label: Text(TrilingualService.instance.getUIText('Activate to Unlock'), style: const TextStyle(color: Colors.white)),
                        ),
                      ],
                    ),
                  )
                else if (effectiveIsAvailable)
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
                              if (moduleId != null) _choosePracticeMode(context, moduleId);
                            },
                            icon: const Icon(Icons.assignment, color: Colors.white, size: 20),
                            label: Text(TrilingualService.instance.getUIText('Practice'), style: const TextStyle(color: Colors.white)),
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
                          icon: const Icon(Icons.play_circle_fill, color: Colors.white),
                          label: Text(TrilingualService.instance.getUIText('Learn'), style: const TextStyle(color: Colors.white)),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          );
        },
      ),
    ),
  ],
),
);
}


  /// Practice opens as a game (learn from every answer) or a timed exam.
  void _choosePracticeMode(BuildContext context, String moduleId) {
    final ui = TrilingualService.instance.getUIText;
    showModalBottomSheet<void>(
      context: context,
      showDragHandle: true,
      builder: (sheetContext) => SafeArea(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              leading: const Icon(Icons.sports_esports, color: Colors.deepPurple),
              title: Text(ui('Quiz Game')),
              subtitle: Text(ui('Learn from every answer, earn XP')),
              onTap: () {
                Navigator.pop(sheetContext);
                context.push('/assessment/game/$moduleId');
              },
            ),
            ListTile(
              leading: const Icon(Icons.timer, color: Colors.orange),
              title: Text(ui('Exam Mode')),
              subtitle: Text(ui('Timed, like the board exam')),
              onTap: () {
                Navigator.pop(sheetContext);
                context.push('/assessment/engine/$moduleId');
              },
            ),
          ],
        ),
      ),
    );
  }
}
