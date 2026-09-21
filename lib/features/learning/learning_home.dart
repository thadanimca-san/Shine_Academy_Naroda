import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/premium_card.dart';
import '../../foundation/theme/brand_app_bar.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class LearningHome extends StatefulWidget {
  const LearningHome({super.key});

  @override
  State<LearningHome> createState() => _LearningHomeState();
}

class _LearningHomeState extends State<LearningHome> with TickerProviderStateMixin {
  late TabController _tabController;
  String _selectedBoard = 'GSEB';

  final Map<String, List<Map<String, String>>> _boardClasses = {
    'GSEB': [
      {'title': 'Nursery', 'id': 'nursery'},
      {'title': 'LKG', 'id': 'lkg'},
      {'title': 'UKG', 'id': 'ukg'},
      {'title': 'Class 1', 'id': 'class1'},
      {'title': 'Class 2', 'id': 'class2'},
      {'title': 'Class 3', 'id': 'class3'},
      {'title': 'Class 4', 'id': 'class4'},
      {'title': 'Class 5', 'id': 'class5'},
      {'title': 'Class 6', 'id': 'class6'},
      {'title': 'Class 7', 'id': 'gseb_class7'},
      {'title': 'Class 8', 'id': 'gseb_class8'},
      {'title': 'Class 9', 'id': 'gseb_class9'},
      {'title': 'Class 10', 'id': 'gseb_class10'},
      {'title': 'Class 11 Science', 'id': 'class11_science'},
      {'title': 'Class 11 Commerce', 'id': 'class11_commerce'},
      {'title': 'Class 11 Arts', 'id': 'class11_arts'},
      {'title': 'Class 12 Science', 'id': 'class12_science'},
      {'title': 'Class 12 Commerce', 'id': 'gseb_class12_commerce'},
      {'title': 'Class 12 Arts', 'id': 'class12_arts'},
    ],
    'CBSE': [
      {'title': 'Class 1', 'id': 'cbse_class1'},
      {'title': 'Class 2', 'id': 'cbse_class2'},
      {'title': 'Class 3', 'id': 'cbse_class3'},
      {'title': 'Class 4', 'id': 'cbse_class4'},
      {'title': 'Class 5', 'id': 'cbse_class5'},
      {'title': 'Class 6', 'id': 'cbse_class6'},
      {'title': 'Class 7', 'id': 'cbse_class7'},
      {'title': 'Class 8', 'id': 'cbse_class8'},
      {'title': 'Class 9', 'id': 'cbse_class9'},
      {'title': 'Class 10', 'id': 'cbse_class10'},
      {'title': 'Class 11 Science', 'id': 'cbse_class11_science'},
      {'title': 'Class 11 Commerce', 'id': 'cbse_class11_commerce'},
      {'title': 'Class 12 Science', 'id': 'cbse_class12_science'},
      {'title': 'Class 12 Commerce', 'id': 'cbse_class12_commerce'},
    ],
    'Competitive': [
      {'title': 'NEET', 'id': 'neet'},
      {'title': 'JEE Main', 'id': 'jee_main'},
      {'title': 'JEE Advanced', 'id': 'jee_advanced'},
      {'title': 'UPSC', 'id': 'upsc'},
      {'title': 'CA Foundation', 'id': 'ca_foundation'},
      {'title': 'CS Executive', 'id': 'cs_executive'},
    ],
    'Special': [
      {'title': 'Speak English Confidently', 'id': 'govindsir_english'},
    ],
  };

  @override
  void initState() {
    super.initState();
    _initTabController();
  }

  void _initTabController() {
    _tabController = TabController(length: _boardClasses[_selectedBoard]!.length, vsync: this);
  }

