import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class FrictionLabWorkspace extends StatelessWidget {
  const FrictionLabWorkspace({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const FrictionSimulator();
  }
}

class FrictionSimulator extends StatefulWidget {
  const FrictionSimulator({Key? key}) : super(key: key);

  @override
  _FrictionSimulatorState createState() => _FrictionSimulatorState();
}

class _FrictionSimulatorState extends State<FrictionSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _mass = 5.0;            
  double _muStatic = 0.50;        
  double _muKinetic = 0.35;      
  double _appliedForce = 0.0;    
  
  late TabController _tabController;
  
  String _targetPath = 'NEET'; 
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  int _activeExplanationTab = 0;

  final double g = 9.8;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
  }

  void _resetSimulation() {
    setState(() { 
      _appliedForce = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
      _activeExplanationTab = 0;
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
        title: Text(TrilingualService.instance.getUIText("Friction Dynamics Sandbox"), 
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)
        ), 
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
            Tab(icon: Icon(Icons.functions), text: "2. Physics"),
            Tab(icon: Icon(Icons.play_arrow), text: "3. Sim"),
            Tab(icon: Icon(Icons.assignment), text: "4. Drill"),
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

  // --- TAB 1: INTRODUCTION VIEW ---
  Widget _buildIntroductionTab() {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("FRICTIONAL FORCES IN MECHANICS", "Contact Mechanics, Normal Interlocking, & Yield Limits"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Friction?",
            "Friction is the electromagnetic contact force that opposes the relative motion or the tendency of relative motion between two surfaces in contact. Rather than simply opposing motion globally, its primary directive is to resist microscopic sliding between interfaces.",
            Colors.blueAccent
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Three Distinct Operational Regimes:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Static Friction (f_s):", "A self-adjusting, passive force that keeps a system locked at rest. It matches the applied external force component 1:1 up until it hits its threshold limit structural capacity."),
          _buildBulletPoint("Limiting Friction (f_l):", "The maximum possible structural resistance value of static friction. Once the applied external force exceeds this exact ceiling value, the microscopic surface interlock yields permanently."),
          _buildBulletPoint("Kinetic Friction (f_k):", "The kinetic drag profile active once steady relative sliding breaks out. Crucially, kinetic friction is a constant value and is mathematically lower than limiting static structural values."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "View Frame Derivations ➡️"),
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
          _buildChapterHeader("THE CONTACT DECOUPLING MATHEMATICAL MATRIX", "Threshold Yield Equations & Net Accel Frameworks"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Normal Force Balance (Vertical equilibrium):\n""   N = m · g\n\n" 
              "2. Limiting Static Threshold Ceiling Formula:\n" 
              "   f_s_max = μ_static · N = μ_static · m · g\n\n" 
              "3. Operational State 1 (At Rest Condition: F_applied <= f_s_max):\n" 
              "   Friction acts as a passive reactive balancer.\n" 
              "   f_actual = F_applied\n" 
              "   F_net = F_applied - f_actual = 0\n" 
              "   Acceleration (a) = 0.00 m/s²\n\n" 
              "4. Operational State 2 (Sliding Breakout: F_applied > f_s_max):\n" 
              "   Microscopic teeth yield. System switches to constant kinetic drag.\n" 
              "   f_actual = f_kinetic = μ_kinetic · N\n" 
              "   F_net = F_applied - f_kinetic\n" 
              "   Acceleration (a) = F_net / m = (F_applied - μ_kinetic·m·g) / m"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE-NEET Mechanics Takeaway:",
            "• Static friction is a variable scalar, NOT a fixed product equation (0 <= f_s <= μ_s·N).\n"
            "• Kinetic friction values sit lower than static yields because surface peaks glide over troughs without fully interlocking.\n"
            "• Transition graphs represent a non-differentiable sharp point drop right at structural failure limits.",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Run Physics Sandbox Sim ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SIMULATION VIEW ---
  Widget _buildSimulationTab() {
    double normalForce = _mass * g;
    double maxStaticFriction = _muStatic * normalForce;
    double kineticFriction = _muKinetic * normalForce;

    double actualFriction;
    bool isMoving;
    double netForce;

    if (_appliedForce <= maxStaticFriction) {
      actualFriction = _appliedForce; 
      isMoving = false;
      netForce = 0.0;
    } else {
      actualFriction = kineticFriction; 
      isMoving = true;
      netForce = _appliedForce - kineticFriction;
    }

    double acceleration = isMoving ? netForce / _mass : 0.0;

    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(vertical: 8),
          color: Colors.blue[50],
          child: Text(
            isMoving 
                ? "Status: SLIDING! (Kinetic Drag Overriding)" 
                : _appliedForce > 0 
                    ? "Status: STATIC LOCK (Resisting Force Match)" 
                    : "Status: Equilibrium (Ready on Pad)",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Colors.blue[900]),
          ),
        ),
        Expanded(
          flex: 42,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.lightBlue[50], borderRadius: BorderRadius.circular(12)),
            child: ClipRRect(
              child: LayoutBuilder(builder: (context, constraints) {
                return CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: FrictionPhysicsPainter(
                    mass: _mass,
                    appliedForce: _appliedForce,
                    actualFriction: actualFriction,
                    maxStaticFriction: maxStaticFriction,
                    kineticFriction: kineticFriction,
                    isMoving: isMoving,
                  ),
                );
              }),
            ),
          ),
        ),
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
          padding: const EdgeInsets.symmetric(vertical: 14),
          decoration: BoxDecoration(
            color: Colors.white, 
            borderRadius: BorderRadius.circular(10),
            border: Border.all(color: Colors.grey[300]!, width: 1),
            boxShadow: [
              BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 4, offset: const Offset(0, 2))
            ]
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(child: _buildTelemetryCard("Normal (N)", "${normalForce.toStringAsFixed(1)} N")),
              Expanded(child: _buildTelemetryCard("Friction (f)", "${actualFriction.toStringAsFixed(1)} N")),
              Expanded(child: _buildTelemetryCard("Accel (a)", "${acceleration.toStringAsFixed(2)} m/s²")),
            ],
          ),
        ),
        _buildControlsTray(),
        const Spacer(),
        Padding(
          padding: const EdgeInsets.only(bottom: 8.0),
          child: _buildSkipButton(3, "Challenge Competitive Exam Drill ➡️"),
        ),
      ],
    );
  }

  // --- TAB 4: EXAM ASSESSMENT VIEW ---
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
                    _activeExplanationTab = 0;
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
          _buildInteractiveQuiz(),
        ],
      ),
    );
  }

  // --- WIDGET GENERATION HELPERS ---
  Widget _buildTelemetryCard(String label, String value) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Text(
          label.toUpperCase(), 
          textAlign: TextAlign.center,
          style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 11, fontWeight: FontWeight.bold, letterSpacing: 0.5)
        ),
        const SizedBox(height: 4),
        Text(
          value, 
          textAlign: TextAlign.center,
          style: TextStyle(color: Theme.of(context).colorScheme.onSurface, fontSize: 14, fontWeight: FontWeight.bold, fontFamily: 'monospace')
        ),
      ],
    );
  }

  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.blueAccent[700])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.blueAccent[700], fontSize: 16)),
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
          backgroundColor: Colors.blueAccent[700], 
          foregroundColor: Colors.white, 
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10)
        ),
        child: Text(prompt, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
      ),
    );
  }

  Widget _buildControlsTray() {
    return Container(
      margin: const EdgeInsets.all(12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white, 
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.grey[200]!)
      ),
      child: Column(
        children: [
          _buildSliderInput("Mass (m)", _mass, 2.0, 10.0, 4, "kg", (val) => setState(() => _mass = val)),
          _buildSliderInput("μ (Static)", _muStatic, 0.40, 0.80, 4, "", (val) {
            setState(() {
              _muStatic = val;
              if (_muKinetic >= _muStatic) _muKinetic = _muStatic - 0.05;
            });
          }),
          _buildSliderInput("μ (Kinetic)", _muKinetic, 0.20, 0.60, 4, "", (val) {
            setState(() => _muKinetic = math.min(val, _muStatic - 0.05));
          }),
          const Divider(height: 16),
          Row(
            children: [
              SizedBox(
                width: 110,
                child: Text("Push: ${_appliedForce.toStringAsFixed(0)} N", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
              ),
              Expanded(
                child: Slider(
                  value: _appliedForce,
                  min: 0,
                  max: 60,
                  divisions: 30,
                  activeColor: Colors.redAccent,
                  inactiveColor: Colors.red.withValues(alpha: 0.15),
                  onChanged: (val) => setState(() => _appliedForce = val),
                ),
              ),
              IconButton(
                icon: Icon(Icons.refresh, color: Colors.blueAccent, size: 20),
                onPressed: _resetSimulation,
              )
            ],
          )
        ],
      ),
    );
  }

  Widget _buildSliderInput(String label, double val, double min, double max, int div, String unit, ValueChanged<double> callback) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2.0),
      child: Row(
        children: [
          SizedBox(
            width: 110,
            child: Text("$label: ${val.toStringAsFixed(2)} $unit", style: TextStyle(fontSize: 11, fontWeight: FontWeight.w600)),
          ),
          Expanded(
            child: Slider(
              value: val,
              min: min,
              max: max,
              divisions: div,
              activeColor: Colors.blueAccent[700],
              onChanged: callback,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInteractiveQuiz() {
    bool isNeet = _targetPath == 'NEET'; 
    double normalForce = _mass * g;
    double maxStatic = _muStatic * normalForce;
    double halfStatic = maxStatic / 2;

    String questionText = isNeet 
        ? "If you apply an external horizontal force exactly equal to half of the maximum static friction limit (${halfStatic.toStringAsFixed(1)} N), what will be the magnitude of friction acting on the crate?" 
        : "Suppose a horizontal push force of 50 N acts on the block. If sliding motion breaks out across the threshold boundaries, what is the net acceleration framework formula?";
    
    List<String> options = isNeet 
        ? ["0.0 N", "${(_muKinetic * normalForce).toStringAsFixed(1)} N", "${halfStatic.toStringAsFixed(1)} N", "${maxStatic.toStringAsFixed(1)} N"] 
        : ["a = (50 - \u03BC_k·m·g) / m", "a = (50 - \u03BC_s·m·g) / m", "a = 50 / m", "0.00 m/s\u00B2"];
    
    int correctIndex = isNeet ? 2 : 0;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          isNeet ? "NEET Statics Question:" : "JEE Dynamics Challenge:", 
          style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)
        ),
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
              title: Text(options[index], style: TextStyle(fontSize: 12, fontWeight: FontWeight.w500, color: Theme.of(context).colorScheme.onSurface)), 
              activeColor: Colors.blueAccent, 
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blueAccent[700], padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Evaluate Trajectory Proofs'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Row(
                  children: [
                    Icon(
                      _selectedAnswerIndex == correctIndex ? Icons.check_circle : Icons.cancel, 
                      color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.red, 
                      size: 18
                    ),
                    const SizedBox(width: 8),
                    Text(
                      _selectedAnswerIndex == correctIndex ? "CORRECT CONCEPT DERIVATION" : "DEEP CONCEPT BREAKDOWN",
                      style: TextStyle(
                        fontWeight: FontWeight.bold, 
                        color: _selectedAnswerIndex == correctIndex ? Colors.green[800] : Colors.red[800], 
                        fontSize: 11
                      ),
                    ),
                  ],
                ),
                const Divider(height: 12),
                Container(
                  color: Colors.grey[200],
                  child: Row(
                    children: [
                      _buildTabButton(0, "Concept"),
                      _buildTabButton(1, "Mathematical"),
                      _buildTabButton(2, "Real-World"),
                      _buildTabButton(3, "Mistake Tracker"),
                    ],
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(12.0),
                  child: Text(
                    _getTabExplanation(isNeet, _selectedAnswerIndex ?? 0, _activeExplanationTab, maxStatic, halfStatic),
                    style: TextStyle(fontSize: 12, height: 1.4, color: Theme.of(context).colorScheme.onSurface, fontFamily: 'monospace'),
                  ),
                ),
              ],
            ),
          )
      ],
    );
  }

  Widget _buildTabButton(int index, String label) {
    bool isActive = _activeExplanationTab == index;
    return Expanded(
      child: InkWell(
        onTap: () {
          setState(() {
            _activeExplanationTab = index;
          });
        },
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 8),
          decoration: BoxDecoration(
            color: isActive ? Colors.white : Colors.transparent,
            border: Border(
              bottom: BorderSide(
                color: isActive ? Colors.blueAccent : Colors.transparent, 
                width: 2.5
              )
            )
          ),
          child: Text(
            label,
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 10, 
              fontWeight: FontWeight.bold, 
              color: isActive ? Colors.blueAccent : Colors.grey[700]
            ),
          ),
        ),
      ),
    );
  }

  String _getTabExplanation(bool isNeet, int selected, int tabIndex, double maxStatic, double halfStatic) {
    if (isNeet) {
      switch (selected) {
        case 2: 
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — PASSIVE FORCE MATCHING:\n\n"
                   "• Static friction is completely passive and self-adjusting.\n"
                   "• It balances the applied force identically up until the limiting ceiling value.\n"
                   "• Since the push force is exactly ${halfStatic.toStringAsFixed(1)} N, which is below the threshold limits, the system does not budge.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Structural ceiling: f_s_max = ${maxStatic.toStringAsFixed(1)} N\n"
                   "• Force condition: F_push = ${halfStatic.toStringAsFixed(1)} N <= f_s_max\n"
                   "• Static equilibrium demands: F_net = 0\n"
                   "  F_push - f_actual = 0 → f_actual = F_push = ${halfStatic.toStringAsFixed(1)} N.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• If you lightly push a heavy wardrobe, it doesn't suddenly slide backwards or jump forwards.\n"
                   "• The microscopic surface weld structure scales up its defensive opposition perfectly to negate whatever force you throw at it.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• The formula trap: Students frequently memorize 'f = μ·N' and apply it indiscriminately.\n"
                   "• Never calculate maximum threshold constants unless you are certain the applied force has exceeded that capacity boundary.";
          }
        default:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — STATIC LOCK BREAKDOWN:\n\n"
                   "• Selecting formulas out of context leads to kinetic or null tracking values.\n"
                   "• Friction cannot exceed the applied force in a stationary system, otherwise the object would spontaneously accelerate backwards without propulsion!";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• If friction equaled the maximum limit value (${maxStatic.toStringAsFixed(1)} N) while the push force stayed low at ${halfStatic.toStringAsFixed(1)} N:\n"
                   "  F_net = ${halfStatic.toStringAsFixed(1)} - ${maxStatic.toStringAsFixed(1)} < 0\n"
                   "• This net value creates a backwards accelerating system without energy input, completely violating the First Law of Thermodynamics.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• Surfaces are passive components. They provide deceleration or anchoring support, but they can never generate autonomous kinetic velocity lines on their own.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Blind substitution failure: Forgetting to verify whether the horizontal force threshold boundaries have yielded prior to extracting coefficient variables.";
          }
      }
    } else {
      switch (selected) {
        case 0: 
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — KINETIC BREAKOUT OVERRIDE:\n\n"
                   "• Once motion begins, the initial static boundaries expire permanently.\n"
                   "• The interface structural parameters scale directly into a steady-state dynamic friction resistance model.\n"
                   "• The kinetic drag vector acts completely separate from static coefficients.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• F_net vector calculation along horizontal coordinate track:\n"
                   "  F_net = F_applied - f_kinetic = 50 - (μ_kinetic · m · g)\n"
                   "• From Newton's Second Law (F = m · a):\n"
                   "  a = F_net / m = (50 - μ_kinetic · m · g) / m.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• This explains why it takes less effort to keep a heavy crate moving than it does to break it loose from rest initially.\n"
                   "• The operational acceleration curve instantly increases upon slipping boundaries.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• The standard coefficient error: Accidentally keeping the static parameter configuration variable 'μ_s' active within kinetic sliding equations.";
          }
        default:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — PROFILE INVALIDATION:\n\n"
                   "• Post-yield configurations cannot map static profiles onto dynamic acceleration frameworks.\n"
                   "• An accelerating platform is completely decoupled from static threshold metrics.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Setting a = 0 assumes the structural limit wasn't breached, but a 50 N force exceeds typical low-mass static structural thresholds.\n"
                   "• Using μ_static calculations over-penalizes the work framework, yielding incorrect acceleration values.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• When tires skid on asphalt during extreme braking scenarios, calculations rely entirely on sliding friction metrics rather than maximum static traction profiles.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Static configuration carry-over trap: Forgetting that microscopic contact tracks change structure dynamically upon macroscopic sliding transitions.";
          }
      }
    }
  }
}

