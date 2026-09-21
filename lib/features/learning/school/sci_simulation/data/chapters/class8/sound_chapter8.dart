import '../../../models/chapter_model.dart';
final ChapterModel class8SoundChapter = ChapterModel(
  standard: 8, subject: "Physics", chapterId: "cls8_phys_sound", chapterName: "Bonus: Sound",
  concepts: ["Sound is produced by vibrating objects and needs a medium to travel.", "Amplitude, time period and frequency of vibration.", "Audible range, noise vs music, and noise pollution."],
  formulas: [
    FormulaDerivation(formulaName: "Frequency and Time Period", expression: "f = 1/T", derivationSteps: [
      "The time period T is the time taken to complete one full vibration.",
      "Frequency is the number of vibrations per second.",
      "So frequency f = 1/T, where T is measured in seconds.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "s8_1", question: "Sound is produced by a [ vibrating / stationary ] object.", answer: "vibrating"),
    QuestionItem(id: "s8_2", question: "Sound needs a [ medium / vacuum ] to travel from one place to another.", answer: "medium"),
    QuestionItem(id: "s8_3", question: "In human beings, sound is produced by the voice box, also known as the [ larynx / pharynx ].", answer: "larynx"),
    QuestionItem(id: "s8_4", question: "Two bands of tissue stretched across the voice box that vibrate to produce sound are called [ vocal cords / eardrums ].", answer: "vocal cords"),
    QuestionItem(id: "s8_5", question: "The to and fro motion of an object is called its [ vibration / rotation ].", answer: "vibration"),
    QuestionItem(id: "s8_6", question: "The number of vibrations per second is called the [ frequency / amplitude ].", answer: "frequency"),
    QuestionItem(id: "s8_7", question: "Frequency is measured in the unit [ hertz (Hz) / decibel (dB) ].", answer: "hertz (Hz)"),
    QuestionItem(id: "s8_8", question: "The maximum displacement of a vibrating object from its rest position is called the [ amplitude / time period ].", answer: "amplitude"),
    QuestionItem(id: "s8_9", question: "The time taken to complete one full vibration is called the [ time period / frequency ].", answer: "time period"),
    QuestionItem(id: "s8_10", question: "A larger amplitude of vibration produces a [ louder / softer ] sound.", answer: "louder"),
    QuestionItem(id: "s8_11", question: "A higher frequency of vibration produces a sound of [ higher pitch / lower pitch ].", answer: "higher pitch"),
    QuestionItem(id: "s8_12", question: "Sound that is pleasant to hear is called [ music / noise ].", answer: "music"),
    QuestionItem(id: "s8_13", question: "Unpleasant or unwanted sound is called [ noise / music ].", answer: "noise"),
    QuestionItem(id: "s8_14", question: "Excessive and unwanted sound in the environment causing discomfort is called [ noise pollution / air pollution ].", answer: "noise pollution"),
    QuestionItem(id: "s8_15", question: "The audible range of frequency for the human ear is [ 20 Hz to 20,000 Hz / 1 Hz to 100 Hz ].", answer: "20 Hz to 20,000 Hz"),
  ],
  numericalProblems: [
    NumericalProblem(id: "s8n1", question: "A vibrating object completes 50 oscillations in 10 seconds. Find its frequency.", given: ["Oscillations = 50", "Time = 10 s"], solutionSteps: ["Frequency = oscillations/time", "= 50/10", "= 5 Hz"], numericAnswer: 5, unit: "Hz"),
    NumericalProblem(id: "s8n2", question: "A tuning fork has a time period of 0.005 s. Find its frequency.", given: ["T = 0.005 s"], solutionSteps: ["f = 1/T", "= 1/0.005", "= 200 Hz"], numericAnswer: 200, unit: "Hz"),
    NumericalProblem(id: "s8n3", question: "A source vibrates at 100 Hz. Find its time period.", given: ["f = 100 Hz"], solutionSteps: ["T = 1/f", "= 1/100", "= 0.01 s"], numericAnswer: 0.01, unit: "s"),
    NumericalProblem(id: "s8n4", question: "A pendulum makes 30 vibrations in 15 seconds. Find its frequency.", given: ["Vibrations = 30", "Time = 15 s"], solutionSteps: ["Frequency = vibrations/time", "= 30/15", "= 2 Hz"], numericAnswer: 2, unit: "Hz"),
    NumericalProblem(id: "s8n5", question: "A source has a frequency of 50 Hz. Find the number of vibrations it makes in 8 seconds.", given: ["f = 50 Hz", "t = 8 s"], solutionSteps: ["Number of vibrations = f × t", "= 50×8", "= 400"], numericAnswer: 400, unit: ""),
  ],
);
