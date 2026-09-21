import 'package:flutter/material.dart';
import '../common/diagram_helpers.dart';
import '../common/sim_frame.dart';

enum _View { neuron, reflexArc, brain }

/// Real, labeled diagrams for the nervous system topics of Control and
/// Coordination — a neuron's structure, the full reflex-arc pathway (not
/// just a step-by-step icon list), and the three main regions of the human
/// brain — each tappable to reveal its function.
class ControlCoordinationSimulationWidget extends StatefulWidget {
  const ControlCoordinationSimulationWidget({super.key});

  @override
  State<ControlCoordinationSimulationWidget> createState() => _ControlCoordinationSimulationWidgetState();
}

class _ControlCoordinationSimulationWidgetState extends State<ControlCoordinationSimulationWidget> {
  _View _view = _View.neuron;
  DiagramPart? _selected;

  static const _neuronParts = [
    DiagramPart(name: 'Dendrites', label: 'Dendrites', color: Color(0xFF43A047), function: 'Branched extensions that receive nerve impulses from other neurons and carry them toward the cell body.'),
    DiagramPart(name: 'Cell Body', label: 'Cell Body', color: Color(0xFF5C6BC0), function: 'Contains the nucleus and cytoplasm; it processes incoming signals and sustains the neuron\'s life processes.'),
    DiagramPart(name: 'Axon', label: 'Axon', color: Color(0xFFEF6C00), function: 'A long fibre that carries the nerve impulse away from the cell body toward the axon terminals.'),
    DiagramPart(name: 'Myelin Sheath', label: 'Myelin Sheath', color: Color(0xFFFFCA28), function: 'A fatty insulating layer around the axon that speeds up the nerve impulse and protects the fibre.'),
    DiagramPart(name: 'Axon Terminals', label: 'Axon Terminals', color: Color(0xFFAB47BC), function: 'Branched endings that release chemical messengers across a synapse to the next neuron or an effector.'),
  ];

  static const _reflexArcParts = [
    DiagramPart(name: 'Receptor', label: 'Receptor', color: Color(0xFFE53935), function: 'Detects the stimulus (e.g. heat from a flame) in the skin and generates a nerve impulse.'),
    DiagramPart(name: 'Sensory Neuron', label: 'Sensory Neuron', color: Color(0xFF43A047), function: 'Carries the impulse from the receptor inward to the spinal cord (the afferent pathway).'),
    DiagramPart(name: 'Spinal Cord', label: 'Spinal Cord', color: Color(0xFF5C6BC0), function: 'Processes the signal instantly at a relay/interneuron, without waiting for the brain — this is what makes a reflex so fast.'),
    DiagramPart(name: 'Motor Neuron', label: 'Motor Neuron', color: Color(0xFFEF6C00), function: 'Carries the response signal outward from the spinal cord to the effector (the efferent pathway).'),
    DiagramPart(name: 'Effector', label: 'Effector', color: Color(0xFFAB47BC), function: 'The muscle that contracts in response to the signal, pulling the hand away from danger.'),
  ];

  static const _brainParts = [
    DiagramPart(name: 'Cerebrum', label: 'Cerebrum', color: Color(0xFF5C6BC0), function: 'The largest part of the forebrain; controls thinking, memory, reasoning, and voluntary actions.'),
    DiagramPart(name: 'Cerebellum', label: 'Cerebellum', color: Color(0xFF43A047), function: 'Located at the back of the brain; controls balance, posture, and coordination of voluntary movements.'),
    DiagramPart(name: 'Medulla', label: 'Medulla', color: Color(0xFFEF6C00), function: 'Part of the hindbrain connecting to the spinal cord; controls involuntary actions like breathing, heartbeat, and blood pressure.'),
  ];

  List<DiagramPart> get _parts => switch (_view) {
        _View.neuron => _neuronParts,
        _View.reflexArc => _reflexArcParts,
        _View.brain => _brainParts,
      };

