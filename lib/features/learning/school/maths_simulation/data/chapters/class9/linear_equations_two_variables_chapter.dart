import '../../../models/chapter_model.dart';
final ChapterModel class9LinearEquationsTwoVariablesChapter = ChapterModel(
  standard: 9, subject: "Mathematics", chapterId: "cls9_math_linearequationstwovariables", chapterName: "Linear Equations in Two Variables",
  concepts: ["Linear equations of the form ax + by + c = 0.", "Solutions of a linear equation in two variables.", "Graph of a linear equation in two variables."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "le9_1", question: "An equation of the form ax + by + c = 0, where a and b are not both zero, is called a [ linear equation in two variables / quadratic equation ].", answer: "linear equation in two variables"),
    QuestionItem(id: "le9_2", question: "A linear equation in two variables has [ infinitely many solutions / exactly one solution ].", answer: "infinitely many solutions"),
    QuestionItem(id: "le9_3", question: "A pair of values of x and y that satisfy the equation is called its [ solution / coefficient ].", answer: "solution"),
    QuestionItem(id: "le9_4", question: "The graph of a linear equation in two variables is always a [ straight line / curve ].", answer: "straight line"),
    QuestionItem(id: "le9_5", question: "Every point on the graph of a linear equation represents a [ solution of the equation / random point ].", answer: "solution of the equation"),
    QuestionItem(id: "le9_6", question: "The equation y = 0 represents the [ x-axis / y-axis ].", answer: "x-axis"),
    QuestionItem(id: "le9_7", question: "The equation x = 0 represents the [ y-axis / x-axis ].", answer: "y-axis"),
    QuestionItem(id: "le9_8", question: "The equation x = a is a line [ parallel to the y-axis / parallel to the x-axis ].", answer: "parallel to the y-axis"),
    QuestionItem(id: "le9_9", question: "The equation y = a is a line [ parallel to the x-axis / parallel to the y-axis ].", answer: "parallel to the x-axis"),
    QuestionItem(id: "le9_10", question: "An equation like 2x + 3 = 0, though it looks like one variable, can also be treated as a linear equation in two variables with [ coefficient of y as 0 / no y term allowed ].", answer: "coefficient of y as 0"),
  ],
  numericalProblems: [
    NumericalProblem(id: "le9n1", question: "Find the value of y when x = 2 in the equation 2x + y = 10.", given: ["2x + y = 10", "x = 2"], solutionSteps: ["2(2) + y = 10", "4 + y = 10", "y = 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "le9n2", question: "Find the value of x when y = 0 in the equation 3x + 2y = 12.", given: ["3x + 2y = 12", "y = 0"], solutionSteps: ["3x + 0 = 12", "x = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "le9n3", question: "Find the value of y when x = 0 in the equation 5x − 3y = 15.", given: ["5x − 3y = 15", "x = 0"], solutionSteps: ["0 − 3y = 15", "−3y = 15", "y = −5"], numericAnswer: -5, unit: ""),
    NumericalProblem(id: "le9n4", question: "Check if (2, 3) is a solution of the equation x + y = 5. Give the LHS value.", given: ["x=2, y=3", "Equation: x+y=5"], solutionSteps: ["LHS = 2 + 3", "= 5 (matches RHS, so it IS a solution)"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "le9n5", question: "Find the value of x when y = 4 in the equation 2x − y = 6.", given: ["2x − y = 6", "y = 4"], solutionSteps: ["2x − 4 = 6", "2x = 10", "x = 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "le9n6", question: "The cost of a notebook (x) is twice the cost of a pen (y), expressed as x = 2y. If the pen costs ₹15, find the cost of the notebook.", given: ["x = 2y", "y = ₹15"], solutionSteps: ["x = 2 × 15", "= ₹30"], numericAnswer: 30, unit: "₹"),
    NumericalProblem(id: "le9n7", question: "Find the value of k if x=1, y=2 is a solution of the equation 3x + ky = 11.", given: ["3x + ky = 11", "x=1, y=2"], solutionSteps: ["3(1) + k(2) = 11", "3 + 2k = 11", "2k = 8, k = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "le9n8", question: "Find the y-intercept (value of y when x=0) of the equation 4x + 5y = 20.", given: ["4x + 5y = 20", "x = 0"], solutionSteps: ["0 + 5y = 20", "y = 4"], numericAnswer: 4, unit: ""),
  ],
);
