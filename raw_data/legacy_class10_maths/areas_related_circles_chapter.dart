import '../../../models/chapter_model.dart';
final ChapterModel class10AreasRelatedCirclesChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_areasrelatedcircles", chapterName: "Areas Related to Circles",
  concepts: ["Perimeter and area of a circle.", "Area of a sector and a segment of a circle.", "Areas of combinations of plane figures."],
  formulas: [
    FormulaDerivation(formulaName: "Area of a Sector", expression: "Area = (θ/360°) × πr²", derivationSteps: [
      "A sector is a 'pie slice' of the circle, corresponding to a central angle θ out of the full 360°.",
      "The full circle (360°) has area πr².",
      "So a sector with angle θ has area proportional to θ/360° of the full circle's area: (θ/360°) × πr².",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "arc1", question: "The circumference of a circle with radius r is [ 2πr / πr² ].", answer: "2πr"),
    QuestionItem(id: "arc2", question: "The area of a circle with radius r is [ πr² / 2πr ].", answer: "πr²"),
    QuestionItem(id: "arc3", question: "The region enclosed by two radii and the corresponding arc is called a [ sector / segment ].", answer: "sector"),
    QuestionItem(id: "arc4", question: "The region enclosed by a chord and the corresponding arc is called a [ segment / sector ].", answer: "segment"),
    QuestionItem(id: "arc5", question: "The area of a sector with angle θ (in degrees) is (θ/360°) × [ πr² / 2πr ].", answer: "πr²"),
    QuestionItem(id: "arc6", question: "The length of an arc with angle θ (in degrees) is (θ/360°) × [ 2πr / πr² ].", answer: "2πr"),
    QuestionItem(id: "arc7", question: "The area of a minor segment equals the area of the corresponding sector minus the area of the [ corresponding triangle / whole circle ].", answer: "corresponding triangle"),
    QuestionItem(id: "arc8", question: "A sector with central angle 180° is called a [ semicircle / quadrant ].", answer: "semicircle"),
    QuestionItem(id: "arc9", question: "A sector with central angle 90° is called a [ quadrant / semicircle ].", answer: "quadrant"),
    QuestionItem(id: "arc10", question: "The area of a combined figure made of a square and a semicircle is found by [ adding their individual areas / subtracting their areas ].", answer: "adding their individual areas"),
  ],
  numericalProblems: [
    NumericalProblem(id: "arcn1", question: "Find the area of a circle with radius 14 cm. (Take π = 22/7)", given: ["r = 14 cm"], solutionSteps: ["Area = πr²", "= (22/7) × 196", "= 616 cm²"], numericAnswer: 616, unit: "cm²"),
    NumericalProblem(id: "arcn2", question: "Find the area of a sector with radius 7 cm and central angle 90°. (Take π = 22/7)", given: ["r=7 cm", "θ=90°"], solutionSteps: ["Area = (θ/360°) × πr²", "= (90/360) × (22/7) × 49", "= (1/4) × 154 = 38.5 cm²"], numericAnswer: 38.5, unit: "cm²"),
    NumericalProblem(id: "arcn3", question: "Find the circumference of a circle with radius 21 cm. (Take π = 22/7)", given: ["r = 21 cm"], solutionSteps: ["C = 2πr", "= 2 × (22/7) × 21", "= 132 cm"], numericAnswer: 132, unit: "cm"),
    NumericalProblem(id: "arcn4", question: "Find the length of an arc with radius 21 cm and central angle 60°. (Take π = 22/7)", given: ["r=21 cm", "θ=60°"], solutionSteps: ["Arc length = (θ/360°) × 2πr", "= (60/360) × 2 × (22/7) × 21", "= (1/6) × 132 = 22 cm"], numericAnswer: 22, unit: "cm"),
    NumericalProblem(id: "arcn5", question: "Find the area of a quadrant of a circle with radius 14 cm. (Take π = 22/7)", given: ["r = 14 cm", "θ = 90°"], solutionSteps: ["Area = (90/360) × πr²", "= (1/4) × (22/7) × 196", "= 154 cm²"], numericAnswer: 154, unit: "cm²"),
    NumericalProblem(id: "arcn6", question: "Find the area of a semicircle with radius 7 cm. (Take π = 22/7)", given: ["r = 7 cm"], solutionSteps: ["Area = (180/360) × πr²", "= ½ × (22/7) × 49", "= 77 cm²"], numericAnswer: 77, unit: "cm²"),
    NumericalProblem(id: "arcn7", question: "The minute hand of a clock is 10.5 cm long. Find the area swept in 30 minutes. (Take π = 22/7)", given: ["r = 10.5 cm", "30 min = 180°"], solutionSteps: ["Area = (180/360) × πr²", "= ½ × (22/7) × 110.25", "= 173.25 cm²"], numericAnswer: 173.25, unit: "cm²"),
    NumericalProblem(id: "arcn8", question: "Find the area of a sector with radius 6 cm and central angle 60°. (Take π = 22/7, round to 2 decimals)", given: ["r=6 cm", "θ=60°"], solutionSteps: ["Area = (60/360) × πr²", "= (1/6) × (22/7) × 36", "≈ 18.86 cm²"], numericAnswer: 18.86, unit: "cm²"),
    NumericalProblem(id: "arcn9", question: "Find the area of a circular ring (annulus) with outer radius 14 cm and inner radius 7 cm. (Take π = 22/7)", given: ["R = 14 cm", "r = 7 cm"], solutionSteps: ["Area = π(R² − r²)", "= (22/7) × (196−49)", "= (22/7) × 147 = 462 cm²"], numericAnswer: 462, unit: "cm²"),
  ],
);
