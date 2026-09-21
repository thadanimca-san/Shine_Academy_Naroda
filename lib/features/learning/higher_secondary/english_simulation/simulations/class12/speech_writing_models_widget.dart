import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model speeches and a debate speech, written to sound natural
/// when read aloud — the way board examiners expect this genre to be
/// answered.
class SpeechWritingModelsWidget extends StatelessWidget {
  const SpeechWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Open with a respectful address to the audience: "Good morning, respected Principal, teachers, and dear friends."',
    'Follow immediately with a hook — a question, statistic, or short anecdote — to capture attention.',
    'Body: build the argument logically across 2–3 points, using rhetorical questions, repetition, or examples to persuade.',
    'A debate speech must take one clear side ("for" or "against") and briefly acknowledge, then counter, the opposing view.',
    'Write in a spoken, natural rhythm — shorter sentences than an essay, since it will be read aloud.',
    'End with a strong, memorable closing line and a thank-you note to the audience.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a speech to be delivered in your school assembly on the topic "The Importance of Time Management for Students".',
      wordCount: '~150–200 words',
      modelAnswer: '''
Good morning, respected Principal, teachers, and my
dear friends.

Have you ever reached the end of a day and wondered
where all the hours went? If so, you are not alone —
and that is exactly why I want to talk to you today
about time management.

As students, we often feel that there simply isn't
enough time for studies, sports, hobbies, and rest,
all at once. But the truth is, it is rarely a shortage
of time — it is a shortage of planning. A student who
spends fifteen minutes each morning listing the day's
priorities almost always accomplishes more than one
who simply reacts to whatever comes up.

Time management is not about filling every minute
with work; it is about making space for what truly
matters, and cutting out what doesn't — like
mindlessly scrolling through our phones for hours.

Friends, our time in school is limited, but what we
build with it — our habits, our discipline — will
stay with us for life. Let us learn to master our
clocks before they master us.

Thank you.''',
    ),
    WritingPrompt(
      prompt: 'Write a debate speech either for or against the motion: "Examinations Should Be Abolished in Schools."',
      wordCount: '~150–200 words',
      modelAnswer: '''
Good morning, respected judges, teachers, and my
fellow debaters. I stand today to speak AGAINST the
motion that examinations should be abolished in
schools.

Those in favour of this motion argue that exams
create unnecessary stress and reduce learning to rote
memorisation. I do not deny that poorly designed
exams can do this. But the solution is to reform how
we test, not to remove testing altogether.

Examinations serve a purpose no textbook can replace:
they measure whether a concept has actually been
understood, and they teach students the discipline of
working towards a deadline — a skill every
professional needs later in life. Without any form of
assessment, how would a teacher know which student
needs extra support, or a university know whom to
admit?

The problem, friends, is not the exam itself, but an
excessive focus on marks over genuine understanding.
Let us reform the system — with more practical and
project-based assessments — rather than throw away a
tool that, used well, drives real learning.

Thank you.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Speech & Debate Writing — Model Answers',
      icon: Icons.record_voice_over,
      accent: Colors.brown,
      description: 'Full speeches written to sound natural when read aloud, plus a complete debate speech.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
