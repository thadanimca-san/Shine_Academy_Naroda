import 'package:flutter/material.dart';
import '../../../../../foundation/theme/app_colors.dart';
import '../../../../../foundation/theme/app_typography.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../core/services/tts_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';

class MasteryWidget extends StatefulWidget {
  final Map<String, dynamic> block;

  const MasteryWidget({super.key, required this.block});

  @override
  State<MasteryWidget> createState() => _MasteryWidgetState();
}

class _MasteryWidgetState extends State<MasteryWidget> {
  bool _isPlaying = false;

  @override
  void initState() {
    super.initState();
    TTSService.instance.isPlayingGlobal.addListener(_onPlayingChanged);
  }

  void _onPlayingChanged() {
    if (mounted) {
      setState(() => _isPlaying = TTSService.instance.isPlayingGlobal.value);
    }
  }

  Future<void> _togglePlay({required bool isStop}) async {
    final body = TrilingualService.instance.getLocalizedText(widget.block, 'body');
    if (body.isEmpty) return;
    if (isStop) {
      await TTSService.instance.stop();
    } else {
      await TTSService.instance.speak(body);
    }
  }

  @override
  void dispose() {
    TTSService.instance.isPlayingGlobal.removeListener(_onPlayingChanged);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final body = TrilingualService.instance.getLocalizedText(widget.block, 'body');
    final title = TrilingualService.instance.getLocalizedText(widget.block, 'title');

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.amber.shade100, Colors.orange.shade50],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.amber.shade400, width: 2),
        boxShadow: [
          BoxShadow(
            color: Colors.amber.withOpacity(0.2),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: Colors.amber.shade200,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
            ),
            child: Row(
              children: [
                Icon(Icons.military_tech, color: Colors.amber.shade900, size: 28),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    title.isEmpty ? TrilingualService.instance.getUIText('Mastery Challenge') : title,
                    style: AppTypography.h4(context, color: Colors.amber.shade900, fontWeight: FontWeight.bold),
                  ),
                ),
                if (body.isNotEmpty)
                  InkWell(
                    onTap: () => _togglePlay(isStop: _isPlaying),
                    borderRadius: BorderRadius.circular(20),
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.05),
                            blurRadius: 4,
                            offset: const Offset(0, 2),
                          ),
                        ],
                      ),
                      child: Icon(
                        _isPlaying ? Icons.stop_rounded : Icons.volume_up_rounded,
                        color: Colors.amber.shade900,
                        size: 20,
                      ),
                    ),
                  ),
              ],
            ),
          ),

          // Body text
          if (body.isNotEmpty)
            Padding(
              padding: const EdgeInsets.all(16),
              child: TtsInteractiveText(
                text: body,
                style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface).copyWith(fontWeight: FontWeight.w500),
              ),
            ),
        ],
      ),
    );
  }
}
