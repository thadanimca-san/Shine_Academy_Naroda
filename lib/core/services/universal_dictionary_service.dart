import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

class UniversalDictionaryService {
  static final UniversalDictionaryService instance = UniversalDictionaryService._internal();
  UniversalDictionaryService._internal();

  bool _isInitialized = false;
  Database? _db;

  bool get isInitialized => _isInitialized;

  /// Initializes the SQLite database.
  Future<void> init({bool forceReload = false}) async {
    if (_isInitialized && !forceReload) return;
    try {
      if (Platform.isWindows || Platform.isLinux) {
        sqfliteFfiInit();
        databaseFactory = databaseFactoryFfi;
      }

      final appDocDir = await getApplicationDocumentsDirectory();
      final dbPath = p.join(appDocDir.path, 'universal_dictionary.db');

      // Always copy from assets on init for this phase to ensure latest terms.
      // In production Phase 3, we would check versions.
      try {
        final byteData = await rootBundle.load('assets/dictionary/universal_dictionary.db');
        final file = File(dbPath);
        await file.writeAsBytes(byteData.buffer.asUint8List(byteData.offsetInBytes, byteData.lengthInBytes));
      } catch (e) {
        debugPrint('Error copying dictionary DB from assets: $e');
        // If it fails to copy, we try to open it anyway (might have been copied previously)
      }

      _db = await openDatabase(dbPath, version: 1);
      _isInitialized = true;
      debugPrint("UniversalDictionaryService SQLite initialized at $dbPath");
    } catch (e) {
      debugPrint('Error loading universal dictionary SQLite: $e');
    }
  }

  /// Get a single term by its ID. Returns null if not found.
  Future<Map<String, dynamic>?> getTermById(String id) async {
    if (_db == null) return null;
    try {
      final List<Map<String, dynamic>> maps = await _db!.query(
        'terms',
        where: 'id = ?',
        whereArgs: [id],
        limit: 1,
      );
      if (maps.isNotEmpty) {
        return json.decode(maps.first['data'] as String);
      }
    } catch (e) {
      debugPrint('Error querying term by id $id: $e');
    }
    return null;
  }

  /// Get all terms in the dictionary (useful for building full knowledge graphs).
  Future<List<Map<String, dynamic>>> getAllTerms() async {
    if (_db == null) return [];
    try {
      final List<Map<String, dynamic>> maps = await _db!.query('terms');
      return maps.map((row) => json.decode(row['data'] as String) as Map<String, dynamic>).toList();
    } catch (e) {
      debugPrint('Error getting all terms: $e');
      return [];
    }
  }

  /// Get the JSON file path where a specific term is stored.
  Future<String?> getSourceFileForTerm(String id) async {
    if (_db == null) return null;
    try {
      final List<Map<String, dynamic>> maps = await _db!.query(
        'terms',
        columns: ['source_file'],
        where: 'id = ?',
        whereArgs: [id],
        limit: 1,
      );
      if (maps.isNotEmpty) {
        return maps.first['source_file'] as String;
      }
    } catch (e) {
      debugPrint('Error querying source file for id $id: $e');
    }
    return null;
  }

  /// Search terms by query (English, Hindi, Gujarati)
  Future<List<Map<String, dynamic>>> searchTerms(String query) async {
    if (_db == null || query.isEmpty) return [];
    
    try {
      final String likeQuery = '$query%'; // Starts with
      final String containsQuery = '%$query%'; // Contains

      // Priority 1: Starts with (English, Hindi, or Gujarati)
      final List<Map<String, dynamic>> startsWithResults = await _db!.query(
        'terms',
        where: 'word_en LIKE ? OR word_hi LIKE ? OR word_gu LIKE ?',
        whereArgs: [likeQuery, likeQuery, likeQuery],
        limit: 50,
      );

      // Priority 2: Contains (English, Hindi, or Gujarati)
      final List<Map<String, dynamic>> containsResults = await _db!.query(
        'terms',
        where: 'word_en LIKE ? OR word_hi LIKE ? OR word_gu LIKE ?',
        whereArgs: [containsQuery, containsQuery, containsQuery],
        limit: 50,
      );

      // Deduplicate and combine
      final Set<String> seenIds = {};
      final List<Map<String, dynamic>> combined = [];

      for (var row in startsWithResults) {
        final id = row['id'] as String;
        if (!seenIds.contains(id)) {
          seenIds.add(id);
          combined.add(json.decode(row['data'] as String));
        }
      }

      for (var row in containsResults) {
        final id = row['id'] as String;
        if (!seenIds.contains(id)) {
          seenIds.add(id);
          combined.add(json.decode(row['data'] as String));
        }
      }

      return combined;
    } catch (e) {
      debugPrint('Error searching terms for "$query": $e');
      return [];
    }
  }
}
