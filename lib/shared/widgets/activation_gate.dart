import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/services/activation_service.dart';
import '../../foundation/theme/app_typography.dart';
import 'activation_dialog.dart';

/// A reusable wrapper that applies a watermark/faded preview effect
/// to locked content in the skillup flavor.
///
/// When [isFree] is true, the child is rendered normally.
/// When [isFree] is false AND activation is not done, the child is rendered
/// with very low opacity (ghosted/watermark look) and a lock overlay.
/// Tapping the locked child shows the [ActivationDialog].
///
/// Usage:
/// ```dart
/// ActivationGate(
///   isFree: index < 2,  // first 2 chapters free
///   onActivated: () => setState(() {}),
///   child: MyChapterCard(...),
/// )
/// ```
class ActivationGate extends StatelessWidget {
  final Widget child;
  final bool isFree;
  final VoidCallback? onActivated;

  /// Optional custom lock badge text. Defaults to '🔒 Premium'.
  final String? lockLabel;

  const ActivationGate({
    super.key,
    required this.child,
    this.isFree = false,
    this.onActivated,
    this.lockLabel,
  });

  @override
  Widget build(BuildContext context) {
    // If content is free OR app is activated, show child normally
    if (isFree || ActivationService.isActivated) {
      return child;
    }

    final scale = AppTypography.scaleFactor(context);

    // Locked: show ghosted/watermark version
    return GestureDetector(
      onTap: () {
        ActivationDialog.show(context, onActivated: onActivated);
      },
      child: Stack(
        children: [
          // The actual content rendered very lightly (watermark effect)
          Opacity(
            opacity: 0.18,
            child: IgnorePointer(
              child: child,
            ),
          ),

          // Lock overlay badge centered on the card
          Positioned.fill(
            child: Center(
              child: Container(
                padding: EdgeInsets.symmetric(horizontal: 14 * scale, vertical: 8 * scale),
                decoration: BoxDecoration(
                  color: Colors.black.withValues(alpha: 0.45),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.lock, color: Colors.white, size: 16 * scale),
                    SizedBox(width: 6 * scale),
                    Text(
                      lockLabel ?? '🔒 Premium',
                      style: GoogleFonts.inter(
                        color: Colors.white,
                        fontSize: 12 * scale,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
