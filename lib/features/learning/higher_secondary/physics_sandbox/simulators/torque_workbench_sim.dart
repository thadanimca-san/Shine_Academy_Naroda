import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class TorqueWorkbenchSimulator extends StatefulWidget {
  const TorqueWorkbenchSimulator({Key? key}) : super(key: key);

  @override
  _TorqueWorkbenchSimulatorState createState() => _TorqueWorkbenchSimulatorState();
}

class _TorqueWorkbenchSimulatorState extends State<TorqueWorkbenchSimulator> with TickerProviderStateMixin {
  // Configurable Parameters
  double _radius = 2.5;         // Distance from pivot (meters)
  double _appliedForce = 20.0;   // Magnitude of force vector (Newtons)
  double _angleDeg = 90.0;       // Angle of application (degrees)
  
  // Selection States
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Auto-defaults to Sandbox (Tab 3)
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Exact Physics Calculations
    double angleRad = _angleDeg * math.pi / 180.0;
    double torqueValue = _radius * _appliedForce * math.sin(angleRad);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Torque Vector Workbench"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.build), text: "3. Sandbox"),
            Tab(icon: Icon(Icons.assignment), text: "4. Test Prep"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroTab(),
            _buildFormulaTab(torqueValue),
            _buildSandboxTab(torqueValue),
            _buildTestPrepTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRO (THEORETICAL OVERVIEW) ---
  Widget _buildIntroTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("ROTATIONAL STATICS & DYNAMICS", "NCERT Class 11 Physics | System of Particles & Rotational Motion"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Torque?",
            "Torque (\$\\tau\$), often referred to as the moment of force, is the rotational equivalent of linear force. Just as a force causes an object to accelerate linearly, a torque causes an object to undergo angular acceleration about an axis of rotation.",
            Colors.amber[900]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Essential Characteristics of Torque:"), style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Vector Nature:", "Torque is a cross-product relationship: \$\\vec{\\tau} = \\vec{r} \\times \\vec{F}\$. The direction of torque is perpendicular to both the position vector and the force vector, determined by the Right-Hand Rule."),
          _buildBulletPoint("The Lever Arm Factor:", "Only the component of force acting perpendicular to the position vector contributes to rotation. Any parallel force component acts purely linearly along the pivot structure, creating zero rotational action."),
          _buildBulletPoint("Cross Product Boundary Conditions:", "Torque is maximized when the vector angle is exactly \$90^\\circ\$ (\$\\sin(90^\\circ) = 1.0\$) and vanishes entirely when the vector angle is parallel at \$0^\\circ\$ or \$180^\\circ\$ (\$\\sin\\theta = 0\$)."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "View Equations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULAS & VECTORS ---
  Widget _buildFormulaTab(double calculatedTorque) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL FORMULATIONS", "Rigid Body Rotational Equations"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Cross-Product Definition (Vector Form):\n""   τ = r × F\n\n" 
              "2. Trigonometric Equivalent (Scalar Form):\n" 
              "   τ = r · F · sin(θ)\n" 
              "   Where:\n" 
              "   • r = distance vector magnitude (lever arm)\n" 
              "   • F = applied force magnitude\n" 
              "   • θ = angle between vectors r and F\n\n" 
              "3. Rotational Analogy to Newton's 2nd Law:\n" 
              "   τ_net = I · α\n" 
              "   Where:\n" 
              "   • I = Moment of Inertia of the rigid body\n" 
              "   • α = Angular Acceleration (rad/s²)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.amberAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Lever Arm Distance Concept:",
            "Alternatively, torque can be expressed as: \$\\tau = d \\cdot F\$, where \$d = r \\sin\\theta\$ is the 'perpendicular distance' from the pivot point axis to the line of action of the applied force.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Open Sandbox Workstation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SANDBOX WORKSPACE ---
  Widget _buildSandboxTab(double torqueValue) {
    return Column(
      children: [
        // Responsive Visual Canvas
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: Colors.amber[50],
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.amber[200]!),
            ),
            child: LayoutBuilder(builder: (context, constraints) {
              return ClipRect(
                child: CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: TorqueVectorPainter(
                    radius: _radius,
                    force: _appliedForce,
                    angleDeg: _angleDeg,
                    scaleRatio: constraints.maxWidth / 400.0,
                  ),
                ),
              );
            }),
          ),
        ),

