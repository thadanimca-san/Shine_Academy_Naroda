import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../core/services/profile_service.dart';
import 'package:flutter/services.dart';
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
  late List<String> _stages;
  late List<String> _boards;

  @override
  void initState() {
    super.initState();
    _initializeStages();
  }

  void _initializeStages() {
    final flavor = appFlavor ?? 'default';
    if (flavor == 'primary') {
      _stages = ['Pre-School (Nursery-UKG)', 'Primary (Class 1-4)'];
      _boards = ['Core Concepts (NCERT)', 'GSEB (Gujarat Board)', 'CBSE'];
    } else if (flavor == 'middle') {
      _stages = ['Class 5', 'Class 6', 'Class 7', 'Class 8'];
      _boards = ['Core Concepts (NCERT)', 'GSEB (Gujarat Board)', 'CBSE'];
    } else if (flavor == 'junior') {
      _stages = ['Pre-School (Nursery-UKG)', 'Primary (Class 1-8)'];
      _boards = ['Core Concepts (NCERT)', 'GSEB (Gujarat Board)', 'CBSE'];
    } else if (flavor == 'highschool') {
      _stages = ['Secondary (Class 9-10)'];
      _boards = ['Core Concepts (NCERT)', 'GSEB (Gujarat Board)', 'CBSE'];
    } else if (flavor == 'commerce') {
      _stages = ['Class 11 Commerce', 'Class 12 Commerce'];
      _boards = ['GSEB (Gujarat Board)', 'CBSE'];
    } else if (flavor == 'achievers') {
      _stages = ['Class 11 Science', 'Class 12 Science', 'Competitive (NEET/JEE)'];
      _boards = ['GSEB (Gujarat Board)', 'CBSE', 'Core Concepts (NCERT)'];
    } else if (flavor == 'skillup') {
      _stages = ['Spoken English & Fluency'];
      _boards = ['Govind Sir Academy'];
      _selectedBoard = 'Govind Sir Academy';
    } else {
      _stages = [
        'Pre-School (Nursery-UKG)',
        'Primary (Class 1-8)',
        'Secondary (Class 9-10)',
        'Class 11 Commerce',
        'Class 12 Commerce',
        'Class 11 Science',
        'Class 12 Science',
        'Competitive (NEET/JEE/UPSC)',
      ];
      _boards = ['Core Concepts (NCERT)', 'GSEB (Gujarat Board)', 'CBSE'];
    }
  }

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
    final flavor = appFlavor ?? 'default';

    // Map the selected stage to normalized userClass and stage
    if (_selectedStage == 'Class 11 Commerce') {
      _selectedClass = 'Class 11 Commerce';
      _selectedStage = 'Higher Secondary (Class 11)';
    } else if (_selectedStage == 'Class 12 Commerce') {
      _selectedClass = 'Class 12 Commerce';
      _selectedStage = 'Higher Secondary (Class 12)';
    } else if (_selectedStage == 'Class 11 Science') {
      _selectedClass = 'Class 11 Science';
      _selectedStage = 'Higher Secondary (Class 11)';
    } else if (_selectedStage == 'Class 12 Science') {
      _selectedClass = 'Class 12 Science';
      _selectedStage = 'Higher Secondary (Class 12)';
    } else if (_selectedStage.contains('Competitive') || _selectedStage.contains('NEET') || _selectedStage.contains('JEE')) {
      _selectedClass = 'Competitive';
      _selectedStage = 'Competitive';
    } else if (_selectedStage == 'Pre-School (Nursery-UKG)') {
      _selectedClass = 'Nursery';
      _selectedStage = 'Pre-School';
    } else if (_selectedStage == 'Primary (Class 1-4)') {
      _selectedClass = 'Class 1-4';
      _selectedStage = 'Primary';
    } else if (['Class 5', 'Class 6', 'Class 7', 'Class 8'].contains(_selectedStage)) {
      _selectedClass = _selectedStage;
      _selectedStage = 'Primary';
    } else if (_selectedStage == 'Upper Primary (Class 5-8)') {
      _selectedClass = 'Class 5-8';
      _selectedStage = 'Primary';
    } else if (_selectedStage == 'Primary (Class 1-8)') {
      _selectedClass = 'Class 3-6';
      _selectedStage = 'Primary';
    } else if (_selectedStage == 'Class 9' || _selectedStage == 'Class 10') {
      _selectedClass = _selectedStage;
      _selectedStage = 'Secondary (Class 9-10)';
    } else if (_selectedStage == 'Secondary (Class 9-10)') {
      _selectedClass = 'Class 10';
      _selectedStage = 'Secondary (Class 9-10)';
    } else if (_selectedStage == 'Spoken English & Fluency' || _selectedStage == 'Skill Up / Special' || flavor == 'skillup') {
      _selectedClass = 'Spoken English';
      _selectedStage = 'Skill Up';
      if (_selectedBoard.isEmpty) _selectedBoard = 'Govind Sir Academy';
    } else if (_selectedStage == 'Higher Secondary (Class 11-12)') {
      if (flavor == 'commerce') {
        _selectedClass = 'Class 12 Commerce';
        _selectedStage = 'Higher Secondary (Class 12)';
      } else if (flavor == 'achievers') {
        _selectedClass = 'Class 12 Science';
        _selectedStage = 'Higher Secondary (Class 12)';
      } else {
        _selectedClass = 'Class 12';
        _selectedStage = 'Higher Secondary (Class 12)';
      }
    } else {
      _selectedClass = _selectedStage;
    }

    if (_selectedBoard.isEmpty && _boards.isNotEmpty) {
      _selectedBoard = _boards.first;
    }

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
