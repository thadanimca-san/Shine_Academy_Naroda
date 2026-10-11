import 'dart:math' as math;

import 'package:flutter/material.dart';

/// Like [AspectRatio], but never taller than [maxScreenFraction] of the screen.
///
/// On a phone (portrait) the child fills the width as usual. On a wide classroom
/// panel (landscape) full width would make the child taller than the screen, so
/// it is shrunk and centred until the whole figure fits in one view.
class BoundedAspectRatio extends StatelessWidget {
  const BoundedAspectRatio({
    super.key,
    required this.aspectRatio,
    required this.child,
    this.maxScreenFraction = 0.55,
  });

  final double aspectRatio;
  final double maxScreenFraction;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    final maxHeight = MediaQuery.sizeOf(context).height * maxScreenFraction;
    return LayoutBuilder(
      builder: (context, constraints) {
        final width = math.min(constraints.maxWidth, maxHeight * aspectRatio);
        return Center(
          child: SizedBox(
            width: width,
            child: AspectRatio(aspectRatio: aspectRatio, child: child),
          ),
        );
      },
    );
  }
}
