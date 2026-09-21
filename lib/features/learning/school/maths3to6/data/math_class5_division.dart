import '../models/math_question.dart';

const class5Division = MathTopic(
  id: 'class5_division',
  title: 'Division',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt: 'What is 84 ÷ 4?',
      emoji: '➗',
      options: ['21', '20', '22', '24'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the tens first: 8 ÷ 4 = 2. Write 2 above the tens digit.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 4: divide 4 ÷ 4 = 1. Write 1 above the ones digit.',
        ),
        SolutionStep(text: 'Combine the digits written: 21.'),
        SolutionStep(text: 'The answer is 21.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 96 ÷ 6?',
      emoji: '➗',
      options: ['14', '15', '16', '18'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the tens first: 9 ÷ 6 = 1, remainder 3 (since 6 × 1 = 6, and 9 - 6 = 3).',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 6, next to the remainder 3, making 36.',
        ),
        SolutionStep(text: 'Divide 36 ÷ 6 = 6 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 6, giving 16.',
        ),
        SolutionStep(text: 'The answer is 16.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 452 ÷ 4?',
      emoji: '➗',
      options: ['112', '113', '123', '111'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Divide the hundreds digit: 4 ÷ 4 = 1, remainder 0.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the tens digit 5: 5 ÷ 4 = 1, remainder 1 (since 4 × 1 = 4, and 5 - 4 = 1).',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 2, next to the remainder 1, making 12.',
        ),
        SolutionStep(text: 'Divide 12 ÷ 4 = 3 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1, 1, 3, giving 113.',
        ),
        SolutionStep(text: 'The answer is 113.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 738 ÷ 6?',
      emoji: '➗',
      options: ['123', '122', '113', '132'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the hundreds digit: 7 ÷ 6 = 1, remainder 1 (since 6 × 1 = 6, and 7 - 6 = 1).',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the tens digit 3, next to the remainder 1, making 13.',
        ),
        SolutionStep(
          text:
              'Divide 13 ÷ 6 = 2, remainder 1 (since 6 × 2 = 12, and 13 - 12 = 1).',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 8, next to the remainder 1, making 18.',
        ),
        SolutionStep(text: 'Divide 18 ÷ 6 = 3 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1, 2, 3, giving 123.',
        ),
        SolutionStep(text: 'The answer is 123.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 156 ÷ 12?',
      emoji: '➗',
      options: ['12', '14', '13', '11'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the first two digits, 15. Since 12 fits into 15 once, divide 15 ÷ 12 = 1, remainder 3 (15 - 12 = 3).',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 6, next to the remainder 3, making 36.',
        ),
        SolutionStep(text: 'Divide 36 ÷ 12 = 3 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 3, giving 13.',
        ),
        SolutionStep(text: 'The answer is 13.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 4,896 ÷ 8?',
      emoji: '➗',
      options: ['602', '622', '601', '612'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the thousands digit: 4 ÷ 8. It does not fit, so combine with the next digit: 48 ÷ 8 = 6, remainder 0.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the tens digit 9: 9 ÷ 8. Wait — since 4 ÷ 8 did not fit alone, the first quotient digit sits over the 8 of 48.',
        ),
        SolutionStep(
          text:
              'After 48 ÷ 8 = 6 (remainder 0), bring down the next digit 9: 09 ÷ 8 = 1, remainder 1 (8 × 1 = 8, 9 - 8 = 1).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 6, next to remainder 1, making 16.',
        ),
        SolutionStep(text: 'Divide 16 ÷ 8 = 2 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 6, 1, 2, giving 612.',
        ),
        SolutionStep(text: 'The answer is 612.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 7 ÷ 2, written as a quotient with a remainder?',
      emoji: '➗',
      options: [
        'Quotient 3, remainder 2',
        'Quotient 4, remainder 0',
        'Quotient 2, remainder 3',
        'Quotient 3, remainder 1',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Find the biggest multiple of 2 that is not more than 7: 2 × 3 = 6.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'So the quotient (how many full groups of 2 fit) is 3.',
        ),
        SolutionStep(text: 'Subtract to find what is left over: 7 - 6 = 1.'),
        SolutionStep(
          text:
              'This leftover, 1, is the remainder, and it must always be smaller than the divisor (2).',
        ),
        SolutionStep(text: '7 ÷ 2 = quotient 3, remainder 1.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 59 ÷ 7?',
      emoji: '➗',
      options: [
        'Quotient 7, remainder 10',
        'Quotient 8, remainder 3',
        'Quotient 8, remainder 4',
        'Quotient 9, remainder 4',
      ],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Find the biggest multiple of 7 that is not more than 59: 7 × 8 = 56.',
          emoji: '📋',
        ),
        SolutionStep(text: 'So the quotient is 8.'),
        SolutionStep(text: 'Subtract: 59 - 56 = 3.'),
        SolutionStep(
          text:
              'The remainder is 3, and it is smaller than the divisor 7, so this is correct.',
        ),
        SolutionStep(text: '59 ÷ 7 = quotient 8, remainder 3.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          '235 sweets are packed equally into boxes of 9. How many full boxes can be made, and how many sweets are left over?',
      emoji: '🍬',
      options: [
        '26 boxes, 1 left over',
        '25 boxes, 10 left over',
        '26 boxes, 0 left over',
        '25 boxes, 1 left over',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the first two digits: 23 ÷ 9 = 2, remainder 5 (9 × 2 = 18, 23 - 18 = 5).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 5, next to remainder 5, making 55.',
        ),
        SolutionStep(
          text: 'Divide 55 ÷ 9 = 6, remainder 1 (9 × 6 = 54, 55 - 54 = 1).',
        ),
        SolutionStep(
          text: 'Combine the digits written above: 2 and 6, giving 26.',
        ),
        SolutionStep(
          text: '26 full boxes can be made, with 1 sweet left over.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          '₹864 is shared equally among 8 friends. How much does each friend get?',
      emoji: '💰',
      options: ['₹106', '₹108', '₹107', '₹118'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Each friend gets = total money ÷ number of friends.',
        ),
        SolutionStep(text: '864 ÷ 8.', emoji: '📐'),
        SolutionStep(
          text: 'Divide the hundreds digit: 8 ÷ 8 = 1, remainder 0.',
        ),
        SolutionStep(
          text:
              'Bring down the tens digit 6: 6 ÷ 8. Too small, so combine with next digit.',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 4, making 64. Divide 64 ÷ 8 = 8 exactly, remainder 0.',
        ),
        SolutionStep(
          text: 'Combine the digits written above: 1, 0, 8, giving 108.',
        ),
        SolutionStep(text: 'Each friend gets ₹108.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A shopkeeper buys 15 dozen bangles for ₹2,700. What is the cost of 1 dozen bangles?',
      emoji: '💍',
      options: ['₹170', '₹190', '₹185', '₹180'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Cost of 1 dozen = total cost ÷ number of dozens.'),
        SolutionStep(text: '2,700 ÷ 15.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 27. Since 15 fits into 27 once, 27 ÷ 15 = 1, remainder 12 (27 - 15 = 12).',
        ),
        SolutionStep(
          text:
              'Bring down the next digit 0, next to remainder 12, making 120.',
        ),
        SolutionStep(text: 'Divide 120 ÷ 15 = 8 exactly, remainder 0.'),
        SolutionStep(
          text: 'Bring down the final digit 0, making 0. Divide 0 ÷ 15 = 0.',
        ),
        SolutionStep(
          text: 'Combine the digits written above: 1, 8, 0, giving 180.',
        ),
        SolutionStep(text: '1 dozen bangles costs ₹180.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 968 ÷ 11?',
      emoji: '➗',
      options: ['86', '87', '88', '89'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the first two digits, 96. Since 11 fits into 96, divide 96 ÷ 11 = 8, remainder 8 (11 × 8 = 88, 96 - 88 = 8).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 8, next to remainder 8, making 88.',
        ),
        SolutionStep(text: 'Divide 88 ÷ 11 = 8 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 8 and 8, giving 88.',
        ),
        SolutionStep(text: 'The answer is 88.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 1,536 ÷ 16?',
      emoji: '➗',
      options: ['96', '94', '95', '86'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the first two digits, 15. Since 16 does not fit into 15, take the first three digits: 153.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Divide 153 ÷ 16 = 9, remainder 9 (16 × 9 = 144, 153 - 144 = 9).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 6, next to remainder 9, making 96.',
        ),
        SolutionStep(text: 'Divide 96 ÷ 16 = 6 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 9 and 6, giving 96.',
        ),
        SolutionStep(text: 'The answer is 96.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A ribbon that is 5,400 cm long is cut into 25 equal pieces. How long is each piece?',
      emoji: '🎀',
      options: ['214 cm', '216 cm', '206 cm', '224 cm'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Length of each piece = total length ÷ number of pieces.',
        ),
        SolutionStep(text: '5,400 ÷ 25.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 54. Since 25 fits into 54 twice, 54 ÷ 25 = 2, remainder 4 (25 × 2 = 50, 54 - 50 = 4).',
        ),
        SolutionStep(
          text: 'Bring down the next digit 0, next to remainder 4, making 40.',
        ),
        SolutionStep(
          text: 'Divide 40 ÷ 25 = 1, remainder 15 (25 × 1 = 25, 40 - 25 = 15).',
        ),
        SolutionStep(
          text:
              'Bring down the last digit 0, next to remainder 15, making 150.',
        ),
        SolutionStep(text: 'Divide 150 ÷ 25 = 6 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 2, 1, 6, giving 216.',
        ),
        SolutionStep(text: 'Each piece is 216 cm long.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A farmer has 342 mangoes and wants to pack them into baskets of 10. How many full baskets can be made, and how many mangoes are left over?',
      emoji: '🧺',
      options: [
        '34 baskets, 0 left over',
        '33 baskets, 12 left over',
        '34 baskets, 2 left over',
        '35 baskets, 2 left over',
      ],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Divide 342 ÷ 10.', emoji: '📐'),
        SolutionStep(
          text:
              'Dividing by 10 means looking at all digits except the last one as the quotient: 34.',
        ),
        SolutionStep(
          text:
              'The last digit, 2, is what is left over since it cannot make another full group of 10.',
        ),
        SolutionStep(text: 'Check: 10 × 34 = 340, and 342 - 340 = 2.'),
        SolutionStep(
          text: '34 full baskets can be made, with 2 mangoes left over.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: '19 pens cost ₹247 in total. What is the cost of 1 pen?',
      emoji: '🖊️',
      options: ['₹11', '₹12', '₹13', '₹14'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Cost of 1 pen = total cost ÷ number of pens.'),
        SolutionStep(text: '247 ÷ 19.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 24. Since 19 fits into 24 once, 24 ÷ 19 = 1, remainder 5 (24 - 19 = 5).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 7, next to remainder 5, making 57.',
        ),
        SolutionStep(text: 'Divide 57 ÷ 19 = 3 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 3, giving 13.',
        ),
        SolutionStep(text: 'Each pen costs ₹13.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 3,125 ÷ 25?',
      emoji: '➗',
      options: ['123', '125', '124', '135'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the first two digits, 31. Since 25 fits into 31 once, 31 ÷ 25 = 1, remainder 6 (31 - 25 = 6).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the next digit 2, next to remainder 6, making 62.',
        ),
        SolutionStep(
          text: 'Divide 62 ÷ 25 = 2, remainder 12 (25 × 2 = 50, 62 - 50 = 12).',
        ),
        SolutionStep(
          text:
              'Bring down the last digit 5, next to remainder 12, making 125.',
        ),
        SolutionStep(text: 'Divide 125 ÷ 25 = 5 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1, 2, 5, giving 125.',
        ),
        SolutionStep(text: 'The answer is 125.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A school has 260 students to be arranged into equal rows of 13 for assembly. How many rows are needed?',
      emoji: '🏫',
      options: ['20', '18', '19', '21'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Number of rows = total students ÷ students per row.',
        ),
        SolutionStep(text: '260 ÷ 13.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 26. Since 13 fits into 26 exactly twice, 26 ÷ 13 = 2, remainder 0.',
        ),
        SolutionStep(
          text: 'Bring down the last digit 0, next to remainder 0, making 0.',
        ),
        SolutionStep(text: 'Divide 0 ÷ 13 = 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 2 and 0, giving 20.',
        ),
        SolutionStep(text: '20 rows are needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 500 ÷ 8, including the remainder?',
      emoji: '➗',
      options: [
        'Quotient 62, remainder 4',
        'Quotient 62, remainder 3',
        'Quotient 63, remainder 4',
        'Quotient 61, remainder 4',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the first two digits: 50 ÷ 8 = 6, remainder 2 (8 × 6 = 48, 50 - 48 = 2).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 0, next to remainder 2, making 20.',
        ),
        SolutionStep(
          text: 'Divide 20 ÷ 8 = 2, remainder 4 (8 × 2 = 16, 20 - 16 = 4).',
        ),
        SolutionStep(
          text:
              'Combine the digits written above: 6 and 2, giving quotient 62.',
        ),
        SolutionStep(text: '500 ÷ 8 = quotient 62, remainder 4.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A cost of ₹1,764 is split equally among 12 students for a class trip. How much does each student pay?',
      emoji: '🚌',
      options: ['₹146', '₹148', '₹157', '₹147'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Each student pays = total cost ÷ number of students.',
        ),
        SolutionStep(text: '1,764 ÷ 12.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 17. Since 12 fits into 17 once, 17 ÷ 12 = 1, remainder 5 (17 - 12 = 5).',
        ),
        SolutionStep(
          text: 'Bring down the next digit 6, next to remainder 5, making 56.',
        ),
        SolutionStep(
          text: 'Divide 56 ÷ 12 = 4, remainder 8 (12 × 4 = 48, 56 - 48 = 8).',
        ),
        SolutionStep(
          text: 'Bring down the last digit 4, next to remainder 8, making 84.',
        ),
        SolutionStep(text: 'Divide 84 ÷ 12 = 7 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1, 4, 7, giving 147.',
        ),
        SolutionStep(text: 'Each student pays ₹147.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 63 ÷ 9?',
      emoji: '➗',
      options: ['6', '8', '9', '7'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Recall the 9 times table: 9, 18, 27, 36, 45, 54, 63...',
          emoji: '📋',
        ),
        SolutionStep(text: '63 is the 7th number in the 9 times table.'),
        SolutionStep(text: 'So 9 × 7 = 63, meaning 63 ÷ 9 = 7.'),
        SolutionStep(text: 'The answer is 7.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 999 ÷ 27?',
      emoji: '➗',
      options: ['35', '36', '37', '34'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the first two digits, 99. Since 27 fits into 99, divide 99 ÷ 27 = 3, remainder 18 (27 × 3 = 81, 99 - 81 = 18).',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 9, next to remainder 18, making 189.',
        ),
        SolutionStep(
          text: 'Divide 189 ÷ 27 = 7 exactly, remainder 0 (27 × 7 = 189).',
        ),
        SolutionStep(
          text: 'Combine the digits written above: 3 and 7, giving 37.',
        ),
        SolutionStep(text: 'The answer is 37.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Meera has ₹450 and wants to buy notebooks that cost ₹18 each. How many notebooks can she buy?',
      emoji: '📓',
      options: ['25', '23', '24', '26'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Number of notebooks = total money ÷ cost per notebook.',
        ),
        SolutionStep(text: '450 ÷ 18.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 45. Since 18 fits into 45 twice, 45 ÷ 18 = 2, remainder 9 (18 × 2 = 36, 45 - 36 = 9).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 0, next to remainder 9, making 90.',
        ),
        SolutionStep(text: 'Divide 90 ÷ 18 = 5 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 2 and 5, giving 25.',
        ),
        SolutionStep(text: 'Meera can buy 25 notebooks.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 100 ÷ 3, including the remainder?',
      emoji: '➗',
      options: [
        'Quotient 33, remainder 0',
        'Quotient 33, remainder 1',
        'Quotient 34, remainder 1',
        'Quotient 32, remainder 4',
      ],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the first two digits: 10 ÷ 3 = 3, remainder 1 (3 × 3 = 9, 10 - 9 = 1).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 0, next to remainder 1, making 10.',
        ),
        SolutionStep(
          text: 'Divide 10 ÷ 3 = 3, remainder 1 (3 × 3 = 9, 10 - 9 = 1).',
        ),
        SolutionStep(
          text:
              'Combine the digits written above: 3 and 3, giving quotient 33.',
        ),
        SolutionStep(text: '100 ÷ 3 = quotient 33, remainder 1.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A tank holds 2,880 litres of water and is filled equally by 24 pipes running together. How much water does each pipe deliver?',
      emoji: '🚰',
      options: ['110 litres', '115 litres', '120 litres', '125 litres'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Water per pipe = total water ÷ number of pipes.'),
        SolutionStep(text: '2,880 ÷ 24.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 28. Since 24 fits into 28 once, 28 ÷ 24 = 1, remainder 4 (28 - 24 = 4).',
        ),
        SolutionStep(
          text: 'Bring down the next digit 8, next to remainder 4, making 48.',
        ),
        SolutionStep(text: 'Divide 48 ÷ 24 = 2 exactly, remainder 0.'),
        SolutionStep(
          text: 'Bring down the last digit 0, making 0. Divide 0 ÷ 24 = 0.',
        ),
        SolutionStep(
          text: 'Combine the digits written above: 1, 2, 0, giving 120.',
        ),
        SolutionStep(text: 'Each pipe delivers 120 litres.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          '17 sacks of rice weigh 1,428 kg in total, all sacks being equal. What is the weight of 1 sack?',
      emoji: '🌾',
      options: ['82 kg', '83 kg', '84 kg', '85 kg'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Weight of 1 sack = total weight ÷ number of sacks.',
        ),
        SolutionStep(text: '1,428 ÷ 17.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 14. Since 17 does not fit into 14, take the first three digits: 142.',
        ),
        SolutionStep(
          text:
              'Divide 142 ÷ 17 = 8, remainder 6 (17 × 8 = 136, 142 - 136 = 6).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 8, next to remainder 6, making 68.',
        ),
        SolutionStep(text: 'Divide 68 ÷ 17 = 4 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 8 and 4, giving 84.',
        ),
        SolutionStep(text: 'Each sack weighs 84 kg.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 45 ÷ 5?',
      emoji: '➗',
      options: ['8', '9', '10', '7'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the 5 times table: 5, 10, 15, 20, 25, 30, 35, 40, 45...',
          emoji: '📋',
        ),
        SolutionStep(text: '45 is the 9th number in the 5 times table.'),
        SolutionStep(text: 'So 5 × 9 = 45, meaning 45 ÷ 5 = 9.'),
        SolutionStep(text: 'The answer is 9.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A dairy farmer collects 384 litres of milk and pours it equally into 8 cans. How much milk does each can hold?',
      emoji: '🥛',
      options: ['48 litres', '46 litres', '52 litres', '44 litres'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Milk per can = total milk ÷ number of cans.'),
        SolutionStep(text: '384 ÷ 8.', emoji: '📐'),
        SolutionStep(
          text:
              'Divide the hundreds digit: 3 ÷ 8 does not fit, so combine with next digit: 38 ÷ 8 = 4, remainder 6 (8 × 4 = 32, 38 - 32 = 6).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 4, next to remainder 6, making 64.',
        ),
        SolutionStep(text: 'Divide 64 ÷ 8 = 8 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 4 and 8, giving 48.',
        ),
        SolutionStep(text: 'Each can holds 48 litres.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 72 ÷ 8?',
      emoji: '➗',
      options: ['9', '7', '8', '6'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the 8 times table: 8, 16, 24, 32, 40, 48, 56, 64, 72...',
          emoji: '📋',
        ),
        SolutionStep(text: '72 is the 9th number in the 8 times table.'),
        SolutionStep(text: 'So 8 × 9 = 72, meaning 72 ÷ 8 = 9.'),
        SolutionStep(text: 'The answer is 9.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A gardener has 675 saplings and wants to plant them in 15 equal rows. How many saplings go in each row?',
      emoji: '🌱',
      options: ['45', '43', '44', '46'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Saplings per row = total saplings ÷ number of rows.',
        ),
        SolutionStep(text: '675 ÷ 15.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 67. Since 15 fits into 67, divide 67 ÷ 15 = 4, remainder 7 (15 × 4 = 60, 67 - 60 = 7).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 5, next to remainder 7, making 75.',
        ),
        SolutionStep(text: 'Divide 75 ÷ 15 = 5 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 4 and 5, giving 45.',
        ),
        SolutionStep(text: 'Each row gets 45 saplings.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A box of 144 crayons is shared equally among 12 children. How many crayons does each child get?',
      emoji: '🖍️',
      options: ['10', '12', '11', '13'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Crayons per child = total crayons ÷ number of children.',
        ),
        SolutionStep(text: '144 ÷ 12.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 14. Since 12 fits into 14 once, 14 ÷ 12 = 1, remainder 2 (14 - 12 = 2).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 4, next to remainder 2, making 24.',
        ),
        SolutionStep(text: 'Divide 24 ÷ 12 = 2 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 2, giving 12.',
        ),
        SolutionStep(text: 'Each child gets 12 crayons.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 84 ÷ 7?',
      emoji: '➗',
      options: ['12', '11', '13', '10'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the tens first: 8 ÷ 7 = 1, remainder 1 (7 × 1 = 7, 8 - 7 = 1).',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 4, next to remainder 1, making 14.',
        ),
        SolutionStep(text: 'Divide 14 ÷ 7 = 2 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 2, giving 12.',
        ),
        SolutionStep(text: 'The answer is 12.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A fruit seller has 486 bananas and packs them into bunches of 6. How many bunches can be made?',
      emoji: '🍌',
      options: ['79', '80', '82', '81'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Number of bunches = total bananas ÷ bananas per bunch.',
        ),
        SolutionStep(text: '486 ÷ 6.', emoji: '📐'),
        SolutionStep(
          text:
              'Divide the hundreds digit: 4 ÷ 6 does not fit, so combine: 48 ÷ 6 = 8, remainder 0.',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 6, next to remainder 0, making 6.',
        ),
        SolutionStep(text: 'Divide 6 ÷ 6 = 1 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 8 and 1, giving 81.',
        ),
        SolutionStep(text: '81 bunches can be made.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A cricket team scored 210 runs in 21 overs, scoring the same number of runs every over. How many runs were scored per over?',
      emoji: '🏏',
      options: ['9', '11', '10', '12'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Runs per over = total runs ÷ number of overs.'),
        SolutionStep(text: '210 ÷ 21.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 21. Since 21 fits into 21 exactly once, 21 ÷ 21 = 1, remainder 0.',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 0, next to remainder 0, making 0.',
        ),
        SolutionStep(text: 'Divide 0 ÷ 21 = 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 0, giving 10.',
        ),
        SolutionStep(text: '10 runs were scored per over.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 91 ÷ 13?',
      emoji: '➗',
      options: ['5', '6', '8', '7'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Recall multiples of 13: 13, 26, 39, 52, 65, 78, 91...',
          emoji: '📋',
        ),
        SolutionStep(text: '91 is the 7th multiple of 13.'),
        SolutionStep(text: 'So 13 × 7 = 91, meaning 91 ÷ 13 = 7.'),
        SolutionStep(text: 'The answer is 7.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A baker has 528 cupcakes to place into boxes of 24. How many boxes are needed?',
      emoji: '🧁',
      options: ['20', '22', '21', '23'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Number of boxes = total cupcakes ÷ cupcakes per box.',
        ),
        SolutionStep(text: '528 ÷ 24.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 52. Since 24 fits into 52 twice, 52 ÷ 24 = 2, remainder 4 (24 × 2 = 48, 52 - 48 = 4).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 8, next to remainder 4, making 48.',
        ),
        SolutionStep(text: 'Divide 48 ÷ 24 = 2 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 2 and 2, giving 22.',
        ),
        SolutionStep(text: '22 boxes are needed.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A charity distributes ₹936 equally among 12 needy families. How much does each family receive?',
      emoji: '🤝',
      options: ['₹76', '₹78', '₹77', '₹79'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Amount per family = total money ÷ number of families.',
        ),
        SolutionStep(text: '936 ÷ 12.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 93. Since 12 fits into 93, divide 93 ÷ 12 = 7, remainder 9 (12 × 7 = 84, 93 - 84 = 9).',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 6, next to remainder 9, making 96.',
        ),
        SolutionStep(text: 'Divide 96 ÷ 12 = 8 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 7 and 8, giving 78.',
        ),
        SolutionStep(text: 'Each family receives ₹78.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 56 ÷ 8, and is there a remainder?',
      emoji: '➗',
      options: [
        'Quotient 6, remainder 2',
        'Quotient 7, remainder 1',
        'Quotient 8, remainder 0',
        'Quotient 7, remainder 0',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Recall the 8 times table: 8, 16, 24, 32, 40, 48, 56...',
          emoji: '📋',
        ),
        SolutionStep(
          text: '56 is exactly the 7th number in the 8 times table.',
        ),
        SolutionStep(
          text: 'So 8 × 7 = 56 exactly, meaning there is no remainder.',
        ),
        SolutionStep(text: '56 ÷ 8 = quotient 7, remainder 0.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A total of 1,050 chairs need to be arranged into 30 equal rows for a function. How many chairs go in each row?',
      emoji: '🪑',
      options: ['33', '34', '36', '35'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Chairs per row = total chairs ÷ number of rows.'),
        SolutionStep(text: '1,050 ÷ 30.', emoji: '📐'),
        SolutionStep(
          text:
              'Dividing by 30 is like dividing by 3 then by 10, or directly: 105 ÷ 3 = 35, then adjust for the extra zero.',
        ),
        SolutionStep(text: 'Check directly: 30 × 35 = 1,050. That matches!'),
        SolutionStep(text: 'Each row has 35 chairs.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 810 ÷ 9?',
      emoji: '➗',
      options: ['80', '85', '90', '95'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Divide the hundreds digit: 8 ÷ 9 does not fit, so combine: 81 ÷ 9 = 9, remainder 0.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'Bring down the ones digit 0, next to remainder 0, making 0.',
        ),
        SolutionStep(text: 'Divide 0 ÷ 9 = 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 9 and 0, giving 90.',
        ),
        SolutionStep(text: 'The answer is 90.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A water tanker carries 2,400 litres and fills tanks that each hold 60 litres. How many tanks can it fill completely?',
      emoji: '🚛',
      options: ['38', '39', '41', '40'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Number of tanks = total water ÷ water per tank.'),
        SolutionStep(text: '2,400 ÷ 60.', emoji: '📐'),
        SolutionStep(
          text:
              'Dividing by 60 is like dividing by 6 then by 10: 240 ÷ 6 = 40, then adjust for the extra zero cancelled.',
        ),
        SolutionStep(text: 'Check directly: 60 × 40 = 2,400. That matches!'),
        SolutionStep(
          text: 'The tanker can fill 40 tanks completely.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A carton holds 288 apples. If they are divided equally among 16 baskets, how many apples does each basket get?',
      emoji: '🧺',
      options: ['16', '17', '18', '19'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Apples per basket = total apples ÷ number of baskets.',
        ),
        SolutionStep(text: '288 ÷ 16.', emoji: '📐'),
        SolutionStep(
          text:
              'Look at the first two digits, 28. Since 16 fits into 28 once, 28 ÷ 16 = 1, remainder 12 (28 - 16 = 12).',
        ),
        SolutionStep(
          text:
              'Bring down the ones digit 8, next to remainder 12, making 128.',
        ),
        SolutionStep(text: 'Divide 128 ÷ 16 = 8 exactly, remainder 0.'),
        SolutionStep(
          text: 'Combine the digits written above: 1 and 8, giving 18.',
        ),
        SolutionStep(text: 'Each basket gets 18 apples.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
  ],
);
