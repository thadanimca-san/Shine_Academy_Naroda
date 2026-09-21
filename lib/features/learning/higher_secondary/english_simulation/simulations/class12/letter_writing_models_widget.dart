import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete board-level model letters — application, complaint, and
/// enquiry — building on the Class 11 letter-writing foundation with the
/// situations Class 12 board papers most often ask for.
class LetterWritingModelsWidget extends StatelessWidget {
  const LetterWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Every formal letter follows the same skeleton: sender\'s address, date, receiver\'s address, subject line, salutation, body, complimentary close, signature.',
    'A letter of application states its purpose in the first line, then supports it with relevant details (qualifications, reasons, references).',
    'A letter of complaint states the issue factually, references the transaction, and clearly states the remedy expected.',
    'A letter of enquiry lists exactly what information is needed, often as short points, and explains briefly why it is needed.',
    'Keep the tone polite and professional throughout — even a complaint should read as reasonable, not accusatory.',
    'Close with "Yours faithfully" (unknown/unnamed recipient) or "Yours sincerely" (named recipient), followed by your full name.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Write a letter of application to the Principal of a school for the post of a part-time Spoken English trainer, mentioning your relevant qualifications.',
      wordCount: '~150 words',
      modelAnswer: '''
                                            56, Ashirwad Society
                                            Rajkot – 360005
                                            9 March 2026

The Principal
Bright Future English Academy
Rajkot

Subject: Application for the Post of Spoken English Trainer

Dear Sir/Madam,

In response to your advertisement dated 5 March 2026
in the Gujarat Herald, I wish to apply for the
part-time post of Spoken English Trainer at your
institute.

I hold a Bachelor's degree in English Literature and
a certification in Teaching English as a Foreign
Language (TEFL). I have two years of experience
conducting spoken English workshops for high school
students at a local coaching centre, focusing on
conversational fluency, pronunciation, and
confidence-building.

I am available to work in the evening batches and
would welcome the opportunity to contribute to your
esteemed institution. My résumé and certificates are
enclosed for your kind consideration.

Yours faithfully,
Devansh Trivedi
(Enclosure: Résumé, Certificates)''',
    ),
    WritingPrompt(
      prompt: 'Write a letter to the Sales Manager of an online retailer complaining about a delayed and damaged delivery, and requesting a refund.',
      wordCount: '~150 words',
      modelAnswer: '''
                                            22, Silver Heights
                                            Surat – 395007
                                            15 May 2026

The Sales Manager
QuickBuy Online Retail Pvt. Ltd.
Mumbai

Subject: Complaint Regarding Delayed and Damaged Delivery

Dear Sir/Madam,

I am writing regarding my order (Order No. QB-77291)
placed on your website on 2 May 2026, for a study
lamp that was promised delivery within five working
days.

The package arrived on 14 May 2026 — nine days late —
and the lamp inside was found cracked, apparently due
to poor packaging. This is disappointing, given the
otherwise reliable service I have received from your
platform in the past.

I request a full refund to my original payment
method, or a prompt replacement, along with an
explanation for the delay. I have attached photographs
of the damaged item along with this letter.

I look forward to a swift resolution.

Yours faithfully,
Meher Fernandes
(Enclosure: Photographs, Order Receipt)''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Board-Level Letters — Model Answers',
      icon: Icons.markunread_mailbox,
      accent: Colors.indigo,
      description: 'Application and complaint letters written exactly to the format Class 12 boards expect.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
