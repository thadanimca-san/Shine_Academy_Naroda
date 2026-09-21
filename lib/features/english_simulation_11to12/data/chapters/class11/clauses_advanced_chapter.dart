import '../../../models/chapter_model.dart';

final class11ClausesAdvancedChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_clausesadvanced", chapterName: "Clauses (Advanced Practice)",
  formulas: [],
  concepts: [
    "A clause is a group of words with its own subject and finite verb; a main clause can stand alone, while a subordinate clause depends on it.",
    "A noun clause functions as a subject, object, or complement and can be introduced by 'that', a wh-word, or 'whether/if'.",
    "An adjective clause modifies a noun or pronoun and is usually introduced by a relative pronoun ('who', 'which', 'that') or relative adverb ('where', 'when').",
    "An adverb clause modifies a verb, adjective, or adverb and shows relationships of time, reason, condition, purpose, contrast, or manner.",
    "Recognising the function of the clause within the sentence (not just the linking word) is essential to correctly classify it.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'In "I know that he is innocent," the clause "that he is innocent" is a(n) [ noun / adjective ] clause.', answer: 'noun'),
    QuestionItem(id: 'q2', question: 'In "The house which stands on the hill is old," the clause is a(n) [ adjective / adverb ] clause.', answer: 'adjective'),
    QuestionItem(id: 'q3', question: 'In "He will succeed if he works hard," the clause "if he works hard" shows [ condition / reason ].', answer: 'condition'),
    QuestionItem(id: 'q4', question: 'In "She spoke as if she knew everything," the clause shows [ manner / purpose ].', answer: 'manner'),
    QuestionItem(id: 'q5', question: 'In "Whoever comes first will win the prize," the clause "Whoever comes first" functions as the [ subject / object ].', answer: 'subject'),
    QuestionItem(id: 'q6', question: 'In "He ran so fast that he caught the bus," the clause shows [ result / condition ].', answer: 'result'),
    QuestionItem(id: 'q7', question: 'In "This is the reason why he resigned," the clause "why he resigned" is a(n) [ adjective / noun ] clause modifying "reason".', answer: 'adjective'),
    QuestionItem(id: 'q8', question: 'In "Although it was raining, they went out," the clause shows a relationship of [ contrast / time ].', answer: 'contrast'),
    QuestionItem(id: 'q9', question: 'A subordinate clause [ cannot / can ] stand alone as a complete sentence.', answer: 'cannot'),
    QuestionItem(id: 'q10', question: 'In "He saved money so that he could buy a car," the clause shows [ purpose / result ].', answer: 'purpose'),
  ],
);
