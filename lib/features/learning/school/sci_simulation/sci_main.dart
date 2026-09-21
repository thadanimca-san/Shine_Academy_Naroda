export 'data/sample_chapters.dart';
export 'views/chapter_detail_view.dart';
import 'package:flutter/material.dart';
import 'data/sample_chapters.dart';
import 'models/chapter_model.dart';
import 'services/license_service.dart';
import 'views/activation_view.dart';
import 'views/chapter_detail_view.dart';
import 'views/multi_chapter_pdf_view.dart';
import 'widgets/video_promo_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../foundation/theme/brand_app_bar.dart';

void main() {
  runApp(const ScienceSimulationApp());
}

class ScienceSimulationApp extends StatelessWidget {
  const ScienceSimulationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Science Simulations 7 to 10',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const AppGate(),
      debugShowCheckedModeBanner: false,
    );
  }
}

/// Shows the one-time [ActivationView] until this device has been
/// unlocked, then hands off to the normal app content.
class AppGate extends StatefulWidget {
  final int? preSelectedGrade;
  const AppGate({super.key, this.preSelectedGrade});

  @override
  State<AppGate> createState() => _AppGateState();
}

class _AppGateState extends State<AppGate> {
  bool? _activated;

  @override
  void initState() {
    super.initState();
    LicenseService.isActivated().then((v) => setState(() => _activated = v));
  }

  @override
  Widget build(BuildContext context) {
    if (_activated == null) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }
    if (_activated == false) {
      return ActivationView(onActivated: () => setState(() => _activated = true));
    }
    return HomeDashboardView(preSelectedGrade: widget.preSelectedGrade);
  }
}

class HomeDashboardView extends StatefulWidget {
  final int? preSelectedGrade;
  const HomeDashboardView({super.key, this.preSelectedGrade});

  @override
  State<HomeDashboardView> createState() => _HomeDashboardViewState();
}

class _HomeDashboardViewState extends State<HomeDashboardView> {
  late int _selectedStandard;

  static final Map<int, List<ChapterModel>> _chaptersByStandard = {
    7: allClass7Chapters,
    8: allClass8Chapters,
    9: allClass9Chapters,
    10: allClass10Chapters,
  };

  @override
  void initState() {
    super.initState();
    _selectedStandard = widget.preSelectedGrade ?? 9;
  }

  @override
  Widget build(BuildContext context) {
    final List<ChapterModel> chapters = _chaptersByStandard[_selectedStandard] ?? [];

    return Scaffold(
      appBar: BrandAppBar(title: 'Science Hub (Class $_selectedStandard)'),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (widget.preSelectedGrade == null) ...[
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
            ],
            const VideoPromoCard(
              title: 'Learn with Videos',
              subtitle: 'Joy of Learning with Kashish — watch on YouTube',
              url: 'https://www.youtube.com/@Kashish_Thadani',
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