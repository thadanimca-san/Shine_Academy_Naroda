import '../../../models/chapter_model.dart';

final class10DialogueCompletionChapter = ChapterModel(
  standard: 10, subject: "English", chapterId: "cls10_eng_dialoguecompletion", chapterName: "Dialogue Completion",
  formulas: [],
  concepts: [
    "Dialogue completion tests the ability to supply a grammatically correct and contextually appropriate response within a conversation.",
    "Question forms and their expected answer forms must match — a yes/no question expects a yes/no-style answer, a wh-question expects specific information.",
    "Politeness markers (please, would you mind, could you) are common in formal dialogue completion.",
    "Tense and pronoun consistency must be maintained across both sides of the dialogue.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'A: "Would you like some tea?" B: "Yes, I ___ love some." [ would / will ]', answer: 'would'),
    QuestionItem(id: 'q2', question: 'A: "Could you help me with this?" B: "Sure, I ___ be happy to." [ would / will ]', answer: 'would'),
    QuestionItem(id: 'q3', question: 'A: "Have you finished your homework?" B: "Yes, I ___ finished it." [ have / has ]', answer: 'have'),
    QuestionItem(id: 'q4', question: 'A: "What time does the shop open?" B: "It ___ at nine." [ opens / open ]', answer: 'opens'),
    QuestionItem(id: 'q5', question: 'A: "Do you mind if I sit here?" B: "Not at all, please ___ ahead." [ go / going ]', answer: 'go'),
    QuestionItem(id: 'q6', question: 'A: "Where were you yesterday?" B: "I ___ at the library." [ was / am ]', answer: 'was'),
    QuestionItem(id: 'q7', question: 'A: "Will you be coming to the party?" B: "Yes, I ___." [ will / would ]', answer: 'will'),
    QuestionItem(id: 'q8', question: 'A: "How long have you lived here?" B: "I have lived here ___ ten years." [ for / since ]', answer: 'for'),
    QuestionItem(id: 'q9', question: 'A: "Excuse me, could you tell me the time, please?" B: "___, it is five o\'clock." [ Certainly / Certain ]', answer: 'Certainly'),
    QuestionItem(id: 'q10', question: 'A: "Is it going to rain today?" B: "It ___ , the sky is clear." [ doesn\'t look like it / isn\'t look ]', answer: "doesn't look like it"),
    QuestionItem(id: 'q11', question: 'A: "Why didn\'t you call me?" B: "I ___ my phone at home." [ had forgotten / forget ]', answer: 'had forgotten'),
    QuestionItem(id: 'q12', question: 'A: "Shall we meet at six?" B: "That ___ perfect for me." [ sounds / sound ]', answer: 'sounds'),
    QuestionItem(id: 'q13', question: 'A: "You look tired today." B: "Yes, I ___ well last night." [ didn\'t sleep / not sleep ]', answer: "didn't sleep"),
    QuestionItem(id: 'q14', question: 'A: "Can I borrow your pen?" B: "Of course, here ___ ." [ you are / you is ]', answer: 'you are'),
    QuestionItem(id: 'q15', question: 'A: "What do you think of the movie?" B: "I ___ it was excellent." [ think / thought ]', answer: 'think'),
  ],
);