  void _onBoardChanged(String board) {
    setState(() {
      _selectedBoard = board;
      _tabController.dispose();
      _initTabController();
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: const BrandAppBar(title: 'Curriculum Browser'),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Board Switcher
          Container(
            color: Colors.white,
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            child: SegmentedButton<String>(
              segments: [
                ButtonSegment(value: 'GSEB', label: Text(TrilingualService.instance.getUIText('GSEB'))),
                ButtonSegment(value: 'CBSE', label: Text(TrilingualService.instance.getUIText('CBSE'))),
                ButtonSegment(value: 'Competitive', label: Text(TrilingualService.instance.getUIText('Competitive'))),
                ButtonSegment(value: 'Special', label: Text(TrilingualService.instance.getUIText('Special'))),
              ],
              selected: {_selectedBoard},
              onSelectionChanged: (Set<String> newSelection) {
                _onBoardChanged(newSelection.first);
              },
              style: ButtonStyle(
                backgroundColor: WidgetStateProperty.resolveWith<Color>((Set<WidgetState> states) {
                  if (states.contains(WidgetState.selected)) {
                    return AppColors.primary;
                  }
                  return Colors.grey[200]!;
                }),
                foregroundColor: WidgetStateProperty.resolveWith<Color>((Set<WidgetState> states) {
                  if (states.contains(WidgetState.selected)) {
                    return Colors.white;
                  }
                  return Colors.black87;
                }),
              ),
            ),
          ),
          Container(
            color: Colors.white,
            child: TabBar(
              controller: _tabController,
              isScrollable: true,
              labelColor: AppColors.primary,
              unselectedLabelColor: AppColors.textSecondary,
              indicatorColor: AppColors.primary,
              indicatorWeight: 3,
              labelStyle: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16),
              tabs: _boardClasses[_selectedBoard]!.map((c) => Tab(text: c['title'])).toList(),
            ),
          ),
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: _boardClasses[_selectedBoard]!.map((c) => _buildClassTab(c['id']!, fallback: _buildSimulations())).toList(),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildClassTab(String curriculumId, {required Widget fallback}) {
    return FutureBuilder<String>(
      future: rootBundle.loadString('app_core/curriculum/$curriculumId.json'),
      builder: (context, snapshot) {
        if (snapshot.hasError) {
          // If the curriculum JSON doesn't exist yet, show the fallback UI
          return fallback;
        }
        if (!snapshot.hasData) {
          return const Center(child: CircularProgressIndicator());
        }

        try {
          final data = json.decode(snapshot.data!);
          final subjects = data['subjects'] as List;

          if (subjects.isEmpty) {
            return Center(child: Text(TrilingualService.instance.getUIText("No subjects available for this class yet.")));
          }

          return GridView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: subjects.length,
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              crossAxisSpacing: 16,
              mainAxisSpacing: 16,
              childAspectRatio: 0.9,
            ),
            itemBuilder: (context, index) {
              final sub = subjects[index];
              Color color = _getColorFromHex(sub['color'] ?? sub['color_hex']);
              IconData icon = _getIconData(sub['icon']);
              String titleText = sub['title'] ?? sub['name'] ?? 'Unknown Subject';

              return PremiumCard(
                color: Colors.white,
                onTap: () {
                  if (sub.containsKey('app_route')) {
                    context.push(sub['app_route']);
                  } else {
                    context.push('/curriculum/$curriculumId/${sub['id']}/chapters');
                  }
                },
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: color.withValues(alpha: 0.1),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(icon, color: color, size: 40),
                    ),
                    const SizedBox(height: 16),
                    Text(
                      titleText,
                      textAlign: TextAlign.center,
                      style: GoogleFonts.inter(
                        fontWeight: FontWeight.bold,
                        fontSize: 16,
                        color: AppColors.textPrimary,
                      ),
                    ),
                  ],
                ),
              );
            },
          );
        } catch (e) {
          return Center(child: Text('Error parsing curriculum: $e'));
        }
      },
    );
  }

  // Temporary Fallback UI for classes that don't have JSONs yet
  Widget _buildSimulations() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.construction, size: 64, color: Colors.grey[400]),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText("Curriculum being updated..."),
            style: GoogleFonts.inter(fontSize: 16, color: Colors.grey[600]),
          ),
        ],
      ),
    );
  }

  Color _getColorFromHex(String? hexString) {
    if (hexString == null) return Colors.blue;
    return Color(int.parse(hexString.replaceAll('0x', ''), radix: 16));
  }

  IconData _getIconData(String? iconName) {
    switch (iconName) {
      case 'science': return Icons.science;
      case 'calculate': return Icons.calculate;
      case 'language': return Icons.language;
      case 'book': return Icons.menu_book;
      case 'account_balance': return Icons.account_balance;
      case 'bar_chart': return Icons.bar_chart;
      case 'biotech': return Icons.biotech;
      default: return Icons.book;
    }
  }
}
