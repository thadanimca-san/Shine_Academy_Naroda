import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/services/tts_service.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

/// The words of [text] as the speech engine counts them.
List<String> spokenWords(String text) => [for (final w in ttsWordSpans(text)) text.substring(w.start, w.end)];

/// Shows [shown], pretends the engine is saying word [index] of [spoken], and
/// returns the highlighted words.
Future<List<String>> highlighted(WidgetTester tester, String shown, String spoken, int index) async {
  final tts = TTSService.instance;
  tts.progress.value = TtsProgress.empty;
  await tester.pumpWidget(MaterialApp(home: Scaffold(body: TtsInteractiveText(text: shown))));
  tts.isPlayingGlobal.value = true;
  final ws = ttsWordSpans(spoken);
  tts.progress.value = TtsProgress(
      text: spoken, startOffset: ws[index].start, endOffset: ws[index].end, word: spoken.substring(ws[index].start, ws[index].end), wordIndex: index);
  await tester.pump();
  final out = <String>[];
  final rich = tester.widget<RichText>(find.byType(RichText).first);
  rich.text.visitChildren((span) {
    if (span is TextSpan && span.style?.backgroundColor == Colors.yellow) out.add(span.text ?? '');
    return true;
  });
  tts.isPlayingGlobal.value = false;
  tts.progress.value = TtsProgress.empty;
  return out;
}

void main() {
  test('speech and screen split words the same way', () {
    expect(spokenWords("Don't stop—go!"), ['Don', 't', 'stop', 'go']);
    expect(spokenWords('• Rain fell.\n- The crop died.'), ['Rain', 'fell', 'The', 'crop', 'died']);
    expect(ttsWordKey('- **Rain** fell.'), ttsWordKey('• Rain fell'));
  });

  testWidgets('highlights the spoken word in a bulleted block', (tester) async {
    const shown = '- Rain fell.\n- **The** crop died.';
    expect(await highlighted(tester, shown, '- Rain fell.\n- The crop died.', 3), ['crop']);
  });

  testWidgets('finds the block inside a longer reading (title + body)', (tester) async {
    expect(await highlighted(tester, 'Rain fell. The crop died.', 'A Letter to God. Rain fell. The crop died.', 7), ['crop']);
  });

  testWidgets('double-tap reading from the middle highlights the right word', (tester) async {
    expect(await highlighted(tester, 'Rain fell. The crop died.', 'crop died.', 0), ['crop']);
  });

  testWidgets('other blocks stay unlit', (tester) async {
    expect(await highlighted(tester, 'Rain fell. The crop died.', 'Something else is being read.', 1), isEmpty);
  });
}
