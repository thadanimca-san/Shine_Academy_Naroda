import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class WorkEnergyTheoremSimulator extends StatefulWidget {
  const WorkEnergyTheoremSimulator({Key? key}) : super(key: key);

  @override
  _WorkEnergyTheoremSimulatorState createState() => _WorkEnergyTheoremSimulatorState();
}

class _WorkEnergyTheoremSimulatorState extends State<WorkEnergyTheoremSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _mass = 3.0;            // Mass of block (kg)
  double _appliedForce = 25.0;   // Constant horizontal push (N)
  double _muKinetic = 0.30;      // Kinetic friction coefficient
  double _time = 0.0;
  bool _isMoving = false;
  
  // Selection & control states
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late AnimationController _physicsController;
  late TabController _tabController;

  final double g = 9.8;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Defaults to Tab 3 (Sandbox)
    
    _physicsController = AnimationController(
      vsync: this, 
      duration: const Duration(milliseconds: 2500)
    )..addListener(() {
      setState(() {
        _time = _physicsController.value * 2.5; // Simulated seconds elapsed
      });
    });
  }

  void _startSimulation() {
    setState(() { 
      _isMoving = true; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
    _physicsController.reset();
    _physicsController.forward();
  }

  void _resetSimulation() {
    setState(() { 
      _isMoving = false; 
      _time = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
    _physicsController.reset();
  }

  @override
  void dispose() { 
    _physicsController.dispose(); 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    // 1. Calculate Forces
    double frictionForce = _muKinetic * _mass * g;
    double netForce = _appliedForce - frictionForce;
    if (netForce < 0) netForce = 0.0;

    // 2. Kinematics & Work Math
    double acceleration = netForce / _mass;
    double tCurrent = _isMoving ? _time : 0.0;
    
    // Displacement: d = 0.5 * a * t^2
    double displacement = 0.5 * acceleration * tCurrent * tCurrent;
    
    // Scale displacement for a 400px baseline track representation
    double visualDisplacement = displacement * 30.0; 
    if (visualDisplacement > 220.0) {
      visualDisplacement = 220.0;
      _physicsController.stop();
      // Recalculate exact real-world displacement at boundary clamp
      displacement = 220.0 / 30.0;
    }

    // Work Integrals / Products
    double workApplied = _appliedForce * displacement;
    double workFriction = -frictionForce * displacement;
    double workNet = netForce * displacement;

    // Kinetic Energy: KE = 0.5 * m * v^2 = Work Net (starting from rest)
    double currentVelocity = acceleration * tCurrent;
    double kineticEnergy = 0.5 * _mass * currentVelocity * currentVelocity;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Work-Energy Theorem"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)), 
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
            Tab(icon: Icon(Icons.functions), text: "2. Formulas"),
            Tab(icon: Icon(Icons.play_arrow), text: "3. Sandbox"),
            Tab(icon: Icon(Icons.assignment), text: "4. Test Prep"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroTab(),
            _buildFormulaTab(frictionForce),
            _buildSandboxTab(visualDisplacement, frictionForce, workApplied, workFriction, workNet, kineticEnergy, displacement, currentVelocity),
            _buildTestPrepTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRO ---
  Widget _buildIntroTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("WORK, ENERGY, AND POWER", "NCERT Class 11 Physics | Chapter 6"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "The Work-Energy Theorem",
            "The theorem states that the work done by the net force acting on a body is equal to the change in its kinetic energy. This remarkably powerful principle simplifies solving complex motion problems because it bypasses Newton's second law equations of acceleration over time and looks directly at initial and final energy states.",
            Palette.primaryDeep
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Crucial Academic Insights:"), style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint(
            "Conservative vs. Non-Conservative Work:", 
            "Both conservative forces (like gravity or springs) and non-conservative forces (like friction or applied push) contribute to the net work done. Every single active force must be included when calculating W_net."
          ),
          _buildBulletPoint(
            "Scalar Mechanics:", 
            "Work and Energy are scalar quantities. While force and displacement are vectors, their dot product (Work) is a pure number. Friction does negative work here because the friction vector opposes the displacement vector."
          ),
          _buildBulletPoint(
            "Frame Dependence:", 
            "While work and kinetic energy can vary depending on your frame of reference, the equality (W_net = \u0394KE) holds true in any inertial frame."
          ),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Review Equations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULAS ---
  Widget _buildFormulaTab(double frictionForce) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL FORMULATIONS", "Work-Energy Theorem Core Relationships"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. General Work-Energy Theorem:\n""   W_net = KE_final - KE_initial = \u0394KE\n\n" 
              "2. Component-Wise Work Expansion:\n" 
              "   W_net = W_applied + W_friction + W_gravity + W_normal\n\n" 
              "3. Calculus Definition (Variable Forces):\n" 
              "   W = \u222b F \u00b7 dx\n\n" 
              "4. Sliding Dynamics on Flat Ground:\n" 
              "   \u2022 Friction Force (f_k) = \u03bc_k \u00b7 m \u00b7 g\n" 
              "   \u2022 W_applied = F_applied \u00b7 d\n" 
              "   \u2022 W_friction = -f_k \u00b7 d"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.tealAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "High-Yield Exam Pointer:",
            "In competitive exams, remember that kinetic friction always acts parallel to the contact surface in a direction opposite to the relative motion. Therefore, the angle \u03b8 between friction and displacement is 180 degrees, leading to Cos(180) = -1, which is why frictional work is mathematically negative.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Sandbox Workspace ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SANDBOX ---
  Widget _buildSandboxTab(
    double visualDisplacement, 
    double frictionForce, 
    double workApplied, 
    double workFriction, 
    double workNet, 
    double kineticEnergy, 
    double displacement, 
    double currentVelocity
  ) {
    return Column(
      children: [
        // Vector Canvas
        Expanded(
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Palette.primarySoft, borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: WorkEnergyPainter(
                  displacement: visualDisplacement,
                  appliedForce: _appliedForce,
                  frictionForce: frictionForce,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),

        // Telemetry Panels
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(color: Palette.primaryDeep, borderRadius: BorderRadius.circular(10)),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildTelemetry("W(Applied)", "+${workApplied.toStringAsFixed(1)} J", Colors.greenAccent),
                  _buildTelemetry("W(Friction)", "${workFriction.toStringAsFixed(1)} J", Colors.redAccent),
                  _buildTelemetry("Net Work (W_net)", "${workNet.toStringAsFixed(1)} J", Colors.amberAccent),
                  _buildTelemetry("System KE", "${kineticEnergy.toStringAsFixed(1)} J", Colors.cyanAccent),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                "Displacement: ${displacement.toStringAsFixed(2)} m  |  Velocity: ${currentVelocity.toStringAsFixed(2)} m/s",
                style: TextStyle(color: Colors.white70, fontSize: 11, fontStyle: FontStyle.italic),
              )
            ],
          ),
        ),

        // Input Controls Tray
        _buildControlsTray(frictionForce),
        const SizedBox(height: 8),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12),
          child: _buildSkipButton(3, "Practice Exam Questions ➡️"),
        ),
        const SizedBox(height: 8),
      ],
    );
  }

  // --- TAB 4: TEST PREP ---
  Widget _buildTestPrepTab() {
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Focus'), style: TextStyle(fontWeight: FontWeight.bold))), 
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildTheoremQuiz(),
        ],
      ),
    );
  }

  // --- UTILITY UI BUILDERS ---
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Palette.primaryDeep)),
        const SizedBox(height: 2),
        Text(subtitle, style: TextStyle(fontSize: 11, color: Colors.blueGrey, fontWeight: FontWeight.bold)),
        const Divider(height: 16, thickness: 1),
      ],
    );
  }

  Widget _buildConceptCard(String title, String body, Color accentColor) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: accentColor.withValues(alpha: 0.06), 
        borderRadius: BorderRadius.circular(8), 
        border: Border.all(color: accentColor.withValues(alpha: 0.3))
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.bold, color: accentColor, fontSize: 13)),
          const SizedBox(height: 6),
          Text(body, style: TextStyle(fontSize: 13, height: 1.4, color: Theme.of(context).colorScheme.onSurface)),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Palette.primaryDeep, fontSize: 16)),
          Expanded(
            child: RichText(
              text: TextSpan(
                style: TextStyle(fontSize: 13, color: Theme.of(context).colorScheme.onSurface, height: 1.3),
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
        style: TextButton.styleFrom(
          backgroundColor: Palette.primary, 
          foregroundColor: Colors.white, 
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)
        ),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value, Color valColor) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label, style: TextStyle(color: Colors.white70, fontSize: 10)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: valColor, fontSize: 12, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildTheoremQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "A constant force performs 60 J of positive work pushing a block, while friction simultaneously does -20 J of negative work. What is the net change in the block's Kinetic Energy?"
        : "An object moving with velocity 'v' is brought to rest over a displacement distance 'd' by a constant braking friction force 'f'. If the initial velocity is doubled (2v), what braking distance is required under the same friction force?";

    List<String> options = isNeet
        ? ["80 J", "40 J", "20 J", "-40 J"]
        : ["2 * d", "3 * d", "4 * d", "Remains d"];

    int correctIndex = isNeet ? 1 : 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          isNeet ? "NEET Basic Scalar Addition:" : "JEE Work-Kinetic Proof:", 
          style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)
        ),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600)),
        const SizedBox(height: 6),
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
              contentPadding: const EdgeInsets.symmetric(horizontal: 8),
              value: index, 
              groupValue: _selectedAnswerIndex, 
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)), 
              activeColor: Palette.primary, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Palette.primary, padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Check Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red),
            ),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "Correct! \u{1F389} According to the Work-Energy Theorem:\n"
                      "W_net = \u0394KE (Change in Kinetic Energy)\n\n"
                      "Simply sum the scalar work values directly:\n"
                      "W_net = 60 J + (-20 J) = 40 J."
                    : "Correct! \u{1F389} Kinetic energy scales quadratically with speed:\n"
                      "KE = 1/2 * m * v^2\n\n"
                      "Doubling velocity (2v) quadruples (4x) the initial kinetic energy. Since:\n"
                      "Work = -f * d = \u0394KE\n\n"
                      "To dissipate four times the energy with the same stopping friction force 'f', it requires 4 times the original stopping distance (4d).")
                : (isNeet 
                    ? "Incorrect \u274C Work is a scalar quantity! Add them algebraically:\n"
                      "W_net = W_applied + W_friction\n\n"
                      "Here, 60 J - 20 J yields a net kinetic energy change of 40 J."
                    : "Incorrect \u274C Remember the quadratic relationship between velocity and kinetic energy:\n"
                      "-f * d = 0 - 1/2 * m * v^2\n\n"
                      "If the initial speed 'v' is doubled (2v), the kinetic energy becomes four times larger, demanding four times the braking distance (4d) to come to rest."),
              style: TextStyle(fontSize: 12, height: 1.4, fontWeight: FontWeight.w500, color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray(double frictionForce) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8), 
      color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Mass: ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 1, max: 5, divisions: 4, activeColor: Colors.blueGrey, onChanged: _isMoving ? null : (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Push Force: ${_appliedForce.toStringAsFixed(0)} N', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _appliedForce, min: 15, max: 40, divisions: 5, activeColor: Colors.green, onChanged: _isMoving ? null : (val) => setState(() => _appliedForce = val))])),
          Expanded(child: Column(children: [Text('Friction \u03BC_k: ${_muKinetic.toStringAsFixed(2)}', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _muKinetic, min: 0.1, max: 0.5, divisions: 4, activeColor: Colors.red, onChanged: _isMoving ? null : (val) => setState(() => _muKinetic = val))])),
        ]),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly, 
          children: [
            ElevatedButton(
              onPressed: _isMoving || (_appliedForce <= frictionForce) ? null : _startSimulation, 
              style: ElevatedButton.styleFrom(
                backgroundColor: Palette.primary,
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12)
              ), 
              child: Text(
                _appliedForce <= frictionForce ? 'Force <= Friction' : 'Exert Force Push', 
                style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)
              )
            ), 
            IconButton(
              onPressed: _resetSimulation, 
              icon: Icon(Icons.refresh),
              color: Palette.primary,
            )
          ]
        ),
      ]),
    );
  }
}

