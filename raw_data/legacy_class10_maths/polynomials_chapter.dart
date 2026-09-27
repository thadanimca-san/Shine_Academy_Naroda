import '../../../models/chapter_model.dart';
final ChapterModel class10PolynomialsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_polynomials", chapterName: "Polynomials",
  concepts: ["Geometrical meaning of zeroes of a polynomial.", "Relationship between zeroes and coefficients of a quadratic polynomial.", "Division algorithm for polynomials."],
  formulas: [
    FormulaDerivation(formulaName: "Sum and Product of Zeroes (Quadratic)", expression: "α+β = −b/a,  αβ = c/a", derivationSteps: [
      "For a quadratic polynomial ax² + bx + c with zeroes α and β, it can be written as a(x−α)(x−β).",
      "Expanding: a[x² − (α+β)x + αβ] = ax² − a(α+β)x + aαβ.",
      "Comparing coefficients with ax²+bx+c: −a(α+β) = b, so α+β = −b/a. And aαβ = c, so αβ = c/a.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "pl10_1", question: "The zeroes of a polynomial p(x) are the x-values where the graph of y=p(x) [ intersects the x-axis / intersects the y-axis ].", answer: "intersects the x-axis"),
    QuestionItem(id: "pl10_2", question: "A linear polynomial has at most [ 1 zero / 2 zeroes ].", answer: "1 zero"),
    QuestionItem(id: "pl10_3", question: "A quadratic polynomial has at most [ 2 zeroes / 3 zeroes ].", answer: "2 zeroes"),
    QuestionItem(id: "pl10_4", question: "A cubic polynomial has at most [ 3 zeroes / 2 zeroes ].", answer: "3 zeroes"),
    QuestionItem(id: "pl10_5", question: "For a quadratic polynomial ax²+bx+c, the sum of zeroes equals [ −b/a / c/a ].", answer: "−b/a"),
    QuestionItem(id: "pl10_6", question: "For a quadratic polynomial ax²+bx+c, the product of zeroes equals [ c/a / −b/a ].", answer: "c/a"),
    QuestionItem(id: "pl10_7", question: "The graph of a quadratic polynomial is a [ parabola / straight line ].", answer: "parabola"),
    QuestionItem(id: "pl10_8", question: "If a parabola opens upwards, the coefficient of x² is [ positive / negative ].", answer: "positive"),
    QuestionItem(id: "pl10_9", question: "The Division Algorithm for polynomials states p(x) = g(x)×q(x) + r(x), where the degree of r(x) is [ less than degree of g(x) / greater than degree of g(x) ].", answer: "less than degree of g(x)"),
    QuestionItem(id: "pl10_10", question: "If the remainder r(x) = 0 when p(x) is divided by g(x), then g(x) is a [ factor of p(x) / zero of p(x) ].", answer: "factor of p(x)"),
  ],
  numericalProblems: [
    NumericalProblem(id: "pl10n1", question: "For the quadratic x² − 5x + 6, find the sum of its zeroes.", given: ["a=1, b=−5, c=6"], solutionSteps: ["Sum of zeroes = −b/a", "= −(−5)/1", "= 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "pl10n2", question: "For the quadratic x² − 5x + 6, find the product of its zeroes.", given: ["a=1, b=−5, c=6"], solutionSteps: ["Product of zeroes = c/a", "= 6/1", "= 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "pl10n3", question: "For the quadratic 2x² + 3x − 5, find the sum of zeroes.", given: ["a=2, b=3, c=−5"], solutionSteps: ["Sum = −b/a", "= −3/2", "= −1.5"], numericAnswer: -1.5, unit: ""),
    NumericalProblem(id: "pl10n4", question: "For the quadratic 2x² + 3x − 5, find the product of zeroes.", given: ["a=2, b=3, c=−5"], solutionSteps: ["Product = c/a", "= −5/2", "= −2.5"], numericAnswer: -2.5, unit: ""),
    NumericalProblem(id: "pl10n5", question: "If the sum and product of zeroes of a quadratic are 4 and 3 respectively, find the quadratic's coefficient ratio -b/a (i.e., find -b/a which equals the sum).", given: ["Sum = 4", "Product = 3"], solutionSteps: ["A quadratic with zeroes summing to 4 has −b/a = 4", "So the value asked is 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "pl10n6", question: "For the quadratic 3x² − 6x + 2, find the sum of zeroes.", given: ["a=3, b=-6, c=2"], solutionSteps: ["Sum = −b/a", "= −(−6)/3", "= 2"], numericAnswer: 2, unit: ""),
    NumericalProblem(id: "pl10n7", question: "Divide p(x)=x²+5x+6 by g(x)=x+2 and find the quotient's constant term.", given: ["p(x) = x²+5x+6", "g(x) = x+2"], solutionSteps: ["x²+5x+6 = (x+2)(x+3)", "Quotient = x+3, constant term = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "pl10n8", question: "If one zero of x² − 7x + k is 3, find k.", given: ["p(x) = x² − 7x + k", "One zero = 3"], solutionSteps: ["p(3) = 0: 9 − 21 + k = 0", "k = 12"], numericAnswer: 12, unit: ""),
    NumericalProblem(id: "pl10n9", question: "For the quadratic x² − 9, find the product of its zeroes.", given: ["a=1, b=0, c=-9"], solutionSteps: ["Product = c/a", "= −9/1", "= −9"], numericAnswer: -9, unit: ""),
    NumericalProblem(id: "pl10n10", question: "If the zeroes of a quadratic are 5 and −3, find the value of −b/a (their sum).", given: ["Zeroes = 5, −3"], solutionSteps: ["Sum = 5 + (−3)", "= 2"], numericAnswer: 2, unit: ""),
  ],
);
