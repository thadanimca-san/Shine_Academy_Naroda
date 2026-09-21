import 'dart:async';
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PulleyDynamicsSimulator extends StatefulWidget {
  const PulleyDynamicsSimulator({Key? key}) : super(key: key);

  @override
  _PulleyDynamicsSimulatorState createState() => _PulleyDynamicsSimulatorState();
}

class _PulleyDynamicsSimulatorState extends State<PulleyDynamicsSimulator> with TickerProviderStateMixin {
  // Simulator Parameters
  double m1 = 15.0; // Mass 1 in kg
  double m2 = 10.0; // Mass 2 in kg
  final double g = 9.81; // Gravity m/s^2

  // Physics Simulation States
  double yOffset = 0.0; // Relative displacement of masses (-120 to 120)
  double velocity = 0.0;
  double acceleration = 0.0;
  double tension = 0.0;
  bool isSimulating = false;
  Timer? _timer;

  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _recalculatePhysics();
  }

  void _recalculatePhysics() {
    setState(() {
      // Net Force = (m1 - m2) * g
      // Total Mass = m1 + m2
      // Acceleration a = Net Force / Total Mass
      acceleration = ((m1 - m2) / (m1 + m2)) * g;

      // Tension T = (2 * m1 * m2 * g) / (m1 + m2)
      tension = (2 * m1 * m2 * g) / (m1 + m2);
    });
  }

  void _startSimulation() {
    if (isSimulating) return;

    setState(() {
      isSimulating = true;
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });

    const fps = 60;
    const dt = 1.0 / fps;

    _timer = Timer.periodic(const Duration(milliseconds: 16), (timer) {
      setState(() {
        // Simple Euler integration
        velocity += acceleration * dt;
        yOffset += velocity * 15; // Scaled up visually for canvas display

        // Bound limits for physical collision (pulley top/bottom limits)
        if (yOffset.abs() >= 120.0) {
          yOffset = 120.0 * (yOffset > 0 ? 1 : -1);
          velocity = 0;
          _timer?.cancel();
          isSimulating = false;
        }
      });
    });
  }

  void _resetSimulation() {
    _timer?.cancel();
    setState(() {
      yOffset = 0.0;
      velocity = 0.0;
      isSimulating = false;
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
      _recalculatePhysics();
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Atwood Machine Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
        backgroundColor: Palette.primaryDeep,
        elevation: 0,
        bottom: TabBar(
          controller: _tabController,
          labelColor: Colors.white,
          unselectedLabelColor: Colors.white60,
          indicatorColor: Palette.accent,
          indicatorWeight: 3,
          tabs: const [
            Tab(icon: Icon(Icons.menu_book), text: "1. Intro"),
            Tab(icon: Icon(Icons.functions), text: "2. Derivation"),
            Tab(icon: Icon(Icons.moped), text: "3. Simulation"),
            Tab(icon: Icon(Icons.assignment), text: "4. Exam Drill"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            // TAB 1: FULL CONCEPT TEXTBOOK INTRODUCTION
            _buildIntroductionTab(),

            // TAB 2: EXAM-CRITICAL FORMULA DERIVATIONS
            _buildDerivationTab(),

            // TAB 3: LIVE PHYSICS GRAPHICS SIMULATOR
            _buildSimulationTab(),

            // TAB 4: INTERACTIVE ASSESSMENT DRILL
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRODUCTION VIEW ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("ATWOOD MACHINE DYNAMICS", "NCERT Class 11 / JEE-NEET Mechanics Core"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is an Atwood Machine?",
            "An Atwood machine consists of two unequal masses connected by an inextensible, massless string hanging over a frictionless, massless pulley. It is the classic experimental tool used to demonstrate the basic principles of dynamics and Newton's Second Law of Motion (F = ma).",
            Colors.orange[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Principles:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.black87)),
          const SizedBox(height: 6),
          _buildBulletPoint("Tension Force (T):", "The pulling force transmitted through the string. In an ideal massless string, tension remains completely uniform across its entire length."),
          _buildBulletPoint("System Acceleration (a):", "Since the string cannot stretch (it is inextensible), both masses must move with the exact same acceleration magnitude."),
          _buildBulletPoint("Constraint Equation:", "A relationship that forces coordinates of physical components to rely on each other. If mass m₁ moves downwards by a distance y, mass m₂ must move upwards by that exact distance y."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip directly to Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: MATHEMATICAL DERIVATION VIEW ---
  Widget _buildDerivationTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("THE MATHEMATICAL DERIVATION", "Rigorous Equation of Motion Breakdown"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Equation of Motion for Mass 1 (assuming m1 > m2):\n""   m1·g - T = m1·a   ---- (Eqn 1)\n\n" 
              "2. Equation of Motion for Mass 2:\n" 
              "   T - m2·g = m2·a   ---- (Eqn 2)\n\n" 
              "3. Adding Eqn 1 & Eqn 2 to eliminate Tension (T):\n" 
              "   (m1 - m2)·g = (m1 + m2)·a\n\n" 
              "   Solving for system acceleration (a):\n" 
              "   a = [(m1 - m2) / (m1 + m2)] · g\n\n" 
              "4. Substituting 'a' back to find uniform Tension (T):\n" 
              "   T = [2 · m1 · m2 · g] / (m1 + m2)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE Boundary Case Extremes:",
            "Case 1: If m1 >> m2, system acceleration approaches gravity (a → g) and tension stabilizes around 2·m2·g.\n\n"
            "Case 2: If m1 = m2, the system is in static equilibrium, resulting in no system acceleration (a = 0) and uniform tension (T = m1·g).",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION VIEW ---
  Widget _buildSimulationTab() {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.orange[50],
          child: Text(
            isSimulating ? "🟢 System Tracking: Dynamic Acceleration Active" : "🛑 System Primed: Adjust Weights & Click Simulate",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.orange[900]),
          ),
        ),

        // Interactive Canvas Rendering
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: PulleyPainter(
                  yOffset: yOffset,
                  m1Radius: 15 + (m1 * 0.8).clamp(5.0, 30.0),
                  m2Radius: 15 + (m2 * 0.8).clamp(5.0, 30.0),
                ),
              );
            }),
          ),
        ),

        // Telemetry readout grid
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.orange[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Acceleration (a)", "${acceleration.toStringAsFixed(2)} m/s²"),
              _buildTelemetry("Tension (T)", "${tension.toStringAsFixed(1)} N"),
              _buildTelemetry("Velocity (v)", "${velocity.toStringAsFixed(1)} m/s"),
              _buildTelemetry("Displacement (y)", "${(yOffset / 15).toStringAsFixed(2)} m"),
            ],
          ),
        ),

        // Controls Area
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Move to Competitive Exam Drill ➡️"),
        ),
      ],
    );
  }

  // --- TAB 4: QUIZ/ASSESSMENT VIEW ---
  Widget _buildAssessmentTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ToggleButtons(
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Rank Booster'), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Advanced Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildPulleyQuiz(),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.orange[900])),
        const SizedBox(height: 2),
        Text(subtitle, style: TextStyle(fontSize: 12, color: Colors.blueGrey, fontWeight: FontWeight.w500)),
        const Divider(height: 16, thickness: 1),
      ],
    );
  }

  Widget _buildConceptCard(String title, String body, Color accentColor) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: accentColor.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(8), border: Border.all(color: accentColor.withValues(alpha: 0.3))),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.bold, color: accentColor, fontSize: 14)),
          const SizedBox(height: 6),
          Text(body, style: TextStyle(fontSize: 13, height: 1.4, color: Colors.black87)),
        ],
      ),
    );
  }

  Widget _buildBulletPoint(String label, String body) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.orange[900], fontSize: 16)),
          Expanded(
            child: RichText(
              text: TextSpan(
                style: TextStyle(fontSize: 13, color: Colors.black87, height: 1.3),
                children: [
                  TextSpan(text: "$label ", style: TextStyle(fontWeight: FontWeight.bold)),
                  TextSpan(text: body),
                ],
              ),
            ),
          )
        ],
      ),
    );
  }

  Widget _buildSkipButton(int targetTabIndex, String prompt) {
    return Align(
      alignment: Alignment.centerRight,
      child: TextButton(
        onPressed: () => _tabController.animateTo(targetTabIndex),
        style: TextButton.styleFrom(backgroundColor: Colors.orange[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label.toUpperCase(), style: TextStyle(color: Colors.amberAccent, fontSize: 9, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildPulleyQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "If Mass 1 is set to 30 kg and Mass 2 is set to 10 kg on an ideal frictionless Atwood machine, what is the resulting acceleration of the system in terms of gravity (g)?"
        : "If we substitute the massless string of the Atwood machine with a real rope of total mass 'M_r', how does the acceleration of the system behave as mass m1 moves downward?";

    List<String> options = isNeet
        ? ["a = g", "a = g / 2", "a = g / 3", "a = g / 4"]
        : [
            "Acceleration remains perfectly uniform",
            "Acceleration continuously increases dynamically",
            "Acceleration continuously decreases dynamically",
            "Acceleration drops immediately to zero"
          ];

    int correctIndex = isNeet ? 1 : 1; // Both solutions mapped to index 1

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Dynamics Quiz:" : "JEE Non-Uniform Mass Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
        const SizedBox(height: 6),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: Colors.black87)),
        const SizedBox(height: 8),
        ...List.generate(options.length, (index) {
          Color? tileColor;
          if (_quizEvaluated) {
            if (index == correctIndex) tileColor = Colors.green[50];
            if (_selectedAnswerIndex == index && index != correctIndex) tileColor = Colors.red[50];
          }
          return Container(
            margin: const EdgeInsets.symmetric(vertical: 3),
            child: RadioListTile<int>(
              dense: true,
              contentPadding: const EdgeInsets.symmetric(horizontal: 10),
              tileColor: tileColor ?? Colors.grey[50],
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6), side: BorderSide(color: Colors.grey[200]!)),
              value: index,
              groupValue: _selectedAnswerIndex,
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500)),
              activeColor: Colors.orange[800],
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val)
            ),
          );
        }),
        const SizedBox(height: 12),
        if (!_quizEvaluated && _selectedAnswerIndex != null)
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: () => setState(() => _quizEvaluated = true),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.orange[800], padding: const EdgeInsets.symmetric(vertical: 12)),
              child: Text(TrilingualService.instance.getUIText('Verify Dynamics Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50], borderRadius: BorderRadius.circular(8), border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red)),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet
                    ? "✅ CORRECT ACCELERATION DERIVATION:\n\nUsing a = [(m1 - m2) / (m1 + m2)] · g:\na = [(30 - 10) / (30 + 10)] · g\na = [20 / 40] · g = g / 2."
                    : "✅ CORRECT DYNAMIC ANALYSIS:\n\nAs the rope slides downward, more of its linear mass shifts to the falling side. The effective pulling mass imbalance increases over time, dynamically raising system acceleration.")
                : "❌ CONCEPT MISALIGNMENT:\n\nCheck the mathematical relationships in the Derivation Tab! Double check your forces and mass distribution factors.",
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Colors.black87),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(10),
      color: Colors.white,
      child: Column(
        children: [
          Row(
            children: [
              Expanded(
                child: Column(
                  children: [
                    Text('Mass 1: ${m1.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                    Slider(
                      value: m1,
                      min: 1.0,
                      max: 50.0,
                      divisions: 49,
                      activeColor: Colors.teal,
                      onChanged: isSimulating ? null : (val) {
                        setState(() {
                          m1 = val;
                          _recalculatePhysics();
                        });
                      },
                    )
                  ],
                ),
              ),
              Expanded(
                child: Column(
                  children: [
                    Text('Mass 2: ${m2.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                    Slider(
                      value: m2,
                      min: 1.0,
                      max: 50.0,
                      divisions: 49,
                      activeColor: Colors.orange,
                      onChanged: isSimulating ? null : (val) {
                        setState(() {
                          m2 = val;
                          _recalculatePhysics();
                        });
                      },
                    )
                  ],
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton.icon(
                onPressed: isSimulating ? null : _startSimulation,
                style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
                icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
                label: Text(TrilingualService.instance.getUIText('Simulate System'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
              ),
              IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.blueGrey))
            ],
          ),
        ],
      ),
    );
  }
}

