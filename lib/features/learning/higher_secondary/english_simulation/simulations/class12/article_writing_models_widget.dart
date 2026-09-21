import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model articles on the topics GSEB and CBSE board papers
/// repeatedly draw from: social issues, technology, and youth concerns.
class ArticleWritingModelsWidget extends StatelessWidget {
  const ArticleWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Catchy title, centred, followed by the writer\'s name just below it.',
    'Introduction: hook the reader (a fact, question, or scenario) and state the topic clearly.',
    'Body (2–3 paragraphs): develop the argument with examples, causes/effects, or reasoning — never just a list of unconnected facts.',
    'Conclusion: summarise the key idea and end with a takeaway, opinion, or call to action.',
    'Personal, persuasive, or reflective tone — more opinionated than a report, but still organised into clear paragraphs.',
    'No salutation or complimentary close — an article is not addressed to anyone in particular.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write an article for your school magazine on "The Impact of Social Media on Today\'s Youth".',
      wordCount: '~150–200 words',
      modelAnswer: '''
        THE IMPACT OF SOCIAL MEDIA ON TODAY'S YOUTH
                        By Aditi Sharma

Scroll, like, comment, repeat — this is how many
young people now spend a large part of their day.
Social media has undeniably transformed the way our
generation communicates, learns, and even thinks
about itself.

On the positive side, platforms like Instagram and
YouTube have made information, learning resources,
and global connections more accessible than ever.
Students can follow educators, join study groups, and
showcase their talents to a wide audience.

However, the same platforms have also fuelled
anxiety, sleep disruption, and an unhealthy obsession
with likes and appearances. Constant comparison with
curated, filtered lives online often leaves teenagers
feeling inadequate, while endless scrolling eats into
time meant for study, sleep, and real conversations.

Social media itself is neither good nor bad — it is a
tool. The real challenge for today's youth is learning
to use it with discipline rather than letting it use
them. A balanced approach, with fixed screen-time
limits and genuine offline relationships, is the need
of the hour.''',
    ),
    WritingPrompt(
      prompt: 'Write an article on "Global Warming: A Growing Threat" highlighting its causes and the steps needed to address it.',
      wordCount: '~150–200 words',
      modelAnswer: '''
            GLOBAL WARMING: A GROWING THREAT
                        By Rohan Mehta

Every summer now feels hotter than the last, and
that is not merely a feeling — it is a fact backed by
decades of scientific data. Global warming, driven
largely by human activity, has become one of the most
urgent challenges of our time.

The relentless burning of fossil fuels for electricity
and transport, large-scale deforestation, and
unchecked industrial emissions have steadily pushed
up the concentration of greenhouse gases in our
atmosphere. The consequences are already visible:
melting glaciers, rising sea levels, erratic monsoons,
and increasingly frequent natural disasters.

Reversing this trend demands action at every level.
Governments must invest in renewable energy and
enforce stricter emission standards, industries must
adopt cleaner technologies, and individuals must
make conscious choices — using public transport,
conserving electricity, and planting trees.

Global warming does not respect borders, and neither
should our response to it. The time to act is not
tomorrow; it is now, before the damage becomes
irreversible.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Article Writing — Model Answers',
      icon: Icons.article,
      accent: Colors.purple,
      description: 'Full articles on the topics examiners return to again and again.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
