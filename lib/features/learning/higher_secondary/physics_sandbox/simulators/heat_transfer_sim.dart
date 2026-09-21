import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class HeatTransferSimulator extends StatefulWidget {
  const HeatTransferSimulator({Key? key}) : super(key: key);

  @override
  _HeatTransferSimulatorState createState() => _HeatTransferSimulatorState();
}

class _HeatTransferSimulatorState extends State<HeatTransferSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _hotTemp = 100.0;          // Hot reservoir temperature (°C)
  double _coldTemp = 20.0;          // Cold reservoir temperature (°C)
  double _thermalConductivity = 400.0; // Thermal conductivity k (W/mK) - default Copper
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
        _time = _controller.value;
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
    double area = 0.01; 
    double length = 0.5; 
    double heatTransferRate = _thermalConductivity * area * (_hotTemp - _coldTemp) / length;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Thermodynamics Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.local_fire_department), text: "3. Simulation"),
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
            _buildSimulationTab(heatTransferRate),
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
          _buildChapterHeader("TEMPERATURE & HEAT TRANSFER", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Heat Transfer?",
            "Heat is the spontaneous transfer of thermal energy from a high-temperature domain to a lower-temperature domain driven strictly by a temperature gradient. Energy migration ceases only when absolute thermal equilibrium is reached throughout the system boundary matrix.",
            Colors.red[800] ?? Colors.red
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Components:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Conduction:", "Thermal energy exchange through direct atomic vibrations and free electron collisions in a medium without macroscopic bulk displacement of matter."),
          _buildBulletPoint("Convection:", "Heat transfer via the actual bulk movement of fluid macroscopic packets driven by buoyant force variations caused by density variations."),
          _buildBulletPoint("Radiation:", "Energy emission via electromagnetic waves governed exclusively by Stefan-Boltzmann relations requiring no material medium to propagate."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "Fourier's Law & Thermal Resistance Analogy"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Fourier's Fundamental Law of Conduction:\n""   dQ / dt = -k · A · (dT / dx)\n\n" 
              "2. Under Steady State Conditions (Constant Gradient):\n" 
              "   dT / dx = (T_cold - T_hot) / L\n" 
              "   H = dQ / dt = k · A · (T_hot - T_cold) / L\n\n" 
              "3. Electric Current Analogy Framework:\n" 
              "   Current (I) = V / R_electric\n" 
              "   Heat Current (H) = ΔT / R_thermal\n\n" 
              "4. Defining Thermal Resistance Expression:\n" 
              "   R_thermal = L / (k · A)\n\n" 
              "5. Composite Bars in Series Configuration:\n" 
              "   R_net = R1 + R2 = [L1/(k1·A)] + [L2/(k2·A)]"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.orangeAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "Always utilize the Ohm's Law thermal circuit analogy to quickly crack composite rod junction temperatures.\n\n"
            "At steady state, the heat current input entering a junction must strictly equal the heat current exiting it: H_in = H_out.",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  Widget _buildSimulationTab(double heatTransferRate) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.red[50],
          child: Text(
            _isOscillating ? "🟢 Thermal Conduction Active: Simulating Heat Flux Vector" : "🛑 System Primed: Select Reservoir Temperatures & Excite System",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.red[900]),
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
                painter: HeatTransferPainter(
                  hotTemp: _hotTemp,
                  coldTemp: _coldTemp,
                  time: _isOscillating ? _time : 0.0,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),
        
        // FIXED TELEMETRY BAR: Swapped column structure with padding-efficient layout rules to stop clipping
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
          decoration: BoxDecoration(color: Colors.red[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(
                child: RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: TextStyle(color: Colors.white, fontFamily: 'monospace', fontSize: 11),
                    children: [
                      const TextSpan(text: "HOT RESERVOIR\n", style: TextStyle(color: Colors.orangeAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${_hotTemp.toStringAsFixed(0)} °C", style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
              Expanded(
                child: RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: TextStyle(color: Colors.white, fontFamily: 'monospace', fontSize: 11),
                    children: [
                      const TextSpan(text: "COLD RESERVOIR\n", style: TextStyle(color: Colors.orangeAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${_coldTemp.toStringAsFixed(0)} °C", style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
              Expanded(
                child: RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: TextStyle(color: Colors.white, fontFamily: 'monospace', fontSize: 11),
                    children: [
                      const TextSpan(text: "HEAT CURRENT (H)\n", style: TextStyle(color: Colors.orangeAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${heatTransferRate.toStringAsFixed(1)} W", style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
              Expanded(
                child: RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: TextStyle(color: Colors.white, fontFamily: 'monospace', fontSize: 11),
                    children: [
                      const TextSpan(text: "THERMAL RES.\n", style: TextStyle(color: Colors.orangeAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${(0.5 / (_thermalConductivity * 0.01)).toStringAsFixed(2)} K/W", style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              ),
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
          _buildHeatQuiz(),
        ],
      ),
    );
  }

  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.red[900])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.red[900], fontSize: 16)),
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
        style: TextButton.styleFrom(backgroundColor: Colors.red[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildHeatQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "Two identical metallic rods are connected first in series and then in parallel configurations between identical hot and cold reservoirs. What is the ratio of heat current in series to parallel (H_series / H_parallel)?"
        : "A composite insulated cylinder consists of two layers with thermal conductivities k1 and k2, and equal lengths. If a steady-state heat flux flows through them in series, what is the exact expression for the joint junction temperature T_j?";

    List<String> options = isNeet
        ? ["4 : 1", "1 : 2", "1 : 4", "2 : 1"]
        : ["(k1·Th + k2·Tc) / (k1 + k2)", "(k1·Tc + k2·Th) / (k1 + k2)", "(k1·k2·Th·Tc) / (k1+k2)", "k1·Th - k2·Tc"];

    int correctIndex = isNeet ? 2 : 0; 

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Thermal Grid Quiz:" : "JEE Composite Junction Core Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? (Colors.green[700] ?? Colors.green) : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.red[800], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.red[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Thermodynamic Continuity Framework'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT SCALING RATIO:\n\nIn series, R_net = R + R = 2R, so H_s = ΔT / 2R. In parallel, 1/R_net = 1/R + 1/R = 2/R, which yields R_net = R/2, so H_p = 2ΔT / R. The ratio H_s / H_p evaluates exactly to 1 / 4."
                    : "✅ CORRECT JUNCTION PROFILE:\n\nEquating steady-state thermal current values gives: k1·A·(T_hot - T_j)/L = k2·A·(T_j - T_cold)/L. Solving explicitly for T_j isolated leads directly to: T_j = (k1·T_hot + k2·T_cold) / (k1 + k2).")
                : "❌ THERMAL GRADIENT MISALIGNMENT:\n\nReview the Derivation Tab! Map your composite rod networks using the electrical series/parallel resistor equivalents (\$R_t = L/kA\$) to correctly solve junction conditions.",
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
          Expanded(child: Column(children: [Text('Hot Temp: ${_hotTemp.toStringAsFixed(0)} °C', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _hotTemp, min: 60, max: 150, divisions: 9, activeColor: Colors.red, onChanged: _isOscillating ? null : (val) => setState(() => _hotTemp = val))])),
          Expanded(child: Column(children: [Text('Cold Temp: ${_coldTemp.toStringAsFixed(0)} °C', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _coldTemp, min: 0, max: 40, divisions: 8, activeColor: Colors.blue, onChanged: _isOscillating ? null : (val) => setState(() => _coldTemp = val))])),
          Expanded(child: Column(children: [Text(TrilingualService.instance.getUIText('Conductivity k'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _thermalConductivity, min: 100, max: 400, divisions: 3, activeColor: Colors.orange, onChanged: _isOscillating ? null : (val) => setState(() => _thermalConductivity = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isOscillating ? null : _releaseSystem, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.red[800], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('Excite Heat Flux'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class HeatTransferPainter extends CustomPainter {
  final double hotTemp, coldTemp, time;
  final double scaleRatio;
  HeatTransferPainter({required this.hotTemp, required this.coldTemp, required this.time, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double centerY = canvasHeight / 2.0;
    double barStartX = 80.0;
    double barEndX = canvasWidth - 80.0;
    double barWidth = barEndX - barStartX;
    double barHeight = 40.0;

    // 1. Draw Hot Reservoir (Left side)
    Paint hotReservoirPaint = Paint()..color = Colors.red[700] ?? Colors.red;
    canvas.drawRect(Rect.fromLTWH(10, centerY - 50, barStartX - 10, 100), hotReservoirPaint);
    _drawText(canvas, Offset(20, centerY - 14), "T_H\n${hotTemp.toStringAsFixed(0)}°C", Colors.white);

    // 2. Draw Cold Reservoir (Right side)
    Paint coldReservoirPaint = Paint()..color = Colors.blue[700] ?? Colors.blue;
    canvas.drawRect(Rect.fromLTWH(barEndX, centerY - 50, canvasWidth - barEndX - 10, 100), coldReservoirPaint);
    _drawText(canvas, Offset(barEndX + 15, centerY - 14), "T_C\n${coldTemp.toStringAsFixed(0)}°C", Colors.white);

    // 3. Draw The Conducting Metal Bar with Gradient Interpolation
    for (double x = 0; x < barWidth; x += 1.0) {
      double currentX = barStartX + x;
      double fraction = x / barWidth;
      
      double tempValue = hotTemp - (fraction * (hotTemp - coldTemp));
      double normalizedTemp = (tempValue - 20) / (150 - 0); 
      normalizedTemp = normalizedTemp.clamp(0.0, 1.0);

      Color sliceColor = Color.lerp(Colors.blue, Colors.red, normalizedTemp) ?? Colors.grey;
      Paint slicePaint = Paint()..color = sliceColor..strokeWidth = 1.5;

      canvas.drawLine(Offset(currentX, centerY - barHeight / 2), Offset(currentX, centerY + barHeight / 2), slicePaint);
    }

    // 4. Moving Energy Flux Particles
    if (time > 0) {
      Paint particlePaint = Paint()..color = Colors.yellowAccent..style = PaintingStyle.fill;
      int particleCount = 6;
      for (int i = 0; i < particleCount; i++) {
        double particleFraction = (time + (i / particleCount)) % 1.0;
        double pX = barStartX + (particleFraction * barWidth);
        double pY = centerY + (8.0 * math.sin(particleFraction * math.pi * 4));
        canvas.drawCircle(Offset(pX, pY), 3.0, particlePaint);
      }
    }

    Paint borderPaint = Paint()..color = Colors.white70..strokeWidth = 2.0..style = PaintingStyle.stroke;
    canvas.drawRect(Rect.fromLTWH(barStartX, centerY - barHeight / 2, barWidth, barHeight), borderPaint);

    canvas.restore();
  }

  void _drawText(Canvas canvas, Offset offset, String text, Color color) {
    TextPainter tp = TextPainter(
      text: TextSpan(style: TextStyle(color: color, fontSize: 13, fontWeight: FontWeight.bold, fontFamily: 'monospace'), text: text),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, offset);
  }

  @override
  bool shouldRepaint(covariant HeatTransferPainter oldDelegate) => true;
}