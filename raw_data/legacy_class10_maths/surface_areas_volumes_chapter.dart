import '../../../models/chapter_model.dart';
final ChapterModel class10SurfaceAreasVolumesChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_surfaceareasvolumes", chapterName: "Surface Areas and Volumes",
  concepts: ["Surface area and volume of combinations of solids.", "Conversion of a solid from one shape to another.", "Frustum of a cone."],
  formulas: [
    FormulaDerivation(formulaName: "Volume of a Frustum of a Cone", expression: "V = (πh/3)(r₁² + r₂² + r₁r₂)", derivationSteps: [
      "A frustum is what remains of a cone after cutting off the top with a plane parallel to the base.",
      "It can be thought of as the difference between a large cone and a smaller cone that was removed.",
      "Working through the algebra with the two radii r₁, r₂ and height h gives V = (πh/3)(r₁² + r₂² + r₁r₂).",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "sv10_1", question: "When a solid is reshaped into another (like melting a metal cone into a cylinder), the [ volume remains the same / surface area remains the same ].", answer: "volume remains the same"),
    QuestionItem(id: "sv10_2", question: "The surface area of a combination of two solids, like a cone on a hemisphere, is found by adding the [ curved surface areas of each visible part, excluding the joined base / total surface areas of each solid ].", answer: "curved surface areas of each visible part, excluding the joined base"),
    QuestionItem(id: "sv10_3", question: "A frustum is obtained by cutting a cone with a plane [ parallel to its base / perpendicular to its base ].", answer: "parallel to its base"),
    QuestionItem(id: "sv10_4", question: "A frustum has [ two circular parallel faces of different radii / one circular face ].", answer: "two circular parallel faces of different radii"),
    QuestionItem(id: "sv10_5", question: "When ice cream is served with a hemispherical top on a cone, the total volume is the sum of the [ volume of the cone and the volume of the hemisphere / volume of the cone only ].", answer: "volume of the cone and the volume of the hemisphere"),
    QuestionItem(id: "sv10_6", question: "The volume of a cylinder of radius r and height h remains πr²h regardless of [ its orientation / its material ].", answer: "its orientation"),
    QuestionItem(id: "sv10_7", question: "Melting a solid sphere and recasting it into smaller identical spheres keeps the [ total volume constant / total surface area constant ].", answer: "total volume constant"),
    QuestionItem(id: "sv10_8", question: "The slant height of a frustum is used to calculate its [ curved surface area / volume only ].", answer: "curved surface area"),
  ],
  numericalProblems: [
    NumericalProblem(id: "sv10n1", question: "A metal sphere of radius 6 cm is melted and recast into a cylinder of radius 6 cm. Find the height of the cylinder (volume is conserved).", given: ["Sphere r=6cm", "Cylinder r=6cm"], solutionSteps: ["Volume of sphere = (4/3)πr³ = (4/3)π(216)", "Volume of cylinder = πr²h = π(36)h", "Equate: (4/3)(216) = 36h", "h = 288/36 = 8 cm"], numericAnswer: 8, unit: "cm"),
    NumericalProblem(id: "sv10n2", question: "Find the volume of a hemisphere with radius 3 cm. (Take π=22/7, round to nearest whole number)", given: ["r = 3 cm"], solutionSteps: ["V = (2/3)πr³", "= (2/3)(22/7)(27)", "≈ 56.57, rounds to 57 cm³"], numericAnswer: 57, unit: "cm³"),
    NumericalProblem(id: "sv10n3", question: "Find the volume of a frustum with radii 6 cm and 3 cm, and height 4 cm. (Take π=22/7)", given: ["r1=6, r2=3, h=4"], solutionSteps: ["V = (πh/3)(r1²+r2²+r1r2)", "= (22/7 × 4/3)(36+9+18)", "= (88/21)(63) = 264 cm³"], numericAnswer: 264, unit: "cm³"),
    NumericalProblem(id: "sv10n4", question: "An ice cream cone has radius 3.5 cm and height 12 cm, topped with a hemisphere of the same radius. Find the volume of the cone part. (Take π=22/7)", given: ["r=3.5 cm", "h=12 cm"], solutionSteps: ["V(cone) = (1/3)πr²h", "= (1/3)(22/7)(12.25)(12)", "= 154 cm³"], numericAnswer: 154, unit: "cm³"),
    NumericalProblem(id: "sv10n5", question: "A solid cylinder of radius 6 cm and height 12 cm is melted and recast into small spheres of radius 3 cm each. Find the number of spheres formed.", given: ["Cylinder: r=6, h=12", "Sphere: r=3"], solutionSteps: ["V(cylinder) = πr²h = π(36)(12) = 432π", "V(sphere) = (4/3)πr³ = (4/3)π(27) = 36π", "Number of spheres = 432π ÷ 36π", "= 12"], numericAnswer: 12, unit: "spheres"),
    NumericalProblem(id: "sv10n6", question: "Find the total surface area of a solid formed by a cylinder of radius 7 cm, height 10 cm, with a hemisphere of the same radius on top (curved surfaces only, plus base). (Take π=22/7)", given: ["r=7 cm", "h=10 cm"], solutionSteps: ["CSA(cylinder) = 2πrh = 2(22/7)(7)(10) = 440 cm²", "CSA(hemisphere) = 2πr² = 2(22/7)(49) = 308 cm²", "Base area = πr² = 154 cm²", "Total = 440+308+154 = 902 cm²"], numericAnswer: 902, unit: "cm²"),
    NumericalProblem(id: "sv10n7", question: "A cone of height 24 cm and radius 6 cm is melted and recast into a sphere. Find the radius of the sphere.", given: ["Cone: r=6, h=24"], solutionSteps: ["V(cone) = (1/3)πr²h = (1/3)π(36)(24) = 288π", "V(sphere) = (4/3)πR³ = 288π", "R³ = 216, R = 6 cm"], numericAnswer: 6, unit: "cm"),
  ],
);
