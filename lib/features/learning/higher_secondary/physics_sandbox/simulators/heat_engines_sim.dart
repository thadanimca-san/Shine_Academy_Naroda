import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class HeatEnginesSimulator extends StatefulWidget {
  const HeatEnginesSimulator({Key? key}) : super(key: key);

  @override
  _HeatEnginesSimulatorState createState() => _HeatEnginesSimulatorState();
}

class _HeatEnginesSimulatorState extends State<HeatEnginesSimulator> with TickerProviderStateMixin {
  double _hotTemp = 600.0;  
  double _coldTemp = 300.0; 
  final double _heatInput = 1000.0; 

  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late TabController _tabController;
  late AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _animController = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    )..repeat();
  }

  double get _carnotEfficiency {
    if (_hotTemp <= _coldTemp) return 0.0;
    return 1.0 - (_coldTemp / _hotTemp);
  }

  double get _workDone => _heatInput * _carnotEfficiency;
  double get _heatRejected => _heatInput - _workDone;

  @override
  void dispose() { 
    _tabController.dispose();
    _animController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Heat Engines Workbench"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
          _buildChapterHeader("HEAT ENGINES & SECOND LAW", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is a Heat Engine?",
            "A heat engine is a cyclic device that absorbs thermal energy from a high-temperature reservoir, converts a portion of it into mechanical work, and exhausts the remaining energy to a low-temperature sink.",
            Colors.teal[800] ?? Colors.teal
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Core Components of a Heat Engine:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Source (Hot Reservoir):", "Supplies heat Q_H at a high absolute temperature T_H."),
          _buildBulletPoint("Working Substance:", "The gas or fluid that undergoes expansion and compression to perform work W."),
          _buildBulletPoint("Sink (Cold Reservoir):", "Absorbs rejected waste heat Q_C at a lower absolute temperature T_C."),
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
          _buildChapterHeader("EFFICIENCY & CARNOT THEOREM", "Thermodynamic Framework"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Conservation of Energy (First Law):\n""   Q_H = W + Q_C\n\n" 
              "2. Thermal Efficiency Formula (η):\n" 
              "   η = Work Done / Heat Absorbed = W / Q_H\n" 
              "   η = (Q_H - Q_C) / Q_H = 1 - (Q_C / Q_H)\n\n" 
              "3. Carnot Engine Efficiency (Absolute Temperature Scale):\n" 
              "   η_max = 1 - (T_C / T_H)\n\n" 
              "4. Crucial Constraint:\n" 
              "   Efficiency can NEVER be 100% (unless T_C = 0 K, which violates the Third Law)."),
              style: TextStyle(fontFamily: 'monospace', color: Colors.amberAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "High-Yield Exam Strategy:",
            "Always convert Celsius temperatures to Absolute Kelvin bounds before computing Carnot efficiency!",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Heat Engine Flow Simulation ➡️"),
        ],
      ),
    );
  }

  Widget _buildSimulationTab() {
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 6, horizontal: 12),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(8),
                boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 2, offset: const Offset(0, 1))],
              ),
              child: Text(TrilingualService.instance.getUIText("🔥 Thermal Cycle Energy Flow & Efficiency Monitor"), textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 11, color: Colors.teal)),
            ),
            const SizedBox(height: 6),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 8),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text("🌡️ Th: ${_hotTemp.toStringAsFixed(0)} K", style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                  Text("❄️ Tc: ${_coldTemp.toStringAsFixed(0)} K", style: TextStyle(color: Colors.blue, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                  Text("⚡ η: ${(_carnotEfficiency * 100).toStringAsFixed(1)}%", style: TextStyle(color: Colors.teal, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                ],
              ),
            ),
            const SizedBox(height: 6),
            // Animated Widget-based Flow Diagram
            Container(
              height: 240,
              padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
              decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Hot Reservoir Box
                  Container(
                    width: 220,
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    decoration: BoxDecoration(color: Colors.red[700], borderRadius: BorderRadius.circular(6)),
                    child: Text('HOT RESERVOIR (${_hotTemp.toStringAsFixed(0)} K)', textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                  
                  // Animated Heat Flow Down (QH)
                  AnimatedBuilder(
                    animation: _animController,
                    builder: (context, child) {
                      return Opacity(
                        opacity: 0.4 + 0.6 * (_animController.value),
                        child: Text('⬇️ QH = ${_heatInput.toStringAsFixed(0)} J (Active Heat Flow)', style: TextStyle(color: Colors.amberAccent, fontSize: 11, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
                      );
                    },
                  ),

                  // Engine Core Row with Work Output on the right
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Container(
                        width: 160,
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        decoration: BoxDecoration(color: Colors.teal[800], borderRadius: BorderRadius.circular(8)),
                        child: Text(TrilingualService.instance.getUIText('HEAT ENGINE CORE'), textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                      ),
                      const SizedBox(width: 16),
                      Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(color: Colors.teal[900], borderRadius: BorderRadius.circular(6), border: Border.all(color: Colors.amberAccent)),
                        child: Text('W = ${_workDone.toStringAsFixed(0)} J\n(η = ${(_carnotEfficiency * 100).toStringAsFixed(1)}%)', textAlign: TextAlign.center, style: TextStyle(color: Colors.amberAccent, fontSize: 10, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
                      ),
                    ],
                  ),

                  // Animated Heat Flow Down to Sink (QC)
                  AnimatedBuilder(
                    animation: _animController,
                    builder: (context, child) {
                      return Opacity(
                        opacity: 0.4 + 0.6 * (1.0 - _animController.value),
                        child: Text('⬇️ QC = ${_heatRejected.toStringAsFixed(0)} J (Exhaust Heat)', style: TextStyle(color: Colors.amberAccent, fontSize: 11, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
                      );
                    },
                  ),

                  // Cold Sink Box
                  Container(
                    width: 220,
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    decoration: BoxDecoration(color: Colors.blue[700], borderRadius: BorderRadius.circular(6)),
                    child: Text('COLD SINK (${_coldTemp.toStringAsFixed(0)} K)', textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 6),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 8),
              decoration: BoxDecoration(color: Colors.teal[900], borderRadius: BorderRadius.circular(10)),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Expanded(child: _buildTelemetry("HEAT INPUT (Q_H)", "${_heatInput.toStringAsFixed(0)} J")),
                  Expanded(child: _buildTelemetry("WORK OUTPUT (W)", "${_workDone.toStringAsFixed(0)} J")),
                  Expanded(child: _buildTelemetry("REJECTED (Q_C)", "${_heatRejected.toStringAsFixed(0)} J")),
                ],
              ),
            ),
            const SizedBox(height: 6),
            _buildControlsTray(),
            const SizedBox(height: 8),
            _buildSkipButton(3, "Move to Heat Engines Exam Drill ➡️"),
          ],
        ),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(label.toUpperCase(), textAlign: TextAlign.center, style: TextStyle(color: Colors.amberAccent, fontSize: 8, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 2),
        Text(value, textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(8), 
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(8)),
      child: Column(
        children: [
          Row(
            children: [
              Expanded(flex: 2, child: Text(TrilingualService.instance.getUIText('Hot Temp Th (K):'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold))),
              Expanded(
                flex: 5,
                child: Slider(
                  value: _hotTemp, 
                  min: 400.0, 
                  max: 1000.0, 
                  divisions: 12, 
                  activeColor: Colors.red, 
                  onChanged: (val) => setState(() => _hotTemp = val > _coldTemp ? val : _coldTemp + 50),
                ),
              ),
              Text('${_hotTemp.toStringAsFixed(0)} K', style: TextStyle(fontSize: 10, fontFamily: 'monospace', fontWeight: FontWeight.bold)),
            ],
          ),
          Row(
            children: [
              Expanded(flex: 2, child: Text(TrilingualService.instance.getUIText('Cold Temp Tc (K):'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold))),
              Expanded(
                flex: 5,
                child: Slider(
                  value: _coldTemp, 
                  min: 150.0, 
                  max: 500.0, 
                  divisions: 7, 
                  activeColor: Colors.blue, 
                  onChanged: (val) => setState(() => _coldTemp = val < _hotTemp ? val : _hotTemp - 50),
                ),
              ),
              Text('${_coldTemp.toStringAsFixed(0)} K', style:  TextStyle(fontSize: 10, fontFamily: 'monospace', fontWeight: FontWeight.bold)),
            ],
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
          _buildEngineQuiz(),
        ],
      ),
    );
  }

  Widget _buildEngineQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "A Carnot engine operates between 400 K and 300 K. What is its thermal efficiency percentage?"
        : "If the temperature of the source in a Carnot engine is doubled while keeping the sink temperature constant, what happens to its efficiency?";

    List<String> options = isNeet
        ? ["25%", "50%", "75%", "100%"]
        : ["Efficiency doubles", "Efficiency increases to more than double its initial value", "Efficiency increases but remains less than double", "Efficiency decreases by half"];

    int correctIndex = isNeet ? 0 : 2; 

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Heat Engine Quiz:" : "JEE Advanced Efficiency Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
                    ? "✅ CORRECT:\n\nη = 1 - (Tc / Th) = 1 - (300 / 400) = 1 - 0.75 = 0.25 or 25%."
                    : "✅ CORRECT:\n\nInitial η1 = 1 - Tc/Th. New η2 = 1 - Tc/(2Th). Since Tc/Th < 1, doubling Th increases efficiency, but because it is fractional subtraction, the efficiency increases by less than a factor of two.")
                : "❌ INCORRECT:\n\nReview the Derivation Tab! Apply η = 1 - (Tc / Th) using strict absolute Kelvin bounds.",
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
}