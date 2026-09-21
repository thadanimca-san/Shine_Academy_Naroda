import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

void main() {
  runApp(const MaterialApp(
    home: GravityVariationSimulator(),
    debugShowCheckedModeBanner: false,
  ));
}

class GravityVariationSimulator extends StatefulWidget {
  const GravityVariationSimulator({Key? key}) : super(key: key);

  @override
  _GravityVariationSimulatorState createState() => _GravityVariationSimulatorState();
}

class _GravityVariationSimulatorState extends State<GravityVariationSimulator> with TickerProviderStateMixin {
  // Distance from center of Earth in units where R = 100 pixels
  // 0 = Core, 100 = Surface, 250 = High Altitude Space
  double _radialDistance = 100.0; 
  
  final double _surfaceG = 9.81;
  final double _earthRadiusMeters = 6400000.0; // 6400 km standard

  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final double rNormalized = _radialDistance / 100.0; // r / R
    double calculatedG = 0.0;
    String locationZone = "";

    // Physics Engine Logic
    if (_radialDistance < 100.0) {
      calculatedG = _surfaceG * rNormalized;
      double depthKm = (1.0 - rNormalized) * (_earthRadiusMeters / 1000.0);
      locationZone = "Underground (Depth: ${depthKm.toStringAsFixed(0)} km)";
    } else if (_radialDistance == 100.0) {
      calculatedG = _surfaceG;
      locationZone = "Earth Surface";
    } else {
      calculatedG = _surfaceG / (rNormalized * rNormalized);
      double altitudeKm = (rNormalized - 1.0) * (_earthRadiusMeters / 1000.0);
      locationZone = "Space (Altitude: ${altitudeKm.toStringAsFixed(0)} km)";
    }

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Gravity Variation Master Lab"), 
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
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
            Tab(icon: Icon(Icons.public), text: "3. Simulation"),
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
            _buildSimulationTab(calculatedG, rNormalized, locationZone),

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
          _buildChapterHeader("GRAVITATIONAL FIELD VARIATION", "NCERT Class 11 / JEE-NEET High Yield"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "Acceleration Due to Gravity (g)",
            "The acceleration experienced by a body in free fall under the influence of Earth's gravitational force. While we assume g ≈ 9.8 m/s² for simple kinematic problems, it varies dynamically based on altitude (height), depth, Earth's rotation, and its non-spherical shape (oblate spheroid nature).",
            Colors.deepPurple[800] ?? Colors.deepPurple // Changed from 850 to 800 with safe fallback
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core Variation Factors:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Altitude (Height):", "As you rise above the surface, the distance from Earth's mass center increases. The field decays exponentially according to an inverse-square law."),
          _buildBulletPoint("Depth (Underground):", "As you go down, the mass shell 'above' you has zero net gravitational pull (Shell Theorem). Only the mass below your radial point pulls you, creating a linear drop-off down to zero at the core."),
          _buildBulletPoint("Latitude / Rotation:", "Centrifugal forces generated by Earth's rotation counteract gravity slightly, meaning g is minimum at the equator and maximum at the poles."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "Calculus & Planetary Shell Theorem"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Earth's Surface Gravity:\n""   g = G·M / R²\n\n" 
              "2. Altitude Variation (h above surface):\n" 
              "   g_h = G·M / (R+h)² = g / (1 + h/R)²\n" 
              "   Using Binomial Approximation (if h ≪ R):\n" 
              "   g_h ≈ g(1 - 2h/R)\n\n" 
              "3. Depth Variation (d below surface):\n" 
              "   Enclosed Mass M' = M · (r/R)³\n" 
              "   g_d = G·M' / r² = G·M·r / R³\n" 
              "   Since r = R - d:\n" 
              "   g_d = g(1 - d/R)  [Perfect Linear Decay]"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Competitive Exam Crux Note:",
            "The linear decrease with depth is exactly half as fast as the initial binomial decrease with altitude.\n\n"
            "• At altitude h, gravity drops by 2% per unit height.\n"
            "• At depth d, gravity drops by 1% per unit depth.\n"
            "This leads to the famous relation: Δg_altitude ≈ 2 * Δg_depth.",
            Colors.blueGrey[900] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double calculatedG, double rNormalized, String locationZone) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.deepPurple[50],
          child: Text(
            "Active Tracking Zone: $locationZone",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.deepPurple[900]),
          ),
        ),

        // Interactive Planet Canvas
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.grey[950], 
              borderRadius: BorderRadius.circular(12),
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: RepaintBoundary(
                child: LayoutBuilder(builder: (context, constraints) {
                  return CustomPaint(
                    size: Size(constraints.maxWidth, constraints.maxHeight),
                    painter: GravityCorePainter(radialDistance: _radialDistance),
                  );
                }),
              ),
            ),
          ),
        ),

        // Telemetry Data Readout (FIXED: Explicit Dark Background)
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
          padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 8),
          decoration: BoxDecoration(
            color: Colors.deepPurple[950] ?? const Color(0xFF1A0B2E), // Safe dark fallback
            borderRadius: BorderRadius.circular(10),
            boxShadow: [
              BoxShadow(
                color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.2),
                blurRadius: 6,
                offset: const Offset(0, 3),
              )
            ]
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Local g Field", "${calculatedG.toStringAsFixed(2)} m/s²"),
              _buildTelemetry("Weight of 10kg", "${(calculatedG * 10).toStringAsFixed(1)} N"),
              _buildTelemetry("r / R Ratio", "${rNormalized.toStringAsFixed(2)} x"),
            ],
          ),
        ),

        // Interactive Sliders Tray
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
          _buildGravityQuiz(),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.deepPurple[900])),
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
      decoration: BoxDecoration(
        color: accentColor.withValues(alpha: 0.08), 
        borderRadius: BorderRadius.circular(8), 
        border: Border.all(color: accentColor.withValues(alpha: 0.3)),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.deepPurple[900], fontSize: 16)),
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
          backgroundColor: Colors.deepPurple[900], 
          foregroundColor: Colors.white, 
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
        ),
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

  Widget _buildGravityQuiz() {
    bool isNeet = _targetPath == 'NEET';

    String questionText = isNeet
        ? "How does the acceleration due to gravity (g) alter mathematically as you move from the surface down to the absolute center of Earth?"
        : "At what height 'h' above the Earth's surface does the acceleration due to gravity diminish to exactly g/4? (Let R be the radius of Earth)";

    List<String> options = isNeet
        ? [
            "Decreases parabolically [g ∝ (1 - d²/R²)]", 
            "Decreases linearly to zero [g ∝ r]", 
            "Increases linearly toward core [g ∝ d]", 
            "Remains absolutely constant"
          ]
        : [
            "h = R / 2", 
            "h = 2R", 
            "h = R", 
            "h = √2R"
          ];

    int correctIndex = isNeet ? 1 : 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          isNeet ? "NEET Core Trend:" : "JEE Altitude Mechanics:", 
          style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14),
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
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(6), 
                side: BorderSide(color: Colors.grey[200] ?? Colors.grey),
              ),
              value: index, 
              groupValue: _selectedAnswerIndex, 
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500)), 
              activeColor: Colors.deepPurple, 
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
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.deepPurple[900], 
                padding: const EdgeInsets.symmetric(vertical: 12),
              ), 
              child: Text(TrilingualService.instance.getUIText('Verify Gravity Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "✅ CORRECT CONCEPT DERIVATION:\n\nInside the Earth, depth scaling dictates that g_d = g(1 - d/R). This can be rewritten as g is proportional to r (distance from center). It decreases in a perfectly straight linear line down to zero at the core."
                    : "✅ CORRECT FIELD MATHEMATICS:\n\nUsing the exact formula: g_h = g [R / (R+h)]². Setting g_h = g/4 yields 1/4 = [R / (R+h)]². Taking the square root gives 1/2 = R / (R+h), which simplifies directly to h = R.")
                : "❌ CONCEPT MISALIGNMENT:\n\nReview the Formula Derivation Tab! Energy transitions dynamically through depth or altitude scaling distribution profiles. Be sure to analyze planetary boundary assertions before choosing tracking options.",
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
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(TrilingualService.instance.getUIText('Center (r=0)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Colors.blueGrey)),
              Text(
                'Probe Position (r): ${_radialDistance.toStringAsFixed(0)}% of R', 
                style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.deepPurple),
              ),
              Text(TrilingualService.instance.getUIText('Space (2.3R)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Colors.blueGrey)),
            ],
          ),
          Slider(
            value: _radialDistance, 
            min: 0.0, 
            max: 230.0, 
            divisions: 46, 
            activeColor: Colors.deepPurple, 
            onChanged: (val) => setState(() => _radialDistance = val),
          ),
        ],
      ),
    );
  }
}

