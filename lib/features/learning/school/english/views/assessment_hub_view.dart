import 'package:flutter/material.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../data/sample_chapters.dart';
import '../models/chapter_model.dart';
import '../theme/app_theme.dart';
import 'chapter_detail_view.dart';
import 'multi_chapter_pdf_view.dart';
import '../widgets/video_promo_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// The original fill-in-the-blank / multi-chapter PDF & Answer Key builder,
/// kept unchanged in behavior but moved out of main.dart and folded into
/// the new home screen as its own tile alongside Dictionary, Phonetics,
/// Practice, Question Papers, and Teacher Dashboard.
class AssessmentHubView extends StatefulWidget {
  const AssessmentHubView({super.key});

  @override
  State<AssessmentHubView> createState() => _AssessmentHubViewState();
}

class _AssessmentHubViewState extends State<AssessmentHubView> {
  int _selectedStandard = 7;

  static final Map<int, List<ChapterModel>> _chaptersByStandard = {
    7: allClass7Chapters,
    8: allClass8Chapters,
    9: allClass9Chapters,
    10: allClass10Chapters,
  };

  @override
  Widget build(BuildContext context) {
    final List<ChapterModel> chapters = _chaptersByStandard[_selectedStandard]!;

    return Scaffold(
      appBar: BrandAppBar(title: 'Assessment Hub — Class $_selectedStandard'),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Text(TrilingualService.instance.getUIText('Class:'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
                const SizedBox(width: 12),
                ToggleButtons(
                  isSelected: _chaptersByStandard.keys.map((s) => s == _selectedStandard).toList(),
                  onPressed: (i) => setState(() => _selectedStandard = _chaptersByStandard.keys.elementAt(i)),
                  borderRadius: BorderRadius.circular(8),
                  selectedColor: Colors.white,
                  fillColor: AppColors.saffron,
                  constraints: const BoxConstraints(minHeight: 36, minWidth: 52),
                  children: _chaptersByStandard.keys.map((s) => Text('$s')).toList(),
                ),
              ],
            ),
            const SizedBox(height: 16),
            const VideoPromoCard(
              title: 'Learn with Videos',
              subtitle: 'Joy of Learning with Kashish — watch on YouTube',
              url: 'https://www.youtube.com/@Kashish_Thadani',
            ),
            const SizedBox(height: 16),
            // Multi-Chapter Assessment Builder Hub Button
            Card(
              elevation: 3,
              color: AppColors.tealTint,
              child: ListTile(
                leading: Icon(Icons.library_books, color: AppColors.saffron, size: 36),
                title: Text(TrilingualService.instance.getUIText('Multi-Chapter Assessment Builder'),
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                ),
                subtitle: Text(TrilingualService.instance.getUIText('Select multiple chapters to generate combined QP & Answer Key PDFs.')),
                trailing: Icon(Icons.arrow_forward_ios),
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => MultiChapterPdfView(chapters: chapters),
                    ),
                  );
                },
              ),
            ),
            const SizedBox(height: 20),
            Text(TrilingualService.instance.getUIText('Available Chapters'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Expanded(
              child: ListView.builder(
                itemCount: chapters.length,
                itemBuilder: (context, index) {
                  final chapter = chapters[index];
                  return Card(
                    margin: const EdgeInsets.only(bottom: 12),
                    elevation: 2,
                    child: ListTile(
                      title: Text(
                        chapter.chapterName,
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      subtitle: Text(
                        'Subject: ${chapter.subject} • ${chapter.fillInTheBlanks.length} Questions available',
                      ),
                      trailing: Icon(Icons.chevron_right),
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => ChapterDetailView(chapter: chapter),
                          ),
                        );
                      },
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
