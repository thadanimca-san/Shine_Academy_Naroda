import '../../../models/chapter_model.dart';
final ChapterModel class10ArithmeticProgressionsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_arithmeticprogressions", chapterName: "Arithmetic Progressions",
  concepts: ["The nth term of an AP.", "Sum of the first n terms of an AP.", "Applications of arithmetic progressions."],
  formulas: [
    FormulaDerivation(formulaName: "nth Term of an AP", expression: "aₙ = a + (n−1)d", derivationSteps: [
      "In an AP, each term is obtained by adding a fixed common difference d to the previous term.",
      "The first term is a. The second term is a+d, the third is a+2d, and so on.",
      "So the nth term is obtained by adding d exactly (n−1) times: aₙ = a + (n−1)d.",
    ]),
    FormulaDerivation(formulaName: "Sum of n Terms of an AP", expression: "Sₙ = n/2 × [2a + (n−1)d]", derivationSteps: [
      "Write the sum forwards: Sₙ = a + (a+d) + ... + [a+(n-1)d].",
      "Write it backwards: Sₙ = [a+(n-1)d] + ... + (a+d) + a.",
      "Adding both, each pair sums to [2a+(n-1)d], and there are n such pairs, giving 2Sₙ = n[2a+(n-1)d].",
      "So Sₙ = n/2 × [2a + (n−1)d].",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "ap10_1", question: "A list of numbers in which each term (after the first) is obtained by adding a fixed number to the previous term is called an [ arithmetic progression (AP) / geometric progression ].", answer: "arithmetic progression (AP)"),
    QuestionItem(id: "ap10_2", question: "The fixed number added at each step of an AP is called the [ common difference / common ratio ].", answer: "common difference"),
    QuestionItem(id: "ap10_3", question: "The common difference is found by subtracting [ any term from its succeeding term / the first term from the last term only ].", answer: "any term from its succeeding term"),
    QuestionItem(id: "ap10_4", question: "The nth term of an AP with first term a and common difference d is [ a + (n−1)d / a + nd ].", answer: "a + (n−1)d"),
    QuestionItem(id: "ap10_5", question: "If the common difference of an AP is positive, the terms are [ increasing / decreasing ].", answer: "increasing"),
    QuestionItem(id: "ap10_6", question: "If the common difference of an AP is negative, the terms are [ decreasing / increasing ].", answer: "decreasing"),
    QuestionItem(id: "ap10_7", question: "The sum of the first n terms of an AP is given by Sₙ = n/2 × [ 2a + (n−1)d / a + (n−1)d ].", answer: "2a + (n−1)d"),
    QuestionItem(id: "ap10_8", question: "The sum of the first n terms can also be written as Sₙ = n/2 × [ (a + l) / (a × l) ], where l is the last term.", answer: "(a + l)"),
    QuestionItem(id: "ap10_9", question: "In an AP, if a₁, a₂, a₃ are consecutive terms, then a₂ is the [ arithmetic mean of a₁ and a₃ / geometric mean of a₁ and a₃ ].", answer: "arithmetic mean of a₁ and a₃"),
    QuestionItem(id: "ap10_10", question: "The natural numbers 1, 2, 3, 4, ... form an AP with common difference [ 1 / 0 ].", answer: "1"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ap10n1", question: "Find the 10th term of the AP: 3, 7, 11, 15, ...", given: ["a = 3", "d = 4", "n = 10"], solutionSteps: ["aₙ = a + (n−1)d", "= 3 + 9×4", "= 3 + 36 = 39"], numericAnswer: 39, unit: ""),
    NumericalProblem(id: "ap10n2", question: "Find the sum of the first 10 terms of the AP: 2, 4, 6, 8, ...", given: ["a=2, d=2, n=10"], solutionSteps: ["Sₙ = n/2 × [2a+(n-1)d]", "= 10/2 × [4 + 9×2]", "= 5 × 22 = 110"], numericAnswer: 110, unit: ""),
    NumericalProblem(id: "ap10n3", question: "Find the common difference of the AP: 5, 11, 17, 23, ...", given: ["Terms: 5,11,17,23"], solutionSteps: ["d = 11 − 5", "= 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "ap10n4", question: "Find the sum of the first 20 natural numbers.", given: ["a=1, d=1, n=20"], solutionSteps: ["Sₙ = n/2 × [2a+(n-1)d]", "= 20/2 × [2 + 19]", "= 10 × 21 = 210"], numericAnswer: 210, unit: ""),
    NumericalProblem(id: "ap10n5", question: "Find the 15th term of the AP: 10, 7, 4, 1, ...", given: ["a=10, d=−3, n=15"], solutionSteps: ["aₙ = a + (n−1)d", "= 10 + 14×(−3)", "= 10 − 42 = −32"], numericAnswer: -32, unit: ""),
    NumericalProblem(id: "ap10n6", question: "Which term of the AP 3, 8, 13, 18, ... is 78?", given: ["a=3, d=5, aₙ=78"], solutionSteps: ["aₙ = a + (n−1)d", "78 = 3 + (n−1)×5", "75 = (n−1)×5, n−1=15, n=16"], numericAnswer: 16, unit: ""),
    NumericalProblem(id: "ap10n7", question: "Find the sum of the first 15 terms of the AP: 5, 9, 13, 17, ...", given: ["a=5, d=4, n=15"], solutionSteps: ["Sₙ = n/2 × [2a+(n-1)d]", "= 15/2 × [10 + 14×4]", "= 7.5 × 66 = 495"], numericAnswer: 495, unit: ""),
    NumericalProblem(id: "ap10n8", question: "The 3rd term of an AP is 15 and the 8th term is 35. Find the common difference.", given: ["a₃ = 15", "a₈ = 35"], solutionSteps: ["a₈ − a₃ = 5d", "35 − 15 = 5d", "20 = 5d, d = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "ap10n9", question: "Find the sum of first 25 multiples of 4.", given: ["a=4, d=4, n=25"], solutionSteps: ["Sₙ = n/2 × [2a+(n-1)d]", "= 25/2 × [8 + 24×4]", "= 12.5 × 104 = 1300"], numericAnswer: 1300, unit: ""),
    NumericalProblem(id: "ap10n10", question: "In an AP, a = 5 and the 12th term is 38. Find the common difference.", given: ["a = 5", "a₁₂ = 38"], solutionSteps: ["a₁₂ = a + 11d", "38 = 5 + 11d", "33 = 11d, d = 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "ap10n11", question: "A person saves ₹200 in the first month and increases the saving by ₹50 each month. Find the total savings in 12 months.", given: ["a=200, d=50, n=12"], solutionSteps: ["Sₙ = n/2 × [2a+(n-1)d]", "= 12/2 × [400 + 11×50]", "= 6 × 950 = ₹5700"], numericAnswer: 5700, unit: "₹"),
  ],
);
