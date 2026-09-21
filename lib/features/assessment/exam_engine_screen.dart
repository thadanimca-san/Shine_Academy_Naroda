import 'dart:async';
import 'package:flutter/services.dart';
import 'dart:convert';
import "package:shine_academy_naroda/core/engine/local_content_manager.dart";
import "dart:io";
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/brand_app_bar.dart';
import '../../foundation/theme/premium_card.dart';
import '../../core/engine/assessment_engine.dart';
import '../../core/services/gamification_service.dart';
import '../gamification/widgets/mast_hai_dialog.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ExamEngineScreen extends StatefulWidget {
  final String moduleId;
  final List<AssessmentQuestion>? customQuestions;
  final String? customTitle;
  final int? customTimeSeconds;

  const ExamEngineScreen({
    super.key, 
    required this.moduleId,
    this.customQuestions,
    this.customTitle,
    this.customTimeSeconds,
  });

  @override
  State<ExamEngineScreen> createState() => _ExamEngineScreenState();
}

class _ExamEngineScreenState extends State<ExamEngineScreen> {
  List<AssessmentQuestion> _questions = [];
  bool _isLoading = true;
  String _error = '';

  int _currentIndex = 0;
  final Map<int, int> _selectedAnswers = {}; // questionIndex -> optionIndex
  final Set<int> _markedForReview = {};
  final ScrollController _scrollController = ScrollController();

  Timer? _timer;
  int _remainingSeconds = 600; // 10 minutes default
  bool _isSubmitted = false;

  @override
  void initState() {
    super.initState();
    _loadExam();
  }

