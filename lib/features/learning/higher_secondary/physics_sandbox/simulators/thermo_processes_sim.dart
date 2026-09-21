import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ThermoProcessesSimulator extends StatefulWidget {
  const ThermoProcessesSimulator({Key? key}) : super(key: key);

  @override
  _ThermoProcessesSimulatorState createState() => _ThermoProcessesSimulatorState();
}

class _ThermoProcessesSimulatorState extends State<ThermoProcessesSimulator> with TickerProviderStateMixin {
  String _processType = "Isothermal"; 

  double _volume = 2.0;       
  final double _initialPressure = 2.0; 
  final double _initialVolume = 1.0; 
  final double _gamma = 1.4;    

  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
  }

  double _calculatePressure(double v) {
    if (_processType == "Isothermal") {
      return (_initialPressure * _initialVolume) / v;
    } else {
      return (_initialPressure * math.pow(_initialVolume, _gamma)) / math.pow(v, _gamma);
    }
  }

  void _updateVolume(double newVol) {
    setState(() {
      _volume = newVol.clamp(1.0, 4.0);
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
  }

  void _switchProcess(String process) {
    setState(() {
      _processType = process;
      _volume = 1.0; 
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
    });
  }

  @override
  void dispose() { 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Thermodynamic Processes Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.show_chart), text: "3. Simulation"),
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
            _buildSimulationTab(),
            _buildAssessmentTab(),
          ],
        ),
      ),
    );
  }

  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("THERMODYNAMIC PROCESSES", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is a Thermodynamic Process?",
            "A thermodynamic process is a transition of a system from one equilibrium state to another. The path of transition determines the amount of heat exchanged and work done by the system.",
            Colors.deepPurple[800] ?? Colors.deepPurple
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core Process Types:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Isothermal Process:", "Temperature remains constant (ΔT = 0). Governed by Boyle's Law: P·V = constant. The system exchanges heat freely with a thermal reservoir."),
          _buildBulletPoint("Adiabatic Process:", "No heat enters or leaves the system (Q = 0). Governed by Poisson's Law: P·V^γ = constant. Rapid compression or expansion is typically adiabatic."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Skip directly to Derivations ➡️"),
        ],
      ),
    );
  }

  Widget _buildDerivationTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("WORK DONE DERIVATIONS", "Isothermal vs Adiabatic Equations"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Isothermal Work Done (T = Constant):\n""   W = ∫ P dV = nRT ln(Vf / Vi)\n" 
              "   Slope on P-V diagram: dP/dV = -P / V\n\n" 
              "2. Adiabatic Work Done (Q = 0):\n" 
              "   PV^γ = Constant  (where γ = Cp / Cv)\n" 
              "   W = (P_i V_i - P_f V_f) / (γ - 1)\n" 
              "   Slope on P-V diagram: dP/dV = -γ (P / V)\n\n" 
              "3. Key Insight:\n" 
              "   Adiabatic curves are steeper than Isothermal curves by a factor of γ!"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.amberAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "For monoatomic gases, γ = 1.67. For diatomic gases (like air/O2/N2), γ = 1.4. Always check γ values during adiabatic expansion problems!",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch P-V Diagram Simulation ➡️"),
        ],
      ),
    );
  }

  Widget _buildSimulationTab() {
    double currentPressure = _calculatePressure(_volume);
    
    return Column(
      children: [
        Container(
          width: double.infinity,
          margin: const EdgeInsets.all(8),
          padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(8),
            boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 2, offset: const Offset(0, 1))],
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              _buildProcessToggleButton("Isothermal Process", "Isothermal"),
              const SizedBox(width: 8),
              _buildProcessToggleButton("Adiabatic Process", "Adiabatic"),
            ],
          ),
        ),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 2),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text("📉 Pressure: ${currentPressure.toStringAsFixed(2)} atm", style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
              Text("📦 Volume: ${_volume.toStringAsFixed(2)} L", style: TextStyle(color: Colors.blue, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
              Text("⚙️ Mode: $_processType", style: TextStyle(color: Colors.deepPurple, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
            ],
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
            decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
            child: LayoutBuilder(builder: (context, constraints) {
              return CustomPaint(
                size: Size(constraints.maxWidth, constraints.maxHeight),
                painter: PVDiagramPainter(
                  volume: _volume,
                  pressure: currentPressure,
                  processType: _processType,
                  initialPressure: _initialPressure,
                  initialVolume: _initialVolume,
                  gamma: _gamma,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
          decoration: BoxDecoration(color: Colors.deepPurple[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(child: _buildTelemetry("CURRENT VOLUME", "${_volume.toStringAsFixed(2)} L")),
              Expanded(child: _buildTelemetry("CURRENT PRESSURE", "${currentPressure.toStringAsFixed(2)} atm")),
              Expanded(child: _buildTelemetry("SYSTEMCURVE", _processType == "Isothermal" ? "P·V = C" : "P·V^1.4 = C")),
            ],
          ),
        ),
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Move to Thermodynamics Exam Drill ➡️"),
        ),
      ],
    );
  }

  Widget _buildProcessToggleButton(String title, String targetProcess) {
    bool isSelected = _processType == targetProcess;
    return InkWell(
      onTap: () => _switchProcess(targetProcess),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
        decoration: BoxDecoration(
          color: isSelected ? Colors.deepPurple[900] : Colors.grey[200],
          borderRadius: BorderRadius.circular(6),
          border: Border.all(color: isSelected ? (Colors.deepPurple[900] ?? Colors.deepPurple) : Colors.transparent),
        ),
        child: Text(title, style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: isSelected ? Colors.white : Colors.deepPurple[900])),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(label.toUpperCase(), textAlign: TextAlign.center, style: TextStyle(color: Colors.amberAccent, fontSize: 8, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 4),
        Text(value, textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 12),
      padding: const EdgeInsets.all(10), 
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(8)),
      child: Column(
        children: [
          Text(TrilingualService.instance.getUIText('Adjust Expansion Volume (L)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
          Slider(
            value: _volume, 
            min: 1.0, 
            max: 4.0, 
            divisions: 30, 
            activeColor: Colors.deepPurple, 
            onChanged: (val) => _updateVolume(val),
          ),
        ],
      ),
    );
  }

  Widget _buildAssessmentTab() {
    final List<Widget> toggleButtonsChildren =  [
      Padding(
        padding: EdgeInsets.symmetric(horizontal: 24),
        child: Text(TrilingualService.instance.getUIText('NEET Rank Booster'), style: TextStyle(fontWeight: FontWeight.bold)),
      ),
      Padding(
        padding: EdgeInsets.symmetric(horizontal: 24),
        child: Text(TrilingualService.instance.getUIText('JEE Core Concept Challenge'), style: TextStyle(fontWeight: FontWeight.bold)),
      ),
    ];

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
                children: toggleButtonsChildren,
              ),
            ],
          ),
          const SizedBox(height: 16),
          _buildThermoQuiz(),
        ],
      ),
    );
  }

  Widget _buildThermoQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "When a gas undergoes adiabatic expansion, what happens to its internal energy?"
        : "How does the slope of an adiabatic curve compare to an isothermal curve on a P-V diagram for the same gas state?";

    List<String> options = isNeet
        ? ["Internal energy decreases as work is done at the expense of thermal energy", "Internal energy remains constant", "Internal energy increases due to heat friction", "Internal energy equals zero"]
        : ["Adiabatic slope is steeper by a factor of γ", "Isothermal slope is steeper by a factor of γ", "Both curves have identical slopes", "Slopes are perpendicular to each other"];

    int correctIndex = 0; 

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Thermodynamic Quiz:" : "JEE Advanced Process Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6), side: BorderSide(color: Colors.grey[200] ?? Colors.grey)),
              value: index, 
              groupValue: _selectedAnswerIndex, 
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500)), 
              activeColor: Colors.deepPurple[800], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Thermodynamic Response'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            ),
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50], borderRadius: BorderRadius.circular(8), border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red)),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "✅ CORRECT:\n\nIn an adiabatic expansion (Q = 0), the gas does work on its surroundings. Since no heat is supplied, this work comes directly from its internal energy, causing temperature and internal energy to drop."
                    : "✅ CORRECT:\n\nDifferentiating PV = C gives dP/dV = -P/V. Differentiating PV^γ = C gives dP/dV = -γ(P/V). Thus, the adiabatic curve is steeper by factor γ.")
                : "❌ INCORRECT:\n\nReview the Derivation Tab! Remember that adiabatic processes involve no heat transfer, making temperature dependent entirely on volumetric work.",
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

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
        style: TextButton.styleFrom(backgroundColor: Colors.deepPurple[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }
}

