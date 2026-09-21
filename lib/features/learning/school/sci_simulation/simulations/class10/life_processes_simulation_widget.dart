import 'package:flutter/material.dart';
import '../common/diagram_helpers.dart';
import '../common/sim_frame.dart';

enum _BodySystem { digestive, respiratory, circulatory, excretory }

/// Real, labeled schematic diagrams of the four human body systems covered
/// in "Life Processes" — digestive, respiratory, circulatory, and
/// excretory — replacing what used to be a single generic pulsing icon.
/// Each organ is hand-drawn to its real shape and is tappable to reveal
/// its function.
class LifeProcessesSimulationWidget extends StatefulWidget {
  const LifeProcessesSimulationWidget({super.key});

  @override
  State<LifeProcessesSimulationWidget> createState() => _LifeProcessesSimulationWidgetState();
}

class _LifeProcessesSimulationWidgetState extends State<LifeProcessesSimulationWidget> {
  _BodySystem _system = _BodySystem.digestive;
  DiagramPart? _selected;

  static const _digestiveParts = [
    DiagramPart(name: 'Mouth', label: 'Mouth', color: Color(0xFFEF6C00), function: 'Teeth and saliva begin the breakdown of food; saliva contains the enzyme amylase, which starts starch digestion.'),
    DiagramPart(name: 'Oesophagus', label: 'Oesophagus', color: Color(0xFFAB47BC), function: 'A muscular tube that pushes food to the stomach using wave-like contractions called peristalsis.'),
    DiagramPart(name: 'Stomach', label: 'Stomach', color: Color(0xFFE53935), function: 'Secretes gastric juices (including HCl and pepsin) that churn food into a semi-liquid paste and kill germs.'),
    DiagramPart(name: 'Liver', label: 'Liver', color: Color(0xFF8D6E63), function: 'Produces bile, which is stored in the gall bladder and helps emulsify (break down) fats in the small intestine.'),
    DiagramPart(name: 'Pancreas', label: 'Pancreas', color: Color(0xFFFFB300), function: 'Secretes pancreatic juice containing enzymes that digest proteins, fats, and carbohydrates in the small intestine.'),
    DiagramPart(name: 'Small Intestine', label: 'Small Intestine', color: Color(0xFF43A047), function: 'The longest part of the tract; digestion is completed here and nutrients are absorbed through finger-like villi.'),
    DiagramPart(name: 'Large Intestine', label: 'Large Intestine', color: Color(0xFF6D4C41), function: 'Absorbs water and some minerals from the undigested food, forming and storing solid waste (faeces).'),
  ];

  static const _respiratoryParts = [
    DiagramPart(name: 'Nasal Cavity', label: 'Nasal Cavity', color: Color(0xFF29B6F6), function: 'Warms, moistens, and filters incoming air using fine hairs and mucus before it travels further.'),
    DiagramPart(name: 'Trachea', label: 'Trachea', color: Color(0xFF66BB6A), function: 'The windpipe — a tube reinforced with cartilage rings that keeps the airway open and carries air to the bronchi.'),
    DiagramPart(name: 'Bronchi', label: 'Bronchi', color: Color(0xFF8D6E63), function: 'Two branches of the trachea, one entering each lung, which further divide into smaller bronchioles.'),
    DiagramPart(name: 'Lungs', label: 'Lungs', color: Color(0xFFEC407A), function: 'A pair of spongy organs that house the branching airways and millions of alveoli where gas exchange occurs.'),
    DiagramPart(name: 'Alveoli', label: 'Alveoli', color: Color(0xFFAB47BC), function: 'Tiny, thin-walled, balloon-like air sacs surrounded by capillaries, where oxygen enters and CO₂ leaves the blood.'),
    DiagramPart(name: 'Diaphragm', label: 'Diaphragm', color: Color(0xFFFFA726), function: 'A dome-shaped muscle below the lungs that contracts (flattens) to draw air in and relaxes to push air out.'),
  ];

