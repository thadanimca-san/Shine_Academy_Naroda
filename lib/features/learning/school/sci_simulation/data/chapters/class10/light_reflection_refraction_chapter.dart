import '../../../models/chapter_model.dart';
final ChapterModel class10LightReflectionRefractionChapter = ChapterModel(
  standard: 10, subject: "Physics", chapterId: "cls10_phys_lightreflectionrefraction", chapterName: "Light – Reflection and Refraction",
  concepts: ["Reflection by spherical mirrors; the mirror formula.", "Refraction of light through lenses; the lens formula.", "Power of a lens."],
  formulas: [
    FormulaDerivation(formulaName: "Mirror Formula", expression: "1/v + 1/u = 1/f", derivationSteps: [
      "For a spherical mirror, u is the object distance, v is the image distance, and f is the focal length, all measured from the pole.",
      "Using the sign convention and similar triangles from ray diagrams, the relation between them is derived as 1/v + 1/u = 1/f.",
    ]),
    FormulaDerivation(formulaName: "Lens Formula", expression: "1/v − 1/u = 1/f", derivationSteps: [
      "For a spherical lens, u is the object distance, v is the image distance, and f is the focal length, all measured from the optical centre.",
      "Using ray diagrams and similar triangles, the relation is derived as 1/v − 1/u = 1/f.",
    ]),
    FormulaDerivation(formulaName: "Power of a Lens", expression: "P = 1/f (f in metres)", derivationSteps: [
      "The power of a lens is defined as the reciprocal of its focal length.",
      "P = 1/f, where f is measured in metres and P is in dioptres (D).",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "lr1", question: "A mirror that curves inward, like the inside of a spoon, is called a [ concave mirror / convex mirror ].", answer: "concave mirror"),
    QuestionItem(id: "lr2", question: "A mirror that curves outward is called a [ convex mirror / concave mirror ].", answer: "convex mirror"),
    QuestionItem(id: "lr3", question: "The distance between the pole and the focus of a spherical mirror is called its [ focal length / radius of curvature ].", answer: "focal length"),
    QuestionItem(id: "lr4", question: "A concave mirror used by dentists to see a magnified image of teeth forms a [ virtual, magnified image / real, diminished image ] when the object is close.", answer: "virtual, magnified image"),
    QuestionItem(id: "lr5", question: "Convex mirrors are used as rear-view mirrors in vehicles because they give a [ wider field of view / magnified image ].", answer: "wider field of view"),
    QuestionItem(id: "lr6", question: "The bending of light as it passes from one transparent medium to another is called [ refraction / reflection ].", answer: "refraction"),
    QuestionItem(id: "lr7", question: "A lens that is thicker in the middle than at the edges is called a [ convex lens / concave lens ].", answer: "convex lens"),
    QuestionItem(id: "lr8", question: "A lens that is thinner in the middle than at the edges is called a [ concave lens / convex lens ].", answer: "concave lens"),
    QuestionItem(id: "lr9", question: "A convex lens is also known as a [ converging lens / diverging lens ] because it converges light rays.", answer: "converging lens"),
    QuestionItem(id: "lr10", question: "A concave lens is also known as a [ diverging lens / converging lens ] because it spreads light rays apart.", answer: "diverging lens"),
    QuestionItem(id: "lr11", question: "The ability of a lens to converge or diverge light rays is called its [ power / focal length ].", answer: "power"),
    QuestionItem(id: "lr12", question: "The SI unit of the power of a lens is the [ dioptre / metre ].", answer: "dioptre"),
    QuestionItem(id: "lr13", question: "The power of a convex lens is [ positive / negative ].", answer: "positive"),
    QuestionItem(id: "lr14", question: "The power of a concave lens is [ negative / positive ].", answer: "negative"),
    QuestionItem(id: "lr15", question: "Power of a lens is calculated as the reciprocal of its [ focal length in metres / radius of curvature ].", answer: "focal length in metres"),
  ],
  numericalProblems: [
    NumericalProblem(id: "lrn1", question: "Find the power of a convex lens with focal length 0.5 m.", given: ["f = 0.5 m"], solutionSteps: ["P = 1/f", "= 1/0.5", "= 2 D"], numericAnswer: 2, unit: "D"),
    NumericalProblem(id: "lrn2", question: "Find the power of a concave lens with focal length 25 cm.", given: ["f = -25 cm = -0.25 m"], solutionSteps: ["P = 1/f", "= 1/(-0.25)", "= -4 D"], numericAnswer: -4, unit: "D"),
    NumericalProblem(id: "lrn3", question: "Find the focal length of a lens with power +2.5 D.", given: ["P = 2.5 D"], solutionSteps: ["f = 1/P", "= 1/2.5", "= 0.4 m"], numericAnswer: 0.4, unit: "m"),
    NumericalProblem(id: "lrn4", question: "An object is placed 30 cm from a convex lens of focal length 10 cm. Find the image distance using the lens formula (u = -30 cm).", given: ["u = -30 cm", "f = 10 cm"], solutionSteps: ["1/v − 1/u = 1/f", "1/v = 1/f + 1/u = 1/10 + (-1/30) = 3/30 - 1/30 = 2/30", "v = 15 cm"], numericAnswer: 15, unit: "cm"),
    NumericalProblem(id: "lrn5", question: "An object is placed 20 cm in front of a concave mirror of focal length 15 cm. Find the image distance (u=-20, f=-15).", given: ["u = -20 cm", "f = -15 cm"], solutionSteps: ["1/v + 1/u = 1/f", "1/v = 1/f − 1/u = -1/15 − (-1/20) = -4/60+3/60 = -1/60", "v = -60 cm"], numericAnswer: -60, unit: "cm"),
    NumericalProblem(id: "lrn6", question: "Find the power of a lens needed for a focal length of -0.2 m.", given: ["f = -0.2 m"], solutionSteps: ["P = 1/f", "= 1/(-0.2)", "= -5 D"], numericAnswer: -5, unit: "D"),
    NumericalProblem(id: "lrn7", question: "Find the focal length of a lens whose power is -2 D.", given: ["P = -2 D"], solutionSteps: ["f = 1/P", "= 1/(-2)", "= -0.5 m"], numericAnswer: -0.5, unit: "m"),
    NumericalProblem(id: "lrn8", question: "Two thin lenses of power +3D and +2D are placed in contact. Find the combined power.", given: ["P1 = 3 D", "P2 = 2 D"], solutionSteps: ["Combined power = P1 + P2", "= 3+2", "= 5 D"], numericAnswer: 5, unit: "D"),
    NumericalProblem(id: "lrn9", question: "An object is placed 15 cm from a convex mirror of focal length 10 cm. Find the image distance using the mirror formula (u=-15, f=+10).", given: ["u = -15 cm", "f = 10 cm"], solutionSteps: ["1/v + 1/u = 1/f", "1/v = 1/10 − (-1/15) = 1/10+1/15 = 3/30+2/30 = 5/30", "v = 6 cm"], numericAnswer: 6, unit: "cm"),
  ],
);
