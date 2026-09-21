import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import '../learning/school/english/services/speech_service.dart';
import '../../../core/services/tts_service.dart';
import '../../../core/services/tts_platform_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class EduOSDoctorScreen extends StatefulWidget {
  const EduOSDoctorScreen({super.key});

  @override
  State<EduOSDoctorScreen> createState() => _EduOSDoctorScreenState();
}

class _EduOSDoctorScreenState extends State<EduOSDoctorScreen>
    with SingleTickerProviderStateMixin {
  Map<String, dynamic>? _report;
  bool _isLoading = true;
  late TabController _tabController;

  // TTS Diagnostic state
  final List<String> _ttsLogs = [];
  bool _ttsRunning = false;
  List<String> _installedEngines = [];
  String _defaultEngine = 'Checking...';
  bool _googleTtsFound = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _loadReport();
    _loadEngineInfo(); // Auto-detect engines on screen open
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  Future<void> _loadReport() async {
    try {
      final jsonStr =
          await rootBundle.loadString('app_core/validation_report.json');
      setState(() {
        _report = json.decode(jsonStr);
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
    }
  }

  // ════════════════════════════════════════════════════════
  // ENGINE DETECTION (runs automatically on open)
  // ════════════════════════════════════════════════════════
  Future<void> _loadEngineInfo() async {
    try {
      final engines = await TtsPlatformService.instance.getInstalledEngines();
      final defaultEng = await TtsPlatformService.instance.getDefaultEngine();
      final hasGoogle = engines.any((e) => e.contains('google'));
      if (mounted) {
        setState(() {
          _installedEngines = engines;
          _defaultEngine = defaultEng;
          _googleTtsFound = hasGoogle;
        });
      }
    } catch (e) {
      _addLog('Engine detection error: $e');
    }
  }

  // ════════════════════════════════════════════════════════
  // TTS DIAGNOSTIC LOGIC
  // ════════════════════════════════════════════════════════
  void _addLog(String msg) {
    if (mounted) {
      setState(() {
        _ttsLogs.add('[${DateTime.now().toLocal().toString().substring(11, 19)}] $msg');
      });
    }
  }

  Future<void> _runTtsDiagnostic() async {
    setState(() {
      _ttsRunning = true;
      _ttsLogs.clear();
    });

    _addLog('=== TTS DIAGNOSTIC START ===');
    _addLog('Panel: Android 13 AOSP (Custom firmware)');
    _addLog('Build: 20240824205917');

    // Step 1: Check engines
    _addLog('─── Step 1: Checking installed TTS engines...');
    await _loadEngineInfo();
    if (_installedEngines.isEmpty) {
      _addLog('❌ NO TTS ENGINES FOUND on this panel!');
      _addLog('   Google TTS APK may not be registering correctly.');
      _addLog('   Try: Reboot the panel, then run this test again.');
    } else {
      _addLog('✅ Found ${_installedEngines.length} engine(s):');
      for (final eng in _installedEngines) {
        final isGoogle = eng.contains('google');
        _addLog('   ${isGoogle ? "⭐" : "•"} $eng');
      }
    }

    // Step 2: Check default engine
    _addLog('─── Step 2: Current default engine...');
    _addLog('   Default = "$_defaultEngine"');
    if (_defaultEngine.contains('google')) {
      _addLog('✅ Google TTS is already the default engine!');
    } else {
      _addLog('⚠️  Google TTS is NOT the default engine.');
      _addLog('   Attempting to set it programmatically...');
      final success = await TtsPlatformService.instance.trySetGoogleTtsEngine();
      if (success) {
        _addLog('✅ Successfully set Google TTS as default!');
        await _loadEngineInfo();
        _addLog('   New default: "$_defaultEngine"');
      } else {
        _addLog('⚠️  Could not auto-set (needs ADB or manual setup).');
        _addLog('   See ADB command section below.');
      }
    }

    // Step 3: Test speak
    _addLog('─── Step 3: Testing TTSService.speak()...');
    try {
      await TTSService.instance.speak('Testing. TTS is working. Shine Academy.');
      _addLog('speak() call sent (no exception)');
    } catch (e) {
      _addLog('❌ speak() THREW: $e');
    }
    await Future.delayed(const Duration(seconds: 3));

    // Step 4: Test SpeechService
    _addLog('─── Step 4: Testing SpeechService.speak()...');
    try {
      await SpeechService.instance.speak('Speech service. Naroda is great!');
      _addLog('SpeechService.speak() call sent (no exception)');
    } catch (e) {
      _addLog('❌ SpeechService.speak() THREW: $e');
    }
    await Future.delayed(const Duration(seconds: 3));

    _addLog('─── COMPLETE ───');
    _addLog('If you heard audio → ✅ TTS is working!');
    _addLog('If silent → press "Open TTS Settings" button above');
    _addLog('Or run ADB commands from the ADB section below.');

    setState(() => _ttsRunning = false);
  }

  Future<void> _testSingleWord() async {
    _addLog('Quick test: "Hello Shine Academy"...');
    try {
      await SpeechService.instance.speak('Hello Shine Academy Naroda!');
      _addLog('Sent. Did you hear it?');
    } catch (e) {
      _addLog('FAILED: $e');
    }
  }

  Future<void> _testDictionary() async {
    _addLog('Dictionary TTS test...');
    try {
      await TTSService.instance
          .speak('Democracy. A system of government by the whole population.');
      _addLog('Done.');
    } catch (e) {
      _addLog('Dictionary TTS FAILED: $e');
    }
  }

  // ════════════════════════════════════════════════════════
  // BUILD
  // ════════════════════════════════════════════════════════
  Widget _buildStatusChip(String status) {
    Color color;
    IconData icon;
    if (status == 'PASS') {
      color = Colors.green;
      icon = Icons.check_circle;
    } else if (status == 'WARNING') {
      color = Colors.orange;
      icon = Icons.warning;
    } else {
      color = Colors.red;
      icon = Icons.error;
    }
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: BoxDecoration(
          color: color.withValues(alpha: 0.1),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: color)),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, color: color, size: 20),
          const SizedBox(width: 8),
          Text(status,
              style: TextStyle(color: color, fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[50],
      appBar: const BrandAppBar(title: 'EduOS Doctor'),
      body: Column(
        children: [
          Container(
            color: Colors.white,
            child: TabBar(
              controller: _tabController,
              labelColor: Colors.indigo,
              unselectedLabelColor: Colors.grey,
              indicatorColor: Colors.indigo,
              tabs: const [
                Tab(icon: Icon(Icons.fact_check), text: 'Content Report'),
                Tab(icon: Icon(Icons.record_voice_over), text: 'TTS Fix'),
              ],
            ),
          ),
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: [
                _buildContentReportTab(),
                _buildTtsDiagnosticTab(),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // ── Tab 1: Content Report ─────────────────────────────
  Widget _buildContentReportTab() {
    if (_isLoading) return const Center(child: CircularProgressIndicator());
    if (_report == null) {
      return Center(
          child: Text(TrilingualService.instance.getUIText('Validation Report not found.\nRun: python3 scripts/eduos_validator.py')));
    }
    final summary = _report!['summary'];
    final errors = _report!['errors'] as List;
    final warnings = _report!['warnings'] as List;

    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                    color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 10)
              ]),
          child: Column(children: [
            _buildStatusChip(_report!['status']),
            const SizedBox(height: 24),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _StatCol(
                    label: 'Scanned',
                    value: summary['total_files_scanned'].toString(),
                    color: Colors.blue),
                _StatCol(
                    label: 'Errors',
                    value: summary['error_count'].toString(),
                    color: Colors.red),
                _StatCol(
                    label: 'Warnings',
                    value: summary['warning_count'].toString(),
                    color: Colors.orange),
              ],
            ),
          ]),
        ),
        if (errors.isNotEmpty) ...[
          const SizedBox(height: 32),
          Text('🚨 Critical Errors (${errors.length})',
              style: GoogleFonts.poppins(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.red[900])),
          const SizedBox(height: 12),
          ...errors.map((e) => _buildIssueCard(e, isError: true)),
        ],
        if (warnings.isNotEmpty) ...[
          const SizedBox(height: 32),
          Text('⚠️ Warnings (${warnings.length})',
              style: GoogleFonts.poppins(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.orange[900])),
          const SizedBox(height: 12),
          ...warnings.map((e) => _buildIssueCard(e, isError: false)),
        ],
      ],
    );
  }

  Widget _buildIssueCard(dynamic issue, {required bool isError}) {
    Color themeColor = isError ? Colors.red : Colors.orange;
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: themeColor.withValues(alpha: 0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Icon(
                isError ? Icons.error_outline : Icons.warning_amber,
                color: themeColor,
                size: 20),
            const SizedBox(width: 8),
            Text(issue['type'],
                style: TextStyle(
                    fontWeight: FontWeight.bold, color: themeColor)),
          ]),
          const SizedBox(height: 8),
          Text(issue['message'], style: TextStyle(fontSize: 14)),
          const SizedBox(height: 8),
          Text('File: ${issue['file']}',
              style: TextStyle(
                  fontSize: 12,
                  color: Colors.grey[600],
                  fontFamily: 'monospace')),
        ],
      ),
    );
  }

  // ── Tab 2: TTS Diagnostic ────────────────────────────
  Widget _buildTtsDiagnosticTab() {
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        // ── Engine Status Card ─────────────────────────
        _buildEngineStatusCard(),
        const SizedBox(height: 16),

        // ── ONE-TAP BUTTONS to open settings directly ──
        _buildOpenSettingsCard(),
        const SizedBox(height: 16),

        // ── Test Buttons ───────────────────────────────
        _buildTestButtonsCard(),
        const SizedBox(height: 16),

        // ── Live Log ───────────────────────────────────
        _buildLogCard(),
        const SizedBox(height: 16),

        // ── ADB Commands for PC-connected setup ────────
        _buildAdbCard(),
        const SizedBox(height: 16),

        // ── Manual path guide specific to this panel ───
        _buildPanelGuideCard(),
      ],
    );
  }

  // Engine status at a glance
  Widget _buildEngineStatusCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: _googleTtsFound ? Colors.green.shade50 : Colors.orange.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
            color: _googleTtsFound
                ? Colors.green.shade300
                : Colors.orange.shade300),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Icon(
              _googleTtsFound ? Icons.check_circle : Icons.warning_amber,
              color: _googleTtsFound ? Colors.green.shade700 : Colors.orange.shade700,
              size: 22,
            ),
            const SizedBox(width: 8),
            Text(
              _googleTtsFound
                  ? 'Google TTS detected ✅'
                  : 'Google TTS not detected ⚠️',
              style: GoogleFonts.poppins(
                fontWeight: FontWeight.bold,
                color: _googleTtsFound
                    ? Colors.green.shade900
                    : Colors.orange.shade900,
              ),
            ),
            const Spacer(),
            TextButton(
              onPressed: _loadEngineInfo,
              child: Text(TrilingualService.instance.getUIText('Refresh')),
            ),
          ]),
          const SizedBox(height: 8),
          Text(
            'Default engine: $_defaultEngine',
            style: TextStyle(
                fontSize: 12,
                color: Colors.grey[700],
                fontFamily: 'monospace'),
          ),
          if (_installedEngines.isNotEmpty) ...[
            const SizedBox(height: 4),
            Text(
              'All engines: ${_installedEngines.join(", ")}',
              style: TextStyle(
                  fontSize: 11,
                  color: Colors.grey[600],
                  fontFamily: 'monospace'),
            ),
          ],
        ],
      ),
    );
  }

  // Open Settings buttons — the KEY feature for AOSP panels
  Widget _buildOpenSettingsCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.indigo.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.indigo.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Icon(Icons.settings, color: Colors.indigo.shade700),
            const SizedBox(width: 8),
            Text(TrilingualService.instance.getUIText('Open Settings — One Tap Fix'),
              style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold,
                  color: Colors.indigo.shade900,
                  fontSize: 15),
            ),
          ]),
          const SizedBox(height: 6),
          Text(TrilingualService.instance.getUIText('Since your panel (AOSP Android 13) hides TTS in Settings,\n''use these buttons to jump directly there:'),
            style: TextStyle(
                fontSize: 12, color: Colors.indigo.shade700, height: 1.4),
          ),
          const SizedBox(height: 12),

          // Button 1: Open Accessibility Settings
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () async {
                _addLog('Opening Accessibility Settings...');
                final result =
                    await TtsPlatformService.instance.openTtsSettings();
                _addLog('Result: $result');
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                    content: Text(TrilingualService.instance.getUIText('Settings opened. Look for "Text-to-Speech" or "TTS"')),
                    backgroundColor: Colors.indigo,
                  ));
                }
              },
              icon: Icon(Icons.accessibility_new),
              label: Text(TrilingualService.instance.getUIText('Open Accessibility Settings')),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.indigo,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 14),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10)),
              ),
            ),
          ),
          const SizedBox(height: 8),

          // Button 2: Open Language & Input (common AOSP path)
          SizedBox(
            width: double.infinity,
            child: OutlinedButton.icon(
              onPressed: () async {
                _addLog('Opening Language & Input Settings...');
                final result =
                    await TtsPlatformService.instance.openLanguageSettings();
                _addLog('Result: $result');
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                    content: Text(TrilingualService.instance.getUIText('Settings opened. Look for "Text-to-Speech Output"')),
                    backgroundColor: Colors.teal,
                  ));
                }
              },
              icon: Icon(Icons.language),
              label: Text(TrilingualService.instance.getUIText('Open Language & Input Settings')),
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 14),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10)),
              ),
            ),
          ),
          const SizedBox(height: 8),

          // Button 3: Try auto-set Google TTS
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () async {
                _addLog('Trying to auto-set Google TTS engine...');
                final success =
                    await TtsPlatformService.instance.trySetGoogleTtsEngine();
                if (success) {
                  _addLog('✅ Google TTS set as default automatically!');
                  await _loadEngineInfo();
                } else {
                  _addLog('⚠️  Could not auto-set. Use ADB command below.');
                }
                if (mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                    content: Text(success
                        ? '✅ Google TTS set as default! Try speaking now.'
                        : '⚠️ Auto-set failed. Connect PC and use ADB command below.'),
                    backgroundColor: success ? Colors.green : Colors.orange,
                  ));
                }
              },
              icon: Icon(Icons.auto_fix_high),
              label: Text(TrilingualService.instance.getUIText('Try Auto-Set Google TTS')),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green.shade600,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 14),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10)),
              ),
            ),
          ),
        ],
      ),
    );
  }

  // Test buttons
  Widget _buildTestButtonsCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText('🎤 Test TTS'),
              style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 12),
          Row(children: [
            Expanded(
              flex: 2,
              child: ElevatedButton.icon(
                onPressed: _ttsRunning ? null : _runTtsDiagnostic,
                icon: _ttsRunning
                    ? const SizedBox(
                        width: 16,
                        height: 16,
                        child: CircularProgressIndicator(
                            strokeWidth: 2, color: Colors.white))
                    : Icon(Icons.play_circle_fill),
                label: Text(_ttsRunning ? 'Running...' : 'Full Diagnostic'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.indigo,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10)),
                ),
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              child: OutlinedButton.icon(
                onPressed: _ttsRunning ? null : _testSingleWord,
                icon: Icon(Icons.volume_up, size: 16),
                label: Text(TrilingualService.instance.getUIText('Quick')),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10)),
                ),
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              child: OutlinedButton.icon(
                onPressed: _ttsRunning ? null : _testDictionary,
                icon: Icon(Icons.menu_book, size: 16),
                label: Text(TrilingualService.instance.getUIText('Dict')),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10)),
                ),
              ),
            ),
          ]),
        ],
      ),
    );
  }

  // Live log
  Widget _buildLogCard() {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFF1E1E2E),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(TrilingualService.instance.getUIText('📋 Live Log'),
                  style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 14)),
              TextButton(
                onPressed: () => setState(() => _ttsLogs.clear()),
                child: Text(TrilingualService.instance.getUIText('Clear'),
                    style: TextStyle(color: Colors.grey, fontSize: 11)),
              ),
            ],
          ),
          const SizedBox(height: 6),
          if (_ttsLogs.isEmpty)
            Text(TrilingualService.instance.getUIText('Press "Full Diagnostic" to see logs here.'),
                style: TextStyle(color: Colors.grey, fontSize: 12))
          else
            ..._ttsLogs.map((log) => Padding(
                  padding: const EdgeInsets.only(bottom: 3),
                  child: Text(
                    log,
                    style: TextStyle(
                      color: log.contains('❌') ||
                              log.contains('FAIL') ||
                              log.contains('THREW')
                          ? Colors.red.shade300
                          : log.contains('✅') ||
                                  log.contains('SUCCESS') ||
                                  log.contains('successfully')
                              ? Colors.green.shade300
                              : log.contains('⚠️') || log.contains('WARNING')
                                  ? Colors.orange.shade300
                                  : Colors.grey.shade300,
                      fontSize: 11,
                      fontFamily: 'monospace',
                    ),
                  ),
                )),
        ],
      ),
    );
  }

  // ADB commands — for PC-connected debug
  Widget _buildAdbCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF0D1117),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
           Row(children: [
            Icon(Icons.terminal, color: Colors.green, size: 18),
            SizedBox(width: 8),
            Text(TrilingualService.instance.getUIText('ADB Commands (connect panel to PC via USB)'),
              style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 13),
            ),
          ]),
          const SizedBox(height: 12),
          _buildAdbCommand(
            title: '1. Force Google TTS as default engine:',
            command:
                'adb shell settings put secure tts_default_synth com.google.android.tts',
          ),
          const SizedBox(height: 8),
          _buildAdbCommand(
            title: '2. Restart TTS service:',
            command:
                'adb shell am force-stop com.google.android.tts && adb shell am startservice -n com.google.android.tts/.GoogleTTSService',
          ),
          const SizedBox(height: 8),
          _buildAdbCommand(
            title: '3. Check if Google TTS is installed:',
            command: 'adb shell pm list packages | grep google.android.tts',
          ),
          const SizedBox(height: 8),
          _buildAdbCommand(
            title: '4. Check current default TTS engine:',
            command:
                'adb shell settings get secure tts_default_synth',
          ),
          const SizedBox(height: 8),
          _buildAdbCommand(
            title: '5. Enable ADB on panel first (if needed):',
            command:
                'Settings → About → Build Number (tap 7 times)\nthen Settings → Developer Options → USB Debugging → ON',
          ),
        ],
      ),
    );
  }

  Widget _buildAdbCommand({required String title, required String command}) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title,
            style: TextStyle(color: Colors.grey, fontSize: 11)),
        const SizedBox(height: 4),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: const Color(0xFF161B22),
            borderRadius: BorderRadius.circular(8),
            border: Border.all(color: Colors.green.shade900),
          ),
          child: Text(
            command,
            style: TextStyle(
                color: Colors.greenAccent,
                fontFamily: 'monospace',
                fontSize: 11),
          ),
        ),
      ],
    );
  }

  // Panel-specific guide for the AOSP Android 13 panel in the photo
  Widget _buildPanelGuideCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.blue.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.blue.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Icon(Icons.tv, color: Colors.blue.shade700, size: 20),
            const SizedBox(width: 8),
            Text(TrilingualService.instance.getUIText('Your Panel (AOSP Android 13) — TTS Path'),
              style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold,
                  color: Colors.blue.shade900,
                  fontSize: 14),
            ),
          ]),
          const SizedBox(height: 10),
          Text(TrilingualService.instance.getUIText('Your panel has a custom AOSP firmware (Build: 20240824205917).\n''The standard "Accessibility → TTS" path may not exist.\n' 
            'Try these paths instead — one of them will work:'),
            style: TextStyle(
                fontSize: 12, color: Colors.blue.shade800, height: 1.5),
          ),
          const SizedBox(height: 12),
          _buildPath('Path A',
              'Settings → System → Language & Input → Text-to-Speech Output',
              Colors.green),
          _buildPath('Path B',
              'Settings → Additional Settings → Language & Input → TTS',
              Colors.teal),
          _buildPath('Path C',
              'Settings → General Management → Language → Text-to-Speech',
              Colors.indigo),
          _buildPath('Path D',
              'Settings → Accessibility → (scroll down) Text-to-Speech',
              Colors.purple),
          _buildPath('Path E (Last resort)',
              'Press "Open Accessibility Settings" button above → it opens Settings automatically',
              Colors.orange),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: Colors.amber.shade50,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: Colors.amber.shade300),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(TrilingualService.instance.getUIText('📌 Once you find TTS Settings:'),
                    style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: Colors.amber.shade900,
                        fontSize: 12)),
                const SizedBox(height: 6),
                _buildStep('1', 'Tap "Preferred Engine" or "Default Engine"'),
                _buildStep('2', 'Select "Google Text-to-speech Engine"'),
                _buildStep(
                    '3',
                    'Tap the ⚙️ gear icon next to Google TTS'),
                _buildStep(
                    '4', 'Tap "Install voice data" → English (India) → Download'),
                _buildStep(
                    '5', 'Come back to app and press "Quick Test" button'),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildPath(String label, String path, Color color) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
            decoration: BoxDecoration(
                color: color.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(4)),
            child: Text(label,
                style: TextStyle(
                    fontSize: 10,
                    fontWeight: FontWeight.bold,
                    color: color)),
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(path,
                style: TextStyle(fontSize: 12, height: 1.4)),
          ),
        ],
      ),
    );
  }

  Widget _buildStep(String num, String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 18,
            height: 18,
            decoration: BoxDecoration(
                color: Colors.amber.shade700,
                shape: BoxShape.circle),
            child: Center(
                child: Text(num,
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 10,
                        fontWeight: FontWeight.bold))),
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(text,
                style: TextStyle(
                    fontSize: 12,
                    color: Colors.amber.shade900,
                    height: 1.4)),
          ),
        ],
      ),
    );
  }
}

class _StatCol extends StatelessWidget {
  final String label;
  final String value;
  final Color color;

  const _StatCol(
      {required this.label, required this.value, required this.color});

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Text(value,
          style: GoogleFonts.poppins(
              fontSize: 32, fontWeight: FontWeight.bold, color: color)),
      Text(label, style: TextStyle(fontSize: 12, color: Colors.grey)),
    ]);
  }
}
