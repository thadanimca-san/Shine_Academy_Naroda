import 'package:flutter/material.dart';

class InteractiveAbacusView extends StatefulWidget {
  const InteractiveAbacusView({super.key});

  @override
  State<InteractiveAbacusView> createState() => _InteractiveAbacusViewState();
}

class AbacusRodModel {
  bool hasUnitDot;
  bool upperActive;
  List<bool> lowerActive;
  AbacusRodModel({required this.hasUnitDot, required this.upperActive, required this.lowerActive});
}

class _InteractiveAbacusViewState extends State<InteractiveAbacusView> {
  final int totalRods = 7;
  late List<AbacusRodModel> rods;
  
  final List<TextEditingController> _controllers = [
    TextEditingController(text: '1'),
    TextEditingController(text: '1'),
    TextEditingController(text: '1'),
    TextEditingController(text: '1'),
    TextEditingController(text: '-2'),
    TextEditingController(text: '-2'),
    TextEditingController(text: '5'),
    TextEditingController(text: '1'),
    TextEditingController(text: '3'),
  ];

  @override
  void initState() {
    super.initState();
    _initRods();
  }

  @override
  void dispose() {
    for (var controller in _controllers) {
      controller.dispose();
    }
    super.dispose();
  }

  void _initRods() {
    rods = List.generate(totalRods, (i) {
      return AbacusRodModel(
        hasUnitDot: (i == totalRods - 3),
        upperActive: false,
        lowerActive: [false, false, false, false],
      );
    });
  }

