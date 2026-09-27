import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/views/student_topic_screen.dart';
import 'package:commerce_accounts_11to12/views/teacher_paper_screen.dart';

void main() {
  group('Student topic screen — Class gating', () {
    testWidgets('Class 11 hides Partnership, Company Accounts and Cash Flow', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: StudentTopicScreen(board: Board.gseb, schoolClass: 11),
      ));
      await tester.pumpAndSettle();

      expect(find.text('Journal, Ledger & Trial Balance'), findsOneWidget);
      expect(find.text('Partnership Accounts'), findsNothing);
      expect(find.text('Company Accounts — Share Capital'), findsNothing);
      expect(find.text('Cash Flow Statement'), findsNothing);
    });

    testWidgets('Class 12 shows both Class 11 and Class 12 topics', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: StudentTopicScreen(board: Board.cbse, schoolClass: 12),
      ));
      await tester.pumpAndSettle();

      expect(find.text('Journal, Ledger & Trial Balance'), findsOneWidget);

      // Later topics render off-screen in a virtualised ListView; scroll
      // down before asserting they exist.
      await tester.drag(find.byType(Scrollable).first, const Offset(0, -2000));
      await tester.pumpAndSettle();

      expect(find.text('Partnership Accounts'), findsOneWidget);
      expect(find.text('Company Accounts — Share Capital'), findsOneWidget);
      expect(find.text('Cash Flow Statement'), findsOneWidget);
    });

    testWidgets('Mock Test duration reflects the selected class', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: StudentTopicScreen(board: Board.gseb, schoolClass: 11),
      ));
      await tester.pumpAndSettle();
      await tester.drag(find.byType(Scrollable).first, const Offset(0, -2000));
      await tester.pumpAndSettle();
      expect(find.textContaining('30-minute'), findsOneWidget);

      await tester.pumpWidget(const MaterialApp(
        home: StudentTopicScreen(board: Board.gseb, schoolClass: 12),
      ));
      await tester.pumpAndSettle();
      await tester.drag(find.byType(Scrollable).first, const Offset(0, -2000));
      await tester.pumpAndSettle();
      expect(find.textContaining('45-minute'), findsOneWidget);
    });
  });

  group('Teacher paper screen — Class gating', () {
    testWidgets('Class 11 topic dropdown does not offer Class-12-only topics', (tester) async {
      await tester.pumpWidget(const MaterialApp(home: TeacherPaperScreen()));
      await tester.pumpAndSettle();

      // Default state is Class 11; open the Topic dropdown (the first
      // dropdown on the screen) by tapping its InputDecorator, since the
      // label text itself isn't directly hit-testable.
      await tester.tap(find.byType(InputDecorator).first);
      await tester.pumpAndSettle();

      expect(find.text('Journal, Ledger & Trial Balance'), findsWidgets);
      expect(find.text('Partnership — Admission'), findsNothing);
      expect(find.text('Company Accounts — Issue of Shares'), findsNothing);
    });
  });
}
