import '../models/math_question.dart';

const class5Multiplication = MathTopic(
  id: 'class5_multiplication',
  title: 'Multiplication',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt: 'What is 23 × 4?',
      emoji: '✖️',
      options: ['82', '88', '96', '92'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Break 23 into 20 + 3, so 23 × 4 = 20 × 4 + 3 × 4.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 20 × 4 = 80.'),
        SolutionStep(text: 'Second partial product: 3 × 4 = 12.'),
        SolutionStep(text: 'Add the partial products: 80 + 12 = 92.'),
        SolutionStep(text: 'The answer is 92.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 56 × 3?',
      emoji: '✖️',
      options: ['158', '168', '178', '148'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Break 56 into 50 + 6, so 56 × 3 = 50 × 3 + 6 × 3.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 50 × 3 = 150.'),
        SolutionStep(text: 'Second partial product: 6 × 3 = 18.'),
        SolutionStep(text: 'Add the partial products: 150 + 18 = 168.'),
        SolutionStep(text: 'The answer is 168.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A basket has 8 apples 🍎. How many apples are there in 15 baskets?',
      emoji: '🍎',
      options: ['110', '115', '120', '125'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Total apples = apples per basket × number of baskets.',
        ),
        SolutionStep(text: '8 × 15. Break 15 into 10 + 5.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 8 × 10 = 80.'),
        SolutionStep(text: 'Second partial product: 8 × 5 = 40.'),
        SolutionStep(text: 'Add the partial products: 80 + 40 = 120.'),
        SolutionStep(text: 'There are 120 apples in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 142 × 6?',
      emoji: '✖️',
      options: ['842', '862', '852', '752'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Break 142 into 100 + 40 + 2, so multiply each part by 6.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 100 × 6 = 600.'),
        SolutionStep(text: 'Second partial product: 40 × 6 = 240.'),
        SolutionStep(text: 'Third partial product: 2 × 6 = 12.'),
        SolutionStep(text: 'Add the partial products: 600 + 240 + 12 = 852.'),
        SolutionStep(text: 'The answer is 852.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A toy shop sells toy cars 🚗 in boxes of 24. How many toy cars are there in 18 boxes?',
      emoji: '🚗',
      options: ['412', '422', '432', '442'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Total toy cars = cars per box × number of boxes.'),
        SolutionStep(text: '24 × 18. Break 18 into 10 + 8.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 24 × 10 = 240.'),
        SolutionStep(text: 'Second partial product: 24 × 8 = 192.'),
        SolutionStep(text: 'Add the partial products: 240 + 192 = 432.'),
        SolutionStep(text: 'There are 432 toy cars in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 305 × 7?',
      emoji: '✖️',
      options: ['2,135', '2,115', '2,035', '2,145'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Break 305 into 300 + 0 + 5, so multiply each part by 7.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 300 × 7 = 2,100.'),
        SolutionStep(text: 'Second partial product: 5 × 7 = 35.'),
        SolutionStep(text: 'Add the partial products: 2,100 + 35 = 2,135.'),
        SolutionStep(text: 'The answer is 2,135.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A classroom has 6 rows of benches, each row seating 9 students. How many students can sit in the classroom?',
      emoji: '🏫',
      options: ['52', '54', '56', '58'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total students = number of rows × students per row.',
        ),
        SolutionStep(text: '6 × 9.', emoji: '📐'),
        SolutionStep(text: 'Recall the 9 times table: 9, 18, 27, 36, 45, 54.'),
        SolutionStep(text: '6 × 9 = 54.'),
        SolutionStep(text: '54 students can sit in the classroom.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 89 × 27?',
      emoji: '✖️',
      options: ['2,403', '2,393', '2,483', '2,363'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Break 27 into 20 + 7, so 89 × 27 = 89 × 20 + 89 × 7.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 89 × 20 = 1,780.'),
        SolutionStep(text: 'Second partial product: 89 × 7 = 623.'),
        SolutionStep(text: 'Add the partial products: 1,780 + 623 = 2,403.'),
        SolutionStep(text: 'The answer is 2,403.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A stadium has 45 rows of seats, with 32 seats in each row. How many seats are there in total?',
      emoji: '🏟️',
      options: ['1,340', '1,350', '1,440', '1,450'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Total seats = number of rows × seats per row.'),
        SolutionStep(text: '45 × 32. Break 32 into 30 + 2.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 45 × 30 = 1,350.'),
        SolutionStep(text: 'Second partial product: 45 × 2 = 90.'),
        SolutionStep(text: 'Add the partial products: 1,350 + 90 = 1,440.'),
        SolutionStep(text: 'There are 1,440 seats in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A farmer plants 125 saplings in each row. How many saplings are planted in 16 rows?',
      emoji: '🌱',
      options: ['1,900', '1,950', '2,000', '2,050'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Total saplings = saplings per row × number of rows.',
        ),
        SolutionStep(text: '125 × 16. Break 16 into 10 + 6.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 125 × 10 = 1,250.'),
        SolutionStep(text: 'Second partial product: 125 × 6 = 750.'),
        SolutionStep(text: 'Add the partial products: 1,250 + 750 = 2,000.'),
        SolutionStep(text: '2,000 saplings are planted in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 6.5 × 4? (Think of 6.5 litres of milk 🥛 poured 4 times.)',
      emoji: '🥛',
      options: ['24', '25', '27', '26'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Ignore the decimal point for a moment and multiply 65 × 4.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '65 × 4 = 260 (since 60 × 4 = 240, and 5 × 4 = 20, giving 240 + 20 = 260).',
        ),
        SolutionStep(
          text:
              'Now place the decimal point back. Since 6.5 has 1 digit after the decimal point, the answer also needs 1 digit after the decimal point.',
        ),
        SolutionStep(text: '260 becomes 26.0, i.e. 26.'),
        SolutionStep(text: 'So 6.5 × 4 = 26.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 3.2 × 5? (Picture 3.2 kg of rice 🌾 weighed 5 times.)',
      emoji: '🌾',
      options: ['16', '15', '15.5', '16.5'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Ignore the decimal point and multiply 32 × 5.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '32 × 5 = 160 (since 30 × 5 = 150, and 2 × 5 = 10, giving 150 + 10 = 160).',
        ),
        SolutionStep(
          text:
              'Since 3.2 has 1 digit after the decimal point, place the decimal point 1 place from the right in 160.',
        ),
        SolutionStep(text: '160 becomes 16.0, i.e. 16.'),
        SolutionStep(text: 'So 3.2 × 5 = 16.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A ribbon 4.5 m long is needed for each gift. How much ribbon is needed for 6 gifts?',
      emoji: '🎀',
      options: ['26 m', '28 m', '29 m', '27 m'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Total ribbon = ribbon per gift × number of gifts.'),
        SolutionStep(
          text: 'Ignore the decimal point and multiply 45 × 6.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '45 × 6 = 270 (since 40 × 6 = 240, and 5 × 6 = 30, giving 240 + 30 = 270).',
        ),
        SolutionStep(
          text:
              'Since 4.5 has 1 digit after the decimal point, place the decimal point 1 place from the right in 270.',
        ),
        SolutionStep(text: '270 becomes 27.0, i.e. 27.'),
        SolutionStep(text: '27 m of ribbon is needed for 6 gifts.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 0.8 × 9?',
      emoji: '✖️',
      options: ['6.2', '7.2', '8.2', '7.8'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Ignore the decimal point and multiply 8 × 9.',
          emoji: '📐',
        ),
        SolutionStep(text: '8 × 9 = 72.'),
        SolutionStep(
          text:
              'Since 0.8 has 1 digit after the decimal point, place the decimal point 1 place from the right in 72.',
        ),
        SolutionStep(text: '72 becomes 7.2.'),
        SolutionStep(text: 'So 0.8 × 9 = 7.2.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A juice bottle holds 1.25 litres 🧃. How much juice is in 4 such bottles?',
      emoji: '🧃',
      options: ['4 litres', '4.5 litres', '5.5 litres', '5 litres'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Total juice = juice per bottle × number of bottles.',
        ),
        SolutionStep(
          text: 'Ignore the decimal point and multiply 125 × 4.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '125 × 4 = 500 (since 100 × 4 = 400, and 25 × 4 = 100, giving 400 + 100 = 500).',
        ),
        SolutionStep(
          text:
              'Since 1.25 has 2 digits after the decimal point, place the decimal point 2 places from the right in 500.',
        ),
        SolutionStep(text: '500 becomes 5.00, i.e. 5.'),
        SolutionStep(text: '5 litres of juice is in 4 bottles.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Neha buys 12 pencils 🖊️ at ₹6.50 each. How much does she spend in total?',
      emoji: '🖊️',
      options: ['₹78', '₹76', '₹77', '₹79'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Total cost = cost per pencil × number of pencils.'),
        SolutionStep(
          text: 'Ignore the decimal point and multiply 650 × 12.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Break 12 into 10 + 2: 650 × 10 = 6,500, and 650 × 2 = 1,300.',
        ),
        SolutionStep(text: 'Add the partial products: 6,500 + 1,300 = 7,800.'),
        SolutionStep(
          text:
              'Since 6.50 has 2 digits after the decimal point, place the decimal point 2 places from the right in 7,800.',
        ),
        SolutionStep(text: '7,800 becomes 78.00, i.e. 78.'),
        SolutionStep(text: 'Neha spends ₹78 in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 214 × 32?',
      emoji: '✖️',
      options: ['6,848', '6,748', '6,948', '6,648'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Break 32 into 30 + 2, so 214 × 32 = 214 × 30 + 214 × 2.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 214 × 30 = 6,420.'),
        SolutionStep(text: 'Second partial product: 214 × 2 = 428.'),
        SolutionStep(text: 'Add the partial products: 6,420 + 428 = 6,848.'),
        SolutionStep(text: 'The answer is 6,848.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A bakery makes 48 cupcakes 🧁 every day. How many cupcakes are made in 30 days?',
      emoji: '🧁',
      options: ['1,340', '1,440', '1,240', '1,540'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total cupcakes = cupcakes per day × number of days.',
        ),
        SolutionStep(text: '48 × 30.', emoji: '📐'),
        SolutionStep(text: 'Multiply 48 × 3 first: 48 × 3 = 144.'),
        SolutionStep(
          text:
              'Since we multiplied by 3 instead of 30, add back the extra zero: 144 × 10 = 1,440.',
        ),
        SolutionStep(text: '1,440 cupcakes are made in 30 days.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A school orders notebooks 📓 for all students. Each of the 28 classrooms gets 45 notebooks. How many notebooks were ordered in total?',
      emoji: '📓',
      options: ['1,160', '1,360', '1,260', '1,060'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Total notebooks = notebooks per classroom × number of classrooms.',
        ),
        SolutionStep(text: '45 × 28. Break 28 into 20 + 8.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 45 × 20 = 900.'),
        SolutionStep(text: 'Second partial product: 45 × 8 = 360.'),
        SolutionStep(text: 'Add the partial products: 900 + 360 = 1,260.'),
        SolutionStep(
          text: '1,260 notebooks were ordered in total.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 7 × 8?',
      emoji: '✖️',
      options: ['54', '56', '58', '64'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Recall the 7 times table: 7, 14, 21, 28, 35, 42, 49, 56.',
          emoji: '📋',
        ),
        SolutionStep(text: '7 × 8 is the 8th number in the 7 times table.'),
        SolutionStep(text: 'The answer is 56.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A cricket coach buys 9 bats 🏏 at ₹450 each. How much does he spend in total?',
      emoji: '🏏',
      options: ['₹3,950', '₹4,050', '₹4,150', '₹4,250'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Total cost = cost per bat × number of bats.'),
        SolutionStep(text: '450 × 9.', emoji: '📐'),
        SolutionStep(
          text: 'Break 450 into 400 + 50: 400 × 9 = 3,600, and 50 × 9 = 450.',
        ),
        SolutionStep(text: 'Add the partial products: 3,600 + 450 = 4,050.'),
        SolutionStep(text: 'He spends ₹4,050 in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 36 × 25?',
      emoji: '✖️',
      options: ['800', '850', '950', '900'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Break 25 into 20 + 5, so 36 × 25 = 36 × 20 + 36 × 5.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 36 × 20 = 720.'),
        SolutionStep(text: 'Second partial product: 36 × 5 = 180.'),
        SolutionStep(text: 'Add the partial products: 720 + 180 = 900.'),
        SolutionStep(text: 'The answer is 900.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A courier company delivers 63 parcels 📦 every day. How many parcels are delivered in 2 weeks?',
      emoji: '📦',
      options: ['852', '872', '882', '892'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: '2 weeks = 14 days, since 1 week has 7 days.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'Total parcels = parcels per day × number of days = 63 × 14.',
        ),
        SolutionStep(
          text: 'Break 14 into 10 + 4: 63 × 10 = 630, and 63 × 4 = 252.',
        ),
        SolutionStep(text: 'Add the partial products: 630 + 252 = 882.'),
        SolutionStep(text: '882 parcels are delivered in 2 weeks.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 4.2 × 3? (Picture 4.2 metres of cloth 🧵 cut 3 times.)',
      emoji: '🧵',
      options: ['12.6', '11.6', '12.2', '13.2'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Ignore the decimal point and multiply 42 × 3.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '42 × 3 = 126 (since 40 × 3 = 120, and 2 × 3 = 6, giving 120 + 6 = 126).',
        ),
        SolutionStep(
          text:
              'Since 4.2 has 1 digit after the decimal point, place the decimal point 1 place from the right in 126.',
        ),
        SolutionStep(text: '126 becomes 12.6.'),
        SolutionStep(text: 'So 4.2 × 3 = 12.6.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'A farmer sells wheat at ₹22.50 per kg. How much will 8 kg cost?',
      emoji: '🌾',
      options: ['₹180', '₹170', '₹190', '₹200'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Total cost = price per kg × number of kg.'),
        SolutionStep(
          text: 'Ignore the decimal point and multiply 2,250 × 8.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              '2,250 × 8 = 18,000 (since 2,000 × 8 = 16,000, and 250 × 8 = 2,000, giving 16,000 + 2,000 = 18,000).',
        ),
        SolutionStep(
          text:
              'Since 22.50 has 2 digits after the decimal point, place the decimal point 2 places from the right in 18,000.',
        ),
        SolutionStep(text: '18,000 becomes 180.00, i.e. 180.'),
        SolutionStep(text: '8 kg of wheat will cost ₹180.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 500 × 40?',
      emoji: '✖️',
      options: ['18,000', '20,000', '22,000', '2,000'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Multiply the non-zero digits first: 5 × 4 = 20.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Count the total zeros in both numbers: 500 has 2 zeros, 40 has 1 zero, so 3 zeros in total.',
        ),
        SolutionStep(text: 'Attach those 3 zeros to 20: 20,000.'),
        SolutionStep(text: 'The answer is 20,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A bus company has 34 buses 🚌, each completing 65 km every day. How many kilometres do all buses cover together in a day?',
      emoji: '🚌',
      options: ['2,110 km', '2,310 km', '2,410 km', '2,210 km'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Total kilometres = km per bus × number of buses.'),
        SolutionStep(text: '65 × 34. Break 34 into 30 + 4.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 65 × 30 = 1,950.'),
        SolutionStep(text: 'Second partial product: 65 × 4 = 260.'),
        SolutionStep(text: 'Add the partial products: 1,950 + 260 = 2,210.'),
        SolutionStep(
          text: 'All buses together cover 2,210 km in a day.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
  ],
);
