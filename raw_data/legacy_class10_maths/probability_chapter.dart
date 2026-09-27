import '../../../models/chapter_model.dart';
final ChapterModel class10ProbabilityChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_probability", chapterName: "Probability",
  concepts: ["Theoretical (classical) probability.", "Complementary events.", "Probability of events related to playing cards, dice and coins."],
  formulas: [
    FormulaDerivation(formulaName: "Theoretical Probability", expression: "P(E) = (favourable outcomes) / (total outcomes)", derivationSteps: [
      "Unlike the experimental probability from Class 9, theoretical probability is calculated assuming all outcomes are equally likely, without needing to perform trials.",
      "P(E) = number of outcomes favourable to E / total number of possible outcomes.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "pb10_1", question: "The probability calculated assuming all outcomes are equally likely, without performing an experiment, is called [ theoretical (classical) probability / empirical probability ].", answer: "theoretical (classical) probability"),
    QuestionItem(id: "pb10_2", question: "P(E) = (number of favourable outcomes) / [ total number of possible outcomes / number of unfavourable outcomes ].", answer: "total number of possible outcomes"),
    QuestionItem(id: "pb10_3", question: "The event 'E does not happen' is called the [ complement of E / union of E ].", answer: "complement of E"),
    QuestionItem(id: "pb10_4", question: "P(E) + P(not E) = [ 1 / 0 ].", answer: "1"),
    QuestionItem(id: "pb10_5", question: "A standard deck of playing cards has [ 52 / 48 ] cards.", answer: "52"),
    QuestionItem(id: "pb10_6", question: "A deck of cards has [ 4 / 2 ] suits.", answer: "4"),
    QuestionItem(id: "pb10_7", question: "Each suit in a deck of cards has [ 13 / 12 ] cards.", answer: "13"),
    QuestionItem(id: "pb10_8", question: "An event that is certain to happen has probability [ 1 / 0 ].", answer: "1"),
    QuestionItem(id: "pb10_9", question: "An event that cannot happen has probability [ 0 / 1 ].", answer: "0"),
    QuestionItem(id: "pb10_10", question: "The probability of an event always lies between [ 0 and 1 (inclusive) / 1 and 100 ].", answer: "0 and 1 (inclusive)"),
  ],
  numericalProblems: [
    NumericalProblem(id: "pb10n1", question: "A die is thrown once. Find the probability of getting an even number.", given: ["Total outcomes = 6", "Even numbers: 2,4,6 (3 outcomes)"], solutionSteps: ["P = favourable/total", "= 3/6", "= 0.5"], numericAnswer: 0.5, unit: ""),
    NumericalProblem(id: "pb10n2", question: "A card is drawn from a well-shuffled deck of 52 cards. Find the probability of drawing a king.", given: ["Total = 52", "Kings = 4"], solutionSteps: ["P = 4/52", "= 1/13 ≈ 0.077"], numericAnswer: 0.077, unit: ""),
    NumericalProblem(id: "pb10n3", question: "A bag has 3 red and 7 black balls. Find the probability of NOT drawing a red ball.", given: ["Red=3, Black=7, Total=10"], solutionSteps: ["P(red) = 3/10", "P(not red) = 1 − 3/10", "= 0.7"], numericAnswer: 0.7, unit: ""),
    NumericalProblem(id: "pb10n4", question: "Two dice are thrown together. Find the probability of getting a sum of 9.", given: ["Total outcomes = 36", "Favourable: (3,6)(4,5)(5,4)(6,3) = 4 outcomes"], solutionSteps: ["P = 4/36", "= 1/9 ≈ 0.111"], numericAnswer: 0.111, unit: ""),
    NumericalProblem(id: "pb10n5", question: "A card is drawn from a deck of 52. Find the probability of drawing a red face card (jack, queen, king of hearts/diamonds).", given: ["Total = 52", "Red face cards = 6"], solutionSteps: ["P = 6/52", "= 3/26 ≈ 0.115"], numericAnswer: 0.115, unit: ""),
    NumericalProblem(id: "pb10n6", question: "A bag has 5 white, 4 red, 3 black balls. Find the probability of drawing a white or red ball.", given: ["White=5, Red=4, Black=3, Total=12"], solutionSteps: ["Favourable = 5+4 = 9", "P = 9/12", "= 0.75"], numericAnswer: 0.75, unit: ""),
    NumericalProblem(id: "pb10n7", question: "Find the probability of getting a number less than 3 when a die is thrown.", given: ["Total outcomes = 6", "Favourable: 1,2 (2 outcomes)"], solutionSteps: ["P = 2/6", "= 1/3 ≈ 0.333"], numericAnswer: 0.333, unit: ""),
    NumericalProblem(id: "pb10n8", question: "A number is chosen at random from 1 to 20. Find the probability that it is a multiple of 4.", given: ["Total = 20", "Multiples of 4: 4,8,12,16,20 (5 outcomes)"], solutionSteps: ["P = 5/20", "= 0.25"], numericAnswer: 0.25, unit: ""),
    NumericalProblem(id: "pb10n9", question: "In a class of 40 students, 24 like cricket. Find the probability that a randomly chosen student does NOT like cricket.", given: ["Total = 40", "Like cricket = 24"], solutionSteps: ["P(like) = 24/40 = 0.6", "P(not like) = 1 − 0.6", "= 0.4"], numericAnswer: 0.4, unit: ""),
    NumericalProblem(id: "pb10n10", question: "Two coins are tossed simultaneously. Find the probability of getting at least one head.", given: ["Outcomes: HH,HT,TH,TT (4 total)", "Favourable: HH,HT,TH (3 outcomes)"], solutionSteps: ["P = 3/4", "= 0.75"], numericAnswer: 0.75, unit: ""),
  ],
);
