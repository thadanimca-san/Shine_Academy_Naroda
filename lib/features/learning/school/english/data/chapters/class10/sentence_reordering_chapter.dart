import '../../../models/chapter_model.dart';

final class10SentenceReorderingChapter = ChapterModel(
  standard: 10, subject: "English", chapterId: "cls10_eng_sentencereordering", chapterName: "Sentence Reordering (Jumbled Words)",
  formulas: [],
  concepts: [
    "Sentence reordering tests the ability to arrange jumbled words or phrases into a grammatically correct and meaningful sentence.",
    "The subject usually comes first in a simple declarative sentence, followed by the verb and then the object.",
    "Question words (wh-words) or auxiliary verbs typically begin interrogative sentences.",
    "Look for capitalisation and punctuation cues — a capitalised word often marks the start, and a full stop marks the end.",
    "Conjunctions and linking words help identify how clauses should be joined.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Jumbled: "playground / children / the / in / are / playing" → The correct first word is [ The / Children ].', answer: 'The'),
    QuestionItem(id: 'q2', question: '"quickly / she / ran / home" correctly orders as "She ran home [ quickly / she ]".', answer: 'quickly'),
    QuestionItem(id: 'q3', question: 'In "book / this / is / interesting / very", the correct sentence begins with [ This / Book ].', answer: 'This'),
    QuestionItem(id: 'q4', question: 'A jumbled interrogative sentence usually begins with a [ wh-word or auxiliary / adjective ].', answer: 'wh-word or auxiliary'),
    QuestionItem(id: 'q5', question: '"to / school / walks / he / every day" correctly ends with [ every day / walks ].', answer: 'every day'),
    QuestionItem(id: 'q6', question: 'In a simple declarative sentence, the [ subject / object ] usually comes first.', answer: 'subject'),
    QuestionItem(id: 'q7', question: '"garden / beautiful / a / is / this" correctly orders as "This is a beautiful [ garden / this ]".', answer: 'garden'),
    QuestionItem(id: 'q8', question: 'The word that typically ends a declarative sentence is followed by a [ full stop / comma ].', answer: 'full stop'),
    QuestionItem(id: 'q9', question: '"fast / cheetah / runs / the / very" correctly orders as "The cheetah runs very [ fast / cheetah ]".', answer: 'fast'),
    QuestionItem(id: 'q10', question: 'In "will / come / tomorrow / she", the correct order places the subject "she" [ first / last ].', answer: 'first'),
    QuestionItem(id: 'q11', question: '"door / please / the / close" correctly orders as "Please close the [ door / please ]".', answer: 'door'),
    QuestionItem(id: 'q12', question: 'A capitalised word in a jumbled set is usually a clue for the [ first word / last word ] of the sentence.', answer: 'first word'),
    QuestionItem(id: 'q13', question: '"letter / wrote / a / she / yesterday" correctly orders as "She wrote a letter [ yesterday / she ]".', answer: 'yesterday'),
    QuestionItem(id: 'q14', question: 'In "must / homework / you / finish / your", the modal verb "must" comes [ after the subject / before the subject ].', answer: 'after the subject'),
    QuestionItem(id: 'q15', question: '"river / flows / the / slowly" correctly orders as "The river flows [ slowly / the ]".', answer: 'slowly'),
  ],
);
