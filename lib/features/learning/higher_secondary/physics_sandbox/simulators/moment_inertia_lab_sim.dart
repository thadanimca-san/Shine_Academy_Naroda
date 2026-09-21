import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

void main() {
  runApp(const MaterialApp(
    home: MomentInertiaLabSimulator(),
    debugShowCheckedModeBanner: false,
  ));
}

class MomentInertiaLabSimulator extends StatefulWidget {
  const MomentInertiaLabSimulator({Key? key}) : super(key: key);

  @override
  _MomentInertiaLabSimulatorState createState() => _MomentInertiaLabSimulatorState();
}

class _MomentInertiaLabSimulatorState extends State<MomentInertiaLabSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _mass = 2.0;               // Mass (M) in kg
  double _radius = 2.0;             // Radius (R) in meters
  double _axisShift = 0.0;          // Distance shifted from CM (d) in meters
  String _selectedShape = 'Solid Disk'; // Shape variant profile
  
  double _rotationAngle = 0.0;
  bool _isRotating = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;

  final Map<String, double> _shapeCoefficients = {
    'Solid Disk': 0.5,
    'Thin Hoop': 1.0,
    'Solid Sphere': 0.4,
    'Hollow Sphere': 0.667,
  };

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 8))..addListener(() {
      if (_isRotating) {
        setState(() {
          // Track uniform rotational speed based on calculated inertia properties
          double baseInertia = _shapeCoefficients[_selectedShape]! * _mass * _radius * _radius;
          double totalInertia = baseInertia + (_mass * _axisShift * _axisShift);
          // Speed inversely proportional to total resistance
          double speedMultiplier = 15.0 / (totalInertia + 0.1);
          _rotationAngle = _controller.value * 2 * math.pi * speedMultiplier;
        });
      }
    });
  }

  void _startLab() {
    setState(() { 
      _isRotating = true; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
    _controller.repeat();
  }

  void _resetLab() {
    setState(() { 
      _isRotating = false; 
      _rotationAngle = 0.0; 
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
    // Parallel Axis Theorem Math: I_total = I_cm + M*d^2
    double iCM = _shapeCoefficients[_selectedShape]! * _mass * _radius * _radius;
    double iTotal = iCM + (_mass * _axisShift * _axisShift);
    double radiusOfGyration = math.sqrt(iTotal / _mass);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Rotational Dynamics Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.loop), text: "3. Simulation"),
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
            _buildSimulationTab(iCM, iTotal, radiusOfGyration),

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
          _buildChapterHeader("MOMENT OF INERTIA & PARALLEL AXIS THEOREM", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Rotational Inertia?",
            "Moment of Inertia (I) measures a body's stubborn resistance to rotational acceleration, playing the identical role that mass plays in linear motion. Unlike mass, it depends heavily on how distance handles mass distribution relative to the selected rotation axis line.",
            Palette.primaryDeep
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Components:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Center of Mass Inertia (I_cm):", "The unique rotational resistance when a body spins cleanly around an axis piercing its geometric center balancing node."),
          _buildBulletPoint("Parallel Axis Theorem:", "States that if you shift an axis parallel by distance 'd', total inertia transforms cleanly following the equation: I = I_cm + Md²."),
          _buildBulletPoint("Radius of Gyration (k):", "The radial distance from the rotation pivot where the entire system mass could compress into a point without altering its rotational inertia: k = √(I/M)."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "Rigorous Parallel Axis Theorem Balancing"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Consider a differential mass element 'dm' at distance 'r' from CM:\n""   Let the axis be shifted by a distance 'd'.\n\n" 
              "2. Coordinate Distance Transformation:\n" 
              "   r_new² = (x + d)² + y²\n" 
              "   r_new² = (x² + y²) + d² + 2xd\n" 
              "   r_new² = r_cm² + d² + 2xd\n\n" 
              "3. Integrating across the Entire Mass System:\n" 
              "   I = ∫ r_new² dm = ∫ (r_cm² + d² + 2xd) dm\n" 
              "   I = ∫ r_cm² dm + d² ∫ dm + 2d ∫ x dm\n\n" 
              "4. Applying Boundary Symmetry Laws:\n" 
              "   By definition of CM, the linear mass balance integral vanishes:\n" 
              "   ∫ x dm = 0\n\n" 
              "5. Foundational Theorem Conclusion:\n" 
              "   I = I_cm + M · d²"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "The calculation axis must ALWAYS run perfectly parallel to the center axis piercing the CM node. You can never shift into a tilted angle space using this theorem structure alone without invoking product-of-inertia tensor matrices.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double iCM, double iTotal, double radiusOfGyration) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Palette.primarySoft,
          child: Text(
            _isRotating ? "🟢 Spin Engine Running: Tracking Rotational Inertia Dynamics" : "🛑 Engine Standby: Configure Mass Details & Spin",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Palette.primaryDeep),
          ),
        ),

        // Interactive Shape Canvas Area
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              // Fix aspect-ratio clipping in landscape viewports by selecting shorter container edge
              double referenceDimension = constraints.maxWidth < constraints.maxHeight 
                  ? constraints.maxWidth 
                  : constraints.maxHeight;
              double scale = referenceDimension / 320.0; 

              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: InertiaLabPainter(
                  angleRad: _rotationAngle,
                  radius: _radius,
                  axisShift: _axisShift,
                  shapeType: _selectedShape,
                  scaleRatio: scale,
                ),
              );
            }),
          ),
        ),

        // Telemetry readout deck
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Palette.primaryDeep, borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("I_cm (Center)", "${iCM.toStringAsFixed(2)} kg·m²", Colors.white),
              _buildTelemetry("Shift (d)", "${_axisShift.toStringAsFixed(1)} m", Colors.cyanAccent),
              _buildTelemetry("Total Inertia", "${iTotal.toStringAsFixed(2)} kg·m²", Colors.orangeAccent),
              _buildTelemetry("Gyration (k)", "${radiusOfGyration.toStringAsFixed(2)} m", Colors.limeAccent),
            ],
          ),
        ),

        // Action controls panel
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
          _buildInertiaQuiz(),
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

  Widget _buildInertiaQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "What is the correct mathematical value for the Radius of Gyration (k) of a uniform thin hoop of radius 'R' rotating around its natural central longitudinal axis?"
        : "A solid uniform sphere and a hollow spherical shell have identical masses and external radii. If they roll down the exact same rough inclined plane without slipping, which one reaches the bottom first?";

    List<String> options = isNeet
        ? ["k = R / √2", "k = R", "k = R * √(2/5)", "k = R / 2"]
        : ["The hollow sphere wins", "The solid sphere wins", "They tie perfectly", "Neither can roll without sliding"];

    int correctIndex = 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Gyration Distribution:" : "JEE Acceleration Dynamics:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              child: Text(TrilingualService.instance.getUIText('Verify Derivation Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT CONCEPT DERIVATION:\n\nThe moment of inertia of a thin hoop is I = MR². Since radius of gyration is defined by k = √(I/M), substituting gives k = √(MR²/M) = R."
                    : "✅ CORRECT FIELD MATHEMATICS:\n\nRolling acceleration down a ramp is given by a = (g·sinθ) / (1 + I/MR²). The solid sphere has a lower inertia coefficient (0.4) than the hollow shell (0.67), meaning it resists rotation less and rolls faster!")
                : "❌ CONCEPT MISALIGNMENT:\n\nReview the Formula Derivation Tab! Hollow shapes place mass at the furthest outer profile boundary, increasing resistance vectors. Review distribution equations closely.",
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
          Expanded(child: Column(children: [Text('Mass M: ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 1.0, max: 4.0, divisions: 3, activeColor: Palette.primary, onChanged: _isRotating ? null : (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Radius R: ${_radius.toStringAsFixed(1)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _radius, min: 1.0, max: 2.5, divisions: 3, activeColor: Colors.cyan, onChanged: _isRotating ? null : (val) => setState(() => _radius = val))])),
          Expanded(child: Column(children: [Text('Axis Shift d: ${_axisShift.toStringAsFixed(1)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _axisShift, min: 0.0, max: 1.5, divisions: 3, activeColor: Colors.orange, onChanged: _isRotating ? null : (val) => setState(() => _axisShift = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          DropdownButton<String>(
            value: _selectedShape,
            disabledHint: Text(_selectedShape),
            items: [
              DropdownMenuItem(value: 'Solid Disk', child: Text(TrilingualService.instance.getUIText('Solid Disk (½MR²)'), style: TextStyle(fontSize: 12))),
              DropdownMenuItem(value: 'Thin Hoop', child: Text(TrilingualService.instance.getUIText('Thin Hoop (MR²)'), style: TextStyle(fontSize: 12))),
              DropdownMenuItem(value: 'Solid Sphere', child: Text(TrilingualService.instance.getUIText('Solid Sphere (⅖MR²)'), style: TextStyle(fontSize: 12))),
              DropdownMenuItem(value: 'Hollow Sphere', child: Text(TrilingualService.instance.getUIText('Hollow Shell (⅔MR²)'), style: TextStyle(fontSize: 12))),
            ],
            onChanged: _isRotating ? null : (val) => setState(() => _selectedShape = val!),
          ),
          ElevatedButton.icon(
            onPressed: _isRotating ? _resetLab : _startLab, 
            style: ElevatedButton.styleFrom(backgroundColor: _isRotating ? Colors.red[700] : Palette.primaryDeep, padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(_isRotating ? Icons.stop : Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(_isRotating ? 'Stop Engine' : 'Spin Engine', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
        ]),
      ]),
    );
  }
}

class InertiaLabPainter extends CustomPainter {
  final double angleRad, radius, axisShift, scaleRatio;
  final String shapeType;
  InertiaLabPainter({required this.angleRad, required this.radius, required this.axisShift, required this.shapeType, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    
    // Correctly compute virtual layout space dimensions bounds
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    // Center layout coordinates accurately
    Offset cmPoint = Offset(canvasWidth / 2.0, canvasHeight / 2.0);
    
    // Configured scale parameters to comfortably house a 2.5m object
    double pixelScale = 42.0; 
    double visualRadius = radius * pixelScale;
    double visualShift = axisShift * pixelScale;

    // Target dynamic shift rotation coordinate reference matrix
    Offset activePivotNode = Offset(cmPoint.dx - visualShift, cmPoint.dy);

    canvas.translate(activePivotNode.dx, activePivotNode.dy);
    canvas.rotate(angleRad);

    Offset localizedCM = Offset(visualShift, 0.0);

    // 1. Render Rigid Solid Geometry profiles
    Paint structurePaint = Paint()..style = PaintingStyle.fill;
    if (shapeType == 'Solid Disk') {
      structurePaint.color = Colors.indigo[200]!;
      canvas.drawCircle(localizedCM, visualRadius, structurePaint);
    } else if (shapeType == 'Thin Hoop') {
      structurePaint.color = Palette.primarySoft;
      canvas.drawCircle(localizedCM, visualRadius, structurePaint);
    } else if (shapeType == 'Solid Sphere') {
      structurePaint.color = Colors.blueGrey[300]!;
      canvas.drawCircle(localizedCM, visualRadius, structurePaint);
    } else if (shapeType == 'Hollow Sphere') {
      structurePaint.color = Colors.blueGrey[100]!;
      canvas.drawCircle(localizedCM, visualRadius, structurePaint);
    }

    // Geometry Stroke Outline Setup
    Paint outlinePaint = Paint()
      ..color = Palette.primaryDeep
      ..style = PaintingStyle.stroke
      ..strokeWidth = (shapeType == 'Thin Hoop' || shapeType == 'Hollow Sphere') ? 5.0 : 2.0;
    canvas.drawCircle(localizedCM, visualRadius, outlinePaint);

    // 2. Structural Crosswire Tethers for rotation tracking
    Paint guidePaint = Paint()..color = Palette.primaryDeep..strokeWidth = 1.0;
    canvas.drawLine(Offset(localizedCM.dx - visualRadius, localizedCM.dy), Offset(localizedCM.dx + visualRadius, localizedCM.dy), guidePaint);
    canvas.drawLine(Offset(localizedCM.dx, localizedCM.dy - visualRadius), Offset(localizedCM.dx, localizedCM.dy + visualRadius), guidePaint);
    
    // Core structural Center of Mass tracking dot
    canvas.drawCircle(localizedCM, 4.0, Paint()..color = Colors.red[700]!);

    // 3. Absolute Position Static Shift Axis Anchor Pin
    canvas.drawCircle(Offset.zero, 5.0, Paint()..color = Colors.black);
    canvas.drawCircle(Offset.zero, 1.5, Paint()..color = Colors.white);

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant InertiaLabPainter oldDelegate) => true;
}