import '../../../models/chapter_model.dart';
final ChapterModel class7ElectricCurrentEffectsChapter = ChapterModel(
  standard: 7, subject: "Physics", chapterId: "cls7_phys_electriccurrenteffects", chapterName: "Electric Current and its Effects",
  concepts: ["Symbols of electric components and circuit diagrams.", "Heating and magnetic effects of electric current.", "Electromagnets and electric bell."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ec1", question: "A simple diagram representing an electric circuit using symbols is called a [ circuit diagram / block diagram ].", answer: "circuit diagram"),
    QuestionItem(id: "ec2", question: "A device used to break or complete an electric circuit is called a [ switch / cell ].", answer: "switch"),
    QuestionItem(id: "ec3", question: "The heating effect of electric current is used in appliances such as an [ electric iron / torch ].", answer: "electric iron"),
    QuestionItem(id: "ec4", question: "The heating effect of current occurs because a wire has [ electrical resistance / no resistance ].", answer: "electrical resistance"),
    QuestionItem(id: "ec5", question: "The element inside an electric bulb that glows and produces light is called the [ filament / switch ].", answer: "filament"),
    QuestionItem(id: "ec6", question: "The filament of an electric bulb is usually made of [ tungsten / copper ], which has a very high melting point.", answer: "tungsten"),
    QuestionItem(id: "ec7", question: "A safety device that melts and breaks the circuit when too much current flows is called a [ fuse / switch ].", answer: "fuse"),
    QuestionItem(id: "ec8", question: "An electric current flowing through a wire creates a [ magnetic effect / gravitational effect ] around it.", answer: "magnetic effect"),
    QuestionItem(id: "ec9", question: "A coil of insulated wire wound around a piece of iron that becomes magnetic when current flows is called an [ electromagnet / permanent magnet ].", answer: "electromagnet"),
    QuestionItem(id: "ec10", question: "An electromagnet's magnetism is [ temporary and can be switched off / permanent ], unlike a permanent magnet.", answer: "temporary and can be switched off"),
    QuestionItem(id: "ec11", question: "The device that uses the magnetic effect of current to produce sound in a ringing device is the [ electric bell / electric iron ].", answer: "electric bell"),
    QuestionItem(id: "ec12", question: "A device used to detect the presence of a small electric current using a magnetic compass needle is called a [ galvanometer / voltmeter ].", answer: "galvanometer"),
    QuestionItem(id: "ec13", question: "Electromagnets are used in [ electric bells and cranes / thermometers ].", answer: "electric bells and cranes"),
    QuestionItem(id: "ec14", question: "Devices that convert electrical energy into heat, like heaters, work on the [ heating effect of current / magnetic effect of current ].", answer: "heating effect of current"),
    QuestionItem(id: "ec15", question: "In a circuit diagram, a cell is represented by two parallel lines, one longer and one [ shorter / equal ].", answer: "shorter"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ecn1", question: "Four cells of 1.5 V each are connected in series in a torch. Find the total voltage.", given: ["4 cells × 1.5 V"], solutionSteps: ["Total voltage in series = number of cells × voltage per cell", "= 4 × 1.5", "= 6 V"], numericAnswer: 6, unit: "V"),
    NumericalProblem(id: "ecn2", question: "A battery pack needs to supply 9 V using 1.5 V cells connected in series. Find the number of cells required.", given: ["Total voltage = 9 V", "Each cell = 1.5 V"], solutionSteps: ["Number of cells = total voltage/voltage per cell", "= 9/1.5", "= 6 cells"], numericAnswer: 6, unit: "cells"),
    NumericalProblem(id: "ecn3", question: "Two cells of 1.5 V each are connected in series. Find the total voltage.", given: ["2 cells × 1.5 V"], solutionSteps: ["Total voltage = 2 × 1.5", "= 3 V"], numericAnswer: 3, unit: "V"),
    NumericalProblem(id: "ecn4", question: "A torch uses 3 cells in series, each rated 1.5 V. Find the total EMF supplied.", given: ["3 cells × 1.5 V"], solutionSteps: ["Total EMF = 3 × 1.5", "= 4.5 V"], numericAnswer: 4.5, unit: "V"),
  ],
);
