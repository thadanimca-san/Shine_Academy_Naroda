import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'screens/activation_screen.dart';
import 'screens/splash_screen.dart';
import 'services/license_service.dart';
import 'services/profile_service.dart';
import 'services/progress_service.dart';
import 'theme/app_theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setEnabledSystemUIMode(SystemUiMode.edgeToEdge);
  
  await ProgressService.instance.init();
  await ProfileService.instance.init();
  await LicenseService.instance.init();

  runApp(const PhysicsSandboxApp());
}

class PhysicsSandboxApp extends StatelessWidget {
  const PhysicsSandboxApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Physics Sandbox',
      theme: AppTheme.light(),
      home: const AppGate(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class AppGate extends StatefulWidget {
  const AppGate({super.key});

  @override
  State<AppGate> createState() => _AppGateState();
}

class _AppGateState extends State<AppGate> {
  bool? _activated;

  @override
  void initState() {
    super.initState(); // Fixed: changed from super.init() to super.initState()
    _checkActivation();
  }

  Future<void> _checkActivation() async {
    bool active = LicenseService.instance.isActivated;
    setState(() => _activated = active);
  }

  @override
  Widget build(BuildContext context) {
    if (_activated == null) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }
    if (_activated == false) {
      return ActivationScreen(
        onActivated: () => setState(() => _activated = true),
      );
    }
    return const SplashScreen();
  }
}