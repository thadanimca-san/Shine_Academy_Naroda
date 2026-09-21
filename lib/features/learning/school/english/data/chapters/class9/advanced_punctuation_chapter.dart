import '../../../models/chapter_model.dart';

final class9AdvancedPunctuationChapter = ChapterModel(
  standard: 9, subject: "English", chapterId: "cls9_eng_advancedpunctuation", chapterName: "Advanced Punctuation",
  formulas: [],
  concepts: [
    "A semicolon joins two closely related independent clauses without a coordinating conjunction.",
    "A colon introduces a list, explanation, or quotation.",
    "An apostrophe shows possession ('s) or marks a contraction (don't, it's).",
    "A hyphen joins compound words or word parts; a dash sets off an abrupt break in thought.",
    "Parentheses enclose extra, non-essential information within a sentence.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'I have finished my homework[ ; / , ] now I can relax.', answer: ';'),
    QuestionItem(id: 'q2', question: 'She bought the following items[ : / ; ] milk, bread and eggs.', answer: ':'),
    QuestionItem(id: 'q3', question: 'This is Rahul[ \'s / s\' ] book.', answer: "'s"),
    QuestionItem(id: 'q4', question: 'It[ \'s / s\' ] raining heavily outside.', answer: "'s"),
    QuestionItem(id: 'q5', question: 'My brother-in-law uses a [ hyphen / dash ] to join the compound word.', answer: 'hyphen'),
    QuestionItem(id: 'q6', question: 'The president—along with his cabinet—arrived on time, using a [ dash / colon ] to add extra emphasis.', answer: 'dash'),
    QuestionItem(id: 'q7', question: 'The report (published last year) confirms the findings, using [ parentheses / a semicolon ] for extra information.', answer: 'parentheses'),
    QuestionItem(id: 'q8', question: 'A [ semicolon / colon ] joins two closely related independent clauses without "and" or "but".', answer: 'semicolon'),
    QuestionItem(id: 'q9', question: 'For plural possessive nouns already ending in "s", we usually add only [ an apostrophe / apostrophe-s ], e.g. "students\' books".', answer: 'an apostrophe'),
    QuestionItem(id: 'q10', question: 'In direct speech, the full stop is placed [ inside / outside ] the closing quotation mark.', answer: 'inside'),
    QuestionItem(id: 'q11', question: 'We need three things[ : / ; ] courage, patience and hope.', answer: ':'),
    QuestionItem(id: 'q12', question: 'The children[ \'s / s\' ] playground was renovated last month.', answer: "'s"),
    QuestionItem(id: 'q13', question: 'I wanted to go; however[ , / ; ] it started raining.', answer: ','),
    QuestionItem(id: 'q14', question: 'A colon is often used to introduce a [ list / new paragraph ].', answer: 'list'),
    QuestionItem(id: 'q15', question: 'An apostrophe is used to mark a contraction such as [ "don\'t" / "dont" ].', answer: '"don\'t"'),
  ],
);
