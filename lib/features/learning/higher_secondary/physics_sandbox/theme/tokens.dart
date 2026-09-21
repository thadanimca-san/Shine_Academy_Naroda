import 'package:flutter/material.dart';

/// Design tokens — the single source of truth for color, type, spacing,
/// radius and motion across the app. Widgets must consume these instead of
/// hardcoding Material palette values.
abstract final class Palette {
  // Brand
  static const Color primary = Color(0xFF4F46E5); // indigo 600
  static const Color primaryDeep = Color(0xFF3730A3); // indigo 800
  static const Color primarySoft = Color(0xFFEEF2FF); // indigo 50
  static const Color accent = Color(0xFFF59E0B); // amber 500
  static const Color accentSoft = Color(0xFFFEF3C7);

  // Canvas (simulation stage)
  static const Color stage = Color(0xFF10122B); // deep space
  static const Color stageLine = Color(0x33FFFFFF);

  // Neutrals
  static const Color bg = Color(0xFFF7F7FB);
  static const Color surface = Colors.white;
  static const Color surfaceAlt = Color(0xFFF1F2F8);
  static const Color border = Color(0xFFE5E7F0);
  static const Color textStrong = Color(0xFF15172B);
  static const Color textBody = Color(0xFF3F4254);
  static const Color textMuted = Color(0xFF757A93);
  static const Color textFaint = Color(0xFFA5A9BF);

  // Semantic
  static const Color success = Color(0xFF16A34A);
  static const Color successSoft = Color(0xFFECFDF3);
  static const Color danger = Color(0xFFDC2626);
  static const Color dangerSoft = Color(0xFFFEF2F2);
  static const Color info = Color(0xFF0284C7);
  static const Color infoSoft = Color(0xFFEFF8FF);

  // Exam tracks
  static const Color neet = Color(0xFF059669);
  static const Color jee = Color(0xFFEA580C);

  // Chapter accents — lesson top-nav colors (dark enough for white text)
  static const Color chMechanics = Color(0xFF3730A3); // indigo 800
  static const Color chWaves = Color(0xFF0E7490); // cyan 700
  static const Color chThermal = Color(0xFFB45309); // amber 700
  static const Color chElectroMag = Color(0xFF6D28D9); // violet 700
  static const Color chOptics = Color(0xFF0F766E); // teal 700
  static const Color chModern = Color(0xFFBE185D); // pink 700
}

abstract final class Gap {
  static const double x1 = 4;
  static const double x2 = 8;
  static const double x3 = 12;
  static const double x4 = 16;
  static const double x5 = 20;
  static const double x6 = 24;
  static const double x8 = 32;
  static const double x10 = 40;
}

abstract final class Corner {
  static const double sm = 8;
  static const double md = 12;
  static const double lg = 16;
  static const double xl = 24;
  static const double pill = 999;
}

abstract final class Motion {
  static const Duration fast = Duration(milliseconds: 160);
  static const Duration base = Duration(milliseconds: 240);
  static const Duration slow = Duration(milliseconds: 400);
  static const Curve ease = Curves.easeOutCubic;
  static const Curve spring = Curves.easeOutBack;
}

abstract final class Type {
  static const TextStyle display = TextStyle(
      fontSize: 26, fontWeight: FontWeight.w800, color: Palette.textStrong, height: 1.2, letterSpacing: -0.5);
  static const TextStyle title = TextStyle(
      fontSize: 19, fontWeight: FontWeight.w700, color: Palette.textStrong, height: 1.25, letterSpacing: -0.3);
  static const TextStyle heading = TextStyle(
      fontSize: 16, fontWeight: FontWeight.w700, color: Palette.textStrong, height: 1.3);
  static const TextStyle body = TextStyle(
      fontSize: 14.5, fontWeight: FontWeight.w400, color: Palette.textBody, height: 1.55);
  static const TextStyle bodyStrong = TextStyle(
      fontSize: 14.5, fontWeight: FontWeight.w600, color: Palette.textStrong, height: 1.55);
  static const TextStyle caption = TextStyle(
      fontSize: 12.5, fontWeight: FontWeight.w500, color: Palette.textMuted, height: 1.4);
  static const TextStyle label = TextStyle(
      fontSize: 11, fontWeight: FontWeight.w700, color: Palette.textMuted, letterSpacing: 0.6);
  static const TextStyle mono = TextStyle(
      fontSize: 13.5, fontFamily: 'monospace', color: Palette.textStrong, height: 1.5);
}
