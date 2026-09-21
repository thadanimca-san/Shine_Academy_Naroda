import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class EscapeVelocitySimulator extends StatefulWidget {
  const EscapeVelocitySimulator({Key? key}) : super(key: key);

  @override
  _EscapeVelocitySimulatorState createState() => _EscapeVelocitySimulatorState();
}

class _EscapeVelocitySimulatorState extends State<EscapeVelocitySimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _planetMassFactor = 2.0;    // Affects gravity strength multiplier
  double _launchVelocity = 6.0;      // Initial upward mechanical boost
  
  double _rocketHeight = 0.0;        // Distance above surface
  double _rocketVelocity = 0.0;      // Current dynamic speed
  bool _isFlying = false;
  String _flightStatus = "Ready on Pad";
  
  final List<double> _heightHistory = [];
  late AnimationController _physicsController;
  late TabController _tabController;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    
    _physicsController = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      if (_isFlying) {
        _runVerticalPhysicsStep();
      }
    });
  }

  void _runVerticalPhysicsStep() {
    setState(() {
      double planetRadius = 40.0;
      double currentRadius = planetRadius + _rocketHeight;
      
      double constantG = 300.0;
      double deceleration = (constantG * _planetMassFactor) / (currentRadius * currentRadius);
      
      _rocketVelocity -= deceleration * 0.2;
      _rocketHeight += _rocketVelocity * 0.2;
      
      _heightHistory.add(_rocketHeight);
      if (_heightHistory.length > 200) _heightHistory.removeAt(0);

      if (_rocketHeight <= 0.0) {
        _rocketHeight = 0.0;
        _rocketVelocity = 0.0;
        _isFlying = false;
        _flightStatus = "Crashed Back to Earth 💥";
        _physicsController.stop();
      } else if (_rocketVelocity > 0 && _rocketHeight > 300.0) {
        double escapeSpeedLimit = math.sqrt((2.0 * constantG * _planetMassFactor) / currentRadius);
        if (_rocketVelocity >= escapeSpeedLimit) {
          _flightStatus = "Escaped Gravity Well! 🚀🌌";
          _isFlying = false; 
          _physicsController.stop();
        }
      } else if (_rocketVelocity <= 0 && _flightStatus == "Ascending...") {
        _flightStatus = "Falling back down... 📉";
      }
    });
  }

  void _launchRocket() {
    setState(() {
      _rocketHeight = 0.0;
      _rocketVelocity = _launchVelocity;
      _isFlying = true;
      _flightStatus = "Ascending...";
      _heightHistory.clear();
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
    _physicsController.repeat();
  }

  void _resetLaunchPad() {
    setState(() {
      _isFlying = false;
      _rocketHeight = 0.0;
      _rocketVelocity = 0.0;
      _flightStatus = "Ready on Pad";
      _heightHistory.clear();
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
    double baseG = 300.0;
    double surfaceRadius = 40.0;
    double realEscapeVelocity = math.sqrt((2.0 * baseG * _planetMassFactor) / surfaceRadius);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Escape Velocity Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)), 
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
            Tab(icon: Icon(Icons.rocket_launch), text: "3. Simulation"),
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
            _buildSimulationTab(realEscapeVelocity),
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
          _buildChapterHeader("PLANETARY GRAVITATION & ESCAPE VELOCITY", "NCERT Class 11 / JEE-NEET High-Yield Chapter"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Escape Velocity?",
            "Escape velocity is defined as the minimum initial speed required for a projectile to permanently break free from the gravitational pull of a celestial body without undergoing any further manual propulsion. The object escapes completely to infinity, where both its kinetic and gravitational potential energy reduce to zero.",
            Colors.teal[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Essential Core Principles:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Gravitational Potential Well:", "Every planet forms a conservative energy trap. The field potential on a planet's surface is strongly negative, written mathematically as U = -GMm/R."),
          _buildBulletPoint("Boundary Target Conditions:", "For successful escaping criteria, total mechanical energy at infinity must be at least equal to 0 Joules. Any velocity less than this threshold causes a closed orbital trajectory or subsequent crash."),
          _buildBulletPoint("Independence of Launch Angle:", "Because mechanical energy is a pure scalar framework, the absolute value of escape velocity is completely independent of the launch angle projection direction (provided it doesn't intersect the planet's terrain)."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip directly to Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULA DERIVATION VIEW ---
  Widget _buildDerivationTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("THE MATHEMATICAL MATRIX PROOF", "Rigorous Energy Conservation Integration"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Total Energy Configuration at Surface:\n""   E_surface = K.E. + P.E.\n" 
              "   E_surface = ½ · m · v_e² - (G · M · m) / R\n\n" 
              "2. Energy Targets at Infinite Boundary (r → ∞):\n" 
              "   P.E._infinity = 0  (Gravity fades entirely)\n" 
              "   K.E._infinity = 0  (Minimum required criteria)\n" 
              "   E_infinity = 0\n\n" 
              "3. Applying Conservation Laws:\n" 
              "   E_surface = E_infinity\n" 
              "   ½ · m · v_e² - (G · M · m) / R = 0\n" 
              "   ½ · m · v_e² = (G · M · m) / R\n\n" 
              "4. Primary Solution Matrix:\n" 
              "   v_e = √[ (2 · G · M) / R ]\n\n" 
              "5. Alternate Acceleration Form (g = GM/R²):\n" 
              "   v_e = √[ 2 · g · R ]"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE-NEET Absolute Key Rules:",
            "• Notice the projection mass 'm' completely cancels out. Escape speed is identical for an electron and a spacecraft.\n"
            "• Earth Parameter Baseline: v_e ≈ 11.2 km/s.\n"
            "• Moon Parameter Baseline: v_e ≈ 2.38 km/s (Explaining its lack of an atmospheric gas envelope).",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION VIEW ---
  Widget _buildSimulationTab(double realEscapeVelocity) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(vertical: 8),
          color: Colors.teal[50],
          child: Text(
            "Status: $_flightStatus",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Colors.teal[900]),
          ),
        ),
        Expanded(
          flex: 40,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[900], borderRadius: BorderRadius.circular(12)),
            child: ClipRect(
              child: CustomPaint(
                size: Size.infinite,
                painter: VerticalLaunchPainter(
                  height: _rocketHeight,
                  history: _heightHistory,
                ),
              ),
            ),
          ),
        ),
        // FIXED HIGH-CONTRAST CONTAINER: Crisp black text elements on a clean solid white card
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.symmetric(vertical: 14),
          decoration: BoxDecoration(
            color: Colors.white, 
            borderRadius: BorderRadius.circular(10),
            border: Border.all(color: Colors.grey[300]!, width: 1),
            boxShadow: [
              BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 4, offset: const Offset(0, 2))
            ]
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(child: _buildTelemetryCard("Current Alt", "${_rocketHeight.toStringAsFixed(0)} km")),
              Expanded(child: _buildTelemetryCard("Live Speed", "${_rocketVelocity.toStringAsFixed(1)} km/s")),
              Expanded(child: _buildTelemetryCard("Required v_e", "${realEscapeVelocity.toStringAsFixed(1)} km/s")),
            ],
          ),
        ),
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Move to Competitive Exam Drill ➡️"),
        ),
      ],
    );
  }

  // --- TAB 4: EXAM ASSESSMENT VIEW ---
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
          _buildEscapeQuiz(),
        ],
      ),
    );
  }

  // --- WIDGET GENERATION HELPERS ---
  // Guaranteed high contrast method using explicit dark typography elements over light backgrounds
  Widget _buildTelemetryCard(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Text(
          label.toUpperCase(), 
          textAlign: TextAlign.center,
          style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 11, fontWeight: FontWeight.bold, letterSpacing: 0.5)
        ),
        const SizedBox(height: 4),
        Text(
          value, 
          textAlign: TextAlign.center,
          style: TextStyle(color: Theme.of(context).colorScheme.onSurface, fontSize: 15, fontWeight: FontWeight.bold, fontFamily: 'monospace')
        ),
      ],
    );
  }

  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.teal[900])),
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
        style: TextButton.styleFrom(backgroundColor: Colors.teal[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildEscapeQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "If a rocket's escape velocity on Earth's surface is 11.2 km/s, what would be the required escape velocity for a payload container that is four times heavier?"
        : "A planet has exactly twice the mass density (ρ) of Earth but boasts the identical radius. What is the ratio of this planet's escape velocity to Earth's escape velocity?";

    List<String> options = isNeet
        ? ["22.4 km/s", "44.8 km/s", "11.2 km/s", "5.6 km/s"]
        : ["1 : 1", "√2 : 1", "2 : 1", "1 : √2"];

    int correctIndex = isNeet ? 2 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          isNeet ? "NEET Mass Independence Theory:" : "JEE Cosmic Density Fields:", 
          style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)
        ),
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
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500, color: Theme.of(context).colorScheme.onSurface)), 
              activeColor: Colors.teal[900], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[900], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Evaluate Trajectory Proofs'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  _selectedAnswerIndex == correctIndex ? "✅ CORRECT CONCEPT DERIVATION" : "❌ DEEP CONCEPT BREAKDOWN",
                  style: TextStyle(fontWeight: FontWeight.bold, color: _selectedAnswerIndex == correctIndex ? Colors.green[800] : Colors.red[800], fontSize: 11),
                ),
                const Divider(height: 10),
                Text(
                  _selectedAnswerIndex == correctIndex
                    ? (isNeet 
                        ? "FORMULA DERIVATION — INDEPENDENCE OF TEST MASS:\n\n"
                          "1. Conservation of Energy Principle:\n"
                          "   To completely escape a planet's gravity field, the rocket must reach infinity (r = ∞) with a terminal kinetic energy state of zero.\n"
                          "   Total Mechanical Energy = K.E. + P.E. = 0\n"
                          "   ½ m(v_e)² + (-GMm / R) = 0\n\n"
                          "2. Mass Cancellation:\n"
                          "   Notice that the mass of the projectile ('m') cancels out completely from both sides of the equation:\n"
                          "   ½ m(v_e)² = GMm / R  →  v_e = √(2GM / R)\n\n"
                          "Because escape speed depends solely on the planet's mass (M) and radius (R), it remains exactly 11.2 km/s regardless of whether you launch a pebble or a 4x heavier payload."
                        : "ADVANCED COSMIC DENSITY MATRIX PROOF:\n\n"
                          "1. Expressing Mass as a Function of Density (ρ):\n"
                          "   For a uniform spherical celestial body, mass is bounded by volume:\n"
                          "   M = Density × Volume = ρ × (⁴/₃ π R³)\n\n"
                          "2. Substituting into Escape Equation:\n"
                          "   v_e = √[ 2G × ρ × (⁴/₃ π R³) / R ] = R × √(⁸/₃ π G ρ)\n\n"
                          "3. Extracting Key Proportionalities:\n"
                          "   If planetary radius (R) is kept completely constant, escape speed scales with the square root of the density factor: v_e ∝ √ρ.\n"
                          "   v_planet / v_earth = √(ρ_planet / ρ_earth) = √(2 / 1) = √2 : 1.")
                    : (isNeet 
                        ? "CRITICAL EXAM PITFALL — EXPLORING INERTIAL BALANCES:\n\n"
                          "Do not fall into the trap of multiplying the target velocity by 4 or dividing it. While a payload container 4x heavier experiences 4x more downward gravitational force (F = 4mg), it also possesses exactly 4x more structural inertia resisting acceleration.\n\n"
                          "These terms perfectly scale out in the energy balance, making v_e independent of mass."
                        : "CONCEPTUAL ERROR — MIXING PLANETARY RADII AND VOLUMES:\n\n"
                          "Remember that modifying density directly alters total mass content when radius remains locked. \n\n"
                          "Since mass scales linearly with density (M ∝ ρ) and escape velocity scales as a square root function of mass (v_e ∝ √M), doubling the core density increases your threshold velocity parameter exactly by a factor of √2."),
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
      padding: const EdgeInsets.all(12), 
      color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('Planet Mass Factor: ${_planetMassFactor.toStringAsFixed(1)}', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.blueGrey[900])), Slider(value: _planetMassFactor, min: 1.0, max: 4.0, divisions: 3, activeColor: Colors.teal, onChanged: _isFlying ? null : (val) => setState(() => _planetMassFactor = val))])),
          Expanded(child: Column(children: [Text('Launch Speed (v): ${_launchVelocity.toStringAsFixed(1)} km/s', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.blueGrey[900])), Slider(value: _launchVelocity, min: 3.0, max: 9.0, divisions: 12, activeColor: Colors.cyan[800], onChanged: _isFlying ? null : (val) => setState(() => _launchVelocity = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isFlying ? null : _launchRocket, 
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.teal[900],
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
            ), 
            icon: Icon(Icons.rocket_launch, color: Colors.white, size: 18),
            label: Text(TrilingualService.instance.getUIText('Fire Rocket Upward'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12))
          ),
          IconButton(onPressed: _resetLaunchPad, icon: Icon(Icons.refresh), color: Colors.blueGrey[700]),
        ]),
      ]),
    );
  }
}

