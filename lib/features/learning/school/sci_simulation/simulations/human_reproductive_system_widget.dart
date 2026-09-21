import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _ReproPart {
  final String name;
  final String function;
  final Offset anchor; // fractional position within the diagram
  const _ReproPart(this.name, this.function, this.anchor);
}

const _maleParts = [
  _ReproPart('Testis', 'Produces sperm (male gametes) and hormones that control sperm production and puberty changes.', Offset(0.42, 0.62)),
  _ReproPart('Scrotum', 'A pouch of skin holding the testes slightly cooler than body temperature, which sperm formation needs.', Offset(0.42, 0.78)),
  _ReproPart('Vas Deferens', 'A long tube that carries sperm from the testis toward the urethra.', Offset(0.35, 0.4)),
  _ReproPart('Prostate Gland', 'Adds fluid that nourishes sperm and helps them stay active and mobile.', Offset(0.55, 0.42)),
];

const _femaleParts = [
  _ReproPart('Ovary', 'Produces eggs (female gametes) and hormones that control the menstrual cycle and puberty changes.', Offset(0.72, 0.32)),
  _ReproPart('Fallopian Tube (Oviduct)', 'Carries the egg from the ovary to the uterus; this is usually where fertilisation happens.', Offset(0.55, 0.22)),
  _ReproPart('Uterus', 'A bag-like, muscular organ where a fertilised egg implants and a foetus develops during pregnancy.', Offset(0.42, 0.42)),
  _ReproPart('Cervix', 'The narrow passage connecting the uterus to the vagina.', Offset(0.42, 0.68)),
];

/// A simple, clinical, textbook-style labelled diagram of the human male
/// and female reproductive systems, matching NCERT's own figure labels.
/// Tapping a label shows its function — same tap-to-explore pattern used
/// for the cell organelle diagram, kept deliberately plain (schematic
/// shapes only, no illustrative detail) to stay age-appropriate.
class HumanReproductiveSystemWidget extends StatefulWidget {
  const HumanReproductiveSystemWidget({super.key});

  @override
  State<HumanReproductiveSystemWidget> createState() => _HumanReproductiveSystemWidgetState();
}

class _HumanReproductiveSystemWidgetState extends State<HumanReproductiveSystemWidget> {
  bool _isMale = true;
  _ReproPart? _selected;

