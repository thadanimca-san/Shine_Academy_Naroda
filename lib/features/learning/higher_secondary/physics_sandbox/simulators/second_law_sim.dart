import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class SecondLawSimulator extends StatefulWidget {
  const SecondLawSimulator({Key? key}) : super(key: key);
  @override
  _SecondLawSimulatorState createState() => _SecondLawSimulatorState();
}

class _SecondLawSimulatorState extends State<SecondLawSimulator> with TickerProviderStateMixin {
  double _mass1 = 2.0, _mass2 = 4.0, _time = 0.0; 
  bool _isAnimating = false; 
  String _targetPath = 'NEET'; 
  int? _selectedAnswerIndex; 
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;
  
  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Set to Sandbox (Tab 3) initially
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 2500))..addListener(() {
      setState(() { _time = _controller.value * 2.5; });
    });
  }
  
  void _startSimulation() { 
    setState(() { _isAnimating = true; _selectedAnswerIndex = null; _quizEvaluated = false; }); 
    _controller.reset(); 
    _controller.forward(); 
  }
  
  void _resetSimulation() { 
    setState(() { _isAnimating = false; _time = 0.0; _selectedAnswerIndex = null; _quizEvaluated = false; }); 
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
    double g = 9.8;
    double acceleration = ((_mass2 - _mass1).abs() * g) / (_mass1 + _mass2);
    double tension = (2 * _mass1 * _mass2 * g) / (_mass1 + _mass2);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Newton's 2nd Law Sandbox"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            _buildSimulationTab(acceleration, tension),
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRODUCTORY CONCEPTS ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("PULLEY DYNAMICS & CONSTRAINED MOTION", "NCERT Class 11 Physics | Laws of Motion"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Atwood's Machine?",
            "An Atwood machine consists of two unequal masses connected by an inextensible, massless string passing over a frictionless pulley. It is the classic laboratory demonstration used to study Newton's Second Law (\$F = ma\$) and the effects of gravitational acceleration under variable inertia.",
            Colors.deepPurple[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Fundamental Equations of Tension & Acceleration:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Acceleration of the System (\$a\$):", "Calculated by looking at the net pulling force divided by total system mass: \$a = \\frac{(m_2 - m_1)g}{m_1 + m_2}\$."),
          _buildBulletPoint("Inextensible Cable Tension (\$T\$):", "The upward pulling tension experienced by both masses is identical under ideal assumptions: \$T = \\frac{2m_1m_2g}{m_1 + m_2}\$."),
          _buildBulletPoint("Rotational Coupling:", "When the pulley is treated as a real object with mass \$M\$, some energy is consumed to angularly accelerate its moment of inertia, slowing the system's linear acceleration."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip to Formulas & Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: MATHEMATICAL FORMULAS & DERIVATIONS ---
  Widget _buildFormulaTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("HIGH-YIELD MATRICES & FREE BODY DIAGRAMS", "Formulas & Derivations for NEET & JEE"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Massless & Ideal Pulley FBD:\n""   • Mass 2 (Falling): m₂g - T = m₂a\n" 
              "   • Mass 1 (Rising):  T - m₁g = m₁a\n" 
              "   • Acceleration:     a = [(m₂ - m₁) / (m₁ + m₂)] * g\n" 
              "   • Tension:          T = [2m₁m₂ / (m₁ + m₂)] * g\n\n" 
              "2. Real / Massive Pulley (Rotational Inertia):\n" 
              "   • Left Tension ≠ Right Tension (T₁ ≠ T₂)\n" 
              "   • Torque equation: (T₂ - T₁) * R = I * α\n" 
              "   • Disk Pulley (I = ½MR²): \n" 
              "     a = [(m₂ - m₁) * g] / (m₁ + m₂ + M/2)\n\n" 
              "3. Force Exerted on Pulley Clamp:\n" 
              "   • Ideal Pulley Support Force: F_clamp = 2T"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.purpleAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Quick Exam Shortcut:",
            "Always treat the entire pulley string as a single linear system. The net pulling force is simply the weight difference (\$m_2g - m_1g\$), and the total inertia resisting this force is the sum of all moving components.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Test in Sandbox Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: VISUAL SIMULATION ---
  Widget _buildSimulationTab(double acceleration, double tension) {
    return Column(
      children: [
        // 1. Dynamic Interactive Painting Canvas
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(color: Colors.purple[50], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return ClipRect(
                child: CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: PulleyPhysicsPainter(
                    mass1: _mass1,
                    mass2: _mass2,
                    time: _time,
                    isAnimating: _isAnimating,
                  ),
                ),
              );
            }),
          ),
        ),

        // 2. Real-Time Telemetry Dashboard (Fixed Units!)
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(color: Colors.deepPurple[900], borderRadius: BorderRadius.circular(10)),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildTelemetry("Mass 1", "${_mass1.toStringAsFixed(1)} kg", Colors.orangeAccent),
                  _buildTelemetry("Mass 2", "${_mass2.toStringAsFixed(1)} kg", Colors.cyanAccent),
                  _buildTelemetry("Acceleration (a)", "${acceleration.toStringAsFixed(2)} m/s²", Colors.pinkAccent),
                  _buildTelemetry("Cable Tension (T)", "${tension.toStringAsFixed(1)} N", Colors.greenAccent),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                "System Velocity: ${(_isAnimating ? acceleration * _time : 0.0).toStringAsFixed(2)} m/s  |  Time: ${_time.toStringAsFixed(2)}s",
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

  // --- TAB 4: TARGETED EXAM ASSESSMENT ---
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
          _isAnimating 
              ? _buildInteractiveQuiz() 
              : Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(color: Colors.amber[50], border: Border.all(color: Colors.amber[300]!), borderRadius: BorderRadius.circular(8)),
                  child:  Row(
                    children: [
                      Icon(Icons.info_outline, color: Colors.amber),
                      SizedBox(width: 12),
                      Expanded(
                        child: Text(TrilingualService.instance.getUIText("Configure the masses on the '3. Sandbox' tab, release the pulley system, and then navigate back here to solve customized dynamic question cards!"),
                          style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
                        ),
                      ),
                    ],
                  ),
                ),
        ],
      ),
    );
  }

  // UI Construction Helper Blocks
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.deepPurple[900])),
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
          backgroundColor: Colors.deepPurple[800], 
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

  Widget _buildInteractiveQuiz() {
    bool isNeet = _targetPath == 'NEET'; 
    double g = 9.8;
    
    double acceleration = ((_mass2 - _mass1).abs() * g) / (_mass1 + _mass2);
    double tension = (2 * _mass1 * _mass2 * g) / (_mass1 + _mass2);
    double massivePulleyAcceleration = ((_mass2 - _mass1).abs() * g) / (_mass1 + _mass2 + 1.0);

    String questionText = isNeet
        ? "Calculate the tension (T) in the string supporting the masses during this motion. (Take g = 9.8 m/s²)"
        : "If the fixed pulley is suddenly replaced by a real disk-pulley of mass M = 2 kg (I = ½MR²), what will be the new linear acceleration of the blocks?";

    List<String> options = isNeet
        ? ["${(tension * 0.7).toStringAsFixed(1)} N", "${tension.toStringAsFixed(1)} N", "${(tension * 1.3).toStringAsFixed(1)} N", "${(g * _mass1).toStringAsFixed(1)} N"]
        : ["${massivePulleyAcceleration.toStringAsFixed(2)} m/s²", "${acceleration.toStringAsFixed(2)} m/s²", "${(((_mass2 - _mass1).abs() * g) / (_mass1 + _mass2 + 2.0)).toStringAsFixed(2)} m/s²", "0.00 m/s²"];

    int correctIndex = isNeet ? 1 : 0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Dynamics Problem:" : "JEE Rotational-Inertia Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600)),
        const SizedBox(height: 4),
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
              activeColor: Colors.deepPurple, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple, padding: const EdgeInsets.symmetric(vertical: 12)), 
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
                  _getDetailedExplanation(isNeet, _selectedAnswerIndex ?? 0, _mass1, _mass2, tension, acceleration, massivePulleyAcceleration),
                  style: TextStyle(fontSize: 12, height: 1.4, color: Theme.of(context).colorScheme.onSurface, fontFamily: 'monospace'),
                ),
              ],
            ),
          )
      ],
    );
  }

  String _getDetailedExplanation(bool isNeet, int selected, double m1, double m2, double T, double aIdeal, double aReal) {
    double heavy = math.max(m1, m2);
    double light = math.min(m1, m2);

    if (isNeet) {
      switch (selected) {
        case 1:
          return "✨ MASTER DERIVATION — ATWOOD FORCE MATRIX:\n\n"
                 "1. System Isolation & Free Body Diagrams (FBD):\n"
                 "   Assume m_heavy accelerates downward (-y) and m_light climbs upward (+y).\n"
                 "   • Block Heavier:  (m_heavy * g) - T = m_heavy * a\n"
                 "   • Block Lighter:  T - (m_light * g) = m_light * a\n\n"
                 "2. Eliminate Tension 'T' to find Acceleration:\n"
                 "   a = [ (m_heavy - m_light) * g ] / (m1 + m2)\n\n"
                 "3. Substitute Acceleration back to find Tension:\n"
                 "   T = (2 * m1 * m2 * g) / (m1 + m2)\n\n"
                 "4. Current Parameters:\n"
                 "   T = (2 * $m1 * $m2 * 9.8) / ($m1 + $m2) = ${T.toStringAsFixed(1)} N.";
        case 0:
          return "❌ VALUE UNDERESTIMATED:\n\n"
                 "From T = m_light * (g + a), the tension must be larger than the static resting weight of the lighter mass (m_light * g = ${(light * 9.8).toStringAsFixed(1)} N). This option is too low.";
        case 2:
          return "❌ VALUE OVERESTIMATED:\n\n"
                 "From T = m_heavy * (g - a), the tension must be smaller than the resting downward weight of the heavier mass (m_heavy * g = ${(heavy * 9.8).toStringAsFixed(1)} N). This option exceeds physical limits.";
        default:
          return "❌ STATIC MODEL FAULT:\n\n"
                 "T = m1 * g is only valid if acceleration is zero (stationary system). Since the system is actively moving, the dynamic tension is different.";
      }
    } else {
      switch (selected) {
        case 0:
          return "✨ MASTER DERIVATION — ROTATIONAL COUPLING:\n\n"
                 "1. Torque and Rotational Mechanics:\n"
                 "   τ_net = (T₂ - T₁) * R = I * α\n\n"
                 "2. Effective Rotational Mass Substitution:\n"
                 "   • Disk Pulley: I = ½ * M * R²\n"
                 "   • No-slip condition: α = a / R\n"
                 "   T₂ - T₁ = ½ * M * a\n\n"
                 "3. Combine Matrix systems:\n"
                 "   a = [ (m₂ - m₁) * g ] / (m₁ + m₂ + M/2)\n\n"
                 "4. Evaluation:\n"
                 "   With M = 2 kg, M/2 contributes an extra 1.0 kg of equivalent linear inertia:\n"
                 "   a = [ ($m2 - $m1) * 9.8 ] / ($m1 + $m2 + 1.0) = ${aReal.toStringAsFixed(2)} m/s².";
        case 1:
          return "❌ IDEAL ASSUMPTION TRAP:\n\n"
                 "This option represents an ideal pulley with zero mass (a = ${aIdeal.toStringAsFixed(2)} m/s²). A massive pulley slows linear acceleration because energy is spent accelerating it rotationally.";
        case 2:
          return "❌ INERTIA MATRIX ADDITION FAULT:\n\n"
                 "Do not add the bulk pulley mass 'M' directly to the denominator. Because the pulley rotates instead of sliding, its rotational distribution reduces its effective linear resistance to M/2.";
        default:
          return "❌ FORCE EQUILIBRIUM ERROR:\n\n"
                 "The system will only lock at zero acceleration if m1 = m2. Since a mass difference exists, gravity overcomes the pulley's inertia and causes motion.";
      }
    }
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(12), color: Colors.white,
      child: Column(children: [
        Row(children: [
          Expanded(child: Column(children: [Text('m1: ${_mass1.toStringAsFixed(0)} kg', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)), Slider(value: _mass1, min: 1, max: 8, divisions: 7, activeColor: Colors.deepPurpleAccent, onChanged: _isAnimating ? null : (val) => setState(() => _mass1 = val))])),
          Expanded(child: Column(children: [Text('m2: ${_mass2.toStringAsFixed(0)} kg', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)), Slider(value: _mass2, min: 1, max: 8, divisions: 7, activeColor: Colors.purple, onChanged: _isAnimating ? null : (val) => setState(() => _mass2 = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton(
            onPressed: _isAnimating ? null : _startSimulation, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700]), 
            child: Text(TrilingualService.instance.getUIText('Release System'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ), 
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.deepPurple))
        ]),
      ]),
    );
  }
}

