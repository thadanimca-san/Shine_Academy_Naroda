import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class FlashcardWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const FlashcardWidget({super.key, required this.data});

  @override
  State<FlashcardWidget> createState() => _FlashcardWidgetState();
}

class _FlashcardWidgetState extends State<FlashcardWidget> {
  bool _isFlipped = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() {
          _isFlipped = !_isFlipped;
        });
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 300),
        margin: const EdgeInsets.only(bottom: 20),
        padding: const EdgeInsets.all(24),
        decoration: BoxDecoration(
          color: _isFlipped ? Colors.indigo[50] : Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.indigo, width: 2),
          boxShadow: [
            BoxShadow(
              color: Colors.indigo.withValues(alpha: 0.1),
              blurRadius: 10,
              offset: const Offset(0, 4),
            )
          ],
        ),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(Icons.flip, color: Colors.indigo[300]),
                Text(
                  _isFlipped ? "ANSWER" : "FLASHCARD",
                  style: GoogleFonts.inter(
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 1.5,
                    color: Colors.indigo[300],
                  ),
                ),
                Icon(Icons.touch_app, color: Colors.indigo[300], size: 16),
              ],
            ),
            const SizedBox(height: 20),
            Text(
              _isFlipped 
                  ? (widget.data['back'] ?? widget.data['definition'] ?? '') 
                  : (widget.data['front'] ?? widget.data['term'] ?? ''),
              textAlign: TextAlign.center,
              style: GoogleFonts.poppins(
                fontSize: 18,
                fontWeight: _isFlipped ? FontWeight.normal : FontWeight.bold,
                color: Theme.of(context).colorScheme.onSurface,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
