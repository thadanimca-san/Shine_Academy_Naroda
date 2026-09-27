import '../../../models/chapter_model.dart';
final ChapterModel class10QuadraticEquationsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_quadraticequations", chapterName: "Quadratic Equations",
  concepts: ["Solving quadratic equations by factorisation.", "The quadratic formula.", "Nature of roots using the discriminant."],
  formulas: [
    FormulaDerivation(formulaName: "The Quadratic Formula", expression: "x = [−b ± √(b²−4ac)] / 2a", derivationSteps: [
      "Starting with ax² + bx + c = 0, divide throughout by a: x² + (b/a)x + c/a = 0.",
      "Complete the square: x² + (b/a)x + (b/2a)² = (b/2a)² − c/a.",
      "This gives (x + b/2a)² = (b²−4ac)/4a².",
      "Taking the square root and solving for x: x = [−b ± √(b²−4ac)] / 2a.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "qe1", question: "An equation of the form ax²+bx+c=0, where a≠0, is called a [ quadratic equation / linear equation ].", answer: "quadratic equation"),
    QuestionItem(id: "qe2", question: "The values of x that satisfy a quadratic equation are called its [ roots (or solutions) / coefficients ].", answer: "roots (or solutions)"),
    QuestionItem(id: "qe3", question: "A quadratic equation has at most [ two roots / three roots ].", answer: "two roots"),
    QuestionItem(id: "qe4", question: "The expression b²−4ac in the quadratic formula is called the [ discriminant / determinant ].", answer: "discriminant"),
    QuestionItem(id: "qe5", question: "If the discriminant is greater than zero, the quadratic equation has [ two distinct real roots / no real roots ].", answer: "two distinct real roots"),
    QuestionItem(id: "qe6", question: "If the discriminant equals zero, the quadratic equation has [ two equal real roots / two distinct roots ].", answer: "two equal real roots"),
    QuestionItem(id: "qe7", question: "If the discriminant is less than zero, the quadratic equation has [ no real roots / two real roots ].", answer: "no real roots"),
    QuestionItem(id: "qe8", question: "Solving a quadratic equation by expressing it as a product of two linear factors is called the [ factorisation method / formula method only ].", answer: "factorisation method"),
    QuestionItem(id: "qe9", question: "The sum of the roots of ax²+bx+c=0 is [ −b/a / c/a ].", answer: "−b/a"),
    QuestionItem(id: "qe10", question: "The product of the roots of ax²+bx+c=0 is [ c/a / −b/a ].", answer: "c/a"),
  ],
  numericalProblems: [
    NumericalProblem(id: "qen1", question: "Solve x² − 5x + 6 = 0 by factorisation. Find the larger root.", given: ["x² − 5x + 6 = 0"], solutionSteps: ["Factorise: (x−2)(x−3) = 0", "x = 2 or x = 3", "Larger root = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "qen2", question: "Find the discriminant of x² − 4x + 4 = 0.", given: ["a=1, b=−4, c=4"], solutionSteps: ["D = b² − 4ac", "= 16 − 16", "= 0"], numericAnswer: 0, unit: ""),
    NumericalProblem(id: "qen3", question: "Solve x² − 9 = 0. Find the positive root.", given: ["x² − 9 = 0"], solutionSteps: ["x² = 9", "x = ±3", "Positive root = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "qen4", question: "Using the quadratic formula, find a root of x² + 2x − 3 = 0 (the larger one).", given: ["a=1, b=2, c=−3"], solutionSteps: ["x = [−2 ± √(4+12)]/2", "= [−2 ± 4]/2", "Larger root: (−2+4)/2 = 1"], numericAnswer: 1, unit: ""),
    NumericalProblem(id: "qen5", question: "Find the sum of the roots of 2x² − 8x + 6 = 0.", given: ["a=2, b=−8, c=6"], solutionSteps: ["Sum of roots = −b/a", "= −(−8)/2", "= 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "qen6", question: "Find the product of the roots of 3x² + 5x − 12 = 0.", given: ["a=3, b=5, c=−12"], solutionSteps: ["Product = c/a", "= −12/3", "= −4"], numericAnswer: -4, unit: ""),
    NumericalProblem(id: "qen7", question: "Solve x² − 7x + 12 = 0 by factorisation. Find the smaller root.", given: ["x² − 7x + 12 = 0"], solutionSteps: ["Factorise: (x−3)(x−4) = 0", "x = 3 or x = 4", "Smaller root = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "qen8", question: "Find the discriminant of 2x² + 3x + 5 = 0, and state whether real roots exist (give discriminant value).", given: ["a=2, b=3, c=5"], solutionSteps: ["D = b² − 4ac", "= 9 − 40", "= −31 (negative, so no real roots)"], numericAnswer: -31, unit: ""),
    NumericalProblem(id: "qen9", question: "The product of two consecutive positive integers is 132. Using x(x+1)=132, find the smaller integer.", given: ["x(x+1) = 132"], solutionSteps: ["x² + x − 132 = 0", "Factorise: (x−11)(x+12) = 0", "x = 11 (rejecting negative root)"], numericAnswer: 11, unit: ""),
    NumericalProblem(id: "qen10", question: "Using the quadratic formula, find the positive root of x² − 6x + 5 = 0.", given: ["a=1, b=−6, c=5"], solutionSteps: ["x = [6 ± √(36−20)]/2", "= [6 ± 4]/2", "Roots: 5 and 1; positive roots are both 5 and 1, larger is 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "qen11", question: "Find the value of k for which x² + kx + 16 = 0 has equal roots (D=0), given k is positive.", given: ["a=1, b=k, c=16", "D = 0"], solutionSteps: ["k² − 4(1)(16) = 0", "k² = 64", "k = 8 (positive value)"], numericAnswer: 8, unit: ""),
  ],
);
