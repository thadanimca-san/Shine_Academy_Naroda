import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model dialogues on the situations GSEB most commonly sets:
/// natural, turn-by-turn conversations that stay focused and resolve
/// logically.
class DialogueWritingSimulationWidget extends StatelessWidget {
  const DialogueWritingSimulationWidget({super.key});

  static const _formatPoints = [
    'Each turn: speaker\'s name, a colon, then their line — one turn per line, never merged together.',
    'Write the way people actually talk: contractions, short sentences, questions, the occasional interruption.',
    'Every reply should genuinely respond to what was just said — no line should feel randomly inserted.',
    'Stay strictly within the given situation and include the specific details it asks for (date, place, reason, etc.).',
    'Structure: a natural opening (greeting/context), a middle where the actual matter is discussed, and a close that resolves it.',
    'Typically 8–12 exchanges (turns) total for a board-level answer — long enough to develop, short enough to stay natural.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a dialogue between a student and a librarian, where the student wants to renew a borrowed book but has lost the library card.',
      wordCount: '~8–10 exchanges',
      modelAnswer: '''
Riya: Good afternoon! I'd like to renew this book,
      please — I still need it for my project.

Librarian: Sure, may I see your library card?

Riya: That's the problem — I think I've misplaced
      it. Can you look it up with my name instead?

Librarian: I can try. What's your name and class?

Riya: Riya Malhotra, Class XI-B.

Librarian: (checking the register) Found it. This
      book was due yesterday, so there's a small
      fine of five rupees.

Riya: Oh, I didn't realise. I'll pay that right
      away. Can it be renewed for two more weeks?

Librarian: Yes, that's fine. But please get a
      duplicate card made from the office by
      tomorrow — you'll need it for future
      borrowing.

Riya: I will, definitely. Thank you so much for your
      help!

Librarian: You're welcome. Enjoy your reading!''',
    ),
    WritingPrompt(
      prompt: 'Write a dialogue between two friends discussing how to prepare for their upcoming board examinations.',
      wordCount: '~8–10 exchanges',
      modelAnswer: '''
Aryan: Have you started revising for the boards yet?
       I'm honestly a bit panicked.

Meera: A little, but I feel scattered. I don't know
       whether to finish the syllabus first or start
       solving previous papers.

Aryan: I read that solving at least five years of
       question papers helps you spot the important
       topics quickly.

Meera: That's a good idea. Maybe we could do that
       together on weekends and discuss the tricky
       questions?

Aryan: Definitely! We could also make a shared
       timetable so neither of us falls behind.

Meera: Agreed. I think two hours each for Physics
       and Chemistry, and one hour for English,
       every day should work.

Aryan: Sounds solid. Let's also promise not to touch
       our phones during study hours.

Meera: Deal! Let's start tomorrow morning — no more
       procrastinating.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Dialogue Writing — Model Answers',
      icon: Icons.forum,
      accent: Colors.pink,
      description: 'Natural, turn-by-turn dialogues on the everyday situations examiners set.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
