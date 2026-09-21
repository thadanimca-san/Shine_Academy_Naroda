import '../../../models/chapter_model.dart';

final class12ClausesBoardChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_clausesboard", chapterName: "Clauses (Board Level)",
  formulas: [],
  concepts: [
    "Board-level clause questions test both identification (naming the clause type) and combination (joining simple sentences using an appropriate clause).",
    "Noun clauses can act as the subject, object, or complement of a sentence, and are introduced by 'that', a wh-word, or 'whether/if'.",
    "Adjective clauses are introduced by relative pronouns ('who', 'whom', 'whose', 'which', 'that') and immediately follow the noun they modify.",
    "Adverb clauses show relationships of time, place, reason, condition, purpose, result, contrast, or manner between the main and subordinate clause.",
    "Two simple sentences can often be combined into one complex sentence using an appropriate subordinating conjunction or relative pronoun.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'In "I wonder whether she will come," the clause "whether she will come" is a(n) [ noun / adverb ] clause.', answer: 'noun'),
    QuestionItem(id: 'q2', question: 'In "The man whose car was stolen filed a report," the clause is a(n) [ adjective / noun ] clause.', answer: 'adjective'),
    QuestionItem(id: 'q3', question: 'In "Wherever you go, I will follow," the clause shows [ place / time ].', answer: 'place'),
    QuestionItem(id: 'q4', question: 'Combine: "He is poor. He is honest." → He is poor [ though / because ] he is honest.', answer: 'though'),
    QuestionItem(id: 'q5', question: 'Combine: "She was tired. She kept working." → [ Although / Since ] she was tired, she kept working.', answer: 'Although'),
    QuestionItem(id: 'q6', question: 'In "I do not know where he lives," the clause "where he lives" functions as the [ object / subject ] of "know".', answer: 'object'),
    QuestionItem(id: 'q7', question: 'In "The reason that he gave was unconvincing," the clause "that he gave" is a(n) [ adjective / noun ] clause.', answer: 'adjective'),
    QuestionItem(id: 'q8', question: 'Combine: "He worked hard. He wanted to succeed." → He worked hard [ so that / although ] he could succeed.', answer: 'so that'),
    QuestionItem(id: 'q9', question: 'In "That she is talented is obvious," the clause "That she is talented" functions as the [ subject / object ].', answer: 'subject'),
    QuestionItem(id: 'q10', question: 'A relative clause immediately [ follows / precedes ] the noun it modifies.', answer: 'follows'),
  ],
);
