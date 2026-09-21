import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class XpPopup {
  static void show(BuildContext context, {int amount = 50, required Offset position}) {
    final overlay = Overlay.of(context);
    final overlayEntry = OverlayEntry(
      builder: (context) => _FloatingXpAnimation(
        amount: amount,
        initialPosition: position,
      ),
    );

    overlay.insert(overlayEntry);

    // Remove the overlay entry after the animation completes (approx 1.5 seconds)
    Future.delayed(const Duration(milliseconds: 1500), () {
      overlayEntry.remove();
    });
  }
}

class _FloatingXpAnimation extends StatefulWidget {
  final int amount;
  final Offset initialPosition;

  const _FloatingXpAnimation({
    required this.amount,
    required this.initialPosition,
  });

  @override
  State<_FloatingXpAnimation> createState() => _FloatingXpAnimationState();
}

class _FloatingXpAnimationState extends State<_FloatingXpAnimation> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _opacityAnimation;
  late Animation<double> _translateYAnimation;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    );

    // Fade in quickly, then fade out
    _opacityAnimation = TweenSequence<double>([
      TweenSequenceItem(tween: Tween(begin: 0.0, end: 1.0).chain(CurveTween(curve: Curves.easeIn)), weight: 20),
      TweenSequenceItem(tween: Tween(begin: 1.0, end: 1.0), weight: 50),
      TweenSequenceItem(tween: Tween(begin: 1.0, end: 0.0).chain(CurveTween(curve: Curves.easeOut)), weight: 30),
    ]).animate(_controller);

    // Float upwards
    _translateYAnimation = Tween<double>(begin: 0, end: -80).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeOutCubic),
    );

    // Pop effect
    _scaleAnimation = TweenSequence<double>([
      TweenSequenceItem(tween: Tween(begin: 0.5, end: 1.2).chain(CurveTween(curve: Curves.elasticOut)), weight: 40),
      TweenSequenceItem(tween: Tween(begin: 1.2, end: 1.0).chain(CurveTween(curve: Curves.easeOut)), weight: 60),
    ]).animate(_controller);

    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Positioned(
      left: widget.initialPosition.dx - 30, // center horizontally roughly
      top: widget.initialPosition.dy - 30,  // start slightly above tap
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          return Opacity(
            opacity: _opacityAnimation.value,
            child: Transform.translate(
              offset: Offset(0, _translateYAnimation.value),
              child: Transform.scale(
                scale: _scaleAnimation.value,
                child: child,
              ),
            ),
          );
        },
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
          decoration: BoxDecoration(
            color: Colors.amber,
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: Colors.amber.withValues(alpha: 0.5),
                blurRadius: 10,
                spreadRadius: 2,
              )
            ],
            border: Border.all(color: Colors.yellowAccent.shade100, width: 2),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.star, color: Colors.white, size: 16),
              const SizedBox(width: 4),
              Text(
                '+${widget.amount} XP',
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  fontWeight: FontWeight.w900,
                  color: Colors.white,
                  shadows: [
                    Shadow(
                      color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26),
                      offset: Offset(1, 1),
                      blurRadius: 2,
                    )
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
