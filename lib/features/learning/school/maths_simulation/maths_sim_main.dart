import 'package:flutter/material.dart';
import 'data/sample_chapters.dart';
import 'models/chapter_model.dart';
import 'services/license_service.dart';
import 'views/activation_view.dart';
import 'views/chapter_detail_view.dart';
import 'views/multi_chapter_pdf_view.dart';
import 'widgets/video_promo_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:go_router/go_router.dart';
import '../../../../foundation/theme/brand_app_bar.dart';
import '../../../../core/engine/local_content_manager.dart';

void main() {
  runApp(const MathsSimulationApp());
}

class MathsSimulationApp extends StatelessWidget {
  const MathsSimulationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Maths Simulations 7 to 10',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
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
  const AppGate({super.key});

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
    return const HomeDashboardView();
  }
}

class HomeDashboardView extends StatefulWidget {
  const HomeDashboardView({super.key});

  @override
  State<HomeDashboardView> createState() => _HomeDashboardViewState();
}

class _HomeDashboardViewState extends State<HomeDashboardView> {
  int _selectedStandard = 7;

  List<Map<String, dynamic>> _dynamicClass10Chapters = [];
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _loadDynamicChapters();
  }

  Future<void> _loadDynamicChapters() async {
    setState(() => _isLoading = true);
    try {
      await LocalContentManager.instance.init();
      final data = await LocalContentManager.instance.readLocalJson('app_core/content_database/cbse_class10_maths/index.json');
      if (data != null && data is List) {
        setState(() {
          _dynamicClass10Chapters = List<Map<String, dynamic>>.from(data);
        });
      }
    } catch (e) {
      debugPrint('Error loading JSON curriculum: $e');
    }
    setState(() => _isLoading = false);
  }

  static final Map<int, List<ChapterModel>> _chaptersByStandard = {
    7: allClass7Chapters,
    8: allClass8Chapters,
    9: allClass9Chapters,
    10: [], // Handled dynamically now
  };

  @override
  Widget build(BuildContext context) {
    final List<ChapterModel> legacyChapters = _chaptersByStandard[_selectedStandard]!;
    final isDynamic = _selectedStandard == 10;

    return Scaffold(
      appBar: BrandAppBar(title: 'Maths Simulations & Assessment Hub (Class $_selectedStandard)'),
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
                  if (!isDynamic) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => MultiChapterPdfView(chapters: legacyChapters),
                      ),
                    );
                  }
                },
              ),
            ),
            const SizedBox(height: 20),
            Text(TrilingualService.instance.getUIText('Available Chapters'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Expanded(
              child: _isLoading && isDynamic
                  ? const Center(child: CircularProgressIndicator())
                  : ListView.builder(
                      itemCount: isDynamic ? _dynamicClass10Chapters.length : legacyChapters.length,
                      itemBuilder: (context, index) {
                        if (isDynamic) {
                          final chapter = _dynamicClass10Chapters[index];
                          return Card(
                            margin: const EdgeInsets.only(bottom: 12),
                            elevation: 2,
                            child: ListTile(
                              title: Text(
                                chapter['title'] ?? 'Unknown',
                                style: const TextStyle(fontWeight: FontWeight.bold),
                              ),
                              subtitle: const Text('Subject: Mathematics (Gold Standard JSON)'),
                              trailing: const Icon(Icons.chevron_right),
                              onTap: () {
                                final assetPath = 'app_core/content_database/cbse_class10_maths/${chapter['file']}';
                                context.push('/learning/engine/gold/$assetPath');
                              },
                            ),
                          );
                        } else {
                          final chapter = legacyChapters[index];
                          return Card(
                            margin: const EdgeInsets.only(bottom: 12),
                            elevation: 2,
                            child: ListTile(
                              title: Text(
                                chapter.chapterName,
                                style: const TextStyle(fontWeight: FontWeight.bold),
                              ),
                              subtitle: Text(
                                'Subject: ${chapter.subject} • ${chapter.fillInTheBlanks.length} Questions available',
                              ),
                              trailing: const Icon(Icons.chevron_right),
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
                        }
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }
}
