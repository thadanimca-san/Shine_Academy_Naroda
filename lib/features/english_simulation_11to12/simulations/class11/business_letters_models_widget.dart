import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model order, complaint, and enquiry letters for the business
/// correspondence questions set by GSEB and CBSE.
class BusinessLettersModelsWidget extends StatelessWidget {
  const BusinessLettersModelsWidget({super.key});

  static const _formatPoints = [
    'Sender\'s (company/individual) address and date at the top, then the receiver\'s name/company and address.',
    'A one-line subject stating the letter\'s exact purpose (e.g. "Subject: Order for Office Stationery").',
    'Order letters: state item, quantity, specification, price, and required delivery/payment terms precisely.',
    'Complaint letters: state the problem factually, quote the order/transaction reference, and clearly state the remedy wanted (replacement, refund, repair).',
    'Enquiry letters: list the specific questions clearly, often as short numbered points.',
    'Close with "Yours faithfully", followed by name, designation, and company name if applicable — polite and professional even when complaining.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a letter to the manager of a stationery supplier placing an order for office stationery items required for your school.',
      wordCount: '~120–150 words',
      modelAnswer: '''
                                            Greenwood Public School
                                            Race Course Road, Vadodara
                                            8 April 2025

The Manager
Shree Stationery Mart
Vadodara

Subject: Order for Office Stationery

Dear Sir,

We would like to place an order for the following
items required for the new academic session:

1. A4 size paper (ream)          –  100 units
2. Ball-point pens (box of 50)   –  20 boxes
3. Registers, 200 pages          –  60 pieces
4. Stapler pins (box)            –  30 boxes

Kindly ensure that the items are of standard quality
and are delivered to our school office by 20 April
2025. Payment will be made by cheque upon delivery,
against your invoice. Please confirm receipt of this
order at the earliest.

Yours faithfully,
Nikhil Rao
Administrative Officer''',
    ),
    WritingPrompt(
      prompt: 'Write a letter of complaint to the manager of an electronics store regarding a defective mixer-grinder you purchased, requesting a replacement.',
      wordCount: '~120–150 words',
      modelAnswer: '''
                                            17, Lotus Apartments
                                            Bhavnagar
                                            22 June 2025

The Manager
Modern Electronics
Bhavnagar

Subject: Complaint Regarding Defective Mixer-Grinder

Dear Sir,

I purchased a mixer-grinder (Model MX-220, Invoice
No. 4587) from your store on 10 June 2025. Within a
week of use, the motor began overheating and making
an unusual grinding noise, even during light use.

Since the appliance is well within the warranty
period, I request you to arrange for its inspection
and provide a replacement at the earliest, as the
defect appears to be a manufacturing fault rather
than a result of misuse. I have retained the original
bill and warranty card for your reference.

I hope for a prompt and satisfactory resolution.

Yours faithfully,
Priya Nair''',
    ),
    WritingPrompt(
      prompt: 'Write a letter of enquiry to a publishing house asking for details about bulk purchase rates and delivery terms for reference books for your school library.',
      wordCount: '~100–120 words',
      modelAnswer: '''
                                            St. Xavier's School
                                            Navrangpura, Ahmedabad
                                            2 August 2025

The Sales Manager
National Book House
Delhi

Subject: Enquiry Regarding Bulk Purchase of Reference Books

Dear Sir/Madam,

We are looking to purchase reference books in
English, Mathematics, and Science for Classes IX to
XII for our school library and would be grateful if
you could provide the following information:

1. Discount offered on bulk orders above 200 copies
2. Approximate delivery time to Ahmedabad
3. Modes of payment accepted
4. Whether a sample catalogue can be sent to us

An early response would help us finalise our order
before the new academic term begins.

Yours faithfully,
Sanya Kapoor
Librarian''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Business Letters — Model Answers',
      icon: Icons.business_center,
      accent: Colors.teal,
      description: 'Order, complaint, and enquiry letters written the way examiners expect to see them.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