class VerticalLaunchPainter extends CustomPainter {
  final double height;
  final List<double> history;
  VerticalLaunchPainter({required this.height, required this.history});

  @override
  void paint(Canvas canvas, Size size) {
    double groundY = size.height - 30.0;
    double centerX = size.width / 2.0;
    
    Paint planetPaint = Paint()..color = Colors.teal[800]!..style = PaintingStyle.fill;
    canvas.drawRect(Rect.fromLTRB(0, groundY, size.width, size.height), planetPaint);

    if (history.isNotEmpty) {
      Paint plotPaint = Paint()..color = Colors.tealAccent.withValues(alpha: 0.3)..strokeWidth = 2.0..style = PaintingStyle.stroke;
      Path plotPath = Path();
      double stepX = (size.width * 0.3) / 200.0;
      plotPath.moveTo(0, groundY - history.first * 0.7);
      for (int i = 0; i < history.length; i++) {
        double plotY = (groundY - history[i] * 0.7).clamp(10.0, groundY);
        plotPath.lineTo(i * stepX, plotY);
      }
      canvas.drawPath(plotPath, plotPaint);
    }

    double currentRocketY = (groundY - height * 0.7).clamp(15.0, groundY); 
    
    if (height > 0) {
      Paint exhaustPaint = Paint()..color = Colors.orangeAccent..style = PaintingStyle.fill;
      canvas.drawCircle(Offset(centerX, currentRocketY + 8), 4.0, exhaustPaint);
    }

    Paint rocketBodyPaint = Paint()..color = Colors.white;
    canvas.drawRect(Rect.fromCenter(center: Offset(centerX, currentRocketY), width: 8.0, height: 16.0), rocketBodyPaint);
    
    Paint noseConePaint = Paint()..color = Colors.red;
    Path conePath = Path();
    conePath.moveTo(centerX - 4.0, currentRocketY - 8.0);
    conePath.lineTo(centerX + 4.0, currentRocketY - 8.0);
    conePath.lineTo(centerX, currentRocketY - 15.0);
    conePath.close();
    canvas.drawPath(conePath, noseConePaint);
  }

  @override
  bool shouldRepaint(covariant VerticalLaunchPainter oldDelegate) => true;
}