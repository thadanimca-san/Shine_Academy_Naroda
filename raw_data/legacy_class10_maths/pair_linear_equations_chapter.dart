import '../../../models/chapter_model.dart';
final ChapterModel class10PairLinearEquationsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_pairlinearequations", chapterName: "Pair of Linear Equations in Two Variables",
  concepts: ["Graphical method of solving a pair of linear equations.", "Algebraic methods: substitution and elimination.", "Consistency of a pair of linear equations."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ple1", question: "A pair of linear equations that has at least one solution is called [ consistent / inconsistent ].", answer: "consistent"),
    QuestionItem(id: "ple2", question: "A pair of linear equations that has no solution is called [ inconsistent / consistent ].", answer: "inconsistent"),
    QuestionItem(id: "ple3", question: "If two lines representing a pair of equations intersect at one point, the pair has [ a unique solution / infinitely many solutions ].", answer: "a unique solution"),
    QuestionItem(id: "ple4", question: "If two lines representing a pair of equations are parallel, the pair has [ no solution / a unique solution ].", answer: "no solution"),
    QuestionItem(id: "ple5", question: "If two lines representing a pair of equations coincide, the pair has [ infinitely many solutions / no solution ].", answer: "infinitely many solutions"),
    QuestionItem(id: "ple6", question: "The method of solving equations by expressing one variable in terms of another and substituting is called the [ substitution method / elimination method ].", answer: "substitution method"),
    QuestionItem(id: "ple7", question: "The method of solving equations by adding or subtracting equations to remove one variable is called the [ elimination method / substitution method ].", answer: "elimination method"),
    QuestionItem(id: "ple8", question: "For the pair a₁x+b₁y+c₁=0 and a₂x+b₂y+c₂=0, if a₁/a₂ ≠ b₁/b₂, the pair has [ a unique solution / no solution ].", answer: "a unique solution"),
    QuestionItem(id: "ple9", question: "If a₁/a₂ = b₁/b₂ ≠ c₁/c₂, the pair of lines is [ parallel with no solution / coincident ].", answer: "parallel with no solution"),
    QuestionItem(id: "ple10", question: "If a₁/a₂ = b₁/b₂ = c₁/c₂, the pair of lines is [ coincident with infinite solutions / parallel ].", answer: "coincident with infinite solutions"),
  ],
  numericalProblems: [
    NumericalProblem(id: "plen1", question: "Solve by substitution: x + y = 10 and x − y = 2. Find x.", given: ["x+y=10", "x−y=2"], solutionSteps: ["From first equation: x = 10 − y", "Substitute: (10−y) − y = 2", "10 − 2y = 2, y = 4", "x = 10 − 4 = 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "plen2", question: "Solve by elimination: 2x + y = 11 and x + y = 7. Find x.", given: ["2x+y=11", "x+y=7"], solutionSteps: ["Subtract the equations: (2x+y) − (x+y) = 11 − 7", "x = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "plen3", question: "Solve by substitution: y = 2x and 3x + y = 20. Find x.", given: ["y=2x", "3x+y=20"], solutionSteps: ["Substitute y=2x: 3x + 2x = 20", "5x = 20", "x = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "plen4", question: "Solve by elimination: 3x + 2y = 12 and 3x − y = 3. Find y.", given: ["3x+2y=12", "3x−y=3"], solutionSteps: ["Subtract: (3x+2y)−(3x−y) = 12−3", "3y = 9, y = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "plen5", question: "The sum of two numbers is 18 and their difference is 4. Find the larger number.", given: ["x+y=18", "x−y=4"], solutionSteps: ["Add the equations: 2x = 22", "x = 11"], numericAnswer: 11, unit: ""),
    NumericalProblem(id: "plen6", question: "5 chairs and 3 tables cost ₹7000, while 3 chairs and 5 tables cost ₹9000. Using elimination, find the cost of a table (let chair=x, table=y: 5x+3y=7000, 3x+5y=9000).", given: ["5x+3y=7000", "3x+5y=9000"], solutionSteps: ["Multiply first by 5, second by 3: 25x+15y=35000, 9x+15y=27000", "Subtract: 16x=8000, x=500", "Substitute in 5(500)+3y=7000: 3y=4500, y=1500"], numericAnswer: 1500, unit: "₹"),
    NumericalProblem(id: "plen7", question: "Determine whether the pair 2x+3y=5 and 4x+6y=10 is consistent (1) or inconsistent with infinite solutions check — give the ratio a1/a2.", given: ["2x+3y=5", "4x+6y=10"], solutionSteps: ["a1/a2 = 2/4 = 0.5, b1/b2 = 3/6 = 0.5, c1/c2 = 5/10 = 0.5", "All equal, so lines coincide (infinite solutions).", "Ratio value = 0.5"], numericAnswer: 0.5, unit: "(a1/a2 = b1/b2 = c1/c2, coincident lines)"),
    NumericalProblem(id: "plen8", question: "Solve: 2x + 3y = 13 and x − y = 1. Find x.", given: ["2x+3y=13", "x−y=1"], solutionSteps: ["From second equation: x = y+1", "Substitute: 2(y+1)+3y=13, so 2y+2+3y=13, 5y=11, y=2.2", "x = y+1 = 3.2"], numericAnswer: 3.2, unit: ""),
  ],
);
