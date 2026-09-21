import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PlanetaryMotionSimulator extends StatefulWidget {
  const PlanetaryMotionSimulator({Key? key}) : super(key: key);

  @override
  _PlanetaryMotionSimulatorState createState() => _PlanetaryMotionSimulatorState();
}

class _PlanetaryMotionSimulatorState extends State<PlanetaryMotionSimulator> with TickerProviderStateMixin {
  // Physical Orbit Variables
  double _eccentricity = 0.4;       // Orbit stretch factor (e)
  bool _showArealSectors = true;    // Visual guide for Kepler's 2nd Law
  double _orbitTrueAnomaly = 0.0;   // Angular position along orbit (theta)
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late AnimationController _orbitController;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);

    // Dynamic Lifecycle Catch: Automatically pause orbital loops when leaving the simulator viewport
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging && _tabController.index != 2) {
        if (_orbitController.isAnimating) {
          _orbitController.stop();
        }
      } else if (!_tabController.indexIsChanging && _tabController.index == 2) {
        if (!_orbitController.isAnimating) {
          _orbitController.repeat();
        }
      }
    });

    _orbitController = AnimationController(vsync: this, duration: const Duration(seconds: 6))..addListener(() {
      setState(() {
        // Kepler's 2nd Law Angular Mechanics: d(theta)/dt = L / (m * r²)
        // Orbit equation: r = a(1 - e²) / (1 + e*cos(theta))
        double semiMajorAxis = 100.0;
        double currentRadius = (semiMajorAxis * (1.0 - _eccentricity * _eccentricity)) / 
                               (1.0 + _eccentricity * math.cos(_orbitTrueAnomaly));
        
        // Compute speed scaling step (inversely proportional to r²)
        double baseAngularVelocity = 2.0 / (currentRadius * currentRadius);
        _orbitTrueAnomaly += baseAngularVelocity * 450.0; 
        
        if (_orbitTrueAnomaly > 2 * math.pi) {
          _orbitTrueAnomaly -= 2 * math.pi;
        }
      });
    });
    _orbitController.repeat();
  }

  @override
  void dispose() {
    _orbitController.dispose();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Kepler's Third Law Verification variables: T² ∝ a³
    double semiMajorA = 100.0;
    double calculatedPeriodRatio = math.sqrt(math.pow(semiMajorA, 3) / 10000.0);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Planetary Motion Laboratory"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
        backgroundColor: Palette.primaryDeep,
        centerTitle: false, // Ensures neat positioning alongside back arrows if nested
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
            Tab(icon: Icon(Icons.blur_circular), text: "3. Simulation"),
            Tab(icon: Icon(Icons.assignment), text: "4. Exam Drill"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroductionTab(),
            _buildDerivationTab(semiMajorA),
            _buildSimulationTab(semiMajorA, calculatedPeriodRatio),
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: CONCEPTUAL INTRODUCTION ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("KEPLER'S LAWS OF PLANETARY MOTION", "NCERT Class 11 / JEE-NEET High-Yield Core"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "Foundational Gravitational Framework",
            "Planetary orbital mechanics are governed by the gravitational interaction between bodies. Kepler's empirical laws completely map these celestial pathways, later proven analytically by Isaac Newton's vector formulations.",
            Colors.amber[900]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Three Laws Explained:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("1. Law of Orbits:", "All planets move in elliptical orbits with the Sun situated at one of the two operational focal points."),
          _buildBulletPoint("2. Law of Areas:", "A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time (proven via constant angular momentum)."),
          _buildBulletPoint("3. Law of Periods:", "The square of the orbital period (T²) of a planet is directly proportional to the cube of the semi-major axis (a³) of its elliptical path."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "View Mathematical Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: MATHEMATICAL FORMULATIONS ---
  Widget _buildDerivationTab(double semiMajorA) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("ANALYTICAL ORBITAL MATHEMATICS", "Core Derivations & Conserved Quantities"),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Elliptical Radial Boundary Function (r):\n""   r(θ) = a · (1 - e²) / (1 + e · cosθ)\n" 
              "   Where:\n" 
              "   • a = Semi-major axis dimension\n" 
              "   • e = Eccentricity stretch factor\n" 
              "   • θ = True anomaly angle position\n\n" 
              "2. Angular Momentum Invariance (Kepler 2):\n" 
              "   dA/dt = L / (2m) = Constant\n" 
              "   Since torque (τ = r × F) is zero in central gravitational fields, \n" 
              "   Angular Momentum (L = mvr) stays perfectly constant.\n\n" 
              "3. Velocity at Boundary Extremities:\n" 
              "   • Perihelion (Closest Focus Point): r_min = a(1 - e)\n" 
              "   • Aphelion (Farthest Focus Point): r_max = a(1 + e)\n" 
              "   Ratio: v_max / v_min = (1 + e) / (1 - e)\n\n" 
              "4. Kepler's Harmony Proportionality:\n" 
              "   T² = (4π² / GM) · a³   =>   T² ∝ a³"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.cyanAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Quick Revision Formula:",
            "When dealing with velocity proportions at the extreme vertex thresholds, use the Conservation of Angular Momentum shortcut:\n"
            "v_perihelion · r_perihelion = v_aphelion · r_aphelion",
            Colors.amber[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Open Interactive Sandbox ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: GRAPHICAL SIMULATION ENVIRONMENT ---
  Widget _buildSimulationTab(double semiMajorA, double calculatedPeriodRatio) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.amber[50],
          child: Text(
            _orbitController.isAnimating ? "🟢 System Tracking: Keplerian Vector Engine Active" : "🛑 Engine Standby: Orbital Velocity Loop Paused",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.amber[900]),
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: ClipRect(
              child: LayoutBuilder(builder: (context, constraints) {
                return CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: PlanetaryOrbitPainter(
                    trueAnomaly: _orbitTrueAnomaly,
                    eccentricity: _eccentricity,
                    showSectors: _showArealSectors,
                  ),
                );
              }),
            ),
          ),
        ),
        
        // FIX: Replaced invalid Colors.amber[950] with a high-contrast dark palette card.
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: Colors.blueGrey[900], 
            borderRadius: BorderRadius.circular(10),
            boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.12), blurRadius: 4, offset: Offset(0, 2))
            ],
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Eccentricity (e)", _eccentricity.toStringAsFixed(2), Colors.white),
              _buildTelemetry("Semi-Major (a)", "${semiMajorA.toStringAsFixed(0)} m", Colors.cyanAccent),
              _buildTelemetry("T²/a³ Constant", "1.00", Colors.greenAccent),
              _buildTelemetry("Period (T)", "${calculatedPeriodRatio.toStringAsFixed(1)} yrs", Colors.orangeAccent),
            ],
          ),
        ),
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Proceed to Exam Assessment ➡️"),
        ),
      ],
    );
  }

  // --- TAB 4: TARGETED DRILL EVALUATION ---
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Concept Check'), style: TextStyle(fontWeight: FontWeight.bold))), 
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Analytical Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildPlanetaryQuiz(),
        ],
      ),
    );
  }

  // Core UI Builder Mixins
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.amber[900])),
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
      decoration: BoxDecoration(color: accentColor.withValues(alpha: 0.06), borderRadius: BorderRadius.circular(8), border: Border.all(color: accentColor.withValues(alpha: 0.25))),
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
        style: TextButton.styleFrom(backgroundColor: Colors.amber[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
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
        Text(value, style: TextStyle(color: valColor, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildPlanetaryQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "Kepler's Second Law (equal areas swept in equal time intervals) directly proves the conservation of which foundational mechanical quantity?"
        : "A planet moves in an elliptical orbit with eccentricity 'e'. What is the ratio of its maximum orbital speed at perihelion to its minimum speed at aphelion (v_max / v_min)?";

    List<String> options = isNeet
        ? ["Linear Momentum", "Kinetic Energy", "Angular Momentum", "Total Binding Energy"]
        : ["(1 + e) / (1 - e)", "(1 - e) / (1 + e)", "1 / e²", "√(1 + e)"];

    int correctIndex = isNeet ? 2 : 0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Keplerian Invariance:" : "JEE Velocity Extremes:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.amber[900], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.amber[900], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Orbital Invariance'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "Correct! 🎉 Kepler's second law is a direct consequence of Conservation of Angular Momentum. Since gravity pulls directly along the radial vector towards the host star's core, the net torque equals zero, keeping angular momentum constant."
                    : "Correct! 🎉 By conserving angular momentum at the endpoints: m · v_max · r_min = m · v_min · r_max. In elliptical paths, r_min = a(1 - e) and r_max = a(1 + e). Swapping these gives the ratio: v_max / v_min = (1 + e) / (1 - e).")
                : (isNeet 
                    ? "Incorrect ❌ Think of torque balances! The central force acts along the radius line, producing zero cross-product torque. This isolates Angular Momentum as an absolute constant."
                    : "Incorrect ❌ Apply angular momentum conservation! Use the minimum and maximum distance values from the focal point, which evaluate directly to the ratio: (1 + e) / (1 - e)."),
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10), 
      color: Colors.white,
      child: Row(children: [
        Expanded(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Orbit Eccentricity (e): ${_eccentricity.toStringAsFixed(2)}', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)), 
              Slider(value: _eccentricity, min: 0.0, max: 0.7, divisions: 7, activeColor: Colors.amber[900], onChanged: (val) => setState(() => _eccentricity = val))
            ]
          )
        ),
        const SizedBox(width: 24),
        Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(TrilingualService.instance.getUIText('Areal Sweeps'), style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)),
            Switch(
              value: _showArealSectors, 
              activeThumbColor: Colors.amber[850], 
              onChanged: (val) => setState(() => _showArealSectors = val)
            )
          ]
        ),
      ]),
    );
  }
}

