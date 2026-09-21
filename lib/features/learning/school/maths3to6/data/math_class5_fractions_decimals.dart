import '../models/math_question.dart';

const class5FractionsDecimals = MathTopic(
  id: 'class5_fractions_decimals',
  title: 'Fractions and Decimals',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt:
          'What is 1/2 + 1/4? (Imagine a pizza 🍕 cut in halves and another cut in quarters.)',
      emoji: '🍕',
      options: ['3/4', '2/6', '2/4', '1/6'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a pizza cut into 2 halves 🍕🍕 and an identical pizza cut into 4 quarters 🍕🍕🍕🍕.',
        ),
        SolutionStep(
          text:
              'The denominators are different (2 and 4), so we cannot add the numerators directly yet.',
        ),
        SolutionStep(
          text:
              'Find a common denominator: 4 is a multiple of both 2 and 4, so use 4 as the common denominator.',
        ),
        SolutionStep(
          text:
              'Convert 1/2 to quarters: multiply top and bottom by 2, giving 2/4.',
        ),
        SolutionStep(
          text:
              'Now add: 2/4 + 1/4 = 3/4 (add numerators, keep the denominator).',
        ),
        SolutionStep(
          text: 'So 1/2 + 1/4 = 3/4 — three quarter-slices of pizza.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'What is 1/3 + 1/6? (Think of a chocolate bar 🍫 split into thirds and another split into sixths.)',
      emoji: '🍫',
      options: ['2/9', '2/6', '1/2', '1/18'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a chocolate bar cut into 3 equal pieces 🟫🟫🟫 and an identical bar cut into 6 equal pieces 🟫🟫🟫🟫🟫🟫.',
        ),
        SolutionStep(
          text:
              'The denominators (3 and 6) are different, so first find a common denominator.',
        ),
        SolutionStep(
          text: '6 is a multiple of 3, so use 6 as the common denominator.',
        ),
        SolutionStep(
          text:
              'Convert 1/3 to sixths: multiply top and bottom by 2, giving 2/6.',
        ),
        SolutionStep(
          text:
              'Now add: 2/6 + 1/6 = 3/6 (add numerators, keep the denominator).',
        ),
        SolutionStep(
          text: 'Simplify 3/6 by dividing top and bottom by 3: 3/6 = 1/2.',
        ),
        SolutionStep(text: 'So 1/3 + 1/6 = 1/2.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 3/4 - 1/2? (Picture a measuring scale 📏 showing 3/4 full, then 1/2 poured out.)',
      emoji: '📏',
      options: ['2/2', '1/4', '2/4', '1/2'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Picture a jug marked in quarters, filled to 3/4.'),
        SolutionStep(
          text:
              'The denominators (4 and 2) are different, so find a common denominator first.',
        ),
        SolutionStep(
          text: '4 is a multiple of 2, so use 4 as the common denominator.',
        ),
        SolutionStep(
          text:
              'Convert 1/2 to quarters: multiply top and bottom by 2, giving 2/4.',
        ),
        SolutionStep(
          text:
              'Now subtract: 3/4 - 2/4 = 1/4 (subtract numerators, keep the denominator).',
        ),
        SolutionStep(
          text: 'So 3/4 - 1/2 = 1/4 remains in the jug.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'What is 2/3 - 1/6? (Imagine a chocolate bar 🍫 with 2/3 shaded, then 1/6 unshaded.)',
      emoji: '🍫',
      options: ['1/2', '1/3', '1/6', '3/6'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a chocolate bar cut into 6 equal pieces (since 6 is a multiple of both 3 and 6).',
          emoji: '🟫',
        ),
        SolutionStep(
          text:
              'Convert 2/3 to sixths: multiply top and bottom by 2, giving 4/6.',
        ),
        SolutionStep(
          text:
              'Now subtract: 4/6 - 1/6 = 3/6 (subtract numerators, keep the denominator).',
        ),
        SolutionStep(
          text: 'Simplify 3/6 by dividing top and bottom by 3: 3/6 = 1/2.',
        ),
        SolutionStep(text: 'So 2/3 - 1/6 = 1/2.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 1/4 + 1/3? (Picture two identical chocolate bars 🍫 cut into quarters and thirds.)',
      emoji: '🍫',
      options: ['2/7', '5/12', '7/12', '2/12'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'The denominators are 4 and 3, which share no common multiple smaller than 12, so use 12 as the common denominator.',
          emoji: '🟫',
        ),
        SolutionStep(
          text:
              'Convert 1/4 to twelfths: multiply top and bottom by 3, giving 3/12.',
        ),
        SolutionStep(
          text:
              'Convert 1/3 to twelfths: multiply top and bottom by 4, giving 4/12.',
        ),
        SolutionStep(
          text:
              'Now add: 3/12 + 4/12 = 7/12 (add numerators, keep the denominator).',
        ),
        SolutionStep(text: 'So 1/4 + 1/3 = 7/12.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Convert the fraction 1/2 to a decimal.',
      emoji: '📏',
      options: ['0.2', '0.12', '1.2', '0.5'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a measuring scale 📏 divided into 2 equal parts, with 1 part marked.',
        ),
        SolutionStep(
          text:
              'To convert 1/2 to a decimal, divide the numerator by the denominator: 1 ÷ 2.',
        ),
        SolutionStep(
          text:
              '1 ÷ 2 = 0.5 (since 2 does not go into 1, we add a decimal point and a zero: 10 ÷ 2 = 5).',
        ),
        SolutionStep(text: 'So 1/2 as a decimal is 0.5.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Convert the fraction 3/4 to a decimal.',
      emoji: '📏',
      options: ['0.34', '0.43', '3.4', '0.75'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a pizza 🍕 cut into 4 slices with 3 shaded.',
        ),
        SolutionStep(
          text:
              'To convert 3/4 to a decimal, divide the numerator by the denominator: 3 ÷ 4.',
        ),
        SolutionStep(
          text:
              'Add a decimal point and zeros: 30 ÷ 4 = 7, remainder 2. Write 0.7 so far.',
        ),
        SolutionStep(
          text: 'Bring down another zero: 20 ÷ 4 = 5, remainder 0. Write 0.75.',
        ),
        SolutionStep(text: 'So 3/4 as a decimal is 0.75.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Convert the decimal 0.25 to a fraction in simplest form.',
      emoji: '📏',
      options: ['25/100', '1/4', '1/25', '2/5'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              '0.25 means 25 hundredths, since there are 2 digits after the decimal point.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Write it as a fraction: 25/100.'),
        SolutionStep(
          text:
              'Simplify by dividing top and bottom by 25: 25 ÷ 25 = 1, and 100 ÷ 25 = 4.',
        ),
        SolutionStep(text: 'So 0.25 simplifies to 1/4.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Convert the decimal 0.6 to a fraction in simplest form.',
      emoji: '📏',
      options: ['3/5', '6/100', '6/10', '6/1'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              '0.6 means 6 tenths, since there is 1 digit after the decimal point.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Write it as a fraction: 6/10.'),
        SolutionStep(
          text:
              'Simplify by dividing top and bottom by 2: 6 ÷ 2 = 3, and 10 ÷ 2 = 5.',
        ),
        SolutionStep(text: 'So 0.6 simplifies to 3/5.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Which is greater: 0.45 or 0.4?',
      emoji: '📏',
      options: [
        '0.4 is greater',
        '0.45 is greater',
        'They are equal',
        'Cannot tell',
      ],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a measuring scale 📏 with marks at every hundredth.',
        ),
        SolutionStep(
          text:
              'Write 0.4 with the same number of decimal places as 0.45 by adding a zero: 0.40.',
        ),
        SolutionStep(
          text:
              'Now compare 0.45 and 0.40 digit by digit: the whole number parts are both 0.',
        ),
        SolutionStep(
          text:
              'Compare the tenths digit: both are 4, so move to the hundredths digit.',
        ),
        SolutionStep(
          text: 'Compare hundredths: 5 (in 0.45) is greater than 0 (in 0.40).',
        ),
        SolutionStep(text: 'So 0.45 is greater than 0.4.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Which is smaller: 0.09 or 0.9?',
      emoji: '📏',
      options: [
        '0.9 is smaller',
        'They are equal',
        'Cannot tell',
        '0.09 is smaller',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a measuring scale 📏 marked in tenths and hundredths.',
        ),
        SolutionStep(
          text:
              'Write 0.9 with the same number of decimal places as 0.09: 0.90.',
        ),
        SolutionStep(
          text: 'Compare the tenths digit: 0 (in 0.09) versus 9 (in 0.90).',
        ),
        SolutionStep(
          text: 'Since 0 is less than 9, 0.09 is the smaller number.',
        ),
        SolutionStep(
          text:
              'So 0.09 is smaller than 0.9 — do not be fooled by 09 having more digits!',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is ₹12.50 + ₹8.25?',
      emoji: '💰',
      options: ['₹20.65', '₹21.75', '₹20.75', '₹19.75'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the decimal points: 12.50 + 8.25.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Add the hundredths (paise): 0 + 5 = 5.'),
        SolutionStep(text: 'Add the tenths: 5 + 2 = 7.'),
        SolutionStep(text: 'Add the ones: 2 + 8 = 10. Write 0, carry 1.'),
        SolutionStep(text: 'Add the tens: 1 + 0 = 1, plus carried 1 = 2.'),
        SolutionStep(text: 'Combine: ₹20.75.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is ₹25.75 - ₹9.50?',
      emoji: '💰',
      options: ['₹16.25', '₹15.25', '₹16.75', '₹15.75'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the decimal points: 25.75 - 9.50.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Subtract the hundredths: 5 - 0 = 5.'),
        SolutionStep(text: 'Subtract the tenths: 7 - 5 = 2.'),
        SolutionStep(
          text:
              'Subtract the ones: 5 - 9. Cannot subtract, borrow from tens: 15 - 9 = 6.',
        ),
        SolutionStep(text: 'Subtract the tens: after lending, 1 - 0 = 1.'),
        SolutionStep(text: 'Combine: ₹16.25.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A chocolate costs ₹15.50 and a candy costs ₹4.75. What is the total cost of both?',
      emoji: '🍫',
      options: ['₹19.25', '₹20.25', '₹20.75', '₹19.75'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Total cost = cost of chocolate + cost of candy.'),
        SolutionStep(text: '15.50 + 4.75.', emoji: '📐'),
        SolutionStep(text: 'Add the hundredths: 0 + 5 = 5.'),
        SolutionStep(text: 'Add the tenths: 5 + 7 = 12. Write 2, carry 1.'),
        SolutionStep(
          text:
              'Add the ones: 5 + 4 = 9, plus carried 1 = 10. Write 0, carry 1.',
        ),
        SolutionStep(text: 'Add the tens: 1 + 0 = 1, plus carried 1 = 2.'),
        SolutionStep(text: 'The total cost is ₹20.25.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'Priya pays ₹50 for a notebook that costs ₹34.50. How much change should she get back?',
      emoji: '💵',
      options: ['₹16.50', '₹15.00', '₹15.50', '₹14.50'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Change = amount paid - cost of the item.'),
        SolutionStep(text: '50.00 - 34.50.', emoji: '📐'),
        SolutionStep(text: 'Subtract the hundredths: 0 - 0 = 0.'),
        SolutionStep(
          text:
              'Subtract the tenths: 0 - 5. Cannot subtract, borrow from ones: 10 - 5 = 5.',
        ),
        SolutionStep(
          text:
              'Subtract the ones: after lending, 9 - 4 = 5. Wait, borrow chain: ones was 0, so borrow from tens too: 9 - 4 = 5.',
        ),
        SolutionStep(text: 'Subtract the tens: after lending, 4 - 3 = 1.'),
        SolutionStep(text: 'Priya should get ₹15.50 back.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A pizza 🍕 is cut into 6 equal slices. Aman eats 1/6 and Rani eats 2/6. What fraction of the pizza have they eaten together?',
      emoji: '🍕',
      options: ['3/12', '1/6', '3/6', '2/6'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the pizza cut into 6 equal slices: 🍕🍕🍕🍕🍕🍕.',
        ),
        SolutionStep(
          text:
              'Aman ate 1 slice (1/6) and Rani ate 2 slices (2/6) from the same pizza.',
        ),
        SolutionStep(
          text:
              'Since both fractions have the same denominator (6), add the numerators: 1 + 2 = 3.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 6.'),
        SolutionStep(
          text: 'Together they ate 3/6 of the pizza, which simplifies to 1/2.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'What is 5/8 + 1/4? (Picture a pizza 🍕 cut into eighths and another cut into quarters.)',
      emoji: '🍕',
      options: ['6/12', '7/8', '6/8', '3/4'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a pizza cut into 8 equal slices, and an identical pizza cut into 4 equal slices.',
        ),
        SolutionStep(
          text:
              'The denominators (8 and 4) are different, so find a common denominator: 8 is a multiple of 4.',
        ),
        SolutionStep(
          text:
              'Convert 1/4 to eighths: multiply top and bottom by 2, giving 2/8.',
        ),
        SolutionStep(
          text:
              'Now add: 5/8 + 2/8 = 7/8 (add numerators, keep the denominator).',
        ),
        SolutionStep(text: 'So 5/8 + 1/4 = 7/8.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Convert the decimal 1.5 to a fraction in simplest form.',
      emoji: '📏',
      options: ['3/2', '1/2', '15/10', '5/1'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: '1.5 means 1 whole and 5 tenths.', emoji: '📋'),
        SolutionStep(text: 'Write 1.5 as an improper fraction over 10: 15/10.'),
        SolutionStep(
          text:
              'Simplify by dividing top and bottom by 5: 15 ÷ 5 = 3, and 10 ÷ 5 = 2.',
        ),
        SolutionStep(text: 'So 1.5 simplifies to 3/2.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Which is greater: 3/5 or 0.5?',
      emoji: '📏',
      options: [
        '3/5 is greater',
        '0.5 is greater',
        'They are equal',
        'Cannot tell',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Convert 3/5 to a decimal: divide 3 ÷ 5.',
          emoji: '📏',
        ),
        SolutionStep(
          text: 'Add a decimal point and a zero: 30 ÷ 5 = 6. So 3/5 = 0.6.',
        ),
        SolutionStep(
          text:
              'Now compare 0.6 and 0.5 digit by digit: whole numbers are both 0.',
        ),
        SolutionStep(text: 'Compare the tenths digit: 6 is greater than 5.'),
        SolutionStep(
          text: 'So 3/5 (which equals 0.6) is greater than 0.5.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A roti 🫓 is cut into 8 equal pieces. If 5/8 is eaten, what fraction of the roti is LEFT?',
      emoji: '🫓',
      options: ['2/8', '5/8', '4/8', '3/8'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the roti cut into 8 equal pieces: 🫓🫓🫓🫓🫓🫓🫓🫓.',
        ),
        SolutionStep(
          text:
              'The whole roti is 8/8. If 5/8 is eaten, what remains = 8/8 - 5/8.',
        ),
        SolutionStep(
          text:
              'Since the denominators are the same, subtract the numerators: 8 - 5 = 3.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 8.'),
        SolutionStep(text: 'So 3/8 of the roti is left.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'Arjun buys a book for ₹120.75 and a pen for ₹15.25. What is the total amount he spends?',
      emoji: '📖',
      options: ['₹135.00', '₹136.50', '₹135.50', '₹136.00'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Total amount = cost of book + cost of pen.'),
        SolutionStep(text: '120.75 + 15.25.', emoji: '📐'),
        SolutionStep(text: 'Add the hundredths: 5 + 5 = 10. Write 0, carry 1.'),
        SolutionStep(
          text:
              'Add the tenths: 7 + 2 = 9, plus carried 1 = 10. Write 0, carry 1.',
        ),
        SolutionStep(text: 'Add the ones: 0 + 5 = 5, plus carried 1 = 6.'),
        SolutionStep(text: 'Add the tens: 2 + 1 = 3.'),
        SolutionStep(text: 'Add the hundreds: 1 + 0 = 1.'),
        SolutionStep(text: 'The total amount spent is ₹136.00.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 7/10 - 3/10? (Picture a measuring jug 📏 marked in tenths.)',
      emoji: '📏',
      options: ['4/20', '4/10', '10/10', '3/10'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a jug marked with 10 equal lines, filled up to the 7th line.',
        ),
        SolutionStep(
          text:
              'Since both fractions have the same denominator (10), subtract the numerators: 7 - 3 = 4.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 10.'),
        SolutionStep(
          text: 'So 7/10 - 3/10 = 4/10, which can also be simplified to 2/5.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Which decimal is equivalent to the fraction 2/5?',
      emoji: '📏',
      options: ['0.4', '0.2', '0.25', '0.5'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'To convert 2/5 to a decimal, divide the numerator by the denominator: 2 ÷ 5.',
          emoji: '📏',
        ),
        SolutionStep(text: 'Add a decimal point and a zero: 20 ÷ 5 = 4.'),
        SolutionStep(text: 'So 2/5 = 0.4.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A tailor has 3/4 metre of cloth and uses 1/2 metre to stitch a pocket. How much cloth is left?',
      emoji: '📏',
      options: ['1/2 metre', '1/4 metre', '2/4 metre', '1/8 metre'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a measuring tape 📏 showing 3/4 metre of cloth.',
        ),
        SolutionStep(
          text:
              'The denominators (4 and 2) are different, so find a common denominator: 4 is a multiple of 2.',
        ),
        SolutionStep(
          text:
              'Convert 1/2 to quarters: multiply top and bottom by 2, giving 2/4.',
        ),
        SolutionStep(
          text:
              'Now subtract: 3/4 - 2/4 = 1/4 (subtract numerators, keep the denominator).',
        ),
        SolutionStep(text: 'So 1/4 metre of cloth is left.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is ₹100.00 - ₹67.50?',
      emoji: '💰',
      options: ['₹33.50', '₹32.00', '₹32.50', '₹42.50'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the decimal points: 100.00 - 67.50.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Subtract the hundredths: 0 - 0 = 0.'),
        SolutionStep(
          text:
              'Subtract the tenths: 0 - 5. Cannot subtract, borrow from ones: 10 - 5 = 5.',
        ),
        SolutionStep(
          text:
              'Subtract the ones: after lending, 9 (borrowed chain from tens and hundreds) - 7 = 2.',
        ),
        SolutionStep(
          text: 'Subtract the tens: after borrowing chain, 9 - 6 = 3.',
        ),
        SolutionStep(
          text: 'Subtract the hundreds: after lending 1, 0 - 0 = 0.',
        ),
        SolutionStep(text: 'The answer is ₹32.50.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 2/9 + 4/9? (Picture a chocolate bar 🍫 cut into 9 equal pieces.)',
      emoji: '🍫',
      options: ['6/18', '8/9', '6/9', '2/9'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a chocolate bar split into 9 equal pieces: 🟫🟫🟫🟫🟫🟫🟫🟫🟫.',
        ),
        SolutionStep(
          text:
              'Since both fractions have the same denominator (9), add the numerators: 2 + 4 = 6.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 9.'),
        SolutionStep(
          text: 'So 2/9 + 4/9 = 6/9, which simplifies to 2/3.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A watermelon 🍉 is cut into 10 equal slices. If 4 slices are eaten, what fraction of the watermelon is eaten?',
      emoji: '🍉',
      options: ['6/10', '4/10', '10/4', '4/6'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the watermelon cut into 10 equal slices: 🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉.',
        ),
        SolutionStep(text: 'Out of the 10 total slices, 4 are eaten.'),
        SolutionStep(
          text: 'The fraction eaten is (slices eaten) / (total slices) = 4/10.',
        ),
        SolutionStep(
          text: 'So 4/10 of the watermelon is eaten, which simplifies to 2/5.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'What is 3/5 + 1/10? (Picture a measuring jug 📏 marked in tenths and fifths.)',
      emoji: '📏',
      options: ['7/10', '4/15', '4/10', '3/50'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'The denominators are 5 and 10, and 10 is a multiple of 5, so use 10 as the common denominator.',
          emoji: '📐',
        ),
        SolutionStep(
          text:
              'Convert 3/5 to tenths: multiply top and bottom by 2, giving 6/10.',
        ),
        SolutionStep(
          text:
              'Now add: 6/10 + 1/10 = 7/10 (add numerators, keep the denominator).',
        ),
        SolutionStep(text: 'So 3/5 + 1/10 = 7/10.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'What is 5/6 - 1/3? (Picture a cake 🎂 cut into sixths and another into thirds.)',
      emoji: '🎂',
      options: ['1/2', '4/3', '4/6', '1/3'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture the cake cut into 6 equal slices (since 6 is a multiple of both 6 and 3).',
          emoji: '🍰',
        ),
        SolutionStep(
          text:
              'Convert 1/3 to sixths: multiply top and bottom by 2, giving 2/6.',
        ),
        SolutionStep(
          text:
              'Now subtract: 5/6 - 2/6 = 3/6 (subtract numerators, keep the denominator).',
        ),
        SolutionStep(
          text: 'Simplify 3/6 by dividing top and bottom by 3: 3/6 = 1/2.',
        ),
        SolutionStep(text: 'So 5/6 - 1/3 = 1/2.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Convert the fraction 7/10 to a decimal.',
      emoji: '📏',
      options: ['0.7', '0.07', '7.10', '0.17'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a measuring jug 📏 marked in tenths, filled to the 7th line.',
        ),
        SolutionStep(
          text:
              'To convert 7/10 to a decimal, divide the numerator by the denominator: 7 ÷ 10.',
        ),
        SolutionStep(
          text:
              'Dividing by 10 simply moves the decimal point one place: 7 becomes 0.7.',
        ),
        SolutionStep(text: 'So 7/10 as a decimal is 0.7.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Convert the decimal 0.05 to a fraction in simplest form.',
      emoji: '📏',
      options: ['5/100', '1/20', '5/10', '1/2'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              '0.05 means 5 hundredths, since there are 2 digits after the decimal point.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Write it as a fraction: 5/100.'),
        SolutionStep(
          text:
              'Simplify by dividing top and bottom by 5: 5 ÷ 5 = 1, and 100 ÷ 5 = 20.',
        ),
        SolutionStep(text: 'So 0.05 simplifies to 1/20.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Which is greater: 2/3 or 5/6?',
      emoji: '🍕',
      options: [
        '5/6 is greater',
        '2/3 is greater',
        'They are equal',
        'Cannot tell',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a pizza cut into 6 slices (a common denominator for thirds and sixths).',
          emoji: '🍕',
        ),
        SolutionStep(
          text:
              'Convert 2/3 to sixths: multiply top and bottom by 2, giving 4/6.',
        ),
        SolutionStep(
          text:
              'Now compare 4/6 and 5/6: since both have the same denominator, compare numerators.',
        ),
        SolutionStep(
          text: '5 is greater than 4, so 5/6 is greater than 2/3.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A jug holds 1 litre of juice. If 0.35 litres is poured into a glass, how much juice remains in the jug?',
      emoji: '🧃',
      options: ['0.55 litres', '0.75 litres', '0.45 litres', '0.65 litres'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Juice remaining = total juice - juice poured out.'),
        SolutionStep(text: '1.00 - 0.35.', emoji: '📐'),
        SolutionStep(
          text:
              'Subtract the hundredths: 0 - 5. Borrow from tenths: 10 - 5 = 5.',
        ),
        SolutionStep(text: 'Subtract the tenths: after lending, 9 - 3 = 6.'),
        SolutionStep(text: 'Subtract the ones: after lending 1, 0 - 0 = 0.'),
        SolutionStep(
          text: '0.65 litres of juice remains in the jug.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is 1/5 + 2/5 + 1/5? (Picture a chocolate bar 🍫 cut into 5 equal pieces.)',
      emoji: '🍫',
      options: ['3/15', '4/15', '4/5', '5/5'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a chocolate bar cut into 5 equal pieces: 🟫🟫🟫🟫🟫.',
        ),
        SolutionStep(
          text:
              'Since all three fractions share the same denominator (5), add the numerators: 1 + 2 + 1 = 4.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 5.'),
        SolutionStep(text: 'So 1/5 + 2/5 + 1/5 = 4/5.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A carpenter cuts a plank that is 0.9 m long into two pieces. One piece is 0.4 m. How long is the other piece?',
      emoji: '🪵',
      options: ['0.4 m', '0.6 m', '1.3 m', '0.5 m'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Length of second piece = total length - length of first piece.',
        ),
        SolutionStep(text: '0.9 - 0.4.', emoji: '📐'),
        SolutionStep(text: 'Subtract the tenths: 9 - 4 = 5.'),
        SolutionStep(text: 'The other piece is 0.5 m long.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Which is smaller: 3/8 or 1/2?',
      emoji: '🍕',
      options: [
        '1/2 is smaller',
        '3/8 is smaller',
        'They are equal',
        'Cannot tell',
      ],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Picture a pizza cut into 8 slices (a common denominator for eighths and halves).',
          emoji: '🍕',
        ),
        SolutionStep(
          text:
              'Convert 1/2 to eighths: multiply top and bottom by 4, giving 4/8.',
        ),
        SolutionStep(
          text:
              'Now compare 3/8 and 4/8: since both have the same denominator, compare numerators.',
        ),
        SolutionStep(
          text: '3 is less than 4, so 3/8 is smaller than 1/2.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A cyclist covers 4.5 km in the morning and 3.25 km in the evening. What is the total distance covered?',
      emoji: '🚴',
      options: ['7.65 km', '7.75 km', '8.75 km', '7.25 km'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total distance = morning distance + evening distance.',
        ),
        SolutionStep(text: '4.50 + 3.25.', emoji: '📐'),
        SolutionStep(text: 'Add the hundredths: 0 + 5 = 5.'),
        SolutionStep(text: 'Add the tenths: 5 + 2 = 7.'),
        SolutionStep(text: 'Add the ones: 4 + 3 = 7.'),
        SolutionStep(
          text: 'The total distance covered is 7.75 km.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 4/7 + 2/7? (Picture a dosa 🫓 cut into 7 equal pieces.)',
      emoji: '🫓',
      options: ['6/14', '8/7', '2/7', '6/7'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Picture the dosa cut into 7 equal pieces: 🫓🫓🫓🫓🫓🫓🫓.',
        ),
        SolutionStep(
          text:
              'Since both fractions have the same denominator (7), add the numerators: 4 + 2 = 6.',
        ),
        SolutionStep(text: 'Keep the denominator the same: 7.'),
        SolutionStep(text: 'So 4/7 + 2/7 = 6/7.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Convert the decimal 2.75 to a fraction in simplest form.',
      emoji: '📏',
      options: ['275/100', '7/4', '2/75', '11/4'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: '2.75 means 2 whole and 75 hundredths.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'Write 2.75 as an improper fraction over 100: 275/100.',
        ),
        SolutionStep(
          text:
              'Simplify by dividing top and bottom by 25: 275 ÷ 25 = 11, and 100 ÷ 25 = 4.',
        ),
        SolutionStep(text: 'So 2.75 simplifies to 11/4.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A recipe needs 3/4 cup of sugar, but Rina only has a 1/4 cup measuring scoop. How many scoops does she need?',
      emoji: '🥄',
      options: ['2 scoops', '4 scoops', '3 scoops', '1 scoop'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Since both amounts are measured in quarters, we can directly compare numerators.',
          emoji: '🥄',
        ),
        SolutionStep(text: 'We need 3/4 cup, and each scoop is 1/4 cup.'),
        SolutionStep(
          text:
              'Number of scoops = 3/4 ÷ 1/4 = 3 (since 3 quarters is 3 lots of 1 quarter).',
        ),
        SolutionStep(text: 'Rina needs 3 scoops.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is ₹45.60 + ₹18.90?',
      emoji: '💰',
      options: ['₹63.50', '₹64.40', '₹63.40', '₹64.50'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the decimal points: 45.60 + 18.90.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Add the hundredths: 0 + 0 = 0.'),
        SolutionStep(text: 'Add the tenths: 6 + 9 = 15. Write 5, carry 1.'),
        SolutionStep(
          text:
              'Add the ones: 5 + 8 = 13, plus carried 1 = 14. Write 4, carry 1.',
        ),
        SolutionStep(text: 'Add the tens: 4 + 1 = 5, plus carried 1 = 6.'),
        SolutionStep(text: 'The answer is ₹64.50.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What fraction of a week are 3 days?',
      emoji: '📅',
      options: ['3/5', '1/3', '3/7', '7/3'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'A week has 7 days in total.', emoji: '📋'),
        SolutionStep(
          text:
              'The fraction is (number of days considered) / (total days in a week) = 3/7.',
        ),
        SolutionStep(text: 'So 3 days is 3/7 of a week.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
  ],
);
