import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete, full-length model essays on the topics GSEB HSC and CBSE
/// Class 12 papers return to most often — written at the depth and word
/// count a board examiner expects.
class EssayWritingSimulationWidget extends StatelessWidget {
  const EssayWritingSimulationWidget({super.key});

  static const _formatPoints = [
    'Introduction (1 paragraph): state the topic, draw the reader in with a fact, question, or brief context.',
    'Body (2–3 paragraphs): one clear idea per paragraph, each supported with examples or reasoning, connected with linking words.',
    'Conclusion (1 paragraph): summarise the argument and close with a reflection, opinion, or call to action — no new ideas here.',
    'Maintain one consistent tone throughout (reflective, persuasive, or analytical, depending on the topic).',
    'Plan for about 300–350 words — long enough to develop ideas, short enough to stay focused within exam time.',
    'No title/byline formatting needed like an article — just a heading naming the topic, then straight into the essay.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write an essay on the topic "Education: The Key to National Development".',
      wordCount: '~300–350 words',
      modelAnswer: '''
        EDUCATION: THE KEY TO NATIONAL DEVELOPMENT

A nation's greatest resource is not its minerals or
its factories, but the minds of its people — and it
is education that shapes those minds. From ancient
gurukuls to modern digital classrooms, the pursuit of
knowledge has always been the foundation on which
civilisations build their future.

Education does far more than teach students to read
and write; it equips them with the ability to think
critically, solve problems, and adapt to a rapidly
changing world. A well-educated population drives
innovation, strengthens democratic institutions
through informed citizenship, and reduces social
inequality by opening doors that would otherwise
remain closed to the underprivileged. Countries that
have invested heavily in education — from Japan's
post-war recovery to South Korea's economic rise —
demonstrate how literacy and skill-building translate
directly into national prosperity.

However, access to quality education remains uneven
in many parts of the world, including in rural and
economically weaker regions of our own country.
Overcrowded classrooms, a shortage of trained
teachers, and the lingering digital divide continue
to prevent countless children from receiving the
education they deserve. Addressing this requires
sustained investment — not just in infrastructure, but
in teacher training, curriculum reform, and equal
access to technology.

Equally important is shifting our understanding of
what education should achieve. Rote memorisation for
examinations must give way to genuine understanding,
creativity, and practical skill development, preparing
students not just to pass tests but to meaningfully
contribute to society.

In conclusion, no nation can hope to progress while
neglecting the education of its people. If we are
serious about building a stronger, more equitable
future, investment in accessible, quality education
must remain our foremost national priority — for an
educated citizen today is the architect of a
developed nation tomorrow.''',
    ),
    WritingPrompt(
      prompt: 'Write an essay on the topic "The Role of Technology in Modern Life".',
      wordCount: '~300–350 words',
      modelAnswer: '''
          THE ROLE OF TECHNOLOGY IN MODERN LIFE

Barely a generation ago, sending a message across the
world took days; today, it takes seconds. Technology
has woven itself so completely into our daily
routines that most of us can no longer imagine life
without it — and this transformation carries both
remarkable promise and real concern.

On one hand, technology has dramatically improved the
quality of human life. Advances in medicine have
extended life expectancy and cured diseases once
considered fatal. The internet has democratised access
to information, allowing a student in a small town to
learn from the same online lectures as one in a major
city. Communication technology keeps families
connected across continents, and automation has made
industries more efficient, freeing up human effort for
more creative and strategic work.

Yet, this rapid technological growth has not come
without cost. Excessive dependence on smartphones and
social media has been linked to shrinking attention
spans, disrupted sleep, and rising anxiety, especially
among young people. Automation, while boosting
efficiency, has also displaced workers in certain
traditional industries, widening the gap between those
equipped with digital skills and those left behind.
Moreover, concerns over data privacy and cybercrime
have grown alongside our increasing reliance on
digital systems.

The challenge before us, therefore, is not to reject
technology, but to use it wisely. This means teaching
digital literacy alongside digital access, encouraging
mindful and balanced use of devices, and building
strong safeguards around data and privacy.

In conclusion, technology is a powerful tool that can
either uplift or overwhelm us, depending on how
responsibly we wield it. As we move further into a
digitally driven future, the real measure of progress
will not be how advanced our technology becomes, but
how wisely we choose to use it.''',
    ),
    WritingPrompt(
      prompt: 'Write an essay on the topic "Environmental Pollution: Causes and Solutions".',
      wordCount: '~300–350 words',
      modelAnswer: '''
        ENVIRONMENTAL POLLUTION: CAUSES AND SOLUTIONS

The air over many of our cities now carries a visible
haze, and rivers that once ran clear are choked with
waste. Environmental pollution, once a distant
concern, has become one of the most pressing crises of
our time, threatening both human health and the
planet's delicate ecological balance.

The causes of this crisis are largely rooted in human
activity. Rapid industrialisation and the unchecked
burning of fossil fuels release harmful gases into the
atmosphere, contributing to both air pollution and
climate change. Untreated industrial and domestic
waste continues to contaminate our rivers and
groundwater, while the widespread use of plastic —
much of which is neither biodegradable nor properly
recycled — pollutes land and oceans alike.
Deforestation, driven by the demand for agricultural
land and timber, further weakens nature's own ability
to absorb pollutants and regulate the climate.

The consequences are already visible around us:
rising respiratory illnesses in urban populations,
disappearing biodiversity, and increasingly erratic
weather patterns that disrupt agriculture and
livelihoods.

Addressing this crisis demands coordinated action at
every level. Governments must enforce stricter
emission and waste-disposal regulations, while
investing in renewable energy sources such as solar
and wind power to reduce dependence on fossil fuels.
Industries must adopt cleaner production methods and
responsible waste management. At the individual level,
simple choices — reducing plastic use, conserving
water and electricity, using public transport, and
planting trees — collectively make a meaningful
difference.

In conclusion, environmental pollution is a crisis of
our own making, and therefore one within our power to
solve. It calls for urgent, collective responsibility
from governments, industries, and citizens alike,
because the health of our planet — and of every
generation to come — depends on the choices we make
today.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Essay Writing — Model Answers',
      icon: Icons.edit_note,
      accent: Colors.deepPurple,
      description: 'Full-length, board-ready essays on the topics examiners return to again and again.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
