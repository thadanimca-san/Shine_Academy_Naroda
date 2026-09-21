import '../models/math_question.dart';

const class5PerimeterArea = MathTopic(
  id: 'class5_perimeter_area',
  title: 'Perimeter and Area',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt:
          'A rectangle has length 8 cm and breadth 5 cm. What is its perimeter?',
      emoji: '⬜',
      options: ['13 cm', '26 cm', '40 cm', '20 cm'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the rectangle ⬜ with length 8 cm and breadth 5 cm.',
        ),
        SolutionStep(
          text: 'Perimeter of a rectangle = 2 × (length + breadth).',
          emoji: '📐',
        ),
        SolutionStep(text: 'First add length and breadth: 8 + 5 = 13.'),
        SolutionStep(text: 'Then multiply by 2: 2 × 13 = 26.'),
        SolutionStep(text: 'The perimeter is 26 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'A square has each side measuring 7 cm. What is its perimeter?',
      emoji: '🟩',
      options: ['28 cm', '14 cm', '21 cm', '49 cm'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the square 🟩 with all 4 sides equal to 7 cm.',
        ),
        SolutionStep(text: 'Perimeter of a square = 4 × side.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 4 × 7 = 28.'),
        SolutionStep(text: 'The perimeter is 28 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular garden is 15 m long and 10 m wide. What is the perimeter of the garden?',
      emoji: '🌷',
      options: ['25 m', '150 m', '50 m', '40 m'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the garden as a rectangle ⬜ with length 15 m and breadth 10 m.',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 15 + 10 = 25.'),
        SolutionStep(text: 'Multiply by 2: 2 × 25 = 50.'),
        SolutionStep(text: 'The perimeter of the garden is 50 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A farmer wants to fence a rectangular field that is 40 m long and 25 m wide. How much fencing wire is needed to go all the way around?',
      emoji: '📏',
      options: ['65 m', '130 m', '1000 m', '100 m'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Fencing all the way around means finding the perimeter of the rectangular field.',
          emoji: '⬜',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 40 + 25 = 65.'),
        SolutionStep(text: 'Multiply by 2: 2 × 65 = 130.'),
        SolutionStep(text: '130 m of fencing wire is needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A rectangle has length 12 cm and breadth 9 cm. What is its area?',
      emoji: '⬜',
      options: ['21 cm²', '42 cm²', '108 cm²', '96 cm²'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the rectangle as a grid of unit squares: 12 columns and 9 rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 12 × 9 = 108.'),
        SolutionStep(
          text:
              'The area is 108 cm² (square centimetres), because area counts unit squares.',
        ),
        SolutionStep(text: 'The area of the rectangle is 108 cm².', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'A square has each side measuring 6 cm. What is its area?',
      emoji: '🟩',
      options: ['12 cm²', '24 cm²', '36 cm²', '18 cm²'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the square as a grid of 6 columns and 6 rows of unit squares: 🟩🟩🟩🟩🟩🟩 repeated 6 times.',
          emoji: '🟩',
        ),
        SolutionStep(text: 'Area of a square = side × side.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 6 × 6 = 36.'),
        SolutionStep(text: 'The area of the square is 36 cm².', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'A floor is 20 m long and 15 m wide. What is its area?',
      emoji: '🟫',
      options: ['300 m²', '35 m²', '70 m²', '150 m²'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the floor as a big grid: 20 unit-columns by 15 unit-rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 20 × 15.'),
        SolutionStep(
          text: 'Break 15 into 10 + 5: 20 × 10 = 200, and 20 × 5 = 100.',
        ),
        SolutionStep(text: 'Add the partial products: 200 + 100 = 300.'),
        SolutionStep(text: 'The area of the floor is 300 m².', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A rectangular hall is 18 m long and 12 m wide. Tiles are square, each covering 1 m². How many tiles are needed to cover the whole floor?',
      emoji: '📐',
      options: ['30 tiles', '216 tiles', '60 tiles', '180 tiles'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Each tile covers exactly 1 m², so the number of tiles needed equals the area of the floor in m².',
          emoji: '🟩',
        ),
        SolutionStep(text: 'Area = length × breadth.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 18 × 12.'),
        SolutionStep(
          text: 'Break 12 into 10 + 2: 18 × 10 = 180, and 18 × 2 = 36.',
        ),
        SolutionStep(text: 'Add the partial products: 180 + 36 = 216.'),
        SolutionStep(
          text: '216 tiles are needed to cover the whole floor.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A square garden has an area of 64 m². What is the length of one side?',
      emoji: '🟩',
      options: ['6 m', '7 m', '8 m', '16 m'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'For a square, area = side × side, so side is the number that multiplies by itself to give the area.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'We need a number that when multiplied by itself gives 64.',
        ),
        SolutionStep(text: 'Try 8: 8 × 8 = 64. That matches!'),
        SolutionStep(text: 'The length of one side is 8 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'The perimeter of a square is 32 cm. What is the length of each side?',
      emoji: '🟩',
      options: ['6 cm', '7 cm', '8 cm', '9 cm'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Perimeter of a square = 4 × side, so side = perimeter ÷ 4.',
          emoji: '📐',
        ),
        SolutionStep(text: '32 ÷ 4 = 8.'),
        SolutionStep(text: 'Each side of the square is 8 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The perimeter of a rectangle is 36 cm and its breadth is 8 cm. What is its length?',
      emoji: '⬜',
      options: ['18 cm', '20 cm', '28 cm', '10 cm'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Perimeter = 2 × (length + breadth), so length + breadth = perimeter ÷ 2.',
          emoji: '📐',
        ),
        SolutionStep(text: '36 ÷ 2 = 18. So length + breadth = 18.'),
        SolutionStep(text: 'We know breadth = 8, so length = 18 - 8.'),
        SolutionStep(text: '18 - 8 = 10.'),
        SolutionStep(text: 'The length of the rectangle is 10 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular playground is 30 m long and 22 m wide. What is the perimeter of the playground?',
      emoji: '🏃',
      options: ['52 m', '104 m', '660 m', '110 m'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the playground as a rectangle ⬜ with length 30 m and breadth 22 m.',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 30 + 22 = 52.'),
        SolutionStep(text: 'Multiply by 2: 2 × 52 = 104.'),
        SolutionStep(
          text: 'The perimeter of the playground is 104 m.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A picture frame is a square with a perimeter of 48 cm. What is the area enclosed by the frame?',
      emoji: '🖼️',
      options: ['96 cm²', '12 cm²', '196 cm²', '144 cm²'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the side using the perimeter: side = perimeter ÷ 4.',
          emoji: '📐',
        ),
        SolutionStep(
          text: '48 ÷ 4 = 12. So each side of the square frame is 12 cm.',
        ),
        SolutionStep(text: 'Now find the area: area = side × side.'),
        SolutionStep(text: '12 × 12 = 144.'),
        SolutionStep(
          text: 'The area enclosed by the frame is 144 cm².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular chart paper is 24 cm long and 18 cm wide. What is its area?',
      emoji: '📄',
      options: ['432 cm²', '42 cm²', '84 cm²', '324 cm²'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the chart paper as a grid: 24 unit-columns by 18 unit-rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 24 × 18.'),
        SolutionStep(
          text: 'Break 18 into 10 + 8: 24 × 10 = 240, and 24 × 8 = 192.',
        ),
        SolutionStep(text: 'Add the partial products: 240 + 192 = 432.'),
        SolutionStep(
          text: 'The area of the chart paper is 432 cm².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A classroom floor is a square with each side 9 m. If one tin of paint covers 9 m², how many tins are needed to paint the whole floor?',
      emoji: '🎨',
      options: ['7 tins', '9 tins', '8 tins', '81 tins'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'First find the area of the floor: area = side × side.',
          emoji: '📐',
        ),
        SolutionStep(text: '9 × 9 = 81. The floor area is 81 m².'),
        SolutionStep(
          text: 'Number of tins needed = total area ÷ area covered by 1 tin.',
        ),
        SolutionStep(text: '81 ÷ 9 = 9.'),
        SolutionStep(text: '9 tins of paint are needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is the perimeter of a square whose side is 15 cm?',
      emoji: '🟩',
      options: ['60 cm', '30 cm', '45 cm', '225 cm'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Perimeter of a square = 4 × side.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 4 × 15 = 60.'),
        SolutionStep(text: 'The perimeter is 60 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular table top is 2 m long and 1 m wide. What is its area?',
      emoji: '🪑',
      options: ['3 m²', '4 m²', '2 m²', '6 m²'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the table top as a grid: 2 unit-columns by 1 unit-row.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 2 × 1 = 2.'),
        SolutionStep(text: 'The area of the table top is 2 m².', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular park is 60 m long and 45 m wide. What length of fencing is needed to go around it once?',
      emoji: '🌳',
      options: ['105 m', '2700 m', '150 m', '210 m'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Going around once means finding the perimeter of the rectangular park.',
          emoji: '⬜',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 60 + 45 = 105.'),
        SolutionStep(text: 'Multiply by 2: 2 × 105 = 210.'),
        SolutionStep(text: '210 m of fencing is needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'Two rectangular tiles, each 5 cm by 4 cm, are placed side by side to form a bigger rectangle 10 cm long and 4 cm wide. What is the area of the bigger rectangle?',
      emoji: '🟦',
      options: ['20 cm²', '14 cm²', '9 cm²', '40 cm²'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture two tiles placed side by side: 🟦🟦, forming a rectangle 10 cm long and 4 cm wide.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 10 × 4 = 40.'),
        SolutionStep(text: 'The area of the bigger rectangle is 40 cm².'),
        SolutionStep(
          text:
              'Check: each small tile has area 5 × 4 = 20 cm², and 2 tiles give 20 + 20 = 40 cm². It matches!',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular notice board is 90 cm long and 60 cm wide. What is its perimeter in metres?',
      emoji: '📋',
      options: ['3 m', '1.5 m', '5400 m', '3.5 m'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the perimeter in cm: perimeter = 2 × (length + breadth).',
          emoji: '📐',
        ),
        SolutionStep(text: 'Add length and breadth: 90 + 60 = 150.'),
        SolutionStep(text: 'Multiply by 2: 2 × 150 = 300 cm.'),
        SolutionStep(
          text:
              'Convert to metres: since 100 cm = 1 m, divide by 100: 300 ÷ 100 = 3.',
        ),
        SolutionStep(text: 'The perimeter is 3 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'A square plot has a perimeter of 100 m. What is its area?',
      emoji: '🟩',
      options: ['400 m²', '250 m²', '2500 m²', '625 m²'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the side using the perimeter: side = perimeter ÷ 4.',
          emoji: '📐',
        ),
        SolutionStep(
          text: '100 ÷ 4 = 25. So each side of the square plot is 25 m.',
        ),
        SolutionStep(text: 'Now find the area: area = side × side.'),
        SolutionStep(text: '25 × 25 = 625.'),
        SolutionStep(text: 'The area of the plot is 625 m².', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular carrom board is 60 cm long and 60 cm wide. Is this shape a square, and what is its area?',
      emoji: '🎯',
      options: [
        'Not a square; area 60 cm²',
        'It is a square; area 3600 cm²',
        'It is a square; area 120 cm²',
        'Not a square; area 3600 cm²',
      ],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Since length (60 cm) equals breadth (60 cm), all 4 sides are equal — this makes it a square.',
          emoji: '🟩',
        ),
        SolutionStep(text: 'Area of a square = side × side.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 60 × 60 = 3600.'),
        SolutionStep(
          text: 'Yes, it is a square, and its area is 3600 cm².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A wall is 8 m long and 3 m high. A tin of paint covers 4 m². How many tins are needed to paint the wall?',
      emoji: '🎨',
      options: ['6 tins', '2 tins', '4 tins', '24 tins'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'First find the area of the wall: area = length × height.',
          emoji: '📐',
        ),
        SolutionStep(text: '8 × 3 = 24. The wall area is 24 m².'),
        SolutionStep(
          text: 'Number of tins needed = total area ÷ area covered by 1 tin.',
        ),
        SolutionStep(text: '24 ÷ 4 = 6.'),
        SolutionStep(text: '6 tins of paint are needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular sheet of paper has a perimeter of 60 cm. If its length is 20 cm, what is its breadth?',
      emoji: '📄',
      options: ['10 cm', '8 cm', '9 cm', '12 cm'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Perimeter = 2 × (length + breadth), so length + breadth = perimeter ÷ 2.',
          emoji: '📐',
        ),
        SolutionStep(text: '60 ÷ 2 = 30. So length + breadth = 30.'),
        SolutionStep(text: 'We know length = 20, so breadth = 30 - 20.'),
        SolutionStep(text: '30 - 20 = 10.'),
        SolutionStep(text: 'The breadth of the sheet is 10 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A garden that is 25 m by 16 m needs to be covered entirely with grass. What area of grass is needed?',
      emoji: '🌱',
      options: ['400 m²', '82 m²', '41 m²', '410 m²'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the garden as a grid: 25 unit-columns by 16 unit-rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of grass needed = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 25 × 16.'),
        SolutionStep(
          text: 'Break 16 into 10 + 6: 25 × 10 = 250, and 25 × 6 = 150.',
        ),
        SolutionStep(text: 'Add the partial products: 250 + 150 = 400.'),
        SolutionStep(text: '400 m² of grass is needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A small square tile has a side of 4 cm. How many such tiles are needed to cover a rectangular floor that is 40 cm by 32 cm?',
      emoji: '🧩',
      options: ['60 tiles', '80 tiles', '70 tiles', '90 tiles'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'First find the area of one tile: area = side × side.',
          emoji: '📐',
        ),
        SolutionStep(text: '4 × 4 = 16. Each tile covers 16 cm².'),
        SolutionStep(text: 'Now find the area of the floor: 40 × 32.'),
        SolutionStep(
          text: 'Break 32 into 30 + 2: 40 × 30 = 1200, and 40 × 2 = 80.',
        ),
        SolutionStep(
          text:
              'Add the partial products: 1200 + 80 = 1280. The floor area is 1280 cm².',
        ),
        SolutionStep(
          text:
              'Number of tiles = floor area ÷ area of one tile = 1280 ÷ 16 = 80.',
        ),
        SolutionStep(
          text: '80 tiles are needed to cover the floor.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular sports field is 90 m long and 45 m wide. What is its perimeter?',
      emoji: '🏟️',
      options: ['270 m', '135 m', '180 m', '4050 m'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the field as a rectangle ⬜ with length 90 m and breadth 45 m.',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 90 + 45 = 135.'),
        SolutionStep(text: 'Multiply by 2: 2 × 135 = 270.'),
        SolutionStep(text: 'The perimeter of the field is 270 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A square handkerchief has a perimeter of 56 cm. What is its area?',
      emoji: '🧣',
      options: ['196 cm²', '182 cm²', '224 cm²', '144 cm²'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the side using the perimeter: side = perimeter ÷ 4.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '56 ÷ 4 = 14. So each side of the square handkerchief is 14 cm.',
        ),
        SolutionStep(text: 'Now find the area: area = side × side.'),
        SolutionStep(text: '14 × 14 = 196.'),
        SolutionStep(
          text: 'The area of the handkerchief is 196 cm².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular pond is 18 m long and 14 m wide. A path runs all the way around the edge of the pond. What is the length of the path?',
      emoji: '🐟',
      options: ['32 m', '252 m', '64 m', '36 m'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'A path all the way around the edge means we need the perimeter of the pond.',
          emoji: '⬜',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 18 + 14 = 32.'),
        SolutionStep(text: 'Multiply by 2: 2 × 32 = 64.'),
        SolutionStep(text: 'The path is 64 m long.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'A classroom door is 2 m tall and 1 m wide. What is its area?',
      emoji: '🚪',
      options: ['3 m²', '2 m²', '4 m²', '6 m²'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the door as a grid: 1 unit-column by 2 unit-rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 2 × 1 = 2.'),
        SolutionStep(text: 'The area of the door is 2 m².', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular badminton court is 13 m long and 6 m wide. What is its area?',
      emoji: '🏸',
      options: ['19 m²', '38 m²', '78 m²', '82 m²'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the court as a grid: 13 unit-columns by 6 unit-rows.',
          emoji: '⬜',
        ),
        SolutionStep(
          text: 'Area of a rectangle = length × breadth.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Multiply: 13 × 6 = 78.'),
        SolutionStep(
          text: 'The area of the badminton court is 78 m².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The perimeter of a square field is 84 m. What is the length of each side?',
      emoji: '🌾',
      options: ['19 m', '20 m', '22 m', '21 m'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Perimeter of a square = 4 × side, so side = perimeter ÷ 4.',
          emoji: '📐',
        ),
        SolutionStep(text: '84 ÷ 4 = 21.'),
        SolutionStep(text: 'Each side of the field is 21 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A rectangular kitchen counter is 3 m long and 60 cm wide. What is its area in cm²?',
      emoji: '🍳',
      options: ['180 cm²', '18,000 cm²', '1,800 cm²', '180,000 cm²'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'First convert the length to cm: since 1 m = 100 cm, 3 m = 300 cm.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Now both measurements are in cm: 300 cm long and 60 cm wide.',
        ),
        SolutionStep(text: 'Area of a rectangle = length × breadth.'),
        SolutionStep(text: 'Multiply: 300 × 60 = 18,000.'),
        SolutionStep(
          text: 'The area of the counter is 18,000 cm².',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular vegetable patch is 12 m long and 7 m wide. If a fence costs ₹50 per metre, what is the total cost of fencing the patch?',
      emoji: '🥦',
      options: ['₹1,700', '₹1,900', '₹1,800', '₹2,000'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the perimeter of the patch: perimeter = 2 × (length + breadth).',
          emoji: '📐',
        ),
        SolutionStep(text: 'Add length and breadth: 12 + 7 = 19.'),
        SolutionStep(
          text: 'Multiply by 2: 2 × 19 = 38. The perimeter is 38 m.',
        ),
        SolutionStep(
          text: 'Total cost = perimeter × cost per metre = 38 × 50.',
        ),
        SolutionStep(text: 'Multiply: 38 × 50 = 1,900.'),
        SolutionStep(text: 'The total cost of fencing is ₹1,900.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is the perimeter of a square whose area is 100 cm²?',
      emoji: '🟩',
      options: ['10 cm', '20 cm', '50 cm', '40 cm'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the side using the area: since area = side × side, we need a number that multiplies by itself to give 100.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Try 10: 10 × 10 = 100. That matches, so the side is 10 cm.',
        ),
        SolutionStep(text: 'Now find the perimeter: perimeter = 4 × side.'),
        SolutionStep(text: '4 × 10 = 40.'),
        SolutionStep(text: 'The perimeter is 40 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A rectangular book cover is 25 cm long and 20 cm wide. What is its perimeter?',
      emoji: '📕',
      options: ['45 cm', '500 cm', '80 cm', '90 cm'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the book cover as a rectangle ⬜ with length 25 cm and breadth 20 cm.',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 25 + 20 = 45.'),
        SolutionStep(text: 'Multiply by 2: 2 × 45 = 90.'),
        SolutionStep(
          text: 'The perimeter of the book cover is 90 cm.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular hall is 16 m long and its area is 176 m². What is its width?',
      emoji: '🏛️',
      options: ['9 m', '10 m', '11 m', '12 m'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Since area = length × breadth, breadth = area ÷ length.',
          emoji: '📐',
        ),
        SolutionStep(text: '176 ÷ 16.'),
        SolutionStep(
          text:
              'Look at the first two digits, 17. Since 16 fits into 17 once, 17 ÷ 16 = 1, remainder 1.',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 6, next to remainder 1, making 16. Divide 16 ÷ 16 = 1 exactly.',
        ),
        SolutionStep(text: 'Combine the digits: 1 and 1, giving 11.'),
        SolutionStep(text: 'The width of the hall is 11 m.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'A square-shaped stamp has a side of 3 cm. What is its area?',
      emoji: '📮',
      options: ['6 cm²', '12 cm²', '3 cm²', '9 cm²'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the stamp as a grid of 3 columns and 3 rows of unit squares.',
          emoji: '🟩',
        ),
        SolutionStep(text: 'Area of a square = side × side.', emoji: '📐'),
        SolutionStep(text: 'Multiply: 3 × 3 = 9.'),
        SolutionStep(text: 'The area of the stamp is 9 cm².', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A rectangular swimming pool is 25 m long and 10 m wide. If a rope goes all the way around it once, how long is the rope?',
      emoji: '🏊',
      options: ['35 m', '50 m', '70 m', '250 m'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Going all the way around means finding the perimeter of the pool.',
          emoji: '⬜',
        ),
        SolutionStep(text: 'Perimeter = 2 × (length + breadth).', emoji: '📐'),
        SolutionStep(text: 'Add length and breadth: 25 + 10 = 35.'),
        SolutionStep(text: 'Multiply by 2: 2 × 35 = 70.'),
        SolutionStep(text: 'The rope needs to be 70 m long.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