  @override
  Widget build(BuildContext context) {
    final parts = _isMale ? _maleParts : _femaleParts;
    return SimFrame(
      title: 'Human Reproductive System',
      icon: Icons.family_restroom,
      accent: const Color(0xFF7A5AA8),
      description: 'A simple labelled diagram, same style as your textbook. Tap a label to see its function.',
      actions: [
        ToggleButtons(
          isSelected: [_isMale, !_isMale],
          onPressed: (i) => setState(() {
            _isMale = i == 0;
            _selected = null;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: const Color(0xFF7A5AA8),
          constraints: const BoxConstraints(minHeight: 34, minWidth: 58),
          children: [Text(TrilingualService.instance.getUIText('Male')), Text(TrilingualService.instance.getUIText('Female'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(
            aspectRatio: 1.3,
            child: Container(
              decoration: BoxDecoration(color: const Color(0xFFF3EEF9), borderRadius: BorderRadius.circular(12), border: Border.all(color: Colors.grey.shade300)),
              child: LayoutBuilder(
                builder: (context, constraints) {
                  return Stack(
                    children: [
                      Positioned.fill(
                        child: CustomPaint(painter: _SchematicPainter(isMale: _isMale)),
                      ),
                      for (final p in parts)
                        Positioned(
                          left: p.anchor.dx * constraints.maxWidth - 9,
                          top: p.anchor.dy * constraints.maxHeight - 9,
                          child: GestureDetector(
                            onTap: () => setState(() => _selected = p),
                            child: Container(
                              width: 18,
                              height: 18,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: _selected?.name == p.name ? const Color(0xFF7A5AA8) : const Color(0xFF7A5AA8).withValues(alpha: 0.35),
                                border: Border.all(color: Colors.white, width: 2),
                              ),
                            ),
                          ),
                        ),
                    ],
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: parts.map((p) {
              final isSelected = _selected?.name == p.name;
              return ActionChip(
                label: Text(p.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? const Color(0xFF7A5AA8) : const Color(0xFF7A5AA8).withValues(alpha: 0.18),
                onPressed: () => setState(() => _selected = p),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selected == null
                ? Text(TrilingualService.instance.getUIText('Tap a labelled point or a chip above to see what it does.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(_selected!.name, style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF7A5AA8), fontSize: 14)),
                      const SizedBox(height: 4),
                      Text(_selected!.function, style: TextStyle(fontSize: 13)),
                    ],
                  ),
          ),
        ],
      ),
    );
  }
}

/// Deliberately plain schematic outlines (rounded shapes, no anatomical
/// illustration) so the diagram stays clinical and textbook-like.
class _SchematicPainter extends CustomPainter {
  final bool isMale;
  _SchematicPainter({required this.isMale});

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final outline = Paint()
      ..color = const Color(0xFF7A5AA8).withValues(alpha: 0.55)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.2;
    final fill = Paint()..color = const Color(0xFF7A5AA8).withValues(alpha: 0.12);

    if (isMale) {
      // Vas deferens tubes (two curved lines meeting at a central point).
      final path = Path()
        ..moveTo(w * 0.35, h * 0.4)
        ..quadraticBezierTo(w * 0.45, h * 0.3, w * 0.5, h * 0.45)
        ..quadraticBezierTo(w * 0.55, h * 0.3, w * 0.55, h * 0.42);
      canvas.drawPath(path, outline);
      // Scrotum + testes.
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.47, h * 0.75), width: w * 0.22, height: h * 0.22), fill);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.47, h * 0.75), width: w * 0.22, height: h * 0.22), outline);
      canvas.drawCircle(Offset(w * 0.42, h * 0.62), 8, fill);
      canvas.drawCircle(Offset(w * 0.42, h * 0.62), 8, outline);
      // Prostate gland.
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.55, h * 0.42), width: w * 0.1, height: h * 0.06), fill);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.55, h * 0.42), width: w * 0.1, height: h * 0.06), outline);
    } else {
      // Uterus (inverted triangle-ish bag shape).
      final uterus = Path()
        ..moveTo(w * 0.32, h * 0.3)
        ..lineTo(w * 0.52, h * 0.3)
        ..lineTo(w * 0.47, h * 0.55)
        ..lineTo(w * 0.37, h * 0.55)
        ..close();
      canvas.drawPath(uterus, fill);
      canvas.drawPath(uterus, outline);
      // Cervix + vagina stem.
      canvas.drawRect(Rect.fromLTWH(w * 0.4, h * 0.55, w * 0.04, h * 0.2), outline);
      // Fallopian tubes curving out to ovaries on both sides.
      final leftTube = Path()..moveTo(w * 0.32, h * 0.32)..quadraticBezierTo(w * 0.2, h * 0.25, w * 0.14, h * 0.32);
      final rightTube = Path()..moveTo(w * 0.52, h * 0.32)..quadraticBezierTo(w * 0.65, h * 0.25, w * 0.72, h * 0.32);
      canvas.drawPath(leftTube, outline);
      canvas.drawPath(rightTube, outline);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.13, h * 0.32), width: w * 0.09, height: h * 0.09), fill);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.13, h * 0.32), width: w * 0.09, height: h * 0.09), outline);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.72, h * 0.32), width: w * 0.09, height: h * 0.09), fill);
      canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.72, h * 0.32), width: w * 0.09, height: h * 0.09), outline);
    }
  }

  @override
  bool shouldRepaint(covariant _SchematicPainter oldDelegate) => oldDelegate.isMale != isMale;
}
