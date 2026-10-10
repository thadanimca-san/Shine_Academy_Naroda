import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/chapter_finish_card.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/inspiration_widget.dart';

void main() {
  testWidgets('inspiration card shows story, quote and future', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: InspirationWidget(data: {
      'title': 'Story', 'person': 'Ramanujan', 'years': '1887–1920', 'body': r'He loved $1729$.', 'quote': 'Interesting!', 'future': 'Security.',
    })))));
    expect(tester.takeException(), isNull);
    expect(find.text('Ramanujan (1887–1920)'), findsOneWidget);
  });

  testWidgets('finish card gives XP once and remembers completion', (tester) async {
    SharedPreferences.setMockInitialValues({});
    var revisionTapped = false;
    Widget card() => MaterialApp(home: Scaffold(body: SingleChildScrollView(child: ChapterFinishCard(
          moduleId: 'm1', onPlayQuiz: () {}, onQuickRevision: () => revisionTapped = true))));
    await tester.pumpWidget(card());
    await tester.pumpAndSettle();
    await tester.tap(find.text('Mark complete (+500 XP)'));
    await tester.pumpAndSettle();
    expect(find.text('Chapter completed! Proud of you.'), findsOneWidget);
    expect(find.text('Mark complete (+500 XP)'), findsNothing);
    final prefs = await SharedPreferences.getInstance();
    expect(prefs.getBool('chapter_completed_m1'), isTrue);
    await tester.tap(find.text('Quick revision'));
    expect(revisionTapped, isTrue);
  });
}