class PlanetaryOrbitPainter extends CustomPainter {
  final double trueAnomaly;
  final double eccentricity;
  final bool showSectors;

  PlanetaryOrbitPainter({
    required this.trueAnomaly, 
    required this.eccentricity, 
    required this.showSectors,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // 1. Establish central nodes relative to dynamic viewport layout bounds
    final Offset center = Offset(size.width / 2.0, size.height / 2.0);
    
    // Dynamic boundary limits scaling safety factors (leaves safety margins around edges)
    final double paddingMargin = 30.0;
    final double maxDimensionRadius = (size.width / 2.0) - paddingMargin;
    
    // Compute true elliptical semi-axes bounding shapes relative to live container size
    final double a = maxDimensionRadius > 140.0 ? 140.0 : maxDimensionRadius; 
    final double b = a * math.sqrt(1.0 - eccentricity * eccentricity);
    
    // Distance from center to focal node points: c = a * e
    final double c = a * eccentricity;
    final Offset starFocus = Offset(center.dx - c, center.dy); // Repositioned to left focus for standardized plotting

    // 2. Draw Elliptical Orbit Track Path
    final Paint orbitLinePaint = Paint()
      ..color = Colors.amber.withValues(alpha: 0.25)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5;
    canvas.drawOval(Rect.fromLTRB(center.dx - a, center.dy - b, center.dx + a, center.dy + b), orbitLinePaint);

    // 3. Draw Equal Area Wedge Sectors (Kepler 2 Demonstration Guide)
    if (showSectors) {
      final Paint wedgePaint = Paint()
        ..color = Colors.cyan.withValues(alpha: 0.12)
        ..style = PaintingStyle.fill;
      
      // Plot three separate visual context blocks around the field trajectory
      _drawSampleWedge(canvas, starFocus, a, eccentricity, 0.0, 0.35, wedgePaint);
      _drawSampleWedge(canvas, starFocus, a, eccentricity, math.pi * 0.45, math.pi * 0.62, wedgePaint);
      _drawSampleWedge(canvas, starFocus, a, eccentricity, math.pi * 0.82, math.pi * 1.18, wedgePaint);
    }

    // 4. Compute Current Instantaneous Planet Coordinates relative to star focal coordinate
    final double r = (a * (1.0 - eccentricity * eccentricity)) / (1.0 + eccentricity * math.cos(trueAnomaly));
    final Offset planetPos = Offset(
      starFocus.dx + r * math.cos(trueAnomaly),
      starFocus.dy + r * math.sin(trueAnomaly)
    );

    // Dynamic radius linking track vector line
    canvas.drawLine(starFocus, planetPos, Paint()..color = Colors.white24..strokeWidth = 1.0);

    // 5. Draw Central Host Parent Star Node
    final Paint starPaint = Paint()
      ..shader = RadialGradient(
        colors: [Colors.amber[300]!, Colors.orange[900]!],
      ).createShader(Rect.fromCircle(center: starFocus, radius: 14.0));
      
    canvas.drawCircle(starFocus, 14.0, starPaint);
    canvas.drawCircle(
      starFocus, 
      14.0, 
      Paint()
        ..color = Colors.orangeAccent.withValues(alpha: 0.3)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );

    // 6. Draw Bounded Orbiting Planet Bob Capsule
    canvas.drawCircle(planetPos, 5.0, Paint()..color = Colors.cyanAccent);
    canvas.drawCircle(
      planetPos, 
      7.5, 
      Paint()
        ..color = Colors.cyan.withValues(alpha: 0.3)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.0,
    );
  }

  void _drawSampleWedge(Canvas canvas, Offset focus, double a, double ecc, double startAngle, double endAngle, Paint paint) {
    final Path wedgePath = Path();
    wedgePath.moveTo(focus.dx, focus.dy);
    
    const int resolutionPoints = 25;
    for (int i = 0; i <= resolutionPoints; i++) {
      final double angle = startAngle + (endAngle - startAngle) * (i / resolutionPoints);
      final double r = (a * (1.0 - ecc * ecc)) / (1.0 + ecc * math.cos(angle));
      wedgePath.lineTo(focus.dx + r * math.cos(angle), focus.dy + r * math.sin(angle));
    }
    wedgePath.close();
    canvas.drawPath(wedgePath, paint);
  }

  @override
  bool shouldRepaint(covariant PlanetaryOrbitPainter oldDelegate) {
    return oldDelegate.trueAnomaly != trueAnomaly || 
           oldDelegate.eccentricity != eccentricity || 
           oldDelegate.showSectors != showSectors;
  }
}