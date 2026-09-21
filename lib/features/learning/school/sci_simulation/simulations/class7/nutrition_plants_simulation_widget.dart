import 'package:flutter/material.dart';
import '../common/diagram_helpers.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A real leaf cross-section diagram — upper epidermis, palisade and
/// spongy mesophyll (with chloroplasts), a vein, and stomata exchanging
/// gases — replacing what used to be a single leaf icon with drifting
/// bubbles. A light-intensity slider still controls how fast photosynthesis
/// (and gas exchange through the stomata) runs, and the other modes of
/// plant nutrition remain explorable below.
class NutritionPlantsSimulationWidget extends StatefulWidget {
  const NutritionPlantsSimulationWidget({super.key});

  @override
  State<NutritionPlantsSimulationWidget> createState() => _NutritionPlantsSimulationWidgetState();
}

class _NutritionPlantsSimulationWidgetState extends State<NutritionPlantsSimulationWidget> with SingleTickerProviderStateMixin {
  double _lightIntensity = 0.6;
  late AnimationController _controller;
  int _selectedMode = 0;
  DiagramPart? _selected;

  static const _leafParts = [
    DiagramPart(name: 'Upper Epidermis', label: 'Upper Epidermis', color: Color(0xFF8D6E63), function: 'A protective, transparent outer layer that lets sunlight pass through to the cells below.'),
    DiagramPart(name: 'Palisade Mesophyll', label: 'Palisade Mesophyll', color: Color(0xFF2E7D32), function: 'Tightly packed, column-shaped cells full of chloroplasts — the main site of photosynthesis.'),
    DiagramPart(name: 'Spongy Mesophyll', label: 'Spongy Mesophyll', color: Color(0xFF81C784), function: 'Loosely packed cells with large air spaces between them, allowing gases to circulate to and from the palisade layer.'),
    DiagramPart(name: 'Vein', label: 'Vein', color: Color(0xFF5C6BC0), function: 'A vascular bundle (xylem and phloem) that brings water in and carries away the sugars made during photosynthesis.'),
    DiagramPart(name: 'Lower Epidermis', label: 'Lower Epidermis', color: Color(0xFF8D6E63), function: 'The bottom protective layer, containing most of the leaf\'s stomata.'),
    DiagramPart(name: 'Stomata', label: 'Stomata', color: Color(0xFFEF6C00), function: 'Tiny pores, each flanked by two guard cells, that open and close to let CO₂ in and O₂ (and water vapour) out.'),
  ];

  static const _modes = [
    ('Parasitic', 'Obtains nutrients from a living host plant, harming it. E.g. Cuscuta (Amarbel).', Icons.link, Colors.red),
    ('Saprotrophic', 'Obtains nutrients from dead and decaying organic matter. E.g. bread mould, mushrooms.', Icons.eco, Colors.brown),
    ('Insectivorous', 'Traps and digests insects for nutrients, often growing in nitrogen-poor soil. E.g. pitcher plant.', Icons.bug_report, Colors.deepPurple),
    ('Symbiotic', 'Two organisms live together, both benefiting. E.g. Rhizobium bacteria in root nodules.', Icons.diversity_3, Colors.teal),
  ];

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final mode = _modes[_selectedMode];

    return SimFrame(
      title: 'Photosynthesis & Modes of Nutrition',
      icon: Icons.local_florist,
      accent: Colors.green.shade700,
      description: 'Tap a labeled layer to learn its role. Brighter light speeds up gas exchange at the stomata.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              ResponsiveDiagram(
                aspectRatio: 1.7,
                maxWidth: 560,
                backgroundGradient: [
                  Color.lerp(Colors.green.shade100, Colors.yellow.shade100, _lightIntensity)!,
                  Colors.green.shade50,
                ],
                painter: _LeafPainter(selectedName: _selected?.name, t: _controller.value, speed: 0.4 + _lightIntensity * 1.6),
                parts: _leafParts,
                hitRects: (size) => _leafHitRects(size),
                onSelect: (p) => setState(() => _selected = p),
              ),
              const SizedBox(height: 12),
              DiagramPartPicker(parts: _leafParts, selected: _selected, onSelect: (p) => setState(() => _selected = p)),
              const SizedBox(height: 14),
              SimMetricPanel(metrics: [
                SimMetric(label: 'CO₂ in', value: 'absorbed', color: Colors.blueGrey),
                SimMetric(label: 'O₂ out', value: 'released', color: Colors.teal),
                SimMetric(label: 'Rate', value: _lightIntensity < 0.4 ? 'Slow' : (_lightIntensity < 0.75 ? 'Medium' : 'Fast'), color: Colors.orange),
              ]),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Sunlight intensity: ${(_lightIntensity * 100).toStringAsFixed(0)}%',
                value: _lightIntensity,
                min: 0.1,
                max: 1.0,
                divisions: 18,
                activeColor: Colors.orange,
                onChanged: (val) => setState(() => _lightIntensity = val),
              ),
              const SizedBox(height: 10),
              Text(TrilingualService.instance.getUIText('Other Modes of Nutrition'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Colors.black54)),
              const SizedBox(height: 6),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: _modes.asMap().entries.map((e) {
                  final isSelected = e.key == _selectedMode;
                  return ChoiceChip(
                    avatar: Icon(e.value.$3, size: 16, color: isSelected ? Colors.white : e.value.$4),
                    label: Text(e.value.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: e.value.$4,
                    backgroundColor: e.value.$4.withValues(alpha: 0.12),
                    onSelected: (_) => setState(() => _selectedMode = e.key),
                  );
                }).toList(),
              ),
              const SizedBox(height: 10),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: mode.$4.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(10)),
                child: Text(mode.$2, style: TextStyle(fontSize: 13)),
              ),
            ],
          );
        },
      ),
    );
  }
}

