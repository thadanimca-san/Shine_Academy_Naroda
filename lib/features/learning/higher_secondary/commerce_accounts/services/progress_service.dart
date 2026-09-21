import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

/// Per-topic practice stats for one student's device: how many questions
/// they've attempted and how many they got right, kept purely on-device
/// (no account/login needed) so it works offline and needs no backend.
class TopicProgress {
  final String topicKey;
  final int attempted;
  final int correct;

  const TopicProgress({required this.topicKey, required this.attempted, required this.correct});

  double get accuracy => attempted == 0 ? 0 : correct / attempted;

  Map<String, dynamic> toJson() => {'topicKey': topicKey, 'attempted': attempted, 'correct': correct};

  factory TopicProgress.fromJson(Map<String, dynamic> json) => TopicProgress(
        topicKey: json['topicKey'] as String,
        attempted: json['attempted'] as int,
        correct: json['correct'] as int,
      );
}

/// Records and reads practice progress per topic, so students can see
/// which topics they're weak in and get pointed back to practice them —
/// the "maximum practice" loop closing on itself with real feedback
/// instead of the student having to self-assess.
class ProgressService {
  ProgressService._();

  static const _storageKey = 'topic_progress_v1';

  static const topicJournalLedgerTB = 'journal_ledger_tb';
  static const topicCashBook = 'cash_book';
  static const topicDepreciation = 'depreciation';
  static const topicRectification = 'rectification';
  static const topicBrs = 'brs';
  static const topicFinalAccounts = 'final_accounts';
  static const topicPartnership = 'partnership';
  static const topicCompanyAccounts = 'company_accounts';
  static const topicCashFlow = 'cash_flow';

  static const topicLabels = {
    topicJournalLedgerTB: 'Journal, Ledger & Trial Balance',
    topicCashBook: 'Double Column Cash Book',
    topicDepreciation: 'Depreciation (SLM & WDV)',
    topicRectification: 'Rectification of Errors',
    topicBrs: 'Bank Reconciliation Statement',
    topicFinalAccounts: 'Final Accounts',
    topicPartnership: 'Partnership Accounts',
    topicCompanyAccounts: 'Company Accounts — Share Capital',
    topicCashFlow: 'Cash Flow Statement',
  };

  static Future<void> recordAttempt({required String topicKey, required bool wasCorrect}) async {
    final prefs = await SharedPreferences.getInstance();
    final all = await _readAll(prefs);
    final existing = all[topicKey] ?? TopicProgress(topicKey: topicKey, attempted: 0, correct: 0);
    all[topicKey] = TopicProgress(
      topicKey: topicKey,
      attempted: existing.attempted + 1,
      correct: existing.correct + (wasCorrect ? 1 : 0),
    );
    await _writeAll(prefs, all);
  }

  static Future<Map<String, TopicProgress>> getAllProgress() async {
    final prefs = await SharedPreferences.getInstance();
    return _readAll(prefs);
  }

  static Future<Map<String, TopicProgress>> _readAll(SharedPreferences prefs) async {
    final raw = prefs.getString(_storageKey);
    if (raw == null) return {};
    final decoded = jsonDecode(raw) as Map<String, dynamic>;
    return decoded.map((key, value) => MapEntry(key, TopicProgress.fromJson(value as Map<String, dynamic>)));
  }

  static Future<void> _writeAll(SharedPreferences prefs, Map<String, TopicProgress> all) async {
    final encoded = jsonEncode(all.map((key, value) => MapEntry(key, value.toJson())));
    await prefs.setString(_storageKey, encoded);
  }
}
