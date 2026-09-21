import '../models/writing_prompt.dart';

const class5Writing = WritingLibrary(
  id: 'class5_writing',
  title: 'Picture Writing',
  grade: 'Class 5',
  prompts: [
    WritingPrompt(
      id: 'class5_writing_science_fair',
      title: 'The School Science Fair',
      sceneEmoji: '🏫🔬🧪🙋‍♀️📊🙋‍♂️',
      sceneDescription:
          'A school science fair: a girl is explaining her volcano model to a small crowd, a boy nearby is '
          'adjusting wires on his electric circuit project, and a judge with a clipboard is walking between '
          'the tables, noting down marks.',
      wordBank: [
        'experiment',
        'explaining',
        'circuit',
        'volcano',
        'curious',
        'judge',
        'display',
        'nervous',
        'impressed',
        'invention',
      ],
      modelAnswer:
          'The school hall is buzzing with excitement during the annual science fair. A girl stands proudly '
          'beside her volcano model, explaining how the eruption works to a group of curious classmates. '
          'Meanwhile, a boy at the next table is carefully adjusting the wires of his electric circuit, hoping '
          'it will light up at just the right moment. A judge moves slowly between the tables, clipboard in '
          'hand, nodding as she listens to each explanation. Some students look nervous as she approaches; '
          'however, most are simply proud to show off what they have built.',
      modelAnswerHighlights: [
        'Opens with a strong overall impression ("buzzing with excitement") rather than a plain fact',
        'Uses "Meanwhile" to connect two things happening in different parts of the scene at once',
        'Includes a small detail that hints at emotion, not just action (nervous students, proud faces)',
        'Uses "however" to show a contrast between two groups of students',
        'Builds the scene from foreground to background, ending with the judge\'s reaction',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class5_writing_cricket_match',
      title: 'The Cricket Match',
      sceneEmoji: '🏏🧢🙌⚡🌤️👦',
      sceneDescription:
          'A cricket match on a school ground: a batsman has just hit the ball hard, fielders are running to '
          'catch it, and teammates on the sidelines are jumping up with their arms raised, cheering loudly.',
      wordBank: [
        'batsman',
        'fielders',
        'boundary',
        'cheering',
        'sprinting',
        'anxious',
        'triumphant',
        'sidelines',
      ],
      modelAnswer:
          'It is an intense moment in the cricket match on the school ground. The batsman has just struck '
          'the ball hard towards the boundary, and two fielders are sprinting after it as fast as they can. '
          'On the sidelines, his teammates leap up with their arms raised, cheering wildly, certain that the '
          'shot will fetch four runs. The fielders, however, look anxious, still hoping they might reach the '
          'ball in time. Above them, the sky is clear and sunny, perfect weather for an afternoon match.',
      modelAnswerHighlights: [
        'Begins by naming the exact moment in the action ("intense moment") to hook the reader',
        'Uses precise cricket vocabulary (batsman, boundary, fielders) instead of general words',
        'Uses "however" to contrast the teammates\' excitement with the fielders\' anxiety',
        'Includes a small detail that hints at emotion, not just action (anxious fielders)',
        'Closes with a background detail (clear sky) that completes the picture',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class5_writing_navratri',
      title: 'Navratri Celebration',
      sceneEmoji: '🪔💃🕺🎶🎉👨‍👩‍👧',
      sceneDescription:
          'A Navratri celebration in a decorated courtyard: families in colourful traditional clothes are '
          'dancing garba in a circle around a lit lamp, a small band plays dandiya music, and children weave '
          'between the dancers with sticks in their hands.',
      wordBank: [
        'traditional',
        'courtyard',
        'garba',
        'rhythm',
        'decorated',
        'joyful',
        'dandiya',
        'swirl',
        'devotion',
      ],
      modelAnswer:
          'The courtyard glows with lights as families gather to celebrate Navratri together. Dressed in '
          'colourful traditional clothes, groups of dancers move in a great circle around a softly lit lamp, '
          'their steps perfectly matching the rhythm of the garba music. Meanwhile, a small band plays lively '
          'dandiya beats, and children weave in and out between the swirling dancers, clicking their sticks '
          'together with delight. The older members of the family watch from the edges, clapping along; their '
          'smiles show both devotion and pure joy. Therefore, the whole courtyard feels alive with colour, '
          'music, and togetherness.',
      modelAnswerHighlights: [
        'Sets the mood immediately with a sensory image ("the courtyard glows with lights")',
        'Uses "Meanwhile" to link the band\'s music with the children\'s movement happening at the same time',
        'Includes a small detail that hints at emotion, not just action (smiles showing devotion and joy)',
        'Uses "Therefore" to draw a conclusion from the details described earlier',
        'Layers the scene by describing dancers, then band, then children, then elders in turn',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class5_writing_farmers_market',
      title: "The Farmers' Market",
      sceneEmoji: '🧺🥬🍅👨‍🌾🚜🗣️',
      sceneDescription:
          "A busy farmers' market at sunrise: a farmer is unloading crates of vegetables from his small "
          'truck, another stallholder is arranging tomatoes into neat pyramids, and customers are bargaining '
          'loudly over the price of fresh greens.',
      wordBank: [
        'stallholder',
        'unloading',
        'bargaining',
        'fresh produce',
        'sunrise',
        'crates',
        'arranging',
        'crowded',
        'earnings',
      ],
      modelAnswer:
          'As the sun rises, the farmers\' market is already crowded and full of activity. A farmer unloads '
          'heavy crates of vegetables from his small truck, stacking them quickly before the customers arrive '
          'in large numbers. Nearby, a stallholder arranges bright red tomatoes into neat pyramids, taking '
          'care that none of them roll away. Meanwhile, a group of customers bargains loudly over the price of '
          'fresh greens, each one hoping for a better deal. The farmer glances over occasionally, clearly '
          'anxious about how much he will earn today; however, his tired face breaks into a smile whenever a '
          'sale is made.',
      modelAnswerHighlights: [
        'Opens with a time marker ("As the sun rises") to set the scene before describing people',
        'Uses "Meanwhile" to connect the stallholder\'s work with the customers\' bargaining at the same time',
        'Includes a small detail that hints at emotion, not just action (the farmer\'s anxious, tired face)',
        'Uses "however" to show a shift from worry to happiness',
        'Uses precise vocabulary (crates, pyramids, bargains) instead of vague words like "things" or "stuff"',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class5_writing_flood_help',
      title: 'Neighbours Helping in the Flood',
      sceneEmoji: '🌧️🏠🚣‍♂️🧑‍🤝‍🧑📦☔',
      sceneDescription:
          'A monsoon flood scene in a neighbourhood: water has risen to knee height on the street, a man is '
          'rowing a small boat to rescue an elderly neighbour, and other residents are passing boxes of dry '
          'food and blankets from balcony to balcony to help a stranded family.',
      wordBank: [
        'flooded',
        'rescue',
        'stranded',
        'elderly',
        'balcony',
        'cooperation',
        'anxious',
        'grateful',
        'relief',
      ],
      modelAnswer:
          'After days of heavy rain, the entire street lies flooded, with water rising to knee height outside '
          'the houses. A young man rows a small boat carefully towards an elderly neighbour who is stranded on '
          'her balcony, looking anxious but relieved to see help arrive. Meanwhile, on the other side of the '
          'street, residents form a human chain, passing boxes of dry food and warm blankets from balcony to '
          'balcony to reach a stranded family. No one waits to be asked; instead, everyone simply pitches in '
          'wherever they can. Therefore, despite the grim weather, the scene shows a neighbourhood coming '
          'together with quiet courage and kindness.',
      modelAnswerHighlights: [
        'Opens by explaining the cause of the scene ("After days of heavy rain") before describing it',
        'Uses "Meanwhile" to connect two rescue efforts happening in different places at once',
        'Includes a small detail that hints at emotion, not just action (anxious but relieved neighbour)',
        'Uses "instead" and "Therefore" to link ideas and draw a conclusion about the community\'s spirit',
        'Ends with an overall reflection (courage and kindness) rather than just stopping at the last action',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class5_writing_library',
      title: 'An Afternoon in the Library',
      sceneEmoji: '📚🤓🔍🧑‍🎓📖🤫',
      sceneDescription:
          'A quiet school library in the afternoon: a girl is searching for a book on a tall shelf using a '
          'small step-stool, a boy is deeply absorbed in reading at a corner table, and the librarian is '
          'stamping due dates into a stack of returned books.',
      wordBank: [
        'absorbed',
        'shelf',
        'librarian',
        'due date',
        'silence',
        'searching',
        'concentration',
        'stacked',
        'peaceful',
      ],
      modelAnswer:
          'A peaceful silence fills the school library on a warm afternoon. Standing on a small step-stool, a '
          'girl reaches carefully towards the top shelf, searching for a book she has been wanting to read for '
          'weeks. In the corner, a boy sits with his knees pulled up, so deeply absorbed in his story that he '
          'does not notice anyone passing by. Meanwhile, the librarian sits at her desk, stamping due dates '
          'into a tall stack of returned books, working steadily through the pile. Although the room is '
          'almost silent, it is easy to sense the quiet concentration and curiosity filling every corner.',
      modelAnswerHighlights: [
        'Sets the mood first ("a peaceful silence") before introducing any character',
        'Uses "Meanwhile" to connect the librarian\'s task with the two students\' actions happening at once',
        'Includes a small detail that hints at emotion, not just action (boy absorbed, unaware of others)',
        'Uses "Although" to link the silence of the room with the busy thinking happening inside it',
        'Ends with a reflective sentence that sums up the feeling of the whole scene',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class5_writing_kite_festival',
      title: 'The Kite-Flying Festival',
      sceneEmoji: '🪁☀️🏠👨‍👩‍👧‍👦🧵😄',
      sceneDescription:
          'Uttarayan on a rooftop: a father and son are launching a bright kite together, an older sister is '
          'winding the string spool quickly as another kite dives, and across the neighbourhood, dozens of '
          'kites of every colour fill the sky under the bright winter sun.',
      wordBank: [
        'rooftop',
        'spool',
        'string',
        'launching',
        'soaring',
        'neighbourhood',
        'triumphant',
        'tangled',
        'countless',
      ],
      modelAnswer:
          'The rooftop is full of energy as the kite-flying festival begins under a bright winter sun. A '
          'father and his son work together to launch a bright red kite, running a few steps until it catches '
          'the wind and soars upward. Beside them, an older sister winds the string spool rapidly, her hands '
          'moving fast as another kite nearby dives and twists dangerously close to theirs. Across the whole '
          'neighbourhood, countless kites of every colour fill the sky, so many that it looks almost like a '
          'painting. Whenever a kite is cut loose, triumphant shouts rise from rooftop to rooftop; however, for '
          'a brief moment, the losing family watches in silence before laughing it off and starting again.',
      modelAnswerHighlights: [
        'Opens with an energetic overall impression before zooming into individual actions',
        'Uses precise verbs (soars, dives, twists) instead of simply saying the kites "move"',
        'Includes a small detail that hints at emotion, not just action (silence before laughing it off)',
        'Uses "however" to contrast the shouts of triumph with the quiet of the losing family',
        'Widens the description to the whole neighbourhood before returning to a specific human reaction',
      ],
      difficulty: Difficulty.hard,
    ),
  ],
);
