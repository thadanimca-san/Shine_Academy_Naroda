import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class CalorimetrySimulator extends StatefulWidget {
  const CalorimetrySimulator({Key? key}) : super(key: key);

  @override
  _CalorimetrySimulatorState createState() => _CalorimetrySimulatorState();
}

class _CalorimetrySimulatorState extends State<CalorimetrySimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _solidMass = 0.2;          // Mass of metal solid (kg)
  double _solidTemp = 100.0;        // Initial temp of solid (°C)
  double _liquidTemp = 20.0;        // Initial temp of water liquid (°C)
  double _solidSpecificHeat = 385.0; // Specific heat of solid (J/kg·K) - default Copper
  
  // Constant water parameters
  final double _waterMass = 0.4;     // Mass of water (kg)
  final double _waterSpecificHeat = 4186.0; // Specific heat of water (J/kg·K)

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
    _controller.forward();
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
    double numerator = (_solidMass * _solidSpecificHeat * _solidTemp) + (_waterMass * _waterSpecificHeat * _liquidTemp);
    double denominator = (_solidMass * _solidSpecificHeat) + (_waterMass * _waterSpecificHeat);
    double equilibriumTemp = numerator / denominator;

    double currentSolidTemp = _solidTemp - (_time * (_solidTemp - equilibriumTemp));
    double currentWaterTemp = _liquidTemp + (_time * (equilibriumTemp - _liquidTemp));
    double netHeatExchanged = _solidMass * _solidSpecificHeat * (_solidTemp - currentSolidTemp);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Calorimetry Master Lab"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.science), text: "3. Simulation"),
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
            _buildSimulationTab(equilibriumTemp, currentSolidTemp, currentWaterTemp, netHeatExchanged),
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
          _buildChapterHeader("THERMAL CALORIMETRY", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Calorimetry?",
            "Calorimetry is the quantitative science of measuring heat exchange changes inside a system boundary loop. It operates directly under the law of conservation of energy, tracking heat transitions through an isolated container environment called a calorimeter.",
            Colors.teal[800] ?? Colors.teal
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core System Components:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Principle of Mixtures:", "In an isolated systemic chamber containing no surrounding escape routes, Heat Lost by hot elements strictly equals Heat Gained by cold bodies."),
          _buildBulletPoint("Specific Heat Capacity (s):", "The thermal metric quantity required to elevate the baseline temperature of 1 kg mass of a pure element by exactly 1 Kelvin (or 1°C). Expressed as Q = m·s·ΔT."),
          _buildBulletPoint("Water Equivalent (W):", "The equivalent mass of water that would absorb or release the exact same quantum of heat energy as the calorimeter vessel block for an identical thermal gradient swing."),
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
          _buildChapterHeader("THE MATHEMATICAL PROOF", "The Principle of Mixtures Equilibrium Formula"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Heat Loss Equation (Hot Solid Element):\n""   Q_lost = m_solid · s_solid · (T_solid - T_equilibrium)\n\n" 
              "2. Heat Gain Equation (Cold Water Fluid):\n" 
              "   Q_gained = m_water · s_water · (T_equilibrium - T_water)\n\n" 
              "3. Equating Under Conservation Law rules:\n" 
              "   Q_lost = Q_gained\n" 
              "   m1·s1·(T1 - Tf) = m2·s2·(Tf - T2)\n\n" 
              "4. Solving for Equilibrium Junction Temperature (Tf):\n" 
              "   m1·s1·T1 - m1·s1·Tf = m2·s2·Tf - m2·s2·T2\n" 
              "   Tf = (m1·s1·T1 + m2·s2·T2) / (m1·s1 + m2·s2)\n\n" 
              "5. Account for Container Water Equivalent (W):\n" 
              "   Denominator shifts to => (m1·s1 + [m2 + W]·s_water)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.tealAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "NEET/JEE High-Yield Note:",
            "During phase change tracking states (e.g., Ice melting into water packets), temperature locks fixed at latent bounds.\n\n"
            "Use Q = m·L for configuration transformations, and switch back to specific updates once structural phase jumps settle.",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Interactive Simulation ➡️"),
        ],
      ),
    );
  }

  Widget _buildSimulationTab(double equilibriumTemp, double solidTemp, double waterTemp, double heatExchanged) {
    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(8),
          color: Colors.teal[50],
          child: Text(
            _isOscillating 
                ? (_time == 1.0 ? "🛑 Thermal Equilibrium Reached!" : "🟢 Mixing Active: Thermal Exchange Vector tracking updates...") 
                : "🛑 System Primed: Adjust masses, heat solid and click Drop Solid",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.teal[900]),
          ),
        ),
        // FIXED: Added real-time ambient values directly above the container canvas box
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text("⚡ Solid Element: ${solidTemp.toStringAsFixed(1)} °C", style: TextStyle(color: Colors.orange[800], fontWeight: FontWeight.bold, fontSize: 12, fontFamily: 'monospace')),
              Text("💧 Water Fluid: ${waterTemp.toStringAsFixed(1)} °C", style: TextStyle(color: Colors.blue[800], fontWeight: FontWeight.bold, fontSize: 12, fontFamily: 'monospace')),
            ],
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
                painter: CalorimetryPainter(
                  time: _time,
                  solidTemp: solidTemp,
                  waterTemp: waterTemp,
                  scaleRatio: constraints.maxWidth / 400.0,
                ),
              );
            }),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
          decoration: BoxDecoration(color: Colors.teal[900], borderRadius: BorderRadius.circular(10)),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(
                child: RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: TextStyle(color: Colors.white, fontFamily: 'monospace', fontSize: 11),
                    children: [
                      const TextSpan(text: "SOLID TEMP\n", style: TextStyle(color: Colors.amberAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${solidTemp.toStringAsFixed(1)} °C", style: TextStyle(fontWeight: FontWeight.bold)),
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
                      const TextSpan(text: "WATER TEMP\n", style: TextStyle(color: Colors.amberAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${waterTemp.toStringAsFixed(1)} °C", style: TextStyle(fontWeight: FontWeight.bold)),
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
                      const TextSpan(text: "HEAT TRAN. (Q)\n", style: TextStyle(color: Colors.amberAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${(heatExchanged / 1000.0).toStringAsFixed(2)} kJ", style: TextStyle(fontWeight: FontWeight.bold)),
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
                      const TextSpan(text: "FINAL EQUIL.\n", style: TextStyle(color: Colors.amberAccent, fontWeight: FontWeight.bold, fontSize: 8)),
                      TextSpan(text: "${equilibriumTemp.toStringAsFixed(1)} °C", style: TextStyle(fontWeight: FontWeight.bold)),
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
          _buildCalorimetryQuiz(),
        ],
      ),
    );
  }

  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.teal[900])),
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
        style: TextButton.styleFrom(backgroundColor: Colors.teal[900], foregroundColor: Colors.white, padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildCalorimetryQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "A copper calorimeter block contains 100g water at 20°C. If 50g of a metallic alloy at 100°C is added, and the calorimeter vessel water equivalent is 10g, what thermodynamic rule determines the final state balances?"
        : "50g of ice at 0°C is introduced into a massless cup holding 200g water at 40°C. Given L_fusion = 80 cal/g and s_water = 1 cal/g°C, what is the exact remaining physical layout composition once final equilibrium establishes?";

    List<String> options = isNeet
        ? ["Heat lost by metal equals heat gained by water plus container vessel", "Temperature parameters scale logarithmically", "Mechanical kinetic transitions negate balance", "Mass configurations double automatically"]
        : ["All ice melts, final temp settles at 16°C", "All ice melts, final temp settles at 20°C", "Partial melting occurs, 10g ice stays floating at 0°C", "System thermal runaway triggers"];

    int correctIndex = isNeet ? 0 : 0; 

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Mixture Balances Quiz:" : "JEE Mixed Phase Boundary Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? (Colors.green[700] ?? Colors.green) : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Colors.teal[800], 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[800], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Verify Thermodynamic Mixture Frame'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
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
                    ? "✅ CORRECT BALANCING FRAME:\n\nUnder conservation of thermal profiles, the water equivalent mass acts as additional water layout capacity. Therefore: Q_lost = (m_water + W)·s_water·ΔT_gained."
                    : "✅ CORRECT PHASE DECONSTRUCTION:\n\nHeat needed to melt all ice = 50g × 80 = 4000 cal. Maximum heat water can release dropping to 0°C = 200g × 1 × 40 = 8000 cal. Since available energy exceeds fusion requirements, all ice melts completely: 8000 - 4000 = (200 + 50)·1·(Tf - 0) => Tf = 4000 / 250 = 16°C.")
                : "❌ THERMODYNAMIC FUSION MISALIGNMENT:\n\nReview the Derivation Tab! Always evaluate phase transition criteria bounds (\$Q = mL\$) completely before mapping specific heat slope parameters.",
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
          Expanded(child: Column(children: [Text('Solid Mass: ${_solidMass.toStringAsFixed(2)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _solidMass, min: 0.05, max: 0.4, divisions: 7, activeColor: Colors.teal, onChanged: _isOscillating ? null : (val) => setState(() => _solidMass = val))])),
          Expanded(child: Column(children: [Text('Solid Temp: ${_solidTemp.toStringAsFixed(0)} °C', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _solidTemp, min: 50, max: 150, divisions: 10, activeColor: Colors.deepOrange, onChanged: _isOscillating ? null : (val) => setState(() => _solidTemp = val))])),
          Expanded(child: Column(children: [Text(TrilingualService.instance.getUIText('Spec. Heat Solid'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)), Slider(value: _solidSpecificHeat, min: 100, max: 900, divisions: 4, activeColor: Colors.amber, onChanged: _isOscillating ? null : (val) => setState(() => _solidSpecificHeat = val))])),
        ]),
        Row(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
          ElevatedButton.icon(
            onPressed: _isOscillating ? null : _releaseSystem, 
            style: ElevatedButton.styleFrom(backgroundColor: Colors.teal[800], padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 10)),
            icon: Icon(Icons.play_arrow, color: Colors.white, size: 16),
            label: Text(TrilingualService.instance.getUIText('Drop Solid into Cup'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
          ),
          IconButton(onPressed: _resetSimulation, icon: Icon(Icons.refresh, size: 20, color: Colors.blueGrey))
        ]),
      ]),
    );
  }
}

