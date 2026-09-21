import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import '../../../../core/services/tts_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../common/widgets/tts_speed_controller.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
class TeacherTipWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  const TeacherTipWidget({super.key, required this.block});

  @override
  State<TeacherTipWidget> createState() => _TeacherTipWidgetState();
}

class _TeacherTipWidgetState extends State<TeacherTipWidget> {
  bool _isPlaying = false;

  String get _body => (widget.block['body'] ?? widget.block['content'] ?? widget.block['tip'] ?? '').toString();

  Future<void> _playAudio() async {
    if (_body.isEmpty) return;
    if (mounted) setState(() => _isPlaying = true);
    final clean = _body.replaceAll(RegExp(r'[*_`#\[\]()>]'), '');
    await TTSService.instance.speak(clean);
    if (mounted) setState(() => _isPlaying = false);
  }

  Future<void> _stopAudio() async {
    await TTSService.instance.stop();
    if (mounted) setState(() => _isPlaying = false);
  }

  @override
  void dispose() {
    if (_isPlaying) TTSService.instance.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.amber.shade50,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.amber.shade300),
      ),
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          Padding(
            padding: const EdgeInsets.all(20.0).copyWith(left: 64),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  widget.block['title'] ?? "Teacher's Tip",
                  style: GoogleFonts.poppins(fontWeight: FontWeight.bold, fontSize: 15, color: Colors.amber.shade900),
                ),
                const SizedBox(height: 8),
                TtsInteractiveText(
                  text: _body,
                  style: GoogleFonts.inter(fontSize: 14, height: 1.5, color: Theme.of(context).colorScheme.onSurface),
                ),

                // TTS controls
                if (_body.isNotEmpty) ...[ 
                  const SizedBox(height: 10),
                  Wrap(
                    spacing: 8,
                    runSpacing: 6,
                    crossAxisAlignment: WrapCrossAlignment.center,
                    children: [
                      InkWell(
                        onTap: _playAudio,
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              Icons.play_circle_fill,
                              color: _isPlaying ? Colors.amber.shade300 : Colors.amber.shade800,
                              size: 24,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Start')),
                              style: TextStyle(
                                fontSize: 12, 
                                color: _isPlaying ? Colors.amber.shade300 : Colors.amber.shade800, 
                                fontWeight: FontWeight.w600
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(width: 4),
                      InkWell(
                        onTap: _stopAudio,
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              Icons.stop_circle,
                              color: Colors.red.shade600,
                              size: 24,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Stop')),
                              style: TextStyle(
                                fontSize: 12, 
                                color: Colors.red.shade600, 
                                fontWeight: FontWeight.w600
                              ),
                            ),
                          ],
                        ),
                      ),
                      const TTSSpeedController(),
                    ],
                  ),
                ],
              ],
            ),
          ),
          Positioned(
            left: -12,
            top: 20,
            child: CircleAvatar(
              radius: 24,
              backgroundColor: Colors.amber,
              child: Icon(Icons.school, color: Colors.white, size: 28),
            ),
          ),
        ],
      ),
    );
  }
}
