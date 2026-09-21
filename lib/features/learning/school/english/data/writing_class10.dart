import '../models/writing_prompt.dart';

const class10Writing = WritingLibrary(
  id: 'class10_writing',
  title: 'Essay, Letter & Report Writing',
  grade: 'Class 10',
  prompts: [
    WritingPrompt(
      id: 'class10_writing_essay_ai_jobs',
      title: 'Essay: Will Artificial Intelligence Take Away Our Jobs?',
      sceneEmoji: '🤖',
      sceneDescription:
          'Write a well-structured argumentative essay (about 200-220 words) discussing whether artificial '
          'intelligence poses a genuine threat to employment, examining evidence on both sides before reaching '
          'a reasoned conclusion.',
      wordBank: [
        'automation',
        'displacement',
        'upskilling',
        'productivity',
        'transition',
        'obsolete',
        'adaptability',
        'workforce',
        'disruption',
        'unprecedented',
      ],
      modelAnswer:
          'Few questions provoke as much anxiety in contemporary discourse as whether artificial intelligence '
          'will render human labour largely obsolete. This concern is not without foundation: automation has '
          'already displaced workers in sectors ranging from manufacturing to basic customer service, and '
          'increasingly sophisticated AI systems now perform tasks once considered exclusively human, including '
          'aspects of writing, analysis, and even certain diagnostic medical work.\n\n'
          'However, historical precedent offers a more nuanced perspective than pure alarm suggests. Previous '
          'waves of technological disruption, from mechanised agriculture to computerisation, did eliminate '
          'specific jobs, yet they also created entirely new categories of employment that earlier generations '
          'could not have anticipated. The critical difference this time may be the speed of transition: '
          'AI-driven change appears to be unfolding faster than the workforce\'s capacity for adaptation and '
          'upskilling, potentially creating painful transitional unemployment even if new jobs eventually '
          'emerge to replace old ones.\n\n'
          'Rather than viewing this as an unstoppable, purely negative force, the more productive response '
          'likely lies in deliberate preparation: education systems emphasising adaptability and skills less '
          'easily automated, such as complex judgement and interpersonal work, alongside genuine policy support '
          'for workers navigating this transition. The question, therefore, may be less about whether AI will '
          'transform employment, which seems inevitable, and more about whether society prepares thoughtfully '
          'enough to manage that transformation humanely.',
      modelAnswerHighlights: [
        'Opens by acknowledging the genuine concern before examining it critically, avoiding a one-sided rant',
        'Uses historical precedent as evidence rather than relying purely on speculation',
        'Identifies the specific nuance that makes this situation different (speed of transition) rather than a generic comparison',
        'Reframes the essay question productively in the conclusion rather than simply repeating the introduction',
        'Maintains formal, exam-appropriate academic register throughout with sophisticated linking phrases',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class10_writing_letter_civic',
      title: 'Formal Letter: Proposal for a Public Recycling Programme',
      sceneEmoji: '♻️',
      sceneDescription:
          'Write a formal letter to the Municipal Commissioner proposing a citywide recycling programme, '
          'outlining the current problem, your proposed solution, and its potential benefits.',
      wordBank: [
        'propose',
        'municipal',
        'segregation',
        'feasible',
        'implement',
        'incentivise',
        'sustainable',
        'infrastructure',
        'pilot scheme',
        'stakeholders',
      ],
      modelAnswer:
          '78, Lake Garden Colony\nNagpur\n20 June\n\n'
          'The Municipal Commissioner\nNagpur Municipal Corporation\nNagpur\n\n'
          'Subject: Proposal for a citywide waste segregation and recycling programme\n\n'
          'Respected Sir/Madam,\n\n'
          'I am writing to bring to your attention the pressing need for an organised recycling programme in '
          'our city, and to propose a feasible framework that I believe the corporation could implement '
          'without excessive cost.\n\n'
          'At present, most households dispose of all waste together, with recyclable material, food waste, '
          'and hazardous items collected in a single bin and typically sent directly to landfills. This not '
          'only wastes valuable recyclable resources but also contributes significantly to landfill overflow '
          'and associated pollution.\n\n'
          'I propose that the corporation begin with a pilot scheme in three wards, distributing colour-coded '
          'bins to households for segregating dry, wet, and hazardous waste, supported by a public awareness '
          'campaign explaining the system clearly. To incentivise participation, households demonstrating '
          'consistent proper segregation could receive a modest reduction in their annual property tax, an '
          'approach some other Indian cities have already implemented successfully.\n\n'
          'I believe this programme, if piloted carefully and expanded gradually based on lessons learned, '
          'could meaningfully improve our city\'s environmental sustainability while also creating employment '
          'opportunities within the recycling sector itself.\n\n'
          'I hope the corporation will give this proposal due consideration.\n\n'
          'Yours faithfully,\n'
          'Aditya Kulkarni',
      modelAnswerHighlights: [
        'Uses correct formal letter format with full addresses, subject line, and formal closing',
        'Clearly separates the problem (current waste disposal) from the specific proposed solution',
        'Proposes a realistic pilot approach rather than an unrealistic citywide overhaul overnight',
        'Supports the proposal with a specific incentive mechanism, showing practical thinking',
        'Closes by connecting the proposal to a broader benefit (sustainability and employment), strengthening its persuasive appeal',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class10_writing_report_water_crisis',
      title: 'Report: Water Scarcity in the School Neighbourhood',
      sceneEmoji: '💧',
      sceneDescription:
          'Write a report (about 150 words) for a school magazine investigating the recent water scarcity '
          'affecting your school\'s neighbourhood, including causes, impact, and any community response.',
      wordBank: [
        'scarcity',
        'groundwater',
        'depletion',
        'rationing',
        'affected',
        'authorities',
        'mitigation',
        'community-led',
        'sustainable',
        'alleviate',
      ],
      modelAnswer:
          'Water Scarcity in Our Neighbourhood — A Report\n\n'
          'Over the past two months, residents in the area surrounding our school have faced increasingly '
          'severe water scarcity, with municipal water supply reduced to alternate days in several localities. '
          'A survey conducted by our school\'s Environment Club found that groundwater depletion, combined with '
          'a delayed monsoon this year, has been the primary cause of the crisis.\n\n'
          'The scarcity has significantly affected daily life, with many families reporting increased '
          'expenditure on private water tankers and disrupted household routines. Local authorities have '
          'responded by introducing water rationing schedules, though residents have criticised the '
          'inconsistency of these deliveries.\n\n'
          'Encouragingly, several residents\' welfare associations have organised community-led rainwater '
          'harvesting workshops, aiming to reduce dependency on groundwater in future years. While these efforts '
          'alone cannot fully resolve the crisis, they represent a meaningful step toward more sustainable '
          'water management in our neighbourhood.',
      modelAnswerHighlights: [
        'States the timeframe, scale, and immediate cause clearly in the opening paragraph',
        'Cites a specific source (the Environment Club survey) to support claims, adding credibility',
        'Balances describing the problem with describing an actual community response, giving a fuller picture',
        'Maintains objective, factual report tone rather than an overly emotional description',
        'Ends with a measured, realistic assessment rather than an unrealistically optimistic conclusion',
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
