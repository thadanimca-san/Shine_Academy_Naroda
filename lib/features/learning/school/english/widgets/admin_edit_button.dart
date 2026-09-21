import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../../../../core/engine/local_content_manager.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A reusable admin edit button that works EXACTLY like the one in
/// GoldStandardChapterView:
///  1. Shows a PIN dialog (PIN: 9999)
///  2. Serialises the current in-memory [data] to JSON via LocalContentManager
///     (creating the file the first time, so the editor has something to open)
///  3. Opens ContentEditorScreen with that JSON path
///  4. Calls [onEditorClosed] when the editor is popped so the caller can
///     reload content from the now-edited JSON file.
///
/// Usage:
///   AdminEditButton(
///     jsonPath: 'app_core/english/chapters/class3_bookfair.json',
///     data: chapter.toJson(),          // snapshot of current data
///     onEditorClosed: () => _reload(), // rebuild from the saved JSON
///   )
class AdminEditButton extends StatelessWidget {
  /// The asset/local path used as the JSON file key (e.g.
  /// 'app_core/english/chapters/class3_bookfair.json').
  final String jsonPath;

  /// The current in-memory data to seed the editor the first time.
  /// If the JSON file already exists locally this is ignored (the local
  /// edited version is used instead).
  final Map<String, dynamic> data;

  /// Called after ContentEditorScreen pops so the caller can reload.
  final VoidCallback? onEditorClosed;

  const AdminEditButton({
    super.key,
    required this.jsonPath,
    required this.data,
    this.onEditorClosed,
  });

  // ─── PIN dialog ────────────────────────────────────────────────────────────

  Future<void> _showPinDialog(BuildContext context) async {
    final pinController = TextEditingController();
    final state = <String, dynamic>{'error': false};

    await showDialog<void>(
      context: context,
      builder: (ctx) => StatefulBuilder(
        builder: (ctx, setS) => AlertDialog(
          title:  Row(
            children: [
              Icon(Icons.admin_panel_settings, color: Colors.orange),
              SizedBox(width: 8),
              Text(TrilingualService.instance.getUIText('Admin Access')),
            ],
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(TrilingualService.instance.getUIText('Enter Admin PIN to edit content:')),
              const SizedBox(height: 16),
              TextField(
                controller: pinController,
                keyboardType: TextInputType.number,
                obscureText: true,
                autofocus: true,
                decoration: InputDecoration(
                  border: const OutlineInputBorder(),
                  hintText: 'PIN',
                  errorText:
                      state['error'] == true ? 'Incorrect PIN' : null,
                ),
                onSubmitted: (_) =>
                    _verify(ctx, pinController, state, setS, context),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(ctx).pop(),
              child: Text(TrilingualService.instance.getUIText('Cancel')),
            ),
            ElevatedButton(
              onPressed: () =>
                  _verify(ctx, pinController, state, setS, context),
              style:
                  ElevatedButton.styleFrom(backgroundColor: Colors.orange),
              child: Text(TrilingualService.instance.getUIText('Verify'),
                  style: TextStyle(color: Colors.white)),
            ),
          ],
        ),
      ),
    );
  }

  void _verify(
    BuildContext dialogCtx,
    TextEditingController pinController,
    Map<String, dynamic> state,
    StateSetter setS,
    BuildContext screenCtx,
  ) {
    if (pinController.text == '9999') {
      Navigator.of(dialogCtx).pop();
      _openEditor(screenCtx);
    } else {
      setS(() => state['error'] = true);
      pinController.clear();
    }
  }

  // ─── Editor opener ─────────────────────────────────────────────────────────

  Future<void> _openEditor(BuildContext context) async {
    // Show a brief loading indicator
    if (!context.mounted) return;
    showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (_) =>  AlertDialog(
        content: Row(
          children: [
            CircularProgressIndicator(),
            SizedBox(width: 16),
            Text(TrilingualService.instance.getUIText('Preparing editor…')),
          ],
        ),
      ),
    );

    try {
      await LocalContentManager.instance.init();

      // Seed the local file with current Dart data only if no local edit
      // already exists (so we don't overwrite admin edits).
      final existing =
          await LocalContentManager.instance.readLocalJson(jsonPath);
      if (existing == null && data.isNotEmpty) {
        const encoder = JsonEncoder.withIndent('  ');
        final seeded = json.decode(encoder.convert(data))
            as Map<String, dynamic>;
        await LocalContentManager.instance.writeLocalJson(jsonPath, seeded);
      }
    } catch (e) {
      debugPrint('AdminEditButton: error seeding JSON: $e');
    }

    if (!context.mounted) return;
    Navigator.of(context, rootNavigator: true).pop(); // close loading dialog

    // Open the exact same ContentEditorScreen used by GoldStandardChapterView
    context.push('/content_editor?path=$jsonPath').then((_) {
      onEditorClosed?.call();
    });
  }

  // ─── Build ─────────────────────────────────────────────────────────────────

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.edit_document, color: Colors.orangeAccent),
      tooltip: 'Edit Content (Admin)',
      onPressed: () => _showPinDialog(context),
    );
  }
}
