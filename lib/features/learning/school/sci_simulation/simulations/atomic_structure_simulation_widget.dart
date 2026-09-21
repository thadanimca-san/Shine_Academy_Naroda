import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';

/// A Bohr-model atom builder: pick an atomic number and watch electrons
/// fill the K, L, M, N shells (2, 8, 8, 18) while orbiting an animated
/// nucleus, making the 2-8-8 filling rule visible instead of memorised.
class AtomicStructureSimulationWidget extends StatefulWidget {
  const AtomicStructureSimulationWidget({super.key});

  @override
  State<AtomicStructureSimulationWidget> createState() => _AtomicStructureSimulationWidgetState();
}

class _AtomicStructureSimulationWidgetState extends State<AtomicStructureSimulationWidget> with SingleTickerProviderStateMixin {
  int _atomicNumber = 11; // Sodium by default - nicely shows 2,8,1
  late AnimationController _controller;

  static const Map<int, String> _symbols = {
    1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
    11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca',
  };

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 6))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  List<int> get _shellFilling {
    final capacities = [2, 8, 8, 18];
    int remaining = _atomicNumber;
    final shells = <int>[];
    for (final cap in capacities) {
      if (remaining <= 0) break;
      final fill = math.min(cap, remaining);
      shells.add(fill);
      remaining -= fill;
    }
    return shells;
  }

  @override
  Widget build(BuildContext context) {
    final shells = _shellFilling;
    final symbol = _symbols[_atomicNumber] ?? 'X';
    final valence = shells.isNotEmpty ? shells.last : 0;

    return SimFrame(
      title: 'Structure of the Atom: Bohr Model',
      icon: Icons.blur_circular,
      accent: Colors.indigo,
      description: 'Electrons fill shells K, L, M, N in order, holding at most 2, 8, 8, 18 electrons respectively.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              LayoutBuilder(builder: (context, constraints) {
                final size = Size(constraints.maxWidth, 220);
                return Container(
                  height: 220,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(colors: [Colors.indigo.shade900, Colors.indigo.shade700], begin: Alignment.topLeft, end: Alignment.bottomRight),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: CustomPaint(
                    size: size,
                    painter: _AtomPainter(shells: shells, symbol: symbol, phase: _controller.value * 2 * math.pi),
                  ),
                );
              }),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Element', value: symbol, color: Colors.indigo),
                SimMetric(label: 'Atomic Number (Z)', value: '$_atomicNumber'),
                SimMetric(label: 'Valence Electrons', value: '$valence', color: Colors.teal),
              ]),
              const SizedBox(height: 8),
              Text(
                'Electron configuration: ${shells.join(' , ')}',
                style: TextStyle(fontWeight: FontWeight.w600),
              ),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Atomic Number (Z): $_atomicNumber',
                value: _atomicNumber.toDouble(),
                min: 1,
                max: 20,
                divisions: 19,
                activeColor: Colors.indigo,
                onChanged: (val) => setState(() => _atomicNumber = val.round()),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _AtomPainter extends CustomPainter {
  final List<int> shells;
  final String symbol;
  final double phase;

  _AtomPainter({required this.shells, required this.symbol, required this.phase});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxRadius = math.min(size.width, size.height) / 2 - 10;
    final orbitColors = [Colors.cyanAccent, Colors.amberAccent, Colors.pinkAccent, Colors.greenAccent];

    for (int s = 0; s < shells.length; s++) {
      final radius = maxRadius * (s + 1) / shells.length;
      canvas.drawCircle(center, radius, Paint()
        ..color = Colors.white.withValues(alpha: 0.3)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.2);

      final count = shells[s];
      for (int e = 0; e < count; e++) {
        final angle = phase * (1 + s * 0.3) + (2 * math.pi * e / count);
        final pos = center + Offset(math.cos(angle) * radius, math.sin(angle) * radius);
        canvas.drawCircle(pos, 5, Paint()..color = orbitColors[s % orbitColors.length]);
      }
    }

    // nucleus
    canvas.drawCircle(center, 16, Paint()..shader = RadialGradient(colors: [Colors.orange.shade200, Colors.red.shade700]).createShader(Rect.fromCircle(center: center, radius: 16)));
    final textPainter = TextPainter(
      text: TextSpan(text: symbol, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 13)),
      textDirection: TextDirection.ltr,
    )..layout();
    textPainter.paint(canvas, center - Offset(textPainter.width / 2, textPainter.height / 2));
  }

  @override
  bool shouldRepaint(covariant _AtomPainter oldDelegate) => true;
}
