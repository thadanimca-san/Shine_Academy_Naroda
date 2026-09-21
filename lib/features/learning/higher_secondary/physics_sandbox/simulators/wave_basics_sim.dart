import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class WaveBasicsSimulator extends StatefulWidget {
  const WaveBasicsSimulator({Key? key}) : super(key: key);

  @override
  _WaveBasicsSimulatorState createState() => _WaveBasicsSimulatorState();
}

class _WaveBasicsSimulatorState extends State<WaveBasicsSimulator> with TickerProviderStateMixin {
  // Wave parameters
  double _amplitude = 30.0;
  double _wavelength = 120.0; // Spatial frequency tracking length (pixels)
  double _frequency = 1.5;     // Cycles per second (Hz)
  
  double _time = 0.0;
  bool _isRunning = true;
  
  // Selection states
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;

  late AnimationController _animationController;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this, initialIndex: 2); // Defaults directly to Sandbox (Tab 3)
    
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 10),
    )..addListener(() {
        if (_isRunning) {
          setState(() {
            _time += 0.03; 
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
    // Dynamic Physics Properties Calculations
    double waveVelocity = _frequency * _wavelength; 
    double angularFrequency = 2 * math.pi * _frequency;
    double waveNumber = (2 * math.pi) / _wavelength;
    double maxParticleVelocity = _amplitude * angularFrequency;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Wave Motion Basics"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.waves), text: "3. Sandbox"),
            Tab(icon: Icon(Icons.assignment), text: "4. Test Prep"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroTab(),
            _buildFormulaTab(waveVelocity, maxParticleVelocity),
            _buildSandboxTab(waveVelocity, maxParticleVelocity, waveNumber, angularFrequency),
            _buildTestPrepTab(),
          ],
        ),
      ),
    );
  }

  // --- TAB 1: INTRO (THEORETICAL CORE) ---
  Widget _buildIntroTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("WAVE MOTION & OSCILLATIONS", "NCERT Class 11 Physics | Chapter 15: Waves"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is a Mechanical Wave?",
            "A wave is a disturbance that travels through a medium, transporting energy and momentum from one point to another without transferring matter. The individual particles of the medium oscillate about their mean static positions, while the wave profile itself propagates onward.",
            Colors.deepPurple[800]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Fundamental Characteristics of Wave Motion:"), style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint(
            "Wave Speed vs. Particle Speed:", 
            "Wave speed (v) is constant for a uniform medium and represents how fast the disturbance propagates. Particle speed (v_p) varies sinusoidally over time, representing how fast an individual piece of the medium vibrates."
          ),
          _buildBulletPoint(
            "Phase Difference:", 
            "Points along the wave separated by distance x have a phase difference of Δφ = k · x. If two points are separated by exactly one wavelength (λ), they oscillate in phase with a phase difference of 2π."
          ),
          _buildBulletPoint(
            "The Envelope Factor:", 
            "A wave function y(x,t) = A sin(kx - ωt) moving to the right represents a continuous harmonic wave where k is the wave number and ω is the angular frequency."
          ),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Review Equations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULAS & WAVE KINEMATICS ---
  Widget _buildFormulaTab(double waveVelocity, double maxParticleVelocity) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL FORMULATIONS", "1D Progressive Wave Mechanics"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. General Progressive Wave Function:\n""   y(x, t) = A · sin(k·x - ω·t + φ)\n\n" 
              "2. Wave Propagation Parameters:\n" 
              "   • Wave Number (k) = 2π / λ\n" 
              "   • Angular Frequency (ω) = 2π · f\n" 
              "   • Wave Speed (v) = f · λ = ω / k\n\n" 
              "3. Medium Particle Kinematics:\n" 
              "   • Velocity (v_p) = dy / dt = -ω · A · cos(k·x - ω·t)\n" 
              "   • Maximum Particle Velocity (v_p_max) = A · ω\n" 
              "   • Differential Link: v_p = -v · (dy / dx)\n" 
              "     (Where dy/dx represents the local spatial slope)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.tealAccent, fontSize: 13, height: 1.45),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "High-Yield Phase Tip:",
            "Notice the negative sign in v_p = -v · (dy/dx). It mathematically proves that when a wave moves in the +x direction (v > 0) and the slope of the wave is positive, the medium's particle moves downwards! This relationship is crucial for tracking particle trajectory trends in JEE and NEET exams.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Sandbox Workspace ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SANDBOX WORKSPACE ---
  Widget _buildSandboxTab(double waveVelocity, double maxParticleVelocity, double waveNumber, double angularFrequency) {
    return Column(
      children: [
        // Wave Animation Box
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: Colors.grey[950],
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.deepPurple[900]!, width: 1.5),
            ),
            child: ClipRRect(
              child: LayoutBuilder(builder: (context, constraints) {
                return CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: WaveBasicsPainter(
                    time: _time,
                    amplitude: _amplitude,
                    wavelength: _wavelength,
                    frequency: _frequency,
                    waveNumber: waveNumber,
                    omega: angularFrequency,
                  ),
                );
              }),
            ),
          ),
        ),

        // Real-Time Telemetry Panels
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.deepPurple[950],
            borderRadius: BorderRadius.circular(10),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Wave Speed (v)", "${(waveVelocity / 10).toStringAsFixed(1)} m/s", Colors.purpleAccent),
              _buildTelemetry("Wave Number (k)", "${waveNumber.toStringAsFixed(3)} rad/m", Colors.amberAccent),
              _buildTelemetry("Angular Freq (ω)", "${angularFrequency.toStringAsFixed(1)} rad/s", Colors.greenAccent),
              _buildTelemetry("Max Particle Vp", "${(maxParticleVelocity / 10).toStringAsFixed(1)} m/s", Colors.cyanAccent),
            ],
          ),
        ),

        // Controls Area
        _buildControlsDrawer(),
        const SizedBox(height: 8),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 12),
          child: _buildSkipButton(3, "Practice Exam Questions ➡️"),
        ),
        const SizedBox(height: 8),
      ],
    );
  }

  // --- TAB 4: TEST PREP (EXCEPTIONAL EVALUATION) ---
  Widget _buildTestPrepTab() {
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
          _buildWaveQuiz(),
        ],
      ),
    );
  }

  // --- CORE UI ELEMENTS ---
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.deepPurple[800])),
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
        color: accentColor.withValues(alpha: 0.06), 
        borderRadius: BorderRadius.circular(8), 
        border: Border.all(color: accentColor.withValues(alpha: 0.3))
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.bold, color: accentColor, fontSize: 13)),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.deepPurple[800], fontSize: 16)),
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
        Text(value, style: TextStyle(color: valColor, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildWaveQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "A progressive wave equation is written as y = A sin(100t - 2x). What is the speed of propagation of this mechanical wave profile?"
        : "For a wave equation y = A sin(kx - ωt), at a structural point where the wave profile slope dy/dx is exactly zero, what is the value of the particle velocity?";

    List<String> options = isNeet
        ? ["50 m/s", "200 m/s", "0.02 m/s", "100 m/s"]
        : ["Maximum value", "Zero", "v_p = -v", "Cannot be determined"];

    int correctIndex = isNeet ? 0 : 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Wave Parameters:" : "JEE Differential Mechanics:", 
            style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600)),
        const SizedBox(height: 6),
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
              activeColor: Colors.deepPurple[800],
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val),
            ),
          );
        }),
        const SizedBox(height: 8),
        if (!_quizEvaluated && _selectedAnswerIndex != null)
          Padding(
            padding: const EdgeInsets.only(top: 6.0),
            child: SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () => setState(() => _quizEvaluated = true),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple[800], padding: const EdgeInsets.symmetric(vertical: 12)),
                child: Text(TrilingualService.instance.getUIText('Check Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              ),
            ),
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
                  isNeet 
                      ? "✨ PROGRESSIVE WAVE SPEED DERIVATION:\n\n"
                        "1. Compare to Standard Wave Equation:\n"
                        "   Standard form: y = A · sin(ω·t - k·x)\n"
                        "   Given form: y = A · sin(100t - 2x)\n\n"
                        "2. Match Coefficients:\n"
                        "   • Angular frequency (ω) = 100 rad/s\n"
                        "   • Wave number (k) = 2 rad/m\n\n"
                        "3. Find Wave Velocity:\n"
                        "   v = ω / k = 100 / 2 = 50 m/s.\n\n"
                        "This corresponds to the spatial rate at which the wave peaks propagate through the medium."
                      : "✨ DIFFERENTIAL TRANSFORMATION METRICS:\n\n"
                        "1. Identify the Master Wave Differential Link:\n"
                        "   v_p = -v · (dy / dx)\n"
                        "   (Where v_p is particle velocity, v is wave speed, and dy/dx is the wave slope).\n\n"
                        "2. Evaluate Point Conditions:\n"
                        "   At crests and troughs of the wave profile, the spatial displacement reaches localized maxima or minima. Consequently, the tangent slope line at these locations is perfectly flat: dy / dx = 0.\n\n"
                        "3. Compute Result:\n"
                        "   v_p = -v · (0) = 0.\n\n"
                        "This proves that particles at the extreme peaks momentarily halt before changing directions.",
                  style: TextStyle(fontSize: 12, height: 1.4, color: Theme.of(context).colorScheme.onSurface, fontFamily: 'monospace'),
                ),
              ],
            ),
          )
      ],
    );
  }

  Widget _buildControlsDrawer() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      color: Colors.white,
      child: Column(
        children: [
          Row(
            children: [
              Expanded(child: _buildSlider("Amplitude (A)", _amplitude, 10.0, 50.0, (v) => setState(() => _amplitude = v))),
              Expanded(child: _buildSlider("Wavelength (λ)", _wavelength, 60.0, 200.0, (v) => setState(() => _wavelength = v))),
            ],
          ),
          Row(
            children: [
              Expanded(child: _buildSlider("Frequency (f)", _frequency, 0.5, 3.0, (v) => setState(() => _frequency = v))),
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const SizedBox(height: 6),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        ElevatedButton(
                          onPressed: () => setState(() => _isRunning = !_isRunning),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: _isRunning ? Colors.amber[800] : Colors.green[800],
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10)
                          ),
                          child: Text(_isRunning ? "Pause Wave" : "Play Wave", style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                        ),
                        IconButton(
                          onPressed: () => setState(() { _time = 0.0; _selectedAnswerIndex = null; _quizEvaluated = false; }),
                          icon: Icon(Icons.refresh),
                          color: Colors.grey[800],
                        )
                      ],
                    ),
                  ],
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildSlider(String label, double value, double min, double max, ValueChanged<double> onChanged) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text("$label: ${value.toStringAsFixed(1)}", style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
        Slider(value: value, min: min, max: max, activeColor: Colors.deepPurple, onChanged: onChanged),
      ],
    );
  }
}