  Future<void> _loadExam() async {
    if (widget.customQuestions != null) {
      setState(() {
        _questions = List.from(widget.customQuestions!);
        if (widget.customTimeSeconds != null) {
          _remainingSeconds = widget.customTimeSeconds!;
        } else {
          // Fallback: 90 seconds per question for custom papers
          _remainingSeconds = _questions.length * 90;
        }
        _isLoading = false;
      });
      _startTimer();
      return;
    }

    try {
      List<AssessmentQuestion> allQuestions = [];
      
      // 1. Try to load Gold Standard Assessment JSON first
      try {
        final jsonString = await rootBundle.loadString('app_core/assessment/${widget.moduleId}_questions.json');
        final dynamic assessmentData = json.decode(jsonString);
        
        List qList = [];
        if (assessmentData is List) {
          qList = assessmentData;
        } else if (assessmentData is Map) {
          if (assessmentData['questions'] != null) {
            qList = assessmentData['questions'] as List;
          } else if (assessmentData['blocks'] != null) {
            qList = assessmentData['blocks'] as List;
          }
        }
        
        for (var q in qList) {
          if (q['type'] == 'mcq' || q['type'] == 'true_false' || q['type'] == 'fill_blank' || q['type'] == 'quiz') {
            final opts = q['options'] as List?;
            List<String> optionTexts = [];
            List<String> optionTextsHi = [];
            List<String> optionTextsGu = [];
            dynamic correctIndexOrAnswer = 0;
            
            if (opts != null) {
              for (int i = 0; i < opts.length; i++) {
                if (opts[i] is Map) {
                  optionTexts.add(opts[i]['english'] ?? opts[i]['text'] ?? '');
                  optionTextsHi.add(opts[i]['hindi'] ?? '');
                  optionTextsGu.add(opts[i]['gujarati'] ?? '');
                  if (opts[i]['id'] == q['answer']) {
                    correctIndexOrAnswer = i;
                  }
                } else if (opts[i] is String) {
                  optionTexts.add(opts[i]);
                  if (q['options_hi'] != null && q['options_hi'] is List && i < q['options_hi'].length) {
                    optionTextsHi.add(q['options_hi'][i].toString());
                  }
                  if (q['options_gu'] != null && q['options_gu'] is List && i < q['options_gu'].length) {
                    optionTextsGu.add(q['options_gu'][i].toString());
                  }
                  if (opts[i] == q['answer'] || i == q['correct_index']) {
                    correctIndexOrAnswer = i;
                  }
                }
              }
            }
            
            allQuestions.add(AssessmentQuestion(
              moduleId: widget.moduleId,
              type: 'quiz', // Unified internal type for UI rendering
              question: (q['question_text'] is Map) ? (q['question_text']['english'] ?? '') : (q['question_text'] ?? q['question'] ?? ''),
              questionHi: (q['question_text'] is Map) ? q['question_text']['hindi'] : q['question_hi'],
              questionGu: (q['question_text'] is Map) ? q['question_text']['gujarati'] : q['question_gu'],
              options: optionTexts,
              optionsHi: optionTextsHi.isNotEmpty ? optionTextsHi : null,
              optionsGu: optionTextsGu.isNotEmpty ? optionTextsGu : null,
              correctIndexOrAnswer: correctIndexOrAnswer,
              explanationEn: (q['explanation'] is Map) ? q['explanation']['english'] : (q['explanation'] ?? q['solution'] ?? q['answer_description']),
              explanationHi: (q['explanation'] is Map) ? q['explanation']['hindi'] : (q['explanation_hi'] ?? q['solution_hi']),
              explanationGu: (q['explanation'] is Map) ? q['explanation']['gujarati'] : (q['explanation_gu'] ?? q['solution_gu']),
              distractorRationaleEn: (q['distractor_rationale'] is Map) ? q['distractor_rationale']['english'] : null,
              distractorRationaleHi: (q['distractor_rationale'] is Map) ? q['distractor_rationale']['hindi'] : null,
              distractorRationaleGu: (q['distractor_rationale'] is Map) ? q['distractor_rationale']['gujarati'] : null,
              bloomTaxonomy: q['bloom_taxonomy'],
              aiHint: (q['ai_context'] is Map) ? q['ai_context']['hint'] : null,
            ));
          }
        }
        
        if (allQuestions.isEmpty) {
          throw Exception("Empty questions list");
        }
      } catch (e) {
        // 2. Fallback to old Chapter JSON format or Gold Standard blocks
        try {
          dynamic chapterData;
          
          final String learningModulePath = 'app_core/learning_modules/${widget.moduleId}/blocks.json';
          try {
             final jsonString = await rootBundle.loadString(learningModulePath);
             chapterData = json.decode(jsonString);
          } catch (e1) {
             final String chapterAssetPath = 'app_core/chapters/${widget.moduleId}.json';
             try {
                final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/${widget.moduleId}.json');
                if (file.existsSync()) {
                  chapterData = json.decode(file.readAsStringSync());
                } else {
                  final jsonString = await rootBundle.loadString(chapterAssetPath);
                  chapterData = json.decode(jsonString);
                }
             } catch(e2) {
                final jsonString = await rootBundle.loadString(chapterAssetPath);
                chapterData = json.decode(jsonString);
             }
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
                if (block['is_board_challenge'] == true) {
                  continue; // Skip Board challenge questions in the standard mock test
                }
                final opts = block['options'] as List?;
                List<String> optionTexts = [];
                if (opts != null) {
                  for (var opt in opts) {
                    if (opt is Map) {
                      optionTexts.add(opt['english'] ?? opt['en'] ?? opt['text'] ?? opt.toString());
                    } else {
                      optionTexts.add(opt.toString());
                    }
                  }
                }
                
                dynamic correctAns = block['correct_index'] ?? 0;
                
                final rawQuestion = block['question_text'] ?? block['question'] ?? '';
                String questionStr = '';
                if (rawQuestion is Map) {
                  questionStr = rawQuestion['english'] ?? rawQuestion['en'] ?? rawQuestion.toString();
                } else {
                  questionStr = rawQuestion.toString();
                }
                
                allQuestions.add(AssessmentQuestion(
                  moduleId: widget.moduleId,
                  type: 'quiz',
                  question: questionStr,
                  questionHi: block['question_text_hi'] ?? block['question_hi'] ?? (rawQuestion is Map ? rawQuestion['hindi'] ?? rawQuestion['hi'] : null),
                  questionGu: block['question_text_gu'] ?? block['question_gu'] ?? (rawQuestion is Map ? rawQuestion['gujarati'] ?? rawQuestion['gu'] : null),
                  paragraph: block['paragraph'],
                  paragraphHi: block['paragraph_hi'],
                  paragraphGu: block['paragraph_gu'],
                  options: optionTexts,
                  optionsHi: block['options_hi'] != null ? (block['options_hi'] as List).map((e) => e.toString()).toList().cast<String>() : null,
                  optionsGu: block['options_gu'] != null ? (block['options_gu'] as List).map((e) => e.toString()).toList().cast<String>() : null,
                  correctIndexOrAnswer: correctAns,
                  explanationEn: block['explanation'] ?? block['solution'] ?? block['answer_description'] ?? (block['content'] != null ? (block['content']['explanation'] ?? block['content']['solution']) : null),
                  explanationHi: block['explanation_hi'] ?? block['solution_hi'] ?? (block['content'] != null ? (block['content']['explanation_hi'] ?? block['content']['solution_hi']) : null),
                  explanationGu: block['explanation_gu'] ?? block['solution_gu'] ?? (block['content'] != null ? (block['content']['explanation_gu'] ?? block['content']['solution_gu']) : null),
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
          throw Exception("CRITICAL MOCK TEST ERROR: " + e.toString());
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
          _error = 'Failed to generate Mock Test for this chapter. Error: ' + e.toString();
        }
        _isLoading = false;
      });
    }
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_remainingSeconds > 0 && !_isSubmitted) {
        setState(() {
          _remainingSeconds--;
        });
      } else {
        timer.cancel();
        if (!_isSubmitted) {
          _submitExam();
        }
      }
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    _scrollController.dispose();
    super.dispose();
  }

  void _submitExam() async {
    setState(() {
      _isSubmitted = true;
      _timer?.cancel();
    });

    int correctCount = 0;
    for (int i = 0; i < _questions.length; i++) {
      if (_selectedAnswers[i] == _questions[i].correctIndexOrAnswer) {
        correctCount++;
      }
    }
    
    // Award XP and Coins!
    if (correctCount > 0) {
      int xpEarned = correctCount * 20; // 20 XP per correct answer
      int coinsEarned = correctCount * 5; // 5 Coins per correct answer
      
      await GamificationService.instance.addCoins(coinsEarned);
      bool leveledUp = await GamificationService.instance.addXp(xpEarned);
      
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text('Awesome! You earned $xpEarned XP and $coinsEarned Shine Coins!'),
          backgroundColor: Colors.green,
          duration: const Duration(seconds: 4),
        ));
      }
    }
    
    if (correctCount == _questions.length && _questions.isNotEmpty) {
      showDialog(
        context: context,
        barrierColor: Colors.black87,
        builder: (context) => const MastHaiDialog(),
      );
    }
  }

  String get _formattedTime {
    int m = _remainingSeconds ~/ 60;
    int s = _remainingSeconds % 60;
    return '${m.toString().padLeft(2, '0')}:${s.toString().padLeft(2, '0')}';
  }

  void _scrollToCurrentIndex() {
    if (_scrollController.hasClients) {
      double screenWidth = MediaQuery.of(context).size.width;
      // Item width is approximately 40 + 12 (margin) = 52. Padding is 16.
      double itemPosition = 16.0 + (_currentIndex * 52.0);
      // Try to center it
      double targetPosition = itemPosition - (screenWidth / 2) + 26.0;
      if (targetPosition < 0) targetPosition = 0;
      if (targetPosition > _scrollController.position.maxScrollExtent) {
        targetPosition = _scrollController.position.maxScrollExtent;
      }
      _scrollController.animateTo(
        targetPosition,
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) return const Scaffold(body: Center(child: CircularProgressIndicator()));
    if (_error.isNotEmpty) return Scaffold(appBar: const BrandAppBar(title: 'Error'), body: Center(child: Text(_error)));

    if (_isSubmitted) {
      return _buildReportScreen();
    }

    final question = _questions[_currentIndex];
    final lang = TrilingualService.instance.activeViewLanguage;
    
    String questionText = question.question;
    if (lang == 'hi' && question.questionHi != null && question.questionHi!.isNotEmpty) {
      questionText = question.questionHi!;
    } else if (lang == 'gu' && question.questionGu != null && question.questionGu!.isNotEmpty) {
      questionText = question.questionGu!;
    }
    
    String? paragraphText = question.paragraph;
    if (lang == 'hi' && question.paragraphHi != null && question.paragraphHi!.isNotEmpty) {
      paragraphText = question.paragraphHi;
    } else if (lang == 'gu' && question.paragraphGu != null && question.paragraphGu!.isNotEmpty) {
      paragraphText = question.paragraphGu;
    }
    
    List<String> options = question.options;
    if (lang == 'hi' && question.optionsHi != null && question.optionsHi!.isNotEmpty) {
      options = question.optionsHi!;
    } else if (lang == 'gu' && question.optionsGu != null && question.optionsGu!.isNotEmpty) {
      options = question.optionsGu!;
    }

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(title: widget.customTitle ?? 'Mock Test'),
      body: Column(
        children: [
          // Timer Header
          Container(
            color: Colors.white,
            padding: const EdgeInsets.all(16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Question ${_currentIndex + 1}/${_questions.length}',
                  style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 18),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  decoration: BoxDecoration(
                    color: _remainingSeconds < 300 ? Colors.red.withValues(alpha: 0.1) : AppColors.primary.withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.timer, color: _remainingSeconds < 300 ? Colors.red : AppColors.primary, size: 20),
                      const SizedBox(width: 8),
                      Text(
                        _formattedTime,
                        style: GoogleFonts.inter(
                          fontWeight: FontWeight.bold,
                          color: _remainingSeconds < 300 ? Colors.red : AppColors.primary,
                          fontSize: 16,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          
          // Question Navigator (Horizontal List)
          Container(
            height: 60,
            color: Colors.grey.shade100,
            child: ListView.builder(
              controller: _scrollController,
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              itemCount: _questions.length,
              itemBuilder: (context, index) {
                bool isSelected = _currentIndex == index;
                bool isAttempted = _selectedAnswers.containsKey(index);
                bool isMarked = _markedForReview.contains(index);

                Color bgColor = Colors.white;
                Color textColor = Colors.grey.shade600;
                Color borderColor = Colors.grey.shade300;

                if (isAttempted) {
                  bgColor = Colors.green;
                  textColor = Colors.white;
                  borderColor = Colors.green;
                }
                if (isMarked) {
                  bgColor = Colors.purple;
                  textColor = Colors.white;
                  borderColor = Colors.purple;
                }
                if (isSelected) {
                  borderColor = AppColors.primary;
                }

                return GestureDetector(
                  onTap: () {
                    setState(() {
                      _currentIndex = index;
                    });
                    _scrollToCurrentIndex();
                  },
                  child: Container(
                    width: 40,
                    margin: const EdgeInsets.only(right: 12),
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: bgColor,
                      shape: BoxShape.circle,
                      border: Border.all(
                        color: borderColor,
                        width: isSelected ? 3 : 1,
                      ),
                    ),
                    child: Text(
                      '${index + 1}',
                      style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: textColor),
                    ),
                  ),
                );
              },
            ),
          ),

          // Question Content
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (paragraphText != null && paragraphText.isNotEmpty) ...[
                    Container(
                      padding: const EdgeInsets.all(16),
                      margin: const EdgeInsets.only(bottom: 24),
                      decoration: BoxDecoration(
                        color: Colors.blue.withValues(alpha: 0.05),
                        border: Border(left: BorderSide(color: Colors.blue, width: 4)),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            paragraphText,
                            style: GoogleFonts.inter(fontSize: 16, height: 1.5, color: Colors.blue.shade900),
                          ),
                        ],
                      ),
                    ),
                  ],
                  Text(
                    questionText,
                    style: GoogleFonts.inter(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                  ),
                  const SizedBox(height: 24),
                  ...List.generate(options.length, (optIndex) {
                    bool isSelected = _selectedAnswers[_currentIndex] == optIndex;
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: InkWell(
                        onTap: () {
                          setState(() {
                            _selectedAnswers[_currentIndex] = optIndex;
                          });
                        },
                        borderRadius: BorderRadius.circular(12),
                        child: Container(
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(
                            color: isSelected ? AppColors.primary.withValues(alpha: 0.1) : Colors.white,
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(color: isSelected ? AppColors.primary : Colors.grey.shade300, width: 2),
                          ),
                          child: Row(
                            children: [
                              Container(
                                width: 24,
                                height: 24,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: isSelected ? AppColors.primary : Colors.white,
                                  border: Border.all(color: AppColors.primary, width: 2),
                                ),
                                child: isSelected
                                    ? Icon(Icons.circle, size: 12, color: Colors.white)
                                    : null,
                              ),
                              const SizedBox(width: 16),
                              Expanded(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      options[optIndex].toString(),
                                      style: GoogleFonts.inter(
                                        fontSize: 16, color: AppColors.textPrimary),
                                    ),
                                  ],
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    );
                  }),
                ],
              ),
            ),
          ),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Container(
          padding: const EdgeInsets.all(16),
          color: Colors.white,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              TextButton.icon(
                onPressed: () {
                  setState(() {
                    if (_markedForReview.contains(_currentIndex)) {
                      _markedForReview.remove(_currentIndex);
                    } else {
                      _markedForReview.add(_currentIndex);
                    }
                  });
                },
                icon: Icon(
                  _markedForReview.contains(_currentIndex) ? Icons.bookmark : Icons.bookmark_border,
                  color: Colors.purple,
                ),
                label: Text(TrilingualService.instance.getUIText('Mark for Review'), style: GoogleFonts.inter(color: Colors.purple, fontWeight: FontWeight.bold)),
              ),
              Row(
                children: [
                  if (_currentIndex > 0)
                    IconButton(
                      icon: Icon(Icons.arrow_back_ios),
                      onPressed: () {
                        setState(() => _currentIndex--);
                        _scrollToCurrentIndex();
                      },
                    ),
                  if (_currentIndex < _questions.length - 1)
                    ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppColors.primary,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      ),
                      onPressed: () {
                        setState(() => _currentIndex++);
                        _scrollToCurrentIndex();
                      },
                      child: FittedBox(
                        fit: BoxFit.scaleDown,
                        child: Text(TrilingualService.instance.getUIText('Next'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
                      ),
                    )
                  else
                    ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.green,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      ),
                      onPressed: () {
                        _showSubmitDialog();
                      },
                      child: FittedBox(
                        fit: BoxFit.scaleDown,
                        child: Text(TrilingualService.instance.getUIText('Submit Exam'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
                      ),
                    ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }

  void _showSubmitDialog() {
    int unattempted = _questions.length - _selectedAnswers.length;
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(TrilingualService.instance.getUIText('Submit Exam?'), style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
        content: Text('You have $unattempted unattempted questions. Are you sure you want to submit?'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: Text(TrilingualService.instance.getUIText('Cancel'))),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: Colors.green, foregroundColor: Colors.white),
            onPressed: () {
              Navigator.pop(context);
              _submitExam();
            },
            child: Text(TrilingualService.instance.getUIText('Submit')),
          ),
        ],
      ),
    );
  }

  Widget _buildReportScreen() {
    final lang = TrilingualService.instance.activeViewLanguage;
    int correct = 0;
    int incorrect = 0;
    int unattempted = 0;
    List<AssessmentQuestion> weakConcepts = [];

    for (int i = 0; i < _questions.length; i++) {
      final q = _questions[i];
      if (_selectedAnswers.containsKey(i)) {
        if (_selectedAnswers[i] == q.correctIndexOrAnswer) {
          correct++;
        } else {
          incorrect++;
          weakConcepts.add(q);
        }
      } else {
        unattempted++;
        weakConcepts.add(q);
      }
    }

    int score = (correct * 4) - (incorrect * 1);
    int totalPossible = _questions.length * 4;

    return Scaffold(
      appBar: const BrandAppBar(title: 'Socratic Reflection Report'),
      backgroundColor: AppColors.background,
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            PremiumCard(
              color: Colors.white,
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    Text(TrilingualService.instance.getUIText('Mock Test Score'), style: GoogleFonts.inter(fontSize: 18, color: AppColors.textSecondary)),
                    const SizedBox(height: 8),
                    Text('$score / $totalPossible', style: GoogleFonts.inter(fontSize: 48, fontWeight: FontWeight.bold, color: AppColors.primary)),
                    const SizedBox(height: 20),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _buildStat('Correct (+4)', correct, Colors.green),
                        _buildStat('Incorrect (-1)', incorrect, Colors.red),
                        _buildStat('Skipped (0)', unattempted, Colors.grey),
                      ],
                    )
                  ],
                ),
              ),
            ),
            const SizedBox(height: 24),
            if (weakConcepts.isNotEmpty) ...[
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.orange.shade50,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.orange.shade200),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.psychology, color: Colors.orange),
                        const SizedBox(width: 8),
                        Text(TrilingualService.instance.getUIText('Socratic Reflection'), style: GoogleFonts.inter(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.orange.shade900)),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'You struggled with ${weakConcepts.length} concepts. Do not worry! Every mistake is a stepping stone. We recommend you revisit the Learning Engine for this chapter and focus on the topics below:',
                      style: GoogleFonts.inter(color: Colors.orange.shade900),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),
            ],
            Text(TrilingualService.instance.getUIText('Detailed Solutions'), style: GoogleFonts.inter(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            ...List.generate(_questions.length, (i) {
              final q = _questions[i];
              final opts = q.options;
                  
              final selected = _selectedAnswers[i];
              final correctIdx = q.correctIndexOrAnswer as int;
              final isCorrect = selected == correctIdx;
              final statusColor = selected == null ? Colors.grey : (isCorrect ? Colors.green : Colors.red);
              
              return Card(
                margin: const EdgeInsets.only(bottom: 16),
                child: ExpansionTile(
                  initiallyExpanded: !isCorrect,
                  leading: Icon(isCorrect ? Icons.check_circle : Icons.cancel, color: statusColor),
                  title: Text('Question ${i + 1}', style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: statusColor)),
                  subtitle: Text(isCorrect ? '+4 Marks' : (selected == null ? '0 Marks' : '-1 Mark')),
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Builder(
                            builder: (context) {
                              String qText = q.question;
                              if (lang == 'hi' && q.questionHi != null && q.questionHi!.isNotEmpty) qText = q.questionHi!;
                              if (lang == 'gu' && q.questionGu != null && q.questionGu!.isNotEmpty) qText = q.questionGu!;
                              
                              String userAns = 'None';
                              if (selected != null) {
                                userAns = opts[selected];
                                if (lang == 'hi' && q.optionsHi != null && q.optionsHi!.length > selected && q.optionsHi![selected].isNotEmpty) userAns = q.optionsHi![selected];
                                if (lang == 'gu' && q.optionsGu != null && q.optionsGu!.length > selected && q.optionsGu![selected].isNotEmpty) userAns = q.optionsGu![selected];
                              }
                              
                              String correctAns = opts[correctIdx];
                              if (lang == 'hi' && q.optionsHi != null && q.optionsHi!.length > correctIdx && q.optionsHi![correctIdx].isNotEmpty) correctAns = q.optionsHi![correctIdx];
                              if (lang == 'gu' && q.optionsGu != null && q.optionsGu!.length > correctIdx && q.optionsGu![correctIdx].isNotEmpty) correctAns = q.optionsGu![correctIdx];
                              
                              String? explText = q.explanationEn;
                              if (lang == 'hi' && q.explanationHi != null && q.explanationHi!.isNotEmpty) explText = q.explanationHi;
                              if (lang == 'gu' && q.explanationGu != null && q.explanationGu!.isNotEmpty) explText = q.explanationGu;

                              return Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(qText, style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w600)),
                                  const SizedBox(height: 16),
                                  Text('Your Answer: $userAns', style: GoogleFonts.inter(color: statusColor)),
                                  if (!isCorrect)
                                    Text('Correct Answer: $correctAns', style: GoogleFonts.inter(color: Colors.green, fontWeight: FontWeight.bold)),
                                  
                                  if (explText != null) ...[
                                    const SizedBox(height: 16),
                                    Container(
                                      padding: const EdgeInsets.all(12),
                                      decoration: BoxDecoration(
                                        color: Colors.blue.withValues(alpha: 0.05),
                                        borderRadius: BorderRadius.circular(8),
                                        border: Border.all(color: Colors.blue.withValues(alpha: 0.2)),
                                      ),
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Row(
                                            children: [
                                              Icon(Icons.lightbulb, color: Colors.blue, size: 18),
                                              const SizedBox(width: 8),
                                              Text(TrilingualService.instance.getUIText('Explanation'), style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: Colors.blue.shade800)),
                                            ],
                                          ),
                                          const SizedBox(height: 8),
                                          Text(explText, style: GoogleFonts.inter(color: Colors.blue.shade900)),
                                        ],
                                      ),
                                    ),
                                  ],
                                ],
                              );
                            }
                          ),

                          if (!isCorrect && q.distractorRationaleEn != null) ...[
                            Builder(
                              builder: (context) {
                                String distractorText = q.distractorRationaleEn!;
                                if (lang == 'hi' && q.distractorRationaleHi != null && q.distractorRationaleHi!.isNotEmpty) distractorText = q.distractorRationaleHi!;
                                if (lang == 'gu' && q.distractorRationaleGu != null && q.distractorRationaleGu!.isNotEmpty) distractorText = q.distractorRationaleGu!;
                                
                                return Column(
                                  children: [
                                    const SizedBox(height: 16),
                                    Container(
                                      padding: const EdgeInsets.all(12),
                                      decoration: BoxDecoration(
                                        color: Colors.red.withValues(alpha: 0.05),
                                        borderRadius: BorderRadius.circular(8),
                                        border: Border.all(color: Colors.red.withValues(alpha: 0.2)),
                                      ),
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          Row(
                                            children: [
                                              Icon(Icons.error_outline, color: Colors.red, size: 18),
                                              const SizedBox(width: 8),
                                              Text(TrilingualService.instance.getUIText('Why your answer was incorrect'), style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: Colors.red.shade800)),
                                            ],
                                          ),
                                          const SizedBox(height: 8),
                                          Text(distractorText, style: GoogleFonts.inter(color: Colors.red.shade900)),
                                        ],
                                      ),
                                    ),
                                  ],
                                );
                              }
                            ),
                          ],
                        ],
                      ),
                    ),
                  ],
                ),
              );
            }),
            const SizedBox(height: 32),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.primary,
                foregroundColor: Colors.white,
                minimumSize: const Size(double.infinity, 56),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              ),
              onPressed: () {
                context.pop();
              },
              child: Text(TrilingualService.instance.getUIText('Return to Curriculum'), style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16)),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStat(String label, int value, Color color) {
    return Column(
      children: [
        Text(value.toString(), style: GoogleFonts.inter(fontSize: 24, fontWeight: FontWeight.bold, color: color)),
        Text(label, style: GoogleFonts.inter(fontSize: 12, color: Colors.grey.shade600)),
      ],
    );
  }
}
