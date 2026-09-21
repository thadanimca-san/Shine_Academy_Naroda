import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import 'brs_practice_screen.dart';
import 'cash_book_practice_screen.dart';
import 'cash_flow_practice_screen.dart';
import 'company_accounts_practice_screen.dart';
import 'depreciation_practice_screen.dart';
import 'final_accounts_practice_screen.dart';
import 'mock_test_screen.dart';
import 'partnership_practice_screen.dart';
import 'progress_screen.dart';
import 'rectification_practice_screen.dart';
import 'student_practice_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// One topic tile's static metadata, including the class it first
/// becomes examinable in — GSEB and CBSE both teach Journal through
/// Final Accounts in Class 11, and Partnership/Company Accounts/Cash
/// Flow only from Class 12 onward. A Class 11 selection hides the
/// Class-12-only topics rather than showing content the student hasn't
/// been taught yet.
class _TopicInfo {
  final IconData icon;
  final Color color;
  final String title;
  final String subtitle;
  final int introducedInClass;
  final WidgetBuilder Function(Board board, int schoolClass, Medium medium) screenBuilder;

  const _TopicInfo({
    required this.icon,
    required this.color,
    required this.title,
    required this.subtitle,
    required this.introducedInClass,
    required this.screenBuilder,
  });
}

/// Topic picker shown to a student after they choose Board + Class +
/// Medium — each tile launches the practice flow for that topic, filtered
/// to only the topics that class has actually been taught.
class StudentTopicScreen extends StatelessWidget {
  final Board board;
  final int schoolClass;
  final Medium medium;

  const StudentTopicScreen({super.key, required this.board, required this.schoolClass, this.medium = Medium.english});

  static final List<_TopicInfo> _allTopics = [
    _TopicInfo(
      icon: Icons.book,
      color: Colors.indigo,
      title: 'Journal, Ledger & Trial Balance',
      subtitle: 'Journalise transactions, post to ledger, prepare trial balance',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => StudentPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.account_balance_wallet,
      color: Colors.teal,
      title: 'Double Column Cash Book',
      subtitle: 'Cash, Bank & Discount columns, contra entries',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => CashBookPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.trending_down,
      color: Colors.deepOrange,
      title: 'Depreciation (SLM & WDV)',
      subtitle: 'Straight Line and Written Down Value methods, year-by-year',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => DepreciationPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.build_circle,
      color: Colors.purple,
      title: 'Rectification of Errors',
      subtitle: 'Find and correct errors using Suspense A/c where needed',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => RectificationPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.account_balance,
      color: Colors.blueGrey,
      title: 'Bank Reconciliation Statement',
      subtitle: 'Reconcile Cash Book and Pass Book balances',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => BrsPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.summarize,
      color: Colors.green,
      title: 'Final Accounts',
      subtitle: 'Trading A/c, Profit & Loss A/c and Balance Sheet with adjustments',
      introducedInClass: 11,
      screenBuilder: (b, c, m) => (_) => FinalAccountsPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.groups,
      color: Colors.brown,
      title: 'Partnership Accounts',
      subtitle: 'Admission, Retirement, Death & Dissolution',
      introducedInClass: 12,
      screenBuilder: (b, c, m) => (_) => PartnershipPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.business,
      color: Colors.blue,
      title: 'Company Accounts — Share Capital',
      subtitle: 'Application, Allotment, Calls, Forfeiture & Reissue of Shares',
      introducedInClass: 12,
      screenBuilder: (b, c, m) => (_) => CompanyAccountsPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
    _TopicInfo(
      icon: Icons.waterfall_chart,
      color: Colors.cyan,
      title: 'Cash Flow Statement',
      subtitle: 'Indirect method — Operating, Investing & Financing activities',
      introducedInClass: 12,
      screenBuilder: (b, c, m) => (_) => CashFlowPracticeScreen(board: b, schoolClass: c, medium: m),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    final visibleTopics = _allTopics.where((t) => t.introducedInClass <= schoolClass).toList();

    return Scaffold(
      appBar: AppBar(
        title: Text('Choose a Topic — Class $schoolClass'),
        actions: [
          IconButton(
            icon: Icon(Icons.insights),
            tooltip: 'My Progress',
            onPressed: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const ProgressScreen())),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            color: Colors.indigo.withValues(alpha: 0.08),
            child: ListTile(
              leading: Icon(Icons.insights, size: 36, color: Colors.indigo),
              title: Text(TrilingualService.instance.getUIText('My Progress')),
              subtitle: Text(TrilingualService.instance.getUIText('See your accuracy by topic and what needs more practice')),
              trailing: Icon(Icons.arrow_forward_ios),
              onTap: () => Navigator.of(context).push(MaterialPageRoute(builder: (_) => const ProgressScreen())),
            ),
          ),
          for (final topic in visibleTopics) ...[
            const SizedBox(height: 12),
            _topicTile(
              context,
              icon: topic.icon,
              color: topic.color,
              title: topic.title,
              subtitle: topic.subtitle,
              onTap: () => Navigator.of(context).push(MaterialPageRoute(
                builder: topic.screenBuilder(board, schoolClass, medium),
              )),
            ),
          ],
          const SizedBox(height: 20),
          Card(
            color: Colors.amber.withValues(alpha: 0.12),
            child: ListTile(
              leading: Icon(Icons.timer, size: 36, color: Colors.amber),
              title: Text(TrilingualService.instance.getUIText('Mock Test (Timed)')),
              subtitle: Text(schoolClass == 12
                  ? '45-minute mixed-topic test in board exam pattern'
                  : '30-minute mixed-topic test in board exam pattern'),
              trailing: Icon(Icons.arrow_forward_ios),
              onTap: () => Navigator.of(context).push(MaterialPageRoute(
                builder: (_) => MockTestScreen(board: board, schoolClass: schoolClass, medium: medium),
              )),
            ),
          ),
        ],
      ),
    );
  }

  Widget _topicTile(
    BuildContext context, {
    required IconData icon,
    required Color color,
    required String title,
    required String subtitle,
    required VoidCallback onTap,
  }) {
    return Card(
      child: ListTile(
        leading: Icon(icon, size: 36, color: color),
        title: Text(title),
        subtitle: Text(subtitle),
        trailing: Icon(Icons.arrow_forward_ios),
        onTap: onTap,
      ),
    );
  }
}
