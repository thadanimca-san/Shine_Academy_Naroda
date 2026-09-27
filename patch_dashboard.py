import re

with open('lib/features/assessment/assessment_dashboard.dart', 'r') as f:
    content = f.read()

# 1. Replace state variables
content = content.replace(
    "Set<String> selectedQuestionTypes = {'quiz'};",
    "Map<String, int> blueprintCounts = {'quiz': 10, 'fill_blank': 0, 'true_false': 0, 'short_note': 5};"
)
content = content.replace("int questionCount = 20;", "")

# 2. Update _generatePaper validation
content = content.replace(
    "if (selectedQuestionTypes.isEmpty) {\n      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText(\"Please select at least one question type.\"))));\n      return;\n    }",
    "if (blueprintCounts.values.every((v) => v == 0)) {\n      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText(\"Please configure the blueprint with at least one question.\"))));\n      return;\n    }"
)

# 3. Update Custom Paper Generation logic
old_gen = """    } else {
      // Fetch all available questions across selected modules for swapping pool
      for (String moduleId in selectedModuleIds) {
        final q = await AssessmentEngine.instance.extractQuestionsForModule(moduleId, selectedQuestionTypes.toList());
        allAvailableQuestions.addAll(q);
      }
      
      allAvailableQuestions.shuffle();
      initialQuestions = allAvailableQuestions.take(questionCount).toList();
    }"""
new_gen = """    } else {
      List<String> activeTypes = blueprintCounts.entries.where((e) => e.value > 0).map((e) => e.key).toList();
      for (String moduleId in selectedModuleIds) {
        final q = await AssessmentEngine.instance.extractQuestionsForModule(moduleId, activeTypes);
        allAvailableQuestions.addAll(q);
      }
      allAvailableQuestions.shuffle();
      
      for (var entry in blueprintCounts.entries) {
        if (entry.value > 0) {
          final typeQs = allAvailableQuestions.where((q) => q.type == entry.key).take(entry.value).toList();
          initialQuestions.addAll(typeQs);
        }
      }
    }"""
content = content.replace(old_gen, new_gen)

# 4. Update UI for 'standard' format
old_ui = """                      if (paperFormat == 'standard') ...[
                        Text(TrilingualService.instance.getUIText("Question Types"), style: GoogleFonts.poppins(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.blue[800])),
                        ...availableQuestionTypes.entries.map((entry) => CheckboxListTile(
                          title: Text(entry.value, style: TextStyle(fontSize: 14)),
                          value: selectedQuestionTypes.contains(entry.key),
                          onChanged: (bool? val) {
                            setState(() {
                              if (val == true) {
                                selectedQuestionTypes.add(entry.key);
                              } else {
                                selectedQuestionTypes.remove(entry.key);
                              }
                            });
                          },
                          controlAffinity: ListTileControlAffinity.leading,
                          contentPadding: EdgeInsets.zero,
                          dense: true,
                        )),
                        const SizedBox(height: 16),
                        DropdownButtonFormField<int>(
                          value: questionCount,
                          decoration: const InputDecoration(labelText: "Number of Questions", labelStyle: TextStyle(fontSize: 14), border: OutlineInputBorder()),
                          style: TextStyle(fontSize: 16, color: Theme.of(context).colorScheme.onSurface),
                          items: [10, 20, 50, 100].map((c) => DropdownMenuItem(value: c, child: Text("$c Questions"))).toList(),
                          onChanged: (val) => setState(() => questionCount = val!),
                        ),
                      ] else ...["""
new_ui = """                      if (paperFormat == 'standard') ...[
                        Text(TrilingualService.instance.getUIText("Blueprint Configuration"), style: GoogleFonts.poppins(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.blue[800])),
                        const SizedBox(height: 8),
                        ...availableQuestionTypes.entries.map((entry) => Padding(
                          padding: const EdgeInsets.only(bottom: 12.0),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Expanded(child: Text(entry.value, style: TextStyle(fontSize: 14, fontWeight: FontWeight.w500))),
                              Row(
                                children: [
                                  IconButton(
                                    icon: const Icon(Icons.remove_circle_outline, color: Colors.blue),
                                    onPressed: () {
                                      setState(() {
                                        if (blueprintCounts[entry.key] != null && blueprintCounts[entry.key]! > 0) {
                                          blueprintCounts[entry.key] = blueprintCounts[entry.key]! - 1;
                                        }
                                      });
                                    },
                                  ),
                                  SizedBox(
                                    width: 30,
                                    child: Text(
                                      '${blueprintCounts[entry.key] ?? 0}',
                                      textAlign: TextAlign.center,
                                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                                    ),
                                  ),
                                  IconButton(
                                    icon: const Icon(Icons.add_circle_outline, color: Colors.blue),
                                    onPressed: () {
                                      setState(() {
                                        blueprintCounts[entry.key] = (blueprintCounts[entry.key] ?? 0) + 1;
                                      });
                                    },
                                  ),
                                ],
                              )
                            ],
                          ),
                        )),
                      ] else ...["""
content = content.replace(old_ui, new_ui)

with open('lib/features/assessment/assessment_dashboard.dart', 'w') as f:
    f.write(content)