class CalorimetryPainter extends CustomPainter {
  final double time, solidTemp, waterTemp, scaleRatio;
  CalorimetryPainter({required this.time, required this.solidTemp, required this.waterTemp, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double centerX = canvasWidth / 2.0;
    double centerY = canvasHeight / 2.0;

    // 1. Draw Outer Insulated Calorimeter Vessel Jacket
    Paint jacketPaint = Paint()..color = Colors.blueGrey[700] ?? Colors.blueGrey..style = PaintingStyle.stroke..strokeWidth = 4.0;
    canvas.drawRect(Rect.fromLTWH(centerX - 70, centerY - 40, 140, 90), jacketPaint);

    // 2. Color calculation for fluid tracking
    double waterNormalized = (waterTemp - 20) / (60 - 20); 
    waterNormalized = waterNormalized.clamp(0.0, 1.0);
    Color waterColor = Color.lerp(Colors.blue[400], Colors.purple[300], waterNormalized)?.withValues(alpha: 0.7) ?? Colors.blue.withValues(alpha: 0.7);

    Paint waterPaint = Paint()..color = waterColor..style = PaintingStyle.fill;
    canvas.drawRect(Rect.fromLTWH(centerX - 66, centerY + 2, 132, 44), waterPaint);

    // 3. Draw Dynamic Dropping Metal Block
    double initialY = centerY - 80;
    double targetY = centerY + 24; 
    double currentSolidY = initialY + (time * (targetY - initialY));

    double solidNormalized = (solidTemp - 20) / (150 - 20);
    solidNormalized = solidNormalized.clamp(0.0, 1.0);
    Color solidColor = Color.lerp(Colors.amber[700], Colors.redAccent, solidNormalized) ?? Colors.orange;

    Paint solidPaint = Paint()..color = solidColor..style = PaintingStyle.fill;
    canvas.drawRect(Rect.fromLTWH(centerX - 20, currentSolidY - 15, 40, 22), solidPaint);
    
    Paint solidBorder = Paint()..color = Colors.white70..strokeWidth = 1.5..style = PaintingStyle.stroke;
    canvas.drawRect(Rect.fromLTWH(centerX - 20, currentSolidY - 15, 40, 22), solidBorder);

    // ALL CANVAS INTERNAL OVERLAPPING TEXT REMOVED TO PREVENT BOUNDARY CLIPPING FLUX
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant CalorimetryPainter oldDelegate) => true;
}