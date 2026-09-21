import '../../../models/chapter_model.dart';

final class12LetterWritingChapter = ChapterModel(
  standard: 12, subject: "English", chapterId: "cls12_eng_letterwriting", chapterName: "Letter Writing (Complaint, Enquiry, Order)",
  formulas: [],
  concepts: [
    "Board-level letter writing focuses on formal letters for practical purposes: complaint, enquiry, order, and application, each with a distinct communicative goal.",
    "A letter of complaint should state the issue clearly, provide evidence/reference (date, order number), and specify the remedy sought.",
    "A letter of enquiry should request specific, itemised information and specify why the information is needed if relevant.",
    "A letter of application (e.g. for a job or leave) should state the purpose clearly in the first paragraph and provide supporting details in the body.",
    "All formal letters follow the same structural skeleton: sender's address, date, receiver's address, subject line, salutation, body, complimentary close, and signature.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'A letter of complaint should specify the [ remedy sought (refund/replacement/action) / writer\'s general mood ].', answer: 'remedy sought (refund/replacement/action)'),
    QuestionItem(id: 'q2', question: 'A letter of enquiry should request [ specific, itemised information / a general chat ].', answer: 'specific, itemised information'),
    QuestionItem(id: 'q3', question: 'A letter of application should state its purpose [ clearly in the first paragraph / only in the closing line ].', answer: 'clearly in the first paragraph'),
    QuestionItem(id: 'q4', question: 'All formal letters begin with the [ sender\'s address and date / recipient\'s phone number ].', answer: "sender's address and date"),
    QuestionItem(id: 'q5', question: 'The [ subject line / postscript ] should briefly state the letter\'s purpose before the salutation.', answer: 'subject line'),
    QuestionItem(id: 'q6', question: 'A letter to a named recipient (e.g. "Dear Mr. Verma") should close with [ "Yours sincerely" / "Yours faithfully" ].', answer: 'Yours sincerely'),
    QuestionItem(id: 'q7', question: 'A complaint letter should reference the [ order or transaction details / competitor\'s prices ] so the issue can be traced.', answer: 'order or transaction details'),
    QuestionItem(id: 'q8', question: 'An order letter should specify [ item, quantity, and delivery details / the sender\'s hobbies ].', answer: 'item, quantity, and delivery details'),
    QuestionItem(id: 'q9', question: 'A formal letter should maintain a [ polite and professional / casual and abrupt ] tone throughout, even when complaining.', answer: 'polite and professional'),
    QuestionItem(id: 'q10', question: 'The final part of a formal letter includes the complimentary close followed by the [ sender\'s signature and name / recipient\'s address again ].', answer: "sender's signature and name"),
  ],
);