class PVDiagramPainter extends CustomPainter {
  final double volume, pressure, initialPressure, initialVolume, gamma, scaleRatio;
  final String processType;

  PVDiagramPainter({
    required this.volume,
    required this.pressure,
    required this.processType,
    required this.initialPressure,
    required this.initialVolume,
    required this.gamma,
    required this.scaleRatio,
  });

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save();
    canvas.scale(scaleRatio);
    final double w = size.width / scaleRatio;
    final double h = size.height / scaleRatio;

    // Strict coordinate boundaries
    double originX = 50.0;
    double originY = h - 35.0;
    double maxPlotWidth = w - 70.0;
    double maxPlotHeight = h - 55.0;

    // Draw grid axes
    Paint axisPaint = Paint()..color = Colors.white60..strokeWidth = 1.5;
    canvas.drawLine(Offset(originX, originY), Offset(originX + maxPlotWidth, originY), axisPaint); 
    canvas.drawLine(Offset(originX, originY), Offset(originX, originY - maxPlotHeight), axisPaint); 

    // Neatly scaled, unobtrusive axis labels
    TextPainter(
      text: const TextSpan(text: 'V (L)', style: TextStyle(color: Colors.white70, fontSize: 11, fontWeight: FontWeight.bold)),
      textDirection: TextDirection.ltr
    )..layout()..paint(canvas, Offset(originX + maxPlotWidth - 15, originY + 4));

