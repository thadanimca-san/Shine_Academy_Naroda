import 'package:flutter/material.dart';
import '../common/choose_completion_widget.dart';

/// Choose the correct convention for writing business and official
/// letters (order, complaint, enquiry).
class BusinessLettersSimulationWidget extends StatelessWidget {
  const BusinessLettersSimulationWidget({super.key});

  static const _examples = [
    CompletionExample(sentenceWithBlank: 'An order letter must clearly mention the ___.', correctWord: 'item, quantity, and payment terms', options: ['item, quantity, and payment terms', "sender's personal opinions"], note: 'These details let the supplier fulfil the order correctly.'),
    CompletionExample(sentenceWithBlank: 'A complaint letter should state the problem ___.', correctWord: 'factually and specifically', options: ['factually and specifically', 'vaguely and emotionally'], note: 'Specific facts help the company resolve the issue efficiently.'),
    CompletionExample(sentenceWithBlank: 'A complaint letter should always mention the ___ for the company to trace the issue.', correctWord: 'order/transaction reference', options: ['order/transaction reference', "competitor's name"], note: 'A reference number lets the company quickly locate the transaction.'),
    CompletionExample(sentenceWithBlank: 'An enquiry letter is written to ___.', correctWord: 'request specific information', options: ['request specific information', 'lodge a complaint'], note: 'Enquiry letters ask about price, availability, or terms.'),
    CompletionExample(sentenceWithBlank: 'The tone of a business letter, even when complaining, should remain ___.', correctWord: 'polite and professional', options: ['polite and professional', 'harsh and accusatory'], note: 'A professional tone is more likely to get a helpful response.'),
    CompletionExample(sentenceWithBlank: 'When enquiring about a product, questions are best organised as ___.', correctWord: 'clear, numbered points', options: ['clear, numbered points', 'one long sentence'], note: 'Numbered points make it easy for the reader to answer each question.'),
  ];

  @override
  Widget build(BuildContext context) {
    return const ChooseCompletionWidget(
      title: 'Business and Official Letters',
      icon: Icons.business_center,
      accent: Colors.blueGrey,
      description: 'Choose the correct convention for business/official letters.',
      examples: _examples,
    );
  }
}
