import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class FirstLawSimulator extends StatefulWidget {
  const FirstLawSimulator({Key? key}) : super(key: key);

  @override
  _FirstLawSimulatorState createState() => _FirstLawSimulatorState();
}

class _FirstLawSimulatorState extends State<FirstLawSimulator> with TickerProviderStateMixin {
  // Physical parameters
  double _initialVelocity = 15.0; 
  double _time = 0.0;
  bool _isMoving = false;
  bool _hasBraked = false;
  double _brakeTime = 0.0; 
  
  late AnimationController _physicsController;
  late TabController _tabController;
  
  String _targetPath = 'NEET'; 
  int? _selectedAnswerIndex;
  bool _quizEvaluated = false;
  int _activeExplanationTab = 0;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    
    _physicsController = AnimationController(
      vsync: this, 
      duration: const Duration(milliseconds: 2500)
    )..addListener(() {
        setState(() { 
          _time = _physicsController.value * 5.0; 
        });
      });
  }

  void _startCart() {
    setState(() { 
      _isMoving = true; 
      _hasBraked = false; 
      _brakeTime = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
      _activeExplanationTab = 0;
    });
    _physicsController.reset(); 
    _physicsController.forward();
  }

  void _applySuddenBrake() {
    setState(() { 
      _hasBraked = true; 
      _brakeTime = _time; 
    });
  }

  void _resetSimulation() {
    setState(() { 
      _isMoving = false; 
      _hasBraked = false; 
      _time = 0.0; 
      _brakeTime = 0.0; 
      _selectedAnswerIndex = null; 
      _quizEvaluated = false; 
      _activeExplanationTab = 0;
    });
    _physicsController.reset();
  }

  @override
  void dispose() { 
    _physicsController.dispose(); 
    _tabController.dispose();
    super.dispose(); 
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText("Newton's 1st Law Sandbox"), 
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
          _buildChapterHeader("NEWTON'S FIRST LAW OF MOTION", "The Foundational Pillar of Classical Mechanics"),
          const SizedBox(height: 12),
          _buildConceptCard(
            "What is Inertia?",
            "Inertia is the inherent property of all physical matter by virtue of which it resists any change in its state of rest or of uniform motion along a straight line. Newton's First Law defines this relationship qualitatively by stating that an object's state cannot alter without an external unbalanced force.",
            Colors.blueAccent
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText("The Three Distinct Forms of Inertia:"), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 6),
          _buildBulletPoint("Inertia of Rest:", "An object at rest stays at rest. For example, when a carpet is beaten with a stick, the dust particles fly off because they struggle to remain stationary while the fibers move."),
          _buildBulletPoint("Inertia of Motion:", "An object in uniform motion resists slowing down or changing speed. This is modeled in our sandbox when the trolley brakes but the free block continues flying forward at constant speed."),
          _buildBulletPoint("Inertia of Direction:", "An object resists changing its path of travel. For example, passengers lean sideways in a car when it takes a sudden sharp curve because their bodies attempt to keep traveling in a straight line."),
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
          _buildChapterHeader("THE MATHEMATICAL REFERENCE FRAME MATRIX", "Inertial vs. Non-Inertial Coordinates"),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.grey[900], borderRadius: BorderRadius.circular(8)),
            child: Text(TrilingualService.instance.getUIText("1. State Prior to Braking (t < t_brake):\n""   Both Trolley and Block share velocity 'u'.\n" 
              "   v_trolley = u\n" 
              "   v_block = u\n\n" 
              "2. At Braking Instant (t = t_brake):\n" 
              "   External braking force acts strictly on the trolley frame.\n" 
              "   F_trolley_net << 0 (Trolley decelerates to a stop)\n" 
              "   F_block_net = 0 (No horizontal force acts on the block)\n\n" 
              "3. From Inertial Frame (Ground Observer):\n" 
              "   According to Newton's First Law:\n" 
              "   a_block = F_block_net / m_block = 0\n" 
              "   v_block(t) = u = constant (Slides off the deck)\n\n" 
              "4. From Non-Inertial Frame (Trolley Observer):\n" 
              "   Since the trolley is decelerating, it is non-inertial.\n" 
              "   We must apply a fictitious Pseudo Force on the block:\n" 
              "   F_pseudo = -m · a_trolley (directed forward)\n" 
              "   This makes the block accelerate forward relative to the trolley!"),
              style: TextStyle(fontFamily: 'monospace', color: Colors.greenAccent, fontSize: 13, height: 1.4),
            ),
          ),
          const SizedBox(height: 16),
          _buildConceptCard(
            "JEE-NEET Mechanics Takeaway:",
            "• Mass is the quantitative measurement of inertia (I ∝ m).\n"
            "• Newton's laws are directly applicable ONLY in Inertial Frames (non-accelerating reference systems).\n"
            "• Frame transformations are essential to resolve complex relative sliding equations.",
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
    double currentBlockVelocity = _initialVelocity;
    if (_hasBraked) {
      double tSlide = _time - _brakeTime;
      double deceleration = 0.25 * 9.8;
      currentBlockVelocity = math.max(0.0, _initialVelocity - (deceleration * tSlide));
    }

    return Column(
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(vertical: 8),
          color: Colors.blue[50],
          child: Text(
            _hasBraked 
                ? "Status: Cart Braked! Block maintains inertia..." 
                : _isMoving 
                    ? "Status: Uniform Velocity Cruise" 
                    : "Status: Ready on Pad",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Colors.blue[900]),
          ),
        ),
        Expanded(
          flex: 45,
          child: Container(
            margin: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.lightBlue[50], borderRadius: BorderRadius.circular(12)),
            child: ClipRRect(
              child: LayoutBuilder(builder: (context, constraints) {
                double scaleRatio = constraints.maxWidth / 400.0;
                return CustomPaint(
                  size: Size(constraints.maxWidth, constraints.maxHeight),
                  painter: ScalableInertiaPainter(
                    velocity: _initialVelocity, 
                    time: _time, 
                    brakeTime: _brakeTime, 
                    isMoving: _isMoving, 
                    hasBraked: _hasBraked, 
                    scaleRatio: scaleRatio
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
              Expanded(child: _buildTelemetryCard("Timer", "${_time.toStringAsFixed(2)} s")),
              Expanded(child: _buildTelemetryCard("Block Speed", "${currentBlockVelocity.toStringAsFixed(1)} m/s")),
              Expanded(child: _buildTelemetryCard("Initial Cruising Speed", "${_initialVelocity.toStringAsFixed(0)} m/s")),
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
          style: TextStyle(color: Theme.of(context).colorScheme.onSurface, fontSize: 15, fontWeight: FontWeight.bold, fontFamily: 'monospace')
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

  Widget _buildInteractiveQuiz() {
    bool isNeet = _targetPath == 'NEET'; 
    double mu = 0.25; 
    double g = 9.8;
    double anticipatedTime = _initialVelocity / (mu * g);
    
    String questionText = isNeet 
        ? "What is the instantaneous velocity of the block relative to the road just after braking?" 
        : "With road friction \u03BC = 0.25, how long does the block slide on the road before coming to a stop?";
    
    List<String> options = isNeet 
        ? ["0 m/s", "${_initialVelocity.toStringAsFixed(0)} m/s", "${(_initialVelocity * 2).toStringAsFixed(0)} m/s", "Depends on mass"] 
        : ["${(anticipatedTime * 0.5).toStringAsFixed(2)} s", "${anticipatedTime.toStringAsFixed(2)} s", "${(anticipatedTime + 1.2).toStringAsFixed(2)} s", "Infinite time"];
    
    int correctIndex = 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          isNeet ? "NEET Inertia Question:" : "JEE Kinematics Challenge:", 
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
                    _getTabExplanation(isNeet, _selectedAnswerIndex ?? 0, _activeExplanationTab, _initialVelocity, anticipatedTime),
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

  String _getTabExplanation(bool isNeet, int selected, int tabIndex, double u, double tAns) {
    if (isNeet) {
      switch (selected) {
        case 1: 
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — NEWTON'S 1ST LAW:\n\n"
                   "• The block is resting loosely on a flat trolley bed.\n"
                   "• An object in motion continues in its state of uniform motion in a straight line unless compelled to change by an external unbalanced force.\n"
                   "• Braking acts strictly on the trolley frame, not on the block itself.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Horizontal force balance on the block at braking instant:\n"
                   "  F_net = 0\n"
                   "• Since F = m · a:\n"
                   "  a = F_net / m = 0 / m = 0 m/s²\n"
                   "• Since acceleration is zero:\n"
                   "  Δv = 0 → v_instantaneous = u_initial = ${u.toStringAsFixed(0)} m/s.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• This is exactly why loose items (like your phone) on the dashboard fly forward when you stamp on the car brakes.\n"
                   "• They don't accelerate; they simply preserve their initial speed while the car halts beneath them.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• A common error is assuming the block is welded or fixed to the cart.\n"
                   "• Do not assume friction acts instantaneously across the boundary at t = 0 to halt everything at once.";
          }
        case 0:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — INERTIAL BREAKDOWN:\n\n"
                   "• To drop velocity instantly to 0 m/s requires an instantaneous loss of momentum.\n"
                   "• Newton's First Law guarantees that inertia of motion keeps the block moving forward. The block has no internal brakes!";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• An instantaneous stop (stopping time dt = 0) demands infinite deceleration:\n"
                   "  a = Δv / dt = (0 - ${u.toStringAsFixed(0)}) / 0 → -∞ m/s²\n"
                   "• Required Force: F = m · (-∞) = -∞ Newtons.\n"
                   "• Since there is no wall blocking the block, F_net is zero, making an instantaneous stop mathematically impossible.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• If things stopped instantly when vehicles braked, seatbelts wouldn't need to exist. \n"
                   "• Seatbelts are necessary specifically to apply the external retarding force that your body's inertia lacks on its own.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• The 'Static Connection' trap: Students often assume the inner cargo shares the exact same deceleration profile as the container chassis. Inertia keeps them separate!";
          }
        case 2:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — ENERGY CONSERVATION:\n\n"
                   "• Spontaneous velocity doubling violates basic mechanics.\n"
                   "• To increase speed, an active forward force must accelerate the block. No such propulsion force exists here.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Work-Energy Theorem states: Work = ΔK.E. = ½m(v² - u²)\n"
                   "• Scaling the speed to ${(u * 2).toStringAsFixed(0)} m/s requires positive work:\n"
                   "  Work = ½m(${(u*2).toStringAsFixed(0)}² - ${u.toStringAsFixed(0)}²) > 0\n"
                   "• Since the system is passive and F_net is 0, Work = 0. Velocity cannot exceed ${u.toStringAsFixed(0)} m/s.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• When a subway train brakes, passengers sway forward at the train's original speed—they do not catapult forward at twice the train's speed.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Momentum Transfer Misconception: Students confuse this slip with an elastic collision where energy concentrates into a smaller mass. No such collision occurs.";
          }
        case 3:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — INERTIAL EQUIVALENCE:\n\n"
                   "• While heavy objects possess more quantitative inertia (resistance to acceleration), their instantaneous speed in a force-free state is identical to light objects.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Let the block's mass be 'm'. From Newton's Second Law:\n"
                   "  a = F_net / m\n"
                   "• Since no horizontal forces act on the block, F_net = 0:\n"
                   "  a = 0 / m = 0 m/s²\n"
                   "• Mass completely cancels out of the motion profile.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• If you slam the brakes of a flatbed truck carrying a heavy steel safe and a light cardboard box, both slide off the front at the exact same forward velocity (assuming negligible air resistance).";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Confusing qualitative Inertia (Inertia ∝ Mass) with quantitative state tracking. Mass determines *how much force* is needed to change state, not the state itself if F = 0.";
          }
        default:
          return "";
      }
    } else {
      switch (selected) {
        case 1: 
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — KINETIC FRICTION ENVELOPE:\n\n"
                   "• Once the block slips off the cart deck and lands on the road, it is subjected to dynamic kinetic friction.\n"
                   "• This friction acts as a constant opposing force, bleeding off kinetic energy until the block stops.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Normal Force (N) = m · g\n"
                   "• Friction Force (f_k) = μ · N = μ · m · g\n"
                   "• Deceleration: a = -f_k / m = -μ · g = -0.25 × 9.8 = -2.45 m/s²\n"
                   "• Using v = u + a·t:\n"
                   "  0 = ${u.toStringAsFixed(0)} - 2.45 · t → t = ${u.toStringAsFixed(0)} / 2.45 = ${tAns.toStringAsFixed(2)} s.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• This explains vehicle braking distances. Heavy trucks and passenger cars lock up and slide under kinetic friction, decelerating at exactly -μg (independent of vehicle weight).";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Make sure you use the road's friction coefficient (μ = 0.25) and not the trolley deck (which is frictionless in this sandbox model).";
          }
        case 0:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — LINEAR RETARDATION:\n\n"
                   "• Friction retards speed at a uniform rate. The block does not lose all its momentum in half the calculated sliding timeline.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Deceleration rate (a) is constant at -2.45 m/s².\n"
                   "• Velocity at t_half (${(tAns * 0.5).toStringAsFixed(2)} s):\n"
                   "  v = u + a · t = ${u.toStringAsFixed(0)} - (2.45 × ${(tAns * 0.5).toStringAsFixed(2)}) = ${(u / 2).toStringAsFixed(1)} m/s.\n"
                   "• Since residual speed > 0, the block is still actively sliding.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• A sliding hockey puck does not come to a complete halt halfway through its calculated stop time; it is simply traveling at half its speed at that midpoint.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Midpoint Trap: Confusing the average speed midpoint calculation parameters with the total boundary condition for complete rest.";
          }
        case 2:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — PASSIVE FORCE CONSTRAINT:\n\n"
                   "• Kinetic friction is a passive, resistive force. It only exists as long as there is relative motion between the sliding block and the road.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• If we calculate velocity past the stopping limit at t = ${(tAns + 1.2).toStringAsFixed(2)} s:\n"
                   "  v = ${u.toStringAsFixed(0)} - (2.45 × ${(tAns + 1.2).toStringAsFixed(2)}) = -2.94 m/s.\n"
                   "• This negative velocity implies the block would spontaneously start moving backwards, which violates friction constraints.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• A sliding box on a floor comes to a dead stop. It doesn't magically spring backward once it stops sliding. Friction decays to exactly zero once motion stops.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Passive Force Rule: Never extend linear kinematics past the v = 0 boundary when dealing with resistive forces like friction or drag.";
          }
        case 3:
          if (tabIndex == 0) {
            return "💡 CONCEPTUAL MATRIX — RESISTIVE DISSIPATION:\n\n"
                   "• Inertia maintains constant motion ONLY in a force-free environment (F_net = 0).\n"
                   "• Landing on the road introduces an active external friction force vector, systematically destroying the inertial state.";
          } else if (tabIndex == 1) {
            return "🔢 MATHEMATICAL VALIDATION:\n\n"
                   "• Work-Energy Theorem: K.E._final - K.E._initial = Work_friction\n"
                   "  0 - ½mu² = -f_k · d = -(μmg) · d\n"
                   "• Stopping Distance: d = u² / (2μg)\n"
                   "• Since the distance 'd' is finite, the stopping time 't' must also be finite.";
          } else if (tabIndex == 2) {
            return "🌍 REAL-WORLD OBSERVATION:\n\n"
                   "• Rolling a ball on a grassy field demonstrates that friction always defeats inertia. Perfect perpetual motion is only achievable in a deep cosmic vacuum.";
          } else {
            return "⚠️ MISTAKE TRACKER:\n\n"
                   "• Idealization Trap: Do not misinterpret Newton's First Law as a shield that prevents environmental forces from altering a body's kinematic state.";
          }
        default:
          return "";
      }
    }
  }

  Widget _buildControlsTray() {
    return Container(
      padding: const EdgeInsets.all(12), 
      color: Colors.white,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            'Initial Velocity (u): ${_initialVelocity.toStringAsFixed(0)} m/s', 
            style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Colors.blueAccent[700])
          ),
          Slider(
            value: _initialVelocity, 
            min: 5, 
            max: 30, 
            divisions: 5, 
            activeColor: Colors.blueAccent[700],
            onChanged: _isMoving ? null : (val) => setState(() => _initialVelocity = val)
          ),
          const SizedBox(height: 4),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly, 
            children: [
              ElevatedButton.icon(
                onPressed: _isMoving ? null : _startCart, 
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green[700],
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                ), 
                icon: Icon(Icons.play_arrow, color: Colors.white, size: 18),
                label: Text(TrilingualService.instance.getUIText('Start Trolley'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12))
              ), 
              ElevatedButton.icon(
                onPressed: (_isMoving && !_hasBraked) ? _applySuddenBrake : null, 
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.red[700],
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                ), 
                icon: Icon(Icons.front_hand, color: Colors.white, size: 16),
                label: Text(TrilingualService.instance.getUIText('Sudden Brake'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12))
              ), 
              IconButton(
                onPressed: _resetSimulation, 
                icon: Icon(Icons.refresh),
                color: Colors.blueGrey[700],
              )
            ]
          )
        ]
      ),
    );
  }
}

