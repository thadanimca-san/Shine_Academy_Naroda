import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

Widget _host(String text) => MaterialApp(
      home: Scaffold(
        body: TtsInteractiveText(text: text, style: const TextStyle(fontSize: 16)),
      ),
    );

/// The plain text drawn by every RichText under the widget, joined together.
String _visibleText(WidgetTester tester) => tester
    .widgetList<RichText>(find.descendant(of: find.byType(TtsInteractiveText), matching: find.byType(RichText)))
    .map((richText) => richText.text.toPlainText())
    .join();

void main() {
  group('repairLatexEscapes', () {
    test('restores commands broken by single-backslash JSON', () {
      expect(repairLatexEscapes('\frac{1}{2}'), r'\frac{1}{2}');
      expect(repairLatexEscapes('3 \times 4'), r'3 \times 4');
      expect(repairLatexEscapes('x \neq 0'), r'x \neq 0');
      expect(repairLatexEscapes('\beta + \right)'), r'\beta + \right)');
    });

    test('leaves correct LaTeX unchanged', () {
      const tex = r'\frac{a}{b} \times \sqrt{2} \neq 0';
      expect(repairLatexEscapes(tex), tex);
    });

    test('keeps real line breaks inside multi-line formulas', () {
      const tex = 'a = 1 \\\\\nb = 2';
      expect(repairLatexEscapes(tex), tex);
    });
  });

  group('normalizeMarkdownLines', () {
    test('turns bullets into dots and headings into bold lines', () {
      expect(
        normalizeMarkdownLines('## Key Points\n- first\n* second\n**Bold** stays'),
        '**Key Points**\n• first\n• second\n**Bold** stays',
      );
    });

    test('does not touch lines inside display formulas', () {
      const text = r'$$' '\n- x\n' r'$$';
      expect(normalizeMarkdownLines(text), text);
    });
  });

  testWidgets('draws inline and display LaTeX with the math engine', (tester) async {
    await tester.pumpWidget(_host(r'HCF is $\frac{a}{b}$ and $$x^2 + y^2 = r^2$$ done'));

    expect(find.byType(Math), findsNWidgets(2));
    expect(tester.takeException(), isNull);
    expect(_visibleText(tester), contains('HCF'));
    expect(_visibleText(tester), contains('done'));
  });

  testWidgets('falls back to the raw formula instead of crashing on bad LaTeX', (tester) async {
    await tester.pumpWidget(_host(r'Broken $\frac{1}{$ formula'));

    expect(tester.takeException(), isNull);
    expect(find.text(r'\frac{1}{'), findsOneWidget);
  });

  testWidgets('bullets are drawn as dots, not italic text', (tester) async {
    await tester.pumpWidget(_host('Key points:\n* remainder is less than b\n* q is unique'));

    final text = _visibleText(tester);
    expect(text, contains('• remainder'));
    expect(text, isNot(contains('*')));
  });
}
