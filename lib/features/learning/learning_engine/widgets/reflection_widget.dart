import 'package:flutter/material.dart';
import '../../../../../foundation/theme/app_colors.dart';
import '../../../../../foundation/theme/app_typography.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../core/services/tts_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';

class ReflectionWidget extends StatefulWidget {
  final Map<String, dynamic> block;

  const ReflectionWidget({super.key, required this.block});

  @override
  State<ReflectionWidget> createState() => _ReflectionWidgetState();
}

class _ReflectionWidgetState extends State<ReflectionWidget> {
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
        color: Colors.teal.shade50,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.teal.shade200, width: 2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: Colors.teal.shade100,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
            ),
            child: Row(
              children: [
                Icon(Icons.self_improvement, color: Colors.teal.shade800),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    title.isEmpty ? TrilingualService.instance.getUIText('Reflection') : title,
                    style: AppTypography.h4(context, color: Colors.teal.shade900, fontWeight: FontWeight.bold),
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
                        color: Colors.teal.shade800,
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
                style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface).copyWith(fontStyle: FontStyle.italic),
              ),
            ),
        ],
      ),
    );
  }
}