class WaveBasicsPainter extends CustomPainter {
  final double time;
  final double amplitude;
  final double wavelength;
  final double frequency;
  final double waveNumber;
  final double omega;

  WaveBasicsPainter({
    required this.time,
    required this.amplitude,
    required this.wavelength,
    required this.frequency,
    required this.waveNumber,
    required this.omega,
  });

  @override
  void paint(Canvas canvas, Size size) {
    double centerY = size.height / 2;

    // Draw reference mean rest line
    canvas.drawLine(Offset(0, centerY), Offset(size.width, centerY), Paint()..color = Colors.white12..strokeWidth = 1);

    // Render continuous medium string wave profile line
    Path wavePath = Path();
    Paint wavePaint = Paint()
      ..color = Colors.deepPurpleAccent
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3.0;

    for (double x = 0; x <= size.width; x += 2) {
      // Progressive formula vector tracking: y = A * sin(kx - wt)
      double y = centerY + amplitude * math.sin((waveNumber * x) - (omega * time));
      if (x == 0) {
        wavePath.moveTo(x, y);
      } else {
        wavePath.lineTo(x, y);
      }
    }
    canvas.drawPath(wavePath, wavePaint);

    // Draw individual highlighted particle beads along the wave string to make propagation mechanics obvious
    Paint beadPaint = Paint()..style = PaintingStyle.fill;
    
    // Distribute particle trackers adaptively along the width of the canvas
    for (double x = 40; x < size.width; x += 60) {
      double currentY = centerY + amplitude * math.sin((waveNumber * x) - (omega * time));
      
      // Compute localized velocity phase slope to pick color indicators
      double slope = waveNumber * amplitude * math.cos((waveNumber * x) - (omega * time));
      
      // Color particle green if moving up, red if moving down (using the negative phase rate)
      beadPaint.color = slope > 0 ? Colors.greenAccent : Colors.redAccent;
      
      canvas.drawCircle(Offset(x, currentY), 5.0, beadPaint);
      
      // Draw subtle motion direction path arrows overlay vectors on particle
      canvas.drawLine(
        Offset(x, currentY), 
        Offset(x, currentY - (slope * 15)), 
        Paint()..color = Colors.white..strokeWidth = 1.5
      );
    }
  }

  @override
  bool shouldRepaint(covariant WaveBasicsPainter oldDelegate) => true;
}