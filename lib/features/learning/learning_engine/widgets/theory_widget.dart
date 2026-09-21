import 'package:flutter/material.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../core/services/tts_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../common/widgets/tts_speed_controller.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import '../../../../foundation/theme/app_typography.dart';

class TheoryWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  final String type;
  
  const TheoryWidget({super.key, required this.block, required this.type});

  @override
  State<TheoryWidget> createState() => _TheoryWidgetState();
}

class _TheoryWidgetState extends State<TheoryWidget> {
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
    // Different visual styles for different semantic types
    Color bgColor = Colors.transparent;
    Color iconColor = Colors.blue;
    IconData icon = Icons.info_outline;
    
    if (widget.type == 'reveal') {
      bgColor = Colors.blue.shade50;
      iconColor = Colors.blue;
      icon = Icons.star;
    } else if (widget.type == 'discovery') {
      bgColor = Colors.teal.shade50;
      iconColor = Colors.teal;
      icon = Icons.explore;
    } else if (widget.type == 'mastery') {
      bgColor = Colors.indigo.shade50;
      iconColor = Colors.indigo;
      icon = Icons.military_tech;
    }

    final body = TrilingualService.instance.getLocalizedText(widget.block, 'body');

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: bgColor != Colors.transparent ? const EdgeInsets.all(20) : EdgeInsets.zero,
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (widget.block.containsKey('title') && widget.block['title'].toString().isNotEmpty) ...[
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (widget.type != 'theory') ...[
                  Icon(icon, color: iconColor, size: 24),
                  const SizedBox(width: 12),
                ],
                Expanded(
                  child: Text(
                    TrilingualService.instance.getLocalizedText(widget.block, 'title'),
                    style: AppTypography.h4(context, color: Theme.of(context).colorScheme.onSurface, fontWeight: FontWeight.bold),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
          ],
          TtsInteractiveText(
            text: body,
            style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface),
          ),
          
          // Controls (TTS & Hindi Toggle)
          if (body.isNotEmpty)
            Padding(
              padding: const EdgeInsets.only(top: 12.0),
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
                          color: _isPlaying ? Colors.blue.shade300 : Colors.blue.shade700,
                          size: 26,
                        ),
                        const SizedBox(width: 4),
                        Text(
                          TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Start')),
                          style: TextStyle(
                            fontSize: 12 * AppTypography.scaleFactor(context), 
                            color: _isPlaying ? Colors.blue.shade300 : Colors.blue.shade700, 
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
                  const TTSSpeedController(),
                ],
              ),
            ),

          if ((widget.block['visuals'] != null && widget.block['visuals']['image_url'] != null) || widget.block['image_url'] != null || widget.block['path'] != null)
            Padding(
              padding: const EdgeInsets.only(top: 16.0),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxHeight: 350),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(12),
                  child: GestureDetector(
                    onTap: () {
                      showDialog(
                        context: context,
                        builder: (context) => Dialog(
                          backgroundColor: Colors.black,
                          insetPadding: EdgeInsets.zero,
                          child: Stack(
                            children: [
                              InteractiveViewer(
                                minScale: 0.5,
                                maxScale: 4.0,
                                child: Center(
                                  child: Image.asset(
                                    widget.block['image_url'] ?? widget.block['path'] ?? widget.block['visuals']['image_url'],
                                    fit: BoxFit.contain,
                                  ),
                                ),
                              ),
                              Positioned(
                                top: 40,
                                right: 20,
                                child: IconButton(
                                  icon: Icon(Icons.close, color: Colors.white, size: 30),
                                  onPressed: () => Navigator.of(context).pop(),
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                    child: Hero(
                      tag: widget.block['image_url'] ?? widget.block['path'] ?? 'image',
                      child: Image.asset(
                        widget.block['image_url'] ?? widget.block['path'] ?? widget.block['visuals']['image_url'],
                        width: double.infinity,
                        fit: BoxFit.contain,
                        errorBuilder: (context, error, stackTrace) => 
                          Container(color: Colors.grey.shade200, height: 150, child: const Center(child: Icon(Icons.broken_image, color: Colors.grey))),
                      ),
                    ),
                  ),
                ),
              ),
            ),
          if (widget.block['caption'] != null && widget.block['caption'].toString().isNotEmpty)
            Padding(
              padding: const EdgeInsets.only(top: 8.0),
              child: Text(
                TrilingualService.instance.getLocalizedText(widget.block, 'caption'),
                style: AppTypography.bodySmall(context, color: Colors.grey.shade700).copyWith(fontStyle: FontStyle.italic),
                textAlign: TextAlign.center,
              ),
            ),
        ],
      ),
    );
  }
}
