import '../models/math_question.dart';

const class5LargeNumbers = MathTopic(
  id: 'class5_large_numbers',
  title: 'Large Number Operations',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt: 'What is 45,678 + 23,145?',
      emoji: '➕',
      options: ['68,723', '68,823', '78,823', '67,823'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the numbers by place value: 45,678 + 23,145.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Ones: 8 + 5 = 13. Write 3, carry 1.'),
        SolutionStep(
          text: 'Tens: 7 + 4 = 11, plus carried 1 = 12. Write 2, carry 1.',
        ),
        SolutionStep(text: 'Hundreds: 6 + 1 = 7, plus carried 1 = 8. Write 8.'),
        SolutionStep(text: 'Thousands: 5 + 3 = 8. Write 8.'),
        SolutionStep(text: 'Ten-thousands: 4 + 2 = 6. Write 6.'),
        SolutionStep(text: 'The answer is 68,823.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is 3,05,214 + 1,48,657?',
      emoji: '➕',
      options: ['4,53,871', '4,63,871', '4,53,781', '3,53,871'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Line up: 3,05,214 + 1,48,657 (numbers in the lakh range).',
          emoji: '📐',
        ),
        SolutionStep(text: 'Ones: 4 + 7 = 11. Write 1, carry 1.'),
        SolutionStep(text: 'Tens: 1 + 5 = 6, plus carried 1 = 7. Write 7.'),
        SolutionStep(text: 'Hundreds: 2 + 6 = 8. Write 8.'),
        SolutionStep(text: 'Thousands: 5 + 8 = 13. Write 3, carry 1.'),
        SolutionStep(
          text: 'Ten-thousands: 0 + 4 = 4, plus carried 1 = 5. Write 5.',
        ),
        SolutionStep(text: 'Lakhs: 3 + 1 = 4. Write 4.'),
        SolutionStep(text: 'The answer is 4,53,871.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 82,340 - 35,675?',
      emoji: '➖',
      options: ['46,765', '47,665', '45,665', '46,665'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Line up: 82,340 - 35,675.', emoji: '📐'),
        SolutionStep(
          text:
              'Ones: 0 - 5. Cannot subtract, so borrow from the tens: 10 - 5 = 5.',
        ),
        SolutionStep(
          text:
              'Tens: after lending, 3 becomes 2. Now 2 - 7. Cannot subtract, borrow from hundreds: 12 - 7 = 5.',
        ),
        SolutionStep(
          text:
              'Hundreds: after lending, 3 becomes 2. Now 2 - 6. Cannot subtract, borrow from thousands: 12 - 6 = 6.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 2 becomes 1. Now 1 - 5. Cannot subtract, borrow from ten-thousands: 11 - 5 = 6.',
        ),
        SolutionStep(
          text: 'Ten-thousands: after lending, 8 becomes 7. Now 7 - 3 = 4.',
        ),
        SolutionStep(text: 'The answer is 46,665.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 5,00,000 - 2,34,567?',
      emoji: '➖',
      options: ['2,66,433', '2,65,433', '2,65,533', '3,65,433'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Line up: 5,00,000 - 2,34,567.', emoji: '📐'),
        SolutionStep(
          text:
              'Since 5,00,000 has zeros everywhere except the lakhs place, we borrow all the way across.',
        ),
        SolutionStep(
          text: 'Ones: 0 - 7. Borrow chains back to make it 10 - 7 = 3.',
        ),
        SolutionStep(text: 'Tens: after borrowing, 9 - 6 = 3.'),
        SolutionStep(text: 'Hundreds: 9 - 5 = 4.'),
        SolutionStep(text: 'Thousands: 9 - 4 = 5.'),
        SolutionStep(text: 'Ten-thousands: 9 - 3 = 6.'),
        SolutionStep(
          text: 'Lakhs: after lending 1 lakh, 4 lakh remains, so 4 - 2 = 2.',
        ),
        SolutionStep(text: 'The answer is 2,65,433.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 234 × 12?',
      emoji: '✖️',
      options: ['2,708', '2,908', '2,608', '2,808'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Break 12 into 10 + 2, so 234 × 12 = 234 × 10 + 234 × 2.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 234 × 10 = 2,340.'),
        SolutionStep(text: 'Second partial product: 234 × 2 = 468.'),
        SolutionStep(text: 'Add the partial products: 2,340 + 468 = 2,808.'),
        SolutionStep(text: 'The answer is 2,808.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 356 × 24?',
      emoji: '✖️',
      options: ['8,444', '8,544', '8,644', '7,544'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Break 24 into 20 + 4, so 356 × 24 = 356 × 20 + 356 × 4.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 356 × 20 = 7,120.'),
        SolutionStep(text: 'Second partial product: 356 × 4 = 1,424.'),
        SolutionStep(text: 'Add the partial products: 7,120 + 1,424 = 8,544.'),
        SolutionStep(text: 'The answer is 8,544.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 148 × 36?',
      emoji: '✖️',
      options: ['5,328', '5,228', '5,428', '5,328'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Break 36 into 30 + 6, so 148 × 36 = 148 × 30 + 148 × 6.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 148 × 30 = 4,440.'),
        SolutionStep(text: 'Second partial product: 148 × 6 = 888.'),
        SolutionStep(text: 'Add the partial products: 4,440 + 888 = 5,328.'),
        SolutionStep(text: 'The answer is 5,328.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 675 × 18?',
      emoji: '✖️',
      options: ['12,050', '12,150', '12,250', '11,150'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Break 18 into 10 + 8, so 675 × 18 = 675 × 10 + 675 × 8.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 675 × 10 = 6,750.'),
        SolutionStep(text: 'Second partial product: 675 × 8 = 5,400.'),
        SolutionStep(text: 'Add the partial products: 6,750 + 5,400 = 12,150.'),
        SolutionStep(text: 'The answer is 12,150.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A village has a population of 45,678 people. If 12,345 more people move in, what is the new population?',
      emoji: '🏘️',
      options: ['57,023', '58,023', '58,123', '57,923'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'New population = old population + people who moved in.',
        ),
        SolutionStep(text: '45,678 + 12,345.'),
        SolutionStep(text: 'Ones: 8 + 5 = 13. Write 3, carry 1.'),
        SolutionStep(
          text: 'Tens: 7 + 4 = 11, plus carried 1 = 12. Write 2, carry 1.',
        ),
        SolutionStep(
          text: 'Hundreds: 6 + 3 = 9, plus carried 1 = 10. Write 0, carry 1.',
        ),
        SolutionStep(
          text: 'Thousands: 5 + 2 = 7, plus carried 1 = 8. Write 8.',
        ),
        SolutionStep(text: 'Ten-thousands: 4 + 1 = 5. Write 5.'),
        SolutionStep(text: 'The new population is 58,023.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The distance from Ahmedabad to Delhi is 9,34,000 metres. If a train has already covered 5,67,500 metres, how much distance is left?',
      emoji: '🚆',
      options: ['3,67,500', '3,65,500', '4,66,500', '3,66,500'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Distance left = total distance - distance covered.',
        ),
        SolutionStep(text: '9,34,000 - 5,67,500.', emoji: '📐'),
        SolutionStep(text: 'Ones and tens: 00 - 00 = 00.'),
        SolutionStep(
          text: 'Hundreds: 0 - 5. Borrow from thousands: 10 - 5 = 5.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 3 - 7. Cannot subtract, borrow from ten-thousands: 13 - 7 = 6.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: after lending, 2 - 6. Cannot subtract, borrow from lakhs: 12 - 6 = 6.',
        ),
        SolutionStep(text: 'Lakhs: after lending, 8 - 5 = 3.'),
        SolutionStep(
          text: 'The train still has 3,66,500 metres left to travel.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A school festival budget is ₹85,600. If ₹38,750 has already been spent, how much money remains?',
      emoji: '💰',
      options: ['47,850', '46,750', '45,850', '46,850'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Remaining budget = total budget - amount spent.'),
        SolutionStep(text: '85,600 - 38,750.', emoji: '📐'),
        SolutionStep(text: 'Ones: 0 - 0 = 0.'),
        SolutionStep(text: 'Tens: 0 - 5. Borrow from hundreds: 10 - 5 = 5.'),
        SolutionStep(
          text:
              'Hundreds: after lending, 5 - 7. Cannot subtract, borrow from thousands: 15 - 7 = 8.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 4 - 8. Cannot subtract, borrow from ten-thousands: 14 - 8 = 6.',
        ),
        SolutionStep(text: 'Ten-thousands: after lending, 7 - 3 = 4.'),
        SolutionStep(text: '₹46,850 remains in the budget.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A wholesaler packs 125 mangoes in each crate. How many mangoes are there in 48 crates?',
      emoji: '🥭',
      options: ['6,100', '5,900', '6,200', '6,000'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Total mangoes = mangoes per crate × number of crates.',
        ),
        SolutionStep(text: '125 × 48. Break 48 into 40 + 8.', emoji: '📐'),
        SolutionStep(text: 'First partial product: 125 × 40 = 5,000.'),
        SolutionStep(text: 'Second partial product: 125 × 8 = 1,000.'),
        SolutionStep(text: 'Add the partial products: 5,000 + 1,000 = 6,000.'),
        SolutionStep(text: 'There are 6,000 mangoes in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is the place value of 7 in the number 3,72,451?',
      emoji: '🔢',
      options: ['70,000', '7,000', '700', '7'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Write out the number with place labels: 3 (lakhs), 7 (ten-thousands), 2 (thousands), 4 (hundreds), 5 (tens), 1 (ones).',
          emoji: '📋',
        ),
        SolutionStep(text: 'The digit 7 sits in the ten-thousands place.'),
        SolutionStep(
          text: 'Place value = digit × value of its place = 7 × 10,000.',
        ),
        SolutionStep(text: 'The place value of 7 is 70,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'How is 4,08,213 read in words using the Indian place value system?',
      emoji: '📖',
      options: [
        'Four lakh eight thousand two hundred thirteen',
        'Forty lakh eight thousand two hundred thirteen',
        'Four lakh eighty thousand two hundred thirteen',
        'Four thousand eight hundred thirteen',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Group the digits using Indian place values: 4,08,213 → lakhs | thousands | hundreds,tens,ones.',
          emoji: '📋',
        ),
        SolutionStep(text: 'The lakhs group is 4, meaning four lakh.'),
        SolutionStep(
          text: 'The thousands group is 08, meaning eight thousand.',
        ),
        SolutionStep(
          text: 'The last three digits are 213, meaning two hundred thirteen.',
        ),
        SolutionStep(
          text:
              'Put it together: four lakh eight thousand two hundred thirteen.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Round 4,56,789 to the nearest thousand.',
      emoji: '🔵',
      options: ['4,56,000', '4,60,000', '4,55,000', '4,57,000'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'To round to the nearest thousand, look at the hundreds digit.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'In 4,56,789, the hundreds digit is 7.'),
        SolutionStep(
          text:
              'Since 7 is 5 or more, round the thousands digit up: 6 becomes 7.',
        ),
        SolutionStep(
          text: 'Everything after the thousands place becomes 0: 4,57,000.',
        ),
        SolutionStep(text: 'So 4,56,789 rounds to 4,57,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 1,25,000 + 2,75,000?',
      emoji: '➕',
      options: ['3,90,000', '4,10,000', '4,00,000', '3,95,000'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Line up: 1,25,000 + 2,75,000.', emoji: '📐'),
        SolutionStep(text: 'Thousands: 25,000 + 75,000 = 1,00,000.'),
        SolutionStep(text: 'This carries 1 lakh into the lakhs place.'),
        SolutionStep(text: 'Lakhs: 1 + 2 = 3, plus the carried 1 = 4.'),
        SolutionStep(text: 'The answer is 4,00,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A stadium has 3,45,600 seats. On match day, 2,89,750 seats are filled. How many seats are empty?',
      emoji: '🏟️',
      options: ['56,850', '55,850', '55,750', '54,850'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Empty seats = total seats - filled seats.'),
        SolutionStep(text: '3,45,600 - 2,89,750.', emoji: '📐'),
        SolutionStep(text: 'Ones: 0 - 0 = 0.'),
        SolutionStep(text: 'Tens: 0 - 5. Borrow from hundreds: 10 - 5 = 5.'),
        SolutionStep(
          text:
              'Hundreds: after lending, 5 - 7. Cannot subtract, borrow from thousands: 15 - 7 = 8.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 4 - 9. Cannot subtract, borrow from ten-thousands: 14 - 9 = 5.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: after lending, 3 - 8. Cannot subtract, borrow from lakhs: 13 - 8 = 5.',
        ),
        SolutionStep(text: 'Lakhs: after lending, 2 - 2 = 0.'),
        SolutionStep(text: 'There are 55,850 empty seats.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 999 × 11?',
      emoji: '✖️',
      options: ['10,889', '11,989', '10,989', '9,989'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Break 11 into 10 + 1, so 999 × 11 = 999 × 10 + 999 × 1.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 999 × 10 = 9,990.'),
        SolutionStep(text: 'Second partial product: 999 × 1 = 999.'),
        SolutionStep(text: 'Add the partial products: 9,990 + 999 = 10,989.'),
        SolutionStep(text: 'The answer is 10,989.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 2,50,000 + 1,99,999?',
      emoji: '➕',
      options: ['4,50,999', '4,49,999', '4,39,999', '4,49,899'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Line up: 2,50,000 + 1,99,999.', emoji: '📐'),
        SolutionStep(text: 'Ones: 0 + 9 = 9.'),
        SolutionStep(text: 'Tens: 0 + 9 = 9.'),
        SolutionStep(text: 'Hundreds: 0 + 9 = 9.'),
        SolutionStep(text: 'Thousands: 0 + 9 = 9.'),
        SolutionStep(text: 'Ten-thousands: 5 + 9 = 14. Write 4, carry 1.'),
        SolutionStep(text: 'Lakhs: 2 + 1 = 3, plus carried 1 = 4.'),
        SolutionStep(text: 'The answer is 4,49,999.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A company printed 2,15,000 textbooks this year, which is 45,600 more than last year. How many textbooks were printed last year?',
      emoji: '📚',
      options: ['1,70,400', '1,69,600', '1,69,400', '1,68,400'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'This year = last year + 45,600, so last year = this year - 45,600.',
        ),
        SolutionStep(text: '2,15,000 - 45,600.', emoji: '📐'),
        SolutionStep(text: 'Ones and tens: 00 - 00 = 00.'),
        SolutionStep(
          text: 'Hundreds: 0 - 6. Borrow from thousands: 10 - 6 = 4.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 4 - 5. Cannot subtract, borrow from ten-thousands: 14 - 5 = 9.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: after lending, 0 - 4. Cannot subtract, borrow from lakhs: 10 - 4 = 6.',
        ),
        SolutionStep(text: 'Lakhs: after lending, 1 - 0 = 1.'),
        SolutionStep(
          text: 'Last year, 1,69,400 textbooks were printed.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 407 × 15?',
      emoji: '✖️',
      options: ['6,015', '6,205', '6,005', '6,105'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Break 15 into 10 + 5, so 407 × 15 = 407 × 10 + 407 × 5.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 407 × 10 = 4,070.'),
        SolutionStep(text: 'Second partial product: 407 × 5 = 2,035.'),
        SolutionStep(text: 'Add the partial products: 4,070 + 2,035 = 6,105.'),
        SolutionStep(text: 'The answer is 6,105.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Which number is the greatest: 3,45,678 or 3,45,687?',
      emoji: '🔍',
      options: ['3,45,678', '3,45,687', 'They are equal', 'Cannot compare'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Compare digit by digit from the left: lakhs 3 = 3, ten-thousands 4 = 4, thousands 5 = 5, hundreds 6 = 6.',
        ),
        SolutionStep(text: 'Now compare the tens digit: 7 vs 8.'),
        SolutionStep(text: 'Since 8 is greater than 7, 3,45,687 is greater.'),
        SolutionStep(text: 'The greatest number is 3,45,687.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A cinema hall sold tickets worth ₹1,80,000 on Saturday and ₹95,500 on Sunday. What was the total ticket sale over the weekend?',
      emoji: '🎬',
      options: ['2,75,500', '2,74,500', '2,85,500', '2,65,500'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Total sale = Saturday sale + Sunday sale.'),
        SolutionStep(text: '1,80,000 + 95,500.', emoji: '📐'),
        SolutionStep(text: 'Ones and tens: 00 + 00 = 00.'),
        SolutionStep(text: 'Hundreds: 0 + 5 = 5.'),
        SolutionStep(text: 'Thousands: 0 + 5 = 5.'),
        SolutionStep(text: 'Ten-thousands: 8 + 9 = 17. Write 7, carry 1.'),
        SolutionStep(text: 'Lakhs: 1 + 0 = 1, plus carried 1 = 2.'),
        SolutionStep(text: 'The total weekend sale was ₹2,75,500.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 293 × 34?',
      emoji: '✖️',
      options: ['9,862', '10,062', '9,962', '9,762'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Break 34 into 30 + 4, so 293 × 34 = 293 × 30 + 293 × 4.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 293 × 30 = 8,790.'),
        SolutionStep(text: 'Second partial product: 293 × 4 = 1,172.'),
        SolutionStep(text: 'Add the partial products: 8,790 + 1,172 = 9,962.'),
        SolutionStep(text: 'The answer is 9,962.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Two towns have populations of 2,34,890 and 1,87,650. What is their combined population?',
      emoji: '🏙️',
      options: ['4,21,540', '4,22,540', '4,22,450', '4,12,540'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Combined population = sum of both populations.'),
        SolutionStep(text: '2,34,890 + 1,87,650.', emoji: '📐'),
        SolutionStep(text: 'Ones: 0 + 0 = 0.'),
        SolutionStep(text: 'Tens: 9 + 5 = 14. Write 4, carry 1.'),
        SolutionStep(
          text: 'Hundreds: 8 + 6 = 14, plus carried 1 = 15. Write 5, carry 1.',
        ),
        SolutionStep(
          text: 'Thousands: 4 + 7 = 11, plus carried 1 = 12. Write 2, carry 1.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: 3 + 8 = 11, plus carried 1 = 12. Write 2, carry 1.',
        ),
        SolutionStep(text: 'Lakhs: 2 + 1 = 3, plus carried 1 = 4.'),
        SolutionStep(text: 'The combined population is 4,22,540.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is the sum of the greatest 5-digit number and the smallest 5-digit number?',
      emoji: '🔢',
      options: ['99,999', '1,10,000', '1,09,999', '1,00,000'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'The greatest 5-digit number is 99,999.'),
        SolutionStep(text: 'The smallest 5-digit number is 10,000.'),
        SolutionStep(text: 'Add them: 99,999 + 10,000.', emoji: '📐'),
        SolutionStep(text: 'Ones to thousands: 9,999 + 0,000 = 9,999.'),
        SolutionStep(
          text: 'Ten-thousands: 9 + 1 = 10, so write 0 and carry 1 lakh.',
        ),
        SolutionStep(text: 'The sum is 1,09,999.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A basket has 3,25,400 apples in cold storage. If 1,18,650 apples are sold, how many apples remain?',
      emoji: '🍎',
      options: ['2,06,750', '2,06,650', '2,07,750', '1,96,750'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Apples remaining = apples in storage - apples sold.',
        ),
        SolutionStep(text: '3,25,400 - 1,18,650.', emoji: '📐'),
        SolutionStep(
          text: 'Ones and tens: 00 - 50. Borrow from hundreds: 100 - 50 = 50.',
        ),
        SolutionStep(
          text:
              'Hundreds: after lending, 3 - 6. Cannot subtract, borrow from thousands: 13 - 6 = 7.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 4 - 8. Cannot subtract, borrow from ten-thousands: 14 - 8 = 6.',
        ),
        SolutionStep(text: 'Ten-thousands: after lending, 1 - 1 = 0.'),
        SolutionStep(text: 'Lakhs: 3 - 1 = 2.'),
        SolutionStep(text: '2,06,750 apples remain.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 76,542 + 8,999?',
      emoji: '➕',
      options: ['84,541', '85,441', '85,541', '84,441'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Line up the numbers by place value: 76,542 + 8,999.',
          emoji: '📐',
        ),
        SolutionStep(text: 'Ones: 2 + 9 = 11. Write 1, carry 1.'),
        SolutionStep(
          text: 'Tens: 4 + 9 = 13, plus carried 1 = 14. Write 4, carry 1.',
        ),
        SolutionStep(
          text: 'Hundreds: 5 + 9 = 14, plus carried 1 = 15. Write 5, carry 1.',
        ),
        SolutionStep(
          text: 'Thousands: 6 + 8 = 14, plus carried 1 = 15. Write 5, carry 1.',
        ),
        SolutionStep(text: 'Ten-thousands: 7 + 0 = 7, plus carried 1 = 8.'),
        SolutionStep(text: 'The answer is 85,541.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A zoo recorded 2,45,800 visitors last year and 3,12,650 visitors this year. How many more visitors came this year?',
      emoji: '🦁',
      options: ['66,750', '67,850', '66,850', '76,850'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Extra visitors = this year visitors - last year visitors.',
        ),
        SolutionStep(text: '3,12,650 - 2,45,800.', emoji: '📐'),
        SolutionStep(text: 'Ones and tens: 50 - 00 = 50.'),
        SolutionStep(
          text:
              'Hundreds: 6 - 8. Cannot subtract, borrow from thousands: 16 - 8 = 8.',
        ),
        SolutionStep(
          text:
              'Thousands: after lending, 1 - 5. Cannot subtract, borrow from ten-thousands: 11 - 5 = 6.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: after lending, 0 - 4. Cannot subtract, borrow from lakhs: 10 - 4 = 6.',
        ),
        SolutionStep(text: 'Lakhs: after lending, 2 - 2 = 0.'),
        SolutionStep(text: '66,850 more visitors came this year.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is the place value of 5 in the number 5,67,890?',
      emoji: '🔢',
      options: ['5', '500', '5,000', '5,00,000'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Write out the number with place labels: 5 (lakhs), 6 (ten-thousands), 7 (thousands), 8 (hundreds), 9 (tens), 0 (ones).',
          emoji: '📋',
        ),
        SolutionStep(text: 'The digit 5 sits in the lakhs place.'),
        SolutionStep(
          text: 'Place value = digit × value of its place = 5 × 1,00,000.',
        ),
        SolutionStep(text: 'The place value of 5 is 5,00,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A carpenter has 456 boxes of nails, each box holding 210 nails. How many nails does he have in total?',
      emoji: '🔨',
      options: ['96,760', '94,760', '95,760', '95,660'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Total nails = nails per box × number of boxes.'),
        SolutionStep(
          text: '210 × 456. Break 456 into 400 + 50 + 6.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 210 × 400 = 84,000.'),
        SolutionStep(text: 'Second partial product: 210 × 50 = 10,500.'),
        SolutionStep(text: 'Third partial product: 210 × 6 = 1,260.'),
        SolutionStep(
          text: 'Add the partial products: 84,000 + 10,500 + 1,260 = 95,760.',
        ),
        SolutionStep(text: 'He has 95,760 nails in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Round 8,34,215 to the nearest ten thousand.',
      emoji: '🔵',
      options: ['8,30,000', '8,34,000', '8,40,000', '8,35,000'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'To round to the nearest ten thousand, look at the thousands digit.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'In 8,34,215, the thousands digit is 4.'),
        SolutionStep(
          text:
              'Since 4 is less than 5, round the ten-thousands digit down (keep it the same): 3 stays 3.',
        ),
        SolutionStep(
          text: 'Everything after the ten-thousands place becomes 0: 8,30,000.',
        ),
        SolutionStep(text: 'So 8,34,215 rounds to 8,30,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Which number is the smallest: 6,78,432, 6,78,342, or 6,78,423?',
      emoji: '🔍',
      options: ['6,78,432', '6,78,342', '6,78,423', 'They are equal'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Compare digit by digit from the left. Lakhs, ten-thousands, thousands are all 6, 7, 8 — the same in all three.',
          emoji: '🔍',
        ),
        SolutionStep(
          text:
              'Now compare the hundreds digit: 4 (in 6,78,432), 3 (in 6,78,342), 4 (in 6,78,423).',
        ),
        SolutionStep(
          text: 'The smallest hundreds digit is 3, found only in 6,78,342.',
        ),
        SolutionStep(
          text:
              'Since 6,78,342 already has the smallest hundreds digit, it must be the smallest number — no need to compare further digits.',
        ),
        SolutionStep(text: 'The smallest number is 6,78,342.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A charity collected ₹3,45,000 in January and ₹2,78,500 in February. What was the total collection over both months?',
      emoji: '🤝',
      options: ['6,23,500', '6,13,000', '6,13,500', '6,33,500'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Total collection = January amount + February amount.',
        ),
        SolutionStep(text: '3,45,000 + 2,78,500.', emoji: '📐'),
        SolutionStep(text: 'Hundreds: 0 + 5 = 5.'),
        SolutionStep(text: 'Thousands: 5 + 8 = 13. Write 3, carry 1.'),
        SolutionStep(
          text:
              'Ten-thousands: 4 + 7 = 11, plus carried 1 = 12. Write 2, carry 1.',
        ),
        SolutionStep(text: 'Lakhs: 3 + 2 = 5, plus carried 1 = 6.'),
        SolutionStep(text: 'The total collection was ₹6,13,500.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 512 × 27?',
      emoji: '✖️',
      options: ['13,724', '13,624', '14,824', '13,824'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Break 27 into 20 + 7, so 512 × 27 = 512 × 20 + 512 × 7.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 512 × 20 = 10,240.'),
        SolutionStep(text: 'Second partial product: 512 × 7 = 3,584.'),
        SolutionStep(
          text: 'Add the partial products: 10,240 + 3,584 = 13,824.',
        ),
        SolutionStep(text: 'The answer is 13,824.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A stationery shop had 4,50,000 sheets of paper. After selling some, only 2,86,750 sheets remain. How many sheets were sold?',
      emoji: '📄',
      options: ['1,63,150', '1,64,250', '1,63,250', '1,53,250'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Sheets sold = sheets before - sheets remaining.'),
        SolutionStep(text: '4,50,000 - 2,86,750.', emoji: '📐'),
        SolutionStep(
          text:
              'Since 4,50,000 has zeros in the last three places, borrow across: think of it as 4,49,999 + 1 before subtracting, so tens=9, hundreds=9, thousands=9 after borrowing, with 1 taken from ten-thousands.',
        ),
        SolutionStep(
          text: 'Ones and tens: (10)0 - 50 = 50. Hundreds: 9 - 7 = 2.',
        ),
        SolutionStep(
          text:
              'Thousands: 9 - 6 = 3. Ten-thousands: after lending 1, 4 - 8. Cannot subtract, borrow from lakhs: 14 - 8 = 6.',
        ),
        SolutionStep(text: 'Lakhs: after lending, 3 - 2 = 1.'),
        SolutionStep(
          text:
              'Check by adding back: 2,86,750 + 1,63,250 = 4,50,000. It matches!',
        ),
        SolutionStep(text: '1,63,250 sheets were sold.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is 3,15,000 + 4,85,000?',
      emoji: '➕',
      options: ['8,00,000', '7,00,000', '7,90,000', '7,10,000'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Line up: 3,15,000 + 4,85,000.', emoji: '📐'),
        SolutionStep(text: 'Thousands: 15,000 + 85,000 = 1,00,000.'),
        SolutionStep(text: 'This carries 1 lakh into the lakhs place.'),
        SolutionStep(text: 'Lakhs: 3 + 4 = 7, plus the carried 1 = 8.'),
        SolutionStep(text: 'The answer is 8,00,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'How is 7,20,045 read in words using the Indian place value system?',
      emoji: '📖',
      options: [
        'Seventy-two thousand forty-five',
        'Seven lakh two thousand forty-five',
        'Seven lakh twenty thousand four hundred five',
        'Seven lakh twenty thousand forty-five',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Group the digits using Indian place values: 7,20,045 → lakhs | thousands | hundreds,tens,ones.',
          emoji: '📋',
        ),
        SolutionStep(text: 'The lakhs group is 7, meaning seven lakh.'),
        SolutionStep(
          text: 'The thousands group is 20, meaning twenty thousand.',
        ),
        SolutionStep(
          text: 'The last three digits are 045, meaning forty-five.',
        ),
        SolutionStep(
          text: 'Put it together: seven lakh twenty thousand forty-five.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A cricket stadium sold 1,25,600 tickets for the first match and 1,45,900 for the second. How many tickets were sold in total for both matches?',
      emoji: '🏏',
      options: ['2,71,500', '2,70,500', '2,61,500', '2,71,400'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Total tickets = first match + second match.'),
        SolutionStep(text: '1,25,600 + 1,45,900.', emoji: '📐'),
        SolutionStep(text: 'Hundreds: 6 + 9 = 15. Write 5, carry 1.'),
        SolutionStep(
          text: 'Thousands: 5 + 5 = 10, plus carried 1 = 11. Write 1, carry 1.',
        ),
        SolutionStep(text: 'Ten-thousands: 2 + 4 = 6, plus carried 1 = 7.'),
        SolutionStep(text: 'Lakhs: 1 + 1 = 2.'),
        SolutionStep(
          text: 'A total of 2,71,500 tickets were sold.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is 605 × 23?',
      emoji: '✖️',
      options: ['13,915', '13,815', '13,715', '14,815'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Break 23 into 20 + 3, so 605 × 23 = 605 × 20 + 605 × 3.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 605 × 20 = 12,100.'),
        SolutionStep(text: 'Second partial product: 605 × 3 = 1,815.'),
        SolutionStep(
          text: 'Add the partial products: 12,100 + 1,815 = 13,915.',
        ),
        SolutionStep(text: 'The answer is 13,915.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A factory manufactured 67,890 toys in one month and 45,230 toys the next month. How many toys were made altogether?',
      emoji: '🧸',
      options: ['1,12,120', '1,13,020', '1,13,120', '1,03,120'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Total toys = first month + second month.'),
        SolutionStep(text: '67,890 + 45,230.', emoji: '📐'),
        SolutionStep(text: 'Ones: 0 + 0 = 0.'),
        SolutionStep(text: 'Tens: 9 + 3 = 12. Write 2, carry 1.'),
        SolutionStep(
          text: 'Hundreds: 8 + 2 = 10, plus carried 1 = 11. Write 1, carry 1.',
        ),
        SolutionStep(
          text: 'Thousands: 7 + 5 = 12, plus carried 1 = 13. Write 3, carry 1.',
        ),
        SolutionStep(
          text:
              'Ten-thousands: 6 + 4 = 10, plus carried 1 = 11. Write 1, carry 1 lakh.',
        ),
        SolutionStep(text: 'The total is 1,13,120 toys.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'What is the place value of 9 in the number 6,95,214?',
      emoji: '🔢',
      options: ['90,000', '9', '90', '900'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Write out the number with place labels: 6 (lakhs), 9 (ten-thousands), 5 (thousands), 2 (hundreds), 1 (tens), 4 (ones).',
          emoji: '📋',
        ),
        SolutionStep(text: 'The digit 9 sits in the ten-thousands place.'),
        SolutionStep(
          text: 'Place value = digit × value of its place = 9 × 10,000.',
        ),
        SolutionStep(text: 'The place value of 9 is 90,000.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A warehouse stores rice in sacks of 75 kg each. How much rice is stored in 236 sacks?',
      emoji: '🌾',
      options: ['17,600 kg', '17,700 kg', '17,800 kg', '16,700 kg'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Total rice = weight per sack × number of sacks.'),
        SolutionStep(
          text: '75 × 236. Break 236 into 200 + 30 + 6.',
          emoji: '📐',
        ),
        SolutionStep(text: 'First partial product: 75 × 200 = 15,000.'),
        SolutionStep(text: 'Second partial product: 75 × 30 = 2,250.'),
        SolutionStep(text: 'Third partial product: 75 × 6 = 450.'),
        SolutionStep(
          text: 'Add the partial products: 15,000 + 2,250 + 450 = 17,700.',
        ),
        SolutionStep(
          text: 'The warehouse stores 17,700 kg of rice.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
  ],
);
