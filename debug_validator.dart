import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('app_core/chapters/gseb_class12_accounts_ch1.json');
  final jsonStr = file.readAsStringSync();
  final fullJson = json.decode(jsonStr);
  final blocks = fullJson['blocks'];

  for (var block in blocks) {
    try {
      final type = block['type'];
      if (type == null) {
        throw const FormatException("Missing 'type' in block.");
      }

      switch (type) {
        case 'theory':
          _requireLegacy(block, 'text', 'content', String);
          break;
        case 'example':
          _requireLegacy(block, 'text', 'content', String);
          break;
        case 'activity':
          _require(block, 'title', String);
          break;
        case 'quiz':
          _require(block, 'question', String);
          _require(block, 'options', List);
          _require(block, 'correct_index', int);
          break;
        case 'flashcard':
          _require(block, 'front', String);
          _require(block, 'back', String);
          break;
        case 'dictionary_link':
          _require(block, 'term_id', String);
          break;
        case 'nursery_rhyme':
          _require(block, 'title', String);
          break;
        case 'trace_alphabet':
          _requireLegacy(block, 'letter', 'character', String);
          break;
        case 'counting_game':
          _require(block, 'target_number', int);
          break;
        case 'color_canvas':
          _requireLegacy(block, 'svg_path', 'shape', String);
          break;
      }
      print('Block $type is VALID.');
    } catch (e) {
      print('Block ${block['type']} THREW $e');
    }
  }
}

void _requireLegacy(Map<String, dynamic> block, String key, String legacyKey, Type expectedType) {
  if (!block.containsKey(key) && !block.containsKey(legacyKey)) {
    throw FormatException("Missing required key: '$key' (or legacy '$legacyKey').");
  }
  
  final val = block.containsKey(key) ? block[key] : block[legacyKey];
  _typeCheck(key, val, expectedType);
}

void _require(Map<String, dynamic> block, String key, Type expectedType) {
  if (!block.containsKey(key)) {
    throw FormatException("Missing required key: '$key'.");
  }
  _typeCheck(key, block[key], expectedType);
}

void _typeCheck(String key, dynamic val, Type expectedType) {
  if (expectedType == String && val is! String) {
    throw FormatException("Expected key '$key' to be String, but got ${val.runtimeType}");
  }
  if (expectedType == List && val is! List) {
    throw FormatException("Expected key '$key' to be List, but got ${val.runtimeType}");
  }
  if (expectedType == int && val is! int) {
    throw FormatException("Expected key '$key' to be int, but got ${val.runtimeType}");
  }
}
