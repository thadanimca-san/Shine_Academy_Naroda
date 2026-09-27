import '../../../models/chapter_model.dart';
final ChapterModel class10StatisticsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_statistics", chapterName: "Statistics",
  concepts: ["Mean of grouped data.", "Mode of grouped data.", "Median of grouped data and the ogive."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "st10_1", question: "For grouped data, the mean can be calculated using the [ direct method, assumed mean method, or step deviation method / range method only ].", answer: "direct method, assumed mean method, or step deviation method"),
    QuestionItem(id: "st10_2", question: "The midpoint of a class interval is called its [ class mark / class width ].", answer: "class mark"),
    QuestionItem(id: "st10_3", question: "The class with the highest frequency is called the [ modal class / median class ].", answer: "modal class"),
    QuestionItem(id: "st10_4", question: "The class in which the median lies is called the [ median class / modal class ].", answer: "median class"),
    QuestionItem(id: "st10_5", question: "A graph representing the cumulative frequency distribution is called an [ ogive / histogram ].", answer: "ogive"),
    QuestionItem(id: "st10_6", question: "The median can be obtained graphically from the point of intersection of the 'less than' and 'more than' [ ogives / bar graphs ].", answer: "ogives"),
    QuestionItem(id: "st10_7", question: "In a distribution, the relationship 3×Median = Mode + 2×[ Mean / Range ] is an empirical formula.", answer: "Mean"),
    QuestionItem(id: "st10_8", question: "Cumulative frequency of a class is the sum of all frequencies [ up to that class / after that class only ].", answer: "up to that class"),
  ],
  numericalProblems: [
    NumericalProblem(id: "st10n1", question: "Using the empirical relationship, find the mode if mean = 30 and median = 28 (Mode = 3×Median − 2×Mean).", given: ["Mean=30, Median=28"], solutionSteps: ["Mode = 3×28 − 2×30", "= 84 − 60", "= 24"], numericAnswer: 24, unit: ""),
    NumericalProblem(id: "st10n2", question: "The class mark of the interval 20-30 is needed for a mean calculation. Find it.", given: ["Interval: 20-30"], solutionSteps: ["Class mark = (lower + upper)/2", "= (20+30)/2", "= 25"], numericAnswer: 25, unit: ""),
    NumericalProblem(id: "st10n3", question: "Using the empirical relationship, find the median if mean = 25 and mode = 19 (3×Median = Mode + 2×Mean).", given: ["Mean=25, Mode=19"], solutionSteps: ["3×Median = 19 + 2(25) = 19+50 = 69", "Median = 69/3", "= 23"], numericAnswer: 23, unit: ""),
    NumericalProblem(id: "st10n4", question: "Find the mean of the data using direct method: values 10,20,30 with frequencies 2,3,5.", given: ["x: 10,20,30", "f: 2,3,5"], solutionSteps: ["Σfx = 10×2+20×3+30×5 = 20+60+150 = 230", "Σf = 2+3+5 = 10", "Mean = 230/10 = 23"], numericAnswer: 23, unit: ""),
    NumericalProblem(id: "st10n5", question: "Find the class mark of the interval 45-60.", given: ["Interval: 45-60"], solutionSteps: ["Class mark = (45+60)/2", "= 52.5"], numericAnswer: 52.5, unit: ""),
    NumericalProblem(id: "st10n6", question: "The cumulative frequency up to class 0-20 is 12, and the class 20-40 has frequency 8. Find the cumulative frequency up to 20-40.", given: ["CF up to 0-20 = 12", "frequency of 20-40 = 8"], solutionSteps: ["CF up to 20-40 = 12 + 8", "= 20"], numericAnswer: 20, unit: ""),
    NumericalProblem(id: "st10n7", question: "Using the empirical relationship, find the mode if mean = 40 and median = 42.", given: ["Mean=40, Median=42"], solutionSteps: ["Mode = 3×Median − 2×Mean", "= 3(42) − 2(40) = 126 − 80", "= 46"], numericAnswer: 46, unit: ""),
  ],
);
