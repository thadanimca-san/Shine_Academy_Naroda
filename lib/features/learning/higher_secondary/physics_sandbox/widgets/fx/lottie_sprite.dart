import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

/// Physics-object sprites: Lottie actors driven by simulation state.
///
/// The pattern for premium sim visuals — the CustomPainter keeps drawing
/// physics geometry (fields, rays, trajectories) while the recognizable
/// OBJECTS (electrons, lenses, cars…) are Lottie sprites overlaid at
/// world positions via [SpriteStage].
class LottieSprite extends StatefulWidget {
  final String asset;
  final double size;

  /// Playback speed multiplier — tie to simulation state (e.g. cart speed).
  final double speed;

  /// Fallback if the asset fails to load; the sim never breaks.
  final Widget? fallback;

  const LottieSprite(
    this.asset, {
    super.key,
    required this.size,
    this.speed = 1.0,
    this.fallback,
  });

  @override
  State<LottieSprite> createState() => _LottieSpriteState();
}

class _LottieSpriteState extends State<LottieSprite>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(vsync: this);

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: widget.size,
      height: widget.size,
      child: Lottie.asset(
        widget.asset,
        controller: _c,
        fit: BoxFit.contain,
        onLoaded: (comp) {
          _c.duration = comp.duration * (1 / widget.speed.clamp(0.05, 20));
          _c.repeat();
        },
        errorBuilder: (_, __, ___) =>
            widget.fallback ?? const SizedBox.shrink(),
      ),
    );
  }

  @override
  void didUpdateWidget(covariant LottieSprite old) {
    super.didUpdateWidget(old);
    if (old.speed != widget.speed && _c.duration != null) {
      final base = _c.duration! * old.speed.clamp(0.05, 20);
      _c.duration = base * (1 / widget.speed.clamp(0.05, 20));
      if (_c.isAnimating) _c.repeat();
    }
  }
}

/// One positioned actor on a [SpriteStage]. [anchor] is in fractional stage
/// coordinates (0..1 × 0..1) so sprites track the painter's world transform.
class SpriteActor {
  final Offset anchor;
  final Widget sprite;
  const SpriteActor({required this.anchor, required this.sprite});
}

/// Stacks Lottie actors over a painted stage. The painter draws the physics;
/// the actors make it beautiful.
class SpriteStage extends StatelessWidget {
  final Widget stage; // usually a CustomPaint
  final List<SpriteActor> actors;
  const SpriteStage({super.key, required this.stage, required this.actors});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, c) => Stack(
        children: [
          Positioned.fill(child: stage),
          for (final a in actors)
            Positioned(
              left: a.anchor.dx * c.maxWidth,
              top: a.anchor.dy * c.maxHeight,
              child: FractionalTranslation(
                translation: const Offset(-0.5, -0.5),
                child: IgnorePointer(child: a.sprite),
              ),
            ),
        ],
      ),
    );
  }
}
