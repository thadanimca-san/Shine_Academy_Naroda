import '../../../models/chapter_model.dart';
final ChapterModel class8IntroductionGraphsChapter = ChapterModel(
  standard: 8, subject: "Mathematics", chapterId: "cls8_math_introductiongraphs", chapterName: "Introduction to Graphs",
  concepts: ["Bar graphs, pie charts and line graphs.", "Coordinates and plotting points on a Cartesian plane.", "Linear graphs and applications."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ig1", question: "A graph that displays data as vertical or horizontal rectangular bars is called a [ bar graph / line graph ].", answer: "bar graph"),
    QuestionItem(id: "ig2", question: "A graph showing changes in data over time, using connected points, is called a [ line graph / pie chart ].", answer: "line graph"),
    QuestionItem(id: "ig3", question: "The horizontal and vertical number lines used to locate a point on a plane are called the [ x-axis and y-axis / diagonal axes ].", answer: "x-axis and y-axis"),
    QuestionItem(id: "ig4", question: "The point where the x-axis and y-axis intersect is called the [ origin / vertex ].", answer: "origin"),
    QuestionItem(id: "ig5", question: "A pair of numbers used to locate a point on a Cartesian plane is called its [ coordinates / vertices ].", answer: "coordinates"),
    QuestionItem(id: "ig6", question: "In the coordinate pair (x, y), x is called the [ x-coordinate (abscissa) / y-coordinate ].", answer: "x-coordinate (abscissa)"),
    QuestionItem(id: "ig7", question: "In the coordinate pair (x, y), y is called the [ y-coordinate (ordinate) / x-coordinate ].", answer: "y-coordinate (ordinate)"),
    QuestionItem(id: "ig8", question: "The coordinates of the origin are [ (0, 0) / (1, 1) ].", answer: "(0, 0)"),
    QuestionItem(id: "ig9", question: "A graph where the plotted points lie on a straight line is called a [ linear graph / curved graph ].", answer: "linear graph"),
    QuestionItem(id: "ig10", question: "A distance-time graph for an object moving at constant speed is a [ straight line / curve ].", answer: "straight line"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ign1", question: "Plot the point (3, 4). What is the x-coordinate?", given: ["Point = (3, 4)"], solutionSteps: ["The first number in a coordinate pair is the x-coordinate.", "x-coordinate = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "ign2", question: "A car travels at a constant 40 km/h. Using the linear graph relation distance = speed × time, find the distance covered in 3 hours.", given: ["Speed = 40 km/h", "Time = 3 h"], solutionSteps: ["Distance = speed × time", "= 40 × 3", "= 120 km"], numericAnswer: 120, unit: "km"),
    NumericalProblem(id: "ign3", question: "Find the y-coordinate of the point (-7, 9).", given: ["Point = (-7, 9)"], solutionSteps: ["The second number in a coordinate pair is the y-coordinate.", "y-coordinate = 9"], numericAnswer: 9, unit: ""),
    NumericalProblem(id: "ign4", question: "A plant grows 2 cm per week (linear growth). Find its height after 6 weeks if it started at 5 cm.", given: ["Growth rate = 2 cm/week", "Initial height = 5 cm", "Time = 6 weeks"], solutionSteps: ["Height = initial + rate × time", "= 5 + 2×6 = 5 + 12", "= 17 cm"], numericAnswer: 17, unit: "cm"),
    NumericalProblem(id: "ign5", question: "Two points (2,3) and (2,9) are plotted. Find the vertical distance between them.", given: ["Point 1 = (2,3)", "Point 2 = (2,9)"], solutionSteps: ["Since x-coordinates are equal, the line is vertical.", "Distance = 9 − 3", "= 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "ign6", question: "A taxi charges ₹20 as base fare plus ₹8 per km. Find the total fare for a 12 km trip (using the linear relation fare = 20 + 8×distance).", given: ["Base fare = ₹20", "Rate = ₹8/km", "Distance = 12 km"], solutionSteps: ["Fare = 20 + 8×12", "= 20 + 96", "= ₹116"], numericAnswer: 116, unit: "₹"),
    NumericalProblem(id: "ign7", question: "Find the x-coordinate of the point (-4, -6).", given: ["Point = (-4, -6)"], solutionSteps: ["The first number in a coordinate pair is the x-coordinate.", "x-coordinate = −4"], numericAnswer: -4, unit: ""),
  ],
);