  void _onTap(Offset localPos, double width, double height, double marginX, double spacingX, double beadWidth) {
    final beamHeight = height * 0.10;
    final beamY = height * 0.28;
    final touchX = localPos.dx;
    final touchY = localPos.dy;

    for (int i = 0; i < rods.length; i++) {
      final rodX = marginX + (i * spacingX);
      if (touchX < rodX - (spacingX * 0.4) || touchX > rodX + beadWidth + (spacingX * 0.4)) continue;

      if (touchY < beamY + (beamHeight / 2)) {
        setState(() => rods[i].upperActive = !rods[i].upperActive);
      } else {
        final beamBottom = beamY + beamHeight;
        int targetIndex = -1;
        double closestDist = double.infinity;
        for (int l = 0; l < 4; l++) {
          final activeY = beamBottom + 2 + (l * beadWidth);
          final inactiveY = height - 2 - ((4 - l) * beadWidth);
          final bY = rods[i].lowerActive[l] ? activeY : inactiveY;
          final dist = (touchY - (bY + beadWidth / 2)).abs();
          if (dist < closestDist) {
            closestDist = dist;
            targetIndex = l;
          }
        }
        if (targetIndex != -1) {
          setState(() {
            final turnActive = !rods[i].lowerActive[targetIndex];
            for (int l = 0; l < 4; l++) {
              if (turnActive && l <= targetIndex) {
                rods[i].lowerActive[l] = true;
              } else if (!turnActive && l >= targetIndex) {
                rods[i].lowerActive[l] = false;
              }
            }
          });
        }
      }
      return;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: AspectRatio(
                aspectRatio: 2.2,
                child: Container(
                  decoration: BoxDecoration(
                    border: Border.all(color: const Color(0xFF3B82F6), width: 4),
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(10),
                    boxShadow: const [
                      BoxShadow(color: Colors.black54, blurRadius: 8, offset: Offset(0, 3)),
                    ],
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(6),
                    child: LayoutBuilder(
                      builder: (context, box) {
                        double width = box.maxWidth;
                        double height = box.maxHeight;
                        double marginX = width * 0.03;
                        double availableW = width - (marginX * 2);
                        double spacingX = availableW / (totalRods - 1);
                        double beadWidth = spacingX * 0.62 * 0.64 * 0.8;

                        return GestureDetector(
                          onTapUp: (details) => _onTap(
                              details.localPosition, width, height, marginX, spacingX, beadWidth),
                          child: CustomPaint(
                            size: Size(width, height),
                            painter: AbacusPainter(
                              rods: rods,
                              marginX: marginX,
                              spacingX: spacingX,
                              beadWidth: beadWidth,
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class AbacusPainter extends CustomPainter {
  final List<AbacusRodModel> rods;
  final double marginX;
  final double spacingX;
  final double beadWidth;

  AbacusPainter({
    required this.rods,
    required this.marginX,
    required this.spacingX,
    required this.beadWidth,
  });

  @override
  void paint(Canvas canvas, Size size) {
    double beamHeight = size.height * 0.10;
    double beamY = size.height * 0.28;
    double beadRadius = beadWidth / 2;
    double beadDiameter = beadWidth;

    Paint rodPaint = Paint()..color = const Color(0xFF3B82F6);
    for (int i = 0; i < rods.length; i++) {
      double rodX = marginX + (i * spacingX);
      canvas.drawRect(Rect.fromLTWH(rodX + beadRadius - 1.2, 2, 2.4, size.height - 4), rodPaint);
    }

    Paint beamPaint = Paint()..color = const Color(0xFF1D4ED8);
    canvas.drawRect(Rect.fromLTWH(0, beamY, size.width, beamHeight), beamPaint);

    Paint dotPaint = Paint()..color = Colors.white;
    for (int i = 0; i < rods.length; i++) {
      if (rods[i].hasUnitDot) {
        double rodX = marginX + (i * spacingX);
        canvas.drawCircle(Offset(rodX + beadRadius, beamY + (beamHeight / 2)), beadRadius * 0.525, dotPaint);
      }
    }

    for (int i = 0; i < rods.length; i++) {
      double rodX = marginX + (i * spacingX);

      // Upper bead
      double upperRestY = 2.0;
      double upperActiveY = beamY - beadDiameter;
      bool isUpperActive = rods[i].upperActive;
      double uY = isUpperActive ? upperActiveY : upperRestY;
      _drawDuolingoBead(canvas, rodX, uY, beadRadius, const Color(0xFFC084FC), const Color(0xFF9333EA), isUpperActive);

      // Lower beads
      double beamBottom = beamY + beamHeight;
      double bottomMargin = 2.0;

      for (int l = 0; l < 4; l++) {
        double activeY = beamBottom + 2 + (l * beadDiameter);
        double restY = size.height - bottomMargin - ((4 - l) * beadDiameter);
        bool isLowerActive = rods[i].lowerActive[l];
        double lY = isLowerActive ? activeY : restY;
        _drawDuolingoBead(canvas, rodX, lY, beadRadius, const Color(0xFFF472B6), const Color(0xFFDB2777), isLowerActive);
      }
    }
  }

  void _drawDuolingoBead(Canvas canvas, double x, double y, double radius, Color mainColor, Color shadowColor, bool isActive) {
    double cx = x + radius;
    double cy = y + radius;

    // Glowing effect when active (touching the counting bar)
    if (isActive) {
      Paint glowPaint = Paint()
        ..color = const Color(0xFFFFD700).withValues(alpha: 0.6)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 8.0);
      canvas.drawCircle(Offset(cx, cy), radius + 3.0, glowPaint);
    }

    Paint shadowPaint = Paint()..color = shadowColor;
    canvas.drawCircle(Offset(cx, cy + 1.2), radius, shadowPaint);

    Paint mainPaint = Paint()..color = mainColor;
    canvas.drawCircle(Offset(cx, cy), radius, mainPaint);

    var gradient = RadialGradient(
      center: const Alignment(-0.4, -0.5),
      radius: 0.8,
      colors: [
        Colors.white.withValues(alpha: isActive ? 1.0 : 0.9),
        Colors.white.withValues(alpha: isActive ? 0.7 : 0.45),
        Colors.white.withValues(alpha: 0.0),
      ],
      stops: const [0.0, 0.35, 1.0],
    );

    Paint highlightPaint = Paint()
      ..shader = gradient.createShader(Rect.fromCircle(center: Offset(cx, cy), radius: radius));
    canvas.drawCircle(Offset(cx, cy), radius, highlightPaint);
  }

  @override
  bool shouldRepaint(covariant AbacusPainter oldDelegate) => true;
}
class AbacusSimulationWidget extends StatelessWidget {
  final Map<String, dynamic> block;

  const AbacusSimulationWidget({super.key, required this.block});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 16.0),
      child: const InteractiveAbacusView(),
    );
  }
}
