import '../models/writing_prompt.dart';

const class4Writing = WritingLibrary(
  id: 'class4_writing',
  title: 'Picture Writing',
  grade: 'Class 4',
  prompts: [
    WritingPrompt(
      id: 'class4_writing_park',
      title: 'A Day at the Park',
      sceneEmoji: '🌳🧒⚽👧🐕☀️',
      sceneDescription:
          'A sunny park scene: a boy is kicking a football, a girl is playing with her dog, and tall '
          'green trees are around them.',
      wordBank: ['sunny', 'kicking', 'football', 'playing', 'trees', 'happy', 'dog', 'grass'],
      modelAnswer:
          'It is a sunny afternoon in the park. A boy is kicking a football near the green trees. Beside '
          'him, a girl is playing happily with her little dog on the grass. Everyone looks cheerful and '
          'full of energy under the bright blue sky.',
      modelAnswerHighlights: [
        'Starts by setting the scene (time and weather)',
        'Describes each person and what they are doing, one at a time',
        'Uses describing words like "sunny", "green", and "happily"',
        'Ends with an overall feeling about the picture',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class4_writing_market',
      title: 'Busy Market Day',
      sceneEmoji: '🏪🍎🥕👩‍🌾🧺',
      sceneDescription:
          'A busy vegetable market: a farmer woman is selling fresh apples and carrots, and a basket full '
          'of vegetables sits on her stall.',
      wordBank: ['market', 'fresh', 'selling', 'basket', 'vegetables', 'customers', 'stall', 'busy'],
      modelAnswer:
          'This picture shows a busy vegetable market. A farmer woman is standing behind her stall, selling '
          'fresh apples and carrots. A large basket full of colourful vegetables is placed beside her. '
          'Customers walk around, choosing the best vegetables for their homes.',
      modelAnswerHighlights: [
        'Opens with "This picture shows..." to introduce the scene clearly',
        'Names the main person and what they are doing',
        'Mentions specific objects (basket, apples, carrots) instead of vague words',
        'Adds a final sentence about the wider scene (customers)',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class4_writing_rain',
      title: 'The First Rain',
      sceneEmoji: '🌧️☂️👦👧🌈',
      sceneDescription:
          'Two children are jumping in puddles under an umbrella during the first rain of the monsoon, '
          'with a rainbow appearing in the sky behind them.',
      wordBank: ['monsoon', 'puddles', 'umbrella', 'jumping', 'rainbow', 'wet', 'excited', 'splash'],
      modelAnswer:
          'The monsoon has finally arrived. Two children are jumping happily in the puddles, sharing one '
          'umbrella to stay a little dry. Their clothes are wet, but their faces show pure excitement. In '
          'the background, a beautiful rainbow stretches across the sky, making the moment even more '
          'special.',
      modelAnswerHighlights: [
        'Introduces the situation (monsoon has arrived) before describing details',
        'Describes the children\'s actions and feelings together',
        'Uses a linking word like "but" to add contrast (wet clothes, excited faces)',
        'Ends with a detail from the background (rainbow) to complete the picture',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class4_writing_birthday',
      title: 'Birthday Celebration',
      sceneEmoji: '🎂🎈🎉👨‍👩‍👧‍👦',
      sceneDescription:
          'A family birthday party: a cake with candles sits on a table, colourful balloons decorate the '
          'room, and family members are gathered together, smiling.',
      wordBank: ['celebration', 'candles', 'balloons', 'decorated', 'gathered', 'smiling', 'gifts', 'cheerful'],
      modelAnswer:
          'This is a joyful birthday celebration. A cake with lit candles is placed at the centre of the '
          'table, ready to be cut. Colourful balloons decorate the walls, making the room feel festive. The '
          'whole family has gathered around, smiling and clapping, clearly excited to celebrate together.',
      modelAnswerHighlights: [
        'Describes the main object (cake) with useful detail (lit candles)',
        'Mentions the setting/decoration before the people',
        'Uses action words like "clapping" to show movement, not just appearance',
        'Ties the description together with one overall mood word (joyful, festive)',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class4_writing_beach',
      title: 'A Trip to the Beach',
      sceneEmoji: '🏖️🌊👦🏄‍♀️🐚',
      sceneDescription:
          'A family beach outing: a boy is building a sandcastle, a girl is surfing on a wave, and '
          'seashells are scattered along the shore.',
      wordBank: ['beach', 'sandcastle', 'waves', 'shore', 'seashells', 'building', 'surfing', 'breeze'],
      modelAnswer:
          'This lively scene takes place at the beach on a bright day. A boy sits near the shore, carefully '
          'building a tall sandcastle. Not far away, a girl rides confidently on a large wave, enjoying the '
          'cool ocean breeze. Scattered seashells lie along the golden sand, waiting to be collected.',
      modelAnswerHighlights: [
        'Opens by naming the setting and general mood ("lively scene")',
        'Uses precise verbs like "rides" and "building" instead of just "is"',
        'Includes a sensory detail (cool ocean breeze) beyond just what is seen',
        'Finishes with a smaller background detail (seashells) for completeness',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class4_writing_classroom',
      title: 'Our Classroom',
      sceneEmoji: '🏫📚✏️🧑‍🏫',
      sceneDescription:
          'A classroom scene: a teacher is writing on the blackboard, students sit at their desks with '
          'open notebooks, and colourful charts hang on the walls.',
      wordBank: ['blackboard', 'notebooks', 'charts', 'attentive', 'writing', 'desks', 'lesson', 'walls'],
      modelAnswer:
          'In this picture, our teacher stands at the blackboard, explaining today\'s lesson. All the '
          'students sit attentively at their desks, their notebooks open and ready. Bright, colourful '
          'charts are pinned to the walls, showing letters and numbers. Everyone seems focused on '
          'learning something new.',
      modelAnswerHighlights: [
        'Uses "In this picture..." to clearly introduce the scene',
        'Describes the teacher\'s action first, then the students as a group',
        'Adds detail about the classroom walls to complete the setting',
        'Ends with a sentence that sums up the overall activity',
      ],
      difficulty: Difficulty.easy,
    ),
  ],
);
