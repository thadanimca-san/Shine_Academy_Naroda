import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/views/mock_test_screen.dart';

void main() {
  setUp(() {
    SharedPreferences.setMockInitialValues({});
  });

  testWidgets('Class 11 mock test shows only Class 11 topics (no Final Accounts/Partnership/Cash Flow)', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: MockTestScreen(board: Board.gseb, schoolClass: 11),
    ));
    await tester.pump();

    expect(find.textContaining('Prepare Final Accounts'), findsNothing);
    expect(find.textContaining('admit'), findsNothing);
    expect(find.textContaining('Prepare a Cash Flow Statement'), findsNothing);
    // Core Class 11 topics should be present.
    expect(find.textContaining('Journalise:'), findsWidgets);
  });

  testWidgets('Class 12 mock test includes Final Accounts, Partnership and Cash Flow questions', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: MockTestScreen(board: Board.cbse, schoolClass: 12),
    ));
    await tester.pump();

    // The ListView virtualises off-screen questions; scroll it directly
    // by its Scrollable state so later questions actually get built.
    final scrollable = find.byType(Scrollable).first;
    for (var i = 0; i < 15; i++) {
      await tester.drag(scrollable, const Offset(0, -400));
      await tester.pump();
    }

    expect(find.textContaining('Prepare Final Accounts'), findsOneWidget);
    expect(find.textContaining('bringing capital'), findsOneWidget);
    expect(find.textContaining('Prepare a Cash Flow Statement'), findsOneWidget);
  });

  testWidgets('Mock test screen builds without throwing for both boards', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: MockTestScreen(board: Board.cbse, schoolClass: 11),
    ));
    await tester.pump();
    expect(find.text('Mock Test'), findsOneWidget);
  });
}
