import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/tts_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';


class DialogueWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const DialogueWidget({super.key, required this.data});

  @override
  State<DialogueWidget> createState() => _DialogueWidgetState();
}

class _DialogueWidgetState extends State<DialogueWidget> {
  int? _playingIndex;

  double get _currentRate {
    switch (TTSService.instance.currentSpeed.value) {
      case TTSSpeed.verySlow: return 0.18;
      case TTSSpeed.slow:     return 0.30;
      case TTSSpeed.medium:   return 0.50;
    }
  }

  Future<void> _playDialogue(int index, String text) async {
    if (_playingIndex == index) {
      await TTSService.instance.stop();
      if (mounted) setState(() => _playingIndex = null);
    } else {
      if (_playingIndex != null) await TTSService.instance.stop();
      if (mounted) setState(() => _playingIndex = index);
      
      // Strip markdown before speaking
      final cleanText = text.replaceAllMapped(RegExp(r'\[([^\|\]]+)\|([^\]]+)\]'), (match) => match.group(1)!);
      
      await TTSService.instance.speak(cleanText);
      
      if (mounted) setState(() => _playingIndex = null);
    }
  }

  @override
  void dispose() {
    TTSService.instance.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final payload = widget.data['data'] ?? widget.data;
    final title = payload['title'] ?? 'Conversation';
    final Map<String, dynamic> characters = payload['characters'] ?? {};
    final List<dynamic> messages = payload['messages'] ?? [];

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.grey[50],
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.blue.withValues(alpha: 0.1), width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.blue.withValues(alpha: 0.05),
            blurRadius: 20,
            offset: const Offset(0, 10),
          )
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
              border: Border(bottom: BorderSide(color: Colors.grey[200]!)),
            ),
            child: Row(
              children: [
                Icon(Icons.forum_rounded, color: Colors.blueAccent),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    title,
                    style: GoogleFonts.poppins(
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                      color: Colors.blue[900],
                    ),
                  ),
                ),
                ValueListenableBuilder<TTSSpeed>(
                  valueListenable: TTSService.instance.currentSpeed,
                  builder: (context, spd, _) {
                    return Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        _buildSpeedChip(TTSSpeed.verySlow, 'Very Slow', spd),
                        _buildSpeedChip(TTSSpeed.slow,     'Slow',      spd),
                        _buildSpeedChip(TTSSpeed.medium,   'Medium',    spd),
                      ],
                    );
                  },
                ),
              ],
            ),
          ),
          
          // Chat Messages
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              children: List.generate(messages.length, (index) {
                final msg = messages[index];
                final speakerId = msg['speaker'];
                final charInfo = characters[speakerId] ?? {};
                final name = charInfo['name'] ?? speakerId;
                final avatar = charInfo['avatar'] ?? '👤';
                
                final text = TrilingualService.instance.getLocalizedText(msg as Map<String, dynamic>, 'text');
                
                // For a simple two person dialogue, determine alignment
                final isMe = index % 2 != 0;

                return _buildChatBubble(
                  isMe: isMe,
                  name: name,
                  avatar: avatar,
                  text: text,
                  index: index,
                );
              }),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSpeedChip(TTSSpeed speed, String label, TTSSpeed current) {
    final isSelected = speed == current;
    return GestureDetector(
      onTap: () => TTSService.instance.setSpeed(speed),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 150),
        margin: const EdgeInsets.symmetric(horizontal: 2),
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
        decoration: BoxDecoration(
          color: isSelected ? Colors.blue : Colors.grey.shade100,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: isSelected ? Colors.blue : Colors.grey.shade300),
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

  Widget _buildChatBubble({
    required bool isMe,
    required String name,
    required String avatar,
    required String text,
    required int index,
  }) {
    final isPlaying = _playingIndex == index;
    
    return Padding(
      padding: const EdgeInsets.only(bottom: 16.0),
      child: Row(
        mainAxisAlignment: isMe ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          if (!isMe) _buildAvatar(avatar),
          if (!isMe) const SizedBox(width: 8),
          
          Flexible(
            child: Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: isMe ? Colors.blue[600] : Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(20),
                  topRight: const Radius.circular(20),
                  bottomLeft: Radius.circular(isMe ? 20 : 0),
                  bottomRight: Radius.circular(isMe ? 0 : 20),
                ),
                border: isMe ? null : Border.all(color: Colors.grey[200]!),
                boxShadow: [
                  BoxShadow(
                    color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05),
                    blurRadius: 5,
                    offset: const Offset(0, 2),
                  )
                ],
              ),
              child: Column(
                crossAxisAlignment: isMe ? CrossAxisAlignment.end : CrossAxisAlignment.start,
                children: [
                  Text(
                    name,
                    style: GoogleFonts.inter(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: isMe ? Colors.blue[100] : Colors.grey[500],
                    ),
                  ),
                  const SizedBox(height: 4),
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Flexible(
                        child: TtsInteractiveText(
                          text: text,
                          style: GoogleFonts.inter(
                            fontSize: 16,
                            color: isMe ? Colors.white : Colors.grey[800],
                            fontWeight: FontWeight.w500,
                          ).adaptToLanguage(),
                        ),
                      ),
                      const SizedBox(width: 12),
                      GestureDetector(
                        onTap: () => _playDialogue(index, text),
                        child: Icon(
                          isPlaying ? Icons.stop_circle : Icons.volume_up_rounded,
                          color: isMe ? Colors.white : Colors.blue[600],
                          size: 24,
                        ),
                      ),
                    ],
                  ),

                ],
              ),
            ),
          ),
          
          if (isMe) const SizedBox(width: 8),
          if (isMe) _buildAvatar(avatar),
        ],
      ),
    );
  }

  Widget _buildAvatar(String emoji) {
    return Container(
      width: 32,
      height: 32,
      decoration: BoxDecoration(
        color: Colors.grey[200],
        shape: BoxShape.circle,
      ),
      alignment: Alignment.center,
      child: Text(emoji, style: TextStyle(fontSize: 16)),
    );
  }
}