class ScalableInertiaPainter extends CustomPainter {
  final double velocity, time, brakeTime; 
  final bool isMoving, hasBraked; 
  final double scaleRatio;
  
  ScalableInertiaPainter({
    required this.velocity, 
    required this.time, 
    required this.hasBraked, 
    required this.isMoving, 
    required this.brakeTime, 
    required this.scaleRatio
  });
  
  @override
  void paint(Canvas canvas, Size size) {
    canvas.save(); 
    canvas.scale(scaleRatio);
    
    final double virtualWidth = size.width / scaleRatio; 
    final double groundY = (size.height / scaleRatio) - 20.0;
    
    canvas.drawLine(Offset(0, groundY), Offset(virtualWidth, groundY), Paint()..color = Colors.black87..strokeWidth = 2);
    
    double cartWidth = 70.0; 
    double cartHeight = 20.0; 
    double wheelRadius = 6.0;
    double blockWidth = 22.0; 
    double blockHeight = 18.0; 
    final double uiSpeedModifier = 2.8;
    
    double absoluteCartX = 15.0; 
    if (isMoving) absoluteCartX += (velocity * (hasBraked ? brakeTime : time)) * uiSpeedModifier;
    
    double absoluteBlockX = 15.0 + 24.0;
    if (isMoving) {
      if (!hasBraked) { 
        absoluteBlockX += (velocity * time) * uiSpeedModifier; 
      } else {
        double tSlide = time - brakeTime; 
        double deceleration = 0.25 * 9.8; 
        double dynamicTime = math.min(tSlide, velocity / deceleration);
        absoluteBlockX += ((velocity * brakeTime) + (velocity * dynamicTime) - (0.5 * deceleration * math.pow(dynamicTime, 2))) * uiSpeedModifier;
      }
    }
    
    double trolleyChassisTopY = groundY - wheelRadius * 2 - cartHeight;
    double targetBlockY = trolleyChassisTopY - blockHeight;
    
    if (hasBraked && ((absoluteBlockX + (blockWidth / 2)) > (absoluteCartX + cartWidth))) {
      targetBlockY = groundY - blockHeight; 
    }
    
    canvas.drawRect(Rect.fromLTWH(absoluteCartX % virtualWidth, trolleyChassisTopY, cartWidth, cartHeight), Paint()..color = Colors.blueAccent);
    
    Paint wheelPaint = Paint()..color = Colors.grey[800]!..style = PaintingStyle.fill;
    double rearWheelX = (absoluteCartX + 16.0) % virtualWidth;
    double frontWheelX = (absoluteCartX + cartWidth - 16.0) % virtualWidth;
    double wheelCenterY = groundY - wheelRadius;
    
    canvas.drawCircle(Offset(rearWheelX, wheelCenterY), wheelRadius, wheelPaint);
    canvas.drawCircle(Offset(frontWheelX, wheelCenterY), wheelRadius, wheelPaint);
    
    canvas.drawRect(Rect.fromLTWH(absoluteBlockX % virtualWidth, targetBlockY, blockWidth, blockHeight), Paint()..color = Colors.redAccent);
    
    canvas.restore();
  }
  
  @override
  bool shouldRepaint(covariant ScalableInertiaPainter oldDelegate) => true;
}