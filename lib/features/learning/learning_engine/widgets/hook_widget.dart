import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/tts_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../common/widgets/tts_speed_controller.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/app_typography.dart';

class HookWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  const HookWidget({super.key, required this.block});

  @override
  State<HookWidget> createState() => _HookWidgetState();
}

class _HookWidgetState extends State<HookWidget> {
  bool _isPlaying = false;

  Future<void> _togglePlay({required bool isStop}) async {
    final body = TrilingualService.instance.getLocalizedText(widget.block, 'body');
    if (body.isEmpty) return;
    if (isStop) {
      await TTSService.instance.stop();
      if (mounted) setState(() => _isPlaying = false);
    } else {
      if (mounted) setState(() => _isPlaying = true);
      await TTSService.instance.speak(body);
      if (mounted) setState(() => _isPlaying = false);
    }
  }

  @override
  void dispose() {
    if (_isPlaying) TTSService.instance.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final body = TrilingualService.instance.getLocalizedText(widget.block, 'body');
    final title = TrilingualService.instance.getLocalizedText(widget.block, 'title');

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.orange.shade50,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.orange.shade200, width: 2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: Colors.orange.shade100,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
            ),
            child: Row(
              children: [
                Icon(Icons.lightbulb, color: Colors.orange),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    title.isEmpty ? 'The Hook' : title,
                    style: AppTypography.h4(context, color: Colors.orange.shade900, fontWeight: FontWeight.bold),
                  ),
                ),
              ],
            ),
          ),

          // Body text
          if (body.isNotEmpty)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
              child: TtsInteractiveText(
                text: body,
                style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface),
              ),
            ),

          // TTS + Hindi controls
          if (body.isNotEmpty)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
              child: Wrap(
                spacing: 8,
                runSpacing: 6,
                crossAxisAlignment: WrapCrossAlignment.center,
                children: [
                  // Play Button
                  InkWell(
                    onTap: () => _togglePlay(isStop: false),
                    borderRadius: BorderRadius.circular(20),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.play_circle,
                          color: _isPlaying ? Colors.orange.shade300 : Colors.orange.shade700,
                          size: 26,
                        ),
                        const SizedBox(width: 4),
                        Text(
                          TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Start')),
                          style: TextStyle(
                            fontSize: 12 * AppTypography.scaleFactor(context), 
                            color: _isPlaying ? Colors.orange.shade300 : Colors.orange.shade700, 
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                  // Stop Button
                  InkWell(
                    onTap: () => _togglePlay(isStop: true),
                    borderRadius: BorderRadius.circular(20),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.stop_circle,
                          color: Colors.red.shade600,
                          size: 26,
                        ),
                        const SizedBox(width: 4),
                        Text(
                          TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Stop')),
                          style: TextStyle(fontSize: 12 * AppTypography.scaleFactor(context), color: Colors.red.shade600, fontWeight: FontWeight.w600),
                        ),
                      ],
                    ),
                  ),
                  // Speed selector
                  const TTSSpeedController(),
                ],
              ),
            ),

          // Image
          if (widget.block['visuals'] != null && widget.block['visuals']['image_url'] != null)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxHeight: 350),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(12),
                  child: Image.asset(
                    widget.block['visuals']['image_url'],
                    width: double.infinity,
                    fit: BoxFit.contain,
                    errorBuilder: (context, error, stackTrace) =>
                        Container(color: Colors.grey.shade200, height: 150, child: const Center(child: Icon(Icons.broken_image, color: Colors.grey))),
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}
