import '../../../models/chapter_model.dart';

final class11BusinessLettersChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_businessletters", chapterName: "Business and Official Letters",
  formulas: [],
  concepts: [
    "Business letters (order, complaint, enquiry) are formal letters exchanged between organisations, customers, and suppliers, so precision and clarity are essential.",
    "An order letter must clearly state the item, quantity, specifications, price, and mode of delivery/payment expected.",
    "A complaint letter should state the problem factually, reference the transaction (date, order number), and specify the resolution expected — without being rude.",
    "An enquiry letter requests specific information (price, availability, terms) and should list questions clearly, often as points.",
    "Business letters end with a professional closing and, unlike personal formal letters, often include the sender's designation or company name typed below the signature.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'An order letter must clearly mention the [ item, quantity, and payment terms / sender\'s personal opinions ].', answer: 'item, quantity, and payment terms'),
    QuestionItem(id: 'q2', question: 'A complaint letter should state the problem [ factually and specifically / vaguely and emotionally ].', answer: 'factually and specifically'),
    QuestionItem(id: 'q3', question: 'A letter of complaint should always mention the [ order/transaction reference / competitor\'s name ] for the company to trace the issue.', answer: 'order/transaction reference'),
    QuestionItem(id: 'q4', question: 'An enquiry letter is written to [ request specific information / lodge a complaint ].', answer: 'request specific information'),
    QuestionItem(id: 'q5', question: 'A business letter should end with a [ clear, specific request for action / vague hope that things improve ].', answer: 'clear, specific request for action'),
    QuestionItem(id: 'q6', question: 'The tone of a business letter, even when complaining, should remain [ polite and professional / harsh and accusatory ].', answer: 'polite and professional'),
    QuestionItem(id: 'q7', question: 'A letter placing a bulk order should specify the [ delivery deadline and address / employees\' names ].', answer: 'delivery deadline and address'),
    QuestionItem(id: 'q8', question: 'When enquiring about a product, questions are best organised as [ clear, numbered points / one long sentence ].', answer: 'clear, numbered points'),
    QuestionItem(id: 'q9', question: 'A business letter typically closes with [ "Yours faithfully" followed by name and designation / just a first name ].', answer: '"Yours faithfully" followed by name and designation'),
    QuestionItem(id: 'q10', question: 'A complaint letter about a defective product should state the [ desired remedy (replacement/refund) / general dissatisfaction only ].', answer: 'desired remedy (replacement/refund)'),
  ],
);
