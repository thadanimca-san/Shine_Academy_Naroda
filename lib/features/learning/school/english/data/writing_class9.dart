import '../models/writing_prompt.dart';

const class9Writing = WritingLibrary(
  id: 'class9_writing',
  title: 'Essay, Letter & Report Writing',
  grade: 'Class 9',
  prompts: [
    WritingPrompt(
      id: 'class9_writing_essay_climate',
      title: 'Essay: What Can Students Do About Climate Change?',
      sceneEmoji: '🌍',
      sceneDescription:
          'Write an argumentative essay (about 180-200 words) on practical steps students can take to address '
          'climate change, moving beyond generic advice to specific, realistic actions.',
      wordBank: [
        'sustainable',
        'carbon footprint',
        'initiative',
        'collective',
        'advocate',
        'consumption',
        'renewable',
        'accountability',
        'tangible',
        'meaningful',
      ],
      modelAnswer:
          'Climate change is often discussed as a problem too large for individual students to influence, but '
          'this view overlooks several meaningful, tangible actions within our reach. At the most immediate '
          'level, students can reduce their own carbon footprint through simple daily choices: walking or '
          'cycling to school where possible, reducing food waste, and being more conscious about electricity '
          'consumption at home. While individually small, these habits shape lifelong patterns of behaviour '
          'that matter over an entire lifetime.\n\n'
          'Beyond personal habits, students hold a form of influence that is easy to underestimate: the ability '
          'to advocate within their own communities. Starting a recycling initiative at school, organising a '
          'tree-planting drive, or simply raising awareness among family members about renewable energy options '
          'can create effects far beyond what one student\'s carbon footprint alone would suggest. Collective '
          'action, even at a small scale, tends to spread through visible example far more effectively than '
          'individual effort alone.\n\n'
          'Ultimately, holding governments and corporations accountable remains essential, since they control '
          'resources and policies at a scale no individual can match. However, dismissing personal and community '
          'action as pointless ignores how such action often builds the public pressure that eventually makes '
          'larger policy accountability possible in the first place.',
      modelAnswerHighlights: [
        'Opens by directly addressing a common counter-argument before responding to it',
        'Organises ideas into a clear structure: personal action, community action, and systemic accountability',
        'Avoids vague generalities, giving specific concrete examples (recycling initiative, tree-planting drive)',
        'Uses academic linking phrases like "Beyond personal habits" and "Ultimately" to guide the reader',
        'Ends by connecting individual action back to the larger systemic point, giving the essay a unified argument',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class9_writing_letter_college',
      title: 'Formal Letter: Requesting Information About a Summer Programme',
      sceneEmoji: '🎓',
      sceneDescription:
          'Write a formal letter to the coordinator of a summer science programme, requesting details about '
          'eligibility, fees, and the application process.',
      wordBank: [
        'inquire',
        'eligibility',
        'curriculum',
        'stipulate',
        'prospectus',
        'commence',
        'accommodate',
        'clarify',
        'prompt',
        'sincerely',
      ],
      modelAnswer:
          '22, Riverside Apartments\nPune\n3 April\n\n'
          'The Coordinator\nYoung Scientists Summer Programme\nPune\n\n'
          'Subject: Inquiry regarding the Young Scientists Summer Programme\n\n'
          'Dear Sir/Madam,\n\n'
          'I recently came across an advertisement for your Young Scientists Summer Programme and am writing to '
          'inquire further about the details, as I am considering applying this year.\n\n'
          'Could you kindly clarify the eligibility criteria for the programme, particularly whether it is open '
          'to students currently in Class 9? I would also appreciate information about the total fees involved, '
          'the exact dates on which the programme will commence and conclude, and whether any scholarships or '
          'fee waivers are available for eligible students.\n\n'
          'Additionally, I would be grateful if you could send a copy of the programme prospectus, along with '
          'details of the application process and the final submission deadline.\n\n'
          'I look forward to your prompt response and thank you in advance for your assistance.\n\n'
          'Yours faithfully,\n'
          'Ananya Deshpande',
      modelAnswerHighlights: [
        'Uses the correct formal letter layout with addresses, subject line, and formal closing',
        'Clearly states the purpose of the letter in the opening line',
        'Asks specific, numbered-style questions rather than one vague request for "more information"',
        'Uses polite, formal request phrases ("Could you kindly clarify", "I would be grateful if")',
        'Ends by thanking the recipient in advance, a professional courtesy expected in formal correspondence',
      ],
      difficulty: Difficulty.hard,
    ),
    WritingPrompt(
      id: 'class9_writing_report_debate',
      title: 'Report: Inter-School Debate Competition',
      sceneEmoji: '🎤',
      sceneDescription:
          'Write a report (about 130 words) for the school newsletter covering an inter-school debate '
          'competition your school hosted, including the topic debated and the result.',
      wordBank: [
        'hosted',
        'contingent',
        'motion',
        'articulate',
        'adjudicators',
        'rebuttal',
        'commendable',
        'runners-up',
        'proceedings',
        'noteworthy',
      ],
      modelAnswer:
          'Inter-School Debate Competition — A Report\n\n'
          'Our school hosted the annual Inter-School Debate Competition on 8 February, welcoming contingents '
          'from six neighbouring schools. The motion for the final round, "This House believes examinations '
          'should be replaced by continuous assessment," generated a particularly spirited exchange between the '
          'two finalist teams.\n\n'
          'Our school\'s team presented an articulate case in opposition to the motion, delivering a noteworthy '
          'rebuttal that impressed the panel of adjudicators with its use of statistical evidence. Although our '
          'team narrowly finished as runners-up, their commendable performance throughout the proceedings '
          'earned praise from judges and visiting teams alike.\n\n'
          'The competition concluded with a prize distribution ceremony, and several participants noted that '
          'the exposure to differing viewpoints had been just as valuable as the competition itself.',
      modelAnswerHighlights: [
        'States the event, date, and scale (six schools) clearly in the opening lines',
        'Includes the specific debate motion rather than a vague description',
        'Reports both the outcome and a specific detail about performance quality, giving a fuller picture than a bare result',
        'Uses objective, report-appropriate language rather than overly emotional description',
        'Closes with a reflective note that adds value beyond simply announcing the winner',
      ],
      difficulty: Difficulty.medium,
    ),
  ],
);
