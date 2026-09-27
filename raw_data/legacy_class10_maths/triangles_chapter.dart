import '../../../models/chapter_model.dart';
final ChapterModel class10TrianglesChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_triangles", chapterName: "Triangles",
  concepts: ["Similar triangles and criteria for similarity.", "Basic Proportionality Theorem (Thales' Theorem).", "The Pythagoras Theorem and its converse."],
  formulas: [
    FormulaDerivation(formulaName: "Basic Proportionality Theorem", expression: "DE ∥ BC ⟹ AD/DB = AE/EC", derivationSteps: [
      "If a line DE is drawn parallel to side BC of triangle ABC, intersecting AB at D and AC at E,",
      "then it divides the other two sides in the same ratio.",
      "This gives AD/DB = AE/EC — known as the Basic Proportionality Theorem or Thales' Theorem.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "tr10_1", question: "Two figures with the same shape but not necessarily the same size are called [ similar / congruent ].", answer: "similar"),
    QuestionItem(id: "tr10_2", question: "Two triangles are similar if their corresponding angles are equal and corresponding sides are [ in the same ratio (proportional) / equal ].", answer: "in the same ratio (proportional)"),
    QuestionItem(id: "tr10_3", question: "The Basic Proportionality Theorem is also known as [ Thales' Theorem / Pythagoras Theorem ].", answer: "Thales' Theorem"),
    QuestionItem(id: "tr10_4", question: "If a line divides two sides of a triangle in the same ratio, the line is [ parallel to the third side / perpendicular to the third side ].", answer: "parallel to the third side"),
    QuestionItem(id: "tr10_5", question: "The AA similarity criterion states that if two angles of one triangle equal two angles of another, the triangles are [ similar / congruent ].", answer: "similar"),
    QuestionItem(id: "tr10_6", question: "The SSS similarity criterion requires corresponding sides to be [ proportional / equal ].", answer: "proportional"),
    QuestionItem(id: "tr10_7", question: "The Pythagoras Theorem applies to [ right triangles / all triangles ].", answer: "right triangles"),
    QuestionItem(id: "tr10_8", question: "The Pythagoras Theorem states (hypotenuse)² = (base)² + [ (height)² / (base) ].", answer: "(height)²"),
    QuestionItem(id: "tr10_9", question: "The converse of the Pythagoras Theorem is used to check if a triangle is a [ right triangle / equilateral triangle ].", answer: "right triangle"),
    QuestionItem(id: "tr10_10", question: "The ratio of areas of two similar triangles equals the [ square of the ratio of their corresponding sides / ratio of their sides ].", answer: "square of the ratio of their corresponding sides"),
  ],
  numericalProblems: [
    NumericalProblem(id: "tr10n1", question: "In a right triangle, the two legs are 9 cm and 12 cm. Find the hypotenuse.", given: ["legs = 9, 12"], solutionSteps: ["hyp² = 9² + 12²", "= 81+144 = 225", "hyp = 15 cm"], numericAnswer: 15, unit: "cm"),
    NumericalProblem(id: "tr10n2", question: "Two similar triangles have corresponding sides in ratio 2:3. If the area of the smaller is 20 cm², find the area of the larger.", given: ["Ratio 2:3", "Smaller area = 20 cm²"], solutionSteps: ["Ratio of areas = (3/2)² = 9/4", "Larger area = 20 × 9/4", "= 45 cm²"], numericAnswer: 45, unit: "cm²"),
    NumericalProblem(id: "tr10n3", question: "In triangle ABC, DE ∥ BC, with AD=4 cm, DB=6 cm, AE=5 cm. Find EC using the Basic Proportionality Theorem.", given: ["AD=4, DB=6, AE=5"], solutionSteps: ["AD/DB = AE/EC", "4/6 = 5/EC", "EC = (5×6)/4", "= 7.5 cm"], numericAnswer: 7.5, unit: "cm"),
    NumericalProblem(id: "tr10n4", question: "A ladder 10 m long reaches a window 8 m above the ground. Find the distance of the foot of the ladder from the wall.", given: ["hypotenuse = 10 m", "height = 8 m"], solutionSteps: ["base² = 10² − 8²", "= 100−64 = 36", "base = 6 m"], numericAnswer: 6, unit: "m"),
    NumericalProblem(id: "tr10n5", question: "Check if a triangle with sides 7 cm, 24 cm, 25 cm is a right triangle. Give (hypotenuse)² − (sum of other squares) [should be 0 if right triangle].", given: ["Sides: 7, 24, 25"], solutionSteps: ["25² = 625, 7²+24² = 49+576 = 625", "625 − 625 = 0, confirming it's a right triangle."], numericAnswer: 0, unit: "(0 confirms right triangle)"),
    NumericalProblem(id: "tr10n6", question: "Two similar triangles have areas 64 cm² and 121 cm². Find the ratio of their corresponding sides (smaller:larger, give as a decimal).", given: ["Area1=64, Area2=121"], solutionSteps: ["Ratio of sides = √(Area1/Area2)", "= √(64/121) = 8/11", "≈ 0.727"], numericAnswer: 0.727, unit: "(= 8/11)"),
    NumericalProblem(id: "tr10n7", question: "In triangle ABC, DE ∥ BC. If AD=3, AB=9, AC=12, find AE.", given: ["AD=3, AB=9, AC=12"], solutionSteps: ["Since DE∥BC, AD/AB = AE/AC", "3/9 = AE/12", "AE = 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "tr10n8", question: "A 6 m tall pole casts a shadow of 8 m. Find the length of the hypotenuse (top of pole to tip of shadow) using Pythagoras.", given: ["height = 6 m", "shadow = 8 m"], solutionSteps: ["hyp² = 6² + 8²", "= 36+64 = 100", "hyp = 10 m"], numericAnswer: 10, unit: "m"),
  ],
);
