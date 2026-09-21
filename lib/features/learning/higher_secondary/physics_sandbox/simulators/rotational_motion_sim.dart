import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class RotationalMotionSimulator extends StatefulWidget {
  const RotationalMotionSimulator({Key? key}) : super(key: key);

  @override
  _RotationalMotionSimulatorState createState() => _RotationalMotionSimulatorState();
}

class _RotationalMotionSimulatorState extends State<RotationalMotionSimulator> with TickerProviderStateMixin {
  double _mass = 3.0;            // Mass of flywheel (kg)
  double _radius = 2.0;          // Radius of flywheel (meters)
  double _appliedForce = 15.0;   // Tangential push force (N)
  String _flywheelShape = 'Disk'; // 'Disk' (1/2 MR^2) or 'Hoop' (MR^2)
  
  double _angleRad = 0.0;
  double _angularVelocity = 0.0;
  double _time = 0.0;
  bool _isSpinning = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Set to Sandbox (Tab 3) initially
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      if (_isSpinning) {
        setState(() {
          _time = _controller.value * 10.0;
          _calculatePhysics();
        });
      }
    });
  }

  void _calculatePhysics() {
    double momentOfInertia = _flywheelShape == 'Disk' 
        ? 0.5 * _mass * _radius * _radius 
        : _mass * _radius * _radius;

    double torque = _appliedForce * _radius;
    double angularAcceleration = torque / momentOfInertia;

    _angularVelocity = angularAcceleration * _time;
    _angleRad = 0.5 * angularAcceleration * _time * _time;
  }

  void _startSimulation() {
    setState(() { _isSpinning = true; _selectedAnswerIndex = null; _quizEvaluated = false; });
    _controller.reset();
    _controller.forward();
  }

  void _resetSimulation() {
    setState(() { _isSpinning = false; _time = 0.0; _angleRad = 0.0; _angularVelocity = 0.0; _selectedAnswerIndex = null; _quizEvaluated = false; });
    _controller.reset();
  }

  @override
  void dispose() { 
    _controller.dispose(); 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    double momentOfInertia = _flywheelShape == 'Disk' ? 0.5 * _mass * _radius * _radius : _mass * _radius * _radius;
    double torque = _appliedForce * _radius;
    double angularAcceleration = torque / momentOfInertia;
    double rotationalKE = 0.5 * momentOfInertia * _angularVelocity * _angularVelocity;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Rotational Motion Sandbox"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.refresh), text: "3. Sandbox"),
            Tab(icon: Icon(Icons.assignment), text: "4. Test Prep"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroductionTab(),
            _buildFormulaTab(),
            _buildSimulationTab(momentOfInertia, torque, angularAcceleration, rotationalKE),
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRODUCTION ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("ROTATIONAL DYNAMICS & MOMENT OF INERTIA", "NCERT Class 11 Physics | Systems of Particles & Rotational Motion"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Rotational Inertia?",
            "Just as mass resists linear change in motion, Moment of Inertia (I) resists changes in rotational velocity. It depends not only on the amount of mass, but how far that mass is distributed from the axis of rotation.",
            Colors.teal[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Core Pillars of Rotation:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Torque (τ):", "The rotational analog of force. It is the action that causes or changes angular acceleration. Calculated as τ = r × F."),
          _buildBulletPoint("Moment of Inertia (I):", "Calculated as I = Σ m_i r_i². A hoop (I = MR²) has all mass far away, giving it twice the rotational resistance of a solid disk (I = ½MR²) of equal mass."),
          _buildBulletPoint("Angular Acceleration (α):", "The rate of change of angular velocity. Derived from Newton's Second Law for rotation: τ = Iα."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip directly to Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: MATHEMATICAL DERIVATIONS ---
  Widget _buildFormulaTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL RIGOR IN ROTATIONAL MECHANICS", "High-Yield Entrance Formulas"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Rotational Analogy Table:\n""   • Linear Mass (M) ───► Inertia (I)\n" 
              "   • Linear Force (F) ───► Torque (τ = r × F)\n" 
              "   • Accel (a) ────────► Angular Accel (α = τ / I)\n" 
              "   • Velocity (v) ─────► Angular Velocity (ω = v / r)\n\n" 
              "2. Moments of Inertia (Standard Shapes):\n" 
              "   • Thin Circular Ring / Hoop: I = MR²\n" 
              "   • Solid Circular Disc / Cylinder: I = ½ MR²\n" 
              "   • Thin Rod (Pivoted at Center): I = (1/12) ML²\n" 
              "   • Thin Rod (Pivoted at Edge): I = ⅓ ML²\n" 
              "   • Solid Sphere: I = (2/5) MR²\n" 
              "   • Hollow Sphere: I = (2/3) MR²\n\n" 
              "3. Rotational Kinetic Energy:\n" 
              "   • K_rot = ½ I ω²"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "The Parallel Axis Theorem:",
            "Useful for shifting the reference axis of calculation: I_new = I_cm + Md², where d is the distance shifted from the center of mass.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Test in Sandbox Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION ---
  Widget _buildSimulationTab(double momentOfInertia, double torque, double angularAcceleration, double rotationalKE) {
    return Column(
      children: [
        // Responsive Interactive Canvas Frame
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(color: Colors.teal[50], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return ClipRect(
                child: CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: FlywheelPainter(
                    angleRad: _angleRad,
                    radius: _radius,
                    shapeType: _flywheelShape,
                  ),
                ),
              );
            }),
          ),
        ),

        // Real-Time Scoreboard / Dashboard Panel (Corrected units here!)
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(color: Colors.teal[900], borderRadius: BorderRadius.circular(10)),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildTelemetry("Inertia (I)", "${momentOfInertia.toStringAsFixed(2)} kg·m²", Colors.orangeAccent),
                  _buildTelemetry("Torque (τ)", "${torque.toStringAsFixed(1)} N·m", Colors.cyanAccent),
                  _buildTelemetry("Alpha (α)", "${angularAcceleration.toStringAsFixed(2)} rad/s²", Colors.pinkAccent),
                  _buildTelemetry("Rotational KE", "${rotationalKE.toStringAsFixed(1)} J", Colors.greenAccent),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                "Angular Velocity (ω): ${_angularVelocity.toStringAsFixed(2)} rad/s  |  Time Elapsed: ${_time.toStringAsFixed(1)}s",
                style: TextStyle(color: Colors.white70, fontSize: 11, fontFamily: 'monospace', fontWeight: FontWeight.bold),
              )
            ],
          ),
        ),

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

  // --- TAB 4: QUIZ / DRILLS ---
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Focus'), style: TextStyle(fontWeight: FontWeight.bold))), 
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildRotationalQuiz(),
        ],
      ),
    );
  }

  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.teal[900])),
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
        color: accentColor.withValues(alpha: 0.08), 
        borderRadius: BorderRadius.circular(8), 
        border: Border.all(color: accentColor.withValues(alpha: 0.3))
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.bold, color: accentColor, fontSize: 14)),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.teal[900], fontSize: 16)),
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
          backgroundColor: Colors.teal[800], 
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
        Text(value, style: TextStyle(color: valColor, fontSize: 12, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildRotationalQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "A solid disk and a thin hoop have identical masses and radii. If you apply the exact same tangential torque to both, which one accelerates faster angularly?"
        : "A thin uniform rod of mass 'M' and length 'L' is pivoted smoothly at one structural endpoint. If it is released from a horizontal rest position, what is its initial angular acceleration (α) under gravity?";

    List<String> options = isNeet
        ? ["The thin hoop accelerates faster", "The solid disk accelerates faster", "They accelerate at identical rates", "Neither rotates because torque cancels"]
        : ["g / L", "3g / 2L", "2g / 3L", "3g / L"];

    int correctIndex = isNeet ? 1 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Mass Distribution:" : "JEE Rigid Body Torque Mechanics:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
        const SizedBox(height: 6),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: Theme.of(context).colorScheme.onSurface)),
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
              activeColor: Colors.teal, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Torque Acceleration Dynamics'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50], 
              borderRadius: BorderRadius.circular(8), 
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red)
            ),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "✅ CORRECT MASS SELECTION:\n\nThe solid disk has a lower moment of inertia (I = ½MR²) than the hoop (I = MR²). Since inertia resists rotational acceleration (α = τ / I), the disk requires less torque to accelerate at the same rate, spinning up much faster!"
                    : "✅ CORRECT TORQUE EVALUATION:\n\n1. Gravitational torque acts right at the Center of Mass: τ = Mg × (L/2).\n2. Moment of inertia of a rod pivoted at its terminal end is I = ⅓ML².\n3. Setting τ = Iα leads directly to:\n   MgL/2 = (ML²/3)α  ==►  α = 3g / 2L.")
                : (isNeet 
                    ? "❌ DISTRIBUTION ERROR:\n\nThink about mass distance! In a hoop, all mass is pulled far away to the boundary rim, maximizing inertia. A solid disk has its mass packed closer to the rotation center, minimizing spin resistance."
                    : "❌ MOMENT OF INERTIA OR PIVOT ERROR:\n\nBe careful! Torque about the pivot is Mg × (L/2). The moment of inertia of a terminal end pivot is ⅓ML² (not 1/12 ML² which is only about its center). Set τ = Iα to solve."),
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(10), 
      color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Mass: ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 1.0, max: 5.0, divisions: 4, activeColor: Colors.teal, onChanged: _isSpinning ? null : (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Radius: ${_radius.toStringAsFixed(1)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _radius, min: 1.0, max: 2.5, divisions: 3, activeColor: Colors.cyan[700], onChanged: _isSpinning ? null : (val) => setState(() => _radius = val))])),
          Expanded(child: Column(children: [Text('Force: ${_appliedForce.toStringAsFixed(0)} N', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _appliedForce, min: 5, max: 25, divisions: 4, activeColor: Colors.pink[600], onChanged: _isSpinning ? null : (val) => setState(() => _appliedForce = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          DropdownButton<String>(
            value: _flywheelShape,
            disabledHint: Text(_flywheelShape),
            items: [
              DropdownMenuItem(value: 'Disk', child: Text(TrilingualService.instance.getUIText('Solid Disk (½MR²)'), style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold))),
              DropdownMenuItem(value: 'Hoop', child: Text(TrilingualService.instance.getUIText('Thin Hoop (MR²)'), style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold))),
            ],
            onChanged: _isSpinning ? null : (val) => setState(() => _flywheelShape = val!),
          ),
          ElevatedButton(
            onPressed: _isSpinning ? null : _startSimulation, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[700]), 
            child: Text(TrilingualService.instance.getUIText('Exert Tangential Force'), style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.teal)),
        ]),
      ]),
    );
  }
}

