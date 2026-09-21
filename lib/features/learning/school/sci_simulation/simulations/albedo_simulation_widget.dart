import 'package:flutter/material.dart';
import 'common/sim_frame.dart';

class _Surface {
  final String name;
  final double albedo; // fraction reflected, 0..1
  final Color color;
  const _Surface(this.name, this.albedo, this.color);
}

const _surfaces = [
  _Surface('Fresh Snow', 0.85, Color(0xFFEAF3FB)),
  _Surface('Ice', 0.6, Color(0xFFBFE0F5)),
  _Surface('Crushed Rock', 0.28, Color(0xFFB9AFA3)),
  _Surface('Light Coloured Soil', 0.4, Color(0xFFD8C79E)),
  _Surface('Black Soil', 0.1, Color(0xFF4A3B2E)),
  _Surface('Ocean Water', 0.08, Color(0xFF2B5C7A)),
  _Surface('Forest Canopy', 0.15, Color(0xFF2F5F3A)),
];

/// Illustrates albedo: pick a surface and watch how much of the incoming
/// sunlight is reflected vs absorbed, matching Table 13.1 in the chapter
/// (fraction of solar radiation reflected by different materials).
class AlbedoSimulationWidget extends StatefulWidget {
  const AlbedoSimulationWidget({super.key});

  @override
  State<AlbedoSimulationWidget> createState() => _AlbedoSimulationWidgetState();
}

class _AlbedoSimulationWidgetState extends State<AlbedoSimulationWidget> with SingleTickerProviderStateMixin {
  _Surface _surface = _surfaces[0];
  late final AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 2200))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final reflectedPct = (_surface.albedo * 100).round();
    final absorbedPct = 100 - reflectedPct;

    return SimFrame(
      title: 'Albedo & Uneven Heating',
      icon: Icons.wb_sunny,
      accent: const Color(0xFF3F6A9C),
      description: 'Pick a surface to see how much sunlight it reflects (albedo) vs absorbs.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _surfaces.map((s) {
              final isSelected = _surface.name == s.name;
              return ChoiceChip(
                label: Text(s.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: const Color(0xFF3F6A9C),
                backgroundColor: const Color(0xFF3F6A9C).withValues(alpha: 0.15),
                onSelected: (_) => setState(() => _surface = s),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: const Color(0xFFEAF2FA), borderRadius: BorderRadius.circular(12), border: Border.all(color: Colors.grey.shade300)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) => CustomPaint(
                size: Size.infinite,
                painter: _AlbedoPainter(surfaceColor: _surface.color, albedo: _surface.albedo, t: _controller.value),
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(
            metrics: [
              SimMetric(label: 'Reflected', value: '$reflectedPct%', color: const Color(0xFF3F6A9C)),
              SimMetric(label: 'Absorbed', value: '$absorbedPct%', color: const Color(0xFFD9622A)),
            ],
          ),
          const SizedBox(height: 10),
          Text(
            _surface.albedo >= 0.5
                ? '${_surface.name} has a HIGH albedo — it reflects most sunlight and stays relatively cool. This is why snow-covered and icy regions stay cold.'
                : '${_surface.name} has a LOW albedo — it absorbs most sunlight and warms up more. This is why dark soil and ocean water are relatively warm.',
            style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant),
          ),
        ],
      ),
    );
  }
}

class _AlbedoPainter extends CustomPainter {
  final Color surfaceColor;
  final double albedo;
  final double t;

  _AlbedoPainter({required this.surfaceColor, required this.albedo, required this.t});

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final groundY = h * 0.72;

    // Sky.
    canvas.drawRect(Rect.fromLTWH(0, 0, w, groundY), Paint()..color = const Color(0xFFCFE3F5));
    // Ground surface.
    canvas.drawRect(Rect.fromLTWH(0, groundY, w, h - groundY), Paint()..color = surfaceColor);

    // Sun.
    final sunCenter = Offset(w * 0.18, h * 0.18);
    canvas.drawCircle(sunCenter, 14, Paint()..color = const Color(0xFFF2C94C));

    final impactX = w * 0.55;
    final impact = Offset(impactX, groundY);

    // Incoming ray (always drawn).
    final rayPaint = Paint()
      ..color = const Color(0xFFF2C94C)
      ..strokeWidth = 2.4
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(sunCenter, impact, rayPaint);

    // Reflected ray: animates outward if albedo is high; length scales with albedo.
    final reflectProgress = (t) % 1.0;
    final reflectEnd = Offset(impactX + 70, groundY - 90);
    final reflectedPoint = Offset.lerp(impact, reflectEnd, reflectProgress)!;
    final reflectPaint = Paint()
      ..color = const Color(0xFF3F6A9C).withValues(alpha: (albedo * 1.6).clamp(0.15, 1.0))
      ..strokeWidth = 2.2 + albedo * 2
      ..strokeCap = StrokeCap.round;
    if (reflectProgress < 0.85) {
      canvas.drawLine(impact, reflectedPoint, reflectPaint);
    }

    // Absorbed heat glow: pulses stronger with low albedo (high absorption).
    final absorption = 1 - albedo;
    final glowRadius = 10 + absorption * 22 * (0.6 + 0.4 * (1 - (reflectProgress - 0.5).abs() * 2).clamp(0.0, 1.0));
    canvas.drawCircle(impact, glowRadius, Paint()
      ..color = const Color(0xFFD9622A).withValues(alpha: (absorption * 0.35).clamp(0.05, 0.4))
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 8));
  }

  @override
  bool shouldRepaint(covariant _AlbedoPainter oldDelegate) => true;
}
