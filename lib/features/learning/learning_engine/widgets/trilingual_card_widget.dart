import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/tts_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';

class TrilingualCardWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const TrilingualCardWidget({super.key, required this.data});

  @override
  State<TrilingualCardWidget> createState() => _TrilingualCardWidgetState();
}

class _TrilingualCardWidgetState extends State<TrilingualCardWidget> {
  bool _isPlaying = false;

  double get _currentRate {
    switch (TTSService.instance.currentSpeed.value) {
      case TTSSpeed.verySlow: return 0.18;
      case TTSSpeed.slow:     return 0.30;
      case TTSSpeed.medium:   return 0.50;
    }
  }

  Future<void> _playAudio() async {
    final text = widget.data['data']['english'] ?? '';
    if (text.isEmpty) return;

    setState(() => _isPlaying = true);
    await TTSService.instance.speak(text);
    if (mounted) setState(() => _isPlaying = false);
  }

  Future<void> _stopAudio() async {
    await TTSService.instance.stop();
    if (mounted) setState(() => _isPlaying = false);
  }

  @override
  void dispose() {
    TTSService.instance.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final payload = widget.data['data'] ?? {};
    final english = payload['english'] ?? '';
    final pronunciation = payload['pronunciation'] ?? '';
    final hindi = payload['hindi'] ?? '';
    final gujarati = payload['gujarati'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.indigo.withValues(alpha: 0.1),
            blurRadius: 10,
            offset: const Offset(0, 4),
          )
        ],
        border: Border.all(color: Colors.indigo.shade100),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // English Header with Audio Controls
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.indigo.shade50,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(16)),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      TtsInteractiveText(
                        text: english,
                        fullTtsText: _isPlaying ? english : null,
                        style: GoogleFonts.poppins(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                          color: Colors.indigo.shade900,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        pronunciation,
                        style: GoogleFonts.poppins(
                          fontSize: 16,
                          color: Colors.indigo.shade400,
                          fontStyle: FontStyle.italic,
                        ),
                      ),
                      const SizedBox(height: 12),
                      Row(
                        children: [
                          ValueListenableBuilder<TTSSpeed>(
                            valueListenable: TTSService.instance.currentSpeed,
                            builder: (context, spd, _) {
                              return Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  _buildSpeedChipTrilingual(TTSSpeed.verySlow, 'Very Slow', spd),
                                  _buildSpeedChipTrilingual(TTSSpeed.slow, 'Slow', spd),
                                  _buildSpeedChipTrilingual(TTSSpeed.medium, 'Medium', spd),
                                ],
                              );
                            },
                          ),
                          const SizedBox(width: 8),
                          // Play Button
                          InkWell(
                            onTap: _playAudio,
                            borderRadius: BorderRadius.circular(30),
                            child: Container(
                              padding: const EdgeInsets.all(8),
                              decoration: BoxDecoration(
                                color: Colors.indigo.shade50,
                                shape: BoxShape.circle,
                              ),
                              child: Icon(
                                Icons.play_arrow_rounded,
                                color: _isPlaying ? Colors.indigo.shade300 : Colors.indigo.shade600,
                                size: 28,
                              ),
                            ),
                          ),
                          const SizedBox(width: 8),
                          // Stop Button
                          InkWell(
                            onTap: _stopAudio,
                            borderRadius: BorderRadius.circular(30),
                            child: Container(
                              padding: const EdgeInsets.all(8),
                              decoration: BoxDecoration(
                                color: Colors.red.shade50,
                                shape: BoxShape.circle,
                              ),
                              child: Icon(
                                Icons.stop_rounded,
                                color: Colors.red.shade600,
                                size: 28,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          
          // Translations
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(TrilingualService.instance.getUIText("Hindi Meaning"),
                        style: GoogleFonts.inter(
                          fontSize: 12,
                          color: Colors.grey.shade600,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        hindi,
                        style: GoogleFonts.notoSans(
                          fontSize: 18,
                          color: Theme.of(context).colorScheme.onSurface,
                        ),
                      ),
                    ],
                  ),
                ),
                Container(width: 1, height: 40, color: Colors.grey.shade300),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(TrilingualService.instance.getUIText("Gujarati Meaning"),
                        style: GoogleFonts.inter(
                          fontSize: 12,
                          color: Colors.grey.shade600,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        gujarati,
                        style: GoogleFonts.notoSansGujarati(
                          fontSize: 18,
                          color: Theme.of(context).colorScheme.onSurface,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// Speed chip used by TrilingualCardWidget
Widget _buildSpeedChipTrilingual(TTSSpeed speed, String label, TTSSpeed current) {
  final isSelected = speed == current;
  return GestureDetector(
    onTap: () => TTSService.instance.setSpeed(speed),
    child: AnimatedContainer(
      duration: const Duration(milliseconds: 150),
      margin: const EdgeInsets.symmetric(horizontal: 2),
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: isSelected ? Colors.indigo : Colors.grey.shade100,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: isSelected ? Colors.indigo : Colors.grey.shade300),
      ),
      child: Text(
        label,
        style: TextStyle(
          fontSize: 10,
          fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
          color: isSelected ? Colors.white : Colors.grey.shade700,
        ),
      ),
    ),
  );
}