  static const _circulatoryParts = [
    DiagramPart(name: 'Right Atrium', label: 'Right Atrium', color: Color(0xFF5C6BC0), function: 'Receives deoxygenated blood returning from the whole body through the vena cava.'),
    DiagramPart(name: 'Right Ventricle', label: 'Right Ventricle', color: Color(0xFF7E57C2), function: 'Pumps deoxygenated blood to the lungs through the pulmonary artery to pick up oxygen.'),
    DiagramPart(name: 'Left Atrium', label: 'Left Atrium', color: Color(0xFFE53935), function: 'Receives oxygenated blood returning from the lungs through the pulmonary vein.'),
    DiagramPart(name: 'Left Ventricle', label: 'Left Ventricle', color: Color(0xFFC62828), function: 'The thickest, most muscular chamber — pumps oxygenated blood out to the entire body through the aorta.'),
    DiagramPart(name: 'Aorta', label: 'Aorta', color: Color(0xFFAD1457), function: 'The body\'s largest artery, carrying oxygen-rich blood from the left ventricle out to every organ.'),
    DiagramPart(name: 'Vena Cava', label: 'Vena Cava', color: Color(0xFF283593), function: 'The body\'s largest vein, returning oxygen-poor blood from the body back into the right atrium.'),
  ];

  static const _excretoryParts = [
    DiagramPart(name: 'Kidney', label: 'Kidney', color: Color(0xFF8D6E63), function: 'A pair of bean-shaped organs that filter nitrogenous waste (like urea) out of the blood, forming urine. Each contains millions of nephrons.'),
    DiagramPart(name: 'Ureter', label: 'Ureter', color: Color(0xFF43A047), function: 'A narrow tube that carries urine from each kidney down to the urinary bladder.'),
    DiagramPart(name: 'Urinary Bladder', label: 'Urinary Bladder', color: Color(0xFF29B6F6), function: 'A muscular sac that stores urine until it is convenient for the body to release it.'),
    DiagramPart(name: 'Urethra', label: 'Urethra', color: Color(0xFFFFA726), function: 'The tube through which urine is finally released from the bladder out of the body.'),
  ];

  List<DiagramPart> get _currentParts => switch (_system) {
        _BodySystem.digestive => _digestiveParts,
        _BodySystem.respiratory => _respiratoryParts,
        _BodySystem.circulatory => _circulatoryParts,
        _BodySystem.excretory => _excretoryParts,
      };

  static const _systemMeta = {
    _BodySystem.digestive: ('Digestive System', Icons.restaurant, Colors.orange),
    _BodySystem.respiratory: ('Respiratory System', Icons.air, Colors.teal),
    _BodySystem.circulatory: ('Circulatory System', Icons.favorite, Colors.red),
    _BodySystem.excretory: ('Excretory System', Icons.water_drop, Colors.blue),
  };

  @override
  Widget build(BuildContext context) {
    final meta = _systemMeta[_system]!;
    return SimFrame(
      title: 'Life Processes in the Human Body',
      icon: Icons.accessibility_new,
      accent: Colors.red.shade600,
      description: 'Tap a labeled organ to see its function. Switch systems below.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _BodySystem.values.map((s) {
              final isSelected = s == _system;
              final m = _systemMeta[s]!;
              return ChoiceChip(
                avatar: Icon(m.$2, size: 16, color: isSelected ? Colors.white : m.$3),
                label: Text(m.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: m.$3,
                backgroundColor: m.$3.withValues(alpha: 0.12),
                onSelected: (_) => setState(() {
                  _system = s;
                  _selected = null;
                }),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          ResponsiveDiagram(
            aspectRatio: 0.8,
            maxWidth: 480,
            backgroundGradient: [meta.$3.withValues(alpha: 0.08), meta.$3.withValues(alpha: 0.03)],
            painter: _BodySystemPainter(system: _system, selectedName: _selected?.name),
            parts: _currentParts,
            hitRects: (size) => _hitRectsFor(_system, size),
            onSelect: (p) => setState(() => _selected = p),
          ),
          const SizedBox(height: 14),
          DiagramPartPicker(parts: _currentParts, selected: _selected, onSelect: (p) => setState(() => _selected = p)),
        ],
      ),
    );
  }
}

