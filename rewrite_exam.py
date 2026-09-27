import re

with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    content = f.read()

start_marker = "Future<void> _loadExam() async {"
end_marker = "void _startTimer() {"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

new_method = """Future<void> _loadExam() async {
    try {
      List<AssessmentQuestion> allQuestions = [];
      
      // 1. Try to load Gold Standard Assessment JSON first
      try {
        final jsonString = await rootBundle.loadString('app_core/assessment/${widget.moduleId}_questions.json');
        final assessmentData = json.decode(jsonString);
        
        if (assessmentData['questions'] != null) {
          final qList = assessmentData['questions'] as List;
          for (var q in qList) {
            if (q['type'] == 'mcq' || q['type'] == 'true_false' || q['type'] == 'fill_blank') {
              final opts = q['options'] as List;
              List<String> optionTexts = [];
              List<String> optionTextsHi = [];
              dynamic correctIndexOrAnswer = 0;
              
              for (int i = 0; i < opts.length; i++) {
                optionTexts.add(opts[i]['english'] ?? '');
                optionTextsHi.add(opts[i]['hindi'] ?? '');
                if (opts[i]['id'] == q['answer']) {
                  correctIndexOrAnswer = i;
                }
              }
              
              allQuestions.add(AssessmentQuestion(
                moduleId: widget.moduleId,
                type: 'quiz', // Unified internal type for UI rendering
                question: q['question_text']?['english'] ?? '',
                questionHi: q['question_text']?['hindi'],
                options: optionTexts,
                optionsHi: optionTextsHi,
                correctIndexOrAnswer: correctIndexOrAnswer,
                explanationEn: q['explanation']?['english'],
                explanationHi: q['explanation']?['hindi'],
                distractorRationaleEn: q['distractor_rationale']?['english'],
                distractorRationaleHi: q['distractor_rationale']?['hindi'],
                bloomTaxonomy: q['bloom_taxonomy'],
                aiHint: q['ai_context']?['hint'],
              ));
            }
          }
        }
      } catch (e) {
        // 2. Fallback to old Chapter JSON format or Gold Standard blocks
        try {
          final String chapterAssetPath = 'app_core/chapters/${widget.moduleId}.json';
          dynamic chapterData;
          try {
             final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/${widget.moduleId}.json');
             if (file.existsSync()) {
               chapterData = json.decode(file.readAsStringSync());
             } else {
               final jsonString = await rootBundle.loadString(chapterAssetPath);
               chapterData = json.decode(jsonString);
             }
          } catch(e) {
             final jsonString = await rootBundle.loadString(chapterAssetPath);
             chapterData = json.decode(jsonString);
          }
          
          if (chapterData == null) {
            throw Exception('Chapter data could not be loaded');
          }
          
          if (chapterData is Map && chapterData['assessments'] != null && chapterData['assessments']['summative_assessments'] != null) {
            final summative = chapterData['assessments']['summative_assessments'] as List;
            for (var q in summative) {
              if (q['type'] == 'mcq') {
                final opts = q['options'] as List;
                List<String> optionTexts = [];
                int correctIndex = 0;
                
                for (int i = 0; i < opts.length; i++) {
                  optionTexts.add(opts[i]['text']);
                  if (opts[i]['id'] == q['correct_option_id']) {
                    correctIndex = i;
                  }
                }
                
                allQuestions.add(AssessmentQuestion(
                  moduleId: widget.moduleId,
                  type: 'quiz', 
                  question: q['question_text'] ?? q['question'] ?? '',
                  options: optionTexts,
                  correctIndexOrAnswer: correctIndex,
                ));
              }
            }
          } else {
            // Handle blocks format (either Map with 'blocks' or direct List)
            List blocks = [];
            if (chapterData is Map && chapterData['blocks'] != null) {
              blocks = chapterData['blocks'] as List;
            } else if (chapterData is List) {
              blocks = chapterData;
            }
            
            List<Map<String, dynamic>> flashcards = [];
            
            for (var block in blocks) {
              if (block['type'] == 'quiz' || block['type'] == 'mcq' || block['type'] == 'knowledge_check' || block['type'] == 'socratic' || block['type'] == 'quiz_multiple_choice') {
                if (block['is_deo_challenge'] == true) {
                  continue; // Skip DEO challenge questions in the standard mock test
                }
                final opts = block['options'] as List?;
                List<String> optionTexts = [];
                if (opts != null) {
                  for (var opt in opts) {
                    optionTexts.add(opt.toString());
                  }
                }
                
                dynamic correctAns = block['correct_index'] ?? 0;
                
                allQuestions.add(AssessmentQuestion(
                  moduleId: widget.moduleId,
                  type: 'quiz',
                  question: block['question_text'] ?? block['question'] ?? '',
                  questionHi: block['question_text_hi'] ?? block['question_hi'],
                  options: optionTexts,
                  optionsHi: block['options_hi'] != null ? List<String>.from(block['options_hi']) : null,
                  correctIndexOrAnswer: correctAns,
                  explanationEn: block['explanation'],
                  explanationHi: block['explanation_hi'],
                ));
              } else if (block['type'] == 'flashcard') {
                flashcards.add(block as Map<String, dynamic>);
              }
            }
            
            // Auto-generate mock test questions from Flashcards
            if (flashcards.isNotEmpty) {
              List<String> allBacks = flashcards.map((f) => f['back'].toString()).toSet().toList();
              
              for (var f in flashcards) {
                String front = f['front'].toString();
                String back = f['back'].toString();
                
                List<String> options = [back];
                List<String> pool = allBacks.where((b) => b != back).toList();
                pool.shuffle();
                options.addAll(pool.take(3));
                
                if (options.length < 2) options.add("None of these");
                if (options.length < 3) options.add("All of the above");
                if (options.length < 4) options.add("I don't know");
                
                options.shuffle();
                int correctIndex = options.indexOf(back);
                
                allQuestions.add(AssessmentQuestion(
                  moduleId: widget.moduleId,
                  type: 'quiz',
                  question: front,
                  options: options,
                  correctIndexOrAnswer: correctIndex,
                  explanationEn: "Flashcard Answer: $back",
                ));
              }
            }
          }
        } catch (e) {
          // 3. Fallback to very old Assessment Engine
          allQuestions = await AssessmentEngine.instance.extractQuestionsForModule(
            widget.moduleId, 
            ['quiz', 'true_false']
          );
        }
      }
      
      // Shuffle and take up to 10 questions
      allQuestions.shuffle();
      final selectedQuestions = allQuestions.take(10).toList();

      if (selectedQuestions.isEmpty) {
        throw Exception("NO_QUESTIONS");
      }

      setState(() {
        _questions = selectedQuestions;
        _remainingSeconds = selectedQuestions.length * 60; // 1 min per question
        _isLoading = false;
      });
      _startTimer();
    } catch (e) {
      setState(() {
        if (e.toString().contains("NO_QUESTIONS")) {
          _error = 'This chapter is highly interactive. There is no written mock test for this module. Please enjoy practicing in the Learn section!';
        } else {
          _error = 'Failed to generate Mock Test for this chapter.';
        }
        _isLoading = false;
      });
    }
  }

  """

with open('lib/features/assessment/exam_engine_screen.dart', 'w') as out:
    out.write(content[:start_idx] + new_method + content[end_idx:])
    
print("Successfully replaced method!")
