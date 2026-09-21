import 'package:flutter/material.dart';

class PresentationService {
  static final ValueNotifier<bool> isPresentationMode = ValueNotifier<bool>(false);

  /// Screen widths above this value are treated as digital panels / IFPs.
  static const double _panelThreshold = 900.0;

  /// Call this once after the first frame is rendered (inside addPostFrameCallback).
  /// It reads the actual screen width and enables Presentation Mode automatically
  /// if the device looks like an Android Digital Panel (width >= 900px).
  /// On a regular phone (small screen), it leaves Presentation Mode OFF.
  static void autoDetect(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final shouldBeOn = width >= _panelThreshold;
    if (isPresentationMode.value != shouldBeOn) {
      isPresentationMode.value = shouldBeOn;
    }
  }

  static void toggle() {
    isPresentationMode.value = !isPresentationMode.value;
  }

  /// Calculates the dynamic text scale factor based on screen width and the manual toggle
  static double getScaleFactor(BuildContext context) {
    double scale = 1.0;
    final width = MediaQuery.of(context).size.width;

    if (width > 1200) {
      scale = 1.6; // Interactive Flat Panel / Large Desktop
    } else if (width > 800) {
      scale = 1.2; // Tablet / Small Desktop
    }

    if (isPresentationMode.value) {
      scale *= 1.125; // Force multiplier for Presentation Mode (25% smaller than original 1.5×)
    }

    // Cap the maximum scale so UI doesn't completely break
    if (scale > 3.0) scale = 3.0;

    return scale;
  }
}
