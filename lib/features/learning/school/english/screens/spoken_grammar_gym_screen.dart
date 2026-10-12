import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../../foundation/theme/brand_app_bar.dart';
import '../data/practice_topics.dart';
import '../models/practice_question.dart';
import 'practice_session_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../shared/widgets/activation_gate.dart';

class SpokenGrammarGymScreen extends StatefulWidget {
  const SpokenGrammarGymScreen({super.key});

  @override
  State<SpokenGrammarGymScreen> createState() => _SpokenGrammarGymScreenState();
}

class _SpokenGrammarGymScreenState extends State<SpokenGrammarGymScreen> {
  int _selectedFilterIndex = 0;

  final List<String> _filters = [
    'All Workouts',
    '🟢 Foundations',
    '🟡 Sentences',
    '🔵 Spoken Fluency',
    '🏆 Advanced Mastery',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8FAFC),
      appBar: BrandAppBar(
        title: TrilingualService.instance.getUIText('Spoken Grammar Gym'),
      ),
      body: Column(
        children: [
          // Header Banner
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [Colors.blue.shade800, Colors.indigo.shade900],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.15),
                    shape: BoxShape.circle,
                  ),
                  child: const Text('🏋️', style: TextStyle(fontSize: 26)),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        TrilingualService.instance.getUIText('Grammar Practice & Mastery'),
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        TrilingualService.instance.getUIText('Learn by doing: 10-question instant interactive drills with trilingual answers'),
                        style: GoogleFonts.inter(
                          color: Colors.white70,
                          fontSize: 12,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),

