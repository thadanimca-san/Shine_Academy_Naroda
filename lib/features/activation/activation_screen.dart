import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../../core/services/activation_service.dart';
import '../../../foundation/theme/app_colors.dart';
import '../../../foundation/theme/premium_card.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ActivationScreen extends StatefulWidget {
  const ActivationScreen({super.key});

  @override
  State<ActivationScreen> createState() => _ActivationScreenState();
}

class _ActivationScreenState extends State<ActivationScreen> {
  final TextEditingController _codeController = TextEditingController();
  bool _isLoading = false;
  String _errorMessage = '';

  Future<void> _handleActivation() async {
    if (_codeController.text.isEmpty) {
      setState(() => _errorMessage = 'Please enter an activation code.');
      return;
    }

    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });

    // Simulate network delay for UX
    await Future.delayed(const Duration(milliseconds: 800));

    final success = await ActivationService.activate(_codeController.text);

    if (!mounted) return;

    if (success) {
      context.go('/'); // Let splash redirect properly
    } else {
      setState(() {
        _isLoading = false;
        _errorMessage = 'Invalid Activation Code. Please contact Shine Academy.';
      });
    }
  }

  Future<void> _sendWhatsAppMessage() async {
    final String message = "Hello Govind Sir, my Shine Academy EduOS Device Code is: *${ActivationService.deviceCode}*\n\nPlease provide my Activation Code.";
    // wa.me without phone number opens contact picker in WhatsApp
    final Uri url = Uri.parse("https://wa.me/?text=${Uri.encodeComponent(message)}");
    if (await canLaunchUrl(url)) {
      await launchUrl(url, mode: LaunchMode.externalApplication);
    } else {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Could not open WhatsApp. Please install it first.')));
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24.0),
            child: PremiumCard(
              color: Colors.white,
              child: Padding(
                padding: const EdgeInsets.all(32.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: AppColors.primary.withValues(alpha: 0.1),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(Icons.lock_outline, size: 48, color: AppColors.primary),
                    ),
                    const SizedBox(height: 24),
                    Text(TrilingualService.instance.getUIText('App Activation Required'),
                      style: GoogleFonts.poppins(fontSize: 24, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 12),
                    Text(TrilingualService.instance.getUIText('This app is protected. Please provide the Device Code below to GovindSir of Shine Academy Naroda to receive your Activation Code.\n\nयह ऐप सुरक्षित है। अपना एक्टिवेशन कोड प्राप्त करने के लिए कृपया नीचे दिया गया डिवाइस कोड शाइन एकेडमी नरोदा के गोविंद सर को दें।'),
                      style: GoogleFonts.inter(fontSize: 14, color: AppColors.textSecondary),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 32),
                    
                    // STEP 1
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.green.withValues(alpha: 0.1),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: Colors.green.shade300),
                      ),
                      child: Column(
                        children: [
                          Text("STEP 1", style: GoogleFonts.poppins(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.green.shade700)),
                          const SizedBox(height: 8),
                          Text(
                            TrilingualService.instance.getUIText('Send your Device Code to Govind Sir on WhatsApp to receive the Activation Code.'),
                            style: GoogleFonts.inter(fontSize: 12, color: AppColors.textSecondary),
                            textAlign: TextAlign.center,
                          ),
                          const SizedBox(height: 12),
                          Text(
                            ActivationService.deviceCode,
                            style: GoogleFonts.robotoMono(fontSize: 28, fontWeight: FontWeight.bold, letterSpacing: 4, color: AppColors.textPrimary),
                          ),
                          const SizedBox(height: 16),
                          SizedBox(
                            width: double.infinity,
                            child: ElevatedButton.icon(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: const Color(0xFF25D366), // WhatsApp Green
                                foregroundColor: Colors.white,
                                padding: const EdgeInsets.symmetric(vertical: 12),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                              ),
                              icon: const Icon(Icons.chat),
                              label: Text("Share via WhatsApp", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
                              onPressed: _sendWhatsAppMessage,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 32),
                    
                    // STEP 2
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: Colors.grey.shade50,
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: Colors.grey.shade300),
                      ),
                      child: Column(
                        children: [
                          Text("STEP 2", style: GoogleFonts.poppins(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.primary)),
                          const SizedBox(height: 16),
                          TextField(
                            controller: _codeController,
                            textCapitalization: TextCapitalization.characters,
                            style: GoogleFonts.robotoMono(fontSize: 20, letterSpacing: 2),
                            decoration: InputDecoration(
                              labelText: 'Enter Activation Code Here',
                              hintText: 'ENTER 8 DIGIT CODE',
                              border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                              focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: const BorderSide(color: AppColors.primary, width: 2)),
                            ),
                          ),
                          
                          if (_errorMessage.isNotEmpty) ...[
                            const SizedBox(height: 12),
                            Text(_errorMessage, style: const TextStyle(color: Colors.red, fontWeight: FontWeight.bold)),
                          ],
                          
                          const SizedBox(height: 24),
                          SizedBox(
                            width: double.infinity,
                            height: 56,
                            child: ElevatedButton(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: AppColors.primary,
                                foregroundColor: Colors.white,
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                              ),
                              onPressed: _isLoading ? null : _handleActivation,
                              child: _isLoading 
                                  ? const CircularProgressIndicator(color: Colors.white)
                                  : Text(TrilingualService.instance.getUIText('Activate App'), style: GoogleFonts.inter(fontSize: 18, fontWeight: FontWeight.bold)),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
