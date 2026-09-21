import '../../../models/chapter_model.dart';

final class12DeterminersBoardChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_determinersboard", chapterName: "Determiners (Board Level)",
  formulas: [],
  concepts: [
    "Board-level determiner questions are usually embedded in gap-filling passages, requiring context (not just the single sentence) to choose correctly.",
    "'The' is used for something specific or already mentioned; 'a/an' is used for something non-specific or mentioned for the first time.",
    "Quantifiers like 'some', 'any', 'much', 'many', 'a lot of' depend on whether the noun is countable/uncountable and on sentence type (affirmative/negative/question).",
    "'Such a/an' is used before a singular countable noun to express degree, while 'such' alone precedes plural or uncountable nouns.",
    "Distributives ('each', 'every', 'either', 'neither') always take singular verbs regardless of what follows them.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Is there ___ water left in the tank? [ any / some ]', answer: 'any'),
    QuestionItem(id: 'q2', question: 'There isn\'t ___ sugar in the jar. [ any / some ]', answer: 'any'),
    QuestionItem(id: 'q3', question: 'It was ___ interesting film that we watched it twice. [ such an / such a ]', answer: 'such an'),
    QuestionItem(id: 'q4', question: 'They are ___ kind people that everyone loves them. [ such / such a ]', answer: 'such'),
    QuestionItem(id: 'q5', question: '___ of the two roads leads to the station. [ Either / Both ]', answer: 'Either'),
    QuestionItem(id: 'q6', question: 'She has ___ money to spare after her expenses. [ little / few ]', answer: 'little'),
    QuestionItem(id: 'q7', question: 'We need ___ information before we proceed with the plan. [ more / many ]', answer: 'more'),
    QuestionItem(id: 'q8', question: 'He asked for ___ advice from his mentor. [ some / a ]', answer: 'some'),
    QuestionItem(id: 'q9', question: '___ citizen has the right to vote in this country. [ Every / All ]', answer: 'Every'),
    QuestionItem(id: 'q10', question: 'I saw an elephant at the zoo yesterday; ___ elephant was huge. [ the / a ]', answer: 'the'),
  ],
);