          // Workout Filter Chips
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
            child: Row(
              children: List.generate(_filters.length, (index) {
                final isSelected = _selectedFilterIndex == index;
                return Padding(
                  padding: const EdgeInsets.only(right: 8.0),
                  child: ChoiceChip(
                    label: Text(TrilingualService.instance.getUIText(_filters[index])),
                    selected: isSelected,
                    onSelected: (val) {
                      if (val) setState(() => _selectedFilterIndex = index);
                    },
                    selectedColor: Colors.blue.shade100,
                    labelStyle: TextStyle(
                      color: isSelected ? Colors.blue.shade900 : Colors.grey.shade700,
                      fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                      fontSize: 13,
                    ),
                  ),
                );
              }),
            ),
          ),

          // Workout Sections List
          Expanded(
            child: ListView(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              children: [
                if (_selectedFilterIndex == 0 || _selectedFilterIndex == 1)
                  _buildSection(
                    title: '🟢 Foundation Workout (बुनियादी व्याकरण)',
                    subtitle: 'Master nouns, verbs, pronouns, and prepositions for error-free daily speaking',
                    color: const Color(0xFF10B981),
                    topics: [
                      _topicWithDetails(practiceTopicsByGrade['Class 3']![1], 'Nouns (संज्ञा & Naming Words)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 3']![4], 'Verbs & Action Words (क्रिया)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 4']![3], 'Pronouns (सर्वनाम: I, He, She, They)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 3']![0], 'Adjectives (विशेषण & Descriptions)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 3']![2], 'Prepositions (संबंधबोधक: in, on, at, under)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 3']![3], 'Singular & Plural (एकवचन व बहुवचन)'),
                    ],
                  ),

                if (_selectedFilterIndex == 0 || _selectedFilterIndex == 2)
                  _buildSection(
                    title: '🟡 Sentence Construction Workout (वाक्य निर्माण)',
                    subtitle: 'Craft clear, complete English sentences with correct tenses and connectors',
                    color: const Color(0xFFF59E0B),
                    topics: [
                      _topicWithDetails(practiceTopicsByGrade['Class 4']![0], 'Articles (A, An, The का सही प्रयोग)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 4']![4], 'Tenses in Action (Present, Past, Future काल)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 5']![4], 'Sentence Types (प्रश्न, आदेश व कथन)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 5']![2], 'Conjunctions (जोड़ने वाले शब्द: and, but, so)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 5']![1], 'Adverbs (क्रियाविशेषण: quickly, easily)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 5']![3], 'Punctuation & Capitalization (विराम चिह्न)'),
                    ],
                  ),

                if (_selectedFilterIndex == 0 || _selectedFilterIndex == 3)
                  _buildSection(
                    title: '🔵 Spoken Fluency Workout (धाराप्रवाह व्याकरण)',
                    subtitle: 'Speak with authority: modal verbs, active/passive voice, and reported speech',
                    color: const Color(0xFF6366F1),
                    topics: [
                      _topicWithDetails(practiceTopicsByGrade['Class 6']![2], 'Modal Verbs (Can, Could, Should, Would, May)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 6']![4], 'Active & Passive Voice (कर्मवाच्य व कर्तृवाच्य)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 6']![3], 'Direct & Indirect Speech (कही हुई बात का वर्णन)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 6']![0], 'Clauses & Connectors (उपवाक्य व संयोजन)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 9']![1], 'Conditionals (If... Then... शर्त वाले वाक्य)'),
                    ],
                  ),

                if (_selectedFilterIndex == 0 || _selectedFilterIndex == 4)
                  _buildSection(
                    title: '🏆 Advanced Mastery Workout (उच्च स्तरीय व्याकरण)',
                    subtitle: 'Professional English: concord, gerunds, error spotters, and integrated grammar',
                    color: const Color(0xFF0284C7),
                    topics: [
                      _topicWithDetails(practiceTopicsByGrade['Class 7']![3], 'Subject-Verb Concord (कर्ता-क्रिया सामंजस्य)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 7']![0], 'Non-Finites (Infinitives, Gerunds & Participles)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 6']![1], 'Determiners & Quantifiers (Some, Any, Much, Many)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 9']![2], 'Error Spotting & Editing (गलती सुधार अभ्यास)'),
                      _topicWithDetails(practiceTopicsByGrade['Class 10']![1], 'Integrated Spoken Grammar (सम्पूर्ण व्याकरण ड्रिल)'),
                    ],
                  ),
                const SizedBox(height: 24),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Map<String, dynamic> _topicWithDetails(PracticeTopic topic, String customTitle) {
    return {
      'topic': topic,
      'title': customTitle,
    };
  }

  Widget _buildSection({
    required String title,
    required String subtitle,
    required Color color,
    required List<Map<String, dynamic>> topics,
  }) {
    final sectionWidget = Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.grey.shade200),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.03),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: color.withValues(alpha: 0.08),
              borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
              border: Border(bottom: BorderSide(color: color.withValues(alpha: 0.2))),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  TrilingualService.instance.getUIText(title),
                  style: GoogleFonts.poppins(
                    fontWeight: FontWeight.bold,
                    fontSize: 15,
                    color: color,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  TrilingualService.instance.getUIText(subtitle),
                  style: GoogleFonts.inter(
                    fontSize: 11.5,
                    color: Colors.grey.shade700,
                  ),
                ),
              ],
            ),
          ),
          ListView.separated(
            padding: const EdgeInsets.all(12),
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: topics.length,
            separatorBuilder: (_, _) => const Divider(height: 12, color: Color(0xFFF1F5F9)),
            itemBuilder: (context, index) {
              final item = topics[index];
              final PracticeTopic topic = item['topic'] as PracticeTopic;
              final String displayTitle = item['title'] as String;

              return InkWell(
                borderRadius: BorderRadius.circular(8),
                onTap: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => PracticeSessionScreen(topic: topic),
                    ),
                  );
                },
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 6),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: color.withValues(alpha: 0.12),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Icon(Icons.fitness_center_rounded, color: color, size: 20),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              displayTitle,
                              style: GoogleFonts.poppins(
                                fontWeight: FontWeight.w600,
                                fontSize: 13.5,
                                color: const Color(0xFF1E293B),
                              ),
                            ),
                            Text(
                              '${topic.bank.length} questions in bank · 10 questions per set',
                              style: GoogleFonts.inter(
                                fontSize: 11,
                                color: Colors.grey.shade600,
                              ),
                            ),
                          ],
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: BoxDecoration(
                          color: color.withValues(alpha: 0.1),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Row(
                          children: [
                            Text(
                              TrilingualService.instance.getUIText('Start'),
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                                color: color,
                              ),
                            ),
                            const SizedBox(width: 4),
                            Icon(Icons.arrow_forward_ios_rounded, size: 10, color: color),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              );
            },
          ),
        ],
      ),
    );

    final bool isSkillup = (appFlavor ?? 'default') == 'skillup';
    if (!isSkillup) return sectionWidget;

    return ActivationGate(
      isFree: false,
      onActivated: () => setState(() {}),
      child: sectionWidget,
    );
  }
}
