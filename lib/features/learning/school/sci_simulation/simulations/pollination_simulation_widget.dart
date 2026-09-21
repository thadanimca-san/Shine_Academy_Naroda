import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _PollinationMode { self, cross }

class _FlowerPart {
  final String name;
  final String function;
  final Color color;
  const _FlowerPart(this.name, this.function, this.color);
}

const _flowerParts = [
  _FlowerPart('Petal', 'Brightly coloured to attract pollinators like insects and birds.', Color(0xFFE85D8A)),
  _FlowerPart('Sepal', 'Green outer covering that protects the flower while it is still a bud.', Color(0xFF6B9E5C)),
  _FlowerPart('Stamen (Anther + Filament)', 'The male part. The anther produces pollen grains, held up by the filament.', Color(0xFFD9A62E)),
  _FlowerPart('Pistil (Stigma + Style + Ovary)', 'The female part. The stigma receives pollen, the style is a tube down to the ovary, which holds the ovules.', Color(0xFF4A8B6F)),
];

/// Tap-to-explore flower diagram plus a self-pollination vs cross-pollination
/// toggle showing pollen travelling from anther to stigma, either on the
/// same flower or between two separate plants.
class PollinationSimulationWidget extends StatefulWidget {
  const PollinationSimulationWidget({super.key});

  @override
  State<PollinationSimulationWidget> createState() => _PollinationSimulationWidgetState();
}

class _PollinationSimulationWidgetState extends State<PollinationSimulationWidget> with SingleTickerProviderStateMixin {
  _PollinationMode _mode = _PollinationMode.self;
  _FlowerPart? _selectedPart;
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1800))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Pollination Explorer',
      icon: Icons.local_florist,
      accent: const Color(0xFF4A8B6F),
      description: 'Tap a flower part to learn its job, then watch pollen travel during self- vs cross-pollination.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _flowerParts.map((p) {
              final isSelected = _selectedPart?.name == p.name;
              return ActionChip(
                label: Text(p.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? p.color : p.color.withValues(alpha: 0.22),
                onPressed: () => setState(() => _selectedPart = p),
              );
            }).toList(),
          ),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selectedPart == null
                ? Text(TrilingualService.instance.getUIText('Tap a flower part above to learn what it does.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(_selectedPart!.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selectedPart!.color, fontSize: 14)),
                      const SizedBox(height: 4),
                      Text(_selectedPart!.function, style: TextStyle(fontSize: 13)),
                    ],
                  ),
          ),
          const SizedBox(height: 18),
          const Divider(),
          const SizedBox(height: 6),
          Row(
            children: [
              Expanded(
                child: ToggleButtons(
                  isSelected: [_mode == _PollinationMode.self, _mode == _PollinationMode.cross],
                  onPressed: (i) => setState(() => _mode = i == 0 ? _PollinationMode.self : _PollinationMode.cross),
                  borderRadius: BorderRadius.circular(8),
                  selectedColor: Colors.white,
                  fillColor: const Color(0xFF4A8B6F),
                  constraints: const BoxConstraints(minHeight: 34, minWidth: 110),
                  children: [Text(TrilingualService.instance.getUIText('Self-pollination')), Text(TrilingualService.instance.getUIText('Cross-pollination'))],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: const Color(0xFFEFF6F1), borderRadius: BorderRadius.circular(12), border: Border.all(color: Colors.grey.shade300)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) => CustomPaint(
                size: Size.infinite,
                painter: _PollinationPainter(mode: _mode, t: _controller.value),
              ),
            ),
          ),
          const SizedBox(height: 10),
          Text(
            _mode == _PollinationMode.self
                ? 'Pollen moves from the anther to the stigma of the SAME flower.'
                : 'Pollen moves from the anther of one flower to the stigma of a flower on a DIFFERENT plant of the same species — often carried by wind, insects, or birds.',
            style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant),
          ),
        ],
      ),
    );
  }
}

class _PollinationPainter extends CustomPainter {
  final _PollinationMode mode;
  final double t;

  _PollinationPainter({required this.mode, required this.t});

  void _drawFlower(Canvas canvas, Offset center, double scale) {
    final petalPaint = Paint()..color = const Color(0xFFE85D8A).withValues(alpha: 0.85);
    for (int i = 0; i < 5; i++) {
      final angle = i * (2 * 3.14159 / 5);
      canvas.save();
      canvas.translate(center.dx, center.dy);
      canvas.rotate(angle);
      canvas.drawOval(Rect.fromCenter(center: Offset(0, -18 * scale), width: 16 * scale, height: 24 * scale), petalPaint);
      canvas.restore();
    }
    canvas.drawCircle(center, 9 * scale, Paint()..color = const Color(0xFFD9A62E));
  }

  @override
  void paint(Canvas canvas, Size size) {
    final leftCenter = Offset(size.width * 0.28, size.height * 0.55);
    final rightCenter = mode == _PollinationMode.self ? leftCenter : Offset(size.width * 0.75, size.height * 0.55);

    _drawFlower(canvas, leftCenter, 1.0);
    if (mode == _PollinationMode.cross) {
      _drawFlower(canvas, rightCenter, 0.85);
    }

    final start = leftCenter + const Offset(6, -4);
    final end = mode == _PollinationMode.self ? leftCenter + const Offset(-8, -10) : rightCenter + const Offset(-6, -8);

    final pollenPos = Offset.lerp(start, end, t)!;
    final arcLift = -20 * (1 - (2 * t - 1) * (2 * t - 1));
    final drawPos = Offset(pollenPos.dx, pollenPos.dy + arcLift);

    final trailPaint = Paint()
      ..color = const Color(0xFFD9A62E).withValues(alpha: 0.4)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4;
    final path = Path()..moveTo(start.dx, start.dy);
    for (double s = 0; s <= t; s += 0.05) {
      final p = Offset.lerp(start, end, s)!;
      final lift = -20 * (1 - (2 * s - 1) * (2 * s - 1));
      path.lineTo(p.dx, p.dy + lift);
    }
    canvas.drawPath(path, trailPaint);

    canvas.drawCircle(drawPos, 4, Paint()..color = const Color(0xFFD9A62E));
    canvas.drawCircle(drawPos, 6, Paint()
      ..color = const Color(0xFFD9A62E).withValues(alpha: 0.3));
  }

  @override
  bool shouldRepaint(covariant _PollinationPainter oldDelegate) => oldDelegate.t != t || oldDelegate.mode != mode;
}
