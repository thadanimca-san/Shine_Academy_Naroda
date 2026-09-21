import '../models/math_question.dart';

const class5PatternsGeometry = MathTopic(
  id: 'class5_patterns_geometry',
  title: 'Patterns and Geometry',
  grade: 'Class 5',
  bank: [
    MathQuestion(
      prompt: 'What is the next number in the pattern? 3, 6, 9, 12, ___',
      emoji: '🔢',
      options: ['13', '14', '15', '16'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the difference between consecutive numbers: 6 - 3 = 3, 9 - 6 = 3, 12 - 9 = 3.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'The pattern adds 3 each time.'),
        SolutionStep(text: 'Add 3 to the last number: 12 + 3 = 15.'),
        SolutionStep(text: 'The next number is 15.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is the next number in the pattern? 2, 4, 8, 16, ___',
      emoji: '🔢',
      options: ['24', '28', '32', '30'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at how each number relates to the one before it: 4 = 2 × 2, 8 = 4 × 2, 16 = 8 × 2.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'The pattern doubles the number each time.'),
        SolutionStep(text: 'Multiply the last number by 2: 16 × 2 = 32.'),
        SolutionStep(text: 'The next number is 32.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt: 'What is the next number in the pattern? 100, 90, 80, 70, ___',
      emoji: '🔢',
      options: ['50', '65', '60', '75'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the difference between consecutive numbers: 90 - 100 = -10, 80 - 90 = -10, 70 - 80 = -10.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'The pattern subtracts 10 each time.'),
        SolutionStep(text: 'Subtract 10 from the last number: 70 - 10 = 60.'),
        SolutionStep(text: 'The next number is 60.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'What is the missing number in the pattern? 5, 10, ___, 20, 25',
      emoji: '🔢',
      options: ['12', '14', '18', '15'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Look at the known differences: 10 - 5 = 5, and 20 - 10 (skipping the gap) suggests a jump of 10 across two steps.',
          emoji: '🔍',
        ),
        SolutionStep(
          text: 'Since 25 - 20 = 5 too, the pattern adds 5 each time.',
        ),
        SolutionStep(text: 'The missing number should be 10 + 5 = 15.'),
        SolutionStep(text: 'Check: 15 + 5 = 20, which matches the next term.'),
        SolutionStep(text: 'The missing number is 15.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'What is the next number in the pattern? 1, 4, 9, 16, ___ (Hint: these are square numbers.)',
      emoji: '🔢',
      options: ['20', '23', '25', '28'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Notice that each number is a number multiplied by itself: 1 = 1×1, 4 = 2×2, 9 = 3×3, 16 = 4×4.',
          emoji: '🔍',
        ),
        SolutionStep(text: 'This is the pattern of square numbers.'),
        SolutionStep(text: 'The next square number is 5 × 5.'),
        SolutionStep(text: '5 × 5 = 25.'),
        SolutionStep(text: 'The next number is 25.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'A pattern of shapes repeats as: 🔴🔵🔵🔴🔵🔵🔴🔵🔵... What shape comes 20th in this pattern?',
      emoji: '🔴',
      options: ['🔴', 'Cannot tell', 'Both equally', '🔵'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'The repeating block is 🔴🔵🔵, which has 3 shapes in each cycle.',
          emoji: '🔍',
        ),
        SolutionStep(
          text:
              'To find the 20th shape, divide 20 by 3: 20 ÷ 3 = 6, remainder 2.',
        ),
        SolutionStep(
          text:
              'A remainder of 2 means the 20th shape is the 2nd shape in the block 🔴🔵🔵.',
        ),
        SolutionStep(text: 'The 2nd shape in the block is 🔵.'),
        SolutionStep(text: 'The 20th shape in the pattern is 🔵.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'An angle measures 45°. What type of angle is this?',
      emoji: '📐',
      options: ['Acute angle', 'Right angle', 'Obtuse angle', 'Straight angle'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the angle types: acute (less than 90°), right (exactly 90°), obtuse (between 90° and 180°), straight (exactly 180°).',
          emoji: '📋',
        ),
        SolutionStep(text: 'A 45° angle is less than 90°.'),
        SolutionStep(text: 'So it is an acute angle.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt: 'An angle measures 120°. What type of angle is this?',
      emoji: '📐',
      options: ['Acute angle', 'Right angle', 'Reflex angle', 'Obtuse angle'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the angle types: acute (less than 90°), right (exactly 90°), obtuse (between 90° and 180°), reflex (more than 180°).',
          emoji: '📋',
        ),
        SolutionStep(text: 'A 120° angle is more than 90° but less than 180°.'),
        SolutionStep(text: 'So it is an obtuse angle.', emoji: '✅'),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'The corner of a square piece of paper 🟩 forms what type of angle?',
      emoji: '🟩',
      options: ['Acute angle', 'Right angle', 'Obtuse angle', 'Straight angle'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Every corner of a square is formed where two sides meet perfectly perpendicular to each other.',
          emoji: '📐',
        ),
        SolutionStep(
          text: 'A perfectly perpendicular corner measures exactly 90°.',
        ),
        SolutionStep(text: 'An angle of exactly 90° is called a right angle.'),
        SolutionStep(
          text: 'The corner of a square forms a right angle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A triangle has all three sides of equal length. What type of triangle is this?',
      emoji: '🔺',
      options: [
        'Equilateral triangle',
        'Scalene triangle',
        'Isosceles triangle',
        'Right triangle',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the types of triangles by side length: scalene (all sides different), isosceles (2 sides equal), equilateral (all 3 sides equal).',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'This triangle has all three sides of equal length.',
        ),
        SolutionStep(
          text:
              'A triangle with all sides equal is called an equilateral triangle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'A triangle has exactly two sides of equal length. What type of triangle is this?',
      emoji: '🔺',
      options: [
        'Isosceles triangle',
        'Scalene triangle',
        'Equilateral triangle',
        'None of these',
      ],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the types of triangles by side length: scalene (all sides different), isosceles (2 sides equal), equilateral (all 3 sides equal).',
          emoji: '📋',
        ),
        SolutionStep(
          text: 'This triangle has exactly 2 sides of equal length.',
        ),
        SolutionStep(
          text:
              'A triangle with exactly 2 equal sides is called an isosceles triangle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A triangle has one angle that measures exactly 90°. What type of triangle is this?',
      emoji: '🔺',
      options: [
        'Acute triangle',
        'Obtuse triangle',
        'Equilateral triangle',
        'Right triangle',
      ],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text:
              'Triangles can also be classified by their angles: acute (all angles less than 90°), right (one angle exactly 90°), obtuse (one angle more than 90°).',
          emoji: '📋',
        ),
        SolutionStep(text: 'This triangle has one angle of exactly 90°.'),
        SolutionStep(
          text: 'A triangle with a 90° angle is called a right triangle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A quadrilateral has all four sides equal and all four angles equal to 90°. What shape is this?',
      emoji: '🟦',
      options: ['Rectangle', 'Square', 'Rhombus', 'Trapezium'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'A rectangle has 4 right angles but sides are not necessarily all equal.',
          emoji: '📋',
        ),
        SolutionStep(
          text:
              'A rhombus has all 4 sides equal but angles are not necessarily 90°.',
        ),
        SolutionStep(
          text:
              'This shape has BOTH all sides equal AND all angles equal to 90°.',
        ),
        SolutionStep(
          text:
              'A quadrilateral with both these properties is called a square.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A quadrilateral has opposite sides equal and parallel, and all four angles are 90°, but not all sides are equal. What shape is this?',
      emoji: '🟨',
      options: ['Square', 'Rectangle', 'Rhombus', 'Parallelogram'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'A square needs all 4 sides equal, but here not all sides are equal, so it is not a square.',
          emoji: '📋',
        ),
        SolutionStep(
          text:
              'This shape has opposite sides equal and parallel, with all angles 90°.',
        ),
        SolutionStep(
          text: 'A quadrilateral with these properties is called a rectangle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A quadrilateral has only one pair of parallel sides. What is this shape called?',
      emoji: '🔷',
      options: ['Rectangle', 'Trapezium', 'Rhombus', 'Parallelogram'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'A parallelogram has 2 pairs of parallel sides, so that is not it.',
          emoji: '📋',
        ),
        SolutionStep(text: 'This shape has only 1 pair of parallel sides.'),
        SolutionStep(
          text:
              'A quadrilateral with exactly one pair of parallel sides is called a trapezium.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'What is the missing number in the pattern? 2, 5, 10, 17, ___ (Hint: look at the differences between terms.)',
      emoji: '🔢',
      options: ['24', '25', '26', '28'],
      correctIndex: 2,
      solutionSteps: [
        SolutionStep(
          text:
              'Find the differences between consecutive terms: 5 - 2 = 3, 10 - 5 = 5, 17 - 10 = 7.',
          emoji: '🔍',
        ),
        SolutionStep(
          text:
              'Notice the differences themselves form a pattern: 3, 5, 7 — each difference increases by 2.',
        ),
        SolutionStep(text: 'The next difference should be 7 + 2 = 9.'),
        SolutionStep(
          text: 'Add this difference to the last term: 17 + 9 = 26.',
        ),
        SolutionStep(text: 'The missing number is 26.', emoji: '✅'),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt:
          'How many degrees are there in a straight angle (a straight line)?',
      emoji: '📏',
      options: ['90°', '120°', '360°', '180°'],
      correctIndex: 3,
      solutionSteps: [
        SolutionStep(
          text: 'A straight angle looks like a straight line ➖ with no bend.',
          emoji: '📐',
        ),
        SolutionStep(text: 'A straight line always measures exactly 180°.'),
        SolutionStep(text: 'A straight angle is 180°.', emoji: '✅'),
      ],
      difficulty: Difficulty.easy,
    ),
    MathQuestion(
      prompt:
          'The three angles of a triangle always add up to how many degrees?',
      emoji: '🔺',
      options: ['180°', '90°', '270°', '360°'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text: 'This is a key geometry rule for triangles.',
          emoji: '📋',
        ),
        SolutionStep(
          text:
              'No matter the shape of the triangle, its 3 interior angles always add up to the same total.',
        ),
        SolutionStep(
          text: 'The sum of the angles in any triangle is 180°.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.medium,
    ),
    MathQuestion(
      prompt:
          'A pattern shows figures made of matchsticks: 1 triangle uses 3 matchsticks, 2 joined triangles use 5 matchsticks, 3 joined triangles use 7 matchsticks. How many matchsticks for 5 joined triangles?',
      emoji: '🔺',
      options: ['11', '9', '10', '13'],
      correctIndex: 0,
      solutionSteps: [
        SolutionStep(
          text:
              'List the pattern: 1 triangle → 3, 2 triangles → 5, 3 triangles → 7.',
          emoji: '🔍',
        ),
        SolutionStep(
          text:
              'Each extra triangle adds 2 more matchsticks (since the differences are 5-3=2, 7-5=2).',
        ),
        SolutionStep(
          text:
              'From 3 triangles (7 matchsticks) to 5 triangles is 2 more triangles, so add 2 × 2 = 4 matchsticks.',
        ),
        SolutionStep(text: '7 + 4 = 11.'),
        SolutionStep(
          text: '5 joined triangles use 11 matchsticks.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.hard,
    ),
    MathQuestion(
      prompt: 'An angle measures 90° exactly. What type of angle is this?',
      emoji: '📐',
      options: ['Acute angle', 'Right angle', 'Obtuse angle', 'Reflex angle'],
      correctIndex: 1,
      solutionSteps: [
        SolutionStep(
          text:
              'Recall the angle types: acute (less than 90°), right (exactly 90°), obtuse (between 90° and 180°).',
          emoji: '📋',
        ),
        SolutionStep(text: 'This angle measures exactly 90°.'),
        SolutionStep(
          text: 'An angle of exactly 90° is called a right angle.',
          emoji: '✅',
        ),
      ],
      difficulty: Difficulty.easy,
    ),
  ],
);
