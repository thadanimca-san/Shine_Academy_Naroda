import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:shine_academy_naroda/core/engine/content_repository.dart';
import 'package:shine_academy_naroda/core/engine/default_blocks.dart';
import 'package:shine_academy_naroda/core/engine/local_content_manager.dart';
import 'package:shine_academy_naroda/features/assessment/quiz_game_screen.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/game_quiz_card.dart';

void main() {
  setUpAll(registerDefaultBlocks);
  setUp(() {
    SharedPreferences.setMockInitialValues({});
    // Each test runs in its own zone, so cached loads from an earlier test must not be reused.
    ContentRepository.instance.clearCache();
    LocalContentManager.instance.init(force: true);
  });

  for (final chapter in ['ncert_class10_maths_ch1', 'ncert_class10_maths_ch2', 'ncert_class10_maths_ch3', 'ncert_class10_maths_ch4', 'ncert_class10_maths_ch5', 'ncert_class10_maths_ch6', 'ncert_class10_maths_ch7', 'ncert_class10_maths_ch8', 'ncert_class10_maths_ch9', 'ncert_class10_maths_ch10', 'ncert_class10_maths_ch11', 'ncert_class10_maths_ch12', 'ncert_class10_maths_ch13', 'ncert_class10_maths_ch14', 'ncert_class10_science_ch1', 'ncert_class10_science_ch2', 'ncert_class10_science_ch3', 'ncert_class10_science_ch4', 'ncert_class10_science_ch5', 'ncert_class10_science_ch6', 'ncert_class10_science_ch7', 'ncert_class10_science_ch8', 'ncert_class10_science_ch9', 'ncert_class10_science_ch10', 'ncert_class10_science_ch11', 'ncert_class10_science_ch12', 'ncert_class10_science_ch13', 'ncert_class10_grammar_ch1', 'ncert_class10_grammar_ch2', 'ncert_class10_grammar_ch3', 'ncert_class10_grammar_ch4', 'ncert_class10_grammar_ch11', 'ncert_class10_grammar_ch6', 'ncert_class10_grammar_ch7', 'ncert_class10_history_ch1', 'ncert_class10_history_ch2', 'ncert_class10_history_ch3', 'ncert_class10_history_ch4', 'ncert_class10_history_ch5', 'ncert_class10_geography_ch1', 'ncert_class10_geography_ch2', 'ncert_class10_geography_ch3', 'ncert_class10_geography_ch4', 'ncert_class10_geography_ch5', 'ncert_class10_geography_ch6', 'ncert_class10_geography_ch7', 'ncert_class10_civics_ch1', 'ncert_class10_civics_ch2', 'ncert_class10_civics_ch3', 'ncert_class10_civics_ch4', 'ncert_class10_civics_ch5', 'ncert_class10_economics_ch1', 'ncert_class10_economics_ch2', 'ncert_class10_economics_ch3', 'ncert_class10_economics_ch4', 'ncert_class10_economics_ch5', 'cbse_class10_english_ch1', 'cbse_class10_english_ch2', 'cbse_class10_english_ch3', 'cbse_class10_english_ch4', 'cbse_class10_english_ch5', 'cbse_class10_english_ch6', 'cbse_class10_english_ch7', 'cbse_class10_english_ch8', 'cbse_class10_english_ch9', 'cbse_class10_english_poem1', 'cbse_class10_english_poem2', 'cbse_class10_english_poem3', 'cbse_class10_english_poem4', 'cbse_class10_english_poem5', 'cbse_class10_english_poem6', 'cbse_class10_english_poem7', 'cbse_class10_english_poem8', 'cbse_class10_english_poem9', 'cbse_class10_english_poem10', 'cbse_class10_english_sup_ch1', 'cbse_class10_english_sup_ch2', 'cbse_class10_english_sup_ch3']) {
    testWidgets('$chapter: plays a round of 10 game questions', (tester) async {
      await tester.pumpWidget(MaterialApp(home: QuizGameScreen(moduleId: chapter)));
      // Content is read from disk, which needs real async time.
      for (var i = 0; i < 100 && find.byType(GameQuizCard).evaluate().isEmpty; i++) {
        await tester.runAsync(() => Future.delayed(const Duration(milliseconds: 100)));
        await tester.pump();
      }
      expect(find.byType(GameQuizCard), findsOneWidget);
      expect(find.text('Question 1 / 10'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  }
}
