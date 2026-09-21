import '../../../models/chapter_model.dart';

final class12ReportedSpeechBoardChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_reportedspeechboard", chapterName: "Reported Speech (Board Level, Mixed)",
  formulas: [],
  concepts: [
    "Board-level reported speech questions mix statements, questions, commands, requests, and exclamations within the same exercise set.",
    "Tense backshift, pronoun change, and time/place-word changes must all be applied together and consistently.",
    "Reporting verbs must match the sentence type: 'said/told' for statements, 'asked' for questions, 'ordered/requested' for commands, 'exclaimed with joy/sorrow' for exclamations.",
    "If the reporting verb is in the present tense ('says', 'has said'), no backshift of tense is required in the reported clause.",
    "Modals shift predictably in reported speech: 'will'→'would', 'can'→'could', 'may'→'might', 'must'→'had to' (for obligation).",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'He said, "I can finish this today." → He said that he ___ finish it that day. [ could / can ]', answer: 'could'),
    QuestionItem(id: 'q2', question: 'She says, "I am happy." → She says that she ___ happy. [ is / was ]', answer: 'is'),
    QuestionItem(id: 'q3', question: 'The manager said, "You must submit the report today." → The manager said that I ___ submit the report that day. [ had to / must ]', answer: 'had to'),
    QuestionItem(id: 'q4', question: 'He asked, "Did you complete the assignment?" → He asked me ___ I had completed the assignment. [ if / that ]', answer: 'if'),
    QuestionItem(id: 'q5', question: 'She exclaimed, "How beautiful the sunset is!" → She exclaimed ___ that the sunset was very beautiful. [ with delight / with sorrow ]', answer: 'with delight'),
    QuestionItem(id: 'q6', question: 'The teacher said, "Keep quiet, boys." → The teacher ordered the boys ___ quiet. [ to keep / keep ]', answer: 'to keep'),
    QuestionItem(id: 'q7', question: 'He said, "I have finished my work." → He said that he ___ finished his work. [ had / has ]', answer: 'had'),
    QuestionItem(id: 'q8', question: 'She said to him, "Please help me." → She requested him ___ help her. [ to / that he ]', answer: 'to'),
    QuestionItem(id: 'q9', question: 'He asked, "What is your name?" → He asked me what ___ name was. [ my / his ]', answer: 'my'),
    QuestionItem(id: 'q10', question: 'They said, "We will visit tomorrow." → They said that they ___ visit the next day. [ would / will ]', answer: 'would'),
  ],
);
