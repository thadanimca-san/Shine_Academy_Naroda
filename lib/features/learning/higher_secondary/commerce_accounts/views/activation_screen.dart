import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';

import '../data/branding.dart';
import '../services/license_service.dart';
import '../widgets/branding_header_widget.dart';
import 'home_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// First screen shown on an unactivated device: displays this install's
/// unique device code (to be sent to the academy for unlocking) and lets
/// the student/teacher enter the unlock code they receive back.
class ActivationScreen extends StatefulWidget {
  const ActivationScreen({super.key});

  @override
  State<ActivationScreen> createState() => _ActivationScreenState();
}

class _ActivationScreenState extends State<ActivationScreen> {
  String? _deviceId;
  final _codeController = TextEditingController();
  String? _error;
  bool _checking = false;

  @override
  void initState() {
    super.initState();
    _loadDeviceId();
  }

  @override
  void dispose() {
    _codeController.dispose();
    super.dispose();
  }

  Future<void> _loadDeviceId() async {
    final id = await LicenseService.getDeviceId();
    setState(() => _deviceId = id);
  }

  Future<void> _activate() async {
    if (_codeController.text.trim().isEmpty) {
      setState(() => _error = 'Please enter the Unlock Code you received.');
      return;
    }
    setState(() {
      _checking = true;
      _error = null;
    });
    final success = await LicenseService.tryActivate(_codeController.text);
    if (!mounted) return;
    setState(() => _checking = false);
    if (success) {
      Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const HomeScreen()));
    } else {
      setState(() => _error = 'Incorrect code. Please check and try again.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Activate App'))),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const BrandingHeaderWidget(),
            const SizedBox(height: 20),
            Text(TrilingualService.instance.getUIText('This app is locked to your device. To activate it:'),
                style: TextStyle(fontSize: 15)),
            const SizedBox(height: 12),
            Text('1. Send the Device Code below to your teacher / ${Branding.academyName}.'),
            const SizedBox(height: 8),
            Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: Colors.indigo.withValues(alpha: 0.08),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Row(
                children: [
                  Expanded(
                    child: SelectableText(
                      _deviceId ?? 'Loading...',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, letterSpacing: 1.2),
                    ),
                  ),
                  IconButton(
                    icon: Icon(Icons.copy),
                    onPressed: _deviceId == null
                        ? null
                        : () async {
                            await Clipboard.setData(ClipboardData(text: _deviceId!));
                            if (context.mounted) {
                              ScaffoldMessenger.of(context)
                                  .showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Device code copied'))));
                            }
                          },
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),
            Text(TrilingualService.instance.getUIText('2. Enter the Unlock Code you receive back:')),
            const SizedBox(height: 8),
            TextField(
              controller: _codeController,
              decoration: InputDecoration(
                labelText: 'Unlock Code',
                border: const OutlineInputBorder(),
                errorText: _error,
              ),
              textCapitalization: TextCapitalization.characters,
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _checking ? null : _activate,
              child: _checking ? const CircularProgressIndicator() : Text(TrilingualService.instance.getUIText('Activate')),
            ),
            const SizedBox(height: 20),
            Center(
              child: TextButton.icon(
                onPressed: () => launchUrl(Uri.parse(Branding.websiteUrl), mode: LaunchMode.externalApplication),
                icon: Icon(Icons.language, size: 18),
                label: Text('Visit ${Branding.academyName}'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
