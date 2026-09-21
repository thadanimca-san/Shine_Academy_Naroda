import 'block_registry.dart';

class BlockValidator {
  /// Validates a single JSON block before rendering.
  /// Throws a format exception if the block is malformed.
  static void validateBlock(Map<String, dynamic> block) {
    BlockRegistry.instance.validate(block);
  }
}

class BlockValidationUtils {
  static void requireLegacy(Map<String, dynamic> block, String key, String legacyKey, Type expectedType) {
    final data = block['data'] as Map<String, dynamic>?;
    if (!block.containsKey(key) && !block.containsKey(legacyKey) && (data == null || (!data.containsKey(key) && !data.containsKey(legacyKey)))) {
      throw FormatException("Missing required key: '$key' (or legacy '$legacyKey').");
    }
    
    var val = block.containsKey(key) ? block[key] : block[legacyKey];
    if (val == null && data != null) {
      val = data.containsKey(key) ? data[key] : data[legacyKey];
    }
    typeCheck(key, val, expectedType);
  }

  static void requireLegacyFlexible(Map<String, dynamic> block, String key, String legacyKey) {
    final data = block['data'] as Map<String, dynamic>?;
    if (!block.containsKey(key) && !block.containsKey(legacyKey) && (data == null || (!data.containsKey(key) && !data.containsKey(legacyKey)))) {
      throw FormatException("Missing required key: '$key' (or legacy '$legacyKey').");
    }
    var val = block.containsKey(key) ? block[key] : block[legacyKey];
    if (val == null && data != null) {
      val = data.containsKey(key) ? data[key] : data[legacyKey];
    }
    if (val is! String && val is! Map) {
      throw FormatException("Expected key '$key' to be String or Map, but got ${val.runtimeType}");
    }
  }

  static void require(Map<String, dynamic> block, String key, Type expectedType) {
    final data = block['data'] as Map<String, dynamic>?;
    if (!block.containsKey(key) && (data == null || !data.containsKey(key))) {
      // Legacy fallback
      if (block.containsKey('content') && block['content'] is Map && (block['content'] as Map).containsKey(key)) {
        typeCheck(key, block['content'][key], expectedType);
        return;
      }
      throw FormatException("Missing required key: '$key'.");
    }
    var val = block.containsKey(key) ? block[key] : data?[key];
    typeCheck(key, val, expectedType);
  }

  static void typeCheck(String key, dynamic val, Type expectedType) {
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
}
