import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ShmDuelSimulator extends StatefulWidget {
  const ShmDuelSimulator({Key? key}) : super(key: key);

  @override
  _ShmDuelSimulatorState createState() => _ShmDuelSimulatorState();
}

class _ShmDuelSimulatorState extends State<ShmDuelSimulator> with TickerProviderStateMixin {
  // Shared & Specific Variables
  double _mass = 2.0;       // m (kg) - affects Spring, NOT Pendulum
  double _stiffness = 8.0;  // k (N/m) - affects Spring only
  double _length = 1.5;     // L (meters) - affects Pendulum only
  double _gravity = 9.81;   // g (m/s²) - affects Pendulum, NOT Spring

  double _time = 0.0;
  bool _isRunning = true;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late AnimationController _animationController;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Start directly on Sandbox (Tab 3)
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 10),
    )..addListener(() {
        if (_isRunning) {
          setState(() {
            _time += 0.04; // Simulation step clock
          });
        }
      });
    _animationController.repeat();
  }

  @override
  void dispose() {
    _animationController.dispose();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Exact Physics Equations
    double omegaSpring = math.sqrt(_stiffness / _mass);
    double periodSpring = (2 * math.pi) / omegaSpring;

    double omegaPendulum = math.sqrt(_gravity / _length);
    double periodPendulum = (2 * math.pi) / omegaPendulum;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("SHM Mechanics Duel"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            _buildSimulationTab(omegaSpring, periodSpring, omegaPendulum, periodPendulum),
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
          _buildChapterHeader("SIMPLE HARMONIC MOTION (SHM) COMPENDIUM", "NCERT Class 11 Physics | Oscillations"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Simple Harmonic Motion?",
            "SHM is a highly specific periodic motion where the restoring force is directly proportional to the displacement from equilibrium and acts in the opposite direction: \$F = -kx\$. This duel visualizes the differences between stiffness-based and gravity-based restoration.",
            Colors.teal[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Restoring Forces Contrasted:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Spring-Mass System:", "Restoration is strictly mechanical, governed by Hooke's Law (\$F = -kx\$). The angular frequency depends solely on the mass and spring stiffness: \$\\omega = \\sqrt{k/m}\$."),
          _buildBulletPoint("Simple Pendulum System:", "Restoration is gravitational, driven by the tangential component of gravity (\$F = -mg \\sin\\theta\$). Under a small angle approximation (\$\\sin\\theta \\approx \\theta\$), its restoring frequency is independent of the bob mass: \$\\omega = \\sqrt{g/L}\$."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "View Formulas & Derivations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULAS ---
  Widget _buildFormulaTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL FORMULATIONS", "High-Yield Entrance Relations"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Mass-Spring System Dynamics:\n""   • Restoring Force:   F = -kx\n" 
              "   • Angular Frequency: ω = √(k/m)\n" 
              "   • Time Period:       T = 2π √(m/k)\n\n" 
              "2. Simple Pendulum Dynamics:\n" 
              "   • Restoring Torque:  τ = -mgL sin(θ) ≈ -mgLθ\n" 
              "   • Angular Frequency: ω = √(g/L)\n" 
              "   • Time Period:       T = 2π √(L/g)\n\n" 
              "3. Energy Relations in SHM:\n" 
              "   • Total Energy:      E = ½ k A² = ½ m ω² A²"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "Crucial Exam Trap:",
            "Notice that Pendulum equations contain NO mass variable (\$m\$), and Spring equations contain NO local gravitational acceleration variable (\$g\$). Altering local gravity changes ONLY the pendulum's rhythm!",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Test in Sandbox Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION ---
  Widget _buildSimulationTab(double omegaSpring, double periodSpring, double omegaPendulum, double periodPendulum) {
    return Column(
      children: [
        // Dual Visual Canvas Panel
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: Colors.grey[900],
              borderRadius: BorderRadius.circular(12),
            ),
            child: LayoutBuilder(builder: (context, constraints) {
              return ClipRect(
                child: CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: ShmDuelPainter(
                    time: _time,
                    omegaSpring: omegaSpring,
                    omegaPendulum: omegaPendulum,
                  ),
                ),
              );
            }),
          ),
        ),

        // Real-time Telemetry Readouts (Fixed Units!)
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.teal[950],
            borderRadius: BorderRadius.circular(10),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Spring Period (T_s)", "${periodSpring.toStringAsFixed(2)} s", Colors.orangeAccent),
              _buildTelemetry("Pendulum Period (T_p)", "${periodPendulum.toStringAsFixed(2)} s", Colors.cyanAccent),
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

  // --- TAB 4: TEST PREP ---
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
                  Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Challenge'), style: TextStyle(fontWeight: FontWeight.bold))),
                ],
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildQuizView(),
        ],
      ),
    );
  }

  // --- UI CONSTRUCTION BLOCKS ---
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
        Text(value, style: TextStyle(color: valColor, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildQuizView() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "If the entire dual-oscillator laboratory setup is transported to the Moon, where gravitational acceleration drops to g/6, how will the time periods change?"
        : "A simple pendulum has a time period T on Earth. If the mass of its bob is doubled, and its string length is cut to one-fourth (L/4), what is its new time period?";

    List<String> options = isNeet
        ? ["Both periods increase", "Spring period remains identical; Pendulum period increases", "Pendulum period stays identical; Spring period decreases", "Both periods decrease"]
        : ["T' = T", "T' = T / 2", "T' = 2T", "T' = T / \u221A2"];

    int correctIndex = isNeet ? 1 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Dependences Check:" : "JEE Mixed Scaling Parameters:", 
            style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600)),
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
              activeColor: Colors.teal[800],
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val),
            ),
          );
        }),
        const SizedBox(height: 8),
        if (!_quizEvaluated && _selectedAnswerIndex != null)
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: () => setState(() => _quizEvaluated = true),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[800], padding: const EdgeInsets.symmetric(vertical: 12)),
              child: Text(TrilingualService.instance.getUIText('Verify Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
            ),
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red),
            ),
            child: Text(
              _selectedAnswerIndex == correctIndex
                  ? (isNeet 
                      ? "✅ Correct! 🎉\n\nFor a spring system, T_s = 2π√(m/k), which is independent of local gravity. For a simple pendulum, T_p = 2π√(L/g). Lowering gravity decreases the denominator, extending the oscillation swing period!"
                      : "✅ Correct! 🎉\n\nThe mass of a pendulum bob does not affect its periodic rate of oscillation because mass cancels out completely in the restoration acceleration equation: a = -gθ. Reducing the cable length to one-fourth (L/4) updates the period to: T' = 2π√(L / 4g) = ½ T.")
                  : (isNeet
                      ? "❌ Dependence Error:\n\nReview the governing variables: spring period relies entirely on stiffness and inertial mass. Gravity only dictates the restorative acceleration of free-swinging pendulums."
                      : "❌ Scaling Error:\n\nRemember that pendulum mass does not matter! Focus purely on the square-root of the length ratio: √((L/4) / L) = √(1/4) = 1/2."),
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
            children: [
              Expanded(child: _buildSlider("Mass (m)", _mass, 0.5, 4.0, (v) => setState(() => _mass = v))),
              Expanded(child: _buildSlider("Stiffness (k)", _stiffness, 3.0, 15.0, (v) => setState(() => _stiffness = v))),
            ],
          ),
          Row(
            children: [
              Expanded(child: _buildSlider("Length (L)", _length, 0.5, 2.5, (v) => setState(() => _length = v))),
              Expanded(child: _buildSlider("Gravity (g)", _gravity, 1.0, 20.0, (v) => setState(() => _gravity = v))),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton(
                onPressed: () => setState(() => _isRunning = !_isRunning),
                style: ElevatedButton.styleFrom(backgroundColor: _isRunning ? Colors.amber[800] : Colors.green[800]),
                child: Text(_isRunning ? "Pause System" : "Run System", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              ),
              ElevatedButton(
                onPressed: () => setState(() { _time = 0.0; _selectedAnswerIndex = null; _quizEvaluated = false; }),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.grey[700]),
                child: Text(TrilingualService.instance.getUIText("Reset Nodes"), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              )
            ],
          )
        ],
      ),
    );
  }

  Widget _buildSlider(String label, double value, double min, double max, ValueChanged<double> onChanged) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text("$label: ${value.toStringAsFixed(1)}", style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
        Slider(value: value, min: min, max: max, activeColor: Colors.teal, onChanged: onChanged),
      ],
    );
  }
}

