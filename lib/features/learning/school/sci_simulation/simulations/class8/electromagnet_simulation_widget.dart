import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Build a virtual electromagnet: toggle the current on/off, adjust the
/// number of coil turns and cells, and watch the magnetic field strength
/// (and how many paper clips it can lift) respond — mirrors Activities
/// 4.3-4.4 in the chapter.
class ElectromagnetSimulationWidget extends StatefulWidget {
  const ElectromagnetSimulationWidget({super.key});

  @override
  State<ElectromagnetSimulationWidget> createState() => _ElectromagnetSimulationWidgetState();
}

class _ElectromagnetSimulationWidgetState extends State<ElectromagnetSimulationWidget> {
  bool _on = false;
  int _turns = 25;
  int _cells = 1;

  int get _clipsAttracted => _on ? ((_turns / 25) * _cells).round().clamp(1, 8) : 0;
  double get _fieldStrength => _on ? (_turns / 100.0) * _cells : 0.0;

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Electromagnet Builder',
      icon: Icons.electric_bolt,
      accent: const Color(0xFFC2455B),
      description: 'Turn the current on, then adjust coil turns and cells to see how the magnet\'s strength changes.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: const Color(0xFFF7E5E8), borderRadius: BorderRadius.circular(14), border: Border.all(color: Colors.grey.shade300)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _ElectromagnetPainter(on: _on, strength: _fieldStrength, clips: _clipsAttracted),
            ),
          ),
          const SizedBox(height: 14),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () => setState(() => _on = !_on),
              icon: Icon(_on ? Icons.power_off : Icons.power),
              label: Text(_on ? 'Switch OFF' : 'Switch ON'),
              style: ElevatedButton.styleFrom(backgroundColor: _on ? Colors.grey.shade700 : const Color(0xFFC2455B), foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Coil turns: $_turns',
            value: _turns.toDouble(),
            min: 25,
            max: 100,
            divisions: 3,
            activeColor: const Color(0xFFC2455B),
            onChanged: (v) => setState(() => _turns = v.round()),
          ),
          const SizedBox(height: 6),
          SimSlider(
            label: 'Number of cells: $_cells',
            value: _cells.toDouble(),
            min: 1,
            max: 4,
            divisions: 3,
            activeColor: const Color(0xFFC2455B),
            onChanged: (v) => setState(() => _cells = v.round()),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(
            metrics: [
              SimMetric(label: 'Field strength', value: _on ? '${(_fieldStrength * 25).round()}%' : 'Off', color: const Color(0xFFC2455B)),
              SimMetric(label: 'Paper clips lifted', value: '$_clipsAttracted', color: const Color(0xFF9C3448)),
            ],
          ),
          const SizedBox(height: 10),
          Text(
            _on
                ? 'More turns and more cells both increase the magnetic field strength — that\'s why the electromagnet can lift more paper clips.'
                : 'Switch the current ON to magnetise the coil. Without current, there is no magnetic field at all.',
            style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant),
          ),
        ],
      ),
    );
  }
}

class _ElectromagnetPainter extends CustomPainter {
  final bool on;
  final double strength;
  final int clips;

  _ElectromagnetPainter({required this.on, required this.strength, required this.clips});

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2;
    final cy = size.height / 2 - 10;
    final coilColor = on ? const Color(0xFFC2455B) : Colors.grey.shade400;
    final nailPaint = Paint()..color = Colors.blueGrey.shade400;

    // Iron nail core.
    canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(cx - 55, cy - 8, 110, 16), const Radius.circular(4)), nailPaint);
    canvas.drawCircle(Offset(cx + 55, cy), 4, nailPaint);

    // Coil loops.
    final coilPaint = Paint()
      ..color = coilColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3;
    for (int i = 0; i < 7; i++) {
      final x = cx - 45 + i * 15.0;
      canvas.drawOval(Rect.fromCenter(center: Offset(x, cy), width: 16, height: 34), coilPaint);
    }

    // Magnetic field glow if on.
    if (on) {
      final glow = Paint()
        ..color = const Color(0xFFC2455B).withValues(alpha: (0.08 + strength * 0.12).clamp(0.08, 0.35))
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 18);
      canvas.drawCircle(Offset(cx, cy), 60 + strength * 20, glow);
    }

    // Paper clips attracted to the right end.
    final clipPaint = Paint()
      ..color = Colors.grey.shade700
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.4;
    for (int i = 0; i < clips; i++) {
      final offset = Offset(cx + 62 + (i % 4) * 10.0, cy + 14 + (i ~/ 4) * 16.0);
      final path = Path()
        ..moveTo(offset.dx - 4, offset.dy - 8)
        ..lineTo(offset.dx - 4, offset.dy + 4)
        ..quadraticBezierTo(offset.dx - 4, offset.dy + 8, offset.dx, offset.dy + 8)
        ..quadraticBezierTo(offset.dx + 4, offset.dy + 8, offset.dx + 4, offset.dy + 4)
        ..lineTo(offset.dx + 4, offset.dy - 4);
      canvas.drawPath(path, clipPaint);
    }

    // Cell/battery symbol.
    final cellPaint = Paint()..color = Colors.black87;
    canvas.drawRect(Rect.fromCenter(center: Offset(cx, cy + 60), width: 30, height: 14), cellPaint..style = PaintingStyle.stroke..strokeWidth = 2);
    canvas.drawLine(Offset(cx - 60, cy), Offset(cx - 60, cy + 60), coilPaint);
    canvas.drawLine(Offset(cx - 60, cy + 60), Offset(cx - 15, cy + 60), coilPaint);
    canvas.drawLine(Offset(cx + 15, cy + 60), Offset(cx + 60, cy + 60), coilPaint);
    canvas.drawLine(Offset(cx + 60, cy + 60), Offset(cx + 60, cy), coilPaint);
  }

  @override
  bool shouldRepaint(covariant _ElectromagnetPainter oldDelegate) => oldDelegate.on != on || oldDelegate.strength != strength || oldDelegate.clips != clips;
}
