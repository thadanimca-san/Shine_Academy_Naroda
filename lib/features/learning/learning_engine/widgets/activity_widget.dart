import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ActivityWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const ActivityWidget({super.key, required this.data});

  @override
  State<ActivityWidget> createState() => _ActivityWidgetState();
}

class _ActivityWidgetState extends State<ActivityWidget> {
  bool _showBack = false;

  @override
  Widget build(BuildContext context) {
    final lang = 'en';
    final interactionType = widget.data['interaction_type'] ?? 'flashcard';
    final frontMap = widget.data['front'] as Map<String, dynamic>? ?? {};
    final frontText = frontMap[lang] ?? frontMap['en'] ?? '';
    final backMap = widget.data['back'] as Map<String, dynamic>? ?? {};
    final backText = backMap[lang] ?? backMap['en'] ?? '';

    if (interactionType != 'flashcard') {
      return const SizedBox(); // Only flashcard supported in PoC
    }

    return GestureDetector(
      onTap: () {
        setState(() {
          _showBack = !_showBack;
        });
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 24),
        height: 200,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: _showBack ? [Colors.purple[400]!, Colors.purple[600]!] : [Colors.indigo[400]!, Colors.indigo[600]!],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: (_showBack ? Colors.purple : Colors.indigo).withValues(alpha: 0.3),
              blurRadius: 20,
              offset: const Offset(0, 10),
            )
          ],
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(_showBack ? Icons.check_circle_outline : Icons.touch_app, color: Colors.white70, size: 40),
              const SizedBox(height: 16),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                child: Text(
                  _showBack ? backText : frontText,
                  textAlign: TextAlign.center,
                  style: GoogleFonts.poppins(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Text(TrilingualService.instance.getUIText("Tap to flip"),
                style: GoogleFonts.inter(fontSize: 12, color: Colors.white54),
              )
            ],
          ),
        ),
      ),
    );
  }
}
