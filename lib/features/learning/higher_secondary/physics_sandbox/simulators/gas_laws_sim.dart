import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class GasLawsSimulator extends StatefulWidget {
  const GasLawsSimulator({Key? key}) : super(key: key);

  @override
  _GasLawsSimulatorState createState() => _GasLawsSimulatorState();
}

class _GasLawsSimulatorState extends State<GasLawsSimulator> with TickerProviderStateMixin {
  String _activeLaw = "Boyle"; 

  double _pressure = 1.0;     
  double _volume = 2.0;       
  double _temperature = 300.0; 
  final double _nR = 2.0;     

  double _time = 0.0;
  bool _isSimulating = false;
  
  String _targetPath = 'NEET';
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  
  late AnimationController _controller;
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 2))..addListener(() {
      setState(() {
        _time = _controller.value;
      });
    });
    if (!_isSimulating) {
      _isSimulating = true;
      _controller.repeat();
    }
  }

  void _updateSystemVariables(String variableChanged, double value) {
    setState(() {
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
      
      if (_activeLaw == "Boyle") {
        if (variableChanged == "Volume") {
          _volume = value.clamp(1.0, 4.0);
          _pressure = ((_nR * _temperature) / _volume).clamp(0.5, 2.0);
        } else if (variableChanged == "Pressure") {
          _pressure = value.clamp(0.5, 2.0);
          _volume = ((_nR * _temperature) / _pressure).clamp(1.0, 4.0);
        }
      } else if (_activeLaw == "Charles") {
        if (variableChanged == "Volume") {
          _volume = value.clamp(1.0, 3.0);
          _temperature = ((_pressure * _volume) / _nR * 300).clamp(150.0, 450.0);
        } else if (variableChanged == "Temperature") {
          _temperature = value.clamp(150.0, 450.0);
          _volume = ((_pressure * _temperature) / (_nR * 150)).clamp(1.0, 3.0);
        }
      } else if (_activeLaw == "Gay-Lussac") {
        if (variableChanged == "Pressure") {
          _pressure = value.clamp(0.5, 2.25);
          _temperature = ((_pressure * _volume) / _nR * 250).clamp(150.0, 450.0);
        } else if (variableChanged == "Temperature") {
          _temperature = value.clamp(150.0, 450.0);
          _pressure = ((_nR * _temperature) / (_volume * 300)).clamp(0.5, 2.25);
        }
      }
    });
  }

  void _changeActiveLaw(String newLaw) {
    setState(() {
      _activeLaw = newLaw;
      _selectedAnswerIndex = null;
      _quizEvaluated = false;
      
      if (newLaw == "Boyle") {
        _temperature = 300.0;
        _volume = 2.0;
        _pressure = 1.0;
      } else if (newLaw == "Charles") {
        _pressure = 1.0;
        _temperature = 300.0;
        _volume = 2.0;
      } else if (newLaw == "Gay-Lussac") {
        _volume = 2.0;
        _temperature = 300.0;
        _pressure = 1.0;
      }
    });
  }

  @override
  void dispose() { 
    _controller.dispose(); 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Ideal Gas Laws Workbench"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.blur_on), text: "3. Simulation"),
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
          _buildChapterHeader("KINETIC THEORY & GAS LAWS", "NCERT Class 11 / JEE-NEET Core Focus"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is an Ideal Gas?",
            "An ideal gas is a theoretical gas composed of randomly moving point particles whose interactions are governed entirely by perfectly elastic collisions. It perfectly obeys the macroscopic ideal gas equation under all ranges of pressure, volume, and temperature parameters.",
            Palette.primaryDeep ?? Palette.primary
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Three Primary Gas Laws:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Boyle's Law (Isothermal):", "At constant temperature, the absolute volume of a fixed mass of gas is inversely proportional to its pressure parameter. (P1·V1 = P2·V2)"),
          _buildBulletPoint("Charles's Law (Isobaric):", "At constant system boundary pressure, the volume of an ideal gas expands linearly with absolute temperature changes. (V1/T1 = V2/T2)"),
          _buildBulletPoint("Gay-Lussac's Law (Isochoric):", "At constant enclosure volume, the absolute pressure exerted by a gas scales directly with its absolute temperature. (P1/T1 = P2/T2)"),
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
          _buildChapterHeader("THE IDEAL GAS DERIVATION", "Equation of State Framework"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Ideal Gas Combined Formula:\n""   P · V = n · R · T\n\n" 
              "2. Constant Temperature state (Boyle's Boundary Condition):\n" 
              "   P · V = Constant  =>  P ∝ 1/V\n\n" 
              "3. Constant Pressure state (Charles's Boundary Condition):\n" 
              "   V / T = Constant  =>  V ∝ T\n\n" 
              "4. Constant Volume state (Gay-Lussac's Boundary Condition):\n" 
              "   P / T = Constant  =>  P ∝ T\n\n" 
              "5. Dalton's Law of Partial Pressures:\n" 
              "   P_total = P1 + P2 + P3 + ... = (n_total · R · T) / V"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.cyanAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "High-Yield Exam Strategy:",
            "Always verify that temperatures are converted to Absolute Kelvin bounds before computing volume or pressure ratios.\n\n"
            "On graphs, Isothermal indicator curves (Boyle's hyperbolas) scale closer to the origin layout axis at lowered absolute temperatures.",
            Colors.blueGrey[950] ?? Colors.blueGrey
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Launch Kinetic Chamber Simulation ➡️"),
        ],
      ),
    );
  }

  Widget _buildSimulationTab() {
    return LayoutBuilder(builder: (context, constraints) {
      return SingleChildScrollView(
        child: ConstrainedBox(
          constraints: BoxConstraints(minHeight: constraints.maxHeight),
          child: IntrinsicHeight(
            child: Column(
              children: [
                Container(
                  width: double.infinity,
                  margin: const EdgeInsets.fromLTRB(12, 12, 12, 4),
                  padding: const EdgeInsets.symmetric(vertical: 6, horizontal: 8),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(8),
                    boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 2, offset: const Offset(0, 1))],
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      _buildLawToggleButton("Boyle (Const T)", "Boyle"),
                      const SizedBox(width: 8),
                      _buildLawToggleButton("Charles (Const P)", "Charles"),
                      const SizedBox(width: 8),
                      _buildLawToggleButton("Gay-Lussac (Const V)", "Gay-Lussac"),
                    ],
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text("💥 Pressure: ${_pressure.toStringAsFixed(2)} atm", style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                      Text("📦 Volume: ${_volume.toStringAsFixed(2)} L", style: TextStyle(color: Colors.blue, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                      Text("🔥 Temperature: ${_temperature.toStringAsFixed(0)} K", style: TextStyle(color: Colors.orange, fontWeight: FontWeight.bold, fontSize: 11, fontFamily: 'monospace')),
                    ],
                  ),
                ),
                SizedBox(
                  height: 220,
                  child: Container(
                    margin: const EdgeInsets.symmetric(horizontal: 12),
                    decoration: BoxDecoration(color: Colors.blueGrey[950], borderRadius: BorderRadius.circular(12)),
                    child: LayoutBuilder(builder: (context, boxConstraints) {
                      return CustomPaint(
                        size: Size(boxConstraints.maxWidth, boxConstraints.maxHeight),
                        painter: GasChamberPainter(
                          time: _time,
                          pressure: _pressure,
                          volume: _volume,
                          temperature: _temperature,
                          scaleRatio: boxConstraints.maxWidth / 400.0,
                        ),
                      );
                    }),
                  ),
                ),
                Container(
                  margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
                  decoration: BoxDecoration(color: Palette.primaryDeep, borderRadius: BorderRadius.circular(10)),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      Expanded(child: _buildTelemetry("CHAMBER VOLUME", "${_volume.toStringAsFixed(2)} L")),
                      Expanded(child: _buildTelemetry("KINETIC PRESSURE", "${_pressure.toStringAsFixed(2)} atm")),
                      Expanded(child: _buildTelemetry("THERMAL STATE", "${_temperature.toStringAsFixed(0)} K")),
                      Expanded(child: _buildTelemetry("STATE COEFFICIENT (PV/T)", "${((_pressure * _volume) / _temperature).toStringAsFixed(3)}")),
                    ],
                  ),
                ),
                _buildControlsTray(),
                const SizedBox(height: 12),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                  child: _buildSkipButton(3, "Move to Gas Laws Exam Drill ➡️"),
                ),
              ],
            ),
          ),
        ),
      );
    });
  }

  Widget _buildLawToggleButton(String title, String targetLaw) {
    bool isSelected = _activeLaw == targetLaw;
    return InkWell(
      onTap: () => _changeActiveLaw(targetLaw),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
        decoration: BoxDecoration(
          color: isSelected ? Palette.primaryDeep : Colors.grey[200],
          borderRadius: BorderRadius.circular(6),
          border: Border.all(color: isSelected ? (Palette.primaryDeep ?? Palette.primary) : Colors.transparent),
        ),
        child: Text(title, style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: isSelected ? Colors.white : Palette.primaryDeep)),
      ),
    );
  }

  Widget _buildTelemetry(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(label.toUpperCase(), textAlign: TextAlign.center, style: TextStyle(color: Colors.cyanAccent, fontSize: 8, fontWeight: FontWeight.bold, letterSpacing: 0.5)),
        const SizedBox(height: 4),
        Text(value, textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold, fontFamily: 'monospace')),
      ],
    );
  }

  Widget _buildControlsTray() {
    Widget firstControl;
    Widget secondControl;

    if (_activeLaw == "Boyle") {
      firstControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Volume (L)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _volume.clamp(1.0, 4.0), min: 1.0, max: 4.0, divisions: 6, activeColor: Colors.blue, onChanged: (val) => _updateSystemVariables("Volume", val)),
          ],
        ),
      );
      secondControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Pressure (atm)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _pressure.clamp(0.5, 2.0), min: 0.5, max: 2.0, divisions: 6, activeColor: Colors.red, onChanged: (val) => _updateSystemVariables("Pressure", val)),
          ],
        ),
      );
    } else if (_activeLaw == "Charles") {
      firstControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Temperature (K)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _temperature.clamp(150.0, 450.0), min: 150.0, max: 450.0, divisions: 6, activeColor: Colors.orange, onChanged: (val) => _updateSystemVariables("Temperature", val)),
          ],
        ),
      );
      secondControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Volume (L)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _volume.clamp(1.0, 3.0), min: 1.0, max: 3.0, divisions: 4, activeColor: Colors.blue, onChanged: (val) => _updateSystemVariables("Volume", val)),
          ],
        ),
      );
    } else {
      firstControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Temperature (K)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _temperature.clamp(150.0, 450.0), min: 150.0, max: 450.0, divisions: 6, activeColor: Colors.orange, onChanged: (val) => _updateSystemVariables("Temperature", val)),
          ],
        ),
      );
      secondControl = Expanded(
        child: Column(
          children: [
            Text(TrilingualService.instance.getUIText('Adjust Pressure (atm)'), style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
            Slider(value: _pressure.clamp(0.5, 2.25), min: 0.5, max: 2.25, divisions: 7, activeColor: Colors.red, onChanged: (val) => _updateSystemVariables("Pressure", val)),
          ],
        ),
      );
    }

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 12),
      padding: const EdgeInsets.all(8), 
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(8)),
      child: Row(
        children: [
          firstControl,
          secondControl,
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
          _buildGasQuiz(),
        ],
      ),
    );
  }

  Widget _buildGasQuiz() {
    bool isNeet = _targetPath == 'NEET';
    String questionText = isNeet
        ? "An ideal gas sample occupies 4.0 L at a pressure of 1.0 atm. If the container is compressed isothermally to 2.0 L, what is the new pressure reading?"
        : "An isobaric system boundary holds gas expanding from 300 K to 600 K temperature values. If the initial volumetric reading is V, what is the updated equilibrium configuration volume?";

    List<String> options = isNeet
        ? ["0.5 atm", "2.0 atm", "4.0 atm", "1.5 atm"]
        : ["V / 2", "V", "2V", "4V"];

    int correctIndex = isNeet ? 1 : 2; 

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(isNeet ? "NEET Gas State Quiz:" : "JEE Isobaric Progression Core Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 14)),
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
              activeColor: Palette.primaryDeep, 
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val)
            ),
          );
        }),
        const SizedBox(height: 12),
        if (!_quizEvaluated && _selectedAnswerIndex != null)
          uiFrameworkButton(),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50], borderRadius: BorderRadius.circular(8), border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red)),
            child: Text(
              _selectedAnswerIndex == correctIndex
                ? (isNeet 
                    ? "✅ CORRECT BALANCING EQUILIBRIUM:\n\nPer Boyle's Law rules at fixed temperatures: P1·V1 = P2·V2. Therefore: (1.0 atm)·(4.0 L) = P2·(2.0 L) which evaluates cleanly to P2 = 2.0 atm."
                    : "✅ CORRECT ISOBARIC COEFFICIENT:\n\nUnder Charles's Law framework parameters at fixed pressure conditions: V1/T1 = V2/T2. Dropping into algebraic substitution transforms to: V / 300 = V2 / 600 => V2 = 2V.")
                : "❌ MOLECULAR VELOCITY VECTOR ERROR:\n\nReview the Derivation Tab! Apply the baseline combined gas relation matrix (PV = nRT) to cleanly deduce invariant system conditions.",
              style: TextStyle(fontSize: 12, height: 1.4, fontFamily: 'monospace', color: Theme.of(context).colorScheme.onSurface),
            ),
          )
      ],
    );
  }

  Widget uiFrameworkButton() {
    return SizedBox(
      width: double.infinity, 
      child: ElevatedButton(
        onPressed: () => setState(() => _quizEvaluated = true), 
        style: ElevatedButton.styleFrom(backgroundColor: Palette.primaryDeep, padding: const EdgeInsets.symmetric(vertical: 12)), 
        child: Text(TrilingualService.instance.getUIText('Verify Gas Law Invariant Vectors'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
      )
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
}

class GasChamberPainter extends CustomPainter {
  final double time, pressure, volume, temperature, scaleRatio;
  GasChamberPainter({required this.time, required this.pressure, required this.volume, required this.temperature, required this.scaleRatio});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    final double canvasWidth = size.width / scaleRatio;
    final double canvasHeight = size.height / scaleRatio;

    double centerX = canvasWidth / 2.0;
    
    double chamberWidth = 160.0;
    double bottomY = canvasHeight - 15.0;
    double chamberHeight = volume * 38.0; 
    double topY = bottomY - chamberHeight;

    Paint wallPaint = Paint()..color = Colors.blueGrey[400]!..style = PaintingStyle.stroke..strokeWidth = 5.0;
    Path containerPath = Path()
      ..moveTo(centerX - chamberWidth / 2, bottomY - 150.0)
      ..lineTo(centerX - chamberWidth / 2, bottomY)
      ..lineTo(centerX + chamberWidth / 2, bottomY)
      ..lineTo(centerX + chamberWidth / 2, bottomY - 150.0);
    canvas.drawPath(containerPath, wallPaint);

    Paint pistonPaint = Paint()..color = Colors.blueGrey[700]!..style = PaintingStyle.fill;
    canvas.drawRect(Rect.fromLTWH(centerX - (chamberWidth / 2) + 2, topY - 6, chamberWidth - 4, 8), pistonPaint);
    canvas.drawRect(Rect.fromLTWH(centerX - 5, topY - 40, 10, 34), pistonPaint);

    double particleVelocity = (temperature / 300.0) * 8.0; 
    int absoluteParticlesCount = 18;
    
    math.Random randomGenerator = math.Random(42); 
    Paint particlePaint = Paint()..color = Colors.cyanAccent..style = PaintingStyle.fill;

    for (int index = 0; index < absoluteParticlesCount; index++) {
      double seedPhaseX = randomGenerator.nextDouble() * 2 * math.pi;
      double seedPhaseY = randomGenerator.nextDouble() * 2 * math.pi;
      
      double relativeX = 0.5 + 0.45 * math.sin(seedPhaseX + (time * particleVelocity));
      double relativeY = 0.5 + 0.45 * math.cos(seedPhaseY + (time * particleVelocity));

      double particleX = (centerX - chamberWidth / 2 + 10) + (relativeX * (chamberWidth - 20));
      double particleY = (topY + 6) + (relativeY * (chamberHeight - 12));

      canvas.drawCircle(Offset(particleX, particleY), 3.0, particlePaint);
    }

    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant GasChamberPainter oldDelegate) => true;
}