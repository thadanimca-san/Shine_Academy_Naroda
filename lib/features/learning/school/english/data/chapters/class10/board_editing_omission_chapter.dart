import '../../../models/chapter_model.dart';

final class10BoardEditingOmissionChapter = ChapterModel(
  standard: 10, subject: "English", chapterId: "cls10_eng_boardeditingomission", chapterName: "Editing and Omission (Board Level)",
  formulas: [],
  concepts: [
    "Board-level editing exercises test the ability to identify one incorrect word per line and supply the correction.",
    "Omission exercises test the ability to identify where a word is missing and what that word should be.",
    "Frequent error areas: verb forms, prepositions, articles, subject-verb agreement, and misuse of degrees of comparison.",
    "Always read the full sentence for meaning before deciding on a correction — errors are often not obvious from a single word alone.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Incorrect: "She always speak the truth." Correction: "She always [ speaks / speak ] the truth."', answer: 'speaks'),
    QuestionItem(id: 'q2', question: 'Incorrect: "He is best player in the team." Missing word: "He is [ the / a ] best player in the team."', answer: 'the'),
    QuestionItem(id: 'q3', question: 'Incorrect: "I am agree with you." Correction: "I [ agree / am agree ] with you."', answer: 'agree'),
    QuestionItem(id: 'q4', question: 'Incorrect: "There is many problems." Correction: "There [ are / is ] many problems."', answer: 'are'),
    QuestionItem(id: 'q5', question: 'Missing word: "He is capable doing it." Correct: "He is capable [ of / for ] doing it."', answer: 'of'),
    QuestionItem(id: 'q6', question: 'Incorrect: "She is senior than me." Correction: "She is senior [ to / than ] me."', answer: 'to'),
    QuestionItem(id: 'q7', question: 'Missing word: "He succeeded passing the test." Correct: "He succeeded [ in / at ] passing the test."', answer: 'in'),
    QuestionItem(id: 'q8', question: 'Incorrect: "This is more better than that." Correction: "This is [ better / more better ] than that."', answer: 'better'),
    QuestionItem(id: 'q9', question: 'Missing word: "He is junior me." Correct: "He is junior [ to / than ] me."', answer: 'to'),
    QuestionItem(id: 'q10', question: 'Incorrect: "The informations were useful." Correction: "The [ information / informations ] was useful."', answer: 'information'),
    QuestionItem(id: 'q11', question: 'Missing word: "I look forward hearing from you." Correct: "I look forward [ to / at ] hearing from you."', answer: 'to'),
    QuestionItem(id: 'q12', question: 'Incorrect: "He prevented me from going." Correction: "He prevented me [ from / of ] going." (this sentence is already correct — choose the matching preposition)', answer: 'from'),
    QuestionItem(id: 'q13', question: 'Missing word: "She is good English." Correct: "She is good [ at / in ] English."', answer: 'at'),
    QuestionItem(id: 'q14', question: 'Incorrect: "Neither of the answers were correct." Correction: "Neither of the answers [ was / were ] correct."', answer: 'was'),
    QuestionItem(id: 'q15', question: 'Missing word: "He apologised his mistake." Correct: "He apologised [ for / of ] his mistake."', answer: 'for'),
  ],
);
