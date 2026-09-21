import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class StandingWavesSimulator extends StatefulWidget {
  const StandingWavesSimulator({Key? key}) : super(key: key);

  @override
  _StandingWavesSimulatorState createState() => _StandingWavesSimulatorState();
}

class _StandingWavesSimulatorState extends State<StandingWavesSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _frequency = 2.0;          // Frequency of driving wave (Hz)
  double _amplitude = 20.0;         // Amplitude of component waves (px)
  int _harmonicMode = 3;            // Harmonic number (n = 1, 2, 3, 4)
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
        _time = _controller.value * 4.0 * _frequency;
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
    double length = 300.0; 
    double wavelength = (2.0 * length) / _harmonicMode;
    double wavenumberK = (2.0 * math.pi) / wavelength;
    double angularFreqOmega = 2.0 * math.pi * _frequency;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Standing Waves Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            _buildSimulationTab(wavelength, wavenumberK, angularFreqOmega),
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
          _buildChapterHeader("SUPERPOSITION & STANDING WAVES", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is a Standing Wave?",
            "A standing wave (stationary wave) is formed by the superposition of two identical wave trains traveling in opposite directions through a medium. Unlike progressive waves, standing waves do not transfer net energy through space—energy remains trapped dynamically between fixed positions.",
            Palette.primaryDeep ?? Palette.primary
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Components:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Nodes (N):", "Coordinates where the string particles experience zero net displacement at all instances. Spaced by a distance of λ/2."),
          _buildBulletPoint("Antinodes (A):", "Coordinates where particles experience maximum oscillation displacement. Spaced exactly halfway between adjacent nodes."),
          _buildBulletPoint("Boundary Conditions:", "For strings fixed at both ends, the boundaries must strictly form displacement nodes, leading to localized discrete resonant frequencies called harmonics."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "Rigorous Wave Function Superposition"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Forward Travelling Wave:\n""   y1 = A · sin(k·x - ω·t)\n\n" 
              "2. Reflected Travelling Wave:\n" 
              "   y2 = -A · sin(k·x + ω·t)  [180° phase flip at wall]\n\n" 
              "3. By Principle of Superposition:\n" 
              "   y_net = y1 + y2\n" 
              "   y_net = A [sin(k·x - ω·t) - sin(k·x + ω·t)]\n\n" 
              "4. Applying Trigonometric Identity:\n" 
              "   y_net = [2A · sin(k·x)] · cos(ω·t)\n\n" 
              "5. Boundary Conditions at x = L:\n" 
              "   sin(k·L) = 0  =>  k·L = n·π\n" 
              "   Resonant Wavelengths: λ = 2L / n  (where n = 1, 2, 3...)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.cyanAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "Notice how the wave function spatial parameters (x) and temporal parameters (t) are completely separated.\n\n"
            "This configuration means all particles in the medium pass through their equilibrium positions simultaneously with different amplitude levels, depending on their position along the path.",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION GRAPH VIEW ---
  Widget _buildSimulationTab(double wavelength, double wavenumberK, double angularFreqOmega) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Palette.primarySoft,
          child: Text(
            _isOscillating ? "🟢 Wave Interference: Dynamic Resonant Superposition Active" : "🛑 Wave State Primed: Select Harmonic Parameters & Click Release",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Palette.primaryDeep),
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: StandingWavesPainter(
                  amplitude: _amplitude,
                  harmonicMode: _harmonicMode,
                  time: _isOscillating ? _time : 0.0,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Palette.primaryDeep, borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Harmonic (n)", "$_harmonicMode"),
              _buildTelemetry("Wavelength", "${wavelength.toStringAsFixed(1)} px"),
              _buildTelemetry("Nodes", "${_harmonicMode + 1}"),
              _buildTelemetry("Antinodes", "$_harmonicMode"),
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
              fillColor: _targetPath == 'NEET' ? (Colors.green[600] ?? Colors.green) : Colors.deepOrange,
              children: [
                Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('NEET Rank Booster'), style: TextStyle(fontWeight: FontWeight.bold))), 
                Padding(padding: EdgeInsets.symmetric(horizontal: 24), child: Text(TrilingualService.instance.getUIText('JEE Advanced Challenge'), style: TextStyle(fontWeight: FontWeight.bold)))
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

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label.toUpperCase(), style: TextStyle(color: Colors.cyanAccent, fontSize: 9, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 2),
        Text(value, style: TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildWaveQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "A string of length L fixed at both ends oscillates in its 3rd harmonic mode. What is the separation distance between a consecutive node and an adjacent antinode?"
        : "If the tension in a fixed-ended string is quadrupled while keeping driving frequency fixed, what structural modification happens to the number of nodes observed inside a set length space L?";

    List<String> options = isNeet
        ? ["L / 3", "L / 6", "L / 4", "2L / 3"]
        : ["Nodes value increases by 2x", "Nodes count drops down by half", "System defaults to pure progressive mechanics", "No modification can trigger"];

    int correctIndex = 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Vector Spacings Quiz:" : "JEE Advanced Resonant Boundary Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? (Colors.green[700] ?? Colors.green) : Colors.deepOrange, fontSize: 14)),
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
              child: Text(TrilingualService.instance.getUIText('Verify Boundary Conditions Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT BOUNDARY SPACING:\n\nFor the 3rd harmonic, length L = 3(λ/2), which means λ = 2L/3. The distance between a consecutive node and antinode is exactly λ/4. Substituting λ gives: (2L/3) / 4 = L / 6."
                    : "✅ CORRECT VELOCITY RELATION:\n\nWave velocity scales with tension: v = √(T/μ). Quadrupling tension doubles the speed (2v). Since v = f·λ and frequency is fixed, λ doubles. To fit inside length L, the harmonic count must drop by half.")
                : "❌ MATHEMATICAL MISALIGNMENT:\n\nReview the Derivation Tab! Check the boundary criteria equations for string loops (\$L = n\lambda/2\$) and recalculate node/antinode distance vectors (\$d = \lambda/4\$).",
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
          Expanded(child: Column(children: [Text('Frequency: ${_frequency.toStringAsFixed(1)} Hz', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _frequency, min: 1.0, max: 4.0, divisions: 3, activeColor: Palette.primary, onChanged: _isOscillating ? null : (val) => setState(() => _frequency = val))])),
          Expanded(child: Column(children: [Text('Amplitude: ${_amplitude.toStringAsFixed(0)} px', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _amplitude, min: 10, max: 40, divisions: 3, activeColor: Colors.cyan, onChanged: _isOscillating ? null : (val) => setState(() => _amplitude = val))])),
          Expanded(child: Column(children: [Text('Harmonic mode (n): $_harmonicMode', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _harmonicMode.toDouble(), min: 1, max: 5, divisions: 4, activeColor: Colors.deepPurple, onChanged: _isOscillating ? null : (val) => setState(() => _harmonicMode = val.toInt()))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isOscillating ? null : _releaseSystem, 
            style: ElevatedButton.styleFrom(backgroundColor: Palette.primaryDeep, padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('Excite Medium'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class StandingWavesPainter extends CustomPainter {
  final double amplitude, time, scaleRatio;
  final int harmonicMode;
  StandingWavesPainter({required this.amplitude, required this.harmonicMode, required this.time, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double centerY = canvasHeight / 2.0;
    double startX = 50.0;
    double endX = canvasWidth - 50.0;
    double totalLength = endX - startX;

    Paint pillarPaint = Paint()..color = (Colors.blueGrey[700] ?? Colors.blueGrey)..strokeWidth = 6.0;
    canvas.drawLine(Offset(startX, centerY - 60), Offset(startX, centerY + 60), pillarPaint);
    canvas.drawLine(Offset(endX, centerY - 60), Offset(endX, centerY + 60), pillarPaint);

    Path primaryWavePath = Path();
    Path structuralEnvelopeTop = Path();
    Path structuralEnvelopeBottom = Path();

    primaryWavePath.moveTo(startX, centerY);
    structuralEnvelopeTop.moveTo(startX, centerY);
    structuralEnvelopeBottom.moveTo(startX, centerY);

    for (double x = 0; x <= totalLength; x += 2.0) {
      double currentCanvasX = startX + x;
      double spatialFactor = math.sin((harmonicMode * math.pi * x) / totalLength);
      double dynamicY = centerY + (2.0 * amplitude * spatialFactor * math.cos(time));
      
      double envelopeTopY = centerY + (2.0 * amplitude * spatialFactor);
      double envelopeBottomY = centerY - (2.0 * amplitude * spatialFactor);

      primaryWavePath.lineTo(currentCanvasX, dynamicY);
      structuralEnvelopeTop.lineTo(currentCanvasX, envelopeTopY);
      structuralEnvelopeBottom.lineTo(currentCanvasX, envelopeBottomY);
    }

    Paint envelopePaint = Paint()
      ..color = Colors.cyan.withValues(alpha: 0.25)
      ..strokeWidth = 1.5
      ..style = PaintingStyle.stroke;
    canvas.drawPath(structuralEnvelopeTop, envelopePaint);
    canvas.drawPath(structuralEnvelopeBottom, envelopePaint);

    Paint stringPaint = Paint()
      ..color = Colors.cyanAccent
      ..strokeWidth = 3.0
      ..style = PaintingStyle.stroke;
    canvas.drawPath(primaryWavePath, stringPaint);

    Paint pointPaint = Paint()..style = PaintingStyle.fill;
    for (int i = 0; i <= harmonicMode; i++) {
      double nodeX = startX + (i * totalLength / harmonicMode);
      canvas.drawCircle(Offset(nodeX, centerY), 4.0, pointPaint..color = Colors.redAccent);
      
      if (i < harmonicMode) {
        double antinodeX = startX + ((i + 0.5) * totalLength / harmonicMode);
        double spatialFactor = math.sin((harmonicMode * math.pi * (antinodeX - startX)) / totalLength);
        double currentAntinodeY = centerY + (2.0 * amplitude * spatialFactor * math.cos(time));
        canvas.drawCircle(Offset(antinodeX, currentAntinodeY), 3.5, pointPaint..color = Colors.greenAccent);
      }
    }

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant StandingWavesPainter oldDelegate) => true;
}