import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../core/services/gamification_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../core/services/tts_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';

/// SentencePuzzleWidget — Interactive Gamified Word Scramble
/// Specially crafted for Spoken English learners, housewives, and beginners.
/// Allows learners to tap scrambled word bubbles to build fluent, real-life English sentences,
/// hear them spoken in a sweet, impressive male voice, and earn XP & Stars.
class SentencePuzzleWidget extends StatefulWidget {
  final Map<String, dynamic> block;

  const SentencePuzzleWidget({super.key, required this.block});

  @override
  State<SentencePuzzleWidget> createState() => _SentencePuzzleWidgetState();
}

class _SentencePuzzleWidgetState extends State<SentencePuzzleWidget> {
  late List<String> _targetTokens;
  late String _targetSentence;
  late List<Map<String, dynamic>> _poolChips;
  final List<Map<String, dynamic>> _trayChips = [];

  bool _isCompleted = false;
  bool _hasError = false;
  bool _isSpeaking = false;

  @override
  void initState() {
    super.initState();
    _initializePuzzle();
  }

  void _initializePuzzle() {
    final payload = widget.block['content'] is Map ? widget.block['content'] : widget.block;
    
    // Extract target sentence
    if (payload['sentence'] != null && payload['sentence'].toString().isNotEmpty) {
      _targetSentence = payload['sentence'].toString().trim();
    } else if (payload['body'] != null && payload['body'].toString().isNotEmpty) {
      _targetSentence = payload['body'].toString().trim();
    } else {
      _targetSentence = "I want to speak English confidently.";
    }

    // Extract word tokens
    if (payload['words'] is List && (payload['words'] as List).isNotEmpty) {
      _targetTokens = (payload['words'] as List).map((e) => e.toString().trim()).toList();
    } else {
      _targetTokens = _targetSentence.split(RegExp(r'\s+')).where((s) => s.isNotEmpty).toList();
    }

    // Create unique chip pool
    final rawList = <Map<String, dynamic>>[];
    for (int i = 0; i < _targetTokens.length; i++) {
      rawList.add({
        'id': i,
        'word': _targetTokens[i],
      });
    }

    // Deterministically shuffle chip order so it is scrambled but reproducible
    final rng = math.Random(widget.block['id']?.hashCode ?? 42);
    _poolChips = List.from(rawList)..shuffle(rng);
    
    // Fallback if shuffle produced original order
    if (_poolChips.length > 1 && _poolChips.map((c) => c['word']).join(' ') == _targetSentence) {
      _poolChips = _poolChips.reversed.toList();
    }

    _trayChips.clear();
    _isCompleted = false;
    _hasError = false;
  }

  void _onPoolChipTapped(Map<String, dynamic> chip) {
    if (_isCompleted) return;
    setState(() {
      _poolChips.remove(chip);
      _trayChips.add(chip);
      _hasError = false;
    });
  }

  void _onTrayChipTapped(Map<String, dynamic> chip) {
    if (_isCompleted) return;
    setState(() {
      _trayChips.remove(chip);
      _poolChips.add(chip);
      _hasError = false;
    });
  }

  void _onResetTapped() {
    if (_isCompleted) return;
    setState(() {
      _initializePuzzle();
    });
  }

  Future<void> _checkAnswer() async {
    if (_trayChips.isEmpty) return;

    final userSentence = _trayChips.map((c) => c['word']).join(' ').trim();
    final cleanUser = userSentence.replaceAll(RegExp(r'[.,!?]'), '').toLowerCase();
    final cleanTarget = _targetSentence.replaceAll(RegExp(r'[.,!?]'), '').toLowerCase();

    if (cleanUser == cleanTarget) {
      setState(() {
        _isCompleted = true;
        _hasError = false;
      });

      // Award Gamification Rewards
      await GamificationService.instance.addXp(20);
      await GamificationService.instance.addCoins(5);

      // Play completed sentence in sweet male voice
      _playAudio();
    } else {
      setState(() {
        _hasError = true;
      });
    }
  }

  Future<void> _playAudio() async {
    if (_isSpeaking) {
      await TTSService.instance.stop();
      if (mounted) setState(() => _isSpeaking = false);
      return;
    }

    setState(() => _isSpeaking = true);
    await TTSService.instance.speak(_targetSentence);
    if (mounted) setState(() => _isSpeaking = false);
  }

