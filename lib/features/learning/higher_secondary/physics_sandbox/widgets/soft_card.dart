import 'package:flutter/material.dart';
import '../theme/tokens.dart';

/// Base surface for the app's card language: soft border, gentle shadow,
/// press-scale micro-interaction when tappable.
class SoftCard extends StatefulWidget {
  final Widget child;
  final VoidCallback? onTap;
  final EdgeInsetsGeometry padding;
  final Color color;
  final double radius;

  const SoftCard({
    super.key,
    required this.child,
    this.onTap,
    this.padding = const EdgeInsets.all(Gap.x4),
    this.color = Palette.surface,
    this.radius = Corner.lg,
  });

  @override
  State<SoftCard> createState() => _SoftCardState();
}

class _SoftCardState extends State<SoftCard> {
  bool _pressed = false;

  @override
  Widget build(BuildContext context) {
    final card = AnimatedScale(
      scale: _pressed ? 0.98 : 1.0,
      duration: Motion.fast,
      curve: Motion.ease,
      child: Container(
        decoration: BoxDecoration(
          color: widget.color,
          borderRadius: BorderRadius.circular(widget.radius),
          border: Border.all(color: Palette.border),
          boxShadow: [
            BoxShadow(
              color: const Color(0xFF15172B).withValues(alpha: 0.04),
              blurRadius: 12,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Material(
          type: MaterialType.transparency,
          child: InkWell(
            borderRadius: BorderRadius.circular(widget.radius),
            onTap: widget.onTap,
            onHighlightChanged: widget.onTap == null
                ? null
                : (v) => setState(() => _pressed = v),
            child: Padding(padding: widget.padding, child: widget.child),
          ),
        ),
      ),
    );
    return card;
  }
}
