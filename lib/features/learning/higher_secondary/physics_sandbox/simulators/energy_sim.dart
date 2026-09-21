import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class EnergySimulator extends StatefulWidget {
  const EnergySimulator({Key? key}) : super(key: key);

  @override
  _EnergySimulatorState createState() => _EnergySimulatorState();
}

class _EnergySimulatorState extends State<EnergySimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _mass = 2.0;               // Mass of block (kg)
  double _springConstant = 50.0;    // Spring constant k (N/m)
  double _compression = 0.5;       // Initial extension/compression x (m)
  double _time = 0.0;
  bool _isOscillating = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 4))..addListener(() {
      setState(() {
        _time = _controller.value * 4.0;
      });
    });
  }

  void _releaseSystem() {
    setState(() { 
      _isOscillating = true; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    });
    _controller.repeat();
  }

  void _resetSimulation() {
    setState(() { 
      _isOscillating = false; 
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
    // Core Physics Calculus engine
    double totalEnergy = 0.5 * _springConstant * math.pow(_compression, 2);
    double omega = math.sqrt(_springConstant / _mass);
    double A = _compression; 
    double tCurrent = _isOscillating ? _time : 0.0;
    
    double currentX = A * math.cos(omega * tCurrent);
    double currentV = -omega * A * math.sin(omega * tCurrent);

    double potentialEnergy = 0.5 * _springConstant * math.pow(currentX, 2);
    double kineticEnergy = 0.5 * _mass * math.pow(currentV, 2);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Work-Power-Energy Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            // TAB 1: FULL CONCEPT TEXTBOOK INTRODUCTION
            _buildIntroductionTab(),

            // TAB 2: EXAM-CRITICAL FORMULA DERIVATIONS
            _buildDerivationTab(),

            // TAB 3: LIVE PHYSICS GRAPHICS SIMULATOR
            _buildSimulationTab(totalEnergy, potentialEnergy, kineticEnergy, currentX, currentV),

            // TAB 4: INTERACTIVE ASSESSMENT DRILL
            _buildAssessmentTab(totalEnergy, kineticEnergy),
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
          _buildChapterHeader("CONSERVATION OF MECHANICAL ENERGY", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Mechanical Energy?",
            "Mechanical energy (E) is the macroscopic sum of a system's Kinetic Energy (K) and Potential Energy (U). In a conservative field (where forces like gravity and spring elasticity do not dissipate heat), the total mechanical energy remains absolutely constant at every single coordinate point.",
            Colors.orange[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Components:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Kinetic Energy (K):", "Energy possessed by virtue of motion. Written as K = ½ mv². Maxima occurs at the equilibrium position."),
          _buildBulletPoint("Potential Energy (U):", "Stored energy possessed by virtue of configuration or position. For an ideal Hooke's Law spring, U = ½ kx²."),
          _buildBulletPoint("Conservative Forces:", "Forces where work done along a closed loop path is identically zero. Work depends strictly on initial and final coordinates, not the track taken."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "Rigorous Calculus & Work-Energy Balancing"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. From Hooke's Law:\n""   F = -k · x\n\n" 
              "2. Work Done by Variable Spring Force:\n" 
              "   W = ∫ F dx = ∫ (-k · x) dx from 0 to x\n" 
              "   W = -½ · k · x²\n\n" 
              "3. By Work-Energy Theorem:\n" 
              "   W_conservative = -ΔU\n" 
              "   -½ · k · x² = -(U_final - U_initial)\n" 
              "   Assuming U(0) = 0, Stored Elastic Potential Energy:\n" 
              "   U = ½ · k · x²\n\n" 
              "4. Absolute Conservation Equation:\n" 
              "   E_total = K + U = ½·m·v² + ½·k·x² = Constant"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "At Maximum Amplitude (x = ± A):\nVelocity is zero → E = ½kA² (Purely Potential)\n\n"
            "At Equilibrium (x = 0):\nPotential Energy is zero → E = ½mv_max² (Purely Kinetic)\n\n"
            "Equating both limits gives the foundational velocity relation: v_max = A√(k/m).",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double totalE, double potE, double kinE, double currentX, double currentV) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.orange[50],
          child: Text(
            _isOscillating ? "🟢 System Tracking: Dynamic Oscillation Active" : "🛑 System Primed: Stretch Spring & Click Release",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.orange[900]),
          ),
        ),

        // Animated Spring Canvas Area
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: EnergyPhysicsPainter(
                  springConstant: _springConstant,
                  initialCompression: _compression,
                  dynamicPositionX: currentX,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),

        // Telemetry readout grid
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.orange[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Total Energy", "${totalE.toStringAsFixed(2)} J"),
              _buildTelemetry("Potential (U)", "${potE.toStringAsFixed(2)} J"),
              _buildTelemetry("Kinetic (KE)", "${kinE.toStringAsFixed(2)} J"),
              _buildTelemetry("Velocity (v)", "${currentV.abs().toStringAsFixed(2)} m/s"),
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
  Widget _buildAssessmentTab(double totalEnergy, double kineticEnergy) {
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
          _buildEnergyQuiz(totalEnergy, kineticEnergy),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.orange[900])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.orange[900], fontSize: 16)),
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
        style: TextButton.styleFrom(backgroundColor: Colors.orange[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
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

  Widget _buildEnergyQuiz(double totalEnergy, double kineticEnergy) {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "Assume this horizontal spring is frictionless and massless. If you double the initial compression distance (x), how will the maximum Kinetic Energy stored in the system change?"
        : "If this exact spring system is reoriented vertically and the initial configuration has zero extension, what is the change in total MECHANICAL energy (ΔE) after releasing the block?";

    List<String> options = isNeet
        ? ["Doubles (2x)", "Triples (3x)", "Quadruples (4x)", "Remains Unchanged"]
        : ["ΔE = mgh", "ΔE = -μ_k · m · g · d", "ΔE = 0 J (No Non-conservative Work)", "ΔE = ½ kx²"];

    int correctIndex = 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Scalar Relations Quiz:" : "JEE Conservative Field Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.orange[800], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.orange[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
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
                    ? "✅ CORRECT CONCEPT DERIVATION:\n\nElastic Work Energy (U = ½kx²) scales quadratically with position. Doubling the compression yields (2)² = 4 times the structural energy potential, transitioning cleanly into peak kinetic energy due to the friction-free barrier rules."
                    : "✅ CORRECT FIELD MATHEMATICS:\n\nGravity and spring internal mechanisms are completely conservative structures. Because no air drag or contact friction vectors exist to dissipate mechanical states, ΔE remains strictly equal to zero.")
                : "❌ CONCEPT MISALIGNMENT:\n\nReview the Formula Derivation Tab! Energy transitions dynamically through a square-law distribution profile. Be sure to analyze conservative field boundary assertions before choosing tracking options.",
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
          Expanded(child: Column(children: [Text('Inertial Mass: ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 1, max: 4, divisions: 3, activeColor: Colors.teal, onChanged: _isOscillating ? null : (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Spring Constant k: ${_springConstant.toStringAsFixed(0)} N/m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _springConstant, min: 20, max: 80, divisions: 3, activeColor: Colors.blueGrey, onChanged: _isOscillating ? null : (val) => setState(() => _springConstant = val))])),
          Expanded(child: Column(children: [Text('Compression x: ${_compression.toStringAsFixed(2)} m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _compression, min: 0.1, max: 0.8, divisions: 7, activeColor: Colors.orange, onChanged: _isOscillating ? null : (val) => setState(() => _compression = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isOscillating ? null : _releaseSystem, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('System Release'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class EnergyPhysicsPainter extends CustomPainter {
  final double springConstant, initialCompression, dynamicPositionX, scaleRatio;
  EnergyPhysicsPainter({required this.springConstant, required this.initialCompression, required this.dynamicPositionX, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double floorY = canvasHeight - 25.0;
    double leftAnchorX = 25.0;
    double equilibriumX = canvasWidth * 0.5;

    // Background Surface Boundaries
    Paint surfacePaint = Paint()..color = Colors.grey[600]!..strokeWidth = 3.0;
    canvas.drawLine(Offset(0, floorY), Offset(canvasWidth, floorY), surfacePaint);
    canvas.drawLine(Offset(leftAnchorX, floorY - 50.0), Offset(leftAnchorX, floorY), surfacePaint..strokeWidth = 4.0);

    double renderX = equilibriumX + (dynamicPositionX * 110.0);
    double blockW = 36.0;
    double blockH = 26.0;

    // Draw Spring Coil Line Segments
    Paint springPaint = Paint()..color = Colors.amberAccent..strokeWidth = 2.0..style = PaintingStyle.stroke;
    double springStartX = leftAnchorX + 2.0;
    double springEndX = renderX - blockW / 2;
    int coils = 14;
    double coilH = 12.0;
    
    Path springPath = Path();
    springPath.moveTo(springStartX, floorY - blockH / 2);
    double deltaX = (springEndX - springStartX) / coils;
    for (int i = 0; i < coils; i++) {
      double localX = springStartX + deltaX * i;
      springPath.lineTo(localX + deltaX / 4, floorY - blockH / 2 - coilH);
      springPath.lineTo(localX + deltaX * 3 / 4, floorY - blockH / 2 + coilH);
    }
    springPath.lineTo(springEndX, floorY - blockH / 2);
    canvas.drawPath(springPath, springPaint);

    // Render Mass Box Block
    canvas.drawRect(Rect.fromLTWH(renderX - blockW / 2, floorY - blockH, blockW, blockH), Paint()..color = Colors.orange[700]!);

    // Reference Equilibrium Plane line
    Paint eqPaint = Paint()..color = Colors.cyan.withValues(alpha: 0.4)..strokeWidth = 1.5;
    canvas.drawLine(Offset(equilibriumX, floorY - 60.0), Offset(equilibriumX, floorY + 5.0), eqPaint);
    
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant EnergyPhysicsPainter oldDelegate) => true;
}