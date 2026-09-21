import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class InclinedPlaneSimulator extends StatefulWidget {
  const InclinedPlaneSimulator({Key? key}) : super(key: key);

  @override
  _InclinedPlaneSimulatorState createState() => _InclinedPlaneSimulatorState();
}

class _InclinedPlaneSimulatorState extends State<InclinedPlaneSimulator> with SingleTickerProviderStateMixin {
  double _angleDegrees = 30.0;   // Ramp angle (theta)
  double _muStatic = 0.5;        // Static friction coefficient
  double _muKinetic = 0.35;      // Kinetic friction coefficient
  double _time = 0.0;
  bool _isSlidingActive = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  late AnimationController _controller;

  final double g = 9.8;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 3000))..addListener(() {
      setState(() {
        _time = _controller.value * 3.0; // Simulated seconds elapsed
      });
    });
  }

  void _releaseBlock() {
    setState(() { _isSlidingActive = true; _selectedAnswerIndex = null; _quizEvaluated = false; });
    _controller.reset();
    _controller.forward();
  }

  void _resetSimulation() {
    setState(() { _isSlidingActive = false; _time = 0.0; _selectedAnswerIndex = null; _quizEvaluated = false; });
    _controller.reset();
  }

  @override
  void dispose() { _controller.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext context) {
    double angleRad = _angleDegrees * math.pi / 180.0;
    
    // Acceleration calculations based on threshold properties
    double acceleration;
    bool motionOccurs = math.tan(angleRad) > _muStatic;

    if (motionOccurs) {
      acceleration = g * (math.sin(angleRad) - _muKinetic * math.cos(angleRad));
      if (acceleration < 0) acceleration = 0.0;
    } else {
      acceleration = 0.0;
    }

    // Displacement formula: s = 0.5 * a * t^2
    double tCurrent = _isSlidingActive ? _time : 0.0;
    double currentDisplacement = 0.5 * acceleration * math.pow(tCurrent, 2) * 20.0; // scaled for canvas pixels

    // Clamp displacement to stay within the ramp length limits
    if (currentDisplacement > 180.0) {
      currentDisplacement = 180.0;
      _controller.stop();
    }

    return DefaultTabController(
      length: 4,
      child: Scaffold(
        backgroundColor: Colors.grey[100],
        appBar: AppBar(
          leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              if (Navigator.canPop(context)) {
                Navigator.pop(context);
              }
            },
          ),
          title: Text(TrilingualService.instance.getUIText("Inclined Plane Mechanics"),
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
          ),
          backgroundColor: Colors.deepPurple,
          foregroundColor: Colors.white,
          bottom: const TabBar(
            indicatorColor: Palette.accent,
            indicatorWeight: 3.0,
            labelColor: Colors.white,
            unselectedLabelColor: Colors.white60,
            tabs: [
              Tab(icon: Icon(Icons.menu_book), text: "1. Intro"),
              Tab(icon: Icon(Icons.functions), text: "2. Physics"),
              Tab(icon: Icon(Icons.play_arrow), text: "3. Sim"),
              Tab(icon: Icon(Icons.assignment), text: "4. Drill"),
            ],
          ),
        ),
        body: SafeArea(
          child: TabBarView(
            physics: const NeverScrollableScrollPhysics(), // Prevents conflict between swipe gestures and sliders
            children: [
              // TAB 1: Intro (Theory & Overview)
              SingleChildScrollView(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(TrilingualService.instance.getUIText("GRAVITY RESOLUTION ON A RAMP"),
                      style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.deepPurple),
                    ),
                    Text(TrilingualService.instance.getUIText("The Foundational Pillar of Inclined Plane Dynamics"),
                      style: TextStyle(fontSize: 12, color: Colors.grey),
                    ),
                    const SizedBox(height: 16),
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.blue[50],
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: Colors.blue.shade100),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(TrilingualService.instance.getUIText("What is an Inclined Plane?"),
                            style: TextStyle(fontWeight: FontWeight.bold, color: Colors.blueAccent, fontSize: 14),
                          ),
                          SizedBox(height: 8),
                          Text(TrilingualService.instance.getUIText("An inclined plane is a flat surface tilted at an angle θ to the horizontal. It reduces the effort force needed to raise a load by distributing it over a longer distance, resolving gravity into two distinct perpendicular components."),
                            style: TextStyle(fontSize: 13, height: 1.4),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 20),
                    Text(TrilingualService.instance.getUIText("The Key Force Resolutions:"),
                      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                    ),
                    const SizedBox(height: 8),
                    _buildBulletPoint("Parallel Gravity Component (g sinθ):", "The force pulling the object down along the incline slope."),
                    _buildBulletPoint("Perpendicular Gravity Component (g cosθ):", "The normal force pushing the block down into the ramp surface, dictating friction limits."),
                    _buildBulletPoint("Angle of Repose:", "The threshold angle where pulling force exactly balances static friction: tan(θ) = μ_s."),
                  ],
                ),
              ),

              // TAB 2: Physics (Real-time Dynamic Telemetry)
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(TrilingualService.instance.getUIText("Real-Time Mathematical Resolution"),
                      style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.deepPurple),
                    ),
                    const SizedBox(height: 16),
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.deepPurple[900],
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          _buildTelemetry("Parallel (g sinθ)", "${(g * math.sin(angleRad)).toStringAsFixed(2)} m/s²"),
                          _buildTelemetry("Friction Limit", "${(_muStatic * g * math.cos(angleRad)).toStringAsFixed(2)} m/s²"),
                          _buildTelemetry("State", motionOccurs ? "Accelerating" : "Equilibrium"),
                          _buildTelemetry("Net Accel.", "${acceleration.toStringAsFixed(2)} m/s²"),
                        ],
                      ),
                    ),
                    const SizedBox(height: 20),
                    Text(TrilingualService.instance.getUIText("Formulas in Action:"), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
                    const Divider(),
                    _buildFormulaRow("Normal Force:", "N = g * cos(${_angleDegrees.toStringAsFixed(0)}°) = ${(g * math.cos(angleRad)).toStringAsFixed(2)} m/s²"),
                    _buildFormulaRow("Max Static Friction Limit:", "f_s = μ_s * N = $_muStatic * ${(g * math.cos(angleRad)).toStringAsFixed(2)} = ${(_muStatic * g * math.cos(angleRad)).toStringAsFixed(2)} m/s²"),
                    _buildFormulaRow("Net Pulling Force:", "F_p = g * sin(${_angleDegrees.toStringAsFixed(0)}°) = ${(g * math.sin(angleRad)).toStringAsFixed(2)} m/s²"),
                  ],
                ),
              ),

              // TAB 3: Sim (Canvas & Control Sliders)
              Column(
                children: [
                  Padding(
                    padding: EdgeInsets.symmetric(vertical: 8.0),
                    child: Text(TrilingualService.instance.getUIText("Gravity Resolution & Components"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold)),
                  ),
                  Expanded(
                    child: Container(
                      margin: const EdgeInsets.symmetric(horizontal: 12),
                      decoration: BoxDecoration(color: Colors.deepPurple[50], borderRadius: BorderRadius.circular(12)),
                      child: LayoutBuilder(builder: (context, constraints) {
                        return CustomPaint(
                          size: Size(constraints.maxWidth, constraints.maxHeight),
                          painter: InclinedPlanePainter(
                            angleRad: angleRad,
                            displacement: currentDisplacement,
                            scaleRatio: constraints.maxWidth / 400.0,
                          ),
                        );
                      }),
                    ),
                  ),
                  _buildControlsTray(),
                ],
              ),

              // TAB 4: Drill (Interactive assessment)
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 8.0),
                      child: ToggleButtons(
                        isSelected: [_targetPath == 'NEET', _targetPath == 'JEE'],
                        onPressed: (index) { 
                          setState(() { 
                            _targetPath = index == 0 ? 'NEET' : 'JEE'; 
                            _selectedAnswerIndex = null; 
                            _quizEvaluated = false; 
                          }); 
                        },
                        borderRadius: BorderRadius.circular(8),
                        selectedColor: Colors.white,
                        fillColor: _targetPath == 'NEET' ? Colors.green[600] : Colors.deepOrange,
                        children: [
                          Padding(padding: EdgeInsets.symmetric(horizontal: 16), child: Text(TrilingualService.instance.getUIText('NEET Focus'))),
                          Padding(padding: EdgeInsets.symmetric(horizontal: 16), child: Text(TrilingualService.instance.getUIText('JEE Challenge')))
                        ],
                      ),
                    ),
                    Expanded(
                      child: Container(
                        width: double.infinity, 
                        padding: const EdgeInsets.all(12), 
                        decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(12)),
                        child: SingleChildScrollView(
                          child: _buildRampQuiz(angleRad, motionOccurs),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildBulletPoint(String label, String detail) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.deepPurple, fontSize: 16)),
          Expanded(
            child: RichText(
              text: TextSpan(
                style: TextStyle(color: Theme.of(context).colorScheme.onSurface, fontSize: 13, height: 1.3),
                children: [
                  TextSpan(text: "$label ", style: TextStyle(fontWeight: FontWeight.bold)),
                  TextSpan(text: detail),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFormulaRow(String label, String content) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          Text(content, style: TextStyle(fontFamily: 'monospace', fontSize: 12, fontWeight: FontWeight.bold, color: Colors.deepPurple)),
        ],
      ),
    );
  }

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label, style: TextStyle(color: Colors.amberAccent, fontSize: 10)),
        Text(value, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
      ],
    );
  }

  Widget _buildRampQuiz(double angleRad, bool motionOccurs) {
    bool isNeet = _targetPath == 'NEET';
    double criticalAngleDeg = math.atan(_muStatic) * 180 / math.pi;

    String questionText = isNeet
        ? "What is the critical 'Angle of Repose' threshold for this system below which the block will not move at all?"
        : "If the plane is elevated exactly to its angle of repose, what is the value of static friction force acting on a block of mass 'm'?";

    List<String> options = isNeet
        ? ["${criticalAngleDeg.toStringAsFixed(1)}°", "30.0°", "45.0°", "60.0°"]
        : ["mg sin(θ)", "μ_s mg cos(θ)", "Both are equal", "0.0 N"];

    int correctIndex = isNeet ? 0 : 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Threshold Analysis:" : "JEE Static Equilibrium Proof:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600)),
        const SizedBox(height: 4),
        ...List.generate(options.length, (index) {
          Color? tileColor;
          if (_quizEvaluated) {
            if (index == correctIndex) tileColor = Colors.green[50];
            if (_selectedAnswerIndex == index && index != correctIndex) tileColor = Colors.red[50];
          }
          return Container(
            margin: const EdgeInsets.symmetric(vertical: 2),
            decoration: BoxDecoration(color: tileColor, borderRadius: BorderRadius.circular(6)),
            child: RadioListTile<int>(
              dense: true, 
              contentPadding: EdgeInsets.zero,
              value: index, 
              groupValue: _selectedAnswerIndex, 
              title: Text(options[index], style: TextStyle(fontSize: 12)), 
              activeColor: Colors.deepPurple, 
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val)
            ),
          );
        }),
        const SizedBox(height: 8),
        if (!_quizEvaluated && _selectedAnswerIndex != null)
          SizedBox(
            width: double.infinity, 
            child: ElevatedButton(
              onPressed: () => setState(() => _quizEvaluated = true), 
              style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple, padding: const EdgeInsets.symmetric(vertical: 10)), 
              child: Text(TrilingualService.instance.getUIText('Check Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(6),
            ),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "Correct! 🎉 The angle of repose is defined by tan(θ) = μ_static. For your configured μ_s = $_muStatic, taking the inverse tangent gives exactly ${criticalAngleDeg.toStringAsFixed(1)}°."
                    : "Correct! 🎉 At the threshold limit of repose, the pulling weight force component matches the restraining friction force perfectly: friction = mg sin(θ) = μ_s mg cos(θ).")
                : (isNeet 
                    ? "Incorrect ❌ Remember the angle of repose formula! It depends entirely on the static friction coefficient: θ = tan⁻¹(μ_s). Plug in $_muStatic to get the boundary line."
                    : "Incorrect ❌ Think about balance! At the exact instant before slipping starts, the static friction has stretched to its maximum limits, which exactly cancels out the down-ramp weight component: mg sin(θ)."),
              style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(12), color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Angle (θ): ${_angleDegrees.toStringAsFixed(0)}°', style: TextStyle(fontSize: 10)), Slider(value: _angleDegrees, min: 15, max: 60, divisions: 9, activeColor: Colors.deepPurple, onChanged: _isSlidingActive ? null : (val) => setState(() => _angleDegrees = val))])),
          Expanded(child: Column(children: [Text('μ_static: ${_muStatic.toStringAsFixed(2)}', style: TextStyle(fontSize: 10)), Slider(value: _muStatic, min: 0.3, max: 0.7, divisions: 4, activeColor: Colors.deepOrange, onChanged: _isSlidingActive ? null : (val) => setState(() { _muStatic = val; if (_muKinetic > _muStatic) _muKinetic = _muStatic - 0.1; }))])),
          Expanded(child: Column(children: [Text('μ_kinetic: ${_muKinetic.toStringAsFixed(2)}', style: TextStyle(fontSize: 10)), Slider(value: _muKinetic, min: 0.15, max: 0.5, divisions: 7, activeColor: Colors.amber, onChanged: _isSlidingActive ? null : (val) => setState(() { _muKinetic = math.min(val, _muStatic - 0.05); }))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [ElevatedButton(onPressed: _isSlidingActive ? null : _releaseBlock, style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple), child: Text(TrilingualService.instance.getUIText('Release Block'), style: TextStyle(color: Colors.white))), IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh))]),
      ]),
    );
  }
}

