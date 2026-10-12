import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../core/engine/assessment_engine.dart';
import '../../../core/services/activation_service.dart';
import '../../../foundation/theme/app_typography.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import '../../shared/widgets/activation_dialog.dart';
import '../../shared/widgets/activation_gate.dart';
import 'question_selection_screen.dart';
import 'package:flutter/services.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class AssessmentDashboardScreen extends StatefulWidget {
  const AssessmentDashboardScreen({super.key});

  @override
  State<AssessmentDashboardScreen> createState() => _AssessmentDashboardScreenState();
}

class _AssessmentDashboardScreenState extends State<AssessmentDashboardScreen> {
  String selectedBoard = "GSEB";
  String selectedClass = "class8";
  int questionCount = 20;
  
  bool isGenerating = false;
  bool isLoadingCurriculum = false;
  
  String generationMode = 'preset'; // 'preset' or 'manual'

  int blueprintSecA = 16;
  int blueprintSecB = 8;
  int blueprintSecC = 6;
  int blueprintSecD = 5;

  late List<String> boards;
  late List<String> classes;

  String _formatClassName(String rawClass) {
    String formatted = rawClass.replaceAll('class', 'Class ').replaceAll('_', ' ');
    // Capitalize words
    return formatted.split(' ').map((word) {
      if (word.isEmpty) return '';
      return word[0].toUpperCase() + word.substring(1).toLowerCase();
    }).join(' ');
  }

  List<CurriculumSubject> availableSubjects = [];
  CurriculumSubject? selectedSubject;
  Set<String> selectedModuleIds = {};
  String _selectedSkillupTrack = 'level1';

  @override
  void initState() {
    super.initState();
    _initializeClassesByFlavor();
    _loadCurriculum();
  }

  void _initializeClassesByFlavor() {
    final flavor = appFlavor ?? 'default';

    if (flavor == 'skillup') {
      boards = ["Govind Sir Academy"];
      classes = ["govindsir_english"];
      selectedClass = "govindsir_english";
      selectedBoard = "Govind Sir Academy";
    } else if (flavor == 'commerce') {
      boards = ["GSEB", "CBSE"];
      selectedBoard = "GSEB";
      classes = ["class11_commerce", "class12_commerce"];
      if (!classes.contains(selectedClass)) selectedClass = "class11_commerce";
    } else if (flavor == 'achievers') {
      boards = ["GSEB", "CBSE", "Core Concepts"];
      selectedBoard = "GSEB";
      classes = ["class11_science", "class12_science"];
      if (!classes.contains(selectedClass)) selectedClass = "class11_science";
    } else if (flavor == 'primary') {
      boards = ["Core Concepts", "GSEB", "CBSE"];
      classes = ["class1", "class2", "class3", "class4"];
      if (!classes.contains(selectedClass)) selectedClass = "class4";
    } else if (flavor == 'middle') {
      boards = ["Core Concepts", "GSEB", "CBSE"];
      classes = ["class5", "class6", "class7", "class8"];
      if (!classes.contains(selectedClass)) selectedClass = "class8";
    } else if (flavor == 'junior') {
      boards = ["Core Concepts", "GSEB", "CBSE"];
      classes = ["class1", "class2", "class3", "class4", "class5", "class6", "class7", "class8"];
      if (!classes.contains(selectedClass)) selectedClass = "class8";
    } else if (flavor == 'highschool') {
      boards = ["Core Concepts", "GSEB", "CBSE"];
      classes = ["class9", "class10"];
      if (!classes.contains(selectedClass)) selectedClass = "class10";
    } else {
      boards = ["Core Concepts", "GSEB", "CBSE"];
      classes = [
        "class1", "class2", "class3", "class4", "class5", "class6",
        "class7", "class8", "class9", "class10",
        "class11", "class11_commerce", "class11_science", "class11_arts",
        "class12_commerce", "class12_science", "class12_arts"
      ];
    }
  }

