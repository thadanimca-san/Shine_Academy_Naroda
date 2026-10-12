import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show appFlavor;
import 'package:google_fonts/google_fonts.dart';

import '../../../../core/services/tts_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../core/services/english_phonetics_helper.dart';
import '../../../common/widgets/tts_speed_controller.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import '../../../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

class TheoryWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  final String type;
  
  const TheoryWidget({super.key, required this.block, required this.type});

  @override
  State<TheoryWidget> createState() => _TheoryWidgetState();
}

class _TheoryWidgetState extends State<TheoryWidget> {
  bool _isPlaying = false;
  bool _showReadingGuide = false;

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

    // Extract side-by-side pronunciation and meanings for adult learners
    final String rawEnglish = widget.block['body']?.toString() ?? widget.block['content']?.toString() ?? '';
    final String rawPhonetics = widget.block['phonetic_hi']?.toString() ??
        widget.block['phonetics']?.toString() ??
        widget.block['pronunciation_hi']?.toString() ??
        widget.block['pronunciation_guide']?.toString() ??
        '';
    final String phonetics = (rawPhonetics.isEmpty || rawPhonetics == 'आई कैन स्पीक इंग्लिश विद कॉन्फिडेंस।')
        ? EnglishPhoneticsHelper.toDevanagari(rawEnglish)
        : rawPhonetics;

    final String hindiMeaning = widget.block['body_hi']?.toString() ??
        widget.block['meaning_hi']?.toString() ??
        widget.block['translation_hi']?.toString() ??
        '';
    final String gujaratiMeaning = widget.block['body_gu']?.toString() ??
        widget.block['meaning_gu']?.toString() ??
        widget.block['translation_gu']?.toString() ??
        '';

