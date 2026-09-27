import re

with open('lib/features/assessment/exam_engine_screen.dart', 'r') as f:
    content = f.read()

# We want to find where `Future<void> _loadQuestions() async {` starts
# and where the method ends.

start_idx = content.find('Future<void> _loadQuestions() async {')

# Let's just find the `void _startTimer() {` which comes right after it!
end_idx = content.find('void _startTimer() {')

if start_idx != -1 and end_idx != -1:
    new_method = """Future<void> _loadQuestions() async {
    setState(() {
      _isLoading = true;
      _error = null;
    });

    try {
      List<AssessmentQuestion> allQuestions = [];
      
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
        // Fallback to old Assessment Engine
        allQuestions = await AssessmentEngine.instance.extractQuestionsForModule(
          widget.moduleId, 
          ['quiz', 'true_false']
        );
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
    
    # We replace from start_idx up to end_idx-1 (since we need to preserve void _startTimer)
    # Wait, _startTimer was already in the file, and we added _startTimer() call inside new_method.
    # Actually, new_method contains `_startTimer();` at the end of the loadQuestions function, then we just need to stitch it.
    
    # Wait, new method above does not end with `}` for the whole method!
    # I missed the final `}` for `_loadQuestions`.
    
    new_method = new_method + "\n"
    
    # But wait! Look at my new_method string.
    # The `catch (e) { ... }` is closed.
    # The method ends.
    # We just need to make sure the brackets match perfectly! Let's count them!
    # Future<void> _loadQuestions() async { (1)
    #   setState(() { (2)
    #   }); (1)
    #   try { (2)
    #     try { (3)
    #       try { (4)
    #         if () { (5)
    #         } else { (4)
    #         }
    #       } catch() { (4)
    #       } (3)
    #       if () { (4)
    #       } (3)
    #       if () { (4)
    #         for () { (5)
    #           if () { (6)
    #             for () { (7)
    #               if () { (8)
    #               } (7)
    #             } (6)
    #           } (5)
    #         } (4)
    #       } else { (4)
    #         if () { (5)
    #         } else if () { (5)
    #         } (4)
    #         for () { (5)
    #           if () { (6)
    #             if () { (7)
    #             } (6)
    #             if () { (7)
    #               for () { (8)
    #               } (7)
    #             } (6)
    #           } else if () { (6)
    #           } (5)
    #         } (4)
    #         if () { (5)
    #           for () { (6)
    #             if () (7 inline)
    #             if () (7 inline)
    #             if () (7 inline)
    #           } (5)
    #         } (4)
    #       } (3)
    #     } catch () { (3)
    #     } (2)
    #     if () { (3)
    #     } (2)
    #     setState(() { (3)
    #     }); (2)
    #   } catch () { (2)
    #     setState(() { (3)
    #       if () { (4)
    #       } else { (4)
    #       } (3)
    #     }); (2)
    #   } (1)
    # } (0) -> NEED to add closing brace!
    
    new_method += "}\n\n  "
    
    with open('lib/features/assessment/exam_engine_screen.dart', 'w') as out:
        out.write(content[:start_idx] + new_method + content[end_idx:])
        
    print("Fixed!")