class InclinedPlanePainter extends CustomPainter {
  final double angleRad, displacement, scaleRatio;
  InclinedPlanePainter({required this.angleRad, required this.displacement, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double groundLeftX = 40.0;
    double groundRightX = canvasWidth - 40.0;
    double baseFloorY = canvasHeight - 30.0;

    double rampLength = 220.0;
    double topRampX = groundRightX - (rampLength * math.cos(angleRad));
    double topRampY = baseFloorY - (rampLength * math.sin(angleRad));

    Paint framePaint = Paint()..color = Colors.blueGrey[300]!..strokeWidth = 2.0..style = PaintingStyle.stroke;
    canvas.drawLine(Offset(groundLeftX, baseFloorY), Offset(groundRightX, baseFloorY), framePaint); 
    canvas.drawLine(Offset(groundRightX, baseFloorY), Offset(groundRightX, topRampY), framePaint); 
    canvas.drawLine(Offset(groundRightX, topRampY), Offset(topRampX, baseFloorY), Paint()..color = Colors.black87..strokeWidth = 3.5); 

    double blockStartX = topRampX + (20.0 * math.cos(angleRad));
    double blockStartY = baseFloorY - (20.0 * math.sin(angleRad));

    double currentBlockX = blockStartX + (displacement * math.cos(angleRad));
    double currentBlockY = blockStartY - (displacement * math.sin(angleRad));

    canvas.save();
    canvas.translate(currentBlockX, currentBlockY);
    canvas.rotate(-angleRad); 

    double bW = 36.0;
    double bH = 22.0;
    Rect blockRect = Rect.fromLTWH(-bW / 2, -bH, bW, bH);
    canvas.drawRect(blockRect, Paint()..color = Colors.deepPurple[400]!);

    _drawComponentArrow(canvas, const Offset(0, -11), const Offset(0, 25), Colors.redAccent, 2.0); 
    _drawComponentArrow(canvas, const Offset(0, -11), const Offset(-20, -11), Colors.blueAccent, 2.0); 

    canvas.restore();
    canvas.restore();
  }

  void _drawComponentArrow(Canvas canvas, Offset start, Offset end, Color color, double thickness) {
    Paint p = Paint()..color = color..strokeWidth = thickness..style = PaintingStyle.stroke;
    canvas.drawLine(start, end, p);
    double angle = math.atan2(end.dy - start.dy, end.dx - start.dx);
    canvas.drawLine(end, Offset(end.dx - 6 * math.cos(angle - math.pi / 6), end.dy - 6 * math.sin(angle - math.pi / 6)), p);
    canvas.drawLine(end, Offset(end.dx - 6 * math.cos(angle + math.pi / 6), end.dy - 6 * math.sin(angle + math.pi / 6)), p);
  }

  @override
  bool shouldRepaint(covariant InclinedPlanePainter oldDelegate) => true;
}