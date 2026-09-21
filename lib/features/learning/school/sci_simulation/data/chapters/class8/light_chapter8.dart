import '../../../models/chapter_model.dart';
final ChapterModel class8LightChapter = ChapterModel(
  standard: 8, subject: "Physics", chapterId: "cls8_phys_light", chapterName: "Bonus: Light",
  concepts: ["Reflection of light: laws of reflection.", "Regular and irregular (diffused) reflection.", "The human eye, and structure of the eye."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "lt1", question: "The bouncing back of light after striking a smooth polished surface is called [ reflection / refraction ].", answer: "reflection"),
    QuestionItem(id: "lt2", question: "The ray of light that falls on a mirror is called the [ incident ray / reflected ray ].", answer: "incident ray"),
    QuestionItem(id: "lt3", question: "The ray of light that bounces back from a mirror is called the [ reflected ray / incident ray ].", answer: "reflected ray"),
    QuestionItem(id: "lt4", question: "The line perpendicular to the mirror surface at the point of incidence is called the [ normal / tangent ].", answer: "normal"),
    QuestionItem(id: "lt5", question: "The angle between the incident ray and the normal is called the [ angle of incidence / angle of reflection ].", answer: "angle of incidence"),
    QuestionItem(id: "lt6", question: "According to the laws of reflection, the angle of incidence is [ equal to / greater than ] the angle of reflection.", answer: "equal to"),
    QuestionItem(id: "lt7", question: "Reflection from a smooth, polished surface producing a clear image is called [ regular reflection / diffused reflection ].", answer: "regular reflection"),
    QuestionItem(id: "lt8", question: "Reflection from a rough surface, scattering light in different directions, is called [ diffused (irregular) reflection / regular reflection ].", answer: "diffused (irregular) reflection"),
    QuestionItem(id: "lt9", question: "An image that cannot be obtained on a screen is called a [ virtual image / real image ].", answer: "virtual image"),
    QuestionItem(id: "lt10", question: "The image formed by a plane mirror is [ virtual, erect and laterally inverted / real and inverted ].", answer: "virtual, erect and laterally inverted"),
    QuestionItem(id: "lt11", question: "The transparent, curved front part of the human eye is called the [ cornea / retina ].", answer: "cornea"),
    QuestionItem(id: "lt12", question: "The screen at the back of the eye on which images are formed is called the [ retina / iris ].", answer: "retina"),
    QuestionItem(id: "lt13", question: "The coloured, muscular part of the eye that controls the size of the pupil is the [ iris / lens ].", answer: "iris"),
    QuestionItem(id: "lt14", question: "The opening in the iris through which light enters the eye is called the [ pupil / cornea ].", answer: "pupil"),
    QuestionItem(id: "lt15", question: "Light-sensitive cells in the retina send signals to the brain through the [ optic nerve / eyelid ].", answer: "optic nerve"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ltn1", question: "A ray of light strikes a mirror at an angle of incidence of 40°. Find the angle of reflection.", given: ["Angle of incidence = 40°"], solutionSteps: ["Angle of incidence = angle of reflection.", "Angle of reflection = 40°"], numericAnswer: 40, unit: "°"),
    NumericalProblem(id: "ltn2", question: "A ray of light strikes a mirror making an angle of 25° with the mirror surface. Find the angle of incidence from the normal.", given: ["Angle with surface = 25°"], solutionSteps: ["Angle of incidence = 90° − angle with surface", "= 90° − 25°", "= 65°"], numericAnswer: 65, unit: "°"),
    NumericalProblem(id: "ltn3", question: "If the angle between the incident ray and the reflected ray is 80°, find the angle of incidence.", given: ["Angle between rays = 80°"], solutionSteps: ["Since angle of incidence = angle of reflection, and together they make the angle between rays,", "Angle of incidence = 80°/2", "= 40°"], numericAnswer: 40, unit: "°"),
    NumericalProblem(id: "ltn4", question: "A ray of light hits a plane mirror perpendicular to its surface (angle of incidence = 0°). Find the angle of reflection.", given: ["Angle of incidence = 0°"], solutionSteps: ["Angle of reflection = angle of incidence", "= 0°"], numericAnswer: 0, unit: "°"),
  ],
);
