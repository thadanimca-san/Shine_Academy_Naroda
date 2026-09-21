import 'dart:math' as math;
import 'dart:ui' as ui;
import 'package:flutter/material.dart';

/// The biological shapes an [Organelle] can be rendered as. Each one gets a
/// hand-drawn silhouette (folded mitochondrial cristae, stacked Golgi
/// cisternae, a branching rough-ER network attached to the nucleus, etc.)
/// instead of a generic circle, so diagrams read like a real textbook
/// illustration rather than clip-art.
enum OrganelleShape { membrane, wall, nucleus, mitochondrion, reticulum, golgi, chloroplast, vacuole, lysosome, ribosomeCluster, cytoplasm }

class Organelle {
  final String name;
  final String label; // short tag drawn directly on the diagram
  final String function;
  final Color color;
  final Alignment center;
  final double scale;
  final OrganelleShape shape;

  const Organelle(this.name, this.label, this.function, this.color, this.center, this.scale, this.shape);
}

/// Returns this organelle's bounding box in canvas pixels. Shared by the
/// painter and the tap-hit overlay so what's drawn is exactly what's tappable.
Rect organelleRect(Size size, Organelle o) {
  final unit = size.height;
  late double w, h;
  switch (o.shape) {
    case OrganelleShape.membrane:
      w = size.width * 0.94;
      h = size.height * 0.94;
      break;
    case OrganelleShape.wall:
      w = size.width * 0.98;
      h = size.height * 0.98;
      break;
    case OrganelleShape.nucleus:
      w = h = o.scale * 0.42 * unit;
      break;
    case OrganelleShape.mitochondrion:
      w = o.scale * 0.5 * unit;
      h = o.scale * 0.22 * unit;
      break;
    case OrganelleShape.reticulum:
      w = o.scale * 0.5 * unit;
      h = o.scale * 0.46 * unit;
      break;
    case OrganelleShape.golgi:
      w = o.scale * 0.5 * unit;
      h = o.scale * 0.3 * unit;
      break;
    case OrganelleShape.chloroplast:
      w = o.scale * 0.44 * unit;
      h = o.scale * 0.22 * unit;
      break;
    case OrganelleShape.vacuole:
      w = o.scale * 0.56 * unit;
      h = o.scale * 0.5 * unit;
      break;
    case OrganelleShape.lysosome:
      w = h = o.scale * 0.14 * unit;
      break;
    case OrganelleShape.ribosomeCluster:
      w = h = o.scale * 0.3 * unit;
      break;
    case OrganelleShape.cytoplasm:
      w = h = 0.001;
      break;
  }
  final cx = size.width / 2 + o.center.x * size.width / 2 * 0.82;
  final cy = size.height / 2 + o.center.y * size.height / 2 * 0.82;
  return Rect.fromCenter(center: Offset(cx, cy), width: w, height: h);
}

/// A tappable, textbook-style labeled cell diagram. Draws whichever
/// [organelles] are passed in as their real biological shapes, highlights
/// [selected] with a soft glow, and reports taps via [onSelect]. Reused by
/// both the Class 8 (simplified) and Class 9 (full-detail) cell simulations
/// so their diagrams stay visually consistent.
class OrganelleDiagramView extends StatelessWidget {
  final bool isPlantCell;
  final List<Organelle> organelles;
  final Organelle? selected;
  final ValueChanged<Organelle> onSelect;

  const OrganelleDiagramView({
    super.key,
    required this.isPlantCell,
    required this.organelles,
    required this.selected,
    required this.onSelect,
  });

