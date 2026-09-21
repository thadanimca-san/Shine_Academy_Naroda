import 'package:flutter/material.dart';

class AppColors {
  // Primary Brand Colors
  static const Color primary = Color(0xFF3F51B5); // Indigo
  static const Color primaryLight = Color(0xFF757DE8);
  static const Color primaryDark = Color(0xFF002984);
  static const Color accent = Color(0xFF009688); // Teal
  
  // Backgrounds
  static const Color background = Color(0xFFF5F7FA);
  static const Color surface = Colors.white;
  static const Color cardShadow = Color(0x1F000000);

  // Typography Colors
  static const Color textPrimary = Color(0xFF2C3E50);
  static const Color textSecondary = Color(0xFF7F8C8D);

  // Module Specific Colors
  static const Color mathColor = Color(0xFF3498DB);
  static const Color englishColor = Color(0xFFE91E63);
  static const Color scienceColor = Color(0xFFFF9800);
  static const Color commerceColor = Color(0xFF00BCD4);
  static const Color physicsColor = Color(0xFF9C27B0);
  
  static const LinearGradient primaryGradient = LinearGradient(
    colors: [Color(0xFF3F51B5), Color(0xFF757DE8)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );
}
