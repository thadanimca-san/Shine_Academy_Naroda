import '../../../models/chapter_model.dart';
final ChapterModel class8AlgebraicIdentitiesChapter = ChapterModel(
  standard: 8, subject: "Mathematics", chapterId: "cls8_math_algebraicidentities", chapterName: "Algebraic Expressions and Identities",
  concepts: ["Multiplication of algebraic expressions.", "Standard identities: (a+b)², (a−b)², (a+b)(a−b).", "Applications of identities in computation."],
  formulas: [
    FormulaDerivation(formulaName: "Square of a Sum", expression: "(a + b)² = a² + 2ab + b²", derivationSteps: [
      "(a + b)² means (a + b) × (a + b).",
      "Expanding using the distributive law: a(a+b) + b(a+b) = a² + ab + ab + b²",
      "= a² + 2ab + b².",
    ]),
    FormulaDerivation(formulaName: "Square of a Difference", expression: "(a − b)² = a² − 2ab + b²", derivationSteps: [
      "(a − b)² means (a − b) × (a − b).",
      "Expanding: a(a−b) − b(a−b) = a² − ab − ab + b²",
      "= a² − 2ab + b².",
    ]),
    FormulaDerivation(formulaName: "Difference of Squares", expression: "(a + b)(a − b) = a² − b²", derivationSteps: [
      "Expanding (a+b)(a−b) using the distributive law: a(a−b) + b(a−b)",
      "= a² − ab + ab − b²",
      "= a² − b².",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "ai1", question: "A statement of equality that is true for all values of the variables is called an [ identity / equation ].", answer: "identity"),
    QuestionItem(id: "ai2", question: "The identity (a+b)² expands to a² + 2ab + [ b² / 2b² ].", answer: "b²"),
    QuestionItem(id: "ai3", question: "The identity (a−b)² expands to a² − 2ab + [ b² / −b² ].", answer: "b²"),
    QuestionItem(id: "ai4", question: "The identity (a+b)(a−b) simplifies to [ a² − b² / a² + b² ].", answer: "a² − b²"),
    QuestionItem(id: "ai5", question: "To multiply a monomial by a binomial, we use the [ distributive law / associative law ].", answer: "distributive law"),
    QuestionItem(id: "ai6", question: "When multiplying two binomials, each term of the first binomial is multiplied by [ each term of the second / only the first term of the second ].", answer: "each term of the second"),
    QuestionItem(id: "ai7", question: "The identity (x+a)(x+b) expands to x² + (a+b)x + [ ab / a+b ].", answer: "ab"),
    QuestionItem(id: "ai8", question: "Standard identities help in [ quick mental calculations and factorisation / only drawing graphs ].", answer: "quick mental calculations and factorisation"),
    QuestionItem(id: "ai9", question: "Using identities, 102 × 98 can be computed quickly as (100+2)(100−2) = [ 100² − 2² / 100² + 2² ].", answer: "100² − 2²"),
    QuestionItem(id: "ai10", question: "In the expansion of (a+b)², the middle term 2ab is called the [ cross term / square term ].", answer: "cross term"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ain1", question: "Expand and evaluate (x + 5)² for x = 3.", given: ["x = 3"], solutionSteps: ["(x+5)² = x² + 10x + 25", "= 9 + 30 + 25", "= 64"], numericAnswer: 64, unit: ""),
    NumericalProblem(id: "ain2", question: "Use an identity to find 105 × 95.", given: ["105 × 95 = (100+5)(100−5)"], solutionSteps: ["(100+5)(100−5) = 100² − 5²", "= 10000 − 25", "= 9975"], numericAnswer: 9975, unit: ""),
    NumericalProblem(id: "ain3", question: "Use an identity to find 998² (as (1000−2)²).", given: ["998 = 1000 − 2"], solutionSteps: ["(1000−2)² = 1000² − 2×1000×2 + 2²", "= 1000000 − 4000 + 4", "= 996004"], numericAnswer: 996004, unit: ""),
    NumericalProblem(id: "ain4", question: "Expand and evaluate (2x − 3)² for x = 4.", given: ["x = 4"], solutionSteps: ["(2x−3)² = 4x² − 12x + 9", "= 4(16) − 12(4) + 9 = 64 − 48 + 9", "= 25"], numericAnswer: 25, unit: ""),
    NumericalProblem(id: "ain5", question: "Use an identity to find 203 × 197.", given: ["203 × 197 = (200+3)(200−3)"], solutionSteps: ["(200+3)(200−3) = 200² − 3²", "= 40000 − 9", "= 39991"], numericAnswer: 39991, unit: ""),
    NumericalProblem(id: "ain6", question: "Use the identity (x+a)(x+b) to expand and evaluate (x+3)(x+7) for x = 5.", given: ["x = 5, a = 3, b = 7"], solutionSteps: ["(x+3)(x+7) = x² + 10x + 21", "= 25 + 50 + 21", "= 96"], numericAnswer: 96, unit: ""),
    NumericalProblem(id: "ain7", question: "If a + b = 12 and ab = 32, find the value of a² + b².", given: ["a + b = 12", "ab = 32"], solutionSteps: ["(a+b)² = a² + 2ab + b²", "144 = a² + b² + 64", "a² + b² = 144 − 64 = 80"], numericAnswer: 80, unit: ""),
    NumericalProblem(id: "ain8", question: "Use an identity to find 79² (as (80−1)²).", given: ["79 = 80 − 1"], solutionSteps: ["(80−1)² = 80² − 2×80×1 + 1²", "= 6400 − 160 + 1", "= 6241"], numericAnswer: 6241, unit: ""),
    NumericalProblem(id: "ain9", question: "If a − b = 6 and ab = 16, find the value of a² + b².", given: ["a − b = 6", "ab = 16"], solutionSteps: ["(a−b)² = a² − 2ab + b²", "36 = a² + b² − 32", "a² + b² = 36 + 32 = 68"], numericAnswer: 68, unit: ""),
    NumericalProblem(id: "ain10", question: "Find the value of 51² − 49² using the difference of squares identity.", given: ["51² − 49²"], solutionSteps: ["a² − b² = (a+b)(a−b)", "= (51+49)(51−49) = 100 × 2", "= 200"], numericAnswer: 200, unit: ""),
  ],
);
