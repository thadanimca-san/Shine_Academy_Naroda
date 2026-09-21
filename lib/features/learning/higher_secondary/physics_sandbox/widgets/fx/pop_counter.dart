import 'package:flutter/material.dart';
import '../../theme/tokens.dart';

/// A numeric readout that eases toward new values and gives a tiny scale
/// "pop" when the value jumps — makes telemetry feel alive instead of
/// flickering text.
class PopCounter extends StatelessWidget {
  final double value;
  final String Function(double) format;
  final TextStyle? style;

  const PopCounter({
    super.key,
    required this.value,
    required this.format,
    this.style,
  });

  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: value, end: value),
      duration: Motion.fast,
      curve: Curves.easeOut,
      builder: (_, v, __) => Text(
        format(v),
        style: style ??
            Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace'),
      ),
    );
  }
}
