import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class GravitationSimulator extends StatefulWidget {
  const GravitationSimulator({Key? key}) : super(key: key);

  @override
  _GravitationSimulatorState createState() => _GravitationSimulatorState();
}

class _GravitationSimulatorState extends State<GravitationSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _planetMass = 3.0;       // Mass factor M (arbitrary scaling units)
  double _launchVelocity = 5.0;   // Launch speed parameter v
  
  double _satelliteX = 0.0;
  double _satelliteY = -35.0;
  double _satelliteVx = 0.0;
  double _satelliteVy = 0.0;
  
  bool _isLaunched = false;
  List<Offset> _orbitTrajectoryPath = [];
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _physicsController;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _physicsController = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      if (_isLaunched) {
        _runOrbitalPhysicsStep();
      }
    });
  }

  void _runOrbitalPhysicsStep() {
    setState(() {
      // Coordinates relative to central planet center (0,0)
      double rSquare = (_satelliteX * _satelliteX) + (_satelliteY * _satelliteY);
      double distance = math.sqrt(rSquare);
      
      // Prevent division by zero or extreme singularities near core center
      if (distance < 25.0) {
        _isLaunched = false;
        _physicsController.stop();
        return;
      }

      // Acceleration = G * M / r² directed towards center
      double constantG = 400.0; // Scaled physics engine constant
      double accelerationMag = (constantG * _planetMass) / rSquare;
      
      double ax = -accelerationMag * (_satelliteX / distance);
      double ay = -accelerationMag * (_satelliteY / distance);

      // Standard Verlet/Euler integration steps
      double dt = 0.15;
      _satelliteVx += ax * dt;
      _satelliteVy += ay * dt;
      _satelliteX += _satelliteVx * dt;
      _satelliteY += _satelliteVy * dt;

      _orbitTrajectoryPath.add(Offset(_satelliteX, _satelliteY));
      
      // Drop trace points if length gets massive to preserve mobile rendering frame rates
      if (_orbitTrajectoryPath.length > 300) {
        _orbitTrajectoryPath.removeAt(0);
      }

      // Escape check: If distance becomes immense, safely pause loop
      if (distance > 600.0) {
        _isLaunched = false;
        _physicsController.stop();
      }
    });
  }

  void _fireProjectile() {
    setState(() {
      _orbitTrajectoryPath.clear();
      _satelliteX = 0.0;
      _satelliteY = -35.0; 
      
      // Horizontal launch projection vector initialization
      _satelliteVx = _launchVelocity;
      _satelliteVy = 0.0;
      
      _isLaunched = true;
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
    _physicsController.repeat();
  }

  void _resetCosmos() {
    setState(() {
      _isLaunched = false;
      _satelliteX = 0.0;
      _satelliteY = -35.0;
      _satelliteVx = 0.0;
      _satelliteVy = 0.0;
      _orbitTrajectoryPath.clear();
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
    _physicsController.stop();
  }

  @override
  void dispose() {
    _physicsController.dispose();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Standardized cosmic derivations for live display panel
    double constantG = 400.0;
    double launchRadius = 35.0;
    double calculatedVo = math.sqrt((constantG * _planetMass) / launchRadius);
    double calculatedVe = math.sqrt(2.0) * calculatedVo;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Gravitation & Orbit Sandbox"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
        backgroundColor: Palette.primaryDeep,
        elevation: 0,
        bottom: TabBar(
          controller: _tabController,
          labelColor: Colors.white,
          unselectedLabelColor: Colors.white60,
          indicatorColor: Palette.accent,
          indicatorWeight: 3,
          tabs: const [
            Tab(icon: Icon(Icons.public), text: "1. Intro"),
            Tab(icon: Icon(Icons.blur_on), text: "2. Dynamics"),
            Tab(icon: Icon(Icons.rocket_launch), text: "3. Simulation"),
            Tab(icon: Icon(Icons.psychology), text: "4. Exam Drill"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            // TAB 1: CORE COSMIC TEXTBOOK INTRODUCTION
            _buildIntroductionTab(),

            // TAB 2: MATHEMATICAL BOUNDARY DERIVATIONS
            _buildDerivationTab(),

            // TAB 3: LIVE ORBITAL GRAPHICS SIMULATOR
            _buildSimulationTab(calculatedVo, calculatedVe),

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
          _buildChapterHeader("NEWTON'S UNIVERSAL GRAVITATION", "NCERT Class 11 / JEE-NEET High-Yield Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Gravitational Binding Energy?",
            "Gravitational field physics deals with long-range conservative forces. The negative energy state of an orbiting body indicates it is bound securely within the central mass's potential well. To release a satellite permanently from this constraint into deep space, its total mechanical energy must be raised to greater than or equal to zero.",
            Palette.primaryDeep
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Critical Orbital Thresholds:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Orbital Velocity (v₀):", "The precise horizontal injection velocity required to establish a stable circular path around a central body: v₀ = √(GM/R)."),
          _buildBulletPoint("Escape Velocity (vₑ):", "The minimum velocity required for an unpowered projectile to escape structural gravitational pull: vₑ = √(2GM/R). Always matches √2 times orbital velocity."),
          _buildBulletPoint("Field Variations:", "Gravitational field intensity drops linearly below a planet's surface and drops quadratically according to an inverse-square law above it."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip to Mathematical Dynamics ➡️"),
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
          _buildChapterHeader("THE ORBITAL EQUATIONS", "Rigorous Field Balancing Equations"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[950], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Circular Motion Constraint:\n""   F_centripetal = F_gravitational\n" 
              "   m·v² / R = G·M·m / R²\n\n" 
              "2. Solving for Stable Orbital Velocity (v_o):\n" 
              "   v_o = √(G·M / R)\n\n" 
              "3. Total Energy Bound State Calculations:\n" 
              "   Total E = Kinetic Energy + Potential Energy\n" 
              "   Total E = ½·m·v_o² + (-G·M·m / R)\n" 
              "   Total E = ½·(G·M·m / R) - (G·M·m / R)\n" 
              "   Total E = - G·M·m / (2·R)  [Bound Condition]\n\n" 
              "4. Deriving Escape Velocity Bound (v_e):\n" 
              "   Set Total Mechanical Energy = 0\n" 
              "   ½·m·v_e² - G·M·m / R = 0\n" 
              "   v_e = √(2·G·M / R) = √2 · v_o"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.cyanAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE / NEET Exam Injection Alert:",
            "If launch vector velocity matches: \n"
            "• v < v_o: Crash path trajectory occurs (spirals down)\n"
            "• v = v_o: Establishes beautiful stable circular orbit\n"
            "• v_o < v < v_e: Shifts path map into closed elliptical tracking\n"
            "• v ≥ v_e: Unbinds completely into an open parabolic or hyperbolic escape line",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Space Sandbox ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double calculatedVo, double calculatedVe) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Palette.primarySoft,
          child: Text(
            _isLaunched ? "🟢 Projectile Fired: Computing Keplerian Trajectory" : "🛑 Launcher Primed: Adjust Mass/Speed & Deploy Vector",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Palette.primaryDeep),
          ),
        ),

        // Interactive Space Orbital Track Viewport
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey[950], borderRadius: BorderRadius.circular(12)),
            child: ClipRect(
              child: LayoutBuilder(builder: (context, constraints) {
                return CustomPaint(
                  size: Size.infinite,
                  painter: SpaceOrbitPainter(
                    satX: _satelliteX,
                    satY: _satelliteY,
                    trailPoints: _orbitTrajectoryPath,
                    scaleRatio: constraints.maxWidth / 400.0,
                  ),
                );
              }),
            ),
          ),
        ),

        // Real-Time Scalar Metrics Panel
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Palette.stage, borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Planet Mass", _planetMass.toStringAsFixed(1), Colors.white),
              _buildTelemetry("Launch Speed", _launchVelocity.toStringAsFixed(1), Colors.cyanAccent),
              _buildTelemetry("Req. Orbital v₀", calculatedVo.toStringAsFixed(1), Colors.greenAccent),
              _buildTelemetry("Req. Escape vₑ", calculatedVe.toStringAsFixed(1), Colors.orangeAccent),
            ],
          ),
        ),

        // Environmental Input Deck controls
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Proceed to Interactive Drill ➡️"),
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
          _buildGravitationQuiz(),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Palette.primaryDeep)),
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
        style: TextButton.styleFrom(backgroundColor: Palette.primaryDeep, foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
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

  Widget _buildGravitationQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "If you dig deep inside a uniform planetary body towards its core, how does the local acceleration due to gravity (g) scale with depth?"
        : "A satellite is coasting in a stable circular orbit around Earth. If its current kinetic energy is boosted instantly by 100% (doubled), what happens to its trajectory path?";

    List<String> options = isNeet
        ? ["Increases exponentially", "Decreases linearly to zero at center", "Stays completely constant", "Increases linearly to infinity"]
        : ["It shifts into a larger circular orbit", "It spirals directly down into the planet", "It breaks free into an escape parabolic/hyperbolic path", "It oscillates in a tight vertical axis line"];

    int correctIndex = isNeet ? 1 : 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Interior Planetary Fields:" : "JEE Cosmic Energy Bounds:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Palette.primaryDeep, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Palette.primaryDeep, padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Orbital Physics Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT CONCEPT DERIVATION:\n\nInside a planet, the field pulls linearly according to g_d = g(1 - d/R). At the absolute center, the surrounding mass balances symmetrically, forcing net gravity down to zero."
                    : "✅ CORRECT FIELD MATHEMATICS:\n\nIn a circular orbit, Potential Energy magnitude is double the Kinetic Energy (|PE| = 2KE, Total Energy = -KE). Doubling KE forces total mechanical energy to zero, instantly launching it onto an escape trajectory!")
                : (isNeet 
                    ? "❌ CONCEPT MISALIGNMENT:\n\nAs you dig deeper, less mass remains beneath you to exert downward pull. Gravity scales down linearly down to exactly 0 at the core center."
                    : "❌ CONCEPT MISALIGNMENT:\n\nDoubling the kinetic energy provides exactly enough energy to neutralize the negative binding energy, triggering an immediate escape trajectory to infinity."),
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(10), color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Planet Mass M: ${_planetMass.toStringAsFixed(1)}', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _planetMass, min: 1.0, max: 5.0, divisions: 4, activeColor: Palette.primary, onChanged: _isLaunched ? null : (val) => setState(() => _planetMass = val))])),
          Expanded(child: Column(children: [Text('Launch Vector speed (v): ${_launchVelocity.toStringAsFixed(1)}', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _launchVelocity, min: 2.0, max: 9.5, divisions: 15, activeColor: Colors.cyan[700], onChanged: _isLaunched ? null : (val) => setState(() => _launchVelocity = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isLaunched ? null : _fireProjectile, 
            style: ElevatedButton.styleFrom(backgroundColor: Palette.primaryDeep, padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.rocket_launch, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('Launch Projectile'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetCosmos, icon: Icon(Icons.refresh, color: Colors.blueGrey)),
        ]),
      ]),
    );
  }
}

