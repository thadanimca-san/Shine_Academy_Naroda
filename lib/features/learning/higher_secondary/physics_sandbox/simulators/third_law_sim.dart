import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ThirdLawSimulator extends StatefulWidget {
  const ThirdLawSimulator({Key? key}) : super(key: key);

  @override
  _ThirdLawSimulatorState createState() => _ThirdLawSimulatorState();
}

class _ThirdLawSimulatorState extends State<ThirdLawSimulator> with TickerProviderStateMixin {
  // Simulation Variables
  double _massCannon = 5.0;      // M (kg)
  double _massBall = 0.5;        // m (kg)
  double _muzzleVelocity = 25.0; // v (m/s)
  double _time = 0.0;
  bool _isFired = false;
  
  // Quiz Variables
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
      duration: const Duration(milliseconds: 2500)
    )..addListener(() {
        setState(() { 
          _time = _animationController.value * 2.5; 
        });
      });
  }

  void _fireCannon() { 
    setState(() { 
      _isFired = true; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    }); 
    _animationController.reset(); 
    _animationController.forward(); 
  }

  void _resetSimulation() { 
    setState(() { 
      _isFired = false; 
      _time = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
    }); 
    _animationController.reset(); 
  }

  @override
  void dispose() { 
    _animationController.dispose(); 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    // Dynamic Physics Calculations
    double g = 9.8;
    double mu = 0.4;
    double recoilVelocity = (_massBall * _muzzleVelocity) / _massCannon;
    double brakingAcc = mu * g; 
    double slideDist = (math.pow(recoilVelocity, 2)) / (2 * brakingAcc);

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Newton's 3rd Law Sandbox"), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
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
            Tab(icon: Icon(Icons.play_arrow), text: "3. Sandbox"),
            Tab(icon: Icon(Icons.assignment), text: "4. Test Prep"),
          ],
        ),
      ),
      body: SafeArea(
        child: TabBarView(
          controller: _tabController,
          children: [
            _buildIntroTab(),
            _buildFormulaTab(recoilVelocity, brakingAcc, slideDist),
            _buildSandboxTab(recoilVelocity, slideDist),
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
          _buildChapterHeader("ACTION-REACTION PAIRS", "NCERT Class 11 Physics | Laws of Motion"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Newton's Third Law?",
            "Newton's Third Law states that for every action, there is an equal and opposite reaction. This means forces always occur in pairs. If Object A exerts a force on Object B, Object B simultaneously exerts an equal and opposite force on Object A.",
            Colors.redAccent[700]!
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("Crucial Conceptual Pillars:"), style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Simultaneous Action:", "Action and reaction forces occur at the exact same instant; there is no time delay between them."),
          _buildBulletPoint("Different Bodies:", "The two forces always act on different objects. Because they act on different bodies, they never cancel each other out to produce static equilibrium."),
          _buildBulletPoint("Conservation of Momentum:", "As a direct consequence of this law, in the absence of external forces, the total momentum of a closed system remains perfectly conserved."),
          const SizedBox(height: 20),
          _buildSkipButton(1, "Review Equations ➡️"),
        ],
      ),
    );
  }

  // --- TAB 2: FORMULAS & DERIVATIONS ---
  Widget _buildFormulaTab(double recoilVelocity, double brakingAcc, double slideDist) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildChapterHeader("MATHEMATICAL FORMULATIONS", "Conservation of Momentum & Friction Kinematics"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. Action-Reaction Force Vector:\n""   F_action = -F_reaction\n\n" 
              "2. Conservation of Linear Momentum:\n" 
              "   P_initial = P_final = 0\n" 
              "   0 = (M * V_recoil) + (m * v_ball)\n" 
              "   V_recoil = - (m * v_ball) / M\n\n" 
              "3. Kinetic Retardation (Friction Work):\n" 
              "   f_k = μ * N = μ * M * g\n" 
              "   a_braking = f_k / M = μ * g\n" 
              "   Stopping Distance (d) = (V_recoil)² / (2 * a_braking)"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.amberAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "High-Yield Tip:",
            "Notice that the friction deceleration (a = μ * g) is completely independent of the cannon's mass! However, the total distance slid depends heavily on the mass, because mass dictates the initial recoil velocity (V_recoil).",
            Colors.blueGrey[900]!
          ),
          const SizedBox(height: 20),
          _buildSkipButton(2, "Open Sandbox Simulation ➡️"),
        ],
      ),
    );
  }

  // --- TAB 3: SANDBOX WORKSPACE ---
  Widget _buildSandboxTab(double recoilVelocity, double slideDist) {
    return Column(
      children: [
        // Live Visual Canvas Panel
        Expanded(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: Colors.orange[50],
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.orange[200]!),
            ),
            child: ClipRRect(
              child: LayoutBuilder(builder: (context, constraints) {
                return CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight), 
                  painter: CannonPhysicsPainter(
                    massCannon: _massCannon, 
                    massBall: _massBall, 
                    muzzleVelocity: _muzzleVelocity, 
                    time: _time, 
                    isFired: _isFired, 
                    scaleRatio: constraints.maxWidth / 400.0
                  ),
                );
              }),
            ),
          ),
        ),

        // Real-Time Telemetry Readouts
        Container(
          margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.grey[900],
            borderRadius: BorderRadius.circular(10),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTelemetry("Recoil Velocity (V)", "${recoilVelocity.toStringAsFixed(2)} m/s", Colors.redAccent),
              _buildTelemetry("Braking Accel. (a)", "3.92 m/s²", Colors.amberAccent),
              _buildTelemetry("Slide Distance (d)", "${slideDist.toStringAsFixed(3)} m", Colors.cyanAccent),
            ],
          ),
        ),

        // Shared Control Drawer
        _buildControlsTray(),
        const SizedBox(height: 8),
      ],
    );
  }

  // --- TAB 4: TEST PREP ---
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
          _isFired 
              ? _buildInteractiveQuiz() 
              : Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(color: Colors.red[50], borderRadius: BorderRadius.circular(12)),
                  child: Column(
                    children: [
                      Icon(Icons.play_circle_outline, color: Colors.redAccent[700], size: 48),
                      const SizedBox(height: 12),
                      Text(TrilingualService.instance.getUIText("Please launch the cannon in the 'Sandbox' tab first to generate the active trajectory and unlock the assessment!"),
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
                      ),
                    ],
                  ),
                ),
        ],
      ),
    );
  }

  // --- REUSABLE UI WIDGETS ---
  Widget _buildChapterHeader(String title, String subtitle) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.redAccent[700])),
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
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontWeight: FontWeight.bold, color: Colors.redAccent[700], fontSize: 16)),
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
          backgroundColor: Colors.redAccent[700], 
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

  Widget _buildInteractiveQuiz() {
    bool isNeet = _targetPath == 'NEET'; 
    double g = 9.8;
    double mu = 0.4;
    
    double recoilVelocity = (_massBall * _muzzleVelocity) / _massCannon;
    double brakingAcc = mu * g; 
    double slideDist = (math.pow(recoilVelocity, 2)) / (2 * brakingAcc);
    
    String questionText = isNeet 
        ? "What is the instantaneous recoil speed of the cannon immediately after firing?" 
        : "Assuming the ground has a friction coefficient of μ = 0.4, how far will the cannon slide backward before stopping?";
    
    List<String> options = isNeet 
        ? ["0.00 m/s", "${recoilVelocity.toStringAsFixed(2)} m/s", "${(recoilVelocity * 2.5).toStringAsFixed(2)} m/s", "Equal to ball velocity (${_muzzleVelocity.toStringAsFixed(0)} m/s)"] 
        : ["${slideDist.toStringAsFixed(3)} m", "${(slideDist * 1.5).toStringAsFixed(3)} m", "0.000 m", "${(slideDist + 0.35).toStringAsFixed(3)} m"];
    
    int correctIndex = isNeet ? 1 : 0;
    
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(isNeet ? "NEET Momentum Question:" : "JEE Work-Energy Friction Challenge:", style: TextStyle(fontWeight: FontWeight.bold, color: isNeet ? Colors.green[700] : Colors.deepOrange, fontSize: 13)),
        const SizedBox(height: 4),
        Text(questionText, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600)),
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
              activeColor: Colors.redAccent, 
              onChanged: _quizEvaluated ? null : (val) => setState(() => _selectedAnswerIndex = val)
            ),
          );
        }),
        const SizedBox(height: 8),
        if (!_quizEvaluated && _selectedAnswerIndex != null) 
          SizedBox(
            width: double.infinity, 
            child: ElevatedButton(
              onPressed: () => setState(() => _quizEvaluated = true), 
              style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent, padding: const EdgeInsets.symmetric(vertical: 12)), 
              child: Text(TrilingualService.instance.getUIText('Check Answer'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
            )
          ),
        if (_quizEvaluated)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: _selectedAnswerIndex == correctIndex ? Colors.green[50] : Colors.red[50],
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: _selectedAnswerIndex == correctIndex ? Colors.green : Colors.redAccent, width: 1),
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
                  _getDerivationExplanation(isNeet, _selectedAnswerIndex ?? 0, _massCannon, _massBall, _muzzleVelocity, recoilVelocity, slideDist),
                  style: TextStyle(fontSize: 12, height: 1.4, color: Theme.of(context).colorScheme.onSurface, fontFamily: 'monospace'),
                ),
              ],
            ),
          )
      ],
    );
  }

  String _getDerivationExplanation(bool isNeet, int selected, double M, double m, double v, double vRecoil, double dSlide) {
    if (isNeet) {
      switch (selected) {
        case 1: // Correct
          return "✨ ACTION-REACTION MOMENTUM DERIVATION:\n\n"
                 "1. Conservation of Linear Momentum:\n"
                 "   Since no external horizontal force acts on the cannon-ball system during explosive discharge, total initial momentum equals final momentum:\n"
                 "   P_initial = P_final = 0\n\n"
                 "2. Vector Velocity Balance:\n"
                 "   0 = (M · V_recoil) + (m · v_ball)\n"
                 "   M · V_recoil = - (m · v_ball) ⟶ V_recoil = - (m · v_ball) / M\n\n"
                 "3. Value Substitution:\n"
                 "   V = ($m kg · $v m/s) / $M kg = ${vRecoil.toStringAsFixed(2)} m/s.\n\n"
                 "The negative sign confirms that the recoil direction is opposite to the shell trajectory vector.";
        case 0:
          return "❌ MOMENTUM VIOLATION DETECTED:\n\n"
                 "• The Trap:\n"
                 "  Assuming the cannon stays completely still (0.00 m/s).\n\n"
                 "• The Physics Proof:\n"
                 "  If the cannon did not move backward, the net system momentum after firing would point forward. This violates Newton's Third Law: the forward gas expansion force pushing the ball must generate an equal and opposite backward force against the rear wall of the chamber.";
        case 2:
          return "❌ OVERESTIMATION ERROR:\n\n"
                 "• The Trap:\n"
                 "  Using an escalated speed scaling calculation (${(vRecoil * 2.5).toStringAsFixed(2)} m/s).\n\n"
                 "• The Physics Proof:\n"
                 "  This velocity violates conservation of energy. Because the cannon contains a high inertia block (\$M kg\$), it restricts structural speed trends. Excess movement speed would imply that energy was added to the system out of nowhere.";
        default:
          return "❌ COUPLING ERROR:\n\n"
                 "• The Trap:\n"
                 "  Assuming the cannon recoils at the same speed as the bullet (\$v\$ m/s).\n\n"
                 "• The Physics Proof:\n"
                 "  Equal speeds occur *only* if the cannon and ball have identical masses (\$M = m\$). Because the cannon is much heavier, its structural inertia resists acceleration, resulting in a lower recoil velocity.";
      }
    } else {
      switch (selected) {
        case 0: // Correct
          return "✨ JEE WORK-ENERGY DERIVATION MATRIX:\n\n"
                 "1. Compute Post-Explosion Recoil Kinematics:\n"
                 "   From linear momentum conservation, the starting backward velocity is:\n"
                 "   V_0 = (m · v) / M = ${vRecoil.toStringAsFixed(2)} m/s\n\n"
                 "2. Isolate Kinetic Retardation Force:\n"
                 "   Friction acts as the sole negative horizontal force: f = \u03BC · N = \u03BC · M · g\n"
                 "   Braking deceleration: a_brake = f / M = \u03BC · g = 0.4 · 9.8 = 3.92 m/s\u00B2\n\n"
                 "3. Work-Energy Theorem Verification:\n"
                 "   The work done by friction converts all kinetic energy into thermal energy:\n"
                 "   Work_friction = \u0394KE ⟶ f · d = \u00BD · M · (V_0)\u00B2\n"
                 "   (\u03BC · M · g) · d = \u00BD · M · (V_0)\u00B2 ⟶ d = (V_0)\u00B2 / (2 · \u03BC · g)\n\n"
                 "4. Evaluation:\n"
                 "   d = (${vRecoil.toStringAsFixed(2)})\u00B2 / (2 · 3.92) = ${dSlide.toStringAsFixed(3)} meters.\n\n"
                 "This clarifies how energy dissipation depends directly on the square of the initial momentum value.";
        case 1:
          return "❌ COEFFICIENT SCALING PITFALL:\n\n"
                 "• The Trap:\n"
                 "  Overestimating displacement via an unweighted linear offset factor (${(dSlide * 1.5).toStringAsFixed(3)} m).\n\n"
                 "• The Physics Proof:\n"
                 "  Frictional energy loss is bound strictly by the normal force. Artificially increasing the slide distance implies a lower coefficient of friction than the specified \u03BC = 0.4.";
        case 2:
          return "❌ THE STATIC FIRE RECOIL TRAP:\n\n"
                 "• The Trap:\n"
                 "  Assuming the cannon does not slide at all (0.000 m).\n\n"
                 "• The Physics Proof:\n"
                 "  The explosive force generates an instantaneous non-zero initial velocity (\$V_0\$). Because the system is already in motion, static friction cannot prevent it from sliding; instead, kinetic friction opposes the movement until it drains the cannon's kinetic energy.";
        default:
          return "❌ ALGEBRAIC OFFSET TRAP:\n\n"
                 "• The Trap:\n"
                 "  Miscalculating the work-energy relation, leading to an incorrect result (${(dSlide + 0.35).toStringAsFixed(3)} m).\n\n"
                 "• The Physics Proof:\n"
                 "  This error typically stems from adding the friction coefficient directly to the displacement instead of dividing by it, which violates basic dimensional analysis.";
      }
    }
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6), 
      color: Colors.white,
      child: Column(
        children: [
          Row(
            children: [
              Expanded(
                child: Column(
                  children: [
                    Text('Cannon (M): ${_massCannon.toStringAsFixed(1)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                    Slider(
                      value: _massCannon, 
                      min: 3.0, 
                      max: 10.0, 
                      divisions: 7, 
                      activeColor: Colors.redAccent, 
                      onChanged: _isFired ? null : (val) => setState(() => _massCannon = val)
                    )
                  ],
                ),
              ),
              Expanded(
                child: Column(
                  children: [
                    Text('Ball (m): ${_massBall.toStringAsFixed(2)} kg', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                    Slider(
                      value: _massBall, 
                      min: 0.1, 
                      max: 1.0, 
                      divisions: 9, 
                      activeColor: Colors.orange, 
                      onChanged: _isFired ? null : (val) => setState(() => _massBall = val)
                    )
                  ],
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly, 
            children: [
              ElevatedButton(
                onPressed: _isFired ? null : _fireCannon, 
                style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent), 
                child: Text(TrilingualService.instance.getUIText('Fire Cannon'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))
              ), 
              IconButton(
                onPressed: _resetSimulation, 
                icon: Icon(Icons.refresh), 
                color: Colors.grey[800]
              )
            ],
          ),
        ],
      ),
    );
  }
}

