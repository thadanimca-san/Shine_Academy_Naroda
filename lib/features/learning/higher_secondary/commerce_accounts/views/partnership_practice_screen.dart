import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/partnership_model.dart';
import '../models/problem_model.dart';
import '../services/dissolution_generator.dart';
import '../services/localization_service.dart';
import '../services/partnership_generator.dart';
import '../services/progress_service.dart';
import '../widgets/capital_accounts_widget.dart';
import '../widgets/realisation_account_widget.dart';
import '../widgets/self_check_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _Mode { admission, departure, dissolution }

/// Student practice for Partnership Accounts: Admission of a new partner
/// and Retirement/Death of a partner, both using the goodwill
/// capital-account-adjustment method. Reveal-based (like Cash Book and
/// Final Accounts) given the multi-step nature of these problems.
class PartnershipPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const PartnershipPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<PartnershipPracticeScreen> createState() => _PartnershipPracticeScreenState();
}

class _PartnershipPracticeScreenState extends State<PartnershipPracticeScreen> {
  _Mode _mode = _Mode.admission;
  GeneratedAdmissionProblem? _admissionProblem;
  GeneratedDepartureProblem? _departureProblem;
  GeneratedDissolutionProblem? _dissolutionProblem;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _revealed = false;
      switch (_mode) {
        case _Mode.admission:
          _admissionProblem = PartnershipGenerator.generateAdmission(
            board: widget.board,
            schoolClass: widget.schoolClass,
            difficulty: widget.difficulty,
          );
        case _Mode.departure:
          _departureProblem = PartnershipGenerator.generateDeparture(
            board: widget.board,
            schoolClass: widget.schoolClass,
            difficulty: widget.difficulty,
          );
        case _Mode.dissolution:
          _dissolutionProblem = DissolutionGenerator.generate(
            board: widget.board,
            schoolClass: widget.schoolClass,
            difficulty: widget.difficulty,
          );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Partnership Accounts — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          SegmentedButton<_Mode>(
            segments: [
              ButtonSegment(value: _Mode.admission, label: Text(LocalizationService.t('Admission', widget.medium))),
              ButtonSegment(
                  value: _Mode.departure,
                  label: Text(
                      '${LocalizationService.t('Retirement', widget.medium)} / ${LocalizationService.t('Death', widget.medium)}')),
              ButtonSegment(value: _Mode.dissolution, label: Text(LocalizationService.t('Dissolution', widget.medium))),
            ],
            selected: {_mode},
            onSelectionChanged: (s) {
              setState(() => _mode = s.first);
              _generateNewProblem();
            },
          ),
          const SizedBox(height: 12),
          if (_mode == _Mode.admission) ..._buildAdmission(),
          if (_mode == _Mode.departure) ..._buildDeparture(),
          if (_mode == _Mode.dissolution) ..._buildDissolution(),
        ],
      ),
    );
  }

  List<Widget> _buildAdmission() {
    final p = _admissionProblem!;
    final sharePercent = (p.newPartnerShare * 100).round();
    return [
      Text(
        '${p.existingPartners.map((e) => '${e.name} (${_fracLabel(e.profitShareRatio)})').join(' and ')} '
        'are partners. They admit ${p.newPartnerName} for a $sharePercent% share in the firm, '
        'bringing in capital of ₹${p.newPartnerCapital.toStringAsFixed(0)}. '
        'Goodwill of the firm is valued at ₹${p.goodwill.totalFirmGoodwill.toStringAsFixed(0)}. '
        'Pass the necessary entries and prepare Partners\' Capital Accounts.',
        style: TextStyle(fontSize: 15),
      ),
      const SizedBox(height: 8),
      Text('Existing capitals: ${p.existingPartners.map((e) => '${e.name} ₹${e.capital.toStringAsFixed(0)}').join(', ')}'),
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
        const SizedBox(height: 8),
        Text('${LocalizationService.t('New Profit Sharing Ratio', widget.medium)}: '
            '${p.result.newProfitSharingRatios.entries.map((e) => '${e.key} ${_fracLabel(e.value)}').join(', ')}'),
        Text('${LocalizationService.t('Sacrificing Ratio', widget.medium)}: '
            '${p.result.sacrificingRatios.entries.map((e) => '${e.key} ${_fracLabel(e.value)}').join(', ')}'),
        CapitalAccountsWidget(rows: p.result.capitalAccounts, medium: widget.medium),
        SelfCheckWidget(key: ValueKey('adm-${p.id}'), topicKey: ProgressService.topicPartnership),
      ],
    ];
  }

  List<Widget> _buildDeparture() {
    final p = _departureProblem!;
    final reasonLabel = p.reason == DepartureReason.retirement ? 'retires' : 'dies';
    return [
      Text(
        '${p.allPartners.map((e) => '${e.name} (${_fracLabel(e.profitShareRatio)})').join(', ')} '
        'are partners. ${p.departingPartnerName} $reasonLabel from the firm. '
        'Goodwill of the firm is valued at ₹${p.goodwill.totalFirmGoodwill.toStringAsFixed(0)}. '
        'The remaining partners continue sharing profits in their existing ratio. '
        'Pass the necessary entries and prepare Partners\' Capital Accounts.',
        style: TextStyle(fontSize: 15),
      ),
      const SizedBox(height: 8),
      Text('Capitals: ${p.allPartners.map((e) => '${e.name} ₹${e.capital.toStringAsFixed(0)}').join(', ')}'),
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
        const SizedBox(height: 8),
        Text('${LocalizationService.t('New Profit Sharing Ratio', widget.medium)}: '
            '${p.result.newProfitSharingRatios.entries.map((e) => '${e.key} ${_fracLabel(e.value)}').join(', ')}'),
        Text('${LocalizationService.t('Gaining Ratio', widget.medium)}: '
            '${p.result.gainingRatios.entries.map((e) => '${e.key} ${_fracLabel(e.value)}').join(', ')}'),
        CapitalAccountsWidget(rows: p.result.capitalAccounts, medium: widget.medium),
        Padding(
          padding: const EdgeInsets.only(top: 8),
          child: Text(
            'Amount payable to ${p.departingPartnerName}: ₹${p.result.amountPayableToDepartingPartner.toStringAsFixed(0)}',
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
        ),
        SelfCheckWidget(key: ValueKey('dep-${p.id}'), topicKey: ProgressService.topicPartnership),
      ],
    ];
  }

  List<Widget> _buildDissolution() {
    final p = _dissolutionProblem!;
    return [
      Text(
        '${p.partners.map((e) => '${e.name} (${_fracLabel(e.profitShareRatio)})').join(', ')} '
        'decide to dissolve the firm. The following assets were realised and liabilities settled:',
        style: TextStyle(fontSize: 15),
      ),
      const SizedBox(height: 8),
      for (final a in p.assets)
        Text('• ${a.assetName}: Book Value ₹${a.bookValue.toStringAsFixed(0)}, Realised ₹${a.realisedAmount.toStringAsFixed(0)}'),
      for (final l in p.liabilities)
        Text('• ${l.liabilityName}: Book Value ₹${l.bookValue.toStringAsFixed(0)}, Paid ₹${l.amountPaid.toStringAsFixed(0)}'),
      if (p.dissolutionExpenses > 0) Text('• Realisation Expenses: ₹${p.dissolutionExpenses.toStringAsFixed(0)}'),
      const SizedBox(height: 8),
      Text('Capitals: ${p.partners.map((e) => '${e.name} ₹${e.capital.toStringAsFixed(0)}').join(', ')}'),
      const SizedBox(height: 8),
      Text(LocalizationService.t('Prepare the Realisation Account and show the final settlement with partners.', widget.medium)),
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
        RealisationAccountWidget(result: p.result, medium: widget.medium),
        SelfCheckWidget(key: ValueKey('diss-${p.id}'), topicKey: ProgressService.topicPartnership),
      ],
    ];
  }

  String _fracLabel(double share) {
    final percent = (share * 100).round();
    return '$percent%';
  }
}