  static const _viewMeta = {
    _View.neuron: ('Neuron', Icons.hub, Colors.indigo),
    _View.reflexArc: ('Reflex Arc', Icons.flash_on, Colors.deepPurple),
    _View.brain: ('Human Brain', Icons.psychology, Colors.teal),
  };

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Control and Coordination',
      icon: Icons.psychology_alt,
      accent: Colors.deepPurple.shade400,
      description: 'Tap a labeled part to learn its role. Switch diagrams below.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _View.values.map((v) {
              final isSelected = v == _view;
              final m = _viewMeta[v]!;
              return ChoiceChip(
                avatar: Icon(m.$2, size: 16, color: isSelected ? Colors.white : m.$3),
                label: Text(m.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: m.$3,
                backgroundColor: m.$3.withValues(alpha: 0.12),
                onSelected: (_) => setState(() {
                  _view = v;
                  _selected = null;
                }),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          ResponsiveDiagram(
            aspectRatio: _view == _View.neuron ? 1.7 : 1.05,
            maxWidth: _view == _View.neuron ? 560 : 440,
            backgroundGradient: [Colors.deepPurple.shade50, Colors.indigo.shade50],
            painter: _ControlPainter(view: _view, selectedName: _selected?.name),
            parts: _parts,
            hitRects: (size) => _hitRectsFor(_view, size),
            onSelect: (p) => setState(() => _selected = p),
          ),
          const SizedBox(height: 14),
          DiagramPartPicker(parts: _parts, selected: _selected, onSelect: (p) => setState(() => _selected = p)),
        ],
      ),
    );
  }
}

Map<String, Rect> _hitRectsFor(_View view, Size size) {
  final w = size.width, h = size.height;
  Rect f(double l, double t, double r, double b) => Rect.fromLTRB(l * w, t * h, r * w, b * h);

  switch (view) {
    case _View.neuron:
      return {
        'Dendrites': f(0.0, 0.05, 0.22, 0.65),
        'Cell Body': f(0.20, 0.25, 0.40, 0.62),
        'Axon': f(0.40, 0.40, 0.80, 0.55),
        'Myelin Sheath': f(0.42, 0.30, 0.78, 0.42),
        'Axon Terminals': f(0.80, 0.20, 1.0, 0.70),
      };
    case _View.reflexArc:
      return {
        'Receptor': f(0.02, 0.62, 0.24, 0.86),
        'Sensory Neuron': f(0.10, 0.30, 0.42, 0.64),
        'Spinal Cord': f(0.34, 0.06, 0.66, 0.34),
        'Motor Neuron': f(0.58, 0.30, 0.90, 0.64),
        'Effector': f(0.76, 0.62, 0.98, 0.86),
      };
    case _View.brain:
      return {
        'Cerebrum': f(0.08, 0.08, 0.72, 0.48),
        'Cerebellum': f(0.55, 0.42, 0.85, 0.72),
        'Medulla': f(0.62, 0.68, 0.80, 0.92),
      };
  }
}

class _ControlPainter extends CustomPainter {
  final _View view;
  final String? selectedName;

  _ControlPainter({required this.view, required this.selectedName});

  bool _sel(String name) => name == selectedName;

  @override
  void paint(Canvas canvas, Size size) {
    switch (view) {
      case _View.neuron:
        _paintNeuron(canvas, size);
        break;
      case _View.reflexArc:
        _paintReflexArc(canvas, size);
        break;
      case _View.brain:
        _paintBrain(canvas, size);
        break;
    }
  }

  void _blob(Canvas canvas, Path path, Color color, String name, {double strokeWidth = 1.4}) {
    final emphasize = _sel(name);
    if (emphasize) drawGlow(canvas, path.getBounds().center, path.getBounds().longestSide * 0.55, color);
    canvas.drawPath(path, Paint()..color = color.withValues(alpha: 0.82));
    canvas.drawPath(path, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? strokeWidth + 1.2 : strokeWidth
      ..color = emphasize ? Colors.black87 : color);
  }

  void _line(Canvas canvas, Path path, Color color, String name, double width) {
    final emphasize = _sel(name);
    if (emphasize) {
      final metric = path.computeMetrics().first;
      drawGlow(canvas, metric.getTangentForOffset(metric.length / 2)!.position, width * 1.8, color);
    }
    canvas.drawPath(path, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = width
      ..strokeCap = StrokeCap.round
      ..color = color.withValues(alpha: emphasize ? 1.0 : 0.85));
  }

