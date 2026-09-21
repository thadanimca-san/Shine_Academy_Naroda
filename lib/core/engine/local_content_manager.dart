import 'dart:io';
import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'package:path_provider/path_provider.dart';
import 'package:flutter/foundation.dart';

class LocalContentManager {
  static final LocalContentManager _instance = LocalContentManager._internal();
  static LocalContentManager get instance => _instance;

  LocalContentManager._internal();

  late Directory _documentsDir;
  bool _isInitialized = false;
  bool _isDesktopSourceMode = false;

  Future<void> init({bool force = false}) async {
    if (_isInitialized && !force) return;
    
    // Check if we are running on Desktop (Linux, macOS, Windows) in development mode
    if (!kIsWeb && (Platform.isLinux || Platform.isMacOS || Platform.isWindows)) {
      _isDesktopSourceMode = true;
      // On desktop, the current directory is usually the project root!
      _documentsDir = Directory(Directory.current.path);
      debugPrint("LocalContentManager: Running in Desktop Source Mode at ${_documentsDir.path}");
    } else {
      _isDesktopSourceMode = false;
      _documentsDir = await getApplicationDocumentsDirectory();
      debugPrint("LocalContentManager: Running in Mobile Sandboxed Mode at ${_documentsDir.path}");
    }
    
    _isInitialized = true;
    
    // Check and copy default curriculum database if it doesn't exist locally
    await ensureFileExists('app_core/learning_modules/master_curriculum.json');
  }

  /// Helper to get the correct absolute file path.
  /// In Desktop Source Mode, we preserve the full assetPath (e.g. app_core/chapters/file.json).
  /// In Mobile Sandbox Mode, we historically flattened to just the filename to avoid folder creation complexity,
  /// but going forward we should use full paths if possible. For safety with legacy data, we flatten on mobile.
  File _getFileFor(String assetPath) {
    if (_isDesktopSourceMode) {
      // Direct source code override
      return File('${_documentsDir.path}/$assetPath');
    } else {
      // Mobile sandbox uses just the filename
      final fileName = assetPath.split('/').last;
      return File('${_documentsDir.path}/$fileName');
    }
  }

  Future<void> ensureFileExists(String assetPath) async {
    final localFile = _getFileFor(assetPath);
    
    if (!await localFile.exists()) {
      debugPrint("Copying $assetPath from assets to local storage...");
      try {
        final byteData = await rootBundle.load(assetPath);
        // Ensure parent directory exists in case of Desktop Source Mode
        if (!await localFile.parent.exists()) {
          await localFile.parent.create(recursive: true);
        }
        await localFile.writeAsBytes(byteData.buffer.asUint8List(byteData.offsetInBytes, byteData.lengthInBytes));
        debugPrint("Successfully copied to local storage: ${localFile.path}");
      } catch (e) {
        debugPrint("Error copying $assetPath: $e");
      }
    }
  }

  /// Read JSON from the local directory using the full asset path.
  Future<dynamic> readLocalJson(String assetPath) async {
    try {
      await ensureFileExists(assetPath);
      final localFile = _getFileFor(assetPath);
      
      if (await localFile.exists()) {
        final content = await localFile.readAsString();
        return json.decode(content);
      }
    } catch (e) {
      debugPrint("Error reading local JSON $assetPath: $e");
    }
    return null;
  }

  /// Write JSON to the local directory using the full asset path
  Future<bool> writeLocalJson(String assetPath, Map<String, dynamic> data) async {
    try {
      final localFile = _getFileFor(assetPath);
      
      // Ensure parent folder exists (critical for desktop source mode)
      if (!await localFile.parent.exists()) {
        await localFile.parent.create(recursive: true);
      }
      
      // Format the JSON nicely for source code commits!
      const encoder = JsonEncoder.withIndent('  ');
      final formattedContent = encoder.convert(data);
      
      await localFile.writeAsString(formattedContent);
      debugPrint("Successfully wrote to ${localFile.path}");
      return true;
    } catch (e) {
      debugPrint("Error writing to local JSON $assetPath: $e");
      return false;
    }
  }

  /// Delete JSON from local documents to allow reloading from assets
  Future<bool> deleteLocalJson(String assetPath) async {
    try {
      final localFile = _getFileFor(assetPath);
      if (await localFile.exists()) {
        await localFile.delete();
        debugPrint("Successfully deleted ${localFile.path}");
        return true;
      }
      return false;
    } catch (e) {
      debugPrint("Error deleting local JSON $assetPath: $e");
      return false;
    }
  }

  /// Wipes all cached JSON files from the mobile sandbox.
  /// This forces the app to reload fresh data from the bundled assets on the next read.
  Future<void> wipeAllCache() async {
    try {
      if (await _documentsDir.exists()) {
        final List<FileSystemEntity> entities = await _documentsDir.list().toList();
        for (FileSystemEntity entity in entities) {
          if (entity is File && entity.path.endsWith('.json')) {
            await entity.delete();
            debugPrint("Deleted cached file: ${entity.path}");
          }
        }
        debugPrint("Successfully wiped all JSON cache from sandbox.");
      }
    } catch (e) {
      debugPrint("Error wiping cache: $e");
    }
  }
}