    final bool isSkillup = (appFlavor == 'skillup');
    final bool hasGuideContent = isSkillup && (phonetics.isNotEmpty || hindiMeaning.isNotEmpty || gujaratiMeaning.isNotEmpty);

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
                  child: MathTitle(
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
          
          // Controls (TTS & Side-by-Side Reading Guide)
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
                          TrilingualService.instance.getUIText('Start'),
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
                          TrilingualService.instance.getUIText('Stop'),
                          style: TextStyle(fontSize: 12 * AppTypography.scaleFactor(context), color: Colors.red.shade600, fontWeight: FontWeight.w600),
                        ),
                      ],
                    ),
                  ),
                  const TTSSpeedController(),

                  // Side-by-Side Pronunciation & Meaning Guide Button
                  if (hasGuideContent)
                    ActionChip(
                      avatar: Icon(
                        _showReadingGuide ? Icons.visibility_off : Icons.translate,
                        size: 16,
                        color: _showReadingGuide ? Colors.indigo.shade900 : Colors.indigo.shade700,
                      ),
                      label: Text(
                        _showReadingGuide
                            ? TrilingualService.instance.getUIText('Hide Guide')
                            : TrilingualService.instance.getUIText('📖 उच्चारण व अर्थ (Guide)'),
                        style: TextStyle(
                          fontSize: 12 * AppTypography.scaleFactor(context),
                          fontWeight: FontWeight.bold,
                          color: _showReadingGuide ? Colors.indigo.shade900 : Colors.indigo.shade700,
                        ),
                      ),
                      backgroundColor: _showReadingGuide ? Colors.indigo.shade100 : Colors.indigo.shade50,
                      side: BorderSide(color: Colors.indigo.shade200),
                      padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 0),
                      onPressed: () {
                        setState(() {
                          _showReadingGuide = !_showReadingGuide;
                        });
                      },
                    ),
                ],
              ),
            ),

          // Side-by-side / Expanded Reading Guide Panel
          if (_showReadingGuide && hasGuideContent)
            _buildReadingGuidePanel(context, phonetics, hindiMeaning, gujaratiMeaning),

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

  Widget _buildReadingGuidePanel(
    BuildContext context,
    String phonetics,
    String hindiMeaning,
    String gujaratiMeaning,
  ) {
    final double width = MediaQuery.of(context).size.width;
    final bool isWide = width >= 700;

    return Container(
      margin: const EdgeInsets.only(top: 14),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.indigo.shade50.withValues(alpha: 0.6),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.indigo.shade200, width: 1.2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.auto_stories, size: 20, color: Colors.indigo.shade700),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  TrilingualService.instance.getUIText('उच्चारण और अर्थ (Reading & Meaning Guide)'),
                  style: GoogleFonts.outfit(
                    fontWeight: FontWeight.bold,
                    fontSize: 13 * AppTypography.scaleFactor(context),
                    color: Colors.indigo.shade900,
                  ),
                ),
              ),
              InkWell(
                onTap: () => setState(() => _showReadingGuide = false),
                child: Container(
                  padding: const EdgeInsets.all(4),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.indigo.shade200),
                  ),
                  child: const Icon(Icons.close, size: 16, color: Colors.indigo),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          if (isWide)
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (phonetics.isNotEmpty)
                  Expanded(
                    child: _buildGuideCard(
                      context: context,
                      badge: '🗣️ उच्चारण (Pronunciation)',
                      text: phonetics,
                      badgeColor: Colors.amber.shade900,
                      isDevanagari: true,
                    ),
                  ),
                if (phonetics.isNotEmpty && (hindiMeaning.isNotEmpty || gujaratiMeaning.isNotEmpty))
                  const SizedBox(width: 10),
                if (hindiMeaning.isNotEmpty || gujaratiMeaning.isNotEmpty)
                  Expanded(
                    child: Column(
                      children: [
                        if (hindiMeaning.isNotEmpty)
                          _buildGuideCard(
                            context: context,
                            badge: '🇮🇳 हिंदी अर्थ',
                            text: hindiMeaning,
                            badgeColor: Colors.deepOrange.shade800,
                          ),
                        if (hindiMeaning.isNotEmpty && gujaratiMeaning.isNotEmpty)
                          const SizedBox(height: 8),
                        if (gujaratiMeaning.isNotEmpty)
                          _buildGuideCard(
                            context: context,
                            badge: '🌾 ગુજરાતી અર્થ',
                            text: gujaratiMeaning,
                            badgeColor: Colors.teal.shade800,
                          ),
                      ],
                    ),
                  ),
              ],
            )
          else
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (phonetics.isNotEmpty)
                  _buildGuideCard(
                    context: context,
                    badge: '🗣️ उच्चारण (Pronunciation)',
                    text: phonetics,
                    badgeColor: Colors.amber.shade900,
                    isDevanagari: true,
                  ),
                if (phonetics.isNotEmpty && hindiMeaning.isNotEmpty)
                  const SizedBox(height: 8),
                if (hindiMeaning.isNotEmpty)
                  _buildGuideCard(
                    context: context,
                    badge: '🇮🇳 हिंदी अर्थ',
                    text: hindiMeaning,
                    badgeColor: Colors.deepOrange.shade800,
                  ),
                if (gujaratiMeaning.isNotEmpty) ...[
                  const SizedBox(height: 8),
                  _buildGuideCard(
                    context: context,
                    badge: '🌾 ગુજરાતી અર્થ',
                    text: gujaratiMeaning,
                    badgeColor: Colors.teal.shade800,
                  ),
                ],
              ],
            ),
        ],
      ),
    );
  }

  Widget _buildGuideCard({
    required BuildContext context,
    required String badge,
    required String text,
    required Color badgeColor,
    bool isDevanagari = false,
  }) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            badge,
            style: TextStyle(
              fontSize: 11 * AppTypography.scaleFactor(context),
              fontWeight: FontWeight.bold,
              color: badgeColor,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            text,
            style: isDevanagari
                ? GoogleFonts.notoSansDevanagari(
                    fontSize: 14 * AppTypography.scaleFactor(context),
                    fontWeight: FontWeight.w600,
                    color: Colors.black87,
                    height: 1.4,
                  )
                : TextStyle(
                    fontSize: 14 * AppTypography.scaleFactor(context),
                    fontWeight: FontWeight.w500,
                    color: Colors.grey.shade900,
                    height: 1.4,
                  ),
          ),
        ],
      ),
    );
  }
}
