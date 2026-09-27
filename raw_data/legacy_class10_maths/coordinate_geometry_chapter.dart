import '../../../models/chapter_model.dart';
final ChapterModel class10CoordinateGeometryChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_coordinategeometry", chapterName: "Coordinate Geometry",
  concepts: ["Distance formula between two points.", "Section formula for a point dividing a line segment.", "Area of a triangle using coordinates."],
  formulas: [
    FormulaDerivation(formulaName: "Distance Formula", expression: "d = √[(x₂−x₁)² + (y₂−y₁)²]", derivationSteps: [
      "Consider two points P(x₁,y₁) and Q(x₂,y₂) on the Cartesian plane.",
      "Drawing a right triangle with legs parallel to the axes, the horizontal leg has length (x₂−x₁) and the vertical leg (y₂−y₁).",
      "By the Pythagoras Theorem, the distance PQ = √[(x₂−x₁)² + (y₂−y₁)²].",
    ]),
    FormulaDerivation(formulaName: "Section Formula", expression: "P(x,y) = [(m₁x₂+m₂x₁)/(m₁+m₂), (m₁y₂+m₂y₁)/(m₁+m₂)]", derivationSteps: [
      "To find a point P dividing the segment joining A(x₁,y₁) and B(x₂,y₂) in the ratio m₁:m₂,",
      "we weight each endpoint's coordinate by the opposite ratio part and divide by the sum of ratio parts.",
      "This gives P = [(m₁x₂+m₂x₁)/(m₁+m₂), (m₁y₂+m₂y₁)/(m₁+m₂)].",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "cg10_1", question: "The distance between two points (x₁,y₁) and (x₂,y₂) is given by [ √[(x₂−x₁)²+(y₂−y₁)²] / (x₂−x₁)+(y₂−y₁) ].", answer: "√[(x₂−x₁)²+(y₂−y₁)²]"),
    QuestionItem(id: "cg10_2", question: "The distance of a point (x,y) from the origin is [ √(x²+y²) / x+y ].", answer: "√(x²+y²)"),
    QuestionItem(id: "cg10_3", question: "The formula used to find a point dividing a segment in a given ratio is called the [ section formula / distance formula ].", answer: "section formula"),
    QuestionItem(id: "cg10_4", question: "The midpoint formula is a special case of the section formula where the ratio is [ 1:1 / 2:1 ].", answer: "1:1"),
    QuestionItem(id: "cg10_5", question: "The midpoint of (x₁,y₁) and (x₂,y₂) is [ ((x₁+x₂)/2, (y₁+y₂)/2) / (x₁+x₂, y₁+y₂) ].", answer: "((x₁+x₂)/2, (y₁+y₂)/2)"),
    QuestionItem(id: "cg10_6", question: "If the area of a triangle formed by three points is zero, the points are [ collinear / non-collinear ].", answer: "collinear"),
    QuestionItem(id: "cg10_7", question: "The area of a triangle with given vertices can be found using the [ coordinate (determinant) formula / distance formula only ].", answer: "coordinate (determinant) formula"),
    QuestionItem(id: "cg10_8", question: "Coordinate geometry connects [ algebra and geometry / only geometry ].", answer: "algebra and geometry"),
  ],
  numericalProblems: [
    NumericalProblem(id: "cg10n1", question: "Find the distance between the points (3, 4) and (0, 0).", given: ["(3,4) and (0,0)"], solutionSteps: ["d = √[(3-0)²+(4-0)²]", "= √[9+16] = √25", "= 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "cg10n2", question: "Find the midpoint of the segment joining (2, 3) and (6, 7).", given: ["(2,3) and (6,7)"], solutionSteps: ["Midpoint = ((2+6)/2, (3+7)/2)", "= (4, 5)", "x-coordinate = 4"], numericAnswer: 4, unit: "(x-coordinate; y=5)"),
    NumericalProblem(id: "cg10n3", question: "Find the distance between (1, 1) and (4, 5).", given: ["(1,1) and (4,5)"], solutionSteps: ["d = √[(4-1)²+(5-1)²]", "= √[9+16] = √25", "= 5"], numericAnswer: 5, unit: ""),
    NumericalProblem(id: "cg10n4", question: "Find the point that divides the segment joining (2,2) and (8,8) in the ratio 1:2 (give the x-coordinate).", given: ["A=(2,2), B=(8,8)", "ratio m1:m2 = 1:2"], solutionSteps: ["x = (m1×x2+m2×x1)/(m1+m2)", "= (1×8+2×2)/3 = (8+4)/3", "= 4"], numericAnswer: 4, unit: ""),
    NumericalProblem(id: "cg10n5", question: "Check if the points (1,1), (3,3), (5,5) are collinear by finding the area of the triangle they form.", given: ["(1,1), (3,3), (5,5)"], solutionSteps: ["Area = ½|x1(y2−y3)+x2(y3−y1)+x3(y1−y2)|", "= ½|1(3−5)+3(5−1)+5(1−3)| = ½|−2+12−10|", "= ½×0 = 0 (collinear)"], numericAnswer: 0, unit: "(area = 0, collinear)"),
    NumericalProblem(id: "cg10n6", question: "Find the distance of the point (-6, 8) from the origin.", given: ["Point = (-6, 8)"], solutionSteps: ["d = √(x²+y²)", "= √(36+64) = √100", "= 10"], numericAnswer: 10, unit: ""),
    NumericalProblem(id: "cg10n7", question: "Find the y-coordinate of the midpoint of (-3, 7) and (5, -1).", given: ["(-3,7) and (5,-1)"], solutionSteps: ["Midpoint y = (7+(-1))/2", "= 6/2", "= 3"], numericAnswer: 3, unit: ""),
    NumericalProblem(id: "cg10n8", question: "Find the area of a triangle with vertices (0,0), (4,0), (0,6).", given: ["(0,0), (4,0), (0,6)"], solutionSteps: ["Area = ½|x1(y2−y3)+x2(y3−y1)+x3(y1−y2)|", "= ½|0(0−6)+4(6−0)+0(0−0)| = ½|24|", "= 12"], numericAnswer: 12, unit: ""),
    NumericalProblem(id: "cg10n9", question: "Find the distance between (-2, -3) and (2, 0).", given: ["(-2,-3) and (2,0)"], solutionSteps: ["d = √[(2-(-2))²+(0-(-3))²]", "= √[16+9] = √25", "= 5"], numericAnswer: 5, unit: ""),
  ],
);