  void _label(Canvas canvas, Offset pos, String text, Color color) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.w700, color: Colors.black87, height: 1.1)),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 74);
    final bg = Rect.fromLTWH(pos.dx - tp.width / 2 - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.82));
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(4)), Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 0.8
      ..color = color.withValues(alpha: 0.6));
    tp.paint(canvas, Offset(pos.dx - tp.width / 2, pos.dy));
  }

  // ---------------- Neuron ----------------
  void _paintNeuron(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final midY = h * 0.47;

    // Dendrites: branching lines converging on the cell body.
    final dendriteEnds = [Offset(w * 0.02, h * 0.1), Offset(w * 0.0, h * 0.3), Offset(w * 0.02, h * 0.55), Offset(w * 0.08, h * 0.65)];
    final dendritePath = Path();
    for (final end in dendriteEnds) {
      dendritePath.moveTo(w * 0.24, midY - h * 0.05);
      dendritePath.quadraticBezierTo(w * 0.14, end.dy, end.dx, end.dy);
    }
    _line(canvas, dendritePath, const Color(0xFF43A047), 'Dendrites', 2.2);

    // Axon (behind myelin), from cell body to terminals.
    final axon = Path()
      ..moveTo(w * 0.36, midY)
      ..lineTo(w * 0.82, midY);
    _line(canvas, axon, const Color(0xFFEF6C00), 'Axon', 4);

    // Myelin sheath segments (sausage links) along the axon.
    final emphMyelin = _sel('Myelin Sheath');
    if (emphMyelin) drawGlow(canvas, Offset(w * 0.6, midY), w * 0.22, const Color(0xFFFFCA28));
    for (int i = 0; i < 5; i++) {
      final cx = w * (0.42 + i * 0.08);
      final rect = Rect.fromCenter(center: Offset(cx, midY), width: w * 0.065, height: h * 0.13);
      final rrect = RRect.fromRectAndRadius(rect, Radius.circular(rect.height / 2));
      canvas.drawRRect(rrect, Paint()..color = const Color(0xFFFFCA28).withValues(alpha: 0.85));
      canvas.drawRRect(rrect, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphMyelin ? 2.2 : 1.2
        ..color = emphMyelin ? Colors.black87 : const Color(0xFFFFB300));
    }

    // Axon terminals branching at the end.
    final termEnds = [Offset(w * 0.96, h * 0.25), Offset(w * 0.98, h * 0.42), Offset(w * 0.98, h * 0.55), Offset(w * 0.96, h * 0.7)];
    final termPath = Path();
    for (final end in termEnds) {
      termPath.moveTo(w * 0.82, midY);
      termPath.quadraticBezierTo(w * 0.90, end.dy, end.dx, end.dy);
    }
    _line(canvas, termPath, const Color(0xFFAB47BC), 'Axon Terminals', 2.2);
    final emphTerm = _sel('Axon Terminals');
    for (final end in termEnds) {
      canvas.drawCircle(end, emphTerm ? 5 : 3.5, Paint()..color = const Color(0xFFAB47BC));
    }

    // Cell body (soma) with nucleus, drawn last so it sits on top of dendrite/axon roots.
    final soma = Path()..addOval(Rect.fromCenter(center: Offset(w * 0.30, midY), width: w * 0.20, height: h * 0.42));
    _blob(canvas, soma, const Color(0xFF5C6BC0), 'Cell Body', strokeWidth: 1.6);
    canvas.drawCircle(Offset(w * 0.30, midY), h * 0.06, Paint()..color = const Color(0xFF303F9F).withValues(alpha: 0.9));

    _label(canvas, Offset(w * 0.05, h * 0.02), 'Dendrites', const Color(0xFF43A047));
    _label(canvas, Offset(w * 0.30, h * 0.92), 'Cell Body', const Color(0xFF5C6BC0));
    _label(canvas, Offset(w * 0.60, h * 0.16), 'Myelin Sheath', const Color(0xFFFFB300));
    _label(canvas, Offset(w * 0.60, h * 0.92), 'Axon', const Color(0xFFEF6C00));
    _label(canvas, Offset(w * 0.93, h * 0.08), 'Axon Terminals', const Color(0xFFAB47BC));
  }

  // ---------------- Reflex Arc ----------------
  void _paintReflexArc(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Sensory neuron (receptor -> spinal cord).
    final sensory = Path()
      ..moveTo(w * 0.16, h * 0.62)
      ..quadraticBezierTo(w * 0.20, h * 0.30, w * 0.40, h * 0.20);
    _line(canvas, sensory, const Color(0xFF43A047), 'Sensory Neuron', 3.5);
    _arrow(canvas, sensory, const Color(0xFF43A047));

    // Motor neuron (spinal cord -> effector).
    final motor = Path()
      ..moveTo(w * 0.60, h * 0.20)
      ..quadraticBezierTo(w * 0.80, h * 0.30, w * 0.84, h * 0.62);
    _line(canvas, motor, const Color(0xFFEF6C00), 'Motor Neuron', 3.5);
    _arrow(canvas, motor, const Color(0xFFEF6C00));

    // Spinal cord cross-section (grey matter butterfly inside white matter oval).
    final cordRect = Rect.fromCenter(center: Offset(w * 0.5, h * 0.16), width: w * 0.34, height: h * 0.26);
    final emphCord = _sel('Spinal Cord');
    if (emphCord) drawGlow(canvas, cordRect.center, cordRect.longestSide * 0.6, const Color(0xFF5C6BC0));
    canvas.drawOval(cordRect, Paint()..color = const Color(0xFFE8EAF6));
    canvas.drawOval(cordRect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphCord ? 2.6 : 1.5
      ..color = emphCord ? Colors.black87 : const Color(0xFF5C6BC0));
    final grey = Path()
      ..moveTo(cordRect.center.dx - cordRect.width * 0.18, cordRect.top + cordRect.height * 0.2)
      ..quadraticBezierTo(cordRect.center.dx, cordRect.center.dy, cordRect.center.dx - cordRect.width * 0.18, cordRect.bottom - cordRect.height * 0.2)
      ..moveTo(cordRect.center.dx + cordRect.width * 0.18, cordRect.top + cordRect.height * 0.2)
      ..quadraticBezierTo(cordRect.center.dx, cordRect.center.dy, cordRect.center.dx + cordRect.width * 0.18, cordRect.bottom - cordRect.height * 0.2);
    canvas.drawPath(grey, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round
      ..color = const Color(0xFF5C6BC0).withValues(alpha: 0.7));

    // Receptor (finger near a flame).
    final emphReceptor = _sel('Receptor');
    if (emphReceptor) drawGlow(canvas, Offset(w * 0.12, h * 0.72), w * 0.16, const Color(0xFFE53935));
    final finger = Path()
      ..moveTo(w * 0.06, h * 0.86)
      ..quadraticBezierTo(w * 0.04, h * 0.66, w * 0.14, h * 0.62)
      ..quadraticBezierTo(w * 0.22, h * 0.66, w * 0.20, h * 0.80)
      ..lineTo(w * 0.06, h * 0.86)
      ..close();
    canvas.drawPath(finger, Paint()..color = const Color(0xFFFFCCBC));
    canvas.drawPath(finger, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphReceptor ? 2.4 : 1.4
      ..color = emphReceptor ? Colors.black87 : const Color(0xFFE53935));
    // Flame.
    final flame = Path()
      ..moveTo(w * 0.24, h * 0.86)
      ..quadraticBezierTo(w * 0.19, h * 0.76, w * 0.24, h * 0.68)
      ..quadraticBezierTo(w * 0.30, h * 0.76, w * 0.24, h * 0.86)
      ..close();
    canvas.drawPath(flame, Paint()..color = const Color(0xFFFFA726));

    // Effector (a small arm/hand pulling away).
    final emphEffector = _sel('Effector');
    if (emphEffector) drawGlow(canvas, Offset(w * 0.88, h * 0.72), w * 0.16, const Color(0xFFAB47BC));
    final hand = Path()
      ..moveTo(w * 0.94, h * 0.86)
      ..quadraticBezierTo(w * 0.98, h * 0.66, w * 0.86, h * 0.62)
      ..quadraticBezierTo(w * 0.78, h * 0.66, w * 0.80, h * 0.80)
      ..lineTo(w * 0.94, h * 0.86)
      ..close();
    canvas.drawPath(hand, Paint()..color = const Color(0xFFE1BEE7));
    canvas.drawPath(hand, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphEffector ? 2.4 : 1.4
      ..color = emphEffector ? Colors.black87 : const Color(0xFFAB47BC));

    _label(canvas, Offset(w * 0.13, h * 0.93), 'Receptor', const Color(0xFFE53935));
    _label(canvas, Offset(w * 0.22, h * 0.42), 'Sensory\nNeuron', const Color(0xFF43A047));
    _label(canvas, Offset(w * 0.5, h * 0.02), 'Spinal Cord', const Color(0xFF5C6BC0));
    _label(canvas, Offset(w * 0.78, h * 0.42), 'Motor\nNeuron', const Color(0xFFEF6C00));
    _label(canvas, Offset(w * 0.87, h * 0.93), 'Effector', const Color(0xFFAB47BC));
  }

  void _arrow(Canvas canvas, Path path, Color color) {
    final metric = path.computeMetrics().first;
    final tangent = metric.getTangentForOffset(metric.length * 0.55)!;
    final dir = tangent.vector;
    final normal = Offset(-dir.dy, dir.dx);
    final tip = tangent.position;
    final p1 = tip - dir * 6 + normal * 4;
    final p2 = tip - dir * 6 - normal * 4;
    canvas.drawPath(Path()..moveTo(tip.dx, tip.dy)..lineTo(p1.dx, p1.dy)..moveTo(tip.dx, tip.dy)..lineTo(p2.dx, p2.dy), Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.5
      ..strokeCap = StrokeCap.round
      ..color = color);
  }

  // ---------------- Brain ----------------
  void _paintBrain(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Head/brain silhouette outline for context (unlabelled, subtle).
    final skull = Path()
      ..moveTo(w * 0.05, h * 0.55)
      ..cubicTo(w * 0.02, h * 0.25, w * 0.25, h * 0.05, w * 0.55, h * 0.06)
      ..cubicTo(w * 0.80, h * 0.07, w * 0.92, h * 0.30, w * 0.88, h * 0.55)
      ..cubicTo(w * 0.90, h * 0.65, w * 0.85, h * 0.72, w * 0.78, h * 0.70)
      ..cubicTo(w * 0.74, h * 0.85, w * 0.55, h * 0.94, w * 0.40, h * 0.90)
      ..cubicTo(w * 0.20, h * 0.86, w * 0.06, h * 0.72, w * 0.05, h * 0.55)
      ..close();
    canvas.drawPath(skull, Paint()..color = const Color(0xFFF3E5F5));
    canvas.drawPath(skull, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5
      ..color = const Color(0xFF9575CD).withValues(alpha: 0.5));

    // Cerebrum: large folded region filling most of the upper/front skull.
    final cerebrum = Path()
      ..moveTo(w * 0.08, h * 0.50)
      ..cubicTo(w * 0.05, h * 0.24, w * 0.26, h * 0.08, w * 0.52, h * 0.09)
      ..cubicTo(w * 0.72, h * 0.10, w * 0.82, h * 0.26, w * 0.78, h * 0.42)
      ..cubicTo(w * 0.70, h * 0.36, w * 0.55, h * 0.40, w * 0.50, h * 0.48)
      ..cubicTo(w * 0.40, h * 0.38, w * 0.24, h * 0.40, w * 0.16, h * 0.52)
      ..close();
    _blob(canvas, cerebrum, const Color(0xFF5C6BC0), 'Cerebrum', strokeWidth: 1.6);
    // Fold hints.
    final foldPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.2
      ..color = Colors.white.withValues(alpha: 0.6);
    for (final dx in [0.22, 0.38, 0.52, 0.66]) {
      canvas.drawLine(Offset(w * dx, h * 0.14), Offset(w * (dx + 0.02), h * 0.30), foldPaint);
    }

    // Cerebellum: smaller rounded, textured region at the back-bottom.
    final cerebellum = Path()..addOval(Rect.fromCenter(center: Offset(w * 0.68, h * 0.58), width: w * 0.26, height: h * 0.28));
    _blob(canvas, cerebellum, const Color(0xFF43A047), 'Cerebellum', strokeWidth: 1.6);
    final texturePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1
      ..color = Colors.white.withValues(alpha: 0.6);
    for (int i = -2; i <= 2; i++) {
      canvas.drawLine(Offset(w * (0.60 + i * 0.03), h * 0.48), Offset(w * (0.60 + i * 0.03), h * 0.68), texturePaint);
    }

    // Medulla: short tube connecting cerebellum/cerebrum base to the spinal cord.
    final medulla = Path()
      ..moveTo(w * 0.62, h * 0.72)
      ..quadraticBezierTo(w * 0.66, h * 0.80, w * 0.68, h * 0.90);
    _line(canvas, medulla, const Color(0xFFEF6C00), 'Medulla', w * 0.045);

    _label(canvas, Offset(w * 0.30, h * 0.02), 'Cerebrum', const Color(0xFF5C6BC0));
    _label(canvas, Offset(w * 0.68, h * 0.90), 'Cerebellum', const Color(0xFF43A047));
    _label(canvas, Offset(w * 0.85, h * 0.92), 'Medulla', const Color(0xFFEF6C00));
  }

  @override
  bool shouldRepaint(covariant _ControlPainter oldDelegate) =>
      oldDelegate.view != view || oldDelegate.selectedName != selectedName;
}
