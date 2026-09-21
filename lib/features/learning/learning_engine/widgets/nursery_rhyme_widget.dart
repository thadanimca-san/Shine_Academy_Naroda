import 'package:flutter/material.dart';
import '../../school/english/services/speech_service.dart';
import '../../../../core/services/tts_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import '../../../../foundation/theme/app_colors.dart';

class NurseryRhymeWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const NurseryRhymeWidget({super.key, required this.data});

  @override
  State<NurseryRhymeWidget> createState() => _NurseryRhymeWidgetState();
}

class _NurseryRhymeWidgetState extends State<NurseryRhymeWidget> with SingleTickerProviderStateMixin {
  bool _isPlaying = false;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 1),
    );
    SpeechService.instance.setOnComplete(() {
      if (mounted) {
        setState(() => _isPlaying = false);
        _controller.stop();
      }
    });
    TTSService.instance.isPlayingGlobal.addListener(_onTtsStateChange);
  }

  void _onTtsStateChange() {
    if (!mounted) return;
    if (!TTSService.instance.isPlayingGlobal.value && _isPlaying) {
      setState(() => _isPlaying = false);
      _controller.stop();
    }
  }

  @override
  void dispose() {
    TTSService.instance.isPlayingGlobal.removeListener(_onTtsStateChange);
    if (_isPlaying) {
      SpeechService.instance.stop();
      TTSService.instance.stop();
    }
    _controller.dispose();
    super.dispose();
  }

  Future<void> _togglePlay() async {
    if (_isPlaying) {
      await SpeechService.instance.stop();
      await TTSService.instance.stop();
      setState(() => _isPlaying = false);
      _controller.stop();
    } else {
      setState(() => _isPlaying = true);
      _controller.repeat(reverse: true);
      String? assetPath = widget.data['audio_url'];
      if (assetPath != null && assetPath.isNotEmpty) {
        await SpeechService.instance.playAudio(assetPath);
      } else {
        await TTSService.instance.speak(widget.data['lyrics'] ?? widget.data['content'] ?? 'No lyrics available');
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final title = widget.data['title'] ?? 'Rhyme';
    final content = widget.data['lyrics'] ?? widget.data['content'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: AppColors.primary.withValues(alpha: 0.1),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: AppColors.primary.withValues(alpha: 0.3), width: 3),
      ),
      child: Column(
        children: [
          Text(
            title,
            style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.primary),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          GestureDetector(
            onTap: _togglePlay,
            child: ScaleTransition(
              scale: Tween<double>(begin: 1.0, end: 1.1).animate(_controller),
              child: Container(
                width: 120,
                height: 120,
                decoration: BoxDecoration(
                  color: _isPlaying ? Colors.red : Colors.green,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: (_isPlaying ? Colors.red : Colors.green).withValues(alpha: 0.4),
                      blurRadius: 15,
                      spreadRadius: 5,
                    ),
                  ],
                ),
                child: Icon(
                  _isPlaying ? Icons.stop_rounded : Icons.play_arrow_rounded,
                  size: 64,
                  color: Colors.white,
                ),
              ),
            ),
          ),
          const SizedBox(height: 24),
          TtsInteractiveText(
            text: content,
            style: TextStyle(fontSize: 20, height: 1.5, fontWeight: FontWeight.w600, color: Theme.of(context).colorScheme.onSurface),
            highlightColor: Colors.amber.withValues(alpha: 0.5),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}