/// Canvas-fraction hit boxes, kept in one place so the painter and the tap
/// overlay always agree on where each organ actually is.
Map<String, Rect> _hitRectsFor(_BodySystem system, Size size) {
  final w = size.width, h = size.height;
  Rect f(double l, double t, double r, double b) => Rect.fromLTRB(l * w, t * h, r * w, b * h);

  switch (system) {
    case _BodySystem.digestive:
      return {
        'Mouth': f(0.40, 0.02, 0.60, 0.09),
        'Oesophagus': f(0.44, 0.09, 0.56, 0.22),
        'Liver': f(0.55, 0.20, 0.80, 0.34),
        'Stomach': f(0.20, 0.22, 0.52, 0.40),
        'Pancreas': f(0.35, 0.36, 0.58, 0.44),
        'Small Intestine': f(0.28, 0.44, 0.72, 0.78),
        'Large Intestine': f(0.14, 0.40, 0.86, 0.92),
      };
    case _BodySystem.respiratory:
      return {
        'Nasal Cavity': f(0.38, 0.02, 0.62, 0.10),
        'Trachea': f(0.44, 0.10, 0.56, 0.32),
        'Bronchi': f(0.28, 0.30, 0.72, 0.42),
        'Lungs': f(0.14, 0.32, 0.86, 0.80),
        'Alveoli': f(0.60, 0.55, 0.86, 0.75),
        'Diaphragm': f(0.14, 0.80, 0.86, 0.88),
      };
    case _BodySystem.circulatory:
      return {
        'Vena Cava': f(0.58, 0.06, 0.78, 0.24),
        'Aorta': f(0.30, 0.04, 0.55, 0.22),
        'Right Atrium': f(0.52, 0.28, 0.76, 0.48),
        'Left Atrium': f(0.24, 0.28, 0.48, 0.48),
        'Right Ventricle': f(0.50, 0.48, 0.78, 0.82),
        'Left Ventricle': f(0.20, 0.48, 0.50, 0.86),
      };
    case _BodySystem.excretory:
      return {
        'Kidney': f(0.14, 0.10, 0.44, 0.40),
        'Ureter': f(0.38, 0.38, 0.50, 0.68),
        'Urinary Bladder': f(0.32, 0.66, 0.68, 0.84),
        'Urethra': f(0.45, 0.83, 0.55, 0.94),
      };
  }
}

class _BodySystemPainter extends CustomPainter {
  final _BodySystem system;
  final String? selectedName;

  _BodySystemPainter({required this.system, required this.selectedName});

  @override
  void paint(Canvas canvas, Size size) {
    switch (system) {
      case _BodySystem.digestive:
        _paintDigestive(canvas, size);
        break;
      case _BodySystem.respiratory:
        _paintRespiratory(canvas, size);
        break;
      case _BodySystem.circulatory:
        _paintCirculatory(canvas, size);
        break;
      case _BodySystem.excretory:
        _paintExcretory(canvas, size);
        break;
    }
  }

  bool _sel(String name) => name == selectedName;