  @override
  Widget build(BuildContext context) {
    // Draw large background structures first so smaller organelles sit on top.
    final drawOrder = [...OrganelleShape.values].asMap().map((i, s) => MapEntry(s, i));
    final sorted = [...organelles]..sort((a, b) => drawOrder[a.shape]!.compareTo(drawOrder[b.shape]!));
    final hasCytoplasmTag = organelles.any((o) => o.shape == OrganelleShape.cytoplasm);

    return AspectRatio(
      aspectRatio: 1.5,
      child: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Colors.green.shade50, Colors.teal.shade50],
          ),
          borderRadius: BorderRadius.circular(12),
        ),
        clipBehavior: Clip.antiAlias,
        child: LayoutBuilder(
          builder: (context, constraints) {
            final canvasSize = Size(constraints.maxWidth, constraints.maxHeight);
            return Stack(
              children: [
                Positioned.fill(
                  child: CustomPaint(
                    painter: CellDiagramPainter(
                      isPlantCell: isPlantCell,
                      organelles: sorted,
                      selectedName: selected?.name,
                    ),
                  ),
                ),
                ...organelles
                    .where((o) => o.shape != OrganelleShape.cytoplasm && o.shape != OrganelleShape.membrane && o.shape != OrganelleShape.wall)
                    .map((o) {
                  final rect = organelleRect(canvasSize, o);
                  return Positioned.fromRect(
                    rect: rect,
                    child: GestureDetector(
                      behavior: HitTestBehavior.translucent,
                      onTap: () => onSelect(o),
                    ),
                  );
                }),
                // Cytoplasm's "hit box" is a discreet tappable area near its
                // on-canvas tag, since it has no drawn shape of its own.
                if (hasCytoplasmTag)
                  Builder(builder: (context) {
                    final cytoplasm = organelles.firstWhere((o) => o.shape == OrganelleShape.cytoplasm);
                    final rect = organelleRect(canvasSize, cytoplasm).inflate(22);
                    return Positioned.fromRect(
                      rect: rect,
                      child: GestureDetector(
                        behavior: HitTestBehavior.translucent,
                        onTap: () => onSelect(cytoplasm),
                      ),
                    );
                  }),
              ],
            );
          },
        ),
      ),
    );
  }
}

class CellDiagramPainter extends CustomPainter {
  final bool isPlantCell;
  final List<Organelle> organelles;
  final String? selectedName;

  CellDiagramPainter({required this.isPlantCell, required this.organelles, required this.selectedName});

  @override
  void paint(Canvas canvas, Size size) {
    final outerRect = Rect.fromCenter(center: size.center(Offset.zero), width: size.width * (isPlantCell ? 0.98 : 0.94), height: size.height * (isPlantCell ? 0.98 : 0.94));

    if (isPlantCell) {
      _drawCellWall(canvas, outerRect);
    } else {
      _drawCellMembrane(canvas, outerRect);
    }
    _scatterRibosomes(canvas, outerRect);

    // The rough ER visually grows out of the nuclear envelope in a real
    // cell — draw a connecting membrane between them before anything else,
    // so the reticulum reads as attached rather than floating in space.
    final nucleusMatches = organelles.where((o) => o.shape == OrganelleShape.nucleus);
    final reticulumMatches = organelles.where((o) => o.shape == OrganelleShape.reticulum);
    if (nucleusMatches.isNotEmpty && reticulumMatches.isNotEmpty) {
      final nucleus = nucleusMatches.first;
      final reticulum = reticulumMatches.first;
      _drawNucleusToERBridge(canvas, organelleRect(size, nucleus), organelleRect(size, reticulum), reticulum.color, reticulum.name == selectedName);
    }

    for (final o in organelles) {
      final rect = organelleRect(size, o);
      final emphasize = o.name == selectedName;
      switch (o.shape) {
        case OrganelleShape.membrane:
        case OrganelleShape.wall:
        case OrganelleShape.cytoplasm:
          break; // handled above / as a corner tag below
        case OrganelleShape.nucleus:
          _drawNucleus(canvas, rect, o.color, emphasize);
          break;
        case OrganelleShape.mitochondrion:
          _drawMitochondrion(canvas, rect, o.color, emphasize);
          _drawMitochondrion(canvas, rect.translate(-rect.width * 0.25, -rect.height * 0.85), o.color, false, decorative: true);
          break;
        case OrganelleShape.reticulum:
          _drawReticulum(canvas, rect, o.color, emphasize);
          break;
        case OrganelleShape.golgi:
          _drawGolgi(canvas, rect, o.color, emphasize);
          break;
        case OrganelleShape.chloroplast:
          _drawChloroplast(canvas, rect, o.color, emphasize);
          _drawChloroplast(canvas, rect.translate(-rect.width * 0.25, rect.height * 0.85), o.color, false, decorative: true);
          break;
        case OrganelleShape.vacuole:
          _drawVacuole(canvas, rect, o.color, emphasize);
          break;
        case OrganelleShape.lysosome:
          _drawLysosome(canvas, rect, o.color, emphasize);
          break;
        case OrganelleShape.ribosomeCluster:
          _drawRibosomeCluster(canvas, rect, o.color, emphasize);
          break;
      }
      if (o.shape != OrganelleShape.membrane && o.shape != OrganelleShape.wall) {
        _drawLabel(canvas, rect, o.label, o.color);
      }
    }

    // Corner tag for the whole-cell boundary, which has no single rect.
    final boundaryLabel = isPlantCell ? 'Cell Wall' : 'Cell Membrane';
    final boundaryColor = isPlantCell ? const Color(0xFF8D6E63) : const Color(0xFF9575CD);
    _drawLabel(canvas, Rect.fromLTWH(outerRect.left + 6, outerRect.top + 6, 0, 0), boundaryLabel, boundaryColor, anchorBelow: false);
  }

