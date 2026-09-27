import '../../../models/chapter_model.dart';
final ChapterModel class10ConstructionsChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_constructions", chapterName: "Constructions",
  concepts: ["Dividing a line segment in a given ratio.", "Constructing a triangle similar to a given triangle with a given scale factor.", "Constructing tangents to a circle from an external point."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "con10_1", question: "To divide a line segment in a given ratio m:n, we draw a ray at an angle and mark off [ m+n equal arcs / m×n arcs ] on it.", answer: "m+n equal arcs"),
    QuestionItem(id: "con10_2", question: "A triangle similar to a given triangle with sides in a scale factor smaller than 1 is called [ a triangle smaller than the given triangle / a triangle equal to the given one ].", answer: "a triangle smaller than the given triangle"),
    QuestionItem(id: "con10_3", question: "When constructing a similar triangle with a scale factor greater than 1, the new triangle is [ larger than the given triangle / smaller than the given triangle ].", answer: "larger than the given triangle"),
    QuestionItem(id: "con10_4", question: "The scale factor is expressed as a ratio, such as [ p/q / p+q ].", answer: "p/q"),
    QuestionItem(id: "con10_5", question: "From an external point, two tangents can be drawn to a circle, and they are constructed using a circle drawn on the [ line joining the point to the centre as diameter / tangent as diameter ].", answer: "line joining the point to the centre as diameter"),
    QuestionItem(id: "con10_6", question: "The tangents drawn from an external point to a circle are [ equal in length / different in length ].", answer: "equal in length"),
    QuestionItem(id: "con10_7", question: "Basic Proportionality is used to justify the construction of a [ similar triangle / congruent triangle ].", answer: "similar triangle"),
    QuestionItem(id: "con10_8", question: "The point where the tangent touches the circle lies on the [ circle itself / centre ].", answer: "circle itself"),
  ],
  numericalProblems: [
    NumericalProblem(id: "con10n1", question: "To divide a line segment in the ratio 3:5, how many total equal arcs must be marked on the auxiliary ray?", given: ["Ratio = 3:5"], solutionSteps: ["Total arcs = m + n", "= 3 + 5", "= 8"], numericAnswer: 8, unit: ""),
    NumericalProblem(id: "con10n2", question: "A triangle is constructed similar to a given triangle with scale factor 3/4. If the given triangle's side is 12 cm, find the new triangle's corresponding side.", given: ["Original side = 12 cm", "Scale factor = 3/4"], solutionSteps: ["New side = original × scale factor", "= 12 × 3/4", "= 9 cm"], numericAnswer: 9, unit: "cm"),
    NumericalProblem(id: "con10n3", question: "A triangle with side 8 cm is enlarged with scale factor 5/3. Find the new side length.", given: ["Original side = 8 cm", "Scale factor = 5/3"], solutionSteps: ["New side = 8 × 5/3", "= 40/3", "≈ 13.33 cm"], numericAnswer: 13.33, unit: "cm"),
    NumericalProblem(id: "con10n4", question: "To divide a segment in the ratio 2:7, how many total equal arcs are marked?", given: ["Ratio = 2:7"], solutionSteps: ["Total arcs = m + n", "= 2 + 7", "= 9"], numericAnswer: 9, unit: ""),
    NumericalProblem(id: "con10n5", question: "Tangents are constructed from a point 15 cm from the centre of a circle of radius 9 cm. Find the tangent length.", given: ["distance = 15 cm", "radius = 9 cm"], solutionSteps: ["tangent² = distance² − radius²", "= 225 − 81 = 144", "tangent = 12 cm"], numericAnswer: 12, unit: "cm"),
  ],
);
