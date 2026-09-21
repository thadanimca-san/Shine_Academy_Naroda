import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete, board-ready model notices a student can study directly —
/// covering the situations GSEB and CBSE most commonly set as questions.
class NoticeWritingModelsWidget extends StatelessWidget {
  const NoticeWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Name of the issuing school/organisation, centred, at the very top.',
    'The word "NOTICE" centred and underlined just below it.',
    'A short, clear title/subject describing what the notice is about.',
    'Date of issue, placed on the left (title/subject may sit on the right of the same line).',
    'Body in about 50 words, answering What, When, Where, and Who to contact — no unnecessary detail.',
    'Writer\'s name and designation at the bottom right (never just a first name).',
    'The whole notice is enclosed in a box when handwritten on an answer sheet.',
    'Formal, impersonal, third-person tone — avoid "I" unless the notice is issued by a named individual acting officially.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'As the Head Boy/Girl of your school, write a notice informing students about the Annual Inter-House Sports Day and inviting them to register for events.',
      wordCount: '~50 words',
      modelAnswer: '''
              DELHI PUBLIC SCHOOL, VADODARA

                       NOTICE

18 August 2025                    Inter-House Sports Day

All students of Classes IX to XII are informed
that the Annual Inter-House Sports Day will be
held on 28 August 2025 at the school ground from
8:00 a.m. onwards. Students wishing to participate
in athletics, kabaddi, or relay events must submit
their names to their respective Physical Education
teacher by 23 August 2025. Sports uniform is
compulsory for all participants.

                                    Ananya Shah
                                    Head Girl''',
    ),
    WritingPrompt(
      prompt: 'Write a notice on behalf of the Red Cross Club of your school announcing a blood donation camp and appealing to eligible students and staff to participate.',
      wordCount: '~50 words',
      modelAnswer: '''
                ST. XAVIER'S SCHOOL, AHMEDABAD

                       NOTICE

3 September 2025               Blood Donation Camp

The Red Cross Club is organising a Blood Donation
Camp in collaboration with the Red Cross Society on
10 September 2025 in the school auditorium from
9:00 a.m. to 1:00 p.m. All healthy students above
18 years of age and staff members are encouraged to
donate blood and support this noble cause. Interested
donors should register with their class teacher by
6 September 2025.

                                    Rohan Patel
                                    Secretary, Red Cross Club''',
    ),
    WritingPrompt(
      prompt: 'As the Librarian of your school, write a notice informing students that the library will remain closed for stock verification and requesting them to return all borrowed books before the given date.',
      wordCount: '~50 words',
      modelAnswer: '''
                  KENDRIYA VIDYALAYA, SURAT

                       NOTICE

12 November 2025               Library Closure Notice

All students are informed that the school library
will remain closed from 20 to 27 November 2025 for
annual stock verification. Students are requested to
return all borrowed books to the library counter on
or before 19 November 2025. No new books will be
issued during this period. Cooperation of all
students is earnestly requested.

                                    Meera Joshi
                                    Librarian''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Notice Writing — Model Answers',
      icon: Icons.announcement,
      accent: Colors.orange,
      description: 'Study these complete, board-ready notices, then try writing your own before checking the model answer.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
