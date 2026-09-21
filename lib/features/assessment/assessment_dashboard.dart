import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../core/engine/assessment_engine.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import 'question_selection_screen.dart';
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

  final List<String> boards = ["GSEB", "CBSE", "NCERT"];
  final List<String> classes = [
    "class3", "class4", "class5", "class6",
    "class7", "class8", "class9", "class10", "class11"
  ];

  List<CurriculumSubject> availableSubjects = [];
  CurriculumSubject? selectedSubject;
  Set<String> selectedModuleIds = {};


  @override
  void initState() {
    super.initState();
    _loadCurriculum();
  }

  Future<void> _loadCurriculum() async {
    setState(() {
      isLoadingCurriculum = true;
      availableSubjects.clear();
      selectedSubject = null;
      selectedModuleIds.clear();
    });

    final curriculumId = "${selectedBoard.toLowerCase()}_$selectedClass";
    final subjects = await AssessmentEngine.instance.fetchCurriculumSubjects(curriculumId);
    
    setState(() {
      availableSubjects = subjects;
      if (subjects.isNotEmpty) {
        selectedSubject = subjects.first;
        // Select all chapters by default
        selectedModuleIds.addAll(selectedSubject!.chapters.map((c) => c.moduleId));
      }
      isLoadingCurriculum = false;
    });
  }

  void _generatePaper() async {
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

    setState(() => isGenerating = false);
    if (mounted) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => QuestionSelectionScreen(
            allQuestionsPool: allAvailableQuestions,
            initialSelectedQuestions: allAvailableQuestions,
            title: "$selectedBoard ${selectedClass.toUpperCase()} - ${selectedSubject?.title ?? 'Test'}",
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final leftColumn = Column(
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
                    child: Text(c.toUpperCase()),
                  ))
              .toList(),
          onChanged: (val) {
            setState(() => selectedClass = val!);
            _loadCurriculum();
          },
        ),
      ],
    );

    final rightColumn = Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(
          TrilingualService.instance.getUIText("2. Select Chapters"),
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
              labelText: TrilingualService.instance.getUIText("Select Subject"),
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
                  selectedModuleIds.addAll(val.chapters.map((c) => c.moduleId));
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
                  "${TrilingualService.instance.getUIText("Chapters")} (${selectedModuleIds.length}/${selectedSubject?.chapters.length ?? 0} selected)",
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
                      selectedModuleIds.addAll(
                          selectedSubject!.chapters.map((c) => c.moduleId));
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
                  return CheckboxListTile(
                    title: Text(chapter.title,
                        style: GoogleFonts.inter(fontSize: 14)),
                    value: selectedModuleIds.contains(chapter.moduleId),
                    onChanged: (bool? val) {
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
                  TrilingualService.instance.getUIText("Generate Paper"),
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
        title: TrilingualService.instance.getUIText("Advanced Paper Generator"),
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
}