    TextPainter(
      text: const TextSpan(text: 'P (atm)', style: TextStyle(color: Colors.white70, fontSize: 11, fontWeight: FontWeight.bold)),
      textDirection: TextDirection.ltr
    )..layout()..paint(canvas, Offset(originX - 38, originY - maxPlotHeight - 12));

    double volScale = maxPlotWidth / 3.0;   
    double pressScale = maxPlotHeight / 2.0; 

    // Plot curve lines
    Paint curvePaint = Paint()
      ..color = processType == "Isothermal" ? Colors.cyanAccent : Colors.amberAccent
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3.0;

    Path curvePath = Path();
    bool first = true;

    for (double vVal = 1.0; vVal <= 4.0; vVal += 0.02) {
      double pVal = processType == "Isothermal" 
          ? (initialPressure * initialVolume) / vVal
          : (initialPressure * math.pow(initialVolume, gamma)) / math.pow(vVal, gamma);

      double px = originX + (vVal - 1.0) * volScale;
      double py = originY - (pVal * pressScale);

      if (px >= originX && px <= (originX + maxPlotWidth) && py <= originY && py >= (originY - maxPlotHeight)) {
        if (first) {
          curvePath.moveTo(px, py);
          first = false;
        } else {
          curvePath.lineTo(px, py);
        }
      }
    }
    
    canvas.drawPath(curvePath, curvePaint);

    // Interactive operating point indicator
    double currentPx = originX + (volume - 1.0) * volScale;
    double currentPy = originY - (pressure * pressScale);

    if (currentPx >= originX && currentPx <= (originX + maxPlotWidth) && currentPy <= originY && currentPy >= (originY - maxPlotHeight)) {
      Paint pointPaint = Paint()..color = Colors.redAccent..style = PaintingStyle.fill;
      canvas.drawCircle(Offset(currentPx, currentPy), 6.0, pointPaint);
    }

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant PVDiagramPainter oldDelegate) => true;
}