class SpaceOrbitPainter extends CustomPainter {
  final double satX, satY, scaleRatio;
  final List<Offset> trailPoints;
  SpaceOrbitPainter({required this.satX, required this.satY, required this.trailPoints, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;
    
    Offset viewportCenter = Offset(canvasWidth / 2.0, canvasHeight / 2.0);

    // 1. Draw Background Stars for deep-space atmosphere immersion
    Paint starPaint = Paint()..color = Colors.white30;
    canvas.drawCircle(Offset(canvasWidth * 0.2, canvasHeight * 0.2), 1.0, starPaint);
    canvas.drawCircle(Offset(canvasWidth * 0.8, canvasHeight * 0.3), 1.5, starPaint);
    canvas.drawCircle(Offset(canvasWidth * 0.15, canvasHeight * 0.75), 1.2, starPaint);
    canvas.drawCircle(Offset(canvasWidth * 0.75, canvasHeight * 0.8), 1.0, starPaint);

    // 2. Draw Central Massive Planet Node
    Paint planetPaint = Paint()
      ..shader = RadialGradient(colors: [Colors.blue[400]!, Colors.blue[900]!]).createShader(Rect.fromCircle(center: viewportCenter, radius: 22.0));
    canvas.drawCircle(viewportCenter, 22.0, planetPaint);
    canvas.drawCircle(viewportCenter, 22.0, Paint()..color = Colors.cyan.withValues(alpha: 0.4)..style = PaintingStyle.stroke..strokeWidth = 1.5);

    // 3. Draw Past Continuous Orbital Trajectory Path Trails
    if (trailPoints.isNotEmpty) {
      Paint trailPaint = Paint()..color = Colors.cyanAccent.withValues(alpha: 0.5)..strokeWidth = 1.5..style = PaintingStyle.stroke;
      Path tracePath = Path();
      tracePath.moveTo(viewportCenter.dx + trailPoints.first.dx, viewportCenter.dy + trailPoints.first.dy);
      for (var point in trailPoints) {
        tracePath.lineTo(viewportCenter.dx + point.dx, viewportCenter.dy + point.dy);
      }
      canvas.drawPath(tracePath, trailPaint);
    }

    // 4. Draw Active Moving Satellite Object Node
    Offset localizedSatPos = Offset(viewportCenter.dx + satX, viewportCenter.dy + satY);
    canvas.drawCircle(localizedSatPos, 4.5, Paint()..color = Colors.orangeAccent);
    canvas.drawCircle(localizedSatPos, 7.0, Paint()..color = Colors.orange.withValues(alpha: 0.3)..style = PaintingStyle.stroke..strokeWidth = 1.0);

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant SpaceOrbitPainter oldDelegate) => true;
}