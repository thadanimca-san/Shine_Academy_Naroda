import 'package:flutter/material.dart';

import 'screens/home_screen.dart';
import 'theme/app_theme.dart';

void main() {
  runApp(const Maths3to6App());
}

class Maths3to6App extends StatelessWidget {
  const Maths3to6App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'maths3to6',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light,
      home: const HomeScreen(),
    );
  }
}

class AppGate extends StatelessWidget {
  const AppGate({super.key});

  @override
  Widget build(BuildContext context) {
    return const HomeScreen();
  }
}