class FrictionPhysicsPainter extends CustomPainter {
  final double mass, appliedForce, actualFriction, maxStaticFriction, kineticFriction; 
  final bool isMoving;

  FrictionPhysicsPainter({
    required this.mass, 
    required this.appliedForce, 
    required this.actualFriction, 
    required this.maxStaticFriction, 
    required this.kineticFriction, 
    required this.isMoving,
  });

  @override
  void paint(Canvas canvas, Size size) {
    double floorY = size.height * 0.35;

    // 1. Draw Surface Floor
    canvas.drawLine(Offset(0, floorY), Offset(size.width, floorY), Paint()..color = Colors.black87..strokeWidth = 2.5);

    // 2. Render Crate
    double boxWidth = 55.0 + (mass * 1.5);
    double boxHeight = 35.0;
    double boxX = (size.width * 0.15);
    double boxY = floorY - boxHeight;
    canvas.drawRect(Rect.fromLTWH(boxX, boxY, boxWidth, boxHeight), Paint()..color = Colors.orange[800]!);

    // Force Vector Arrows
    if (appliedForce > 0) {
      _drawArrow(canvas, Offset(boxX - 35, boxY + boxHeight / 2), Offset(boxX - 5, boxY + boxHeight / 2), Colors.redAccent, 3.0);
    }
    if (actualFriction > 0) {
      double arrowLen = (actualFriction * 1.5).clamp(10.0, 60.0);
      _drawArrow(canvas, Offset(boxX + 15, floorY), Offset(boxX + 15 - arrowLen, floorY), Colors.blueAccent, 3.0);
    }

    // 3. Classical Friction Transition Chart
    double graphX = 45.0;
    double graphY = size.height - 20.0;
    double graphW = size.width - 75.0;
    double graphH = (size.height - floorY) - 45.0;

    Paint axisPaint = Paint()..color = Colors.grey.shade700..strokeWidth = 1.2;
    canvas.drawLine(Offset(graphX, graphY), Offset(graphX + graphW, graphY), axisPaint); 
    canvas.drawLine(Offset(graphX, graphY), Offset(graphX, graphY - graphH), axisPaint); 

    // Compute plot bounds
    double peakX = graphX + (maxStaticFriction * 2.2).clamp(20.0, graphW * 0.45);
    double peakY = graphY - (maxStaticFriction * 1.2).clamp(15.0, graphH * 0.8);
    double dropY = graphY - (kineticFriction * 1.2).clamp(10.0, graphH * 0.7);
    double endX = graphX + graphW;

    Path curvePath = Path()
      ..moveTo(graphX, graphY)
      ..lineTo(peakX, peakY)
      ..lineTo(peakX + 10, dropY)
      ..lineTo(endX, dropY);
    
    canvas.drawPath(curvePath, Paint()..color = Colors.grey.withValues(alpha: 0.4)..strokeWidth = 2..style = PaintingStyle.stroke);

    // Dynamic Tracking Node Placement
    double dotX; double dotY;
    if (!isMoving) {
      dotX = graphX + (appliedForce * 2.2).clamp(0.0, peakX - graphX);
      dotY = graphY - (appliedForce * 1.2).clamp(0.0, graphY - peakY);
    } else {
      dotX = (graphX + (appliedForce * 2.2)).clamp(peakX + 10, endX);
      dotY = dropY;
    }

    canvas.drawCircle(Offset(dotX, dotY), 5.0, Paint()..color = isMoving ? Colors.amber[800]! : Colors.green[700]!);
  }

  void _drawArrow(Canvas canvas, Offset start, Offset end, Color color, double weight) {
    Paint p = Paint()..color = color..strokeWidth = weight..style = PaintingStyle.stroke;
    canvas.drawLine(start, end, p);
    double angle = math.atan2(end.dy - start.dy, end.dx - start.dx);
    canvas.drawLine(end, Offset(end.dx - 6 * math.cos(angle - math.pi / 6), end.dy - 6 * math.sin(angle - math.pi / 6)), p);
    canvas.drawLine(end, Offset(end.dx - 6 * math.cos(angle + math.pi / 6), end.dy - 6 * math.sin(angle + math.pi / 6)), p);
  }

  @override
  bool shouldRepaint(covariant FrictionPhysicsPainter oldDelegate) => true;
}