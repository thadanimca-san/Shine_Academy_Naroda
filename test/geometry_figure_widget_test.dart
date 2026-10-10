import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/geometry_figure_widget.dart';

const _bpt = {
  'title': 'DE parallel to BC',
  'points': {'A': [1, 4], 'B': [0, 0], 'C': [5, 0], 'D': [0.5, 2], 'E': [3, 2]},
  'segments': [['A', 'B'], ['B', 'C'], ['C', 'A'], {'from': 'D', 'to': 'E', 'highlight': true}],
  'parallel': [['D', 'E', 'B', 'C']],
  'angles': [{'points': ['B', 'A', 'C'], 'label': 'x'}],
  'lengths': [{'from': 'A', 'to': 'D', 'label': '1.5 cm'}],
};

void main() {
  test('reads points and both segment forms', () {
    expect(geometryPoints(_bpt)['E'], const Offset(3, 2));
    final segments = geometrySegments(_bpt);
    expect(segments, hasLength(4));
    expect(segments.last.highlight, isTrue);
  });

  test('detects parallel segments and right angles', () {
    expect(segmentsParallel(const Offset(0.5, 2), const Offset(3, 2), Offset.zero, const Offset(5, 0)), isTrue);
    expect(segmentsParallel(Offset.zero, const Offset(1, 1), Offset.zero, const Offset(1, 2)), isFalse);
    expect(isRightAngle(const Offset(0, 3), Offset.zero, const Offset(4, 0)), isTrue);
    expect(isRightAngle(const Offset(1, 3), Offset.zero, const Offset(4, 0)), isFalse);
  });

  testWidgets('draws and finishes the animation without errors', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: GeometryFigureWidget(data: _bpt)))));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    expect(find.text('DE parallel to BC'), findsOneWidget);
  });

  testWidgets('reduced motion shows the finished figure at once', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: MediaQuery(
        data: MediaQueryData(disableAnimations: true),
        child: Scaffold(body: SingleChildScrollView(child: GeometryFigureWidget(data: _bpt))),
      ),
    ));
    await tester.pump();
    expect(tester.hasRunningAnimations, isFalse);
  });
}
