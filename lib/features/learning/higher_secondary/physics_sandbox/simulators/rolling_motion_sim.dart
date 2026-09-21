import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class RollingMotionSimulator extends StatefulWidget {
  const RollingMotionSimulator({Key? key}) : super(key: key);

  @override
  _RollingMotionSimulatorState createState() => _RollingMotionSimulatorState();
}

class _RollingMotionSimulatorState extends State<RollingMotionSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _linearVelocity = 4.0;    // v (m/s)
  double _angularVelocity = 2.0;   // ω (rad/s)
  final double _radius = 2.0;      // R (meters) fixed for calculations

  double _positionX = 50.0;
  double _rotationAngle = 0.0;
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late AnimationController _controller;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      setState(() {
        // Integrate positions based on separate dynamic velocity vectors
        _positionX += _linearVelocity * 0.3;
        _rotationAngle += _angularVelocity * 0.04;

        // Wraparound boundary logic
        if (_positionX > 500.0) {
          _positionX = -50.0;
        }
      });
    });
    _controller.repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double productRomega = _radius * _angularVelocity;
    String rollingState;
    Color stateColor;

    if ((_linearVelocity - productRomega).abs() < 0.1) {
      rollingState = "Pure Rolling (v = Rω)";
      stateColor = Colors.green;
    } else if (_linearVelocity > productRomega) {
      rollingState = "Forward Slipping (v > Rω) - Skidding";
      stateColor = Colors.orange[800]!;
    } else {
      rollingState = "Backward Slipping (v < Rω) - Spinning";
      stateColor = Colors.pink[700]!;
    }

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Rolling Motion Sandbox"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            // TAB 1: INTRODUCTORY CONCEPTS
            _buildIntroductionTab(),

            // TAB 2: MATHEMATICAL FORMULAS & RIGOROUS DERIVATIONS
            _buildDerivationTab(),

            // TAB 3: VISUAL SANDBOX CANVAS & SLIDERS
            _buildSimulationTab(rollingState, stateColor, productRomega),

            // TAB 4: ASSESSMENT EXAM DRILL
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: CONCEPT INTRODUCTION ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("COMBINED TRANSLATIONAL & ROTATIONAL MOTION", "NCERT Class 11 / JEE-NEET Rigid Body Dynamics"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Rolling Motion?",
            "Rolling motion is a complex combination of translational (linear) motion of the center of mass and rotational (circular) motion of the body around its center of mass. Instead of sliding flatly, the wheel pivots continuously about its contact point with the surface.",
            Colors.purple[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Three Physical Regimes:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Pure Rolling:", "Occurs when the point of contact with the ground is instantaneously at rest. This requires \$v = R\\omega\$. No sliding friction exists, only rolling resistance."),
          _buildBulletPoint("Forward Slipping (Skidding):", "Happens when linear velocity exceeds rotational velocity (\$v > R\\omega\$). Typical during sudden high-speed braking where wheels lock but the car slides forward."),
          _buildBulletPoint("Backward Slipping (Spinning):", "Happens when rotation velocity exceeds linear velocity (\$v < R\\omega\$). Typical when a car is stuck in mud; wheels spin incredibly fast, but the vehicle doesn't advance forward."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip directly to Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: DERIVATION VIEW ---
  Widget _buildDerivationTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("THE MATHEMATICS OF SPHERICAL ROLLING", "Velocity Composition & Total Kinetic Energy"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Velocity Vector Addition at Points:\n""   The velocity of any point on a rolling body is the vector sum:\n" 
              "   v_point = v_cm + (ω × r)\n\n" 
              "2. Critical Boundary Points:\n" 
              "   • Topmost Point: Translates forward (+v) and spins forward (+Rω).\n" 
              "     v_top = v + Rω = 2v (during pure rolling)\n\n" 
              "   • Center Point: Translates forward with v_cm = v.\n" 
              "     v_center = v\n\n" 
              "   • Lowest Point (Contact Point): Translates forward (+v), spins backward (-Rω).\n" 
              "     v_bottom = v - Rω\n" 
              "     Under pure rolling, v_bottom = 0.\n\n" 
              "3. Kinetic Energy of a Rolling Body:\n" 
              "   K_total = K_translation + K_rotation\n" 
              "   K_total = ½ M(v_cm)² + ½ I(ω)²\n" 
              "   Using I = M(k)² (where k is the radius of gyration):\n" 
              "   K_total = ½ M(v_cm)² [1 + (k/R)¹]"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Energy Ratios (Extremely High Yield):",
            "The fraction of total kinetic energy that is rotational depends entirely on the body's mass distribution (k²/R²):\n"
            "• Ring / Thin Hollow Cylinder: 50% Translational / 50% Rotational\n"
            "• Solid Disc / Cylinder: 67% Translational / 33% Rotational\n"
            "• Solid Sphere: 71% Translational / 29% Rotational",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION VIEW ---
  Widget _buildSimulationTab(String rollingState, Color stateColor, double productRomega) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: stateColor.withValues(alpha: 0.1),
          child: Text(
            "Current State: $rollingState",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: stateColor),
          ),
        ),

        // 1. Interactive Rolling Wheel Canvas
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(color: Colors.purple[50], borderRadius: BorderRadius.circular(12)),
            child: ClipRect(
              child: CustomPaint(
                size: Size.infinite,
                painter: RollingWheelPainter(
                  posX: _positionX,
                  angleRad: _rotationAngle,
                  radius: _radius,
                  v: _linearVelocity,
                  omega: _angularVelocity,
                ),
              ),
            ),
          ),
        ),

        // 2. Real-Time Scalar Metrics Panel
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(color: Colors.purple[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Linear Vel (v)", "${_linearVelocity.toStringAsFixed(1)} m/s", Colors.white),
              _buildTelemetry("Radius (R)", "${_radius.toStringAsFixed(1)} m", Colors.cyanAccent),
              _buildTelemetry("Angular (ω)", "${_angularVelocity.toStringAsFixed(1)} rad/s", Colors.limeAccent),
              _buildTelemetry("R × ω Product", "${productRomega.toStringAsFixed(1)} m/s", stateColor),
            ],
          ),
        ),

        // 3. Sliders Tray
        _buildControlsTray(),
        
        const SizedBox(height: 8),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12),
          child: _buildSkipButton(3, "Move to Competitive Exam Drill ➡️"),
        ),
        const SizedBox(height: 8),
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Focus'), style: TextStyle(fontWeight: FontWeight.bold))), 
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildRollingQuiz(),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.purple[900])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.purple[900], fontSize: 16)),
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
        style: TextButton.styleFrom(backgroundColor: Colors.purple[800], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
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

  Widget _buildRollingQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "During perfect 'Pure Rolling' without slipping, what is the instantaneous velocity of the absolute lowest contact point of the wheel touching the ground?"
        : "A ring of mass 'M' and radius 'R' executes pure rolling with linear velocity 'v'. What is its total kinetic energy combined (translational + rotational)?";

    List<String> options = isNeet
        ? ["Equal to linear velocity (v)", "Twice the linear velocity (2v)", "Perfectly zero (0)", "Inversely proportional to radius"]
        : ["½ Mv²", "Mv²", "³/₂ Mv²", "2 Mv²"];

    int correctIndex = isNeet ? 2 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Contact Kinematics:" : "JEE Combined Kinetic Mechanics:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.purple[800], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.purple[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Kinematic Vector Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT CONTACT ANALYSIS:\n\nIn pure rolling, the lowermost contact point has zero instantaneous velocity (v = 0) because the forward linear translation vector (+v) and backward spin rotation vector (-Rω) cancel each other out perfectly (v - Rω = 0)."
                    : "✅ CORRECT ENERGY CONSERVATION:\n\nTotal Energy is Kinetic Translation + Kinetic Rotation:\nE = ½ Mv² + ½ Iω².\nFor a thin ring, I = MR². Substituting ω = v/R yields:\nE = ½ Mv² + ½(MR²)(v/R)² = Mv².")
                : (isNeet 
                    ? "❌ VECTOR CANCELLATION ERROR:\n\nLook closely at the wheel base vectors in simulation! The forward velocity pushing right matches the backward spin pushing left. They negate each other to 0 relative to the ground surface."
                    : "❌ INCOMPLETE MOMENT OF INERTIA:\n\nRecall that a thin ring splits its total energy exactly 50/50 between linear translational progression and circular angular spin. Re-sum both halves together."),
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(12), 
      color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Forward Vel (v): ${_linearVelocity.toStringAsFixed(1)} m/s', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _linearVelocity, min: 0.0, max: 8.0, divisions: 8, activeColor: Colors.purple, onChanged: (val) => setState(() => _linearVelocity = val))])),
          Expanded(child: Column(children: [Text('Spin Speed (ω): ${_angularVelocity.toStringAsFixed(1)} rad/s', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _angularVelocity, min: 0.0, max: 4.0, divisions: 8, activeColor: Colors.purple[400], onChanged: (val) => setState(() => _angularVelocity = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          ElevatedButton.icon(
            onPressed: () => setState(() {
              _angularVelocity = _linearVelocity / _radius;
            }), 
            icon: Icon(Icons.flash_on, size: 16, color: Colors.white),
            label: Text(TrilingualService.instance.getUIText("Snap to Pure Rolling (v = Rω)"), style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
            style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[700]),
          )
        ]),
      ]),
    );
  }
}

