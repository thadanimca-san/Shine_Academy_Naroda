import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class OscillationsWavesSimulator extends StatefulWidget {
  const OscillationsWavesSimulator({Key? key}) : super(key: key);

  @override
  _OscillationsWavesSimulatorState createState() => _OscillationsWavesSimulatorState();
}

class _OscillationsWavesSimulatorState extends State<OscillationsWavesSimulator> with TickerProviderStateMixin {
  // Physical Input Parameters
  double _mass = 2.0;       // m (kg)
  double _stiffness = 5.0;  // k (N/m)
  double _amplitude = 30.0; // A (Scalar pixels)
  
  double _time = 0.0;
  bool _isOscillating = true;
  
  late AnimationController _animationController;
  late TabController _tabController;
  final List<double> _waveHistory = [];

  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    
    // Safety Lifecycle Catch: Freeze oscillation threads when user leaves the simulator screen view
    _tabController.addListener(() {
      if (!_tabController.indexIsChanging) {
        if (_tabController.index != 2) {
          if (_isOscillating) {
            setState(() => _isOscillating = false);
            _animationController.stop();
          }
        }
      }
    });

    _animationController = AnimationController(vsync: this, duration: const Duration(seconds: 10))..addListener(() {
      if (_isOscillating) {
        setState(() {
          _time += 0.05;
          double omega = math.sqrt(_stiffness / _mass);
          double currentY = _amplitude * math.sin(omega * _time);
          
          _waveHistory.insert(0, currentY);
          if (_waveHistory.length > 250) {
            _waveHistory.removeLast();
          }
        });
      }
    });
    
