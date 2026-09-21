import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model formal and informal letters covering the situations most
/// commonly asked in GSEB and CBSE Class 11 papers.
class LettersFormalInformalModelsWidget extends StatelessWidget {
  const LettersFormalInformalModelsWidget({super.key});

  static const _formatPoints = [
    'Sender\'s address and date at the top left (or top right in some board formats — follow what your teacher/board sample paper uses).',
    'Formal letters add the receiver\'s designation and address, then a one-line subject stating the purpose, before the salutation.',
    'Salutation: "Dear Sir/Madam" for an unknown authority, "Dear Mr./Ms. [Name]" if named; "Dear [first name]" for an informal letter.',
    'Body in 2–3 clear paragraphs: reason for writing, details/explanation, and a polite closing request or wish.',
    'Complimentary close: "Yours faithfully" after "Dear Sir/Madam"; "Yours sincerely" after a named formal salutation; "Yours affectionately"/"Love" for informal letters.',
    'Sign off with your name only (no surname needed in an informal letter to family/friends).',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a formal letter to the Editor of a newspaper expressing your concern about the increasing noise pollution in your locality due to loudspeakers and traffic.',
      wordCount: '~120–150 words',
      modelAnswer: '''
                                            24, Shanti Nagar Society
                                            Rajkot – 360001
                                            5 July 2025

The Editor
The Gujarat Herald
Rajkot

Subject: Rising Noise Pollution in Residential Areas

Dear Sir/Madam,

Through the columns of your esteemed newspaper, I
wish to draw the attention of the concerned
authorities to the alarming rise in noise pollution
in our locality, Shanti Nagar.

Loudspeakers blaring late into the night during
functions, and constant honking by vehicles on the
narrow lanes, have made it difficult for students to
study and for elderly residents to rest. Despite
several verbal complaints to the local ward office,
no action has been taken so far.

I request the municipal authorities to strictly
enforce the permissible noise limits and take action
against repeated offenders. I hope this letter will
draw prompt attention to the problem.

Yours faithfully,
Arjun Mehta''',
    ),
    WritingPrompt(
      prompt: 'Write a formal letter to the Principal of your school requesting a week\'s leave of absence as you need to accompany your family on an urgent trip.',
      wordCount: '~100–120 words',
      modelAnswer: '''
                                            B-14, Sarvodaya Society
                                            Ahmedabad – 380015
                                            2 October 2025

The Principal
Sunrise Public School
Ahmedabad

Subject: Application for Leave of Absence

Dear Madam,

I am Kavya Desai, a student of Class XI-B, Roll No.
17. I am writing to request leave from school for one
week, from 6 to 11 October 2025, as I have to
accompany my parents on an urgent family visit to my
grandfather, who is unwell.

I assure you that I will complete all pending
assignments and cover the missed syllabus with the
help of my classmates immediately upon my return. I
request you to kindly grant me leave for the
mentioned period.

Yours sincerely,
Kavya Desai''',
    ),
    WritingPrompt(
      prompt: 'Write an informal letter to your younger cousin advising them on how to manage time between studies and extracurricular activities.',
      wordCount: '~100–120 words',
      modelAnswer: '''
                                            42, Green Park Avenue
                                            Surat
                                            14 January 2026

Dear Ishaan,

I heard from Mausi that you have been feeling
overwhelmed juggling your basketball practice and the
Class X board exam preparation. I remember feeling
exactly the same way, so I thought I would share a
few things that helped me.

Try making a simple weekly timetable, and stick to
short, focused study sessions of about 45 minutes
instead of long, tiring ones. Do not drop
basketball completely — it will actually help you
return to your books with a fresher mind. Also, sleep
on time; tired brains forget everything by morning!

Take care, and call me if you want to talk it
through.

Love,
Riya''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Formal & Informal Letters — Model Answers',
      icon: Icons.mail_outline,
      accent: Colors.indigo,
      description: 'Complete letters you can study line by line, covering both formal and informal situations.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
