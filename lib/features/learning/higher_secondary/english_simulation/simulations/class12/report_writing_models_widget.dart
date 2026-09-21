import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model newspaper/event reports in the exact format board
/// examiners expect: headline, byline, and the 5 Ws and H.
class ReportWritingModelsWidget extends StatelessWidget {
  const ReportWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Headline: short, catchy, summarises the event — no full sentence needed.',
    'Byline: reporter\'s name and place, just below the headline (e.g. "By Neha Kulkarni, Surat").',
    'Opening line covers the most important facts: what happened, when, and where.',
    'Body answers the remaining 5 Ws and H (who, why, how) and may include a quoted eyewitness or official statement for credibility.',
    'Written in past tense, third person, in an objective, factual tone — no personal opinions.',
    'Organised in the "inverted pyramid" style: most essential information first, minor details last.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a newspaper report on an Annual Cultural Festival organised by your school, covering the main events and highlights.',
      wordCount: '~150 words',
      modelAnswer: '''
      SCHOOL'S ANNUAL CULTURAL FEST DRAWS HUGE CROWD
                    By Kabir Ahuja, Vadodara

Riverside Public School celebrated its Annual
Cultural Festival, "Rangotsav", on 14 December 2025
at its main campus, drawing enthusiastic participation
from over 800 students and parents.

The day-long event featured classical and Bollywood
dance performances, a battle-of-bands music
competition, and a street play highlighting the
importance of water conservation. The chief guest,
noted classical vocalist Ms. Radhika Iyer, praised the
students' talent and discipline.

"Events like these give students a platform to
explore talents beyond textbooks," said Principal Mr.
S. K. Verma while addressing the gathering.

The festival concluded with a prize distribution
ceremony, where Class XI-B was declared the overall
winner. Teachers and students alike hailed the event
as one of the most memorable in recent years.''',
    ),
    WritingPrompt(
      prompt: 'Write a newspaper report on a heavy rainfall that caused waterlogging and disrupted normal life in your city.',
      wordCount: '~150 words',
      modelAnswer: '''
      HEAVY RAINS THROW CITY LIFE OUT OF GEAR
                    By Simran Kaur, Ahmedabad

Ahmedabad witnessed one of its heaviest spells of
rainfall this monsoon on 19 August 2025, with over
120 mm recorded within six hours, leading to severe
waterlogging across several low-lying areas of the
city.

Major roads near Maninagar and Naranpura were
submerged under nearly two feet of water, forcing
commuters to wade through flooded streets and
causing long traffic snarls that lasted well into the
evening. Several schools declared an early closure as
a precautionary measure.

"We have deployed additional pumps to clear the
water, and the situation is expected to improve by
tomorrow morning," said a Municipal Corporation
official.

While no major casualties were reported, residents
have urged the civic body to improve the city's
drainage infrastructure ahead of future monsoons.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Report Writing — Model Answers',
      icon: Icons.description,
      accent: Colors.blueGrey,
      description: 'Full newspaper-style reports, headline to byline, exactly as examiners expect them.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