        // Live Telemetry Readout Panel
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.amber[900],
            borderRadius: BorderRadius.circular(10),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Lever Arm (r)", "${_radius.toStringAsFixed(1)} m", Colors.white),
              _buildTelemetry("Force (F)", "${_appliedForce.toStringAsFixed(0)} N", Colors.limeAccent),
              _buildTelemetry("Angle (θ)", "${_angleDeg.toStringAsFixed(0)}°", Colors.cyanAccent),
              _buildTelemetry("Net Torque (τ)", "${torqueValue.toStringAsFixed(1)} N·m", Colors.orangeAccent),
            ],
          ),
        ),

        // Parameter Adjustment Drawer
        _buildControlsTray(),
        const SizedBox(height: 8),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12),
          child: _buildSkipButton(3, "Practice Exam Questions ➡️"),
        ),
        const SizedBox(height: 8),
      ],
    );
  }

  // --- TAB 4: TEST PREP (EXAM PREPARATION) ---
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Challenge'), style: TextStyle(fontWeight: FontWeight.bold))),
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildTorqueQuiz(),
        ],
      ),
    );
  }

  // --- UI CONSTRUCTION BLOCKS ---
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.amber[900])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.amber[900], fontSize: 16)),
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
          backgroundColor: Colors.amber[900], 
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
        Text(label.toUpperCase(), style: TextStyle(color: Colors.white70, fontSize: 8, fontWeight: FontWeight.bold)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: valColor, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildTorqueQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "A mechanic wants to produce maximum possible torque to loosen a stubborn lug nut. At what angle relative to the wrench handle should the force be directed?"
        : "A uniform heavy horizontal door of mass 'M' and width 'W' is pivoted on hinges. If a constant force 'F' is pushed perpendicularly right at the midpoint of the door (W/2), what is the resulting torque magnitude around the hinges?";

    List<String> options = isNeet
        ? ["Parallel to the handle (0°)", "At an oblique slant (45°)", "Exactly perpendicular (90°)", "Directly into the nut (180°)"]
        : ["F * W", "(F * W) / 2", "(F * W) / 4", "M * g * W"];

    int correctIndex = isNeet ? 2 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Angular Efficiency:" : "JEE Rigid Body Axis Distribution:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
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
            child: RadioListTile<int>(
              dense: true, 
              contentPadding: const EdgeInsets.symmetric(horizontal: 8),
              tileColor: tileColor ?? Colors.grey[50],
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6), side: BorderSide(color: Colors.grey[200]!)),
              value: index, 
              groupValue: _selectedAnswerIndex, 
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)), 
              activeColor: Colors.amber[900], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.amber[900], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Check Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red, width: 1),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(_selectedAnswerIndex == correctIndex ? Icons.check_circle : Icons.cancel, color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red, size: 16),
                    const SizedBox(width: 6),
                    Text(_selectedAnswerIndex == correctIndex ? "CORRECT BREAKDOWN" : "INCORRECT BREAKDOWN", style: TextStyle(fontWeight: FontWeight.bold, color: _selectedAnswerIndex == correctIndex ? Colors.green[800] : Colors.red[800], fontSize: 12)),
                  ],
                ),
                const Divider(height: 12),
                Text(
                  isNeet 
                      ? "✨ ANGULAR MOMENT OF FORCE DERIVATION:\n\n"
                        "1. Governing Law:\n"
                        "   The scalar magnitude of torque is modeled as: τ = r · F · sin(θ)\n\n"
                        "2. Analyzing Trigonometric Extremes:\n"
                        "   • For θ = 0° or 180°: sin(θ) = 0 ⟶ τ = 0 (No turning impact)\n"
                        "   • For θ = 90°: sin(θ) = 1.0 (Absolute maximum boundary parameter)\n\n"
                        "Therefore, pushing perfectly perpendicular (90°) yields the highest possible mechanical yield."
                      : "✨ PIVOTED DOOR RIGID BODY MECHANICS:\n\n"
                        "1. Torque Equation:\n"
                        "   τ = r · F_perpendicular\n\n"
                        "2. Isolate Spatial Parameters:\n"
                        "   • Applied Force is perpendicular to the radial coordinate vector, so sin(θ) = sin(90°) = 1.0.\n"
                        "   • The force is pressed at the geometric midpoint: r = W / 2.\n\n"
                        "3. Evaluation:\n"
                        "   τ = (W / 2) · F = (F · W) / 2.\n\n"
                        "Note: The structural mass 'M' of the door determines the rotational inertia (I), affecting the resulting angular acceleration (α), but it does not affect the applied torque parameter itself.",
                  style: TextStyle(fontSize: 12, height: 1.4, color: Theme.of(context).colorScheme.onSurface, fontFamily: 'monospace'),
                ),
              ],
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6), 
      color: Colors.white,
      child: Row(
        children: [
          Expanded(
            child: Column(
              children: [
                Text('Position (r): ${_radius.toStringAsFixed(1)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                Slider(
                  value: _radius, 
                  min: 1.0, 
                  max: 3.5, 
                  divisions: 5, 
                  activeColor: Colors.amber[800], 
                  onChanged: (val) => setState(() => _radius = val)
                )
              ],
            ),
          ),
          Expanded(
            child: Column(
              children: [
                Text('Force (F): ${_appliedForce.toStringAsFixed(0)} N', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                Slider(
                  value: _appliedForce, 
                  min: 10, 
                  max: 40, 
                  divisions: 6, 
                  activeColor: Colors.lime[800], 
                  onChanged: (val) => setState(() => _appliedForce = val)
                )
              ],
            ),
          ),
          Expanded(
            child: Column(
              children: [
                Text('Angle (θ): ${_angleDeg.toStringAsFixed(0)}°', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                Slider(
                  value: _angleDeg, 
                  min: 0, 
                  max: 180, 
                  divisions: 12, 
                  activeColor: Colors.cyan[800], 
                  onChanged: (val) => setState(() => _angleDeg = val)
                )
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class TorqueVectorPainter extends CustomPainter {
  final double radius, force, angleDeg, scaleRatio;
  TorqueVectorPainter({required this.radius, required this.force, required this.angleDeg, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    // Use responsive centering base coordinates
    Offset pivotPoint = Offset(canvasWidth * 0.25, canvasHeight / 2.0);
    double visualLength = radius * 55.0; // Dynamic pixel scaling ratio
    Offset forceApplyPoint = Offset(pivotPoint.dx + visualLength, pivotPoint.dy);

    // 1. Draw Stationary Fulcrum Pivot Bolt
    Paint boltPaint = Paint()..color = Colors.grey[700]!..style = PaintingStyle.fill;
    canvas.drawCircle(pivotPoint, 12.0, boltPaint);
    canvas.drawCircle(pivotPoint, 12.0, Paint()..color = Colors.black87..style = PaintingStyle.stroke..strokeWidth = 2.0);
    canvas.drawCircle(pivotPoint, 4.0, Paint()..color = Colors.white);

    // 2. Draw Lever Structural Arm Handle
    Paint armPaint = Paint()..color = Colors.amber[600]!..strokeWidth = 12.0..strokeCap = StrokeCap.round;
    canvas.drawLine(Offset(pivotPoint.dx + 8, pivotPoint.dy), forceApplyPoint, armPaint);

    // 3. Draw Dynamic Applied Force Vector Arrow
    double angleRad = angleDeg * math.pi / 180.0;
    double vectorLength = force * 1.6; // Visual scaling length multiplier
    
    // Calculate the end coordinate of the force vector pointing outward
    Offset forceEnd = Offset(
      forceApplyPoint.dx + vectorLength * math.cos(angleRad),
      forceApplyPoint.dy - vectorLength * math.sin(angleRad), // Inverted Y-axis to match coordinate system rotation
    );

    // Paint the vector body
    Paint forceVectorPaint = Paint()..color = Colors.teal[800]!..strokeWidth = 3.0..style = PaintingStyle.stroke;
    canvas.drawLine(forceApplyPoint, forceEnd, forceVectorPaint);
    
    // Draw vector arrowhead pointing outwards from the application node
    double arrowheadAngle = math.atan2(forceEnd.dy - forceApplyPoint.dy, forceEnd.dx - forceApplyPoint.dx);
    canvas.drawLine(forceEnd, Offset(forceEnd.dx - 10 * math.cos(arrowheadAngle - math.pi / 6), forceEnd.dy - 10 * math.sin(arrowheadAngle - math.pi / 6)), forceVectorPaint);
    canvas.drawLine(forceEnd, Offset(forceEnd.dx - 10 * math.cos(arrowheadAngle + math.pi / 6), forceEnd.dy - 10 * math.sin(arrowheadAngle + math.pi / 6)), forceVectorPaint);

    // 4. Mark Contact Point Node Indicator
    canvas.drawCircle(forceApplyPoint, 6.0, Paint()..color = Colors.pink[700]!);

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant TorqueVectorPainter oldDelegate) => true;
}