  Future<void> _loadCurriculum() async {
    setState(() {
      isLoadingCurriculum = true;
      availableSubjects.clear();
      selectedSubject = null;
      selectedModuleIds.clear();
    });

    final flavor = appFlavor ?? 'default';
    final curriculumId = flavor == 'skillup'
        ? "govindsir_english"
        : "${(selectedBoard == "Core Concepts" || selectedBoard == "NCERT") ? "ncert" : selectedBoard.toLowerCase()}_$selectedClass";
    final subjects = await AssessmentEngine.instance.fetchCurriculumSubjects(curriculumId);
    
    setState(() {
      availableSubjects = subjects;
      if (subjects.isNotEmpty) {
        selectedSubject = subjects.first;
        if (flavor == 'skillup') {
          _applySkillupTrack(_selectedSkillupTrack);
        } else {
          // Select all chapters by default
          selectedModuleIds.addAll(selectedSubject!.chapters.map((c) => c.moduleId));
        }
      }
      isLoadingCurriculum = false;
    });
  }

  void _applySkillupTrack(String track) {
    _selectedSkillupTrack = track;
    selectedModuleIds.clear();
    final bool isActivated = ActivationService.isActivated;

    if (track == 'free' || (!isActivated && track == 'level1')) {
      selectedModuleIds.add('govindsir_english_ch1');
      selectedModuleIds.add('govindsir_english_ch2');
    } else if (track == 'level1') {
      for (int i = 1; i <= 20; i++) {
        selectedModuleIds.add('govindsir_english_ch$i');
      }
    } else if (track == 'level2') {
      for (int i = 21; i <= 40; i++) {
        selectedModuleIds.add('govindsir_english_ch$i');
      }
    } else if (track == 'level3') {
      for (int i = 41; i <= 63; i++) {
        selectedModuleIds.add('govindsir_english_ch$i');
      }
    } else if (track == 'all') {
      for (int i = 1; i <= 63; i++) {
        selectedModuleIds.add('govindsir_english_ch$i');
      }
    }
  }

