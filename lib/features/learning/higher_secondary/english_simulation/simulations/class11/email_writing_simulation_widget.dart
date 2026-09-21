import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model formal and informal emails covering the situations most
/// commonly asked in GSEB and CBSE Class 11 papers.
class EmailWritingSimulationWidget extends StatelessWidget {
  const EmailWritingSimulationWidget({super.key});

  static const _formatPoints = [
    'To: recipient\'s email address, and a specific, informative Subject line — never left blank or vague.',
    'Salutation: "Dear Sir/Madam" or "Respected Sir/Madam" for a formal email; "Hi/Hello [name]" for an informal one.',
    'First line states the purpose directly — an email is read quickly, so do not delay the point.',
    'Body in short paragraphs or points; formal emails avoid abbreviations, slang, and emojis.',
    'Closing: "Regards" / "Yours sincerely" for formal emails; "Best" / "Take care" / "Love" for informal ones — followed by your full name.',
    'Keep formal emails concise (well under 200 words) — long emails are less likely to be read carefully.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a formal email to your class teacher requesting an extension for submitting a project due to a family emergency.',
      wordCount: '~100–120 words',
      modelAnswer: '''
To: teacher.sharma@brightschool.edu
Subject: Request for Extension — Physics Project Submission

Respected Ma'am,

I am Karan Bhatt from Class XI-A. I am writing to
request a short extension for submitting my Physics
project, originally due on 12 September.

My grandmother was hospitalised over the weekend, and
I had to travel with my family to be with her, which
left me unable to complete the project on time. I
have already finished most of the work and would need
just three additional days to submit it properly.

I sincerely apologise for the inconvenience and
assure you this will not affect the quality of my
work. I would be grateful if you could kindly grant
this extension.

Regards,
Karan Bhatt
Class XI-A, Roll No. 22''',
    ),
    WritingPrompt(
      prompt: 'Write a formal email to the customer support team of an online learning platform reporting a technical issue with accessing your course videos.',
      wordCount: '~100–120 words',
      modelAnswer: '''
To: support@learnwise.com
Subject: Unable to Access Purchased Course Videos

Dear Sir/Madam,

I am writing to report a technical issue with my
account (registered email: neha.d123@gmail.com). Since
yesterday, I have been unable to play any video
lectures in the "Class 12 Chemistry" course I
purchased on 3 January, despite a stable internet
connection. The screen simply shows a loading icon
that never completes.

I have already tried logging out and back in, and
clearing my browser cache, but the issue persists.
Since my exams are approaching, I would appreciate a
quick resolution.

Please let me know if you need any further
information from my end.

Regards,
Neha Deshmukh''',
    ),
    WritingPrompt(
      prompt: 'Write an informal email to a friend inviting them to your birthday celebration and sharing details of the plan.',
      wordCount: '~80–100 words',
      modelAnswer: '''
To: arjun.friend@gmail.com
Subject: You're Invited — My Birthday This Saturday!

Hey Arjun,

Guess what — my birthday is this Saturday, and I'm
throwing a small get-together at my place from 5 pm
onwards! We're planning some music, games, and of
course, cake.

It won't be the same without you, so please try to
make it. A few of the gang from the cricket team are
coming too, so it should be a fun evening.

Let me know if you can come, and feel free to bring
your guitar along!

Best,
Yash''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Email Writing — Model Answers',
      icon: Icons.email,
      accent: Colors.cyan,
      description: 'Complete formal and informal emails you can study directly, covering the situations boards commonly ask about.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
