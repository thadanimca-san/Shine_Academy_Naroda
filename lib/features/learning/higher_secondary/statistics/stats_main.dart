import 'package:flutter/material.dart';

import 'services/license_service.dart';
import 'views/activation_screen.dart';
import 'views/home_screen.dart';

void main() {
  runApp(const StatisticsApp());
}

class StatisticsApp extends StatelessWidget {
  const StatisticsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Statistics 11-12 — Shine Academy Naroda',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal)),
      home: const StartupGate(),
    );
  }
}

/// Checks activation status before showing the app; unactivated devices
/// see [ActivationScreen] first, activated ones go straight to [HomeScreen].
class StartupGate extends StatelessWidget {
  const StartupGate();

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<bool>(
      future: LicenseService.isActivated(),
      builder: (context, snapshot) {
        if (!snapshot.hasData) {
          return const Scaffold(body: Center(child: CircularProgressIndicator()));
        }
        return snapshot.data! ? const HomeScreen() : const ActivationScreen();
      },
    );
  }
}