    if (_isOscillating) {
      _animationController.repeat();
    }
  }

  void _toggleSimulation() {
    setState(() { 
      _isOscillating = !_isOscillating; 
      if (_isOscillating) {
        _animationController.repeat();
      } else {
        _animationController.stop();
      }
    });
  }

  void _resetSimulation() {
    setState(() {
      _time = 0.0;
      _waveHistory.clear();
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
  }

  @override
  void dispose() {
    _animationController.dispose();
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double omega = math.sqrt(_stiffness / _mass);
    double timePeriod = (2.0 * math.pi) / omega;
    double frequency = 1.0 / timePeriod;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Oscillations & Waves Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.waves), text: "3. Simulation"),
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
            _buildSimulationTab(omega, timePeriod, frequency),
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
          _buildChapterHeader("SIMPLE HARMONIC MOTION & WAVEPROPAGATION", "NCERT Class 11 / JEE-NEET High Yield Syllabus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Simple Harmonic Motion (SHM)?",
            "SHM is a highly specific type of periodic baseline structural motion where the restoring force acting on an oscillating object is directly proportional to its displacement from its mean equilibrium position, acting in a direction opposite to it.",
            Colors.cyan[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Essential Core Postulates:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("The Restoring Law:", "Expressed linearly as F = -k·x, where k indicates spring stiffness, and x equals systemic linear displacement values."),
          _buildBulletPoint("Energy Conservation Parameters:", "Energy seamlessly cycles between maximum Kinetic Energy at the mean spatial center position and maximum Potential Energy at maximum amplitude boundaries."),
          _buildBulletPoint("Wave Trace Projections:", "Plotting individual point spatial displacements against time traces an exact sinusoidal wave profile down an ongoing linear vector axis."),
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
          _buildChapterHeader("THE DIFFERENTIAL EQUATION METHOD", "Rigorous Mechanical Derivations"),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Equation of Hooke's Forces Law:\n""   F = -k · x\n" 
              "   m · (d²x / dt²) + k · x = 0\n\n" 
              "2. Defining Angular Frequency Parameter (ω):\n" 
              "   d²x / dt² + (k / m) · x = 0\n" 
              "   Let ω² = k / m  =>  ω = √(k / m)\n\n" 
              "3. Systemic Time Period Evaluation (T):\n" 
              "   T = 2·π / ω  =>  T = 2·π · √(m / k)\n\n" 
              "4. Sinusoidal Position Trajectory Output:\n" 
              "   x(t) = A · sin(ω·t + φ)\n" 
              "   v(t) = dx/dt = A·ω · cos(ω·t + φ)\n" 
              "   a(t) = dv/dt = -A·ω² · sin(ω·t + φ)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE-NEET Problem Solving Insight:",
            "Spring structural combinations scale parameters directly! \n"
            "• Parallel configuration setup: k_eq = k1 + k2\n"
            "• Series configuration setup: 1/k_eq = 1/k1 + 1/k2",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Real-Time Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double omega, double timePeriod, double frequency) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.cyan[50],
          child: Text(
            _isOscillating ? "🟢 Mechanical Drive: Tracking Sinusoidal Wave Train" : "🛑 Engine Paused: Parameters Locked in Place",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.cyan[900]),
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[900], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: WaveMachinePainter(
                  waveHistory: _waveHistory,
                  amplitude: _amplitude,
                  stiffness: _stiffness,
                  mass: _mass,
                  time: _time,
                ),
              );
            }),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.cyan[950], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Angular Freq (ω)", "${omega.toStringAsFixed(2)} rad/s", Colors.cyanAccent),
              _buildTelemetry("Time Period (T)", "${timePeriod.toStringAsFixed(2)} s", Colors.amberAccent),
              _buildTelemetry("Frequency (f)", "${frequency.toStringAsFixed(2)} Hz", Colors.white),
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
          _buildOscillationQuiz(),
        ],
      ),
    );
  }

  // UI Construction Helper Elements
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.cyan[900])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.cyan[900], fontSize: 16)),
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
        style: TextButton.styleFrom(backgroundColor: Colors.blueGrey[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
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

  Widget _buildOscillationQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "If you keep the spring stiffness constant but load 4 times more mass onto the hanger, what happens to the systemic Time Period (T) of the oscillation?"
        : "A spring-mass system oscillates with an angular frequency ω. If the spring is cut precisely into two equal halves and connected in parallel to the same mass, what is the new angular frequency?";

    List<String> options = isNeet
        ? ["T becomes doubled", "T is halved", "T increases 4 times", "T drops to zero"]
        : ["ω' = ω", "ω' = √2 ω", "ω' = 2 ω", "ω' = 4 ω"];

    int correctIndex = isNeet ? 0 : 2;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET SHM Formula Proportions:" : "JEE Compound Spring Scaling:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.cyan[900], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.cyan[900], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Harmonic Parameters'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "Correct! 🎉 Time period follows T = 2π√(m/k). Because mass sits inside a square root directly on the numerator, making mass 4x greater increases the overall time period by √4 = 2 times."
                    : "Correct! 🎉 Cutting a spring in half doubles the spring constant of each piece (2k). Connecting two such identical springs in a parallel layout sums their values together (k_eq = 2k + 2k = 4k). Since ω = √(k/m), scaling stiffness by 4 increases angular frequency by √4 = 2ω.")
                : (isNeet 
                    ? "Incorrect ❌ Look back at the period ratio. Mass is on the numerator inside a radical symbol: T ∝ √m."
                    : "Incorrect ❌ Think about spring cutting laws! Cutting a spring increases individual stiffness because length decreases. Then adding them in parallel increases total stiffness further."),
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
          Expanded(child: Column(children: [Text('Mass (m): ${_mass.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _mass, min: 0.5, max: 5.0, divisions: 9, activeColor: Colors.cyan[700], onChanged: (val) => setState(() => _mass = val))])),
          Expanded(child: Column(children: [Text('Stiffness (k): ${_stiffness.toStringAsFixed(1)} N/m', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _stiffness, min: 2.0, max: 12.0, divisions: 10, activeColor: Colors.teal, onChanged: (val) => setState(() => _stiffness = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _toggleSimulation, 
            style: ElevatedButton.styleFrom(backgroundColor: _isOscillating ? Colors.orange[800] : Colors.green[800], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(_isOscillating ? Icons.pause : Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(_isOscillating ? 'Pause Motion' : 'Resume Motion', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class WaveMachinePainter extends CustomPainter {
  final List<double> waveHistory;
  final double amplitude;
  final double stiffness;
  final double mass;
  final double time;

  WaveMachinePainter({
    required this.waveHistory,
    required this.amplitude,
    required this.stiffness,
    required this.mass,
    required this.time,
  });

  @override
  void paint(Canvas canvas, Size size) {
    double centerY = size.height / 2.0;
    double oscillatorX = 60.0; 

    double omega = math.sqrt(stiffness / mass);
    double currentDisplacement = waveHistory.isNotEmpty ? waveHistory.first : amplitude * math.sin(omega * time);
    double activeBobY = centerY + currentDisplacement;

    // Draw reference mean position line
    canvas.drawLine(Offset(oscillatorX, centerY), Offset(size.width, centerY), Paint()..color = Colors.white10..strokeWidth = 1.0);

    // Spring Painting Logic
    Paint springPaint = Paint()..color = Colors.white54..strokeWidth = 2.0..style = PaintingStyle.stroke;
    Path springPath = Path();
    springPath.moveTo(oscillatorX, 10.0); 
    
    int coilsCount = 12;
    double springSliceHeight = (activeBobY - 10.0) / coilsCount;
    for (int i = 0; i <= coilsCount; i++) {
      double currentSliceY = 10.0 + (i * springSliceHeight);
      double currentSliceX = oscillatorX + (i % 2 == 0 ? 12.0 : -12.0);
      if (i == 0 || i == coilsCount) currentSliceX = oscillatorX; 
      springPath.lineTo(currentSliceX, currentSliceY);
    }
    canvas.drawPath(springPath, springPaint);

    // Draw Mass Block
    Paint blockPaint = Paint()..color = Colors.cyanAccent..style = PaintingStyle.fill;
    canvas.drawRect(Rect.fromCenter(center: Offset(oscillatorX, activeBobY), width: 24.0, height: 16.0), blockPaint);

    // Sinusoidal Wave Trace History Pipeline
    if (waveHistory.isNotEmpty) {
      Paint waveLinePaint = Paint()..color = Colors.tealAccent..strokeWidth = 2.5..style = PaintingStyle.stroke;
      Path wavePath = Path();
      wavePath.moveTo(oscillatorX, activeBobY);

      double spacingDeltaX = (size.width - oscillatorX) / 200.0; 

      for (int i = 0; i < waveHistory.length; i++) {
        double ptX = oscillatorX + (i * spacingDeltaX);
        double ptY = centerY + waveHistory[i];
        if (ptX <= size.width) {
          wavePath.lineTo(ptX, ptY);
        }
      }
      canvas.drawPath(wavePath, waveLinePaint);
      
      // Decorative Wave Carrier Beads
      Paint beadPaint = Paint()..color = Colors.amberAccent..style = PaintingStyle.fill;
      for (int i = 10; i < waveHistory.length; i += 25) {
        double ptX = oscillatorX + (i * spacingDeltaX);
        if (ptX <= size.width) {
          canvas.drawCircle(Offset(ptX, centerY + waveHistory[i]), 3.0, beadPaint);
        }
      }
    }
  }

  @override
  bool shouldRepaint(covariant WaveMachinePainter oldDelegate) => true;
}