  void _glow(Canvas canvas, Offset center, double radius, Color color) {
    final glowPaint = Paint()
      ..color = color.withValues(alpha: 0.45)
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 10);
    canvas.drawCircle(center, radius, glowPaint);
  }

  /// A soft drop shadow beneath a filled shape, so organelles feel like
  /// they sit inside the cytoplasm rather than being pasted flat onto it.
  void _shadow(Canvas canvas, Path path, {Offset offset = const Offset(1.5, 2.5)}) {
    canvas.drawPath(
      path.shift(offset),
      Paint()
        ..color = Colors.black.withValues(alpha: 0.10)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 3),
    );
  }

  void _drawCellWall(Canvas canvas, Rect rect) {
    final rrect = RRect.fromRectAndRadius(rect, Radius.circular(rect.shortestSide * 0.08));
    canvas.drawRRect(rrect, Paint()..color = const Color(0xFFF1E8DC));
    canvas.drawRRect(rrect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 6
      ..color = const Color(0xFF8D6E63));
    // Inner plasma membrane, just inside the rigid wall.
    final inner = rect.deflate(rect.shortestSide * 0.045);
    final innerRRect = RRect.fromRectAndRadius(inner, Radius.circular(inner.shortestSide * 0.08));
    canvas.drawRRect(innerRRect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.6
      ..color = const Color(0xFF9575CD).withValues(alpha: 0.7));
  }

  void _drawCellMembrane(Canvas canvas, Rect rect) {
    // An organic, slightly irregular outline — real animal cells aren't
    // perfect circles or rounded rectangles. Bumpy radii at evenly spaced
    // angles are joined with quadratic curves through their midpoints
    // (a simple Catmull-Rom-style smoothing) for a soft, cell-like blob.
    final cx = rect.center.dx, cy = rect.center.dy;
    final rx = rect.width / 2, ry = rect.height / 2;
    const bumps = [1.0, 1.05, 0.95, 1.08, 0.97, 1.03, 0.94, 1.06, 1.0, 0.96, 1.04, 0.98];
    final points = <Offset>[
      for (int i = 0; i < bumps.length; i++)
        Offset(
          cx + rx * bumps[i] * math.cos(i / bumps.length * 2 * math.pi),
          cy + ry * bumps[i] * math.sin(i / bumps.length * 2 * math.pi),
        ),
    ];

    final path = Path()..moveTo((points[0].dx + points.last.dx) / 2, (points[0].dy + points.last.dy) / 2);
    for (int i = 0; i < points.length; i++) {
      final curr = points[i];
      final next = points[(i + 1) % points.length];
      final mid = Offset((curr.dx + next.dx) / 2, (curr.dy + next.dy) / 2);
      path.quadraticBezierTo(curr.dx, curr.dy, mid.dx, mid.dy);
    }
    path.close();

    canvas.drawPath(path, Paint()
      ..shader = ui.Gradient.radial(rect.center, rect.longestSide * 0.6, [const Color(0xFFFAF3FB), const Color(0xFFEDE0F5)]));
    canvas.drawPath(path, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..color = const Color(0xFF9575CD));
  }

  void _scatterRibosomes(Canvas canvas, Rect rect) {
    // A denser, evenly-spread field of free-ribosome dots so the cytoplasm
    // reads as a busy, fluid-filled interior rather than empty white space.
    final rnd = math.Random(7); // fixed seed: identical every rebuild, no shimmer
    final dotPaint = Paint()..color = Colors.black.withValues(alpha: 0.22);
    for (int i = 0; i < 42; i++) {
      final fx = (rnd.nextDouble() - 0.5) * 1.7;
      final fy = (rnd.nextDouble() - 0.5) * 1.7;
      final p = Offset(rect.center.dx + fx * rect.width / 2, rect.center.dy + fy * rect.height / 2);
      if (!rect.deflate(rect.shortestSide * 0.03).contains(p)) continue;
      canvas.drawCircle(p, 1.1 + rnd.nextDouble() * 0.7, dotPaint);
    }
  }

  void _drawNucleusToERBridge(Canvas canvas, Rect nucleusRect, Rect erRect, Color color, bool emphasize) {
    final start = Offset(
      nucleusRect.center.dx + (erRect.center.dx - nucleusRect.center.dx).sign * nucleusRect.width * 0.42,
      nucleusRect.center.dy + (erRect.center.dy - nucleusRect.center.dy).sign * nucleusRect.height * 0.3,
    );
    final end = Offset(erRect.center.dx - erRect.width * 0.3, erRect.center.dy - erRect.height * 0.3);
    final path = Path()
      ..moveTo(start.dx, start.dy)
      ..quadraticBezierTo((start.dx + end.dx) / 2, (start.dy + end.dy) / 2 - 6, end.dx, end.dy);
    canvas.drawPath(path, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 5 : 3.5
      ..strokeCap = StrokeCap.round
      ..color = color.withValues(alpha: emphasize ? 0.9 : 0.55));
  }

  void _drawNucleus(Canvas canvas, Rect rect, Color color, bool emphasize) {
    if (emphasize) _glow(canvas, rect.center, rect.shortestSide * 0.68, color);
    final outerPath = Path()..addOval(rect);
    _shadow(canvas, outerPath);

    // Nuclear envelope: a double membrane with small pores, not a single flat ring.
    canvas.drawOval(rect, Paint()..shader = ui.Gradient.radial(rect.center - Offset(rect.width * 0.15, rect.height * 0.15), rect.longestSide * 0.75, [
      Color.lerp(color, Colors.white, 0.25)!.withValues(alpha: 0.92),
      color.withValues(alpha: 0.92),
    ]));
    final innerEnvelope = rect.deflate(rect.shortestSide * 0.05);
    canvas.drawOval(innerEnvelope, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.2
      ..color = Colors.white.withValues(alpha: 0.55));
    canvas.drawOval(rect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.8 : 1.8
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95));
    // Nuclear pores: small notches crossing the double membrane.
    final porePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4
      ..color = Colors.white.withValues(alpha: 0.85);
    for (int i = 0; i < 8; i++) {
      final angle = i / 8 * 2 * math.pi + 0.3;
      final p1 = rect.center + Offset(math.cos(angle), math.sin(angle)) * (rect.shortestSide / 2 - 1);
      final p2 = rect.center + Offset(math.cos(angle), math.sin(angle)) * (rect.shortestSide / 2 - 5);
      canvas.drawLine(p1, p2, porePaint);
    }

    // Chromatin: irregular blobby threads, not clean parallel sine lines.
    final rnd = math.Random(rect.center.dx.toInt());
    final chromatinPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.2
      ..strokeCap = StrokeCap.round
      ..color = Colors.white.withValues(alpha: 0.4);
    for (int i = 0; i < 5; i++) {
      final start = rect.center + Offset((rnd.nextDouble() - 0.5) * rect.width * 0.6, (rnd.nextDouble() - 0.5) * rect.height * 0.6);
      final path = Path()..moveTo(start.dx, start.dy);
      var p = start;
      for (int seg = 0; seg < 3; seg++) {
        final next = p + Offset((rnd.nextDouble() - 0.5) * rect.width * 0.25, (rnd.nextDouble() - 0.5) * rect.height * 0.25);
        final ctrl = Offset.lerp(p, next, 0.5)! + Offset((rnd.nextDouble() - 0.5) * 10, (rnd.nextDouble() - 0.5) * 10);
        path.quadraticBezierTo(ctrl.dx, ctrl.dy, next.dx, next.dy);
        p = next;
      }
      canvas.drawPath(path, chromatinPaint);
    }

    // Nucleolus, prominent with a subtle inner gradient.
    final nucleolusCenter = Offset(rect.center.dx + rect.width * 0.14, rect.center.dy - rect.height * 0.08);
    final nucleolusRadius = rect.shortestSide * 0.19;
    canvas.drawCircle(nucleolusCenter, nucleolusRadius, Paint()
      ..shader = ui.Gradient.radial(nucleolusCenter - Offset(nucleolusRadius * 0.3, nucleolusRadius * 0.3), nucleolusRadius * 1.3, [
        Color.lerp(color, Colors.black, 0.15)!,
        Color.lerp(color, Colors.black, 0.4)!,
      ]));
    canvas.drawCircle(nucleolusCenter, nucleolusRadius, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1
      ..color = Colors.black.withValues(alpha: 0.35));

    // Sub-structure call-outs so the parts inside "Nucleus" are individually
    // named, the way a textbook figure would label them — even though they
    // share the Nucleus's single tap target and function description.
    _calloutLine(canvas, nucleolusCenter, nucleolusCenter + Offset(rect.width * 0.42, -rect.height * 0.05), 'Nucleolus', Colors.black87);
    final membranePoint = rect.center + Offset(rect.width * 0.35, rect.height * 0.38);
    _calloutLine(canvas, membranePoint, membranePoint + Offset(rect.width * 0.28, rect.height * 0.18), 'Nuclear\nMembrane', Colors.black87);
    final chromatinPoint = rect.center + Offset(-rect.width * 0.28, -rect.height * 0.3);
    _calloutLine(canvas, chromatinPoint, chromatinPoint + Offset(-rect.width * 0.32, -rect.height * 0.12), 'Chromatin', Colors.black87);
  }

  void _calloutLine(Canvas canvas, Offset from, Offset to, String text, Color textColor) {
    canvas.drawLine(from, to, Paint()
      ..strokeWidth = 1
      ..color = Colors.black45);
    canvas.drawCircle(from, 1.6, Paint()..color = Colors.black45);
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 8, fontWeight: FontWeight.w600, color: textColor, height: 1.05)),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 60);
    final pos = Offset(to.dx - tp.width / 2, to.dy - tp.height / 2);
    final bg = Rect.fromLTWH(pos.dx - 2, pos.dy - 1, tp.width + 4, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(3)), Paint()..color = Colors.white.withValues(alpha: 0.9));
    tp.paint(canvas, pos);
  }

  void _drawMitochondrion(Canvas canvas, Rect rect, Color color, bool emphasize, {bool decorative = false}) {
    if (emphasize) _glow(canvas, rect.center, rect.longestSide * 0.62, color);
    final rrect = RRect.fromRectAndRadius(rect, Radius.circular(rect.height / 2));
    _shadow(canvas, Path()..addRRect(rrect));
    canvas.drawRRect(rrect, Paint()
      ..shader = ui.Gradient.linear(rect.topLeft, rect.bottomRight, [
        Color.lerp(color, Colors.white, 0.2)!.withValues(alpha: decorative ? 0.65 : 0.92),
        color.withValues(alpha: decorative ? 0.55 : 0.85),
      ]));
    canvas.drawRRect(rrect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.4 : 1.4
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95));
    // Cristae — the folded inner-membrane ridges that make a mitochondrion
    // recognisable. Irregular in spacing, depth and length, alternating
    // from both long edges so they read as packed folds filling the
    // interior rather than a few neat symmetric arcs.
    final cristaePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.3
      ..strokeCap = StrokeCap.round
      ..color = Colors.white.withValues(alpha: decorative ? 0.5 : 0.78);
    final rnd = math.Random(rect.center.dx.toInt() + rect.center.dy.toInt());
    final n = 7;
    for (int i = 1; i < n; i++) {
      final x = rect.left + rect.width * i / n + (rnd.nextDouble() - 0.5) * rect.width * 0.03;
      final fromTop = i.isOdd;
      final depth = rect.height * (0.55 + rnd.nextDouble() * 0.25);
      final path = Path();
      if (fromTop) {
        path.moveTo(x, rect.top + rect.height * 0.1);
        path.quadraticBezierTo(x + (rnd.nextDouble() - 0.5) * rect.width * 0.12, rect.top + depth * 0.5, x + (rnd.nextDouble() - 0.5) * rect.width * 0.06, rect.top + depth);
      } else {
        path.moveTo(x, rect.bottom - rect.height * 0.1);
        path.quadraticBezierTo(x + (rnd.nextDouble() - 0.5) * rect.width * 0.12, rect.bottom - depth * 0.5, x + (rnd.nextDouble() - 0.5) * rect.width * 0.06, rect.bottom - depth);
      }
      canvas.drawPath(path, cristaePaint);
    }
  }

  void _drawReticulum(Canvas canvas, Rect rect, Color color, bool emphasize) {
    if (emphasize) _glow(canvas, rect.center, rect.longestSide * 0.6, color);
    final fill = Paint()..color = color.withValues(alpha: 0.16);
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.6 : 1.7
      ..strokeCap = StrokeCap.round
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95);

    // A branching membrane network (not repeated identical strips): a
    // handful of curved tubules fanning out and reconnecting, the way ER
    // actually looks under a microscope. The two branches nearest the
    // nucleus are rough ER (ribosome-studded); the two further out are
    // smooth ER (bare membrane) — a real, examinable distinction.
    final rnd = math.Random(rect.center.dy.toInt());
    final start = Offset(rect.left, rect.center.dy);
    final branchEnds = <Offset>[];
    for (int i = 0; i < 4; i++) {
      final endY = rect.top + rect.height * (0.15 + i * 0.24);
      final end = Offset(rect.right - rect.width * (0.05 + rnd.nextDouble() * 0.15), endY);
      branchEnds.add(end);
      final ctrl1 = Offset(rect.left + rect.width * 0.35, rect.top + rect.height * (0.1 + i * 0.28));
      final ctrl2 = Offset(rect.left + rect.width * 0.7, endY + (rnd.nextDouble() - 0.5) * rect.height * 0.15);
      final path = Path()..moveTo(start.dx, start.dy)..cubicTo(ctrl1.dx, ctrl1.dy, ctrl2.dx, ctrl2.dy, end.dx, end.dy);
      canvas.drawPath(path, fill..style = PaintingStyle.stroke..strokeWidth = rect.height * 0.16);
      canvas.drawPath(path, stroke);
    }
    // Cross-links between adjacent tubules so it reads as a connected sheet.
    for (int i = 0; i < branchEnds.length - 1; i++) {
      final a = branchEnds[i], b = branchEnds[i + 1];
      final mid1 = Offset.lerp(a, b, 0.35)!;
      final mid2 = Offset.lerp(a, b, 0.65)!;
      canvas.drawPath(Path()..moveTo(a.dx, a.dy)..quadraticBezierTo(mid1.dx, mid1.dy, mid2.dx, mid2.dy)..lineTo(b.dx, b.dy), Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.2
        ..color = color.withValues(alpha: 0.4));
    }
    // Ribosome studs along the first two (rough ER) tubules only.
    final dotPaint = Paint()..color = Colors.black.withValues(alpha: 0.5);
    for (int i = 0; i < 2; i++) {
      final end = branchEnds[i];
      for (int d = 0; d < 4; d++) {
        canvas.drawCircle(end + Offset(-7.0 * d, -3 + rnd.nextDouble() * 2), 1.3, dotPaint);
      }
    }
    _calloutLine(canvas, branchEnds[0] + const Offset(-14, 0), branchEnds[0] + const Offset(-30, -14), 'Rough ER', Colors.black87);
    _calloutLine(canvas, branchEnds[3], branchEnds[3] + const Offset(14, 10), 'Smooth ER', Colors.black87);
  }

  void _drawGolgi(Canvas canvas, Rect rect, Color color, bool emphasize) {
    if (emphasize) _glow(canvas, rect.center, rect.longestSide * 0.6, color);
    final fill = Paint()..color = color.withValues(alpha: emphasize ? 1.0 : 0.82);
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.2 : 1.4
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95);

    // A genuine stacked-cisternae body: filled crescent bands, each a real
    // closed shape (not a bare stroked arc), stacked with a slight offset.
    const layers = 5;
    Offset lastTip = rect.topLeft;
    for (int i = 0; i < layers; i++) {
      final t = i / (layers - 1);
      final w = rect.width * (1 - t * 0.4);
      final layerRect = Rect.fromCenter(center: Offset(rect.center.dx - t * rect.width * 0.05, rect.top + rect.height * (0.22 + t * 0.56)), width: w, height: rect.height * 0.2);
      final path = Path()
        ..moveTo(layerRect.left, layerRect.center.dy)
        ..quadraticBezierTo(layerRect.center.dx, layerRect.top, layerRect.right, layerRect.center.dy)
        ..quadraticBezierTo(layerRect.center.dx, layerRect.top + layerRect.height * 0.55, layerRect.left, layerRect.center.dy)
        ..close();
      if (i == 0) _shadow(canvas, path, offset: const Offset(1, 1.5));
      canvas.drawPath(path, fill);
      canvas.drawPath(path, stroke);
      if (i == layers - 1) lastTip = layerRect.centerRight;
    }
    // Budding vesicles pinching off the last cisterna, connected by a short thread.
    final vesiclePaint = Paint()..color = color.withValues(alpha: 0.85);
    final v1 = lastTip + const Offset(10, 6);
    final v2 = lastTip + const Offset(16, 16);
    canvas.drawLine(lastTip, v1, Paint()..strokeWidth = 1.2..color = color.withValues(alpha: 0.6));
    canvas.drawLine(v1, v2, Paint()..strokeWidth = 1.2..color = color.withValues(alpha: 0.6));
    canvas.drawCircle(v1, 3, vesiclePaint);
    canvas.drawCircle(v2, 2.4, vesiclePaint);
  }

  void _drawChloroplast(Canvas canvas, Rect rect, Color color, bool emphasize, {bool decorative = false}) {
    if (emphasize) _glow(canvas, rect.center, rect.longestSide * 0.6, color);
    final rrect = RRect.fromRectAndRadius(rect, Radius.circular(rect.height / 2));
    _shadow(canvas, Path()..addRRect(rrect));
    canvas.drawRRect(rrect, Paint()
      ..shader = ui.Gradient.linear(rect.topLeft, rect.bottomRight, [
        Color.lerp(color, Colors.white, 0.2)!.withValues(alpha: decorative ? 0.65 : 0.92),
        color.withValues(alpha: decorative ? 0.55 : 0.85),
      ]));
    canvas.drawRRect(rrect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.4 : 1.4
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95));
    // Grana — stacks of thylakoid discs, the hallmark of a chloroplast.
    final granaPaint = Paint()..color = Colors.white.withValues(alpha: decorative ? 0.5 : 0.7);
    for (final dx in [-0.25, 0.0, 0.25]) {
      final cx = rect.center.dx + dx * rect.width * 0.7;
      for (int i = 0; i < 3; i++) {
        final cy = rect.center.dy - rect.height * 0.18 + i * rect.height * 0.18;
        canvas.drawRect(Rect.fromCenter(center: Offset(cx, cy), width: rect.width * 0.12, height: rect.height * 0.14), granaPaint);
      }
    }
  }

  void _drawVacuole(Canvas canvas, Rect rect, Color color, bool emphasize) {
    if (emphasize) _glow(canvas, rect.center, rect.longestSide * 0.58, color);
    canvas.drawOval(rect, Paint()..color = color.withValues(alpha: 0.22));
    canvas.drawOval(rect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.4 : 1.5
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.9));
    // A faint highlight to suggest the watery cell sap inside.
    canvas.drawOval(rect.deflate(rect.shortestSide * 0.18).translate(-rect.width * 0.08, -rect.height * 0.08), Paint()..color = Colors.white.withValues(alpha: 0.25));
  }

  void _drawLysosome(Canvas canvas, Rect rect, Color color, bool emphasize) {
    // Lysosomes really are simple round membrane-bound sacs, so a filled
    // circle is biologically accurate here — unlike organelles with a
    // distinctive shape, this one earns its circle.
    if (emphasize) _glow(canvas, rect.center, rect.shortestSide * 0.9, color);
    _shadow(canvas, Path()..addOval(rect));
    canvas.drawOval(rect, Paint()
      ..shader = ui.Gradient.radial(rect.center - Offset(rect.width * 0.2, rect.height * 0.2), rect.longestSide * 0.7, [
        Color.lerp(color, Colors.white, 0.25)!,
        color,
      ]));
    canvas.drawOval(rect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.2 : 1.3
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95));
    // Digestive enzyme granules inside.
    final rnd = math.Random(rect.center.dx.toInt() + 3);
    final granulePaint = Paint()..color = Colors.white.withValues(alpha: 0.55);
    for (int i = 0; i < 4; i++) {
      canvas.drawCircle(rect.center + Offset((rnd.nextDouble() - 0.5) * rect.width * 0.4, (rnd.nextDouble() - 0.5) * rect.height * 0.4), 1.2, granulePaint);
    }
    // A couple of smaller companion lysosomes, since these are usually numerous.
    canvas.drawCircle(rect.center + Offset(rect.width * 0.75, rect.height * 0.55), rect.shortestSide * 0.32, Paint()..color = color.withValues(alpha: 0.7));
    canvas.drawCircle(rect.center + Offset(-rect.width * 0.7, rect.height * 0.6), rect.shortestSide * 0.24, Paint()..color = color.withValues(alpha: 0.6));
  }

  void _drawRibosomeCluster(Canvas canvas, Rect rect, Color color, bool emphasize) {
    if (emphasize) _glow(canvas, rect.center, rect.shortestSide * 0.75, color);
    final rnd = math.Random(11);
    final paint = Paint()..color = color.withValues(alpha: emphasize ? 1.0 : 0.85);
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 1.4 : 0.8
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.9);
    for (int i = 0; i < 10; i++) {
      final p = rect.center + Offset((rnd.nextDouble() - 0.5) * rect.width * 0.85, (rnd.nextDouble() - 0.5) * rect.height * 0.85);
      final r = rect.shortestSide * (0.05 + rnd.nextDouble() * 0.04);
      canvas.drawCircle(p, r, paint);
      canvas.drawCircle(p, r, stroke);
    }
  }

  void _drawLabel(Canvas canvas, Rect rect, String text, Color color, {bool anchorBelow = true}) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.w700, color: Colors.black87)),
      textDirection: TextDirection.ltr,
    )..layout();
    final pos = anchorBelow ? Offset(rect.center.dx - tp.width / 2, rect.bottom + 2) : Offset(rect.left, rect.top);
    // A short leader line whenever the label sits outside the shape it
    // names, so nothing reads as an orphaned, unattached tag.
    if (anchorBelow && rect.height > 1 && pos.dy - rect.bottom > 3) {
      canvas.drawLine(Offset(rect.center.dx, rect.bottom), Offset(pos.dx + tp.width / 2, pos.dy), Paint()
        ..strokeWidth = 1
        ..color = color.withValues(alpha: 0.5));
    }
    final bgRect = Rect.fromLTWH(pos.dx - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bgRect, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.85));
    canvas.drawRRect(RRect.fromRectAndRadius(bgRect, const Radius.circular(4)), Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 0.8
      ..color = color.withValues(alpha: 0.6));
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant CellDiagramPainter oldDelegate) =>
      oldDelegate.isPlantCell != isPlantCell || oldDelegate.selectedName != selectedName;
}
