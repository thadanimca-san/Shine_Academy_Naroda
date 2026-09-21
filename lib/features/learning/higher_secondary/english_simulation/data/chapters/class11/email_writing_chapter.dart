import '../../../models/chapter_model.dart';

final class11EmailWritingChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_emailwriting", chapterName: "Email Writing",
  formulas: [],
  concepts: [
    "An email has a clear structure: recipient's address, a specific subject line, a salutation, a body, a closing, and the sender's name — even though it is sent digitally.",
    "A formal email (to a school, company, or authority) uses a professional tone, avoids abbreviations/emojis, and keeps the subject line precise and informative.",
    "An informal email (to friends or family) can be conversational and relaxed, similar to an informal letter, but still needs a clear subject line.",
    "The body of a formal email should be concise — state the purpose in the first line, add necessary details, and close with a clear request or expectation.",
    "Formal emails close with 'Regards' or 'Yours sincerely' followed by the sender's full name; informal emails may close with 'Best' or 'Take care'.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'The [ subject line / greeting ] of an email should be specific and informative, not vague.', answer: 'subject line'),
    QuestionItem(id: 'q2', question: 'A formal email should [ state the purpose in the first line / build up to the purpose slowly ].', answer: 'state the purpose in the first line'),
    QuestionItem(id: 'q3', question: 'Formal emails should generally avoid using [ emojis and casual abbreviations / complete sentences ].', answer: 'emojis and casual abbreviations'),
    QuestionItem(id: 'q4', question: 'A formal email to a school authority should close with [ "Regards" or "Yours sincerely" / "Bye!" ].', answer: '"Regards" or "Yours sincerely"'),
    QuestionItem(id: 'q5', question: 'An informal email to a friend can be [ conversational and relaxed / strictly formal in tone ].', answer: 'conversational and relaxed'),
    QuestionItem(id: 'q6', question: 'Even an informal email should include a [ clear subject line / long, dramatic introduction ].', answer: 'clear subject line'),
    QuestionItem(id: 'q7', question: 'A formal email requesting information should end with a [ clear, specific request / vague hope ].', answer: 'clear, specific request'),
    QuestionItem(id: 'q8', question: 'An email is different from a letter mainly in its [ mode of delivery, not its core structure / total absence of structure ].', answer: 'mode of delivery, not its core structure'),
    QuestionItem(id: 'q9', question: 'The sender\'s full name should appear [ at the end of the email, after the closing / only in the email address ].', answer: 'at the end of the email, after the closing'),
    QuestionItem(id: 'q10', question: 'A formal email should be kept [ concise and to the point / as long and detailed as possible ].', answer: 'concise and to the point'),
  ],
);