class WorkEnergyPainter extends CustomPainter {
  final double displacement, appliedForce, frictionForce, scaleRatio;
  WorkEnergyPainter({required this.displacement, required this.appliedForce, required this.frictionForce, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double floorY = canvasHeight - 30.0;
    double startX = 50.0;

    // 1. Draw Linear Surface Floor
    Paint linePaint = Paint()..color = Colors.black87..strokeWidth = 2.5;
    canvas.drawLine(Offset(0, floorY), Offset(canvasWidth, floorY), linePaint);

    // Draw reference dashed track markers
    Paint dashPaint = Paint()..color = Palette.primary.withValues(alpha: 0.2)..strokeWidth = 1.0;
    for (double i = startX; i < canvasWidth - 30; i += 30) {
      canvas.drawLine(Offset(i, floorY), Offset(i, floorY - 6), dashPaint);
    }

    // 2. Compute dynamic sliding position
    double currentBlockX = startX + displacement;
    double bW = 44.0;
    double bH = 26.0;

    // 3. Draw Sliding Block Node
    Rect blockRect = Rect.fromLTWH(currentBlockX - bW / 2, floorY - bH, bW, bH);
    canvas.drawRect(blockRect, Paint()..color = Colors.indigo[400]!);
    canvas.drawRect(blockRect, Paint()..color = Palette.primaryDeep..style = PaintingStyle.stroke..strokeWidth = 1.5);

    // 4. Render Active Work/Force Arrows (FIXED MATH HERE)
    // Applied Force Vector Arrow (Pulling cleanly from the RIGHT face of the block)
    double forceScale = appliedForce * 1.2;
    _drawComponentArrow(
      canvas, 
      Offset(currentBlockX + bW / 2, floorY - bH / 2), 
      Offset(currentBlockX + bW / 2 + forceScale, floorY - bH / 2), 
      Colors.green[700]!, 
      2.5
    );

    // Friction Vector Arrow (Directly opposing motion at the BOTTOM contact surface of the block)
    double frictionScale = frictionForce * 1.2;
    _drawComponentArrow(
      canvas, 
      Offset(currentBlockX, floorY), 
      Offset(currentBlockX - frictionScale, floorY), 
      Colors.red[700]!, 
      2.0
    );

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
  bool shouldRepaint(covariant WorkEnergyPainter oldDelegate) => true;
}