// Draw the Pulley Setup dynamically on Canvas
class PulleyPainter extends CustomPainter {
  final double yOffset;
  final double m1Radius;
  final double m2Radius;

  PulleyPainter({
    required this.yOffset,
    required this.m1Radius,
    required this.m2Radius,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final centerX = size.width / 2;
    const pulleyCenterY = 60.0;
    const pulleyRadius = 30.0;

    final paint = Paint()
      ..color = Colors.white
      ..strokeWidth = 2.0
      ..style = PaintingStyle.stroke;

    final fillPaint = Paint()..style = PaintingStyle.fill;

    // 1. Draw Pulley Wheel
    canvas.drawCircle(Offset(centerX, pulleyCenterY), pulleyRadius, paint);
    canvas.drawCircle(Offset(centerX, pulleyCenterY), 5.0, fillPaint..color = Colors.grey);

    // 2. Draw Strings
    final leftStringX = centerX - pulleyRadius;
    final rightStringX = centerX + pulleyRadius;

    final leftMassY = 150.0 + yOffset;   // Mass 1 (Moves Down when offset is positive)
    final rightMassY = 150.0 - yOffset;  // Mass 2 (Moves Up when offset is positive)

    paint.color = Colors.grey.shade400;
    paint.strokeWidth = 3.0;
    
    // Left side rope
    canvas.drawLine(Offset(leftStringX, pulleyCenterY), Offset(leftStringX, leftMassY), paint);
    // Right side rope
    canvas.drawLine(Offset(rightStringX, pulleyCenterY), Offset(rightStringX, rightMassY), paint);

    // 3. Draw Masses as circular weights
    // Mass 1
    fillPaint.color = Colors.orangeAccent;
    canvas.drawCircle(Offset(leftStringX, leftMassY), m1Radius, fillPaint);
    _drawLabel(canvas, Offset(leftStringX, leftMassY), "m₁");

    // Mass 2
    fillPaint.color = Colors.lightBlueAccent;
    canvas.drawCircle(Offset(rightStringX, rightMassY), m2Radius, fillPaint);
    _drawLabel(canvas, Offset(rightStringX, rightMassY), "m₂");
  }

  void _drawLabel(Canvas canvas, Offset offset, String text) {
    final textPainter = TextPainter(
      text: TextSpan(
        text: text,
        style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold, fontSize: 12),
      ),
      textDirection: TextDirection.ltr,
    );
    textPainter.layout();
    textPainter.paint(
      canvas,
      Offset(offset.dx - textPainter.width / 2, offset.dy - textPainter.height / 2),
    );
  }

  @override
  bool shouldRepaint(covariant PulleyPainter oldDelegate) {
    return oldDelegate.yOffset != yOffset ||
        oldDelegate.m1Radius != m1Radius ||
        oldDelegate.m2Radius != m2Radius;
  }
}