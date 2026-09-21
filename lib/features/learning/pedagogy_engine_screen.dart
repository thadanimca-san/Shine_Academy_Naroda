import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';
import '../../foundation/theme/app_colors.dart';
import '../../core/services/gamification_service.dart';
import '../gamification/widgets/mast_hai_dialog.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/features/learning/widgets/knowledge_graph_visualizer.dart';

class PedagogyEngineScreen extends StatefulWidget {
  const PedagogyEngineScreen({super.key});

  @override
  State<PedagogyEngineScreen> createState() => _PedagogyEngineScreenState();
}

class _PedagogyEngineScreenState extends State<PedagogyEngineScreen> with SingleTickerProviderStateMixin {
  final PageController _pageController = PageController();
  int _currentStep = 0;
  final int _totalSteps = 8;
  
  late AnimationController _fadeController;
  late Animation<double> _fadeAnimation;

  @override
  void initState() {
    super.initState();
    _fadeController = AnimationController(vsync: this, duration: const Duration(milliseconds: 600));
    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(CurvedAnimation(parent: _fadeController, curve: Curves.easeIn));
    _fadeController.forward();
  }

  @override
  void dispose() {
    _pageController.dispose();
    _fadeController.dispose();
    super.dispose();
  }

  void _nextStep() {
    if (_currentStep < _totalSteps - 1) {
      _fadeController.reset();
      _pageController.nextPage(duration: const Duration(milliseconds: 400), curve: Curves.easeInOut);
      setState(() {
        _currentStep++;
      });
      _fadeController.forward();
    } else {
      _finishLesson();
    }
  }

