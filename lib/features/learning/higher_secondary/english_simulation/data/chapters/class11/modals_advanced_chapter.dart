import '../../../models/chapter_model.dart';

final class11ModalsAdvancedChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_modalsadvanced", chapterName: "Modals (Advanced Usage)",
  formulas: [],
  concepts: [
    "Modal verbs express necessity, possibility, permission, ability, or obligation and are followed by the base form of the main verb.",
    "'Must' expresses strong obligation or logical certainty; 'should'/'ought to' express advice or moral obligation, which is weaker than 'must'.",
    "'May'/'might' express possibility or formal permission, with 'might' indicating a lower degree of certainty than 'may'.",
    "'Need not' expresses absence of obligation, distinct from 'must not', which expresses prohibition.",
    "Perfect modals ('should have', 'might have', 'must have' + past participle) refer to past possibilities, obligations, or deductions that did or did not happen.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'You [ must / need not ] wear a helmet while riding — it is the law.', answer: 'must'),
    QuestionItem(id: 'q2', question: 'You [ need not / must not ] come if you are busy; it is not compulsory.', answer: 'need not'),
    QuestionItem(id: 'q3', question: 'She [ should have / must have ] studied harder; she failed the exam.', answer: 'should have'),
    QuestionItem(id: 'q4', question: 'He is not in his office; he [ must have / should have ] gone home.', answer: 'must have'),
    QuestionItem(id: 'q5', question: '[ May / Must ] I come in, sir?', answer: 'May'),
    QuestionItem(id: 'q6', question: 'It [ might / must ] rain later, though the forecast is unclear.', answer: 'might'),
    QuestionItem(id: 'q7', question: 'You [ must not / need not ] smoke in this hospital — it is strictly prohibited.', answer: 'must not'),
    QuestionItem(id: 'q8', question: 'We [ ought to / need ] respect our elders.', answer: 'ought to'),
    QuestionItem(id: 'q9', question: 'He [ could / must ] speak French fluently when he lived in Paris.', answer: 'could'),
    QuestionItem(id: 'q10', question: 'They [ might have / should have ] missed the train; I am not sure.', answer: 'might have'),
  ],
);
