import '../../../models/chapter_model.dart';
final ChapterModel class10RealNumbersChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_realnumbers", chapterName: "Real Numbers",
  concepts: ["Euclid's Division Lemma and Algorithm.", "The Fundamental Theorem of Arithmetic.", "Irrational numbers and decimal expansions of rational numbers."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "rn10_1", question: "Euclid's Division Lemma states that for positive integers a and b, there exist unique integers q and r such that a = bq + r, where [ 0 ≤ r < b / r > b ].", answer: "0 ≤ r < b"),
    QuestionItem(id: "rn10_2", question: "Euclid's Division Algorithm is used to find the [ HCF (GCD) of two positive integers / LCM of two integers ].", answer: "HCF (GCD) of two positive integers"),
    QuestionItem(id: "rn10_3", question: "The Fundamental Theorem of Arithmetic states every composite number can be expressed as a product of primes in a way that is [ unique, apart from the order of factors / never unique ].", answer: "unique, apart from the order of factors"),
    QuestionItem(id: "rn10_4", question: "HCF × LCM of two numbers equals the [ product of the two numbers / sum of the two numbers ].", answer: "product of the two numbers"),
    QuestionItem(id: "rn10_5", question: "√2, √3, √5 are all examples of [ irrational numbers / rational numbers ].", answer: "irrational numbers"),
    QuestionItem(id: "rn10_6", question: "The decimal expansion of a rational number p/q terminates if the prime factorisation of q has only [ 2s and/or 5s / any prime factors ].", answer: "2s and/or 5s"),
    QuestionItem(id: "rn10_7", question: "If the denominator of a rational number in simplest form has a prime factor other than 2 or 5, its decimal expansion is [ non-terminating repeating / terminating ].", answer: "non-terminating repeating"),
    QuestionItem(id: "rn10_8", question: "The product of a non-zero rational number and an irrational number is always [ irrational / rational ].", answer: "irrational"),
    QuestionItem(id: "rn10_9", question: "The HCF of two prime numbers is always [ 1 / the smaller prime ].", answer: "1"),
    QuestionItem(id: "rn10_10", question: "Every composite number can be uniquely factorised into a product of [ primes / composite numbers only ].", answer: "primes"),
  ],
  numericalProblems: [
    NumericalProblem(id: "rn10n1", question: "Use Euclid's Division Algorithm to find the HCF of 60 and 100.", given: ["60 and 100"], solutionSteps: ["100 = 60×1 + 40", "60 = 40×1 + 20", "40 = 20×2 + 0", "HCF = 20"], numericAnswer: 20, unit: ""),
    NumericalProblem(id: "rn10n2", question: "If HCF(a,b) = 6 and LCM(a,b) = 72, and a = 18, find b.", given: ["HCF=6", "LCM=72", "a=18"], solutionSteps: ["HCF × LCM = a × b", "6 × 72 = 18 × b", "432 = 18b", "b = 24"], numericAnswer: 24, unit: ""),
    NumericalProblem(id: "rn10n3", question: "Find the HCF of 12 and 18 using prime factorisation.", given: ["12 = 2²×3", "18 = 2×3²"], solutionSteps: ["Common prime factors with lowest power: 2¹ × 3¹", "= 2 × 3", "= 6"], numericAnswer: 6, unit: ""),
    NumericalProblem(id: "rn10n4", question: "Find the LCM of 12 and 18 using prime factorisation.", given: ["12 = 2²×3", "18 = 2×3²"], solutionSteps: ["LCM uses highest powers of all primes: 2² × 3²", "= 4 × 9", "= 36"], numericAnswer: 36, unit: ""),
    NumericalProblem(id: "rn10n5", question: "Use Euclid's Division Algorithm to find the HCF of 210 and 55.", given: ["210 and 55"], solutionSteps: ["210 = 55×3 + 45", "55 = 45×1 + 10", "45 = 10×4 + 5", "10 = 5×2 + 0", "HCF = 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "rn10n6", question: "Find the HCF and LCM of 26 and 91 using prime factorisation, then verify HCF×LCM = product. Give the LCM.", given: ["26 = 2×13", "91 = 7×13"], solutionSteps: ["HCF = 13", "LCM = 2×7×13 = 182", "Check: 13×182 = 2366 = 26×91 ✓"], numericAnswer: 182, unit: ""),
    NumericalProblem(id: "rn10n7", question: "If HCF(a,b) = 5 and the product of a and b is 500, find LCM(a,b).", given: ["HCF = 5", "a×b = 500"], solutionSteps: ["HCF × LCM = a × b", "5 × LCM = 500", "LCM = 100"], numericAnswer: 100, unit: ""),
    NumericalProblem(id: "rn10n8", question: "Find the largest number that divides 70 and 90 exactly (i.e., their HCF).", given: ["70 and 90"], solutionSteps: ["70 = 2×5×7", "90 = 2×3²×5", "Common factors: 2×5 = 10"], numericAnswer: 10, unit: ""),
    NumericalProblem(id: "rn10n9", question: "Find the number of times 5 appears as a factor in the prime factorisation of 3750.", given: ["3750"], solutionSteps: ["3750 = 2 × 1875 = 2 × 3 × 625 = 2 × 3 × 5⁴", "5 appears 4 times."], numericAnswer: 4, unit: ""),
  ],
);
