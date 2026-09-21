import 'dart:convert';
import 'package:flutter/services.dart';
import 'local_content_manager.dart';

class CurriculumDatabase {
  static final CurriculumDatabase _instance = CurriculumDatabase._internal();
  static CurriculumDatabase get instance => _instance;

  CurriculumDatabase._internal();

  Map<String, dynamic> _db = {};
  bool _isLoaded = false;

  /// Loads the entire curriculum database into memory.
  /// This should be called once during app startup (e.g., in SplashScreen).
  Future<void> load({bool forceReload = false}) async {
    if (_isLoaded && !forceReload) return;
    try {
      await LocalContentManager.instance.init();
      final localData = await LocalContentManager.instance.readLocalJson('app_core/learning_modules/master_curriculum.json');
      
      if (localData != null) {
        _db = localData;
      } else {
        // Fallback to assets if local read fails for some reason
        final jsonString = await rootBundle.loadString('app_core/learning_modules/master_curriculum.json');
        _db = jsonDecode(jsonString) as Map<String, dynamic>;
      }
      _isLoaded = true;
    } catch (e) {
      throw Exception('Failed to load Master Curriculum Database: $e');
    }
  }

  /// Checks if a module exists in the database.
  bool hasModule(String moduleId) {
    return _db.containsKey(moduleId);
  }

  /// Retrieves the blocks array for a specific module.
  List<dynamic>? getModuleBlocks(String moduleId) {
    if (!_isLoaded) {
      throw Exception('CurriculumDatabase is not loaded. Call load() first.');
    }
    if (_db.containsKey(moduleId)) {
      final moduleData = _db[moduleId];
      if (moduleData == null) return null;
      
      if (moduleData is List) {
        return moduleData; // Direct array of blocks
      } else if (moduleData is Map) {
        if (moduleData.containsKey('blocks')) {
          final blocks = moduleData['blocks'];
          if (blocks is List) return blocks;
        }
      }
    }
    return null;
  }

  /// Retrieves the metadata for a specific module.
  Map<String, dynamic>? getModuleMetadata(String moduleId) {
    if (!_isLoaded) {
      throw Exception('CurriculumDatabase is not loaded. Call load() first.');
    }
    if (_db.containsKey(moduleId)) {
      final moduleData = _db[moduleId];
      if (moduleData is Map && moduleData.containsKey('metadata')) {
        return moduleData['metadata'] as Map<String, dynamic>?;
      }
    }
    return null;
  }

  /// Returns the total number of modules in the database.
  int get moduleCount => _db.length;

  /// Returns all module IDs
  List<String> get allModuleIds => _db.keys.toList();
}