  void _generatePaper() async {
    final flavor = appFlavor ?? 'default';
    if (flavor == 'skillup' && !ActivationService.isActivated) {
      final hasLocked = selectedModuleIds.any((id) {
        final match = RegExp(r'govindsir_english_ch(\d+)').firstMatch(id);
        if (match != null) {
          final num = int.tryParse(match.group(1)!) ?? 1;
          return num > 2;
        }
        return false;
      });
      if (hasLocked) {
        ActivationDialog.show(context, onActivated: () => setState(() {}));
        return;
      }
    }

    if (selectedModuleIds.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText("Please select at least one chapter!"))));
      return;
    }

    setState(() => isGenerating = true);

    List<AssessmentQuestion> allAvailableQuestions = [];
    final activeTypes = ['quiz', 'fill_blank', 'true_false', 'short_note', 'descriptive', 'practice_question', 'challenge_question'];

    for (String moduleId in selectedModuleIds) {
      final q = await AssessmentEngine.instance.extractQuestionsForModule(
        moduleId,
        activeTypes,
      );
      allAvailableQuestions.addAll(q);
    }

    if (allAvailableQuestions.isEmpty) {
      setState(() => isGenerating = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText("No questions found for the selected chapters and types."))));
      }
      return;
    }

    List<AssessmentQuestion> initialQuestions = [];

    if (flavor == 'skillup') {
      if (generationMode == 'preset') {
        allAvailableQuestions.shuffle();
        initialQuestions = allAvailableQuestions.take(questionCount).toList();
      } else {
        initialQuestions = List.from(allAvailableQuestions);
      }
    } else {
      // Subjects with an official board blueprint get a paper in the exact board pattern.
      final blueprintPaper = generationMode == 'preset' && selectedSubject != null
          ? await AssessmentEngine.instance.generateFromBlueprint(selectedModuleIds.toList(), selectedSubject!.id)
          : null;
      if (blueprintPaper != null && blueprintPaper.items.isNotEmpty) {
        initialQuestions = blueprintPaper.items;
        if (!blueprintPaper.isComplete && mounted) {
          final missing = blueprintPaper.shortfalls.map((s) => 'Section ${s.section}: ${s.found}/${s.wanted}').join(', ');
          ScaffoldMessenger.of(context).showSnackBar(SnackBar(
            duration: const Duration(seconds: 8),
            content: Text('${TrilingualService.instance.getUIText('Not enough questions yet for a full board paper')} '
                '(${blueprintPaper.totalMarks}/${blueprintPaper.blueprint.totalMarks} marks). $missing'),
          ));
        }
      } else if (generationMode == 'preset') {
        initialQuestions = await AssessmentEngine.instance.generateBoardPatternPaper(
          selectedModuleIds.toList(),
          targetSecA: blueprintSecA,
          targetSecB: blueprintSecB,
          targetSecC: blueprintSecC,
          targetSecD: blueprintSecD,
        );
        if (initialQuestions.isEmpty) {
          // Fallback if board pattern gives nothing (e.g., no suitable types)
          initialQuestions = List.from(allAvailableQuestions);
        }
      } else {
        initialQuestions = List.from(allAvailableQuestions);
      }
    }

    setState(() => isGenerating = false);
    if (mounted) {
      final screenTitle = (flavor == 'skillup')
          ? "${selectedSubject?.title ?? 'Govind Sir Academy'} - English Fluency Test"
          : "$selectedBoard ${_formatClassName(selectedClass)} - ${selectedSubject?.title ?? 'Test'}";
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => QuestionSelectionScreen(
            allQuestionsPool: allAvailableQuestions,
            initialSelectedQuestions: initialQuestions,
            title: screenTitle,
            isManualMode: generationMode == 'manual',
          ),
        ),
      );
    }
  }

  Widget _buildSkillupLeftColumn() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          TrilingualService.instance.getUIText("1. Fluency Track & Test Setup"),
          style: GoogleFonts.poppins(
            fontSize: 18,
            fontWeight: FontWeight.bold,
            color: Colors.blue[800],
          ),
        ),
        const SizedBox(height: 8),
        Text(
          TrilingualService.instance.getUIText("Select your fluency stage or custom practice:"),
          style: GoogleFonts.inter(
            fontSize: 13,
            color: Colors.grey[700],
          ),
        ),
        const SizedBox(height: 16),
        _buildSkillupTrackCard(
          trackId: 'free',
          title: TrilingualService.instance.getUIText("Free Trial: Lessons 1 & 2 (100% Free)"),
          subtitle: TrilingualService.instance.getUIText("Why Learn English? & The Alphabet and Sounds"),
          icon: Icons.check_circle_outline,
          color: const Color(0xFF10B981),
          isFree: true,
        ),
        _buildSkillupTrackCard(
          trackId: 'level1',
          title: TrilingualService.instance.getUIText("Level 1: Foundations (Lessons 1–20)"),
          subtitle: TrilingualService.instance.getUIText("Magic of Courtesy, Helping Verbs, Basic Daily Phrases"),
          icon: Icons.looks_one_rounded,
          color: const Color(0xFF10B981),
          isFree: false,
        ),
        _buildSkillupTrackCard(
          trackId: 'level2',
          title: TrilingualService.instance.getUIText("Level 2: Conversations (Lessons 21–40)"),
          subtitle: TrilingualService.instance.getUIText("Tenses in Action, Social Dialogues, Common Idioms"),
          icon: Icons.looks_two_rounded,
          color: const Color(0xFFF59E0B),
          isFree: false,
        ),
        _buildSkillupTrackCard(
          trackId: 'level3',
          title: TrilingualService.instance.getUIText("Level 3: Professional (Lessons 41–63)"),
          subtitle: TrilingualService.instance.getUIText("Workplace Speaking, Public Eloquence, Complex Phrases"),
          icon: Icons.looks_3_rounded,
          color: const Color(0xFF6366F1),
          isFree: false,
        ),
        _buildSkillupTrackCard(
          trackId: 'all',
          title: TrilingualService.instance.getUIText("Full Course Grand Mock (All 63 Lessons)"),
          subtitle: TrilingualService.instance.getUIText("Comprehensive English test across all Govind Sir chapters"),
          icon: Icons.military_tech_rounded,
          color: const Color(0xFFD97706),
          isFree: false,
        ),
        _buildSkillupTrackCard(
          trackId: 'custom',
          title: TrilingualService.instance.getUIText("Custom Practice (Pick Lessons)"),
          subtitle: TrilingualService.instance.getUIText("Hand-pick any lessons from the right panel"),
          icon: Icons.tune_rounded,
          color: const Color(0xFF0284C7),
          isFree: true,
        ),
        const SizedBox(height: 16),
        DropdownButtonFormField<int>(
          value: questionCount,
          decoration: InputDecoration(
            labelText: TrilingualService.instance.getUIText("Test Length"),
            labelStyle: const TextStyle(fontSize: 14),
            border: const OutlineInputBorder(),
          ),
          items: [
            DropdownMenuItem(
              value: 10,
              child: Text(TrilingualService.instance.getUIText("10 Questions (Quick 10-Min Drill)")),
            ),
            DropdownMenuItem(
              value: 20,
              child: Text(TrilingualService.instance.getUIText("20 Questions (Standard Practice)")),
            ),
            DropdownMenuItem(
              value: 30,
              child: Text(TrilingualService.instance.getUIText("30 Questions (Thorough Test)")),
            ),
            DropdownMenuItem(
              value: 50,
              child: Text(TrilingualService.instance.getUIText("50 Questions (Comprehensive Mock)")),
            ),
          ],
          onChanged: (val) {
            if (val != null) setState(() => questionCount = val);
          },
        ),
        const SizedBox(height: 16),
        DropdownButtonFormField<String>(
          value: generationMode,
          decoration: InputDecoration(
            labelText: TrilingualService.instance.getUIText("Test Mode"),
            labelStyle: const TextStyle(fontSize: 14),
            border: const OutlineInputBorder(),
          ),
          items: [
            DropdownMenuItem(
              value: 'preset',
              child: Text(TrilingualService.instance.getUIText("Preset Test (Balanced Random)")),
            ),
            DropdownMenuItem(
              value: 'manual',
              child: Text(TrilingualService.instance.getUIText("Manual Selection (Hand-pick Questions)")),
            ),
          ],
          onChanged: (val) {
            if (val != null) setState(() => generationMode = val);
          },
        ),
      ],
    );
  }

  Widget _buildSkillupTrackCard({
    required String trackId,
    required String title,
    required String subtitle,
    required IconData icon,
    required Color color,
    bool isFree = true,
  }) {
    final isSelected = _selectedSkillupTrack == trackId;
    final cardWidget = InkWell(
      onTap: () {
        if (!isFree && !ActivationService.isActivated) {
          ActivationDialog.show(context, onActivated: () => setState(() {}));
          return;
        }
        setState(() {
          _applySkillupTrack(trackId);
        });
      },
      borderRadius: BorderRadius.circular(10),
      child: Container(
        margin: const EdgeInsets.only(bottom: 8),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          color: isSelected ? color.withValues(alpha: 0.08) : Colors.white,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(
            color: isSelected ? color : Colors.grey.shade300,
            width: isSelected ? 2 : 1,
          ),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: color.withValues(alpha: 0.14),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: color, size: 20),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: GoogleFonts.poppins(
                      fontSize: 13 * AppTypography.scaleFactor(context),
                      fontWeight: FontWeight.w600,
                      color: isSelected ? color : Colors.black87,
                    ),
                  ),
                  Text(
                    subtitle,
                    style: GoogleFonts.inter(
                      fontSize: 11 * AppTypography.scaleFactor(context),
                      color: Colors.grey.shade600,
                    ),
                  ),
                ],
              ),
            ),
            if (isSelected)
              Icon(Icons.check_circle, color: color, size: 20),
          ],
        ),
      ),
    );

    if (isFree || ActivationService.isActivated) return cardWidget;

    return ActivationGate(
      isFree: false,
      onActivated: () => setState(() {}),
      child: cardWidget,
    );
  }

  Widget _buildDefaultLeftColumn() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          TrilingualService.instance.getUIText("1. Curriculum Setup"),
          style: GoogleFonts.poppins(
            fontSize: 18,
            fontWeight: FontWeight.bold,
            color: Colors.blue[800],
          ),
        ),
        const SizedBox(height: 16),
        DropdownButtonFormField<String>(
          value: selectedBoard,
          decoration: InputDecoration(
            labelText: TrilingualService.instance.getUIText("Select Board"),
            labelStyle: const TextStyle(fontSize: 14),
            border: const OutlineInputBorder(),
          ),
          style: TextStyle(
            fontSize: 16,
            color: Theme.of(context).colorScheme.onSurface,
          ),
          items: boards
              .map((b) => DropdownMenuItem(value: b, child: Text(b)))
              .toList(),
          onChanged: (val) {
            setState(() => selectedBoard = val!);
            _loadCurriculum();
          },
        ),
        const SizedBox(height: 16),
        DropdownButtonFormField<String>(
          value: selectedClass,
          decoration: InputDecoration(
            labelText: TrilingualService.instance.getUIText("Select Class"),
            labelStyle: const TextStyle(fontSize: 14),
            border: const OutlineInputBorder(),
          ),
          style: TextStyle(
            fontSize: 16,
            color: Theme.of(context).colorScheme.onSurface,
          ),
          items: classes
              .map((c) => DropdownMenuItem(
                    value: c,
                    child: Text(_formatClassName(c)),
                  ))
              .toList(),
          onChanged: (val) {
            setState(() => selectedClass = val!);
            _loadCurriculum();
          },
        ),
        const SizedBox(height: 16),
        DropdownButtonFormField<String>(
          value: generationMode,
          decoration: InputDecoration(
            labelText: TrilingualService.instance.getUIText("Generation Mode"),
            labelStyle: const TextStyle(fontSize: 14),
            border: const OutlineInputBorder(),
          ),
          style: TextStyle(
            fontSize: 16,
            color: Theme.of(context).colorScheme.onSurface,
          ),
          items: [
            DropdownMenuItem(
              value: 'preset',
              child: Text(TrilingualService.instance.getUIText("Preset Blueprint (Board Pattern)")),
            ),
            DropdownMenuItem(
              value: 'manual',
              child: Text(TrilingualService.instance.getUIText("Manual Selection")),
            ),
          ],
          onChanged: (val) {
            setState(() => generationMode = val!);
          },
        ),
        if (generationMode == 'preset') ...[
          const SizedBox(height: 16),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.blue[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: Colors.blue[200]!),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Text(
                  TrilingualService.instance.getUIText("Configure Blueprint"),
                  style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.blue[900]),
                ),
                const SizedBox(height: 12),
                _buildBlueprintCounter("Section A (1 Mark)", blueprintSecA, (val) => setState(() => blueprintSecA = val)),
                const SizedBox(height: 8),
                _buildBlueprintCounter("Section B (2 Marks)", blueprintSecB, (val) => setState(() => blueprintSecB = val)),
                const SizedBox(height: 8),
                _buildBlueprintCounter("Section C (3 Marks)", blueprintSecC, (val) => setState(() => blueprintSecC = val)),
                const SizedBox(height: 8),
                _buildBlueprintCounter("Section D (4/5 Marks)", blueprintSecD, (val) => setState(() => blueprintSecD = val)),
              ],
            ),
          ),
        ],
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    final flavor = appFlavor ?? 'default';
    final isSkillup = flavor == 'skillup';
    final leftColumn = isSkillup ? _buildSkillupLeftColumn() : _buildDefaultLeftColumn();

    final rightColumn = Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          TrilingualService.instance.getUIText(isSkillup ? "2. Select Practice Lessons" : "2. Select Chapters"),
          style: GoogleFonts.poppins(
            fontSize: 18,
            fontWeight: FontWeight.bold,
            color: Colors.blue[800],
          ),
        ),
        const SizedBox(height: 16),
        if (isLoadingCurriculum)
          const Center(child: CircularProgressIndicator())
        else if (availableSubjects.isEmpty)
          Center(
            child: Text(
              TrilingualService.instance.getUIText("No subjects found for this curriculum."),
              style: const TextStyle(fontSize: 16),
            ),
          )
        else ...[
          DropdownButtonFormField<CurriculumSubject>(
            value: selectedSubject,
            decoration: InputDecoration(
              labelText: TrilingualService.instance.getUIText(isSkillup ? "Select Practice Track" : "Select Subject"),
              labelStyle: const TextStyle(fontSize: 14),
              border: const OutlineInputBorder(),
            ),
            style: const TextStyle(fontSize: 16, color: Colors.black),
            items: availableSubjects
                .map((s) => DropdownMenuItem(value: s, child: Text(s.title)))
                .toList(),
            onChanged: (val) {
              setState(() {
                selectedSubject = val;
                selectedModuleIds.clear();
                if (val != null) {
                  if (isSkillup) {
                    _applySkillupTrack(_selectedSkillupTrack);
                  } else {
                    selectedModuleIds.addAll(val.chapters.map((c) => c.moduleId));
                  }
                }
              });
            },
          ),
          const SizedBox(height: 16),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  "${TrilingualService.instance.getUIText(isSkillup ? "Lessons" : "Chapters")} (${selectedModuleIds.length}/${selectedSubject?.chapters.length ?? 0} selected)",
                  style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                ),
              ),
              TextButton(
                onPressed: () {
                  setState(() {
                    if (selectedModuleIds.length == selectedSubject?.chapters.length) {
                      selectedModuleIds.clear();
                    } else {
                      selectedModuleIds.clear();
                      if (isSkillup && !ActivationService.isActivated) {
                        selectedModuleIds.add('govindsir_english_ch1');
                        selectedModuleIds.add('govindsir_english_ch2');
                      } else {
                        selectedModuleIds.addAll(
                            selectedSubject!.chapters.map((c) => c.moduleId));
                      }
                    }
                  });
                },
                child: Text(
                  selectedModuleIds.length == selectedSubject?.chapters.length
                      ? TrilingualService.instance.getUIText("Deselect All")
                      : TrilingualService.instance.getUIText("Select All"),
                  style: const TextStyle(fontSize: 14),
                ),
              ),
            ],
          ),
          Container(
            height: 300, // Fixed height for ListView since we removed Expanded
            decoration: BoxDecoration(
              border: Border.all(color: Colors.grey[300]!),
              borderRadius: BorderRadius.circular(8),
              color: Colors.white,
            ),
            child: Material(
              color: Colors.transparent,
              child: ListView.builder(
                shrinkWrap: true,
                itemCount: selectedSubject?.chapters.length ?? 0,
                itemBuilder: (context, index) {
                  final chapter = selectedSubject!.chapters[index];
                  final isChapterFree = !isSkillup || index <= 1 || ActivationService.isActivated;
                  final scale = AppTypography.scaleFactor(context);

                  final tile = CheckboxListTile(
                    title: Text(chapter.title,
                        style: GoogleFonts.inter(fontSize: 14 * scale)),
                    value: selectedModuleIds.contains(chapter.moduleId),
                    onChanged: !isChapterFree
                        ? null
                        : (bool? val) {
                            setState(() {
                              if (val == true) {
                                selectedModuleIds.add(chapter.moduleId);
                              } else {
                                selectedModuleIds.remove(chapter.moduleId);
                              }
                            });
                          },
                    dense: true,
                  );

                  if (isChapterFree) return tile;

                  return ActivationGate(
                    isFree: false,
                    onActivated: () => setState(() {}),
                    child: tile,
                  );
                },
              ),
            ),
          ),
        ],
        const SizedBox(height: 24),
        isGenerating
            ? const Center(child: CircularProgressIndicator())
            : ElevatedButton.icon(
                icon: const Icon(Icons.flash_on, color: Colors.white),
                label: Text(
                  TrilingualService.instance.getUIText(isSkillup ? "Start Fluency Test" : "Generate Paper"),
                  style: GoogleFonts.poppins(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blue[600],
                  padding: const EdgeInsets.symmetric(vertical: 20),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
                onPressed: _generatePaper,
              ),
      ],
    );

    return Scaffold(
      backgroundColor: Colors.grey[50],
      appBar: BrandAppBar(
        title: TrilingualService.instance.getUIText(isSkillup ? "English Fluency Assessment" : "Advanced Paper Generator"),
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          final isDesktop = constraints.maxWidth >= 800;

          if (isDesktop) {
            return Center(
              child: Container(
                constraints: const BoxConstraints(maxWidth: 1000),
                padding: const EdgeInsets.all(24),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      flex: 1,
                      child: SingleChildScrollView(child: leftColumn),
                    ),
                    const SizedBox(width: 32),
                    Expanded(
                      flex: 1,
                      child: SingleChildScrollView(child: rightColumn),
                    ),
                  ],
                ),
              ),
            );
          } else {
            return SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  leftColumn,
                  const SizedBox(height: 32),
                  rightColumn,
                ],
              ),
            );
          }
        },
      ),
    );
  }

  Widget _buildBlueprintCounter(String label, int value, Function(int) onChanged) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(TrilingualService.instance.getUIText(label), style: const TextStyle(fontSize: 14)),
        Row(
          children: [
            IconButton(
              icon: const Icon(Icons.remove_circle_outline),
              color: Colors.blue[700],
              onPressed: value > 0 ? () => onChanged(value - 1) : null,
              padding: EdgeInsets.zero,
              constraints: const BoxConstraints(),
            ),
            const SizedBox(width: 12),
            Text(
              value.toString(),
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
            ),
            const SizedBox(width: 12),
            IconButton(
              icon: const Icon(Icons.add_circle_outline),
              color: Colors.blue[700],
              onPressed: () => onChanged(value + 1),
              padding: EdgeInsets.zero,
              constraints: const BoxConstraints(),
            ),
          ],
        ),
      ],
    );
  }
}
