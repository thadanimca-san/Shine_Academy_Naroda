import '../models/writing_prompt.dart';

const class8Writing = WritingLibrary(
  id: 'class8_writing',
  title: 'Essay, Letter & Report Writing',
  grade: 'Class 8',
  prompts: [
    WritingPrompt(
      id: 'class8_writing_essay_technology',
      title: 'Essay: Is Technology Making Us Lazy?',
      sceneEmoji: '📱',
      sceneDescription:
          'Write a balanced essay (about 150-180 words) discussing whether technology is making students lazy. '
          'Present both a possible advantage and a possible disadvantage before giving your own opinion.',
      wordBank: [
        'convenience',
        'dependency',
        'productivity',
        'distraction',
        'balance',
        'efficient',
        'overreliance',
        'perspective',
        'moderation',
        'undeniably',
      ],
      modelAnswer:
          'Technology has undeniably changed the way students learn, work, and communicate, but whether it '
          'makes us lazy depends largely on how it is used. On one hand, technology offers remarkable '
          'convenience: a student can research a topic in seconds that once required an entire afternoon in a '
          'library, and this efficiency frees up time for deeper thinking rather than tedious searching. On the '
          'other hand, this same convenience can encourage overreliance, where students copy information '
          'without truly understanding it, or become distracted by entertainment apps instead of completing '
          'their work.\n\n'
          'In my opinion, technology itself is neither lazy-making nor productive; it simply reflects the habits '
          'of the person using it. A student who uses the internet to research thoroughly and then writes '
          'original answers is being more productive than ever before, while one who copies answers without '
          'thinking is misusing a powerful tool. The real solution lies not in avoiding technology, but in using '
          'it with moderation and self-discipline, treating it as a resource rather than a replacement for '
          'genuine effort.',
      modelAnswerHighlights: [
        'Presents both sides of the argument clearly before giving a personal opinion',
        'Uses linking phrases like "On one hand" and "On the other hand" to structure the balanced discussion',
        'Avoids an extreme, one-sided conclusion, instead offering a nuanced final opinion',
        'Uses academic vocabulary (overreliance, efficiency, moderation) naturally within the argument',
        'Ends with a clear, memorable statement that summarises the main point',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class8_writing_letter_newspaper',
      title: 'Formal Letter: Complaint About Traffic Near School',
      sceneEmoji: '🚦',
      sceneDescription:
          'Write a formal letter to the editor of a local newspaper, drawing attention to the dangerous traffic '
          'situation near your school gate during dismissal time and suggesting a possible solution.',
      wordBank: [
        'congestion',
        'hazard',
        'pedestrian',
        'authorities',
        'urge',
        'concerned',
        'measures',
        'jeopardise',
        'appeal',
        'cooperation',
      ],
      modelAnswer:
          '45, Green Park Road\nVadodara\n15 September\n\n'
          'The Editor\nCity Times\nVadodara\n\n'
          'Subject: Dangerous traffic congestion outside Greenfield School\n\n'
          'Dear Sir/Madam,\n\n'
          'Through your esteemed newspaper, I wish to draw the attention of the concerned authorities to a '
          'serious traffic hazard outside Greenfield School on Green Park Road.\n\n'
          'Every afternoon during school dismissal, vehicles park haphazardly on both sides of the narrow road, '
          'leaving barely any space for pedestrians, including young children, to walk safely. On several '
          'occasions, I have personally witnessed near-accidents as cars reverse suddenly without checking for '
          'children crossing the road.\n\n'
          'I would like to appeal to the traffic police to station an officer near the school gate during peak '
          'dismissal hours and to consider marking a designated pick-up zone a short distance away from the '
          'main gate, so vehicles do not crowd the entrance directly. I believe this small measure, along with '
          'cooperation from parents, could prevent a serious accident before it happens.\n\n'
          'I hope this matter receives the urgent attention it deserves.\n\n'
          'Yours faithfully,\n'
          'A concerned resident',
      modelAnswerHighlights: [
        'Follows the correct format for a letter to a newspaper editor, including a clear subject line',
        'States the problem specifically (location, time, and exact danger) rather than vaguely',
        'Includes a concrete, practical suggestion rather than only complaining',
        'Uses formal, respectful language appropriate for a published letter ("I wish to draw attention", "I would like to appeal")',
        'Closes by emphasising urgency without sounding overly dramatic',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class8_writing_report_sports_day',
      title: 'Report: Annual Sports Day',
      sceneEmoji: '🏃',
      sceneDescription:
          'Write a report (about 120 words) for the school magazine describing your school\'s Annual Sports Day, '
          'including the main events, an outstanding performance, and the overall outcome.',
      wordBank: [
        'commenced',
        'participants',
        'enthusiasm',
        'outstanding',
        'triumph',
        'spectators',
        'concluded',
        'trophy',
        'sportsmanship',
        'memorable',
      ],
      modelAnswer:
          'Annual Sports Day — A Report\n\n'
          'The school\'s Annual Sports Day commenced on the morning of 20 January with an energetic march-past '
          'by all four houses. Over three hundred participants took part in track and field events, ranging '
          'from the 100-metre sprint to the long jump, cheered on enthusiastically by spectators throughout '
          'the day.\n\n'
          'The most outstanding performance came from Class 8 student Rehan Sheikh, who set a new school record '
          'in the 400-metre race, earning a standing ovation from the crowd. Despite the fierce competition, '
          'the day was marked by excellent sportsmanship, with several students helping opponents who fell '
          'during races.\n\n'
          'The event concluded with a prize distribution ceremony, where the Blue House was declared overall '
          'champion. It was a memorable day that celebrated both athletic talent and team spirit across the '
          'school.',
      modelAnswerHighlights: [
        'Opens with a clear heading and states the date and starting event immediately',
        'Presents information in chronological order: opening, main events, a highlight, and the conclusion',
        'Includes a specific, memorable detail (the record-breaking race) rather than only general statements',
        'Notes a value beyond winning (sportsmanship), giving the report a rounded perspective',
        'Stays close to the word limit while covering every required element',
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
