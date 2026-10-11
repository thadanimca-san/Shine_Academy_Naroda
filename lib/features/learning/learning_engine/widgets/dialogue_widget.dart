import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/tts_service.dart';
import '../../../../core/services/gamification_service.dart';
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

  final Set<int> _practicedIndices = {};
  bool _isPlayingAll = false;
  bool _awardedXp = false;

  Future<void> _playAll(List<dynamic> messages) async {
    if (_isPlayingAll) {
      await TTSService.instance.stop();
      if (mounted) setState(() => _isPlayingAll = false);
      return;
    }

    setState(() => _isPlayingAll = true);
    for (int i = 0; i < messages.length; i++) {
      if (!_isPlayingAll || !mounted) break;
      final msg = messages[i];
      final text = TrilingualService.instance.getLocalizedText(msg as Map<String, dynamic>, 'text');
      final cleanText = text.replaceAllMapped(RegExp(r'\[([^\|\]]+)\|([^\]]+)\]'), (match) => match.group(1)!);
      
      setState(() {
        _playingIndex = i;
        _practicedIndices.add(i);
      });
      
      await TTSService.instance.speak(cleanText);
      await Future.delayed(const Duration(milliseconds: 600));
    }

    if (mounted) {
      setState(() {
        _playingIndex = null;
        _isPlayingAll = false;
      });
      _checkCompletion(messages.length);
    }
  }

  void _checkCompletion(int total) {
    if (_practicedIndices.length >= total && !_awardedXp) {
      _awardedXp = true;
      GamificationService.instance.addXp(30);
      GamificationService.instance.addCoins(10);
      if (mounted) setState(() {});
    }
  }

  @override
  Widget build(BuildContext context) {
    final payload = widget.data['data'] ?? widget.data;
    final title = payload['title'] ?? 'Conversation Practice';
    final Map<String, dynamic> characters = payload['characters'] ?? {};
    final List<dynamic> messages = payload['messages'] ?? [];

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.grey[50],
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.blue.withValues(alpha: 0.15), width: 1.5),
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
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        title,
                        style: GoogleFonts.poppins(
                          fontSize: 17,
                          fontWeight: FontWeight.w700,
                          color: Colors.blue[900],
                        ),
                      ),
                      Text(
                        _practicedIndices.length >= messages.length
                            ? 'Conversation Mastered! +30 XP ⭐'
                            : 'Practice speaking each turn aloud',
                        style: TextStyle(
                          fontSize: 12,
                          color: _practicedIndices.length >= messages.length
                              ? Colors.green[700]
                              : Colors.grey[600],
                          fontWeight: _practicedIndices.length >= messages.length
                              ? FontWeight.bold
                              : FontWeight.normal,
                        ),
                      ),
                    ],
                  ),
                ),
                // Play All Button (Sweet Male Voice)
                IconButton.filledTonal(
                  icon: Icon(_isPlayingAll ? Icons.stop_rounded : Icons.play_arrow_rounded),
                  tooltip: _isPlayingAll ? 'Stop Conversation' : 'Play full conversation in male voice',
                  onPressed: () => _playAll(messages),
                  style: IconButton.styleFrom(
                    backgroundColor: Colors.blue.shade50,
                    foregroundColor: Colors.blue.shade800,
                  ),
                ),
                const SizedBox(width: 8),
                ValueListenableBuilder<TTSSpeed>(
                  valueListenable: TTSService.instance.currentSpeed,
                  builder: (context, spd, _) {
                    return Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        _buildSpeedChip(TTSSpeed.slow,   'Slow',   spd),
                        _buildSpeedChip(TTSSpeed.medium, 'Medium', spd),
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
              children: [
                ...List.generate(messages.length, (index) {
                  final msg = messages[index];
                  final speakerId = msg['speaker'];
                  final charInfo = characters[speakerId] ?? {};
                  final name = charInfo['name'] ?? speakerId;
                  final avatar = charInfo['avatar'] ?? '👤';
                  
                  final text = TrilingualService.instance.getLocalizedText(msg as Map<String, dynamic>, 'text');
                  final isMe = index % 2 != 0;

                  return _buildChatBubble(
                    isMe: isMe,
                    name: name,
                    avatar: avatar,
                    text: text,
                    index: index,
                  );
                }),

                if (_practicedIndices.length >= messages.length) ...[
                  const SizedBox(height: 12),
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.green.shade50,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: Colors.green.shade300),
                    ),
                    child: Row(
                      children: [
                        const Text('🎉', style: TextStyle(fontSize: 22)),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Text(
                            'Great job! You completed this real-life conversation simulation! (+30 XP)',
                            style: GoogleFonts.poppins(
                              fontSize: 13,
                              fontWeight: FontWeight.w600,
                              color: Colors.green.shade900,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ],
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
