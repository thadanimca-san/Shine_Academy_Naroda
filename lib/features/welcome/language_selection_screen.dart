import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../foundation/theme/app_colors.dart';
import '../../core/services/trilingual_service.dart';
import '../../core/services/activation_service.dart';
import '../../core/services/profile_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class LanguageSelectionScreen extends StatelessWidget {
  const LanguageSelectionScreen({super.key});

  Future<void> _selectLanguage(BuildContext context, String langCode) async {
    await TrilingualService.instance.setPrimaryLanguage(langCode);
    
    if (context.mounted) {
      if (!ActivationService.isActivated) {
        context.go('/activate');
      } else {
        bool hasProfile = await ProfileService.isProfileSet();
        if (context.mounted) {
          if (hasProfile) {
            context.go('/home');
          } else {
            context.go('/welcome');
          }
        }
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 40.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Spacer(flex: 1),
              Center(
                child: Container(
                  width: 100,
                  height: 100,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.primary.withValues(alpha: 0.1),
                        blurRadius: 20,
                        spreadRadius: 5,
                      ),
                    ],
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(12.0),
                    child: Image.asset(
                      'assets/shineacademynarodalogo.jpg',
                      fit: BoxFit.contain,
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 32),
              Text(TrilingualService.instance.getUIText("Choose Your Language\nअपनी भाषा चुनें\nતમારી ભાષા પસંદ કરો"),
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                  color: AppColors.primaryDark,
                  height: 1.4,
                ),
              ),
              const SizedBox(height: 16),
              Text(TrilingualService.instance.getUIText("You can always change this later.\nआप इसे बाद में बदल सकते हैं।"),
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontSize: 14,
                  color: AppColors.textSecondary,
                ),
              ),
              const Spacer(flex: 2),
              
              _buildLanguageCard(
                context,
                title: 'English',
                subtitle: 'Learn primarily in English',
                langCode: 'en',
                color: Colors.blue.shade50,
                borderColor: Colors.blue.shade200,
              ),
              const SizedBox(height: 16),
              
              _buildLanguageCard(
                context,
                title: 'हिन्दी',
                subtitle: 'मुख्य रूप से हिंदी में सीखें',
                langCode: 'hi',
                color: Colors.orange.shade50,
                borderColor: Colors.orange.shade200,
              ),
              const SizedBox(height: 16),
              
              _buildLanguageCard(
                context,
                title: 'ગુજરાતી',
                subtitle: 'મુખ્યત્વે ગુજરાતીમાં શીખો',
                langCode: 'gu',
                color: Colors.green.shade50,
                borderColor: Colors.green.shade200,
              ),
              const Spacer(flex: 2),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildLanguageCard(
    BuildContext context, {
    required String title,
    required String subtitle,
    required String langCode,
    required Color color,
    required Color borderColor,
  }) {
    return Material(
      color: color,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: borderColor, width: 1.5),
      ),
      child: InkWell(
        onTap: () => _selectLanguage(context, langCode),
        borderRadius: BorderRadius.circular(16),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 24),
          child: Row(
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: GoogleFonts.poppins(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                        color: AppColors.primaryDark,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      subtitle,
                      style: GoogleFonts.inter(
                        fontSize: 14,
                        color: AppColors.textSecondary,
                      ),
                    ),
                  ],
                ),
              ),
              Icon(Icons.arrow_forward_ios, color: AppColors.primaryDark, size: 20),
            ],
          ),
        ),
      ),
    );
  }
}
