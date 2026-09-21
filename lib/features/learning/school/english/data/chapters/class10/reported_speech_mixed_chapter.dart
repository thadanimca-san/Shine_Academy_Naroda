import '../../../models/chapter_model.dart';

final class10ReportedSpeechMixedChapter = ChapterModel(
  standard: 10, subject: "English", chapterId: "cls10_eng_reportedspeechmixed", chapterName: "Reported Speech: Mixed Practice",
  formulas: [],
  concepts: [
    "Board-level reported speech combines statements, questions, commands and exclamations within the same exercise set.",
    "Identify the sentence type first (statement, question, command, exclamation) before applying the correct reporting rule.",
    "Reporting verbs change to match the sentence type: 'said/told' for statements, 'asked' for questions, 'ordered/requested' for commands, 'exclaimed' for exclamations.",
    "Backshift of tense, pronoun change, and time/place changes apply consistently across all sentence types.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'He said, "I am busy right now." → He said that he ___ busy right then. [ was / is ]', answer: 'was'),
    QuestionItem(id: 'q2', question: 'She asked, "What is your favourite subject?" → She asked me what my favourite subject ___. [ was / is ]', answer: 'was'),
    QuestionItem(id: 'q3', question: 'The officer said, "Stop the car!" → The officer ordered them ___ the car. [ to stop / stop ]', answer: 'to stop'),
    QuestionItem(id: 'q4', question: 'She exclaimed, "What a lovely view!" → She exclaimed ___ joy that the view was lovely. [ with / in ]', answer: 'with'),
    QuestionItem(id: 'q5', question: 'He said, "I will finish it by tomorrow." → He said that he ___ finish it by the next day. [ would / will ]', answer: 'would'),
    QuestionItem(id: 'q6', question: 'She asked, "Are you free this evening?" → She asked me ___ I was free that evening. [ if / that ]', answer: 'if'),
    QuestionItem(id: 'q7', question: 'The teacher said, "Do not run in the corridor." → The teacher ordered us ___ run in the corridor. [ not to / to not ]', answer: 'not to'),
    QuestionItem(id: 'q8', question: 'He said, "Alas! I have lost my way." → He exclaimed ___ sorrow that he had lost his way. [ with / for ]', answer: 'with'),
    QuestionItem(id: 'q9', question: 'She said, "I bought this yesterday." → She said that she ___ that the day before. [ had bought / bought ]', answer: 'had bought'),
    QuestionItem(id: 'q10', question: 'He asked, "Where do you work?" → He asked me where I ___. [ worked / work ]', answer: 'worked'),
    QuestionItem(id: 'q11', question: 'She requested, "Please pass the salt." → She requested me ___ the salt. [ to pass / pass ]', answer: 'to pass'),
    QuestionItem(id: 'q12', question: 'A sentence that begins with a wh-word is reported using the same [ wh-word / conjunction ].', answer: 'wh-word'),
    QuestionItem(id: 'q13', question: 'He said, "I have never seen such beauty." → He said that he ___ never seen such beauty. [ had / has ]', answer: 'had'),
    QuestionItem(id: 'q14', question: 'She said, "This is not mine." → She said that ___ was not hers. [ that / this ]', answer: 'that'),
    QuestionItem(id: 'q15', question: 'He said, "Let us go for a walk." → He suggested ___ they go for a walk. [ that / to ]', answer: 'that'),
  ],
);
