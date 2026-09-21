import '../../../models/chapter_model.dart';
final ChapterModel class7WastewaterChapter = ChapterModel(
  standard: 7, subject: "Chemistry", chapterId: "cls7_chem_wastewater", chapterName: "Wastewater Story",
  concepts: ["Water used and contaminated by domestic and industrial activities is called wastewater.", "Sewage treatment plants and the steps of wastewater treatment.", "Better housekeeping practices to reduce water pollution."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "ww1", question: "Water that has become dirty after use in homes, industries and other places is called [ wastewater (sewage) / rainwater ].", answer: "wastewater (sewage)"),
    QuestionItem(id: "ww2", question: "The used water along with human excreta, released from homes and industries, is called [ sewage / potable water ].", answer: "sewage"),
    QuestionItem(id: "ww3", question: "The process of removing pollutants from wastewater before releasing it into water bodies is called [ sewage/wastewater treatment / evaporation ].", answer: "sewage/wastewater treatment"),
    QuestionItem(id: "ww4", question: "A facility where sewage is treated and cleaned before being released or reused is called a [ wastewater treatment plant / dam ].", answer: "wastewater treatment plant"),
    QuestionItem(id: "ww5", question: "The first step of wastewater treatment, where large floating objects are removed with a bar screen, is called [ screening / sedimentation ].", answer: "screening"),
    QuestionItem(id: "ww6", question: "The process where sand and grit settle at the bottom of a tank in wastewater treatment is called [ grit and sand removal / aeration ].", answer: "grit and sand removal"),
    QuestionItem(id: "ww7", question: "The step where suspended solid impurities settle down as sludge in a large tank is called [ sedimentation / screening ].", answer: "sedimentation"),
    QuestionItem(id: "ww8", question: "The partially cleared water left after sedimentation, before further treatment, is called [ clarified water / sludge ].", answer: "clarified water"),
    QuestionItem(id: "ww9", question: "The settled solid impurities collected at the bottom of a sedimentation tank are called [ sludge / effluent ].", answer: "sludge"),
    QuestionItem(id: "ww10", question: "Air is pumped into clarified water to help aerobic bacteria decompose organic waste; this step is called [ aeration / screening ].", answer: "aeration"),
    QuestionItem(id: "ww11", question: "Microorganisms used in wastewater treatment to break down human waste and other organic matter are called [ bacteria / algae only ].", answer: "bacteria"),
    QuestionItem(id: "ww12", question: "Dried sludge can be used as [ manure / drinking water ] since it is rich in nutrients.", answer: "manure"),
    QuestionItem(id: "ww13", question: "Substances that should never be released into a drain, since they clog pipes and pollute water, include [ oil, fat, and chemicals / paper only ].", answer: "oil, fat, and chemicals"),
    QuestionItem(id: "ww14", question: "Releasing untreated sewage into rivers and lakes causes [ water pollution / water conservation ].", answer: "water pollution"),
    QuestionItem(id: "ww15", question: "Toilets that use very little or no water to dispose of human waste are called [ eco-friendly (low-flush) toilets / flush toilets only ].", answer: "eco-friendly (low-flush) toilets"),
  ],
  numericalProblems: [
    NumericalProblem(id: "wwn1", question: "A regular flush toilet uses 10 litres of water per flush. Find the water used for 5 flushes in a day.", given: ["10 L per flush", "5 flushes"], solutionSteps: ["Total water = 10 × 5", "= 50 litres"], numericAnswer: 50, unit: "litres"),
    NumericalProblem(id: "wwn2", question: "A family of 4 uses 150 litres of water per person per day. Find the total daily water usage of the family.", given: ["4 people", "150 L per person"], solutionSteps: ["Total = 4 × 150", "= 600 litres"], numericAnswer: 600, unit: "litres"),
    NumericalProblem(id: "wwn3", question: "A low-flush toilet uses only 4 litres per flush instead of 10 litres. Find the water saved over 5 flushes.", given: ["Saving per flush = 10-4 = 6 L", "5 flushes"], solutionSteps: ["Water saved = 6 × 5", "= 30 litres"], numericAnswer: 30, unit: "litres"),
    NumericalProblem(id: "wwn4", question: "A treatment plant processes 2000 litres of sewage per hour. Find the amount processed in 8 hours.", given: ["2000 L/hour", "8 hours"], solutionSteps: ["Total = 2000 × 8", "= 16000 litres"], numericAnswer: 16000, unit: "litres"),
  ],
);
