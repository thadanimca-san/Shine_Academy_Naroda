import 'package:flutter/material.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import '../models/chapter_model.dart';
import '../services/pdf_generator_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class MultiChapterPdfView extends StatefulWidget {
  final List<ChapterModel> chapters;

  const MultiChapterPdfView({Key? key, required this.chapters}) : super(key: key);

  @override
  State<MultiChapterPdfView> createState() => _MultiChapterPdfViewState();
}

class _MultiChapterPdfViewState extends State<MultiChapterPdfView> {
  // Track which chapters are selected by their chapterId
  final Set<String> _selectedChapterIds = {};

  @override
  void initState() {
    super.initState();
    // By default, select all chapters initially
    for (var chapter in widget.chapters) {
      _selectedChapterIds.add(chapter.chapterId);
    }
  }

  @override
  Widget build(BuildContext context) {
    final selectedChapters = widget.chapters
        .where((c) => _selectedChapterIds.contains(c.chapterId))
        .toList();

    int totalQuestions = selectedChapters.fold(
      0,
      (sum, chapter) => sum + chapter.fillInTheBlanks.length,
    );

    final standard = widget.chapters.isNotEmpty ? widget.chapters.first.standard : null;
    final allSelected = _selectedChapterIds.length == widget.chapters.length;

    return Scaffold(
      appBar: BrandAppBar(
        title: 'Multi-Chapter Assessment Builder${standard != null ? ' (Class $standard)' : ''}',
        actions: [
          TextButton.icon(
            onPressed: () {
              setState(() {
                if (allSelected) {
                  _selectedChapterIds.clear();
                } else {
                  _selectedChapterIds
                    ..clear()
                    ..addAll(widget.chapters.map((c) => c.chapterId));
                }
              });
            },
            icon: Icon(allSelected ? Icons.deselect : Icons.select_all, color: Colors.white),
            label: Text(allSelected ? 'Deselect All' : 'Select All', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
      body: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            color: Colors.blue[50],
            child: Text(TrilingualService.instance.getUIText('Select multiple chapters below to combine their fill-in-the-blanks into a unified question paper and answer key PDF set.'),
              style: TextStyle(fontSize: 13, color: Theme.of(context).colorScheme.onSurface),
              textAlign: TextAlign.center,
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: widget.chapters.length,
              itemBuilder: (context, index) {
                final chapter = widget.chapters[index];
                final isSelected = _selectedChapterIds.contains(chapter.chapterId);

                return CheckboxListTile(
                  title: Text(
                    chapter.chapterName,
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  subtitle: Text(
                    'Subject: ${chapter.subject} • ${chapter.fillInTheBlanks.length} Questions available',
                  ),
                  value: isSelected,
                  onChanged: (bool? value) {
                    setState(() {
                      if (value == true) {
                        _selectedChapterIds.add(chapter.chapterId);
                      } else {
                        _selectedChapterIds.remove(chapter.chapterId);
                      }
                    });
                  },
                );
              },
            ),
          ),
          Container(
            padding: const EdgeInsets.all(16.0),
            decoration: BoxDecoration(
              color: Colors.white,
              boxShadow: [
                BoxShadow(
                  color: Colors.grey.withValues(alpha: 0.3),
                  blurRadius: 5,
                  offset: const Offset(0, -3),
                ),
              ],
            ),
            child: Row(
              children: [
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: selectedChapters.isEmpty
                        ? null
                        : () async {
                            await PdfGeneratorService.generateAndOpenQuestionPaper(
                              selectedChapters,
                            );
                          },
                    icon: Icon(Icons.picture_as_pdf),
                    label: Text('Generate QP ($totalQuestions Qs)'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue[800],
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: selectedChapters.isEmpty
                        ? null
                        : () async {
                            await PdfGeneratorService.generateAndOpenAnswerKey(
                              selectedChapters,
                            );
                          },
                    icon: Icon(Icons.task_alt),
                    label: Text(TrilingualService.instance.getUIText('Generate Answer Key')),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green[700],
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}