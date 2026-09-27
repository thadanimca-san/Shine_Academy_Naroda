import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:commerce_accounts_11to12/services/progress_service.dart';
import 'package:commerce_accounts_11to12/widgets/self_check_widget.dart';

void main() {
  setUp(() {
    SharedPreferences.setMockInitialValues({});
  });

  testWidgets('tapping "Yes, correct" records a correct attempt in ProgressService', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(body: SelfCheckWidget(topicKey: ProgressService.topicCashBook)),
    ));

    await tester.tap(find.text('Yes, correct'));
    await tester.pumpAndSettle();

    expect(find.text('Marked as correct — nice work!'), findsOneWidget);

    final progress = await ProgressService.getAllProgress();
    final cashBookProgress = progress[ProgressService.topicCashBook]!;
    expect(cashBookProgress.attempted, 1);
    expect(cashBookProgress.correct, 1);
  });

  testWidgets('tapping "No, I made a mistake" records an incorrect attempt', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(body: SelfCheckWidget(topicKey: ProgressService.topicFinalAccounts)),
    ));

    await tester.tap(find.text('No, I made a mistake'));
    await tester.pumpAndSettle();

    expect(find.textContaining('Marked for revision'), findsOneWidget);

    final progress = await ProgressService.getAllProgress();
    final faProgress = progress[ProgressService.topicFinalAccounts]!;
    expect(faProgress.attempted, 1);
    expect(faProgress.correct, 0);
  });

  testWidgets('buttons are replaced by the result after answering, cannot double-record', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(body: SelfCheckWidget(topicKey: ProgressService.topicPartnership)),
    ));

    await tester.tap(find.text('Yes, correct'));
    await tester.pumpAndSettle();

    expect(find.text('Yes, correct'), findsNothing);
    expect(find.text('No, I made a mistake'), findsNothing);
  });
}
