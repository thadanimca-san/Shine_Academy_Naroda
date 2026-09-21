import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
import 'services/license_service.dart';
import 'theme/app_theme.dart';
import 'views/activation_view.dart';

void main() {
  runApp(const EnglishSimulationApp());
}

class EnglishSimulationApp extends StatelessWidget {
  const EnglishSimulationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'english7to10',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light,
      // Wraps every screen so content never sits under the phone's bottom
      // system bar (Android gesture bar / iOS home indicator).
      builder: (context, child) => SafeArea(bottom: true, child: child!),
      home: const AppGate(),
    );
  }
}

/// Shows the one-time [ActivationView] until this device has been
/// unlocked, then hands off to the normal app content.
class AppGate extends StatefulWidget {
  final int? preSelectedGrade;
  const AppGate({super.key, this.preSelectedGrade});

  @override
  State<AppGate> createState() => _AppGateState();
}

class _AppGateState extends State<AppGate> {
  bool? _activated;

  @override
  void initState() {
    super.initState();
    LicenseService.isActivated().then((v) => setState(() => _activated = v));
  }

  @override
  Widget build(BuildContext context) {
    if (_activated == null) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }
    if (_activated == false) {
      return ActivationView(onActivated: () => setState(() => _activated = true));
    }
    return HomeScreen(preSelectedGrade: widget.preSelectedGrade);
  }
}
