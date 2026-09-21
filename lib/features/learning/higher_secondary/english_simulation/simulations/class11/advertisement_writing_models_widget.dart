import 'package:flutter/material.dart';
import '../common/writing_skill_widget.dart';

/// Complete model classified advertisements across the categories GSEB and
/// CBSE most often ask for.
class AdvertisementWritingModelsWidget extends StatelessWidget {
  const AdvertisementWritingModelsWidget({super.key});

  static const _formatPoints = [
    'Written in a compressed, telegraphic style — articles ("a/the") and non-essential words are dropped to save space.',
    'Grouped under a category heading in bold/capitals: FOR SALE, TO LET, SITUATIONS VACANT, LOST & FOUND, etc.',
    'Include only what the reader actually needs: item/role, key features or requirements, price if relevant, and contact details.',
    'Common abbreviations (BHK, Rs., Contact, Yrs, Exp.) are acceptable and expected — they are not considered "incomplete sentences" in this format.',
    'Always end with a working contact number, email, or address.',
    'Usually kept under 50 words, since classified space in a newspaper is paid for by length.',
  ];

  static const _prompts = [
    WritingPrompt(
      prompt: 'Draft a classified advertisement for the "To Let" column offering a 2BHK flat for rent.',
      wordCount: '~40–50 words',
      modelAnswer: '''
TO LET

2BHK flat, 2nd floor, Vastrapur, Ahmedabad. Semi-
furnished, modular kitchen, covered parking, 24-hr
water supply. Near school and bus stop. Suitable for
small family. Rent Rs. 15,000/month + maintenance.
No brokers. Contact: 98xxxxxx21 (Mr. Shah).''',
    ),
    WritingPrompt(
      prompt: 'Draft a classified advertisement for the "Situations Vacant" column on behalf of a school looking to hire a Mathematics teacher.',
      wordCount: '~40–50 words',
      modelAnswer: '''
SITUATIONS VACANT

Required: Mathematics Teacher for Classes IX–XII.
Qualification: B.Sc./M.Sc. with B.Ed., min. 3 yrs
teaching exp. CBSE curriculum knowledge preferred.
Attractive salary as per experience. Apply with
resume to Riverside Public School, Race Course Road,
Vadodara, or email hr@riversideschool.edu within
7 days.''',
    ),
    WritingPrompt(
      prompt: 'Draft a classified advertisement for the "For Sale" column to sell a used bicycle in good condition.',
      wordCount: '~30–40 words',
      modelAnswer: '''
FOR SALE

Hero Sprint bicycle, 1 yr old, excellent condition,
gears working perfectly, includes lock and lights.
Genuine reason for sale — moving abroad. Price
Rs. 3,500 (negotiable). Contact: Karan, 97xxxxxx48,
Surat.''',
    ),
    WritingPrompt(
      prompt: 'Draft a "Lost and Found" classified advertisement for a lost school bag containing important documents.',
      wordCount: '~30–40 words',
      modelAnswer: '''
LOST

Black school bag lost near Ellis Bridge, Ahmedabad,
on 14 Sept, containing school ID card and important
mark-sheets. No monetary value to anyone else but
urgently needed by owner. Suitable reward offered.
Contact: 96xxxxxx73.''',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return const WritingSkillWidget(
      title: 'Classified Advertisements — Model Answers',
      icon: Icons.campaign,
      accent: Colors.deepOrange,
      description: 'Real classified-style ads across the categories examiners commonly ask for.',
      formatPoints: _formatPoints,
      prompts: _prompts,
    );
  }
}
