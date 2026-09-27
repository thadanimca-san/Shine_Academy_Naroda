import '../../../models/chapter_model.dart';
final ChapterModel class10ApplicationsTrigonometryChapter = ChapterModel(
  standard: 10, subject: "Mathematics", chapterId: "cls10_math_applicationstrigonometry", chapterName: "Some Applications of Trigonometry",
  concepts: ["Height and distance problems using trigonometric ratios.", "Angle of elevation and angle of depression.", "Line of sight and horizontal level."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "at1", question: "The line drawn from the eye of an observer to the point being viewed is called the [ line of sight / horizontal line ].", answer: "line of sight"),
    QuestionItem(id: "at2", question: "The angle between the line of sight and the horizontal, when looking upward at an object, is called the [ angle of elevation / angle of depression ].", answer: "angle of elevation"),
    QuestionItem(id: "at3", question: "The angle between the line of sight and the horizontal, when looking downward at an object, is called the [ angle of depression / angle of elevation ].", answer: "angle of depression"),
    QuestionItem(id: "at4", question: "As the angle of elevation increases, the height of the object appears [ greater relative to the fixed distance / smaller ].", answer: "greater relative to the fixed distance"),
    QuestionItem(id: "at5", question: "In height and distance problems, we typically use trigonometric ratios in a [ right triangle / any triangle ].", answer: "right triangle"),
    QuestionItem(id: "at6", question: "The height of a tower can be found using tan θ = [ height/distance / distance/height ], where θ is the angle of elevation.", answer: "height/distance"),
    QuestionItem(id: "at7", question: "The angle of elevation of an object as seen from a point equals the angle of depression of that [ point as seen from the object / same point twice ].", answer: "point as seen from the object"),
    QuestionItem(id: "at8", question: "As an observer moves closer to the base of a tower, the angle of elevation [ increases / decreases ].", answer: "increases"),
  ],
  numericalProblems: [
    NumericalProblem(id: "atn1", question: "The angle of elevation of the top of a tower from a point 30 m away is 45°. Find the height of the tower.", given: ["distance = 30 m", "angle = 45°"], solutionSteps: ["tan 45° = height/distance", "1 = height/30", "height = 30 m"], numericAnswer: 30, unit: "m"),
    NumericalProblem(id: "atn2", question: "A tower is 20√3 m tall. Find the distance from its base to a point where the angle of elevation of the top is 30° (tan 30° = 1/√3).", given: ["height = 20√3 m", "angle = 30°"], solutionSteps: ["tan 30° = height/distance", "1/√3 = 20√3/distance", "distance = 20√3 × √3 = 60 m"], numericAnswer: 60, unit: "m"),
    NumericalProblem(id: "atn3", question: "From the top of a 60 m tall cliff, the angle of depression of a boat is 30°. Find the distance of the boat from the base of the cliff (tan 30° = 1/√3 ≈ 0.577).", given: ["height = 60 m", "angle = 30°"], solutionSteps: ["tan 30° = height/distance", "0.577 = 60/distance", "distance = 60/0.577 ≈ 103.98 m"], numericAnswer: 103.98, unit: "m"),
    NumericalProblem(id: "atn4", question: "The angle of elevation of the sun is 60°. Find the length of the shadow of a 15 m tall pole (tan 60° = √3 ≈ 1.732).", given: ["height = 15 m", "angle = 60°"], solutionSteps: ["tan 60° = height/shadow", "1.732 = 15/shadow", "shadow = 15/1.732 ≈ 8.66 m"], numericAnswer: 8.66, unit: "m"),
    NumericalProblem(id: "atn5", question: "A ladder makes an angle of 60° with the ground and its foot is 5 m from the wall. Find the height it reaches (tan 60° = √3 ≈ 1.732).", given: ["distance = 5 m", "angle = 60°"], solutionSteps: ["tan 60° = height/distance", "height = 5 × 1.732", "≈ 8.66 m"], numericAnswer: 8.66, unit: "m"),
    NumericalProblem(id: "atn6", question: "A tower stands 100 m from an observation point, with an angle of elevation of 45° to the top. Find the height of the tower.", given: ["distance = 100 m", "angle = 45°"], solutionSteps: ["tan 45° = height/distance", "1 = height/100", "height = 100 m"], numericAnswer: 100, unit: "m"),
    NumericalProblem(id: "atn7", question: "From a point 50 m from a building, the angle of elevation to the top is 60°. Find the height of the building (tan 60° ≈ 1.732).", given: ["distance = 50 m", "angle = 60°"], solutionSteps: ["tan 60° = height/distance", "height = 50 × 1.732", "≈ 86.6 m"], numericAnswer: 86.6, unit: "m"),
  ],
);
