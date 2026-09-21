import '../../../models/chapter_model.dart';
final ChapterModel class9QuadrilateralsChapter = ChapterModel(
  standard: 9, subject: "Mathematics", chapterId: "cls9_math_quadrilaterals", chapterName: "Quadrilaterals",
  concepts: ["Angle sum property of a quadrilateral.", "Properties of a parallelogram.", "The Midpoint Theorem."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "qd9_1", question: "The sum of the angles of a quadrilateral is [ 360° / 180° ].", answer: "360°"),
    QuestionItem(id: "qd9_2", question: "A diagonal of a parallelogram divides it into [ two congruent triangles / two different triangles ].", answer: "two congruent triangles"),
    QuestionItem(id: "qd9_3", question: "In a parallelogram, opposite sides are [ equal / unequal ].", answer: "equal"),
    QuestionItem(id: "qd9_4", question: "In a parallelogram, opposite angles are [ equal / supplementary ].", answer: "equal"),
    QuestionItem(id: "qd9_5", question: "In a parallelogram, the diagonals [ bisect each other / are always equal ].", answer: "bisect each other"),
    QuestionItem(id: "qd9_6", question: "A quadrilateral is a parallelogram if a pair of opposite sides is [ equal and parallel / just equal ].", answer: "equal and parallel"),
    QuestionItem(id: "qd9_7", question: "The diagonals of a rectangle are [ equal / unequal ] in length.", answer: "equal"),
    QuestionItem(id: "qd9_8", question: "The diagonals of a rhombus bisect each other at [ right angles / any angle ].", answer: "right angles"),
    QuestionItem(id: "qd9_9", question: "The Midpoint Theorem states that the segment joining the midpoints of two sides of a triangle is [ parallel to the third side and half its length / equal to the third side ].", answer: "parallel to the third side and half its length"),
    QuestionItem(id: "qd9_10", question: "A quadrilateral formed by joining the midpoints of the sides of any quadrilateral is always a [ parallelogram / rectangle ].", answer: "parallelogram"),
    QuestionItem(id: "qd9_11", question: "In a square, all sides are equal and all angles are [ 90° / 60° ].", answer: "90°"),
    QuestionItem(id: "qd9_12", question: "A quadrilateral with exactly one pair of parallel sides is called a [ trapezium / parallelogram ].", answer: "trapezium"),
  ],
  numericalProblems: [
    NumericalProblem(id: "qd9n1", question: "Three angles of a quadrilateral are 70°, 80° and 100°. Find the fourth.", given: ["70°, 80°, 100°"], solutionSteps: ["Sum of angles = 360°", "Fourth = 360 − 70 − 80 − 100", "= 110°"], numericAnswer: 110, unit: "°"),
    NumericalProblem(id: "qd9n2", question: "In a triangle, the midpoints of two sides are joined, and the third side is 18 cm. Find the length of the segment joining the midpoints.", given: ["Third side = 18 cm"], solutionSteps: ["By the Midpoint Theorem, the segment is half the third side.", "= 18/2", "= 9 cm"], numericAnswer: 9, unit: "cm"),
    NumericalProblem(id: "qd9n3", question: "In a parallelogram, one angle is 112°. Find the adjacent angle.", given: ["One angle = 112°"], solutionSteps: ["Adjacent angles in a parallelogram are supplementary.", "Adjacent angle = 180° − 112°", "= 68°"], numericAnswer: 68, unit: "°"),
    NumericalProblem(id: "qd9n4", question: "The diagonals of a rectangle are 26 cm each and intersect at O. Find the distance from O to a vertex.", given: ["Diagonal = 26 cm"], solutionSteps: ["Diagonals of a rectangle bisect each other and are equal.", "Distance from O to a vertex = 26/2", "= 13 cm"], numericAnswer: 13, unit: "cm"),
    NumericalProblem(id: "qd9n5", question: "In a parallelogram ABCD, AB = 9 cm. Find CD (opposite side).", given: ["AB = 9 cm"], solutionSteps: ["In a parallelogram, opposite sides are equal.", "CD = AB", "= 9 cm"], numericAnswer: 9, unit: "cm"),
    NumericalProblem(id: "qd9n6", question: "A triangle has sides 10 cm, 14 cm, 18 cm. Find the perimeter of the triangle formed by joining the midpoints of its sides.", given: ["Sides: 10, 14, 18 cm"], solutionSteps: ["Each side of the midpoint triangle is half the corresponding original side.", "Perimeter = (10+14+18)/2", "= 21 cm"], numericAnswer: 21, unit: "cm"),
    NumericalProblem(id: "qd9n7", question: "Two angles of a quadrilateral are equal and the other two are 85° and 95°. Find each equal angle.", given: ["Angle1 = 85°", "Angle2 = 95°", "Remaining two are equal"], solutionSteps: ["Sum of remaining = 360° − 85° − 95° = 180°", "Each = 180°/2", "= 90°"], numericAnswer: 90, unit: "°"),
  ],
);
