import '../../../models/chapter_model.dart';
final ChapterModel class9AreasParallelogramsTrianglesChapter = ChapterModel(
  standard: 9, subject: "Mathematics", chapterId: "cls9_math_areasparallelogramstriangles", chapterName: "Areas of Parallelograms and Triangles",
  concepts: ["Figures on the same base and between the same parallels.", "Parallelograms on the same base and between the same parallels have equal area.", "Triangles on the same base and between the same parallels have equal area."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ap1", question: "Two figures are said to be on the same base and between the same parallels if they share a common [ base and their opposite side/vertex lies on a line parallel to the base / colour ].", answer: "base and their opposite side/vertex lies on a line parallel to the base"),
    QuestionItem(id: "ap2", question: "Parallelograms on the same base and between the same parallels are [ equal in area / different in area ].", answer: "equal in area"),
    QuestionItem(id: "ap3", question: "The area of a parallelogram is the product of its base and the corresponding [ height (altitude) / diagonal ].", answer: "height (altitude)"),
    QuestionItem(id: "ap4", question: "A diagonal of a parallelogram divides it into two triangles of [ equal area / unequal area ].", answer: "equal area"),
    QuestionItem(id: "ap5", question: "Triangles on the same base and between the same parallels are [ equal in area / different in area ].", answer: "equal in area"),
    QuestionItem(id: "ap6", question: "The area of a triangle is half the product of its base and [ height / perimeter ].", answer: "height"),
    QuestionItem(id: "ap7", question: "A triangle and a parallelogram on the same base and between the same parallels have areas in the ratio [ 1:2 / 1:1 ].", answer: "1:2"),
    QuestionItem(id: "ap8", question: "If a triangle and a parallelogram have equal areas and are on the same base, they must lie [ between the same parallels / on different lines ].", answer: "between the same parallels"),
    QuestionItem(id: "ap9", question: "The median of a triangle divides it into two triangles of [ equal area / unequal area ].", answer: "equal area"),
    QuestionItem(id: "ap10", question: "Two parallelograms on equal bases and between the same parallels have areas that are [ equal / in ratio 2:1 ].", answer: "equal"),
  ],
  numericalProblems: [
    NumericalProblem(id: "apn1", question: "Find the area of a parallelogram with base 10 cm and height 6 cm.", given: ["base = 10 cm", "height = 6 cm"], solutionSteps: ["Area = base × height", "= 10 × 6", "= 60 cm²"], numericAnswer: 60, unit: "cm²"),
    NumericalProblem(id: "apn2", question: "A triangle and parallelogram share the same base 8 cm and are between the same parallels 5 cm apart. If the parallelogram's area is 40 cm², find the triangle's area.", given: ["Parallelogram area = 40 cm²"], solutionSteps: ["Triangle and parallelogram on the same base, between same parallels: triangle area = half of parallelogram area", "= 40/2", "= 20 cm²"], numericAnswer: 20, unit: "cm²"),
    NumericalProblem(id: "apn3", question: "Find the area of a triangle with base 14 cm and height 9 cm.", given: ["base = 14 cm", "height = 9 cm"], solutionSteps: ["Area = ½ × base × height", "= ½ × 14 × 9", "= 63 cm²"], numericAnswer: 63, unit: "cm²"),
    NumericalProblem(id: "apn4", question: "A diagonal divides a parallelogram of area 84 cm² into two triangles. Find the area of one triangle.", given: ["Parallelogram area = 84 cm²"], solutionSteps: ["A diagonal divides a parallelogram into two triangles of equal area.", "Each triangle's area = 84/2", "= 42 cm²"], numericAnswer: 42, unit: "cm²"),
    NumericalProblem(id: "apn5", question: "Two parallelograms are on equal bases and between the same parallels. One has area 55 cm². Find the area of the other.", given: ["Area of parallelogram 1 = 55 cm²"], solutionSteps: ["Parallelograms on equal bases between same parallels have equal area.", "Area of parallelogram 2 = 55 cm²"], numericAnswer: 55, unit: "cm²"),
    NumericalProblem(id: "apn6", question: "The median of a triangle with area 72 cm² divides it into two smaller triangles. Find the area of each.", given: ["Triangle area = 72 cm²"], solutionSteps: ["A median divides a triangle into two triangles of equal area.", "Each = 72/2", "= 36 cm²"], numericAnswer: 36, unit: "cm²"),
    NumericalProblem(id: "apn7", question: "A parallelogram has area 96 cm² and base 12 cm. Find its height.", given: ["Area = 96 cm²", "base = 12 cm"], solutionSteps: ["Area = base × height, so height = Area/base", "= 96/12", "= 8 cm"], numericAnswer: 8, unit: "cm"),
  ],
);
