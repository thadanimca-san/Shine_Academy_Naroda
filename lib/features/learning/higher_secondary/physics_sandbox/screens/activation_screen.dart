import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../services/license_service.dart';
import 'splash_screen.dart'; // Or your home screen
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class ActivationScreen extends StatefulWidget {
  const ActivationScreen({super.key, this.onActivated});

  final VoidCallback? onActivated;

  @override
  State<ActivationScreen> createState() => _ActivationScreenState();
}

class _ActivationScreenState extends State<ActivationScreen> {
  final TextEditingController _codeController = TextEditingController();
  bool _isLoading = false;
  String? _errorMessage;

  void _verifyCode() async {
    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    final success = await LicenseService.instance.validateAndActivate(_codeController.text);

    setState(() {
      _isLoading = false;
    });

    if (success) {
      if (!mounted) return;
      if (widget.onActivated != null) {
        widget.onActivated!();
      } else {
        Navigator.of(context).pushReplacement(
          MaterialPageRoute(builder: (_) => const SplashScreen()),
        );
      }
    } else {
      setState(() {
        _errorMessage = 'Invalid activation code. Please check with support.';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final deviceId = LicenseService.instance.deviceId;

    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('App Activation'))),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(TrilingualService.instance.getUIText('Activation Required'),
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 12),
            Text(TrilingualService.instance.getUIText('To use Physics Lab, please share your Device Code with GovindSir of Shine Academy Naroda to receive your unlock code.\n\nफिजिक्स लैब का उपयोग करने के लिए, अपना अनलॉक कोड प्राप्त करने के लिए कृपया अपना डिवाइस कोड शाइन एकेडमी नरोदा के गोविंद सर को दें।'),
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.grey),
            ),
            const SizedBox(height: 32),
            Text(TrilingualService.instance.getUIText('Your Device Code:'), style: TextStyle(fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.grey.shade200,
                borderRadius: BorderRadius.circular(8),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(deviceId, style: TextStyle(fontWeight: FontWeight.bold, letterSpacing: 1.5)),
                  IconButton(
                    icon: Icon(Icons.copy),
                    onPressed: () {
                      Clipboard.setData(ClipboardData(text: deviceId));
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text(TrilingualService.instance.getUIText('Device code copied!'))),
                      );
                    },
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),
            TextField(
              controller: _codeController,
              decoration: InputDecoration(
                labelText: 'Enter Activation Code',
                border: const OutlineInputBorder(),
                errorText: _errorMessage,
              ),
            ),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: _isLoading ? null : _verifyCode,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
              ),
              child: _isLoading 
                ? const CircularProgressIndicator(color: Colors.white)
                : Text(TrilingualService.instance.getUIText('Activate App'), style: TextStyle(fontSize: 16)),
            ),
          ],
        ),
      ),
    );
  }
}