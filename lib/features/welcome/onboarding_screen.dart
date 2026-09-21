import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../core/services/profile_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  int _currentStep = 0;
  
  String _selectedRole = '';
  String _selectedStage = '';
  String _selectedClass = '';
  String _selectedBoard = '';

  final List<String> _roles = ['Student', 'Teacher', 'Parent'];
  final List<String> _stages = ['Pre-School (Nursery-UKG)', 'Primary (Class 1-8)', 'Secondary (Class 9-10)', 'Higher Secondary (Class 11-12)', 'Competitive (UPSC/JEE)'];
  final List<String> _boards = ['NCERT', 'GSEB (Gujarat Board)', 'CBSE'];

  void _nextStep() {
    if (_currentStep == 0 && _selectedRole.isEmpty) return;
    if (_currentStep == 1 && _selectedStage.isEmpty) return;
    if (_currentStep == 2 && _selectedBoard.isEmpty) return;

    if (_currentStep < 2) {
      setState(() {
        _currentStep++;
      });
    } else {
      _finishOnboarding();
    }
  }

  Future<void> _finishOnboarding() async {
    // Derive class string for simplicity
    if (_selectedStage == 'Pre-School (Nursery-UKG)') _selectedClass = 'Nursery';
    if (_selectedStage == 'Primary (Class 1-8)') _selectedClass = 'Class 3-6';
    if (_selectedStage == 'Secondary (Class 9-10)') _selectedClass = 'Class 10';
    if (_selectedStage == 'Higher Secondary (Class 11-12)') _selectedClass = 'Class 12 Commerce';

    await ProfileService.saveProfile(
      role: _selectedRole,
      stage: _selectedStage,
      userClass: _selectedClass,
      board: _selectedBoard,
    );

    if (mounted) {
      context.go('/');
    }
  }

  Widget _buildSelectionCard(String text, bool isSelected, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        margin: const EdgeInsets.only(bottom: 16),
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: isSelected ? AppColors.primary.withValues(alpha: 0.1) : Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected ? AppColors.primary : Colors.grey.shade300,
            width: isSelected ? 2 : 1,
          ),
          boxShadow: [
            if (isSelected)
              BoxShadow(
                color: AppColors.primary.withValues(alpha: 0.2),
                blurRadius: 10,
                offset: const Offset(0, 4),
              )
          ],
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              text,
              style: GoogleFonts.poppins(
                fontSize: 16,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
                color: isSelected ? AppColors.primaryDark : AppColors.textPrimary,
              ),
            ),
            if (isSelected)
              Icon(Icons.check_circle, color: AppColors.primary),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 20),
              LinearProgressIndicator(
                value: (_currentStep + 1) / 3,
                backgroundColor: Colors.grey.shade300,
                color: AppColors.primary,
                minHeight: 8,
                borderRadius: BorderRadius.circular(4),
              ),
              const SizedBox(height: 24),
              
              Expanded(
                child: SingleChildScrollView(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      if (_currentStep == 0) ...[
                        Text(TrilingualService.instance.getUIText("Who are you?"),
                          style: GoogleFonts.poppins(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                        ),
                        const SizedBox(height: 8),
                        Text(TrilingualService.instance.getUIText("Let's personalize your learning experience."),
                          style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary),
                        ),
                        const SizedBox(height: 40),
                        ..._roles.map((role) => _buildSelectionCard(
                          role,
                          _selectedRole == role,
                          () => setState(() => _selectedRole = role),
                        )),
                      ],

                      if (_currentStep == 1) ...[
                        Text(TrilingualService.instance.getUIText("What is your stage?"),
                          style: GoogleFonts.poppins(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                        ),
                        const SizedBox(height: 8),
                        Text(TrilingualService.instance.getUIText("This helps us find the right courses for you."),
                          style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary),
                        ),
                        const SizedBox(height: 40),
                        ..._stages.map((stage) => _buildSelectionCard(
                          stage,
                          _selectedStage == stage,
                          () => setState(() => _selectedStage = stage),
                        )),
                      ],

                      if (_currentStep == 2) ...[
                        Text(TrilingualService.instance.getUIText("Select your Board"),
                          style: GoogleFonts.poppins(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                        ),
                        const SizedBox(height: 8),
                        Text(TrilingualService.instance.getUIText("We map the curriculum strictly to your board."),
                          style: GoogleFonts.inter(fontSize: 16, color: AppColors.textSecondary),
                        ),
                        const SizedBox(height: 40),
                        ..._boards.map((board) => _buildSelectionCard(
                          board,
                          _selectedBoard == board,
                          () => setState(() => _selectedBoard = board),
                        )),
                      ],
                    ],
                  ),
                ),
              ),
              
              const SizedBox(height: 16),
              SizedBox(
                width: double.infinity,
                height: 56,
                child: ElevatedButton(
                  onPressed: _nextStep,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  ),
                  child: Text(
                    _currentStep == 2 ? "Get Started" : "Continue",
                    style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                  ),
                ),
              ),
              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }
}
