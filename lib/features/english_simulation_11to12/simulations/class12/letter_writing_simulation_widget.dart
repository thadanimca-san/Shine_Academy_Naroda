import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing a complaint, enquiry, or
/// order letter.
class LetterWritingSimulationWidget extends StatelessWidget {
  const LetterWritingSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'A letter of complaint should specify the ___.', correctWord: 'remedy sought (refund/replacement/action)', options: ['remedy sought (refund/replacement/action)', "writer's general mood"], note: 'Stating the desired remedy makes the letter actionable for the recipient.'),
    CompletionExample(sentenceWithBlank: 'A letter of enquiry should request ___.', correctWord: 'specific, itemised information', options: ['specific, itemised information', 'a general chat'], note: 'Clear, itemised questions make it easy for the recipient to respond fully.'),
    CompletionExample(sentenceWithBlank: 'A letter of application should state its purpose ___.', correctWord: 'clearly in the first paragraph', options: ['clearly in the first paragraph', 'only in the closing line'], note: 'Stating the purpose upfront helps the reader understand the letter immediately.'),
    CompletionExample(sentenceWithBlank: 'All formal letters begin with the ___.', correctWord: "sender's address and date", options: ["sender's address and date", "recipient's phone number"], note: 'This is a fixed structural convention of formal letters.'),
    CompletionExample(sentenceWithBlank: 'A letter to a named recipient should close with ___.', correctWord: 'Yours sincerely', options: ['Yours sincerely', 'Yours faithfully'], note: '"Yours sincerely" pairs with a named salutation.'),
    CompletionExample(sentenceWithBlank: 'An order letter should specify ___.', correctWord: 'item, quantity, and delivery details', options: ['item, quantity, and delivery details', "the sender's hobbies"], note: 'These are the practical details the supplier needs to fulfil the order.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Letter Writing (Complaint, Enquiry, Order)',
      icon: Icons.mail_outline,
      accent: Colors.blue,
      description: 'Choose the correct convention for formal letters.',
      examples: _examples,
    );
  }
}
