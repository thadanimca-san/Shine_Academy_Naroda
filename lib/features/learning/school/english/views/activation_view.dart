import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../services/license_service.dart';
import '../theme/app_theme.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Shown once, before the first-run student can reach the app content.
/// Displays this device's unique code for the student to send to Shine
/// Academy Naroda, and lets them enter the matching unlock code sent back.
class ActivationView extends StatefulWidget {
  final VoidCallback onActivated;

  const ActivationView({super.key, required this.onActivated});

  @override
  State<ActivationView> createState() => _ActivationViewState();
}

class _ActivationViewState extends State<ActivationView> {
  String? _deviceId;
  final _codeController = TextEditingController();
  String? _error;
  bool _checking = false;

  @override
  void initState() {
    super.initState();
    LicenseService.getDeviceId().then((id) => setState(() => _deviceId = id));
  }

  @override
  void dispose() {
    _codeController.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    setState(() {
      _checking = true;
      _error = null;
    });
    final ok = await LicenseService.tryActivate(_codeController.text);
    if (!mounted) return;
    setState(() => _checking = false);
    if (ok) {
      widget.onActivated();
    } else {
      setState(() => _error = 'That code did not match this device. Please check it and try again.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.tealDeep,
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 460),
              child: Card(
                elevation: 6,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Icon(Icons.lock_outline, size: 48, color: AppColors.tealDeep),
                      const SizedBox(height: 12),
                      Text(TrilingualService.instance.getUIText('Activate Your App'),
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: AppColors.tealDeep),
                      ),
                      const SizedBox(height: 8),
                      Text(TrilingualService.instance.getUIText('This app is for enrolled Shine Academy Naroda students only. Send the device code below to your teacher on WhatsApp — they will reply with your unlock code.'),
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 13.5, color: AppColors.inkFaint),
                      ),
                      const SizedBox(height: 20),
                      Text(TrilingualService.instance.getUIText('Your Device Code'), style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.inkFaint)),
                      const SizedBox(height: 6),
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 12),
                        decoration: BoxDecoration(
                          color: AppColors.saffronTint,
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(color: AppColors.saffron),
                        ),
                        child: Row(
                          children: [
                            Expanded(
                              child: Text(
                                _deviceId ?? 'Generating…',
                                textAlign: TextAlign.center,
                                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, letterSpacing: 1.2, fontFamily: 'monospace'),
                              ),
                            ),
                            IconButton(
                              icon: Icon(Icons.copy, color: AppColors.saffronDeep),
                              tooltip: 'Copy device code',
                              onPressed: _deviceId == null
                                  ? null
                                  : () {
                                      Clipboard.setData(ClipboardData(text: _deviceId!));
                                      ScaffoldMessenger.of(context).showSnackBar(
                                        SnackBar(content: Text(TrilingualService.instance.getUIText('Device code copied.'))),
                                      );
                                    },
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 20),
                      Text(TrilingualService.instance.getUIText('Enter Your Unlock Code'), style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.inkFaint)),
                      const SizedBox(height: 6),
                      TextField(
                        controller: _codeController,
                        textAlign: TextAlign.center,
                        textCapitalization: TextCapitalization.characters,
                        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, letterSpacing: 1.2),
                        decoration: InputDecoration(
                          hintText: 'e.g. 4F82A9C1',
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(10)),
                        ),
                      ),
                      if (_error != null) ...[
                        const SizedBox(height: 10),
                        Text(_error!, style: TextStyle(color: AppColors.critical, fontSize: 12.5)),
                      ],
                      const SizedBox(height: 18),
                      ElevatedButton(
                        onPressed: _checking ? null : _submit,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: AppColors.tealDeep,
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(vertical: 14),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                        ),
                        child: _checking
                            ? const SizedBox(height: 20, width: 20, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white))
                            : Text(TrilingualService.instance.getUIText('Activate'), style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold)),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
