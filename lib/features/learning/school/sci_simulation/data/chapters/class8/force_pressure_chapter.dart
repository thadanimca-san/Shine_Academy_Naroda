import '../../../models/chapter_model.dart';
final ChapterModel class8ForcePressureChapter = ChapterModel(
  standard: 8, subject: "Physics", chapterId: "cls8_phys_forcepressure", chapterName: "Bonus: Force and Pressure",
  concepts: ["Force as a push or pull; effects of force.", "Muscular, gravitational, magnetic, electrostatic and frictional forces.", "Contact and non-contact forces; pressure exerted by solids, liquids and gases."],
  formulas: [
    FormulaDerivation(formulaName: "Pressure", expression: "P = F / A", derivationSteps: [
      "Pressure is defined as the force acting perpendicular to a surface, per unit area of that surface.",
      "Pressure P = Force (F) / Area (A).",
      "For the same force, a smaller area produces greater pressure, and a larger area produces less pressure.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "fp1", question: "A push or a pull on an object is called a [ force / pressure ].", answer: "force"),
    QuestionItem(id: "fp2", question: "A force can change the [ speed, direction or shape of an object / colour of an object ].", answer: "speed, direction or shape of an object"),
    QuestionItem(id: "fp3", question: "The force exerted by our muscles is called [ muscular force / gravitational force ].", answer: "muscular force"),
    QuestionItem(id: "fp4", question: "The force that pulls objects toward the centre of the Earth is called [ gravitational force / magnetic force ].", answer: "gravitational force"),
    QuestionItem(id: "fp5", question: "The force exerted by a magnet on magnetic materials is called [ magnetic force / electrostatic force ].", answer: "magnetic force"),
    QuestionItem(id: "fp6", question: "The force exerted by a charged body on another object is called [ electrostatic force / magnetic force ].", answer: "electrostatic force"),
    QuestionItem(id: "fp7", question: "Forces that act on an object only when they are in physical contact with it are called [ contact forces / non-contact forces ].", answer: "contact forces"),
    QuestionItem(id: "fp8", question: "Forces such as gravitational, magnetic and electrostatic force that act without touching the object are called [ non-contact forces / contact forces ].", answer: "non-contact forces"),
    QuestionItem(id: "fp9", question: "Muscular force and frictional force are examples of [ contact forces / non-contact forces ].", answer: "contact forces"),
    QuestionItem(id: "fp10", question: "The force per unit area is called [ pressure / thrust ].", answer: "pressure"),
    QuestionItem(id: "fp11", question: "Wide straps of a bag are more comfortable to carry than thin ones because they [ reduce pressure by increasing the area / increase pressure ].", answer: "reduce pressure by increasing the area"),
    QuestionItem(id: "fp12", question: "Liquids exert pressure that acts [ in all directions / only downward ].", answer: "in all directions"),
    QuestionItem(id: "fp13", question: "The pressure exerted by air around us is called [ atmospheric pressure / water pressure ].", answer: "atmospheric pressure"),
    QuestionItem(id: "fp14", question: "A sharp knife cuts better than a blunt one because it has a [ smaller area, so more pressure / larger area, so less pressure ].", answer: "smaller area, so more pressure"),
    QuestionItem(id: "fp15", question: "Gases exert pressure on the [ walls of their container / floor only ].", answer: "walls of their container"),
  ],
  numericalProblems: [
    NumericalProblem(id: "fpn1", question: "A force of 60 N acts on an area of 3 m². Find the pressure.", given: ["F = 60 N", "A = 3 m²"], solutionSteps: ["P = F/A", "= 60/3", "= 20 Pa"], numericAnswer: 20, unit: "Pa"),
    NumericalProblem(id: "fpn2", question: "A block exerts a force of 100 N on an area of 0.5 m². Find the pressure exerted.", given: ["F = 100 N", "A = 0.5 m²"], solutionSteps: ["P = F/A", "= 100/0.5", "= 200 Pa"], numericAnswer: 200, unit: "Pa"),
    NumericalProblem(id: "fpn3", question: "A knife blade of area 0.02 m² is pressed with a force of 10 N. Find the pressure.", given: ["F = 10 N", "A = 0.02 m²"], solutionSteps: ["P = F/A", "= 10/0.02", "= 500 Pa"], numericAnswer: 500, unit: "Pa"),
    NumericalProblem(id: "fpn4", question: "Find the area over which a force of 45 N must act to produce a pressure of 15 Pa.", given: ["F = 45 N", "P = 15 Pa"], solutionSteps: ["A = F/P", "= 45/15", "= 3 m²"], numericAnswer: 3, unit: "m²"),
    NumericalProblem(id: "fpn5", question: "A bag strap presses on the shoulder with a force of 40 N over 0.02 m². Find the pressure exerted.", given: ["F = 40 N", "A = 0.02 m²"], solutionSteps: ["P = F/A", "= 40/0.02", "= 2000 Pa"], numericAnswer: 2000, unit: "Pa"),
    NumericalProblem(id: "fpn6", question: "Find the force exerted if a pressure of 250 Pa acts over an area of 4 m².", given: ["P = 250 Pa", "A = 4 m²"], solutionSteps: ["F = P×A", "= 250×4", "= 1000 N"], numericAnswer: 1000, unit: "N"),
  ],
);
