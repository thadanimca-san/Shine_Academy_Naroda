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

  late Map<String, List<Map<String, String>>> _boardClasses;

  @override
  void initState() {
    super.initState();
    _initializeBoardClasses();
    _initTabController();
  }

  void _initializeBoardClasses() {
    final flavor = appFlavor ?? 'default';

    Map<String, List<Map<String, String>>> fullCurriculum = {
      'Core Concepts': [
        {'title': 'Class 3', 'id': 'ncert_class3'},
        {'title': 'Class 4', 'id': 'ncert_class4'},
        {'title': 'Class 5', 'id': 'ncert_class5'},
        {'title': 'Class 6', 'id': 'ncert_class6'},
        {'title': 'Class 7', 'id': 'ncert_class7'},
        {'title': 'Class 8', 'id': 'ncert_class8'},
        {'title': 'Class 9', 'id': 'ncert_class9'},
        {'title': 'Class 10', 'id': 'ncert_class10'},
      ],
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

    if (flavor == 'primary') {
      _boardClasses = {
        'Core Concepts': fullCurriculum['Core Concepts']!.where((c) => int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) != null && int.parse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) <= 4).toList(),
        'GSEB': fullCurriculum['GSEB']!.where((c) => c['title']!.contains('Nursery') || c['title']!.contains('KG') || (int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) != null && int.parse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) <= 4)).toList(),
        'CBSE': fullCurriculum['CBSE']!.where((c) => int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) != null && int.parse(c['title']!.replaceAll(RegExp(r'[^0-9]'), '')) <= 4).toList(),
      };
      _selectedBoard = 'GSEB';
    } else if (flavor == 'middle' || flavor == 'junior') {
      _boardClasses = {
        'Core Concepts': fullCurriculum['Core Concepts']!.where((c) {
          final val = int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), ''));
          return val != null && (flavor == 'junior' ? val <= 8 : (val >= 5 && val <= 8));
        }).toList(),
        'GSEB': fullCurriculum['GSEB']!.where((c) {
          final val = int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), ''));
          if (flavor == 'junior' && (c['title']!.contains('Nursery') || c['title']!.contains('KG'))) return true;
          return val != null && (flavor == 'junior' ? val <= 8 : (val >= 5 && val <= 8));
        }).toList(),
        'CBSE': fullCurriculum['CBSE']!.where((c) {
          final val = int.tryParse(c['title']!.replaceAll(RegExp(r'[^0-9]'), ''));
          return val != null && (flavor == 'junior' ? val <= 8 : (val >= 5 && val <= 8));
        }).toList(),
      };
      _selectedBoard = 'GSEB';
    } else if (flavor == 'highschool') {
      _boardClasses = {
        'Core Concepts': fullCurriculum['Core Concepts']!.where((c) => c['title'] == 'Class 9' || c['title'] == 'Class 10').toList(),
        'GSEB': fullCurriculum['GSEB']!.where((c) => c['title'] == 'Class 9' || c['title'] == 'Class 10').toList(),
        'CBSE': fullCurriculum['CBSE']!.where((c) => c['title'] == 'Class 9' || c['title'] == 'Class 10').toList(),
      };
      _selectedBoard = 'Core Concepts';
    } else if (flavor == 'commerce') {
      _boardClasses = {
        'GSEB': fullCurriculum['GSEB']!.where((c) => c['title']!.contains('Commerce')).toList(),
        'CBSE': fullCurriculum['CBSE']!.where((c) => c['title']!.contains('Commerce')).toList(),
        'Competitive': fullCurriculum['Competitive']!.where((c) => c['title']!.contains('CA ') || c['title']!.contains('CS ')).toList(),
      };
      _selectedBoard = 'GSEB';
    } else if (flavor == 'achievers') {
      _boardClasses = {
        'GSEB': fullCurriculum['GSEB']!.where((c) => c['title']!.contains('Science')).toList(),
        'CBSE': fullCurriculum['CBSE']!.where((c) => c['title']!.contains('Science')).toList(),
        'Competitive': fullCurriculum['Competitive']!.where((c) => c['title']!.contains('NEET') || c['title']!.contains('JEE')).toList(),
      };
      _selectedBoard = 'GSEB';
    } else if (flavor == 'skillup') {
      _boardClasses = {
        'Special': fullCurriculum['Special']!,
      };
      _selectedBoard = 'Special';
    } else {
      _boardClasses = fullCurriculum;
    }
  }

  void _initTabController({int initialIndex = 0}) {
    int length = _boardClasses[_selectedBoard]?.length ?? 0;
    if (initialIndex >= length) initialIndex = 0;
    _tabController = TabController(initialIndex: initialIndex, length: length, vsync: this);
  }

  void _onBoardChanged(String board) {
    if (!_boardClasses.containsKey(board)) return;

    String currentTitle = '';
    if (_boardClasses[_selectedBoard] != null && _boardClasses[_selectedBoard]!.isNotEmpty) {
      if (_tabController.index >= 0 && _tabController.index < _boardClasses[_selectedBoard]!.length) {
        currentTitle = _boardClasses[_selectedBoard]![_tabController.index]['title'] ?? '';
      }
    }

    setState(() {
      _selectedBoard = board;
      
      int newIndex = 0;
      if (currentTitle.isNotEmpty && _boardClasses[_selectedBoard] != null) {
        final classes = _boardClasses[_selectedBoard]!;
        for (int i = 0; i < classes.length; i++) {
          if (classes[i]['title'] == currentTitle) {
            newIndex = i;
            break;
          }
        }
      }
      
      _tabController.dispose();
      _initTabController(initialIndex: newIndex);
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
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: SegmentedButton<String>(
                segments: _boardClasses.keys.map((boardKey) {
                  return ButtonSegment(value: boardKey, label: Text(TrilingualService.instance.getUIText(boardKey)));
                }).toList(),
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
              tabs: (_boardClasses[_selectedBoard] ?? []).map((c) => Tab(text: c['title'])).toList(),
            ),
          ),
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: (_boardClasses[_selectedBoard] ?? []).map((c) => _buildClassTab(c['id']!, fallback: _buildSimulations())).toList(),
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
                  if (_selectedBoard == 'Core Concepts') {
                    context.push('/core_concepts_search/$curriculumId/${sub['id']}');
                  } else if (sub.containsKey('app_route')) {
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
