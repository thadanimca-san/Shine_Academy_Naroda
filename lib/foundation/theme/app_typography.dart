import 'package:flutter/material.dart';

import 'dart:math' as math;

class AppTypography {
  // We assume a standard mobile logical width is around 400 pixels.
  static const double _baseMobileWidth = 400.0;

  /// Calculates a continuous, mathematically smooth responsive multiplier 
  /// based on the device's screen width.
  static double scaleFactor(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    
    // If the device is smaller than or equal to a standard mobile phone, use 1x scale.
    if (screenWidth <= _baseMobileWidth) {
      return 1.0;
    }
    
    // Mathematical scaling logic:
    // Instead of fixed "jumps" (which cause jarring changes between devices),
    // we scale smoothly. For every 100% increase in screen width beyond mobile,
    // we increase the font size by 40%.
    // Example: 
    // - Mobile (400px) -> 1.0x
    // - Tablet (800px) -> 1.4x
    // - Laptop (1200px) -> 1.8x
    // - Digital Panel (1920px) -> 2.52x
    // - 4K Panel (3840px) -> 4.44x
    
    double extraWidth = screenWidth - _baseMobileWidth;
    double scale = 1.0 + (extraWidth / _baseMobileWidth) * 0.40;
    
    // Clamp to a reasonable maximum to ensure layout doesn't break on extreme edge cases
    return math.min(scale, 5.0);
  }

  // Define base font sizes
  static const double _baseBody = 16.0;
  static const double _baseBodySmall = 14.0;
  static const double _baseH1 = 32.0;
  static const double _baseH2 = 28.0;
  static const double _baseH3 = 24.0;
  static const double _baseH4 = 20.0;
  
  // Expose scalable TextStyles
  static TextStyle body(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseBody * scaleFactor(context),
      color: color ?? Colors.black87,
      fontWeight: fontWeight ?? FontWeight.normal,
      height: 1.5, // Good readability
    );
  }

  static TextStyle bodySmall(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseBodySmall * scaleFactor(context),
      color: color ?? Colors.black54,
      fontWeight: fontWeight ?? FontWeight.normal,
      height: 1.4,
    );
  }

  static TextStyle h1(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseH1 * scaleFactor(context),
      color: color ?? Colors.black,
      fontWeight: fontWeight ?? FontWeight.bold,
      height: 1.2,
    );
  }

  static TextStyle h2(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseH2 * scaleFactor(context),
      color: color ?? Colors.black,
      fontWeight: fontWeight ?? FontWeight.bold,
      height: 1.2,
    );
  }

  static TextStyle h3(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseH3 * scaleFactor(context),
      color: color ?? Colors.black87,
      fontWeight: fontWeight ?? FontWeight.w600,
      height: 1.3,
    );
  }

  static TextStyle h4(BuildContext context, {Color? color, FontWeight? fontWeight}) {
    return TextStyle(
      fontSize: _baseH4 * scaleFactor(context),
      color: color ?? Colors.black87,
      fontWeight: fontWeight ?? FontWeight.w600,
      height: 1.3,
    );
  }
}
