import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/company_accounts_generator.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/self_check_widget.dart';
import '../widgets/share_issue_steps_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Company Accounts — Issue of Shares: application,
/// allotment, calls, and (at higher difficulty) forfeiture & reissue of
/// defaulted shares. Reveal-based given the multi-step nature.
class CompanyAccountsPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const CompanyAccountsPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<CompanyAccountsPracticeScreen> createState() => _CompanyAccountsPracticeScreenState();
}

class _CompanyAccountsPracticeScreenState extends State<CompanyAccountsPracticeScreen> {
  late GeneratedShareIssueProblem _problem;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = CompanyAccountsGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _revealed = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final c = _problem.calls;
    final premiumText = c.premiumPerShare > 0 ? ' (including a premium of ₹${c.premiumPerShare.toStringAsFixed(0)} per share)' : '';
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Company Accounts — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            'A company issued ${_problem.sharesIssued} shares of ₹${c.faceValue.toStringAsFixed(0)} each$premiumText, '
            'payable as: Application ₹${c.applicationAmount.toStringAsFixed(0)}, '
            'Allotment ₹${c.allotmentAmount.toStringAsFixed(0)}'
            '${c.firstCallAmount > 0 ? ', First Call ₹${c.firstCallAmount.toStringAsFixed(0)}' : ''}'
            '${c.finalCallAmount > 0 ? ', Final Call ₹${c.finalCallAmount.toStringAsFixed(0)}' : ''}. '
            'All shares were subscribed and all money was received'
            '${_problem.sharesForfeited > 0 ? ', except the final call on ${_problem.sharesForfeited} shares, which were '
                'subsequently forfeited and reissued at ₹${_problem.reissuePricePerShare.toStringAsFixed(0)} per share, fully paid up' : ''}. '
            'Pass the necessary journal entries.',
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 16),
          Center(
            child: ElevatedButton.icon(
              onPressed: () => setState(() => _revealed = !_revealed),
              icon: Icon(_revealed ? Icons.visibility_off : Icons.lightbulb_outline),
              label: Text(_revealed
                  ? LocalizationService.t('Hide Solution', widget.medium)
                  : LocalizationService.t('Show Solution', widget.medium)),
            ),
          ),
          if (_revealed) ...[
            ShareIssueStepsWidget(steps: _problem.result.steps, medium: widget.medium),
            const SizedBox(height: 8),
            Text('${LocalizationService.t('Total Capital Raised', widget.medium)}: ₹${_problem.result.totalCapitalRaised.toStringAsFixed(0)}',
                style: TextStyle(fontWeight: FontWeight.bold)),
            if (_problem.result.securitiesPremiumBalance > 0)
              Text('${LocalizationService.t('Securities Premium', widget.medium)}: ₹${_problem.result.securitiesPremiumBalance.toStringAsFixed(0)}'),
            if (_problem.result.capitalReserveOnReissue > 0)
              Text('${LocalizationService.t('Capital Reserve (from reissue)', widget.medium)}: ₹${_problem.result.capitalReserveOnReissue.toStringAsFixed(0)}'),
            SelfCheckWidget(key: ValueKey(_problem.id), topicKey: ProgressService.topicCompanyAccounts),
          ],
        ],
      ),
    );
  }
}
