import 'package:flutter/material.dart';

/// Shared visual identity for english7to10: a warm, textbook-like palette
/// (saffron for student surfaces, teal for teacher surfaces) rather than a
/// generic Material purple, matching the product blueprint.
class AppColors {
  AppColors._();

  static const paper = Color(0xFFFBF8F2);
  static const paperRaised = Color(0xFFF3EEE2);
  static const ink = Color(0xFF22201B);
  static const inkSoft = Color(0xFF56503F);
  static const inkFaint = Color(0xFF8A8271);
  static const rule = Color(0xFFDDD4BF);

  static const saffron = Color(0xFFC4622D);
  static const saffronDeep = Color(0xFF9C4A1F);
  static const saffronTint = Color(0xFFF4E3D5);

  static const teal = Color(0xFF1F5E52);
  static const tealDeep = Color(0xFF163F38);
  static const tealTint = Color(0xFFDFEAE6);

  static const success = Color(0xFF2F7A4F);
  static const warning = Color(0xFFB8862E);
  static const critical = Color(0xFFB33F3F);
}

class AppTheme {
  AppTheme._();

  static ThemeData light = ThemeData(
    useMaterial3: true,
    scaffoldBackgroundColor: AppColors.paper,
    colorScheme: const ColorScheme.light(
      primary: AppColors.saffron,
      onPrimary: Colors.white,
      secondary: AppColors.teal,
      onSecondary: Colors.white,
      surface: AppColors.paperRaised,
      onSurface: AppColors.ink,
      error: AppColors.critical,
    ),
    appBarTheme: const AppBarTheme(
      backgroundColor: AppColors.paper,
      foregroundColor: AppColors.ink,
      elevation: 0,
      centerTitle: false,
    ),
    cardTheme: CardThemeData(
      color: AppColors.paperRaised,
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
        side: const BorderSide(color: AppColors.rule),
      ),
    ),
    textTheme: const TextTheme(
      headlineMedium: TextStyle(fontWeight: FontWeight.w800, color: AppColors.ink),
      titleLarge: TextStyle(fontWeight: FontWeight.w700, color: AppColors.ink),
      titleMedium: TextStyle(fontWeight: FontWeight.w600, color: AppColors.ink),
      bodyMedium: TextStyle(color: AppColors.inkSoft),
    ),
  );
}
