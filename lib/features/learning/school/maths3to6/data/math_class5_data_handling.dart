import '../models/math_question.dart';

const class5DataHandling = MathTopic(
  id: 'class5_data_handling',
  title: 'Data Handling',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt:
          'A fruit stall recorded apples sold each day: Monday: 🍎🍎🍎🍎 (4), Tuesday: 🍎🍎 (2), Wednesday: 🍎🍎🍎 (3), Thursday: 🍎🍎🍎🍎🍎 (5). How many apples were sold on Thursday?',
      emoji: '🍎',
      options: ['2', '5', '3', '4'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'Look at the row for Thursday in the data: 🍎🍎🍎🍎🍎 (5).',
          emoji: '🔍',
        ),
        SolutionStep(
          text:
              'Count the apple symbols for Thursday: there are 5 apples shown.',
        ),
        SolutionStep(text: '5 apples were sold on Thursday.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A fruit stall recorded apples sold each day: Monday: 🍎🍎🍎🍎 (4), Tuesday: 🍎🍎 (2), Wednesday: 🍎🍎🍎 (3), Thursday: 🍎🍎🍎🍎🍎 (5). How many apples were sold in total over these 4 days?',
      emoji: '🍎',
      options: ['12', '13', '14', '15'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'List the apples sold each day: Monday 4, Tuesday 2, Wednesday 3, Thursday 5.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 4 + 2 + 3 + 5.'),
        SolutionStep(text: '4 + 2 = 6, then 6 + 3 = 9, then 9 + 5 = 14.'),
        SolutionStep(
          text: 'A total of 14 apples were sold over the 4 days.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A class recorded favourite fruits: Mango 🥭🥭🥭🥭🥭🥭 (6), Banana 🍌🍌🍌🍌 (4), Apple 🍎🍎🍎🍎🍎 (5), Grapes 🍇🍇🍇 (3). Which fruit is the LEAST favourite?',
      emoji: '🍇',
      options: ['Mango', 'Banana', 'Grapes', 'Apple'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'List the votes for each fruit: Mango 6, Banana 4, Apple 5, Grapes 3.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'Compare all four numbers to find the smallest: 6, 4, 5, 3.',
        ),
        SolutionStep(
          text: 'The smallest number is 3, which belongs to Grapes.',
        ),
        SolutionStep(text: 'Grapes is the least favourite fruit.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A class recorded favourite fruits: Mango 🥭🥭🥭🥭🥭🥭 (6), Banana 🍌🍌🍌🍌 (4), Apple 🍎🍎🍎🍎🍎 (5), Grapes 🍇🍇🍇 (3). How many students voted in total?',
      emoji: '🥭',
      options: ['16', '17', '18', '19'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'List the votes for each fruit: Mango 6, Banana 4, Apple 5, Grapes 3.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 6 + 4 + 5 + 3.'),
        SolutionStep(text: '6 + 4 = 10, then 10 + 5 = 15, then 15 + 3 = 18.'),
        SolutionStep(text: '18 students voted in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'Runs scored by a batsman in 5 matches: 20, 35, 40, 15, 40. What is the mean (average) score?',
      emoji: '🏏',
      options: ['28', '30', '32', '34'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'To find the mean, add all the values and divide by how many values there are.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add the runs: 20 + 35 + 40 + 15 + 40.'),
        SolutionStep(
          text:
              '20 + 35 = 55, then 55 + 40 = 95, then 95 + 15 = 110, then 110 + 40 = 150.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of matches: 150 ÷ 5 = 30.',
        ),
        SolutionStep(text: 'The mean score is 30 runs.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The heights (in cm) of 4 plants are: 12, 18, 22, 8. What is the mean height?',
      emoji: '🌱',
      options: ['13 cm', '14 cm', '16 cm', '15 cm'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'To find the mean, add all the heights and divide by the number of plants.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add the heights: 12 + 18 + 22 + 8.'),
        SolutionStep(
          text: '12 + 18 = 30, then 30 + 22 = 52, then 52 + 8 = 60.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of plants: 60 ÷ 4 = 15.',
        ),
        SolutionStep(text: 'The mean height is 15 cm.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A shop recorded umbrellas sold each day of a rainy week: Mon: ☔☔ (2), Tue: ☔☔☔☔ (4), Wed: ☔☔☔ (3), Thu: ☔☔☔☔☔ (5), Fri: ☔ (1). On which day were the MOST umbrellas sold?',
      emoji: '☔',
      options: ['Thursday', 'Monday', 'Tuesday', 'Wednesday'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'List the umbrellas sold each day: Mon 2, Tue 4, Wed 3, Thu 5, Fri 1.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'Compare all the numbers to find the largest: 2, 4, 3, 5, 1.',
        ),
        SolutionStep(
          text: 'The largest number is 5, which belongs to Thursday.',
        ),
        SolutionStep(
          text: 'The most umbrellas were sold on Thursday.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A shop recorded umbrellas sold each day of a rainy week: Mon: ☔☔ (2), Tue: ☔☔☔☔ (4), Wed: ☔☔☔ (3), Thu: ☔☔☔☔☔ (5), Fri: ☔ (1). What is the mean number of umbrellas sold per day?',
      emoji: '☔',
      options: ['2', '4', '5', '3'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'List the umbrellas sold each day: Mon 2, Tue 4, Wed 3, Thu 5, Fri 1.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 2 + 4 + 3 + 5 + 1.'),
        SolutionStep(
          text: '2 + 4 = 6, then 6 + 3 = 9, then 9 + 5 = 14, then 14 + 1 = 15.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of days: 15 ÷ 5 = 3.',
        ),
        SolutionStep(
          text: 'The mean number of umbrellas sold per day is 3.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A table shows marks scored by 5 students in a maths test: Aman: 18, Bina: 20, Chetan: 15, Deepa: 17, Esha: 20. How many students scored 20 marks?',
      emoji: '📊',
      options: ['1', '2', '3', '4'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'List the marks: Aman 18, Bina 20, Chetan 15, Deepa 17, Esha 20.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Look for students whose mark is exactly 20.'),
        SolutionStep(
          text: 'Bina scored 20, and Esha scored 20 — that is 2 students.',
        ),
        SolutionStep(text: '2 students scored 20 marks.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A table shows marks scored by 5 students in a maths test: Aman: 18, Bina: 20, Chetan: 15, Deepa: 17, Esha: 20. What is the mean mark of the class?',
      emoji: '📊',
      options: ['18', '16', '17', '19'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'List the marks: 18, 20, 15, 17, 20.', emoji: '📋'),
        SolutionStep(text: 'Add them all together: 18 + 20 + 15 + 17 + 20.'),
        SolutionStep(
          text:
              '18 + 20 = 38, then 38 + 15 = 53, then 53 + 17 = 70, then 70 + 20 = 90.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of students: 90 ÷ 5 = 18.',
        ),
        SolutionStep(text: 'The mean mark is 18.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A pet shop recorded animals sold in a month: Dogs 🐶🐶🐶 (3), Cats 🐱🐱🐱🐱🐱 (5), Birds 🐦🐦 (2), Fish 🐠🐠🐠🐠 (4). How many more cats were sold than birds?',
      emoji: '🐱',
      options: ['3', '2', '4', '5'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'Look at the values: Cats 5, Birds 2.', emoji: '🔍'),
        SolutionStep(text: 'Difference = cats sold - birds sold.'),
        SolutionStep(text: '5 - 2 = 3.'),
        SolutionStep(text: '3 more cats were sold than birds.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A pet shop recorded animals sold in a month: Dogs 🐶🐶🐶 (3), Cats 🐱🐱🐱🐱🐱 (5), Birds 🐦🐦 (2), Fish 🐠🐠🐠🐠 (4). How many animals were sold in total?',
      emoji: '🐠',
      options: ['12', '14', '13', '15'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'List the animals sold: Dogs 3, Cats 5, Birds 2, Fish 4.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 3 + 5 + 2 + 4.'),
        SolutionStep(text: '3 + 5 = 8, then 8 + 2 = 10, then 10 + 4 = 14.'),
        SolutionStep(text: '14 animals were sold in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The weights (in kg) of 5 sacks of rice are: 20, 25, 30, 20, 30. What is the mean weight?',
      emoji: '🌾',
      options: ['23 kg', '24 kg', '26 kg', '25 kg'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'To find the mean, add all the weights and divide by the number of sacks.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add the weights: 20 + 25 + 30 + 20 + 30.'),
        SolutionStep(
          text:
              '20 + 25 = 45, then 45 + 30 = 75, then 75 + 20 = 95, then 95 + 30 = 125.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of sacks: 125 ÷ 5 = 25.',
        ),
        SolutionStep(text: 'The mean weight is 25 kg.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A table shows books read by 4 students in a month: Priya: 6, Raj: 4, Sonia: 8, Tarun: 6. What is the mean number of books read?',
      emoji: '📚',
      options: ['6', '5', '5.5', '6.5'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'List the books read: 6, 4, 8, 6.', emoji: '📋'),
        SolutionStep(text: 'Add them all together: 6 + 4 + 8 + 6.'),
        SolutionStep(text: '6 + 4 = 10, then 10 + 8 = 18, then 18 + 6 = 24.'),
        SolutionStep(
          text: 'Divide the total by the number of students: 24 ÷ 4 = 6.',
        ),
        SolutionStep(text: 'The mean number of books read is 6.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A weather record shows rainy days each month: Jan 🌧️🌧️ (2), Feb 🌧️🌧️🌧️ (3), Mar 🌧️🌧️🌧️🌧️🌧️ (5), Apr 🌧️🌧️🌧️🌧️ (4). Which month had the FEWEST rainy days?',
      emoji: '🌧️',
      options: ['February', 'January', 'March', 'April'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'List the rainy days: Jan 2, Feb 3, Mar 5, Apr 4.',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'Compare all the numbers to find the smallest: 2, 3, 5, 4.',
        ),
        SolutionStep(
          text: 'The smallest number is 2, which belongs to January.',
        ),
        SolutionStep(text: 'January had the fewest rainy days.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A weather record shows rainy days each month: Jan 🌧️🌧️ (2), Feb 🌧️🌧️🌧️ (3), Mar 🌧️🌧️🌧️🌧️🌧️ (5), Apr 🌧️🌧️🌧️🌧️ (4). What is the mean number of rainy days per month?',
      emoji: '🌧️',
      options: ['3', '3.5', '4', '4.5'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(text: 'List the rainy days: 2, 3, 5, 4.', emoji: '📋'),
        SolutionStep(text: 'Add them all together: 2 + 3 + 5 + 4.'),
        SolutionStep(text: '2 + 3 = 5, then 5 + 5 = 10, then 10 + 4 = 14.'),
        SolutionStep(
          text: 'Divide the total by the number of months: 14 ÷ 4 = 3.5.',
        ),
        SolutionStep(
          text: 'The mean number of rainy days per month is 3.5.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A survey of favourite sports in a class: Cricket 🏏🏏🏏🏏🏏🏏🏏🏏 (8), Football ⚽⚽⚽⚽⚽ (5), Badminton 🏸🏸🏸 (3). How many students were surveyed in total?',
      emoji: '🏏',
      options: ['14', '15', '16', '17'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text: 'List the votes: Cricket 8, Football 5, Badminton 3.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 8 + 5 + 3.'),
        SolutionStep(text: '8 + 5 = 13, then 13 + 3 = 16.'),
        SolutionStep(text: '16 students were surveyed in total.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A survey of favourite sports in a class: Cricket 🏏🏏🏏🏏🏏🏏🏏🏏 (8), Football ⚽⚽⚽⚽⚽ (5), Badminton 🏸🏸🏸 (3). How many more students chose cricket than badminton?',
      emoji: '⚽',
      options: ['3', '4', '6', '5'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'Look at the values: Cricket 8, Badminton 3.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'Difference = cricket votes - badminton votes.'),
        SolutionStep(text: '8 - 3 = 5.'),
        SolutionStep(
          text: '5 more students chose cricket than badminton.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'The number of trees planted by 5 classes: Class A: 10, Class B: 15, Class C: 10, Class D: 20, Class E: 15. What is the mean number of trees planted per class?',
      emoji: '🌳',
      options: ['13', '14', '16', '15'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'List the trees planted: 10, 15, 10, 20, 15.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 10 + 15 + 10 + 20 + 15.'),
        SolutionStep(
          text:
              '10 + 15 = 25, then 25 + 10 = 35, then 35 + 20 = 55, then 55 + 15 = 70.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of classes: 70 ÷ 5 = 14.',
        ),
        SolutionStep(
          text: 'The mean number of trees planted per class is 14.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A table shows the number of goals scored by a team in 4 matches: 2, 0, 3, 3. What is the mean number of goals per match?',
      emoji: '⚽',
      options: ['2', '1.5', '2.5', '3'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(text: 'List the goals scored: 2, 0, 3, 3.', emoji: '📋'),
        SolutionStep(text: 'Add them all together: 2 + 0 + 3 + 3.'),
        SolutionStep(text: '2 + 0 = 2, then 2 + 3 = 5, then 5 + 3 = 8.'),
        SolutionStep(
          text: 'Divide the total by the number of matches: 8 ÷ 4 = 2.',
        ),
        SolutionStep(
          text: 'The mean number of goals per match is 2.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A table shows visitors to a school library each day: Mon: 12, Tue: 18, Wed: 15, Thu: 9, Fri: 21. On which day did the library have the FEWEST visitors?',
      emoji: '📚',
      options: ['Thursday', 'Monday', 'Wednesday', 'Friday'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'List the visitors each day: Mon 12, Tue 18, Wed 15, Thu 9, Fri 21.',
          emoji: '📋',
        ),
        SolutionStep(
          text:
              'Compare all the numbers to find the smallest: 12, 18, 15, 9, 21.',
        ),
        SolutionStep(
          text: 'The smallest number is 9, which belongs to Thursday.',
        ),
        SolutionStep(text: 'Thursday had the fewest visitors.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A table shows visitors to a school library each day: Mon: 12, Tue: 18, Wed: 15, Thu: 9, Fri: 21. What is the mean number of visitors per day?',
      emoji: '📚',
      options: ['13', '15', '14', '16'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text: 'List the visitors: 12, 18, 15, 9, 21.',
          emoji: '📋',
        ),
        SolutionStep(text: 'Add them all together: 12 + 18 + 15 + 9 + 21.'),
        SolutionStep(
          text:
              '12 + 18 = 30, then 30 + 15 = 45, then 45 + 9 = 54, then 54 + 21 = 75.',
        ),
        SolutionStep(
          text: 'Divide the total by the number of days: 75 ÷ 5 = 15.',
        ),
        SolutionStep(
          text: 'The mean number of visitors per day is 15.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
  ],
);