class CannonPhysicsPainter extends CustomPainter {
  final double massCannon, massBall, muzzleVelocity, time, scaleRatio; 
  final bool isFired;
  
  CannonPhysicsPainter({
    required this.massCannon, 
    required this.massBall, 
    required this.muzzleVelocity, 
    required this.time, 
    required this.isFired, 
    required this.scaleRatio
  });

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    
    final double virtualWidth = size.width / scaleRatio; 
    final double groundY = (size.height / scaleRatio) - 20.0;
    
    // Draw Ground
    canvas.drawLine(Offset(0, groundY), Offset(virtualWidth, groundY), Paint()..color = Colors.black87..strokeWidth = 2.0);
    
    double initialCannonX = virtualWidth * 0.45; 
    double cannonRecoilX = initialCannonX; 
    double ballX = initialCannonX + 45.0;
    
    if (isFired) {
      double vRecoil = (massBall * muzzleVelocity) / massCannon;
      double tStop = vRecoil / 3.92;
      double tCannon = math.min(time, tStop);
      
      double cannonSlideDist = (vRecoil * tCannon) - (0.5 * 3.92 * math.pow(tCannon, 2));
      cannonRecoilX = initialCannonX - (cannonSlideDist * 5.0); 
      
      ballX = (initialCannonX + 45.0) + (muzzleVelocity * time * 5.0);
    }
    
    // Draw Cannon Body
    canvas.drawRect(Rect.fromLTWH(cannonRecoilX, groundY - 26, 50, 18), Paint()..color = Colors.blueGrey[800]!);
    // Draw Cannon Wheels
    canvas.drawCircle(Offset(cannonRecoilX + 12, groundY - 4), 5, Paint()..color = Colors.black);
    canvas.drawCircle(Offset(cannonRecoilX + 38, groundY - 4), 5, Paint()..color = Colors.black);
    
    // Draw Ball Node if in frame
    if (isFired && ballX < virtualWidth) {
      canvas.drawCircle(Offset(ballX, groundY - 17), 5, Paint()..color = Colors.redAccent);
    }
    
    canvas.restore();
  }
  
  @override
  bool shouldRepaint(covariant CannonPhysicsPainter oldDelegate) => true;
}