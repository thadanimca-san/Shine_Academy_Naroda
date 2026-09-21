import '../../../models/chapter_model.dart';
final ChapterModel class8StarsSolarSystemChapter = ChapterModel(
  standard: 8, subject: "Physics", chapterId: "cls8_phys_starssolarsystem", chapterName: "Bonus: Stars and the Solar System",
  concepts: ["The Moon's surface and phases.", "Stars and constellations.", "The Solar System: planets, and other members like asteroids and comets."],
  formulas: [
    FormulaDerivation(formulaName: "Light Year", expression: "1 light year = speed of light × 1 year", derivationSteps: [
      "A light year is the distance light travels in one year, used to measure huge distances in space.",
      "Speed of light ≈ 3 × 10⁵ km/s, and there are about 3.15 × 10⁷ seconds in a year.",
      "So 1 light year ≈ 3×10⁵ × 3.15×10⁷ ≈ 9.46 × 10¹² km.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "ss1", question: "The natural satellite of the Earth is the [ Moon / Sun ].", answer: "Moon"),
    QuestionItem(id: "ss2", question: "The different shapes of the bright part of the Moon seen on different days are called the [ phases of the Moon / eclipses ].", answer: "phases of the Moon"),
    QuestionItem(id: "ss3", question: "A group of stars that appears to form a recognisable pattern is called a [ constellation / galaxy ].", answer: "constellation"),
    QuestionItem(id: "ss4", question: "The constellation also known as the Great Bear is [ Ursa Major / Orion ].", answer: "Ursa Major"),
    QuestionItem(id: "ss5", question: "The star that indicates the direction of the North is the [ Pole Star (Dhruva Tara) / Sirius ].", answer: "Pole Star (Dhruva Tara)"),
    QuestionItem(id: "ss6", question: "The hunter-shaped constellation visible mainly in winter is [ Orion / Cassiopeia ].", answer: "Orion"),
    QuestionItem(id: "ss7", question: "The huge system of stars, gases and dust held together by gravity is called a [ galaxy / constellation ].", answer: "galaxy"),
    QuestionItem(id: "ss8", question: "Our solar system is located in the galaxy called the [ Milky Way / Andromeda ].", answer: "Milky Way"),
    QuestionItem(id: "ss9", question: "The family of the Sun, consisting of planets and other celestial bodies orbiting it, is called the [ Solar System / Universe ].", answer: "Solar System"),
    QuestionItem(id: "ss10", question: "The planet closest to the Sun is [ Mercury / Venus ].", answer: "Mercury"),
    QuestionItem(id: "ss11", question: "The largest planet in the solar system is [ Jupiter / Saturn ].", answer: "Jupiter"),
    QuestionItem(id: "ss12", question: "The planet known for its prominent ring system is [ Saturn / Uranus ].", answer: "Saturn"),
    QuestionItem(id: "ss13", question: "Small rocky bodies that orbit the Sun, mostly found between Mars and Jupiter, are called [ asteroids / comets ].", answer: "asteroids"),
    QuestionItem(id: "ss14", question: "A celestial body made of ice, dust and gas that develops a glowing tail as it nears the Sun is called a [ comet / meteor ].", answer: "comet"),
    QuestionItem(id: "ss15", question: "A small piece of rock that burns up upon entering Earth's atmosphere, appearing as a shooting star, is called a [ meteor / meteorite ].", answer: "meteor"),
  ],
  numericalProblems: [
    NumericalProblem(id: "ssn1", question: "Light from the Sun takes about 8 minutes to reach Earth. Convert this to seconds.", given: ["Time = 8 minutes"], solutionSteps: ["Seconds = minutes × 60", "= 8×60", "= 480 s"], numericAnswer: 480, unit: "s"),
    NumericalProblem(id: "ssn2", question: "The Moon is about 384,400 km from Earth. If light travels at 300,000 km/s, find the time light takes to reach us from the Moon (in seconds, rounded to 2 decimals).", given: ["Distance = 384400 km", "Speed = 300000 km/s"], solutionSteps: ["Time = distance/speed", "= 384400/300000", "≈ 1.28 s"], numericAnswer: 1.28, unit: "s"),
    NumericalProblem(id: "ssn3", question: "A star is 4 light years away. If 1 light year ≈ 9.46×10¹² km, find the distance in km.", given: ["Distance = 4 light years"], solutionSteps: ["Distance = 4 × 9.46×10¹²", "≈ 3.784×10¹³ km"], numericAnswer: 3.784e13, unit: "km"),
    NumericalProblem(id: "ssn4", question: "Earth takes 365 days to orbit the Sun once. Find how many days it takes to complete 3 orbits.", given: ["1 orbit = 365 days", "3 orbits"], solutionSteps: ["Total days = 365 × 3", "= 1095 days"], numericAnswer: 1095, unit: "days"),
  ],
);