class FlywheelPainter extends CustomPainter {
  final double angleRad, radius;
  final String shapeType;
  FlywheelPainter({required this.angleRad, required this.radius, required this.shapeType});

  @override
  void paint(Canvas canvas, Size size) {
    // Determine the safe bounds of our painting viewport
    double centerX = size.width / 2.0;
    double centerY = size.height / 2.0;
    Offset centerPoint = Offset(centerX, centerY);

    // DYNAMIC FITTING CALCULATION:
    // This dynamically scales the flywheel so it never overflows, regardless of screen orientation.
    // We reserve room (with a multiplier of 0.70) for the outer tangential force arrow.
    double maxUsableDimension = math.min(size.width, size.height);
    double visualRadius = (maxUsableDimension / 2.0) * 0.70 * (radius / 2.5);

    // 1. Draw Geometric Flywheel
    if (shapeType == 'Disk') {
      canvas.drawCircle(centerPoint, visualRadius, Paint()..color = Colors.teal[200]!..style = PaintingStyle.fill);
    } else {
      canvas.drawCircle(centerPoint, visualRadius, Paint()..color = Colors.teal[50]!..style = PaintingStyle.fill);
    }
    
    // Perimeter Outline
    canvas.drawCircle(
      centerPoint, 
      visualRadius, 
      Paint()..color = Colors.teal[900]!..style = PaintingStyle.stroke..strokeWidth = shapeType == 'Hoop' ? 5.0 : 2.0
    );

    // 2. Reference Spokes
    Paint spokePaint = Paint()..color = Colors.teal[900]!..strokeWidth = 1.5;
    for (int i = 0; i < 4; i++) {
      double spokeAngle = angleRad + (i * math.pi / 2.0);
      Offset spikeEnd = Offset(centerPoint.dx + visualRadius * math.cos(spokeAngle), centerPoint.dy + visualRadius * math.sin(spokeAngle));
      canvas.drawLine(centerPoint, spikeEnd, spokePaint);
      canvas.drawCircle(spikeEnd, 4.0, Paint()..color = Colors.pink[600]!);
    }

    // 3. Center Hub Axis Node
    canvas.drawCircle(centerPoint, 6.0, Paint()..color = Colors.black87);
    canvas.drawCircle(centerPoint, 2.0, Paint()..color = Colors.white);

    // 4. Force Input Tangent Vector Arrow (Scales dynamically relative to the flywheel size)
    Offset tangentForceOrigin = Offset(centerPoint.dx, centerPoint.dy - visualRadius);
    double arrowLength = visualRadius * 0.5; // Scaled to look proportional
    Offset tangentForceEnd = Offset(tangentForceOrigin.dx + arrowLength, tangentForceOrigin.dy);
    
    Paint forceVectorPaint = Paint()..color = Colors.pink[700]!..strokeWidth = 3.0..style = PaintingStyle.stroke;
    canvas.drawLine(tangentForceOrigin, tangentForceEnd, forceVectorPaint);
    canvas.drawLine(tangentForceEnd, Offset(tangentForceEnd.dx - 8, tangentForceEnd.dy - 5), forceVectorPaint);
    canvas.drawLine(tangentForceEnd, Offset(tangentForceEnd.dx - 8, tangentForceEnd.dy + 5), forceVectorPaint);
  }

  @override
  bool shouldRepaint(covariant FlywheelPainter oldDelegate) => true;
}