class PulleyPhysicsPainter extends CustomPainter {
  final double mass1, mass2, time; 
  final bool isAnimating;

  PulleyPhysicsPainter({
    required this.mass1, 
    required this.mass2, 
    required this.time, 
    required this.isAnimating, 
  });
  
  @override
  void paint(Canvas canvas, Size size) {
    double cx = size.width / 2;
    double cy = size.height * 0.25; 
    
    // Calculate dynamic pulley radius based on viewport size to prevent clipping
    double rad = math.min(size.width, size.height) * 0.12; 
    
    // Draw Ceiling Mount Anchor Support
    canvas.drawLine(Offset(cx, 0), Offset(cx, cy), Paint()..color = Colors.grey[700]!..strokeWidth = 4.0);
    
    // Calculate magnitude of acceleration using absolute mass difference
    double netMassDifference = (mass2 - mass1).abs();
    double acceleration = (netMassDifference * 9.8) / (mass1 + mass2);
    
    // Base displacement on true scalar movement magnitude
    double dispMag = isAnimating ? 0.5 * acceleration * math.pow(time, 2) * 12.0 : 0.0;
    
    // Safe boundary limit calculation so weights never drop below the visual boundary
    double maxDisp = (size.height - cy - rad - 50.0);
    dispMag = dispMag.clamp(0.0, maxDisp);

    // Apply explicit directions depending on which mass dominates
    double m1DispDirection = (mass1 >= mass2) ? dispMag : -dispMag; 
    double m2DispDirection = (mass2 >= mass1) ? dispMag : -dispMag; 

    Paint stringPaint = Paint()..strokeWidth = 2.0..color = Colors.black87;
    double restingStringLength = size.height * 0.45; 
    
    // Draw Left and Right Strings
    canvas.drawLine(Offset(cx - rad, cy), Offset(cx - rad, cy + restingStringLength + m1DispDirection), stringPaint);
    canvas.drawLine(Offset(cx + rad, cy), Offset(cx + rad, cy + restingStringLength + m2DispDirection), stringPaint);
    
    // Draw Central Pulley Disk Structure
    canvas.drawCircle(Offset(cx, cy), rad, Paint()..color = Colors.blueGrey[400]!..style = PaintingStyle.fill);
    canvas.drawCircle(Offset(cx, cy), rad, Paint()..color = Colors.blueGrey[800]!..style = PaintingStyle.stroke..strokeWidth = 3.0);
    canvas.drawCircle(Offset(cx, cy), 5, Paint()..color = Colors.white);
    
    // Proportional physical sizes for hanging weight blocks
    double m1SideLength = 18.0 + (mass1 * 3.0);
    double m2SideLength = 18.0 + (mass2 * 3.0);

    // Draw Mass 1 Block
    canvas.drawRect(
      Rect.fromLTWH(cx - rad - (m1SideLength / 2), cy + restingStringLength + m1DispDirection, m1SideLength, m1SideLength), 
      Paint()..color = Colors.deepPurpleAccent
    );
    // Draw Mass 2 Block
    canvas.drawRect(
      Rect.fromLTWH(cx + rad - (m2SideLength / 2), cy + restingStringLength + m2DispDirection, m2SideLength, m2SideLength), 
      Paint()..color = Colors.purple
    );
  }
  
  @override
  bool shouldRepaint(covariant PulleyPhysicsPainter oldDelegate) => true;
}