  void _organ(Canvas canvas, Rect rect, Color color, String name, {double radius = 10, bool oval = false}) {
    final emphasize = _sel(name);
    if (emphasize) drawGlow(canvas, rect.center, rect.longestSide * 0.6, color);
    final fill = Paint()..color = color.withValues(alpha: 0.8);
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.6 : 1.4
      ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95);
    if (oval) {
      canvas.drawOval(rect, fill);
      canvas.drawOval(rect, stroke);
    } else {
      final rrect = RRect.fromRectAndRadius(rect, Radius.circular(radius));
      canvas.drawRRect(rrect, fill);
      canvas.drawRRect(rrect, stroke);
    }
  }

  void _tube(Canvas canvas, Path path, Color color, String name, double width) {
    final emphasize = _sel(name);
    if (emphasize) {
      final metric = path.computeMetrics().first;
      drawGlow(canvas, metric.getTangentForOffset(metric.length / 2)!.position, width * 1.6, color);
    }
    final stroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = width
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round
      ..color = color.withValues(alpha: emphasize ? 1.0 : 0.85);
    canvas.drawPath(path, stroke);
    if (emphasize) {
      canvas.drawPath(path, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = width + 3
        ..strokeCap = StrokeCap.round
        ..color = Colors.black38);
      canvas.drawPath(path, stroke);
    }
  }

  // ---------------- Digestive ----------------
  void _paintDigestive(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Oesophagus (tube from mouth to stomach).
    final oes = Path()
      ..moveTo(w * 0.5, h * 0.09)
      ..lineTo(w * 0.5, h * 0.22);
    _tube(canvas, oes, const Color(0xFFAB47BC), 'Oesophagus', w * 0.05);

    // Large intestine frame (drawn first, behind).
    final large = Path()
      ..moveTo(w * 0.20, h * 0.46)
      ..lineTo(w * 0.20, h * 0.84)
      ..quadraticBezierTo(w * 0.20, h * 0.90, w * 0.30, h * 0.90)
      ..lineTo(w * 0.42, h * 0.90)
      ..moveTo(w * 0.20, h * 0.46)
      ..moveTo(w * 0.80, h * 0.42)
      ..lineTo(w * 0.80, h * 0.78)
      ..quadraticBezierTo(w * 0.80, h * 0.84, w * 0.70, h * 0.84)
      ..lineTo(w * 0.42, h * 0.84);
    final largeTop = Path()
      ..moveTo(w * 0.20, h * 0.46)
      ..lineTo(w * 0.20, h * 0.42)
      ..quadraticBezierTo(w * 0.20, h * 0.38, w * 0.30, h * 0.38)
      ..lineTo(w * 0.70, h * 0.38)
      ..quadraticBezierTo(w * 0.80, h * 0.38, w * 0.80, h * 0.42);
    final combinedLarge = Path()..addPath(large, Offset.zero)..addPath(largeTop, Offset.zero);
    _tube(canvas, combinedLarge, const Color(0xFF6D4C41), 'Large Intestine', w * 0.055);

    // Small intestine coil (in front of large intestine frame).
    final coil = Path()..moveTo(w * 0.32, h * 0.48);
    const loops = 4;
    for (int i = 0; i < loops; i++) {
      final yTop = h * (0.48 + i * 0.075);
      final yBot = h * (0.52 + i * 0.075);
      coil.quadraticBezierTo(w * 0.68, yTop, w * 0.32, yBot);
      coil.quadraticBezierTo(w * 0.68, yBot + h * 0.02, w * 0.32, yBot + h * 0.04);
    }
    _tube(canvas, coil, const Color(0xFF43A047), 'Small Intestine', w * 0.045);

    // Stomach (J-shaped pouch).
    final stomach = Path()
      ..moveTo(w * 0.5, h * 0.22)
      ..cubicTo(w * 0.30, h * 0.22, w * 0.18, h * 0.28, w * 0.22, h * 0.36)
      ..cubicTo(w * 0.26, h * 0.42, w * 0.38, h * 0.40, w * 0.42, h * 0.35)
      ..lineTo(w * 0.5, h * 0.24)
      ..close();
    final emphStomach = _sel('Stomach');
    if (emphStomach) drawGlow(canvas, Offset(w * 0.32, h * 0.30), w * 0.22, const Color(0xFFE53935));
    canvas.drawPath(stomach, Paint()..color = const Color(0xFFE53935).withValues(alpha: 0.82));
    canvas.drawPath(stomach, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphStomach ? 2.6 : 1.5
      ..color = emphStomach ? Colors.black87 : const Color(0xFFE53935));

    // Liver (wedge, upper right).
    final liver = Path()
      ..moveTo(w * 0.55, h * 0.21)
      ..cubicTo(w * 0.62, h * 0.19, w * 0.80, h * 0.20, w * 0.80, h * 0.28)
      ..cubicTo(w * 0.80, h * 0.34, w * 0.65, h * 0.35, w * 0.56, h * 0.30)
      ..close();
    _fillBlob(canvas, liver, const Color(0xFF8D6E63), 'Liver');

    // Pancreas (small elongated shape).
    final pancreas = Path()
      ..moveTo(w * 0.38, h * 0.38)
      ..cubicTo(w * 0.45, h * 0.36, w * 0.56, h * 0.38, w * 0.58, h * 0.42)
      ..cubicTo(w * 0.50, h * 0.45, w * 0.40, h * 0.43, w * 0.38, h * 0.38)
      ..close();
    _fillBlob(canvas, pancreas, const Color(0xFFFFB300), 'Pancreas');

    // Mouth.
    _organ(canvas, Rect.fromCenter(center: Offset(w * 0.5, h * 0.05), width: w * 0.12, height: h * 0.035), const Color(0xFFEF6C00), 'Mouth', oval: true);

    _labelAt(canvas, Offset(w * 0.5, h * 0.02), 'Mouth', const Color(0xFFEF6C00));
    _labelAt(canvas, Offset(w * 0.58, h * 0.14), 'Oesophagus', const Color(0xFFAB47BC));
    _labelAt(canvas, Offset(w * 0.66, h * 0.19), 'Liver', const Color(0xFF8D6E63));
    _labelAt(canvas, Offset(w * 0.10, h * 0.30), 'Stomach', const Color(0xFFE53935));
    _labelAt(canvas, Offset(w * 0.10, h * 0.42), 'Pancreas', const Color(0xFFFFB300));
    _labelAt(canvas, Offset(w * 0.72, h * 0.58), 'Small\nIntestine', const Color(0xFF43A047));
    _labelAt(canvas, Offset(w * 0.06, h * 0.60), 'Large\nIntestine', const Color(0xFF6D4C41));
  }

  void _fillBlob(Canvas canvas, Path path, Color color, String name) {
    final emphasize = _sel(name);
    if (emphasize) drawGlow(canvas, path.getBounds().center, path.getBounds().longestSide * 0.6, color);
    canvas.drawPath(path, Paint()..color = color.withValues(alpha: 0.82));
    canvas.drawPath(path, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphasize ? 2.6 : 1.4
      ..color = emphasize ? Colors.black87 : color);
  }

  void _labelAt(Canvas canvas, Offset pos, String text, Color color) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 9, fontWeight: FontWeight.w700, color: Colors.black87, height: 1.1)),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 70);
    final bg = Rect.fromLTWH(pos.dx - tp.width / 2 - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.8));
    tp.paint(canvas, Offset(pos.dx - tp.width / 2, pos.dy));
  }

  // ---------------- Respiratory ----------------
  void _paintRespiratory(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Nasal cavity.
    _organ(canvas, Rect.fromCenter(center: Offset(w * 0.5, h * 0.05), width: w * 0.14, height: h * 0.04), const Color(0xFF29B6F6), 'Nasal Cavity', oval: true);

    // Trachea.
    final trachea = Path()
      ..moveTo(w * 0.5, h * 0.09)
      ..lineTo(w * 0.5, h * 0.34);
    _tube(canvas, trachea, const Color(0xFF66BB6A), 'Trachea', w * 0.06);
    // Cartilage ring hints.
    final ringPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.2
      ..color = Colors.white.withValues(alpha: 0.6);
    for (int i = 0; i < 5; i++) {
      final y = h * (0.11 + i * 0.045);
      canvas.drawLine(Offset(w * 0.47, y), Offset(w * 0.53, y), ringPaint);
    }

    // Bronchi (branching Y).
    final bronchi = Path()
      ..moveTo(w * 0.5, h * 0.34)
      ..quadraticBezierTo(w * 0.35, h * 0.38, w * 0.28, h * 0.44)
      ..moveTo(w * 0.5, h * 0.34)
      ..quadraticBezierTo(w * 0.65, h * 0.38, w * 0.72, h * 0.44);
    _tube(canvas, bronchi, const Color(0xFF8D6E63), 'Bronchi', w * 0.04);

    // Lungs (two lobes).
    final leftLung = Path()
      ..moveTo(w * 0.28, h * 0.40)
      ..cubicTo(w * 0.10, h * 0.44, w * 0.10, h * 0.72, w * 0.24, h * 0.80)
      ..cubicTo(w * 0.34, h * 0.85, w * 0.40, h * 0.75, w * 0.38, h * 0.60)
      ..cubicTo(w * 0.37, h * 0.48, w * 0.33, h * 0.42, w * 0.28, h * 0.40)
      ..close();
    final rightLung = Path()
      ..moveTo(w * 0.72, h * 0.40)
      ..cubicTo(w * 0.90, h * 0.44, w * 0.90, h * 0.72, w * 0.76, h * 0.80)
      ..cubicTo(w * 0.66, h * 0.85, w * 0.60, h * 0.75, w * 0.62, h * 0.60)
      ..cubicTo(w * 0.63, h * 0.48, w * 0.67, h * 0.42, w * 0.72, h * 0.40)
      ..close();
    final emphLungs = _sel('Lungs');
    if (emphLungs) {
      drawGlow(canvas, Offset(w * 0.25, h * 0.6), w * 0.2, const Color(0xFFEC407A));
      drawGlow(canvas, Offset(w * 0.75, h * 0.6), w * 0.2, const Color(0xFFEC407A));
    }
    for (final lung in [leftLung, rightLung]) {
      canvas.drawPath(lung, Paint()..color = const Color(0xFFEC407A).withValues(alpha: 0.35));
      canvas.drawPath(lung, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphLungs ? 2.6 : 1.5
        ..color = emphLungs ? Colors.black87 : const Color(0xFFEC407A));
    }

    // Bronchioles + alveoli clusters inside right lung.
    final broncholiePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.3
      ..color = const Color(0xFF8D6E63).withValues(alpha: 0.8);
    canvas.drawLine(Offset(w * 0.72, h * 0.44), Offset(w * 0.80, h * 0.56), broncholiePaint);
    canvas.drawLine(Offset(w * 0.72, h * 0.44), Offset(w * 0.68, h * 0.60), broncholiePaint);

    final emphAlv = _sel('Alveoli');
    if (emphAlv) drawGlow(canvas, Offset(w * 0.76, h * 0.62), w * 0.14, const Color(0xFFAB47BC));
    final alvPaint = Paint()..color = const Color(0xFFAB47BC).withValues(alpha: 0.85);
    final alvStroke = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphAlv ? 2.2 : 1
      ..color = emphAlv ? Colors.black87 : const Color(0xFFAB47BC);
    const alvOffsets = [Offset(0, 0), Offset(0.035, -0.02), Offset(0.035, 0.02), Offset(-0.03, 0.03), Offset(0.06, 0)];
    for (final o in alvOffsets) {
      final c = Offset(w * (0.78 + o.dx), h * (0.63 + o.dy));
      canvas.drawCircle(c, w * 0.02, alvPaint);
      canvas.drawCircle(c, w * 0.02, alvStroke);
    }

    // Diaphragm.
    final diaphragm = Path()
      ..moveTo(w * 0.14, h * 0.84)
      ..quadraticBezierTo(w * 0.5, h * 0.78, w * 0.86, h * 0.84);
    _tube(canvas, diaphragm, const Color(0xFFFFA726), 'Diaphragm', w * 0.025);

    _labelAt(canvas, Offset(w * 0.5, h * 0.02), 'Nasal\nCavity', const Color(0xFF29B6F6));
    _labelAt(canvas, Offset(w * 0.62, h * 0.22), 'Trachea', const Color(0xFF66BB6A));
    _labelAt(canvas, Offset(w * 0.5, h * 0.37), 'Bronchi', const Color(0xFF8D6E63));
    _labelAt(canvas, Offset(w * 0.15, h * 0.60), 'Lung', const Color(0xFFEC407A));
    _labelAt(canvas, Offset(w * 0.90, h * 0.66), 'Alveoli', const Color(0xFFAB47BC));
    _labelAt(canvas, Offset(w * 0.5, h * 0.90), 'Diaphragm', const Color(0xFFFFA726));
  }

  // ---------------- Circulatory ----------------
  void _paintCirculatory(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Great vessels.
    final vena = Path()
      ..moveTo(w * 0.68, h * 0.06)
      ..lineTo(w * 0.68, h * 0.30);
    _tube(canvas, vena, const Color(0xFF283593), 'Vena Cava', w * 0.06);
    final aorta = Path()
      ..moveTo(w * 0.4, h * 0.04)
      ..quadraticBezierTo(w * 0.3, h * 0.10, w * 0.34, h * 0.26);
    _tube(canvas, aorta, const Color(0xFFAD1457), 'Aorta', w * 0.055);

    // Heart outline (whole shape), then chambers on top.
    final outline = Path()
      ..moveTo(w * 0.5, h * 0.30)
      ..cubicTo(w * 0.20, h * 0.22, w * 0.10, h * 0.55, w * 0.32, h * 0.75)
      ..cubicTo(w * 0.42, h * 0.85, w * 0.5, h * 0.90, w * 0.5, h * 0.90)
      ..cubicTo(w * 0.5, h * 0.90, w * 0.58, h * 0.85, w * 0.68, h * 0.75)
      ..cubicTo(w * 0.90, h * 0.55, w * 0.80, h * 0.22, w * 0.5, h * 0.30)
      ..close();
    canvas.drawPath(outline, Paint()..color = const Color(0xFFFFEBEE));
    canvas.drawPath(outline, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2
      ..color = const Color(0xFFB71C1C).withValues(alpha: 0.5));

    // Chambers are the heart outline intersected with each quadrant, so
    // every chamber inherits the heart's organic curve at its outer edge
    // instead of looking like a plain rectangle dropped on top.
    void chamber(Rect quadrant, Color color, String name) {
      final quadPath = Path()..addRect(quadrant);
      final path = Path.combine(PathOperation.intersect, outline, quadPath);
      final emphasize = _sel(name);
      if (emphasize) drawGlow(canvas, path.getBounds().center, path.getBounds().longestSide * 0.55, color);
      canvas.drawPath(path, Paint()..color = color.withValues(alpha: 0.85));
      canvas.drawPath(path, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphasize ? 2.6 : 1.4
        ..color = emphasize ? Colors.black87 : color.withValues(alpha: 0.95));
    }

    chamber(Rect.fromLTRB(w * 0.5, h * 0.15, w * 1.0, h * 0.52), const Color(0xFF5C6BC0), 'Right Atrium');
    chamber(Rect.fromLTRB(w * 0.0, h * 0.15, w * 0.5, h * 0.52), const Color(0xFFE53935), 'Left Atrium');
    chamber(Rect.fromLTRB(w * 0.5, h * 0.52, w * 1.0, h * 1.0), const Color(0xFF7E57C2), 'Right Ventricle');
    chamber(Rect.fromLTRB(w * 0.0, h * 0.52, w * 0.5, h * 1.0), const Color(0xFFC62828), 'Left Ventricle');

    // Septum, redrawn on top of the chamber fills.
    canvas.drawLine(Offset(w * 0.5, h * 0.32), Offset(w * 0.5, h * 0.86), Paint()
      ..strokeWidth = 3
      ..color = const Color(0xFFB71C1C).withValues(alpha: 0.5));

    _labelAt(canvas, Offset(w * 0.86, h * 0.14), 'Vena\nCava', const Color(0xFF283593));
    _labelAt(canvas, Offset(w * 0.16, h * 0.10), 'Aorta', const Color(0xFFAD1457));
    _labelAt(canvas, Offset(w * 0.90, h * 0.40), 'Right\nAtrium', const Color(0xFF5C6BC0));
    _labelAt(canvas, Offset(w * 0.10, h * 0.40), 'Left\nAtrium', const Color(0xFFE53935));
    _labelAt(canvas, Offset(w * 0.90, h * 0.68), 'Right\nVentricle', const Color(0xFF7E57C2));
    _labelAt(canvas, Offset(w * 0.10, h * 0.68), 'Left\nVentricle', const Color(0xFFC62828));
  }

  // ---------------- Excretory ----------------
  void _paintExcretory(Canvas canvas, Size size) {
    final w = size.width, h = size.height;

    // Ureters.
    final ureterL = Path()
      ..moveTo(w * 0.32, h * 0.36)
      ..quadraticBezierTo(w * 0.34, h * 0.55, w * 0.42, h * 0.68);
    final ureterR = Path()
      ..moveTo(w * 0.68, h * 0.36)
      ..quadraticBezierTo(w * 0.66, h * 0.55, w * 0.58, h * 0.68);
    _tube(canvas, ureterL, const Color(0xFF43A047), 'Ureter', w * 0.03);
    _tube(canvas, ureterR, const Color(0xFF43A047), 'Ureter', w * 0.03);

    // Kidneys (bean shapes).
    Path bean(double cx, double cy, double scale) {
      return Path()
        ..moveTo(cx, cy - 0.12 * scale)
        ..cubicTo(cx + 0.11 * scale, cy - 0.12 * scale, cx + 0.13 * scale, cy + 0.05 * scale, cx + 0.08 * scale, cy + 0.12 * scale)
        ..cubicTo(cx + 0.02 * scale, cy + 0.16 * scale, cx - 0.02 * scale, cy + 0.10 * scale, cx - 0.06 * scale, cy + 0.05 * scale)
        ..cubicTo(cx - 0.12 * scale, cy + 0.02 * scale, cx - 0.13 * scale, cy - 0.10 * scale, cx - 0.02 * scale, cy - 0.12 * scale)
        ..close();
    }

    final leftKidney = bean(w * 0.24, h * 0.22, w);
    final rightKidney = bean(w * 0.76, h * 0.22, w);
    final emphKidney = _sel('Kidney');
    if (emphKidney) {
      drawGlow(canvas, Offset(w * 0.24, h * 0.22), w * 0.16, const Color(0xFF8D6E63));
      drawGlow(canvas, Offset(w * 0.76, h * 0.22), w * 0.16, const Color(0xFF8D6E63));
    }
    for (final k in [leftKidney, rightKidney]) {
      canvas.drawPath(k, Paint()..color = const Color(0xFF8D6E63).withValues(alpha: 0.82));
      canvas.drawPath(k, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphKidney ? 2.6 : 1.5
        ..color = emphKidney ? Colors.black87 : const Color(0xFF8D6E63));
    }

    // Bladder.
    final bladder = Path()
      ..moveTo(w * 0.38, h * 0.68)
      ..cubicTo(w * 0.30, h * 0.68, w * 0.28, h * 0.80, w * 0.5, h * 0.82)
      ..cubicTo(w * 0.72, h * 0.80, w * 0.70, h * 0.68, w * 0.62, h * 0.68)
      ..close();
    _fillBlob(canvas, bladder, const Color(0xFF29B6F6), 'Urinary Bladder');

    // Urethra.
    final urethra = Path()
      ..moveTo(w * 0.5, h * 0.82)
      ..lineTo(w * 0.5, h * 0.92);
    _tube(canvas, urethra, const Color(0xFFFFA726), 'Urethra', w * 0.035);

    _labelAt(canvas, Offset(w * 0.24, h * 0.08), 'Kidney', const Color(0xFF8D6E63));
    _labelAt(canvas, Offset(w * 0.76, h * 0.08), 'Kidney', const Color(0xFF8D6E63));
    _labelAt(canvas, Offset(w * 0.14, h * 0.55), 'Ureter', const Color(0xFF43A047));
    _labelAt(canvas, Offset(w * 0.5, h * 0.75), 'Bladder', const Color(0xFF29B6F6));
    _labelAt(canvas, Offset(w * 0.5, h * 0.95), 'Urethra', const Color(0xFFFFA726));
  }

  @override
  bool shouldRepaint(covariant _BodySystemPainter oldDelegate) =>
      oldDelegate.system != system || oldDelegate.selectedName != selectedName;
}
