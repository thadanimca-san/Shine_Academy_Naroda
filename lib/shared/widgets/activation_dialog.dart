import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/services/activation_service.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A premium-looking dialog that lets users activate the app inline
/// without leaving the current screen. Shows device code, WhatsApp share,
/// and activation code entry.
///
/// Usage:
/// ```dart
/// ActivationDialog.show(context, onActivated: () => setState(() {}));
/// ```
class ActivationDialog {
  static Future<void> show(BuildContext context, {VoidCallback? onActivated}) {
    return showDialog(
      context: context,
      barrierDismissible: true,
      builder: (dialogContext) => _ActivationDialogContent(
        onActivated: () {
          Navigator.of(dialogContext).pop();
          onActivated?.call();
        },
      ),
    );
  }
}

class _ActivationDialogContent extends StatefulWidget {
  final VoidCallback onActivated;
  const _ActivationDialogContent({required this.onActivated});

  @override
  State<_ActivationDialogContent> createState() => _ActivationDialogContentState();
}

class _ActivationDialogContentState extends State<_ActivationDialogContent> {
  final TextEditingController _codeController = TextEditingController();
  bool _isLoading = false;
  String _errorMessage = '';

  Future<void> _handleActivation() async {
    if (_codeController.text.isEmpty) {
      setState(() => _errorMessage = TrilingualService.instance.getUIText('Please enter an activation code.'));
      return;
    }

    setState(() {
      _isLoading = true;
      _errorMessage = '';
    });

    await Future.delayed(const Duration(milliseconds: 600));

    final success = await ActivationService.activate(_codeController.text);

    if (!mounted) return;

    if (success) {
      widget.onActivated();
    } else {
      setState(() {
        _isLoading = false;
        _errorMessage = TrilingualService.instance.getUIText('Invalid Activation Code. Please contact Shine Academy.');
      });
    }
  }

  Future<void> _sendWhatsApp() async {
    final String message =
        "Hello Govind Sir, my Shine Academy EduOS Device Code is: *${ActivationService.deviceCode}*\n\nPlease provide my Activation Code.";
    final Uri url = Uri.parse("https://wa.me/?text=${Uri.encodeComponent(message)}");
    if (await canLaunchUrl(url)) {
      await launchUrl(url, mode: LaunchMode.externalApplication);
    } else {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text(TrilingualService.instance.getUIText('Could not open WhatsApp.'))),
        );
      }
    }
  }

  @override
  void dispose() {
    _codeController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final scale = AppTypography.scaleFactor(context);

    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
      child: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(24.0 * scale),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Lock icon
              Container(
                padding: EdgeInsets.all(14 * scale),
                decoration: const BoxDecoration(
                  gradient: LinearGradient(
                    colors: [Color(0xFFFF6F00), Color(0xFFFFCA28)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  shape: BoxShape.circle,
                ),
                child: Icon(Icons.lock_outline, size: 36 * scale, color: Colors.white),
              ),
              SizedBox(height: 16 * scale),

              // Title
              Text(
                TrilingualService.instance.getUIText('🔒 Premium Content'),
                style: GoogleFonts.poppins(
                  fontSize: 20 * scale,
                  fontWeight: FontWeight.bold,
                  color: AppColors.textPrimary,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 8 * scale),

              // Subtitle
              Text(
                TrilingualService.instance.getUIText(
                  'This content requires activation.\nइस सामग्री के लिए सक्रियण आवश्यक है।\nઆ સામગ્રી માટે સક્રિયકરણ જરૂરી છે।',
                ),
                style: GoogleFonts.inter(fontSize: 13 * scale, color: AppColors.textSecondary, height: 1.5),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 20 * scale),

              // Device Code Box
              Container(
                width: double.infinity,
                padding: EdgeInsets.all(14 * scale),
                decoration: BoxDecoration(
                  color: Colors.green.withValues(alpha: 0.08),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.green.shade300),
                ),
                child: Column(
                  children: [
                    Text(
                      TrilingualService.instance.getUIText('Your Device Code'),
                      style: GoogleFonts.inter(fontSize: 12 * scale, color: Colors.green.shade700, fontWeight: FontWeight.w600),
                    ),
                    SizedBox(height: 6 * scale),
                    Text(
                      ActivationService.deviceCode,
                      style: GoogleFonts.robotoMono(
                        fontSize: 24 * scale,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 3,
                        color: AppColors.textPrimary,
                      ),
                    ),
                    SizedBox(height: 10 * scale),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFF25D366),
                          foregroundColor: Colors.white,
                          padding: EdgeInsets.symmetric(vertical: 10 * scale),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                        ),
                        icon: Icon(Icons.chat, size: 18 * scale),
                        label: Text(
                          TrilingualService.instance.getUIText("Send via WhatsApp"),
                          style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 13 * scale),
                        ),
                        onPressed: _sendWhatsApp,
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(height: 16 * scale),

              // Activation Code Entry
              TextField(
                controller: _codeController,
                textCapitalization: TextCapitalization.characters,
                style: GoogleFonts.robotoMono(fontSize: 18 * scale, letterSpacing: 2),
                decoration: InputDecoration(
                  labelText: TrilingualService.instance.getUIText('Enter Activation Code'),
                  hintText: 'XXXXXXXX',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: const BorderSide(color: AppColors.primary, width: 2),
                  ),
                  contentPadding: EdgeInsets.symmetric(horizontal: 16 * scale, vertical: 14 * scale),
                ),
              ),

              if (_errorMessage.isNotEmpty) ...[
                SizedBox(height: 8 * scale),
                Text(_errorMessage, style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold, fontSize: 12 * scale)),
              ],

              SizedBox(height: 16 * scale),

              // Activate Button
              SizedBox(
                width: double.infinity,
                height: 48 * scale,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  onPressed: _isLoading ? null : _handleActivation,
                  child: _isLoading
                      ? SizedBox(width: 24 * scale, height: 24 * scale, child: const CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                      : Text(
                          TrilingualService.instance.getUIText('Activate Now'),
                          style: GoogleFonts.inter(fontSize: 16 * scale, fontWeight: FontWeight.bold),
                        ),
                ),
              ),

              SizedBox(height: 8 * scale),

              // Cancel
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: Text(
                  TrilingualService.instance.getUIText('Maybe Later'),
                  style: GoogleFonts.inter(color: AppColors.textSecondary, fontSize: 13 * scale),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
