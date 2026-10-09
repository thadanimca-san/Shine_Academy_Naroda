import 'dart:io';
import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'package:path_provider/path_provider.dart';
import 'package:flutter/foundation.dart';
import '../services/app_version_service.dart';

/// Reads and writes educational JSON content.
///
/// Bundled assets are the source of truth. A local file only exists when
/// content was edited on the device (Content Editor / admin edit button); such
/// a file overrides the bundled asset.
///
/// - Desktop (development): reads and writes the project files directly, so
///   editor changes land in the source tree and can be committed.
/// - Mobile: edits are stored under `<documents>/content_overrides/<assetPath>`.
///   All overrides are discarded when the app is updated, so students always
///   get the content shipped with the version they installed.
class LocalContentManager {
  static final LocalContentManager _instance = LocalContentManager._internal();
  static LocalContentManager get instance => _instance;

  LocalContentManager._internal();

  static const String _overridesFolderName = 'content_overrides';

  late Directory _rootDir;
  Future<void>? _initFuture;
  bool _isDesktopSourceMode = false;

  /// True when running on desktop, where edits go straight into the project files.
  bool get isDesktopSourceMode => _isDesktopSourceMode;

  Future<void> init({bool force = false}) {
    if (force) _initFuture = null;
    return _initFuture ??= _initialize();
  }

  Future<void> _initialize() async {
    if (!kIsWeb && (Platform.isLinux || Platform.isMacOS || Platform.isWindows)) {
      _isDesktopSourceMode = true;
      // On desktop the current directory is the project root.
      _rootDir = Directory.current;
      debugPrint("LocalContentManager: Desktop Source Mode at ${_rootDir.path}");
      return;
    }

    _isDesktopSourceMode = false;
    final documentsDir = await getApplicationDocumentsDirectory();
    _rootDir = Directory('${documentsDir.path}/$_overridesFolderName');
    debugPrint("LocalContentManager: Mobile Mode, overrides at ${_rootDir.path}");

    await AppVersionService.init();
    if (AppVersionService.isNewVersion) {
      await _discardOverrides(documentsDir);
    }
  }

  File _localFileFor(String assetPath) => File('${_rootDir.path}/$assetPath');

  /// Returns the content for [assetPath]: the local override if one exists,
  /// otherwise the bundled asset. Returns null if neither can be read.
  Future<dynamic> readLocalJson(String assetPath) async {
    await init();
    try {
      final localFile = _localFileFor(assetPath);
      if (await localFile.exists()) {
        return json.decode(await localFile.readAsString());
      }
    } catch (e) {
      debugPrint("LocalContentManager: error reading local copy of $assetPath: $e");
    }

    try {
      return json.decode(await rootBundle.loadString(assetPath));
    } catch (e) {
      debugPrint("LocalContentManager: error reading bundled asset $assetPath: $e");
      return null;
    }
  }

  /// Saves [data] as the local version of [assetPath].
  Future<bool> writeLocalJson(String assetPath, Map<String, dynamic> data) async {
    await init();
    try {
      final localFile = _localFileFor(assetPath);
      await localFile.parent.create(recursive: true);

      // Indented so desktop edits produce readable diffs in the source tree.
      const encoder = JsonEncoder.withIndent('  ');
      await localFile.writeAsString(encoder.convert(data));
      debugPrint("LocalContentManager: wrote ${localFile.path}");
      return true;
    } catch (e) {
      debugPrint("LocalContentManager: error writing $assetPath: $e");
      return false;
    }
  }

  /// Removes the local version of [assetPath] so the bundled asset is used again.
  /// In Desktop Source Mode this would delete the source file itself, so it is refused.
  Future<bool> deleteLocalJson(String assetPath) async {
    await init();
    if (_isDesktopSourceMode) {
      debugPrint("LocalContentManager: refusing to delete source file $assetPath in Desktop Source Mode.");
      return false;
    }
    try {
      final localFile = _localFileFor(assetPath);
      if (await localFile.exists()) {
        await localFile.delete();
        debugPrint("LocalContentManager: deleted ${localFile.path}");
        return true;
      }
      return false;
    } catch (e) {
      debugPrint("LocalContentManager: error deleting $assetPath: $e");
      return false;
    }
  }

  /// Discards every on-device edit so all content comes from the bundled assets.
  Future<void> wipeAllCache() async {
    await init();
    if (_isDesktopSourceMode) {
      debugPrint("LocalContentManager: nothing to wipe in Desktop Source Mode.");
      return;
    }
    await _discardOverrides(_rootDir.parent);
  }

  Future<void> _discardOverrides(Directory documentsDir) async {
    try {
      if (await _rootDir.exists()) {
        await _rootDir.delete(recursive: true);
      }
      // Older versions copied every JSON file flat into the documents folder.
      await for (final entity in documentsDir.list()) {
        if (entity is File && entity.path.endsWith('.json')) {
          await entity.delete();
        }
      }
      debugPrint("LocalContentManager: discarded local content copies.");
    } catch (e) {
      debugPrint("LocalContentManager: error discarding local content copies: $e");
    }
  }
}