class RollingWheelPainter extends CustomPainter {
  final double posX, angleRad, radius, v, omega;
  RollingWheelPainter({required this.posX, required this.angleRad, required this.radius, required this.v, required this.omega});

  @override
  void paint(Canvas canvas, Size size) {
    double groundY = size.height - 40.0;
    double visualRadius = radius * 25.0; // Scaled for presentation display
    Offset wheelCenter = Offset(posX, groundY - visualRadius);

    // 1. Draw Ground Surface Line
    Paint groundPaint = Paint()..color = Colors.grey[800]!..strokeWidth = 3.0;
    canvas.drawLine(Offset(0, groundY), Offset(size.width, groundY), groundPaint);

    // 2. Draw Main Spinning Wheel Circular Structure
    Paint wheelPaint = Paint()..color = Colors.purple[100]!..style = PaintingStyle.fill;
    canvas.drawCircle(wheelCenter, visualRadius, wheelPaint);
    canvas.drawCircle(wheelCenter, visualRadius, Paint()..color = Colors.purple[900]!..style = PaintingStyle.stroke..strokeWidth = 3.0);

    // 3. Draw Rotational Reference Spokes
    Paint spokePaint = Paint()..color = Colors.purple[900]!..strokeWidth = 2.0;
    for (int i = 0; i < 6; i++) {
      double spokeAngle = angleRad + (i * math.pi / 3.0);
      Offset spokeEnd = Offset(
        wheelCenter.dx + visualRadius * math.cos(spokeAngle),
        wheelCenter.dy + visualRadius * math.sin(spokeAngle)
      );
      canvas.drawLine(wheelCenter, spokeEnd, spokePaint);
    }
    canvas.drawCircle(wheelCenter, 5.0, Paint()..color = Colors.black);

    // 4. Vector Indicators: Forward Translation Vector (Center)
    Paint vPaint = Paint()..color = Colors.blue[800]!..strokeWidth = 3.0;
    double vLength = v * 10.0;
    if (vLength > 0) {
      Offset vEnd = Offset(wheelCenter.dx + vLength, wheelCenter.dy);
      canvas.drawLine(wheelCenter, vEnd, vPaint);
      canvas.drawLine(vEnd, Offset(vEnd.dx - 6, vEnd.dy - 4), vPaint);
      canvas.drawLine(vEnd, Offset(vEnd.dx - 6, vEnd.dy + 4), vPaint);
    }

    // 5. Vector Indicators: Tangential Spin Vector at Bottom Contact Point
    Paint omegaPaint = Paint()..color = Colors.pink[700]!..strokeWidth = 3.0..style = PaintingStyle.stroke;
    double omegaLength = (omega * radius) * 10.0;
    Offset bottomPoint = Offset(wheelCenter.dx, groundY);
    if (omegaLength > 0) {
      Offset omegaEnd = Offset(bottomPoint.dx - omegaLength, bottomPoint.dy);
      canvas.drawLine(bottomPoint, omegaEnd, omegaPaint);
      canvas.drawLine(omegaEnd, Offset(omegaEnd.dx + 6, omegaEnd.dy - 4), omegaPaint);
      canvas.drawLine(omegaEnd, Offset(omegaEnd.dx + 6, omegaEnd.dy + 4), omegaPaint);
    }
  }

  @override
  bool shouldRepaint(covariant RollingWheelPainter oldDelegate) => true;
}