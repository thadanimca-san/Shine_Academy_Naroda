import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../../core/services/tts_service.dart';
import '../theme/app_theme.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A self-contained "Read aloud" button with:
///   • Play / Stop toggle
///   • Inline speed selector: Very Slow | Slow | Medium
///   • Optional Hindi translation panel (shown when [hindiText] is provided)
///
/// Used in chapter readers and passage screens throughout Shine Academy.
class ReadAloudButton extends StatefulWidget {
  final String text;
  final String label;
  final String? hindiText; // If provided, a Hindi toggle button is shown
  final String? forceLanguage; // If provided, forces TTS to use this language regardless of UI language

  const ReadAloudButton({
    super.key,
    required this.text,
    this.label = 'Read aloud',
    this.hindiText,
    this.forceLanguage,
  });

  @override
  State<ReadAloudButton> createState() => _ReadAloudButtonState();
}

class _ReadAloudButtonState extends State<ReadAloudButton> {
  bool _speaking = false;

  @override
  void initState() {
    super.initState();
    TTSService.instance.progress.addListener(_onProgress);
  }

  void _onProgress() {
    if (TTSService.instance.progress.value == TtsProgress.empty && _speaking) {
      if (mounted) setState(() => _speaking = false);
    }
  }

  @override
  void dispose() {
    TTSService.instance.progress.removeListener(_onProgress);
    if (_speaking) TTSService.instance.stop();
    super.dispose();
  }

  Future<void> _playAudio() async {
    if (mounted) setState(() => _speaking = true);
    await TTSService.instance.speak(widget.text, forceLanguage: widget.forceLanguage);
    if (mounted) setState(() => _speaking = false);
  }

  Future<void> _stopAudio() async {
    await TTSService.instance.stop();
    if (mounted) setState(() => _speaking = false);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // ── Row: Play button + speed chips ──────────────────────────────
        Wrap(
          spacing: 8,
          runSpacing: 6,
          crossAxisAlignment: WrapCrossAlignment.center,
          children: [
            InkWell(
              borderRadius: BorderRadius.circular(20),
              onTap: _playAudio,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: _speaking ? AppColors.tealTint.withValues(alpha: 0.5) : AppColors.tealTint,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(
                    color: AppColors.rule,
                  ),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      Icons.play_circle_fill,
                      size: 18,
                      color: _speaking ? AppColors.tealDeep.withValues(alpha: 0.5) : AppColors.tealDeep,
                    ),
                    const SizedBox(width: 6),
                    Text(TrilingualService.instance.getUIText('Start'),
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                        color: _speaking ? AppColors.tealDeep.withValues(alpha: 0.5) : AppColors.tealDeep,
                      ),
                    ),
                  ],
                ),
              ),
            ),

            // Stop button
            InkWell(
              borderRadius: BorderRadius.circular(20),
              onTap: _stopAudio,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: Colors.red.shade50,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(
                    color: Colors.red.shade200,
                  ),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      Icons.stop_circle,
                      size: 18,
                      color: Colors.red.shade600,
                    ),
                    const SizedBox(width: 6),
                    Text(TrilingualService.instance.getUIText('Stop'),
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                        color: Colors.red.shade600,
                      ),
                    ),
                  ],
                ),
              ),
            ),

            // Speed chips (inline, compact)
            _InlineSpeedSelector(),
          ],
        ),
      ],
    );
  }
}

// ── Inline speed selector ────────────────────────────────────────────────────
class _InlineSpeedSelector extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<TTSSpeed>(
      valueListenable: TTSService.instance.currentSpeed,
      builder: (context, current, _) {
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: Colors.grey.shade300),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              _chip(TTSSpeed.verySlow, 'Very Slow', current),
              const SizedBox(width: 2),
              _chip(TTSSpeed.slow,     'Slow',      current),
              const SizedBox(width: 2),
              _chip(TTSSpeed.medium,   'Medium',    current),
            ],
          ),
        );
      },
    );
  }

  Widget _chip(TTSSpeed speed, String label, TTSSpeed current) {
    final isSelected = speed == current;
    return GestureDetector(
      onTap: () => TTSService.instance.setSpeed(speed),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 150),
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
        decoration: BoxDecoration(
          color: isSelected ? Colors.teal : Colors.transparent,
          borderRadius: BorderRadius.circular(10),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 10,
            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
            color: isSelected ? Colors.white : Colors.grey.shade600,
          ),
        ),
      ),
    );
  }
}
