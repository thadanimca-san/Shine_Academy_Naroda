import '../../../models/chapter_model.dart';

final class12ModalsBoardChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_modalsboard", chapterName: "Modals (Board Level)",
  formulas: [],
  concepts: [
    "Board-level modal questions often appear within gap-filling or editing passages, testing the ability to select the modal that matches the intended meaning precisely.",
    "'Can'/'could' express ability; 'may'/'might' express possibility or formal permission; 'must'/'have to' express obligation or necessity.",
    "'Would' is used for polite requests, habitual past actions, and the main clause of unreal conditionals.",
    "Perfect modals ('could have', 'would have', 'must have' + past participle) describe unrealised possibilities or confident deductions about the past.",
    "'Shall' is used in formal offers and suggestions ('Shall we begin?') and in first-person future statements in formal registers.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'If I had studied harder, I ___ passed the exam. [ would have / would ]', answer: 'would have'),
    QuestionItem(id: 'q2', question: '___ we begin the meeting now? [ Shall / Will ]', answer: 'Shall'),
    QuestionItem(id: 'q3', question: 'When I was a child, I ___ swim for hours. [ could / can ]', answer: 'could'),
    QuestionItem(id: 'q4', question: 'You ___ finish this report by Friday; it is mandatory. [ have to / may ]', answer: 'have to'),
    QuestionItem(id: 'q5', question: 'He ___ have taken the wrong road; he is very late. [ must / can ]', answer: 'must'),
    QuestionItem(id: 'q6', question: '___ you please pass the salt? [ Would / Shall ]', answer: 'Would'),
    QuestionItem(id: 'q7', question: 'She ___ have called before visiting; it was rude of her not to. [ should / would ]', answer: 'should'),
    QuestionItem(id: 'q8', question: 'They ___ have won the match if they had played better. [ could / can ]', answer: 'could'),
    QuestionItem(id: 'q9', question: '___ I use your phone for a moment? [ May / Must ]', answer: 'May'),
    QuestionItem(id: 'q10', question: 'You ___ not worry about the results; you did your best. [ need / must ]', answer: 'need'),
  ],
);
