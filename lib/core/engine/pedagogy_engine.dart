import 'package:flutter/foundation.dart';

class PedagogyReport {
  final bool isValid;
  final List<String> missingComponents;
  final List<String> warnings;

  PedagogyReport({required this.isValid, required this.missingComponents, required this.warnings});
}

class PedagogyEngine {
  /// Analyzes a chapter's blocks to ensure it meets the Shine Academy Pedagogy Standard.
  static PedagogyReport validateChapterFlow(List<dynamic> rawBlocks) {
    bool hasTheory = false;
    bool hasExample = false;
    bool hasActivity = false;
    bool hasDictionary = false;
    bool hasQuiz = false;
    bool hasSummary = false;

    for (var rawBlock in rawBlocks) {
      if (rawBlock is! Map<String, dynamic>) continue;
      
      final type = rawBlock['type'];
      if (type == 'theory') hasTheory = true;
      if (type == 'worked_example' || type == 'real_world_example' || type == 'example') hasExample = true;
      if (type == 'activity' || type == 'animated_diagram' || type == 'presentation') hasActivity = true;
      if (type == 'dictionary_link' || type == 'definition') hasDictionary = true;
      if (type == 'quiz' || type == 'flashcard') hasQuiz = true;
      if (type == 'summary' || type == 'revision') hasSummary = true;
    }

    List<String> missing = [];
    if (!hasTheory) missing.add("Theory Block");
    if (!hasExample) missing.add("Example Block");
    if (!hasDictionary) missing.add("Dictionary Link/Definition");
    if (!hasQuiz) missing.add("Quiz/Flashcard");
    if (!hasSummary) missing.add("Summary Block");
    
    // Warn if missing activities, but don't fail validation just yet to allow legacy chapters to pass
    List<String> warnings = [];
    if (!hasActivity) warnings.add("Missing Interactive Activity (Animation/Presentation)");

    return PedagogyReport(
      isValid: missing.isEmpty, 
      missingComponents: missing, 
      warnings: warnings
    );
  }
}
