import '../../../models/chapter_model.dart';
final ChapterModel class9HeronsFormulaChapter = ChapterModel(
  standard: 9, subject: "Mathematics", chapterId: "cls9_math_heronsformula", chapterName: "Heron's Formula",
  concepts: ["Area of a triangle using Heron's Formula, without needing the height.", "Application of Heron's Formula to quadrilaterals by splitting into triangles."],
  formulas: [
    FormulaDerivation(formulaName: "Heron's Formula", expression: "Area = √[s(s−a)(s−b)(s−c)]", derivationSteps: [
      "For a triangle with sides a, b, c, first calculate the semi-perimeter s = (a+b+c)/2.",
      "Heron's formula then gives the area directly in terms of the three sides, without needing to know the height.",
      "Area = √[s(s−a)(s−b)(s−c)].",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "hf1", question: "Heron's Formula calculates the area of a triangle using its [ three sides / height and base ].", answer: "three sides"),
    QuestionItem(id: "hf2", question: "The semi-perimeter of a triangle is half of its [ perimeter / area ].", answer: "perimeter"),
    QuestionItem(id: "hf3", question: "The semi-perimeter is usually denoted by the letter [ s / p ].", answer: "s"),
    QuestionItem(id: "hf4", question: "Heron's Formula is especially useful when the [ height of the triangle is not known / base is not known ].", answer: "height of the triangle is not known"),
    QuestionItem(id: "hf5", question: "To find the area of a general quadrilateral using Heron's formula, we split it into [ two triangles using a diagonal / four equal triangles ].", answer: "two triangles using a diagonal"),
    QuestionItem(id: "hf6", question: "For an equilateral triangle with side a, all three sides used in Heron's formula are [ equal to a / different ].", answer: "equal to a"),
    QuestionItem(id: "hf7", question: "Heron's formula was named after the ancient mathematician [ Heron of Alexandria / Euclid ].", answer: "Heron of Alexandria"),
    QuestionItem(id: "hf8", question: "Heron's formula is valid for [ any triangle / only right triangles ].", answer: "any triangle"),
  ],
  numericalProblems: [
    NumericalProblem(id: "hfn1", question: "Find the area of a triangle with sides 3 cm, 4 cm, 5 cm using Heron's formula.", given: ["a=3, b=4, c=5"], solutionSteps: ["s = (3+4+5)/2 = 6", "Area = √[6(6-3)(6-4)(6-5)]", "= √[6×3×2×1] = √36 = 6 cm²"], numericAnswer: 6, unit: "cm²"),
    NumericalProblem(id: "hfn2", question: "Find the area of a triangle with sides 5 cm, 12 cm, 13 cm.", given: ["a=5, b=12, c=13"], solutionSteps: ["s = (5+12+13)/2 = 15", "Area = √[15(15-5)(15-12)(15-13)]", "= √[15×10×3×2] = √900 = 30 cm²"], numericAnswer: 30, unit: "cm²"),
    NumericalProblem(id: "hfn3", question: "Find the semi-perimeter of a triangle with sides 7 cm, 8 cm, 9 cm.", given: ["a=7, b=8, c=9"], solutionSteps: ["s = (7+8+9)/2", "= 24/2", "= 12 cm"], numericAnswer: 12, unit: "cm"),
    NumericalProblem(id: "hfn4", question: "Find the area of an equilateral triangle with side 6 cm using Heron's formula.", given: ["a=b=c=6 cm"], solutionSteps: ["s = (6+6+6)/2 = 9", "Area = √[9(9-6)(9-6)(9-6)]", "= √[9×3×3×3] = √243 ≈ 15.59 cm²"], numericAnswer: 15.59, unit: "cm²"),
    NumericalProblem(id: "hfn5", question: "Find the area of a triangle with sides 9 cm, 12 cm, 15 cm.", given: ["a=9, b=12, c=15"], solutionSteps: ["s = (9+12+15)/2 = 18", "Area = √[18(18-9)(18-12)(18-15)]", "= √[18×9×6×3] = √2916 = 54 cm²"], numericAnswer: 54, unit: "cm²"),
    NumericalProblem(id: "hfn6", question: "A triangular field has sides 20 m, 21 m, 29 m. Find its area using Heron's formula.", given: ["a=20, b=21, c=29"], solutionSteps: ["s = (20+21+29)/2 = 35", "Area = √[35(35-20)(35-21)(35-29)]", "= √[35×15×14×6] = √44100 = 210 m²"], numericAnswer: 210, unit: "m²"),
    NumericalProblem(id: "hfn7", question: "Find the area of an isosceles triangle with equal sides 13 cm and base 10 cm.", given: ["a=13, b=13, c=10"], solutionSteps: ["s = (13+13+10)/2 = 18", "Area = √[18(18-13)(18-13)(18-10)]", "= √[18×5×5×8] = √3600 = 60 cm²"], numericAnswer: 60, unit: "cm²"),
    NumericalProblem(id: "hfn8", question: "A rhombus-shaped field has sides of 30 m each and one diagonal of 48 m. Find its area (split into two triangles, each with sides 30,30,48).", given: ["Sides = 30 m each, diagonal = 48 m"], solutionSteps: ["For one triangle: s = (30+30+48)/2 = 54", "Area of one triangle = √[54(54-30)(54-30)(54-48)] = √[54×24×24×6] = 432 m²", "Total rhombus area = 2 × 432", "= 864 m²"], numericAnswer: 864, unit: "m²"),
  ],
);