class ShmDuelPainter extends CustomPainter {
  final double time;
  final double omegaSpring;
  final double omegaPendulum;

  ShmDuelPainter({required this.time, required this.omegaSpring, required this.omegaPendulum});

  @override
  void paint(Canvas canvas, Size size) {
    double midX = size.width / 2;
    double leftCenter = size.width * 0.25;
    double rightCenter = size.width * 0.75;
    double baselineY = 40.0;

    // Center divider paint
    canvas.drawLine(Offset(midX, 10), Offset(midX, size.height - 10), Paint()..color = Colors.white12..strokeWidth = 1);

    // Dynamic scale helper to avoid out-of-bounds painting on multiple screen resolutions
    double visualScaleFactor = math.min(size.width, size.height) / 400.0;

    // --- LEFT SIDE: SPRING WORKBENCH ---
    double springAmplitude = 35.0 * visualScaleFactor;
    double springDisplacement = springAmplitude * math.sin(omegaSpring * time);
    double springBobY = baselineY + (80.0 * visualScaleFactor) + springDisplacement;

    // Draw Anchor Roof line
    canvas.drawLine(Offset(leftCenter - 30, baselineY), Offset(leftCenter + 30, baselineY), Paint()..color = Colors.white..strokeWidth = 3);
    
    // Draw Spring Coils
    Path springPath = Path()..moveTo(leftCenter, baselineY);
    int coils = 12;
    double sliceHeight = (springBobY - baselineY) / coils;
    for (int i = 0; i <= coils; i++) {
      double y = baselineY + (i * sliceHeight);
      double x = leftCenter + (i == 0 || i == coils ? 0 : (i % 2 == 0 ? 12 * visualScaleFactor : -12 * visualScaleFactor));
      springPath.lineTo(x, y);
    }
    canvas.drawPath(springPath, Paint()..color = Colors.orangeAccent..style = PaintingStyle.stroke..strokeWidth = 2);
    // Draw Mass Bob
    canvas.drawCircle(Offset(leftCenter, springBobY), 14, Paint()..color = Colors.orange);

    // --- RIGHT SIDE: PENDULUM WORKBENCH ---
    double maxAngle = 0.45; // Swing amplitude boundary condition
    double angle = maxAngle * math.sin(omegaPendulum * time);
    double stringLengthPixels = 120.0 * visualScaleFactor;

    double bobX = rightCenter + stringLengthPixels * math.sin(angle);
    double bobY = baselineY + stringLengthPixels * math.cos(angle);

    // Draw Anchor Roof line
    canvas.drawLine(Offset(rightCenter - 30, baselineY), Offset(rightCenter + 30, baselineY), Paint()..color = Colors.white..strokeWidth = 3);
    // Draw Suspension String line
    canvas.drawLine(Offset(rightCenter, baselineY), Offset(bobX, bobY), Paint()..color = Colors.cyanAccent..strokeWidth = 1.5);
    // Draw Pendulum Bob Node
    canvas.drawCircle(Offset(bobX, bobY), 12, Paint()..color = Colors.cyan);
  }

  @override
  bool shouldRepaint(covariant ShmDuelPainter oldDelegate) => true;
}