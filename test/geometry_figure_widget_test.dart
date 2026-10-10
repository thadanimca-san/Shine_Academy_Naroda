import 'dart:math' as math;

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

  test('axes include the origin with a unit of space', () {
    const data = {'axes': true, 'points': {'A': [2, 3], 'B': [5, 7]}};
    final bounds = geometryBounds(data, geometryPoints(data));
    expect(bounds, const Rect.fromLTRB(-1, -1, 6, 8));
  });

  testWidgets('draws a coordinate plane with labelled points', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: GeometryFigureWidget(data: {
      'title': 'Distance AB', 'axes': true, 'points': {'A': [2, 3], 'B': [-4, 1]}, 'segments': [['A', 'B']], 'labels': {'A': 'A(2, 3)', 'B': 'B(-4, 1)'},
    })))));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });

  testWidgets('draws a circle with a tangent', (tester) async {
    const data = {
      'title': 'Tangent at P',
      'points': {'O': [0, 0], 'P': [0, 3], 'T': [4, 3]},
      'circles': [{'centre': 'O', 'radius': 3, 'through': ['P']}],
      'segments': [['O', 'P'], ['P', 'T']],
      'right_angles': [['O', 'P', 'T']],
    };
    expect(geometryCircles(data).single.radius, 3);
    expect(geometryBounds(data, geometryPoints(data)).left, -3);
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: GeometryFigureWidget(data: data)))));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });

  testWidgets('shades a sector and a segment', (tester) async {
    const data = {
      'title': 'Sector and segment',
      'points': {'O': [0, 0], 'A': [3, 0], 'B': [0, 3], 'C': [-3, 0]},
      'circles': [{'centre': 'O', 'radius': 3, 'through': ['A', 'B', 'C']}],
      'shaded': [{'kind': 'sector', 'centre': 'O', 'from': 'A', 'to': 'B'}, {'kind': 'segment', 'centre': 'O', 'from': 'B', 'to': 'C'}, {'kind': 'arc', 'centre': 'O', 'from': 'C', 'to': 'A'}],
    };
    final regions = geometryRegions(data);
    expect(regions.first.isSector, isTrue);
    expect(regions.last.isArc, isTrue);
    final arc = regionArc(regions.first, geometryPoints(data), samples: 2);
    expect(arc[1].dx, closeTo(3 * math.cos(math.pi / 4), 1e-9));
    expect(arc[1].dy, closeTo(3 * math.sin(math.pi / 4), 1e-9), reason: 'anticlockwise from A to B');
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: GeometryFigureWidget(data: data)))));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });

  test('a corner sector only widens the figure by its arc', () {
    const data = {
      'points': {'A': [0, 0], 'P': [5, 0], 'Q': [0, 5], 'C': [15, 15]},
      'shaded': [{'kind': 'sector', 'centre': 'A', 'from': 'P', 'to': 'Q'}],
    };
    expect(geometryBounds(data, geometryPoints(data)).left, closeTo(0, 1e-9));
  });
}