  void _finishLesson() {
    // Gamification Trigger
    GamificationService.instance.addXp(50);
    GamificationService.instance.addCoins(10);
    
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => const MastHaiDialog(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.close, color: Theme.of(context).colorScheme.onSurface),
          onPressed: () => context.pop(),
        ),
        title: Column(
          children: [
            Text(TrilingualService.instance.getUIText("Class 10 Science"),
              style: GoogleFonts.inter(fontSize: 12, color: Colors.grey[600], fontWeight: FontWeight.bold),
            ),
            Text(TrilingualService.instance.getUIText("Chemical Reactions"),
              style: GoogleFonts.poppins(fontSize: 16, color: Theme.of(context).colorScheme.onSurface, fontWeight: FontWeight.bold),
            ),
          ],
        ),
        centerTitle: true,
      ),
      body: SafeArea(
        child: Column(
          children: [
            _buildProgressBar(),
            Expanded(
              child: PageView(
                controller: _pageController,
                physics: const NeverScrollableScrollPhysics(), // Force using the Next button
                children: [
                  _buildStep1Hook(),
                  _buildStep2Socratic(),
                  _buildStep3Discovery(),
                  _buildStep4Reveal(),
                  _buildStep5KnowledgeCheck(),
                  _buildStep6Reflection(),
                  _buildStep7Connection(),
                  _buildStep8Mastery(),
                ],
              ),
            ),
            _buildBottomNav(),
          ],
        ),
      ),
    );
  }

  Widget _buildProgressBar() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 12.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                "Step ${_currentStep + 1} of $_totalSteps",
                style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: AppColors.primary),
              ),
              Text(
                _getStepName(_currentStep),
                style: GoogleFonts.inter(fontSize: 12, color: Colors.grey[600]),
              ),
            ],
          ),
          const SizedBox(height: 8),
          ClipRRect(
            borderRadius: BorderRadius.circular(10),
            child: LinearProgressIndicator(
              value: (_currentStep + 1) / _totalSteps,
              backgroundColor: Colors.grey[200],
              valueColor: AlwaysStoppedAnimation<Color>(AppColors.primary),
              minHeight: 8,
            ),
          ),
        ],
      ),
    );
  }

  String _getStepName(int index) {
    const names = ["Hook", "Socratic Thinking", "Discovery", "Reveal", "Knowledge Check", "Reflection", "Connection", "Mastery"];
    return names[index];
  }

  Widget _buildBottomNav() {
    return Container(
      padding: const EdgeInsets.all(24.0),
      decoration: BoxDecoration(
        color: Colors.white,
        boxShadow: [
          BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 10, offset: const Offset(0, -4)),
        ],
      ),
      child: SizedBox(
        width: double.infinity,
        height: 56,
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.primary,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            elevation: 0,
          ),
          onPressed: _nextStep,
          child: Text(
            _currentStep == _totalSteps - 1 ? "Complete Lesson" : "Continue",
            style: GoogleFonts.poppins(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
          ),
        ),
      ),
    );
  }

  // --- THE 8 STEPS CONTENT ---

  Widget _buildStepTemplate({required IconData icon, required String subtitle, required String title, required Widget child}) {
    return FadeTransition(
      opacity: _fadeAnimation,
      child: Padding(
        padding: const EdgeInsets.all(32.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: AppColors.primary.withValues(alpha: 0.1),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: AppColors.primary, size: 32),
            ),
            const SizedBox(height: 24),
            Text(
              subtitle.toUpperCase(),
              style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: AppColors.primary, letterSpacing: 1.2),
            ),
            const SizedBox(height: 8),
            Text(
              title,
              style: GoogleFonts.poppins(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.textPrimary, height: 1.2),
            ),
            const SizedBox(height: 32),
            Expanded(child: child),
          ],
        ),
      ),
    );
  }

  Widget _buildStep1Hook() {
    return _buildStepTemplate(
      icon: Icons.lightbulb_outline,
      subtitle: "Step 1: The Hook",
      title: "The Mystery of the Brown Apple",
      child: Column(
        children: [
          Expanded(
            child: Container(
              decoration: BoxDecoration(
                color: Colors.orange[50],
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: Colors.orange[200]!, width: 2),
              ),
              child: Center(
                child: Icon(Icons.apple, size: 100, color: Colors.red[300]),
              ),
            ),
          ),
          const SizedBox(height: 32),
          Text(TrilingualService.instance.getUIText("You cut a fresh, crisp apple and leave it on the kitchen counter. An hour later, the white flesh has turned completely brown and unappetizing."),
            style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary, height: 1.5),
          ),
        ],
      )
    );
  }

  Widget _buildStep2Socratic() {
    return _buildStepTemplate(
      icon: Icons.question_answer_outlined,
      subtitle: "Step 2: Socratic Thinking",
      title: "What is attacking the apple?",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("The apple didn't turn brown by itself. Something invisible in the air interacted with it."),
            style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary, height: 1.5),
          ),
          const SizedBox(height: 32),
          Text(TrilingualService.instance.getUIText("What gas in the air do you think caused this?"),
            style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
          ),
          const SizedBox(height: 16),
          TextField(
            decoration: InputDecoration(
              hintText: "Type your prediction...",
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
              filled: true,
              fillColor: Colors.grey[100],
            ),
          ),
        ],
      )
    );
  }

  Widget _buildStep3Discovery() {
    return _buildStepTemplate(
      icon: Icons.explore_outlined,
      subtitle: "Step 3: Discovery",
      title: "Look at this bicycle.",
      child: Column(
        children: [
          Expanded(
            child: Container(
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.brown[50],
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: Colors.brown[200]!, width: 2),
              ),
              child: Center(
                child: Icon(Icons.pedal_bike, size: 100, color: Colors.brown[400]),
              ),
            ),
          ),
          const SizedBox(height: 32),
          Text(TrilingualService.instance.getUIText("When an iron bicycle is left in the rain, it turns reddish-brown. This is rust. The iron in the bike is reacting with Oxygen in the air, just like the enzymes in the apple did!"),
            style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary, height: 1.5),
          ),
        ],
      )
    );
  }

  Widget _buildStep4Reveal() {
    return _buildStepTemplate(
      icon: Icons.menu_book_outlined,
      subtitle: "Step 4: The Reveal",
      title: "Chemical Reaction",
      child: Container(
        padding: const EdgeInsets.all(24),
        decoration: BoxDecoration(
          color: Colors.indigo[50],
          borderRadius: BorderRadius.circular(20),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(TrilingualService.instance.getUIText("Definition:"),
              style: GoogleFonts.poppins(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.indigo),
            ),
            const SizedBox(height: 12),
            Text(TrilingualService.instance.getUIText("A process in which one or more substances (reactants) are converted to one or more different substances (products)."),
              style: GoogleFonts.inter(fontSize: 18, color: Colors.indigo[900], height: 1.5, fontWeight: FontWeight.w500),
            ),
            const SizedBox(height: 24),
            Text(TrilingualService.instance.getUIText("In both the apple and the bicycle, the invisible process happening was Oxidation—a type of chemical reaction where oxygen is added to a substance."),
              style: GoogleFonts.inter(fontSize: 14, color: Colors.indigo[700], height: 1.5),
            ),
          ],
        ),
      )
    );
  }

  Widget _buildStep5KnowledgeCheck() {
    return _buildStepTemplate(
      icon: Icons.fact_check_outlined,
      subtitle: "Step 5: Knowledge Check",
      title: "Let's test it.",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("Which of the following is an example of a chemical reaction?"),
            style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
          ),
          const SizedBox(height: 24),
          _buildOptionButton("A. Melting of ice into water"),
          const SizedBox(height: 12),
          _buildOptionButton("B. Tearing a piece of paper"),
          const SizedBox(height: 12),
          _buildOptionButton("C. Digestion of food in our body", isCorrect: true), // Correct
          const SizedBox(height: 12),
          _buildOptionButton("D. Boiling water to form steam"),
        ],
      )
    );
  }

  Widget _buildOptionButton(String text, {bool isCorrect = false}) {
    // Simple static UI for demo purposes
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey[300]!, width: 2),
      ),
      child: Text(
        text,
        style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.w600, color: AppColors.textPrimary),
      ),
    );
  }

  Widget _buildStep6Reflection() {
    return _buildStepTemplate(
      icon: Icons.psychology_outlined,
      subtitle: "Step 6: Reflection",
      title: "Look around you.",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("Chemical reactions are happening constantly inside you and around you."),
            style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary, height: 1.5),
          ),
          const SizedBox(height: 32),
          Text(TrilingualService.instance.getUIText("Can you think of a chemical reaction that happens in your kitchen every morning?"),
            style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
          ),
          const SizedBox(height: 16),
          TextField(
            maxLines: 4,
            decoration: InputDecoration(
              hintText: "Example: Making tea, boiling milk...",
              border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
              filled: true,
              fillColor: Colors.grey[100],
            ),
          ),
        ],
      )
    );
  }

  Widget _buildStep7Connection() {
    return _buildStepTemplate(
      icon: Icons.hub_outlined,
      subtitle: "Step 7: Connection",
      title: "Knowledge Graph",
      child: const KnowledgeGraphVisualizer(nodeId: "gseb_class8_science_ch1"),
    );
  }

  Widget _buildStep8Mastery() {
    return _buildStepTemplate(
      icon: Icons.emoji_events_outlined,
      subtitle: "Step 8: Mastery",
      title: "The Final Challenge",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(
              gradient: const LinearGradient(colors: [Colors.purple, Colors.deepPurple]),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.science, color: Colors.white, size: 40),
                const SizedBox(height: 16),
                Text(TrilingualService.instance.getUIText("Magnesium ribbon burns with a dazzling white flame and changes into a white powder. What is this powder?"),
                  style: GoogleFonts.inter(fontSize: 18, color: Colors.white, height: 1.5, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 24),
                TextField(
                  decoration: InputDecoration(
                    hintText: "Your final answer...",
                    hintStyle: TextStyle(color: Colors.white54),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(16), borderSide: BorderSide(color: Colors.white)),
                    enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(16), borderSide: BorderSide(color: Colors.white54)),
                    filled: true,
                    fillColor: Colors.white.withValues(alpha: 0.1),
                  ),
                  style: TextStyle(color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      )
    );
  }
}