  @override
  Widget build(BuildContext context) {
    final trilingual = TrilingualService.instance;
    final payload = widget.block['content'] is Map ? widget.block['content'] : widget.block;

    // Localized prompt
    final rawPrompt = trilingual.getLocalizedText(payload, 'prompt');
    final prompt = rawPrompt.isNotEmpty ? rawPrompt : 'Assemble the sentence correctly:';
    final rawTitle = trilingual.getLocalizedText(payload, 'title');
    final title = rawTitle.isNotEmpty ? rawTitle : 'Sentence Builder Puzzle';
    final phonetics = payload['phonetics'] ?? payload['pronunciation_hi'] ?? '';

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: _isCompleted 
              ? Colors.green.shade400 
              : (_hasError ? Colors.orange.shade300 : AppColors.primary.withValues(alpha: 0.18)),
          width: _isCompleted ? 2.2 : 1.5,
        ),
        boxShadow: [
          BoxShadow(
            color: (_isCompleted ? Colors.green : AppColors.primary).withValues(alpha: 0.08),
            blurRadius: 16,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header with Gamified Badges
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
            decoration: BoxDecoration(
              color: _isCompleted ? Colors.green.shade50 : const Color(0xFFF0F7FF),
              borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
              border: Border(bottom: BorderSide(color: Colors.grey.shade200)),
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: _isCompleted ? Colors.green.shade100 : Colors.blue.shade100,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(
                    _isCompleted ? Icons.check_circle_rounded : Icons.extension_rounded,
                    color: _isCompleted ? Colors.green.shade800 : Colors.blue.shade800,
                    size: 22,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        title,
                        style: GoogleFonts.poppins(
                          textStyle: AppTypography.h4(context),
                          fontWeight: FontWeight.w700,
                          color: _isCompleted ? Colors.green.shade900 : const Color(0xFF1E3A8A),
                        ),
                      ),
                      Text(
                        _isCompleted ? 'Goal Completed! +20 XP' : 'Tap words in correct order',
                        style: AppTypography.bodySmall(
                          context,
                          color: _isCompleted ? Colors.green.shade700 : Colors.blueGrey.shade600,
                        ),
                      ),
                    ],
                  ),
                ),
                // Audio listen button (Sweet Male Voice)
                IconButton.filledTonal(
                  icon: Icon(_isSpeaking ? Icons.stop_rounded : Icons.volume_up_rounded),
                  tooltip: 'Hear pronunciation in Govind Sir\'s male voice',
                  onPressed: _playAudio,
                  style: IconButton.styleFrom(
                    backgroundColor: _isCompleted ? Colors.green.shade100 : Colors.blue.shade50,
                    foregroundColor: _isCompleted ? Colors.green.shade800 : Colors.blue.shade800,
                  ),
                ),
              ],
            ),
          ),

          Padding(
            padding: const EdgeInsets.all(18),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Prompt text
                Text(
                  prompt,
                  style: GoogleFonts.inter(
                    textStyle: AppTypography.body(context),
                    fontWeight: FontWeight.w600,
                    color: Colors.black87,
                  ),
                ),

                // Devanagari Phonics Helper (Govind Sir's signature method)
                if (phonetics.toString().isNotEmpty) ...[
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                    decoration: BoxDecoration(
                      color: Colors.amber.shade50,
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(color: Colors.amber.shade300),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.record_voice_over_rounded, color: Colors.amber.shade900, size: 18),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            'बोलने का सही उच्चारण: $phonetics',
                            style: GoogleFonts.mukta(
                              textStyle: AppTypography.bodySmall(context),
                              color: Colors.amber.shade900,
                              fontWeight: FontWeight.w700,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],

                const SizedBox(height: 16),

                // Answer Tray (Where chosen words appear)
                Container(
                  constraints: const Duration(milliseconds: 100) == Duration.zero ? null : const BoxConstraints(minHeight: 70),
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: _isCompleted 
                        ? Colors.green.shade50 
                        : (_hasError ? Colors.orange.shade50 : const Color(0xFFF8FAFC)),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: _isCompleted 
                          ? Colors.green.shade300 
                          : (_hasError ? Colors.orange.shade400 : Colors.blueGrey.shade200),
                      width: 1.5,
                      style: BorderStyle.solid,
                    ),
                  ),
                  child: _trayChips.isEmpty
                      ? Center(
                          child: Text(
                            'Tap the word cards below to arrange your sentence here',
                            style: GoogleFonts.inter(
                              textStyle: AppTypography.bodySmall(context),
                              color: Colors.grey.shade500,
                              fontStyle: FontStyle.italic,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        )
                      : Wrap(
                          spacing: 8,
                          runSpacing: 8,
                          children: _trayChips.map((chip) {
                            return ActionChip(
                              avatar: const Icon(Icons.touch_app_outlined, size: 14, color: Colors.white70),
                              label: Text(
                                chip['word'],
                                style: GoogleFonts.poppins(
                                  textStyle: AppTypography.body(context),
                                  color: Colors.white,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                              backgroundColor: _isCompleted ? Colors.green.shade600 : const Color(0xFF1565C0),
                              onPressed: () => _onTrayChipTapped(chip),
                              elevation: 2,
                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                            );
                          }).toList(),
                        ),
                ),

                const SizedBox(height: 16),

                // Word Pool (Scrambled words to tap)
                if (_poolChips.isNotEmpty) ...[
                  Text(
                    'Available Words:',
                    style: AppTypography.bodySmall(context, color: Colors.grey.shade600, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 8),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: _poolChips.map((chip) {
                      return ActionChip(
                        label: Text(
                          chip['word'],
                          style: GoogleFonts.poppins(
                            textStyle: AppTypography.body(context),
                            color: const Color(0xFF0D47A1),
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                        backgroundColor: const Color(0xFFE3F2FD),
                        side: BorderSide(color: Colors.blue.shade300),
                        onPressed: () => _onPoolChipTapped(chip),
                        elevation: 1,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      );
                    }).toList(),
                  ),
                ],

                // Error / Encouragement Feedback
                if (_hasError) ...[
                  const SizedBox(height: 14),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                    decoration: BoxDecoration(
                      color: Colors.orange.shade50,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.orange.shade300),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.lightbulb_rounded, color: Colors.orange.shade800),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Text(
                            'Good try! Check the word order and try again. You can tap words in the top box to undo them.',
                            style: GoogleFonts.inter(
                              textStyle: AppTypography.bodySmall(context),
                              color: Colors.orange.shade900,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],

                // Success Celebration Banner
                if (_isCompleted) ...[
                  const SizedBox(height: 14),
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.green.shade50,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: Colors.green.shade400),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            const Text('⭐⭐⭐', style: TextStyle(fontSize: 20)),
                            const SizedBox(width: 8),
                            Expanded(
                              child: Text(
                                'Fantastic! You spoke the sentence correctly!',
                                style: GoogleFonts.poppins(
                                  textStyle: AppTypography.body(context),
                                  fontWeight: FontWeight.w700,
                                  color: Colors.green.shade900,
                                ),
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 6),
                        Text(
                          'Now listen to Govind Sir\'s sweet pronunciation and repeat it aloud twice to build speaking confidence!',
                          style: GoogleFonts.inter(
                            textStyle: AppTypography.bodySmall(context),
                            color: Colors.green.shade800,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],

                const SizedBox(height: 18),

                // Action Buttons
                Row(
                  children: [
                    if (!_isCompleted) ...[
                      TextButton.icon(
                        icon: const Icon(Icons.refresh_rounded, size: 18),
                        label: const Text('Reset'),
                        onPressed: _trayChips.isEmpty ? null : _onResetTapped,
                        style: TextButton.styleFrom(
                          foregroundColor: Colors.blueGrey,
                        ),
                      ),
                      const Spacer(),
                      ElevatedButton.icon(
                        icon: const Icon(Icons.check_rounded, color: Colors.white),
                        label: Text(
                          'Check Answer',
                          style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.white),
                        ),
                        onPressed: _trayChips.isEmpty ? null : _checkAnswer,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFF1976D2),
                          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                        ),
                      ),
                    ] else ...[
                      const Spacer(),
                      FilledButton.icon(
                        icon: Icon(_isSpeaking ? Icons.stop_rounded : Icons.volume_up_rounded),
                        label: Text(_isSpeaking ? 'Stop Audio' : 'Listen Again (Male Voice)'),
                        onPressed: _playAudio,
                        style: FilledButton.styleFrom(
                          backgroundColor: Colors.green.shade700,
                          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                        ),
                      ),
                    ],
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
