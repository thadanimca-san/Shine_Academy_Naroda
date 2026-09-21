import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../theme/tokens.dart';

/// Duolingo-style 2.5D button: a raised face sitting on a darker edge.
/// Pressing sinks the face onto the edge with a light haptic — the button
/// physically "gives" under your finger.
class BevelButton extends StatefulWidget {
  final String label;
  final IconData? icon;
  final VoidCallback? onPressed;
  final Color color;
  final Color? textColor;
  final bool expanded;
  final EdgeInsetsGeometry padding;

  const BevelButton({
    super.key,
    required this.label,
    this.icon,
    required this.onPressed,
    this.color = Palette.primary,
    this.textColor,
    this.expanded = true,
    this.padding = const EdgeInsets.symmetric(vertical: 14, horizontal: Gap.x5),
  });

  /// Green "go" variant.
  const BevelButton.go({
    super.key,
    required this.label,
    this.icon,
    required this.onPressed,
    this.expanded = true,
    this.padding = const EdgeInsets.symmetric(vertical: 14, horizontal: Gap.x5),
  })  : color = Palette.success,
        textColor = null;

  /// Quiet neutral variant (light face, dark text).
  const BevelButton.quiet({
    super.key,
    required this.label,
    this.icon,
    required this.onPressed,
    this.expanded = true,
    this.padding = const EdgeInsets.symmetric(vertical: 14, horizontal: Gap.x5),
  })  : color = Palette.surface,
        textColor = Palette.textStrong;

  @override
  State<BevelButton> createState() => _BevelButtonState();
}

class _BevelButtonState extends State<BevelButton> {
  static const double _depth = 4;
  bool _down = false;

  bool get _enabled => widget.onPressed != null;

  Color get _face {
    if (!_enabled) return Palette.surfaceAlt;
    return widget.color;
  }

  Color get _edge {
    if (!_enabled) return Palette.border;
    final hsl = HSLColor.fromColor(widget.color);
    return hsl
        .withLightness((hsl.lightness - 0.14).clamp(0.0, 1.0))
        .withSaturation((hsl.saturation * 1.05).clamp(0.0, 1.0))
        .toColor();
  }

  Color get _label {
    if (!_enabled) return Palette.textFaint;
    return widget.textColor ??
        (ThemeData.estimateBrightnessForColor(widget.color) == Brightness.dark
            ? Colors.white
            : Palette.textStrong);
  }

  void _set(bool down) {
    if (!_enabled || _down == down) return;
    setState(() => _down = down);
    if (down) HapticFeedback.lightImpact();
  }

  @override
  Widget build(BuildContext context) {
    final needsBorder = widget.color == Palette.surface;
    final content = Row(
      mainAxisSize: widget.expanded ? MainAxisSize.max : MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        if (widget.icon != null) ...[
          Icon(widget.icon, size: 18, color: _label),
          const SizedBox(width: Gap.x2),
        ],
        Text(
          widget.label,
          style: Type.bodyStrong.copyWith(
            color: _label,
            fontSize: 15,
            letterSpacing: 0.2,
          ),
        ),
      ],
    );

    return Semantics(
      button: true,
      enabled: _enabled,
      label: widget.label,
      child: GestureDetector(
        onTapDown: (_) => _set(true),
        onTapUp: (_) {
          _set(false);
          widget.onPressed?.call();
        },
        onTapCancel: () => _set(false),
        child: Stack(
          children: [
            // Edge (the "ground" the face sinks into)
            Positioned.fill(
              top: _depth,
              child: Container(
                decoration: BoxDecoration(
                  color: needsBorder ? Palette.border : _edge,
                  borderRadius: BorderRadius.circular(Corner.lg),
                ),
              ),
            ),
            // Face
            AnimatedContainer(
              duration: const Duration(milliseconds: 70),
              curve: Curves.easeOut,
              margin: EdgeInsets.only(
                  top: _down ? _depth : 0, bottom: _down ? 0 : _depth),
              padding: widget.padding,
              decoration: BoxDecoration(
                color: _face,
                borderRadius: BorderRadius.circular(Corner.lg),
                border: needsBorder ? Border.all(color: Palette.border) : null,
              ),
              child: content,
            ),
          ],
        ),
      ),
    );
  }
}
