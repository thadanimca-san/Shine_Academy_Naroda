import 'package:flutter/material.dart';
import '../../../core/services/tts_service.dart';
import '../../../foundation/theme/app_colors.dart';
import '../../../core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A compact speed selector row used wherever TTS is active.
/// Provides three options: Very Slow | Slow | Medium (no Fast).
class TTSSpeedController extends StatelessWidget {
  const TTSSpeedController({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<TTSSpeed>(
      valueListenable: TTSService.instance.currentSpeed,
      builder: (context, currentSpeed, child) {
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: Colors.grey.shade300),
            boxShadow: [
              BoxShadow(
                color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.04),
                blurRadius: 4,
                offset: const Offset(0, 2),
              )
            ],
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.graphic_eq, size: 16, color: Colors.grey),
              const SizedBox(width: 6),
              _SpeedChip(speed: TTSSpeed.verySlow, label: TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Very Slow')), current: currentSpeed),
              const SizedBox(width: 4),
              _SpeedChip(speed: TTSSpeed.slow,     label: TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Slow')),      current: currentSpeed),
              const SizedBox(width: 4),
              _SpeedChip(speed: TTSSpeed.medium,   label: TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Medium')),    current: currentSpeed),
            ],
          ),
        );
      },
    );
  }
}

class _SpeedChip extends StatelessWidget {
  final TTSSpeed speed;
  final String label;
  final TTSSpeed current;

  const _SpeedChip({required this.speed, required this.label, required this.current});

  @override
  Widget build(BuildContext context) {
    final isSelected = speed == current;
    return GestureDetector(
      onTap: () => TTSService.instance.setSpeed(speed),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
        decoration: BoxDecoration(
          color: isSelected ? AppColors.primary : Colors.transparent,
          borderRadius: BorderRadius.circular(12),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 11,
            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
            color: isSelected ? Colors.white : Colors.grey.shade700,
          ),
        ),
      ),
    );
  }
}
