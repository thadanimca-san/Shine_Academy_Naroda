import '../../../models/chapter_model.dart';

final class12EditingOmissionBoardChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_editingomissionboard", chapterName: "Editing and Omission (Board Level)",
  formulas: [],
  concepts: [
    "Board-level editing passages present a short text with one incorrect word per line, to be identified and corrected.",
    "Omission passages present a short text with one word missing per line, to be identified and supplied.",
    "High-frequency error areas at board level: verb tense/form, prepositions, articles, subject-verb agreement, and degrees of comparison.",
    "Always read at least the full sentence — and ideally the surrounding sentences — before deciding on a correction, since context often determines the right word.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Incorrect: "He has went to the market." Correction: "He has [ gone / went ] to the market."', answer: 'gone'),
    QuestionItem(id: 'q2', question: 'Missing word: "She is responsible the mistake." Correct: "She is responsible [ for / of ] the mistake."', answer: 'for'),
    QuestionItem(id: 'q3', question: 'Incorrect: "One of the boys were late." Correction: "One of the boys [ was / were ] late."', answer: 'was'),
    QuestionItem(id: 'q4', question: 'Missing word: "He is not aware the risks." Correct: "He is not aware [ of / for ] the risks."', answer: 'of'),
    QuestionItem(id: 'q5', question: 'Incorrect: "This is the most unique idea." Correction: "This is a [ unique / most unique ] idea."', answer: 'unique'),
    QuestionItem(id: 'q6', question: 'Missing word: "They congratulated him his success." Correct: "They congratulated him [ on / for ] his success."', answer: 'on'),
    QuestionItem(id: 'q7', question: 'Incorrect: "The news were shocking." Correction: "The news [ was / were ] shocking."', answer: 'was'),
    QuestionItem(id: 'q8', question: 'Missing word: "He is deprived his rights." Correct: "He is deprived [ of / from ] his rights."', answer: 'of'),
    QuestionItem(id: 'q9', question: 'Incorrect: "She has been suffering from fever since three days." Correction: "She has been suffering from fever [ for / since ] three days."', answer: 'for'),
    QuestionItem(id: 'q10', question: 'Missing word: "He is entitled a refund." Correct: "He is entitled [ to / for ] a refund."', answer: 'to'),
  ],
);
