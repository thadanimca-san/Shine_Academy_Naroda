import '../models/writing_prompt.dart';

const class3Writing = WritingLibrary(
  id: 'class3_writing',
  title: 'Picture Writing',
  grade: 'Class 3',
  prompts: [
    WritingPrompt(
      id: 'class3_writing_pet_dog',
      title: 'My Pet Dog',
      sceneEmoji: '🐕🦴🏠😊',
      sceneDescription:
          'A happy dog is playing with a bone in front of a small house.',
      wordBank: ['dog', 'happy', 'playing', 'bone', 'house', 'brown', 'tail', 'run'],
      modelAnswer:
          'This is my dog. He is brown and happy. He is playing with his bone near the house. His tail '
          'is wagging fast.',
      modelAnswerHighlights: [
        'Uses a simple opening sentence',
        'Names the animal and the object (bone)',
        'Uses one describing word like "happy" or "brown"',
        'Uses short, easy sentences',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class3_writing_family_dinner',
      title: 'Family Dinner',
      sceneEmoji: '🍛👨‍👩‍👧‍👦🍽️😋',
      sceneDescription:
          'A family is sitting together at a table, eating dinner and smiling.',
      wordBank: ['family', 'dinner', 'table', 'eating', 'happy', 'plate', 'food', 'together'],
      modelAnswer:
          'My family is eating dinner together. We are sitting at the table. Mummy made tasty food. '
          'Everyone is happy and smiling.',
      modelAnswerHighlights: [
        'Starts with who is in the picture',
        'Tells what the family is doing',
        'Uses a simple feeling word like "happy"',
        'Keeps sentences short and clear',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class3_writing_school_day',
      title: 'A Day at School',
      sceneEmoji: '🏫🎒📖👧',
      sceneDescription:
          'A girl is walking into school with her bag, holding a book, ready for class.',
      wordBank: ['school', 'bag', 'book', 'walking', 'class', 'teacher', 'friends', 'happy'],
      modelAnswer:
          'This girl is going to school. She has her bag and her book. She is happy to see her friends. '
          'She likes going to class.',
      modelAnswerHighlights: [
        'Names the person and what she is carrying',
        'Uses one feeling word like "happy"',
        'Tells what she likes to do',
        'Uses easy words a Class 3 student knows',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class3_writing_birthday_balloons',
      title: 'Birthday Balloons',
      sceneEmoji: '🎈🎂🎁👦',
      sceneDescription:
          'A boy is standing next to a cake and colourful balloons on his birthday.',
      wordBank: ['birthday', 'balloons', 'cake', 'gift', 'colourful', 'happy', 'party', 'candles'],
      modelAnswer:
          'It is his birthday. There is a big cake with candles. Colourful balloons are all around him. '
          'He got a gift and he is very happy.',
      modelAnswerHighlights: [
        'Tells the occasion first (birthday)',
        'Names the objects in the picture (cake, balloons, gift)',
        'Uses a describing word like "colourful" or "happy"',
        'Ends with how the child feels',
      ],
      difficulty: Difficulty.medium,
    ),
    WritingPrompt(
      id: 'class3_writing_garden',
      title: 'In the Garden',
      sceneEmoji: '🌻🦋🌳👧',
      sceneDescription:
          'A girl is watering flowers in a garden while a butterfly flies near a tree.',
      wordBank: ['garden', 'flowers', 'butterfly', 'watering', 'tree', 'yellow', 'happy', 'plant'],
      modelAnswer:
          'This girl is in the garden. She is watering the yellow flowers. A butterfly is flying near '
          'the tree. She likes taking care of her plants.',
      modelAnswerHighlights: [
        'Names the place at the start (garden)',
        'Tells what the girl is doing',
        'Uses a colour word like "yellow"',
        'Adds one more detail from the picture (butterfly)',
      ],
      difficulty: Difficulty.easy,
    ),
    WritingPrompt(
      id: 'class3_writing_rainy_day',
      title: 'A Rainy Day',
      sceneEmoji: '🌧️☂️👦💦',
      sceneDescription:
          'A boy is walking with an umbrella in the rain, splashing through a puddle.',
      wordBank: ['rain', 'umbrella', 'wet', 'puddle', 'splash', 'walking', 'happy', 'cold'],
      modelAnswer:
          'It is raining outside. This boy is holding an umbrella. He is splashing in a puddle. He '
          'looks very happy in the rain.',
      modelAnswerHighlights: [
        'Starts by saying what the weather is',
        'Names the object the boy is holding (umbrella)',
        'Uses an action word like "splashing"',
        'Ends with how the boy feels',
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
