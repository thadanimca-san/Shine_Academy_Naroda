import '../models/writing_prompt.dart';

/// Writing prompts for Class 7-10: essay, letter, and report topics
/// appropriate for teen writers, using the same WritingPrompt fields as
/// the Class 3-6 app's picture-description prompts (title emoji, word
/// bank, model answer, highlights) but with writing-task framing instead
/// of a visual scene.
const class7Writing = WritingLibrary(
  id: 'class7_writing',
  title: 'Essay, Letter & Report Writing',
  grade: 'Class 7',
  prompts: [
    WritingPrompt(
      id: 'class7_writing_favourite_festival',
      title: 'Essay: My Favourite Festival',
      sceneEmoji: '🪔',
      sceneDescription:
          'Write a short essay (about 120-150 words) describing your favourite festival. Mention which '
          'festival it is, how your family celebrates it, and why it means so much to you.',
      wordBank: [
        'tradition',
        'celebrate',
        'delicacies',
        'decorate',
        'gather',
        'anticipation',
        'cherish',
        'atmosphere',
        'custom',
        'joyous',
      ],
      modelAnswer:
          'Among all the festivals celebrated in my family, Diwali remains my favourite. Weeks before the '
          'festival arrives, our house is filled with a joyous atmosphere as we clean every corner and '
          'decorate the entrance with colourful rangoli. On the evening of Diwali itself, we light rows of '
          'small earthen lamps along the balcony, and the whole street begins to glow warmly as neighbours do '
          'the same. My favourite part, however, is not the fireworks but the quiet hour beforehand, when my '
          'grandmother tells us stories about why we celebrate this festival while my mother prepares '
          'traditional delicacies in the kitchen. Later, relatives visit with sweets and warm greetings, and '
          'even distant cousins seem to gather under one roof. Diwali reminds me that festivals are not just '
          'about lights and food, but about the anticipation of togetherness that builds for weeks beforehand. '
          'This is why, every year, I cherish this festival more than any other.',
      modelAnswerHighlights: [
        'Opens by directly naming the festival and stating a clear opinion',
        'Organises ideas in a logical order: preparation, the main event, and personal reflection',
        'Uses topic-specific vocabulary (rangoli, delicacies, traditional) naturally within sentences',
        'Includes a personal detail (grandmother\'s stories) that makes the essay feel genuine, not generic',
        'Ends by returning to the opening idea, giving the essay a complete, rounded feeling',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class7_writing_letter_principal',
      title: 'Formal Letter: Requesting a School Library Extension',
      sceneEmoji: '📖',
      sceneDescription:
          'Write a formal letter to your school principal requesting that the library remain open for one '
          'extra hour after school so students can study before going home. Include a proper greeting, a '
          'clear reason for your request, and a polite closing.',
      wordBank: [
        'respectfully',
        'request',
        'convenient',
        'facility',
        'beneficial',
        'consideration',
        'grateful',
        'sincerely',
        'assistance',
        'arrangement',
      ],
      modelAnswer:
          'The Principal\nSunrise Public School\nAhmedabad\n\n'
          'Subject: Request to extend school library timings\n\n'
          'Respected Madam,\n\n'
          'I am writing on behalf of the Class 7 students to respectfully request that the school library '
          'remain open for one extra hour after school hours, until 5 p.m. instead of 4 p.m.\n\n'
          'Many students, including myself, find it difficult to study effectively at home due to household '
          'distractions or a lack of quiet space, especially before examinations. An extra hour in the library '
          'would give us a calm environment to complete our homework and revise lessons before returning home. '
          'It would also reduce the number of books we need to carry back and forth each day.\n\n'
          'I understand that this arrangement may require additional staff supervision, and we would be happy '
          'to follow any rules set for this purpose, such as signing in and out or maintaining silence at all '
          'times.\n\n'
          'I hope you will give this request your kind consideration. We would be extremely grateful for this '
          'facility.\n\n'
          'Thanking you,\n'
          'Yours sincerely,\n'
          'A student of Class 7',
      modelAnswerHighlights: [
        'Follows the correct formal letter format: sender/receiver address, subject line, and formal closing',
        'States the request clearly in the very first paragraph',
        'Supports the request with specific, believable reasons rather than vague statements',
        'Anticipates a possible objection (extra supervision) and offers a solution',
        'Uses polite, formal vocabulary throughout ("respectfully", "kind consideration", "grateful")',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class7_writing_letter_friend',
      title: 'Informal Letter: Telling a Friend About Your New School',
      sceneEmoji: '✉️',
      sceneDescription:
          'Write an informal letter to a friend who has moved to another city, telling them about your new '
          'class teacher, a new friend you have made, and one interesting thing that happened at school this '
          'month.',
      wordBank: [
        'guess what',
        'by the way',
        'honestly',
        'hilarious',
        'miss you',
        'update',
        'meanwhile',
        'can\'t wait',
        'take care',
        'write back soon',
      ],
      modelAnswer:
          '123, Lake View Society\nSurat\n12 August\n\n'
          'Dear Priya,\n\n'
          'How are you settling into your new school? I miss having you in class, but I have some news to '
          'share!\n\n'
          'Guess what — we have a new English teacher this year, Mrs. Kapoor, and honestly, she makes even '
          'grammar lessons feel interesting. By the way, I have also made a new friend, Ritika, who sits at '
          'your old desk. She is hilarious and already reminds me a little of you.\n\n'
          'The most interesting thing that happened this month was our class trip to the science museum. Our '
          'friend Aman accidentally set off the fire alarm in the robotics section, and honestly, half the '
          'class could not stop laughing for the rest of the day! Meanwhile, everything else here is much the '
          'same as before, except that I keep forgetting you are not just one street away anymore.\n\n'
          'Please write back soon and tell me everything about your new school. I can\'t wait to hear all '
          'about it.\n\n'
          'Take care,\n'
          'Your friend,\n'
          'Ishaan',
      modelAnswerHighlights: [
        'Uses an informal, friendly tone throughout, unlike a formal letter',
        'Includes specific, personal details (a funny classroom incident) rather than generic statements',
        'Uses natural conversational phrases like "guess what" and "by the way" to connect ideas',
        'Asks a genuine question about the friend\'s life, keeping the letter two-directional',
        'Ends warmly, matching the informal relationship between the writers',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class7_writing_report_cleanliness_drive',
      title: 'Report: School Cleanliness Drive',
      sceneEmoji: '🧹',
      sceneDescription:
          'Write a short report (about 100 words) for the school newsletter about a cleanliness drive '
          'organised by your class. Mention when it happened, what students did, and the result.',
      wordBank: [
        'organised',
        'participated',
        'volunteers',
        'collected',
        'awareness',
        'initiative',
        'successful',
        'appreciated',
        'segregated',
        'outcome',
      ],
      modelAnswer:
          'Class 7 Cleanliness Drive — A Report\n\n'
          'On 5 August, Class 7 organised a cleanliness drive across the school playground and surrounding '
          'garden area. Around thirty student volunteers participated, divided into small groups and equipped '
          'with gloves and dustbags provided by the school. Within two hours, the students collected several '
          'bags of waste and carefully segregated plastic, paper, and organic material into separate bins.\n\n'
          'The initiative also included a short awareness talk by a Class 7 student on the effects of litter '
          'on the environment. Teachers and the principal appreciated the effort, noting that the playground '
          'looked noticeably cleaner by the end of the day. The successful outcome has encouraged the school '
          'to consider organising similar drives every month.',
      modelAnswerHighlights: [
        'Begins with a clear heading and states the date and organiser immediately',
        'Presents facts in a logical order: what happened, how many participated, and the result',
        'Uses factual, objective language suited to a report, avoiding overly personal opinions',
        'Includes a specific outcome (cleaner playground, monthly drives considered) to show impact',
        'Stays close to the word limit while still covering every required detail',
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