Map<String, Rect> _leafHitRects(Size size) {
  final w = size.width, h = size.height;
  Rect f(double l, double t, double r, double b) => Rect.fromLTRB(l * w, t * h, r * w, b * h);
  return {
    'Upper Epidermis': f(0.0, 0.06, 1.0, 0.16),
    'Palisade Mesophyll': f(0.0, 0.16, 1.0, 0.44),
    'Vein': f(0.42, 0.16, 0.58, 0.84),
    'Spongy Mesophyll': f(0.0, 0.44, 1.0, 0.78),
    'Lower Epidermis': f(0.0, 0.78, 1.0, 0.88),
    'Stomata': f(0.10, 0.84, 0.30, 0.96),
  };
}

class _LeafPainter extends CustomPainter {
  final String? selectedName;
  final double t;
  final double speed;

  _LeafPainter({required this.selectedName, required this.t, required this.speed});

  bool _sel(String name) => name == selectedName;

  void _label(Canvas canvas, Offset pos, String text, Color color, {TextAlign align = TextAlign.left}) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 9, fontWeight: FontWeight.w700, color: Colors.black87, height: 1.1)),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 78);
    double dx = pos.dx;
    if (align == TextAlign.center) dx -= tp.width / 2;
    if (align == TextAlign.right) dx -= tp.width;
    final bg = Rect.fromLTWH(dx - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.82));
    tp.paint(canvas, Offset(dx, pos.dy));
  }

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Upper epidermis.
    final emphUpper = _sel('Upper Epidermis');
    if (emphUpper) drawGlow(canvas, Offset(w * 0.5, h * 0.11), w * 0.5, const Color(0xFF8D6E63));
    canvas.drawRect(Rect.fromLTRB(0, h * 0.06, w, h * 0.16), Paint()..color = const Color(0xFFD7CCC8).withValues(alpha: emphUpper ? 0.95 : 0.75));
    canvas.drawRect(Rect.fromLTRB(0, h * 0.06, w, h * 0.16), Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphUpper ? 2.2 : 1
      ..color = emphUpper ? Colors.black87 : const Color(0xFF8D6E63));

    // Palisade mesophyll: tall column cells with chloroplast dots.
    final emphPalisade = _sel('Palisade Mesophyll');
    final palisadeRect = Rect.fromLTRB(0, h * 0.16, w, h * 0.44);
    if (emphPalisade) drawGlow(canvas, palisadeRect.center, w * 0.5, const Color(0xFF2E7D32));
    canvas.drawRect(palisadeRect, Paint()..color = const Color(0xFFA5D6A7).withValues(alpha: emphPalisade ? 0.9 : 0.55));
    const cols = 10;
    final cellPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphPalisade ? 1.6 : 1
      ..color = emphPalisade ? Colors.black54 : const Color(0xFF2E7D32).withValues(alpha: 0.5);
    for (int i = 1; i < cols; i++) {
      final x = w * i / cols;
      canvas.drawLine(Offset(x, palisadeRect.top), Offset(x, palisadeRect.bottom), cellPaint);
    }
    final chloroplastPaint = Paint()..color = const Color(0xFF1B5E20).withValues(alpha: emphPalisade ? 1.0 : 0.8);
    for (int i = 0; i < cols; i++) {
      final cx = w * (i + 0.5) / cols;
      canvas.drawCircle(Offset(cx, palisadeRect.top + palisadeRect.height * 0.35), 2.2, chloroplastPaint);
      canvas.drawCircle(Offset(cx, palisadeRect.top + palisadeRect.height * 0.65), 2.2, chloroplastPaint);
    }

    // Spongy mesophyll: irregular blob cells with air spaces.
    final emphSpongy = _sel('Spongy Mesophyll');
    final spongyRect = Rect.fromLTRB(0, h * 0.44, w, h * 0.78);
    if (emphSpongy) drawGlow(canvas, spongyRect.center, w * 0.5, const Color(0xFF81C784));
    canvas.drawRect(spongyRect, Paint()..color = const Color(0xFFC8E6C9).withValues(alpha: emphSpongy ? 0.9 : 0.55));
    final blobPaint = Paint()..color = const Color(0xFF81C784).withValues(alpha: emphSpongy ? 0.95 : 0.75);
    final blobStroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphSpongy ? 1.6 : 1
      ..color = emphSpongy ? Colors.black54 : const Color(0xFF558B2F);
    final rnd = [0.1, 0.35, 0.6, 0.85, 0.2, 0.5, 0.75, 0.05, 0.45, 0.9];
    for (int i = 0; i < 9; i++) {
      final cx = w * (i + 0.5) / 9;
      final cy = spongyRect.top + spongyRect.height * (0.3 + rnd[i % rnd.length] * 0.4);
      canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy), width: w * 0.085, height: h * 0.09), blobPaint);
      canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy), width: w * 0.085, height: h * 0.09), blobStroke);
    }

    // Lower epidermis.
    final emphLower = _sel('Lower Epidermis');
    final lowerRect = Rect.fromLTRB(0, h * 0.78, w, h * 0.88);
    if (emphLower) drawGlow(canvas, lowerRect.center, w * 0.5, const Color(0xFF8D6E63));
    canvas.drawRect(lowerRect, Paint()..color = const Color(0xFFD7CCC8).withValues(alpha: emphLower ? 0.95 : 0.75));
    canvas.drawRect(lowerRect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphLower ? 2.2 : 1
      ..color = emphLower ? Colors.black87 : const Color(0xFF8D6E63));

    // Vein (vascular bundle) cutting vertically through the mesophyll.
    final emphVein = _sel('Vein');
    final veinRect = Rect.fromLTRB(w * 0.42, h * 0.16, w * 0.58, h * 0.84);
    if (emphVein) drawGlow(canvas, veinRect.center, w * 0.3, const Color(0xFF5C6BC0));
    final veinRRect = RRect.fromRectAndRadius(veinRect, Radius.circular(veinRect.width / 2));
    canvas.drawRRect(veinRRect, Paint()..color = const Color(0xFFE8EAF6).withValues(alpha: 0.95));
    canvas.drawRRect(veinRRect, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphVein ? 2.4 : 1.4
      ..color = emphVein ? Colors.black87 : const Color(0xFF5C6BC0));
    canvas.drawCircle(Offset(veinRect.center.dx, veinRect.top + veinRect.height * 0.3), veinRect.width * 0.28, Paint()..color = const Color(0xFF1E88E5).withValues(alpha: 0.9));
    canvas.drawCircle(Offset(veinRect.center.dx, veinRect.top + veinRect.height * 0.7), veinRect.width * 0.28, Paint()..color = const Color(0xFF43A047).withValues(alpha: 0.9));

    // Stomata with guard cells, on the lower epidermis — a couple of pores.
    final emphStomata = _sel('Stomata');
    for (final fx in [0.20, 0.80]) {
      final cx = w * fx;
      final cy = lowerRect.center.dy;
      if (emphStomata) drawGlow(canvas, Offset(cx, cy), w * 0.06, const Color(0xFFEF6C00));
      // Gap in the epidermis.
      canvas.drawRect(Rect.fromCenter(center: Offset(cx, cy), width: w * 0.05, height: lowerRect.height), Paint()..color = Colors.white);
      // Guard cells (bean pair).
      final guardPaint = Paint()..color = const Color(0xFFEF6C00).withValues(alpha: emphStomata ? 1.0 : 0.85);
      canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy - h * 0.012), width: w * 0.045, height: h * 0.03), guardPaint);
      canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy + h * 0.012), width: w * 0.045, height: h * 0.03), guardPaint);

      // Gas exchange arrows (animated): CO2 in (down), O2 out (up).
      final travel = (t) % 1.0;
      final co2Y = lowerRect.bottom + h * 0.06 - travel * h * 0.05;
      final o2Y = lowerRect.bottom + h * 0.01 + travel * h * 0.05;
      final dotPaint1 = Paint()..color = Colors.blueGrey.withValues(alpha: (1 - travel).clamp(0.0, 1.0));
      final dotPaint2 = Paint()..color = Colors.teal.withValues(alpha: travel.clamp(0.0, 1.0));
      canvas.drawCircle(Offset(cx - w * 0.02, co2Y), 2.4, dotPaint1);
      canvas.drawCircle(Offset(cx + w * 0.02, o2Y), 2.4, dotPaint2);
    }

    _label(canvas, Offset(4, h * 0.02), 'Upper Epidermis', const Color(0xFF8D6E63));
    _label(canvas, Offset(4, h * 0.19), 'Palisade Mesophyll', const Color(0xFF2E7D32));
    _label(canvas, Offset(4, h * 0.58), 'Spongy Mesophyll', const Color(0xFF558B2F));
    _label(canvas, Offset(4, h * 0.90), 'Lower Epidermis', const Color(0xFF8D6E63));
    _label(canvas, Offset(w * 0.62, h * 0.30), 'Vein', const Color(0xFF3949AB));
    _label(canvas, Offset(w * 0.5, h * 0.94), 'Stomata (guard cells)', const Color(0xFFEF6C00), align: TextAlign.center);
  }

  @override
  bool shouldRepaint(covariant _LeafPainter oldDelegate) => true;
}