class GravityCorePainter extends CustomPainter {
  final double radialDistance;
  GravityCorePainter({required this.radialDistance});

  @override
  void paint(Canvas canvas, Size size) {
    Offset center = Offset(size.width / 2.0, size.height / 2.0);
    double earthRadiusPixels = 75.0; // Absolute scale mapping

    // 1. Draw Space Background Atmosphere Ring
    Paint spacePaint = Paint()..color = Colors.blue.withValues(alpha: 0.08)..style = PaintingStyle.fill;
    canvas.drawCircle(center, earthRadiusPixels * 2.3, spacePaint);

    // 2. Draw Solid Earth Planet Body
    Paint mantlePaint = Paint()..color = Colors.deepOrange[800] ?? Colors.deepOrange..style = PaintingStyle.fill;
    canvas.drawCircle(center, earthRadiusPixels, mantlePaint);
    
    // Draw Earth Crust Outline boundary
    Paint crustPaint = Paint()..color = Colors.green[700] ?? Colors.green..style = PaintingStyle.stroke..strokeWidth = 3.0;
    canvas.drawCircle(center, earthRadiusPixels, crustPaint);

    // 3. Draw Liquid Hot Core Center
    Paint corePaint = Paint()..color = Colors.yellowAccent..style = PaintingStyle.fill;
    canvas.drawCircle(center, earthRadiusPixels * 0.25, corePaint);

    // 4. Calculate Vector Position of the Interactive Test Probe
    // Map slider 100 units to match our 75-pixel radius
    double renderingRadius = (radialDistance / 100.0) * earthRadiusPixels;
    
    // Lock angle along a clean 30-degree vector line for scanning
    double scanAngle = -math.pi / 6.0; 
    Offset probePos = Offset(
      center.dx + renderingRadius * math.cos(scanAngle),
      center.dy + renderingRadius * math.sin(scanAngle)
    );

    // Draw connecting radius measurement line
    Paint vectorLinePaint = Paint()..color = Colors.white30..strokeWidth = 1.5;
    canvas.drawLine(center, probePos, vectorLinePaint);

    // 5. Draw the Test Probe Target Node
    canvas.drawCircle(probePos, 6.0, Paint()..color = Colors.cyanAccent);
    canvas.drawCircle(probePos, 9.0, Paint()..color = Colors.cyan.withValues(alpha: 0.4)..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  @override
  bool shouldRepaint(covariant GravityCorePainter oldDelegate) {
    return oldDelegate.radialDistance != radialDistance;
  }
}