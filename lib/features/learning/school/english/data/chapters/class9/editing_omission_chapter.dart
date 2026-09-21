import '../../../models/chapter_model.dart';

final class9EditingOmissionChapter = ChapterModel(
  standard: 9, subject: "English", chapterId: "cls9_eng_editingomission", chapterName: "Editing and Omission",
  formulas: [],
  concepts: [
    "Editing exercises test the ability to spot and correct a single wrong word in each line of a passage.",
    "Omission exercises test the ability to identify a missing word (often an article, preposition, auxiliary, or conjunction) and its correct position.",
    "Common errors include wrong verb forms, incorrect prepositions, missing articles, and subject-verb disagreement.",
    "Careful reading of each part of the sentence is essential to spot subtle grammar errors.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Incorrect: "He go to school daily." Correction: "He [ goes / going ] to school daily."', answer: 'goes'),
    QuestionItem(id: 'q2', question: 'Incorrect: "She is best student in class." Missing word: "She is [ the / a ] best student in class."', answer: 'the'),
    QuestionItem(id: 'q3', question: 'Incorrect: "He is fond in music." Correction: "He is fond [ of / in ] music."', answer: 'of'),
    QuestionItem(id: 'q4', question: 'Incorrect: "They was playing football." Correction: "They [ were / was ] playing football."', answer: 'were'),
    QuestionItem(id: 'q5', question: 'Missing word: "I have been living here 2010." Correct: "I have been living here [ since / from ] 2010."', answer: 'since'),
    QuestionItem(id: 'q6', question: 'Incorrect: "Each of the boys were present." Correction: "Each of the boys [ was / were ] present."', answer: 'was'),
    QuestionItem(id: 'q7', question: 'Missing word: "He is interested cricket." Correct: "He is interested [ in / on ] cricket."', answer: 'in'),
    QuestionItem(id: 'q8', question: 'Incorrect: "She don\'t like tea." Correction: "She [ doesn\'t / don\'t ] like tea."', answer: "doesn't"),
    QuestionItem(id: 'q9', question: 'Missing word: "I am waiting you." Correct: "I am waiting [ for / at ] you."', answer: 'for'),
    QuestionItem(id: 'q10', question: 'Incorrect: "He has went home." Correction: "He has [ gone / went ] home."', answer: 'gone'),
    QuestionItem(id: 'q11', question: 'Editing exercises usually involve correcting [ one / several ] word per line.', answer: 'one'),
    QuestionItem(id: 'q12', question: 'Missing word: "Neither of them ready." Correct: "Neither of them [ is / are ] ready."', answer: 'is'),
    QuestionItem(id: 'q13', question: 'Incorrect: "This is more better." Correction: "This is [ better / more better ]."', answer: 'better'),
    QuestionItem(id: 'q14', question: 'Missing word: "There is no reason it." Correct: "There is no reason [ for / of ] it."', answer: 'for'),
    QuestionItem(id: 'q15', question: 'Incorrect: "I amn\'t going." Correction: "I [ am not / amn\'t ] going."', answer: 'am not'),
  ],
);
