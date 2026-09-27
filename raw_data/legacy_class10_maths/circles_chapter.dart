import '../../../models/chapter_model.dart';
final ChapterModel class10CirclesChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_circles", chapterName: "Circles",
  concepts: ["Tangent to a circle.", "Number of tangents from a point to a circle.", "Length of tangents from an external point."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ci10_1", question: "A line that touches a circle at exactly one point is called a [ tangent / secant ].", answer: "tangent"),
    QuestionItem(id: "ci10_2", question: "A line that intersects a circle at two points is called a [ secant / tangent ].", answer: "secant"),
    QuestionItem(id: "ci10_3", question: "The point where a tangent touches the circle is called the [ point of contact / centre ].", answer: "point of contact"),
    QuestionItem(id: "ci10_4", question: "The tangent to a circle is [ perpendicular to the radius / parallel to the radius ] at the point of contact.", answer: "perpendicular to the radius"),
    QuestionItem(id: "ci10_5", question: "From a point outside a circle, exactly [ two tangents / one tangent ] can be drawn to the circle.", answer: "two tangents"),
    QuestionItem(id: "ci10_6", question: "The lengths of the two tangents drawn from an external point to a circle are [ equal / different ].", answer: "equal"),
    QuestionItem(id: "ci10_7", question: "From a point on the circle, [ only one tangent / two tangents ] can be drawn.", answer: "only one tangent"),
    QuestionItem(id: "ci10_8", question: "From a point inside a circle, [ no tangent / one tangent ] can be drawn.", answer: "no tangent"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ci10n1", question: "A tangent from an external point is 12 cm, and the radius of the circle is 5 cm. Find the distance of the point from the centre.", given: ["tangent = 12 cm", "radius = 5 cm"], solutionSteps: ["The radius is perpendicular to the tangent, forming a right triangle.", "distance² = 12² + 5² = 144+25 = 169", "distance = 13 cm"], numericAnswer: 13, unit: "cm"),
    NumericalProblem(id: "ci10n2", question: "The distance of a point from the centre of a circle is 25 cm, and the circle's radius is 7 cm. Find the length of the tangent from that point.", given: ["distance = 25 cm", "radius = 7 cm"], solutionSteps: ["tangent² = distance² − radius²", "= 625 − 49 = 576", "tangent = 24 cm"], numericAnswer: 24, unit: "cm"),
    NumericalProblem(id: "ci10n3", question: "Two tangents PA and PB are drawn from external point P to a circle. If PA = 9 cm, find PB.", given: ["PA = 9 cm"], solutionSteps: ["Tangents from the same external point are equal in length.", "PB = PA", "= 9 cm"], numericAnswer: 9, unit: "cm"),
    NumericalProblem(id: "ci10n4", question: "A tangent from a point 17 cm from the centre of a circle has length 15 cm. Find the radius.", given: ["distance = 17 cm", "tangent = 15 cm"], solutionSteps: ["radius² = distance² − tangent²", "= 289 − 225 = 64", "radius = 8 cm"], numericAnswer: 8, unit: "cm"),
    NumericalProblem(id: "ci10n5", question: "A circle has radius 6 cm. Find the length of the tangent from a point 10 cm away from the centre.", given: ["radius = 6 cm", "distance = 10 cm"], solutionSteps: ["tangent² = distance² − radius²", "= 100 − 36 = 64", "tangent = 8 cm"], numericAnswer: 8, unit: "cm"),
    NumericalProblem(id: "ci10n6", question: "From an external point, two tangents of length 20 cm each are drawn to a circle of radius 15 cm. Find the distance from the point to the centre.", given: ["tangent = 20 cm", "radius = 15 cm"], solutionSteps: ["distance² = tangent² + radius²", "= 400 + 225 = 625", "distance = 25 cm"], numericAnswer: 25, unit: "cm"),
  ],
);
