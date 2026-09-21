import '../../../models/chapter_model.dart';
final ChapterModel class9ProbabilityChapter = ChapterModel(
  standard: 9, subject: "Mathematics", chapterId: "cls9_math_probability", chapterName: "Probability",
  concepts: ["Empirical (experimental) approach to probability.", "Probability of an event based on trials.", "Range of values probability can take."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "pb1", question: "The class 9 approach to probability, based on actual experiments/trials, is called the [ empirical (experimental) probability / theoretical probability ].", answer: "empirical (experimental) probability"),
    QuestionItem(id: "pb2", question: "Empirical probability of an event = (number of trials in which the event happened) / [ total number of trials / total number of outcomes ].", answer: "total number of trials"),
    QuestionItem(id: "pb3", question: "The probability of an event always lies between [ 0 and 1 (inclusive) / 1 and 100 ].", answer: "0 and 1 (inclusive)"),
    QuestionItem(id: "pb4", question: "The probability of an impossible event is [ 0 / 1 ].", answer: "0"),
    QuestionItem(id: "pb5", question: "The probability of a sure (certain) event is [ 1 / 0 ].", answer: "1"),
    QuestionItem(id: "pb6", question: "As the number of trials in an experiment increases, the empirical probability tends to get [ closer to the true probability / less accurate ].", answer: "closer to the true probability"),
    QuestionItem(id: "pb7", question: "The sum of the probabilities of all possible outcomes of a trial is [ 1 / 0 ].", answer: "1"),
    QuestionItem(id: "pb8", question: "Tossing a coin and observing whether it lands heads or tails is an example of a [ random experiment / fixed outcome ].", answer: "random experiment"),
    QuestionItem(id: "pb9", question: "A result of a random experiment is called an [ outcome / event only ].", answer: "outcome"),
    QuestionItem(id: "pb10", question: "Probability, as studied in Class 9, is based on real data collected through [ actual experiments / theoretical assumptions only ].", answer: "actual experiments"),
  ],
  numericalProblems: [
    NumericalProblem(id: "pbn1", question: "A coin is tossed 50 times and lands heads 28 times. Find the empirical probability of getting heads.", given: ["Trials = 50", "Heads = 28"], solutionSteps: ["Probability = 28/50", "= 0.56"], numericAnswer: 0.56, unit: ""),
    NumericalProblem(id: "pbn2", question: "In 200 trials of rolling a die, the number 6 appeared 40 times. Find the empirical probability of getting a 6.", given: ["Trials = 200", "Sixes = 40"], solutionSteps: ["Probability = 40/200", "= 0.2"], numericAnswer: 0.2, unit: ""),
    NumericalProblem(id: "pbn3", question: "In a survey of 500 families, 320 have a car. Find the empirical probability that a randomly chosen family has a car.", given: ["Total = 500", "Have car = 320"], solutionSteps: ["Probability = 320/500", "= 0.64"], numericAnswer: 0.64, unit: ""),
    NumericalProblem(id: "pbn4", question: "A bag was drawn from 300 times; a red ball came out 75 times. Find the empirical probability of drawing a red ball.", given: ["Trials = 300", "Red = 75"], solutionSteps: ["Probability = 75/300", "= 0.25"], numericAnswer: 0.25, unit: ""),
    NumericalProblem(id: "pbn5", question: "Out of 150 days, it rained on 30 days. Find the empirical probability that it rains on a given day.", given: ["Total days = 150", "Rainy days = 30"], solutionSteps: ["Probability = 30/150", "= 0.2"], numericAnswer: 0.2, unit: ""),
    NumericalProblem(id: "pbn6", question: "A batsman played 40 innings and scored a century in 8 of them. Find the empirical probability of scoring a century in the next innings.", given: ["Innings = 40", "Centuries = 8"], solutionSteps: ["Probability = 8/40", "= 0.2"], numericAnswer: 0.2, unit: ""),
    NumericalProblem(id: "pbn7", question: "In 1000 items produced, 25 were found defective. Find the empirical probability that an item is defective.", given: ["Total = 1000", "Defective = 25"], solutionSteps: ["Probability = 25/1000", "= 0.025"], numericAnswer: 0.025, unit: ""),
  ],
);
