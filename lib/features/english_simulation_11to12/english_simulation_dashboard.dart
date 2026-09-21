import 'package:flutter/material.dart';
import 'data/sample_chapters.dart';
import 'models/chapter_model.dart';
import 'services/license_service.dart';
import 'views/activation_view.dart';
import 'views/chapter_detail_view.dart';
import 'views/multi_chapter_pdf_view.dart';
import 'widgets/website_promo_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../foundation/theme/brand_app_bar.dart';

const Color kNavy = Color(0xFF0D2A4A);

// Dashboard for English Simulation

class HomeDashboardView extends StatefulWidget {
  const HomeDashboardView({super.key});

  @override
  State<HomeDashboardView> createState() => _HomeDashboardViewState();
}

class _HomeDashboardViewState extends State<HomeDashboardView> {
  int _selectedStandard = 11;

  static final Map<int, List<ChapterModel>> _chaptersByStandard = {
    11: allClass11Chapters,
    12: allClass12Chapters,
  };

  @override
  Widget build(BuildContext context) {
    final List<ChapterModel> chapters = _chaptersByStandard[_selectedStandard]!;

    return Scaffold(
      appBar: BrandAppBar(title: 'English Simulations & Assessment Hub (Class $_selectedStandard)'),
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
                  fillColor: Colors.indigo,
                  constraints: const BoxConstraints(minHeight: 36, minWidth: 52),
                  children: _chaptersByStandard.keys.map((s) => Text('$s')).toList(),
                ),
              ],
            ),
            const SizedBox(height: 16),
            const WebsitePromoCard(
              title: 'Visit Shine Academy Naroda',
              subtitle: 'More resources and classes — visit our website',
              url: 'https://sites.google.com/view/shine-academy-naroda/home',
            ),
            const SizedBox(height: 16),
            // Multi-Chapter Assessment Builder Hub Button
            Card(
              elevation: 3,
              color: Colors.indigo.withValues(alpha: 0.06),
              child: ListTile(
                leading: Icon(Icons.library_books, color: Colors.indigo, size: 36),
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
