import '../models/math_question.dart';

const class5TimeMoney = MathTopic(
  id: 'class5_time_money',
  title: 'Time and Money',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt:
          'A train leaves at 9:15 am and arrives at 11:40 am. How long is the journey?',
      emoji: '🚆',
      options: [
        '2 hours 15 minutes',
        '2 hours 35 minutes',
        '2 hours 25 minutes',
        '1 hour 55 minutes',
      ],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕘 at 9:15 am, the start time.'),
        SolutionStep(text: 'From 9:15 am to 11:15 am is exactly 2 hours.'),
        SolutionStep(text: 'From 11:15 am to 11:40 am is 25 more minutes.'),
        SolutionStep(text: 'Add the two parts together: 2 hours + 25 minutes.'),
        SolutionStep(text: 'The journey takes 2 hours 25 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A movie starts at 4:30 pm and ends at 6:50 pm. How long does the movie last?',
      emoji: '🎬',
      options: [
        '2 hours',
        '2 hours 10 minutes',
        '2 hours 20 minutes',
        '1 hour 20 minutes',
      ],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a clock 🕓 at 4:30 pm, the start time.',
          emoji: '🕓',
        ),
        SolutionStep(text: 'From 4:30 pm to 6:30 pm is exactly 2 hours.'),
        SolutionStep(text: 'From 6:30 pm to 6:50 pm is 20 more minutes.'),
        SolutionStep(text: 'Add the two parts together: 2 hours + 20 minutes.'),
        SolutionStep(text: 'The movie lasts 2 hours 20 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A school assembly begins at 7:45 am and ends at 8:10 am. How long did the assembly last?',
      emoji: '🏫',
      options: ['15 minutes', '25 minutes', '35 minutes', '45 minutes'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕢 at 7:45 am, the start time.'),
        SolutionStep(
          text:
              'From 7:45 am to 8:00 am is 15 minutes (since 45 + 15 = 60, one full hour mark).',
        ),
        SolutionStep(text: 'From 8:00 am to 8:10 am is 10 more minutes.'),
        SolutionStep(
          text:
              'Add the two parts together: 15 minutes + 10 minutes = 25 minutes.',
        ),
        SolutionStep(text: 'The assembly lasted 25 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A bus leaves the depot at 6:50 am and reaches the school at 7:35 am. How long is the bus ride?',
      emoji: '🚌',
      options: ['35 minutes', '55 minutes', '45 minutes', '25 minutes'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕡 at 6:50 am, the start time.'),
        SolutionStep(
          text: 'From 6:50 am to 7:00 am is 10 minutes (since 50 + 10 = 60).',
        ),
        SolutionStep(text: 'From 7:00 am to 7:35 am is 35 more minutes.'),
        SolutionStep(
          text:
              'Add the two parts together: 10 minutes + 35 minutes = 45 minutes.',
        ),
        SolutionStep(text: 'The bus ride is 45 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A cricket match starts at 2:00 pm and finishes at 5:30 pm. How long did the match last?',
      emoji: '🏏',
      options: [
        '3 hours 30 minutes',
        '3 hours',
        '2 hours 30 minutes',
        '4 hours',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕑 at 2:00 pm, the start time.'),
        SolutionStep(text: 'From 2:00 pm to 5:00 pm is exactly 3 hours.'),
        SolutionStep(text: 'From 5:00 pm to 5:30 pm is 30 more minutes.'),
        SolutionStep(text: 'Add the two parts together: 3 hours + 30 minutes.'),
        SolutionStep(text: 'The match lasted 3 hours 30 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A flight departs at 10:20 am and lands at 1:05 pm. How long is the flight?',
      emoji: '✈️',
      options: [
        '2 hours 45 minutes',
        '2 hours 35 minutes',
        '3 hours 15 minutes',
        '2 hours 25 minutes',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕥 at 10:20 am, the start time.'),
        SolutionStep(
          text:
              'From 10:20 am to 1:20 pm is exactly 3 hours (10 to 11 to 12 to 1).',
        ),
        SolutionStep(
          text:
              'But the flight lands at 1:05 pm, which is 15 minutes before 1:20 pm.',
        ),
        SolutionStep(
          text:
              'So subtract those 15 minutes from 3 hours: 3 hours - 15 minutes = 2 hours 45 minutes.',
        ),
        SolutionStep(
          text: 'The flight duration is 2 hours 45 minutes.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'Convert 150 minutes into hours and minutes.',
      emoji: '⏱️',
      options: [
        '2 hours 30 minutes',
        '2 hours 20 minutes',
        '1 hour 50 minutes',
        '3 hours 10 minutes',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'We know 60 minutes = 1 hour.', emoji: '📋'),
        SolutionStep(
          text:
              'Divide 150 by 60 to find the whole hours: 150 ÷ 60 = 2, remainder 30 (60 × 2 = 120, 150 - 120 = 30).',
        ),
        SolutionStep(
          text:
              'The quotient (2) is the number of hours, and the remainder (30) is the leftover minutes.',
        ),
        SolutionStep(text: '150 minutes = 2 hours 30 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Convert 3 hours 45 minutes into minutes.',
      emoji: '⏱️',
      options: ['180 minutes', '225 minutes', '215 minutes', '205 minutes'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'We know 1 hour = 60 minutes.', emoji: '📋'),
        SolutionStep(
          text: 'Convert the 3 hours to minutes: 3 × 60 = 180 minutes.',
        ),
        SolutionStep(text: 'Add the extra 45 minutes: 180 + 45 = 225.'),
        SolutionStep(text: '3 hours 45 minutes = 225 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'Convert 2 hours into minutes.',
      emoji: '⏱️',
      options: ['120 minutes', '100 minutes', '110 minutes', '200 minutes'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'We know 1 hour = 60 minutes.', emoji: '📋'),
        SolutionStep(text: 'Multiply: 2 × 60 = 120.'),
        SolutionStep(text: '2 hours = 120 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Convert 90 minutes into hours and minutes.',
      emoji: '⏱️',
      options: [
        '1 hour 20 minutes',
        '1 hour 40 minutes',
        '2 hours',
        '1 hour 30 minutes',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'We know 60 minutes = 1 hour.', emoji: '📋'),
        SolutionStep(
          text:
              'Divide 90 by 60: 90 ÷ 60 = 1, remainder 30 (60 × 1 = 60, 90 - 60 = 30).',
        ),
        SolutionStep(
          text:
              'The quotient (1) is the number of hours, and the remainder (30) is the leftover minutes.',
        ),
        SolutionStep(text: '90 minutes = 1 hour 30 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'Ravi buys a kite for ₹35 and a ball for ₹28. If he pays with a ₹100 note, how much change does he get?',
      emoji: '🪁',
      options: ['₹35', '₹47', '₹63', '₹37'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'First find the total cost: kite + ball = 35 + 28.',
          emoji: '💰',
        ),
        SolutionStep(text: 'Add the ones: 5 + 8 = 13. Write 3, carry 1.'),
        SolutionStep(text: 'Add the tens: 3 + 2 = 5, plus carried 1 = 6.'),
        SolutionStep(text: 'Total cost = 63.'),
        SolutionStep(text: 'Change = amount paid - total cost = 100 - 63.'),
        SolutionStep(text: 'Subtract: 100 - 63 = 37.'),
        SolutionStep(text: 'Ravi gets ₹37 change.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A shopkeeper sells 3 notebooks at ₹22 each. If a customer pays with a ₹100 note, how much change should they get?',
      emoji: '📓',
      options: ['₹44', '₹56', '₹34', '₹66'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'First find the total cost of 3 notebooks: 22 × 3.',
          emoji: '💰',
        ),
        SolutionStep(text: 'Multiply: 22 × 3 = 66.'),
        SolutionStep(text: 'Change = amount paid - total cost = 100 - 66.'),
        SolutionStep(
          text:
              'Subtract: ones: 0 - 6, borrow from tens: 10 - 6 = 4. Tens: after lending, 9 - 6 = 3.',
        ),
        SolutionStep(text: 'So 100 - 66 = 34.'),
        SolutionStep(text: 'The customer should get ₹34 change.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Sonal has ₹250. She spends ₹85 on a book and ₹60 on a pencil box. How much money does she have left?',
      emoji: '💵',
      options: ['₹95', '₹115', '₹105', '₹125'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'First find the total amount spent: 85 + 60.',
          emoji: '💰',
        ),
        SolutionStep(text: 'Add: 85 + 60 = 145.'),
        SolutionStep(
          text: 'Money left = money she had - money spent = 250 - 145.',
        ),
        SolutionStep(
          text: 'Subtract the ones: 0 - 5. Borrow from tens: 10 - 5 = 5.',
        ),
        SolutionStep(text: 'Subtract the tens: after lending, 4 - 4 = 0.'),
        SolutionStep(text: 'Subtract the hundreds: 2 - 1 = 1.'),
        SolutionStep(text: 'Sonal has ₹105 left.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A school fair sells samosas at ₹12 each. How much would 8 samosas cost?',
      emoji: '🥟',
      options: ['₹86', '₹96', '₹106', '₹84'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total cost = cost per samosa × number of samosas.',
          emoji: '💰',
        ),
        SolutionStep(text: '12 × 8.'),
        SolutionStep(
          text: 'Break 12 into 10 + 2: 10 × 8 = 80, and 2 × 8 = 16.',
        ),
        SolutionStep(text: 'Add the partial products: 80 + 16 = 96.'),
        SolutionStep(text: '8 samosas cost ₹96.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'Kavita buys 5 bangles at ₹15 each and pays with a ₹100 note. How much change will she receive?',
      emoji: '💍',
      options: ['₹15', '₹25', '₹20', '₹35'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'First find the total cost: 15 × 5.', emoji: '💰'),
        SolutionStep(text: 'Multiply: 15 × 5 = 75.'),
        SolutionStep(text: 'Change = amount paid - total cost = 100 - 75.'),
        SolutionStep(
          text: 'Subtract the ones: 0 - 5. Borrow from tens: 10 - 5 = 5.',
        ),
        SolutionStep(text: 'Subtract the tens: after lending, 9 - 7 = 2.'),
        SolutionStep(text: 'So 100 - 75 = 25.'),
        SolutionStep(text: 'Kavita will receive ₹25 change.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A movie show starts at 6:00 pm and the film runs for 2 hours 15 minutes. At what time does the movie end?',
      emoji: '🎬',
      options: ['8:00 pm', '8:30 pm', '8:15 pm', '7:45 pm'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕕 starting at 6:00 pm.'),
        SolutionStep(text: 'Add the hours first: 6:00 pm + 2 hours = 8:00 pm.'),
        SolutionStep(
          text:
              'Now add the remaining 15 minutes: 8:00 pm + 15 minutes = 8:15 pm.',
        ),
        SolutionStep(text: 'The movie ends at 8:15 pm.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A train journey that started at 5:40 am took 3 hours 25 minutes. At what time did the train arrive?',
      emoji: '🚆',
      options: ['8:05 am', '9:15 am', '8:15 am', '9:05 am'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕠 starting at 5:40 am.'),
        SolutionStep(text: 'Add the hours first: 5:40 am + 3 hours = 8:40 am.'),
        SolutionStep(
          text: 'Now add the remaining 25 minutes: 8:40 am + 25 minutes.',
        ),
        SolutionStep(
          text:
              'From 8:40 to 9:00 is 20 minutes, using up 20 of the 25 minutes, leaving 5 minutes.',
        ),
        SolutionStep(text: 'Add the remaining 5 minutes to 9:00 am: 9:05 am.'),
        SolutionStep(text: 'The train arrived at 9:05 am.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A shop opens at 9:30 am and closes at 8:00 pm. How long is the shop open each day?',
      emoji: '🏪',
      options: [
        '10 hours 30 minutes',
        '9 hours 30 minutes',
        '10 hours',
        '11 hours',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕤 at 9:30 am, the opening time.'),
        SolutionStep(
          text: 'From 9:30 am to 8:30 pm would be exactly 11 hours.',
        ),
        SolutionStep(
          text:
              'But the shop closes at 8:00 pm, which is 30 minutes before 8:30 pm.',
        ),
        SolutionStep(
          text:
              'Subtract those 30 minutes: 11 hours - 30 minutes = 10 hours 30 minutes.',
        ),
        SolutionStep(
          text: 'The shop is open for 10 hours 30 minutes.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Meena buys vegetables worth ₹142.50 and fruits worth ₹67.75. What is the total amount she spends?',
      emoji: '🥕',
      options: ['₹209.25', '₹209.75', '₹210.25', '₹200.25'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total amount = cost of vegetables + cost of fruits.',
          emoji: '💰',
        ),
        SolutionStep(text: '142.50 + 67.75.'),
        SolutionStep(text: 'Add the hundredths: 0 + 5 = 5.'),
        SolutionStep(text: 'Add the tenths: 5 + 7 = 12. Write 2, carry 1.'),
        SolutionStep(
          text:
              'Add the ones: 2 + 7 = 9, plus carried 1 = 10. Write 0, carry 1.',
        ),
        SolutionStep(
          text:
              'Add the tens: 4 + 6 = 10, plus carried 1 = 11. Write 1, carry 1.',
        ),
        SolutionStep(text: 'Add the hundreds: 1 + 0 = 1, plus carried 1 = 2.'),
        SolutionStep(text: 'The total amount spent is ₹209.75.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A shopkeeper gives ₹500 to a customer who returns ₹123.25 as change owed back. How much did the customer actually keep from the ₹500?',
      emoji: '💵',
      options: ['₹376.75', '₹377.75', '₹376.25', '₹386.75'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'Amount kept = total given - change returned.',
          emoji: '💰',
        ),
        SolutionStep(text: '500.00 - 123.25.'),
        SolutionStep(
          text:
              'Subtract the hundredths: 0 - 5. Borrow from tenths: 10 - 5 = 5.',
        ),
        SolutionStep(text: 'Subtract the tenths: after lending, 9 - 2 = 7.'),
        SolutionStep(
          text: 'Subtract the ones: 9 (after borrow chain) - 3 = 6.',
        ),
        SolutionStep(
          text: 'Subtract the tens: 9 (after borrow chain) - 2 = 7.',
        ),
        SolutionStep(
          text: 'Subtract the hundreds: after lending 1, 4 - 1 = 3.',
        ),
        SolutionStep(text: 'The customer kept ₹376.75.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A stopwatch shows a runner finished a race in 1 hour 5 minutes. Another runner finished 20 minutes earlier. What was the second runner\'s time?',
      emoji: '🏃',
      options: ['45 minutes', '55 minutes', '35 minutes', '1 hour 25 minutes'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'First convert 1 hour 5 minutes into minutes: 1 hour = 60 minutes, plus 5 minutes = 65 minutes.',
          emoji: '⏱️',
        ),
        SolutionStep(
          text:
              'The second runner finished 20 minutes earlier, so subtract: 65 - 20.',
        ),
        SolutionStep(text: '65 - 20 = 45.'),
        SolutionStep(
          text: 'The second runner\'s time was 45 minutes.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A school event begins at 11:50 am and lasts for 1 hour 30 minutes. At what time does it end?',
      emoji: '🎉',
      options: ['1:20 pm', '12:50 pm', '1:00 pm', '12:20 pm'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕚 starting at 11:50 am.'),
        SolutionStep(text: 'Add the hour first: 11:50 am + 1 hour = 12:50 pm.'),
        SolutionStep(
          text: 'Now add the remaining 30 minutes: 12:50 pm + 30 minutes.',
        ),
        SolutionStep(
          text:
              'From 12:50 to 1:00 pm uses 10 of the 30 minutes, leaving 20 minutes.',
        ),
        SolutionStep(text: 'Add the remaining 20 minutes to 1:00 pm: 1:20 pm.'),
        SolutionStep(text: 'The event ends at 1:20 pm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Amit has three ₹100 notes, two ₹50 notes, and one ₹20 note. How much money does he have in total?',
      emoji: '💴',
      options: ['₹380', '₹420', '₹400', '₹450'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Find the value of the ₹100 notes: 3 × 100 = 300.',
          emoji: '💰',
        ),
        SolutionStep(text: 'Find the value of the ₹50 notes: 2 × 50 = 100.'),
        SolutionStep(text: 'The ₹20 note is worth 20.'),
        SolutionStep(text: 'Add all the amounts: 300 + 100 + 20.'),
        SolutionStep(text: '300 + 100 = 400, then 400 + 20 = 420.'),
        SolutionStep(text: 'Amit has ₹420 in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A library is open from 10:00 am to 5:30 pm. If it closes for a 45-minute lunch break, how many hours and minutes is it actually open?',
      emoji: '📚',
      options: [
        '6 hours',
        '6 hours 45 minutes',
        '7 hours 30 minutes',
        '6 hours 15 minutes',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'First find the total time from opening to closing: 10:00 am to 5:30 pm.',
          emoji: '🕙',
        ),
        SolutionStep(
          text:
              'From 10:00 am to 5:00 pm is 7 hours. Add the extra 30 minutes: 7 hours 30 minutes total.',
        ),
        SolutionStep(
          text:
              'Now subtract the 45-minute lunch break: 7 hours 30 minutes - 45 minutes.',
        ),
        SolutionStep(
          text:
              'Convert 30 minutes to borrow: 7 hours 30 minutes = 6 hours 90 minutes.',
        ),
        SolutionStep(
          text:
              'Subtract: 90 minutes - 45 minutes = 45 minutes, keeping 6 hours.',
        ),
        SolutionStep(
          text: 'The library is actually open for 6 hours.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A birthday party started at 4:00 pm and the last guest left at 7:20 pm. How long did the party last?',
      emoji: '🎂',
      options: [
        '3 hours',
        '2 hours 40 minutes',
        '3 hours 40 minutes',
        '3 hours 20 minutes',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕓 at 4:00 pm, the start time.'),
        SolutionStep(text: 'From 4:00 pm to 7:00 pm is exactly 3 hours.'),
        SolutionStep(text: 'From 7:00 pm to 7:20 pm is 20 more minutes.'),
        SolutionStep(text: 'Add the two parts together: 3 hours + 20 minutes.'),
        SolutionStep(text: 'The party lasted 3 hours 20 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Neha saves ₹15 every day. How much will she save in 12 days?',
      emoji: '🐷',
      options: ['₹160', '₹170', '₹180', '₹190'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Total savings = amount saved per day × number of days.',
          emoji: '💰',
        ),
        SolutionStep(text: '15 × 12.'),
        SolutionStep(
          text: 'Break 12 into 10 + 2: 15 × 10 = 150, and 15 × 2 = 30.',
        ),
        SolutionStep(text: 'Add the partial products: 150 + 30 = 180.'),
        SolutionStep(text: 'Neha will save ₹180 in 12 days.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A watch shows 11:40 am. What time will it show after 50 minutes?',
      emoji: '⌚',
      options: ['12:20 pm', '12:10 pm', '12:30 pm', '1:30 pm'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕚 at 11:40 am.'),
        SolutionStep(
          text:
              'From 11:40 am to 12:00 pm (noon) is 20 minutes, using up 20 of the 50 minutes.',
        ),
        SolutionStep(text: 'Remaining minutes to add: 50 - 20 = 30.'),
        SolutionStep(
          text: 'Add the remaining 30 minutes to 12:00 pm: 12:30 pm.',
        ),
        SolutionStep(text: 'The watch will show 12:30 pm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Rohan buys a football for ₹450 and a pair of socks for ₹85. If he has ₹600, how much money will he have left?',
      emoji: '⚽',
      options: ['₹55', '₹65', '₹75', '₹45'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'First find the total cost: football + socks = 450 + 85.',
          emoji: '💰',
        ),
        SolutionStep(text: 'Add: 450 + 85 = 535.'),
        SolutionStep(
          text: 'Money left = money he has - total cost = 600 - 535.',
        ),
        SolutionStep(
          text:
              'Subtract: ones 0 - 5, borrow from tens: 10 - 5 = 5. Tens: after lending, 9 - 3 = 6. Hundreds: 5 - 5 = 0.',
        ),
        SolutionStep(text: 'So 600 - 535 = 65.'),
        SolutionStep(text: 'Rohan will have ₹65 left.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A tuition class starts at 4:20 pm and runs for 1 hour 40 minutes. At what time does it end?',
      emoji: '📖',
      options: ['5:40 pm', '6:00 pm', '6:20 pm', '5:20 pm'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕟 starting at 4:20 pm.'),
        SolutionStep(text: 'Add the hour first: 4:20 pm + 1 hour = 5:20 pm.'),
        SolutionStep(
          text: 'Now add the remaining 40 minutes: 5:20 pm + 40 minutes.',
        ),
        SolutionStep(
          text: 'From 5:20 to 6:00 pm uses 40 of the 40 minutes exactly.',
        ),
        SolutionStep(text: 'The tuition class ends at 6:00 pm.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'A vendor sells 6 mangoes for ₹90. What is the cost of 1 mango?',
      emoji: '🥭',
      options: ['₹12', '₹18', '₹15', '₹10'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'Cost of 1 mango = total cost ÷ number of mangoes.',
          emoji: '💰',
        ),
        SolutionStep(text: '90 ÷ 6.'),
        SolutionStep(
          text:
              'Divide: 9 ÷ 6 = 1, remainder 3. Bring down 0, making 30. Divide 30 ÷ 6 = 5.',
        ),
        SolutionStep(text: 'Combine the digits: 1 and 5, giving 15.'),
        SolutionStep(text: 'Each mango costs ₹15.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A football match kicked off at 3:45 pm. Half-time was called after 45 minutes of play. What time was half-time?',
      emoji: '⚽',
      options: ['4:30 pm', '4:15 pm', '4:45 pm', '4:00 pm'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕞 at 3:45 pm, the kick-off time.'),
        SolutionStep(
          text:
              'From 3:45 pm to 4:00 pm is 15 minutes, using up 15 of the 45 minutes.',
        ),
        SolutionStep(text: 'Remaining minutes to add: 45 - 15 = 30.'),
        SolutionStep(text: 'Add the remaining 30 minutes to 4:00 pm: 4:30 pm.'),
        SolutionStep(text: 'Half-time was called at 4:30 pm.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Geeta has ₹20 notes. She has 8 of them. How much money does she have in total?',
      emoji: '💴',
      options: ['₹140', '₹160', '₹150', '₹170'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Total money = value of one note × number of notes.',
          emoji: '💰',
        ),
        SolutionStep(text: '20 × 8.'),
        SolutionStep(text: 'Multiply: 20 × 8 = 160.'),
        SolutionStep(text: 'Geeta has ₹160 in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'Convert 4 hours 10 minutes into minutes.',
      emoji: '⏱️',
      options: ['240 minutes', '260 minutes', '270 minutes', '250 minutes'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'We know 1 hour = 60 minutes.', emoji: '📋'),
        SolutionStep(
          text: 'Convert the 4 hours to minutes: 4 × 60 = 240 minutes.',
        ),
        SolutionStep(text: 'Add the extra 10 minutes: 240 + 10 = 250.'),
        SolutionStep(text: '4 hours 10 minutes = 250 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A carpenter charges ₹350 per day. How much will he earn for working 6 days?',
      emoji: '🔨',
      options: ['₹1,900', '₹2,000', '₹2,200', '₹2,100'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Total earning = charge per day × number of days.',
          emoji: '💰',
        ),
        SolutionStep(text: '350 × 6.'),
        SolutionStep(
          text: 'Break 350 into 300 + 50: 300 × 6 = 1,800, and 50 × 6 = 300.',
        ),
        SolutionStep(text: 'Add the partial products: 1,800 + 300 = 2,100.'),
        SolutionStep(text: 'The carpenter will earn ₹2,100.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A train is scheduled to depart at 5:55 am but is delayed by 25 minutes. At what time does it actually depart?',
      emoji: '🚆',
      options: ['6:10 am', '6:15 am', '6:25 am', '6:20 am'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Picture a clock 🕕 at 5:55 am, the scheduled time.',
        ),
        SolutionStep(
          text:
              'From 5:55 am to 6:00 am is 5 minutes, using up 5 of the 25 minutes delay.',
        ),
        SolutionStep(text: 'Remaining minutes to add: 25 - 5 = 20.'),
        SolutionStep(text: 'Add the remaining 20 minutes to 6:00 am: 6:20 am.'),
        SolutionStep(
          text: 'The train actually departs at 6:20 am.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'Dev has 4 fifty-rupee notes and 3 ten-rupee notes. How much money does he have?',
      emoji: '💵',
      options: ['₹200', '₹210', '₹220', '₹230'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Find the value of the fifty-rupee notes: 4 × 50 = 200.',
          emoji: '💰',
        ),
        SolutionStep(
          text: 'Find the value of the ten-rupee notes: 3 × 10 = 30.',
        ),
        SolutionStep(text: 'Add both amounts: 200 + 30 = 230.'),
        SolutionStep(text: 'Dev has ₹230 in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A school play began at 10:10 am and ended at 12:35 pm. How long did the play last?',
      emoji: '🎭',
      options: [
        '2 hours 15 minutes',
        '2 hours 35 minutes',
        '1 hour 55 minutes',
        '2 hours 25 minutes',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(text: 'Picture a clock 🕙 at 10:10 am, the start time.'),
        SolutionStep(text: 'From 10:10 am to 12:10 pm is exactly 2 hours.'),
        SolutionStep(text: 'From 12:10 pm to 12:35 pm is 25 more minutes.'),
        SolutionStep(text: 'Add the two parts together: 2 hours + 25 minutes.'),
        SolutionStep(text: 'The play lasted 2 hours 25 minutes.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
