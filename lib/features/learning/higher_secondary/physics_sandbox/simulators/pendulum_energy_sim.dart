import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PendulumEnergySimulator extends StatefulWidget {
  const PendulumEnergySimulator({Key? key}) : super(key: key);

  @override
  _PendulumEnergySimulatorState createState() => _PendulumEnergySimulatorState();
}

class _PendulumEnergySimulatorState extends State<PendulumEnergySimulator> with TickerProviderStateMixin {
  // Physical Input Parameters
  double _length = 2.5;         // Length of pendulum string L (meters)
  double _mass = 2.0;           // Mass of the bob m (kg)
  double _maxAngleDeg = 45.0;   // Release angle amplitude theta_max (degrees)
  double _time = 0.0;
  bool _isSwinging = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;

  final double g = 9.8; // Acceleration due to gravity (m/s²)

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    
    // Safety Lifecycle Catch: Freeze animation threads when user leaves the simulator screen view
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging && _tabController.index != 2) {
        if (_isSwinging) {
          _controller.stop();
          setState(() {
            _isSwinging = false;
            _time = 0.0;
          });
        }
      }
    });

    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      setState(() {
        // Ticking engine mapping global animation loop time
        _time = _controller.value * 10.0 * 2.0; 
      });
    });
  }

  void _releasePendulum() {
    setState(() { 
      _isSwinging = true; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
    _controller.repeat();
  }

  void _stopPendulum() {
    setState(() { 
      _isSwinging = false; 
      _time = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
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
    // 1. Calculate Maximum Potential Energy at release height
    double maxAngleRad = _maxAngleDeg * math.pi / 180.0;
    double maxHeight = _length * (1.0 - math.cos(maxAngleRad));
    double totalEnergy = _mass * g * maxHeight;

    // 2. Compute Simple Harmonic / Circular Kinematics
    double omega = math.sqrt(g / _length);
    double tCurrent = _isSwinging ? _time : 0.0;
    
    // Angular dynamic tracking
    double currentAngleRad = maxAngleRad * math.cos(omega * tCurrent);
    
    // Angular velocity: d(theta)/dt = -theta_max * omega * sin(omega * t)
    double angularVelocity = -maxAngleRad * omega * math.sin(omega * tCurrent);
    // Linear velocity: v = omega * L
    double linearVelocity = angularVelocity * _length;

    // 3. Energy Component Isolation
    double currentHeight = _length * (1.0 - math.cos(currentAngleRad));
    double potentialEnergy = _mass * g * currentHeight;
    double kineticEnergy = 0.5 * _mass * math.pow(linearVelocity, 2);

    // Safeguard mathematical floating point errors at boundary limits
    if (potentialEnergy > totalEnergy) potentialEnergy = totalEnergy;
    if (kineticEnergy > totalEnergy) kineticEnergy = totalEnergy;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Mechanical Energy Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.hourglass_empty), text: "3. Simulation"),
            Tab(icon: Icon(Icons.assignment), text: "4. Exam Drill"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroductionTab(),
            _buildDerivationTab(),
            _buildSimulationTab(totalEnergy, potentialEnergy, kineticEnergy, currentHeight, linearVelocity, currentAngleRad),
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
          _buildChapterHeader("CONSERVATION OF MECHANICAL ENERGY", "NCERT Class 11 / JEE-NEET Main Focus Area"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "The Law of Energy Conservation",
            "In an isolated system experiencing only conservative forces (such as gravity), the total mechanical energy remains constant over time. Energy cannot be created or destroyed; it transforms continuously back and forth between potential and kinetic states.",
            Colors.purple[700]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Key Lab Principles:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Extreme Boundaries:", "At maximum displacement points, velocity drops to zero. Total energy resides purely as Potential Energy (mgh)."),
          _buildBulletPoint("Equilibrium Center Passing:", "At the absolute lowest point (height h = 0), potential energy reaches its minimum, converting entirely to Kinetic Energy (½mv²)."),
          _buildBulletPoint("Conservative Fields:", "Neglecting resistive air drag implies that the total mathematical sum of E_k + E_p remains constant at every point along the circular arc."),
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
          _buildChapterHeader("THE MECHANICAL ENERGY DECONSTRUCTION", "Rigorous Work-Energy Equations"),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Instantaneous Displacement Height (h):\n""   Measured relative to lowest datum level:\n" 
              "   h = L - L·cosθ = L · (1 - cosθ)\n\n" 
              "2. Total Energy at Release Boundary State:\n" 
              "   v = 0 at θ = θ_max\n" 
              "   E_total = E_p = m · g · L · (1 - cosθ_max)\n\n" 
              "3. Velocity at Velocity Apex Center:\n" 
              "   Apply Conservation Law: E_p(max) = E_k(max)\n" 
              "   m·g·h_max = ½·m·v_max²\n" 
              "   v_max = √(2 · g · L · (1 - cosθ_max))\n\n" 
              "4. Intermediate Mechanics Equation:\n" 
              "   At any arbitrary vector position state angle:\n" 
              "   E_total = m·g·h(θ) + ½·m·v(θ)² = Constant"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE-NEET Problem Solving Shortcut:",
            "Kinetic energy relates directly to linear momentum through the following mathematical expression:\n"
            "KE = p² / (2m)\n"
            "Therefore, if momentum scales by factor x, Kinetic Energy scales by x squared!",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Visual Simulator ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double totalE, double potE, double kinE, double height, double velocity, double angleRad) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.purple[50],
          child: Text(
            _isSwinging ? "🟢 Conservative Field Active: Simulating Energy Transformation" : "🛑 System Stationary: Ready for Trajectory Release",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.purple[900]),
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.purple[50]!.withValues(alpha: 0.5), borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: PendulumEnergyPainter(
                  angleRad: angleRad,
                  pendulumLength: _length,
                  maxAngleDeg: _maxAngleDeg, // Dynamic scale metrics parameters linked
                ),
              );
            }),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.purple[900], borderRadius: BorderRadius.circular(10)),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildTelemetry("Total Mechanical", "${totalE.toStringAsFixed(1)} J", Colors.amberAccent),
                  _buildTelemetry("Potential (mgh)", "${potE.toStringAsFixed(1)} J", Colors.cyanAccent),
                  _buildTelemetry("Kinetic (½mv²)", "${kinE.toStringAsFixed(1)} J", Colors.greenAccent),
                ],
              ),
              const Divider(color: Colors.white24, height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text("Height: ${height.toStringAsFixed(2)} m", style: TextStyle(color: Colors.white70, fontSize: 11, fontFamily: 'monospace')),
                  const SizedBox(width: 24),
                  Text("Velocity: ${velocity.abs().toStringAsFixed(2)} m/s", style: TextStyle(color: Colors.white70, fontSize: 11, fontFamily: 'monospace')),
                ],
              )
            ],
          ),
        ),
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Move to Evaluation Drill ➡️"),
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
          _buildEnergyQuiz(),
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
        style: TextButton.styleFrom(backgroundColor: Colors.purple[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value, Color valColor) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label.toUpperCase(), style: TextStyle(color: Colors.white70, fontSize: 9, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: valColor, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildEnergyQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "At what structural position during its path does the swinging pendulum bob achieve its maximum absolute linear momentum?"
        : "If linear momentum of the pendulum bob at its lowest point is increased by exactly 50% via an external strike impulse, by what factor does its Kinetic Energy increase at that instant?";

    List<String> options = isNeet
        ? ["At the maximum left displacement peak", "At the maximum right displacement peak", "At the lowest equilibrium center point", "Momentum is constant throughout"]
        : ["1.50 times", "2.25 times", "1.25 times", "3.00 times"];

    int correctIndex = isNeet ? 2 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Energy Locations:" : "JEE Variable Proportions:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.purple, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.purple[700], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Conservation Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "Correct! 🎉 At the lowest point, Potential Energy drops to zero. By Conservation of Mechanical Energy, all energy converts to Kinetic Energy, maximizing velocity and thus linear momentum (p = mv)."
                    : "Correct! 🎉 Kinetic Energy relates to momentum via KE = p² / 2m. If momentum is increased to 1.5p (a 50% rise), the new KE scales by (1.5)² = 2.25 times.")
                : (isNeet 
                    ? "Incorrect ❌ Look closely at the telemetry! At the high endpoints, velocity is zero, so momentum is zero. Linear momentum peaks where kinetic energy peaks—at the lowest equilibrium center point."
                    : "Incorrect ❌ Keep the squared momentum shortcut in mind: KE = p² / 2m. Since momentum scales up by 1.5, squaring that fraction gives (1.5 * 1.5) = 2.25 times the initial energy value."),
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
          Expanded(child: Column(children: [Text('Length: ${_length.toStringAsFixed(1)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _length, min: 1.5, max: 3.5, divisions: 4, activeColor: Colors.deepPurple, onChanged: _isSwinging ? null : (val) => setState(() => _length = val))])),
          Expanded(child: Column(children: [Text('Mass: ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 1.0, max: 5.0, divisions: 4, activeColor: Colors.purple, onChanged: _isSwinging ? null : (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Angle: ${_maxAngleDeg.toStringAsFixed(0)}°', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _maxAngleDeg, min: 15, max: 60, divisions: 3, activeColor: Colors.purpleAccent, onChanged: _isSwinging ? null : (val) => setState(() => _maxAngleDeg = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isSwinging ? null : _releasePendulum, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.purple[700], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('Release Swing'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _stopPendulum, icon: Icon(Icons.refresh, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class PendulumEnergyPainter extends CustomPainter {
  final double angleRad;
  final double pendulumLength;
  final double maxAngleDeg;

  PendulumEnergyPainter({
    required this.angleRad, 
    required this.pendulumLength,
    required this.maxAngleDeg,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // 1. Establish anchor points relative to the true runtime canvas size
    final Offset topAnchor = Offset(size.width / 2.0, 25.0);
    final double availableHeight = size.height - topAnchor.dy - 30.0; // Leaves a 30px buffer zone at the bottom

    // 2. Compute the maximum theoretical drop height at the maximum slider configuration value
    // This guarantees the bob stays bounded even at its lowest point (θ = 0)
    final double maxAngleRad = maxAngleDeg * math.pi / 180.0;
    
    // 3. Dynamically compute pixel scaling ratio using real layout bounds
    // We base the scale on the maximum possible length the pendulum could reach vertically
    final double universalScale = availableHeight / pendulumLength;

    // Convert real physical metrics directly to bounded canvas coordinate dimensions
    final double visualLength = pendulumLength * universalScale;

    // 4. Draw Support Stand Mount Line
    final Paint mountPaint = Paint()
      ..color = Colors.black87
      ..strokeWidth = 4.0
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(
      Offset(topAnchor.dx - 40.0, topAnchor.dy), 
      Offset(topAnchor.dx + 40.0, topAnchor.dy), 
      mountPaint,
    );
    canvas.drawCircle(topAnchor, 4.0, Paint()..color = Colors.white);

    // 5. Compute the live trig positions of the Bob
    final double bobX = topAnchor.dx + visualLength * math.sin(angleRad);
    final double bobY = topAnchor.dy + visualLength * math.cos(angleRad);
    final Offset bobCenter = Offset(bobX, bobY);

    // 6. Draw Center Line Pathway Guide
    final Paint eqPathPaint = Paint()
      ..color = Colors.purple.withValues(alpha: 0.12)
      ..strokeWidth = 1.5
      ..style = PaintingStyle.stroke;
    canvas.drawLine(topAnchor, Offset(topAnchor.dx, topAnchor.dy + visualLength), eqPathPaint);

    // 7. Draw Suspended Cord
    final Paint stringPaint = Paint()
      ..color = Colors.black54
      ..strokeWidth = 2.0
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(topAnchor, bobCenter, stringPaint);

    // 8. Draw Bounded Spherical Bob Node (Will fit nicely above the telemetry panel now)
    final double bobRadius = 14.0;
    final Paint bobPaint = Paint()
      ..color = Colors.purple[600]!
      ..style = PaintingStyle.fill;
    
    canvas.drawCircle(bobCenter, bobRadius, bobPaint);
    canvas.drawCircle(
      bobCenter, 
      bobRadius, 
      Paint()
        ..color = Colors.purple[900]!
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );
    
    // Subtle central highlight bead for visual depth
    canvas.drawCircle(bobCenter.translate(-3, -3), 3.0, Paint()..color = Colors.white38);
  }

  @override
  bool shouldRepaint(covariant PendulumEnergyPainter oldDelegate) {
    return oldDelegate.angleRad != angleRad || 
           oldDelegate.pendulumLength != pendulumLength ||
           oldDelegate.maxAngleDeg != maxAngleDeg;
  }
}