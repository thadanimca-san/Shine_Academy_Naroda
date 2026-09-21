import 'package:flutter/material.dart';

class AppTheme {
  // Deep indigo as the primary brand color for Shine Platform
  static const Color primaryColor = Colors.indigo;
  
  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      colorSchemeSeed: primaryColor,
      brightness: Brightness.light,
      appBarTheme: const AppBarTheme(
        centerTitle: true,
        elevation: 0,
      ),
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      colorSchemeSeed: primaryColor,
      brightness: Brightness.dark,
      appBarTheme: const AppBarTheme(
        centerTitle: true,
        elevation: 0,
      ),
    );
  }
}
